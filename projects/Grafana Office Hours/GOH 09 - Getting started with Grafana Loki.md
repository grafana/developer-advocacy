---
url: https://youtube.com/live/OLebNPLIJMI
date:
---
# [[GOH 09 - Getting started with Grafana Loki]]




## Checklist

- [x] Contact the guest and tell them about Office Hours.
	> At Grafana Labs, we do a weekly livestream called [Grafana Office Hours](https://www.youtube.com/watch?v=uk7NoagbJ28&list=PLDGkOdUX1Ujrrse-cdj20RRah9hyHdxBu), where we have guests on to talk about how to use Grafana, observability, or visualization. I saw your [blog post/video/post] on [source] and I think it would be great to have you on the show to share your experience about [topic].
	Office Hours is an hour-long live conversation that is streamed to the [Grafana YouTube channel](https://youtube.com/@grafana). It's very casual, and you can also share your screen if you'd like to do a demo (not required). If you'd like to join, I'd love to have you! 
- [x] If the guest agrees, choose a date for the Office Hours session. Confirm the time: 15:00 UTC (17:00 CEST) on Friday. Ask them for a photo you can use for promotion, or ask for permission to use their profile pic on social media.
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
- [x] Schedule a Slack message on the public Grafana Slack workspace (in `#grafana`)


## Talking points

> Enumerate talking points for the show. It's better to keep these as bullet points to encourage a more casual, rather than scripted, conversation.

- Intro
	- *Hello and welcome to Grafana Office Hours. I'm `<name>`, a `<position>` at Grafana Labs and today, we're going to talk about `<topic>`.*
- Announcements
	- New project releases
	- Recent content published
- Introduce Ward Bekker
	- Who are you?
	- What do you do?
	- How long have you been using Grafana/other project?
- What is a log and how is it different from metrics?
	- You can usually start with a log, and then create metrics from it.
- What are some issues regarding logs?
	- Difficulty in parsing: Sometimes logs are unstructured. Sometimes they're structured. Mostly they're in text. Could be CSV, JSON
	- Can be really verbose, filling up storage
	- Distributed computing means distributed logs
	- Ephemeral nature of pods means logs can also be ephemeral
- What is log aggregation? Why do logs need to be aggregated?
- What is Loki? 
	- What does Loki do?
		- Log aggregation
	- Why do we say Loki is "like Prometheus, but for logs?"
	- How do you install it?
		- binary
		- Helm chart - use this one: https://grafana.com/docs/loki/latest/installation/helm/install-scalable/
	- Features
		- ease of use
		- 100% persistence to object storage-- what does this mean?
		- only indexes metadata rather than full text (faster, cheaper to run)
			- way more performant
			- log line is stored (and compressed) but not indexed.
			- grepping workload is distributed - parallelized way
		- collects logs using Promtail
			- Promtail is the agent (out of the box)
			- If there is something wrong, there is an exponential backoff so it doesn't hammer your server.
		- LogQL (like PromQL)
		- alerting
		- horizontally scalable, multi-tenant: how do you scale Loki?
			- Promtail
			- load balancer
			- three microservices:
				- read
				- write
				- Loki cluster administrative microservice (`backend`)
		- works well with Grafana stack, K8s
		- object storage
			- You can use Minio
			- It's really important to benchmark this because it won't be
		- Alerting - works with Prometheus Alert Manager
			- You create a metric out of your logs with LogQL
	- Alternatives
		- Lucine
		- Splunk
		- How is it different from Logstash?
			- Works well with Grafana and Prometheus
			- Better for cloud native, which generates a huge amount of logs
- Outro
	- If people want to learn more about Loki, where should they go?
	- https://www.youtube.com/playlist?list=PLDGkOdUX1UjqEzcxQrbROMy8DN7MZv_h4

### Just before the show

> Here are some points to discuss with the guest in the 15 minutes before the stream begins.

- [x] How do you pronounce your name?
- [ ] What are your pronouns?
- [x] We will be using the talking points, but we don't have to be strict about it. We don't have to go through all of them, or follow a specific order. They're only there to make us comfortable.
- [x] Does anyone want to share their screen? We can do that now, and I can show you how that works
- [x] We'll be streaming to YouTube.
- [x] You'll be able to see comments, but if you have links, I have to paste it into the private chat.
- [x] You can also use the private chat if you need to say something, but you can also just say it out loud.
- [ ] If at any point you aren't comfortable talking about something, please either say so or let me know in the private chat, and I'll pivot away from that topic.
- [x] Afterwards, we'll say goodbye to the stream, but please stay on past that so we can debrief.
- [x] Just in case I disconnect... stall for a minute and I'll be right back.

## Timestamps

00:00:00 Introductions
00:03:34 What is a log? How is it different from a metric?
00:12:29 Why is it called Loki?
00:14:58 What is Grafana Loki?
00:20:50 How is Loki different from alternatives?
00:27:20 How does Loki work?
00:33:39 Cost, performance, scalability
00:42:14 Q - What to use for object storage with Loki
00:44:13 Q - Which Helm chart to use for Loki
00:48:56 Q - How do you do alerting with Loki?
00:52:29 Q - What is the backend component in the Loki Helm chart?
00:53:33 Loki dashboard on Grafana Play
00:56:36 5-minute summary

## After the show

- [ ] Add timestamps to the video (at least four).
- [ ] Add any links shared to the description of the video.
- [ ] Add the video to video playlists that make sense (at the very least, the "Grafana Office Hours" one.)