# Scaling Monitoring &amp; Observability for a Software Platform with Grafana Cloud | Builder.ai | Grafana

In this talk, Utsav and James from Builder.ai discuss their journey in scaling their composable software platform. Builder.ai ...

Published on 2024-06-08T08:00:10Z

URL: https://www.youtube.com/watch?v=HUuXp9jgXmo

Transcript: Hi everyone. So I'm Utsav and James. We are from Builder.ai and today we are
going to be talking about our journey at scale. But first I think what, who, what does Builder.ai do or who we are?
So we are a composable software platform, and we believe, like in trying
to unlock human potential. So we are a platform. We allow people to build on their ideas
and come together and we kind of take care of all the technical
details. So anybody, right from an entrepreneur to a
student, an enterprise, an SMB, they can just come and
build their platform. I'm an associate director
of engineering. James, I'll allow you to introduce yourself. Yeah, as it says, I'm a technical lead
for the developer service platform. Perfect. So just a little bit of
context before we kind of deep in. So Builder.ai under the hood looks like
these different verticals that we have: customer experience, delivery
experience, assembly line, marketplace, AI decision
making. So there's a lot of
things that are going out. But one of the core things that we wanted
to talk about today is in terms of one of our platforms, which is
called a developer surface. How did we start using Grafana
Cloud? What did we use previously? It's a very busy system. It, and I
let the TLDR come in the next slide, but it's more around not only it
allowed us allowed us to go through the process of monitoring
and observing our customers, but it also allowed us to give
them a better performance, understand bottlenecks with cloud
providers that we were using and a lot of different things. So I go next slide and over to you James. So what is the builder developer service? So think about it being
a virtual desktop that we have deployed and configured for
developers or what we like to term experts. They can access this using their web
browser from anywhere in the world, although we try and localize that to
wherever they are in the world because obviously latency. The tool the actual developer, well the virtual desktop
itself has everything required
for them to do the piece of work that we've assigned to them. So it has all the software packages
and libraries, et cetera that it needs. And as the sort of the
highlight on the right, there's sort of lots of numbers there, but ultimately we have
quite a few of these things. We've got across six geographical
regions across the world. Again, I think we're two cloud
providers at the moment, but we'll probably be
going to three or four. We run in just our unit alone
in the developer service, we have over 20 clusters running. And yet we have quite a lot of
metrics that come out of that. So you'll probably hear me talk about
that quite a lot. So metrics . So what was our challenges? So
basically the sad kitten faced, we had our own, so we knew about Grafana, we knew we've used that tooling before,
but we kind of deployed it in-house. We had it deployed within our stack. So we had Grafana and Prometheus
and a bit of Elastic in there. But it was sort of self-managed
by ourselves and each team. It was a bit of a pain for me
because it was not a big team. So having to deal with 20 plus clusters
with the monitoring stack built into the cluster, constantly trying to deal with Prometheus
and various memory leaking issues, or sorry, memory issues. I'm not saying
it leaks , but memory issues. So it took time constantly
having to manage it, maintain
it and stuff like that. So it became a real problem for us because
just to maintain that going forward required lots of cycles within
the team just to do that. And so when you look at sort
of a centralized solution, you wanna look for various
different things around that for us. So we looked at cost, tooling, so obviously we've got experience with
Grafana in the past that's quite a nice fit there. How easy is it to set up
and roll out? And when we looked, which was not that long ago, I think within the last year there was
very nice ways or easy ways for us to deploy that we are very
Kubernetes heavy. So again, there was a nice sort of at the time,
easy way a path for us to follow. Whether it would handle
the scale and again, that's Grafana's problem in this case,
so yay takes that problem off us. But just dealing with the scale and
the size and the amount of metrics send them, and also the help. So you know, from the professional services
people you might have seen, I think have one today. We talked to them, they helped us a lot with
the integration at the time. So with all those things we kind of
decided, oh, let's use Grafana Cloud. Ultimately when we did this, I
should say I've got an experience, I'm a background of DevOps. So when
we say solution within two weeks, that's because I knew kind
of what I was doing there. But , it did only take me about
two weeks to take the helm charts, the examples they gave us, put that within our clusters and
deploy that across the board. So we were able to go
from 20 plus dashboards, stuff that's self-hosted to an actual
centralized view within about two weeks. And obviously there's lots of other
things you have to do at the other end of that, but it gave us that visibility across
all of those clusters within that short frame of time. And it was
relatively easy to set up for us. So we didn't have issues
with legacy things of log in, et cetera like that because we
could just lift and shift basically. So it was a nice easy conversion. And again, I should talk about metrics. So we, it's very difficult 'cause when
they talk to you, they always go, how many metrics are you running?
How many, well, I dunno, , it's really hard to
determine it sometimes. But what it did enable us to
do as part of a trial period, we were able to actually put some of
our production clusters on there and we could actually work out a
relatively good volume of metrics. So whenever we put a new cluster on there, we had a good idea of
the cost going forward. So it was a nice easy way for us to sort
of get an understanding of actually how many metrics we were generating for
each of our production clusters. And another important aspect was at the
time they had the nice recommendation things for lowering your
cost. And there's a very good, which I recommend you use, but they have a very good example of
board and that if you go and log in, it gives you a set of recommendations
about how you can reduce your metric costs. And we do that on a two or three weekly
cycle just to make sure that we're capturing those over time. So I think everybody's
seen Grafana dashboards, but obviously you get some included.
So this is the Kubernetes one. You just, you do the integration, you set it up and you get
some nice dashboards for free, which is always good because
as it's been alluded to before, there wasn't many of us, it's very difficult to get
people to learn something new. So having stuff for free always helps
with your adoption because you don't have to learn anything over time. What we did was obviously
created some custom dashboards. So we were able to, for
example, so an ID for, and it is a virtual desktop,
think of it like that. So this tells us the number that we're
running on each cluster and how many, and we have an arbitrary limit of around
200, which is why that one on the red, it's gone red, it's not, it's
not a problem, don't worry. But it's just telling us that we are
running over the capacity on that cluster at the time. But we were able to produce
that with Grafana relatively quickly. Tying in with our logs and metrics
and our database to actually produce this view. So again, I think I've talked
about metrics and costs. This is the example. So we've used
the dashboard and the tooling. So and if you look at the example on
the top right,  zero cost, that's great , which but we on average are doing
about 5 million metrics at the moment. There's a big spike there,
but just ignore that. There's nothing, nothing to see there,
but ultimately . But ultimately it was a good way for us to be able to
see what was going on in the system. And it all comes for free with Grafana.
So you can actually see what's going on. You can actually see what's happening.
You can see your costs, you can add, and as you add more and more, you can actually see that mine go
up or down or whatever. And again, adaptive metrics, I can't but recommend that enough from a
cost control like point of view because it does affect ultimately how many
metrics you end up paying for. And again, that's one of the things that we ran on
a two or three weekly cycle and they've made that a lot easier to do
than previously where you had to, you had to cut and paste, but now it's literally press a button
and then either go through the list and apply it or sort of do a bit more
things around it. But it's up to you. It helped us understand output on our
logs because everybody has logs, but we are able to obviously see across all
the clusters and see the effect of a debug output. So everybody accidentally
put print statements in there
or they've put DMOG mode on and you didn't realize you can see
it quite easily and it can help you understand that. And, and again log storage is cheaper than metrics. And now I'll talk about why and why
it's quite important to us for that. But it is something to be mindful of. So
for us it's quite important. You know, we have a lot of metrics
going along in our systems, but we actually ended up using the logs
in a sort of a interesting way that I'll elaborate in a minute. So we have all these desktops. We have over a thousand of them running. We have what we call
like our health check, which kind of is an inbuilt
thing that checks to see what, what's actually going on that
desktop to see whether it's healthy. So basically what does that mean? It just means it does a load of different
sort of checks internally to see whether it can do X or Y or whatever.
And we admit that as a log entry, but what we were able to build was just
by talking to the Loki endpoint within Grafana, we could then build an API on top of that
and then build custom logic depending on what you saw as an actual
event or a health check event in this case. So it was an easy, cheap way for us to not necessarily
have to build a big scalable solution to actually take all this information that's
coming out of all these desktops and then build an actionable system on it. We don't have to worry about where
they're stored, that's Grafana's problem. We pay them, but ultimately they deal with the endpoint
and we just talked to that to get the actual health check information
in this case out of it. So it enabled us to build this
system relatively quickly and now we have a system of if
something's not going quite right, it can run various things to try
and fix that automatically for us. So we don't have to necessarily
worry too much about the alerts. But yeah, that's a nice
bonus for us because again, metrics are okay, but we don't necessarily need that
resolution of time of to the the second we get, we run this every five minutes and when
we're trying to fix issues and stuff like that in our system
for these kind of things, that kind of time of resolution is really
useful for us because we just need to understand whether it's a transitory
issue because somebody ran a build that they shouldn't have done or whether
it was an actual longer term thing. And that's what we're
tending to be moved towards. We need to understand longer term
trends rather than sort of, you know, what was a problem 10
seconds or 20 seconds. I think I've ran through
that pretty quickly, but. That's fine. We can save
some time for your questions. Yeah. hand back over. Thank you so much. So just a
quick recap. I know it was a very, very quick presentation. So the
developer surface platform that we have, it serves more than 2000
active users at the same time. If you think about the
scale of the system, we have six different regions that we
have to support multiple cloud providers. The challenge definitely is like we
are trying to replace people's laptop, so their local environments, they have to now code into this
platform that we are giving. So latency and all those metrics
are really, really important to us. Any sort of issue that happens, it, we have strict SLAs that we have that
we have to adhere to. So it's very, very important that our metrics and
logging systems don't actually eat the resources of the clusters in
which they're running, right? So that's why having something which
is outside was very, very important. So SLAs is something which is is
really improved after we've moved on to Grafana Cloud because it just gives you
the pointers without taking too much effort. Cost management, as James already
covered, the tools are really nice. It allows us to get a
good grip of the cost. And we are able to go to the level of
what does it cost for this particular expert in this particular region
just based on the cost metrics. The nice cherry on top is around the
fraud detection capabilities that Grafana Cloud system allows us to do. So whether it was the logs bit so that
we can see if there's any sort of anomaly that's happening or metrics
ingestion because it's really easy to tap into the low key endpoint. It just becomes really useful for our
fraud detection capabilities because when we are running a platform
of this size, there is, there are fraudulent activities, there are people with malicious intents
that are trying to use the system. So whether it's the face detection system, something is going off that it has
detected or it's around what exactly an expert or a developer
is doing on the system, that could cause because it's against
the fair value of the shared model. So somebody can virtually impact
other people on the cluster if they do something interesting. Right. And
everybody likes to hack into things. So that's a little bit of a recap. I'll try in terms of the next steps. Yes. so Grafana Alloy is very good.
Sorry, that's the second point of it. I just wanted to say it's quite useful.
We are currently using Grafana Agent, the plan is to move to Alloy
because we want to make it really, really easy for other teams to adapt
to it. We don't want them to use any dev time. Basically, it should be just a flag for them that
they just set it on their clusters and that's it. We take care of everything else because
Builder runs a hundred percent on Kubernetes, everything is templated and
it's probably the same set of stack. So it's very easy for us to understand
what is running and we can roll out alerts, dashboards, just as
part of the base template. We have more than 70 services, so IDs just consist of about
10 or 12 services that are more that's there. So we're just trying to scale
up and add more teams to it. Not every team has a DevOps experience, so of course that becomes a big challenge, which is why we are trying to make it
as simple as that for them so that they don't need to. It basically is around them seeing the
value and not actually putting in the effort to drive the value. Getting a service map for
the entire organization is
one of the north stars that we are trying to do this quarter so that
we exactly have those nice dashboards that I think we saw in
the Dojo presentation that
we want to show it in the office and probably
start That's a nice idea. So we should probably
start doing that. But yeah, that's when the intent
behind the service map. Tracing and frontend observability is
definitely something that we are tracking actively. And we want to see as to how
we can use the EBF to do the tracing capabilities because it takes a lot of
effort for an engineer to wrap their heads around all of the things
and how to instrument their app. Lost, I mean, not lost of course
the OnCall integration with SRE. So we have a site
reliability engineering team. They work slightly differently today, but we are trying to get them hooked onto
the OnCall system in Grafana Cloud so that we can start
reporting partial outages. The wonderful AI features that we just
saw this morning afternoon actually earlier today around how we can generate
outage reports and all that is quite useful because we can then actively talk
to our customers and show them what is happening with the stack. And
last, but not the least, LLM ops, so Builder, of course the
name is quite obvious, but we are a very heavy AI tech company, so we have a lot of models that we
run. We have a lot of LLMs that we use. There are more than 20 services that
are running around LLMs in production today, which really involves that we need to
have a lot of observability around it. And these are just not regular
services. Like there are OpenAI stuff, so there needs to be an agent around
OpenAI so that we can see tokens, we can rate limit people, we can see what is the cost and the
amount of metrics that going that is going out. So all of those pieces. And along with that we have our own local
models as well that we would want to put in some sort of pre
or post observability so
that it's easier for us to track what happened in
this customer interaction. I'll take a pause there. Thank you. C.

