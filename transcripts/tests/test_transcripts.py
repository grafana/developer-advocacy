import argparse
import contextlib
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
import urllib.error
import urllib.parse
from unittest import mock

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

import audit_public
import check_duplicates
import recurring_shows_index as rsi
import transcripts as t


def video(video_id="abc123DEF_-", title="A title", description="Plain description",
          published="2026-11-03T18:58:57Z", privacy="public"):
    return {"id": video_id, "status": {"privacyStatus": privacy},
            "snippet": {"title": title, "description": description, "publishedAt": published,
                        "liveBroadcastContent": "none"}}


def write_transcript(directory, name, video_id, body="text"):
    with open(os.path.join(directory, name), "w") as f:
        f.write(f"# T\n\nURL: https://www.youtube.com/watch?v={video_id}\n\n{body}\n")


class IndexFirstSentenceTests(unittest.TestCase):
    def test_abbreviation_periods_do_not_end_the_sentence(self):
        for title in (
            "Set up a new Grafana Cloud Account | Grafana for Beginners Ep. 5",
            "The AI Software Engineering Revolution, feat. Anthropic | Big Tent S3E9",
        ):
            summary = f"The show is titled {title} and was held on February 8, 2024. More text follows."
            self.assertEqual(
                rsi.one_line(summary),
                f"The show is titled {title} and was held on February 8, 2024.",
            )


class DirTestCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = self._tmp.name
        self.addCleanup(self._tmp.cleanup)
        self.args = argparse.Namespace(path=self.dir)


class DedupeByVideoIdTests(DirTestCase):
    def test_existing_ids_come_from_url_lines(self):
        write_transcript(self.dir, "2026-11-04T15:46:09Z-logs-overview-grafana-cloud.md", "2EG695XU2nE")
        self.assertEqual(t.existing_video_ids(self.dir), {"2EG695XU2nE"})

    def test_republished_video_with_new_time_and_title_is_skipped(self):
        write_transcript(self.dir, "2026-11-04T15:46:09Z-logs-overview-grafana-cloud.md", "2EG695XU2nE")
        republished = video("2EG695XU2nE", "Logs Overview | Grafana Cloud", published="2026-11-10T16:49:05Z")
        with mock.patch.object(t, "get_transcript") as get_transcript, \
                mock.patch.object(t, "write_markdown") as write:
            processed = t.fetch_transcripts(self.args, [republished])
        self.assertEqual(processed, [])
        get_transcript.assert_not_called()
        write.assert_not_called()

    def test_same_video_twice_in_one_run_is_written_once(self):
        with mock.patch.object(t, "get_transcript", return_value=("x" * 80, "[00:00:00] x")), \
                mock.patch.object(t, "write_markdown") as write, \
                mock.patch.object(t.time, "sleep"):
            t.fetch_transcripts(self.args, [video("one"), video("one", "Renamed")])
        self.assertEqual(write.call_count, 1)

    def test_new_video_is_processed(self):
        write_transcript(self.dir, "a.md", "other")
        with mock.patch.object(t, "get_transcript", return_value=("x" * 80, "[00:00:00] x")), \
                mock.patch.object(t, "write_markdown") as write:
            processed = t.fetch_transcripts(self.args, [video("fresh")])
        self.assertEqual(len(processed), 1)
        write.assert_called_once()


