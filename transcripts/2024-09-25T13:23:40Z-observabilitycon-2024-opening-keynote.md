# ObservabilityCON 2024 - Opening Keynote

Coming to you from NYC, Grafana ObservabilityCON 2024's keynote introduces the latest features and AI/ML developments in the ...

Published on 2024-09-25T13:23:40Z

URL: https://www.youtube.com/watch?v=GlIhZVhH48k

Transcript: Hello everyone. My name is Raj Dutt. I'm one of the co-founders and the CEO
here at Grafana Labs. It's my pleasure, my great pleasure to welcome
all of you to ObservabilityCON. We've got over 400 people joining
us here in my favorite city, my home city, New York. It's been a couple
years since we put an event on here, and it's really cool to be back. Who
here traveled from outside New York, by the way, to, to come? Wow, that's
actually surprising. So, like I said, welcome to one of the
greatest cities in the world, and for those of you who traveled from
the US welcome to the only city in the United States. The rest
of them are our villages. And that's a friendly jab to our
friends in the in the Bay Area. No, but in all seriousness, good to
be back. Really excited to be here. Hope you all are too. Make some noise if
you're excited to kick off with ObsCON. Yeah? Very cool. So, we've got a lot to share in this
keynote. It's jam packed, maybe, maybe two packed, to be honest. We were doing a run through a little bit
earlier and we're worried that we might go over time, but assuming we don't go over time or don't
go over time too badly, we will have, a Q&A session after the keynote. So
if you want to load up some questions, go ahead, scan that QR code, and we'll
try to make some time at the end. But like I said, I'm
here just for a welcome. We've got some really great presenters. You're gonna hear from some of the
Grafana engineers who are actually building these products,
making the cool stuff happen. You're gonna hear from Tom, our CTO, Jen, our director of product.
You're gonna hear from Manoj, one of our VP of engineering. And you're also going to hear from two
customers that we've partnered around to do some really interesting stuff. Specifically Aaron at NVIDIA
and Olin at BlackRock. So we've got a really cool
keynote scheduled for you. Also, hello to everyone watching the
live stream. You're not here, so you're not as cool, but, you know,
hopefully you're gonna have some fun. Alright, so speaking of events, you know, one of the coolest things about
my job is I get to travel a lot, and I love to travel. And one of the reasons I get to
travel a lot is we are an extremely international company. We're
a remote-first company. We don't have a single
office anywhere in the world, which makes life interesting for
1,200 people in 40-plus countries. You know, it's really nice
being an international company. It's really nice being,
having such a global flavor. And one of the things when we first
started the company that I used to tell investors all the time is
investors would say, "Hey, you're gonna save a lot of money on
office space." And I'd say, "Yep, but we're gonna spend it right back and
more on travel." And that has been the case the last few years. We really like getting out
there and meeting our customers, and these events are so important to us. And it's just been awesome the last
few years as we've spooled up our event cadence. You know, let's
kind of leave 2020-2021 in a repressed-memory state. But it's
really cool to, you know, meet customers, have these hallway tracks, and our event
strategy is really on fire. You know, we've had over 7,000 workshops
signups the last year. I think we've had over 80,000
people attend a webinar. You know, GrafanaCON is
also a key event for us. Has anyone been to a GrafanaCON in
this room by any chance? Alright, well, it is a different event
than ObservabilityCON. GrafCON's all about our community,
our open source projects. Not a lot about our commercial products. It's not necessarily focused
on observability. It's
all about our big tent, showing all the wide use cases
that Grafana is used for. We do these GrafanaCON local events
where we bring GrafanaCON content to your city. And it's really a
community-focused event, but this event, the one you're here at, ObservabilityCON,
is really our flagship conference. It's about our products. It's
really for our customers. It's focused on observability
and, again, welcome. We also have ObservabilityCON on the
road where we meet our customers again, wherever they are. In the next few months, the team's gonna be hitting
up São Paulo, Brazil, Paris, I believe London. But it's
pretty crazy. We've got a, a pretty crazy schedule from an
events perspective, but again, it's really nice and a pleasure, meeting
our community and meeting customers. So the last year has been an
incredible year for the company. In terms of progression, in terms
of maturity, in terms of stats, kind of three cool stats that I'm happy
to share that we've talked about is we now have over 25 million users
within the Grafana community. That's overwhelmingly open source.
That's our entire business model, right? We want to create a really large pie
and monetize a very small piece of that pie. Um, and it's incredible to see how
the Grafana community continues to grow. With over 25 million engineers and
developers using our software every day. The company itself has also made
quite a lot of progress from a commercialization standpoint. We now
have over 5,000 paying customers, which is pretty incredible given where
we started, which was obviously at zero. Um, and, uh, you know, we've managed
to kind of monetize, um, a fair bit. Speaking of monetization, uh,
this stat blows my mind, but, uh, we announced that, uh, earlier this year, the Grafana Labs has hit a $250 million
annualized run rate from a revenue perspective, um, which is
pretty incredible. That's, uh, over $20 million a month in
terms of revenue. So, who, who here is a customer of
ours, by the way? Excellent. And who here is a potential
customer also? Excellent. And we should take a photo of that
and pass it to our sales team. No, just kidding, . But in all
seriousness, you know, these stats, we couldn't have done this without you.
Uh, we really appreciate your support, particularly customers who've been with
us for, you know, since the early days, the platform, the breadth of our platform, the completeness of the
vision has really, you know, kind of improved a lot the last
few years and this last year. And we're eager to share that
with you during the keynote. We've also achieved some recognition
from across the industry. I'm not gonna list these accolades, but one of the interesting things that's
happening for us as a company is we're maturing and kind of moving beyond
our open source community and starting to really go more head to head
with some of the other observability players in the marketplace, right? And that's part of a journey
that we're really excited about. Because we have ambitions to become and
be the dominant observability platform in the world, but we're starting to appeal to the
more mainstream audience rather than the early adopters and the, you know,
startups that we kind of grew up with. And that's a really exciting change
for us as a company that Tom, Jen, and others will talk more about.
One award that we did get, which is, which is kind of cool, is
recognition from Gartner, where Grafana Labs was named a leader
in the Magic Quadrant for observability platforms from Gartner. Who here listens to what Gartner has to
say in terms of these sort of things? It's okay. Yep. A few people.
That's cool. But, you know, a lot of people consider them pretty
knowledgeable in these things. and, yeah, they know some stuff. But anyway,
cool stuff. Overall, lots of momentum. And obviously some of
you may have also read, we recently did a new fundraise, which, was quite an accomplishment, particularly in the market that we're
in and just as an indicator of the, the momentum and progress that
the company's made. Alright, so I'll just quickly announce
a new program that we're, we're launching startup program and a
lot of companies have similar programs. Obviously we have an open source project, so a lot of startups can obviously
use our open source software for free, and that's by design. But we
did see that there was a gap, for startups who are not
necessarily VC funded, and they're going through periods of
tremendous growth and scaling and, good problem to have, obviously, but it carries financial risk for
these companies. So, you know, particularly for startups
that have limited funds, they're often caught between reinvesting
in their growth versus keeping the lights on. And we think it
doesn't have to be like that. So we're really pleased to announce
the Grafana Lab startup program. And what this program includes is a
hundred thousand dollars of credits to be used within the first 12
months of the partnership. And that includes the whole Grafana
Cloud stack, everything from, you know, our backend telemetry to performance
testing, to profiles to incident response, all the stuff we're
gonna talk about today. And it also includes a 20% discount on
all our services once that 12 months is over, as well as kind of consulting from
Grafana Labs to help startups bring their solutions into the Grafana
ecosystem. So, pretty excited about that. And unlike a lot of other programs, we don't require startups to be
VC backed or US based, right? We're really looking to work
with interesting companies, no matter your funding situation, no
matter your location. So that's my intro. Like I said, we've got a really
interesting keynote for you. We'll try to keep it on
time. And to kick things off, I'd like to welcome our CTO Tom Wilkie
and our Director of Product Jen Villa to, uh, tell you all this cool
stuff that we've been up to. So thank you very much, Tom. Thank you, Raj. Thank
you. Hello, everyone. It's good to be back in New York. I
haven't been here for two years, I think. So, yeah, my name is Tom. Jen
is gonna come up a bit later. We thought we'd not
stand on stage together. So in the keynote we're gonna
talk about three things, right? We're gonna talk about how we're making
our LGTM platform easier for a more mainstream market, for a more mainstream
audience. As Raj talked about. We're gonna talk about AI/ML. No tech keynote in 2024 would
be complete without a mention of AI/ML. And we want to talk about how we
are using it to really scale, you know, your seasoned expertise and bring it
to every engineer in your organization. And finally, we are gonna talk
about root cause analysis, how we're automating some of that and how
we're bringing context to your Grafana stack. So I'm not gonna talk
about all of this, don't worry. I'm gonna focus mostly on the first
bit, and we've got other guests, other speakers for the next two pieces.
So let's talk about easier LGTM. So firstly, what is LGTM, right? Who
here's familiar with that term? Hopefully, if you're at this conference, you are
at least vaguely familiar with LGTM. This is our kind of our observability
platform, right? It means Loki, Grafana, Tempo, and Mimir for logs,
Grafana, traces, and metrics. If you ask some of our sales
team at the back, they'll say, it means let's get the money. If
you ask our product management, they probably think it
means let's get this merged, but we all know it also means,
looks good to me, right? So this LGTM platform's been,
been very popular, very, you know, huge number of users worldwide, huge
volume of data is being stored in it, both in Grafana Cloud and on premise
with the open source software. It really appeals to
these early adopters and, and kind of people who
wanna get their hands dirty, people who wanna learn PromQL,
LogQL, the query languages, people that wanna build
their own dashboards, people that like getting their
hands on technology, right? We grew with this kind of rise of
observability with all of these practitioners, kind of, you know, learning how to build these things and
how to get value out of these tools. But what we found over the past few years
is that we've been appealing more to this broader, more mainstream audience. Who here would think they're an
early adopter of this technology? Who here thinks they're mainstream? Hands up if you're a mainstream audience
for this. Oh, okay, not, not that many. Oh, well, you, you know, might wanna
have a nap for the next few section then. Anyway. So we noticed the audience that
a lot of our events was changing, right? And these people, these are
people who have day jobs, right? These are people who don't have the
time, they don't have the expertise to, to deal with all of this, and they just
want something that works out the box. So about, oh, this was
about three years ago, we started trying to build a more
curated experience in Grafana, right? In Grafana Cloud. We, started first by building lots of
what we call integrations. Not, not very imaginatively named. I will
say. We, when we started this project, we launched the first integration,
which was the Linux integration. So this is a package of curated
dashboards and alerts with the Grafana agent. Now, now using Alloy,
of course, that just works out the box, right? So when you sign
up to Grafana Cloud, you click the button and you just
get something that works, right? We launched with one, it was a little
bit embarrassing just to have one, but we very quickly over the
next year or so, got our, got up to 50 integrations, uh, when last
time we were in New York two years ago, we had 50 of these things. It
was a big milestone for us. I think it was when this
really started to work for us. So today I wanted to kind
of show the, the breadth of, of cloud integrations that we have. We
have over a hundred now. We've been, we've been beavering away. There's at
least 24 of them are new this year, but also we are not just
like launching new ones. 30 of these have been revised and updated
this year. These behind the scenes, these are all open source.
They all live on GitHub. We work with the upstream community to
make sure that they're actually showing the right telemetry and the
right signals for the users. And we get to build very pretty, prettier
slides like this. If you are not, if you're not familiar with
the sort order, it's by color. So one of the other things that I, I quite like about this
project is behind the scenes, we've built a lot of really cool tools
to help maintain the quality and improve the quality of these integrations. So there's a little known project in
our GitHub called the Dashboard Linter, that has like 50 or so really opinionated
rules about what should be on your dashboards and how they should be
presented, and it'll fail. For instance, if you don't have labels on your axes, pet peeve of mine is no one
ever labels their axes. So yeah, all of these integrations
have labels on their axes. These drive about 25% of all
of the volume of telemetry that gets sent to Grafana Cloud. I
just wanna call out a couple in here. The most popular ones is actually
still the Linux integration. The first one we launched three
or four years ago. The, you know, and then the open source stack is really
still the most popular set. So, MySQL, Postgres, things like NGINX, Docker, Istio is also one of
our most popular ones. A logo missing from here is, I
think it's missing, uh, yeah, a logo missing from here is Kubernetes. We started with one of the first
integrations after the Linux. One was the Kubernetes integration. And this was quite a big collection of
dashboards based on a project called the Kubernetes mixin, it had a dashboard for every
single resource type in Kubernetes, and they were all connected together, and you could kind of
navigate between them, but it was a bit of a clunky experience. So we took all of that and we built
a React application embedded in Grafana that's much more seamless,
much more interconnected and richer, allows you to more easily navigate
between all your Kubernetes resources. For instance, one of the workflows that I really like
about the Kubernetes app is that you can find your pod that you're
particularly interested in, you can quickly navigate to the host that
that pod's sitting on and see all the noisy neighbors that are
impacting your pods performance. This is no longer an integration. This is now a fully fledged cloud
application that we've built. We, we launched it a year ago. I just wanted to highlight the difference
between these integrations and these applications. And we've slowly been
extending the Kubernetes app to add, like, cost monitoring to it. For instance, today I want to announce that
we've also taken the AWS, Google, and Azure integrations and turned
those into rich Cloud Provider applications inside, inside Grafana Cloud. These are so much more now than
just a set of dashboards and alerts. This is Grafana scenes,
which is our technology to,
to build these applications, like our Kubernetes app. This is interconnected and a unified
experience that makes it much easier for you to navigate your cloud provider
accounts and figure out what's going on today. This is going GA with support for
all of the three major cloud providers, and it's serverless, if you
know what I mean, right? You don't have to install the agent, you just have to connect your Grafana
cloud account to your cloud provider account and we'll automatically
slurp in all the telemetry. So yeah, if you wanna see this, go and check
out the demo booths downstairs. I think we've got some
demos showing there. So I want to move on from
infrastructure observability. I want to talk a little bit
about synthetic monitoring
and performance testing. Synthetic monitoring is actually one
of the very first kind of opinionated solutions we built for this more
mainstream audience. It actually predates, I think, almost all of our products
at Grafana Labs. It's like a, we launched it eight years ago as
a thing called World Ping, right? And it's one of the easiest ways
to get started with Grafana Cloud. You just put in the name of your
website, the domain of your website, and we will, you know, ping it and check reachability
from 25 locations around the world. It's really useful to know if people
in Asia or Europe where I'm from, can, can actually reach your website,
right? k6, on the other hand, is our performance testing tool. This is really popular around
this time of year, you know, and users use it to check that their
web store is gonna survive the kind of surge of traffic on Black
Friday. Over the past year, we've really seen these two products
as as two ends of a spectrum, right? And we've been unifying them to make it
so that not only can you take all of the power ofk6 and run those in
synthetic monitoring checks, but you can take any test you write
and run them as either, right? This kind of unification should give
you a lot more flexibility to write a synthetic monitor check that runs,
you know, every five minutes from, from 20-30 locations around the world. But then when it comes to that time of
the year when you need to check your website is up, you can actually run it a hundred thousand
times from one data center to make sure your website will
survive Black Friday. But we're not just focused on unifying
the technology behind the scenes and making this possible. We're also focused on making it
easier for you to write these tests. Up until now, the tests for
k6 have been JavaScript tests, and we think that's been a bit of a
barrier to adoption for k6 because not everyone, including myself,
wants to write JavaScript. More of a Golang engineer. Anyway, today our focus is on making it easier
to write tests for k6 and synthetics. We are launching a desktop application. I think this might actually be our
first desktop application we've ever launched. And it allows you to more easily build
these tests using low code, no code and, and a UI, right? One of the reasons we built this as a
desktop application is it can actually intercept the web traffic
from your browser, record the pages that you
are visiting into a test, and then upload that to Grafana Cloud, run it as a synthetic check
or as a load test, right? So it can record these browser sessions
for automatically building these tests. Something we're very excited
about, love you to give it a go. Try it out and see what
you, see, what you think. And that's not the only way we're
making it easier to run tests. We're also making it easier to
get data out of these tests. So as part of synthetics
browser based tests, we are running little headless Chrome
instances and fully loading your webpage, right? So not just checking now
that your website is reachable, we're checking that the page loads,
that all the resources loads, that all the scripts
run properly. You know, we are exposing and recording all of
the web vitals from this page load. We're also exposing the dom from your
website to to a k6 JavaScript test so you can start to introspect it and
check it's loaded properly, right? And these browser-based synthetics has
been one of the biggest requests from our customers on synthetics for a while now. And we're really kind of excited
to announce a private preview. If this is something you're interested in, talk to one of the team at
the ask the experts booth, they'll get you signed up and hopefully
this will be publicly available pretty soon, right? Then lastly, we are not just focused on making
Grafana Cloud easier to use, easier to get started with,
easier to write tests for. We're also focused on making it easier
for you to migrate from other vendors, right? We've got a lot of customers
coming to us saying our bills with, with, you know, some of our, some of
the other vendors are too high, we wanna move to Grafana Cloud. OpenTelemetry is this technology that
promises this kind of vendor neutrality, right? Promises you the ability
to seamlessly, you know, instrument once and migrate
between different, uh, different vendors really
easily. Unfortunately, it doesn't really deliver on that. Not,
not necessarily from day zero, right? A lot of vendors support
receiving OpenTelemetry. We supported receiving
OpenTelemetry for years now, but they don't really let you, you know, instrument with vendor specific frameworks
and then send that telemetry to any vendor you want, right? You have to
use the OpenTelemetry instrumentation. As Raj mentioned at the beginning,
you know, big tent. This, this idea that we prioritize
interoperability is core
to what we do at Grafana Labs, and we think
OpenTelemetry is promise of, of interoperability is brilliant, and we think it's our job to make
sure it delivers on that promise. As part of that, we've built a Datadog Metrics receiver
and upstreamed it to the OpenTelemetry collector. So now if you are
an existing Datadog customer, you can use the Open Telemetry
collector, be it the upstream one, be it Grafana Alloy, our distribution
of the OpenTelemetry collector. You can use it to translate the metrics
from your Datadog agent and from your Datadog instrumentation into OTLP
Open Telemetry line protocol, right? And then from there you can send that
to any Prometheus compatible system, including obviously Grafana Cloud, like we hope some of you will
choose Grafana Cloud for that. But you can also choose to
send it anywhere, right? You can choose to send it to any
vendor that supports Open Telemetry, not just us, right? We really believe that this kind of
rising tide approach will raise all ships. So if you want to hear more, there is
a talk later about instrumentation, about Alloy and Beyla,
where the authors of this, they're in the audience somewhere.
We'll talk about how this is done. Okay, so finally, oh, there's one other
thing that I think is really cool here. You know, this is just part of
the part of the problem, right? So we can migrate the data path so that
quickly, you know, you can send your, your telemetry from, you know, existing instrumentation through the Open
Telemetry collector to Grafana Cloud. But one of the other things we can do
is export the dashboards from Datadog, translate those queries into PromQL,
and import them into Grafana seamlessly. And that's not all. We can take the Datadog monitors where
you might have tens of thousands of monitors written in Datadog, and we can
translate those into Prometheus alerts. And because of the way Prometheus
does alerting does it in kind of multi-dimensional alerting, we can actually dedupe like tens of
thousands of alerts down to a handful, maybe a thousand or so alerts in
Grafana Cloud to make them much more manageable. So there's this really
cool translation tool, um, that, that we have that we can help, uh, help you if you wanna migrate from Datadog
to Grafana Cloud. Okay? So with that, I'm done. For now, I want to introduce Jen who's gonna
talk about some other ease of use improvements. Thank you. Thank you. Welcome. Alright, thanks very much Tom. I'm gonna continue on the topic of how
we're making observability easier for a wider audience to adopt. And to do that, I'm gonna talk about Explore
Metrics and Explore Logs. Some of you may remember we
first announced these back
in April at GrafanaCON. What they are, are experiences that allow you to
navigate data stored in Prometheus or any Prometheus compatible backend like
Mimir, or in the case of Explore Logs, a Loki backend and do it without
having to write a query language, say PromQL or LogQL. And why is this? We'd heard from a lot of users that one
of the biggest challenges to getting started with observability is the fact
that you had to learn a query language before you can actually start to get any
value out of your observability data. So what we did with Explore
Metrics and Explore Logs is that we now have replaced typing queries
with a point and click UI. We've replaced empty start screens
with pre-populated visualizations, making it possible for anyone from day
one to start getting value outta their metrics and logs. Now, since we
announced this back in April, we've seen a ton of enthusiasm
and adoption for both of these. And given that we've spent the last
couple months really listening to early adopter feedback and making a
lot of improvements to both, and that's why today I'm super excited
to announce the fact that both Explore Metrics and Explore Logs are
now generally available for both cloud and in open source. Now we made a number of improvements
in the lead up to GA with Explorer Metrics. We've improved our
related metrics section, making it easier and better
recommendations about what
metrics you should look at based on the one you currently
have open. With Explorer Logs, we added the ability to auto automatically
visualize attributes stored in Loki's structured metadata. This is particularly great for those
of you out there using OpenTelemetry logging. We also tuned our pattern
retention functionality so
that we can quickly surface the most common patterns
in your log lines to you. And we're definitely not
done there. After this GA, we intend to fast follow with a number
of upgrades to both Explore Metrics and Logs. For Explore Metrics, we're
adding support for native histograms, a higher resolution histogram type
relative to classic histograms. We're also gonna be incorporating machine
learning into our related metrics so we can surface metrics that have similar
shapes and patterns to all of your users. With Explore Logs, we're adding streaming support
both to your graphs and to the log lines we show you, which means less
time for you waiting around for results. Now based on the success of both
Explorer Metrics and Explorer Logs, I'm excited to announce that we have
two new additions to the Family: Explorer Traces and Profiles. We've decided to extend the experience
of these two across all the pillars of observability. Both of Explore Traces and Profiles
are available in public preview, again, both in cloud and in open source. Upon completing this
suite of Explore apps, what we can now offer is
a full suite of options. So each user can choose how
it is that they wanna work. This reflects our belief
that observability isn't a
one size fits all solution. For those who are gonna want that
full control and infinite flexibility, they can type out queries in
code mode. And lemme tell you, I have been blown away by the things
I've seen some of the folks on our engineering team do with these
like 50 plus line PromQL queries for those who want something
kind of more in the middle, there's the builder mode. That's sort of what I think of as maybe
like a low code or a visual programming experience. That's gonna be a great way actually
to learn the query languages because it gives you a point and click way to
string together numerous operations. And then for those that just want
push to start, let's get going. We have the Explore apps,
no queries, no code, just easy insights. Whew. Well, it wouldn't be a Grafana Labs
keynote without a live demo, so I'm gonna try to do
this right now. You know, I had wanted to do a video demo
and then Tom told me that was lame,so please cross your fingers for me. I'm about to take you on
a little ride through, Explore Traces one of our
newest additions to the family. Now I'm a product manager, which means I've left the noble
discipline of engineering. But let's pretend for the sake of this
demo that Jen is still an engineer working on an e-commerce platform. If you drop into Explore Traces, let's say I'm just here on the screen
and let's say I've gotten a page that my error budget SLO for my product
catalog service is burning down a bit quicker than we would expect.
Dropping into the main Explore pages, Explore Traces page. You see
your red metrics at the top, your request rate, error
rate, and your duration. Since my page was about errors, I'm
gonna start by selecting errors. Hopefully down here you'll see that
Explorer Traces automatically breaks down that error rate by service name. Since my page was about the
product catalog service, I'll quickly add that to my filters. The next thing you kind of ask yourself
in a classic debugging workflow is what is unique about these requests that are
erroring as compared to the ones that are completing successfully? Luckily, now we have this comparison
tab to help you with that. What the comparison is going to do
is compare a selection. In this case, the selected traces are my
erroring traces to my baseline. So those are the traces representing
requests that are completing successfully. What Explore Traces gonna
do is out of the box, it's gonna look at every single attribute
on my traces and compare the baseline to the selection. It's gonna sort to the top the attributes
that show the largest delta between the baseline and the selection. And what do I see quickly
pushed to the top here? Well, it actually looks like all of my errors
are happening on one particular product ID and clicking inspect,
that's exactly what I can see. This product ID represents
all of the errors. All of the other product IDs
seem to be completing just fine. I can quickly add that
product ID to my filters, and then from there I can actually open
up some erroring traces matching that criteria. Again, speeding along my debugging because I
go to exactly the sort of representative trace that I want. Now, let's pretend while we've been
here dealing with our error, SLO at the same time got a
notification from my support team. It seems like some of my users on my
e-commerce site are complaining that the site's loading pretty slowly for them. Maybe they weren't using the
Synthetics that Tom was talking about. So there, since the page
is about slow loading, what I'm gonna do is look at
my duration signal. Again. The first thing you see is that Explore
Traces is showing you all of your services and breaking
down their P90 latencies. What I can see is that I have several
services with P nineties on the order of seconds. So I wanna now
figure out what again, is going wrong. And so again, I ask myself, what is unique about these high
latency requests versus those that are completing in a reasonable
amount of time? Again, I come over to my trusty comparison tab. This time we can actually use a
selection ability in the Explore Traces app to pick a set of traces. I'm gonna try to select here the
slowest of the slow traces here up top. Then I'm gonna be able to compare
the traces falling in this selection, this orange box to the traces
falling outside of that my baseline. I'm gonna hope that my page actually
loads. All right, there we go, and so again, you see the distinction. We're automatically comparing
across all attributes, the difference between my selection,
my super slow traces and my baseline. Since support said it was
something related to some users, I'll quickly filter down
to user related attributes. And what I can see is, hey, there's a certain set of user IDs that
seem to be in the Slow Traces group and then a certain set
that are in my baseline. I can similarly see if I look at
the user location that certain locations are disproportionately
represented in those slow traces. So that allows me to, again, narrow my search and look at traces
from those particular locations to figure out what's going on. It's also great for me because I
can go back to support and say, Hey, this looks like this probably isn't
an issue for all of our users, but it's just a subset. So with that, I know that was a bit of a whirlwind
tour, uh, of Explore Traces. If you wanna see a longer demo,
please check out our session tomorrow on, let's see if, uh, if I
can get my slides back up. I will tell you what the name of said
session is, but we'll be doing a much, much deeper dive into all
of the Explore apps. I, Alright, I got my next slide. Okay, so that wraps up what we wanted to
talk about with our easier LGTM story. And now, as Tom said, we're gonna talk about the topic that
no 2024 tech keynote would be complete without, which is AI/ML. Now at Grafana, we have spent a lot of time thinking
about what AI/ML means for our industry for observability. And what we've concluded
is that the biggest impact
AI/ML will have in our space is that it's gonna allow all of you, all of your companies to scale
observability expertise across your entire organization. It's as if you're gonna be able to take
that intuition and judgment of your most seasoned observability engineer and
give that to everyone at your company. Let's take for example, what
we've done with Adaptive Metrics at Grafana Labs. When our time
series started running away from us, we used to have to go to our most seasoned
veterans to help us out with that. So we'd take someone like Bryan
Boreham at our company who is an actual Prometheus maintainer with a
title of distinguished engineer, and we'd send him out to go spelunk
and, and find some savings for us. That would probably involve things like
writing PromQL queries to identify high cardinality metrics and high churn labels, writing LogQL queries to
analyze our query logs. It might involve jumping into our code
base to actually manually update our instrumentation. It would involve his knowledge of our
company reaching out to the specific teams who own that instrumentation
and say, "Hey, I'm gonna have to make some changes
here." Now with Adaptive Metrics, what we've done is take that
expertise and actually build it into Grafana Cloud. We've turned human intelligence
into machine intelligence
and scaled it in a way that wasn't possible before. Now, a new joiner in their first week can
review a recommendation to aggregate a metric and start saving your company
thousands of dollars and do it with the confidence that the engineer
next to them is not gonna shout at them because they just made some alert
go haywire or broke a dashboard. We've been extremely impressed with the
success of Adaptive Metrics to date, both in terms of adoption and
in terms of total savings. And we've continued to
invest. In particular, we're investing more and more
in our recommendation service, making it more sophisticated so it
can identify more savings and making it more real time so it can react
more quickly to changes in your company's usage patterns. Building on that success, we talked
last year about adaptive logs, which we announced in research and now
I'm excited to say that we're ready to promote adaptive logs
to general availability. I'm extremely excited and hats off to
our team that developed this with the speed at which we were able to take
adaptive logs from inception to ga, having the time it took us to
do this for Adaptive Metrics. Now, Adaptive Logs is built on the same
philosophy as Adaptive Metrics where we analyze your incoming data and we
compare it to your usage patterns to make a scent of tailored
recommendations for you. However, because metrics and logs are
slightly different telemetry signals, what's happening under the hood is
slightly different. With Adaptive Logs, what we're doing is using an ML
algorithm known as drain to extract the most common patterns from
your incoming log lines. Then we analyze all the queries
happening in your system and we count the number of times in the
query results that we return to your queries. A certain pattern shows up. That allows us to then make a customized
recommendation to you of how much we should keep versus sample
each particular pattern. With the philosophy that for patterns
where we see log lines matching that pattern being returned very frequently, we wanna mostly hold onto those patterns. If on the other hand you have a pattern
that is almost never returned in a query result, we're gonna recommend
sampling most of that away. Now using this kind of approach,
we've actually seen our customers, our early adopters and even ourselves, decrease their total ingested log
volume by anywhere from 40 to 60%. And that's pretty impressive, because what we can say now is that
it's actually using this becoming more cost effective to use Grafana
Cloud Logs than it is to run open source Loki yourself. As
with Adaptive Metrics, the savings that we're able to realize
here used to be the sort of savings that you can only get if you had some sort
of seasoned observability engineer on your team. Now again, we've built that directly into our
product so that any engineer from day one can help you realize
that kind of savings. Now, the grand vision that we're working
towards is what we've taken to calling Adaptive Telemetry. This is a world in which we pruned
away all the noise and just retain the signal, extracting it from
that fire hose of observability. We know everyone's systems
are generating in so doing, we're ensuring that every byte of data
that you store is worth what you're paying for it. This vision is only possible
via the use of AI and ML because without this, there's no way we would able to do the
kind of analysis of your incoming data and your query patterns at the scale
and as real time as it needs to be for this to work. And if you
can't do that kind of analysis, there's no way you can provide intelligent
recommendations about what to drop versus what to keep. Now, for those of you wishing that
those research tags up there under Adaptive Traces and Adaptive
Profiles actually said GA, I do have some good news for you. We're
excited to announce that Sean Porter, the founder of startups TailCtrl and
Sensu has joined Grafana Labs. TailCtrl's mission, which was to make every
trace stored worthy of attention, aligns extremely well with our
own vision for Adaptive Traces. And we've been really impressed with what
TailCtrl was already doing to develop intelligent sampling policies for
traces that evolve in real time based on changes in your own systems.
With Sean's leadership, we're excited, we know it'll supercharge our development
of Adaptive Traces after which we'll be on to tackle Adaptive Profiles. If you wanna learn more about
Adaptive Telemetry in general, please make sure to join my talk tomorrow
that I'll be giving with one of our engineers, Edward, where we'll dive even further into
some of the AI/ML capabilities in Grafana Cloud. And with that, I'm happy to bring Tom back up on stage
to keep adding to the AI/ML conversation this time with some updates
on LLM observability. Thank you, Jen. Thank
you. Welcome. Alright, me again. Yeah, so as Jen kind
of spoiled with her introduction, thank you , we want to talk a
little bit about LLM observability. We've been working on a series of
technologies here to make it easier to understand the training and operation
of large language models, right? Unlike things like infrastructure where
the USE method is a really common kind of monitoring pattern or microservices
where the RED method is something you might use. LLMs have a series of
unique challenges and you know, when it comes to instrumenting and
understanding the behavior, you know, this is a really developing field. So we are doing all of this
in open source on our GitHub. We really want to hear from people using
these tools we've developed and tell us, you know, where they help, where
they don't help. And, you know, we're looking for a community kind
of collaboration here. So firstly, I want to talk about a project. There we go. I want to talk
about how we're using Beyla, which is our eBPF-based auto
instrumentation library to automatically instrument CUDA calls.
So CUDA is a common library used. I'm not a AI ML expert. I don't really know much about
this kind of thing to be honest, but we are doing this so that AI
developers can quickly get insights into their models as they're running
and as they're being trained, right? We've added these probes to
intercept these API calls, it's, they're in a branch on Beyla.
It's all in open source in GitHub, and that generates a series
of Prometheus metrics. We are working on extending this to also
do kind of profiling of these models as well, and we really just wanna see where
the, where the community is interested. So if this is something you're
interested in, like again, ask the expert booth
can give you more info, point you to the right place on
GitHub. The second project we, we've been working together
on is an OpenLit integration. So OpenLit is an open source framework
for monitoring the infra, the inference, like the running of these models, right? It's open telemetry native and helps
you kind of gain insights into the performance of these
applications in production. We've built an open source cloud
integration, right? So this is again, a package of curated dashboards and
alerts and makes it really easy to get started with OpenLit on your open
source Grafana or on Grafana Cloud. It's all sitting up on GitHub. Again,
link will be at the ask the experts booth. The third project, though is
the one I'm most excited about, but I'm not gonna talk about that.
As I said, I'm not the expert here. We've got, a Grafana Cloud customer, Aaron from Nvidia to come and talk
about it. Please welcome Aaron on stage. Thank you, Aaron. Oh yeah, that's me. Hi.
Good to see everybody. So one of the things we're
really excited about, and we're really happy to
be a Grafana customers, and this is really critical for
what we're trying to accomplish, is actually being able to understand
the telemetry for how training is going. So imagine you're trying to build a
foundation model or trying to do a massive tune of model. Actually understanding
is the model converging? Is the training progressing along with
the low level telemetry to understand are, you know, are our GPUs OK or
is the heat OK? Everything else? It's critical to be able to understand, am I making a good investment
in these training runs? Sometimes these training runs can run
for weeks or months, and if it fails, that's a lot of resources that you've
given up for no particularly good reason. It is really important to have this
and we're really thrilled to be design partners to help them build this out so
we can achieve what we need to achieve as well as any other customer that needs
to run training jobs and GPUs as well. So we're super excited about that. I'm gonna talk today though about a
little story, a very brief story about what my life was like back in the
day when I was a VP of engineering for an observability company. Now imagine you wake
up every day at 6 a.m. And you're responsible for helping
your CEO understand by say, 8 a.m., what happened last night? What
happened the night before? What I would often have to do, read the
back, scroll in Slack, read everything, call a bunch of directors,
call a bunch of ICs, call the people that were
handling the incident, ask things like what customers were
impacted, what regions were impacted, what was the possible root causes, so we can actually start to write the
incident report so we can inform our customers what's happening. This was during a move to the cloud
every day of my life for six months while we were resolving this
problem. It was not a fun time. And one thing I realized
once we had LLMs is we know LLMs hallucinate sometimes, right?
So everybody had an LLM hallucinate? Who amongst us, who's ever resolved an incident and had
a senior leader ask that morning what happened, who here is also not
hallucinated as to what happened? It's all happened to all of us.
And if you don't believe it, ask your developers, it,
it happens all the time. And it's really something that
inspired me. Once I realized that, wait a second, with this
new technology with GPT-4, I can take a question in
human and translate that to a question in any number of query
languages, including things like PromQL, including everything that we would use
with Grafana to understand what happened last night. For me to be
able to, as an engineer, initially get some idea initially, then start to ask some more questions
and really come up with at least a plausible cause of what happened and
dive into issues so I can get better answers. And again, it may not be
perfect, but neither are the humans. So as we started to think
about this idea more at NVIDIA, we really got excited about
this system we're building, which starts with something
called retrieval agents. These are based on NVIDIA NIM technology, what's called NVIDIA
Inference Microservices. And they call up all the data sources, including all of our Grafana data sources
that are required to be able to answer these questions. They answer questions from analyst agents
that are trained on things like how to H100s, how do GB2-00s run? How do all the different
components run in the data center? These are asked oriented by
orchestrator agents or things that we put in what's called the OODA
loop: observe, orient, do, act. And these things actually try to
ask those questions to the analysts, figure out what went wrong, and then invoke actions and tasks to be
able to bring a JIRA ticket up or call PagerDuty, or whatnot. And we think this agent flywheel of not
just being able to do this in a cycle, but having more and more agents added to
the system allows us to solve many more problems. We've built
something, we call it Lollipop, it's kind of a cheesy name, large
language model for observability. And what this is allowing us
to do is ask questions like, give the graph of Slurm job failures. Give me the five best possible
causes of what wrong last night. Give me something about
what were the, you know, clusters that need maintenance over
time - all these different kinds of questions, anything about the data
center, we can talk to the data center, early days, and start to get answers from that because
it's multiple LLMS trained on various areas of expertise. It's really, really incredible concept that
we are really excited about. So amongst those things, we have conviction that this will be
a model that a lot of people will use. But most importantly, this stuff does not work if you
do not ground it in ground truth. If you do not understand that the
query that you're coming back with, what the LLM might generate is actually
has something in a Grafana dashboard or some kind of technology that allows you
to understand exactly what happened. OK? Because LLMS are not perfect.
They do hallucinate sometimes. And so we want to be able to use
this to build dashboards over time, to be able to ask a question, get a
dashboard link, ask another question, get another dashboard link, and start to really understand more
dynamically what is happening in our data centers across the world, across
any number of cloud providers, across every continent on
earth where we have GPUs. This is what we're really excited about. We can't wait to see what we build with
Grafana to be able to enable all this kind of stuff. That is really, I, I never thought I'd be able
to see this in my career, and I'm really happy we
get to do it. Thank you. Thank you, Arron. That's Brilliant.
Thank you. Thank you, Aaron. Right then last time I'm on, I promise, I want to talk about one more thing.
No, no keynote would be complete. I try and slip one of these in
every time. Raj normally stops me. I'm surprised he didn't this time, but
yeah, I wan to talk about one more thing. And that's how we actually build
products Grafana Labs, right? We have, we have a pretty unique
engineering culture. I think, we, we give a lot of freedom and a lot of
autonomy to the engineers at the company, right? And part of the part of
the culture here is that we, we do these quarterly hackathons, right? So we give them a week of each quarter
to do whatever they want, like, and it's very much whatever they want. Some teams use it to improve their
internal tooling or just catch up on some backlog. Some teams go off and do
completely greenfield projects. A lot of the, a lot of the things we've presented to
you so far started life as a hackathon project. The Explore apps were a
hackathon project, right, for instance. And I want to show you a sneak peek
into the winner of the hackathon. That was about five weeks ago, right? And we're working to get
this into the product. We're looking again for customers and
users to kind of work with us on this. But I want to talk about something
called Incident Rooms, right? The winning hackathon
project from last year. It's a really good use case in exciting
new case of AI/ML .I'm actually not gonna talk about it. I'm, I'm just gonna show you the part of the
hackathon process is we have every team record a five minute video, and then
we judge those videos. Everyone, you know, we all get together, we
judge those videos, and then the, the short list gets shown at a company
all-hands where the whole company votes for the winner. We're not gonna
show you the whole five minutes, we've edited it down to about two
minutes. So I'm just, should we, should we run the video? I'm the bot and today we are thrilled
to introduce you to a revolutionary addition to our incident
management tool, Incident. We call it Incident Rooms. Incident response teams often
face a common challenge: staying focused on resolving issues
while keeping accurate records. During the intensity of an incident, it's easy to forget to
document crucial details. Let's step into a day in the life of our
incident response team before incident rooms. So the problem is that the coffee
machine is out of memory again. Why is our coffee machine
equipped with memory? It stores profiles for
different coffee types. I'm following the runbook and
checked water, beans, and power. Have you tried power cycling it? Power cycling. Oh, that's a
good idea. Gimme a sec. Yeah, looks like power cycling helped. I think that resolves
the incident then, right? I think so. Can someone mark
the incident as resolved? Looks like the coffee is brewing again.
Everyone's gonna be happy, including me. Thanks everyone. Great work team. I'll document the steps taken their
expertise leads to a swift resolution. Notice their intense focus on
the problem, but also note, notes and logs are sometimes missed
in the process. With no notes or logs, hey resort to using an AI to
help when there is no context. The AI hallucinates, generating a
report filled with inaccuracies. Now let's reimagine this
scenario with incident Rooms. Incident Rooms is a built-in feature
within Incident enhanced by a helpful LLM bot. Now our team enters an incident room
with the bot seamlessly integrated into their workflow. While the team
focuses on resolving the issue, the bot keeps track of
their conversations, notes, key points and response to voice commands, allowing them to stay fully
engaged in problem solving. But the bot isn't just a note taker.
He's learned a few new tricks too. From executing Grafana incident actions
on your behalf to delivering instant ad hoc summaries via the Grafana
Incident Slack assistant, the bot makes managing incidents
smoother and more efficient. Throughout the process, stakeholders can interact with the bot
for real time updates on the incident's status. This ensures that everyone is
informed and up to date effortlessly. With the bot by your side, syncing
incident statuses, providing updates, or running actions across different
media channels has never been easier or faster. We are excited to see how Incident
Rooms can revolutionize your incident response workflow. So yeah, we are, we're super
excited about getting that in, in the hands of our users. We're
starting to use it internally and, not having to take notes during an
incident bridge is just like amazing. So I'm, I'm now officially done for the
day. I'm going to introduce you to our, our last speaker Manoj. Um, thank you
very much for having me. Welcome Manoj. Hey. Okay, so I'm in the overtime, and you all just saved the
best for the last, right? Excited to be back in New York City, the city I called home
for about three years and, me and my wife totally enjoyed our
time here. When we started having, we started to have kids, we
moved to suburban Bay Area, but once we ship them to college
here, we plan to go back to the city, come back to Rod City. So,
let me tell you about like, how I joined Grafana here. So I started Grafana just about a year
ago through an acquisition call Asserts, some of you may have heard of it,
or from the last year's ObsCON. Now, so the founding idea of Asserts, you know, so I've been kind of building this
monitoring products APM products for my li felong, for about 20-plus years. So the founding idea of Asserts
was very simple. Literally as, Jen was talking about Bryan Boreham. So there are only few Bryan Borehams
in the world, you know, so I, we cannot really, and how do I make Bryan's intuition
go into every engineer's head in my, in my org, right? So
that was the main idea. So like, what if there was an expert system
that really understood what our telemetry data looks like,
and continuously analyzing
it, and finding all those, you know, tidbits of information that
automatically makes troubleshooting super easy. So, you know, like troubleshooting is something that
we do every day. We get excited about it, you know, we go on rabbit
holes, but, you know, if you don't have the
intuition of an engineer, like a distinguished engineer like Bryan,
you could be, you know, going in like, in all the different directions because
you have quite a few dashboards. And I've met organizations who have
like thousands, you know, like 20,000, maybe a hundred thousand dashboards. And these days we can't even generate
dashboards, right? We can just write, I don't know, maybe LMS can't even
start creating dashboards now. So, but the dashboards are pretty good.
I don't know which one to go to. That's kind of a big problem, right?
And again, each of the metric, you know, every metric, every traces
and logs that I'm generating, there is no consistency in labeling the
data. I mean, in the world of AI/ML, we called this thing labeling the data.
I mean, so that's kind of a big problem. There's no consistency in
labeling. And then, you know, I used to work at a company called,
actually Citibank right here, was responsible for trading platform,
but I joined a different company. I mean, the architecture is completely
different. You know, the trading platform looks very
different. So, and now imagine, how do I transcribe this knowledge
to every engineer in the org? So, let me share with you like how we are
approaching this problem in Grafana Cloud. Now, so we don't ask you to
install any new agents. You know, we got LGTM easier, pretty cool stuff.
We got all the integrations catalog, or you can bring your own
metrics. You know, you, you are running your own
Prometheus exporter right now, so bring it on to Grafana Cloud.
And once you send the data to cloud, so we have this thing we are
calling Asserts inference engine. The idea is very simple, right? You know,
I wanna have the intuition of Bryan, the inference thing that Bryan
does in his head into the product. So what if this engine actually
understood all the labels, all the data coming to the cloud
and automatically catalog them, and then start walking
the topology, you know, like imagine the topology of the data,
analyze it and present it to you, this beautiful, cool, what are you calling this RCA workbench
that brings all the data together so you can do troubleshooting like Bryan. OK? Now my next demo is dedicated to Bryan. Okay, let's get us started.
I'm gonna switch from, OK, so let's get started.
Now, we know about alerts. We love our alerts, symptom-based
alerts. We all know about it. I mean, we call them SLOs, but how do
you make SLOs easy? You know, I go and talk to engineering leaders,
you know, I don't know, like, man, how do I know which one I should find?
I mean, how do you even create SLO? How do I know I should be
creating SLO on this or not? So the first thing we did is like,
you know, integrate the whole SLO, improve the whole SLO experience
in Grafana Cloud. So if you are, let's say I'm running a web
app, I'm just gonna type - just refresh my screen here. My laptop is kind of been
slipping - so I just pick up my, I have a frontend service and I pick
up the service name. I said, OK, I wanna create an SLO for this.
You know, I just a new guy. I know there's a frontend app there. I'll pick the app name and I'll
create a SLO for that, right? So now I've already done that here. So if I go back to my SLO screen here, Now what's happened is
like, once you create SLO, the beauty of what we did is that we are,
as the telemetry is getting ingested, we automatically tagging those metrics. The system knows that what's the
request metric? What's the error metric? What's the duration metric? What
are the CPU and disk metrics? It's adding the lead, adding, tagging those metrics as it is coming
to the Grafana Cloud. So it's automatic. You don't wanna do the work,I mean,
if you already have a custom metrics, just bring it on, right? We'll show
you how to do that yourself. Um, but in this case, the frontend data coming from our
Faro agent is, is already labeled. So if you're using open source Faro agent, send it on and we will label
it and have it that all to you. So I have this SLO created, pretty
simple, right? You know, right, or total request total, look at the ratio
and tell me if something went wrong. I mean, it cannot be easier than this. So now I have an alert that fired, I mean, I'm kinda simulating some error here. It fired yesterday while
I was in New York City, and it was a nice little link here calls,
and I'll take me to the RCA workbench, right? So like, I just click on it. Now what happened here is that
every time you create an SLO or an alert, it'll
automatically link you back. It'll look at the service
label or the job label, and automatically take you
to the connected services. So it's kind of scanning the
system and quickly figured out, OK, the frontend app is connected
to all the services, and I'm gonna pull all those things
and show you all the potential causes, you know, the troubleshooting
gates. And in this case, you know, we call them assertions or checks. So there is a quick graph here if you
wanna get curious and take a look at this thing and quickly understand what part
of the architecture is in trouble. So, and here I have this thing called
frontend proxy that is sending all the requests to frontend
service, and it's, it's, looks like it's ranked to the very
top here. So it's like, you know, higher score, you know, we have a scoring this based on what
they call as like assertion score. They get time and space analysis. So
it's, it's pulled to the very top. So that's interesting. Now, I wanna,
I'm really curious, OK, this alert fire, where are my end users
affected? You know, like in, we always care for like Tom talked about
Synthetic, I mean, I love Synthetic, it's cool, but there's real fun and
real user monitoring, right? You know, like Synthetic will not catch real user
monitoring. So I'm gonna ask the system, "Hey dude, can you tell me
if any users were affected? So I'm gonna click on this button called
"Find me problematic connections." So every time you ask this
question to Asserts, what it does, it again walks the graph, right? It'll walk the graph and pull in all the
relevant information. So in this case, it has now pulled in the
frontend client at the very top, like right to the very top. And I'm gonna quickly launch the
look at the summary view here. Oh, looks like all those different
endpoints, the product endpoint, the card endpoint, are having
a massive amount of errors. So, I can quickly jump into the frontend
observability, right? So we have a fully React app that is built for
frontend data only, right? So Grafana already has for Kubernetes,
for Application Observability, for OpenTelemetry, for your browser
data. Everything is kind of built in, but now it is taking you
to that part of the app. And quickly you can start browsing and
launch Frontend Observability and get into more details at our logs and
at our sessions and everything else. I'll not do that. I'll save that
for our upcoming session. Now, let's come back to the app, right? So,
OK, this is all based on the score, but what if I can all know like
what order the sequence of things happened? So I'm gonna quickly start
by time, right? So time and space, the two dimensions, our brain is trying to weave this
information and transcribe into a root cause analysis, right? So
here, um, so when I switched to time, I can see there is a feature flag
service that was triggered on. So somebody decided to turn a
feature flag, like, you know, we are modern development-conscious
releasing features and turning them on in production, right? You know, so,
so when the feature was turned on, right? Then there, the frontend
client having a lot of errors, and this catalog service seems
to be the biggest troublemaker. So now, so if I take a quick look here, it's having pod crash looping
and application errors. So I wanna jump into like the
relevant, again, dashboards, right? So I wanna look at my
Kubernetes Monitoring data. I wanna look at my OpenTelemetry data,
all the data, Application Observability, Kubernetes Monitoring, everything
is already part of Grafana Cloud. It's already there. So we weaved this intelligence into
all the Grafana Cloud products. It was like, it took a
village to build this product. Grafana Labs is very unique. So it's
like a hundred startups in a startup, so, and Tom like said, right? Um, we kind of let the engineers do whatever
they want, you know, in some funny way. But then once in a while Tom will
come around and say, "You know what? This is actually something that we should
do together." And then he will put in this OKR, right? I mean, you guys write
OKRs, but once in a while he'll do that. He'll say, I have this, unique
ability to do this only, but I only can do twice in a year,
and that's it, right? And he decided, this tech looks pretty
cool, Manoj, let's do it. So you kind of put it as an OKR.
So we kind of came together, "Avengers assemble," And we built
it, right? I'm excited to, you know, share today and quickly
going back to slides now. So everything I showed you is, now available to all the
Grafana Cloud Pro customers, in, we already started rolling
around production, right? It's already happening right now as
I speak, but, and by October 2nd, I think that's the date,
everybody will have it, right? Everybody will have access to it. So
you guys can launch it, play with it, you know, start asserting on
your data. Now, this is all fun, but you know, again, we, while we
are building this product, right, we needed some really solid design
partners to come and work with us, right? You know, and who could, I
mean, actually give me early feedback. So now this is, this is where I
wanna bring in my good friend Olin. He runs this magical
system called Aladdin. Tell me about Alladin. Yeah. so thanks for having
me up, Manoj, first of all, great to be here for ObservabilityCON. So before I pick on you a little
bit about getting beers, we can, we can talk about Aladdin. So, I am part of BlackRock and one of our
most important platforms is Aladdin. And Aladdin is an operating
system for investment managers. And it brings together the
data, the technology platform, and the people to manage money in
real time. And my team, in particular, the observability team, is very focused on all the signals
that have come up in today's talks, right? Your logs, your
traces, especially your metrics, and making those available both from a
tooling perspective and from a user experience perspective to enable our
teams to resolve issues faster, right? So that's the purpose of what
we're doing in observability. Now, to get back to the Asserts conversation, when we were at ObsCON in London last
year, Manoj was like the new guy, right? He was brand new and we're getting beers. And I kind of cornered you
because I was really interested in the Asserts platform, the Asserts product.
And I think what is super cool about, first of all, how cool was
that demo? Wait, well done. But specifically I was very excited because we have our biggest core partnerships
with teams like SRE within our organization, and they are asking for more
and more insights from the existing investment that we've made
in things like metrics, logs, traces. And this platform is about
extracting more information, more connectivity, more value with
things like a service graph, right? All those different things
connected, a workbench. These were precisely the things that
our SREs are beating down the door for us to do. And I think we've been, we've been talking about that in
our partnership as telemetry in practice. How do we use these things? And Asserts is kind of like pushing us
more towards driving those actions and ultimately resolving the
issues we see in the infra. So that was the excitement
that that got us started. Thank you. So, when I first went
to Olin in London last year, so I told Olin, OK, you guys are the biggest asset
management company in the world. I'm sure you have a lot of money
you can afford any tools, you know, it's not like you had to use
Grafana, right? So, but then, what is it that excited you most? And
then Olin started telling me, Manoj, which we have put a lot of effort in
instrumenting our app. Like, you know, we have great engineers. The system
has been there for like rock solid, it's the foundation of our
product, of our platform, and we don't throw away all
this investments, you know, and I read a blog and I saw a thing. So that kind of got me really
excited because as an engineer, and now we not only want to
use this outta the box metrics, we wanna actually instrument our code,
right? You know, monitoring as a code. Like, it's something that
we all believe in. So, so all it tell us like how it's
been your journey, you know, coming and onboarding Asserts. 100 Percent. Like we
started with, you know, open source Prometheus and metrics
has been a core part of the culture, and observability internally. But as we've made the transition and we've
grown that estate and we've built and built and built with with
Grafana, what we realized is, you know, the curse is going
back and re instrumenting, right? If you have to go back into your code
base and redo the things you've done, that is the worst possible outcome.
And what was super exciting, even in London a year ago, especially
now, with what you're seeing here, is that Asserts can be driven from the
metrics that you already have, right? And I think that element of being able
to always be after more leverage and more value from the existing estate that we've
built was the reason that we wanted to get super involved. And frankly,
the partnership has been great. You stop by the office, we've
been working together, the teams, like these things are, we're seeing the evolution of Asserts
as a product that can make more and more leverage from those existing
investments we've made. And that's the thing that has kept us
really excited and we continue to be excited, you know, seeing the kind of
stuff you're seeing on stage today. So, like I was in BlackRock
office yesterday and it's
got this beautiful view of Hudson Yards, and, uh, so Olin,
and the team was in the room. And we are starting to talk
about like, what's next. You know how exactly you wanna
take it to your entire group. Yeah, a hundred percent. I would, I would
say, biggest plug I can, I can make, if this demo was interesting, if hearing about the stuff we're
doing with Asserts is interesting. There is a session at 3:30 today with
Baljeet that's on my observability team and with Goutham from Grafana.
You gotta see this, like, you gotta go to that session and see
all the stuff that we're doing there. So my biggest shout out, you wanna
know more, go to the experts. But just in summary, like, I think our
partnership continuing to see Asserts cover more and more. And, importantly, it's that concept of telemetry and
practice and workflow and the idea that we need the tools in the hands of
our operators and engineers. And frankly, I was talking today with one of our
team members here from BlackRock, and people have looked at this tool and
the experience is so there's intuition, there's value, there's
linkage of all these systems. That's what we need in the
hands of more and more people. So our vision is get this,
existing dataset, you know, bring it into this Asserts environment
and ultimately hand it off to our key operators. And we're getting the same thing that
probably everybody in the room is looking for, you know, reducing MTTR, you know, getting after incidents faster and
basically being able to power, you know, a healthier Aladdin platform. Thank you. Thank you all. Thank
you. Thanks for joining us. So if you like everything you saw there, come and meet us as the
ask the expert booth, come to the session that's
coming in the afternoon. And now I'm excited to bring back
Raj on the stage to take us home. Cool. Thanks, Manoj, Olin, Tom,
Jen and Aaron - great keynote. We're over time as I was worried about,
we're running about 10 minutes behind. I was supposed to do a quick recap.
I'm gonna just buzz through that, but in the meantime, I'm gonna invite the presenters
to come up for a a few questions, because we definitely wanted
to do that. So my recap is, we talked about a lot of stuff today,
obviously around three key areas: making our stack easier to
use as we go more mainstream, using AI and ML to help both save
you money with Adaptive Telemetry, as well as help you troubleshoot better. And I hope you're excited about some of
the announcements that we were making this year at ObservabilityCON.
I know I am. So, I think we have just a few
minutes for Q&A. Like I said, we're running a bit over, and Mat's
gonna run through that with us. Yes, absolutely. Okay, so the
first question is, Anonymous asks, what are the most common failure modes
when building a new observability stack and how can I avoid them? I've only done it once. . I don't think I've got enough of a pattern
to know what the failure modes are. You got it right though, didn't you? I dunno, you tell me. Like, I think one of the things
we did differently with
LGTM was instead of putting all of the you know,
logs, metrics, traces, profiles into one service, we put
them into separate services, right? And that was very different to the
established kind of observability stacks, like Elastic and so on, right? And we
did that like intentionally, right? We did that because we wanted, you know, to be able to change things for how we
did logs and not have to figure out how to do that for metrics, right? So we wanted to be able to innovate in
each individual project, and, you know, get them to learn from
each other and honestly, like to get the teams kind of separated
so that we could scale them more quickly and they could be more productive.
I know some people would, sorry, did you want... I was gonna say, but what about if, if people are building their own
stack to observe their own stuff? Well, I was, I was gonna get to that. But a bit quicker, please. Yeah, I know. I would
say like, in hindsight, like one of the criticisms of the LGTM
stack is I've got four things to install or five things to install with Pyroscope,
right? So, yeah, like, you know, trying to find a balance,
there is difficulty, but if you are using the LGTM stack to
build your own kind of observability solutions internally, I guess I would say, like you can try and roll it all
yourself and you need a certain level of expertise there, right? But
leverage what's out there, leverage the mixins that are all
open source, right? Use, you know, all of the projects out there and, and
learn how to assemble them together. Yeah, I dunno. Yeah. And a few people ask
this same question as well. It seems like Grafana Cloud is
where most innovation is happening. Will this trend continue going forward? I'll get a shot of that. So,
you know, I'd say most of the, most of the work we do from an engineering
perspective at Grafana Labs is still open source, right? That's
where the majority of, sort of, if however you wanna measure it by -
by headcount, by lines of code, by, you know, just team effort.
But we're definitely focused, in terms of Grafana Cloud, we believe
is the best way to consume all the, you know, innovation that we're
delivering in a really seamless, easy-to-use manner, right? So ObservabilityCON's definitely focus
more on Grafana Cloud at this point. From a revenue perspective, Grafana cloud accounts for more
revenue than our on-prem solutions. But we're still actively, you know,
selling, supporting our on-prem solutions. We wanna meet our
customers where they are. The fact that we can offer both on-prem
and cloud or a hybrid deployment is a advantage for Grafana as a company.
But I think it's a fair, you know, fair observation that, you know, we consider the future of where
we're going to be, our cloud product, and quite frankly, we need to prioritize,
you know, balancing that innovation. So I'd say that we're still putting
most of our innovation in open source, and that's just a fact that
you can, you know, look at our, go look at our GitHub, go look at our innovation cadence on
open source projects like Grafana, Loki, k6, and others. But from
a product standpoint, we're definitely quite
focused on Grafana Cloud. I'd also, do you mind if I... Please. Yeah. Take take as
long as you like . Thank you, Mat. So I'll also add that
like, there's a chicken and egg here, right? Like cause and effect. The reason a lot of innovation
is in Grafana Cloud is
because it's significantly easier for us to deliver value there,
right? Because we are running it, you know, we don't have to
figure out how to package it up, how to document the
operations side of things, how to figure out how
to integrate it, right? We can make a huge number of
assumptions that you have metrics, logs, and traces stored in known
locations, right? In Grafana Cloud, like if we tried to deliver, you know, there was a diagram that Jen had about
Adaptive Metrics and how many individual components are involved in
delivering that end-to-end feature. If we tried to package that up and
deliver it, you know, on premise, it would be really challenging. It would slow us down and would slow down
the pace of innovation at the company. So I would turn it around to say, like, the reason we are able to release so
much stuff so quickly is because we do it in cloud, where it's
easier for us to do that.

