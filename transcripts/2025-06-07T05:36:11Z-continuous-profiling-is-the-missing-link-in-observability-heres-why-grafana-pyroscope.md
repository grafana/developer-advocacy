# Continuous Profiling Is the Missing Link in Observability — Here&#39;s Why | Grafana Pyroscope

Published on 2025-06-07T05:36:11Z

## Description

Pyroscope founder Ryan explains why continuous profiling matters and how it helped companies like Shopify and Uber cut costs ...

URL: https://www.youtube.com/watch?v=fMkoJpSByV8

## Summary

In this video, Ryan, one of the founders of Pyroscope, discusses the evolution and importance of continuous profiling in software development. He shares insights into how Pyroscope originated from an internal system that proved valuable in optimizing resources and performance. Ryan emphasizes the significance of using various observability tools, including profiling, traces, and logs, in tandem to enhance application performance and reduce costs. He explains the proactive and reactive benefits of profiling, highlighting its unique ability to optimize both revenue and resource expenses. The video features a demonstration of Pyroscope's Drilldown app, showcasing how users can analyze and visualize profiling data, identify performance bottlenecks, and connect profiling information with traces for deeper insights. Throughout the presentation, Ryan shares examples from companies like Shopify and Uber, illustrating the tangible benefits of continuous profiling in real-world scenarios.

# Pyroscope Presentation Transcript

**Ryan:** My name's Ryan. I am one of the founders of Pyroscope, which is the open-source database behind our profiling tool. We started it about four years ago when we were working at a different company. We built an internal system that was doing a hacky version of what Pyroscope does today. This system was very valuable for our company; we got a lot of use out of it, saving both money and resources. This led my co-founder and me to think, "Hey, we could probably open-source this as a project that others might find valuable." And that’s exactly what we did.

Today, I'll talk about *Profiles Drilldown*, which I know you've seen a lot about in the various Drilldown suite this week. I will also discuss why it's important to care about continuous profiling. It's definitely one of the later signals that people tend to pick up, but I believe it’s just as valuable, if not more so, than some of the other ones you might be familiar with. 

### Why Care About Continuous Profiling?

I like to start with this question because there are many opinions out there regarding observability tooling. Some say you only need traces, others say logs or metrics. From my experience, especially starting with profiling on its own, I've found that if you have a hammer, everything looks like a nail. It's easy to claim that everything's a profiling problem, regardless of the database. However, having a complete suite of tools allows you to choose the best tool for each task, whether it's profiling, traces, logs, metrics, or load tests. Using these tools together enhances their collective value.

At Grafana, our focus has been on expanding beyond just providing profiling in isolation with Pyroscope. We also integrate with other tools, like Tempo, for instance.

### The Evolution of Profiling

This is a rough visualization of how things progress in profiling. You typically start with a signal, often locally. For example, most of us first typed "Hello world" in some programming language. Then, you move to something more official, which might be ephemeral and run on machines. After that, you start centralizing the data with a database, whether that's S3, ClickHouse, or any of the databases available today. Eventually, you reach a stage where that data communicates, and everything moves towards production data.

Profiling is undergoing a significant shift right now. Many people I've spoken to this week have mentioned they are doing some form of profiling, whether storing data in S3 or having a simple pprof file on their desktop. We’re seeing a shift towards continuous profiling, where you can quickly query the Pyroscope database for profiles associated with performance issues in production without needing to recreate them.

One major factor driving this shift is our work with OpenTelemetry. In April 2022 at KubeCon, profiling was voted the number one requested new signal for OpenTelemetry. We took this feedback and began efforts to integrate profiling into OpenTelemetry. Initially, we thought it would take about six months to achieve this, but as anyone familiar with OpenTelemetry knows, it takes longer than expected. However, this extended timeline allowed us to refine the format for the data, how we send it, and connect it with traces, logs, or other signals.

As of 2025, the OpenTelemetry profiler is in experimental mode, and we are working towards making it stable.

### The Unique ROI of Profiling

Profiling is unique because it directly optimizes both sides of the ROI equation. This is a hot topic in observability data—how much data you collect versus the value you derive from it. 

On one side, profiling can increase revenue by enhancing throughput and improving user experience through faster applications, reduced latency, etc. On the other side, it helps minimize costs by providing insights into CPU and memory usage, allowing teams to optimize resources. Often, users discover low-hanging fruit they were unaware of that consumes excessive resources.

### Proactive vs. Reactive Profiling

