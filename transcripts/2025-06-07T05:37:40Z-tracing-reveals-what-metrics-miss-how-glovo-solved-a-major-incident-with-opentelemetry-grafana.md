# Tracing Reveals What Metrics Miss: How Glovo Solved a Major Incident with OpenTelemetry &amp; Grafana

Published on 2025-06-07T05:37:40Z

## Description

See how Glovo's SRE team used Grafana Tempo and Traces Drilldown to debug a complex checkout failure and reshape their ...

URL: https://www.youtube.com/watch?v=2JX0D-4VkyQ

## Summary

In this YouTube video, Andrew Stucky from Grafana discusses the importance of tracing in observability for distributed systems, emphasizing that metrics and logs alone do not provide a complete picture. He is joined by Deepika and Alex from Glovo, who share their experiences with Grafana's Traces Drilldown feature during a recent incident where users were unable to checkout on their platform. The video explains tracing fundamentals, such as what a trace and a span are, and how they can help identify issues in complex microservices environments. Alex and Deepika detail a specific incident where they used Traces Drilldown to analyze service interactions, pinpoint the root causes of errors, and enhance their telemetry collection practices based on insights gained. The discussion highlights the value of integrating tracing with metrics and logs, showcasing how it can improve incident response and system reliability.

# Grafana Traces and Traces Drilldown Presentation

Hello. Thank you for joining us. I'm going to try this again. Hello everyone... Woohoo. I'm excited to talk to you today about **Traces**, **Tempo**, and **Traces Drilldown**. We'll be doing a QA session at the end. I know you've probably seen this QR code a million times, so I'm going to skip past it, but scan it if you haven't.

Actually, I think I had our intro notes on that slide. I'm Andrew Stucky from Grafana, where I lead the Grafana Drilldown group. I'm honored to be joined by Deepika and Alex from Glovo, a subsidiary of Delivery Hero. 

## Introduction to Tracing

I want to talk a bit about how metrics and logs alone leave this story half-told. Pretend you wake up to an alert—users are unable to check out. Your metrics tell you that something is happening; after all, they probably triggered your alert. But metrics alone probably won't tell you what is happening or where. Logs are pretty good at informing you about what is happening. For example, an exception is thrown, etc. However, finding that needle in the haystack can be challenging.

As teams continue to adopt microservices, a single backend service is often just a piece of the puzzle. You might have 2 microservices or 10, and the puzzle has a way of getting larger.

So, what is tracing and how does it help with the observability of distributed systems? Tracing is basically logging improved with context that is shared across HTTP boundaries, allowing you to see the flow through the various components that your system contains.

### Tracing Basics

A trace represents an entire request across multiple services and visualizes the flow from start to finish to identify bottlenecks and dependencies. Traces are often high volume and have high cardinality. They can also contain logs or events. 

A span represents a particular operation within the request flow, detailing "where" it occurred. They usually include timing, success or failure data, and relevant tags or metadata, which we call attributes. Attributes are essentially key-value pairs. 

Spans can also contain events, which record significant occurrences, such as an exception. Finally, spans can contain links to other spans or traces, which can be helpful when dealing with really large traces.

Coming back to the beginning, traces provide us a structure to visualize what would otherwise be a chaotic environment. This structure can be incredibly useful in distributed systems. A common use case of traces is to pinpoint errors in the context of a larger system. 

This doesn't necessarily mean that one signal is better than the others; traces don’t rule them all. Each has its own strengths and weaknesses, and I think they really are better together. Metrics tell us that something might be happening, traces tell us where it is happening, and logs tell us what is happening.

## Tracing in Grafana

Now that we've covered the basics, let's look at what tracing looked like in Grafana before Traces Drilldown. 

Imagine you wake up to your alert—users are unable to check out. You're in dashboards, looking at metrics and logs, but they might not be sufficient for this particular incident. You think, "Alright, we're going to navigate to traces in Grafana. This will save the day." You go to Explore, select your Tempo data source, and... "no data." Okay, so what now? 

