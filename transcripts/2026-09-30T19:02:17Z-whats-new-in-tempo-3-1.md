# What&#39;s New in Tempo 3.1

Published on 2026-09-30T19:02:17Z

## Description

Tempo 3.1 is here. This release adds query-based trace redaction, arithmetic in TraceQL metrics queries, and experimental span ...

URL: https://www.youtube.com/watch?v=87mI6N8L9Z8

## Summary

The community call titled "What's New in Tempo 3.1," published on September 30, 2026, discussed the latest features and improvements in Tempo 3.1. The speakers highlighted key updates, including query-based trace redaction, arithmetic capabilities in TraceQL metrics queries, and experimental span pruning. Notable enhancements also included Kafka client improvements and the introduction of TLS for secure connections. The key takeaway was the ability to redact sensitive trace data using queries, making it easier to manage sensitive information without extensive enumeration.

Topics: Tempo 3.1, query-based trace redaction, TraceQL metrics, Kafka client improvements, span pruning.

## Chapters

00:00:00 Overview of Tempo 3.1 features
00:01:34 Query-based trace redaction and TraceQL metrics in Tempo 3.1
00:03:07 Experimental span pruning in Tempo 3.1

Tempo 3.1 is now available. It builds on 3.0 with Kafka client improvements, query-based trace redaction, new TraceQL metrics capabilities, span pruning, vParquet5 as the default block format, and more. If you haven't caught up on the new architecture in 3.0 and other changes, please check out the 3.0 blog and release notes. Tempo 3.0 moved microservices mode ingestion onto Kafka, and 3.1 comes with several improvements.

For instance, the client it shipped with could authenticate, but only with SASL PLAIN over a plaintext connection. It had no TLS settings, so a broker that requires TLS would just refuse the connection. Version 3.1 adds TLS and four more SASL mechanisms, among other improvements.

Let's take a look at a few of the new features of Tempo 3.1. Trace data can contain sensitive information, and sometimes you need to remove it without waiting for retention to expire. Version 3.0 added redaction, but it only accepted trace IDs, so you had to enumerate every affected trace. Sensitive data usually lands in whatever traffic hit a given code path, which is often more traces than you can practically list. Any trace you miss is data still sitting in your object storage. With 3.1, you can redact with a query instead. So the query that you use to find your issue could potentially be one that you used to remove it.

Let's take a look at an example where someone shipped a change that put an API key on their export spans for the article service. If we go and look at one of the traces here and click on that, if we open it up and take a look at our span attributes, we can see that we have this API key that we definitely do not want here. We can use the Tempo CLI and the query that we had before to do our redaction. There's also the option to set a start and end time. You can also use the dry run flag before actually running redaction since redaction can't be undone. 

We can see that we have a batch ID here and a number of jobs that were created. If we take a look at the active jobs in our backend scheduler, we can now see that we have all of those redaction jobs that are here. If we then go back over to Tempo itself, we can close this. Then, if we run our query again, we should be able to see that these traces are no longer there and they're gone. This will likely take longer to show for you since I dropped my live store times. You can see what we currently allow for queries in the documentation, as we intentionally have limited the scope since redaction is permanent and we are still working on more functionality for this feature.

In 3.0, TraceQL metrics went GA. With TraceQL metrics, you can generate ad hoc metrics directly from trace data at query time. The metrics you want out of traces are relationships between two measurements rather than one. Error rate is a common example. TraceQL could already measure errors in total traffic separately, but it couldn't divide one by the other. So you ran two queries and divided them with a math expression in Grafana. Version 3.1 lets you combine queries with arithmetic. Now we can use division in the query to get the error rate. We can also use scalers such as multiplying by a hundred to get a percentage. We could also see this per service as well.

A single request can produce a lot of spans. If the app runs a hundred nearly identical database queries, you get one root and a hundred leaves that all look the same. That's hard to read, and the more queries the request makes, the worse it gets. Version 3.1 can collapse each group of five or more similar leaf spans into one summary span with their experimental span pruning. This happens to read time, so nothing leaves storage.

Let's take a look at an example. We can see that there are a lot of spans here that look similar, and this can be really difficult to look through. Let's take a look at this with span pruning. You need to set `span_pruning_enabled_by_default` to true in the Tempo config file to prune trace by ID V2 requests that don't include a span pruning parameter. Grafana's trace view doesn't send one, so for now, that setting is what makes pruning visible in the UI. We can just run our query again, and now we can see that this is a lot easier to look at. We only have our two spans here. 

