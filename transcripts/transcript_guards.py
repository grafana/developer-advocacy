"""Checks that run on text the model wrote, and on the captions it was given, before anything is saved.

The prompts ask the model to be careful with names, music and invented addresses. These functions do not rely on
that: each one changes or rejects the output deterministically, so it can be unit tested.
"""
import difflib
import os
import re

KNOWN_NAMES_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "known_names.txt")

# A close misspelling is fixed only for names of at least this many letters, and only if it is at least this similar.
FUZZY_MIN_LETTERS = 6
FUZZY_MIN_RATIO = 0.85


def load_known_names(path=KNOWN_NAMES_FILE):
    """The known names as a list of (name, [wrong spellings]), read from the data file."""
    names = []
    try:
        with open(path, encoding="utf-8") as file:
            lines = file.read().splitlines()
    except OSError:
        return names
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        name, _, wrong = line.partition("|")
        names.append((name.strip(), [w.strip() for w in wrong.split(";") if w.strip()]))
    return names


def _present(spelling, reference):
    return re.search(rf"(?<!\w){re.escape(spelling)}(?!\w)", reference, re.IGNORECASE) is not None


def correct_known_names(text, reference="", names=None):
    """`text` with misspelled known names fixed, and the list of (wrong, right) changes made.

    `reference` is the video title and description: a spelling that appears there is the author's own and is kept."""
    if not text:
        return text, []
    names = load_known_names() if names is None else names
    changes = []

    def replace(pattern, right, text):
        def swap(match):
            if match.group(0) == right or _present(match.group(0), reference):
                return match.group(0)
            changes.append((match.group(0), right))
            return right
        return re.sub(pattern, swap, text, flags=re.IGNORECASE)

    for name, wrong_spellings in names:
        for wrong in wrong_spellings:
            text = replace(rf"(?<!\w){re.escape(wrong)}(?!\w)", name, text)
        if " " not in name and sum(ch.isalpha() for ch in name) >= FUZZY_MIN_LETTERS:
            lowered = name.lower()

            def close(match, name=name, lowered=lowered):
                word = match.group(0)
                if word.lower() == lowered or word[0].lower() != lowered[0]:
                    return word
                if difflib.SequenceMatcher(None, word.lower(), lowered).ratio() < FUZZY_MIN_RATIO:
                    return word
                if _present(word, reference):
                    return word
                changes.append((word, name))
                return name
            text = re.sub(r"(?<!\w)[^\W\d_]{%d,%d}(?!\w)" % (len(name) - 2, len(name) + 2), close, text)
    return text, changes


def known_names_prompt(names=None):
    names = load_known_names() if names is None else names
    return ", ".join(name for name, _ in names)


# Captions that are not speech.
_BRACKETED = re.compile(r"^[\[(][^\])]*[\])]$")
_MUSIC_NOTES = re.compile(r"[♪♫♬♩]")
# A short fragment repeated this many times within this many captions is a song hook, not speech.
LYRIC_REPEATS = 5
# Ordinary speech that is often repeated and is never a song hook.
COMMON_SPEECH = {"thank you", "thanks", "yes", "yeah", "yep", "no", "okay", "ok", "all right", "alright", "right",
                 "so", "well", "um", "uh", "mm", "hmm", "you know", "sure", "great", "cool", "good", "bye",
                 "hello", "hi", "now", "and", "but", "the"}
LYRIC_WINDOW = 8
LYRIC_MAX_WORDS = 4


def _normal(text):
    return " ".join(re.sub(r"[^\w\s]", "", text.lower()).split())


def is_non_speech_caption(text):
    """A caption that is only a sound label such as [Music] or [Applause], or has music notes."""
    text = (text or "").strip()
    return bool(_BRACKETED.match(text)) or bool(_MUSIC_NOTES.search(text))


def noise_flags(texts):
    """One boolean per caption text: True for sound labels, music notes, and short fragments that repeat
    like song lyrics."""
    texts = list(texts)
    keys = [_normal(t) for t in texts]
    noise = [is_non_speech_caption(t) or not k for t, k in zip(texts, keys)]
    for index, key in enumerate(keys):
        words = key.split()
        if noise[index] or not words or len(words) > LYRIC_MAX_WORDS or key in COMMON_SPEECH:
            continue
        # A fragment that repeats ("respect respect respect") or recurs close by is a song hook.
        within = keys[max(0, index - LYRIC_WINDOW + 1):index + LYRIC_WINDOW]
        if len(set(words)) == 1 and len(words) >= LYRIC_REPEATS or within.count(key) >= LYRIC_REPEATS:
            noise[index] = True
    return noise


def split_speech_and_noise(texts):
    """Split caption texts into (kept, noise), each in the original order."""
    texts = list(texts)
    flags = noise_flags(texts)
    return [t for t, n in zip(texts, flags) if not n], [t for t, n in zip(texts, flags) if n]


def noise_words(noise_texts):
    return {w for t in noise_texts for w in _normal(t).split() if len(w) >= 3}


def title_only_in_noise(title, noise, window_text):
    """True when a chapter title's words come from the music or lyric captions that were dropped and do not appear
    in the speech of the window the chapter was written for."""
    words = [w for w in _normal(title).split() if len(w) >= 3]
    if not words or not noise:
        return False
    heard = set(_normal(window_text).split())
    return all(w in noise and w not in heard for w in words)


EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
URL = re.compile(r"(?:https?://|www\.)[^\s<>()\[\]\"']+", re.IGNORECASE)


def _strip_trailing(url):
    return url.rstrip(".,;:!?)\"'")


def _squash(text):
    return re.sub(r"\s+", "", text.lower())


def unsupported_strings(text, *sources):
    """The email addresses and URLs in `text` that appear in none of the `sources` (the captions, the title and the
    description), in the order they appear."""
    haystack = _squash(" ".join(s for s in sources if s))
    found = []
    for pattern in (EMAIL, URL):
        for match in pattern.finditer(text or ""):
            candidate = _strip_trailing(match.group(0))
            if _squash(candidate) not in haystack and candidate not in found:
                found.append(candidate)
    return found


def remove_unsupported(text, *sources):
    """`text` with every email address or URL that is not in the sources removed, and the list removed."""
    removed = unsupported_strings(text, *sources)
    for item in removed:
        text = text.replace(item, "")
    return text, removed
