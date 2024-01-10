---
url: https://youtube.com/live/EYR5lQJ_kG8
date:
---
# [[GOH 15 - Agentless monitoring for Prometheus in Grafana Cloud]]

<iframe width="560" height="315" src="https://www.youtube.com/embed/" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Guest:: 

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

## Resources

- [Design doc](https://docs.google.com/document/d/1_gnpPA00ZsxCpoaRwOPGIAp92bsPmNkRqFEAkVAL_H0/edit#heading=h.5sybau7waq2q) - describing the problem and solution
- Docs: https://grafana.com/docs/grafana-cloud/monitor-infrastructure/integrations/integration-reference/integration-metrics-endpoint/
- Blog post: https://grafana.com/blog/2023/09/21/introducing-agentless-monitoring-for-prometheus-in-grafana-cloud/
- [The original hackathon video](https://raintank-corp.slack.com/archives/C04T3F5GCF3/p1679077709938139) - this is a little older, but lays out some context and the general theme

## Talking points

> Enumerate talking points for the show. It's better to keep these as bullet points to encourage a more casual, rather than scripted, conversation.

- Announcements
	- New project releases
	- Recent content published
- Introduce Matt Nolf
	- Who are you?
	- What do you do?
	- How long have you been working at Grafana Labs?
- Monitoring and instrumentation
	- What is instrumentation?
	- Is instrumentation always necessary for monitoring?
	- What is an agent?
	- How do you collect data?
	- How are agents related to instrumentation?
		- Agents require instrumentation
	- What is Grafana Agent? How does it work?
	- Advantages of agent-based monitoring
	- Disadvantages of agent-based monitoring
- What is agentless monitoring?
	- How does it work?
		- We run hosted Grafana Agents
		- Not Prometheus Service Discovery - it's just a URL. It doesn't crawl other services.
	- Is agentless monitoring the same as scraping?
	- Does agentless monitoring still require instrumentation?
	- How does it address the disadvantages of agent-based monitoring?
	- What are some advantages of agentless monitoring?
		- Easier to set up because there's nothing to install
		- Less infrastructure to manage
		- Brings observability to customers who are using serverless functions or PaaS products
	- What are some disadavantages/limitations of agent-based monitoring?
- Metrics Endpoint integration for Grafana Cloud
	- What is it?
		- hosted ("agentless") Integration that will allow users to generically scrape metrics from any publicly accessible /metrics endpoint (Prometheus based of course) over HTTPs into Grafana Cloud without the need to for them to host a standalone agent
	- How did it start?
		- Two Hackathons: The Scrapers
			- Prometheus Service Discovery for scraping from an external cloud provider that supports Prometheus Service Discovery (ex: DigitalOcean)
			- Part 2: Adding more platforms like Supabase, Fly.io, Vercel, Aiven, Mongo Atlas
	- Why Grafana Cloud?
		- How does it make life easier?
		- What's the value of having integrations for the most common services?
		- Why do we need a generic HTTP integration if we have integrations?
	- How does it work?
	- Demo
		- Requirements and pre-reqs
		- How to set up scraping for a metrics endpoint
		- How to add dashboards and alerting afterwards
	- What are some of its limitations?
		- Prometheus only
		- Not suitable for all use cases. Situations where agents are still required?
			- private systems where endpoints can't be exposed
			- convenience vs. functionality: when you need a decoupled agent to perform some added functionalities
				- transforming or filtering out metrics (for example, to avoid cost)
				- changing routing
- Future plans for Metrics Endpoint
	- scraping at intervals
	- 
- Outro
	- If people want to learn more about this topic, where should they go?
	- Docs: https://grafana.com/docs/grafana-cloud/monitor-infrastructure/integrations/integration-reference/integration-metrics-endpoint/
	- Blog post: https://grafana.com/blog/2023/09/21/introducing-agentless-monitoring-for-prometheus-in-grafana-cloud/
	- Grafana Agent

- In our docs, we say we shouldn't do agentless config because we want a man in the middle so that we can change the routing if we want to. Agentless is awesome if you can make it work. When should we not do this? Convenience vs functionality. What about being able to transform metrics through Agent too? Filter things out from Agent to avoid cost.

### Just before the show

> Here are some points to discuss with the guest in the 15 minutes before the stream begins.

- [x] How do you pronounce your name?
- [x] What are your pronouns?
- [x] We will be using the talking points, but we don't have to be strict about it. We don't have to go through all of them, or follow a specific order. They're only there to make us comfortable.
- [ ] Does anyone want to share their screen? We can do that now, and I can show you how that works
- [x] We'll be streaming to YouTube.
- [ ] You'll be able to see comments, but if you have links, I have to paste it into the private chat.
- [ ] You can also use the private chat if you need to say something, but you can also just say it out loud.
- [ ] If at any point you aren't comfortable talking about something, please either say so or let me know in the private chat, and I'll pivot away from that topic.
- [ ] Afterwards, we'll say goodbye to the stream, but please stay on past that so we can debrief.
- [ ] Just in case I disconnect... stall for a minute and I'll be right back.

## After the show

- [ ] Add timestamps to the video (at least four).
- [ ] Add any links shared to the description of the video.
- [ ] Add the video to video playlists that make sense (at the very least, the "Grafana Office Hours" one.)