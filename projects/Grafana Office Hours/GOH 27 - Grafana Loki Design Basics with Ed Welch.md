---
url: https://www.youtube.com/live/3uFMJLufgSo
date: 2024-06-07
---
# [[GOH 27 - Grafana Loki Design Basics with Ed Welch]]

<iframe width="560" height="315" src="https://www.youtube.com/embed/3uFMJLufgSo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Guest:: Ed Welch

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

00:00:00 Introductions to Nicole, Jay, and Ed Welch
00:02:52 Why was Loki created?
00:08:37 Why do we need a logs-specific database?
00:15:51 What is an index?
00:22:27 Keyspace, index, label, metadata, and tags
00:25:57 What is a log stream? How can you make them long-lived?
00:31:51 Tradeoff in databases: ingestion, query, and complexity
00:35:35 How Loki stores logs as strings
00:39:39 Columnar vs row-oriented databases
00:46:58 When logs get deduplicated in Loki
00:50:29 How to query in Loki with LogQL
00:56:25 Best practices for querying logs from Loki

## Talking points

> Enumerate talking points for the show. It's better to keep these as bullet points to encourage a more casual, rather than scripted, conversation.

- Intro
	- *Hello and welcome to Grafana Office Hours. I'm `<name>`, a `<position>` at Grafana Labs and today, we're going to talk about `<topic>`.*

Title: Loki For Beginners with Ed Welch (TBD)


- Intro, who we are (Ed & Nicole & Jay)
	- Loki was announced six years ago in November 2018. Ed started with Grafana in January 2019. He was the first engineer officially on the project.
	- Tom Wilkie and David Kaltschmidt created the idea of Loki. Some engineers at Grafana (then about 30 people in the whole company) were working on Cortex, and some of them worked on Loki too, like Goutham and Jacob Lissi.
