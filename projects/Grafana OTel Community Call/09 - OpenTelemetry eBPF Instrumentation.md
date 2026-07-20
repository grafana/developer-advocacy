---
url:
date:
---

# [[09 - OpenTelemetry eBPF Instrumentation]]

[Link to YouTube video](https://www.youtube.com/live/VEFn_ljZhCw)

Guests:: Nikola Grcevski, Mario Macías

**Title:** OpenTelemetry eBPF Instrumentation (Grafana ❤️‍🔥 OTel Community Call #9)

**Description:**

In this episode of the Grafana OTel Community Call, we're exploring OpenTelemetry eBPF Instrumentation (OBI). OpenTelemetry eBPF Instrumentation (OBI) offers a powerful way to instrument applications at the system kernel level, capturing essential "RED metrics" — request rate, error rate, and duration — and network flows without requiring code changes, rebuilds, or redeployments.

We will cover the project's architecture, discuss its origins as Grafana Beyla, and look ahead to the roadmap for language and runtime coverage.

Guests: Mario Macías (https://www.linkedin.com/in/mariomac/), Nikola Grcevski (https://www.linkedin.com/in/nikola-grcevski-16796717/)
Hosts: Imma Valls (https://www.linkedin.com/in/imma-valls/)

Join the conversation, bring your questions, and learn how this project is evolving with contributions from across the community.

#opentelemetry #ebpf #grafana #observability

## Pre-show checklist

- [x] Create a new `.md` file and copy this template into it. Check things off as you work through it.
- [x] Update [Grafana OTel Community Call Readme](/projects/Grafana%20OTel%20Community%20Call.md) to add this file to the `Upcoming` section.
- [x] Contact Nikola and Mario about the show (internal — just a Slack ping, not a cold outreach).
- [x] Choose a date for late July. Check [the Monday board](https://grafana-labs.monday.com/boards/5724430500) to avoid clashing with another livestream (Beyla community call is 2nd Wednesday of the month — avoid that day).
- [x] Confirm the time with both guests (1.5 hours total: 15 min tech check + 1hr stream + 15 min debrief).
- [x] Send the calendar invite ("this instance only").
- [x] Create a thumbnail on Canva using the standard format; check on thumbsup.tv.
- [x] Schedule the broadcast on Streamyard → Grafana YouTube channel.
  - [x] Title: OpenTelemetry eBPF Instrumentation (Grafana ❤️‍🔥 OTel Community Call #9)
  - [x] Add standard description + guests' contact/social links.
- [x] Get the Streamyard invite link into the calendar invite location field.
- [x] Announce on the Grafana Meetup page and the Luma Grafana & Friends calendar.
- [ ] Slack: `#opentelemetry`, `#community-champions` (internal); public Grafana Slack `#opentelemetry` + events.
- [ ] Add to the monthly Community Calendar forum thread (community.grafana.com) and Google Calendar.
- [ ] Create a community forum thread for the episode (same pattern as past ones, e.g. the GenAI apps thread).

Reference links to gather ahead of time:

- https://opentelemetry.io/docs/zero-code/obi/
- https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation
- https://grafana.com/blog/opentelemetry-ebpf-instrumentation-beyla-donation/
- https://opentelemetry.io/blog/2025/obi-announcing-first-release/

## Talking points

> Bullet points, not a script — keep it casual.

- Intro
  - *Hello and welcome to Grafana OTel Community Call. I'm `<name>`, a `<position>` at Grafana Labs, and today we're talking about eBPF-based auto-instrumentation and what it's like maintaining OpenTelemetry eBPF Instrumentation (OBI) — the project formerly known as Beyla.*
- Introduce guests: Nikola Grcevski, Mario Macías
  - Who are you, and what do you do at Grafana Labs?
  - How did each of you end up working on eBPF?
- From Beyla to OBI
  - What Beyla was, and why Grafana donated it to OpenTelemetry
  - What actually changed technically/organizationally when it became OBI
  - Who's contributing now — Grafana, Splunk, Odigos, Coralogix, others
- How eBPF instrumentation actually works
  - Zero-code, out-of-process instrumentation at the protocol level vs. library-level instrumentation
  - What you get "for free" vs. what still needs an SDK
  - Live demo: instrumenting a service with zero code changes
- Maintaining an OTel SIG day-to-day
  - What does a maintainer actually do — triage, review, roadmap calls?
  - How the eBPF Instrumentation SIG runs (weekly community call, CNCF Slack `#otel-ebpf-instrumentation`)
  - The hardest part of maintaining something used across many companies/vendors now
  - Nikola's GPU/eBPF auto-instrumentation work (SREcon25 EMEA talk) — anything crossing over into OBI?
- Where it's headed
  - 2026 goals for OBI
  - Language/runtime coverage gaps today
  - How it plays with SDK-based instrumentation and Grafana Alloy/Tempo/Pyroscope
- The human side
  - Favorite "aha" moment maintaining this
  - Advice for someone who wants to start contributing to OBI
- Outro
  - Where should people go to learn more / get involved?

### Just before the show

> Here are some points to discuss with the guests in the 15 minutes before the stream begins.

- [ ] How do you pronounce your names?
- [ ] Pronouns?
- [ ] Reassure: talking points are a guide, not a script.
- [ ] Screen-share check if doing a live demo.
- [ ] Standard streaming logistics reminder (comments via private chat, can pivot away from any topic, stick around after for debrief, stall if host disconnects).

## Post-show checklist

- [ ] Add timestamps (at least four).
- [ ] Add shared links to the video description.
- [ ] Add YouTube cards at relevant points.
- [ ] Add to the "Grafana OTel Community Call" playlist.
- [ ] Upload recording to the shared Drive folder.
- [ ] Consider repurposing into shorts (e.g., "what is eBPF instrumentation in 60 seconds", "zero-code instrumentation demo").
- [ ] Update the Advocate Contributions sheet.
- [ ] Promote on Grafana socials (X, Bluesky, LinkedIn).

### Timestamps

00:00:00 Introductions
