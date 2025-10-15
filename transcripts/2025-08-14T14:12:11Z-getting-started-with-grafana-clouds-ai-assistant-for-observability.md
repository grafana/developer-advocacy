# Getting Started with Grafana Cloud&#39;s AI Assistant for Observability

Published on 2025-08-14T14:12:11Z

## Description

The pace of software delivery in 2025 is unprecedented — cloud-native apps, microservices, and AI-generated code are shipping ...

URL: https://www.youtube.com/watch?v=UtZkFYUmjrM

## Summary

In this video, the presenter discusses the rapid advancements in software development, particularly in 2025, where "vibe coding" has transformed the pace at which software is created, often with the assistance of large language models (LLMs). The focus is on how the new Grafana Assistant can enhance observability and operations management for services, specifically using a Python API, Kafka, and Postgres setup. The video demonstrates how the assistant can quickly generate dashboards, set alerts based on key metrics, and optimize telemetry configurations, significantly improving productivity for both novice and experienced Grafana users. The presenter emphasizes the importance of real-time monitoring and cost efficiency, highlighting that the assistant can reduce ingestion costs by 60 to 70%. The video concludes with an encouragement to explore the Grafana Assistant, which is currently in public preview.

# Life in 2025: The Rise of Vibe Coding

Okay, so life as we know it has changed. **2025 has fully submerged us into the deep waters of vibe coding**, and we're now shipping software at such a rapid pace. It’s super exciting, but also terrifying. With this pace of innovation comes a new reality: a lot of code isn’t even written by us humans anymore; it’s written by these LLMs, usually a French guy named Claude.

The services that used to take us months or quarters to prototype and bring to users are now taking just a few weeks, sometimes even days. But even with the rise of vibe coding, one aspect remains constant: **we need to maintain it**. We have to know when it breaks and why it breaks. If you're watching this video, that someone is probably you or your team, and you may be hoping there’s finally an easier way. However, I understand you're likely skeptical because, let’s be honest, every SaaS product right now claims to have the next groundbreaking AI solution.

In this video, I'm going to do the exact opposite. I’m not going to hype anything; I’m just going to show you the new **Grafana** and how it can help you get real observability coverage for a new service a heck of a lot faster, giving you a little more of that vibe coding energy when it comes to operations. 

## Setting Up the Environment

Alright, let’s see what we're working with. We’ve essentially got a Python API that simulates a service with the endpoint `/produce`. It’s publishing events to a Kafka broker and also writing them to a Postgres database. All of this is wrapped in a Docker container and hosted in Kubernetes. It’s all open source; we’re not using any cloud services.

We’ve also added **Prometheus exporter** and **Kafka exporter** containers so we can monitor them in Grafana. Additionally, we are running a load test through **K6** to generate traffic, essentially piping those metrics from the load test into Grafana Cloud using **Grafana Alloy**. This is an open-source, OpenTelemetry, and Prometheus-compatible collector. It serves as our pipeline generation tool, scraping those metrics and sending them into Grafana Cloud to our managed databases.

At this point, everything is up and running, and we can see that in Grafana Cloud. Now it’s time for fun—time to dive into the vibes of what vibe coding is or vibe ops, in this case. We’re going to use the assistant to help onboard this new service.

## Creating Dashboards and Alerts

First up, I’m going to ask it to create a dashboard for my Kafka and Postgres setup. The prompt I’m going to use is: **"Can you generate a dashboard showing key Kafka and Postgres metrics for correlation of my services?"** 

While this work is being done in the background, you’ll see on the right-hand side with the assistant that this is all context-aware. It already knows what data is available because it’s scoped to your Grafana Cloud stack. It’s not guessing; it’s building with the live data sources and the live data flowing into them. 

Things like logs in **Loki**, metrics in **Mimir/Prometheus**, **Tempo** for traces, and **Pyroscope** for profiles. It’s also going to look at our docs, so if we have any best practice questions or need help integrating with some other features of Grafana Cloud, we can easily ask.

The assistant just scaffolded out a dashboard for me with panels for broker throughput, consumer lag, connections, locks, query times—all the stuff I really care about—without me having to dig through a dozen metric names or write the queries myself.

