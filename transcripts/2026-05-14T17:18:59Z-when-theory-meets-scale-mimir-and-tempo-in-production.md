# When Theory Meets Scale: Mimir and Tempo in Production

Published on 2026-05-14T17:18:59Z

## Description

Marty (Grafana Tempo maintainer) and Marco (Grafana Mimir maintainer) share three real incidents from Grafana Cloud and the ...

URL: https://www.youtube.com/watch?v=iFyGv5nOgr4

## Summary

The show titled "When Theory Meets Scale: Mimir and Tempo in Production" was published on May 14, 2026. The speakers, Marty (Grafana Tempo maintainer) and Marco (Grafana Mimir maintainer), discussed real incidents from Grafana Cloud that highlighted challenges faced with the Mimir and Tempo databases. Key topics included the "query of death" incident that led to architectural changes in Mimir, improvements in query handling and resource management in Tempo, and the redesign of the query scheduler in Mimir to prevent slow queries from affecting performance. The speakers emphasized the importance of isolation in architecture, effective on-call practices, and continuous learning from incidents to enhance system resilience.

Topics: Mimir, Tempo, query handling, architecture, incident response, Grafana Cloud.

## Chapters

00:00:00 The query of death incident in Grafana Mimir
00:07:05 New architecture for ingestion and query isolation in Mimir and Tempo
00:14:00 Improving query performance in Mimir

Hi, hello. Welcome. First, I would like to start with a little preface. Grafana is an open company, but open doesn't just mean open source. Of course, 80% of our code is open source, but it also means we're transparent about our culture and operations, and we hope that this talk is an example of that. 

Today, we will share with you a few real incidents that we had in Grafana Cloud, some lessons that we learned the hard way, and how they shaped the way we've improved our databases. 

Okay, let's introduce ourselves. I'm Marty, an engineer and maintainer of Grafana Tempo, and Tempo is our distributed tracing database. 

- Hello, I'm Marco. I'm a Grafana Mimir maintainer. Similarly to Tempo, Mimir is a distributed time series database for metrics, supporting OpenTelemetry and Prometheus metrics. Both databases are open source, and they share the same architecture, designed to run at a massive scale. However, these databases are also complex, and sometimes they can fail in unexpected ways. 

Today, we will be very open with you and share some real incidents we had and what we learned from them. The first case we want to show you is what we call the "query of death." Let me introduce it with a real incident we had in March 2023, about three years ago. This was our largest Mimir cluster at that time. At some point, several alerts fired: the ingestion path was down, queries were failing, and we were experiencing high latency. 

We took a look at the cluster and noticed that the ingester CPU was maxed out. The Kubernetes nodes where these ingesters were running had their CPU saturated. Even worse, the garbage collector couldn't keep up, and one after another, the ingesters went down due to out of memory errors. 

Now, a quick refresher on the Mimir architecture: the ingester is a stateful component that holds the most recent metrics received before they are available for querying through the object storage. In the old architecture, which we were running in 2023, the write path (the ingestion path) was directly writing into the ingesters. When a query came in, the querier was querying the most recent data from the ingesters and the older data from the object storage through the store gateways. This meant that with the old architecture, if the ingesters were down or unavailable, both the ingestion and the read path were unavailable at the same time. 

Now, back to the incident. The symptoms were clear: ingesters were somewhat overloaded, but the root cause was still unknown. We grabbed the CPU profiles and noticed something unexpected: the regular expression engine was consuming all CPU and memory. Regular expressions are used by some PromQL label matchers, so we do expect to run the engine in the ingesters during the index lookup phase, but we didn't expect the engine to take all CPU and memory. 

Since they are used in queries, we checked the in-flight queries through the logs and found that a customer was running a bunch of queries with very long regular expressions—about 40 kilobyte regular expressions in each query. To try to stop the bleeding, we blocked this query and immediately contacted the customer. But unfortunately, the system did not recover. It turned out the problem was even worse. When one of those queries was canceled or timed out, the regular expression engine was still running under the hood inside the ingester process until all the label values were checked. 

