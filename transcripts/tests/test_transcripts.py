import argparse
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

import check_duplicates
import transcripts as t
import transcript_guards as guards


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


class RepeatedChapterTitleTests(unittest.TestCase):
    STAMPED = "\n".join(f"[00:{m:02d}:00] words" for m in range(0, 30, 3))

    def run_chapters(self, fake_chat):
        with mock.patch.object(t, "openai_key", "k"), mock.patch.object(t.openai, "OpenAI"), \
                mock.patch.object(t, "chat", side_effect=fake_chat):
            return t.create_chapters(video(), self.STAMPED, "vid")

    def titles(self, out):
        return [line.split(" ", 1)[1] for line in out.splitlines()]

    def test_repeated_title_is_asked_again_with_the_earlier_titles_and_gets_a_specific_one(self):
        prompts, calls = [], {}

        def fake_chat(client, system, text, temperature):
            prompts.append(system)
            first = text.strip().split("]")[0].lstrip("[")
            calls[first] = calls.get(first, 0) + 1
            if first == "00:00:00" or calls[first] == 1:
                return f"{first} Introduction to Grafana Notebooks"  # the first answer repeats chapter one
            return f"{first} Notebook cells in practice at {first}"
        titles = self.titles(self.run_chapters(fake_chat))
        self.assertEqual(len(titles), len({title.lower() for title in titles}))
        self.assertEqual(titles[0], "Introduction to Grafana Notebooks")
        self.assertIn("Notebook cells in practice at 00:09:00", titles)
        self.assertTrue(any("Introduction to Grafana Notebooks" in p and "do not repeat" in p for p in prompts))

    def test_a_title_the_model_keeps_repeating_is_dropped_not_written_twice(self):
        def fake_chat(client, system, text, temperature):
            first = text.strip().split("]")[0].lstrip("[")
            return f"{first} Introduction to Grafana Notebooks"
        out = self.run_chapters(fake_chat)
        self.assertEqual(self.titles(out), ["Introduction to Grafana Notebooks"])
        self.assertTrue(out.startswith("00:00:00 "))

    def test_titles_differing_only_in_case_or_punctuation_count_as_repeats(self):
        self.assertEqual(t.chapter_key("Intro to Notebooks!"), t.chapter_key("intro to  notebooks"))

    def test_different_non_latin_titles_are_all_kept(self):
        names = {"00:00:00": "Введение", "00:09:00": "Обзор алертов", "00:15:00": "入门指南", "00:21:00": "告警规则"}

        def fake_chat(client, system, text, temperature):
            first = text.strip().split("]")[0].lstrip("[")
            return f"{first} {names[first]}"
        titles = self.titles(self.run_chapters(fake_chat))
        self.assertEqual(titles, list(names.values()))
        self.assertNotEqual(t.chapter_key("Grafana 入门"), t.chapter_key("Grafana 告警"))
        self.assertEqual(t.chapter_key("Año"), t.chapter_key("año!"))