Well, you write a query, but even simple queries can get complex. For example, if we dissect the query on the screen, we want to see a list of services, specifically the descendant services, which are experiencing errors that originate from traces using the frontend service. These dependencies can be quite complex when you try to query for them. 

This is why we built **Traces Drilldown**—no more writing complex queries. You can deliver value from tracing faster using a point-and-click experience.

Instead of me doing the demo, I've talked enough about traces and Drilldown. I'm going to give Glovo the opportunity to share one of their use cases and sell you on Traces Drilldown. Thank you.

---

## Glovo's Use Case

Hello everyone. My name is Alex, and I'm here with Deepika. We're part of the SRE team at Glovo, an on-demand delivery platform that lets users order anything from food, groceries, or any other item that a local store might sell. We operate in 23 countries across Europe, Africa, and Asia, and we are part of a larger group called Delivery Hero, one of the biggest delivery groups in the world.

To give you more insights into our business, one of the most important metrics we have at Glovo is called the "Orders Created" metric. As you can see, the volume per day has different peaks at different times of the day. For example, at lunch or dinner, we have many more orders. An incident during lunch is much more impactful than one at breakfast.

### Incident Scenario

Imagine the following scenario: it's Monday at 12:50 PM, there are 10 minutes to lunch, and you're getting hungry. You go to the Glovo app, select your favorite restaurant, find that perfect dish, and go to checkout. But then the app is not responding. Your order is closed, and you don't know what to do. You're getting more and more hungry.

On our side, we get paged because the order creation rate drops below normal. We quickly check the orders created dashboard and see that orders are going down, meaning we are losing money as we speak. 

In the next few minutes, Deepika will explain how we mitigated this incident.

### Incident Mitigation

As SREs, we are often in the dark when such incidents happen because any part of our distributed system could fail, causing order loss. To help us during such incidents, we built many custom dashboards and metrics in Grafana.

This is an example dashboard that clearly highlights that the checkout part of the flow failed. We dive into the checkout RED dashboards and find that one of its downstream dependencies, called catalog, failed because it was rate-limiting checkout. For context, the catalog service provides product information for the order.

During the daytime, whenever an incident happens, we always suspect a code change. So we built a change log dashboard that pulls events from our deployment tool called Argo. We can see there was a deployment in catalog when this incident happened, along with some feature toggle changes. 

We reached out to the engineers in the team, and they confirmed that this could have impacted the checkout failure. We quickly rolled back the deployment, and within five minutes, order creation returned to normal. In fact, we exceeded last week's values—great mitigation! However, as SREs, our job doesn't end there because we need to find the root cause of the incident to ensure it doesn't happen again.

### Root Cause Analysis

We go to the application monitoring page of checkout to look for clues. As expected, we see a huge spike in the error panel because all the traces were being rate-limited. Interestingly, we also observed that the latency of the checkout was very high. This was surprising because we were just rate-limited, so the request should have taken a few milliseconds and failed.

We dig deeper and check the logs, where most of the errors point to the Hikari Connection Pool. This is again strange because we didn't have anything database-related going on, but it clearly showed that the application was failing to get connections from the connection pool. 

When we check further into the metrics for Hikari, we see that a lot of threads are waiting for connections. So it seems like two different issues. Our mitigation suggested a faulty deployment in a downstream service led to the issue being resolved by rolling back. But looking at the logs and metrics, the issue pointed towards the database as well. 

We checked the performance insights and found our database was perfectly fine. Thus, we realized the database issue was an effect of the original problem, not the cause. We still couldn't determine how the catalog failure caused the database failure.

### Using Traces for Resolution

We decided to use traces because they usually provide samples or examples. However, when we queried for "500" traces, most of the examples again showed short database problems, which didn't help us much.

As users of Grafana Cloud at Glovo, we had the opportunity to pilot many of the features they build. When this incident happened a couple of months back, we had been using Drilldown for about one or two weeks, and it had helped us during previous incidents. So, we thought, why not see if Drilldown can assist us in finding those interesting traces?

