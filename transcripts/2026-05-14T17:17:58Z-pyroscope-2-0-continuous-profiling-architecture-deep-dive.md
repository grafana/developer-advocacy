# Pyroscope 2.0: Continuous Profiling Architecture Deep Dive

Published on 2026-05-14T17:17:58Z

## Description

Pyroscope 2.0 brings a major architectural rewrite that cuts production infrastructure costs by up to 74%. Christian Simon and ...

URL: https://www.youtube.com/watch?v=vseSm-pzgmc

## Summary

In this video, Pyroscope team members Christian Simon and Alberto Soto discuss the release of Pyroscope 2.0, focusing on the importance of continuous profiling for monitoring application performance. They explain how traditional profiling methods can be cumbersome and costly, particularly in production environments, and highlight the advantages of continuous profiling in reducing overhead and improving debugging during incidents. The presenters review the limitations of version 1 of Pyroscope, detailing its architecture flaws and the challenges faced with scaling and resource consumption. They then introduce the significant improvements made in version 2, including a new architecture that separates the read and write paths, utilizes object storage for data, and enhances performance and cost-efficiency. The video concludes with a live demo showcasing new features such as flame graphs and heatmaps, which provide deeper insights into application performance. The presenters encourage viewers to adopt or upgrade to Pyroscope 2.0 for its improved capabilities and ease of use.

## Chapters

Here are the key moments from the livestream along with their timestamps:

00:00:00 Introductions to the livestream and speakers  
00:01:30 Overview of Pyroscope 2.0 release and its significance  
00:03:00 Explanation of continuous profiling and its advantages  
00:05:15 Discussion on the limitations of profiling in development vs. production  
00:07:00 Major use cases for continuous profiling in incident debugging  
00:10:00 Transition from Pyroscope v1 architecture to v2 architecture  
00:12:30 Detailed explanation of Pyroscope v1 architecture and its flaws  
00:15:30 Introduction of the new architecture in Pyroscope v2  
00:18:00 Key benefits of using object storage in Pyroscope v2  
00:22:00 Live demo showcasing new features in Pyroscope 2.0  

Feel free to ask if you need more details on any specific moment!

# Pyroscope 2.0 Presentation Transcript

**Christian Simon**: Hello everyone, thanks for being here. We're going to tell you a bit more about Pyroscope 2.0, the major release we made yesterday. There's already a 2.0.1 out, which is a small fix. My name is Christian Simon, and I have been working on the Pyroscope team for the last three years.

**Alberto Soto**: And I'm Alberto Soto, working at Pyroscope as well for almost two years now. Hola, Barcelona!

**Christian Simon**: Today, we're going to teach you about why you should use continuous profiling. We will review our previous decisions as part of the v1 version, discuss what didn’t work, and how we fixed it with v2. We'll also cover lessons learned while rolling this out to production, and finally, we'll showcase the new features this new architecture allows—ending with a hopefully successful live demo of those new features.

## What is Profiling?

Profiling is the process of collecting information about how your code runs and how much resources it uses in different components and packages, down to the line number. Traditionally, profiling was conducted in development environments close to your source code checkout, which came with significant overhead, affecting performance. 

While this method is useful, we all know how little we can predict real production data from our tests and benchmarks. Often, production behaves quite differently than our microbenchmarks suggest. This is where continuous profiling shines; it can run in production without increasing costs or latency for your applications. It does this by using a low sampling rate, which might miss certain events but will still capture significant ones due to continuous monitoring.

This capability is particularly powerful for debugging incidents. You can review changes in CPU usage or memory allocations from last week to this week, or from the last hour to now, when a problem arises and all services stop responding.

### Use Cases for Profiling

1. **Incident Debugging**: Metrics and logs can alert you to issues, but profiling helps you zoom into a service, showing resource consumption changes, which can help confirm your theories about system problems and expedite solutions.

2. **Latency Reduction**: In businesses like food delivery apps, waiting time is critical. If your service is slow, customers will switch to competitors. Profiling helps identify what to cache in order to reduce latency.

3. **Cost Optimization**: Over time, services may slow down, prompting scaling up resources. Profiling can help identify low-hanging fruit for optimization, highlighting changes in the application that require attention.

