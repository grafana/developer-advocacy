# 5 Years in, Loki Turns 3.0 | GrafanaCON 2024 | Grafana

Grafana Loki was announced at KubeCon + CloudNativeCon in Seattle at the end of 2018, and five years later, the popular ...

Published on 2024-04-25T22:51:27Z

URL: https://www.youtube.com/watch?v=H_7yHut6hvw

Transcript: Oh yeah, I need the clicker,
Cyril. Oh, I can talk. Alright, so we're going to talk
about five years in Loki turns 3.0. Okay. Alright, here we go. Thanks,
bud. You can leave now. You're, you're, you're done. No. Okay. Yeah, so I, I mentioned earlier Cyril and I have
been working together for a long time. Both responsible for putting a
lot of bugs in each other's code. So hopefully some of y'all can kind of
share that experience.  yeah, so Loki 3.0 5 years in touch on a couple
of these things earlier. I will pace, so beware. So let's take a
look at what this brings. But before we do, I want to take a step back and kind of
look at some of the initial things that we wanted to do when we set
out to build the project, how that's changed over time and how
it still influences what we do today. Basically what changed and
how it stayed the same. Okay. anyways, these were from the slide earlier when
I originally put together this deck. I didn't realize we were going to be doing
the keynote and then this like almost immediately after. So you've just seen this and I have some
extensive notes I'm reading down here. It says, growth and exciting. Thank you. So how do we get here? It's really helpful for a
project to have a clear purpose. So ours was distributed grip, you know, for developers and
operators. Okay. Helpful. We really try to focus on ease of
use for targeted search initially. And if you kind of go look at the, the somewhere out there is still the old
Loki design doc and it has like a lot of things that we do now. And it was like, we're explicitly not going to do these
things, but things, things do change. So it's built on a couple
of these principles here. Standard cloud infrastructure, right?
More and more important in today's world, right? So it's microservices orchestrated
in Kubernetes, written in go. But we also have other forms to run this. You can kind of start small
in what we call single binary, where everything is co-located
in the same process. That's helpful for development, but
you can also kind of extend that and, you know, run small projects. And then
there's an intermediate mode we call SSD, simple scalable deployment,
which is, you know, if you're trying on microservice,
you want some distribution and, and isolation between different
components. And then finally, you know, the kind of full-fledged
thing. That's kinda what we, we run in cloud and a lot of
people run for larger scale things. Basically we can go from your laptop,
you know, or your Raspberry Pi to, you know, thousands of cores in the cloud and
there's some configuration difficulties, but all in all, not too bad. We
also separate storage and compute, and this is really helpful when you
want to scale them independently. And my favorite one here, I'm going
to be talking about this a lot today, bites not records. Loki is schemaless. This is really important and really
fundamental to the nature of the project. We do not care what your logs look like. They can come from NGINX pods
that you do not control really. They can come from things
that you do control. They can ingest JSON and log format
and all manner of other stuff. I've seen people put GIFs in
Loki, do not do that, please. But I have seen it. So this is what it looks like. Basically there's a couple
different pieces here. Nanosecond precision
timestamps-- these are indexed. Prometheus style label
pairs--we use Prometheus as
a library internally in Loki, built basically build
on top of that project. So the same basically key value pairs
you use for Prometheus labels we also use within Loki and
helps you correlate these
two things--logs and metrics. And then finally, all of the log content. Actually I don't like this slide
because the log content is tiny here, right on the right. But in like reality,
it's many, many times everything else. So I need to change that.
But anyways, no schemas. You can ingest stuff from anywhere,
any team, any language, no problem. This does pose some challenges
and we'll talk about that. So what does this minimal indexing
look like in practice? Now for us, this is from one of
the, we call them cells, but Loki database clusters
that we run internally. Ingesting was 43 terabytes
a day of raw logs. And it comes up to just shy of
200 megabytes of index for that. So in real terms, that's somewhere over
200,000 times smaller for the index. So this is not really a traditional
thing. It's a table of contents, not an appendix. It
tells you where to look. And then Loki basically
scans the appropriate data. And we could paralyze this in many, many different ways across the commodity
hardware that we talked about earlier. So, oh, this next slide is fun. I went and looked back through like a
bunch of our old releases, put them up, mapped them. This took me an enormous
amount of time to make actually, so you better appreciate it. And it shows kind of the
velocity of the change. Sure, like as we add different features, but there's some other stuff
underneath. And, this is not exhaustive, but illustrative. I tried to generate this image and it's, the idea is that you kind of have
to balance scale with features. You always want to build new
features for users for yourself, and hopefully those are the same
user base. And then the other side, you know, sometimes you have to kind of eat your
scale vegetables beforehand to get there because you know it's ever
increasing need in today's world. So this is the previous slide, but again, kind of overlaid with all
of the kind of maximum, the fastest queries that we would see
running at kind of different phases of Loki's evolution. And this is
kind of a really fun one. It's, it's non-linear, the growth here. One of my kind of favorite anecdotes
is back in like the really, really early days, we ran
about 10 gigabytes a second
maximum query throughputs. And by today's standards, I
mean tiny, right? Yeah, yeah. But it actually works. It worked for us as we were building
out Grafana cloud in the early days. And I still hold it--it's still
highly usable there. But anyways, so it kind of shows how we've
tried to balance these two things, adding new features and support for
new use cases while also being able to support, you know, the underlying
scale requirements of it. So Loki 3.0, there's a kind of a change in how we
think about some of these problems. Because up till now we've really
improved query performance mostly through additional horsepower, you know, new ways to paralyze and kind of distribute work across, you
know, thousands of core. But the future is probably not
more of that. It's probably less. It's probably not scanning more faster. It's not scanning stuff we don't need to. So being more efficient with our time
and our energy and our resources, while also staying true to a
lot of our principles here. And so story time this is
something I found out last year. So Loki stores its data
in what we call chunks. They're compressed logs that we
dump in object storage somewhere. 75% of the time that we spent downloading and querying chunks was
completely useless for our purposes. They were requested, like the
queries wanted to iterate that data, but it turns out there was never going
to be what they were looking for inside. So like, this is what I mean, right? We probably want to work a little
bit more efficiently. Okay, so how, how do we do that? Because this becomes
a lot when it starts being measured in, you know, petabytes of data and thousands
of CPU cores and things like that. Yeah. So , I've kind
of got a anti schema rant here both because Loki doesn't
really likes schemas, but also because I used to run into
this problem all the time where I would build out using things that
that kind of required really, really the rigid structure. And I
ended up spending more time in my org, like working on pipelining backwards
compatible changes through everything, you know, than I was on actually getting value
out of the things I was ingesting. So we need to do this, but we need to maintain simplicity rather. And indexing here is like
the super obvious choice,
right? For a lot of reasons, but kind of wanted to challenge
ourselves here and do this in a way that didn't kind of fall prey to some
of those things I just mentioned. So it kind of comes down
to a couple points here. We want to stay true to
the schemaless, you know, unstructured search that Loki has
always done. And then the other one, which is the kicker, is unstructured data kind of lets
you ingesting that is a really, really nice benefit, primarily for
operators and to some extent, you know, developers and whatnot. But we want to extend those same
easy use benefits to people querying Loki. We don't want them to write
huge query plans and really, really, you know, painful, long, exhaustive things to be able to get data
out and to get data out effectively. So we want to write
something that's transparent, meaning that you can get faster queries
automatically that are more efficient just because it can kind of
detect what you're looking for. So this is actual photo of me
when I was a little younger and  again, end of last year, we were kind of going back and forth on
a lot of these kind of more traditional ideas and I was sitting here
kind of asking myself like, is this possible? Can we do this with these kind of
constraints that we've given ourselves? And so brief aside, it's really important to surround
yourself with people who will like, push you to not do the thing
that's most obvious or easiest at hand, but to like, you know, keep uncovering the next idea until you
get to something that you're really, really excited about. And so,
Cyril's one of these people for me, for sure Ed Bryan, some people on the databases
side of Grafana Labs really kept trying to get me to find the next
thing. So one day I had this idea, Hmm, okay, what if we took an impossibly
large amount of data and, you know, put it into an
unreasonably small space, right? Basically make a sketch of what
your data actually looks like, but don't store it in and in and of itself Because a sketch doesn't have to
be precise when you're interested, where the data isn't. You just care where the lines have
been colored in and where they haven't. And in our case, if you remember back to
the 75% of data being "bad," you know, not necessary for our use
cases, that's just as, or arguably more important than the
25% of data that we actually want. And so, in a way, eliminating data that we don't want is
the same thing as finding data that we do. So I started putting together an idea
and it kind of felt like a mirage. Again, I try to generate this picture too.
I think there's like a monster there, but the idea is, you know, there's a
mirage and you're kind of, you know, you can't tell if it's real. So we went through a couple iterations
of things that seemed like there's no way this is going to work. It's going
to be impossible for X, Y, Z reason. These are some of them--sort of
building some of these experiments, knocking down, you know, bowling
pins one at a time, so to speak, and finally got to the point where,
hey, maybe we should just, you know, build it. So looking at time, I'm going to go a little
quickly through this section. We're going to be at the
booth later at the AMA. So if you want to come kind of talk
about how this works internally, please love to nerd out
about that. So anyways, bloom filters in 30 seconds,
as I say up here, . Basically this is--I think about this
as like a kind of negative search. We invert the problem. All it
does is takes, you know, keys, it maps data into buckets, and it just
knows if the bucket is empty or full. Now, the cool part about this is that
you can then compress that down. Well, reduce the size of it because that
something being empty or full is basically just a bit, you know,
it's a zero or a one. So you can get a lot of data
into a very small space. And next bit here N-gram--this
has long history and you know, full text processing, things like
that. They're just character sequences. Fancy word for character sequences. These are the trigrams
and can be any number. These are the trigrams of length
3 for the first 1, 2, 3, 4, 5, 6, 7 letters of the alphabet. So what if we take these
two things and combine them, we ingest all of your data,
we extract N-grams from them, we put them into Blooms and we cross
our fingers, right? Like, does it work? ? now it turns out that this gives
us the ability to kind of index unstructured data, but to do
it in a space efficient way, kind of combining these two properties
to automatically index everything. Now, brief example this
is like a, you know, HTTP path, you know, so I'm looking
for /users, if I want to query on this, I basically have to run all of
the N-grams and test them all. And if a bloom returns like
says, oh, hey, you know, I match all of these things, then
I know I need to check that data, otherwise I can discard it. So
the next kind of big question, which I spent a lot of time trying
to really, really understand was, I guess two things, right?
Well, one, why is this so big? It has to be too much data. I remember
talking to Tom here somewhere, and I was like, first thing that he
said to me, he was like, there's no way. And I was like, I know. But anyways, so it turns out that logs are about 90%
template and 10% variable, you know, on average, give or take.
But that's the idea. So here's a real example of what
a log glide kind of looks like by, you know, partitioned, by how often
that is repeated over successive lines, right? So we realized that a lot
of that is just there all the time. This template, some of
it changes a little bit. And then a few things have
really, really high entropy. So basically the noise
here outweighs the signal. Now there's a cool property about Blooms, and it's that duplicates
are completely free. So you can kind of see
where I'm going, right? Yes, this should create a lot of data, but because there's so much
noise relative to the signal, so much duplication of
data, of templates, it actually ends up working out. So we, we've run this in a bunch
of different places, but basically we see the size of Bloom
filters at around two to 3% of the underlying log size. So what does this actually look like? Here's kind of an example of a log QL
query and, you know, fizz 1, 2, 3, 4, like some UID basically
transaction ID, if you will, right? So kind of support use case. We're seeing these types of things
a lot more in Loki, you know, not just the developers and the operators
kind of scanning the logs when they understand their systems and
understand that, you know, I care about this application from this
cluster at this point in time, but hey, you know, I'm coming, I'm
looking for support logs. I'm looking over all of my
prod infrastructure for this
over a week long period, because I don't know where it comes from
and I don't know what my infrastructure looks like. So turns out this is
unique and it has a lot of N-grams inside of it,
right? So we can test that. Now, one of the really cool things here, so this is an actual example
of what this looks like for us. And we're filtering out, you know,
90 something percent of all the data, and this happens automatically. We are implicitly looking at what
users are querying for in our examples, kind of filter expressions, we call them
in Loki. And we are extracting that, we are running them against the
blooms for all of our queries, and then we are just discarding a bunch
of data that we know will never match. All in all, the root of that
idea is very, very simple. This is where we're at right now. So I said experimental support
and  very that's very true. So it definitely works. There's
going be a 3.1 at some point, probably next couple months. And by that point we'll probably be a
little bit further along and really, really operationalizing it and
making it easier to run for everyone. And there's also a kind of a number
of things I want to clean up to tighten it up. I ran through
these pretty quick. Yeah, you're going to have
some time for the demo. Cyril's going come talk about Loki and
OTel. Thanks for your time everyone. Alright, thank you. Everyone loves OpenTelemetry. I mean vendor not all
standardization, the problem is Loki, doesn't really like it. It has been built for unstructured
data and ultimately OpenTelemetry specification is actually structure. So it makes it hard for the Loki backend, but also the UI--the
experience is not that great. So in terms of querying, obviously we are trying to make
OpenTelemetry and 3.0 much better. So you're not going to need the new JSON parser in your queries.
We also improved the UI, so it's going be a bit better.
So you're not going a big blob of JSON which OpenTelemetry
ended up being. And operationally you're also not
going to need the gateway anymore. So we used to have like
another component to ingest and transform OpenTelemetry format
into what Loki could understand. So it would be natively, so from now on Loki will be
natively supporting OpenTelemetry. We also used that opportunity
of a big release to clean up. We did a lot of cleanup, mainly
configuration. So, you know, we've been running Loki for more than
five years and it was a good time to update the default with all
the experience that we have. And also make some breaking changes, like remove some storage that
we were supporting before, some legacy features that we
don't think should stay there. And also improve the metrics. Make sure that all the metrics
that are in Loki are valuable. So we did a lot of cleanup. Helm, so we are going a bit bigger on Helm. We used to actually not be that big
on Helm because we are  at Grafana. But the community wants
Helm definitively. So, you know, we, we are going a bit bigger and we have
like three different installs depending on what you want: what you want to use Loki
for. So single binary for the Lab kind of
installation. Simple, scalable, if you just don't want to run
the big thing from the start, but still scales with like a read
and write path that is different. And then the distributed version, which is the one we actually
use at scale at Grafana Labs. And that one scales you know,
to the terabytes per days. You are going to see the docs in 3.0, big shout out to the Docs team
but also to the whole team. Alright, last section. So I touched
on this already during the keynote, but I want to, you know, tell this story
'cause I've seen this story many times. "I don't want to learn Loki," you know
and I've been biased on that because, you know, Owen and I have been using Loki for a
long time and we find it super powerful. So I was like why? You know, what's,
what's the deal? And I realized, okay you know, SREs, platform
engineers, they usually like, you know learn PromQL and
then they transfer that into
LogQL and then they build dashboards like this one with
like mixing logs or, you know, building metrics out of the
logs and it works well for them. But then they go to the app developer, which normally should be focusing
on their business, right? Not learning another language.
And it's too complicated for them. And they don't want to learn a new
language or not necessarily you know, from the start, like get value
without having to learn a new language straight away. So yes, that's
actually a quite complicated query. I bet not everyone in the
room understands what it does. And so I think this has
been a big problem for Loki. And that's what we try to
solve. So first iteration, I think Torkel touched on this. During
the keynote we were like, "Okay, let's just make a query builder." But
then the problem is you still need to understand the data model. You still
need to understand the query language, because ultimately you're still
building a query. Instead, we decided to build a new app, which we called Explore Logs, doesn't really require
you to know about LogQL, but more to explore the logs and
use the app and just clicking. I think everyone loves clicking,
especially Matt and Jonathan. Alright, we have time. I'm going to show you a couple of features
that I haven't shown in the keynote. So let's do that! Cool. You want it full screen? Well we can, yes, do the full. Screen. Yea, I can do it this
way, yes. Oh yes, good. Cool. Alright. Alright, let's
do it. Perfect. All right, so I'm going to start with so
this, as opposed to earlier today, this is actually a real workload.
So this is not like generic data. I wanted to show you how it
looks like in our dev instances. So the first thing I haven't shown is,
you know, you can search logs obviously, you know you have a text
box and you can start typing words and you don't necessarily
need to know about the language. So this is something that I didn't show
earlier and it reacts automatically as you start typing. So
again, no query language, just trying to explore your
logs and find what you looking for. I want to touch on the labels. So let's see if the wifi can do it. So this one has much
more labels than before. So maybe I'm going to need to
refresh the page. Not sure. Alright, I'll give it to refresh.
Alright, here we go. I want to show you something is Grafana
Labs and probably like in any company, it's quite hard to keep all labels under
control. Like we have a lot of them. But we have a new API in Loki 3.0
that is actually trying to tailor and only show you labels that will be
interesting for you to break down, and, and use to filter down. So things like ID usually will go away
automatically or will not be shown by default. Things that are like too high cardinality
past the 500th element, you know, it's almost going to be impossible to
use that to try to figure it out how to filter with it. And so we
try to use the right label, like level containers, pods, to try to find inside your label.
And Loki does that automatically. I want to show you the detected field,
how it works on the real workload. So this is actually you know
Grafana Agent running in our dev cluster and it's kind of very
interesting to be able to see, you know for the color, which is
a very popular log format fields, which gives you the log site where
that log comes from in your code. And you can have a sense of, you know quickly how much each gofi
here is actually logging. So this one is actually very iterating often. You have
also, for instance, the components. All of those are extracted directly
from the log line and you can, you know use those to filter. So I can add one now I'm
filtering on cluster. I want to show you. So I'm going
to remove this filter here, Carlos. Let's go . All right,
so again, that's the pattern. So I wanted to show you the pattern
now it looks like on real workload. And you can see the trend again
of, you know, that one here. So the way the pattern works is that
it's going to actually add white card in element that are viable. And then everything that is the same
between all the log lines it's going to group them up as a time series
and show you the pattern. That is a kind of powerful way
to see a huge amount of logs, but restrained to just couple of
like different patterns. Again, this is a new API that
we added in Loki 3.0, and we are going to keep working
and making it better. It's not, it's not there yet for some of the
other format, like JSON is a bit harder, especially if the key moves around. Some
people really like to have JSON and, you know, the order of the key going
differently, you shouldn't do that. So you can use those filter to
filter down, you know and, and only look at this patterns of log
and get detail of that specific pattern. So I can look at all the different receive file watcher event, but all
the different names here. So very powerful to
explore your logs without having to write a single query. The pattern is actually a new a new
syntax that we added in LogQL and Loki 3.0. So what you can do
also is open and explore. It's actually going to show
you the query that it's using. So you can learn about LogQL by using
the app and you can share it with your colleague. And you can also use that to
just add it to a dashboard. You know, you can go and then add to a dashboard
without having to type anything. You know, I'm a beginner in Loki and I
can quickly go and use it. So, you know, we really want to make it easier for the
app developer to get started on using Loki without having to learn the language. So this is just the beginning of this app. We really work only four weeks
on that. We're just going to, you know invest much more.
We have a lot of ideas, a lot of new features that we want
to build. Also want to, you know, make it a bit better and do some
tweaks and adjustments, but really, really proud where we
landed. So, you know, again, big thank you to the team who work on
this and also everyone who worked on Loki 3.0. I think we can
switch back to a slide. So I think we have like two minutes.
Should we we have two minutes left, so maybe we can take some
question, right? Let me see, right? So I already showed that slide, so
if you don't want to install it, you can just go on play.grafana.org and
then just give it a try that, you know, if you want to show it to your colleagues,
you don't even need to install it. Obviously this is new. So do provide feedback in the
channel community well Loki channel in the community Slack or directly
create an issue on the repo. Thank you.