class RegenerateTests(DirTestCase):
    def setUp(self):
        super().setUp()
        write_transcript(self.dir, "2024-02-01T00:00:00Z-b.md", "bbb", "OLD B")
        write_transcript(self.dir, "2023-01-01T00:00:00Z-a.md", "aaa", "OLD A")
        write_transcript(self.dir, "2025-03-01T00:00:00Z-c.md", "ccc", "OLD C")
        self.args = argparse.Namespace(path=self.dir, video_ids=None, limit=None, offset=0)

    def test_limit_takes_the_oldest_by_filename(self):
        self.args.limit = 2
        selected = t.select_regeneration(self.args, t.existing_files_by_id(self.dir))
        self.assertEqual([v for v, _ in selected], ["aaa", "bbb"])

    def test_offset_continues_the_next_batch(self):
        self.args.limit, self.args.offset = 2, 2
        selected = t.select_regeneration(self.args, t.existing_files_by_id(self.dir))
        self.assertEqual([v for v, _ in selected], ["ccc"])

    def test_video_ids_pick_those_videos_without_duplicates(self):
        self.args.video_ids = "ccc, aaa,ccc"
        selected = t.select_regeneration(self.args, t.existing_files_by_id(self.dir))
        self.assertEqual([v for v, _ in selected], ["ccc", "aaa"])

    def test_unknown_id_is_an_error_and_a_selection_is_required(self):
        self.args.video_ids = "zzz"
        with self.assertRaises(SystemExit):
            t.select_regeneration(self.args, t.existing_files_by_id(self.dir))
        self.args.video_ids = None
        with self.assertRaises(SystemExit):
            t.select_regeneration(self.args, t.existing_files_by_id(self.dir))

    def regenerate(self, videos, ids, transcript=("new text " * 20, "[00:00:00] new text")):
        selected = [(i, t.existing_files_by_id(self.dir)[i]) for i in ids]
        with mock.patch.object(t.time, "sleep"), \
                mock.patch.object(t, "get_transcript", return_value=transcript), \
                mock.patch.object(t, "openai_cleanup", return_value=["NEW SUMMARY", None]), \
                mock.patch.object(t, "create_chapters", return_value=None):
            return t.regenerate_transcripts(self.args, selected, videos)

    def read(self, name):
        with open(os.path.join(self.dir, name)) as f:
            return f.read()

    def test_overwrites_the_existing_file_in_place_even_if_the_title_changed(self):
        done = self.regenerate([video("aaa", title="Retitled", published="2023-01-01T00:00:00Z")], ["aaa"])
        self.assertEqual(len(done), 1)
        self.assertIn("NEW SUMMARY", self.read("2023-01-01T00:00:00Z-a.md"))
        self.assertEqual(sorted(os.listdir(self.dir)),
                         ["2023-01-01T00:00:00Z-a.md", "2024-02-01T00:00:00Z-b.md", "2025-03-01T00:00:00Z-c.md"])
        self.assertIn("OLD B", self.read("2024-02-01T00:00:00Z-b.md"))
        self.assertEqual(list(t.existing_video_ids(self.dir)).count("aaa"), 1)

    def test_non_public_or_missing_or_captionless_videos_keep_their_file(self):
        self.assertEqual(self.regenerate([video("aaa", privacy="private")], ["aaa"]), [])
        self.assertEqual(self.regenerate([], ["aaa"]), [])
        self.assertEqual(self.regenerate([video("aaa")], ["aaa"], transcript=(None, None)), [])
        self.assertIn("OLD A", self.read("2023-01-01T00:00:00Z-a.md"))

    def test_stops_when_the_quota_budget_is_spent(self):
        selected = [(i, t.existing_files_by_id(self.dir)[i]) for i in ("aaa", "bbb")]
        with mock.patch.object(t.time, "sleep"), \
                mock.patch.object(t, "get_transcript", side_effect=t.captions_api.QuotaExhausted("budget")):
            done = t.regenerate_transcripts(self.args, selected, [video("aaa"), video("bbb")])
        self.assertEqual(done, [])
        self.assertIn("OLD A", self.read("2023-01-01T00:00:00Z-a.md"))

    def test_one_failing_video_does_not_discard_the_rest_of_the_batch(self):
        selected = [(i, t.existing_files_by_id(self.dir)[i]) for i in ("aaa", "bbb")]
        calls = []

        def cleanup(video, *a, **k):
            calls.append(get_video_id(video))
            if get_video_id(video) == "aaa":
                raise RuntimeError("OpenAI is down")
            return ["NEW SUMMARY", None]

        def get_video_id(v):
            return v["id"]

        with mock.patch.object(t.time, "sleep"), \
                mock.patch.object(t, "get_transcript", return_value=("new text " * 20, "[00:00:00] new text")), \
                mock.patch.object(t, "openai_cleanup", side_effect=cleanup), \
                mock.patch.object(t, "create_chapters", return_value=None):
            done = t.regenerate_transcripts(self.args, selected, [video("aaa"), video("bbb")])
        self.assertEqual(calls, ["aaa", "bbb"])
        self.assertEqual([get_video_id(v) for v in done], ["bbb"])
        self.assertIn("OLD A", self.read("2023-01-01T00:00:00Z-a.md"))
        self.assertIn("NEW SUMMARY", self.read("2024-02-01T00:00:00Z-b.md"))

    def test_a_degraded_result_does_not_replace_a_good_existing_file(self):
        good = ("# T\n\nURL: https://www.youtube.com/watch?v=aaa\n\n## Summary\n\nA real summary.\n\n"
                "## Chapters\n\n00:00:00 Intro\n\n" + "Cleaned text. " * 40 + "\n\n## Raw YouTube Transcript\n\nraw\n")
        path = os.path.join(self.dir, "2023-01-01T00:00:00Z-a.md")
        with open(path, "w") as f:
            f.write(good)
        transcript = ("word " * 120, "[00:00:00] " + "word " * 120)
        selected = [("aaa", path)]
        for summary, cleaned, chapters in (("Summary not available", "cleaned", "00:00:00 Intro"),
                                           ("New summary", "cleaned", "Chapters not available"),
                                           ("New summary", None, "00:00:00 Intro")):
            with mock.patch.object(t.time, "sleep"), \
                    mock.patch.object(t, "is_short_video", return_value=False), \
                    mock.patch.object(t, "get_transcript", return_value=transcript), \
                    mock.patch.object(t, "openai_cleanup", return_value=[summary, cleaned]), \
                    mock.patch.object(t, "create_chapters", return_value=chapters):
                done = t.regenerate_transcripts(self.args, selected, [video("aaa")])
            self.assertEqual(done, [], (summary, cleaned, chapters))
            self.assertEqual(self.read("2023-01-01T00:00:00Z-a.md"), good)

    def test_main_needs_openai_and_never_touches_files_without_it(self):
        self.args.limit = 1
        self.args.regenerate = True
        with mock.patch.object(t.time, "sleep"), mock.patch.object(t, "openai_key", ""):
            with self.assertRaises(SystemExit):
                t.main(self.args)
        self.assertIn("OLD A", self.read("2023-01-01T00:00:00Z-a.md"))

    def test_regenerated_files_pass_the_duplicate_check(self):
        self.regenerate([video("aaa", published="2023-01-01T00:00:00Z")], ["aaa"])
        self.assertEqual(check_duplicates.find_duplicates(self.dir), {})