In the next few slides, I'll show how we utilize Drilldown to find the root cause of this problem.

### Navigating Drilldown

Usually, we go to the Traces Drilldown main page where we can see the error rate already selected. It's very easy to filter by service name. Here, we filter by the checkout API, the service that had the problem. 

Another straightforward way to identify if there's a problem in the service is to try different span attributes or resource attributes. Sometimes, we go for pod names or service versions to understand if the problem is localized or global. Unfortunately, in this specific case, we couldn't find more than what the metrics and logs showed us.

So, we thought, why not go backwards from the end to the start? We checked the product-catalog API traces. We filtered by HTTP status code to focus our search on the rejections from the product catalog. Drilldown allows us to easily select one of the status codes that appear in the spans, and we selected the "429"s.

The next step was useful because we didn't know exactly what attributes to look for. The comparison tab gives insights on attributes that have different values from the baseline. Scrolling down the page, we saw that one of the attributes called "flow_name," which in Glovo means the client, had much larger values than the others. In this case, the checkout was responsible for 88% of the rejections.

At this moment, we had three filters: the product catalog API, the "429" HTTP status code, and the client. We then knew we were dealing with a cascading failure. The database issue was caused by something else, so we wanted to check some exemplars from the beginning of the incident to determine the cause.

### Analyzing the Trace

We checked one of the first seconds of the incident, opened a trace, and noticed we were calling the database. Interestingly, the database call took less than one millisecond, but the entire trace took 3.7 seconds and then timed out. 

Going down the trace, we saw that one of the methods called "batch product validator" was taking the most time. If we look inside its nested components, we see that the product catalog API is called twice, but we didn't understand why there was a delay between the calls.

To investigate further, we wanted to check if this was indeed the longest-running span in our incident. So, we went to Drilldown again and checked the duration tab, which showed us all the spans sorted by duration in decreasing order. As expected, "batch product validator" was indeed one of the longest-running spans.

Returning to the trace, we deep dove into the product catalog API trace and saw the exception message indicating that we were being rate-limited. Here, a key piece of information was revealed: the remaining ban seconds value was sent back from the product catalog to checkout in a Retry-After header. 

So, what happened was that the checkout was being told to wait a certain amount of seconds before calling back. This made sense—checkout was called once, it was rejected quickly, and then three seconds of vital time were lost before the second call to the product catalog, which timed out.

### Connection Pool Issues

We understood the problem with the long-running request, but we still didn't comprehend how this was connected to the database. We went further and checked another trace. Here, we noted that the database also took a lot of time—about one second. 

We observed the same behavior as in the first trace, where the product catalog was called multiple times. In this case, it was called five times, with delays in between the calls. At this moment, we speculated that if they happened in the same thread, the connection would be held for the entire duration of this trace.

Thus, we used another useful feature from the Trace Explorer, filtering by the thread ID. This granularity helped us understand that, in fact, the calls were happening in the same thread. However, there was something missing because we had encountered this problem in the past. 

For all services with many downstream dependencies, we use a property called "open-in-view" in Spring to disable holding the data source connection while other actions occur. Setting this property to "false" releases the primary data source connection from the thread pool. 

However, in this specific case, the checkout API had overridden this with the "@Transactional" annotation on their method. So, this did not resolve the issue.

### Incident Resolution

Ultimately, the incident resolution was that the checkout API was calling the product catalog, getting rate-limited, and then experiencing retries with long waiting times in between. While all of this was happening, connections were being held from the thread pool for the database, preventing new requests to the checkout API from being processed.

Deepika will now explain how this incident shaped the way we collect telemetry at Glovo.

---

## Collecting Telemetry at Glovo

Before we dive into that, let me briefly explain our OpenTelemetry collector setup. Our applications run on Kubernetes, and we've instrumented them with OTel agents. For non-Java-based apps, we use SDKs that create spans. We also have a load balancing collector to ensure that all spans of a given trace go to the same version of our traces collector. 

