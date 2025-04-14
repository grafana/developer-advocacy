# New Ways to Unlock Faster Insights: Metrics, Logs, Traces &amp; Profiles | Demo | ObservabilityCON

Galen and Ryan from Grafana Labs dive into practical strategies for accelerating insights from your observability data — including ...

Published on 2025-04-08T05:56:29Z

URL: https://www.youtube.com/watch?v=jVWaGjgNKWY

Transcript: Howdy everybody. How's everyone doing? Great. Good. Everyone happy to be in
Chicago? Yeah. All right, well somebody is. Alright,
cool. Well I'm Galen. I'm an engineer on the log squad and
I'm going to get us started on this talk which shows you how to get faster
insights from your metrics, logs, traces and profiles. I almost
said next slide, sorry. Alright, but before we, you guys have
been through this a few times, it's 18,001 now. If
you have any questions, you know what to do. So yeah, it feels
good to be here. It's a beautiful city. It's lovely weather for me
at least from Minneapolis. So I hope you plan some extra time to explore
the city because there's a lot to see and do. So this map shows a couple
of things to do in the area, but let's talk about what's
really important - pizza. So where do I find the
best pizza in Chicago? So there's endless options and
if you're non-native like me, you've got two ways to find the best pizza
in the city. Option A, find a friend, someone who knows what's up, ask them
where to go for the best spot. In my case, my friend Michelangelo, who is a pizza expert but is
also a bit opinionated as only a Chicagoan can be pointed
me to the right place. So I put it in Google Maps and boom,
I'm there - 10 minutes. Option B, you go full tourist, you use
Google Maps, you search around, maybe you find the right thing. You filter through all the options until
you narrow down something that finds what you're looking for. So the difference between these two
methods is like the shift we're making in Grafana's user experience and is what
we're going to be talking about today. Option A, asking the expert, it's kind of like our
traditional query-based system.
If you're an expert it's precise and useful, but option
B, exploring with filters. You don't need to be an
expert or a query wizard. You can start with a broad search like
pizza and refine your options as you go. And that's where our
new explore apps come in. They make exploring your data as
easy as searching for the best pizza, guiding you step-by-step to the
solution. No expert knowledge required. Introducing the queryless Drilldown Suite. So as we go through this talk today, we're going to highlight all the ways
that we have improved the experience so that you're no longer required to be
an expert in LogQL, PromQL, et cetera, and instead make logs, metrics, traces and profiling data accessible
and actionable for everyone across the board. So let's get a little
hands-on. Metrics Drilldown. So it's almost Black Friday. You and your team are getting ready for
the big day hoping that your system can handle all the customers. Things seem
to be going good. So you go to bed, but beep, beep, beep. Two in
the morning, you get pinged, your customers are seeing slow response
times, webpages are timing out, your team is freaking out. So you jump into Grafana to hunt for
some indication of what's going on. In general, you can narrow things down, but it takes time and understanding of
the relations between your services. Which is pretty hard
at two in the morning, you know that there's slow response times, so you look for metrics that could be
related to HTTP requests. You query it, find the problem, so you find another metric and you
repeat this cycle until you finally find something that shows a spike, a gap or some anomaly that
indicates what's going on, but there might be other
problems, CPU usage or memory. So you have to continue this process over
and over again until you finally have an idea of which service is misbehaving.
And let's not even talk about how many hours it took you and your team Googling
errors trying to figure out how PromQL works in the first place. So
now with Metrics Drilldown, you're able to quickly visualize telemetry
from a Prometheus data source without writing any queries. You can dig
into each metric effortlessly, click on metrics and related services
and organize metrics by namespace. Now it's much easier, quicker for you and your team to perform
an investigation leading to faster time to first insight or in the case that
alert fired in the middle of the night M-T-B-T-B, meantime back to bed. So now we're going to be joined virtually
by Catherine from the Metrics Squad to show you how this all
works. Let's dive into the. Functionality of explore Metrics
somewhere. So as you can see, when you land on explore metrics,
there's a list of metric graphs here. You can hover into one of
them to show the metric description as well as the type. You can also search and filter
for metrics. For example, if you knew it was coming in from a
Kubernetes or if it was coming in from a container, you can filter by that or
you can search for metrics as well. So in this case, I know that my
customers are seeing slow response times. I think this might be
related to a request metric, so I would search that and I know this
has been happening in the last 12 hours, so I could filter for that as well. Now I'm seeing that there is a
spike showing on this metric here. So I'm going to go into
it and I'm going to go into this breakdown tab, which shows a list of all of the
labels and I'm thinking these might be related to a certain endpoint. So I would select this label
to dig into this some more. And I can see that this similar spike
is showing up for this health endpoint here. So I would add this to a filter so now that I see this filter
with the health endpoint, I want to see if there's any other
metrics that would also be having similar spikes. So I can see that this is also showing
up for these sub metrics as well. So I may want to select
another metric to do a bit of investigation as well. And I may want to do other things
like share this once I figured out if there is a problem. So for example, I may want to bookmark this and I
can bookmark this view to look at later. I may want to share this with
my colleagues so I can copy this URL or I may want to
even view this explorer for example, if I wanted to let's say
play with the query some more, make it a bit more complex or
even add this to a dashboard, going back into Explore Metrics, I can see that there's also a history
here where I can go back and forth between certain steps. For example, if I wanted to go back into
the filter applied step or if I want to go back to a step where
I looked at another metric. Alright, so thank you Catherine. So now we know that there's a problem and
we found some associated metrics which gave us some understanding when and
how our infrastructure is impacted, but we really need to know what the
problem is so we can fix it or pass our investigation onto somebody who can. And this is where Logs
Drilldown comes into play. The challenges of looking for logs is
similar to looking for metrics in Grafana. If you can't find what you need, it can
be easy to get stuck and frustrated. You might know containers are crashing
or have high resource consumption, but you might not know where to start
looking for the right information in your logs. And even if you do, narrowing down your search can be hard
if you're unsure which fields or patterns to focus on. Logs Drilldown streamlines the process of identifying
and diagnosing problems in our infrastructure, the what and how as opposed to metrics
which will help us discover the when and the where. Finding the right logs allows
you to filter and refine
your understanding of the incident. And that's why we created Logs Drilldown. So we're going to do a live demo here. So back to our metrics
investigation. We learned, yeah, a couple hours ago we got paged or yeah, we found out that users were periodically
unable to access the website, something's going wrong. So
we jump into explore logs. So right off the bat here we're
seeing periodic spikes and error and warning volume in our logs. We're just going to take these two
services, it's two in the morning, I'm kind of tired, but it seems
like the right thing to do. So now we can either, at this point we can kind of see,
oh, okay, there's a visual anomaly, we can drill in and just look at a selection and then maybe just read through
our log lines and try to figure out what's going on. But I'm saying, okay, I know we've got some reports
of slow request times, so I'm going to jump into my fields
on the log lines and I'm going to say just show me all of the logs that took longer than 150 milliseconds. And then from here I'm
going to say, all right, well now let's take a look at
our jobs on these services. Everything, it seems correlated, but maybe not too much. Let's
go ahead and look at our pods. Alright, well interesting that it's again a mild
correlation and it seems to be equally impacting all of the pods
that we have a duration for. But I know that for recent data like this, Loki is an in-memory
data store of patterns, which will kind of analyze the bits
between your logs that have changed and they'll tokenize out the high
cardinality bits that are different, the timestamps and your trace IDs and
give you this view where you can kind of see, alright, again,
it's two in the morning, I'm just going to pick everything that's
kind of got this sawtooth pattern that seems to be correlated with
that five minute spike. And then we're going to
jump back into our logs. Suddenly we have a much cleaner
view of what's going on. Take a look at our logs right there
at the top. Query lock timeout, that seems interesting. Whole bunch
of failed requests, all right, already without really doing
any work or writing any queries, we can probably make a pretty safe guess
that there's some job that's getting run every five minutes, causing our database to lock
up and people are unable to access the APIs. Explains
everything, why we got pinged. So then from here I
might be skipping ahead. You might want to debug further and you
might want to jump into the traces on these logs, but we'll come
back to that in a second. Oh, I was hitting the wrong button, but also can we go back
to the slides? Thank you. As part of this launch, we'll be announcing support
for OpenTelemetry and
Metrics and Logs Drilldown. So we know that many of our customers
use OpenTelemetry to collect and instrument their data and now you can
view your OTel compatible metrics and logs in Metrics Drilldown and Logs Drilldown. So as a recap with Metrics
Drilldown and Logs Drilldown, you're able to reduce time
to first insight, reduce
time to diagnose a problem, leading to significant time and cost
savings for you and your team and improve your meantime back to bed. Both of these are GA and
available open source and on-prem. And in cloud. Ryan. Alright. Alright, thank you. Okay, so now we've
talked a little bit about metrics, about logs. I'm going to
quickly go through traces, spend a little bit more time on profiles
since I imagine for a lot of you that will be a little bit newer. But
basically with our Traces Drilldown, you saw a little bit of
this when Jen spoke earlier, you kind of understand what's going
wrong and traces are going to help you understand exactly where
that's happening and how to fix it. And so we're
going to play a quick video here. Let's talk about Traces Drilldown.
Just like with metrics and logs, there's no need to write queries anymore.
The interface guides you visually, allowing you to explore the data,
notice patterns and navigate with ease. The interface offers three distinct
views for displaying your data. The first one shows you the rate of
incoming spans and this is the default way to browse your tracing data. There is also errors of view which only
shows spans with errors in them and this helps you pinpoint issues
within your applications. And last but not least is this duration
view which allows you to identify and address latency related concerns. Alright, now let's go to the comparison page. Comparison page helps you understand
which attributes are contributing to latency the most. So what
are we actually comparing? Let's look at this histogram. You can see that the top slow
requests are highlighted in orange and that is what we call selection. Everything
else that is not selected on this histogram becomes the baseline. And so now for each
attribute key and value, you can see the percentage of how many
spans are present in the baseline versus the selection. And so for example, for span name you can see that there's
this slash profile span name and it appears in the selection a
lot more than anything else. There is a little bit of slash contacts
and slash avatar sprinkled in and maybe we should look into these as well. But slash profiles definitely
appears to be the biggest offender. And so to continue this investigation, you can click on this add to filters
button until you get to a page that looks like this, you can see that there's now no
difference between baseline and selection anywhere. And that's how you know that you probably
filtered enough and you're looking at the most important spans that are
contributing to the latency. And so what do these spans and
traces look like? For that, we can go to the root cause page and it
will show us this aggregated view of all the traces that match our filters.
So this is not just one trace, this is an aggregation and it
shows the most important spans. So typically this is a very good overview
of what's going on and if you want to go deeper, you can click on one of these buttons
and it will take you to the regular trace page where you can do deeper analysis
and work with specific individual traces. Last thing I want to show is how the
same concepts apply to the errors view. For example, if you go
to the root cause page, it shows us this aggregated trace view
and it highlights all the spans with errors in them. So now we can very quickly see which spans
are causing the errors without having to look at every single trace. Similarly, if we go to the comparison page, it works
the same way as it does for latency, but your baseline is now all the spans
that don't have errors in them and your selection is all the spans that do have
errors in them. And as you can imagine, this allows you to very quickly
identify all the attributes that are contributing to errors. And so
that's it for Traces Drilldown. Back to you Dmitri. Alright, I'm obviously
not Dmitri, but yes, back to me. Can we go
back to the slides? Yeah, so Jen talks about this a lot earlier. I mean I think the biggest takeaway
here is that we've really kind of transformed the way that you interact
with your traces to make it much easier to, even if you are going from not
knowing what's going on at all, you can kind of drill down
into exactly what's happening, which is why we renamed it to this.
And so we've talked about metrics, logs and traces. Now for my favorite
signal, I'm a little biased, I didn't mention earlier, I'm
one of the founders of Pyroscope, which is the database behind
our profiling product. And so yes, I'm very biased, but I do think that profiling has a lot of utility for a lot of different companies, a lot of different use cases. And here
at Grafana we're seeing it to be one of the most popular ways that people are
getting a lot more value from their data than they used to be. And so the reason why that is is because
profiling helps you complete the story of why something went wrong and
how to fix it. So a lot of times, let's say your metrics are telling you
that there's a spike in CPU or your logs are telling you that there's an out of
memory error with any of these kinds of situations, that's great, but at some point some engineer or
somebody is going to have to go write some code somewhere or change some
config in order to fix the problem. And what profiling does is it takes you
down to the line of code that's causing the problem so that you can actually
fix the problem and not just know that something's going wrong. And so whether
that's metrics, logs, traces, k6, Kubernetes, IRM, whatever it is, profiling always gives you just one
level deeper that last 20% that you need to actually resolve the issue.
The other side of that is that, or the outcome of that is that
you can either be both proactive or reactive with profiles.
Typically metrics, logs, and traces tend to have value
when you're reacting to something and profiling has value before
something even goes wrong. And so we most often see that
in the form of cutting costs, but we also see that in the
form of either getting rid of latency proactively or reactively and
then obviously responding to incidents. So I'll talk about the proactive version
first. How does it help you cut costs? Like here's an example of just
a theoretical world where, or maybe not theoretical, a very common situation where
years ago costs tend to be less. As time goes on, your costs will
continue to grow. A lot of bloat, things kind of work their
way into your system slowly. And then one day you wake
up and someone's like, "Hey, we need to get our costs down. Where do we go to address that problem?"
What profiling does is it basically breaks down all of these
various components of your
system to tell you, "Okay, here's where all of your costs are
being attributed and if you wanted to decrease costs, here are the areas that you can focus
on." And it even goes one level deeper than this obviously in telling you, here are the lines of code that are
actually causing these problems. It does this using a flame
graph. For the sake of time, I'm not going to go through this, but basically think of these are
giant pie charts that essentially tell you, and they're even nested pie charts that
essentially tell you this is the line of code and it calls this line of code which
calls this line of code and it'll tell you basically the width is
a hundred percent of your
CPU or a hundred percent of your costs. And then as
you go from top to bottom, it'll tell you which lines of
code are making up that 100%. So here's an example. This is
actually a company I used to work for. The reason that we started
Pyroscope and basically me and Dmitri, who you heard earlier were
working there and we had a queue that was constantly overflowing. We couldn't figure out what the issue was. And basically long story short, we enacted a hacky version of
what now exists as Pyroscope. And it was able to show us like, "Hey, you're spending a lot of
your CPU on," it was a compression task and basically we were
doing what we thought we should be doing and compressing something. But a change in the underlying API of
the thing that we were compressing had gone from compressing images
to compressing videos. And as you can imagine,
that's much more expensive. And then thus it was causing
our cues to overflow. This is something we wouldn't have been
able to see if we didn't have profiling. And it ended up actually saving
us ultimately like 20% of our CPU, which is around the number that we see
most commonly with what people are able to save using profiling. Next is responding to things as well.
So we have a couple of examples here. Shopify, one of our
biggest users of Pyroscope, they spoke at this conference
several months back and they use profiling, both preparing and during
the heat of Black Friday, which if you're not familiar with
Shopify - is a really large day for them. Everybody's using their online
stores to buy a lot of things. For them, One minute of downtime can mean
up to 2.85 million dollars in lost revenue. So every minute is extremely important
and understanding where their resource allocation is and making sure that they
have the proper amount of resources allocated is the difference between
them losing millions of dollars and not. Similarly Uber, they also spoke at this conference a
couple weeks back and for them they were using it in that more proactive use case. And so for them they were able to
find 10,000 CPU core reductions, saving more than a million dollars in
their infrastructure costs by using this profiling to understand what they were
doing. And they actually were able to integrate a genAI
integration in order to automatically then recommend fixes
and PRs and be able to resolve that. We have some product coming out soon to
be able to do some things like that and I'll show what we have in the
genAI space in just a second here actually. Yeah, I'll do it right
now. So yeah, so for this demo, basically what we're going to show
is a sample rideshare company. We do this more just to show
conceptually what's going on, but you can imagine this, each one of these boxes if you're using
Kubernetes would be a pod or if you're using whatever. If you're not, it would just be a process.
And essentially what this
is, is it's saying, "Okay, we have our clients who are generating
load, it's going to either the east, north or south region, which we add the region label," and
then it's either going to a car, a bike, or a scooter that you're ordering.
And that goes with the vehicle label. And the way Pyroscope works is every 15
seconds it's going to essentially buffer these profiles, send them off to the
server where they can then be analyzed. And if we can switch
to the demo here. Yes. So yeah, this is what it'll look like at the top
level once you get into the product, obviously this looks very similar
to the other ones that you've seen, but the difference is here you're going
to be drilling down until you get to the code level. And so at the highest
level, if I switch to rows here, we're looking at our data
source, we're looking at CPU, this is across a bunch
of different services. We're going to look at the rideshare go
service that I was just showing there. And so the next thing is, okay,
so we can see the CPU here, let's look at the various profile types
and see if we want to see something other than CPU.
So we can see CPU, we can see memory, we can see in use objects,
allocated objects. And so let's say there was
a memory leak or something, this would allow you to be able to
drill down into whatever that was. In this case, we're going to take a look at CPU and
those labels that I was showing just a moment ago. And so here
we have all of our labels. So this top chart is showing you CPU, just overall like something that
you would get from your metrics. But down here you're seeing CPU broken
down by the labels that I was showing before. So we can see
our region label here, we can see our vehicle label here, which were the two ones
that I showed you before. We can see it broken down
by totals, by maximum CPU, by histograms. I think totals shows really clearly what's
going on in this particular example. Actually, let me make this a little
bit bigger, sorry about that. In this particular example, so here we
can see that over this last 30 minutes, the north region has used
16 minutes of CPU time. The south and the east regions have
used three minutes of CPU time or almost four in this case. Let's say there's
an incident and that's the reason, or let's say we don't know
if it's an incident or not, but we want to understand what is the
difference between the north region and the south region that's
representative of this CPU usage. So we would select this and you
can basically select one as your baseline. So I'm going to say this is what we
expect since we see this multiple times, and this is the comparison, this is what we're trying to understand
what the difference is between the two of these. When I hit the compare button
and it's usually a little easier to see, I'm super zoomed in here.
But yeah, hit the compare button. And so basically what you have here is
on the left you have one query AP south for this time period on the right you
have another query EU north for this period. And basically the flame graph that we
get down here is showing us that in AP South we were only using 32% of CPU on
this check driver availability function. But in EU north we were using 78% of CPU. And so in an incident scenario, now this saves you from digging through
all the wrong parts of the code to figure out what's wrong. It's
going to highlight in red, "Oh yesterday when things were normal, you were only using this much CPU here
today you're using this much," or if it's a memory leak, "Yesterday this much memory was being
used and today it's much more," whatever that is. And we don't have a ton of time
to go through all the extra bells and whistles here, but we have this LLM integration
as well that will basically allow you to not have to read
this yourself if this isn't a visualization you're familiar with. And this will actually break it down
for us and essentially conclude that the problem is our Mutex lock function, which is using more CPU
than it should be using. And last but not least, ooh, I don't know if you are
authenticated on GitHub, but let's see, we'll give it a shot. If you click the function
details button here and let's see if you are. Alright, we got function details. So with the function details you can
also basically add a GitHub integration. We don't store any of
this coded ourselves, but basically now you can go from
this performance insight to seeing what's causing these performance issues. And in this case it's because we
designed this demo to have an issue. But you can actually see here the reason
that there's an issue is because for a period of time we're simply just
iterating i randomly to cause CPU so that we can show you a nice
looking flame graph. But in your case, this would show something much more
interesting and you would be able to basically click this
optimized code button, which is going to tell you not just
based off the performance profile, but the performance
profile plus your code, what you should do to fix this problem.
And it's probably going to tell us, yeah, we should sleep instead of just
iterating i randomly for the time period. So yeah, we can go back to the slides. I think that's pretty much
everything there may be. Yeah, so you've seen a lot of the
explore apps here. I mean, sorry, the Drilldown apps here. The biggest thing to take away is
that we've really focused on making it as easy as possible in order to start
from not knowing what's going on, drill down into exactly the root
cause of whatever issue it is and you kind of have all these tools
that you can be most efficient, as efficient as you need to
be to do that effectively. So that's all I have and thank you.