class CommandLineTests(unittest.TestCase):
    def test_video_ids_accepts_an_id_that_starts_with_a_dash(self):
        # Real IDs can start with "-" (for example -bxMP9lbHG4); the "=" form keeps argparse from
        # reading them as an option, which is how the workflow and the README pass them.
        args = t.build_parser().parse_args(["--regenerate", "--video-ids=-bxMP9lbHG4,abc123DEF_-"])
        self.assertEqual(args.video_ids, "-bxMP9lbHG4,abc123DEF_-")

    def test_video_ids_with_a_space_before_a_leading_dash_is_rejected(self):
        # Documents why the "=" form is required.
        with mock.patch("sys.stderr"), self.assertRaises(SystemExit):
            t.build_parser().parse_args(["--regenerate", "--video-ids", "-bxMP9lbHG4"])


class ValidateArgsTests(unittest.TestCase):
    def check(self, *argv):
        parser = t.build_parser()
        args = parser.parse_args(list(argv))
        with mock.patch("sys.stderr"):
            t.validate_args(parser, args)

    def rejected(self, *argv):
        with self.assertRaises(SystemExit):
            self.check(*argv)

    def test_valid_regeneration_commands_are_accepted(self):
        self.check("--regenerate", "--video-ids=-bxMP9lbHG4")
        self.check("--regenerate", "--limit", "5", "--offset", "5")
        self.check("--days", "14")

    def test_regenerate_rejects_options_it_would_ignore(self):
        for extra in (["--days", "14"], ["--start", "2024-01-01T00:00:00Z"], ["--end", "2024-02-01T00:00:00Z"],
                      ["--channel", "UCother"], ["--playlist", "PLabc"]):
            self.rejected("--regenerate", "--limit", "5", *extra)

    def test_video_ids_cannot_be_combined_with_limit_or_offset(self):
        self.rejected("--regenerate", "--video-ids=abc", "--limit", "5")
        self.rejected("--regenerate", "--video-ids=abc", "--offset", "5")

    def test_negative_or_zero_numbers_are_rejected(self):
        self.rejected("--regenerate", "--limit", "-1")
        self.rejected("--regenerate", "--limit", "0")
        self.rejected("--regenerate", "--limit", "5", "--offset", "-2")

    def test_regenerate_only_options_need_regenerate(self):
        self.rejected("--video-ids=abc")
        self.rejected("--offset", "5")


class PublicOnlyTests(DirTestCase):
    def skipped(self, v):
        with mock.patch.object(t, "get_transcript") as get_transcript, \
                mock.patch("builtins.print") as printed:
            processed = t.fetch_transcripts(self.args, [v])
        get_transcript.assert_not_called()
        self.assertEqual(processed, [])
        return " ".join(str(c) for c in printed.call_args_list)

    def test_private_and_unlisted_videos_are_skipped_without_their_title(self):
        for privacy in ("private", "unlisted", "privacyStatusUnspecified"):
            log = self.skipped(video("secret1", "Secret Roadmap Title", privacy=privacy))
            self.assertIn("secret1", log)
            self.assertIn(privacy, log)
            self.assertNotIn("Secret Roadmap Title", log)

    def test_video_without_status_is_not_published(self):
        v = video("nostatus")
        del v["status"]
        self.assertIn("unknown", self.skipped(v))

    def test_upcoming_and_live_broadcasts_wait_until_they_air(self):
        for state in ("upcoming", "live"):
            v = video("stream1")
            v["snippet"]["liveBroadcastContent"] = state
            self.assertIn(state, self.skipped(v))

    def test_finished_public_video_is_processed(self):
        v = video("ok1")
        v["snippet"]["liveBroadcastContent"] = "none"
        with mock.patch.object(t, "get_transcript", return_value=("x" * 80, "[00:00:00] x")), \
                mock.patch.object(t, "write_markdown"):
            self.assertEqual(len(t.fetch_transcripts(self.args, [v])), 1)

    def test_video_lists_request_the_status_part(self):
        youtube = mock.Mock()
        youtube.playlistItems().list().execute.return_value = {
            "items": [{"contentDetails": {"videoId": "v1", "videoPublishedAt": "2026-11-05T00:00:00Z"},
                       "snippet": {"publishedAt": "2026-11-05T00:00:00Z"}}]}
        youtube.videos().list().execute.return_value = {"items": [video("v1")]}
        youtube.videos().list.reset_mock()
        with mock.patch.object(t, "build_youtube", return_value=youtube):
            t.get_channel_videos("UCabc", "2026-11-01T00:00:00Z", "2026-11-30T00:00:00Z")
        self.assertEqual(youtube.videos().list.call_args.kwargs["part"], "snippet,status")


class PlaylistLoggingTests(unittest.TestCase):
    def test_playlist_path_never_prints_a_title(self):
        youtube = mock.Mock()
        youtube.playlistItems().list().execute.return_value = {
            "items": [{"snippet": {"resourceId": {"videoId": "priv1"}}}]}
        secret = video("priv1", "Secret Roadmap Title", privacy="private")
        youtube.videos().list().execute.return_value = {"items": [secret]}
        with mock.patch.object(t, "build_youtube", return_value=youtube), \
                mock.patch.object(t.time, "sleep"), mock.patch("builtins.print") as printed:
            videos = t.get_playlist_videos("PLx")
        log = " ".join(str(c) for c in printed.call_args_list)
        self.assertEqual([v["id"] for v in videos], ["priv1"])
        self.assertIn("priv1", log)
        self.assertNotIn("Secret Roadmap Title", log)


