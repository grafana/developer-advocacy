# How to Speed Up Grafana Dashboards 100x with ASAPQuery

Published on 2026-05-14T17:17:45Z

## Description

ASAPQuery drops into your existing Prometheus-Grafana stack as an open-source query accelerator, delivering near-instant ...

URL: https://www.youtube.com/watch?v=Y0ZtUhw5evc

## Summary

The show is titled "How to Speed Up Grafana Dashboards 100x with ASAPQuery," published on May 14, 2026. The speaker, Milind, a PhD student at Carnegie Mellon and lead of ProjectASAP, introduces ASAPQuery, an open-source query accelerator designed to enhance the performance of Grafana dashboards using a Prometheus-Grafana stack. ASAPQuery significantly reduces loading times and query costs by employing sketches, which are compact data structures that summarize large streams of data for efficient querying. Key takeaways include the ease of integrating ASAPQuery into existing setups without changing dashboards or queries, and its ability to provide near-instantaneous responses to queries. 

Topics: ASAPQuery, Grafana, Prometheus, query acceleration, sketches.

## Chapters

00:00:00 Discussion
00:04:01 Understanding sketches for efficient data summarization
00:07:04 Overview of ASAPQuery and its benefits

Right. Hey, everyone, it's great to be here. It's gonna be a quick 10-minute lightning talk, so let's get right into it.

Let's say you have your Prometheus-Grafana stack set up. You're trying to understand what's happening in your deployment. You're trying to monitor it, and then every time you open Grafana, every time you change a certain time range in the dashboard, you have to deal with this loading lag, right? As you increase the time range that you're querying, this lag is gonna get worse and worse. What if this is something that you didn't have to deal with? What if there's an alternative to this?

So, what I want you to do is pay close attention to that Refresh button on the top right. You just saw that? It was like an absolutely instant dashboard refresh. This is exactly what ASAPQuery does for you. It gives you orders of magnitude faster Grafana dashboards, and at the same time, it lowers your query costs.

So, I'm Milind. I'm a PhD student at Carnegie Mellon, and I lead ProjectASAP, which is a research effort towards rethinking and redesigning observability and analytics pipelines to make them cheaper and faster. ASAPQuery is one such research effort inside ProjectASAP, and that's what I'm here to show you today.

ASAPQuery is an open-source drop-in query accelerator that fits right into your existing Prometheus-Grafana stack. So, let's say this is what a typical deployment looks like. You have your exporters on the bottom left of the slide, and Prometheus is configured to scrape metrics from it regularly. Then you have a Grafana dashboard, which is continuously sending queries to Prometheus. ASAPQuery fits right into it like so. It intercepts the queries that are being sent from Grafana to Prometheus and is able to send answers blazingly fast back to Grafana. It implements the same query API that Prometheus does, so you don't really have to change anything in Grafana, except you point it to ASAPQuery.

ASAPQuery also needs a source of raw data, and the way that we do that is by configuring the `remote_write` configuration in Prometheus. For those of you who are not familiar, `remote_write` allows Prometheus to send whatever data it has just scraped to a remote endpoint, in this case, ASAPQuery's data ingest endpoint.

So, what's the secret sauce behind ASAPQuery? How is it able to give you these blazingly fast dashboards? The answer to this is something called sketches. 

Now, to explain the intuition behind sketches, let's forget about metrics for a second. Imagine you're on a safari in Africa, and you're seeing a bunch of different animals during your two to three-hour-long safari. At the end of the safari, a friend asks you a question: Did you see a giraffe or not? The usual way to answer this would be through exact query computation, where you try to keep track of each and every animal that you saw, and then at the end, you tell your friend, "Okay, I did see a giraffe." The problem is it's hard to keep track of so many animals in your head; you only have so much memory. This is an exact method, but it's costly.

The other option is to sample the data. You might say, "Okay, instead of keeping track of every animal, maybe I only keep track of every fifth animal." That makes sense; you can monitor a lot more animals, but then it's inaccurate because you might just miss a rare animal, like a giraffe.