We implement something called **tail sampling** to help save costs by selecting which traces to send to Grafana. Our current tail sampling policy is that if there are server errors, we send 100% of them. For client errors, we send 5%. Sometimes, when teams are creating new services, they ask to keep all traces to observe patterns. So we made a custom OTTL condition to support that.

In general, our probabilistic sampling rate is 1%. We thought, why should we send all traces? This led to a situation during the checkout incident where we saw many slow traces, but when we checked the histogram duration, we only saw a few examples of the slow traces. This was due to our probabilistic sampling; it doesn’t guarantee that the slowest spans are sent to Grafana.

We explored the OpenTelemetry library to see if there were any tail sampling processes based on latency. There was one, but it only supported static latency thresholds. Given our complex distributed system, we had different thresholds for various services and endpoints, which could quickly become outdated. The teams needed something effective soon because traces data was deemed not useful in instances of high latency issues.

### New Sampling Policy

To address this, we built a stop-gap solution. We always send the SLOs of the spans in their context. Since we already had this information in the root spans, we developed an OTTL condition to intercept the root span. We check its duration, compare it with the SLA in the span context, and if the span breaches the SLA, we keep the whole trace. 

As a result, we saw improvements. After implementing this, we experienced a latency issue, and we now have more examples of slow traces. This enhances the usage of Traces Drilldown, providing us with valuable insights from the tracing data.

### Summary

In summary, I want to highlight how we are using Traces Drilldown in our day-to-day activities at Glovo. Personally, I mainly use the error panel because it is very helpful for picking exemplars. For instance, if you have a deployment, you can select traces from a specific version of the service. If one of your pods is crashing due to memory or another issue, you can pick traces from those pods. 

We also utilize the duration tab for identifying slow traces during latency issues. 

Thank you everyone for giving us this opportunity. I hope you found this information useful!

## Raw YouTube Transcript

