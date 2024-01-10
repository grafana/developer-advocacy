---
url: https://youtube.com/live/ZEUzucqXUnQ
date: 2024-01-05
---
# [[GOH 25 - Introduction to eBPF with Grafana Beyla, with Nikola Grcevski]]

<iframe width="560" height="315" src="https://www.youtube.com/embed/" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Guest:: Nikola Grcevski

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
- [x] Schedule posts on socials just when the show begins to say "We're live now!"
- [x] Schedule a Slack message on the internal Grafana workspace (in `#community`).
- [x] Schedule a Slack message on the public Grafana Slack workspace (in `#announcements`)

## Reference links

Grafana Beyla repo: https://github.com/grafana/beyla
Grafana Beyla docs: https://grafana.com/docs/grafana-cloud/monitor-applications/beyla/
Application Observability docs: https://grafana.com/docs/grafana-cloud/monitor-applications/application-observability/

## Timestamps



## Talking points

> Enumerate talking points for the show. It's better to keep these as bullet points to encourage a more casual, rather than scripted, conversation.

- Intro
	- *Hello and welcome to Grafana Office Hours. I'm `<name>`, a `<position>` at Grafana Labs and today, we're going to talk about `application auto-instrumentation with eBPF and Grafana Beyla, and pretty much what all those words mean`.
- Introduce Nikola
	- Who are you?
	- What do you do?
	- How long have you worked at Grafana/on Beyla?
	- What did you do previously?
		- compiler engineer, worked on Java SDK
		- Elasticsearch DB
- The problems with instrumentation
	- Types of instrumentation
		- Source instrumentation
		- Binary instrumentation - including eBPF
	- Issues
		- multiple agents collecting different signals
		- agents don't exist for every language
		- proliferation of exporters
	- The dream: automagically observe everything with little to no effort
- What is eBPF?
	- What is auto-instrumentation? How close is it to the automagical dream?
	- How does it try to solve the issues with instrumentation?
	- Do you eventually see it as a replacement for manual instrumentation?
- What is Grafana Beyla?
	- One of the requirements of Beyla is that "eBPF is enabled in the host". What does that entail?
	- Demo of how to set it up on Kubernetes
	- What languages does it support?
		- Distributed tracing on Go - what's the status of this?
- What is Application 011y? (demo)
	- Can Beyla only be run on Grafana Cloud?
- Partnership with Isovalent
	- What is Cilium and how does it compare to Beyla?
	- Cilium libraries are also used in Beyla
	- What protocols does Beyla do that Cilium can't?
- What is a service mesh? How is Beyla different from a service mesh like Istio or Linkerd?
	- Service mesh is on network level
	- Beyla can get more information than a service mesh
	- Differences in protocols supported?
- Outro
	- If people want to learn more about this topic, where should they go?
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