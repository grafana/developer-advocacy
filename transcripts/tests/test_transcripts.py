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
          published="2026-11-03T18:58:57Z"):
    return {"id": video_id, "snippet": {"title": title, "description": description, "publishedAt": published}}


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

    def test_video_with_placeholder_is_skipped_and_logged(self):
        draft = video("draft1", description="[INSERT DESCRIPTION HERE]")
        with mock.patch.object(t, "get_transcript") as get_transcript, \
                mock.patch("builtins.print") as printed:
            processed = t.fetch_transcripts(self.args, [draft])
        self.assertEqual(processed, [])
        get_transcript.assert_not_called()
        self.assertTrue(any("template placeholder" in str(c) and "draft1" in str(c)
                            for c in printed.call_args_list))


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