- Why do we need a logs-specific database? Why was Loki created?
	- Loki is not particularly Kubernetes (especially not anymore) but it was a big part of why it was created. There wasn't an easy way to get logs out of Kubernetes. There was really nothing that was built for Kubernetes. Service discovery, which is one of the core features, was not there. So it borrowed the concept of labels from Prometheus, although now we use it differently from Prometheus.
	- Key to what Loki does: use object storage to simplify maintenance-- you don't get paged for disks running out of space
	- Loki makes tradeoffs around the type of data and how we expect it to get used. No database gets anything for free and design decisions help determine what it's optimising for.
		- What Loki wanted: very simple ingestion, very simple schema requirements so you don't have to figure out your schema beforehand.
			- LogQL as a query language + "Schema at query"
	- Ephemeral nature of pods
	- Microservices-based, cloud-native
	- Efficiency and high volume: Logs are write-intensive, time-series data
	- (Horizontal) scalability due to amount of logs
		- Don't have to worry about scaling disks or running out of disk space.
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
			- Columnar databases are better for metrics
			- Metrics can be looked at as kind of an index for logs too
	- Definitions of terms
		- Index: way to reduce a large amount of data into a smaller set so that it's easier to find what you're looking for. It's also a way to take data in different columns
			- Keyspaces: key-value pairs. An index is a way of storing a keyspace.
			- Ideally, you want to choose a key that breaks apart evenly into different systems
		- Labels: Labels are also indices. Loki is not index-free.
			- Also "metadata", "tags"
			- Labels and tags are nearly interchangeable. Index and metadata are very related.
			- OpenTelemetry: "semantic conventions" that are opinions on how labelling is done
			- In Loki, this is limited. We recommend 15.
		- Log streams: separate files on disk - unique combination of key-value pairs
			- analogous to "series" in Prometheus. We made up "stream" in Loki
			- good streams live forever because the label values are very consistent (though in practice, labels definitely churn and don't last forever)
		- Chunks: multiple log streams
	    - How are chunks and labels related to log streams?
	    - Log entry - one line
	- Can you explain the Loki architecture?
		- Built as a distributed system
	- Loki can be deployed in different ways, can you explain the different ways to deploy Loki? (Deployment Modes - Monolithic, Microservices, etc.)
- Writing to Loki: Ingestion options
	- What are the ways that you can write stuff to Loki?
    - How does Loki handle log retention and storage backends? How are logs stored in Loki?
    - Influx is a metrics database. Timestamp is the primary key. If a line comes in that has exactly the same timestamp, it will overwrite the first one. In Loki, if it's the same content, they're deduplicated (only one is kept). If it's different content, both are stored. The problem with this is that it does also happen a lot because systems don't keep perfect time. Also we have exact duplicates because of replication.
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
	- Finding small bits of information over a huge dataset (though bloom filters are going to help with this)
	- Columnar queries - what does that mean?
		- Loki is row-oriented: it receives data in rows (strings), in files, and stores them on disk. Columnar database: define schema and then fill out the column with specific data. The key-value pairs become columns. Where this matters is in the read path, when it's queried. If you wanted to sum up all values in Column A, Loki would have to read the entire row - it's not efficient at this. Loki stores rows physically together. Columnar databases store columns together.
		- Prometheus is more of a columnar store (but Ed doesn't feel comfortable saying this)-- this is better for metrics in general. Metrics can be thought of as an index for logs. You can use recording rules for Loki where you store metrics to Mimir or Prometheus. Metrics also normalise data over time -- they're way more consistent over time. "Logs are the only true observability signal." Metrics are a good way to narrow down logs. Next step would be instrumenting for metrics specifically.
	- "Needle in a haystack" queries
	- High-cardinality label values - what does that mean?
- Common Problems you see in the wild
	- What are some common problems you see with Loki deployments?
	- Common problems with how users use labels
		- The fewer labels you use, the better.
		- Use labels that: describe infrastructure, are long-lived, and are intuitive for querying, are low cardinality
	- How should users write logs into Loki efficiently?
		- What if you have to change a label? This is always tricky because it always happens. It's good practice to normalsie data upon ingest, but accept it will change. You can change the schema or you can also change the query over time (this is probably easier).
		- Use fewer labels
		- Use long-lived labels (not unique)
		- Use labels people would actually query for (postcodes, not house numbers)
	- How should users query logs from Loki efficiently?
		- All key values in Loki are parsed labels (it doesn't really matter). Can you put it within curly braces?
		- LogQL isn't great at `count` or `distinct` (SQL is better at this)
		- Loki is more like a Table of Contents in a book (the back of the book is more like a reverse index where it's very specific). 
		- Tips (do this in order, left to right in the query - these are sequentially executed)
			- Narrow down your time range first. This is usually the best way to reduce the number of logs that need to be parsed, but in practice, if there's another label that reduces the amount of logs more, then use that.
			- The more specific you can be at the start, the faster you'll be able to get your result. You don't have to do country, suburb, post code, etc-- go with the post code if you know already.
			- Then do filter expressions (like `|=` [contain] or `!=` [not contain]) - this is the next fastest thing that Loki can evaluate. Always prefer these to the regular expression equivalents because they're more expensive to evaluate. Never use the case insensitive variant (this is purposely hard to do in Loki because it's so slow and expensive).
			- *Then* parse. (JSON parsing, like `parent = cat`)
		- The tips above become more important the larger your database is-- you should optimise if it's >100s of GBs or TBs
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
  
Next:
- deployment and execution of Loki - Ed would have the opportunity to apologise for how difficult it can be
	- Configuration is complicated and it's changed a lot over time
	- People underestimate the amount of resources that you need to run a high-performant setup. Most people still just use a single binary and are happy with that, but there are somer cases where that's just not enough.
	- We recommend Helm and Kubernetes, but that's not the way we do it-- we don't use that.
	- Jay is already using the simple scalable Helm chart and it's working now.
		- Simple scalable was Ed's idea and he's not sure it's a good idea now...
	- Break it down: monolithic, SSD, microservices
	- Advice on how many ingesters we need, how many queriers, how would you set it up onsite. 
	- How we run it on the cloud-- we autoscale everything all the time, automating limits configuration.
	- You *can* make Loki easier to run, but it costs more money.
- Ingest
	- Should we use the OTel endpoint? The client can't specify the labels if you use this. You send the payload and the seven keys are promoted to labels. The rest goes to structured metadata. YOu can't do this unless you run it yourself. You can do that in the YAML config.
- Query
- Bloom filters
- Adaptive Logs

### Just before the show

> Here are some points to discuss with the guest in the 15 minutes before the stream begins.

- [x] How do you pronounce your name?
- [ ] What are your pronouns?
- [x] We will be using the talking points, but we don't have to be strict about it. We don't have to go through all of them, or follow a specific order. They're only there to make us comfortable.
- [ ] Does anyone want to share their screen? We can do that now, and I can show you how that works
- [ ] We'll be streaming to YouTube.
- [ ] You'll be able to see comments, but if you have links, I have to paste it into the private chat.
- [x] You can also use the private chat if you need to say something, but you can also just say it out loud.
- [x] If at any point you aren't comfortable talking about something, please either say so or let me know in the private chat, and I'll pivot away from that topic.
- [ ] Afterwards, we'll say goodbye to the stream, but please stay on past that so we can debrief.
- [ ] Just in case I disconnect... stall for a minute and I'll be right back.

## After the show

- [ ] Add timestamps to the video (at least four).
- [ ] Add any links shared to the description of the video.
- [ ] Add the video to video playlists that make sense (at the very least, the "Grafana Office Hours" one.)