Now that we’ve got full visibility of these two services, the next thing I want to ensure is that I know when things go sideways. We need alerts. Dashboards are great, but I don’t want to handle PromQL writing right now. So I’m going to ask the assistant to help out. 

Again, the prompt I’m going to use here is: **"Can you create alerts for Kafka consumer lag and Postgres query latency?"** This is a more targeted prompt, and this is where the assistant really goes above and beyond. It gives me context on why the thresholds it sets actually matter. It doesn’t just say, “Set this to 200 milliseconds.” It explains what normal looks like for that metric and what a spike might mean.

## Optimizing Telemetry

So, I’ve got a dashboard and an alert created for monitoring my stack, which is awesome. But now I need to clean up the telemetry I’ve been sending in. You can see we’re sending quite a bit in, and it doesn’t necessarily mean we need all of it. One of the biggest challenges with telemetry is that these exporters from Prometheus and OpenTelemetry can often throw the kitchen sink at you. You have to make decisions about what to get rid of, what to aggregate, and what to keep.

I’m going to feed my current configuration into the Grafana AI Assistant and ask it to optimize based on best practices to only keep what’s crucial. My prompt will be: **"Given my Alloy config, optimize based on best practices to remove the non-critical Kafka and Postgres metrics."**

What’s awesome here is that it helps optimize the config by filtering out the non-critical metrics while keeping the essential ones that we just prompted for to create our dashboards and alerts. It searches over Prometheus metrics, looking at high cardinality metrics that are problematic for both cost and storage. Based on that analysis, it gives me a proper config that I can copy and implement in my IDE.

It also provides key optimizations made, telling me exactly what it’s getting rid of, what it’s keeping, and what it’s dropping. This is crucial because you’ll want to review these configs. You never want to just go with something at face value; you want to understand what’s going on. The assistant indicates that these changes can reduce ingestion costs by **60 to 70%** in both Kafka and Postgres metric volume. This is huge and will lead to massive savings as we scale.

## Conclusion

To wrap things up, the Grafana assistant is pretty sweet and has personally saved me a ton of hours. If you’ve been a long-time Grafana user, it will rapidly increase your productivity. If you’re new to Grafana, the assistant will have you feeling like an expert in no time. 

And yes, that’s vibe ops. If that term ends up in a conference talk, just make sure to add Grafana in the footnotes. I don’t know if it’s going to catch on, but go check it out. The assistant is now in public preview, and we really look forward to seeing how this saves you time. 

**Take it easy!**

## Raw YouTube Transcript

