---
url: https://youtube.com/live/RXLavQT58YA
date: 2023-11-10
---
# [[GOH 19 - PLZv2 with Olha and Daniel]]

<iframe width="560" height="315" src="https://www.youtube.com/embed/" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Guest:: Olha Yevtushenko, Daniel González Lopes

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
This week, we're talking about how you can do load testing on Kubernetes with k6 Private Load Zones, a new feature on Grafana Cloud k6 that leverages the k6 Kubernetes operator to allow you to run distributed load tests against applications behind a firewall. Here to discuss this new feature are Senior Software Engineer Olha Yevtushenko, Product Manager Daniel González Lopes, Developer Advocate Paul Balogh, and Senior Developer Advocate Nicole van der Hoeven.

The Grafana k6 repo: https://github.com/grafana/k6
k6 operator repo: https://github.com/grafana/k6-operator
Docs on Private Load Zones in Grafana Cloud k6: https://grafana.com/docs/grafana-cloud/k6/author-run/private-load-zone-v2/

---
Contact Daniel:
LinkedIn: https://www.linkedin.com/in/danielgonzalezlopes/
GitHub: https://github.com/dgzlopes
X: https://twitter.com/dgzlopes

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
	- Today we're going to talk about two things:
		- k6 operator, a Kubernetes operator for k6 that lets you run distributed load tests from within your Kubernetes cluster
		- Private Load Zones, a Grafana Cloud k6 feature that uses k6 operator to let you run load tests on private infrastructure-- good for getting past firewalls.
	- Introductions all around: who are you, and what do you do?
- But first: Announcements
	- Catch me and Marie Cruz at Agile Testing Days on November 16th (*Adobo & Avocados: Intersectionality in Tech and DevRel*): https://agiletestingdays.com/2023/session/adobo-and-avocados-intersectionality-in-tech-and-devrel/
	- [ObservabilityCON 2023](https://grafana.com/blog/2023/11/02/observabilitycon-2023-a-sneak-peek-at-the-opening-keynote/)is coming up! Next Tuesday, November 14 at 13:30 GMT, the keynote will be streamed live. If you sign up for it (for free), you'll also be noticed when other on-demand sessions are made available.
- What is k6?
- What is k6-operator?: https://github.com/grafana/k6-operator
	- Previous k6 Office Hours episode on this: https://youtu.be/5d5zxsGz8L4
	- Why would someone run distributed load tests?
	- How do you install k6 operator?
		- Previously: `make deploy`
		- Now: bundle deployment and Helm chart are probably the way to go.
	- What is a CRD?
	- What is a Kubernetes operator?
	- (Demo) What does the config look like for the k6 operator?
	- This can be used for free distributed load testing with k6
- What is Private Load Zones?
	- What is a load zone?
	- Why might you want to use a private load zone?
		- When you want to run a load test *from* your own infrastructure
		- When you want to run a load test *against* an application on private infrastructure (not publicly exposed)
	- Previously covered on k6 Office Hours: https://youtu.be/sqKc95zdXyI
	- What did v1 look like?
	- What's changed in v2?
	- How do you set it up? (demo)
	- We're no longer promoting v1 - why?
	- What are the limitations of PLZv2?
		- Being able to use multiple private load zones. Only one per cluster.
		- No environment variable support.
		- Browser tests not supported yet.
		- Logs not yet exposed to the cloud.
	- Is this only on Grafana Cloud k6?
- Outro
	- If people want to learn more about this topic, where should they go?
	- How can people reach you?
	- Announcements
		- We're hiring! https://grafana.com/about/careers/open-positions/
			- [k6 core team](https://boards.greenhouse.io/grafanalabs/jobs/5007589004)
			- Synthetic monitoring
	- Next week: AtomicJar - TestContainers

### Just before the show

> Here are some points to discuss with the guest in the 15 minutes before the stream begins.

- [x] How do you pronounce your name?
- [ ] What are your pronouns?
- [x] We will be using the talking points, but we don't have to be strict about it. We don't have to go through all of them, or follow a specific order. They're only there to make us comfortable.
- [x] Does anyone want to share their screen? We can do that now, and I can show you how that works
- [x] We'll be streaming to YouTube.
- [x] You'll be able to see comments, but if you have links, I have to paste it into the private chat.
- [x] You can also use the private chat if you need to say something, but you can also just say it out loud.
- [x] If at any point you aren't comfortable talking about something, please either say so or let me know in the private chat, and I'll pivot away from that topic.
- [ ] Afterwards, we'll say goodbye to the stream, but please stay on past that so we can debrief.
- [ ] Just in case I disconnect... stall for a minute and I'll be right back.

## After the show

- [ ] Add timestamps to the video (at least four).
- [ ] Add any links shared to the description of the video.
- [ ] Add the video to video playlists that make sense (at the very least, the "Grafana Office Hours" one.)