class LongTitleTests(DirTestCase):
    def long_video(self):
        raw = "x" * 100
        first = raw + " " + " ".join(["wordy"] * 200)
        return video(title=raw, description=first + "\nmore")

    def test_completed_title_is_capped_at_a_word_boundary(self):
        title = t.video_title(self.long_video())
        self.assertLessEqual(len(title), t.MAX_COMPLETED_TITLE_CHARS)
        self.assertTrue(title.endswith("wordy"))
        self.assertTrue(title.startswith("x" * 100))

    def test_filename_stays_well_under_255_bytes(self):
        name = os.path.basename(t.file_for_video(self.args, self.long_video()))
        self.assertLess(len(name.encode()), 200)
        # Any long title, not just completed ones, gets a capped slug.
        huge = video(title="word " * 200)
        self.assertLess(len(os.path.basename(t.file_for_video(self.args, huge)).encode()), 200)

    def test_markdown_for_a_very_long_title_can_be_written(self):
        v = self.long_video()
        v["transcript"], v["timestamped"] = "x " * 100, "[00:00:00] x\n[00:05:00] y"
        with mock.patch.object(t, "openai_key", ""):
            t.write_markdown(self.args, v)
        self.assertTrue(os.path.isfile(t.file_for_video(self.args, v)))


class UrlLineInDescriptionTests(DirTestCase):
    def test_last_url_line_is_the_videos_own(self):
        with open(os.path.join(self.dir, "a.md"), "w") as f:
            f.write("# T\n\n## Description\n\nURL: https://www.youtube.com/watch?v=OTHERvideo1\n\n"
                    "URL: https://www.youtube.com/watch?v=REALvideo_01\n\n## Summary\n")
        self.assertEqual(t.existing_video_ids(self.dir), {"REALvideo_01"})

    def test_duplicate_check_uses_the_last_url_line_too(self):
        with open(os.path.join(self.dir, "new.md"), "w") as f:
            f.write("URL: https://www.youtube.com/watch?v=OTHERvideo1\n\nURL: https://www.youtube.com/watch?v=NEWvideo_001\n")
        write_transcript(self.dir, "old.md", "OTHERvideo1")
        self.assertEqual(check_duplicates.find_duplicates(self.dir, ["new.md"]), {})


class PlaceholderEdgeTests(unittest.TestCase):
    def test_ordinary_bracketed_text_is_not_a_placeholder(self):
        for text in ("[Add-on]", "[Insert coin]", "[Add to calendar]", "[ADD-ON]", "[Instructions]"):
            self.assertIsNone(t.find_placeholder(f"x {text} y"), text)

    def test_template_forms_still_match(self):
        for text in ("[Add Pyroscope/GCX docs and blog links]", "[INSTRUCTIONS: EDIT ANY AREA]",
                     "[INSERT TIMESTAMPS IF VIDEO IS 5 MIN OR MORE]", "[ADD LINKS]", "[add the docs and blog links]"):
            self.assertIsNotNone(t.find_placeholder(f"x {text} y"), text)


class DedupeRulesTests(unittest.TestCase):
    def test_markdown_rules_are_not_collapsed(self):
        desc = "Part one\n----------\nbody text here\n----------\nPart two\n==========\n==========\n"
        self.assertEqual(t.dedupe_description(desc), desc.rstrip("\n"))

    def test_repeated_text_lines_still_collapse(self):
        self.assertEqual(t.dedupe_description("same long line\nsame long line").count("same long line"), 1)


class BatchDuplicateLimitTests(DirTestCase):
    def test_in_batch_duplicates_do_not_count_toward_the_limit(self):
        a, a2, b, c = video("aaa"), video("aaa", "Renamed"), video("bbb"), video("ccc")
        args = argparse.Namespace(path=self.dir, playlist="PLx", channel="UCx", start="s", end="e",
                                  limit=2, days=None)
        with mock.patch.object(t.time, "sleep"), \
                mock.patch.object(t, "get_playlist_videos", return_value=[a, b]), \
                mock.patch.object(t, "get_channel_videos", return_value=[a2, c]), \
                mock.patch.object(t, "fetch_transcripts") as fetch:
            t.main(args)
        self.assertEqual([t.get_id(v) for v in fetch.call_args.args[1]], ["aaa", "bbb"])


class PlaceholderTests(DirTestCase):
    def test_detects_youtube_template_text(self):
        for text in ("[INSTRUCTIONS: EDIT ANY AREA IN BRACKETS]", "[INSERT DESCRIPTION HERE]",
                     "Links: [Add Pyroscope/GCX docs and blog links]"):
            self.assertIsNotNone(t.find_placeholder(f"Intro\n{text}\nThanks"), text)

    def test_ordinary_brackets_are_fine(self):
        self.assertIsNone(t.find_placeholder("See [the docs](https://grafana.com) and [Addendum] [1]"))
        self.assertIsNone(t.find_placeholder("Date: [TBD] and [TODO] later"))
        self.assertIsNone(t.find_placeholder(""))
        self.assertIsNone(t.find_placeholder(None))

    def test_placeholder_video_is_skipped_and_logged_once_by_main(self):
        draft = video("draft1", description="[INSERT DESCRIPTION HERE]")
        args = argparse.Namespace(path=self.dir, playlist=None, channel="chan", start=None,
                                  end=None, limit=None)
        with mock.patch.object(t, "get_channel_videos", return_value=[draft]), \
                mock.patch.object(t, "get_transcript") as get_transcript, \
                mock.patch.object(t.time, "sleep"), mock.patch.object(t.random, "uniform", return_value=0), \
                mock.patch("builtins.print") as printed:
            t.main(args)
        get_transcript.assert_not_called()
        logged = [c for c in printed.call_args_list
                  if "template placeholder" in str(c) and "draft1" in str(c)]
        self.assertEqual(len(logged), 1)