In version one, we profiled our own database extensively and found high usage areas that required major refactoring. 

## Pyroscope v1 Architecture

**Alberto Soto**: Let’s start with an overview of the Pyroscope v1 architecture. As many of you might know, this architecture is based on a Cortex model, which has ingesters between the write and read paths. 

In the write path, profiles enter the database through distributors and are written to ingesters, which hold profiles for one hour in memory. Queries come through queriers, which sometimes check ingesters for profiles from the last hour. However, this architecture struggles to scale, as ingesters can become overcrowded with queries, affecting the write path.

Here are some key issues with the v1 architecture:

- **Availability Problems**: Heavy query traffic can affect writes.
- **Write Amplification**: Profiles are replicated three times, and due to our sharding strategy, profiles can be spread across all ingesters, leading to inefficiencies.
- **Operational Complexity**: Scaling ingesters takes hours instead of minutes, making it hard to accommodate fluctuating traffic.

## Transition to Pyroscope v2

**Christian Simon**: We frequently asked ourselves what would happen if our data volume suddenly increased tenfold. With the v1 flaws, we were able to scale up temporarily, but costs would not remain linear. 

To address these issues, we aimed to increase availability by decoupling the read and write paths. We decided to store large profiling data in object storage, which allows for high parallel access, low cost, and data redundancy. 

### New Architecture Overview

In the new architecture, ingesters have been replaced with segment writers. Profiles arrive at the distributor, which maps them to segment writers. The profile data is uploaded to an object store, and the metadata is recorded in a new component called the meta store. This allows for a stateless read component that can scale independently based on query load, with minimal dependency on the write path.

The way we shard data has also changed. Now, we shard by service, which means data is stored only once if the service is small enough. This leads to favorable storage reductions.

### Improvements in Storage Efficiency

For example, consider a simple pod running 30 replicas with 1 MB/s of profiling data. In v1, we stored this data three times, leading to a 66% reduction in storage in v2. For symbol data, which was previously stored multiple times, we’ve seen reductions of up to 95% in certain cases.

The read path benefits from this reduced data storage as well. Query front ends ask the meta store where the data resides in the bucket, which leads to quicker response times and allows us to react faster to changing workloads.

## Why Upgrade to Pyroscope v2?

**Alberto Soto**: We have been running Pyroscope v2 in Grafana Cloud for over a year. After rolling it out in lower environments, we moved to production, and by September last year, it was deployed across all Grafana Cloud regions. 

In our largest clusters, we saw significant reductions in memory and persistent volume usage. This demonstrates the benefits of transitioning from v1 to v2.

### New Features in Pyroscope v2

We have built several exciting features exclusively for v2:

- **Recording Rules**: Now you can record any profiling information and export it as a metric.
- **Profile Exemplars**: This feature allows for better visibility into specific profiling data.
- **Heatmap Panel**: Provides visualization of request distributions.
- **Profiles to Trace Flow**: Enables tracing requests through the system.

## Live Demo

**Christian Simon**: Now, let’s move on to the live demo. 

(Transition to demo)

In this demo, I’m looking at our Profile's Drilldown app, specifically the query backend. Here, you can see the workload over the last three hours displayed in a flame graph. This visualization breaks down CPU usage by different parts of our code.

We can now zoom into specific profiles, allowing us to identify why certain pods perform slower than others. 

Additionally, with the heatmap, you can visualize the request breakdown. Red fields indicate higher request volumes, while darker fields indicate fewer requests. This helps us identify which requests consume the most CPU time and need optimization.

## Conclusion

To summarize, continuous profiling helps reduce downtime, find root causes quicker, improve service latency, and optimize resource efficiency, ultimately saving costs. 

If you’re not using Pyroscope, we encourage you to start with v2. If you’re already using it, upgrading to v2 will make your experience cheaper, easier, and more robust.

Everything we've shown today is available in the open-source version. If you prefer not to manage it yourself, you can use Grafana Cloud, which offers a free tier.

Thank you for your attention! We will now take questions. 

(Audience applauds)

## Raw YouTube Transcript

