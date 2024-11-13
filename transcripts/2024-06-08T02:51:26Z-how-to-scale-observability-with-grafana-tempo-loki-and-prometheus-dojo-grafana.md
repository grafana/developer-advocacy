# How to Scale Observability with Grafana, Tempo, Loki, and Prometheus | Dojo | Grafana

In this talk, Roberto, a staff engineer at Dojo, outlines the company's journey toward achieving advanced observability, which has ...

Published on 2024-06-08T02:51:26Z

URL: https://www.youtube.com/watch?v=_oNqh9rZPbM

Transcript: Good afternoon everyone.
So my name is Roberto. I'm a Staff Engineer back at Dojo. I've
been with Dojo for about, three years, and one of my main passions, at Dojo has always been to focus on how
to highlight and bring the awareness about reliability to teams. And for us, we always felt that Observability was one
of the main drivers vehicles for that. So we've been focused on that for about
the last two or three years. With that, we partnered with Grafana for about three
years back and we want to support this journey. And today I'm gonna talk to
you about all the steps we took forward, with our journey where we are. And hopefully it's gonna be insightful
for you folks. So a bit about the agenda, just gonna talk very briefly about
our business to give you some context. And there's pretty much kind of two
stages on our observability journey. So there's one first stage
about how we got to monitoring, then monitoring over to observability. Then we'll talk a bit also about what's
coming forward, on our agenda, like, kind of like the roadmap. So about our
business making every second count. So we're pretty much a
payments provider in the UK. We sell this, this great product,
which is a card terminal, to a small and enterprise
customers in the UK. We're also expanding internationally
into Spain and also into Ireland. We have an app that also can do a lot
of transaction management and insights. The full system supports point-to-point
encryption, a lot of EPOS integration. It's unique, it's fast, it's
simple, secure, pretty much that. Over the last three years, so some statistics our product
is pretty much 50% faster than the average on the industry. We've inserted ourselves into more than
150,000 small and enterprise customers in the UK and we've integrated
with more than 450 EPOS, partners so far. So as you can see, this has been a big scale for
us in the last three years. We couldn't have not done this with
any observability in mind, right? It was key for our success. So we start
with the first part of the journey, which is everything to do with monitoring.
And this was with no doubt for us, the rollercoaster experience. There a lot of up and downs that Will
has already talked about also before. So for some context, our workload force runtime estates
is pretty much 70% around .Net. The other 30% is Golang. So we
felt at the very early start, we should focus, in the .Net
workloads, right? So when we started, there was pretty much
nothing about metrics. Every alerting was done on logs.
There was a lot of alert fatigue. There was no maturity
model whatsoever, right? There's no center of
excellence around at Dojo. There's these alerts were firing. There
was no any accountability whatsoever. And there was no platform tribe
like, Willie explained previously. So it was a bit hard when we started
the first time. It was simple. So let's grab a service from .Net,
let's get it instrumented with metrics. Let's run it with some load.
We grabbed k6 out of it. And what we wanted to show to the first
internal customers was pretty much, look, did you know that your
service is not fit for scale? So remember this was three years
back, right? We came up with this, very simple dashboard to show them some
statistics about the metrics of what was happening with the service. So for a team of engineers that have
never seen this only focused on logs and start to see like black dash
root panels with some stats, they found this interesting to start
showing them the problems they could have in terms of the service would
not scale beyond that, right? So this was the very early start. And we knew at that time we wanted
to focus pretty much on metrics. So there was four pillars for us. There was instrumentation and we know we
need to build some libraries around it, get it instrumented, get it available for
everyone. And we focused only on .Net. We didn't go into the Golang
world yet at this point. Then we knew we need to ship that
telemetry to our cloud provider of choice. And we also wanted to build some
basic dashboards for team to use, some basic system that people could
pretty much put their alerts on. And we also knew in the future we
could use the same focus on metrics to adopt it for different use cases
that could solve either the different problems such as auto
scaling, canary deployments. And we knew we're big
fans of CNCF products. We knew we could go out and
adopt in the future CNCF products that could focus simply
on metrics. And that's what we did. So over just a period of like three months
at a time, we got over 50 workloads. Workloads for us are like pretty
much deployments in Kubernetes world. And we got over 50 workloads instrumented
with metrics using some basic dashboards and started to set
up some alerts. That's cool. And also by this time, I think
this is a really good number. We already had 30 over 30
dashboards created by teams. But how did we get there? So
we didn't have a central team. There was a lot of initiatives
around innersourcing, nearly like out outsourcing,
but inside the company, right? So this were pools of experts and
champions within their teams that could collaborate on building a, a central
.Net library with instrumentation. We spent a lot of time on documentation.
Of course, simple documentation, long pages of documentation was worthless.
People would simply not read, right? So sometimes just filming a small video
of one or two minutes helps a lot with the documentation and spreading
that around on the org. I won't lie, there was a lot of handholding.
What do I mean by this? We did need to work a lot with teams and
raising PRs for them on their behalf, how to instrument services. That did happen at the beginning
to get the show on the road. And we did internal tech talks also
to bring the awareness and also promote some influence for the teams
to understand if you adopt this, this is all the benefits you get. You
get all these insights you've never seen. Everything you have is just
based on logs. That's not enough. So we did even further, as
people started to adopt, we started bringing up these nice flashy
architecture diagrams with flow charts and Grafana and putting
them on the office screens. So it's obvious anyone that goes
through the office screen would stop, stare at it. It's like,
'I don't know what it is, but I definitely want that.' So this is
how we start getting people to actually care about Grafana, to care about metrics and start
planting the seed within Dojo. But now, of course, story was too good,
right? We start getting some challenges. The first one was Golang,
Python, et cetera. Those other teams using different runtime
started to demand metrics also for those run times. So bit difficult 'cause
we already have a tight innersource. It starts to get really complicated.
There starts to be interest in tracing. So people, not only metrics, want to go
a little bit beyond that. Okay, cool. And we started, we didn't have a structured process to
deploy agents to collect our telemetry, right? It was pretty much custom
resources and Kubernetes, take them out, deploy them. That's it. No cost control. People could ship whatever metrics
they would love and so on and so forth. We didn't put strict governance around
it. Dashboards were on the wild. People just create random
dashboards around the company. We had loads of support requests asking
for help out to build this panel. Explain it a bit more in depth with
so many different type of requests. And alerts, they had no routing ownership. So people would typically go into an
alert manager file, set up a receiver, all done by hand. And
even the CI wasn't robust. But of course this was not possible 'cause
we only had maybe four or five people with expertise that could support this
for a workforce of like over a hundred engineers that this is unfeasible, right? So we got to a point that
we needed a platform team. And the platform tribe was spin up
and along that observability squad was created dedicated to start
taking these concerns a step forward. So we focused on
multiple things, right? The start with the instrumentation, the
first one was really, really obvious, right? We need to standardize. We talked about the semantic conventions
just before on the OpenTelemetry at this time. OpenTelemetry two, three years back wasn't as
mature as it is nowadays. So we already felt at that time that we
need to standardize our metrics and also the labels that we ship. On the shipping,
the same thing: We had common labels. So anything that we would
be shipped from a cluster, we wanted to understand that
metric when it ends up in Grafana, who's the source of that metric?
Which cluster does it come from? So we wanted to understand all of that
 commonality on those labels. 'cause if you don't do that, it's gonna be difficult to build
