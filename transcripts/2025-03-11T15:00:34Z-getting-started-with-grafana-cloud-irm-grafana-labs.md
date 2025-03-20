# Getting Started with Grafana Cloud IRM | Grafana Labs

In this video, Joey Orlando, Engineering Manager at Grafana, walks you through Grafana Cloud Incident Response Management ...

Published on 2025-03-11T15:00:34Z

URL: https://www.youtube.com/watch?v=Eu0iLDFVdy0

Transcript: Grafana alerting is a big deal on our
YouTube channel with some of our most popular videos all about it. So we totally get how important it is
to you. You know the basics of alerting. But have you heard of Grafana Cloud IRM? Grafana Cloud IRM or Grafana Cloud
Incident Response Management complements Grafana alerting in monitoring, resolving, and responding to incidents effectively. It's a new application that
combines the best of both worlds, Grafana Incidents and Grafana OnCall. It replaces the existing OnCall and
Incident plugins to provide you a more unified and seamless incident
management experience. In this video, my colleague and engineering
manager, Joey Orlando, will show you how to get started with
Grafana using his Home IOT system as the example scenario. He'll also give a quick overview on how
to migrate to Grafana Cloud IRM from PagerDuty. So if that is of interest,
let's go ahead and check it out. Hi, I'm Joey Orlando and
I'm an engineering manager
on the Grafana IRM team. Today I wanted to give you a
quick sneak peek into Grafana IRM. Grafana IRM unifies your
existing Grafana IRM workflows in Grafana OnCall and Grafana Incident
into one seamless experience. We decided to make this change as it sets
the stage for simplifying things like configuring your IRM
integrations and configuration, as well as providing a consistent
incident response and management user experience. If you're already using Grafana Oncall
where you're using Grafana Incident in Grafana Cloud, then what I about
share might look familiar to you. If you're not, then welcome to
Grafana IRM. I'll give you a quick, roughly five minute walkthrough
on how to get started. So when you first land in Grafana IRM,
you'll notice the My IRM landing page. This gives you a quick overview of alert
groups and incidents that pertain to you. I'll go over alert groups
and incidents shortly, but first, let's get an on-call schedule set up. So I've already gone ahead and set up
a simple schedule which follows the "follow the sun" on-call model. We have one engineer from NASA
or North America + South America, one from Europe and one from Asia.
On an eight hour rotation. Great. So next we'll quickly review my
own personal notification rules. These settings are specific to each
individual user in Grafana IRM, every user can configure their personal
notification rules to suit their preferences and how they want
to get notified about alerts. I'll go over the difference
between default and important
shortly, but for now, I just want to point out that
when I receive an important alert, I'd like to use the mobile push
important notification rule, which is a slightly elevated notification
in that it can override do not disturb mode on my phone. So a quick side note on
what I want to monitor here. I have a pretty unique use case. I want to monitor my home's IoT system, which includes my garden
and my aquarium. And yes, my team and my manager all get to be
on call for my personal home garden and aquarium, sorry to them, but hopefully
I don't forget to water my plants. So let's continue with setting
up our on-call setup here. We'll continue with escalation chains. So an escalation chain defines a series
of steps on how an incoming alert is escalated to you and your team. There's a lot of customization available
here so that you can tweak your team's escalation to best suit
your specific needs. I've already gone ahead and
configured a few escalation chains, two for my home garden and one for
my aquarium. The steps within these, which are pretty similar, I first sent a notification to the
on-call engineer from my schedule that we just saw. And one thing about escalation
chains is that my alerts will continue being escalated according
to the steps that I defined, so long as the alert is
still in a firing state, meaning that no one has acknowledged
resolved or silenced the alert. So here, if no one has acknowledged my alert, it's going to wait 15 minutes and
then notify the team's manager before repeating these steps all over again. My default escalation chain simply
sends out a default notification, whereas the critical escalation chain
sends out an important notification. And lastly, before we
continue our quick demo, let's set up the integration
with my home's IoT system. So integrations are the entry point
for alerts coming from your monitoring systems into Grafana IRM when Grafana
IRM receives an alert from your external system, we'll try to group these alerts into what
we call alert groups based on whether or not there's an existing firing alert
group, which has a similar grouping id, which is just the type of
template that you can configure, and I'll get more into templates
shortly. So for my IoT setup, I've set up a generic webhook integration, but there's many integrations
available to you. Integrations provide you
with lots of configuration. You can configure what
notifications look like. I've set up a few labels based on the
alert payloads that'll get assigned to alert groups as well as change how
some of the default notifications load. So if there's any problems with
any components of my IoT set up, I'll have them send an alert to the
URL that's assigned to my integration. Alternatively, I can have my IoT set up, send regular heartbeats to a specific URL, and if there's gaps in those heartbeats,
that'll also create an alert. So that could maybe tell me did
the power maybe go out at my house. It can also route alerts to different
escalation chains based on either the alert payload or labels. So in this case, I'm routing alerts from my aquarium and
garden to different escalation chains. Also for my garden when the soil
moisture drops below a certain level, that's really urgent to me. So we'll route that to the critical
escalation chain that I showed earlier. Oh, no. So actually an
alert just went off. It looks like my tomato plants are
really dry. So this looks really serious. So I think I'm going to go ahead
and actually declare an incident. So now we're moving away from the incident
response part of Grafana IRM and into the incident management portion. Let's
go ahead and get that incident created. We'll say that this is critical because
I need to make some tomato sauce pretty soon and my tomatoes are really precious and we'll jump back to
the web for the rest here. So I'll go ahead and sign
myself as the commander. So Grafana IRM has a lot of
integrations and capabilities, which makes your teams incident management
workflows easy and frictionless as possible so that your team can focus
on the investigation in front of them. Some of these things include auto
creating ChatOps channels for Slack or MS teams for each incident,
autocreating PIR documents for you. We also have some unique AI/ML
capabilities available to you. One of these is Sift. So Sift is an example of how we're using
your telemetry data in combination with the fact that you're running an
incident workflow in Grafana Cloud. It's combined telemetry data within
the context of an incident. Better put, we run a series of checks against your
data. In the context of this incident, it'll surface interesting information, which might be useful to your engineers
in identifying an incident's root cause. For my IoT setup, this is maybe less
relevant, but for your production systems, this could mean automatically surfacing
telemetry data relevant to the incident and saving you and your team time. You can also attach pieces of context
as well throughout the life of an incident. These can be things like
notes, relevant links, documents. This can all be helpful in giving other
engineers context about what is going on or be useful when you're working
on post-incident review. So, okay, I'll go ahead and resolve this incident. It looks like I'm looking at the IoT
system here and the moisture level's starting to return to normal levels. So I'm going to use the OpenAI integration
that we have to auto generate an incident summary for me
and it gives a pretty good summary that I can go ahead and change.
But for now, that looks pretty good. Lastly, if you want to get
started on Grafana IRM, I'd like to highlight some migrator
tools that we have available to you. So if you're currently using PagerDuty
or Splunk on-call and you'd like to quickly migrate over some of your
existing IRM data to get up and running, check out our Grafana
OnCall repo within there, check out the tools/migrators directory. And in the readme we have
plenty of information on how to run, how to configure these migrators just
to get you up and running on Grafana IRM even quicker. So that's Grafana IRM. So from here as next
steps on getting started, you might also be interested in checking
out our documentation on setting up our Slack and MS teams integrations or
downloading the Grafana IRM mobile app and linking that to your Grafana
IRM user to allow you to receive alerts right to your mobile phone
just as I here in the demo.