- Yeah. Hello everyone,
thanks for being here. We gonna tell you a bit
more about Pyroscope 2.0, the major release we made yesterday. There's already a 2.0.1
out, so a small fix. My name is Christian Simon, I work on the Pyroscope team
for the last three years. - Yep, and Alberto Soto here working in Pyroscope as well
for almost two years now and Hola, Barcelona! - And so today we gonna teach you about why should you use continuous profiling, and then we make a bit
of a review of your, of our previous decision
as part of the v1 version and what kind of things didn't
work and we fixed with V2. Lessons learned while rolling
this out to production, and then finally the new features this new architecture will allow, and I'm ending with a
hopefully successful live demo of those new features. So first of all, what is profiling? So profiling is the process when you try to collect
information, how your code runs and how much resources it
use in different components, different packages down
to the line number. And so profiling typically was run more like on the development environment, so we're pretty close to
your source code checkout and with quite extensive
implications for the target. So you would have a significant overhead collecting those profiles. And while this is good enough, I think we all know how
little we can predict the real production data in
our tests and benchmarks. So often the production has
quite a different behavior than maybe your microbenchmarks predict. And this is where continuous
profiling just shines because it is able to run in production, it does that by reducing the overhead to not increase your cost or the latency of your applications. And so it does that on
a very low sampling rate so it misses certain events, but it will still pick
up the significant ones just by the fact that it
looks all the time at it. And that is particularly powerful when it comes to things like incidents because you can jump back in time and investigate how your application might have shifted the CPU
usage, or the memory allocations from last week to this week,
or from the last hour to now where you suddenly have a problem and all services no longer reply. So this is also a major use case for us, this kind of debugging
in an incident scenario. Obviously we have metrics,
we might get alerted because of a high error
rate seen by our customers. We might have logs that tell
us there's something wrong, there's like a client timeout or we're not able to respond in time. And then also those logs
might contain traces, which further allow us to
pinpoint it down to a service or even a component in a service. But then where profiling helps you more is when you want to
zoom into that service, it actually then can go
up to the line number, show you kind of how the
resource consumption changed, and you can then hopefully
pinpoint more what is happening, maybe confirm your theories,
what is wrong with the system, and then hopefully quicker fix the system and bring them back online. Where this is also super helpful is when you are or have to
go to lower your latency, and I think that's quite
important for many businesses. So if you imagine a kind of Eat order app, there's only so much
time you're gonna wait until you can get your order through and otherwise you're gonna
move to a competitor. And as many of those services are composed of multiple microservices, this latency between
the services can add up. And while maybe tracing tells
you a good war clock number, you still wanna understand maybe
how you can shave off more, and profiling will tell you what kind of things you maybe should cache and therefore reduce latency in, and what actually has
impact in your hot path. And the final use case is the
kind of cost optimization, reduce efficient resource usage. So obviously we all know
our service is slow, we maybe scale it up and then maybe the week
later we scale it up again and give it a bit more memory. And I guess over time this might sum up and you might be looking
for a good opportunity, the low hanging fruit to optimize and profiles will point you
into the right direction, and it can also be pretty powerful to highlight things that have changed. When you maybe wrote the
applications five years ago, your constants might have
been right for the usage, for the data format that you saw then, but something's changed since then and maybe the whole format grew and it's no longer the right constant, and things like that you
will see in a profile and you can actually react to that. We obviously, as the profiling team, we profile our own database quite a lot and in version one we saw
quite a lot of high usage areas where, I guess, the
simple low hanging fruit was no longer feasible and in that v1 architecture
we had a couple of flaws that took a major refactoring. Gonna look at that now and, yep. - Yeah, so let me introduce, yeah, let's just start with
for the beginning let's see, let's take a look into
Pyroscope v1 architecture and let's see what's wrong
here, or what can be improved. So these may be familiar for some of you, this is because Pyroscope v1 architecture, as many other Grafana databases, is based in the Cortex architecture. This one with the ingesters
in the middle in the, between the write and the read path. And yeah, if you're not
familiar, no worries, I'm gonna explain it. So in the left you have the write, the profiles come into the
database through the distributors and are written in the ingesters. Ingesters are servers that hold profiles for one hour in memory. So they're scaled to be very big in memory and they can even start using disk if they run out of memory. On the other hand, we have the query path. Queries come through queriers and we sometimes need to
go check into ingesters for the profiles on the last hour. And that's when we start to see that these architecture hardly scales, ingesters can be overcrowded by queries, and write path can be affected easily. This architecture is more complex, this is only a simplification. We are completely omitting the part where ingesters persist
data into object storage. But yeah, this is enough to
explain our pains with v1. Let's get into detail with the write path. So once a profile reaches Pyroscope, first the distributor
will compute a series hash from all its labels, values and names. This makes that, for example, if we have service name checkout and allow a label, for
example, region, Europe. It will compute a hash of
it, it's the series hash and we will chart this profile according to this series hash. Distributors will then write this profile into three different ingesters. We call this replication factor of three. And new profiles with the same labels will end up in the same
ingesters, but different profile, another profile with similar labels don't necessarily need to
end up in these ingesters because our digest series hash function. Whenever we, whenever two
ingesters acknowledge our write we call this a quorum and we
consider the profile written, and then the distributors acknowledge the write to the client. On the other hand, we have the read path. It's a bit more tricky in the
sense of replication factor just because when queriers receive a query they don't necessarily need to know in which ingester the data is, and they need to replicate the query and forward it to every ingester
looking for that series. That means that most of the time we need to query all the ingesters not only the three that we
know or where that data is. And then if we have 10 ingesters we will replicate this query times 10. Then we need to duplicate because once we've found where's the data, maybe after querying eight,
nine, maybe 10 ingesters, we need to duplicate that information before making the queries result. Now that we have the architecture in mind, we can take a look into the
flows of this architecture. First of all and very obviously
we have these ingesters sitting in the middle of
the write and the read path. And this makes availability harder just because whenever we have
heavy traffic on the queries, writes can be affected. Also because we have these
ingesters stateful set, we need to scale these to
accommodate both traffics and this implies a lot of cost as well. So yeah, we have availability problems, we have cost problems here. On the other hand we
have write amplification. I just told you that we replicate
every profile three times, but also because our sharding strategy is not super strong here and we just use a series
hash to split it everywhere. Two profiles from the same service that have different labels may end up in different ingesters, which means that profiles
are actually spread in all ingesters. This is very bad for
us in terms of symbols because profiles comes with
a lot of symbolic data, for example, stack traces,
function names, lines. Those are repeated over all our ingesters not only three but the more because of our sharding strategy. Also the write amplification, I mean this is very costly
to have all this replication but also makes latency worse
because on the query path we need to duplicate all this
information all the time. And finally another pain
point for Pyroscope v1 is how hard it is to operate with it. We lack a lot of elasticity, it's very hard to scale up
or down those ingesters, it takes hours to do
so instead of minutes, and we need to scale
ingesters for both traffics, meaning that maybe we need
to scale ingesters a lot to accommodate the 1% of the queries that are hard to compute. But the 99% of the time we are just sitting on
an oversized ingesters that are increasing again
our write amplification. And now we are gonna look
how we solved all of this on Pyroscope v2. - Yeah, something we ask us a lot in the databases department where I guess Pyroscope is in as well, what would happen if suddenly
our customers send us 10x of the data if we
have 10x of customers, or like if we have 10x of
services with a lot smaller data. And I guess with the
flaws that we seen in v1, we bought us a bit of time by scaling up, but it definitely, like the
costs wouldn't go linear anymore if we would do the 10x. And so this definitely was a problem for this outlook of
what is the road ahead. And so we kind of sat down
and tried to figure out, like what do we wanna solve with this? And so obviously we had the major flaws, and I think the start for us was we need to increase our availability. So how can we achieve this decoupling of the
read and the write path? Our thinking was obviously the data, the profiling data, symbol data is large and we get quite a lot of it, while the metadata is rather small and we basically only use it to look up where to
look for the real data. And so we kind of split those two paths and store the actual big profile data in ideally a medium with
a lot of parallel access, low cost and high
redundancy for data storage. And basically that ended
up into the major decision of storing data only in
object store buckets. So before we had quite a
lot of the most recent data in memory and on persistent
discs on those ingesters. That's no more. So all the data will be in the bucket and will be accessible for
any new pod we spin up, it has access to that bucket. And in order to make sure clients, when they send data to us, we can confidently say them, we got it, we now wait until the
data reaches the bucket and we register that kind
of fact in the metadata and only then we return
to our uploads clients. And so what does, this allows us to have a
stateless read component that we can scale
exactly to the query load with very minimal dependencies
on the write path. So the only dependency
is in this metadata, and so that leads to this architecture. So we can see now the ingesters are gone and we replaced them with
the so-called segment writers and they are now in the red color, so they are write path only. And so a profile arrives, the distributors will map
them into segment writers and then, as I said, we
upload to object store, register the fact in a new
component called meta store. The nice thing about the
object store as well, is it is not our concern. So we pay our cloud provider for scaling the object
store for our needs, and so our concern only
remains with the meta stores that they can both handle the
read and the write workloads. And then the read path will then use the meta store for planning and execute the queries only based on the data in the bucket. So what I wanna focus on now
is this kind of first step. So a profile arrives,
it hits the distributor and now we need to decide
where do we wanna have this? And as Alberto told us there was a big flaw in
that we used the series hash to kind of spread and
chart the data around, and that meant for the symbols we're storing data over and over again. And the way we tackle this is now we try to figure out
what is the underlying service and we shard it by service. And ideally a service is
small enough to fit one shard, and in that case we store
the data really only once. If the service becomes
bigger, it might be a company that only runs one service
and at a mega scale, we can still shard the
data to split the problem, make queries fast, but only
then and not in every case. And that leads to, kind of some very favorable
storage reduction with v2. So I'm assuming a simple
pod, we run 30 replicas and let's say we have
about one megabyte a second in profiling data. So roughly about 60%
of that is symbol data and the rest is sample data. So sample data it will basically, when we stored it in v1
we stored it three times, so the reduction is 66% because
we now store it only once without the replication factor. And for symbol data, the
scale of the whole cell depended on how often we stored the data because the more ingester, the more copies of the
symbol data we would have. So in this case I'm assuming a cell with
about 50 ingester pods and we would've stored a
megabyte a second in symbol data, so actually more than we received. And then in v2 we would
actually go down by 95%, so this is actually a value
from our production rollout. Theoretically it can be maybe
going down to 2% in that case, but this is more the value
that we generally have seen. And now looking at the read path, obviously that reduction
in things we store also reduces how much we have
to read when a query hits us. So the processes, the query front end is the one that will ask the meta store, where do we have this data in bucket? And then it would hand
it off to query backends. And the query backends can
be spun up within seconds so there's no disc attached so
that there's not much weight, so we can react a lot quicker
to changing workload patterns. Also in our initial plan we always wanted to have
a serverless component. So obviously it takes a while for us to create more replicas in pods, and we still wanna be able
to serve those queries. So this is one of the things that we haven't quite yet
managed to do, but it is, there's no more limitation for doing that. - Colin, you may think now
should I change to Pyroscope v2, anyone running their own Pyroscope? And yeah, I bring you some reasons here. First of all, we've been trying this, we've been running this
for in Grafana Cloud for more than a year. We started rolling this out
in our lower environments where all our Grafana labs
and profiles are stored and we found this to be so
useful that the following month we started rolling this out in production. And yeah, after a few
tweaks on heavy customers that were sending a lot of data, by September last year we
managed to roll out this to every Grafana Cloud region. And it's been running since then, it's been already seven months until today and now we are confident enough to recommend this for everyone. We think this is great and, yeah, I'll also bring you some
data about around this. So this is from our of, this is one of our
biggest regions clusters and yeah, you can easily see
a drop and you may think, "Wow this is when you
used start using v2." Well not actually, the drop
is when we stop using v1. So we can clearly see
this very prominent drop. And before that we see a small increase, that's when we start using v2. So for sometime to do a smooth migration we started running, we both
running v1 and v2 on the region and we do this migration. And yeah, so we first enable
v2, we increase our cost a bit, then we drop v1 and we see this huge gain, mostly on this, on the yellow, the second part from the bottom
one which belongs to memory and the top red one that
belongs to persistent disc. Let's see, just a
breakdown on the details. We basically reduced the volume
on object storage by a lot because we're not storing,
we're storing unique data, we are not obligating anymore. We increased in object storage operations because our segment writers are writing profiles to object
storage every half a second. But yeah, you may see as a summary that we reduced on
uncertain cells up to 74%, mostly in memory and persistent
volume with 19% of gains just because we got rid
of those heavy ingesters. And I'll let you bring
more reasons to move to v2. We've been building over the last year cool features only on v2, and we are gonna demo some of them today. The first one is recording rules. This one won't see,
won't be seen in the demo but I'll explain real quick. You can as we now are
storing profiles better, we can process them easily and now we're offering
metrics from profiles, recording rules. You can record any profiling information you are interested in and
export it as a metric. You can target, for
example, function names which is pretty useful if
you are developing libraries. Next one, this one will
appear in the demo, is the profile exemplars
that Christian will show. Then heatmap panel, and
profiles to trace flow. Yeah, Christian will show they
are available in the backend but now we've done UI
version so you can consume. - Yes, like now looking at the demo. So yeah, this is basically my
screen should be showing up and yeah, there we go. So you can see kind of the entry point of our Profile's Drilldown app. In this case, as per usual, I'm looking at our own deployment, so this is a def cell of us, and I'm looking at this query backend, so the one that fetches the
data, calculates the result. So you can see this is a
quite spiky workload already. I'm now kind of going to the flame graph. So what the flame graph tells us is a good aggregation of what has happened in those last three hours. So this will break down the CPU usage, in this case to different
parts of our code. And so what we can now do that we have a lot more processing power in our query backend, we can now show you
actual particular profile. So often it's interesting how
a particular profile performs. So in this case this is a pod set DMM MSS, and this particular pod in that time, you can now look at the profile and see what maybe
particular reasons it has to be slower than the others. And so you can see we picked
out that single one now and that allows you to
zoom in a lot easier. So before you needed
to do a lot of zooming, a lot of filtering. This is a real life time saver here. And so we actually want
to go a step further and Alberto has mentioned
the heatmaps, ban heatmap. So when we collect profiles, we actually collect also the
information about traces. So previously you could
jump from the trace view into a flame graph, but the
way back was not possible just because of the limited
query processing time we had available, but now we can do that. So what you can see in the heatmap is fields that are more red, more on this side of the rainbow. They will have a lot more requests. And so this is a real kind
of span request breakdown while the ones you see in
the dark blue indigo color, there's only a few. So you can see, like the
red here for example, has 13,000 requests
that fall in this bucket of 10 milliseconds CPU use and up to 500 milliseconds CPU use. And so obviously with that information, you can now basically look
at and find the top requests, so which is I guess this one, and you can see 10 seconds
are spent on the CPU alone during that request. And you can also open the flame
graph, kind of understanding where exactly this 10 seconds
are spent, in which libraries. But what we also can do
with this information is actually pulling data from Tempo. So you can see the data we've seen so far is stored in the profiling database, and now we're trying to
find mappings in Tempo and that gives you a lot more context where the request is coming from, how is it traveling through your system. So you can see the 10 seconds on the CPU actually means 17 seconds
for the whole query to wait, and that's obviously quite a long time. It's quite a heavy query. This is maybe something
we should optimize next. Okay, and now I wanna
go back to the slides and wanna look at the conclusion. So why should you do continuous profiling? It allows you to reduce your downtime, it helps you find the root cause quicker. You can also improve your
latency of your services, improve the resource
efficiency of your service and therefore save costs. If you start doing that, use
Pyroscope 2.0 straight away. If you already do that,
upgrade to Pyroscope 2.0 because it's cheaper,
it will be easier to run and this is a lot more robust. It is a OSS project. Everything we shown today
is available in OSS. Some are PR's what are shown in demos, so expect them to roll into
the next Grafana versions. Obviously if you wanna avoid all the toil of running it yourself,
you can use Grafana Cloud. There's a free tier. We are there. Any more questions here?
A couple more resources. We do a live community call
tomorrow morning at 10:30 and we are at the Ask The Expert
booth right after the call. And that's it. (audience applauds)

