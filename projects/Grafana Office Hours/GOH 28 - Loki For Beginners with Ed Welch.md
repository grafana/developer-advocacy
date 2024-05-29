---
url:
date: 
---
# [[GOH 28 - Loki For Beginners with Ed Welch]]

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

🖊️ Open-source log monitoring: The concise guide to Grafana Loki: https://grafana.com/blog/2023/12/11/open-source-log-monitoring-the-concise-guide-to-grafana-loki/?pg=blog&plcmt=body-txt
🖊️ Everything you need to know about labels: https://grafana.com/blog/2023/12/20/the-concise-guide-to-grafana-loki-everything-you-need-to-know-about-labels/
🖊️ How to work with out-of-order and older logs: https://grafana.com/blog/2024/01/04/the-concise-guide-to-loki-how-to-work-with-out-of-order-and-older-logs/


## Timestamps



## Talking points

> Enumerate talking points for the show. It's better to keep these as bullet points to encourage a more casual, rather than scripted, conversation.

- Intro
	- *Hello and welcome to Grafana Office Hours. I'm `<name>`, a `<position>` at Grafana Labs and today, we're going to talk about `<topic>`.*

Title: Loki For Beginners with Ed Welch (TBD)


- Intro, who we are (Ed & Nicole & Jay)
	- We're going to be asking all the beginner questions for Loki!
- Why do we need a logs-specific database? Why was Loki created?
	- Efficiency and high volume: Logs are write-intensive, time-series data
	- (Horizontal) scalability due to amount of logs
	- Cost-effectiveness
		- Databases usually have a large index, requiring "tall" (vertically scaled up) machines
	- Query performance: querying logs is a pain, tagging and labelling
	- "Prometheus but for logs" + integration with Grafana + Cortex's distributed system design
	- What problems were you trying to solve with Loki vs. other logging solutions?
		- Promtail
		- What were/are the alternatives on the market?
		- Why does Loki avoid full-text indexing?
- What is Loki?
	- How does Loki work? How is Loki different?
		- Loki's data model: store everything as a string.
		- Schema-less, structureless data model ("schema at query")
		- Loki is a row-oriented database, not a columnar one. What's the difference?
	- Definitions of terms
		- Log streams
		- Chunks
		- Labels
	    - How are chunks and lables related to log streams?
	- Can you explain the Loki architecture?
		- Built as a distributed system
	- Loki can be deployed in different ways, can you explain the different ways to deploy Loki? (Deployment Modes - Monolithic, Microservices, etc.)
- Writing to Loki: Ingestion options
	- What are the ways that you can write stuff to Loki?
    - How does Loki handle log retention and storage backends? How are logs stored in Loki?
- Reading from Loki: LogQL
	- How does Loki find data?
		- Sorting algorithms: bubble sort, insertion sort, merge sort, bucket sort
		- What Loki uses
			- minimal indexing
			- chunking
			- sharding
			- replication/parallelization
			- compression and storage optimisation
	- How does it compare to other query languages?
	- What are some common queries you can run in Loki?
- What is Loki NOT good at?
	- Columnar queries - what does that mean?
	- "Needle in a haystack" queries
	- High-cardinality label values - what does that mean?
- Common Problems you see in the wild
	- What are some common problems you see with Loki deployments?
	- Common problems with how users use labels
		- The fewer labels you use, the better.
		- Use labels that: describe infrastructure, are long-lived, and are intuitive for querying, are low cardinality
	- How should users write logs into Loki efficiently?
	- How should users query logs from Loki efficiently?
	- What are typical troubleshooting steps for performance issues in Loki?
	- How can users monitor the health and performance of their Loki deployments?
- Recent changes in Loki
	- Automatic stream sharding
	- OpenTelemetry support: *structured metadata*.
	- Bloom filters: "needle in a haystack" queries
- Any future plans for Loki?
	- Adaptive Logs and reduction of TCO
	- Architectural rewrite to remove replication factor?
	- Explore Logs and queryless experience
  


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