---
url: https://www.youtube.com/watch?v=3u8UxLfmq6I
date:
---
# [[2025-03-25-loki-cache]]

![](https://www.youtube.com/watch?v=3u8UxLfmq6I)

Guest:: "Poyzan Taneli" & "Paul Rogers"

## Pre-show checklist

- [ ] Create a new `.md` file and copy this template into it. Check things off as you work through it.
- [ ] Update [Grafana Office Hours Readme](projects/Grafana%20Office%20Hours/Grafana%20Office%20Hours%20Readme.md) to add the new file to the `Upcoming` section.
- [ ] Contact the guest and tell them about Office Hours.
	> At Grafana Labs, we do a livestream called [Grafana Office Hours](https://www.youtube.com/watch?v=uk7NoagbJ28&list=PLDGkOdUX1Ujrrse-cdj20RRah9hyHdxBu), where we have guests on to talk about how to use Grafana, observability, or visualization. I saw your [blog post/video/post] on [source] and I think it would be great to have you on the show to share your experience about [topic].
	Office Hours is an hour-long live conversation that is streamed to the [Grafana YouTube channel](https://youtube.com/@grafana). It's very casual, and you can also share your screen if you'd like to do a demo (not required). If you'd like to join, I'd love to have you! 
- [ ] If the guest agrees, choose a date for the Office Hours session. Check [the Monday board](https://grafana-labs.monday.com/boards/5724430500) to make sure no other livestream is scheduled for that day. Add a card for that date and time to save the spot.
- [ ] Confirm the time (16:00 CEST on Friday is generally best) with the guest. Ask them for a photo you can use for promotion, or ask for permission to use their profile pic on social media.
- [ ] Invite them to the Grafana Office Hours calendar invite (choose "this instance only", not the whole series). Schedule the invite for 15 minutes before the stream (to do a tech check) until 15 minutes after the stream (to debrief). The invite should be for 1.5 hours total. Explain this to them.
- [ ] Create a thumbnail on [Canva](https://canva.com) using the Grafana Office Hours thumbnail format. Use [thumbsup.tv](https://thumbsup.tv) to check how the thumbnail looks on different devices. [Here are some guidelines for creating thumbnails](https://notes.nicolevanderhoeven.com/Create+engaging+thumbnails).
- [ ] Schedule the broadcast on [Streamyard](https://streamyard.com), and select the Grafana YouTube channel as the destination.
	- [ ] In the title, include the instance of Office Hours, i.e. `What's new in Grafana 10? (Grafana Office Hours #01)`. Including the number or the date (such as `All About Explore Logs (Loki Community Call November 2024`) helps people remember it.
	- [ ] Add the standard description as per previous Grafana Office Hours shows. Check the video description and add guests' contact details.
- [ ] Get familiar with how to use Streamyard. [Here's a crash course on how to use Streamyard](https://drive.google.com/file/d/1hb8FeoO88zinZu638MfnBwGctyspgfm0/view?usp=drive_link) and [here's a second recorded call with the Grafana Campfire hosts](https://drive.google.com/file/d/1hdX4SvDM67KRwGkzA6HWEETK1-gy8iUk/view?usp=drive_link) to get them onboarded with Streamyard. These include how to create the stream on Streamyard.
- [ ] Get the Streamyard invite link and put it in the "location" of the calendar invite to the guest.
- [ ] Get the YouTube link to the show. Put the link on this page, in the URL property above.
- [ ] Create an event and announce it [on the Grafana Meetup page](https://www.meetup.com/grafana-friends-virtual-meetup-group/).
- [ ] Schedule posts on socials just when the show begins to say "We're live now!" [Buffer](https://buffer.com/) is a good free tool to use for this. Set it up for your socials and be sure to tag/mention the official Grafana account-- they'll usually boost/repost it if you do.
- [ ] Schedule a Slack message on the internal Grafana workspace (in `#community`, `#content-video`, `#video-offsite-2025-futurism`, and anywhere else you think it might be relevant). Yes this is excessive. Let's change this process!
- [ ] Schedule a Slack message on the public Grafana Slack workspace (in the appropriate channel, such as `#loki` or `#announcements`).
- [ ] Add your call to the Community Calendar (ask David, Richi, Nicole, and Usman).
- [ ] Think of any reference links you might want to give the audience. Add it to the YouTube description.

## Talking points

> Enumerate talking points for the show. It's better to keep these as bullet points to encourage a more casual, rather than scripted, conversation.

- Intro
	- *Hello and welcome to Grafana Office Hours. I'm `<name>`, a `<position>` at Grafana Labs and today, we're going to talk about `<topic>`.*
- Announcements
	- New project releases
	- Recent content published
- Introduce guest
	- Who are you?
		- Paul
			- involved in infrastructure scaling of Loki in the last year
	- What do you do?
	- How long have you been using Grafana/other project?
- Cache Concepts
  - What is a cache? What's a memcache? What's memcached?
	  - Cache: Software/hardware designed to speed up certain operations
	  - Memcache: memory
	  - memcached: key-value pairing operation, open source
  - What are the things that Loki caches?
	  - biggest: chunk cache
	  - query results (memcached frontend, memcached results cache)
		  - 3 endpoints: metrics, volume queries, 
	  - index writes and lookups (labels)
		  - You don't need this if you're using TSDB and not using BoltDB (memcached index queries in JSONNET and Helm chart)
  - What are the telltale signs that indicate you might need a cache?
    - (e.g. high latency retrieving from the store despite all other components working fine)
  - What tradeoffs do you consider when using cache?
    - (e.g. latency versus potential inaccuracy/outdated data, and cost implications)
  - What types of queries benefit most from caching, and when might caching be less effective?
    - (repeated query behaviour, touching the same data, most queried time period, recent data)
    - Last 3 hours of data
    - It depends on how the user is using Loki. The intent is that the data you're touching very often is what should be cached.
  
- Memcached Tiering & Differences
	- What's the role of tiering in cache?
  - Can you describe the different components involved in memcache tiering? (Live Draw)
    - (e.g. Memcache frontend (metrics, labels, volume; done via a hash in header), results cache (query hash, is it in cash or not in cash), and chunks cache (biggest cache, no need for tennancy understanding chunk ref holds this metadata))
  - What is the role of the results cache?
    - (Note: It saves computation cost)
  - What is the role of the chunks cache?
    - (Note: It reduces storage IOPS and bandwidth usage)
    - QUESTION from Andre Ziviani on dedup and chunks cache - what is a good/expected ratio for dedups?
  - What is a spillover cache and why might it not be necessary for most users?
    - (e.g. it prevents issues where memcache isn’t smart enough to retain parts of a query)
- Q: What are the key metrics to look at to know if the cache is correctly tuned?
	- IOPS
	- bandwidth usage
	- computation cost
	- latency - read path (query)
	- The memcached software itself has a command `stat` that will print out all sorts of info - hit rate, eviction, how often cache is compacted. Use this in conjunction with outside metrics.
	- Close to 90% utilization of memcached is what we aim for. When you deploy it as a pod, there are resource limits. But there's also an internal setting that you should have 90%. Correctly tuned memached should never OOM.

- Scaling Memcache
	- How we handle cache at Grafana
		- memcached-extstore attached SSDs to memcached. it gets all data in memory and then flushes to the disk. (Disk, not persistent volumes)
			- When should you scale chunk cache pods vertically/horizontally?
			- 
		- (Danny Kopping) L1 cache - huge storage (extstore)
		- (Ed Welch) L2 cache - update cache based on hits and misses. This is a spillover cache. There is a handoff period of a few days or more. WHen a query hits, look at handoff time. if within L1 time, check L1. If not, check L2.
		- We keep 7 days in cache. We create a recording rule 
	- Extstore is relevant for >half a PB per month.
  - How do we deploy memcache at scale in a Loki environment?
    - Mention Helm value differnces from JSONnet
    - (Note: Considerations include capacity up to 3TB and where to start)
  - How often should we revisit our caching decisions?
    - (Note: Reference [Community PR for not writing to cache if outside chosen window](https://github.com/grafana/loki/issues/14983))
    - Storge access (API calls), Latencties that come cache, trace would show the latency of each component
  - How to decide on cache numbers?
    - (Note: A heuristic suggests that 70% of the query timerange should hit a cell in 7 days; also, the Loki team manages our own instances)
  - How long do cached entries stay valid?
    - Reset 24 hours
    - Don't cache when we flush to storage
    - cache data will go stale. Time to live (TTL)
- What Poyzan and Paul are working on: dynamically sizing memcache
	- Recording rules, then memcache scales up or down dynamically based on the hit ratio of etc. Appropriately sizing

- Failure Scenarios
  - What happens when the system is hit by a large number of queries that cover a long time period?
    - (Note: This could trigger a writeback loop for memcache)
    - Is my cache provisioned correctly? 1 day provisioned but querying 7 days
  - What are the performance impacts if we lose 20%, 50%, or all of the cache pods?
    - (Note: Loki can still serve up to 3 hours of data under such scenarios)
  - What happnes if you see your cache OOMing? Or what should you do if you want verticaly scale your cache?
    - Cache CPU and RAM, configuration how much its allowed to use. Default covers for this
    - memory_limit_mb and max_item_size 
    - Boxes are to big bad for memcache check chunk size

- Monitoring Memcache
  - What are some best practices for monitoring cache performance in a Loki environment?
  - How can you verify that Loki is actually utilizing the cache?

- Cache vs other methods of query
   - When should you use a cache versus a recording rule?
      - (e.g. recording rules for data that changes over a period and is aggregatable vs. cache for similar repeated queries)

- Outro
	- If people want to learn more about this topic, where should they go?

Useful links:
Underlining code for how storage ansd cache works: https://github.com/grafana/loki/tree/main/pkg/storage 


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

## Post-show checklist

- [ ] Add timestamps to the video (at least four).
- [ ] Add any links shared to the description of the video.
- [ ] Add YouTube cards when relevant to certain points during the video.
- [ ] Add the video to video playlists that make sense (at the very least, the "Grafana Office Hours" one.)
- [ ] Download all videos for the recording on Streamyard and upload it [to this shared drive](https://drive.google.com/drive/folders/1sLnnYzmphet7K7QwogcZrYDI-Re07HS4) in the appropriate folder.
- [ ] Think about how you could repurpose this content. [This Loki Community Call](https://youtube.com/live/XJMQbEuBeMc) on Explore Logs was turned into [these](https://youtube.com/shorts/6RfI5UeJo08) [two shorts](https://youtube.com/shorts/jx1DATkGIz4) (*Short - Grafana Cloud Explore Apps for no-code querying of Loki, Mimir, Tempo, Pyroscope* and *Short - How to enable Explore Logs app for Grafana*) and [this shorter video](https://youtu.be/eXwE2vqLcyY) (*How to use the Explore Logs app for Grafana*) + docs.
- [ ] Update [Advocate Contributions sheet](https://docs.google.com/spreadsheets/d/1LataDRRX4DZy8VnCiBDXmynjmpOJdibM7ek_uvpim4Y/edit?gid=0#gid=0) with your work.



### Timestamps

00:00:00 Introductions


### Reference links


🖊️ How we scaled Grafana Cloud Logs Memcached Cluster to 50 TB: https://grafana.com/blog/2023/08/23/how-we-scaled-grafana-cloud-logs-memcached-cluster-to-50tb-and-improved-reliability/ 
💻 Community PR for skipping writing to chunks cache if outside of desired window: https://github.com/grafana/loki/issues/14983 