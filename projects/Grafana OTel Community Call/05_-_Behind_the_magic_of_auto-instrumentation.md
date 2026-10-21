---
url: https://youtube.com/live/HItumi3qt90
date: 2026-02-27
---

# [[043 - Observability for GenAI Apps]]

[Link to YouTube video](https://youtube.com/live/HItumi3qt90)

Guests:: "Jay DeLuca"

## Pre-show checklist

- [x] Create a new `.md` file and copy this template into it. Check things off as you work through it.
- [x] Update [Grafana OTel Community Call Readme](/projects/Grafana%20OTel%20Community%20Call.md) to add the new file to the `Upcoming` section.
- [x] Contact the guest and tell them about Grafana OTel Community Call.
	> At Grafana Labs, we do a livestream called [Grafana OTel Community Call](https://www.youtube.com/watch?v=uk7NoagbJ28&list=PLDGkOdUX1Ujrrse-cdj20RRah9hyHdxBu) - TODO, where we have guests on to talk about OpenTelemetry and Grafana working together to provide observability. I saw your [blog post/video/post] on [source] and I think it would be great to have you on the show to share your experience about [topic].
	Grafana OTel Community Call is an hour-long live conversation that is streamed to the [Grafana YouTube channel](https://youtube.com/@grafana). It's very casual, and you can also share your screen if you'd like to do a demo (not required). If you'd like to join, I'd love to have you!
- [x] If the guest agrees, choose a date for the Grafana OTel Community Call session. Check [the Monday board](https://grafana-labs.monday.com/boards/5724430500) to make sure no other livestream is scheduled for that day. Add a card for that date and time to save the spot.
- [x] Confirm the time with the guest. Ask them for a photo you can use for promotion, or ask for permission to use their profile pic on social media.
- [x] Invite them to the Grafana OTel Community Call calendar invite (choose "this instance only", not the whole series). Schedule the invite for 15 minutes before the stream (to do a tech check) until 15 minutes after the stream (to debrief). The invite should be for 1.5 hours total. Explain this to them.
- [x] Create a thumbnail on [Canva](https://canva.com) using the Grafana OTel Community Call thumbnail format. Use [thumbsup.tv](https://thumbsup.tv) to check how the thumbnail looks on different devices. [Here are some guidelines for creating thumbnails](https://notes.nicolevanderhoeven.com/Create+engaging+thumbnails).
- [x] Schedule the broadcast on [Streamyard](https://streamyard.com), and select the Grafana YouTube channel as the destination.
	- [x] In the title, include the instance of Grafana OTel Community Call, i.e. `Declarative Configuration (Grafana OTel Community Call #01)`. Including the number or the date (such as `All About Explore Logs (Loki Community Call November 2024`) helps people remember it.
	- [x] Add the standard description as per previous Grafana OTel Community Call shows. Check the video description and add guests' contact details.
- [x] Get familiar with how to use Streamyard. [Here's a crash course on how to use Streamyard](https://drive.google.com/file/d/1hb8FeoO88zinZu638MfnBwGctyspgfm0/view?usp=drive_link) and [here's a second recorded call with the Grafana Campfire hosts](https://drive.google.com/file/d/1hdX4SvDM67KRwGkzA6HWEETK1-gy8iUk/view?usp=drive_link) to get them onboarded with Streamyard. These include how to create the stream on Streamyard.
- [x] Get the Streamyard invite link and put it in the "location" of the calendar invite to the guest.
- [x] Get the YouTube link to the show. Put the link on this page, in the URL property above.
- [x] Create an event and announce it [on the Grafana Meetup page](https://www.meetup.com/grafana-friends-virtual-meetup-group/).
- [x] Schedule a Slack messages:
  - [x] internal slack: `#opentelemetry`
- [x] Announce in `#community-champions` and `#opentelemetry` community slack channels and ask for questions.  Yes this is excessive. Let's change this process!
- [x] Schedule a Slack message on the public Grafana Slack workspace (`#opentelemetry`).
- [x] Add your call to the Community Calendar
- [ ] Think of any reference links you might want to give the audience. Add it to the YouTube description.

## Talking points

> Enumerate talking points for the show. It's better to keep these as bullet points to encourage a more casual, rather than scripted, conversation.

- Intro
	- *Hello and welcome to Grafana Grafana OTel Community Call. I'm `<name>`, a `<position>` at Grafana Labs and today, we're going to talk about `<topic>`.*
- Announcements
	- Grafana Con ?
- Introduce guest: Jay DeLuca
	- Who are you?
	- What do you do?
- [ ] Java Agent “Magic” Demo
  - Drop in the Java agent and show that a lot of telemetry is collected instantly.
  - What’s included by default: HTTP / RPC, Databases, Messaging, JVM runtime metrics, Spring, etc
  - How does the agent actually work under the hood?
  - What are the other ways to onboard to OpenTelemetry (e.g., manual instrumentation)?
  - This is awesome and covers application observability really well — but are there challenges?
- [ ] The Discoverability Problem
  - How do I know if a specific library or framework is instrumented?
  - How many instrumentations are there?
  - How do I know what telemetry they emit?
  - Do they follow semantic conventions?
  - What configuration options are available?
  - How do I know what changes between versions?

- [ ] Making It Discoverable: Ecosystem Explorer
  - Demo of the Ecosystem Explorer
  - How does it help with transparency?
- [ ] Project Status & Vision
  - Can people try it today?
  - Where is the project heading?
  - What are the dreams and big goals?
  - How is it related to: https://opentelemetry.io/ecosystem/ and the OpenTelemetry Registry?
- [ ] Semantic Conventions & Stability
  - What are OpenTelemetry Semantic Conventions?
  - How should people think about instrumentation stability when conventions aren’t stable?
  - Can we associate semantic conventions with specific instrumentations or versions?
  - How does this connect with Weaver (the tool for writing, validating, and checking conventions against emitted telemetry)?
- [ ] The Human Side
  - Jay’s OTel story: How did you start contributing?
  - How did you become an approver and project lead?
  - What are the most important challenges OpenTelemetry should tackle next?
  - How can someone get involved in the Ecosystem Explorer?

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

- [x] Add timestamps to the video (at least four).
- [ ] Add any links shared to the description of the video.
- [ ] Add YouTube cards when relevant to certain points during the video.
- [x] Add the video to video playlists that make sense (at the very least, the "Grafana OTel Community Call" one.)
- [ ] Download all videos for the recording on Streamyard and upload it [to this shared drive](https://drive.google.com/drive/folders/1sLnnYzmphet7K7QwogcZrYDI-Re07HS4) in the appropriate folder.
- [ ] Think about how you could repurpose this content. [This Loki Community Call](https://youtube.com/live/XJMQbEuBeMc) on Explore Logs was turned into [these](https://youtube.com/shorts/6RfI5UeJo08) [two shorts](https://youtube.com/shorts/jx1DATkGIz4) (*Short - Grafana Cloud Explore Apps for no-code querying of Loki, Mimir, Tempo, Pyroscope* and *Short - How to enable Explore Logs app for Grafana*) and [this shorter video](https://youtu.be/eXwE2vqLcyY) (*How to use the Explore Logs app for Grafana*) + docs.
- [ ] Update [Advocate Contributions sheet](https://docs.google.com/spreadsheets/d/1LataDRRX4DZy8VnCiBDXmynjmpOJdibM7ek_uvpim4Y/edit?gid=0#gid=0) with your work.
- [ ] Let's try promoting content on Grafana socials after this call this time (twitter, bsky, linkedin)

### Timestamps

00:00:00 Introductions