The third option is something called sketches. Sketches are compact data structures that summarize a large stream of data, in this case, animals. I can keep this compact data structure, which is like a bit array with a few cells. Every time I see an animal, I can hash it to one of those cells and keep track of the animals that I've seen or not seen. These sketches are approximate summaries of our data, but they can be configured to answer queries really accurately, and at the same time, they consume orders of magnitude lower resources compared to keeping track of all the raw data.

The sketch I showed on the previous slide is called a Bloom filter. This sketch can answer a specific kind of query: "Did I see a particular item in a data stream or not?" But there are other kinds of sketches that can help you answer different kinds of queries, like "How many times did I see a particular animal or an item?" and "What are the top five animals that I saw?" Each of these sketches is purpose-built to answer a specific kind of query.

So, that works on animals. You can actually use the same techniques to monitor metrics instead of animals. Now, instead of animals, I have, let's say, a time series of CPU usage metrics, which is annotated with two labels: host and services. I can use these same purpose-built sketches to answer different kinds of queries, which are PromQL queries that people like to ask on Grafana dashboards, like "What's the average CPU usage across services?" or "What is the P90 CPU usage across hosts?"

These sketches are classical techniques from computer science research, but they're very hard to use. What we've done with ASAPQuery is essentially bridge the gap between these lower-level, cool algorithmic primitives and where observability is today. ASAPQuery brings the benefits of sketches to the world of metrics observability in the form of faster dashboards, as well as lower CPU and memory costs for queries, which ultimately reduces your infrastructure spend.

To give you a high-level overview of what ASAPQuery's architecture looks like, this is a high-level overview of what an existing Prometheus-Grafana stack is. As I said, ASAPQuery is just able to drop in as a query accelerator. 

The first module here is the `asap-planner`. This is the brains of the operation. The input to the `asap-planner` is the queries that Grafana is sending to Prometheus. It looks at the query workload, sees what kinds of aggregations are being used, how often the queries are repeating, what labels they are looking at, what the time range is, etc. It analyzes this query workload to compute a query plan, which essentially maps these high-level PromQL queries down to sketches.

This query plan is then executed by the next two modules in ASAPQuery. The second module is the `asap-sketch-ingest`. Whenever Prometheus pulls metrics and does a `remote_write` to ASAPQuery, the `sketch-ingest` module takes these metrics and computes sketches on them in a streaming manner at ingest time. This is done completely at ingest time before any queries are actually hitting Prometheus. These sketches are then sent to the third module, which is the `query-engine`. 

This `query-engine` sits between Grafana and Prometheus. It intercepts the queries, and when a query comes from Grafana, it uses the sketches that have been computed to quickly give you an answer to the query. In some cases, if ASAPQuery is not able to answer it because it's not supported by sketches right now, then ASAPQuery can actually just forward the query to Prometheus, which still has all of your raw data, and then send it back to Grafana.

All right, so let me show you a quick demo of ASAPQuery. This is the quickstart that you can run from the repository yourself. It's just a docker-compose command up there. This is a pre-configured Prometheus-Grafana setup that you have, and here, I'm just opening Grafana. I want to show you ASAPQuery versus Prometheus side-by-side. You see, ASAPQuery loads almost instantly while it...

Takes Prometheus a few seconds. Each row here is the same query that's being sent to ASAPQuery and Prometheus. Every time Grafana refreshes the dashboard and sends a query, Prometheus will take some time to load, while ASAPQuery is almost instant. So that's essentially the benefit that you get. You don't have to change your dashboard or rewrite your queries to use any of this.

All right, so that's basically what I wanted to show you. ASAPQuery is open source at that GitHub link. There's also a link to our website. Try out the quickstart. We're making some ease of use improvements to ASAPQuery so that it works without any manual configuration in your existing Prometheus-Grafana stack. We're also going to be writing some blog posts about sketches and about the internals of ASAPQuery.

