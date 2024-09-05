---
url: https://youtube.com/live/1Buk3wPpJdY
date: 2024-07-19
---
# [GOH 28 - OpenTelemetry Metrics with Traefik](GOH%2028%20-%20OpenTelemetry%20Metrics%20with%20Traefik.md)

<iframe width="560" height="315" src="https://www.youtube.com/embed/1Buk3wPpJdY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Guest:: 

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



## Timestamps

00:00:00 Introductions
00:03:30 What does Traefik Labs do?
00:08:12 What is a reverse proxy and why might you need one?
00:20:50 What are the advantages of Traefik over Nginx?
00:25:52 How is Traefik improve observability for microservices?
00:31:20 Demo: Traefik + Grafana for observability
00:41:02 Grafana dashboard using Traefik for API performance
00:53:17 Personal use cases for Grafana
00:57:09 Zero trust and security for APIs
00:58:42 How can you learn more about Traefik?


## Talking points

> Enumerate talking points for the show. It's better to keep these as bullet points to encourage a more casual, rather than scripted, conversation.

- Intro
	- *Hello and welcome to Grafana Office Hours. I'm `<name>`, a `<position>` at Grafana Labs and today, we're going to talk about `<topic>`.*

Title: Something with OpenTelemetry Metrics (TBD)


- Intro, who we are (Maytham & Immánuel)  
- How we’ve met (API Days Paris booth)    
- Why Traefik was created
	- Reverse proxies are not cloud-native, dynamic configuration did not exist. Service discovery was very early/nonexistent.
	- Traefik automates thousands of microservices. Truly cloud native and Kubernetes-native because everything can be configured using CRDs.
	- Traefik is the default ingress for Rancher and k3s
	- Traefik takes into account the ephemeral nature of Kubernetes pods.
- About Traefik Labs
	- Community as a core value
	- DockerHub stats, etc. regular pitch
	- Used to be an application proxy, then full-fledged API gateway. Now also API management.
- Why do you need a reverse proxy?
	- You don't have to expose the application directly
	- You might want to use the same domain name for different services. (microservices)
	- You can also use it as an ingress controller to access parts of your service
	- automatic routing
	- web UI
	- load balancer
- Why isn't Nginx enough?
	- Config isn't enough in Nginx
	- Nginx has LUA based plugin system. Traefik doesn't use Lua.
	- Traefik is written in Go
	- The level of automation
	- Static vs dynamic config
	- Plugins in LUA vs Go/WASM
- Portfolio
	- Proxy - OSS reverse proxy/ingress controller
	- Enterprise - an API GW based on Proxy
	- Hub - API GW & API Management, based on Proxy & Enterprise
- Observability
	- Challenges of IT departments, why observability matters
	- State of metrics in the portfolio
		- Prometheus
		- StatsD
		- Datadog
		- InfluxDB
	- About OTel in general
		- Why a new standard
		- The Go SDK support metrics + tracing, logs in dev
	- OTel metrics in
		- Proxy - proxy/ingress metrics
		- Hub - API Mgmt metrics, most metrics on the market as far as we saw
	- OTel tracing in
		- Proxy v3
		- Soon in Hub
- Demo: [https://github.com/traefik-workshops/traefik-hub-gitops](https://github.com/traefik-workshops/traefik-hub-gitops) 
	- Present the demo application
	- Explain GitOps with Flux, the needed components deployed
		- Must be declarative and immutable
		- Continuous
	- Showcase our pre-built Grafana dashboards on Grafana Cloud
	- Demo flow and use cases:
		- API change management - Show the use of the static analyzer for catching errors early and the impact analysis of a change. GH PRs and Flux deployment events show up on the Grafana dashboard
		- Incident mitigation and resolution - Since we have event correlation, it’s easy to observe when things go wrong (e.g., latency spike) and then revert the PR that caused the outage. Now teams have time to resolve the underlying issue without time pressure, deploy it to another env, test it, etc. then try it confidently again.
- Grafana Cloud is used for Traefik Labs internal monitoring as well
- Learn more
	- Docs: 
		- Proxy: [https://doc.traefik.io/traefik/v3.0/observability/metrics/opentelemetry/](https://doc.traefik.io/traefik/v3.0/observability/metrics/opentelemetry/) 
		- Hub API Mgmt: [https://doc.traefik.io/traefik-hub/operations/telemetry/metrics/](https://doc.traefik.io/traefik-hub/operations/telemetry/metrics/)
	- Blog: [https://traefik.io/blog/opentelemetry-traefik-hub/](https://traefik.io/blog/opentelemetry-traefik-hub/)
	- academy.traefik.io
- Meet us at KubeCon EU (Paris)
	- Wednesday, March 20–Friday, March 22
	- Traefik Labs: Booth H23

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