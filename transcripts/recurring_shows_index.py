"""Generate transcripts/recurring-shows.md, an index of every recurring show and community call.

The index is built from the transcript files in this directory, so re-run it
after fetching new transcripts with transcripts.py:

    python3 recurring_shows_index.py

Only the standard library is needed. It also writes a short community-calls.md that points
to the community call sections.

Show detection rules (first match wins, matched against the video title):

1. A title that contains "community call" is a community call. It goes to the first rule in
   COMMUNITY_CALL_SHOWS whose pattern matches (Loki, Tempo, Mimir, ...). Add a new product
   there to give a new community call show its own section.
2. Any other title is checked against SERIES_SHOWS: recurring series recognised by a title
   pattern such as "Office Hours", "The Context Window" or "Zero to Hero: Loki".
3. A title that looks like an episode of a series ("Ep 3", "#12", "Part 2", "Episode 4")
   but matches no rule is listed on stderr as a candidate, so a new show can be added.
"""
import argparse
import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(HERE, "recurring-shows.md")
COMMUNITY_OUTPUT = os.path.join(HERE, "community-calls.md")

# Community call shows: (section name, regex on the title, per-show page or None).
# Only titles containing "community call" are tested against these.
COMMUNITY_CALL_SHOWS = [
    ("Grafana OpenTelemetry Community Call", r"opentelemetry community call|alloy, opentelemetry|otel and alloy|opamp", "../projects/Grafana OTel Community Call/README.md"),
    ("Loki Community Call", r"loki", "../projects/Loki Community Calls/Loki Community Calls.md"),
    ("Tempo Community Call", r"tempo", None),
    ("Mimir Community Call", r"mimir", None),
    ("Alloy and Grafana Agent Community Call", r"alloy|grafana agent", None),
    ("Beyla Community Call", r"beyla", None),
    ("Pyroscope Community Call", r"pyroscope", None),
    ("OnCall Community Call", r"oncall", None),
    ("Grafana Campfire (Grafana Community Call)", r"campfire", None),
]
OTHER_COMMUNITY_CALLS = "Other Community Calls"

# Other recurring series: (section name, regex on the title, per-show page or None).
SERIES_SHOWS = [
    ("The Context Window", r"context window", None),
    ("Kubernetes Monitoring Helm Chart Office Hours", r"(k8s-monitoring|kubernetes monitoring).*office hours", None),
    ("Grafana Office Hours", r"office hours", "../projects/Grafana Office Hours"),
    ("Observability Sessions", r"observability sessions", None),
    ("Grafana Alloy for Beginners", r"alloy for beginners", None),
    ("Grafana for Beginners", r"grafana for beginners", None),
    ("Zero to Hero: Loki", r"zero to hero", None),
    ("Cafe con Grafana (Spanish)", r"caf. con grafana", "../projects/CafeConGrafana/README.md"),
    ("Ask the Experts", r"ask the experts", None),
    ("Grafana Release TL;DR", r"tl;dr", None),
    ("Observability as Code with Grafana Foundation SDK", r"observability as code with grafana foundation sdk", None),
    ("Big Tent (Podcast)", r"big tent", None),
    ("The Story of Grafana (Documentary)", r"story of grafana", None),
    ("Grafana & Friends and Grafana Meetups", r"grafana (&|and) friends|grafana meetup", None),
]

# A title that looks like an episode of some series.
EPISODE_PATTERN = r"\b(ep\.? ?\d+|episode \d+|#\d+|part \d+)\b"