Profiling also offers a proactive approach to observability, unlike metrics, logs, or traces, which are usually reactive. When something goes wrong, you investigate the incident. With profiling, turning it on provides insights into your application’s bottlenecks before issues occur. You can identify potential problems, such as which components will fail first under load, allowing you to address them proactively.

### Understanding Overhead

A common question when starting with Pyroscope is about overhead and costs. It's valid, but we emphasize that our profiling has very low overhead because we use sampling profilers. Unlike other profilers that might disrupt application performance, our approach samples stack traces at a rate of 100 times per second, sending data to the backend without significant impact on the application's performance. Many users realize they were wasting CPU on unnecessary logging or excessive trace spans once they start using profiling.

### Observability Insights

Profiling also enhances observability across various systems, especially messaging and queuing systems like Kafka or Sidekiq. These systems can accumulate bloat, causing problems down the line, and profiling can help identify and resolve those issues.

### Case Studies

- **Shopify:** On Black Friday, where one minute of downtime can cost nearly $3 million, they utilized profiling to achieve zero downtime and enhanced performance. Using Pyroscope, they improved various libraries, reducing CPU usage by over 20%.

- **Uber:** They managed to cut over 10,000 cores from their infrastructure using profiling, resulting in significant cost savings.

### How the Database Works

Both Shopify and Uber, along with many other companies, utilize a system where profiles are stored efficiently. Pyroscope doesn't just drop raw profiles into object storage like S3; we heavily compress the data to minimize storage costs. We serialize function names to eliminate redundancy, and we store profiling data at different levels to enable efficient querying.

### Demo of Profiles Drilldown

Now, let’s switch to a demo of the Drilldown app using a sample rideshare application. In the app, you can start at a high level, viewing services and CPU usage. You can drill down into profile types and labels, allowing you to analyze CPU, allocated objects, and more.

Here’s how it works:

1. **High-Level Overview:** Start by examining the CPU usage across services.
2. **Drill Down:** Move into specific profile types and view detailed information.
3. **Flame Graphs:** View aggregated data over a timeframe to identify CPU bottlenecks.
4. **Comparative Analysis:** Compare different regions or services to find discrepancies in CPU usage.

For example, you might see that the north region is using four times as much CPU as the south region. Instead of just knowing there's a problem, profiling allows you to pinpoint the specific functions causing the issue.

### Conclusion

This was a brief introduction to how the Profiles Drilldown app works. If you have any questions, I’m happy to answer them now.

## Raw YouTube Transcript

