---
url: https://youtube.com/live/6Ph5nvicm6M
date:
---
# [[GOH 30 - Direction of Grafana Loki, Mimir, Tempo, and Pyroscope]]

<iframe width="560" height="315" src="https://www.youtube.com/embed/" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Guest:: "Name"

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

- Intro and announcements
- Introduce guest: Dee Kitchen
	- they/them
	- VP of Engineering for Databases (Loki, Mimir, Tempo, Pyroscope)
- Briefly introduce the four databases and what telemetry signal they store
- Differences and similarities between the databases with regards to:
	- architecture: What architectural principles guide the design of all four systems? Are there common patterns or shared components?
	- How do you think about tradeoffs between indexing, compression, and query performance across these backends?
	- Prometheus influence
	- schema requirements
	- common issues among all four
	- How do you prioritize engineering effort and features across all four projects?
- Projects across all four
	- WarpStream
	- OTel compatibility
	- Performance
	- Adaptive Telemetry
	- Drilldown apps
- Focus: Loki
	- Loki famously avoids full-text indexing—what are the hardest challenges in maintaining query performance as data volume scales?
	- Current projects?
		- Replication Factor 1 - Project Thor
		- Extensible columnar storage
		- Scalable stateless query engine
- Focus: Mimir
	- What are the key architectural differences between Cortex and Mimir, and how have they improved scalability or operability?
	- How do you approach schema evolution in Mimir, especially when operating at scale across many tenants?
	- Current projects?
		- Project Sigyn
		- New query engine: https://grafana.com/docs/mimir/latest/references/architecture/mimir-query-engine/
- Focus: Tempo
	- Tempo uses a trace-by-ID model without indexing most attributes—how do you balance simplicity with user demands for flexible querying?
	- Are there plans to support more advanced trace analytics or custom aggregations?
	- Current projects?
		- 
- Focus: Pyroscope
	- Continuous profiling is still emerging—what’s unique or especially hard about storing and querying profile data?
	- How are you thinking about integrating pprof, eBPF, and other profiling sources going forward?
	- Current projects?
		- 
- Future changes coming (that we can talk about)
	- What about AI/ML? How do you see that fitting into the future of our databases?
		- Grafana Assistant
	- Have you thought about cross-database queries or unified ingestion pipelines?
	- What about unified storage between the projects? Why or why not?
	- ?
- Challenges
- Outro


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

