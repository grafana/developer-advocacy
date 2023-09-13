---
url: https://youtube.com/live/_V81Xm22l_c
date: 2023-09-08
---
# [[GOH 11 - Huzaifa Bin Asif]]

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

[Huzaifa's agenda](https://docs.google.com/document/d/1KG9fkuxaO0OsH4_li-fj0YRJ1SvtqC_c1rU9a0-pJP0/edit#heading=h.5j9oouyj0zox)

> Enumerate talking points for the show. It's better to keep these as bullet points to encourage a more casual, rather than scripted, conversation.

- Introduce guest: Huzaifa Asif
	- Who are you?
	- What do you do?
		- 20M messages at Respond.io and they didn't do performance testing
	- How long have you been using Grafana/k6? 
	- Why did you choose k6 as a testing tool?
- Purposes of k6
	- Regression testing
	- Frontend and backend performance testing (including load, but also database tuning, etc.)
	- Fault injection
	- Contract testing
	- Infrastructure testing: auto-scaling and auto-recovery
- WebSockets case study
	- HTTP is the popular use case, but today we're talking about WebSockets
	- Lots of tools don't support WebSockets.
	- What are WebSockets?
	- [Huzaifa's case study](https://huzaifa-asif.notion.site/Performance-Assessment-of-Echo-Server-s-Horizontal-Scalability-using-K6-07e9c5904d844684a7e0620a5b788116?pvs=4)
		- integrated Redis with sockets and wanted to check the impact on Redis
		- They have 1 giant websocket server for 20M+ messages. They can't scale that server more.
		- Implemented Redis adapter with 4-5 WEbSocket servers and one client server.
		- How to find out which type of Redis to use?
		- They tested with 10,000 VUs and there was only a 2-3% change in the CPU utilization in the server. They realised they don't need to worry about the type of Redis server to use. He thought the medium instance would not handle it well, but surprisingly, it did! Still working fine now!
- Infrastructure testing
	- What is infrastructure testing?
	- Issues and concerns regarding infrastructure testing
	- Autoscaling
		- Screenshare: Huzaifa (how the application auto scales when we run load testing, this helps us test the auto-scaling configuration of infrastructure)
	- Application auto-recovery
		- Screenshare: Huzaifa (Run the k6 script of the application without auto-scaling so that the application crashes. Then we verify how the system recovers when it crashes. Does the application need manual intervention or it auto recover?)
	- Using k6 to Decide Infrastructure Capacity Based on Expected Concurrent Users.
		- Simulate expected peak concurrent users with k6's constant-vus executor. Monitor system performance and adjust infrastructure based on response times and resource utilization. Iterate until the system reliably handles the anticipated load
	- Security testing: Distributed test case to mimic DDoS attack
		- Deploy multiple k6 instances as pods within a Kubernetes cluster to distribute and scale the testing load. This approach leverages Kubernetes' orchestration capabilities, allowing for simulating massive concurrent users from different nodes, and ensuring comprehensive stress testing across distributed systems and regions. Utilize Kubernetes' native services for efficient load balancing, pod management, and monitoring.
- How does k6 fit into the overall observability picture?
	- Integrations with the Grafana Labs stack: Grafana, Prometheus, Tempo, Faro
	- Screenshare: Huzaifa - k6 Integration with Local Grafana & InfluxDB
		- https://github.com/Huzaifa-Asif/K6-Local-Testing-With-Grafana-InfluxDB
- Outro
	- If people want to learn more about this topic, where should they go?
	- Next week, we have a global shutdown day, which means no Grafana Office Hours.
	- Coming up in an hour: stay tuned for the 100th episode of k6 Office Hours, in which we'll be talking about our favourite features of k6 as well as the our favourite moments during that livestream series. Paul and I will be there, joined by our other DevRel colleagues, Marie Cruz and Leandro Melendez.

### Just before the show

> Here are some points to discuss with the guest in the 15 minutes before the stream begins.

- [x] How do you pronounce your name?
- [x] What are your pronouns?
- [x] We will be using the talking points, but we don't have to be strict about it. We don't have to go through all of them, or follow a specific order. They're only there to make us comfortable.
- [x] Does anyone want to share their screen? We can do that now, and I can show you how that works
- [x] We'll be streaming to YouTube.
- [x] You'll be able to see comments, but if you have links, I have to paste it into the private chat.
- [x] You can also use the private chat if you need to say something, but you can also just say it out loud.
- [x] If at any point you aren't comfortable talking about something, please either say so or let me know in the private chat, and I'll pivot away from that topic.
- [x] Afterwards, we'll say goodbye to the stream, but please stay on past that so we can debrief.
- [ ] Just in case I disconnect... stall for a minute and I'll be right back.

## After the show

- [ ] Add timestamps to the video (at least four).
- [ ] Add any links shared to the description of the video.
- [ ] Add the video to video playlists that make sense (at the very least, the "Grafana Office Hours" one.)