My name's Ryan. I am one of
the founders of Pyroscope, which is the open source
database behind our profiling tool. And yeah, we started it maybe, I guess it's been like four years ago now, where we were working
at a separate company. We had built kind of an internal system
that was doing a hacky version of what Pyroscope now does today. And basically it was very
valuable for our company. We got a lot of use out of
it. We saved a lot of money, we saved a lot of resources, and I'll talk a little bit more
about that in a little bit. But that basically led me and
my co-founder to say, "Hey, we could probably open source this as a
project that other people might want to use similarly and get value to
the rest of the community." And so that's what we ended up doing.
And today I'm going to talk about not only Profiles Drilldown, which I know you've seen a lot about
the various Drilldown suite since you've been here this week, but then also about just why care
about continuous profiling at all? It's definitely one of the, I would say later signals
that people tend to pick up, but I definitely think that doesn't mean
that it's just as valuable if not more than some of the other ones that you
might be more familiar with. Yeah, you know the drill - Q&A. Yeah. So why care about continuous profiling? I like to always start with this because
there's a lot of people out there who say various schools of thought
about various observability tooling. You only need traces, you
only need logs, you only need metrics, whatever it is. And the way that I see it, especially coming from somewhere where
we had started with profiling just totally on its own is
that if you have a hammer, everything looks like a nail. It's very
easy to, as a profiling database to say, "Oh, everything's a profiling problem,"
regardless of which database it is. But as it turns out, really having this whole suite of tools
means that you end up getting the best tool for whatever task you're trying
to do, which sometimes is profiling, sometimes it's traces, logs, metrics,
load tests, whatever that might be. And so really being able to use
all of these tools together is something that makes them all
more valuable collectively. And that's what we've really focused on
inside of Grafana is expanding past just providing profiling in
a silo with Pyroscope, but also connecting to other
tools like Tempo, for example. Cool. And this is kind of just showing, I would say this is something
that is a very unscientific visualization of how things progress. And so normally you start with a signal,
you start with it locally. For example, most of us, the first
thing we ever typed was, "Hello world," on some language somewhere. And then you move into a little bit
more official where it's ephemeral, it's on machines. You move more official than that where
you start to centralize it with some sort of database, whether
that's S3, ClickHouse, any of the databases that we have
here, whatever that might be. And then you kind of move into more kind
of production data somewhere that all that data kind of talks to each other
and so everything sort of moves to the right, whether it skips one
or jumps over the other. But the big thing that I want to talk
about is just how profiling is really experiencing this shift right now where
I would imagine a lot of people in here, and a lot of people who I've talked to
at the booth and throughout this week have said, "Hey, I'm doing some sort of profiling.
I have this data we stored in S3 for my company, or I pull it down, I just have a little file pprof file
on my desktop," whatever it might be. And really we're seeing much
more rapid shift I think with profiling from that level of profiling
to a more continuous sense where you can have something that goes wrong
in production and you don't have to try to recreate it to get a
profile associated with that. Instead you just query the Pyroscope
database and you can pull profiles of what's going on from a performance
standpoint, from your application, pull flame graphs. And like I said, I'll show some examples of if you aren't
familiar with profiling and what a profile is, what a flame graph is,
I'll show that in a little bit. One of the big reasons that I think it
has made this big jump has been a lot of the work we've been doing
with OpenTelemetry. And so several years ago now, I
guess three years ago now, in April of 2022 at
KubeCon profiling was voted the number one requested
new signal that people wanted to see in OpenTelemetry. And
so basically we took that information, this was before we had joined
the Grafana suite of tooling, and we were basically like, "Okay, well
this seems like something people want. We obviously are very knowledgeable about
profiling." And so we decided to start the group that would eventually
get it into OpenTelemetry. At that time we were very bright-eyed,
bushy tailed, and we were like, oh, maybe six months and we'll
have it into OpenTelemetry. If you know anything about OpenTelemetry, nothing happens in six months.
So many things have happened since then. And honestly I think it was for
the best because we've really, really nailed down the
best format for the data, the best way of sending
the data across the wire, the best way of connecting the
data to traces or logs or other signals. And so we've done that
over these past several years. We've met with several language
maintainers - Go, Java, .NET, and gotten a lot of feedback and just
made sure that the direction we're going is one that will last very far into
the future and not be just yet another format for profiling data. And so here we are in 2025,
about three years later, and I would say that my estimate
would be in six months again, but this time I actually believe
it much more than I did then based off of the progress that we've
made. And it's in experimental right now. So you can actually use the OpenTelemetry
profiler to collect profiles. We just need to basically graduate
from experimental to stable. And so all that work is ongoing right now. And the other reason that I think
profiling is really unique compared to the other signals is that it's the
only tool that really directly optimizes both sides of the ROI equation. And I know that's something that
definitely can be a hot topic when it comes to observability data. How much are you collecting versus how
much value are you getting back from that data? And the interesting
thing about profiling, and I'm going to show some
examples here in a second, is that on one side you can definitely
increase the revenues that you're getting from your application because
you're able to increase throughput, you're able to just have a better user
experience with your applications running faster, reduce latency, and all of those are directly tied
to the information you get about your application in the flame graphs. And then on the other side
you have the cost side. This is one that I think is much more
unique to profiling where you're able to basically see where your costs
are going, whether that's memory, CPU are the most popular ones, but really any resource you can
get info into how much it's costing so that you can then optimize
those costs, minimize those costs. And a lot of times, as we've
seen with many people using this, it tends to be some easy low hanging
fruits of things that you didn't realize were using as much resources
as they are. Alright. Similarly as the kind
to the ROI conversation, there's also a proactive approach
to using profiling and then a reactive approach to using it as well. This is also something that I think is
pretty unique to profiling in that with metrics, logs, traces, a lot of times you're going to
get most of your value from those. When you're something's on fire, you're able to get an alert and you kind
of go down the path of investigating it. With profiling, you have this nice sort of proactive
approach that pretty much anytime you turn it on, unless your application
is perfectly optimized, which is just not really a thing. And so in reality, as soon
as you turn on profiling, you're going to understand something
that if you're not using profiling, you just don't know what is the biggest
bottleneck in your application When traffic spikes, what's the first thing that's going to
fall over that's going to cause CPU to run out, that's going to cause memory
to run out, whatever that might be. And you can discover all that
proactively with profiling and then have that benefit.
And then on the opposite side, when something does happen now you already
are familiar with it so that you're able to react to an incident or
a latency issue or a customer request or whatever that might be, and use profiling as needed there. Here's kind of an example sort
of showing what that looks like. So a big thing that people often
think about with profiling, I would say the number one question that
we get when people try to start using Pyroscope for the first time is, "What's the overhead and how much is
it going to cost me?" And it's a valid question, but what we usually say
and what is true about it is that it is very low overhead
because we're using sampling profilers. So if you've used profiling in the past
and you've had problems with overhead or how much overhead it's
adding to your application, that's likely because you were probably
using a different kind of profiler. Whereas this one is just simply sampling
the stack trace a hundred times per second to be able to understand what's
going on in your application and then it's sending that off
to whatever backend. And the convenient thing there is that
it's happening from a separate process. And so if you think about
that relative to your metrics, logs, traces, other signals that
you're doing in those, it's typically going to be some sort of
code that you've inserted into the path of your application.
And so just by default, that's more likely to actually have
much more overhead for your application than profiling ever would. And so one of the most popular things
that we end up finding once people add profiling for the first time and start
using Pyroscope is that they realize, oh, we were accidentally spending
10% of CPU logging some useless thing that we weren't
supposed to be logging or we had too many trace spans and those were causing
too much issues or whatever that might be. And so that's kind of where having
this observability into what your application is actually spending
its resources on is almost all, I mean I guess I'm biased, but I would say always
worth the 1% overhead to
understand what's going on with the other 99% of your
resources that you're spending. And I talked about the observability
side, that's just the top one here, but that's true for your incidents, that's true for messaging and queuing
systems is actually I would say one of the most popular ones. So if you ever
have overflowing cues, Kafka, consumers, sidekick workers,
whatever your queuing system is, profiling is always a very, very good tool because notoriously
an area where you can just send something to your asynchronous
land and just forget about it. And then it's really common
that it then picks up a lot of bloat and can then cause problems later and profiling will help you fix that. And then obviously infrastructure
deployment tools, other things as well. A couple examples of this, one of our biggest
profiling users, Shopify, this was a tweet from their CEO
talking about how much traffic they deal with on Black Friday. They're kind of like storefronts I guess
for lack of a better way to describe it.
But yeah, basically they're doing tons of requests
and for them they're processing so much money through their platform that one
minute of downtime can mean almost 3 million in lost revenue. And so they started using profiling
in this kind of preparation scenario in order to be able to
either get zero downtime or whatever downtime is there,
resolve it as fast as possible. And so they actually had some really
cool examples that they found using Pyroscope and profiling too They made some improvements to variousails
libraries and system libraries and things like that that they were able
to then decrease their CPU by over 20%, which at that scale is a massive amount
that they're then saving on their infrastructure. And so my favorite is a quote
down here from one of their engineering directors about how one
of their engineers who was focused on efficiency and performance was like, I had no idea how I was doing this before
continuous profiling. And so if you're someone who it's your job to
be focusing on performance, this is going to be something that's
super helpful for you to have and be able to just have a good idea of what's
going on in your application. Another example, this one I'd like to
share for slightly different reasons, they were focused more on the cost side. People here I think are
very familiar with Uber, and basically they were able to
use profiling to decrease the amount of cores that they had and
they deployed it across their entire infrastructure and were able
to cut out over 10,000 cores, saving a lot of money
on their infrastructure. And so what allows this to happen, I'm going to kind of quickly go through
a little bit of why the database works so well. So two things about actually
both of those companies I just mentioned, and possibly some of you here, many other companies that we talked to
is that you kind of have built some sort of system. Maybe you're just dropping
these profiles into object storage. And so this is how a profile
gets turned into a flame graph. And so basically what you're seeing here, these are just simple functions with
how long they're being run and then they turn into a flame graph like this. And so more than just
dropping them raw into S3, which would be very cost prohibitive if
you were doing that as essentially using that as a database or whatever
your object storage is, is that we then do a lot of compression
to make sure that all of this data that is getting replicated or
sorry duplicated many, many times as you're adding these
flame graphs to wherever you're storing them, we then use trees
to compress them very, very heavily. And then after we
compress the actual functions themselves, the symbol names themselves as well
tend to have a lot of duplications. So here you have net/http
requests, net/io.read, net/io.write, you don't need to save
net that many times in the database. And so by also serializing those symbols, we're able to then get the actual
storage of the profiling data down very, very low. On top of
that. then it's like, okay, so you have all this profiling data.
Again, we're collecting it continuously. And so let's say you're getting a
profile from every pod every 10 seconds, and so that can really
add up very quickly. Now if you want to get a profile
of the last week's worth of data, you then need to somehow at
read time or at query time, merge all of these profiles together so
that you get one profile for the last week or the last month or whatever.
And so basically how we solve that problem is we use these segment trees,
storage is cheaper than compute. And so essentially we store the profiling
data at different levels to make it so that if you're then querying 50
seconds worth of profiling data, it goes from you getting all
these segments to instead of doing four merges, you then just do one merge of a
giant segment and a small segment in order to get those queries. I'll save this for after and
go ahead and switch to the demo and show you a little bit about what
the Drilldown app looks like and how you then would solve an issue inside
of a UI. So for this, we're going to use a sample rideshare
application just because what people - more for conceptually so that you
understand what's going on here. And so basically we have a region
label, we have a vehicle label, and I'm going to show you how this looks
when we're collecting profiles from these various regions and then viewing them inside the UI.
And so if I go to the Drilldown app here, yes, I think it's definitely big enough. And so the Drilldown app here. And so basically what we've built is
something that allows you to drill down into the root cause of an issue. And
so if you start at the high level, you have all of the services here. In
this case we have our rideshare service, some other services, we're looking at the CPU for
this service and seeing if there's anything interesting here. Maybe there's CPU spiking
like there is here. I'm not going to go into that
one for this demo. But yeah, that allows you to see from a
high level what's going on there. And so from there you can
drill down either into the
profile types or the labels for that service. So I'll
start with profile types. So now we're looking at
the same service here, but we're looking at all the different
profile types for that service. I'll switch to grid here. So you can see
'em all. CPU, allocated objects, allocated space, in-use
objects, in-use space. And again now this allows you to see
a little bit more information about something you might want to dig more
into. We can click into our labels here. And so well actually I'll
do flame graph first. So from there you can go into the flame
graph and then now you're just looking at over the last 30 minutes, these
are all the data points that we have. They've all been aggregated together
to say that we spent 23 minutes of CPU time and these are the functions
that we spent that CPU time on. And so you can see here
what the bottleneck would be and if you can start there, but
we also have these labels here. And so like I said, I showed before
that there was the region label, there was the vehicle label, and you can see that reflected here.
We also have span name here, and so we're actually connecting
these profiles with our traces to be able to actually get a trace, or sorry,
a profile per trace span as well. So yeah, so now from here you can already
see if I go to totals for example, you can see that the north region is using
four times as much CPU as these other two regions. I can also go to
maximum, I can go to histograms, but based off of these totals, let's say there's an incident going
on in the north region and we need to resolve it. Now, if you just had metrics, you might see something like this that's
showing that this region is using a ton of CPU, but if you actually have profiles, you don't know that this is
just using the CPU, you can know the functions that are associated with it.
So if I select this as my baseline and I select this north region as my
comparison and I hit this compare button, I'm going to just auto
select the time period. Now what we're seeing is
that there is the difference, it's almost like a gitdif the difference
between the south region and the north region is that we only spent 28% of CPU on this specific function
in the south region. And then in the north region
we used 78% of CPU on the same function. And so if there was an incident like
now this is telling you specifically why you're running out of CPU as opposed to
just showing you that you're using a lot of CPU. And so now you
know down to the line of code. There's some nice bells and whistles here as well. We have this LLM integration here that
allows you to also kind of explain this. There's a lot going on here obviously, especially if you're not
familiar with flame graphs, but this actually will kind of walk
you through what the impact is, what the biggest problems
are in the application, and what you should look at to go fix
it. And so this kind of shows you that. And then if we actually go to
the flame graph here for now, we only have this for Go at the moment, but we're actually bringing this to
other languages as well because we're so close to the actual code here, I can go to function details and I can
actually connect this with GitHub and it will bring up this actual function
that we're running and what's actually happening here. And so in
this case, this is a demo, so you can actually see how I
got the demo to look like this. I basically just said if the region is
EU North force a mutex lock and then it's forcing a mutex lock. And so that's
how we're able to see that there. Then this allows you to see that last
thing I'll show is what this looks like inside of our traces there see demo traces. I'm going
to select that same service: Rideshare, Go and run a query. And so here I can sort
by the slowest traces. And so here we can actually
see that there was one trace that was significantly
slower than the rest. And so similarly to how we were
looking at all those profiles that were aggregated together,here we're looking
at one profile that is associated with just this specific trace span.
So this trace span was 19.2 seconds. We see this profile was 19 seconds, and so now you know more than you
would just have with just tracing, but you have a little bit more insight
here into what's actually causing that slowdown. We can switch back to the slides, I think. Yeah, and so that's kind
of a real quick intro to how our Profiles
Drilldown app works and there's any questions
I can answer those now.

