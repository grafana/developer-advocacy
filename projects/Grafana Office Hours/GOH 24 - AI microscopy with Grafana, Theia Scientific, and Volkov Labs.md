---
url: https://youtube.com/live/BgRd-RAFMEE
date: 2023-12-15
---
# [[GOH 24 - AI microscopy with Grafana, Theia Scientific, and Volkov Labs]]

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
- [x] Schedule posts on socials just when the show begins to say "We're live now!"
- [x] Schedule a Slack message on the internal Grafana workspace (in `#community`).
- [x] Schedule a Slack message on the public Grafana Slack workspace (in `#announcements`)

## Reference links

How Theia Scientific and Volkov Labs use Grafana and AI to analyze scientific images (blog): https://grafana.com/blog/2022/04/29/how-theia-scientific-and-volkov-labs-use-grafana-and-ai-to-analyze-scientific-images/
Using Grafana and machine learning for real time microscopy image analysis (video of talk at GrafanaCONline 2022): https://www.youtube.com/watch?v=WRPnTFBX4rg
How to create an ideal Grafana dashboard for science and engineering (blog): https://grafana.com/blog/2023/08/04/how-to-create-an-ideal-grafana-dashboard-for-science-and-engineering/


## Timestamps



## Talking points

> Enumerate talking points for the show. It's better to keep these as bullet points to encourage a more casual, rather than scripted, conversation.

- Intro
	- *Hello and welcome to Grafana Office Hours. I'm `<name>`, a `<position>` at Grafana Labs and on this show, we often talk about observability of computer systems. Today, though, we're talking about observability of a different nature. Our guests today have built a platform called Theiascope that uses Grafana, among other things, to collect and analyse images from microscopes.*
- But first, some announcements!
	- Releases
		- Grafana Agent v0.38: https://grafana.com/blog/2023/11/29/grafana-agent-v0.38-release-new-opentelemetry-components-configuration-improvements-and-more/
			- new OTel components for Flow mode
		- k6 v0.48: https://grafana.com/blog/2023/12/14/new-in-grafana-k6-the-latest-oss-features-in-v0.48.0-and-user-defined-project-limits-in-grafana-cloud-k6/
			- `k6 new`, performance insights for browser
	- The Story of Grafana: Community: https://youtu.be/lbBQk_QPnEs
	- Grafana for Beginners series: How to download and run Grafana on macOS: https://www.youtube.com/watch?v=T51Qa7eE3W8
- Introduce guests
	- Christopher Field: Co-Founder/President/Principal Investigator
		- What is Theia Scientific?
			- experts in edge computing architectures for scientific instrumentation, data analysis, AI model development
			- originally a hobby project
	- Mikhail Volkov: Founder/CEO
		- What is Volkov Labs?
			- agency that develops custom plugins for Grafana
		- When did you first start using Grafana?
- Walk us through the process of manual analysis
	- What is microscopy?
	- What are you analysing? : black dots on white backgrounds
	- The problem with microscopy
		- abundance of data! How do you analyse it?
		- needs to be real-time
	- How can AI help? What are the problems associated with AI?
- What is the Theiascope?
	- What does your stack look like?: Grafana, Prometheus, (eventually) Loki, live streaming, PostgreSQL/Timescale, Docker
	- What issues did you encounter when adapting Grafana for your needs?
	- What plugins did Mikhail create, and are they opensourced?
- End result with Grafana: 80% improvement in time and cost over manual post-acquisition image analysis
- What do you wish were better?
- Outro
	- If people want to learn more about the Theiascope or your work at Theia Scientific or Volkov Labs, where should they go?

### Just before the show

> Here are some points to discuss with the guest in the 15 minutes before the stream begins.

- [ ] How do you pronounce your name?
- [ ] What are your pronouns?
- [x] We will be using the talking points, but we don't have to be strict about it. We don't have to go through all of them, or follow a specific order. They're only there to make us comfortable.
- [x] Does anyone want to share their screen? We can do that now, and I can show you how that works
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