The fix was easy: just periodically check for cancellation. But I'm showing you the screenshot of the real code as an example of an edge case that we hadn't considered. When we built these four-line for loops, we hadn't considered that there could have been an edge case where this for loop would take 15 minutes to run instead of 15 milliseconds. 

After stopping the bleeding by blocking the queries and fixing this bug, we started working on longer-term improvements. Here are the most significant ones:

- First of all, we introduced what we call regular expression unrolling. The core idea is that many regular expressions can be rewritten as simpler operations, like a set of equality matchers, prefix matchers, suffix matchers, and so on. We support many of them. When a regex is unrolled, we can completely skip the regex engine. This both makes the index lookup faster and reduces resource utilization. Just to give you a rough idea, in Grafana Cloud, nowadays, 97% of the regular expressions used in PromQL completely skip the engine, thanks to the unrolling.

- Second, we introduced a cost-based planner. Nowadays, when a query is executed, we evaluate the cost of each label matcher in the query and run the cheapest but most selective ones first. The remaining matchers, like complex regular expression matchers, are typically evaluated as a filtering step in a later stage. The main difference is that the set of values against which we evaluate these complex regular expressions is much smaller, thanks to the lazy label matchers.

- We also introduced an overload protection mechanism. The ingesters continuously monitor their CPU and memory utilization and can reject queries if they are overloaded. The core idea is that rejecting queries for a short period of time is better than having ingesters go out of memory, from which it takes longer to recover.

But this was not a one-off incident. Back in 2023, we saw multiple incidents caused by the query of death. The actual issue was that when the ingesters were overloaded, both ingestion and the query path were down at the same time. Ideally, queries should never be able to take down ingestion. 

So, Marty, what did we do? 

This led us to take a bigger change. What we needed was a new architecture that had stronger isolation guarantees. In both the 3.0 releases of Mimir and Tempo, that's what we're introducing: a new Kafka-based architecture that completely decouples ingestion from the read path. As we saw in that previous incident, a burst of queries can no longer take down ingestion, and vice versa. 

In the 3.0 releases, in this new architecture, there are just two dependencies: object storage (the same as before) and also Kafka, or any Kafka-compatible backend. In Grafana Cloud, we use WarpStream, which is a cloud-native Kafka implementation. 

Okay, so now here's another story. This time involving Tempo and what we thought were tiny traces. This story begins with an alert in one of our cells: queriers are running out of memory and OOMing, and requests are failing—not just a little, but a lot. 

At first glance, we're not sure what the problem is. The request rate is typical, and ingestion hasn't changed. Because queriers are crashing, they're taking down a lot of concurrent requests, making it hard for us to pinpoint the problem. However, it looks like trace lookups are failing more than other read requests, so that's where we focus our attention. 

We have to dig a little bit deeper. We are able to get a memory profile off of a querier in the few moments before it OOMs. What we see are large memory allocations reading the Parquet dictionary. Our first thought was that maybe these are very large traces or something like that. But when we pick out some traces that are failing every time and start digging into it, we find the opposite: it's actually very small, only about 500 spans. 

What we also didn't expect is that this small trace wasn't received in a short period of time; it had actually been trickled in just a few spans at a time over seven days. So it wasn't written to just one Parquet file in object storage like usual, but actually many files over the seven days. 

And so this still didn't explain why the memory allocation was so high. We knew where and how, but it's still not the why. So we had to dig a little bit deeper. We get one of those traces that's failing every time, and...

we start digging a little bit deeper. But to take a step back, actually, to talk about dictionary encoding, it's pretty common in columnar formats. And it's what we use in Parquet. The way it works is that to read the row in green, we first have to unpack the dictionary at the top of the column, and then we are able to extract the value referenced by that row. Normally, they're very small and efficient, like this, but when we focused on one of those traces that was failing every time, we started to see the real answer. This trace had very large and high-cardinality JSON attached to it. It wasn't just this trace; virtually the entire workload was following this pattern of trickling spans in with large JSON over days at a time. 