class KnownNameTests(unittest.TestCase):
    NAMES = [("Beyla", ["Grafana Baa"]), ("Pyroscope", []), ("Vanderhoeven", []),
             ("Nicole Vanderhoeven", ["Nicole Vanderhovven"])]

    def fix(self, text, reference=""):
        return guards.correct_known_names(text, reference, names=self.NAMES)[0]

    def test_a_listed_wrong_spelling_is_replaced_ignoring_case(self):
        self.assertEqual(self.fix("We use Grafana Baa and grafana baa."), "We use Beyla and Beyla.")

    def test_a_close_misspelling_of_a_long_name_is_replaced(self):
        self.assertEqual(self.fix("Host: Nicole Vanderhovven."), "Host: Nicole Vanderhoeven.")
        self.assertEqual(self.fix("Thanks, Vanderhoven!"), "Thanks, Vanderhoeven!")

    def test_exact_names_in_addresses_and_files_are_not_rewritten(self):
        text = "mail tom@grafana.com or run docker grafana/grafana; prometheus.yml"
        names = self.NAMES + [("Grafana", []), ("Prometheus", [])]
        self.assertEqual(guards.correct_known_names(text, "", names=names)[0], text)

    def test_ordinary_words_and_other_names_are_left_alone(self):
        text = "A periscope, a baa from a sheep, Pyroscope and Vanderhoeven are fine."
        self.assertEqual(self.fix(text), text)

    def test_a_plural_of_a_known_name_is_left_alone(self):
        names = [("Grafana", []), ("Prometheus", []), ("Pyroscope", [])]
        text = "Many Grafanas, two Pyroscopes and some prometheuss."
        self.assertEqual(guards.correct_known_names(text, "", names=names)[0], text)
        self.assertEqual(guards.correct_known_names("Grafanna and Pyrscope", "", names=names)[0],
                         "Grafana and Pyroscope")

    def test_the_authors_own_spelling_in_the_description_is_kept(self):
        self.assertEqual(self.fix("Grafana Baa is a band.", reference="Live with Grafana Baa"),
                         "Grafana Baa is a band.")

    def test_changes_are_reported(self):
        _, changes = guards.correct_known_names("Grafana Baa", "", names=self.NAMES)
        self.assertEqual(changes, [("Grafana Baa", "Beyla")])

    def test_the_data_file_covers_the_known_cases_and_can_be_extended(self):
        names = dict(guards.load_known_names())
        self.assertIn("Grafana Baa", names["Beyla"])
        self.assertIn("Nicole Vanderhovven", names["Nicole Vanderhoeven"])
        for product in ("Alloy", "Mimir", "Loki", "Tempo", "Pyroscope"):
            self.assertIn(product, names)
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "names.txt")
            with open(path, "w") as file:
                file.write("# comment\n\nFoo | Bar baz; Qux\nQuux\n")
            self.assertEqual(guards.load_known_names(path), [("Foo", ["Bar baz", "Qux"]), ("Quux", [])])

    def test_the_summary_cleaned_text_and_chapters_are_corrected_but_the_raw_transcript_is_not(self):
        v = video(title="A show", description="About the show")
        v["transcript"] = "Grafana Baa is great " + "word " * 20
        v["timestamped"] = "\n".join(f"[00:{m:02d}:00] Grafana Baa" for m in range(0, 30, 3))

        def fake_chat(client, system, user, temperature):
            if "Write the title of ONE" in system:
                first = user.strip().split("]")[0].lstrip("[")
                return f"{first} Using Grafana Baa {first}"
            return "Grafana Baa from Nicole Vanderhovven " + "word " * 20
        with mock.patch.object(t, "openai_key", "k"), mock.patch.object(t.openai, "OpenAI"), \
                mock.patch.object(t, "chat", side_effect=fake_chat), mock.patch("builtins.print"):
            summary, cleaned = t.openai_cleanup(v, v["transcript"], "vid")
            chapters = t.create_chapters(v, v["timestamped"], "vid")
            args = argparse.Namespace(path=tempfile.mkdtemp())
            self.addCleanup(lambda: shutil.rmtree(args.path))
            t.write_markdown(args, v)
            with open(t.file_for_video(args, v)) as f:
                written = f.read()
        self.assertTrue(summary.startswith("Beyla from Nicole Vanderhoeven "))
        self.assertTrue(cleaned.startswith("Beyla from Nicole Vanderhoeven "))
        self.assertIn("Using Beyla", chapters)
        self.assertNotIn("Grafana Baa", chapters)
        self.assertIn("Grafana Baa is great", written.split("## Raw YouTube Transcript")[1])


class ChapterAddressTests(unittest.TestCase):
    def test_a_chapter_left_with_no_title_after_an_invented_address_is_removed(self):
        stamped = "\n".join(f"[00:{m:02d}:00] words" for m in range(0, 30, 3))

        def fake_chat(client, system, text, temperature):
            first = text.strip().split("]")[0].lstrip("[")
            return f"{first} tom@grano.com" if first == "00:09:00" else f"{first} Topic at {first}"
        with mock.patch.object(t, "openai_key", "k"), mock.patch.object(t.openai, "OpenAI"), \
                mock.patch.object(t, "chat", side_effect=fake_chat), mock.patch("builtins.print"):
            out = t.create_chapters(video(), stamped, "vid")
        self.assertNotIn("grano", out)
        self.assertNotIn("00:09:00", out)
        for line in out.splitlines():
            self.assertRegex(line, r"^\d\d:\d\d:\d\d \S")
        self.assertIn("Topic at 00:15:00", out)


