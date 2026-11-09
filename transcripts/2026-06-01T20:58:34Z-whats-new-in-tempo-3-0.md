# What&#39;s New in Tempo 3.0

Published on 2026-06-01T20:58:34Z

## Description

Tempo 3.0 introduces a major architectural shift that decouples the read and write paths, with Kafka handling durability on the ...

URL: https://www.youtube.com/watch?v=JEOne1NHeyo

## Summary

The show is titled "What's New in Tempo 3.0," published on June 1, 2026. The speakers discussed the significant updates in Tempo 3.0, highlighting the new architecture that separates read and write paths, which enhances scalability and reduces storage overhead. Key features include the general availability of TraceQL metrics, improvements in trace redaction capabilities, and the introduction of new query operators. The migration from Tempo 2.x to 3.0 is facilitated by a dedicated guide and CLI commands. Overall, Tempo 3.0 aims to provide better performance and flexibility for users managing trace data.

Topics: Tempo 3.0, architecture changes, TraceQL metrics, trace redaction, migration guide.

## Chapters

00:00:00 Overview of Tempo 3.0 architecture changes
00:01:31 Using the Tempo CLI to redact trace data
00:03:07 Trace redaction in Tempo 3.0

# What's New in Tempo 3.0

Tempo 3.0 marks a major step for Grafana Tempo with a new architecture that separates reads and writes, TraceQL metrics hitting general availability, and improvements across the board, including trace redaction, new query operators, and lower storage overhead.

The biggest change in 3.0 is a new architecture that splits the read and write paths. Before this, ingesters sat in the middle of the system, and parts of reads and writes were tightly coupled. That made independent scaling harder and drove up storage overhead. Now they're separated.

On the write side, the distributor sends traces to Kafka, which handles durability, and the block builder consumes from Kafka and writes blocks to block storage. On the read side, the live store handles recent traces for low latency queries, while historical queries go against blocks and object storage. The new architecture writes blocks at a replication factor of one instead of three. This means that we have one copy instead of the old three, which is where the storage savings come from. Reads and writes are also now separate components, so you can scale them independently.

If you're running in monolithic mode, Tempo still runs as a single binary and does not require Kafka. We've created a migration guide as well as the Tempo CLI command to help you migrate from 2.x to 3.0.

TraceQL metrics is now GA in 3.0. You can generate ad hoc metrics directly from trace data at query time without pre-computing the specific metrics first. Just as a heads up, alerting on TraceQL metrics is still experimental.

Let's take a look at a couple of new features of Tempo 3.0. TraceQL metrics now also support comparison operators, so you can filter metric results directly in your query instead of scanning everything that comes back. For example, let's get the per second span rate for every service except for Tempo, all grouped by service name. We will be doing this using the single binary example that is in the Tempo repo. I've only been running this for a few minutes, so I'm just going to go for the last five minutes and then we can see how this looks here.

If I instead want to use the comparison operator and get the services that are sending more than one span per second, I can just do greater than one and then run that query. We can see very visually here that we are getting something different from this.

Trace data can contain sensitive information, and sometimes you need to remove it without waiting for retention to expire. The new Tempo CLI Redact commands let you do that by submitting a job to rewrite the flick blocks and object storage. 

If we go to search, I'm just going to pick a service that I have running here and then pick this trace that we have. If I go ahead and copy the Trace ID, I have this command here. Since I'm running everything inside of a Docker compose, I'm just using Docker to run the Tempo CLI. So then it's just `redact`. I give it the tenant, which in this case is single tenant, the trace ID that we're looking at, and then the container name that we have here. 

When I run that, we can see that there are four jobs that were created. If we check the status of the backend scheduler and refresh, we can actually see those four jobs there. If we go over to Prometheus, you can see this. I ran this beforehand. We can just have the compaction, and if I refresh that, we can see that we have the redaction as well. Some of these things can take a little bit of time. It's adjustable for how quickly you can see it over in the backend, and then it'll take time for the trace to actually be redacted.

