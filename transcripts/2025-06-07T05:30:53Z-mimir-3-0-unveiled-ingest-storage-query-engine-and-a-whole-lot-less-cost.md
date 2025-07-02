# Mimir 3.0 Unveiled: Ingest Storage, Query Engine, and a Whole Lot Less Cost

Published on 2025-06-07T05:30:53Z

## Description

Mimir 3.0 is coming—and it's faster, more cost effective, and more reliable. Learn how ingest storage and a new streaming query ...

URL: https://www.youtube.com/watch?v=yabtVakeqc8

## Summary

In this YouTube video, Jonathan, an engineer at Grafana Labs, presents an overview of Mimir 3, focusing on its new features aimed at improving reliability, performance, and cost-effectiveness. He highlights the transition from Mimir 2 to Mimir 3, explaining the challenges of the previous architecture and how the introduction of ingest storage using Kafka enhances scalability and resilience. Jonathan describes the new architecture's write and read paths, emphasizing how it decouples these processes for better performance. David follows up by discussing the Mimir query engine, which improves query execution efficiency and resource usage, showcasing its ability to handle larger queries with significantly reduced memory and CPU usage. The video concludes with a promise of these features being available later in the year, inviting viewers to engage with the team for further inquiries.

# Mimir 3 Presentation Transcript

Hello everyone. My name is Jonathan. I'm an engineer at Grafana Labs, and today we're going to be talking about Mimir 3. In particular, we'll discuss some new features that are coming later this year with Mimir 3. As usual, if you have any questions, you can add them to Slido, and we will answer them at the end.

The major themes of Mimir 3 revolve around **reliability**, **performance**, and **cost**. We'll hear quite a bit about how Mimir 3 improves cost throughout this talk. At Grafana Labs, we operate some of the largest Mimir clusters in the world, and we also work with customers, some of whom I’ve spoken to here, who operate very large Mimir clusters as well. We’ve taken what we’ve learned from those operational experiences and incorporated them into Mimir 3, which is coming later this year.

We’re excited to discuss some big new features that will be part of Mimir 3. The two features in particular that we’ll cover today are **ingest storage** and the **Mimir query engine**. 

But before we dive into the new features, I want to set the stage by discussing Mimir 2 so we can understand how it works as a baseline. 

## Mimir 2 Architecture

This is a high-level diagram of the Mimir 2 architecture. The way Mimir 2 works is through two different paths for request processing. On one path, write requests come into distributors. Distributors are responsible for taking a write request, inspecting the samples and values inside of it, breaking those apart, and forwarding them onto ingesters. Ingesters are responsible for indexing the data that comes into Mimir and making it available for querying later on.

Read requests come in through a separate path and eventually make their way to queriers. Queriers will query recent data from ingesters, aggregate the results, and send them back to clients. The main point to note about this architecture is that ingesters are central to everything. They sit in between both writes and reads, so we think of this architecture as having a write path and a read path, with ingesters playing a role on both.

This works most of the time, but occasionally, ingesters can become overloaded. This happens, for example, if we get a large burst of queries or if some very expensive queries come in. Those queries can put a lot of load on ingesters, and the load from the read path can impact ingesters' ability to serve the write path. This is one of the challenges with the current architecture.

### Write Path in Mimir 2

Taking a closer look at how the write path works today in Mimir 2, each sample from a write request gets replicated three ways for reliability. Each series and sample we receive are sharded by series ID, which helps determine which ingesters we should forward the series to for storage. We attempt to replicate each sample to three ingesters. Once we’ve heard from two of those ingesters that the sample was stored successfully, we consider the request to be successful and respond to the client.

### Read Path in Mimir 2

The read path is somewhat similar in that queriers look up series on some ingesters. If a query is interested in some series, it shards the series IDs to figure out which ingesters the data lives on. It queries up to three ingesters and looks for a response from two out of three. Once it receives a successful response from two out of three, we consider the query complete and respond to the client. 