class MusicCaptionTests(unittest.TestCase):
    def entries(self, texts):
        return [{"text": text, "start": float(i * 5)} for i, text in enumerate(texts)]

    SPEECH = ["welcome everyone to the keynote of this conference", "today we will talk about observability"]

    def test_only_literal_labels_leave_the_written_text_and_lyrics_leave_the_chapter_text(self):
        texts = ["[Music]", "\u266a \u266a", "[Applause]", "heat", "heat", "heat", "heat", "heat"] + self.SPEECH
        text, stamped = t.entries_to_transcript(self.entries(texts), "keynote")
        self.assertEqual(text, " ".join(["\u266a \u266a"] + ["heat"] * 5 + self.SPEECH))
        self.assertNotIn("heat", stamped.lower())
        self.assertNotIn("\u266a", stamped)
        self.assertIn("welcome everyone", stamped)
        self.assertIn("heat", " ".join(t.CAPTION_NOISE["keynote"]))

    def test_ordinary_repeated_speech_is_kept_in_both_texts(self):
        texts = ["thank you", "so", "thank you", "yes", "thank you"] + self.SPEECH
        text, stamped = t.entries_to_transcript(self.entries(texts), "qa")
        self.assertEqual(text, " ".join(texts))
        for part in texts:
            self.assertIn(part, stamped)

    def test_a_phrase_repeated_fewer_than_five_times_is_kept(self):
        texts = ["heat"] * 4 + self.SPEECH
        _, stamped = t.entries_to_transcript(self.entries(texts), "four")
        self.assertEqual(stamped.lower().count("heat"), 4)

    def test_a_word_said_once_in_speech_is_kept(self):
        texts = ["I want some respect for open source", "respect", "and so on today we will be learning more"]
        text, _ = t.entries_to_transcript(self.entries(texts), "once")
        self.assertIn("respect", text)
        self.assertEqual(text.count("respect"), 2)

    def test_a_chapter_named_from_the_music_is_not_written(self):
        t.CAPTION_NOISE["keynote2"] = ["respect"] * 5 + ["Heat", "heat"]
        stamped = "\n".join(f"[00:{m:02d}:00] we talk about alerting rules" for m in range(0, 30, 3))
        calls = {}

        def fake_chat(client, system, text, temperature):
            first = text.strip().split("]")[0].lstrip("[")
            calls[first] = calls.get(first, 0) + 1
            if first == "00:00:00":
                return f"{first} Respect"
            return f"{first} Alerting rules at {first}"
        with mock.patch.object(t, "openai_key", "k"), mock.patch.object(t.openai, "OpenAI"), \
                mock.patch.object(t, "chat", side_effect=fake_chat), mock.patch("builtins.print"):
            out = t.create_chapters(video(), stamped, "keynote2")
        self.assertNotIn("Respect", out)
        self.assertEqual(calls["00:00:00"], 2)
        self.assertIn("Alerting rules", out)

    def test_a_title_with_words_that_are_also_spoken_is_not_dropped(self):
        noise = guards.noise_words(["respect"])
        self.assertFalse(guards.title_only_in_noise("Respect for maintainers", noise, "we show respect for maintainers"))
        self.assertTrue(guards.title_only_in_noise("Respect", noise, "we talk about alerting"))


class InventedAddressTests(unittest.TestCase):
    CAPTION = "you can email me at tomgrano.com or see https://grafana.com/docs for more " + "word " * 20

    def test_the_address_the_cleanup_made_up_is_found(self):
        self.assertEqual(guards.unsupported_strings("write to tom@grano.com", self.CAPTION), ["tom@grano.com"])

    def test_addresses_in_the_captions_title_or_description_are_fine(self):
        text = "see https://grafana.com/docs. Mail tom@grafana.com or www.example.org/x."
        self.assertEqual(guards.unsupported_strings(text, self.CAPTION, "tom@grafana.com", "WWW.EXAMPLE.ORG/x"), [])

    def test_removal_leaves_the_rest_of_the_text(self):
        text, removed = guards.remove_unsupported("Email tom@grano.com today.", self.CAPTION)
        self.assertEqual((text, removed), ("Email  today.", ["tom@grano.com"]))

    def run_cleanup(self, summary, cleaned, description="Plain description"):
        v = video(title="Big Tent", description=description)

        def fake_chat(client, system, user, temperature):
            return summary if "3 to 5 sentences" in system else cleaned
        with mock.patch.object(t, "openai_key", "k"), mock.patch.object(t.openai, "OpenAI"), \
                mock.patch.object(t, "chat", side_effect=fake_chat), mock.patch("builtins.print"):
            return t.openai_cleanup(v, self.CAPTION, "vid")

    def test_cleanup_that_invents_an_email_falls_back_to_the_raw_text_for_that_chunk(self):
        summary, cleaned = self.run_cleanup("A talk.", "You can email me at tom@grano.com. " + "Word " * 20)
        self.assertEqual(cleaned, self.CAPTION.strip())
        self.assertNotIn("tom@grano.com", cleaned)

    def test_the_summary_loses_an_invented_address_but_keeps_one_from_the_description(self):
        summary, _ = self.run_cleanup("Contact tom@grano.com or tom@grafana.com. Topics: a", "ok " * 100,
                                      description="Contact tom@grafana.com")
        self.assertNotIn("tom@grano.com", summary)
        self.assertIn("tom@grafana.com", summary)

    def test_the_emitted_prompts_tell_the_model_the_same_rules(self):
        seen = []

        def fake_chat(client, system, user, temperature):
            seen.append(system)
            return "text " * 30
        stamped = "\n".join(f"[00:{m:02d}:00] words" for m in range(0, 30, 3))
        with mock.patch.object(t, "openai_key", "k"), mock.patch.object(t.openai, "OpenAI"), \
                mock.patch.object(t, "chat", side_effect=fake_chat), mock.patch("builtins.print"):
            t.openai_cleanup(video(), self.CAPTION, "vid")
            t.create_chapters(video(), stamped, "vid")
        self.assertGreaterEqual(len(seen), 3)
        for prompt in seen:
            self.assertIn("Do not write an email address or a web address", prompt)
            self.assertIn("Ignore song lyrics", prompt)
            self.assertIn("Beyla", prompt)