STAMPED = ("[00:00:00] a " + " ".join(f"\n[00:{m:02d}:00] w" for m in range(1, 10)))


class CleanupFallbackTests(unittest.TestCase):
    def run_cleanup(self, replies):
        client = mock.Mock()
        with mock.patch.object(t, "openai_key", "k"), \
                mock.patch.object(t.openai, "OpenAI", return_value=client), \
                mock.patch.object(t, "chat", side_effect=replies) as chat:
            return t.openai_cleanup(video(), "word " * 200, "vid"), chat

    def test_full_length_cleanup_is_kept(self):
        # summary, then one chunk
        (summary, cleaned), _ = self.run_cleanup(["Summary", "word " * 190])
        self.assertEqual(summary, "Summary")
        self.assertTrue(cleaned.startswith("word"))

    def test_truncated_after_retry_falls_back_to_raw(self):
        (summary, cleaned), chat = self.run_cleanup(["Summary", "In conclusion, short.", "Still short."])
        self.assertEqual(summary, "Summary")
        self.assertIsNone(cleaned)
        self.assertEqual(chat.call_count, 3)

    def test_retry_that_recovers_is_used(self):
        (_, cleaned), _ = self.run_cleanup(["Summary", "short", "word " * 190])
        self.assertTrue(cleaned.startswith("word"))


class ChapterTests(unittest.TestCase):
    DESC = "About\n00:00 Intro\n1:30 - Demo of alerts\n[12:05] Q&A with guests\nThanks!"

    def test_description_timestamps_are_reused(self):
        self.assertEqual(t.description_chapters(self.DESC),
                         "00:00:00 Intro\n00:01:30 Demo of alerts\n00:12:05 Q&A with guests")

    def test_hour_long_timestamps(self):
        d = "0:00 Start\n10:00 Middle\n1:02:03 End"
        self.assertEqual(t.description_chapters(d).splitlines()[-1], "01:02:03 End")

    def test_needs_three_chapters_starting_at_zero(self):
        self.assertIsNone(t.description_chapters("00:00 One\n01:00 Two"))
        self.assertIsNone(t.description_chapters("00:10 One\n01:00 Two\n02:00 Three"))
        self.assertIsNone(t.description_chapters("Posted at 12:30 today"))

    def test_create_chapters_prefers_description_and_skips_model(self):
        stamped = "[00:00:00] a\n[00:12:00] b\n[00:13:00] c"
        with mock.patch.object(t, "chat") as chat:
            out = t.create_chapters(video(description=self.DESC), stamped, "vid")
        self.assertIn("Demo of alerts", out)
        chat.assert_not_called()

    def test_short_videos_get_no_chapters(self):
        with mock.patch.object(t, "chat") as chat:
            self.assertIsNone(t.create_chapters(video(description=self.DESC), "[00:00:00] a\n[00:00:45] b", "v"))
        chat.assert_not_called()
        self.assertTrue(t.is_short_video("[00:00:00] a\n[00:00:45] b"))
        self.assertFalse(t.is_short_video("[00:00:00] a\n[00:10:00] b"))
        self.assertFalse(t.is_short_video("no markers"))

    def test_generic_titles_are_never_written(self):
        stamped = "\n".join(f"[00:{m:02d}:00] words" for m in range(0, 30, 3))

        def fake_chat(client, system, text, temperature):
            first = text.strip().split("]")[0].lstrip("[")
            return f"{first} Discussion" if first == "00:00:00" else f"{first} Setting up Alloy"
        with mock.patch.object(t, "openai_key", "k"), mock.patch.object(t.openai, "OpenAI"), \
                mock.patch.object(t, "chat", side_effect=fake_chat):
            out = t.create_chapters(video(), stamped, "vid")
        self.assertNotIn("Discussion", out)
        self.assertNotIn("00:00:00 Setting up Alloy", out)

    def test_generic_title_detection(self):
        self.assertTrue(t.is_generic_title("Discussion"))
        self.assertTrue(t.is_generic_title("Q&A"))
        self.assertFalse(t.is_generic_title("Discussion of Tempo sampling"))


class TitleCleanTests(DirTestCase):
    RAW = "02   Grafana   ObservabilityCON 26   London"

    def test_clean_title_collapses_spaces(self):
        self.assertEqual(t.clean_title(f"  {self.RAW} "), "02 Grafana ObservabilityCON 26 London")

    def test_filename_uses_clean_title(self):
        name = os.path.basename(t.file_for_video(self.args, video(title=self.RAW)))
        self.assertEqual(name, "2026-11-03T18:58:57Z-02-grafana-observabilitycon-26-london.md")

    def test_markdown_heading_uses_clean_title(self):
        v = video(title=self.RAW)
        v["transcript"], v["timestamped"] = "x " * 100, "[00:00:00] " + "x " * 100 + "\n[00:05:00] y"
        with mock.patch.object(t, "openai_key", ""):
            t.write_markdown(self.args, v)
        with open(t.file_for_video(self.args, v)) as f:
            self.assertEqual(f.readline().strip(), "# 02 Grafana ObservabilityCON 26 London")


