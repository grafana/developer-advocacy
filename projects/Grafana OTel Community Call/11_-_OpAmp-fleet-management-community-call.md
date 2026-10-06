---
url:
date: TBD
---

# [[11 - OpAMP and Fleet Management]]

Link to YouTube video: TBD

Guests:: [Bejal Lewis](https://www.linkedin.com/in/bejal-lewis/), [Paschalis Tsilias](https://www.linkedin.com/in/tsilias/)

**Title:** Managing Collectors at Scale: OpAMP and Fleet Management (Grafana ❤️‍🔥 OpenTelemetry Community Call #11)

**Description:**

In this episode of the Grafana OTel Community Call, we're joined by Bejal Lewis and Paschalis Tsilias from Grafana Labs to talk about OpAMP, the Open Agent Management Protocol, and what it takes to manage OpenTelemetry Collectors at scale. We'll cover what OpAMP is and why fleet management matters, where the spec stands today (it's still pre-release), and what it was like building production tooling on top of it.

We'll also look at what went into adding the OpAMP extension to Grafana Alloy's OTel Engine, what "GA" means for Grafana Fleet Management versus the maturity of the upstream spec, and where OpAMP is headed next.

Guests:
- Bejal Lewis (https://www.linkedin.com/in/bejal-lewis/)
- Paschalis Tsilias (https://www.linkedin.com/in/tsilias/)
Hosts:
- Imma Valls (https://www.linkedin.com/in/imma-valls/)

Join the conversation, bring your questions, and learn how OpenTelemetry evolves with contributions from across the community.

#opentelemetry #opamp #collector #grafana #observability

## Pre-show checklist

- [x] Create a new `.md` file and copy this template into it. Check things off as you work through it.
- [x] Update [Grafana OTel Community Call Readme](README.md) to add this file to the table.
- [ ] Contact Paschalis and Bejal about the show.
- [ ] Choose a date/time with both guests (date is TBD). Check [the Monday board](https://grafana-labs.monday.com/boards/5724430500) to avoid clashing with another livestream.
- [ ] Confirm the time with the guests (1.5 hours total: 15 min tech check + 1hr stream + 15 min debrief).
- [ ] Create a thumbnail on Canva using the standard format; check on thumbsup.tv.
- [ ] Schedule the broadcast on Streamyard → Grafana YouTube channel.
  - [ ] Title: "Managing Collectors at Scale: OpAMP and Fleet Management (Grafana ❤️‍🔥 OpenTelemetry Community Call #11)"
  - [ ] Add standard description + guests' contact/social links.
- [ ] Send the calendar invite ("this instance only").
- [ ] Get the Streamyard invite link into the calendar invite location field.
- [ ] Announce on the Grafana Meetup page and the Luma Grafana & Friends calendar.
- [ ] Slack: `#opentelemetry`, `#community-champions` (internal); public Grafana Slack `#opentelemetry` + events.
- [ ] Add to the monthly Community Calendar forum thread (community.grafana.com) and Google Calendar.
- [ ] Create a community forum thread for the episode (same pattern as past ones).
- [ ] Ask the guests if they want to do a live demo (e.g. onboarding a collector in Fleet Management and rolling out a config with attribute matchers), and if so, do a quick screen-share check beforehand.
- [ ] Get the LinkedIn profile URLs for Paschalis and Bejal and add them above and to the README.
- [ ] Re-check the latest opamp-spec release the day before the call (v0.20.0, Aug 12 2026, as of Oct 6 2026).
- [ ] Confirm with the Fleet Management team what can be said publicly: the collector scale numbers (see below) and anything about the Alloy-native OpAMP solution.
- [ ] Optional: ask if an upstream OpAMP maintainer or approver (not from Grafana) would like to join for a short segment or Q&A.

Reference links to gather ahead of time:

- https://grafana.com/whats-new/2026-07-08-remote-management-of-opentelemetry-collectors-is-generally-available/ (Fleet Management GA announcement, July 8 2026)
- https://github.com/open-telemetry/opamp-spec (OpAMP spec)
- https://github.com/open-telemetry/opamp-spec/releases (releases; latest checked: v0.20.0, Aug 12 2026, prerelease)
- https://github.com/open-telemetry/opamp-go (Go implementation)
- https://github.com/grafana/alloy/pull/6632 (Add OpAMP Extension to OTel Engine, merged July 3 2026)
- https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/opampextension (opampextension)
- Link to the Grafana Fleet Management docs (TODO)
- Guests' LinkedIn profiles (TODO)

## Talking points

> Tentative bullet points, not a script. Keep it casual and adjust with the guests. Items marked **[VERIFY]** need confirming with them first.

- Intro
  - *Hello and welcome to Grafana OTel Community Call. I'm `<name>`, a `<position>` at Grafana Labs, and today we're talking about OpAMP and managing OpenTelemetry Collectors at scale.*
- Introduce guests: Paschalis Tsilias and Bejal Lewis
  - Who are you, and what do you work on day to day?
  - How did you each end up working on OpAMP / fleet management?
- What is OpAMP and why does it matter?
  - The problem at scale: config drift, no visibility into which collectors are healthy, risky manual rollouts
  - What OpAMP is: a vendor-agnostic protocol for agents to report status, receive remote config and receive package updates
  - Why a supervisor process manages the Collector, rather than the Collector managing itself
  - Mixed fleets: one place to manage Alloy and upstream Collectors
- The spec today (Paschalis)
  - Still pre-release: latest is v0.20.0 (Aug 2026), five prereleases since Feb 2026
  - Recent changes worth mentioning **[VERIFY which matter to Fleet Management]**: duplicate `instance_uid` detection (v0.17), transport message size limits and `ComponentHealth.attributes` (v0.19), config map semantics ("file" renamed to "object") (v0.20)
  - What contributing upstream looks like: opamp-spec and opamp-go, who maintains and approves, how to get a proposal accepted
  - What's working well in the spec, and what's still hard or unsolved **[Paschalis to bring the concrete list]**
- Building on a pre-release spec
  - How do you ship something production-grade on a spec that can still change? **[VERIFY how compatibility is handled, don't claim practices that aren't real]**
  - Where the project and the spec disagree, or the spec is silent
- Adding OpAMP to Alloy's OTel Engine (Bejal)
  - Why #6632 was needed and how it relates to the OpAMP supervisor
  - What it took to integrate `opampextension` from collector-contrib, testing and edge cases **[Bejal to bring specifics]**
  - What users can do now: manage Alloy and upstream Collectors from one place
  - What Bejal would do differently
- What does "GA" mean here?
  - Grafana Fleet Management GA (July 8 2026): health monitoring, centralized configuration, attribute matchers for targeted rollouts, standard OTel YAML pipelines
  - Product GA is not spec stability. How do we talk about that honestly with users?
  - Scale: Fleet Management is managing roughly 500k concurrent collectors, up from about 150k on Jan 1 2026 **[VERIFY: not in the GA announcement, confirm the numbers and approved wording]**
  - What's working well in production, and the known rough edges
- Where is it headed?
  - The built-in / Alloy-native OpAMP solution that #6632 is a prerequisite for **[VERIFY what can be said publicly]**
  - What Grafana would like to see upstream
  - How people can contribute: spec issues, opamp-go, testing against real fleets
- Community questions to seed the discussion
  - What would make you comfortable adopting OpAMP in production while the spec is pre-release?
  - What do you need from fleet management that the spec doesn't cover yet (auth, rollout strategies, rollback, non-Collector agents)?
  - How do you manage collector config today (GitOps, Ansible, Helm, custom control plane), and what would it take to move to OpAMP?
- Outro
  - Where should people go to get started with OpAMP and to contribute?

### Just before the show

> Here are some points to discuss with the guests in the 15 minutes before the stream begins.

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
- [ ] Consider repurposing into shorts (e.g., "what is OpAMP in 60 seconds", "what does GA mean on a pre-release spec").
- [ ] Update the Advocate Contributions sheet.
- [ ] Promote on Grafana socials (X, Bluesky, LinkedIn).
- [ ] Update the README table with the date and YouTube link.

### Timestamps

00:00:00 Introductions
