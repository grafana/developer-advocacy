import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

import captions_api as api
import get_refresh_token as helper


def track(language, kind="standard", draft=False, track_id=None):
    return {"id": track_id or f"{language}-{kind}",
            "snippet": {"language": language, "trackKind": kind, "isDraft": draft}}


class ChooseTrackTests(unittest.TestCase):
    def test_manual_english_beats_auto_english(self):
        chosen = api.choose_track([track("en", "ASR"), track("en", "standard")])
        self.assertEqual(chosen["id"], "en-standard")

    def test_auto_english_when_no_manual_track(self):
        chosen = api.choose_track([track("es", "ASR"), track("en", "ASR")])
        self.assertEqual(chosen["id"], "en-ASR")

    def test_lowercase_asr_kind_as_returned_by_the_api(self):
        chosen = api.choose_track([track("und", "standard"), track("en", "asr")])
        self.assertEqual(chosen["id"], "en-asr")

    def test_plain_english_beats_regional_english(self):
        chosen = api.choose_track([track("en-GB"), track("en")])
        self.assertEqual(chosen["id"], "en-standard")

    def test_regional_english_is_accepted(self):
        self.assertEqual(api.choose_track([track("en-US", "ASR")])["id"], "en-US-ASR")

    def test_spanish_video_uses_spanish_track(self):
        self.assertEqual(api.choose_track([track("es", "ASR")])["id"], "es-ASR")

    def test_forced_and_draft_tracks_are_ignored(self):
        tracks = [track("en", "forced"), track("en", "standard", draft=True)]
        self.assertIsNone(api.choose_track(tracks))

    def test_unsupported_language_and_empty_list(self):
        self.assertIsNone(api.choose_track([track("pt", "ASR")]))
        self.assertIsNone(api.choose_track([]))


SRT = """﻿1
00:00:00,000 --> 00:00:02,500
Hello and welcome

2
00:00:02,500 --> 00:00:05,000
to the <i>community</i> call.
It starts now

3
01:02:03,450 --> 01:02:05,000
[Music]
"""


class ParseSrtTests(unittest.TestCase):
    def test_parses_times_text_and_joins_lines(self):
        entries = api.parse_srt(SRT)
        self.assertEqual(entries[0], {"text": "Hello and welcome", "start": 0.0})
        self.assertEqual(entries[1], {"text": "to the community call. It starts now", "start": 2.5})
        self.assertEqual(entries[2]["start"], 3723.45)

    def test_accepts_bytes_and_crlf(self):
        entries = api.parse_srt(SRT.replace("\n", "\r\n").encode("utf-8"))
        self.assertEqual(len(entries), 3)

    def test_garbage_gives_no_entries(self):
        self.assertEqual(api.parse_srt("not a caption file"), [])
        self.assertEqual(api.parse_srt(b""), [])


class QuotaTests(unittest.TestCase):
    def test_spends_until_budget_then_stops(self):
        quota = api.QuotaTracker(budget=500)
        quota.spend(api.COST_CAPTIONS_LIST)
        quota.spend(api.COST_CAPTIONS_DOWNLOAD)
        self.assertEqual(quota.remaining(), 250)
        quota.spend(api.COST_CAPTIONS_LIST)
        quota.spend(api.COST_CAPTIONS_LIST)
        self.assertEqual(quota.used, 350)
        with self.assertRaises(api.QuotaExhausted) as raised:
            quota.spend(api.COST_CAPTIONS_DOWNLOAD)
        self.assertIn("350 of 500", str(raised.exception))
        self.assertEqual(quota.used, 350)  # a refused request is not counted

    def test_budget_from_env(self):
        self.assertEqual(api.budget_from_env({}), api.DEFAULT_QUOTA_BUDGET)
        self.assertEqual(api.budget_from_env({"YOUTUBE_QUOTA_BUDGET": "1200"}), 1200)
        self.assertEqual(api.budget_from_env({"YOUTUBE_QUOTA_BUDGET": "99999"}), api.DAILY_QUOTA)
        with self.assertRaises(ValueError):
            api.budget_from_env({"YOUTUBE_QUOTA_BUDGET": "lots"})

    def test_credentials_from_env_needs_all_three(self):
        full = {"YOUTUBE_OAUTH_CLIENT_ID": "id", "YOUTUBE_OAUTH_CLIENT_SECRET": "secret",
                "YOUTUBE_OAUTH_REFRESH_TOKEN": "token"}
        self.assertEqual(api.credentials_from_env(full), ("id", "secret", "token"))
        partial = dict(full, YOUTUBE_OAUTH_REFRESH_TOKEN=" ")
        self.assertIsNone(api.credentials_from_env(partial))
        self.assertIsNone(api.credentials_from_env({}))


class Request:
    def __init__(self, result, on_execute=None):
        self.result, self.on_execute = result, on_execute

    def execute(self):
        if self.on_execute:
            self.on_execute()
        if isinstance(self.result, Exception):
            raise self.result
        return self.result


