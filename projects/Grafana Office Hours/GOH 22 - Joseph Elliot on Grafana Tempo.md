---
url: https://youtube.com/live/zDrA7Ly3ovU
date: 2023-12-01
---
# [[GOH 22 - Joseph Elliot on Grafana Tempo]]

<iframe width="560" height="315" src="https://www.youtube.com/embed/" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Guest:: Joseph (Joe) Elliot

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
- [x] Schedule a tweet just when the show begins to say "We're live now!"
- [x] Schedule a Slack message on the internal Grafana workspace (in `#community`).
- [x] Schedule a Slack message on the public Grafana Slack workspace (in `#announcements`)


## References

```
Contact Joe:
LinkedIn: https://www.linkedin.com/in/joe-elliott-5a9911b1/
GitHub: https://github.com/joe-elliott
Site: http://www.inkedgames.com/
```

Getting started with Tempo (video): https://www.youtube.com/watch?v=pUAmL28uzos
Grafana Tempo repo: https://github.com/grafana/tempo
Grafana Tempo docs: https://grafana.com/docs/tempo/latest/getting-started/
The Tempo category on the Grafana community forum: https://community.grafana.com/c/grafana-tempo/40
Video playlist for Grafana Tempo: https://www.youtube.com/playlist?list=PLDGkOdUX1UjrA4D1MRdAzUgEGp5UXvW3z
Distributed tracing with Grafana Cloud k6 (Grafana Office Hours video): https://www.youtube.com/watch?v=petbezEmIw4

## Talking points

> Enumerate talking points for the show. It's better to keep these as bullet points to encourage a more casual, rather than scripted, conversation.

- Intro
	- *Hello and welcome to Grafana Office Hours. I'm `<name>`, a `<position>` at Grafana Labs and today, we're going to talk about `<topic>`.*
- Announcements
	- Lisa's video on *Grafana, Observability, & DevOps*: https://youtu.be/4-z1-eEHhvs
	- Café con Grafana yesterday with Raúl Marin (in spanish): https://www.youtube.com/watch?v=irUr96JV-Sg
- Introduce guest: Joe Elliot
	- Who are you?
	- What do you do?
	- How long have you been using Grafana/other project?
- What is distributed tracing?
	- Basic tracing concepts
		- Define: trace, span, context propagation
		- How does tracing work?
	- Why should we do distributed tracing?
	- How is it different from metrics and logs?
		- What don't metrics and logs cover that traces do?
			- Metrics: good for aggregations, bad for fine-grained information
			- Logs: good for revealing what happened sequentially in one application or across applications, but bad at showing how a single request behaves inside a service
		- Known problems vs. issues with unknown causes
	- How is it different from continuous profiling?
		- Tracing is done at a high level but about one specific transaction
		- Continuous profiling is sampled over time, aggregated over many transactions
	- The more distributed an application is, the more unpredictable its failure modes become.
	- What does tracing have to do with OpenTelemetry?
	- What is instrumentation? Why do applications need to be instrumented?
- What is Tempo?
	- History of Tempo
		- Goal: Sample 100% of read path, scale Cassandra and Elastic
	- How is Tempo different from other tracing backends? (Key features)
		- scalability
		- integration with other tools in the Grafana Labs stack
	- What is TraceQL?
- Walk us through it: we have an application. How do we start seeing traces with Tempo? (demo?)
	- Client instrumentation (automatic or manual)
	- (Optional) Set up tracing pipeline (ex: Agent)
	- Deploy and configure Tempo: Docker Compose, Helm, Tanka
	- Visualize (ex: Grafana)
	- Alerting
- Best practices for setting up distributed tracing
- Relationship between distributed tracing and performance testing
	- Grafana Cloud k6 Tempo integration
- Outro
	- If people want to learn more about this topic, where should they go?
	- Grafana Office Hours next week: [GOH 23 - Juraci Paixāo Kröhling on OpenTelemetry](GOH%2023%20-%20Juraci%20Paixāo%20Kröhling%20on%20OpenTelemetry.md)
	- 

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