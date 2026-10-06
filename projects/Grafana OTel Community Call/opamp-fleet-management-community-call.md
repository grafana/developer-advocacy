# Grafana OpenTelemetry Community Call: OpAMP & Fleet Management

> DRAFT. Items marked **[VERIFY]** need confirmation before publishing.

## 1. Title

**Managing Collectors at Scale: OpAMP, Fleet Management, and Building on a Pre-1.0 Spec**

Alternates:
- OpAMP in Production: What Works, What's Missing, What's Next
- "GA" on a Pre-Release Spec: Lessons from Running OpAMP at Scale

## 2. Public description

Managing a handful of OpenTelemetry Collectors is easy. Managing thousands is a different problem. OpAMP, the Open Agent Management Protocol, is the vendor-neutral answer, but the spec is still pre-release (v0.20.0 at the time of writing). In this community call, two Grafana Labs engineers walk through what it took to ship remote management for upstream OTel Collectors and Grafana Alloy on top of OpAMP, what we learned running it in production, and where the spec still has gaps. Bring your questions, war stories, and opinions on where OpAMP should go next.

## 3. Speakers

**Paschalis Tsilias**, Principal Software Engineer, Grafana Labs (Greece)
Paschalis works on Grafana's Fleet Management team and contributes upstream to open-telemetry/opamp-spec and open-telemetry/opamp-go, where they are among the top contributors. They also registered Grafana Labs as an OpenTelemetry vendor/distributor on opentelemetry.io. Paschalis brings the upstream and spec perspective.

**Bejal Lewis**, Staff Software Engineer, Grafana Labs (Berlin, Germany)
Bejal works on Grafana Alloy and authored the change that added the OpAMP extension to Alloy's OpenTelemetry Engine (grafana/alloy#6632). That work lets users manage Alloy and upstream Collector distributions via the OpAMP supervisor. Bejal brings the hands-on implementation perspective.

**Host / moderator:** Imma Valls **[VERIFY: confirm hosts, add co-host/OTel community guest if any]**

*Suggestion:* invite an upstream OpAMP maintainer or approver (non-Grafana) for a short segment or as a Q&A panelist. It strengthens the community-first framing, but they must opt in.

## 4. Agenda (60 min)

| Time | Section | Lead |
|---|---|---|
| 0:00–0:05 | Welcome & framing | Host |
| 0:05–0:15 | OpAMP 101: why fleet management matters | Paschalis |
| 0:15–0:27 | The spec today: state, process, and gaps | Paschalis |
| 0:27–0:40 | Building and shipping on OpAMP | Bejal |
| 0:40–0:47 | What GA means (and doesn't) | Both |
| 0:47–0:52 | What's next | Both |
| 0:52–1:00 | Community Q&A | Host |

### 0:00–0:05 Welcome & framing
- Introduce speakers and the format: community call, not a product demo.
- State the goal: share what's built, where the spec is heading, and hear from the community.
- Quick poll or chat prompt: who is running more than 10 / 100 / 1000 collectors?
- Point to the upstream repos and the #otel-opamp channel for follow-up **[VERIFY channel name]**.

### 0:05–0:15 OpAMP 101: why fleet management matters
- The problem: config drift, no visibility into which collectors are healthy, and risky manual rollouts once a fleet grows.
- What OpAMP is: a vendor-agnostic protocol for agents to report status, receive remote config, and receive package updates.
- The value of a single pane of glass across mixed fleets, not just one vendor's agents.
- The supervisor model: why a separate process manages the Collector rather than the Collector managing itself.
- Where OpAMP sits relative to what people do today (config management tools, GitOps, custom control planes).

### 0:15–0:27 The spec today: state, process, and gaps
- Maturity: still pre-release (latest is v0.20.0, Aug 12 2026; 5 prereleases since Feb 2026: v0.16 to v0.20), so breaking changes remain possible.
- Recent spec movement worth discussing: v0.17 (duplicate `instance_uid` detection, default OpAMP port, HTTP routing through the Collector), v0.19 (transport message size limits, `ComponentHealth.attributes`, role support in agent config, proto folder restructure), v0.20 (config map semantics: "file" renamed to "object", empty keys allowed). **[VERIFY with Paschalis which of these matter in practice for Fleet Management]**
- Cadence: roughly one release every 1 to 3 months; ask how that affects compatibility pinning.
- How the spec and opamp-go evolve: who maintains and approves, and how contributors can get involved.
- Paschalis's experience contributing upstream: what the process is like, what a good proposal looks like.
- What's working well in the spec and what's still hard or unsolved. **[Paschalis to supply the concrete list; e.g. areas such as capabilities, auth, large-fleet behavior, if accurate]**
- The tension: shipping production tooling against a moving spec, and how to manage compatibility risk.

### 0:27–0:40 Building and shipping on OpAMP
- Why add the OpAMP extension to Alloy's OTel Engine (#6632), and how it relates to the OpAMP supervisor path.
- What it took in practice: integrating `opampextension` from collector-contrib, testing, and edge cases. **[Bejal to supply specifics]**
- What users can do now: manage Alloy and upstream Collectors from one place.
- Short demo or screenshot walk-through (optional, max 3 min): onboard a collector, push a config, use attribute matchers for a targeted rollout.
- Lessons learned and things Bejal would do differently.

### 0:40–0:47 What GA means (and doesn't)
- Grafana's GA: Fleet Management support for remote management of OTel Collectors is production-ready, with health monitoring, centralized config, and attribute matchers.
- Not the same as spec maturity: GA of a product feature does not make the OpAMP spec stable.
- How Grafana handles the gap: version pinning, compatibility testing, upstream engagement. **[VERIFY with speakers; don't claim practices that aren't real]**
- Scale signal: Fleet Management is managing roughly 500k concurrent collectors, up from about 150k on Jan 1 2026. **[VERIFY: not in the GA announcement; confirm figure and approved wording for public use]**
- What's working well in production, and honest limits or known rough edges.

### 0:47–0:52 What's next
- The Alloy-native/built-in OpAMP solution that #6632 was a prerequisite for. **[VERIFY what can be said publicly; keep to what's approved]**
- Upstream priorities Grafana would like to see in the spec.
- How community members can contribute: spec issues, opamp-go, testing against real fleets.

### 0:52–1:00 Community Q&A
Suggested seed questions if the room is quiet:
1. What would make you comfortable adopting OpAMP in production while the spec is pre-release? What's the blocker today?
2. What do you need from fleet management that today's OpAMP spec doesn't cover (auth models, rollout strategies, rollback, non-Collector agents)?
3. How do you manage collector config today (GitOps, Ansible, Helm, custom control plane), and what would it take to move to OpAMP?

## 5. Notes before publishing

- **Source check:** The GA page confirms GA, health monitoring, centralized config, attribute matchers, Alloy plus upstream Collector support, mixed fleets, standard OTel YAML pipelines, and the OpAMP supervisor. It does **not** include scale numbers or supervisor implementation details, so the ~500k/150k figures and any technical depth must come from you or the speakers.
- **Dates:** Your brief has #6632 merged July 3, 2026 and GA on July 8, 2026. Spec version checked against opamp-spec releases on Oct 6, 2026: latest is v0.20.0 (Aug 12, 2026, prerelease). The brief said v0.18.0, which is now two releases behind. Re-check the day before the call.
- **Internal details left out:** Engineering managers and squad names are intentionally not in the public bios.
- **Pronouns:** Bios avoid pronouns; add them if the speakers want.
- **Tone check:** Consider running the public description through brand review.