Putting it all together into storage had actually created huge dictionaries in every block. So, to read just one of those tiny traces, we had to unpack gigabytes of dictionaries in memory. That was the real source of the OOMs. The steps that we took to fix it included blocking some of the most failing queries. We had some tunables on the server side, so we could adjust concurrency to spread out the memory allocations and reduce the OOMs. This helped address a lot of OOMs. However, this incident showed that we had an area in Tempo that was completely undefined. There was no limit to how long an attribute could be, and Tempo had no protection from this write pattern. 

So, we introduced an attribute length limit, and everything longer than that is truncated. This has the intentional side effect of keeping the dictionary small. While these changes helped stabilize things, they weren't a great answer. Limiting data isn't what we really want to do. What we really wanted was to support the large attributes and this workload. Therefore, we needed to change the way we store the data. 

In Tempo 3, we have a new block format still based on Parquet, an evolution of our format, that gives us more precise control over the dictionary usage on a per-attribute basis. For the types of traces that we saw in this incident, we're seeing good results: a 95% memory reduction on those lookups. This would have prevented that incident. It also has other benefits, such as reducing the amount of overread from object storage, because we're no longer having to read those large dictionaries containing unrelated values. The real goal, finally, is that we want to support that workload, which will allow us to greatly raise that attribute length limit.

Now, back to Mimir. The third and last case we want to show you involves an incident where a few slow queries ended up slowing down many fast queries. Like most incidents, it started with an alert firing. In this case, a specific customer was experiencing very high query latency. We started digging into it and found that most of the queries were not slow because of execution; they were slow just because they were waiting in a queue, specifically the query scheduler queue.

Now, a quick refresher: the query scheduler is a component that holds a per-tenant queue with all the queries that need to be executed and dispatches these queries to the queriers for execution. When the querier executes a query, the data can come from two different places: the ingesters, which hold all the most recent data, or from the object storage through the store gateways, where we store all the longer-term data. Depending on the query, it may just hit the ingester, just the store gateways, or both of them. Typically, the majority of the queries just hit the ingesters.

Back to the incident. We found that a small number of queries, the ones hitting the store gateways, were actually slow. The other queries, the ones hitting the ingesters, were fast, but they were stuck in the query scheduler queue. Why? At that time, the query scheduler had a per-tenant, first-in-first-out queue. We did have fairness across different tenants, but within a single tenant, every query was treated the same. 

Imagine what happens: a slow query enters the system and occupies one query worker for that specific tenant. Then we have a bunch of fast queries that get executed quickly, but then another slow query comes in and occupies another query worker. Gradually, these slow queries, even if they are at a low rate, occupy all the query workers until all of them are occupied. When the next query comes in, it gets stuck in the queue waiting for a free worker to be executed, even if that query execution would be fast. 

This was not an isolated case; we've seen the store gateways slowing down all the queries multiple times. So, what did we do? First of all, we redesigned the query scheduler queue and introduced a multidimensional queue. The core idea is to split the per-tenant queue in the query scheduler into multiple lanes, depending on which Mimir component the query will hit under the hood: just ingesters, just the store gateways, or both of them. This was a very simple change but had a significant impact. Slow store gateway queries, after this change, were not able to slow down fast ingester queries anymore.

But there's more to why the store gateways were slow. There were multiple reasons that we addressed over time, but in this presentation, I want to focus on two of them. First, the store gateways used an on-disk cache loaded using memory mapping. When we built it, we didn't know, but we learned the hard way that in Golang, the language we use for our databases, when data is loaded using memory mapping from disk, and a page fault is triggered by the kernel to load the data from disk into memory, the Go processor responsible for running the goroutines gets stuck until the page fault is executed. 

We didn't notice this at a small scale; a low rate of page faults doesn't even register. But at a large scale, this became a real problem because the process was stuck or hanging from time to time, even if for very short periods, which increased the latency. Second, store gateways and queriers were buffering all the data in memory before sending anything back to the client. This had two consequences: high memory utilization peaks, and sometimes store gateways going out of memory; and slow queries, especially for high-cardinality queries.