Hello. Thank you for joining us. I'm
going to try this again. Hello everyone... Woohoo. I'm excited to talk
to you today about traces, Tempo and Traces Drilldown. We'll be doing QA at the end and I know
you've probably seen this QR code a million times, so I'm going to skip
past it, but scan it if you haven't. Actually, I think I had our intro
(notes) on that slide. I'm Andrew Stucky. I'm from Grafana. I lead
the Grafana Drilldown group. I'm honored to be joined by
Deepika and Alex from Glovo, a subsidiary of Delivery Hero. So, I want to talk a bit about how metrics
and logs alone leave this story half-told. Pretend you
wake up to an alert. You might not have to pretend, this might have happened to you recently
and users are unable to checkout. Your metrics, tell you that
something is happening. After all, they probably triggered your alert, but metrics alone probably won't
tell you what is happening or where. Logs, they're pretty good about
telling you what is happening. An exception is thrown,
et cetera, et cetera. You can find the needle in the haystack, but finding that (needle)
can be challenging. To complicate matters further, as
teams continue to adopt microservices, a single backend service is
often just a piece of the puzzle. We might have 2 microservices or 10. The puzzle has a way of getting larger. So what is tracing and how does it
help with observability of distributed systems? Tracing is basically logging improved
with context that is shared across HTTP boundaries, which allow you to see the flow through
the various components that your system contains. But first I want to cover
some tracing basics. A trace represents an entire
request across multiple services and visualizes start to finish the
flow to identify bottlenecks and or dependencies. Traces are often high volume
and have high cardinality. They can also contain
logs or events as well. A span represents a particular
operation within the request flow dealing with "where" it occurred.
They usually include timing, success or failure data and
relevant tags or metadata, which we call attributes. Attributes are basically key value
pairs. That metadata I spoke about, spans can also contain events
which record significant occurrences, such as an
exception. And finally, spans can contain links to
other spans or other traces, which can be helpful when
you have really large traces. Coming back to the beginning, traces really provide us a structure
to visualize what would otherwise be a pretty chaotic environment. This structure can be really, really
useful in distributed systems. A common use case of traces is to
pinpoint errors in the context of such a larger system. This doesn't necessarily mean that
one signal is better than the other. Traces doesn't rule them all. It has
its own strengths and weaknesses. So I think they really
are better together. Metrics tell us that
something might be happening. Traces tell us where something is
happening and logs tell us what is happening. Now that
we've covered the basics, let's look at what tracing looked like
in Grafana before Traces Drilldown. You wake up to your alert,
user's unable to check out. You're in dashboards, you're looking
at metrics, you're looking at logs, and they might not be sufficient for
this particular incident. So you think, all right, we're going to navigate to
traces in Grafana. This will save the day. Andrew told-me-so. This
will find the where. So you go to Explore, you select your tempo data
source and ... "no data". Okay, so what now? Well, we write a query and even simple
queries can get complex. For example, if we dissect the query on the screen, we want to see a list of services and that list of services
will be descendant services, which are experiencing errors that
originate from traces using the front end service. And these dependencies can be kind
of complex when you try to query for them. So easy, right? This is why we built Traces
Drilldown. No more writing queries, deliver value from tracing faster,
using point and click experiences. But instead of me doing the demo, I've already talked enough
about traces and Drilldown. I'm going to give Glovo the opportunity
to share one of their use-cases and sell you on Traces Drilldown. Thank you. Hello everyone. My name is Alex and I'm here with Deepika. We're a part of the SRE team at Glovo. And today we want to
touch upon two topics, how we use Traces Drilldown during one
of our recent incidents and how we shape the way we collect telemetry.
So first of all, who is Glovo? Glovo is an on-demand delivery platform
that lets users order anything from food, groceries, or any other item
that a local store might sell. We are operating in 23 countries
across Europe, Africa, and Asia. And we are part of a bigger
group called Delivery Hero, which is one of the biggest
delivery groups in the world. To give you more insights
into our business, this is one of the most important
metrics we have in Glovo. It's called the "Orders created
metric". And as you can see, the volume per day has different peaks
at different times of the day. For example, at lunch or dinner, we have
much more orders. And as you can imagine, an incident at lunch is much more
impactful than one at breakfast. So with that in mind, imagine
the following. It's Monday 12:50, there are 10 minutes to lunch
and you're getting hungry. You go to the Glovo app, you select that restaurant that is
your favorite restaurant in the city. Find that perfect dish, go to
check out. And this happens. The app is not responding, the order
is closed, you don't know what to do, you're getting more and more hungry. And on our side we get paged because
the order creation goes below the normal rate, we go quickly and check
the orders created dashboard. We see that orders are going down
and we are losing money as we speak. So in the next couple of minutes, Deepika will explain how
we mitigated this incident. As SREs, we are kind of in the dark when such
incidents happen because any part of our distributed system could
fail causing the order loss. So we built many custom
dashboards and metrics in Grafana, which helps us during such incidents.
This is an example dashboard. It clearly highlights the
checkout part of the flow failed. We go further into the
checkout RED dashboards, we find that one of its downstream
dependencies called catalog failed because it was rate limiting checkout. So for context catalog is the service
which gives the product information for the order. During the daytime,
whenever incident happens, we always suspect it
could be a code change. So we have built a change log dashboard
which pulls events from our deployment tool called Argo. So we can see here that there was a
deployment in catalog when this incident happened and there were also some
feature toggle changes. We reached out to the engineers in the team, they confirmed that this could
have impacted the checkout failure. So we quickly rolled back the
deployment and in five minutes we are back to our order creation
being normal. In fact, we are over the last week's
values, so great mitigation, but as SRE again, our job doesn't end here because we need
to find the root cause of the incident and make sure it doesn't repeat again. So we go to the application monitoring
page of checkout to look for some clues. As expected, we see a huge spike in the error panel
because all the traces were being rate limited. What was interesting was we also saw
that the latency of the checkout was very high. This was kind of surprising
because we were just rate limited. So the request should have taken
few milliseconds and failed. So we dig deep and then we go to the logs.
We see most of the errors were pointing to Hikari Connection Pool. Again, weird because we didn't have anything
related to database going on, but it clearly showed that the application
was failing to get connections from the connection pool. We check
further the metrics for Hikari, we see a lot of threads are
waiting for the connections. So they seem like two different
issues. As per our mitigation, it seemed like there was a faulty
deployment in a downstream service. So we just rolled back
and the issue was solved. But then looking at logs and metrics,
the issue was pointing towards database. We checked the performance insights and
stuff and our database was perfectly fine. So we realized that the database issue
was rather the effect of the original problem, not the cause of the problem. We still couldn't find what exactly how
the catalog failure caused the database failure. We thought to use traces
because traces usually give us a sample. I mean example.
Traces can give us the hints, but then in this case when we went there
and then we query for "500" traces, most of the examples we got
again, short database problems, which didn't help us much. We are users of Grafana Cloud at Glovo, so we get to pilot many of
the features they build. So when this incident happened
a couple of months back, we've been using Drilldown for I think
one or two weeks and it helped us during one of our earlier
incidents. So we thought why not? Let's see if Drilldown can help us
to find those interesting traces. So in the next slide, Alex will walk you through how we actually
use Drilldown to find the root cause of this problem. Alright, so in the next couple of slides
I'm going to show how we use Drilldown. Usually we go to the (traces) Drillown
main page here we can see the error rate already selected and it's a
very easy thing to filter by. It's the service name. Here we
try to filter by the checkout API, so the service that had the problem. And then another easy way to understand
if there's any problem in the service is to try different span
attributes or resource attributes. Sometimes we go for pod name or service
version to understand if the problem is localized or a global problem.
But in this specific case, unfortunately we couldn't find more than
what the metrics and logs showed us. So we thought why not go backwards
from the end to the start? Why not check product-catalog API traces? And that's what we did. It's as easy
as selecting here the service name to "product-ctg-api". And then what we wanted to do is to focus
our search on the rejections that we get from product catalog. So that's why
we also filter by the HTTP status code. Drilldown shows you very nicely that you
can select one of the status code that appears in the spans. And here in
this case we selected the "429"s. The next step was very
useful because we didn't know exactly what attributes to look for. So the comparison tab gives you insight
on what attributes are having different values from the baseline.
And scrolling down the page, we saw that one of the
attributes called "flow_name", which basically in Glovo means the client, is having much bigger values than
the others. And in this case, checkout was having 88% of the
times rejections. So we said why not filter by this as well? And
this moment we have three filters. The first one is "product-ctg-api". The second one is the "429"s on the HTP
status code and the third one is the client. Now here we knew that this
is a cascading failure. We knew that the database issue
was caused by something else, so we wanted to check some exemplars
from the beginning of the incident to see what caused this. So that's
exactly what we did here. We check one of the first seconds
of the incident, open a trace, look inside the trace. And as you can
see here we are calling the database. There's a very interesting fact here
because the database called it's less than one millisecond, but the whole trace it's taking
3.7 seconds and then timing out. So something is not right. We go
down the trace and we see that one of the methods called "batch product
validator" is taking the most time. And if we look inside of it
in the nested components, we can see that product catalog
API is called two times. Still, we didn't understand why there's
a space in between the calls, but before going further, we wanted to check if in fact this
is the longest running span in our incident. That's why we
went to Drilldown again, we checked the duration tab and this
showed us in decreasing order of span durations, all the spans that
took so much time in the incident. And as you can see, "batch product validator" is indeed
one of the longest running spans. Coming back to the trace, we deep dive into the
product catalog API trace, and we see the exception message
tells us rate-limited. So we already knew that we are getting rate-limited, but there was a key
information that was missing. If you see in this screenshot we have
a field called "remaining ban seconds". And this value was actually sent
back from product catalog to checkout in a Retry-After header. So basically what happened
is that checkout was being
told you should wait this amount of seconds before
calling back and now it all made sense. So product catalog was
being called once by checkout. They were getting rejected very fast, like one millisecond and then three
seconds of vital time was taken here. And then calling again by the
second time we call product catalog, already the request was timing out. So we understood what was the
problem with long running request, but we still didn't understand how
is this connected to the database and we went further and checked on
another trace. And here in this trace I want to highlight that the
database also takes a lot of time. It takes one second. We also see the same behavior as in the
first trace where product catalog is called multiple times. In this case
it's even called more than two times, it's called five times and there's some time in between the calls. So what we thought at this moment is
what if they happen in the same thread and in fact the connection is being held
for the whole duration of this trace. So that's why we also used another
useful feature from the Trace Explorer. We were able to filter by the
thread ID - specifically - this granularity helped us understand that
in fact they were happening in the same thread, but there was something missing because
in Glovo we had this problem in the past a few years ago. And for all the
services that have a lot of downstream dependencies we use on property
called "open-in-view" in Spring to disable, to disable the data source connection being held while other
things are happening. So this is the property that we have
and as you can see in the first line, this is a screenshot from
the checkout API codebase. Setting it to "false" will release the
primary data source connection from the thread pool. So this
should not be a problem, but in this specific case, checkout API has overridden
this with the "@Transactional" annotation on their method. So this didn't really help with anything. So this was the incident resolution.
Checkout API was calling product catalog, was getting very limited, there were retries and long waiting
times in between the retries. While all of this was happening, we were holding connections from
the thread pool for the DB and new connections to checkout API. New requests could not fulfill
their processing because this connection were being held. And
in the next following slide, Deepika will explain to us how it shaped
the way we collect telemetry at the Glovo. Before we go there, I just want to take a moment to explain
our open telemetry collector setup. So we have apps running on Kubernetes. We've instrumented them with OTel
agents for some other non-Java based apps. We use SDKs. These create the spans and then we
have something called "load balancing collector". So among the other uses, we use it for making sure that
all the spans of a given trace go to the same version of
our traces collector. And then we do something
called tail sampling. This helps us to save the costs a lot
because we select which traces we send to Grafana. So how Drilldown made us
rethink our sampling policy. So this is our current tail sampling
policy. If there are server errors, we send 100% of them. And
for client errors we send 5%. And sometimes when teams are
making new services, they ask us, they want to keep all the traces
because they want to see some patterns. So we made a custom OTTL condition
to support that. In general, our probabilistic sampling is 1% because
we thought why do we have to send all the 200 traces. During this
incident with checkout, as you saw in the application page,
there were so many slow traces, but when we went to
the histogram duration, we only saw few examples
in the slow traces. This is because of our probabilistic
sampling because it just says it's 1%. It doesn't guarantee that the
slowest spans get sent to Grafana. We went and explored the open telemetry
library to see if there are any processes, tail sampling processes
based on latency. There was one, but at this moment it was only
supporting static latency thresholds. And in Glovo, since we have
a complex distributed system, we had different thresholds for different
services and endpoints and we thought this could get outdated quickly. But also the teams needed something like
this soon because they thought traces data was not useful in case
of high latency issues. So we built something as a stop gap. So we always send the SLOs of
the spans in their context. So we already had this information
available in the root spans, so we thought why not we
make an OTTL condition? So we intercept the root
span, we check its duration, we compare it with the SLA in
the span context and if the span has breached the SLA. We keep the whole trace
since we use tail sampling, we end up keeping the whole
trace with all the spans. So this was another example where after
we build this we had a latency issue and you can see that now we have
more examples of slow traces. This makes the usage of (traces)
Drilldown also better as we get a lot of insights from the tracing data. I just want to summarize how we are
using it in our day-to-day activities at Glovo. I personally mainly use the error
panel because it's very helpful to pick exemplar. As example, if you have a deployment you can pick
from a particular version of the service. If one of your pods is crashing
because of memory or something, you can pick traces from those pods. And there are various resources
and span attributes you can use. We also use the duration tab for
picking the slow traces during latency issues. That's pretty much about it. Thank you everyone for giving us this
opportunity and I hope you found it useful.

