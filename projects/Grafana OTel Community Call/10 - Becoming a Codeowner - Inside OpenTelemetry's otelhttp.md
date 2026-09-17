---
url:
date: September 28th 2026, 14:00 CEST
---

# [[10 - Becoming a Codeowner - Inside OpenTelemetry's otelhttp]]

[Link to YouTube video]()

Guests:: Sonal Gaud

**Title:** Becoming a Codeowner: Inside OpenTelemetry's otelhttp (Grafana ❤️‍🔥 OTel Community Call #10)

**Description:**

In this episode of the Grafana OTel Community Call, we're joined by Sonal Gaud, codeowner of `otelhttp` on `opentelemetry-go-contrib`. We'll trace her path from writing test-coverage PRs to owning the instrumentation library that most Go services use to get HTTP traces and metrics for free — and go deep on how otelhttp actually works under the hood: context propagation, metrics/attributes via the `Labeler`, route cardinality, and how the library evolves alongside HTTP semantic conventions.

We'll also talk about what it's like reviewing PRs and protecting backwards compatibility in a widely-used contrib package, and where otelhttp is headed next.

Guests: Sonal Gaud (https://www.linkedin.com/in/sonal-gaud/, https://github.com/sonalgaud12)
Hosts: Imma Valls (https://www.linkedin.com/in/imma-valls/)

Join the conversation, bring your questions, and learn how this project evolves with contributions from across the community.

#opentelemetry #golang #http #grafana #observability

## Pre-show checklist

- [x] Create a new `.md` file and copy this template into it. Check things off as you work through it.
- [x] Update [Grafana OTel Community Call Readme](/projects/Grafana%20OTel%20Community%20Call.md) to add this file to the table.
- [ ] Contact Sonal about the show (internal — just a Slack ping, not a cold outreach).
- [ ] Date/time already agreed with Sonal: September 28th 2026, 14:00 CEST. Double check [the Monday board](https://grafana-labs.monday.com/boards/5724430500) to avoid clashing with another livestream.
- [ ] Confirm the time with Sonal (1.5 hours total: 15 min tech check + 1hr stream + 15 min debrief).
- [ ] Send the calendar invite ("this instance only").
- [ ] Create a thumbnail on Canva using the standard format; check on thumbsup.tv.
- [ ] Schedule the broadcast on Streamyard → Grafana YouTube channel.
  - [ ] Title: Becoming a Codeowner: Inside OpenTelemetry's otelhttp (Grafana ❤️‍🔥 OTel Community Call #10)
  - [ ] Add standard description + guest's contact/social links.
- [ ] Get the Streamyard invite link into the calendar invite location field.
- [ ] Announce on the Grafana Meetup page and the Luma Grafana & Friends calendar.
- [ ] Slack: `#opentelemetry`, `#community-champions` (internal); public Grafana Slack `#opentelemetry` + events.
- [ ] Add to the monthly Community Calendar forum thread (community.grafana.com) and Google Calendar.
- [ ] Create a community forum thread for the episode (same pattern as past ones, e.g. the GenAI apps thread).
- [ ] Ask Sonal if she wants to do a live demo (otelhttp or otherwise), and if so, do a quick screen-share check beforehand.
- [ ] Confirm whether Sonal's IndiaFOSS talk ("How OTel instrumentation works under the hood") lands on/around the same day — mention it briefly, don't cross-promote if it's not out yet.

Reference links to gather ahead of time:

- https://github.com/open-telemetry/opentelemetry-go-contrib/tree/main/instrumentation/net/http/otelhttp
- https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp
- https://github.com/open-telemetry/opentelemetry-go-contrib/blob/main/CODEOWNERS
- https://github.com/open-telemetry/opentelemetry-go-contrib/pull/8831 (PR adding Sonal as otelhttp codeowner)
- https://github.com/open-telemetry/opentelemetry-go-contrib/pull/8688 (Labeler redesign — scoped context keys, function-based API)
- https://github.com/open-telemetry/opentelemetry-go-contrib/pull/8587 (deprecating `WithMetricAttributesFn` in favor of `Labeler`)
- https://github.com/open-telemetry/opentelemetry-go-contrib/pull/8801 (recording `error.type` metric on transport failures)
- https://github.com/open-telemetry/opentelemetry-go-contrib/pull/8885 (otelconf cardinality limits support)
- https://opentelemetry.io/docs/specs/semconv/http/ (HTTP semantic conventions)
- https://www.linkedin.com/in/sonal-gaud/
- https://github.com/sonalgaud12
- https://fossunited.org/c/indiafoss/2026/cfp/9i6peimmer (Sonal's IndiaFOSS talk: "How OTel instrumentation works under the hood")

## Talking points

> Bullet points, not a script — keep it casual.

- Intro
  - *Hello and welcome to Grafana OTel Community Call. I'm `<name>`, a `<position>` at Grafana Labs, and today we're talking with the codeowner of otelhttp about how Go's most-used HTTP instrumentation library actually works, and what it took to get there.*
- Introduce guest: Sonal Gaud
  - Who are you, and what do you do day to day?
  - How did you first get into OpenTelemetry / Go?
- The journey to codeowner
  - Her early PRs were test-coverage work (e.g. tests for `zpages`, `xray` propagator) — how did that lead to bigger things?
  - The turning point: deprecating `WithMetricAttributesFn` in favor of `Labeler` (#8587) — a real API redesign, not just a fix
  - Becoming codeowner in April 2026 (#8831) — how does one become a codeowner in go-contrib? What's the bar?
  - What surprised her most about stepping into a maintainer role
  - Advice for someone hoping to go from "occasional contributor" to "codeowner"
- otelhttp under the hood
  - What otelhttp actually instruments: `Transport` (client) vs `Handler` (server)
  - Context propagation — how trace context flows through `http.RoundTripper` / middleware
  - Metrics & the `Labeler` — how custom attributes get attached without blowing up cardinality
  - Route/path cardinality pitfalls in production — what goes wrong when people don't set `WithRouteTag` (or similar) correctly
  - Live demo? (open to whatever Sonal wants to show — could be otelhttp, could be something else)
- Semantic conventions & evolution
  - The `error.type` metric attribute work (#8801) — why HTTP semconv keeps evolving, and what that means for a stable library
  - How otelhttp balances shipping semconv changes with not breaking existing users
- PR review & backwards compatibility in go-contrib
  - What she looks for when reviewing a PR to otelhttp
  - Deprecation as a pattern (not deletion) — how the project keeps compatibility promises
  - Working with other approvers/codeowners — how decisions get made when people disagree
- Where otelhttp is headed
  - The open `Labeler` redesign (#8688) — scoped context keys, function-based API — what problem does this solve?
  - What's on the roadmap for otelhttp / semconv alignment
  - How semconv, go-contrib, and other language SIGs coordinate on HTTP instrumentation
- Mention: Sonal's upcoming IndiaFOSS talk, "How OTel instrumentation works under the hood" — quick plug if timing allows
- The human side
  - Favorite "aha" moment maintaining otelhttp
  - What keeps her motivated to keep contributing
- Outro
  - Where should people go to start contributing to otelhttp?

### Just before the show

> Here are some points to discuss with the guest in the 15 minutes before the stream begins.

- [ ] How do you pronounce your name?
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
- [ ] Consider repurposing into shorts (e.g., "what is otelhttp in 60 seconds", "how to become an OTel codeowner").
- [ ] Update the Advocate Contributions sheet.
- [ ] Promote on Grafana socials (X, Bluesky, LinkedIn).

### Timestamps

00:00:00 Introductions
