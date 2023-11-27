---
url: https://youtube.com/live/-_SsFLoJvoc
date: 2023-11-24
---
# [[GOH 21 - How to use flow mode for Grafana Agent with Matt Durham]]

<iframe width="560" height="315" src="https://www.youtube.com/embed/-_SsFLoJvoc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Guest:: Matt Durham

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
- [ ] Create an event and announce it [on the Grafana Meetup page](https://www.meetup.com/grafana-friends-virtual-meetup-group/).
- [ ] Schedule a tweet just when the show begins to say "We're live now!"
- [x] Schedule a Slack message on the internal Grafana workspace (in `#community`).
- [x] Schedule a Slack message on the public Grafana Slack workspace (in `#announcements`)


## Talking points

> Enumerate talking points for the show. It's better to keep these as bullet points to encourage a more casual, rather than scripted, conversation.
  
- Intro
	- *Hello and welcome to Grafana Office Hours. I'm `<name>`, a `<position>` at Grafana Labs and today, we're going to talk about Grafana Agent Flow mode: what it is, how it's different from static mode, and how to use it.*
- Announcements
	- What is Devops?: https://www.youtube.com/watch?v=gmrbHD6UbAE
	- Grafana k6 for beginners: Why observability needs testing https://www.youtube.com/watch?v=1mtYVDA2_iQ
	- Observability survey: https://docs.google.com/forms/d/e/1FAIpQLSfEDVCT0Wax4CdZxy2t4Z_P2lg8JPZDCeW3BlcEJPeOz4e-aw/viewform
		- tools you're using
		- whether or not you're using AI, and how
		- what are you excited about
		- your observability strategy
		- Last year's results: https://grafana.com/observability-survey-2023/?pg=blog&plcmt=body-txt#quantifiable-impact-of-observability
- Introduce guest: Matt Durham
	- Who are you?
	- What do you do?
- What is Grafana Agent?
	- Grafana Agent is a vendor nuetral signal collector. See Paschalis office hours session for a great dive into what the Agent is: https://youtube.com/live/i0mA0w_MCPQ
- What is static mode?
	- What does it look like?
	- What are the things that are not so good about it?
		- Data pipelines are hard to do in YAML. What are data pipelines and why are they important?
		- Flow is OTel native, more big tent than static (which is only Prometheus)
- What is Flow?
	- Flow is our new mode of the Agent Collector that is all about building telemetry pipelines. The previous iteration Static was built in a very prometheus way. The original concept was that the Agent was a lightweight version of Prometheus for moving metrics. The ability to chain together components to make telemetry pipelines is key. Very much like a traditional ETL pipeline.
	- Short History
		- Discussions started almost 2 years ago between Robert Fratto and myself on how to improve the Agent.
- What is River?
	- River is a language we created based on HCL. Its based around the idea of *expressions*.
	- 

```
remote.secret_store "secret" {
    url = "[http://example.com/secret](http://example.com/secret)"
}

local.file "secret" {
   path = "/secret/pw.txt"
}

component.test "t1" {
    // Coalesce will return the first not blank value. With the last value being return regardless.   
    content =  coalesce(env("password"),local.file.secret.content,remote.secret_store.secret.value)
}
```

Note we also have static -> river converters that cover most use cases.

- Why did we invent our own language?
	- Flow is constantly being re-evaluated. HCL is a one-time runtime configuration. 
	- HCL was not as performant.
	- There is a lot of discussion in our github repository on this. The team iterated on several examples to see how the system would look and feel. The fact we wanted to create relationships and use expressions made this difficult and difficult to use.  Referencing other components and expressions would have led us to create our own parser for that and it ended up being very dense and error prone. This allows much better error messages to be sent to the user. *show this in demo*
- Why Flow?
	- What things were hard to do in static mode?
		- writing to multiple Prometheus Remote Write endpoints
		- converting Prometheus metrics
		- secret management
	- Better at error messages
	- Static mode hid complexity
		- Static mode was very easy to do simple things and impossible to do hard things. There was a lot of magic on how remote writes and integrations worked from both a user perspective and developer perspective.
	- Drive more contributions
		- Adding new features to static mode was difficult for developers since how the individual items iteracted. In Flow components are driven by inputs and outputs, so a developer can create a component that accepts an input and exports an output without caring how it works in the bigger picture.
	- Allow more use cases beyond telemetry
		- Ingesting of rules from kubernetes crds is our first example but we imagine it will grow as time increases. The black box nature of components allows quick creation.
	- Documentation
		- Static mode is a collection of other projects rolled into one, and in most of those cases the team reused the available YAML config and exposed that config directly. This could create a drift between the documentation the team documented versus what was available. This also led to documentation being linked to external sources. Now all config is documented in a very standard way. This reference documentation is pretty high quality and standardized. Task based documentation is coming.
	- Better support and integration for advanced features
		- **Clustering** has allowed the team to reduce Agent costs by 50%, previously we used hashmod which duplicates metrics to ensure high availability. Clustering allows us to ensure metrics are only read by one source. Each component can implement clustering as the component sees fit which allows smaller more focused changes compared to static. 
	- UI
		- DAG of all the entire data pipeline, all the inputs and outputs
		- Shows dependencies
- Performance of flow is within 1-2% of static mode. HCL had worse performance.
- Demo Flow and its interesting use cases
	- Conversion of prometheus metrics and logs to otlp.
- Unique features to flow
	* Clustering
		* vs hashmod sharding
			- write the data twice to ensure high availability (very expensive to do)
			- you have to know how many nodes you're running beforehand
			- you hash the metric name and get a number. If you have five shards, the number would be 0-4. Specify the shard and if it matches, keep it. Otherwise drop it. This is scalability but not availability.
			- flow is more flexible: you can add or remove a mode
	* OTLP support
		* static mode: Tempo (OTel)
		* flow mode: all OTel
	* config conversions available for Prometheus and static mode to flow (in most cases)
		* Promtail to Agent transition
	* more than just telemetry: you can do rules (alerting from CRD in k8s to Mimir cluster)
	* better community contributions
	* Continuous profiling support via Pyroscope
		- eBPF-based profiling
	- built-in UI
* Installation changes
	* Helm chart
	* rpm and deb for Linux
	* any Agent executable can run flow
* Limitations of Flow
- Future of Flow
	- Go over our future plans.
	- Feature parity already between flow and static
	- When is static mode going away?
		- A long time in the future, yes
	- "modules"
		- groups of components that solve a particular problem
		- listing of prepackaged solutions
	- share config
- Outro
	- If people want to learn more about this topic, where should they go?
	- Next week, we're talking to Joseph Elliot all about Grafana Tempo.

### Just before the show

> Here are some points to discuss with the guest in the 15 minutes before the stream begins.

- [x] How do you pronounce your name?
- [x] What are your pronouns?
- [x] We will be using the talking points, but we don't have to be strict about it. We don't have to go through all of them, or follow a specific order. They're only there to make us comfortable.
- [x] Does anyone want to share their screen? We can do that now, and I can show you how that works
- [ ] We'll be streaming to YouTube.
- [ ] You'll be able to see comments, but if you have links, I have to paste it into the private chat.
- [ ] You can also use the private chat if you need to say something, but you can also just say it out loud.
- [x] If at any point you aren't comfortable talking about something, please either say so or let me know in the private chat, and I'll pivot away from that topic.
- [ ] Afterwards, we'll say goodbye to the stream, but please stay on past that so we can debrief.
- [x] Just in case I disconnect... stall for a minute and I'll be right back.

## After the show

- [ ] Add timestamps to the video (at least four).
- [ ] Add any links shared to the description of the video.
- [ ] Add the video to video playlists that make sense (at the very least, the "Grafana Office Hours" one.)