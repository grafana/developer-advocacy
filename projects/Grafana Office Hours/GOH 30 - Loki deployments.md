---
url:
date: 
---
# [GOH 30 - Loki deployments](projects/Grafana%20Office%20Hours/GOH%2030%20-%20Loki%20deployments.md)

<iframe width="560" height="315" src="https://www.youtube.com/embed/" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

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



## Talking points

> Enumerate talking points for the show. It's better to keep these as bullet points to encourage a more casual, rather than scripted, conversation.

- Intro
	- *Hello and welcome to Grafana Office Hours. I'm `<name>`, a `<position>` at Grafana Labs and today, we're going to talk about `<topic>`.*
- Announcements
	- New project releases
	- Recent content published
- Introduce guest
	- Who are you?
	- What do you do?
	- How long have you been using Grafana/other project?

- Three deployment methods (monolithic, simple scalable, microservices) and when you should use what.
	- When should you do monolithic federated (multiple replicas) vs. simple scalable vs. microservices
- Production setup
	- How many replicas of each?
	- Storage
		- Minio bridge to AWS S3?
	- Quirks in cloud providers: how to authenticate-- i.e. IAM for AWS. How do we make sure Loki can talk to object storage? What are some best practices there?
	- Why does GEL exist? At what point do you recommend that people switch over?
- Migration
	- from one version of Loki to another
	- from one type of storage to another
- Using a ruler to query Prometheus instead of Loki

### Questions

- What's the status of loki-disributed helm chart? Will it be updated to with Loki 3.0? There is migration document about migrating from loki-distributed chart to loki chart with "distributed mode". Does it mean that loki-distributed chart is deprecated? Ref: https://github.com/grafana/helm-charts/issues/3086 (local)
- Are there any plans improving the documentation of Loki, considering the many open issues on Github and the Grafana community? (local)
- How to deploy in ssd mode in kubernetes using helm chart (GCP)
- It feels like I pay a tremendous amount in PUT/LIST requests versus actual storage costs on AWS. My storage is a couple bucks while my PUT/LISTs result in 80+ dollar bills. What are optimizations I can make to lower my costs when using cloud storage costs?
- what is the future of jsonnet based deployment? seems it is not updated frequently
- We do multi-cloud deployments of our apps but have loki configured so it writes back to a single cloud/region. Do you have other users doing this?
- Considering single-store tsdb is recommended now, are there any reasons to still support any alternatives in Loki 3?
- How to configure helm chart values for a proper production ready loki (GCP)
- What does non-cloud deployment look like? For example is minio or similar S3 store a bad idea

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