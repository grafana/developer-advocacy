# Observability 2.0 in the Real World: Lessons from SimpliSafe’s Engineering Journey

In this candid and insightful talk from Observability Sessions Boston, Laban Eilers, a platform engineer at SimpliSafe, takes us on ...

Published on 2025-05-22T20:54:32Z

URL: https://www.youtube.com/watch?v=Z6WCs9p4yjE

Transcript: Hey, I'm Laban Eilers, I work at SimpliSafe and I'm going to
do this talk about Observability 2.0. Let's see. I don't really know how
to work this. That works. Okay, so a little about me. I'm a
sort of generalist developer. I did a lot of really, really early front end stuff
before Chrome or jQuery or things like that, and spent about five years, about five years ago doing
mostly engineering management. Discovered it wasn't really for me, much happier back working
on platform engineering, which I've been doing for
maybe the past six years, just hands-on and I'm
much happier this way. So I work for SimpliSafe
SimpliSafe. We may have heard us, if you listen to podcasts or NPR
something, we sell security systems. What's kind of different about SimpliSafe
versus a lot of other security systems is that our actual product is
the outcome around security. We're not really trying to sell cameras, we're trying to sell safety
in your home for your family. We have this really cool new product. Essentially it's service called Active
Guard where you have a camera mounted on the outside of your house. It's using AI to recognize the difference
between the Postman and your dog and the kids versus an actual intruder. And if somebody's there who's not
supposed to be one of our monitoring agents, a human professional monitoring agent is
going to start talking to them through the phone, at which point
most of them run away. So it's an actual really
effective deterrent against actual danger. So we have our systems all cloud-based, and we have many hundreds
of microservices with probably in total, many thousands
of replicas across many regions. And I just want to assure
my host at Grafana, I am going to talk about
Grafana and why I love it, but there's a little journey involved.
We're going to go on a little journey. All right, so observability 2.0. Observability 2.0, sort
of a marketing hype term, coined by Charity Majors who if you
haven't, you just don't. Follower. She's prolific blogger and thought
leaders, the CTO of Honeycomb, and just a fountain of insight on all
kinds of stuff, not just observability, but engineering management and other
stuff. I highly recommend following her. So yeah, the term observability
2.0 was something she came up with. It very much describes Honeycomb,
which you could understand. All that aside, I think it's a really useful framing
and a way to think about what observability could be if we
kind of started from scratch. So first, let's contrast
it with observability 1.0. This is Charity's definition. So this
is centered around the three pillars. So logs, metrics, and traces. You really have a lot of
duplication between the different signals you might have traces and logs
representing the same events or metrics summarizing the same events
and metrics is really kind of the workhorse of the
observability 1.0 paradigm. It's it's much more about monitoring, so knowing when things go wrong than it
is about deep understanding of a system. And dashboards are probably the most common symbol I
think of observability 1.0. So in contrast, observability 2.0
centered around the idea of wide events. So wide events you can think of if
you're familiar with logs that maybe structured data like key value pairs. Traces are also considered wide events.
You have a single source of truth. So I think in charity's definition, it's like you actually have a single
data store for all your telemetry. And in contrast with observability 1.0, you have the ability to ask questions
iteratively of your single source of truth. And the idea is that you understand, understand your systems behavior
much more deeply than you do, just knowing when you're
getting to error conditions. So yeah, in this model, you're taking a single data store and
then you can ad hoc ask questions that you didn't have to know the answer to or you
didn't have to know you were going to ask in advance, and you end up getting
metrics out of these wide events iteratively. So
oops, went too fast. So wow, this sounds amazing, right? Why would I want to pay
store my data three times? Why wouldn't I want to be able to
ask ad hoc questions all the time? This sounds amazing,
right? As with most things, there's tradeoffs involved. So I'll discuss this in
kind of four sections. The idea of metrics. Metrics are fundamentally trade off
the notion of sampling the limits of the current state of tracing and
the maturity of the ecosystem, especially around OpenTelemetry.
So metrics are a trade off. So metrics are a series
of measurements over time. So a metric is fundamentally
an aggregate of a particular set of data. So instead of tracking individual events, a metric is a summary of all
the events that happened in one interval of time over a long period. And a metric you can think of as a
traditional metric, you can think of it as an answer to a specific question
that you have to know you want to ask up front. So some example metrics
request per second, the percentiles of a particular
latency, distribution percentage of something
that results in an error, excuse me. So something that's fundamental about
metrics is they have low cardinality or to be useful metrics,
have to have low cardinality. This is just a fundamental
kind of physical limitation
of time series databases. So time series databases are the most
efficient way we know of the store metrics and they work really well
with low cardinality data, not so well if you start adding very
high cardinality fields. So for example, like a user id, if you
have millions of users, that means you're going to have millions
of time series that have to be stored in memory in your time series database. So it's just not useful once you
get to that scale with cardinality. But it's okay because in metrics, you think about metrics in terms of big
picture trends, not individual events. So you're looking at all the events that
happened within 30 seconds and give me some meaningful number that
describes all those metrics, sorry, all those events. So just to illustrate the difference
between the observability 2.0 and the observability 1.0 model, in the 2.0 model, you have this single data store for
wide events from which you can just ad hoc ask questions, whereas with the more
traditional metrics model, you're defining your metrics in code, you're writing some go code that goes
into your application that answers a question that you knew you were
going to need the answer to upfront. Okay? So you're going to ask Laban,
why would we ever use metrics? Obviously the other solution
is much more flexible. The answer is the cost
discrepancy is ridiculous. Metrics are absurdly cheap when
you compare them to the cost of storing high cardinality wide events. It's just a really compact representation. So a metric is just you describe a
metric with a set of labels and values, and then that's just at
the beginning of a metric. And then after that it's just a series
of numbers. So that's a very, very, very tight representation
of a whole lot of data. There might be millions and millions
of events that you're representing with just a series of numbers. So the trade-off is fundamentally
one directly between cost and power. So just as an example on the left, we have a metric, we we're going to talk about an artificial
case here where we're measuring HTP requests for a particular microservice.
Let's say we've got 10 pods, they're getting about a
hundred requests per second. So a total of a thousand requests
per second over the 10 pods, the things we care about,
half method status codes, stuff that you think about per http
request. And if you combine, you take the, you combine all, sorry, all those labels, you get, let's just say a hundred unique
combinations in practice of actual label combinations. On the right, we're going to represent the
same thing in a wide event. So this means we have effectively
unlimited cardinality. You can store any data we want, but we're going to be storing every
individual event with all of its data. So the difference, and I took
here on the left, we've got, I think this is Grafana's list pricing
for Mimir-their metrics product. And on the right I took
Honeycomb's list price. I'm sure they'll negotiate better
deals with you guys if you want. So you can see there's already
a pretty tremendous difference, several orders of magnitude. And fundamentally you're generating a
thousand spans would span meaning a wide event per second. If you have
a thousand requests per second, you're generating a thousand spans per
second with a metric you're generating only the number of series you
care about. So in this case, it was a hundred series. Let's
amp this up a little bit. Let's say we fixed some bugs, we got
some performance profiling going on. Now we are able to handle a
thousand requests for second. In Honeycomb, my bill went up to $33,000
a month because I just 10x the time, the amount
of spans I was generating, but I still have the same a hundred
possible combinations of metrics, so I'm not paying a single dollar
more. That's pretty crazy to get off. Alright? And now I'll
do a little plug for, or one of my favorite Grafana
features, which is Adaptive Metrics. Adaptive Metrics allows me to aggregate
away labels I don't care about. So of those a hundred metrics, maybe
I don't care about the pod label, I just care about the metrics
in aggregate across all my pods. So I've reduced the series down to 10
series instead of a hundred series. So now I'm paying 80 cents a month, still paying $33,000 a month If
I was doing this in wide events. And you're going to say, Laban,
this is a totally contrived example. There's no way this is
reality. It really is. In SimpliSafe we have all three, we're utilizing all three pillars. And
there is indeed an order of magnitude, a cost difference between
metrics and in this case traces. But as you remember, it's the trade
off. We are giving up something. Of course, if I could use wide events
for everything and I could afford that, awesome. I would also love to only
dine in Michelin star restaurants, but that's just not in the cards for me. So how does anyone actually
afford wide events? The answer is sampling. So I mean I guess there comes a time
in many the lives of many platform engineers where you might have
some uncomfortable feelings, some new feelings about
your observability bill, and you might want to engage
in some risky behaviors like statistical sampling, but I
don't want to shame anyone. This is a normal and healthy behavior. So statistical sampling with traces, you generally have a system
that intercepts all the
traces you're generating across your system. And then just statistically sample, like say in our case we sample about one
out of every 30 traces that go through the system. And then this is a pretty
cool feature of Honeycomb, don't know if Grafana does this, I
hope they do add it if they don't. But it does statistical
extrapolation at query times. So you're looking for a particular
event that happened over a period of time and it'll say, oh,
well I've only got one of these, but I'm going to multiply the value
that they're looking for by 30. So it's pretty opaque to you as an
end user and just get a sense of the real values of, and this
is built in into OpenTelemetry. Yeah, sorry. OpenTelemetry has the
primitives that make this possible. So they have things like the sampling
ratio as a property of the events. I feel like the person that this happened
to with me is maybe in this room at this point, but I was at another Grafana event
and I was talking with someone about Honeycomb and they use Honeycomb. And without thinking, I kind of blurted
it out like what's your sampling ratio? And then the table went quiet and I was
a little afraid I had made a faux pas that I wasn't aware of, so I apologizd
to that person if they're in the room, if I need you uncomfortable. I can't possibly divulge
this in confidence. So there are some challenges with
sampling. It is a really powerful tool, but it has a ton of moving parts. You have notions of head sampling
versus tail sampling. In head sampling, it's like the producer of telemetry
has to decide what to sample the tail sampling. You're waiting until traces come from
all your different sources and get assembled into a larger trace and then
you make decisions about sampling much more powerful. And in practice,
that's really what you want to do, but it's really complicated. You need a lot more infrastructure
to make this all happen. There's a lot of things that can go
wrong on the way to doing the actual sampling decision. And because
you're doing statistics here, there's a margin of error. And if
you're a person asking questions, you don't know enough about statistics, you might not be able to judge how
accurate the answers really are. And this is maybe more
of a question of human techno-social systems,
but one programmer can, because of the nature of traces
flowing through multiple systems, one programmer can make a mistake
and one system that flows all the way downstream and you end up with
wacky answers to queries downstream. And this has probably been the hardest
thing for us personally at SimpliSafe, that we have a lot of these use cases
for observability that are sort of like forensics. We have a particular security camera
that didn't do something right, didn't log in or a video frame
got dropped or something. We want to go look at logs for that thing. In the case with these sample traces, when we're sampling away
29 out of 30 traces, the odds are it's not there anymore. So we just can't rely on traces
for these kinds of use cases. And luckily this hasn't
happend to us, I say luckily, but we take security
very seriously obviously. But if we were trying to investigate
an actual incident where we had a breach or something, could you imagine trying to do that
with sample data on your security audit logs? You really need a
hundred percent of those logs. So overall sampling is an
incredibly valuable tool and it allows us to afford
tracing and tracing. I mean if you guys haven't actually used
it is an incredibly valuable tool for understanding a big distributed system. It's hard to imagine how we would solve
a lot of the kinds of problems we have without it and sampling
makes it affordable. But I think the caveat
is you need something to
corroborate the answers you get because they can be wacky sometimes. And what's great for corroborating traces, logs and metrics are
fantastic because you're doing the calculations in
completely different sets of data. You can have a lot more competence
that you're getting the right answers. And there's some other just
limits of tracing at the moment. Maybe these are all solvable, but right now in practice
they really are a challenge. A big one is third party code. So if you're running a Kubernetes
distribution and you have a whole bunch of system components, odds are they're
producing metrics and logs but not traces. So you just won't have a lot of visibility
into those if you're relying fully on traces. Long duration events, events that are more than say hundred a
half or two are just sort of an unsolved problem in tracing -
in OTel in particular. half, sorry, [Audience question] you
say longer than how much? [Laban} I'd say between a minute
and a half and two minutes. I mean because your traces come into a
system that's going to do sampling or aggregation on them and it has to batch
them up and you don't want telemetry data behind more than a minute or two. Another is if you have an asynchronous
system where you have different processes that have say message queues or
something in between them and they're not actually linked by a
request idea or something you'd need to correlate trace. It is really hard to actually follow
a trace all the way through a bunch of asynchronous processes. And then the just really basic
stuff like an application crashes, traditionally we'd get the
stack trace or something or the memory dump or something
in a crash report in logs with tracing. The tracing is usually
done inside the process itself. You usually have an SDK installed in
the application and when the app crashes that all that state that you've
been building up is gone. So it's really hard to
debug a crash via traces. And then there's just things where
it's not technically impossible, but it's not a great modeling fit. It's hard to model things like background
processes and startup and the events and stuff in terms of traces because
they're fundamentally about a series of linked requests, not about
individual events that happened. And then just in practice, we've
had our fair share of foot guns regarding tracing. Graceful shutdown is really important
to get right because as I mentioned, tracing is sort of accumulating
telemetry state as you go and then flushing it at some interval. And if you're shutting down when you still
have state to flush and you didn't do your graceful shutdown properly, you're going to drop spans and then
you end up with indecipherable traces. We've found and sometimes fixed
a number of context propagation bugs traces really require
context to link between different systems spans. And there
was this one nasty one in, there's a NodeJS library called Bluebird, which we had been using for a long time. And it was ultimately
discovered it was the source of context being dropped across
async tasks and NodeJS, and that was a source of a whole lot of
pain. We finally figured all this out, we've got it working nicely now. And then there's the overall
maturity of the ecosystem. So Honeycomb did approach us about going all in on observability 2.0 and
replacing everything with traces. And we had already had some
of the experiences we had
talked about with tracing and had a sense that generally
the ecosystem wasn't ready for it. And in gathering the context across, gathering the opinions of my colleagues
and some folks from Grafana gave us some pretty good tips on this. They pointed out the virtues of
some of the more traditional, the two more traditional
pillars. So logs are everywhere. They're produced by everything,
they're rich and high cardinality, you can query the heck out of them. The developer experience
for logs is amazing. You do print F and you get a log in
your terminal and you can grep it or whatever you want. And the stuff has been going on for
since the dawn of computing, right? Like logs, everybody
knows how to use logs. And as we've learned, metrics are
not only simple and ubiquitous, but absurdly cheap. When you
compare them to comparable events, they're very efficient and
fast, not just at query time, but when you are in
your actual application, producing spans and logs is a lot
more expensive in terms of memory serialization, FU time network than metrics because
metrics are just sending a number every 30 seconds or so. And just the reality of the situation is
if you look across mature industries in the world, manufacturing
and telecommunication stuff, they all run on metrics. This is a problem we've solved around
when you're talking about monitoring known infrastructure that we
understand its behavior. You cannot beat metrics
for cost effectiveness. Okay, so all that said, I still think observability 2.0
is a really interesting North Star and it's a pretty compelling vision
if you're not bringing black and white thinking to it. I think it's something that we can sort
of think of as a target we can move towards incrementally. And instead of thinking very literally
about Charity's description of it, I'm sort of thinking about the outcomes
she's describing rather than the implementation details. So I think I'm thinking of
these in these three categories. So affordability, the cost difference between the time
series database and these wide event databases. I think it's
fundamental to the data structures. It's not something we're ever going to
be able to completely make it go away, but we can probably narrow the
gap a lot more than we are. There's already been a ton
of progress in that. Oops, I don't even have Adobe.
What is this? Oh, sorry, I'm getting an error message on
top of my Oh, this is your machine. That's my machine, yeah, sorry. There
we go. It popped up an Adobe thing. And just a caveat, I'm talking about
wide events being an expensive source. I'm just going to compare it,
I don't want to name names, but compared to certain dominant
rent seeking observability vendors, like something like Grafana or
Honeycomb is not that bad at all. And there's a lot of really cool
stuff going on in open source around, in particular around columnar data stores, which seems to be a really
amazing product or product design pattern that comes
out of analytics products. We've been using this, I mean this
has been around for many years, but it's sort of making its way
into the observability space. There's these open source products
like the Apache Parquet format, Clickhouse, which is an analytics database which is
beginning to be used really successfully for observability and Grafana Tempo, which I believe is a columner
data store of its own. That's, this is Grafana's tracing
product for those who haven't used it. So the developer experience
for OpenTelemetry is still a little bit rough. We've gone through the whole journey
and we're in a good place now, but it was a little
painful, a little trauma, but there's a lot of
things you can get wrong, all those drop spans and things
like that. But just in general, setting up the SDKs, it takes some fortitude
in your applications and instrumenting for us, 150 ish microservices is a big lift. But all that said, I just want to say if there's any
OpenTelemetry contributors listening, I love you guys. I like
you are doing God's work. OpenTelemetry is the
future. I have no doubt. I think of OpenTelemetry is
like where Kubernetes was seven, eight years ago. It's like obviously
it's the solution, it's the future. We just have to work together to
get it there. So I love you guys. So finally, there's the ecosystem, just the reality of the
state of the ecosystem today. The third party infrastructure, like all these Kubernetes components
and things that mostly admit logs and metrics today that's changing gradually. There are some new hotel
enabled things happening, especially in the Kubernetes world. The fact that tracing doesn't address all
the use cases you can handle with logs like crash dumps and things. Overall, I sort of think of this as
the ecosystem is ripe for a bunch of new innovation that can
solve all kinds of usability problems. So if you've ever used
the Prometheus Operator, you install it with a Helm
Chart and it just works. It's amazing until you get to a
certain scale. But it works great. It's super easy from a developer
experience perspective, I really want to see more OTel stuff
that works that easily and I'm sure we'll get there, but I think
we're not quite there yet. And there's a ton of amazing stuff
going on with eBPF, like Grafana Beyla. There's other products too. I haven't
used them. I would really like to, I wish I had them like three years ago
because they might've saved me a lot of time having to configure OTel SDKs. But I think it's ripe for some
really incredible innovation. So I think we want thinking about outcomes rather
than the actual implementation details. For Observability 2.0. The thing that's really cool is the
ability to ask ad hoc questions and not have to be stuck with the questions
you knew you were going to ask when you wrote the code. That's
the outcome we want, and I think there's other ways to do it. One of the main ways is I think tools
that integrate that take the three pillars and integrate them really seamlessly is just a much more practical solution
than trying to throw away all the history behind logs and metrics. And it's a way that we can incrementally
move to more dependence on richer data sources and maybe less on metrics, but still have the bridge to
the past and then just utilize the pillars for their strength. And you can also shift your dependence
when you have that kind system you can shift your dependence away
from maybe as you learn, a system becomes more mature and there's
not much active developing going on can shift more of the observability load
into metrics where it's a lot more cost effective. And then stuff where you're
doing tons of active development, you've got a really distributed system
shift more of your energy into traces where you can deeply understand the
behaviors of your systems. And that way to manage costs can
be incredibly effective. And so let me just point out the system
I just described where you can do all these things and you have the
power of those trade-offs. I think Grafana Cloud does
this really well. This seems, I mean I've never talked to anyone
about this idea specifically at Grafana, but it seems to be like the way they're heading all these new
types of richer applications beyond what you can do just with dashboards
that are integrating signals and allowing you to use exemplars to hop
between metrics and traces. Having dashboards that combine signals, being able to build alerts that
combine from different data sources. This stuff is actually really seems to
be really happening inside Grafana and the architecture seems to work
really well for it. That is it.

