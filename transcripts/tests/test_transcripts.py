import argparse
import os
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

import check_duplicates
import transcripts as t


def video(video_id="abc123DEF_-", title="A title", description="Plain description",
          published="2026-11-03T18:58:57Z", privacy="public"):
    return {"id": video_id, "status": {"privacyStatus": privacy},
            "snippet": {"title": title, "description": description, "publishedAt": published,
                        "liveBroadcastContent": "none"}}


def write_transcript(directory, name, video_id, body="text"):
    with open(os.path.join(directory, name), "w") as f:
        f.write(f"# T\n\nURL: https://www.youtube.com/watch?v={video_id}\n\n{body}\n")


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


if __name__ == "__main__":
    unittest.main()
