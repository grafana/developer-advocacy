---
url:
date: 
---
# [[GOH 14 - Distributed tracing with Grafana Cloud k6]]

<iframe width="560" height="315" src="https://www.youtube.com/embed/" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Guest:: [[Łukasz Gut]]

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
- [ ] Schedule a Slack message on the internal Grafana workspace (in `#community`).
- [ ] Schedule a Slack message on the public Grafana Slack workspace (in `#announcements`)


## Talking points

> Enumerate talking points for the show. It's better to keep these as bullet points to encourage a more casual, rather than scripted, conversation.

- ObsCON
- Introduce Łukasz
	- Who are you?
	- What do you do?
	- How long have you been using Grafana/other project?
- What is distributed tracing?
	- What is a trace?
	- Terminology: span, header, propagator, exporter
	- What do traces give us that logs and metrics don't?
	- Why is distributed tracing particularly useful for microservices-based architectures?
- What is Tempo?
- What is Distributed Tracing with Grafana Cloud k6? (Demo)
	- History
		- this started as a hackathon project after we joined Grafana
		- CrocoSpans, now Insights
		- xk6-distributed tracing vs k6-tracing
		- What is the lay of the land in tracing? What other tools existed? What was missing?
	- How does it work?
		- Show diagram [here](https://docs.google.com/presentation/d/1rC8kifF6X1ZSH8jgh-yUp6NfgK_UaLiOG8TWLa5dQBQ/edit#slide=id.g21da9c1008c_0_932) and ask Łukasz if that's still accurate
	- What do you have to do to make it work?
		- Instrumentation (w3c, jaeger, b4, ot)
		- Modify k6 script
		- Run test
	- Using it on Grafana Cloud k6 + using it without Grafana Cloud-- what's free and not free?
- Why is this cool?
	- Black box testing and its limitations
	- What are the advantages of having a testing tool that can instrument headers?
	- What does testing have to do with observability?
	- Who is this for? (Testers/developers/devops?)
- What are some gotchas?
	- Is Tempo performant enough to be able to handle thousands of requests that might occur in a load test?
	- Should every test have Traces enabled?
- What are some plans for the future of Insights?
	- Can requests through k6 browser be instrumented as well?
- Outro
	- How can people use this today?
	- If people want to learn more about this topic, where should they go?
	- Next week: agentless monitoring for Prometheus in Grafana Cloud, with one of the engineers who worked on that feature, Matt Nolf

### Just before the show

> Here are some points to discuss with the guest in the 15 minutes before the stream begins.

- [ ] How do you pronounce your name?
- [ ] What are your pronouns?
- [ ] We will be using the talking points, but we don't have to be strict about it. We don't have to go through all of them, or follow a specific order. They're only there to make us comfortable.
- [x] Does anyone want to share their screen? We can do that now, and I can show you how that works
- [ ] We'll be streaming to YouTube.
- [ ] You'll be able to see comments, but if you have links, I have to paste it into the private chat.
- [ ] You can also use the private chat if you need to say something, but you can also just say it out loud.
- [ ] If at any point you aren't comfortable talking about something, please either say so or let me know in the private chat, and I'll pivot away from that topic.
- [ ] Afterwards, we'll say goodbye to the stream, but please stay on past that so we can debrief.
- [ ] Just in case I disconnect... stall for a minute and I'll be right back.

## After the show

- [x] Add timestamps to the video (at least four).
- [ ] Add any links shared to the description of the video.
- [ ] Add the video to video playlists that make sense (at the very least, the "Grafana Office Hours" one.)


## Links

Quick video on distributed tracing: https://www.youtube.com/watch?v=62ci4xi39Rw
The k6 and Tempo integration (k6 Office Hours): https://www.youtube.com/watch?v=g9xU_pFr-Vc
More on distributed tracing for testing using Tracetest (Grafana Office Hours): https://www.youtube.com/watch?v=oJ0wdneD8Po
Docs https://grafana.com/docs/grafana-cloud/k6/analyze-results/integration-with-grafana-cloud-traces
Blog: https://grafana.com/blog/2023/09/19/troubleshoot-failed-performance-tests-faster-with-distributed-tracing-in-grafana-cloud-k6/