So yeah, that's it. That's all I wanted to talk about. Come find me at the conference. You can send me an email or find me on LinkedIn if you have any questions, thoughts, or feedback. 

Yeah, that's it. Thank you. (audience applauding)

## Raw YouTube Transcript

- Right. Hey, everyone, it's great to be here. It's gonna be a quick
10-minute lightning talk, so let's get right into it. So let's say you have your
Prometheus-Grafana stack set up. You're trying to
understand what's happening in your deployment. You're trying to monitor it, and then every time you open Grafana, every time you change a certain
time range in the dashboard, you have to deal with this,
like, loading lag, right? And as you increase the time
range that you're querying, this lag is gonna get worse and worse. What if this is something that
you didn't have to deal with? What if there's an alternative to this? So what I want you to do
is pay close attention to that Refresh button on the top right. You just saw that? It was like an absolutely
instant dashboard refresh. So this is exactly what
ASAPQuery does for you. It gives you orders of magnitude
faster Grafana dashboards, and at the same time, it
lowers your query costs. So I'm Milind. I'm a PhD student at Carnegie Mellon and I lead ProjectASAP, which is a research
effort towards rethinking and redesigning observability and analytics pipelines to
make them cheaper and faster. And ASAPQuery is one such research effort inside ProjectASAP, and that's what I'm
here to show you today. So ASAPQuery is an open source
drop-in query accelerator that fits in right into your existing Prometheus-Grafana stack. So let's say this is what a
typical deployment looks like. So you have your exporters on
the bottom left of the slide, and Prometheus is configured to scrape metrics from it regularly, and then you have a Grafana dashboard, which is continuously sending
queries to Prometheus. So ASAPQuery fits right into it like so. It intercepts the queries that are being sent from
Grafana to Prometheus and it's able to send answers blazingly fast back to Grafana, and it implements the same
query API that Prometheus does, so you don't really have to
change anything in Grafana, except you point it to ASAPQuery. So ASAPQuery also needs
a source of raw data, and the way that we do
that is we configure the remote_write
configuration in Prometheus. So for those of you who are not familiar, remote_write allows Prometheus
to send whatever data it has just scraped to a remote endpoint, in this case, ASAPQuery's
data ingest endpoint. So what's the secret
sauce behind ASAPQuery? How is it able to give you
these blazingly fast dashboards? And the answer to this is
something called sketches. Now, to explain the
intuition behind sketches, let's forget about metrics for a second. Imagine you're on a safari in Africa, and you're seeing a bunch
of different animals as you're on your, you know, two to three-hour-long safari, right? And at the end of the safari, a friend asks you a question,
if you saw a giraffe or not. The usual way that you would
do this is this sort of notion of exact query computation, right, where you try to keep track of each and every animal that you saw, and then at the end you try
to, you tell your friend, "Okay, I did see a giraffe." And the problem is it's hard to keep track of so many animals in your head, right? You only have so much memory. And so, this is, it's an
exact method, but it's costly. The other thing that you could do is you could sample the data, right? So you're gonna say that,
"Okay, instead of keeping track "of each and every animal,
maybe I only keep track "of every fifth animal." All right, that makes sense. I can, you know, sort of
monitor a lot more animals, but then it's inaccurate, because you might just miss a
rare animal, like a giraffe. The third option here is
something called sketches. So sketches are these
compact data structures which summarize a large stream of data, in this case, animals. So I can keep this compact
data structure which only has, it's like a bit array with a few cells, and every time I see an
animal, I can hash it to one of those cells, and
keep track of the animals that I've seen or not seen. So these sketches are approximate
summaries of our data, but they can be configured to answer queries really,
really accurately, and at the same time, they consume orders of magnitude lower resources compared to keeping track
of all the raw data. Now, the sketch that I
showed on the previous slide is called a Bloom filter, and this is a sketch that can answer a specific kind of query, which is, "Did I see a particular item "in a data stream or not?" But there are other kinds of sketches that can help you answer other
different kinds of queries, like, "How many times did
I see a particular animal "or an item?" And, "What are the top
five animals that I saw?" So each of these sketches is purpose-built to answer a specific kind of query. So, all right, so that works on animals. You can actually then
use the same techniques to monitor metrics instead of animals. So now instead of animals, I have, let's say, a time
series of CPU usages, CPU usage metrics, which is annotated with, let's say, two
labels, host and services, and I can use these same
purpose-built sketches to answer different kinds of queries, which are PromQL queries, let's say, that people like to ask
on Grafana dashboards, like, "What's the average
CPU usage across services?" Or, "What is the P90
CPU usage across hosts?" So these sketches are
actually classical techniques from computer science research, but they're very hard to use. And so, what we've done with
ASAPQuery is essentially bridge the gap between these lower level, cool algorithmic primitives and where observability is today. So ASAPQuery essentially
brings the benefits of sketches to the world of metrics observability in the form of faster dashboards, as well as lower CPU and
memory cost for queries, which ultimately reduces
your infrastructure spend. So just to give you a high-level overview of what ASAPQuery's
architecture looks like, so this is, like, a high-level overview of what an existing
Prometheus-Grafana stack is, and like I said, ASAPQuery
is just able to drop in as a query accelerator. So the first module here
is the asap-planner. This is the brains of the operation. The input to the
asap-planner is the queries that Grafana is sending to Prometheus. So it looks at the query workload, it sees what kinds of
aggregations are being used, how often are the queries repeating, what labels are they looking at, what is the time range
they're looking at, et cetera, and it looks at, and it
analyzes this query workload to then compute a query plan, and a query plan essentially maps these high-level PromQL
queries down to sketches. So this query plan is then executed by the next two modules in ASAPQuery. So the second module here
is the asap-sketch-ingest. So whenever Prometheus pulls metrics and it does a remote_write to ASAPQuery, the sketch-ingest modules
takes these metrics and computes sketches on
them in a streaming manner at ingest time. So this is done completely at ingest time before any queries are
actually hitting Prometheus. And then these sketches are
sent to the third module, which is the query-engine. And this query-engine sits
between Grafana and Prometheus. This is the query-engine that's actually intercepting the queries, and when a query comes from Grafana, it uses the sketches
that have been computed to quickly give you an
answer to the query. And in some cases, if
ASAPQuery is actually not able to answer it, because
it's, you know, not supported by sketches right now, then ASAPQuery can actually
just forward the query to Prometheus, because
Prometheus still has all of your raw data, and then sort of send it back to Grafana. All right, so let me show you
a quick demo of ASAPQuery. So this is the quickstart that you can run from
the repository yourself. It's just a docker-compose
command up there. So this is a pre-configured
Prometheus-Grafana setup that you have, and here,
I'm just opening Grafana, and I want to show you ASAPQuery versus Prometheus side-by-side. So you see, ASAPQuery
loads almost instantly while it takes Prometheus a few seconds. So each row here is the
same query that's being sent to ASAPQuery and Prometheus, and then every time Grafana
is refreshing the dashboard and sending a query, Prometheus will take some time to load while ASAPQuery's almost instant. So that's essentially
the benefit that you get, and you don't have to
change your dashboard, you don't have to rewrite your
queries to use any of this. All right, so that's basically
what I wanted to show you. ASAPQuery is open source
at that GitHub link. There's also a link to our website. So try out the quickstart. We're making some ease of use
improvements to ASAPQuery, so that it's, you know, it works without any manual configuration in your existing Prometheus-Grafana stack, and we're also gonna be
writing some blog posts about sketches and about
the internals of ASAPQuery. So yeah, that's it. That's all what I wanted to talk about. Come find me in the conference. You can send me an email or find me on LinkedIn if
you have any questions, or thoughts, or feedback. Yeah, that's it, thank you. (audience applauding)