Now we can do a curl for the trace that we have, and we can see that it's not there anymore. If we go back over to Tempo, I can just refresh it or copy the ID there, and we can see that it's gone. If I want to close it, I can go to TraceQL, put in the ID, and it says that it's not found. So as expected, it is redacted.

If you're interested in seeing anything more with Tempo 3.0, please check out the blog, the release notes, and the change log, as well as the code if you're interested.

## Raw YouTube Transcript

Tempo 3.0 marks a major step for Grafana
Tempo with a new architecture that separates reads and writes, TraceQL
metrics hitting general availability, and improvements across the
board, including trace redaction, new query operators and
lower storage overhead. The biggest change in 3.0
is a new architecture that
splits the read and write paths. Before this, ingesters sat in the middle of the
system and parts of reads and writes were tightly coupled. That made independent scaling harder
and drove up storage overhead. Now they're separated. On the write side,
the distributor sends traces to Kafka, which handles  durability, and the block builder consumes from
Kafka and writes blocks to block storage. On the read side, the live store handles recent traces
for low latency queries while historical queries go against blocks
and object storage. The new architecture writes blocks at
replication factor of one instead of three. So that means that we have
one copy instead of the old three, which is where the storage savings end
up coming from. Reads and writes are also now separate components so you
could scale them independently. If you're running monolithic mode, Tempo still runs as a single binary
area and does not require Kafka. We've created a migration guide as well
as the Tempo CLI command to help you migrate from 2.x to 3.0. TraceQL
metrics is now GA in 3.0. You can generate ad hoc metrics directly
from trace data at query time without pre-computing the specific metrics
first. So also just as a heads up, alerting on TraceQL metrics
is still experimental. Let's take a look at a couple
of new features of Tempo 3.0. TraceQL metrics now also
support comparison operators
so you can filter metric results directly in your query instead
of scanning everything that comes back. Let's get the per second span rate
for every service except for Tempo all grouped by service name. And we're going to be doing this using
the single binary example that is in the Tempo repo. I've only been
running this for a few minutes, so I'm just going to go for the last
five minutes and then we can see how this looks here. If I instead want to be using the
comparison operator and I want to get the services that are sending
more than one span per second, I can just do greater than one and then I can go and run that query and
then we can see very visually here that we are getting something
different from this. Trace data can contain
sensitive information and
sometimes you need to remove it without waiting for retention to expire. The new Tempo CLI Redact commands lets
you do that by submitting a job to rewrite the flick blocks
and object storage. So if
we just go and go to search, I'm just going to pick a service that I
have running here and then I'm going to go and just pick this trace that
we have here. So if I go ahead and copy the Trace ID, then
I have this command here. So since I'm running everything
inside of a Docker compose, I'm just using Docker to run the
Tempo CLI. So then it's just redact. I give it the tenant. So in
this case, it's single tenant. I have the trace ID that
we're just looking at and
then the container name that we have here. So I run that, we can see that there are
four jobs that were created. If we go and take a look here at
the status of the backend scheduler, if we refresh, we can actually
see those four jobs there. If we go over to Prometheus, you
can see this. I ran this beforehand. We can just have the compaction
and if I go just and refresh that, then we can see that we have
the redaction as well. So some of these things can
take a little bit of time. It's adjustable for how quickly you can
see it over in the back end and then it'll take time for the trace
to actually be redacted. Now we can go and do a curl
for the trace that we have. So we can see that it's not there anymore. If we go back over to Tempo, I can just go refresh
it or copy the ID there. We can see that it's gone there.
If I want to go and close it, I can go to TraceQL and put it in the
ID and it says that it's not found. So as expected, it is redacted. So if you're interested in seeing
anything more with Tempo 3.0, please check out the
blog, the release notes, and the change log as well as
the code if you're interested.