So, what did we do? As you can guess, we got rid of memory mapping and replaced the cache with direct disk I/O syscalls. More importantly, and way more complex, we redesigned the Mimir query engine from scratch. This took a huge effort. The new Mimir query engine is streaming-based. The data is streamed from the object storage or the cache to the store gateways, and the store gateways stream the data to the queriers. The queriers run the new memory query engine that processes the query in a streaming way as the data arrives. 

The query is evaluated while we still read the data from disk. The same happens for the data coming from the ingesters. The ingesters stream the data to the queriers, feeding this data into the query engine. Nowadays, with Mimir 3.0 and the new Mimir query engine, the data is not fully loaded into memory anymore at query time; it gets processed gradually. This reduced resource utilization both in the store gateways and queriers, but even more importantly, it significantly reduced the query latency for long time range queries or high-cardinality queries.

Marty: Okay, we have walked you through a few incidents here and how we handled them and the improvements that came out of them. In hindsight, some of this might seem obvious, but the truth is that it's hard to predict where things will break. And when you're creating...

Something new: you can't prevent unknown unknowns. There will just have to be some lessons you learn the hard way. However, there are steps you can take to help yourself.

In the design phase, focus on isolation and a smaller blast radius. The new architectures that we've introduced to each database are a good example of this, as they totally decouple the read and write paths.

At Grafana, we strive to have a healthy on-call process. This philosophy is encapsulated in the idea of "You build it, you run it." The same engineers who create the databases are also the ones running them in the cloud. We have a follow-the-sun rotation and no competing priorities. It’s not just encouraged; on some teams, it’s the rule that when you're on call, project work stops.

In the short term, when an incident does happen, try to have a lot of tools in your toolkit that you already know how to use. Things like runbooks and scripts eliminate guessing when something's on fire. Additionally, try to build mechanisms that you can use to stop the bleeding, such as feature flags, circuit breakers, or the ability to block problematic queries.

In the long term, keep asking questions until you get down to the real root cause and deeply understand what happened. Use those learnings to continuously improve the system. This is how we've shaped our databases here at Grafana and how we run them in Grafana Cloud. Thank you. (audience applauding)

## Raw YouTube Transcript