By using a majority on both the write and read paths, we ensure that our data is stored across multiple nodes in case of failure, and we can also ensure a complete set of data on the read path.

### Multi-Zone Replication

Things get more interesting when we spread data across multiple zones. Mimir has the ability to spread ingesters across multiple availability zones to provide better availability. If we lose one zone, having additional zones allows us to keep serving data. However, if ingesters are unhealthy in more than half of the zones, our read path would become unhealthy. This is a challenge with the current Mimir 2 architecture.

## Mimir 3 Overview

Now that we've seen how Mimir 2 works, let’s talk about Mimir 3, starting with ingest storage. The goal of ingest storage is to provide better scalability and resilience than we saw with Mimir 2. Ingest storage starts with Kafka, which is central to both the read and write paths in this architecture.

In this new setup, distributors still handle write requests, but instead of forwarding write data to ingesters, they write to Kafka. Ingesters, which were previously central components, now become read path-only components. They consume data from Kafka. Querier functionality remains the same, but the big change is that Kafka allows us to decouple the read and write paths, enhancing resiliency compared to Mimir 2.

In Mimir 2, ingesters had the added responsibility of building large blocks and periodically uploading them to object storage. With the ingest storage architecture, we move that responsibility to a separate component, allowing us to scale those components based on their unique loads.

### Kafka API and Alternatives

While this architecture introduces a Kafka dependency, it’s actually a dependency on the Kafka API. At Grafana Labs, we use WarpStream in place of Kafka, which is a Kafka API-compatible cloud service backed by object storage. You can use Kafka, WarpStream, Redpanda, or any other Kafka API-compatible service with Mimir and ingest storage.

One of the significant benefits of this architecture is that when the read path becomes unhealthy, the write path remains healthy. This is a huge advantage of the new architecture that leverages Kafka.

### Write and Read Path in Mimir 3

Starting with the write path, distributors are still responsible for distributing series, but they now write to Kafka partitions instead of sending samples to ingesters. Each sample is sharded by its series ID to determine which partition to write to, and we only need to write to one partition one time. This differs from Mimir 2, where we wrote to a majority of ingesters. Kafka ensures data availability later on the read path.

In the read path, each ingester consumes from one Kafka partition. You can have multiple partitions or ingesters consuming from the same partition for high availability. With ingest storage, querying a single ingester in each partition provides a complete set of data, making the quorum size effectively one. For high availability, we only need two ingesters.

### Enhanced Availability

This new approach to replication and availability is much stronger. The likelihood of a read path outage is significantly lower, and you can further reduce that probability by creating more partitions. You control the number of partitions you create, which can be dozens or hundreds. 

This leads to a comparison of the outage probability in Mimir 2 versus Mimir 3 with ingest storage. While Mimir 2 shows a quick increase in outage probability with failing ingesters, Mimir 3 maintains a low probability of outage, even with fewer ingesters. This improvement not only enhances availability but also translates into lower operational costs.

## Resource Usage and Cost

A chart comparing the resource usage of a Mimir 2 cluster that we migrated to Mimir 3 with ingest storage shows a decrease of 15% in total resource usage, factoring in the costs of running Kafka or WarpStream. With ingest storage, you can expect to be resource and cost neutral or see a cost decrease.

### Transition to Mimir 3

In summary, ingest storage is a new architecture option in Mimir 3 that provides better efficiency and resource usage compared to Mimir 2. Next, I’m going to hand it over to David, who will discuss some other Mimir 3 features.

---

## Mimir Query Engine

Okay, how's it going everyone? I’m David, and I'm going to talk about the Mimir query engine, which is a foundational feature in Mimir 3.0. It brings a lot of improvements to analysis power, reliability, and cost. 

### Analysis Power

As Jonathan mentioned, we run some very large Mimir clusters. We often have to answer detailed questions about these clusters, such as the average CPU usage across the entire cluster. This kind of query can potentially touch tons of data, and when dealing with millions of containers, we can run into errors like the "chunks limit error." 