class DescriptionDedupeTests(DirTestCase):
    DESC = ("Intro text here\n\nThanks for watching!\n\n#Grafana #Pyroscope\n---\nThanks for watching! \n\n"
            "Like and subscribe\n\n#Grafana #Observability")

    def test_repeated_lines_are_dropped_once_seen(self):
        out = t.dedupe_description(self.DESC)
        self.assertEqual(out.count("Thanks for watching!"), 1)
        self.assertIn("#Grafana #Pyroscope", out)
        self.assertIn("#Grafana #Observability", out)
        self.assertNotIn("\n\n\n", out)

    def test_short_and_blank_lines_are_kept(self):
        self.assertEqual(t.dedupe_description("---\na\n---\n\n\nx\n---"), "---\na\n---\n\nx\n---")

    def test_written_description_has_one_footer(self):
        v = video(description=self.DESC)
        v["transcript"], v["timestamped"] = "x " * 100, "[00:00:00] x\n[00:05:00] y"
        with mock.patch.object(t, "openai_key", ""):
            t.write_markdown(self.args, v)
        with open(t.file_for_video(self.args, v)) as f:
            self.assertEqual(f.read().count("Thanks for watching!"), 1)


class TruncatedTitleTests(unittest.TestCase):
    FULL = "Grafana ObservabilityCON 26 London: Building an Observable Enterprise for AI Driven Operations"
    CUT = "01   Grafana ObservabilityCON 26   London   Building an Observable Enterprise for AI Driven Operatio"

    def test_title_at_limit_is_completed_from_the_description_first_line(self):
        raw = (self.FULL + " and more words to fill up")[:100]
        self.assertEqual(len(raw), 100)
        v = video(title=raw, description=f"\n{self.FULL} and more words to fill up and beyond\nMore")
        self.assertEqual(t.video_title(v), f"{self.FULL} and more words to fill up and beyond")

    def test_truncated_title_without_matching_description_warns(self):
        self.assertEqual(len(self.CUT), 100)
        v = video(title=self.CUT, description="[INSERT DESCRIPTION]")
        with mock.patch("builtins.print") as printed:
            self.assertEqual(t.video_title(v), t.clean_title(self.CUT))
        self.assertTrue(any("probably truncated" in str(c) for c in printed.call_args_list))

    def test_short_titles_are_untouched_and_silent(self):
        with mock.patch("builtins.print") as printed:
            self.assertEqual(t.video_title(video(title="Short   title")), "Short title")
        printed.assert_not_called()


class ShortVideoOutputTests(DirTestCase):
    def test_short_video_has_no_chapters_or_cleaned_copy(self):
        v = video(title="eBPF in 1 minute")
        v["transcript"], v["timestamped"] = "so what is ebpf " * 10, "[00:00:00] so what is ebpf"
        with mock.patch.object(t, "openai_cleanup", return_value=["Sum", "cleaned copy"]):
            t.write_markdown(self.args, v)
        with open(t.file_for_video(self.args, v)) as f:
            text = f.read()
        self.assertNotIn("## Chapters", text)
        self.assertNotIn("cleaned copy", text)
        self.assertIn("## Raw YouTube Transcript", text)


class CheckDuplicatesTests(DirTestCase):
    def test_no_duplicates(self):
        write_transcript(self.dir, "a.md", "AAA")
        write_transcript(self.dir, "b.md", "BBB")
        self.assertEqual(check_duplicates.find_duplicates(self.dir), {})

    def test_new_file_duplicating_existing_one_fails(self):
        write_transcript(self.dir, "2026-11-04-logs-overview.md", "2EG695XU2nE")
        write_transcript(self.dir, "2026-11-10-logs-overview.md", "2EG695XU2nE")
        dupes = check_duplicates.find_duplicates(self.dir, ["2026-11-10-logs-overview.md"])
        self.assertEqual(dupes, {"2EG695XU2nE": ["2026-11-04-logs-overview.md", "2026-11-10-logs-overview.md"]})

    def test_old_duplicates_not_involving_new_files_are_ignored(self):
        write_transcript(self.dir, "old1.md", "OLD")
        write_transcript(self.dir, "old2.md", "OLD")
        write_transcript(self.dir, "new.md", "NEW")
        self.assertEqual(check_duplicates.find_duplicates(self.dir, ["new.md"]), {})

    def git(self, *cmd):
        subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@example.com", *cmd],
                       cwd=self.dir, check=True, capture_output=True)

    def test_cli_against_git_base(self):
        self.git("init", "-q", "-b", "main")
        write_transcript(self.dir, "old.md", "VID1")
        self.git("add", "."), self.git("commit", "-qm", "base")
        self.git("checkout", "-qb", "feature")
        write_transcript(self.dir, "new.md", "VID1")
        self.git("add", "."), self.git("commit", "-qm", "dup")
        with mock.patch("builtins.print"):
            self.assertEqual(check_duplicates.main(["--base", "main", "--path", self.dir]), 1)
            os.remove(os.path.join(self.dir, "new.md"))
            write_transcript(self.dir, "fresh.md", "VID2")  # untracked and unique
            self.git("commit", "-qam", "drop dup")
            self.assertEqual(check_duplicates.main(["--base", "main", "--path", self.dir]), 0)


