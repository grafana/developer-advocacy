# AGENTS.md

This repository is **public**. It holds the Grafana Developer Advocacy team's processes, project notes, and an automated YouTube transcript archive. Anything committed here, including PR text and CI logs, is visible to everyone.

## What is in the repo

| Path | What it is | Hand-edited? |
|---|---|---|
| `README.md` | Entry point: team intro, links to processes and projects | Yes |
| `processes/` | How-to docs (video, blog post, docs contribution, conference talk, Office Hours / community call) | Yes |
| `templates/` | Checklists for shows (`GOH checklist.md`, `A&A checklist.md`) | Yes |
| `projects/` | One folder per program or tutorial (Office Hours, Café con Grafana, Adobo and Avocados, Loki and OTel community calls, Play, Visualize CSV, Kapa-Summarize, Talks, ...) | Yes |
| `workshops/`, `code-examples/` | Workshop material and example code | Yes |
| `transcripts/` | Python tooling plus about 780 generated transcript `.md` files (see below) | Tooling yes; transcripts: regenerate with the script, hand-edit only to remove invented or private content |
| `.github/workflows/` | `refresh-transcripts.yml` (weekly), `audit-transcripts.yml` (weekly public-video audit), `check-transcripts.yml` (PR checks) | Yes |
| `.github/CODEOWNERS` | Owners of `transcripts/`, the refresh and audit workflows, and the agent-steering files (`AGENTS.md`, `CLAUDE.md`, `.no-mistakes.yaml`, `.agents/`) | Yes |

Prose areas (`processes/`, `projects/`, `templates/`, `workshops/`) are plain Markdown with no build step. Keep relative links working (many paths contain spaces) and do not add personal data (emails, phone numbers, private links).

## The transcripts system (`transcripts/`)

Most of the code and most of the review risk live here.

- `transcripts.py` is the generator. It lists channel videos, keeps only **public, finished** videos, fetches captions through `captions_api.py` (official YouTube captions API with OAuth), calls OpenAI for a summary, chapters and cleaned text, and writes `<publish time>-<slug>.md`.
- `check_duplicates.py` fails if a new transcript is for a video that already has one. Identity is the video ID in the `URL:` line, never the filename or title.
- `audit_public.py` fails if any transcript's video is not public (run weekly by `audit-transcripts.yml`). Its CI logs show counts only. Run `--details` only locally with a `YOUTUBE_API_KEY`, and never put its output in a PR, issue or log.
- `recurring_shows_index.py` regenerates `recurring-shows.md` and `community-calls.md`. **Those two files are generated. Never edit them by hand**; re-run the script and commit its output.
- `categorize.py`, `get_refresh_token.py`, `run.sh`, `env.example`: helpers and setup. Real secrets live in Vault (`ci/repo/grafana/developer-advocacy/`), never in the repo or in GitHub secrets.
- `tests/` holds the unit tests (`unittest`, Python 3.12 in CI).
- Details, quota budget and failure runbook: `transcripts/README.md`.

The weekly workflow opens an automated PR (`automation/refresh-transcripts`) with new transcripts. Those PRs are mostly generated Markdown; review them by sampling and by checking the invariants in the review skill, not line by line.

### Commands

```bash
cd transcripts
pip install -r requirements.txt
python -m unittest discover -s tests                 # run the tests (same as CI)
python recurring_shows_index.py                      # regenerate the generated index files
python check_duplicates.py --base origin/main        # duplicate-video check (same as CI)
python transcripts.py --days 14                      # needs API keys in .env; spends quota
```

Do not run `transcripts.py` against the real YouTube or OpenAI APIs just to verify a change. It spends quota and money. Use the tests.

## Conventions

- Dependencies in `transcripts/requirements.txt` are pinned. Renovate opens the bump PRs.
- GitHub Actions are pinned to full commit SHAs with a version comment, and workflows use `permissions: {}` at the top with per-job grants.
- Commit and PR titles use Conventional Commits, for example `fix(transcripts): ...`.
- Keep a PR to one concern, and keep its description accurate about what the diff does.
- Never commit `.env`, tokens, or `venv/`. Do not commit `.claude/` (local agent state and worktrees).
- Content from non-public YouTube videos (private, unlisted, unaired) must never be written to the repo, logs or PR text.

## Opening PRs: use no-mistakes

Open PRs through [no-mistakes](https://github.com/kunchenguid/no-mistakes) instead of pushing to `origin` and opening the PR by hand. It runs review, tests, docs and lint checks in a disposable worktree and only opens the PR once they pass.

```bash
no-mistakes init                 # once per clone (installs the /no-mistakes agent skill)
git checkout -b my-change
# ...make and commit changes...
git push no-mistakes             # runs the pipeline, then opens the PR
```

Agents can run `/no-mistakes <task>` to do a task and gate it in one step. Forks: `no-mistakes init --fork-url <your-fork-url>`.

The repo's review guidance for the pipeline is in `.no-mistakes.yaml` and `.agents/skills/review/SKILL.md`. Only the copy of `.no-mistakes.yaml` on the default branch is read, so changes to it take effect after merge. Changes to `AGENTS.md` are a deliberate human decision.

## Reviewing a PR

Follow `.agents/skills/review/SKILL.md`.
