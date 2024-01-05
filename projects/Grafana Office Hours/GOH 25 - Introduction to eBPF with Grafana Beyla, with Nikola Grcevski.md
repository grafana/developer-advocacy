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
	- Sometimes when you see a problem, it's too late - the issue has occurred and you didn't have it already instrumented.
	- Types of instrumentation
		- Source instrumentation
		- Binary instrumentation
		- External instrumentation - including eBPF
	- Issues
		- multiple agents collecting different signals
		- agents don't exist for every language
		- proliferation of exporters
	- The dream: automagically observe everything with little to no effort
- What is eBPF?
	- Only works on Linux kernel (eBPF on Windows is being worked on but it's not operational yet)
	- What is auto-instrumentation? How close is it to the automagical dream?
	- How does it try to solve the issues with instrumentation?
	- eBPF used to be just bPF (Berkley Packet Filter) - you can extend the kernel with additional logic (modules). Making the kernel programmable.
		- eBPF (with the e) can also extend the kernel but it's different. We have a virtual machine on the kernel (just like the JVM) that can execute instructions.
		- VMs are better than modules because they're safer, doesn't break the kernel, and it's isolated.
	- Do you eventually see it as a replacement for manual instrumentation?
	- eBPF can be used for other purposes: security, load balancing (circuit breaker pattern)
	- eBPF:
		- kernel side: written in C
		- user space side: written in Go (or other language)
- What is Grafana Beyla?
	- Initial goal: tool that captures signals for application monitoring, not infrastructure monitoring
		- HTTP and gRPC
	- One of the requirements of Beyla is that "eBPF is enabled in the host". What does that entail?
	- Demo of how to set it up on Kubernetes
	- What languages does it support?
		- Distributed tracing on Go - what's the status of this?
	- Beyla automatically reduces the cardinality of URL paths by collapsing paths so that when you send this to Prometheus, you don't get charged more because of a cardinality explosion.
	- Beyla tells you not just the response time but also the time it took *before* the goroutine picks up and actions a request. This can only be seen at the kernel level
- What is Application 011y? (demo)
	- Can Beyla only be run on Grafana Cloud?
- Is it possible to do distributed tracing with Beyla/eBPF?
	- It IS, but it's not been released yet. They have an implementation for Go. 
	- Trace IDs are generated and tracked through the Go runtime as Goroutines start the flow within the Go application. They can tie when a incoming and outgoing requests are made.
	- In the process of doing this for gRPC.
- Partnership with Isovalent (now Cisco)
	- What is Cilium and how does it compare to Beyla?
		- Cilium captures things at the network level. There are some limitations to that - it's a different approach. We believe that instrumenting at the application level rather than the network level can give us richer information. For example, for GO, we can get information about the runtime. It's easier to track things at the protocol level, like SQL calls in Go, at the application level.
		- At some level, some of the information can also be extracted by both. But we think Beyla can add extra value
	- Cilium libraries are also used in Beyla
		- Beyla is built with Cilium Go
	- What protocols does Beyla do that Cilium can't?
		- HTTPS implementation in Beyla doesn't require certificates unlike Cilium
	- How does the Cisco acquisition affect us, if at all?
- What is a service mesh? How is Beyla different from a service mesh like Istio or Linkerd?
	- This is similar to Cilium - they can extract some info about Level 7 HTTP events. But how do you do gRPC? How do you do Layer 2? That's going to be more chalelnging.
	- Service mesh is on network level
	- Beyla can get more information than a service mesh
	- Differences in protocols supported?
- Outro
	- If people want to learn more about this topic, where should they go?
	- 

### Just before the show

> Here are some points to discuss with the guest in the 15 minutes before the stream begins.

- [x] How do you pronounce your name?
- [ ] What are your pronouns?
- [x] We will be using the talking points, but we don't have to be strict about it. We don't have to go through all of them, or follow a specific order. They're only there to make us comfortable.
- [x] Does anyone want to share their screen? We can do that now, and I can show you how that works
- [x] We'll be streaming to YouTube.
- [x] You'll be able to see comments, but if you have links, I have to paste it into the private chat.
- [x] You can also use the private chat if you need to say something, but you can also just say it out loud.
- [x] If at any point you aren't comfortable talking about something, please either say so or let me know in the private chat, and I'll pivot away from that topic.
- [x] Afterwards, we'll say goodbye to the stream, but please stay on past that so we can debrief.
- [x] Just in case I disconnect... stall for a minute and I'll be right back.

## After the show

- [ ] Add timestamps to the video (at least four).
- [ ] Add any links shared to the description of the video.
- [ ] Add the video to video playlists that make sense (at the very least, the "Grafana Office Hours" one.)