class AnchoredUrlLineTests(DirTestCase):
    def write(self, name, text):
        with open(os.path.join(self.dir, name), "w") as f:
            f.write(text)

    def test_url_line_in_the_summary_or_transcript_is_not_the_videos(self):
        self.write("a.md", "# T\n\n## Description\n\nhi\n\nURL: https://www.youtube.com/watch?v=REALvideo_01\n\n"
                   "## Summary\n\nsum\n\nURL: https://www.youtube.com/watch?v=SPOKENvideo1\n\n"
                   "## Raw YouTube Transcript\n\nURL: https://www.youtube.com/watch?v=LATERvideo_1\n")
        self.assertEqual(t.existing_video_ids(self.dir), {"REALvideo_01"})
        self.assertEqual(check_duplicates.video_ids(os.path.join(self.dir, "a.md")), {"REALvideo_01"})

    def test_generated_file_round_trips(self):
        v = video("ROUNDtrip_01", description="URL: https://www.youtube.com/watch?v=OTHERvideo1")
        v["transcript"], v["timestamped"] = "word " * 80, "[00:30:00] word"
        with mock.patch.object(t, "openai_key", ""):
            t.write_markdown(self.args, v)
        self.assertEqual(t.existing_video_ids(self.dir), {"ROUNDtrip_01"})


class AtomicWriteTests(DirTestCase):
    def test_a_crash_while_writing_leaves_no_transcript_behind(self):
        v = video("CRASHvideo_1")
        v["transcript"], v["timestamped"] = "word " * 80, "[00:30:00] word"
        with mock.patch.object(t, "openai_key", ""), \
                mock.patch.object(t.os, "replace", side_effect=KeyboardInterrupt):
            with self.assertRaises(KeyboardInterrupt):
                t.write_markdown(self.args, v)
        self.assertEqual([n for n in os.listdir(self.dir) if n.endswith(".md")], [])
        self.assertEqual(t.existing_video_ids(self.dir), set())

    def test_a_finished_write_leaves_only_the_transcript(self):
        v = video("DONEvideo_001")
        v["transcript"], v["timestamped"] = "word " * 80, "[00:30:00] word"
        with mock.patch.object(t, "openai_key", ""):
            t.write_markdown(self.args, v)
        self.assertEqual(len(os.listdir(self.dir)), 1)


class RedactedLoggingTests(DirTestCase):
    def test_nothing_with_a_title_or_description_is_printed_for_a_bad_video(self):
        secret = "Secret launch title"
        bad = {"id": "", "snippet": {"title": secret, "description": "Secret description"}}
        with mock.patch("builtins.print") as printed:
            t.fetch_transcripts(self.args, [bad])
            t.write_markdown(self.args, bad)
            no_transcript = video("NOTRANSCRIPT1", title=secret)
            no_transcript["transcript"] = ""
            t.write_markdown(self.args, no_transcript)
        output = " ".join(str(a) for call in printed.call_args_list for a in call.args)
        self.assertNotIn("Secret", output)
        self.assertTrue(printed.called)


class ShortVideoCostTests(DirTestCase):
    def test_short_video_asks_openai_for_a_summary_only(self):
        v = video(title="eBPF in 1 minute")
        v["transcript"], v["timestamped"] = "so what is ebpf " * 10, "[00:00:00] so what is ebpf"
        with mock.patch.object(t, "openai_cleanup", return_value=["Sum", None]) as cleanup:
            t.write_markdown(self.args, v)
        self.assertIs(cleanup.call_args.kwargs["clean"], False)

    def test_long_video_still_gets_the_cleanup(self):
        v = video()
        v["transcript"], v["timestamped"] = "word " * 80, "[00:30:00] word"
        with mock.patch.object(t, "openai_cleanup", return_value=["Sum", "clean"]) as cleanup:
            t.write_markdown(self.args, v)
        self.assertIs(cleanup.call_args.kwargs["clean"], True)

    def test_summary_only_makes_one_model_call(self):
        with mock.patch.object(t, "openai_key", "k"), mock.patch.object(t.openai, "OpenAI"), \
                mock.patch.object(t, "chat", return_value="Summary") as chat:
            self.assertEqual(t.openai_cleanup(video(), "word " * 50, "vid", clean=False), ["Summary", None])
        self.assertEqual(chat.call_count, 1)


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def read(self, *args):
        return json.dumps(self.payload).encode()