As engineers, we prefer to see such queries processed without destroying the system, allowing us to provide results instead of running into roadblocks.

### Memory Management in Mimir 2

Running a Mimir cluster involves managing resources effectively. In Mimir 2.0, we noticed that memory usage was highly variable, leading to overscaling and wasted costs. If we exceed a certain memory threshold, we risk being killed by Kubernetes, which results in errors for our customers. 

The motivation behind the Mimir query engine is to flatten these spikes in memory usage significantly, allowing us to reduce costs and enable more extensive data analysis.

### Query Execution in Mimir

Mimir is built on top of Prometheus, and prior to Mimir 3.0, it used the Prometheus query engine for executing queries. However, when queries load massive amounts of data, the Prometheus query engine uses a lot of memory.

For example, the Prometheus query engine would fetch all the `disk_used_bytes` data, which could lead to significant memory spikes. In contrast, the Mimir query engine processes queries as streams of series. This means it can keep peak memory usage low by only looking at a small window of data at any given time. Our benchmarks show a 92% reduction in memory usage and a 38% increase in execution speed.

### Benefits of the Mimir Query Engine

We didn’t just implement a single type of query; we’ve implemented 100% of the stable PromQL grammar. This means that complex operational queries will also benefit from streaming. 

Another optimization in the Mimir query engine is common sub-expression elimination, where it recognizes duplicate terms in queries and only fetches them once. This reduces load operations against the data plane, benefiting both efficiency and performance.

### Results and Savings

As we’ve enabled the Mimir query engine, we've observed significant results. While performance can vary based on the types of queries, we have seen a reduction in memory usage by 3x and an 80% decrease in peak CPU usage. 

When Mimir 3.0 launches this year, the Mimir query engine will be the default query engine, available in the open-source version of Mimir.

---

In conclusion, we’ve discussed ingest storage and the Mimir query engine, both of which contribute to better reliability, performance, and lower costs. We’re excited about bringing these enhancements to Mimir 3.0 later this year. Thank you for your attention, and come see us at Ask the Experts if you have further questions!

## Raw YouTube Transcript