generic dashboards for teams. No more unstructured, custom resources to
deploy agents on clusters. We build a proper centralized
helm chart at that time. We put some governance on how to
issue API keys for the agents to ship telemetry. And we started put our own controls on
alerts on Grafana itself for the cost so we could know what was going on.
Same thing with dashboarding, right? Single Sign On permissions
for the teams. We, we invested a lot of time in creating
those generic dashboards that was super valuable even until today. We have like, the most used dashboard we have in the
company is one called Container Health. It's a, it's pretty much everything
to do with CPU usage, throttling, network requests, et cetera. And very low level that people still use
a lot and tells them everything about how the container's operating
inside Kubernetes ecosystem. And also for the payment
side of the business, we wanted to build a high
availability dual site. So we not only run on GCP Cloud, but we run Grafana also
in Azure for redundancy. In case of one the clouds goes down. And
we wanted to standardize data sources. This seems so simple, but
people hate to go to Grafana, hit the Explore tab and then suddenly see
a list of data sources that they don't understand, right? We have low environments and production
environments pretty much being served from the same Grafana UI. So we wanted to standardize even the
data source names to make it simple for teams to use. On the alerting
aspect, we also did the same thing. So we started putting in, we pretty much adopted the Spotify model
for the mains and systems that would pretty much establishes the owner
for any metric that would be around in the system. And based
on ownership on metrics, we can easily route that to
our on-call notification system and also start producing dashboards
with that same ownership. We also have the beginning with
a lot of advice from our SREs. We didn't want to focus on alerting
based on causes. So we adopted SLOths. Sloth it, pretty popular
around SLI/SLO alerting. So we adopted that at
the very start as well. And we didn't want to add too much
support for Slack alerts, right? Slack alerts it's just a lot of
distraction for teams and there's no accountability. There's two main reasons threw us off to
not focus too much on Slack for alerts. So this was a lot. But there was one common piece
that was instrumental for us until today on this journey,
which was to do with ownership. That Spotify model about
domains and systems and every
single metric shipped has a domain and system tacked to it as
labels is what allowed us to understand, okay, I can build a generic dashboard
that teams go for domain and the system know exactly the metrics that
that they have, right? The alerting, the same thing. People don't need to go
to alert manager and specify receivers. Just based on the domains and systems
we had now an automated process based on that it routed it to
the correct ownership. 'cause typically the domain and system
for a deployment doesn't change, but the team ownership can change.
That can actually change anytime. A simple case of that could be
a reorg inside a company, right? So that's how we kind of did
it. The ownership was really, really key until today. So by this time we had a pretty good
monitoring coverage. This is the simple, very high level architecture. Just a simple container exposing
metrics in prometheus format, the agent collecting it, sending it over
to Grafana, right? And on this case, nowadays with Mimir alerts get
triggered, sent to alert manager, which you can read to your notification
system. So by this time, and sorry, there's a small glitch on the slide, but by this time we already had
some instrumentation also on Golang. So we had 175 instrumented workloads. We already have 45 clusters deployed
with agents and shipping metrics. And over 75 users running actually using Grafana on an active monthly basis. And by this time already 500 alerts
set up, right? So by this time we felt, okay, we have a good monitoring
coverage, but this wasn't enough, right? We wanted to go a step further. This had to do with now the
real journey into observability. Everything to do with correlation,
how to troubleshoot faster. That is now what we really wanted, right? So so far everything has been based
on metrics. Alerting is in metrics, troubleshooting with dashboards,
everything's still based in metrics. We have that consistency
also with standards in place. Those standards and the ownership
still played a key role. But now if we want to
enhance troubleshooting, we need to invest in the other
pillars of observability. We need to go into traces, into logs
and correlate all of these three. That was really key for us. So we already had some teams
shipping traces to Jaeger, but this was a self-hosted
Jaeger. It wasn't that scalable. We really had problems. We couldn't
actually sample the traces. And we had logs because most of our
workloads do run on GCP and people would have now different tools had Grafana
for metrics, Jaeger for traces, logs that go to GKE,
stackdriver logs, right? We wanted everything consolidated in
a single pane of glass that could be Grafana, right? It would
be more cost effective. And we can also control very
easily the more retention periods. And also one thing in Jaeger, for
example, at that time we couldn't, didn't have support for regex when you
search for some tags and even for just simple service names. That's
something that we felt, well, Grafana Tempo and Grafana Loki seemed
a natural fit for this, so why not? We'll give it a shot. And the other big advantage for us is
this would be fully cloud agnostic. There's no vendor lock-in with Tempo and
Loki. So it made sense for us, right? So once we've done this, cool,
we have trace, we have logs. But the great thing we could
do that started getting
engineers really excited is correlating traces to logs. So
as you can see on the screen, you can go to a simple span,
click on it you get to the logs. And remember, because there's so different maturity
levels on teams in the business, for some teams that are still to stick
to logs, they like to see this view, right? Have the distributed tracing
be able to go to logs very quickly. What about the other way around, the
teams that really, really love logs? If you show them logs, get them back to
traces, that's even better, right? So, so at this point now, it's getting
really the interest of the company. You're starting to correlate stuff. You can find things by correlating two
different pillars of observability. But this was still not enough.
There's one last piece missing, right? What about the metrics?
Can I correlate metrics? Can I do a full drill down
from metrics to traces to logs? And then yes, you can. So
examplars was the solution for us. We call that internally "The Dots"
and examplars are nothing more, nothing less than simple sample
information of traces on your Prometheus metrics. And with that, it gave
us the drill down capability. It could very easily surface
relevant issues for teams. And the troubleshooting experience
is so quick. So from an alert, you have a link to a
dashboard. That dashboard, you have an exemplar from the
exemplar you go into a trace. You go into a log and you can
go all the way reverse as well. So this is what it looks like. This is simply a panel
on a dashboard that for non 200 response codes
for an HP server, right? And what you see there
is the typical requests per second on non 200 response
codes. The dots you see at the top, those are the ones that are
examples, or in this case, examplars are samples of
potential trace IDs related to those errors and to that path,
to that method, right? From here, you can go to traces, you can go
all the way back to logs, right? So this speeded us a lot in our
troubleshooting journey. Make things so, so simple. The other thing
was, this is all great, but our primary focus still with Grafana
or the Grafana Stack is still the focus on alerts on alerting. No one wants to
keep staring at dashboards the whole day, or that is pretty obvious nowadays,
right? But we had some growth pain. So at the beginning we focused too
much on promoting symptom-based alerts. So the typical multi window, multi burn
rate, uh, strategy from Google SRE book, well really well known. We
had some problems with that.
So it's a great system, great methodology to alert on, but it does require some teams to
be really high on their maturity. If you look at Sloth for example, it has so many convoluted recording rules
for teams to debug that when they have an incident. We had a lot
of problems with that. It took them a long time to understand it. So it does require some high maturity
teams to be able to follow symptom-based alerts. We have a lot of alert redundancy. So people having any random alerts
copy/pasting them around and just wasting their time. You just want to
use the same type of alerts, but there's a lot of copy/paste. And
the typical cognitive load friction. So engineers are so focused on their
daily features that they need to work on and deliver. No one's up to be a
PromQL expert whatsoever, right? So that was a problem for us in terms
of how do we find easier ways to promote alerting and we want engineering
teams to be focused on that in terms of our observability offering. So we came up with a simple
templating system about global alerts. Not gonna go into technical details here. But global alerts are nothing more than
like a simple template. For example, for CPU your container has is being CPU
throttled, right? It's a simple alert. You create one template. What we would do that is replicated same
alert for all the domains and systems in Dojo 'cause that is what
tag the ownership, right? So teams automatically get out
of the box alerts for these, which they can turn off. And we do encourage them to turn them
off after they start on their journey to focus and elevate the maturity
to focus on symptom-based alerts. But this brought us
multiple things, right? When you're in a platform tribe and
you have the observability squad, you'll typically have more squads on
the same tribe, right? With this system, it allowed us to put in also a
framework for other platform products. Let's say we have a building
processor team, right? And they offer Argo CD
installations as a product, right? If that team wants to ship that product
and automatically get alerts out of it, you could use this system automatically
to empower those teams to ship their products and features and
have some alerts on it, right? So we build all of those like
probe failures, crash loops, the typical Kubernetes failures
that you would expect, right? We don't want hundreds of alerts
on those. That is not the point. The point is raising the awareness
to teams that they should start thinking about observability, right? This
will cause alert fatigue. It's normal. And the intent is that get them interested
to buy in time on their sprints to focus on symptom-based alerts,
which is a bit harder to grasp, but way more valuable
for the business, right? Where are we today? So, pretty much we were already shipping
all the metrics to Grafana, to Mimir, traces to Tempo and logs to Loki as well. We use the standard Grafana agent
that is provided by Grafana as well. We went from 175 to over 400 workloads
inside Dojo that are shipping, that are instrumenting
with .Net and Golang. Over 80 agents on multiple different
clusters and also across different clouds. We have over 200 active users
across engineering, ops, and also product. And believe me, sometimes to get product people to get
the buy-in for Grafana is not that easy, right? It's a too technical tool. And with Global Alerts empowering this
with all this SLI/SLO alerting and some custom alerts that people have built, they have gotten better with
PromQL and some interest as well. We've scaled that to about 11
times. That is a lot, right? That, we've achieved. So what is next for us? Pretty much we want to go
into the fourth pillar. We want to look into profiling
and obviously we were using, looked into some use cases with Pyroscope. We had a couple of memory leaks that
Pyroscope has actually helped us in understanding where metrics,
traces, and logs weren't enough. We want to probably potentially invest
more time on Pyroscope for the future. Also, we want to continue leveraging
Grafana as a central piece to drive, to empower FinOps practices
in the company, right? We already have all the metrics for it. How about we get some
leverage open cost as well, and start raising cost awareness,
get it driven by alerts, but we want responsible actions out of
it to stop with waste happening on our workforce. And that's
pretty much it. I mean, if you enjoyed the, the talk and you'd love to join us at
Dojo to continue with this journey, you can scan the QR code or go to Dojo
careers. There's a lot of open roles, uh, available , if you want to, if you want to discuss any of these
details in a bit more in depth, come find me at the reception. Happy
to talk. That's pretty much it. Thank you very much for your time.