- Hi, hello. Welcome. First, I would like to
start with a little preface. Grafana is an open company, but open doesn't just mean open source. Of course, 80% of our code is open source, but it also means we're transparent about our culture and operations, and we hope that this talk
is an example of that. And today, we will share
with you a few real incidents that we had in Grafana Cloud, and some lessons that
we learned the hard way, and how they shaped the way
we've improved our databases. Okay, let's introduce ourselves. I'm Marty, an engineer and
maintainer of Grafana Tempo, and Tempo is our distributed
tracing database. - Hello, I'm Marco. I'm a Grafana Mimir maintainer. Similarly to Tempo, Mimir is a distributed
time series database, so for metrics, supports OpenTelemetry
and Prometheus metrics. Both databases are open source, and they share the same architecture, and they've been designed
to run at a massive scale. But these databases are also complex and sometimes they can
fail in unexpected ways. Today we will be very open with you and we will share with you
some real incidents we had, and what we learned from them. The first case we want to show you is what we call the query of death. Let me introduce it with a real incident we had in March 2023, about three years ago. This was our largest Mimir
cluster at that time. At some point, several alerts fired. The ingestion path, down, queries failing,
experiencing high latency. We take a look at the cluster and we notice that the
ingester CPU is maxed out. The Kubernetes nodes where
these ingesters were running have the CPU saturated. Even worse, the garbage
collector can't keep up, and one after another one the ingester goes down, out of memory. Now a quick refresher of
the Mimir architecture. The ingester is a stateful component that holds the most
recent metrics received before they are available for querying through the object storage. In the old architecture, the
one we were running in 2023, the write path, the ingestion path, was directly writing into the ingesters. And then on the read path,
when a query came in, the querier was querying the most recent data from the ingesters and the older data from the object storage through the store gateways. This means that with the old architecture, if the ingesters were down, unavailable, both the ingestion and the read path was unavailable at the same time. Now, back to the incident. The symptoms of this incident were clear, ingesters were somewhat overloaded, but the root cause was still unknown. So we grabbed the CPU profiles and we notice something unexpected. The regular expression engine is consuming all CPU and memory. Now regular expressions are used by some PromQL label matchers, so we do expect to run the
engine in the ingesters during the index lookup phase, but we don't expect the engine
to take all CPU and memory. Since they're used in queries, we check the in-flight
queries through the logs and we find that a customer
is running a bunch of queries with very long regular expressions each, about 40 kilobyte regular
expressions in each query. To try to stop the bleeding, we block this query and we
immediately contact the customer. But unfortunately, the
system does not recover. Turns out the problem was even worse. When one of those queries were
canceled or was timing out, under the hood inside
the ingester process, the regular expression
engine was still running until all the label values were checked. Now, the fix was easy, just periodically
checking for cancellation. But I'm showing you the
screenshot of the real code, just as an example of an edge case that we haven't considered. When we built these four-line for loops, we haven't considered that there could have been an edge case where this for loop would've
taken 15 minutes to run instead of 15 milliseconds. So after stopping the bleeding
by blocking the queries and fixing this bug, we started working on
longer-term improvements. And these are the most significant ones. First of all, we introduced what we call regular expression unrolling. The core idea is that
many regular expressions can be rewritten as simpler operations, like a set of equality matchers, prefix matchers, suffix
matchers, and so on. We support many of them. When a regex is unrolled, we can completely skip the regex engine. This both makes the index lookup faster, but also reduces the resource utilization. Just to give you a rough idea, in Grafana Cloud, nowadays,
97% of the regular expressions used in PromQL completely skip the engine, thanks to the unrolling. Second, we introduced
a cost-based planner. Nowadays, when a query is executed, we evaluate the cost of each
label matcher in the query, and we run the cheapest but
most selective ones first. The remaining matchers, like complex regular expression matchers, are typically evaluated as a filtering step in a later stage. The main difference is
that the set of values against which we evaluate these
complex regular expressions is much, much smaller thanks
to the lazy label matchers. And we also introduced an
overload protection mechanism. The ingesters continuously monitor their CPU and memory utilization, and they can reject queries
if they are overloaded. The core idea is that rejecting queries for a short period of time is better than having
ingesters going out of memory from which it takes longer to recover. But this was not a one-off incident. Back in 2023, we have
seen multiple incidents caused by query of death. And the actual issue was that when the ingesters were overloaded, both ingestion and the query
path was down at the same time. But ideally, queries should never be able to take down ingestion. So Marty, what did we do? - This led us to take a bigger change. What we needed was a new architecture that had stronger isolation guarantees, and in both the 3.0
releases of Mimir and Tempo, that's what we're introducing, a new Kafka-based architecture that completely decouples
ingestion from the read path. So that, as we saw in
that previous incident that a burst of queries can
no longer take down ingestion, and vice versa. And in the 3.0 releases, in this new architecture there
are just two dependencies, object storage, the same as before, and also Kafka, or any
Kafka-compatible backend. And in Grafana Cloud we use WarpStream, which is a cloud-native
Kafka implementation. Yeah. Okay. So now here's another story. This time involving Tempo, and what we thought were tiny traces. And this story begins with
an alert in one of our cells. Queriers are running out
of memory and OOMing, and requests are failing,
not just a little, but a lot. And at first glance, we're
not sure what the problem is. The request rate is typical,
and ingestion hasn't changed. And because queriers are crashing, they're taking down a lot
of concurrent requests. So it's hard for us to
pinpoint the problem, but it looks like trace
lookups are failing more than other read requests. So that's where we focus our attention. And so we have to dig a little bit deeper. And we are able to get a memory profile off of a queriers in the
few moments before it OOMs. And what we see are
large memory allocations reading the Parquet dictionary. And our first thought was maybe
these are very large traces or something like that. But when we pick out some traces that are failing every time, and we start digging into
it, we find the opposite. It's actually very small,
only about 500 spans. And what we also didn't expect is that this small trace wasn't received in a short period of time, but it had actually been trickled in just a few spans at a
time over seven days. And so it wasn't written
to just one Parquet file in object storage like usual, but actually many files
over the seven days. And so this still didn't explain why the memory allocation was so high. We knew where and how, but
it's still not the why. So we had to dig a little bit deeper. So we get one of those traces
that's failing every time, and we start digging a little bit deeper. But to take a step back, actually, to talk about dictionary encoding, it's pretty common in columnar formats. And it's what we use in Parquet. And the way it works is
to read the row in green we first have to unpack the dictionary at the top of the column, and then we are able to extract the value referenced by that row. Normally they're very small
and efficient, like this, but when we focused on one of those traces that was failing every time, we start to see the real answer, which is that this trace had very large and high-cardinality
JSON attached to it. And it wasn't just this trace, but actually virtually the entire workload was following this pattern
of trickling spans in with large JSON over days at a time. And so putting it all
together into storage had actually created huge
dictionaries in every block. And so to read just one
of those tiny traces, we had to unpack gigabytes of
dictionaries in the memory. And that was the real source of the OOMs. So the steps that we took to fix it, first, we were able to block some of the most failing queries. We had some tunables on server side, so we could adjust concurrency to spread out the memory
allocations and reduce the OOMs. And this helped address a lot of OOMs. But this incident had actually shown that we had an area in Tempo
that was completely undefined. There was no limit to how
long an attribute could be, and Tempo had no protection
from this write pattern. So we introduced an
attribute length limit, and everything longer
than that is truncated. And this has the intentional side effect of keeping the dictionary small. But these help stabilize things, but they're not a great answer. Limiting data isn't what
we really want to do. What we really wanted to do was support the large attributes
and support this workload. So what we really needed to do was change the way we store the data. And that's what we've been working on. In Tempo 3, we have a new block format
still based on Parquet, an evolution of our format, that gives us more precise control over the dictionary usage
on a per-attribute basis. And for the types of traces
that we saw in this incident, we're seeing good results, 95% memory reduction on those lookups. And so it would've
prevented that incident. It also has some other benefits. It reduces the amount of
overread from object storage, because we're no longer having to read those large dictionaries
containing unrelated values. But the real goal, finally, is that we want to support that workload. So it will let us greatly raise
that attribute length limit. Cool. - Back to Mimir. Third, and last, case we want to show you. In this case, we had an incident
where a few slow queries ended up slowing down many fast queries. Like most of the incidents, it started with an alert firing. In this case, a specific customer was experiencing a very
high query latency. So we started digging into it, and we found out that most of the queries were not slow because of execution. They were slow just because
they were waiting in a queue, specifically the query scheduler queue. Now a quick refresher, the query scheduler is a component that holds a per-tenant queue with all the queries
that need to be executed and dispatches these queries
to the queriers for execution. Then when the querier executes a query, the data can come from
two different places. The ingesters, that hold
all the most recent data, or from the object storage
through the store gateways where we store all the longer-term data. Depending on the query, a query
may just hit the ingester, or just the store
gateways, or both of them. Typically, the majority of the queries just hit the ingesters. Back to the incident. We find out that there's
a small number of queries, the ones hitting the store
gateways, were actually slow. The other queries, the
ones hitting the ingesters, were fast, but they were stuck
in the query scheduler queue. Why? At that time, the query
scheduler had a per-tenant, first-in-first-out queue. So we did have fairness
across different tenants, but within a single tenant, every query was treated the same. Imagine what happens, a slow query enters the system and occupies one query worker
for that specific tenant. Then we have a bunch of fast queries. They get executed quickly, but then another slow query comes in and occupies another query worker. Gradually, these slow queries, even if they are at a low rate, they occupy all the query workers until all of them are occupied. And then when the next query comes in, it'll just be stuck in the queue waiting for a free worker to be executed, even if that query
execution would be fast. And again, this was not an isolated case. Back in time, we've seen the
store gateways slowing down all the queries multiple times. So what did we do? Well, first of all, we redesigned the query scheduler queue, and we introduced a
multidimensional queue. The core idea is to split
the per-tenant queue in the query scheduler
into multiple lanes, depending on which Mimir component the query will hit under the hood, just ingesters, just the store gateways, or both of them. This was a very simple change, but with a significant impact. Slow store gateways
queries after this change, were not able to slow down
fast ingester queries anymore. But there's more why the
store gateways was slow, why back in time querying
the long-term data was slow. Well, there were multiple reasons that we addressed over time, but in this presentation, I
want to focus on two of them. First of all, the store gateways did
use an on-disk cache loaded using memory mapping. And when we built it, we didn't know, but we learned the hard
way that in Golang, the language we use for our databases, when data is loaded using
memory mapping from disk, and a page fault is
triggered by the kernel to load the data from disk into memory, the Go processor that's
responsible to run the goroutines gets stuck until the
page fault is executed. Now, we didn't notice
this at a small scale, low rate of page faults,
you don't even notice. But on a large scale, this
became a real problem. 'cause the process was stuck
or hanging from time to time, even if for very short periods of time, this was increasing the latency. Second, store gateways and queriers were buffering all the data in memory before sending anything
back to the client. This had two consequences. First of all, high
memory utilization peaks, and sometimes store gateways
going out of memory. Second, slow queries, especially for high-cardinality queries. So what did we do? Well, as you can guess, we
got rid of memory mapping, and we replaced the cache just using direct disk I/O syscalls. But more importantly,
and way more complex, we redesigned the Mimir
query engine from scratch. And this took a huge effort. The new Mimir query
engine is streaming-based. The data is streamed from the object storage or the
cache to the store gateways, and the store gateways stream
the data to the queriers, and the queriers run the
new memory query engine that processes the query
in a streaming way as well as the data arrives. So the query is evaluated while we still read the data from disk. And the same happens for the data coming from the ingesters. The ingesters stream the
data to the queriers, and they feed this data
into the query engine. So nowadays with Mimir 3.0, and the new Mimir query engine, the data is not fully
loaded into memory anymore at query time, but it gets processed gradually. This reduced the resources utilization both in the store gateways and queriers, but even more importantly, significantly reduced the query latency for long time range queries
or high-cardinality queries. Marty. - Okay, we have walked you
through a few incidents here and how we handled them and the improvements
that came out of them. And in hindsight, some of
this might seem obvious, but the truth is that it's hard to predict where things will break. And when you're creating something new, you can't prevent unknown unknowns. There will just have to be some lessons you learn the hard way. But there are steps you
can take to help yourself. And in the design phase, focus on isolation and
smaller blast radius. And the new architectures that we've introduced to each database is a good example of that, that totally decouples
the read and write paths. And on-call. At Grafana, we strive to
have a healthy on-call. And what this looks like is the philosophy of "You
build it, you run it." So the same engineers
creating the databases are also the ones running
them in the cloud. We have a follow-the-sun rotation, and also no competing priorities. So it's not just encouraged, but on some teams, the rule
that when you're on call, project work stops. And short term, when an
incident does happen, try to have a lot of tools in your toolkit that you already know how to use. Things like runbooks and scripts eliminate guessing when
something's on fire. And try to build mechanisms that you can use to stop the bleeding, like feature flags, circuit breakers, or being able to block
the problematic queries. And long-term. Keep asking questions until you get down to the real root cause, and deeply understand what happened. And use those learnings to
continuously improve the system. And this is how we've shaped
our databases here at Grafana, and how we run them in Grafana Cloud. Thank you. (audience applauding)