Hello everyone. My name is Jonathan.
I'm an engineer at Grafana Labs, and today we're going to
be talking about Mimir 3. And in particular we're going to be
talking about some new features that are coming later this year with Mimir 3. As usual, if you have any questions, you can add them to the Slido and
we will answer them at the end. The major themes of Mimir 3
orient around a few things: reliability, performance, and cost. We're going to hear quite a bit about
how Mimir 3 improves cost throughout this talk. At Grafana Labs, we operate some of the largest
Mimir clusters in the world, and we also work with customers,
and I've spoken to some of you here, who also operate very
large Mimir clusters. And we've taken what we've learned
from those operations experiences and incorporated them into Mimir 3,
which is coming later this year. So we're excited to talk about some big
new features that are going to be part of Mimir 3. And the two features in particular that
we're going to be talking about today are ingest storage, and
the Mimir query engine. But before we talk about the new features, I want to set the stage by talking about
Mimir 2 so we can understand how it works as a baseline. So this is a high level diagram
of the Mimir 2 architecture. The way the Mimir 2 works is request
processing comes in two different paths. So on one path, write requests
come into distributors, and distributors are responsible
for taking a write request, inspecting the samples and values inside
of it and breaking those apart and forwarding them onto ingesters. Ingesters are responsible for indexing
the data that comes into Mimir and making it available for querying later on. Read requests come in through a separate
path and eventually make their way to queriers and queriers will query recent data
from investors and then aggregate the results and send it back to clients. The main thing to note about this
architecture is ingesters are central to everything. So ingesters sit in
between both writes and reads. So we think of this architecture as
having a wite path and a read path and ingesters play a role
on both of those paths. This works out most of
the time, this is fine, but occasionally ingesters can become
overloaded. This happens, for example, if we get a large burst of queries or if
we get some very expensive queries that come in, those queries can put a lot of load on
ingesters and the load from the read path from queriers can end up
impacting ingesters' ability
to serve the write path. And so this is one of the challenges
with the current architecture. Taking a look at how the wite path
works a little bit more closely today in Mimir 2, each sample from a write request gets
replicated three ways for reliability. When we look at each series
and each sample we receive, we shard the series id. So this is a way of figuring out
what we want to do with the series, and that helps determine which ingesters
we're going to forward the series onto, to store it on. We attempt to replicate
each sample to three ingesters. And once we've heard from
two of those ingesters, so two out of three that the
sample was stored successfully, then we consider the request to be
successful and we respond to the client. The way the read path works is a little
bit similar in that queriers are looking up series on some ingesters. So if a query is
interested in some series, it shards the series IDs to figure
out which ingesters the data lives on, and it'll query the data on up to three
ingesters and look for a response from two out of three ingesters
once it receives a successful
response from two out of three, so again, a majority, then we consider the query to
be complete and have all the data and the query will
respond to the client. By using a majority on both the
wite path and the read path, we're able to make sure that our data
is stored across multiple nodes in case there's a failure, but we're also able to make sure that we
have a complete set of data on the read path. Things get a little bit more interesting
when we spread data across multiple zones. So Mimir has this ability to
spread ingesters across multiple availability zones to
provide better availability. So in this diagram we can see
we have zones A, B, and C, and if we lose one zone, having additional zones or having your
ingesters spread across additional zones allows you to keep serving data,
write requests and read requests. But in this diagram you can see we have
an ingester that's unhealthy in zone A and an ingester that's
unhealthy in zone B. And when using multi-zone replication, availability becomes based on what is
going on with the majority of zones. And in this case, since the
majority of zones is unhealthy, our read path would actually be unhealthy. This is more likely to
happen in larger clusters, but it's something to be aware of
with the current Mimir 2 architecture. So now that we've seen a
bit about how Mimir 2 works, let's talk about Mimir 3 and we're
going to start by talking about ingest storage. So as I mentioned before, ingest storage is a new
architecture option, which
we're introducing in Mimir 3. And the goal of ingest storage is to
provide better scalability and resilience than we saw with Mimir 2. Ingest storage starts with Kafka. So Kafka is central to the read
and write paths in ingest storage. The way it works is distributors
as before still write data. So write requests come into distributors, but rather than forwarding
write data to ingesters, distributors are writing
to Kafka. Ingesters, as we saw before, we're
kind of a central component, but they move over and become
a read path only component. So ingesters consume data from
Kafka in this architecture. Queriers query from ingesters as they did before, but the main thing to note about
this architecture is Kafka allows us to divide and decouple the
read path in the write path, which provides better resiliency than
we've had with Mimir 2. And in Mimir 2, ingesters have an additional
responsibility of building
large blocks and a periodically uploading
them to object storage. In Mimir 3, with the ingest
storage architecture, we're able to move that responsibility
to a separate component. And being able to have these types of
responsibilities in individual components allows us to better scale those
components based on their unique loads, which is another benefit of
this architecture. Of course, this architecture does
mean that we have Kafka, but it's not actually Kafka that
we depend on, it's the Kafka API. At Grafana Labs, we've talked about how
we use WarpStream in place of Kafka. So we've written about our usage of
WarpStream on our engineering blog. WarpStream is a Kafka API compatible
cloud service that's backed by object storage. So we use this in place of
Kafka and it's worked really well for us. But the key thing to note about this
Kafka dependency is, like I said, it's a dependency on the Kafka
API. So you can use Kafka, you can use WarpStream, you can use
Redpanda, you can use some other Kafka, API compatible cloud service,
whatever works for you, you can use it in Mimir
with ingest storage. As we saw before, one of the downsides of the current
architecture is when the read path becomes unhealthy, the wite
path could be impacted. But this slide kind of just illustrates
how when the read path becomes unhealthy, like when I
ingesters become overloaded, which can happen occasionally in large
clusters, the wite path is still healthy. And so this is a huge benefit of the
current architecture by using Kafka. So I want to look at what
the new architecture looks
like a bit more closely. We're going to look at the wite path
and the read path in particular. So starting with the write path, distributors are still responsible
for distributing series as before, but rather than distributing
samples to ingesters, they're writing to Kafka partitions. So Kafka partitions are a way that
Kafka uses to divide data so that it can better scale its data processing and
storage internally. And they also allow us to better scale our read path
as we'll see in a little bit. Each sample that comes in gets sharded
by its series ID to figure out which partition to write to, and we only need
to write to one partition one time. So this is a little bit different than
how things work with a Mimir two where we wrote to a majority of ingesters. Kafka takes care of making sure that
the data is highly available later on, on the read path. One trade off with this approach is we
are waiting for response from Kafka from a distributor. So there can be increased latency on the
write path using this new architecture depending on which Kafka
implementation you're using. Like I mentioned before at Grafana
Labs in our cloud, we use WarpStream. WarpStream is backed by object storage. So depending on which Kafka
implementation you're using, you might have an additional latency
cost going round trip to something like object storage. Let's look
at how the read path works. So the read path is interesting. The way it works is one ingester
consumes from one partition. So each ingester consumes from
one and only one partition, a Kafka partition that is. But you can have multiple partitions or
multiple ingesters consuming from the same partition for high availability. So that way if one ingester goes down, you can still have another ingester
that's available and able to serve queries for some partition. The neat thing about Kafka and
partitions is that the ingesters consuming from a partition have a
complete set of the data. So with Mimir 2, we saw how a query needs to access
some series on a majority of ingesters or in a majority of
zones. But with ingest storage, you can get a majority or you can get
a complete set of the data by querying just a single ingester in each partition.
So the quorum size in other words, is one. By having a second ingester though
we can add high availability. So in order to have all the data, we
only need one ingester per partition. And for high availability,
we only need two ingesters. And this availability approach by using
partitions is actually much stronger as we'll see in a moment. To better
illustrate what the availability looks like, earlier we saw how with
multi-zone replication in Mimir 2, if you have ingesters
unavailable in a majority of zones, then your read path would be
unhealthy. But with ingest storage, you can actually have ingesters
that are unavailable in each zone. You can have ingesters that are
unavailable in each partition. As long as you have one ingester
available in each partition, your read path is still healthy. So this approach to replication and
availability is much more resilient, and the probability of a read
path outage is much lower, and you can decrease the probability
of a read path outage by creating more partitions. And you can control
how many partitions you create. You can create dozens or hundreds, and this chart shows what the
probability of an outage looks like. So this chart is comparing the
probability of a read path outage in Mimir 2, which is the blue line
compared to Mimir 3 with ingest storage. As some number of
ingesters start to fail, along the bottom X axis, you can see the probability of a Mimir
2 outage can increase quite quickly. But with Mimir 3, with ingest storage, we can lose lots of ingesters and the
probability of a read path outage stays quite low. So this is due to the fact that we're
consuming from partitions and I ingesters have a more complete set of
the data than they had before. So this is a huge benefit
of the new architecture. But something else that's interesting
about this is it's actually not an apples to apples comparison because this chart
shows the probability of an outage using Mimir 2 with three zones worth
of ingesters. But in Mimir 3, the data that feeds this chart is only
running two zones worth of ingesters. So we're running a third fewer
ingesters and we have massively better availability. This is a huge benefit of
the new architecture and
something we're really happy about. As you can imagine, running fewer ingesters also
translates into lower costs. So this is a chart that shows the resource
usage of a Mimir 2 cluster that we migrated to a Mimir 3 with ingest storage. And this is one of our larger
clusters. And as you can see, the total resource usage, so this takes into account
CPU and object storage costs, decreased by 15%. This takes into account the additional
costs for us to run and use Kafka or using WarpStream in our case.
But even factoring in that cost, we're able to run fewer ingesters,
which more than offsets the cost. And we expect that when
using ingest storage, you'll either be resource and cost
neutral or see a cost decrease. So to recap, ingest storage is a new architecture
option coming in Mimir 3. It helps provide better efficiency and
resource usage than you had in Mimir 2. And next I'm going to
hand it over to David, who's going to talk about
some other Mimir 3 features. Okay, how's it going everybody? I'm David. I'm going to be talking
about the Mimir query engine, which is a new foundational
feature in Mimir 3.0. It provides a lot of new
improvements to analysis power, reliability, and cost. Who
cares about cost? Anybody? Okay, shout out to cost. All right, first I'm going to talk
about the analysis power. So Jonathan said we run some very
large Mimir clusters. This is true. We are frequently asking pointed
questions about these clusters, the huge numbers of pods, the
huge numbers of disks, and so on. I know you all are interested in your
huge numbers of volcanoes and cars and stuff like that. Here is a
question I asked last week: What's the average CPU
usage in the entire cluster? So this kind of query has a simple result, but it can potentially touch tons of data. And what happens sometimes when we
have like 10 million containers? Unfortunately, you can run into an error like this. Anyone's seen this error
before? The chunks error,
the chunks limit error? Okay, good. So if you're trying to do analysis, this is a roadblock for me. I have to figure out how to constrain
my query to get it to work or issue three smaller queries and
scotch tape them together afterwards. It's a bummer. As engineers, we would rather see this
query coming across and say, you know what? Yeah, that's
an expensive query, I can tell, but we're going to execute it anyway
without destroying the system, and we're going to give a
result back to the people. So I'm going to switch gears a little
bit and talk about the same problem, but from a different angle. And
that is running a Mimir cluster. No one in here runs a Mimir
cluster. I already asked a few, and I'm pretty sure no
one runs one. Am I right? Okay, I guess I'm right about that.
We run a bunch of Mimir clusters. Here is one of 'em, and
this is a Mimir 2.0 cluster. So this is actually a pool of querier
pods and the squiggly lines you see: it's memory usage. As you can see, the memory usage
is just kind of all over the place. So we have to tell Kubernetes
how much memory we want, and that's how much we pay for. So the bummer about this is most of the
time we're not using anywhere near that much memory. So we're kind of
just leaving cash on the table. And the other thing that's a bit
sketchy about this is if we go over the yellow line, we
can be killed by Kubernetes. We will issue errors to our
customers. We'll get paged. We try to stay out of the danger zone. So we have a couple knobs for
staying out of this danger zone. One of them is this dynamic you see, which is we're paying a bunch
of cash to be overscaled: we're wasting a bunch of money. And the other one is, well,
you've already seen that too. It's the error. So we put these limits in the
system to protect the system to keep from crashing. So we keep
from running out of memory. So if we could flatten these
spikes out significantly, we would stand to spend a lot less money. We could take that yellow
line and move it way down, and you folks issuing the queries could
do analysis that touches a lot more data. So that is the motivation
for the Mimir query qngine, and I'm going to tell you a
little bit about how it works. So Mimir is built on top of Prometheus. It largely strings together
Prometheus components to build a more scalable Prometheus. And one of the things it
does before Mimir 3.0 is use the Prometheus query
engine to execute queries. So the problem is when your queries
load massive amounts of data, the Prometheus query engine
uses massive amounts of memory. And I'm going to show you why the Mimir
query engine tends to be a game changer for these gigantic queries. So here's how it works, and here's how the Prometheus query engine
that we used in Mimir 2 would execute this example, query: sum over
disk_used_bytes. So the question is, how many disk_used_bytes are
we using in the entire cluster? So the first thing it does, it
says, okay, sum of disk_used_bytes? First thing I'm going to do is go
out and grab the disk_used_bytes. I'm going to go out to storage, fetch
'em, load 'em all up into memory, and it could be a massive
amount of data. It could be five gigs or whatever. This is the source of the memory spikes
that we saw on the previous slide. And once it's all loaded into memory, it sends it on over to the sum
operator and computes the sum easy. So I'm going to show you how the Mimir
query engine would execute the same query. And the big difference is we work
on streams of series this time. So the first thing we do:
sum of disk_used_bytes, go out and just get the first series, send it on over to the sum
operator and start a running tally. Go ahead and get the second
series, stream it over, and so on and so on until
you get the final result, which is the same that
Prometheus computed. So this massively reduces peak memory
usage because we're only looking at a small window of data at any given time, and we have a benchmark
that covers this exact query, and the results are pretty
staggering. We use 92% less memory, and we are 38% faster at
executing the same query. So I'm showing Thanos in here too.
They also improve upon Prometheus. They're a little bit faster than
us in the latency department. That's because they paralellize
more. We're not doing that yet. I think we might. Okay, cool. I like this chart even more. As we ratchet up the number of
series that we're pulling in, you can see Prometheus and
Thanos go linear with memory, and we're all in almost a
different algorithmic class here. We're using constant
memory. That's really cool. So we knew we were onto something
good with this query engine, so we didn't just implement summations. We have implemented a hundred
percent of the stable PromQL grammar. So that means not only does
that summation toy query work, but all these hairy operational
queries that exist in your runbooks and glue your system together, they also
get to take advantage of streaming. So that's streaming. That's not the
only feature of the Mimir query engine, by the way. I'm going to talk about this other type
of query that we see quite often at Grafana Labs. This is
a success rate query. You see it a lot in web apps. How many, what's the percentage
of succeeding requests? So the interesting thing about this query
is the success term appears multiple times. Actually, some of our clusters, 20% of the time is spent executing a
query that has the term in there twice. And let's add the data plane
into the mix and see how the Prometheus query engine
would execute this query. Success over success plus
failure. What do I do first? I'm going to go out
and grab success. Okay, next up success. What am I going to do? I'm going to go out again and
grab it from the data plane. And failure: I'm going to
go grab that too. Okay. It has loaded success multiple times.
It's the same data. It's not changing. So the Mimir query engine knows what's
going on here and identifies that that is a duplicate term in the query, and it goes and fetches
it one time instead. So it's a third less load
operations against the data plane, which reduces load on your
ingesters and store gateways. Okay? So this optimization is good. I
mean for you, compiler geeks or whatever, this is the common sub expression
elimination. It's a common optimization. We don't just implement this one. We actually implement an entire framework
where we can keep on adding these kinds of transformations and
optimizations over time safely. So if we return to our resource
hog query that I showed you before, we'll be more likely to get a result
like this instead of the scary error that we saw before. So as we've enabled the Mimir
query engine at Grafana Labs, I have some results to show you
about that. And the caveat is, if you know anything about Mimir, the performance of Mimir is highly
dependent on the kind of queries you're serving. So this is one favorable result. Your results could be a much better
or a little more mediocre or whatever, but see if you can discern when we
turned on the Mimir query engine. It's 3x less memory. We can take that yellow line from before
and ratchet it way down and just save a lot of memory, save a
lot of money right away, and so will you this year when
it comes out. And how about CPU? It's a similar story. 80% less peak CPU. CPUs are expensive. You'll be
able to save money there too. So when Mimir 3.0 drops this year, the Mimir query engine
will be the query engine. So you'll get it just by upgrading,
and it'll be in the open source Mimir. Okay, so we've talked
about ingest storage, we've talked about the Mimir query engine. Both of them conspire to bring you
better reliability, performance, and lower cost. So we're excited about getting these and
other enhancements to Mimir 3.0 in your hands later this year. Come see us at Ask the Experts. Some of you have others, should too.
Well, thanks a lot for the attention.

