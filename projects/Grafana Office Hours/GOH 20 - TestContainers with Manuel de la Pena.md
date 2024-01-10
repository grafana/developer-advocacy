---
url: https://www.youtube.com/watch?v=LtlRvmWzCRE
date: 2023-11-17
---
# [[GOH 20 - Testcontainers with Manuel de la Peña]]

<iframe width="560" height="315" src="https://www.youtube.com/embed/LtlRvmWzCRE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Guest:: Manuel de la Peña ([AtomicJar](https://www.atomicjar.com/)), Pablo Chacin (Grafana)

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

## Description

```
In this episode of Grafana Office Hours, we talk about realistic unit tests utilizing actual instances of databases and other dependencies. We'll be joined by Manuel de la Peña from AtomicJar, and Pablo Chacin from Grafana to learn how we can use the Testcontainers open-source framework to create lightweight, throwaway dependencies for our tests.

Testcontainers: https://testcontainers.com/
k3s Module: https://testcontainers.com/modules/k3s/
k6 Module: https://testcontainers.com/modules/k6/

---
Contact Manuel:
X: https://twitter.com/mdelapenya
GitHub: https://github.com/mdelapenya

Contact Pablo:
X: https://twitter.com/pablochacin
GitHub: https://github.com/pablochacin

Contact Nicole:
Mastodon: https://pkm.social/@nicole
GitHub: https://github.com/nicolevanderhoeven
Site: https://nicolevanderhoeven.com

Contact Paul:
X: https://twitter.com/javaducky
GitHub: https://github.com/javaducky
Site: https://javaducky.com/

Learn more about Grafana Labs:
Website: https://grafana.com
Repo: https://github.com/grafana/grafana
```

## Talking points

> Enumerate talking points for the show. It's better to keep these as bullet points to encourage a more casual, rather than scripted, conversation.

- Intro
	- Introductions all around: who are you, and what do you do?
- But first: Announcements
	- Nicole and Marie Cruz have been at Agile Testing Days (*Adobo & Avocados: Intersectionality in Tech and DevRel*): https://agiletestingdays.com/2023/session/adobo-and-avocados-intersectionality-in-tech-and-devrel/
		- We shall see what happens as the lunatic(s) run the asylum!
	- [ObservabilityCON 2023](https://grafana.com/about/events/observabilitycon/2023/opening-keynote-event/) happened this week where there were some major announcements
		- [Application Observability](https://grafana.com/blog/2023/11/14/announcing-application-observability-in-grafana-cloud-with-native-support-for-opentelemetry-and-prometheus/)
		- [Grafana Beyla](https://grafana.com/blog/2023/11/14/grafana-beyla-1.0-release-zero-code-instrumentation-for-application-telemetry-using-ebpf/)
		- Acquisition of [Asserts.ai](https://grafana.com/blog/2023/11/14/grafana-labs-acquires-asserts/)
		- [Sift](https://grafana.com/docs/grafana-cloud/alerting-and-irm/machine-learning/sift/) for response management
		- What is Devops?: https://www.youtube.com/watch?v=gmrbHD6UbAE
- Feature discussion
	- This _WAS_ originally going to be on Cafe Con Grafana since everyone is a spanish speaker
	- Introduction to Testcontainers (Manu)
		- Testcontainers
			- set of Java, .NET, Golang, Node.js, Scala, Rust, Elixir libraries (but mostly Java) that exposes HTTP endpoints to interact with Docker and spin up images within the script.
			- Lets you expose ports, use conditional logic
		- Who is AtomicJar? - created testcontainers
			- Hires maintainers (Node.js, java, Go)
		- Is this for integration tests or unit tests?
			- Whatever works for you
			- Breaks down silos between dev, test, ops
			- Semantics of "unit" vs "integration" vs "e2e" lose meaning when you can do e2e in application code.
	- How we are using TC in k6 for e2e tests  (Pablo and Manu)
		- Was this "scratching an itch" for a project?
		- Running k6 image within the code using Testcontainers
	- K3s module
		- I'll be trying this out!
	- k6 module
		- Noticed this is missing for Java implementation...I may have to dust off my IDE and take a look
	- Demo (Pablo)
	- Looking for more contributions?
		- Are specific modules needed or in progress?
- Outro
	- If people want to learn more about this topic, where should they go?
	- How can people reach you?
	- Announcements
		- We're hiring! https://grafana.com/about/careers/open-positions/
			- [k6 core team](https://boards.greenhouse.io/grafanalabs/jobs/5007589004)
			- Synthetic monitoring
			- Developer Advocate
			- Community Manager
	- Next week: we're off for Thanksgiving in the US and Grafana shutdown day, so we'll be streaming a recorded episode about Grafana Agent's Flow mode.

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