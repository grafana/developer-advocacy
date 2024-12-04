# How Maersk is Navigating the Seas of Observability with the LGTM Stack

Maersk, a global leader in shipping and logistics, is forging its path to enhanced observability. To streamline operations and empower developers to take the helm in observability, Maersk embarked on a journey to consolidate tools into a centralised platform. 

Director of Platform Engineering Roshith Radhakrishnan and Senior Engineering Manager for Observability Platforms Henry Kühl unveil how Maersk revolutionised its observability using the LGTM Stack – featuring Loki for logs, Grafana for visualisation, Tempo for traces, and Mimir for metrics – complemented by Grafana Faro for real user monitoring (RUM).

Chapters
0:00 Introductions
3:00 About Maersk
5:00 Problem statement and challenges
6:35 Maersk observability platform overview
8:12 Platform capabilities: Ingestion, Query, RUM
23:10 Reliability
26:20 What's next?

Published on 2023-12-11T22:57:32Z

URL: https://www.youtube.com/watch?v=YIuTuSZIyos

Transcript: Thank you. Good afternoon, everyone. We are very excited to be here talking
about how we have transformed the Observability practices at Maersk.
My name is Roshith Radhakrishnan. I'm a Director Engineering for
Platform Engineering Group at Maersk. I have the privilege to support quite
a number of awesome engineering teams, including observability,
tools engineering, and container runtime engineering. I am okay, . I'm,
I live here in the UK. It's been a couple of
years since I've been, I've been living here and we
shifted with my family for work and still getting used to this
you know, ways of working. And then of course, the
weather things like it. But I'm originally from
India a place called Kerala, which is down south of India. It's often referred to as God's own
country for its beautiful landscapes and and, you know, backwaters and so
on. Before, before moving to London, I've been I've been in
Bangalore for about 16 years, and for very obvious reasons,
it's a, it's a beautiful city. And my second home as well,
along with me is Henry. Why don't you introduce
yourself, yourself, Henry. Yeah, thank you very much, Roshith.
Really excited to be here today. So my name is Henry. For the past one and a half years I've
been working as an Engineering Manager and with the main focus on like
building an observability platform, a companywide observability
platform for Maersk. And yeah, I'm really happy to share some insights
and how that went the past one and a half years. And yeah, this is
what I do when I'm not working, taking selfies with some random
people. So obviously that's my family. Like we have two wonderful sons, and this picture was taken during one
of our last trips when we went to the Arctic Circle in, in Finland. Cool. So why are we here, right? I mean during the next 20 or, you know just less than 20 30 minutes, what we'll do is we'll walk you through
our experience building an internal platform from scratch, of
course, using LGTM Stack, our challenges along the way, of course, our experience and our future
forward as well. Alright, before we start in disclaimer, we
are just the engineering leads, but our team did all the awesome work. Few of our team members are here. I don't know if they can just raise
their hands. Yeah, they, there you go. They've been doing all the amazing work
we are just here to, to cheer them on, right? And FYI, if I may add to
that, so we are not going, doing a live Q and A at
the end of this session. This has nothing to do with
us being managers, right? It's just because we have so
much content to throw at you. If you have a question, I just made a
post in the Community Slack of Grafana. So I opened a new thread and our wonderful
engineers are ready with their phones to answer any question that you
might have to just pop it in there, and they're gonna go
ahead and answer that. Alright? So people who don't know Maersk, we are the global leader in
integrated container logistics, right? We operate across our, what's our purpose? Our purpose is to make sure that
20 percentage of the world's global trade is flowing
smoothly. You know, all, all days, right? I mean, that's, that's
what our purpose is. And we have, we have our operations actually
stem across ocean, ports, air, and land. We have over 100,000 customers
across 130 plus countries. And and and beyond business, our purpose is to improve life
for all by integrating the world. We operate in a, I mean,
along with this, right? We, we handle a large
infrastructure footprint and, and very critical infrastructure
footprints as well, right? I'm talking about infrastructures like
large container vessels to, you know, to ports, to terminals, and also like, you know warehouse and logistic
facilities. And, and it's a very, very you know, it's, it's,
it's not standardized, you know correctly well, right?
And we are using technology to, to do that for us. So technology forms the core
of our digital transformation. We are investing in quite a lot
including modernizing our technology landscape building, cutting edge, digital, you know frontends. And also investing quite a lot
on making sure that we build the greatest and easiest developer
experience for all of our customers. And we use AI and ML to, to make sure that we provide more
reliability, better visibility, and agility for our customers. So over the last few years, we have
been going through a digital or, or a transformation journey, right? So we transformed our ways
of working to be a bit more cloud first, you know,
technology driven company. And what we have done is we have
empowered our business functions to move faster, right? Make the technology
choices you know, on their hands. And they were able to do that quite well,
right? But over the years, you know, it have introduced quite a lot of
challenges for us as well, right? I know we all agree,
particularly as engineers, looking at the observability
space, there's a, I mean, there is no one size fits all, you know, solution when it comes to
observability practices, right? And that's exactly the
same case here as well, especially when you're
handling large and, you know, complex infrastructure and
technology footprints. So, so over the years we have, we have
acquired quite a number of, you know, vendor toolings just to
isolate these you know, individual monitoring requirements and
managing these infrastructure or managing these toolings. And, you know correlating the data
was nearly impossible, right? And that actually introduced us, you know, quite a lot on siloed issues and no, not having comprehensive coverage
across all, right? And of course, as the infrastructure footprint
grew, the cost also went, you know, over and beyond. And managing observability requirements with, with cost control measures
remain a constant concern for us. So we try to solve this problem using an
internally developed platform from the scratch, right? We call it Maersk
Observability Platform or MOP. And these, what do you see on the screen represents
our guiding principles and you know, strategy behind building
this particular platform. We, our goal was to provide a centralized
platform for all observability requirements across, across Maersk. Cell service capabilities enable every
developer within the organization to onboard into the platform easily without
any additional barriers or approvals. So it's actually shifting the culture
back, you know, to, to the owners, to the developers to have
accountability and ownership as well. Open source is one of
our guiding principle. Not only it helps us actually you
know, build cost effective solutions, but also it ensures that you know, there is no vendor lock
in and more importantly, selecting the right tools
for the right job, right? And democratizing data is
another fundamental principle. We wanted to break the data silos that
exist in different parts of the org and make observability data available
for all users across Maersk. And importantly, I mean, you know, we wanted to build a solution which
is purpose built for Maersk, right? It has to be customized, and customization is the key and only
lever through which we can analyze this solution back to the organizational
objectives end goals. With that said, I'll pass it over to Henry to give us
a platform overview and capabilities. Thanks. Roshith. Thank, please
give me the clicker, I don't know what to do with
my hands, otherwise. Yeah. So let me give you an
overview of the platform here. So now Roshith introduce you
a bit into the problem space, and I'm now gonna give you like a high
level overview of the capabilities of the platform, and then we deep
dive into the stack as well. So on this chart you can see like, these are all the capabilities that we
either have already stood up or will be standing up in the future. And you can
imagine with this strategy of Maersk, like being the integrator
of container logistics, observability data occurs at probably
every step of the supply chain. And so far we, for us, this materializes
in logs, metrics, or traces. There are some tools on this chart
where we actually stood up something ourself where the open source tooling
was just not up to the mark of the requirements that we were facing. So
diving a bit into the core stack here. So we actually run the stock
images as Grafana publishes them, and then we use JSONnet to just
configure them and deploy them. And in the field out there, almost
commonly used agent is the Grafana Agent. We run it as a cluster module for
all the clusters that are there, the, all the Kube clusters in, but we also support the Telegraf
agent and the OpenTelemetry Collector. But basically, you can send data
to us with any agent you want, as long as you adhere
to our ingestion APIs. Now that we talked about
some of the capabilities, let me try to stitch this together for
you a bit from a customer's perspective. So imagine you're a new
engineer at the team, you're the puppy of the team in one of
the Maersk Logistics engineers team. And your task from the staff engineers,
"Hey, we wrote this new application, please onboard it to the
Maersk Observability platform. In the last community of practice meeting,
I heard that that's a cool platform, so we want to use it for our latest
application." And yeah, there you go. He, he's providing you the link. He's so nice. He gives you the link to the
Grafana instance that we have, and you just open it in your
browser and you realize, hey, cool single sign-on works. I can just
log in. There's no approval needed. That's one of the things we
try to embrace, as Roshitt
mentioned, self-service, right? So no one should be able to, like, everyone should be able to access
the platform, send data to it, and then you realize, oh, there's even
documentation that you can use, right? So you can dive into that, and
there's an onboarding guide. Nice. So that's exactly what you need, right? You want to know how to get onboarded
to the platform, and it's right there. And you realize, oh, if your application is running on one of
the Maersk provided Kubernetes clusters done, your job is basically done because
telemetry is already ingested to the platform. It's tightly integrated with all the
other platform products that we offer inside of Maersk technology, which
is nice, but even if it wouldn't be, there's also guides on how to set up
agents yourself and how to integrate that all on a, with, with like
self-service built in. Just send it, that's what
we call it. And then yeah, you of course want to query the
data, right? So how do you do that? You use labels, right? That's probably
not something I'd have to tell you about. For us, labels also play a very important role
when it comes to running the platform, because we use them for
different kind of things. Obviously we use them for retention
like adjusting the retention time, for instance, for logs. Dev logs obviously have a way lower
retention time than production logs. We also use these labels
for usage tracking. So want to find out who's the top talker
on our platform at the moment. Yeah, we use labels for that to find that out.
Same goes with cardinality tracking. If there's a spike in cardinality, these labels help us to find out
like who has caused the spike, and also we use them for traffic routing. In the beginning when we started with
this platform, this happened, right? So we probably had the most
comprehensive list of how to define a pre-production environment with
different spellings, , and yeah, obviously this is not something
you would want, right? So how did we handle this? We stood up a Guard at
our front gate, right? And that one actually materialized as
a custom application that we wrote. So Guard is a write proxy, and you are looking at the
configuration file of Guard here. So as you can see on line three, Guard forces you to send an ENV label
alongside the telemetry data that you ingest to our platform, and it also forces you to
provide a certain list of like, like a value out of a certain
list of allowed values. So that's how we enforce
standards by using a write proxy on our ingestion path. And you
can see on line 11 as well, there's another label that we enforce,
which is app for the application, but we do not prescribe any
valid values for that one. Okay? So what happens if you
violate those standards once
the data's being sent to us? We just drop your data.
Sounds hard, but yeah, we don't do it silently. There's a
dashboard that you can go to, right? So this is like the Data Validation
Dashboard is what's called, and probably this is one of the most
used dashboard that we have in the platform. So probably every week there's
a support case that we get like, "Hey, I can't find my observability
data." And what we then do is, yeah, here's a troubleshooting
guide. Step number one, check the Data Validation Dashboard. Is
your data being dropped? And oh, it is. Yeah. See, problem solved. So coming back to like your new job,
right? You get it, standards matter, okay? But that's all taken care of. Fine. Let
me deep dive into my observability data. Now I wanna start
querying, right? So yeah, this is what we saw what
was happening, right? So the same customers that came up with
all these nice spellings for environment names also have great ideas on how
to do querying in the wrong way. And actually we were bucked by some
incidents because of customers doing some weird queries or creating recording
rules that were not like, very optimized. And actually this is a very nice feature
of Loki that was recently introduced where you see the amount of data that
would be queried before you even submit the query. And yeah, what did we
do? You might guess it already. We summoned a wizard to
help us with some magic, and Wizard is actually another
custom component that we stood up. Not on the ingestion path this time,
but on the read part, on the query part. And as you can see here, Wizard is providing also some
visual guidance to the user, actually who's using Grafana. And there's
different messages You can see here, the latest one being on the bottom right. Piggybacking on this Loki
feature that I just explained. So whenever a customer a query
by a customer using our platform and Loki exceeds 200 gigabytes of
log volume that it would query, we just don't allow the query.
So that's a nice addition. And there's other validations
that we do on the query path. A quick shout out here to Madhu, who was one of the main
contributors of Wizard in this case. And also there's a, of course, a dashboard that we have to give us
some insights on what query validation errors occur, and if there's an actual learning
process that kicks in of the users of our platform because of these
things that we display to them. Alright, summarizing this again,
so we actually run the LGTM stack. We have added two things to
it, which is Guard and Wizard. Wizard for the query path for
either via Grafana or our query api, and we added Guard on the
ingestion path. And as a whole, this is pretty awesome for us, and
you now may ask yeah, but hey, wait, open source goes both ways,
right? And we totally agree. So this is a list of pull requests
that we provided back to the community, the top one probably being
the biggest one that we did, where we upgraded the Azure SDK of Tempo. And we also did this because we
were haunted by a nasty bug in it, which gave us some odd hour
pages, which obviously is bad. So now that I talked about all these
capabilities and the deep dive into the stack we also found ourselves desperately
in the need of a real user monitoring capability as part of the
platform. And once again, Grafana Labs saved us by releasing Faro
and Roshith will now tell you a little bit more about that. Alright, so we started this
journey in early 2022, right? And it was during mid 2022, we actually looked at looked at,
you know, this problem statement, how do you enable front-end
absorbability, right? How do you standardize those practices? And the launch of Grafana Faro was
right on time, right? So as of now, we have integrated Grafana Faro
into our observability pipelines. And you know, along with Grafana Faro, what we have also done is
we have added a, you know, a number of custom
OpenTelemetry, JavaScript, instrumentation libraries. We have developed our own custom
modules and we packaged it in the, in a, in a custom SDK, right? And that's, that's been embedded within
our applications code base, or our users just need to embed this
in our, in their application code base. And then, you know, you get the
observability data, including logs, you know exceptions events
like the page clicks, URL page navigations, et cetera. And
we, we can then forward it, you know, into our core observability engine
using the OpenTelemetry format, right? And in this diagram, we use a custom version of the Grafana
Agent. We, we use that, you know, particularly to ensure there are app
validations in place and quite a number of additional enhancements that we do, right? While we do that we, we could actually, we provide default dashboards
or templatized dashboards
for our front end users, right? And we include the
page performance summary, including the web vitals exceptions
and errors, and of course, user analytics data and users can then
customize it according to like, I mean, you know, if it is gonna be the entire webpage
or URL based view or even individual sessions, right? Okay. So we have added a ton
of...Grafana. Faro, by the way, did, did a lot of heavyweight for
us, but at the same time, we had to do a lot of instrumentations
and customizations to support our, our user base, our user requirements,
right? As you could see on the screen, majority of these events are you know, custom events generated
by the applications to the
traces. And then we know we, we add configuration options back to the
users to be included within their SDK. You know, to, to gather these information
over. We provide support for Beacon. This is especially you know, useful for
applications who are resource heavy. I mean, I know, which is who are very much
I know interested on their
application performance using this, you know, they'll be
able to send the request, you know, on the fly and then, you know, on through
the backend and, and without letting, it's more like a
<inaudible. Method, right? We also added the performance marks.
This will actually capture the, you know, render page rendering times
rather than just the page upload times. And then we give session
sampling, you know, for these for the users in
order to instrument what, what do they need to really push, you
know, further to their log pipelines. This is yet another
feature or customization, which is which is not available out
of the box using Faro. And then, you know same customized
it, you know, and, you know, configure it as per the user
needs is what the mantra. Here. We have also replaced you know, zone
context manager, which is one of, I mean, basically because of the compatible
issues with applications. I know, like this is one of the,
one of the I won't say bug, but an issue which is getting worked
you know, with Faro engineering team. And we have also implemented custom
error handling, right? I mean, and, and to support our applications working
on offline mode. As I said, I mean, I know we have tons of vessels and
applications running on vessels, which actually requires you know, logs to be pushed only when there
is network connectivity, right? And then we could funnel that and then, you know or we could actually funnel
that network calls when and when application comes online, push that
over to our observability pipeline. While this was all good,
we went further beyond, and then we had to support our mobile
app or mobile customers as well, right? So, so Maersk mobile app is used by app
and very much everything that you can do on the web, you can do very
much on the mobile as well, but users generally track it for, you know use it for tracking
their shipments online. And we have seen a tremendous
increase in the mobile app, you know since Covid right more than 460% increase over. And our mobile team uses Flutter
for cross app platform development. And the requirement was to
how to support them, right? So we have developed an SDK, which
is nothing but a custom code, which directly interacts with the, with
the backend API or with the APIs native, APIs for both web bot, iOS, and Android. And we use method channels within
Flutter to satisfy that particular need, right? We then
funnel that over you know, into our pipeline and using a
custom version of the Grafana Agent. We would be able to, you know pick the
instrumentation data or the, you know, device data, just like
how you do it, you know, via a web SDK back into our core engines. So we, we provide again default dashboards
for including the mobile vitals, errors, exceptions, and analytics data. And this is a summary of what
we could actually, you know, capture at this particular
point in time, right? As I said, a ton of customizations
or instrumentations that
went in in order to capture events, logs, and measurement,
including few meta information. And we use the method channels to
actually capture the device you know, CPU memory the, the ANR
stats, and then the, the frames you know, native
slow frozen frames as well. We use you know RUM HTTP overrides
for getting the load duration you know, request response
sizes and asset bundle to, to capture the asset load times and the
asset sizes as well. And we use RUM, you know, navigation observer to get the view
page information and also the routes and also the user interaction
widgets to get more in depth, in depth details around the tap, you know, clicks and other user
information data as well. By the way this custom module, we
are, you know, we are looking at, I mean open sourcing and then, you know, giving it back to the community
as well in case if you know, people are more interested in this.
Alright, over to Henry for reliability. Thanks Rashith. Are you getting a page
right now? Are we down? No, . Okay. So let, let me talk a bit
about reliability of the platform, because if you can, you can imagine probably that
the platform at this scale it is, it's important to run it
in a reliable fashion. And I'm going to tell you a bit about
the technical challenges we had, but we also invested a lot into cultural
and mindset things when it comes to reliability. So we really try to embrace
this SRE mindset as part of a team. There's no separate SRE team running
the platform. We do it ourselves, the engineers do it themselves.
And yeah, this is how it went. Basically in the beginning. We
couldn't keep up with the growth. So all of these graphs just basically
point up except the one from GitHub. We use GitHub for support. So I don't
know why that graph drops in the end, but it's just how GitHub renders this.
Also, this is a very nice dashboard. Shout out to Liam who created this nice
dashboard and also the metrics that it's based on. You can see these numbers are
huge at least we think they're huge. But there's also some hidden
truths to this, right? That probably not all of this data
is being used by our customers. There's actually this one
article that I read where, like a simple hello world application
deployed to Kube cluster and you instrument it, it produces like half a terabyte
of observability data in one one, which is crazy. So, yeah, good thing that Grafana has this feature
of Adaptive Metrics and cardinality tracking, right? We still have to double down on
that area as part of our platform. So we run on Azure with
AKS, we run on spot node. I wanna put on a cowboy hat just
by saying that. And we run it in, in a single tenant configuration
through the whole stack. We do not yet see a
requirement to change that, but we might see that in the future. This was one of the first setups, cluster setups that we did once we
stood up the platform. So super, super simple actually. The zone awareness is the only thing
providing some kind of high availability here and the like, Tempo wasn't even zone
aware once we when, when we did this. So the zone awareness feature,
we provided that back as a PR to, to Tempo and yeah. And actually reality hit us because of
this huge adoption that we saw across Maersk. And hands up, if any of you were bugged by one of
these issues running out of ARP Cache or running out of contract
connections. Yeah, one, two, let's give each other a hug after the
talk because like, yeah, we survived, right? Woo-Hoo. So based on that, we improved the setup to keep our 99%
promise of availability that we have given our customers in the beginning. So we moved each of the tools
to a separate node pool, we split the storage accounts.
So yeah, that got us so far, and then we split it even further
because we wanted to go to, to like increase our promise even
further to 99.5% of availability. So each tool is now sitting in its
own cluster and we even have loads of other ideas on how to improve
this even further. But yeah, if you want to hear more details about
that, just find me after the talk. Since my focus here was on reliability
only we are also facing very complex requirements from the
organization moving forward. But a little bit more
on that from Roshith. Alright, so what next? We, we are at a
very critical juncture wherein, you know, we have provided basic
observability requirements. When I say basic majority of you know,
the bucket falls as a basic requirement, but considering where we are in our
reliability and the user adoption is, is our primary you know
area of focus right? Along with this though there are tons of
real requirements that we need to cater as we look forward in 2024. And
one of the thing is, you know, how to enable observability at our edge
end points. I talked about, you know, handling large infrastructure footprints,
and these are exactly the ones, right? We have got 700 plus vessels you know, tons of terminals and 450 plus
warehousing facilities wherein, you know, these are large
pieces of infrastructure,
but very digitally you know, fragmented, right? We wanted to bring this together and
then build observability, you know, across all of these edge
endpoints, which is critical. And we wanted to do that with, with consistent observability
experience for our developers, right? So here we are looking
at you know stitching our
observability pipeline into the internal platform internet development
platform that we are building. And we don't want to miss out on the
wave of AI and ML as well, right? While we are pretty pragmatic on our
approach, but we wanted to tap in the, the intelligent
observability practices to, to provide better visibility and
better operational insights for, for our customers as well. And with the recent announcement
that Grafana has made, and I hope, like I know that would be
pretty, pretty easy task there. So as much as we embrace open source
you know we also wanted to continue contributing back along with many,
many tools that, or, you know, custom components that we
just mentioned over here. We have also made you know a synthetic
monitoring tool. Unfortunately, we did not chance to discuss that.
But, but the point is, you know, we are looking at contributing back to
the community you know in the open source world, right? And that, that remains our, one of our core objective
as well in 2024. I think. With that said that's pretty
much the end of our talk. I hope you have enjoyed
this particular experience. Should you have any questions feel free
to grab us, you know, post this call. Thank you.

