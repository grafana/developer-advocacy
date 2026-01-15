---
url: https://www.youtube.com/watch?v=LfDVygRWQJU
date: 2026-01-21
---

# [[043 - Observability for GenAI Apps]]

[Link to YouTube video](https://www.youtube.com/watch?v=LfDVygRWQJU)

Guests:: "Ishan Jain, Luccas Quadros"

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
	- Register for [OpenTelemetry Unplugged](https://events.humanitix.com/otelunplugged-eu2026)
	- TODO
- Introduce guest: Ishan Jain, Luccas Quadros
	- Who are you?
	- What do you do?
- [ ] What’s Generative AI and how do we use it in software?
- [ ] What’s special about Generative AI that requires new observability approaches
  - Non-deterministic LLM responses, dynamic agentic flows, variability, and hallucinations
    - We can’t rely on unit tests to validate response contents
    - We often need another model, or humans, or both to evaluate output quality
    - How can we test the AI part before hitting production and real users?
  - Traditional RED metrics still apply, but they’re not enough
  - New usage patterns, new scenarios, and fast-moving technology
  - **For AI builders**: Infra around models themselves is new
    - Self-hosted models need more HW (e.g. GPU) insights
    - Model training, fine-tuning
  - **For AI users:** we need to record more context:
    - Prompts and completions, configuration
    - Token counts, usage, and costs
    - Streaming details (time-between-chunks)
    - Evaluations correlated with other telemetry
- [ ] Demo (Ishan)
  - Show trace of a couple of agents working on a problem
  - Exploring traces and AI dashboard in Grafana Cloud
-  [] Debugging and data retention challenges
   - Debugging individual operations often depends on prompts and completions being recorded. Also needed for evals and sometimes audit
   - How to handle sensitive user inputs?
   - Volume is a real problem. Do we record images or videos as telemetry?
   - **How this works in practice today**
     - How this is handled in OpenTelemetry
     - What wider industry instrumentations do
     - How Grafana Assistant approaches it
- [ ] Evaluations
  - What evaluations are and how to run them
    - Using models to judge models
    - Recording human feedback
  - Should evaluations run on top of telemetry or independently?
- [ ] Agentic workflows at scale
  - It’s 2026 and agentic workflows are everywhere. Multiple agents with their own toolsets are common. Does this change how we observe them?
  - Distributed tracing records and correlated all layers - agent loops, tools and LLM calls
  - What do we evaluate: individual LLM calls, agents, or orchestration layers?
- [ ] Where the ecosystem is today
  - Current common practices and gaps
  - What’s happening in the OTel GenAI SIG
  - Polishing LLM semantic conventions
  - Working on agentic conventions
  - Expanding instrumentation coverage
  - Evolving content-upload hooks
  - Many instrumentations exist today (Traceloop, OpenInference, OpenLit, and others)
  - Most are interested in OTel standards
  - Adoption is partial, and standardization takes time

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
- [ ] Add the video to video playlists that make sense (at the very least, the "Grafana Grafana OTel Community Call" one.)
- [ ] Download all videos for the recording on Streamyard and upload it [to this shared drive](https://drive.google.com/drive/folders/1sLnnYzmphet7K7QwogcZrYDI-Re07HS4) in the appropriate folder.
- [ ] Think about how you could repurpose this content. [This Loki Community Call](https://youtube.com/live/XJMQbEuBeMc) on Explore Logs was turned into [these](https://youtube.com/shorts/6RfI5UeJo08) [two shorts](https://youtube.com/shorts/jx1DATkGIz4) (*Short - Grafana Cloud Explore Apps for no-code querying of Loki, Mimir, Tempo, Pyroscope* and *Short - How to enable Explore Logs app for Grafana*) and [this shorter video](https://youtu.be/eXwE2vqLcyY) (*How to use the Explore Logs app for Grafana*) + docs.
- [ ] Update [Advocate Contributions sheet](https://docs.google.com/spreadsheets/d/1LataDRRX4DZy8VnCiBDXmynjmpOJdibM7ek_uvpim4Y/edit?gid=0#gid=0) with your work.
- [ ] Let's try promoting content on Grafana socials after this call this time (twitter, bsky, linkedin)

### Timestamps

00:00:00 Introductions