def read_transcript(path):
    """Return the metadata and one-line topic for a transcript file."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    lines = text.split("\n")
    title = html.unescape(lines[0].lstrip("# ").strip())
    published = re.search(r"^Published on (\S+)", text, re.M)
    url = re.search(r"^URL: (\S+)", text, re.M)
    summary = re.search(r"^## Summary\s*\n+(.+?)\n\s*\n", text, re.M | re.S)
    return {
        "title": title,
        "date": published.group(1)[:10] if published else os.path.basename(path)[:10],
        "url": url.group(1) if url else "",
        "topic": one_line(summary.group(1)) if summary else "",
        "file": os.path.basename(path),
    }


def one_line(summary, limit=220):
    """First sentence of the summary, shortened to a single line."""
    summary = html.unescape(" ".join(summary.split()))
    sentence = re.split(r"(?<=[.!?])\s", summary, maxsplit=1)[0]
    if len(sentence) > limit:
        sentence = sentence[:limit].rsplit(" ", 1)[0].rstrip(",;:") + "..."
    return sentence


def show_for(title):
    """Return the show section for a title, or None if it is not part of a recurring show."""
    if re.search(r"community call", title, re.I):
        for name, pattern, _ in COMMUNITY_CALL_SHOWS:
            if re.search(pattern, title, re.I):
                return name
        return OTHER_COMMUNITY_CALLS
    for name, pattern, _ in SERIES_SHOWS:
        if re.search(pattern, title, re.I):
            return name
    return None


def collect():
    """Find episodes of recurring shows among the transcripts.

    Returns the matched episodes and the titles that look like episodes of an unknown series."""
    episodes, candidates = [], []
    for name in sorted(os.listdir(HERE)):
        if not name.endswith(".md") or name in ("README.md", "recurring-shows.md", "community-calls.md"):
            continue
        info = read_transcript(os.path.join(HERE, name))
        info["show"] = show_for(info["title"])
        if info["show"]:
            episodes.append(info)
        elif re.search(EPISODE_PATTERN, info["title"], re.I):
            candidates.append(info["title"])
    return episodes, candidates


def show_order():
    return ([n for n, _, _ in COMMUNITY_CALL_SHOWS] + [OTHER_COMMUNITY_CALLS]
            + [n for n, _, _ in SERIES_SHOWS])


def render(episodes):
    community = {n for n, _, _ in COMMUNITY_CALL_SHOWS} | {OTHER_COMMUNITY_CALLS}
    pages = {n: p for n, _, p in COMMUNITY_CALL_SHOWS + SERIES_SHOWS if p}
    by_show = {n: [e for e in episodes if e["show"] == n] for n in show_order()}
    n_community = sum(len(v) for n, v in by_show.items() if n in community)

    out = [
        "# Recurring Shows and Community Calls",
        "",
        "Index of every recurring Grafana show on the YouTube channel: all community calls "
        "(Loki, Tempo, Mimir, Alloy, Beyla, Pyroscope, OnCall, OpenTelemetry, Campfire), "
        "Office Hours, The Context Window, and other series. "
        "Each show lists its episodes newest first, with the YouTube publish date, title, "
        "a one-line topic and the video link. Full transcripts are in this directory.",
        "",
        f"This file is generated by `recurring_shows_index.py` from the transcripts: "
        f"{len(episodes)} episodes, of which {n_community} are community calls. Do not edit it by hand.",
        "",
        "## Shows",
        "",
        "Community calls:",
        "",
    ]
    for name in show_order():
        if not by_show[name]:
            continue
        if name in community:
            out.append(f"- [{name}](#{anchor(name)}) ({len(by_show[name])})")
        elif out[-1] != "Other series:" and "Other series:" not in out:
            out += ["", "Other series:", "", f"- [{name}](#{anchor(name)}) ({len(by_show[name])})"]
        else:
            out.append(f"- [{name}](#{anchor(name)}) ({len(by_show[name])})")
    out.append("")
    for name in show_order():
        group = sorted(by_show[name], key=lambda e: e["date"], reverse=True)
        if not group:
            continue
        out += [f"## {name}", ""]
        if name in pages:
            page = pages[name]
            out += [f"Per-show page: [{page.split('/')[-2] if page.endswith('.md') else page.split('/')[-1]}]({page.replace(' ', '%20')})", ""]
        for e in group:
            line = f"- {e['date']} - [{e['title']}]({e['url']})"
            if e["topic"]:
                line += f": {e['topic']}"
            out.append(line)
        out.append("")
    return "\n".join(out)


def render_community_pointer(episodes):
    community = {n for n, _, _ in COMMUNITY_CALL_SHOWS} | {OTHER_COMMUNITY_CALLS}
    counts = [(n, sum(1 for e in episodes if e["show"] == n)) for n in show_order() if n in community]
    out = [
        "# Grafana Community Calls",
        "",
        "The full list of past Grafana community calls, with dates, titles, topics and YouTube links, "
        "is in [recurring-shows.md](recurring-shows.md), together with Office Hours, The Context Window "
        "and the other recurring shows. This file is generated by `recurring_shows_index.py`.",
        "",
        "Community call shows:",
        "",
    ]
    for name, count in counts:
        if count:
            out.append(f"- [{name}](recurring-shows.md#{anchor(name)}) ({count} episodes)")
    return "\n".join(out)


def anchor(heading):
    slug = re.sub(r"[^\w\s-]", "", heading.lower())
    return re.sub(r"\s", "-", slug.strip())


def main():
    parser = argparse.ArgumentParser(description="Generate the recurring shows index from transcript files.")
    parser.add_argument("-o", "--output", default=OUTPUT, help="Output file (default: recurring-shows.md)")
    parser.add_argument("--community-output", default=COMMUNITY_OUTPUT,
                        help="Output file for the community calls pointer (default: community-calls.md)")
    args = parser.parse_args()
    episodes, candidates = collect()
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(render(episodes) + "\n")
    with open(args.community_output, "w", encoding="utf-8") as f:
        f.write(render_community_pointer(episodes) + "\n")
    print(f"Wrote {len(episodes)} episodes to {args.output}")
    for title in candidates:
        print(f"Possible new series, no show rule matches: {title}", file=sys.stderr)


if __name__ == "__main__":
    main()
