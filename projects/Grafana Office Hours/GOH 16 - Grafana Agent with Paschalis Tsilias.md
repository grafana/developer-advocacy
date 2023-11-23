---
url: https://youtube.com/live/i0mA0w_MCPQ
date:
---
# [[GOH 16 - Grafana Agent with Paschalis Tsilias]]

<iframe width="560" height="315" src="https://www.youtube.com/embed/" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Guest:: Paschalis Tsilias

## Checklist

- [x] Contact the guest and tell them about Office Hours.
	> At Grafana Labs, we do a weekly livestream called [Grafana Office Hours](https://www.youtube.com/watch?v=uk7NoagbJ28&list=PLDGkOdUX1Ujrrse-cdj20RRah9hyHdxBu), where we have guests on to talk about how to use Grafana, observability, or visualization. I saw your [blog post/video/post] on [source] and I think it would be great to have you on the show to share your experience about [topic].
	Office Hours is an hour-long live conversation that is streamed to the [Grafana YouTube channel](https://youtube.com/@grafana). It's very casual, and you can also share your screen if you'd like to do a demo (not required). If you'd like to join, I'd love to have you! 
- [x] If the guest agrees, choose a date for the Office Hours session. Confirm the time: 13:00 UTC (15:00 CEST) on Friday. Ask them for a photo you can use for promotion, or ask for permission to use their profile pic on social media.
- [x] Invite them to the Grafana Office Hours calendar invite (choose "this instance only", not the whole series). Change the invite to include the episode number and their name, ie `Grafana Office Hours #01 with Mitch`. This is to save the date. Schedule the invite for 15 minutes before the stream (to do a tech check) until 15 minutes after the stream (to debrief). The invite should be for 1.5 hours.
- [x] Create a thumbnail on [Canva](https://canva.com) using the Grafana Office Hours thumbnail format. Use [thumbsup.tv](https://thumbsup.tv) to check how the thumbnail looks on different devices.
- [x] Schedule the broadcast on [Streamyard](https://streamyard.com), and select the Grafana YouTube channel as the destination.
	- [x] In the title, include the instance of Office Hours, i.e. `What's new in Grafana 10? (Grafana Office Hours #01)`.
	- [x] Add the standard description as per previous Grafana Office Hours shows. Check the video description and add guests' contact details.
- [x] Get the Streamyard invite link and put it in the "location" of the calendar invite to the guest.
- [x] Get the YouTube link to the show. Put the link on this page, in the URL property above.
- [x] Create an event and announce it [on the Grafana Meetup page](https://www.meetup.com/grafana-friends-virtual-meetup-group/).
- [ ] Schedule a tweet just when the show begins to say "We're live now!"
- [x] Schedule a Slack message on the internal Grafana workspace (in `#community`).
- [x] Schedule a Slack message on the public Grafana Slack workspace (in `#announcements`)


## Talking points

> Enumerate talking points for the show. It's better to keep these as bullet points to encourage a more casual, rather than scripted, conversation.

- Intro
- Introduce Paschalis
	- Who are you?
	- What do you do?
	- How long have you been working at Grafana?
	- How long have you been working on Grafana Agent?
- Announcements
	- Café con Grafana 000 yesterday: https://youtube.com/live/Kdgu2gutp7o
	- [ObservabilityCON 2023](https://grafana.com/about/events/observabilitycon/2023/?pg=blog&plcmt=body-txt#register) is sold out, but there's a waitlist and you can also stream the keynote live.
	- Sign up for the Grafana Cloud newsletter - October version is coming out soon
		- GOH 04 - Private Datasource Connect
		- [GOH 15 - Agentless monitoring for Prometheus in Grafana Cloud](GOH%2015%20-%20Agentless%20monitoring%20for%20Prometheus%20in%20Grafana%20Cloud.md)
		- Grafana Agent - Feature parity between static and flow mode, easier migration
- What is Grafana Agent?
	- vendor neutral telemetry collector
	- What's telemetry?: metrics, logs, traces, profiles
		- What kind of signals does Agent collect?
			- Prometheus
			- OpenTelemetry
			- Loki, Grafana, Tempo, Mimir, Pyroscope
	- What is a telemetry collector?
	- Why do you need telemetry collectors?
	- "batteries included": what does this mean
		- bundles in Prometheus exporters so you don't have to do it yourself. Prometheus metrics are exposed
	- For the sake of completeness, what are other telemetry collectors that are available?
		- Many that cater to one or two types of telemetry (example: Jaeger for tracing, FluentD/FluentBit for logs, Telegraf for metrics)
		- OTel Collector (aims to be for metrics, traces, logs). How does this differ from Grafana Agent?
	- If you couldn't use Grafana Agent, what would you do?
		- Instrument application to send telemetry directly
		- Use OTel collector or something else
- How do you get started with Grafana Agent?
	- Flow mode vs static mode (high level only - Matt will cover this in a future episode)
		- Flow is a rebuild of Grafana Agent - more modular, reusable components that can be reused in pipelines, connected by expressions.
			- What controls this pipeline?
				- Each component has a set of arguments that dictate what it should do and also outputs that other components can reference.
				- Flow dynamically reevaluation of all the components so that if one thing changes, all downstream components change as well.
		- Inspired by HCL (language called River)
		- Just hit feature parity
		- Example of where flow mode shines: send from promtail to Kafka topic
			- Take promtail logs, convert them, and then send them to Kafka using an exporter
		- Flow also has cluster mode which is awesome
	- Installation options
		- Static mode: Docker, Kubernetes, choose your operating system, standalone binary
		- Static mode Kubernetes operator (Helm chart: https://grafana.github.io/helm-charts, `grafana-agent-operator`)
		- Flow mode
			- Paschalis recommends doing this
- How does Grafana Agent scale?
	- Either Grafana Agent cluster mode: https://grafana.com/docs/agent/latest/flow/concepts/clustering/
	- or hashmod sharding (same as Prometheus)
- Performance
	- They haven't reinvented the wheel - they use battle-tested techniques from Prometheus and OTel Collector
	- dogfooding
- Metrics Endpoint integration for Grafana Cloud ("agentless" integration)
	- In what cases is the agentless integration not enough? When would you still need Grafana Agent?
		- When you need more than just Prometheus metrics
		- Private systems where endpoints can't be exposed
		- Transforming or filtering out metrics
		- Changing routing
- Recent changes in Grafana Agent
	- flow mode feature parity
	- Continuous profiling support via Pyroscope
		- eBPF-based profiling
- Future of Grafana Agent
	- Get people to use Flow and not static
	- better UI, better scaling,
	- play even better with OTel ecosystem
		- Become an OTel Collector itself - what does this mean?
			- distribution of OTel Collector - like a flavour. Be a drop-in replacement for OTel collector.
	- Ability to convert one type of signal to another (Prometheus to Loki for example) - some OTel collectors already do this
	- Auto-instrumentation?
- Outro
	- If people want to learn more about this topic, where should they go?
	- Next week: frontend observability with Grafana Faro

### Just before the show

> Here are some points to discuss with the guest in the 15 minutes before the stream begins.

- [x] How do you pronounce your name?
- [ ] What are your pronouns?
- [ ] We will be using the talking points, but we don't have to be strict about it. We don't have to go through all of them, or follow a specific order. They're only there to make us comfortable.
- [x] Does anyone want to share their screen? We can do that now, and I can show you how that works
- [x] We'll be streaming to YouTube.
- [x] You'll be able to see comments, but if you have links, I have to paste it into the private chat.
- [x] You can also use the private chat if you need to say something, but you can also just say it out loud.
- [ ] If at any point you aren't comfortable talking about something, please either say so or let me know in the private chat, and I'll pivot away from that topic.
- [x] Afterwards, we'll say goodbye to the stream, but please stay on past that so we can debrief.
- [ ] Just in case I disconnect... stall for a minute and I'll be right back.

## After the show

- [ ] Add timestamps to the video (at least four).
- [ ] Add any links shared to the description of the video.
- [ ] Add the video to video playlists that make sense (at the very least, the "Grafana Office Hours" one.)


## Timestamps

00:00:00 Introductions and announcements
00:04:04 What is Grafana Agent?
00:07:20 What is a telemetry collector?
00:09:53 Question: Is Agent a specialized version of the OTel collector?
00:11:54 Difference between Agent and other telemetry collectors
00:16:08 Alternatives to using Agent
00:18:53 Question: How can you forward messages from Promtail logs to Kafka?
00:21:39 Flow mode vs. static mode - what's the difference?
00:28:40 Directed Acyclic Graph of components from Agent
00:34:09 Installation options for Grafana Agent
00:35:49 Question: When will the cluster mode for Grafana Agent be production ready?
00:37:54 Other options to scale Grafana Agent horizontally
00:39:36 How to get the DAG UI from Agent
00:41:56 Performance considerations for Grafana Agent
00:43:16 Metrics Endpoint on Grafana Cloud vs. local Grafana Agent
00:47:17 Continuous profiling support via Pyroscope in Grafana Agent
00:50:10 The future of Grafana Agent
00:55:04 Five-minute summary of everything in this episode