class AuditPublicTests(DirTestCase):
    def api(self, statuses):
        def urlopen(request, timeout=None):
            self.requested = request
            ids = urllib.parse.parse_qs(urllib.parse.urlparse(request.full_url).query)["id"][0].split(",")
            return FakeResponse({"items": [{"id": i, "status": {"privacyStatus": statuses[i]}}
                                           for i in ids if i in statuses]})
        return urlopen

    def run_main(self, statuses, *extra):
        out = io.StringIO()
        with mock.patch.dict(os.environ, {"YOUTUBE_API_KEY": "key-123"}), contextlib.redirect_stdout(out):
            code = audit_public.main(["--path", self.dir, *extra], urlopen=self.api(statuses))
        return code, out.getvalue()

    def test_all_public_passes(self):
        write_transcript(self.dir, "a.md", "AAA")
        code, out = self.run_main({"AAA": "public"})
        self.assertEqual(code, 0)
        self.assertIn("all 1", out)

    def test_unrecognized_source_files_fail_with_counts_only(self):
        write_transcript(self.dir, "public.md", "PUB")
        for name, content in (
                ("short-secret-title.md", "URL: https://youtu.be/SECRETID"),
                ("source-secret-title.md", "Source: https://www.youtube.com/watch?v=SECRETID"),
                ("missing-secret-title.md", "# Secret title\nNo source URL")):
            with open(os.path.join(self.dir, name), "w") as file:
                file.write(content)
        code, out = self.run_main({"PUB": "public"})
        self.assertEqual(code, 1)
        self.assertIn("UNVERIFIED: 3 transcript file(s)", out)
        for leaked in ("OK:", "secret-title", "Secret title", "SECRETID"):
            self.assertNotIn(leaked, out)
        code, details = self.run_main({"PUB": "public"}, "--details")
        self.assertEqual(code, 1)
        self.assertIn("missing-secret-title.md", details)

    def test_readme_and_generated_indexes_are_not_transcripts(self):
        write_transcript(self.dir, "public.md", "PUB")
        for name in ("README.md", "recurring-shows.md", "community-calls.md"):
            with open(os.path.join(self.dir, name), "w") as file:
                file.write("# Documentation or index\n")
        self.assertEqual(self.run_main({"PUB": "public"})[0], 0)

    def test_unreadable_files_fail_without_leaking_names_or_errors(self):
        write_transcript(self.dir, "secret-title.md", "SECRETID")
        for error in (PermissionError("secret-title.md"),
                      UnicodeDecodeError("utf-8", b"\xff", 0, 1, "secret-title")):
            with self.subTest(error=type(error).__name__), \
                    mock.patch.object(audit_public, "video_ids", side_effect=error):
                code, out = self.run_main({})
                self.assertEqual(code, 1)
                self.assertIn("UNVERIFIED: 1 transcript file(s)", out)
                self.assertNotIn("secret-title", out)
                self.assertNotIn("SECRETID", out)

    def test_unlisted_private_and_missing_videos_fail_with_counts_only(self):
        for name, vid in [("pub.md", "PUB"), ("unl-secret-title.md", "UNL"), ("priv-secret-title.md", "PRIV"),
                          ("gone-secret-title.md", "GONE")]:
            write_transcript(self.dir, name, vid)
        code, out = self.run_main({"PUB": "public", "UNL": "unlisted", "PRIV": "private"})  # GONE: not returned
        self.assertEqual(code, 1)
        self.assertIn("3 of 4", out)
        for leaked in ("UNL", "PRIV", "GONE", "secret-title"):
            self.assertNotIn(leaked, out)

    def test_details_flag_lists_files_for_private_use(self):
        write_transcript(self.dir, "unl.md", "UNL")
        code, out = self.run_main({"UNL": "unlisted"}, "--details")
        self.assertEqual(code, 1)
        self.assertIn("unl.md", out)

    def test_ids_are_sent_in_batches_and_the_key_stays_out_of_the_url(self):
        for i in range(120):
            write_transcript(self.dir, f"{i:03}.md", f"V{i:03}")
        calls = []
        def urlopen(request, timeout=None):
            calls.append(request)
            return FakeResponse({"items": []})
        audit_public.find_not_public(self.dir, "key-123", urlopen)
        self.assertEqual(len(calls), 3)
        self.assertNotIn("key-123", calls[0].full_url)
        self.assertEqual(calls[0].get_header("X-goog-api-key"), "key-123")

    def test_api_errors_cannot_leak_the_key_or_pass_silently(self):
        write_transcript(self.dir, "a.md", "AAA")
        def urlopen(request, timeout=None):
            raise urllib.error.HTTPError(request.full_url, 403, "quota", {}, None)
        out = io.StringIO()
        with mock.patch.dict(os.environ, {"YOUTUBE_API_KEY": "key-123"}), contextlib.redirect_stdout(out):
            code = audit_public.main(["--path", self.dir], urlopen=urlopen)
        self.assertEqual(code, 2)
        self.assertIn("403", out.getvalue())
        self.assertNotIn("key-123", out.getvalue())

    def test_missing_key_is_a_cannot_audit_not_a_pass(self):
        out = io.StringIO()
        with mock.patch.dict(os.environ, {}, clear=True), contextlib.redirect_stdout(out):
            self.assertEqual(audit_public.main(["--path", self.dir]), 2)

    def test_connection_reset_while_reading_is_a_private_cannot_audit_error(self):
        write_transcript(self.dir, "secret-title.md", "SECRETID")
        with mock.patch.object(FakeResponse, "read", side_effect=ConnectionResetError(
                "key-123 SECRETID secret-title.md")):
            code, out = self.run_main({"SECRETID": "public"})
        self.assertEqual(code, 2)
        self.assertIn("ConnectionResetError", out)
        for leaked in ("key-123", "SECRETID", "secret-title"):
            self.assertNotIn(leaked, out)


if __name__ == "__main__":
    unittest.main()
