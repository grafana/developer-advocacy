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
- Announcements
	- New project releases
	- Café con Grafana 000 yesterday: https://youtube.com/live/Kdgu2gutp7o
	- [ObservabilityCON 2023](https://grafana.com/about/events/observabilitycon/2023/?pg=blog&plcmt=body-txt#register) is sold out, but there's a waitlist and you can also stream the keynote live.
	- Sign up for the Grafana Cloud newsletter - October version is coming out soon
		- GOH 04 - Private Datasource Connect
		- [GOH 15 - Agentless monitoring for Prometheus in Grafana Cloud](GOH%2015%20-%20Agentless%20monitoring%20for%20Prometheus%20in%20Grafana%20Cloud.md)
		- Grafana Agent - Feature parity between static and flow mode, easier migration
- Introduce Paschalis
	- Who are you?
	- What do you do?
	- How long have you been working at Grafana?
	- How long have you been working on Grafana Agent?
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
	- For the sake of completeness, what are other telemetry collectors that are available?
		- Many that cater to one or two types of telemetry (example: Jaeger for tracing, FluentD/FluentBit for logs, Telegraf for metrics)
		- OTel Collector (aims to be for metrics, traces, logs). How does this differ from Grafana Agent?
- How do you get started with Grafana Agent?
	- Flow mode vs static mode (high level only - Matt will cover this in a future episode)
		- Just hit feature parity
	- Installation options
		- Static mode: Docker, Kubernetes, choose your operating system, standalone binary
		- Static mode Kubernetes operator (Helm chart: https://grafana.github.io/helm-charts, `grafana-agent-operator`)
		- Flow mode
- How does Grafana Agent scale?
- Metrics Endpoint integration for Grafana Cloud ("agentless" integration)
	- In what cases is the agentless integration not enough? When would you still need Grafana Agent?
		- When you need more than just Prometheus metrics
		- Private systems where endpoints can't be exposed
		- Transforming or filtering out metrics
		- Changing routing
- Recent changes in Grafana Agent
	- Continuous profiling support via Pyroscope
- Future of Grafana Agent
	- Become an OTel Collector itself - what does this mean?
	- Ability to convert one type of signal to another (Prometheus to Loki for example)
	- Auto-instrumentation?
- Outro
	- If people want to learn more about this topic, where should they go?
	- Next week: frontend observability with Grafana Faro

### Just before the show

> Here are some points to discuss with the guest in the 15 minutes before the stream begins.

- [ ] How do you pronounce your name?
- [ ] What are your pronouns?
- [ ] We will be using the talking points, but we don't have to be strict about it. We don't have to go through all of them, or follow a specific order. They're only there to make us comfortable.
- [ ] Does anyone want to share their screen? We can do that now, and I can show you how that works
- [ ] We'll be streaming to YouTube.
- [ ] You'll be able to see comments, but if you have links, I have to paste it into the private chat.
- [ ] You can also use the private chat if you need to say something, but you can also just say it out loud.
- [ ] If at any point you aren't comfortable talking about something, please either say so or let me know in the private chat, and I'll pivot away from that topic.
- [ ] Afterwards, we'll say goodbye to the stream, but please stay on past that so we can debrief.
- [ ] Just in case I disconnect... stall for a minute and I'll be right back.

## After the show

- [ ] Add timestamps to the video (at least four).
- [ ] Add any links shared to the description of the video.
- [ ] Add the video to video playlists that make sense (at the very least, the "Grafana Office Hours" one.)