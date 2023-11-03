---
url: https://www.youtube.com/watch?v=8Z67vAkv3J0
date: 2023-11-03
---
# [[GOH 18 - Combining frontend and backend performance with John Hill]]

<iframe width="560" height="315" src="https://www.youtube.com/embed/8Z67vAkv3J0?si=M_fAz2K5g1u2OqOd" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Guest:: John Hill

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


## Talking points

> Enumerate talking points for the show. It's better to keep these as bullet points to encourage a more casual, rather than scripted, conversation.

- Intro
	- *Hello and welcome to Grafana Office Hours. I'm `<name>`, a `<position>` at Grafana Labs and today, we're going to talk about `<topic>`.*
- Announcements
	- New project releases
	- Recent content published
		- [Grafana for Beginner series!](https://www.youtube.com/watch?v=TQur9GJHIIQ) 
- Introduce John
	- Who are you?
	- What do you do?
	- How long have you been using Grafana/other project?
- The stack
- What is Open MCT?
	- k6
	- k6 browser
	- Prometheus
		- because YAMS (backend that provides a native Prometheus endpoint)
	- Grafana
- Why is performance important?
- What makes Open MCT performance different (openmct-performance)?
  - Why does it exist?
  - Is it using Grafana and k6?
- What are some general performance problems you see?
	- Performance tuning: what can you do with limited time to improve performance?
	- How to have gentle conversations with architects to tell them what's not working
	- Frontend application sending too many requests to the backend (Open MCT can take the blame for backend problems)
	- Siloes that can happen if frontend and backend teams are not communicating
	- Synthetic monitoring is fragile and owned by the wrong team
- What's been your history in using performance tools before k6?
- How are you combining Grafana and k6 to test the frontend and backend performance of your application?
- Why k6 browser?
	- Already using k6 on protocol-level
	- Recommended practices you've shared with the community
		- Do everything you can to actually demonstrate what a user is going to do
			- Add think time
		- Use consistent locator logic
			- Aria locators use screenreader locators
			- Talk to developers
			- Make locator changes yourself to make your tests more resilient
			- "Self-healing"
        - It's easy to export data to different data sources
        - Working closely with developers (selector example)
        - Hybrid testing
	        - Contract-based UI testing approach (keeping your tests in sync with the development)
	        - Synthetic user monitoring (how can you use k6 browser for this?)
	        - Using the same tooling
        - What use cases or scenarios can you think of where k6 browser is not a good fit?
- Demo?
	- openmct-performance and k6
	- Recording a browser test with playwright 
	- Record and convert har files using har-to-k6 plugin
	- Hybrid performance test?
	- Exporting data to Prometheus and Visualizing results to Grafana
- Outro
	- If people want to learn more about this topic, where should they go?
        - Contributors wanted! (Open e2e Test Initiative)
	- Next week: PLZv2 with Olha and Daniel

### Just before the show

> Here are some points to discuss with the guest in the 15 minutes before the stream begins.

- [x] How do you pronounce your name?
- [x] What are your pronouns?
- [ ] We will be using the talking points, but we don't have to be strict about it. We don't have to go through all of them, or follow a specific order. They're only there to make us comfortable.
- [x] Does anyone want to share their screen? We can do that now, and I can show you how that works
- [ ] We'll be streaming to YouTube.
- [ ] You'll be able to see comments, but if you have links, I have to paste it into the private chat.
- [ ] You can also use the private chat if you need to say something, but you can also just say it out loud.
- [ ] If at any point you aren't comfortable talking about something, please either say so or let me know in the private chat, and I'll pivot away from that topic.
- [ ] Afterwards, we'll say goodbye to the stream, but please stay on past that so we can debrief.
- [ ] Just in case I disconnect... stall for a minute and I'll be right back.

## After the show

- [ ] Add timestamps to the video (at least four).
- [ ] Add any links shared to the description of the video.
- [x] Add the video to video playlists that make sense (at the very least, the "Grafana Office Hours" one.)
