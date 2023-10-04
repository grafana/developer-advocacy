---
url: https://youtube.com/live/DEv5wtZxNCk
date: 2023-09-29
---
# [[GOH 13 - How to deploy Grafana on Kubernetes]]

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
- [x] Schedule a Slack message on the public Grafana Slack workspace (in `#grafana`)


## Talking points

> Enumerate talking points for the show. It's better to keep these as bullet points to encourage a more casual, rather than scripted, conversation.

- Introduce Usman
	- Who are you?
	- What do you do?
	- How long have you been using Grafana/other project?
- Different ways to install Grafana
	- Binary for your operating system (Linux, macOS, Windows)
	- Docker (which we discussed previously)
	- Kubernetes
- Evolution of distributed computing
	- Hardware servers
	- Virtualized servers
	- Containerized servers
	- Container orchestration
- What is Kubernetes?
	- Key characteristics of Kubernetes
	- Structure of Kubernetes
	- How to use Docker and k8s in software dev processes
	- Why does Kubernetes matter? for developers? for testers? for platform engineers?
	- Which flavour of Kubernetes to use?
		- vanilla Kubernetes
		- managed Kubernetes (what are distributions?)
	- Other k8s-related tools
		- Helm
		- kubens
		- kubectx
	- k8s and Docker
		- How is it different from Docker?
		- How does Kubernetes run within Docker?
	- Importance of creating a namespace
	- Installing Grafana by copying manifest
	- Installing Grafana via Helm chart
	- How to access Grafana
		- If on managed cloud service: use IP address
		- If local
			- EITHER expose the service
			- OR, use port forwarding
	- Importance of setting up rollout strategy so you can fall back to previous version
	- Changing Grafana image version.
		- Change image name: `grafana/grafana:latest` > `grafana/grafana:dev-10.1...`
- How to install Grafana on Kubernetes: 
- Outro
	- If people want to learn more about this topic, where should they go?
	- https://grafana.com/docs/grafana/latest/setup-grafana/installation/kubernetes/

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


## Timestamps

00:00:00 Introductions - Usman Ahmad
00:03:08 Kubernetes as an evolution of distributed computing
00:14:09 Docker vs. Kubernetes
00:17:54 Basic architecture of Kubernetes
00:24:20 How to configure Kubernetes
00:27:00 What are Kubernetes distributions?
00:31:12 Deploying Grafana on Kubernetes
00:40:20 Accessing Grafana - exposing service and port forwarding
00:44:54 Rolling update strategy for existing deployment
00:47:59 Logging in to Grafana
00:51:28 Changing Grafana version
00:57:59 Five-minute summary of this livestream