Okay, so life as we know it has changed. 2025 has fully submerged us into the deep waters of vibe coding and we're now shipping software at such a
rapid pace. It's super exciting, but also terrifying. And with that pace of innovation is
coming a new reality that a lot of code isn't even written by us humans anymore. It's written by these LLM's and
usually a French guy named Claude. The services that used to take us months
or quarters to prototype and bring to users are now taking just a few
weeks in, sometimes even days. But even with the rise of vibe coding,
one aspect is still remaining constant. We got to maintain it. We have to
know when it breaks and why it breaks. And if you're watching this video that
someone is probably you or your team, and you're maybe hoping there's
finally an easier way, however, I understand you're probably
skeptical because let's be honest, every SaaS product right now claims to
have the next groundbreaking AI solution. So in this video, I'm going
to do the exact opposite. I'm not going to hype anything. I'm just going to show you the new Grafana
assistant and how it can help you get real observability coverage for a new
service a heck of a lot faster and give you a little more of that vibe coding
energy when it comes to operations. Let's get into it. Alright, so
let's see what we're working with. We've essentially got a Python, API that simulates a service with
the endpoint /produce it's publishing events to a Kafka broker and also
writes them to a Postgres database. All of this is then being wrapped
in a Docker container and hosted in Kubernetes. It's all open source. It's not using any cloud
services or anything like that. We've also added Prometheus
exporter and Kafka exporter containers, so we can
monitor them in Grafana. Now we're also running a load test through
K6 because we need a way to generate traffic, and we're essentially piping those metrics
from the load test into Grafana Cloud using Grafana Alloy.
This is an open source, open telemetry and Prometheus
compatible collector. So this is sort of going to be used for
our pipeline generation that's going to scrape those metrics and then send
them into Grafana Cloud to our managed databases. Now at this point, everything is up and running and
we can see that in Grafana Cloud. So now it's time for fun. It's time for actually giving into the
vibes of what Vibe Coding is or vibe ops in this case. And we're going to use the assistant
to help us onboard this new service. So first up, I'm going to ask it to create a dashboard
for my Kafka and Postgres setup. The prompt I'm going to be using is can
you generate a dashboard showing key Kafka and Postgres metrics for
correlation of my services? Now while this work is being
done in the background, you'll see on the right hand side with
the assistant that this is all context aware. It already knows what data is
available because it's scoped to your Grafana cloud stack or the Grafana
Cloud environment. So it's not guessing, it's building with the live datasources
and the live data flowing into them. So things like logs in Loki
metrics in Mimir/Prometheus, Tempo for traces, Pyroscope for profiles. And then it's also going
to look at our docs. So in case we have any best practice
questions or how to integrate with some of the other features of Grafana Cloud, we can easily ask that and we're going
to go through some of that process here. But you'll see that this is going to
start doing the work in the background. It's going to navigate
us to the dashboard, and then it's going to essentially pick
the best visualization types for the data we're looking to actually show.
And we'll see that here. Right on, so the assistant just scaffolded out
a dashboard for me with the panels for broker throughput, consumer
lag connections, locks, query times, all the stuff I really care about
without me having to dig through a dozen metric names or write the queries myself
and be an expert in promQL. So now that we've got full visibility
of these two services, the next thing I want to make sure
is I know when things go sideways, we need alerts. Dashboards are great, but I don't want to handle
promQL writing right now. So I'm going to ask the
assistant to help out. Again, prompt I'm going to use here is can you
create alerts for Kafka consumer lag and Postgres query latency? This
is a more targeted prompt, but this is where the assistant
really goes above and beyond, and it gives me context on why the
thresholds it sets actually matter. So it doesn't just say, set
this to 200 milliseconds. It explains what normal actually looks
like for that metric and what a spike actually might mean. Okay, so I got a dashboard and an alert
created for monitoring my stack, which is awesome, but now I need to do some cleanup of
the telemetry that I've been sending in. You can see here that we're
sending quite a bit in, and it doesn't necessarily
mean we need all of it. So that's one of the biggest things with
telemetry as a whole is these exporters from Prometheus and Open Telemetry can
oftentimes throw the kitchen sink at you and you have to kind of make the
decision of what to get rid of, what to aggregate, what to keep, or
just send to object storage and whatnot. And these are all questions
that weigh on you and your team. So I am going to actually feed
my current configuration into the Grafana AI Assistant and ask it
based on best practices to only keep what's crucial. My prompt's going to be given my Alloy
config optimize based on best practices to remove the non-critical
Kafka and Postgres metrics. What's awesome here is you can see that
it's going to help optimize the config, but it's going to filter
out the noncritical metrics
while keeping the essential ones that we just prompted for to create
our dashboards and alerts. So you can see that this is searching over Prometheus
metrics that are stored like Kafka, PG and Postgres, and then it's going to look at the high
cardinality metrics that are really problematic for both cost and
storage. And then it's going to, based on that analysis, give me a proper config that I can
copy and actually go back into my configuration in my IDE change
that and make the proper updates. You can see that it's going to give
me the key optimizations made as well. So it's going to tell me exactly
what it's getting rid of, what it's keeping and what it's dropping, which is super crucial because you're
going to want to walk over these configs anyways, right? You never want to
just go with something at face value. You're going to want to
understand what's going on, but it says that this can reduce
ingestion costs by 60 to 70% in both Kafka and Postgres Metric volume.
This is huge because you scale that out, it's going to be massive savings. So the assistant has been really handy
in this regard. So to wrap things up, the Grafana assistant is pretty sweet
and has personally saved me a ton of hours. Now, if you've been
a long time Grafana user, it's going to rapidly increase
your productivity, and
if you're new to Grafana, the assistant is really going to have
you feeling like an expert in very short time. Yeah, that's vibeops. And if that term ends
up in a conference talk, just make sure to add
Grafana in the footnotes. I don't know if it's going to
catch on, but go check it out. Now, the assistant is now in public preview
and we really look forward to seeing how this saves you time. Take it easy.