So we click on this one and look into our span attributes. We can see there are things here for aggregation, and then if we scroll down further, we can see that the aggregation is listed as a summary, and we can also see that the span count for it is a hundred. We can also take a look at this using the API, the Tempo CLI, and gcx. Here we're using the API, so we can see that with it disabled, we have 101 spans, and when we have it enabled, we have only two.

If you're curious to see a lot more about what is new with 3.1, please check out the blog, the release notes, and the change log.

## Raw YouTube Transcript

Tempo 3.1 is now available. It builds
on 3.0 with Kafka client improvements, query-based trace redaction, new TraceQL
metrics capabilities, span pruning, vParquet5 as the default
block format and more. If you haven't caught up on the new
architecture in 3.0 and other changes, please check out the 3.0
blog and release notes. Tempo 3.0 moved microservices
mode ingestion onto Kafka. 3.1 comes with several
improvements. For instance, the client it's shipped
with could authenticate, but only with SASL PLAIN over a plaintext
connection. It had no TLS settings, so a broker that requires TLS
would just refuse the connection. 3.1 adds TLS and four more SASL
mechanisms amongst other improvements. Let's take a look at a few of
the new features of Tempo 3.1. Trace data can contain
sensitive information and
sometimes you need to remove it without waiting for retention
to expire. 3.0 added redaction, but it only accepted trace IDs, so you had to enumerate every affected
trace. Sensitive data usually lands in whatever traffic hit a given code path, which is often more traces
than you can practically list. And any trace you miss is data still
sitting in your object storage. With 3.1, you can redact with a query instead. So the query that you use to find your
issue could potentially be one that you used to remove it. Let's take a look at an example where
someone shipped a change that put an API key on their export spans
for the article service. So if we go and look at one of
the traces here and click on that, if we open it up and take a look
at our span attributes here, we can see that we have this API key
that we definitely do not want here. We can use the Tempo CLI and the query
that we had before to do our redaction. There's also the option to
set a start and end time. You can also use the dry run flag
before actually running redaction since redaction can't be undone. We can see that we have a batch ID here
and a number of jobs that were created. If we take a look here at the active
jobs in our backend scheduler, we can now see that we have all of
those redaction jobs that are here. If we then go back over to
tempo itself, we can close this. And then if we run our query again, we should be able to see that
these traces are no longer there and they're gone. This will likely take longer to show
for you since I dropped my live store times. You can see what we currently allow
for queries in the documentation as we intentionally have limited the scope
since redaction is permanent and we are still working on more functionality
for this feature. In 3.0, TraceQL metrics went GA.
With TraceQL metrics, you can generate ad hoc metrics
directly from trace data at query time. So the metrics you want out of traces are
relationships between two measurements rather than one. Error
rate is a common example. TraceQL could already measure
errors in total traffic separately, but it couldn't divide one by the other. So you ran two queries and divided
them with a math expression in Grafana. 3.1 lets you combine
queries with arithmetic. Now we can use division in the
query to get the error rate. We can also use scalers
such as multiplying by
hundred to get a percentage. We could also see this
per service as well. A single request can
produce a lot of spans. If the app runs a hundred nearly
identical database queries, you get one root and a hundred
leaves that all look the same. That's hard to read and the more queries
the request makes, the worse it gets. 3.1 can collapse each group of five or
more similar leaf spans into one summary span with their experimental span pruning. This happens to read time
so nothing leaves storage. Let's take a look at an example. We can see that there are a lot of spans
here that look similar and this can be really difficult to look through. Let's
take a look at this with span pruning. You need to set
span_pruning_enabled_by_default
to true in the Tempo config file to prune trace by ID V2 requests that
don't include a span pruning parameter. Grafana's trace view doesn't send one, so for now that setting is what
makes pruning visible in the UI. We can just run our query again and now we can see that this
is a lot easier to look at. We only have our two spans here. So we click on this one and we
look into our span attributes. We can see there are things here for
aggregation and then if we scroll down further, we can see that the aggregation is listed
as a summary and then we can also see that the span count for it is a hundred. We can also take a look at this
using the API, the Tempo CLI and gcx. Here we're using the API
so we can see that with it disabled that we have 101 spans
and when we have it enabled, we have only two. So if you're curious to see a lot
more about what is new with 3.1, please check out the blog, the
release notes and the change log.