class FakeCaptions:
    def __init__(self, tracks, srt):
        self.tracks, self.srt, self.downloads = tracks, srt, []

    def list(self, part, videoId):
        return Request({"items": self.tracks})

    def download(self, id, tfmt):
        # Recorded when the request is executed, i.e. when quota is actually spent.
        return Request(self.srt, lambda: self.downloads.append((id, tfmt)))


class FakeYoutube:
    def __init__(self, captions):
        self._captions = captions

    def captions(self):
        return self._captions


class FetchEntriesTests(unittest.TestCase):
    def client(self, tracks, srt=SRT.encode(), budget=1000):
        captions = FakeCaptions(tracks, srt)
        logs = []
        return api.CaptionsClient(FakeYoutube(captions), api.QuotaTracker(budget), logs.append), captions, logs

    def test_downloads_chosen_track_as_srt_and_counts_quota(self):
        client, captions, _ = self.client([track("en", "ASR", track_id="abc")])
        entries = client.fetch_entries("vid")
        self.assertEqual(captions.downloads, [("abc", "srt")])
        self.assertEqual(len(entries), 3)
        self.assertEqual(client.quota.used, api.COST_CAPTIONS_LIST + api.COST_CAPTIONS_DOWNLOAD)

    def test_no_usable_track_costs_only_the_listing(self):
        client, captions, logs = self.client([track("en", "forced")])
        self.assertIsNone(client.fetch_entries("vid"))
        self.assertEqual(captions.downloads, [])
        self.assertEqual(client.quota.used, api.COST_CAPTIONS_LIST)
        self.assertTrue(any("No usable caption track" in line for line in logs))

    def test_stops_before_a_download_that_would_pass_the_budget(self):
        client, captions, _ = self.client([track("en")], budget=api.COST_CAPTIONS_LIST + 100)
        with self.assertRaises(api.QuotaExhausted):
            client.fetch_entries("vid")
        self.assertEqual(captions.downloads, [])

    def test_quota_exceeded_response_becomes_quota_exhausted(self):
        from googleapiclient.errors import HttpError

        class Resp(dict):
            status = 403
            reason = "Forbidden"

        body = b'{"error": {"errors": [{"reason": "quotaExceeded"}]}}'
        error = HttpError(Resp(), body)
        client, captions, _ = self.client([track("en")], srt=error)
        with self.assertRaises(api.QuotaExhausted):
            client.fetch_entries("vid")

    def test_refresh_error_becomes_auth_error(self):
        class RefreshError(Exception):
            pass

        client, _, _ = self.client([track("en")], srt=RefreshError("invalid_grant"))
        with self.assertRaises(api.CaptionsAuthError):
            client.fetch_entries("vid")


class PipelineTests(unittest.TestCase):
    """The official-API entries go through the same text conversion as the unofficial source."""

    def test_entries_to_transcript_drops_noise_and_adds_markers(self):
        import transcripts
        entries = api.parse_srt(SRT)
        text, timestamped = transcripts.entries_to_transcript(entries, "vid")
        self.assertEqual(text, "Hello and welcome to the community call. It starts now [Music]"
                         .replace(" [Music]", ""))
        self.assertTrue(timestamped.startswith("[00:00:00] Hello and welcome"))

    def test_too_little_text_is_rejected(self):
        import transcripts
        self.assertEqual(transcripts.entries_to_transcript([{"text": "Hi", "start": 0}], "vid"), (None, None))

    def test_get_transcript_uses_official_client_and_passes_quota_stop_up(self):
        import transcripts

        class Stub:
            def __init__(self, result):
                self.result = result

            def fetch_entries(self, video_id):
                if isinstance(self.result, Exception):
                    raise self.result
                return self.result

        original = transcripts.get_captions_client
        try:
            transcripts.get_captions_client = lambda: Stub(api.parse_srt(SRT))
            self.assertIsNotNone(transcripts.get_transcript("vid")[0])
            transcripts.get_captions_client = lambda: Stub(None)
            self.assertEqual(transcripts.get_transcript("vid"), (None, None))
            transcripts.get_captions_client = lambda: Stub(api.QuotaExhausted("budget"))
            with self.assertRaises(api.QuotaExhausted):
                transcripts.get_transcript("vid")
        finally:
            transcripts.get_captions_client = original


class HelperTests(unittest.TestCase):
    def test_pkce_challenge_matches_verifier(self):
        import base64
        import hashlib
        verifier, challenge = helper.pkce_pair()
        expected = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).rstrip(b"=").decode()
        self.assertEqual(challenge, expected)

    def test_auth_url_asks_for_offline_access_and_captions_scope(self):
        url = helper.build_auth_url("cid", "http://127.0.0.1:1234", "st", "ch")
        self.assertIn("access_type=offline", url)
        self.assertIn("prompt=consent", url)
        self.assertIn("youtube.force-ssl", url)
        self.assertIn("code_challenge_method=S256", url)


if __name__ == "__main__":
    unittest.main()