class EventTypeTests(unittest.TestCase):
    """The summary must take the event type from the title and description, not assume a community call."""

    def prompts(self, **video_kwargs):
        seen = []

        def fake_chat(client, system, user, temperature):
            seen.append(system)
            return "text " * 20
        v = video(**video_kwargs)
        stamped = "\n".join(f"[00:{m:02d}:00] words" for m in range(0, 30, 3))
        with mock.patch.object(t, "openai_key", "k"), mock.patch.object(t.openai, "OpenAI"), \
                mock.patch.object(t, "chat", side_effect=fake_chat), mock.patch("builtins.print"):
            t.openai_cleanup(v, "words " * 50, "vid")
            t.create_chapters(v, stamped, "vid")
        return seen

    def test_no_prompt_assumes_a_community_call(self):
        for prompt in self.prompts(title="How Bayer runs Grafana: a customer presentation",
                                   description="Bayer talks about their setup."):
            self.assertNotIn("community call", prompt.replace(t.EVENT_TYPE_RULES, ""))

    def test_summary_prompt_takes_event_type_from_title_and_description_and_gives_both(self):
        summary = self.prompts(title="Fireside chat with thredd", description="A chat about payments.")[0]
        self.assertIn("title and description only", summary)
        self.assertIn("not the event date", summary)
        self.assertIn("Video title: Fireside chat with thredd", summary)
        self.assertIn("Description: A chat about payments.", summary)


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

    def setUp(self):
        t._warned_truncated_titles.clear()

    def test_truncated_title_without_matching_description_is_marked_and_warns(self):
        self.assertEqual(len(self.CUT), 100)
        v = video(title=self.CUT, description="[INSERT DESCRIPTION]")
        with mock.patch("builtins.print") as printed:
            self.assertEqual(t.video_title(v), t.clean_title(self.CUT) + "\u2026")
        self.assertTrue(any("probably truncated" in str(c) for c in printed.call_args_list))

    def test_truncated_title_warns_once_per_video_however_often_it_is_read(self):
        v = video(title=self.CUT, description="[INSERT DESCRIPTION]")
        with mock.patch("builtins.print") as printed:
            titles = {t.video_title(v) for _ in range(5)}
            t.video_title(video(video_id="other_id_11", title=self.CUT, description=""))
        self.assertEqual(len(titles), 1)
        self.assertEqual(len([c for c in printed.call_args_list if "probably truncated" in str(c)]), 2)

    def test_marked_title_reaches_the_heading_and_the_marker_is_not_doubled(self):
        v = video(title=self.CUT, description="[INSERT DESCRIPTION]")
        v["transcript"], v["timestamped"] = "x " * 100, "[00:00:00] x\n[00:05:00] y"
        with mock.patch.object(t, "openai_key", ""), mock.patch("builtins.print"):
            args = argparse.Namespace(path=tempfile.mkdtemp())
            self.addCleanup(lambda: shutil.rmtree(args.path))
            t.write_markdown(args, v)
            with open(t.file_for_video(args, v)) as f:
                heading = f.readline().rstrip("\n")
        self.assertTrue(heading.endswith("Operatio\u2026"))
        self.assertFalse(heading.endswith("\u2026\u2026"))

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
