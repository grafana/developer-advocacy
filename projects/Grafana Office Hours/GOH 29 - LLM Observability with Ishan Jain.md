---
url: https://www.youtube.com/watch?v=9X7M-bvnZG0
date: 2024-11-08
---
# [GOH 29 - LLM Observability with Ishan Jain](projects/Grafana%20Office%20Hours/GOH%2029%20-%20LLM%20Observability%20with%20Ishan%20Jain.md)

<iframe width="560" height="315" src="https://www.youtube.com/embed/9X7M-bvnZG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Guest:: "Ishan Jain"

## Checklist

- [ ] Contact the guest and tell them about Office Hours.
	> At Grafana Labs, we do a weekly livestream called [Grafana Office Hours](https://www.youtube.com/watch?v=uk7NoagbJ28&list=PLDGkOdUX1Ujrrse-cdj20RRah9hyHdxBu), where we have guests on to talk about how to use Grafana, observability, or visualization. I saw your [blog post/video/post] on [source] and I think it would be great to have you on the show to share your experience about [topic].
	Office Hours is an hour-long live conversation that is streamed to the [Grafana YouTube channel](https://youtube.com/@grafana). It's very casual, and you can also share your screen if you'd like to do a demo (not required). If you'd like to join, I'd love to have you! 
- [ ] If the guest agrees, choose a date for the Office Hours session. Confirm the time: 13:00 UTC (15:00 CEST) on Friday. Ask them for a photo you can use for promotion, or ask for permission to use their profile pic on social media.
- [ ] Invite them to the Grafana Office Hours calendar invite (choose "this instance only", not the whole series). Change the invite to include the episode number and their name, ie `Grafana Office Hours #01 with Mitch`. This is to save the date. Schedule the invite for 15 minutes before the stream (to do a tech check) until 15 minutes after the stream (to debrief). The invite should be for 1.5 hours.
- [ ] Create a thumbnail on [Canva](https://canva.com) using the Grafana Office Hours thumbnail format. Use [thumbsup.tv](https://thumbsup.tv) to check how the thumbnail looks on different devices.
- [ ] Schedule the broadcast on [Streamyard](https://streamyard.com), and select the Grafana YouTube channel as the destination.
	- [ ] In the title, include the instance of Office Hours, i.e. `What's new in Grafana 10? (Grafana Office Hours #01)`.
	- [ ] Add the standard description as per previous Grafana Office Hours shows. Check the video description and add guests' contact details.
- [ ] Get the Streamyard invite link and put it in the "location" of the calendar invite to the guest.
- [ ] Get the YouTube link to the show. Put the link on this page, in the URL property above.
- [ ] Create an event and announce it [on the Grafana Meetup page](https://www.meetup.com/grafana-friends-virtual-meetup-group/).
- [ ] Schedule posts on socials just when the show begins to say "We're live now!"
- [ ] Schedule a Slack message on the internal Grafana workspace (in `#community`).
- [ ] Schedule a Slack message on the public Grafana Slack workspace (in `#announcements`)

## Reference links


Ishan Jain on LLM observability with OpenTelemetry: 

(blog) A Guide to LLM Observability with OpenTelemetry: https://techstrong.ai/building-with-ai/a-guide-to-llm-observability-with-opentelemetry/
(blog) An Introduction to Observability for LLM-based applications using OpenTelemetry: https://opentelemetry.io/blog/2024/llm-observability/
(blog) A complete guide to LLM observability with OpenTelemetry and Grafana Cloud:  https://grafana.com/blog/2024/07/18/a-complete-guide-to-llm-observability-with-opentelemetry-and-grafana-cloud/
(docs) AI Observability: https://grafana.com/docs/grafana-cloud/monitor-applications/ai-observability/
(repo) OpenLit repository
(docs) OpenLit docs

## Timestamps



## Talking points

> Enumerate talking points for the show. It's better to keep these as bullet points to encourage a more casual, rather than scripted, conversation.

- Intro
	- *Hello and welcome to Grafana Office Hours. Artificial intelligence has gone very quickly from something out of sci-fi books to something quite commonplace that we use in various forms as part of our every day lives. Some of us might have even tried our hand at creating apps leveraging AI SDKs. Our guest today is going to talk about observability for AI: why we should do it, what to watch out for, and how exactly to set it up.*
	- *I'm Nicole van der Hoeven, a Senior Developer Advocate at Grafana Labs, and I'm joined by a colleague of mine, Ishan Jain, a Senior Developer Experience Engineer.*
- Introduce guest: Ishan Jain
	- Who are you?
	- What do you do?
- Definition of terms
	- Artificial intelligence
	- Machine learning
	- LLM
	- What are we talking about observing today?
	- Ishan says AI is the biggest area. ML is under AI and LLM is under ML. 
- Why should we monitor AI?
	- Is AI Observability just another type of Application Observability?
	- How are AI-based apps different?
		- massive datasets
		- costs can increase quickly
		- possibility of model drift
		- security concerns
		- existence of rate limiting for many models
		- latency is important
- What do we need to monitor?
	- Traces
		- Request metadata, like temperature (amount of creativity/randomness), model version, etc
		- Response metadata, like tokens and cost
		- These are the most important for LLMs becuase it talks about the sequence of events. Did I make an LLM call or did I make a call to the Vector DB instead?
	- Metrics
		- Request volume
		- Request duration
		- Costs and token counters
	- What about logs?
- How can we monitor AI?
	- Instrumentation
		- Manual: OpenTelemetry
		- Automated: OpenLIT SDK, Traceloop, Langtrace?
	- Demo? : AI integration for Grafana Cloud: AI Observability (Tempo, Prometheus or Mimir)
		- There was already an OpenAI integration but it wasn't OTel specific. He really wanted something that was a one line or one-click thing.
	- OpenLit dashboard for Grafana Cloud
- Outro
	- If people want to learn more about this topic, where should they go?
	- 


Ollama: https://ollama.com/

GPT 4 all: https://www.nomic.ai/gpt4all
### Just before the show

> Here are some points to discuss with the guest in the 15 minutes before the stream begins.

- [x] How do you pronounce your name?
- [ ] What are your pronouns?
- [x] We will be using the talking points, but we don't have to be strict about it. We don't have to go through all of them, or follow a specific order. They're only there to make us comfortable.
- [x] Does anyone want to share their screen? We can do that now, and I can show you how that works
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