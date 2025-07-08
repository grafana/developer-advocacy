---
url: https://youtube.com/live/tKcnQ0Q2E-k
date:
---
# [[2025-06-08 All About Metric Queries]]

<iframe width="560" height="315" src="https://www.youtube.com/embed/tKcnQ0Q2E-k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Guest:: "Cyril Tovena"

## Pre-show checklist

- [x] Create a new `.md` file and copy this template into it. Check things off as you work through it.
- [x] Update [Grafana Office Hours Readme](projects/Grafana%20Office%20Hours/Grafana%20Office%20Hours%20Readme.md) to add the new file to the `Upcoming` section.
- [x] Contact the guest and tell them about Office Hours.
	> At Grafana Labs, we do a livestream called [Grafana Office Hours](https://www.youtube.com/watch?v=uk7NoagbJ28&list=PLDGkOdUX1Ujrrse-cdj20RRah9hyHdxBu), where we have guests on to talk about how to use Grafana, observability, or visualization. I saw your [blog post/video/post] on [source] and I think it would be great to have you on the show to share your experience about [topic].
	Office Hours is an hour-long live conversation that is streamed to the [Grafana YouTube channel](https://youtube.com/@grafana). It's very casual, and you can also share your screen if you'd like to do a demo (not required). If you'd like to join, I'd love to have you! 
- [x] If the guest agrees, choose a date for the Office Hours session. Check [the Monday board](https://grafana-labs.monday.com/boards/5724430500) to make sure no other livestream is scheduled for that day. Add a card for that date and time to save the spot.
- [x] Confirm the time (16:00 CEST on Friday is generally best) with the guest. Ask them for a photo you can use for promotion, or ask for permission to use their profile pic on social media.
- [x] Invite them to the Grafana Office Hours calendar invite (choose "this instance only", not the whole series). Schedule the invite for 15 minutes before the stream (to do a tech check) until 15 minutes after the stream (to debrief). The invite should be for 1.5 hours total. Explain this to them.
- [x] Create a thumbnail on [Canva](https://canva.com) using the Grafana Office Hours thumbnail format. Use [thumbsup.tv](https://thumbsup.tv) to check how the thumbnail looks on different devices. [Here are some guidelines for creating thumbnails](https://notes.nicolevanderhoeven.com/Create+engaging+thumbnails).
- [x] Schedule the broadcast on [Streamyard](https://streamyard.com), and select the Grafana YouTube channel as the destination.
	- [x] In the title, include the instance of Office Hours, i.e. `What's new in Grafana 10? (Grafana Office Hours #01)`. Including the number or the date (such as `All About Explore Logs (Loki Community Call November 2024`) helps people remember it.
	- [x] Add the standard description as per previous Grafana Office Hours shows. Check the video description and add guests' contact details.
- [x] Get familiar with how to use Streamyard. [Here's a crash course on how to use Streamyard](https://drive.google.com/file/d/1hb8FeoO88zinZu638MfnBwGctyspgfm0/view?usp=drive_link) and [here's a second recorded call with the Grafana Campfire hosts](https://drive.google.com/file/d/1hdX4SvDM67KRwGkzA6HWEETK1-gy8iUk/view?usp=drive_link) to get them onboarded with Streamyard. These include how to create the stream on Streamyard.
- [x] Get the Streamyard invite link and put it in the "location" of the calendar invite to the guest.
- [x] Get the YouTube link to the show. Put the link on this page, in the URL property above.
- [ ] Create an event and announce it [on the Grafana Meetup page](https://www.meetup.com/grafana-friends-virtual-meetup-group/).
- [x] Create a post on the community forum. ([link](https://community.grafana.com/t/loki-community-call-july-2025-how-to-generate-metrics-from-logs-metric-queries/153794))
- [ ] Schedule posts on socials just when the show begins to say "We're live now!" [Buffer](https://buffer.com/) is a good free tool to use for this. Set it up for your socials and be sure to tag/mention the official Grafana account-- they'll usually boost/repost it if you do.
- [ ] Schedule a Slack message on the internal Grafana workspace (in `#community`, `#content-video`, `#video-offsite-2025-futurism`, and anywhere else you think it might be relevant). Yes this is excessive. Let's change this process!
- [ ] Schedule a Slack message on the public Grafana Slack workspace (in the appropriate channel, such as `#loki` or `#announcements`).
- [x] Add your call to the Community Calendar (ask David, Richi, Nicole, and Usman).
- [x] Think of any reference links you might want to give the audience. Add it to the YouTube description.

## Talking points

> Enumerate talking points for the show. It's better to keep these as bullet points to encourage a more casual, rather than scripted, conversation.

- Announcements
	- Loki Helm Maintainers! (Jay)
- Intro to Cyril-- his work on Loki, and what he's working on now
	- Last time, we talked about [query best practices](../../transcripts/2024-12-06T05:24:36Z-grafana-loki-query-best-practices-with-logql-loki-community-call-december-2024.md) with Cyril, but we didn't really get a chance to discuss metric queries.
- Metric query basics
	- What is a metric query?
	- How is it different from a log query?
	- Is the syntax for metric queries any different? How similar is it to PromQL?
	- Why would you turn logs into metrics instead of just collecting metrics? (advantages and disadvantages/use cases)
	- Can you only do aggregations with metric queries, or can you also transform them (conversion between units for example)?
	- When should you do a metric query and when should you use Grafana transformations?
- Demo: examples of metric queries (show on Grafana Play)
	- What are good use cases for metric queries?
- Are there best practices for labels when you know you're going to be using them for metric queries? What makes a label set good for aggregation?
- Types of metric queries
	- What are the types of metric queries?
	- What's a range vector aggregation? Are all metric queries range vector aggregations?
	- What's the difference between a log range aggregation and an unwrapped range aggregation?
	- What does it mean to "unwrap" an aggregation?
	- There's a `vector()` function that turns a scalar into a vector. What's a scalar, what's a vector, and why would you want to turn one into the other?
	- What's the difference between `count_over_time()` and `rate()`? When should you use one over the other? Are there performance impacts?
	- How does Loki compute `rate()` under the hood? Is it true streaming rate or derived from sampled intervals?
	- **How does LogQL handle missing time buckets or sparse log streams in metric queries?**  (like during service downtime or when log volume is very low)
- Alerting
	- Can you create an alert based on a metric query?
	- **How should you tune alert thresholds and evaluation windows when working with logs?** For example, how do you avoid alert fatigue due to bursty log patterns?
	- **How would you build an alert to detect anomalous behavior (not just static thresholds) using logs?** Are there patterns for outlier detection?
- Performance consideration for metric queries
	- What are some do's and don'ts for using metric queries?
	- Are metric queries slower or faster than log queries?
- In the future
	- Will metric queries become faster with the adoption of some of the changes coming in Loki 4.0 (columnar store, new query engine)?


### Community questions

> [!question] Avanish Vaghela
> Hey Nicole, It would be great if we can get some advice on running metrics queries on tens of terabytes of logs. I am well aware that current Loki architecture is not designed for such use case and Loki 4.0 will greatly improve the performance in this area but any tips on what we can do improve the performance in the meanwhile would be great.

> [!question] Wilfried Roset
> I quite interested about the `rate` in logql and weither or not they have the same unexpected behavior as they do in promql due to the extrapolation.  
> Beware this is a tricky topic even the prom community has a hard time with it.  
> The back-story: [https://github.com/prometheus/prometheus/issues/3746](https://github.com/prometheus/prometheus/issues/3746)  
> The new attempt to address this: [https://github.com/prometheus/proposals/pull/52](https://github.com/prometheus/proposals/pull/52)

> [!question] Andre Ziviani
> Some examples using `unwrap` and, I’m not sure if it is possible, actually parse/convert the unit of the field (e.g.  a `size` field that have dynamic unit like `100 MB` and `1 GB`)

> [!question] Avanish Vaghela
> It would be good to know what kind of performance impact does structure metadata and different parsers have on the metrics queries.

- [damienclark](https://community.grafana.com/t/possible-to-conditionally-disable-metric-query/14438) from Community Forum: When using a metric query as a variable in a Grafana dashboard, can you conditionally disable a metric if it's null?

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

