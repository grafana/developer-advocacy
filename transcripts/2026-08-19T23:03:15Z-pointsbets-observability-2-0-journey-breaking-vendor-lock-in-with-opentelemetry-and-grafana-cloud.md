# PointsBet&#39;s Observability 2.0 Journey: Breaking vendor lock-in with OpenTelemetry and Grafana Cloud

Published on 2026-08-19T23:03:15Z

## Description

PointsBet runs a fast-paced, high-stakes wagering platform across Australia and Ontario, Canada — where every second of ...

URL: https://www.youtube.com/watch?v=Q3HIPmQ_nrM

## Summary

The community call titled "PointsBet's Observability 2.0 Journey: Breaking vendor lock-in with OpenTelemetry and Grafana Cloud" was held on August 19, 2026, featuring Adam, a Staff Site Reliability Engineer at PointsBet. The discussion focused on PointsBet's transition to Observability 2.0, emphasizing the importance of breaking vendor lock-in through OpenTelemetry and adopting Grafana Cloud for a unified observability platform. Key takeaways included the need for a single source of truth for telemetry, the benefits of using OpenTelemetry for decoupling instrumentation from vendors, and the implementation of a dual export strategy to facilitate a smooth migration. Adam also highlighted the cultural challenges of adopting new observability practices and the role of AI in enhancing the observability experience.

Topics: Observability 2.0, OpenTelemetry, Grafana Cloud, vendor lock-in, telemetry management, AI in observability.

## Chapters

00:00:00 PointsBet's journey to observability 2.0
00:05:27 PointsBet's observability journey with OpenTelemetry
00:10:55 Scaling telemetry with the Alloy receiver and config management
00:16:22 Leveraging AI for observability and dashboarding

# PointsBet's Observability 2.0 Journey: Breaking Vendor Lock-in with OpenTelemetry and Grafana Cloud

I am here to talk to you all about PointsBet's journey to Observability 2.0, but more importantly, about breaking vendor lock-in with OpenTelemetry and making observability a first-class citizen within our organization.

## Introduction

My name's Adam. I am a Staff Site Reliability Engineer here at PointsBet, and I have been with the company for about five, five and a half years. I am part of the infrastructure team, which is similar to our platform team. We own the shared infrastructure and internal tooling, and we are really an enabling team. Our goal is to empower developers and delivery teams to ship code to production confidently and reliably. I specialize more in the observability and reliability front, hence the SRE title.

At PointsBet, we have a very Azure-oriented tech stack. The majority of our services are .NET applications, and most of these are hosted in the Azure Kubernetes Service. We also have a few Rust applications running around, as well as a small subset of our applications running on the PaaS ecosystem for things like app service plans and container apps.

## Who We Are at PointsBet

PointsBet is part of the wagering industry. We are an online gambling product, operating nationwide in Australia and in Ontario, Canada. In both Australia and Canada, we have a sports book offering. Specifically in Australia, we have a racing offering, which is a significant business period for us. In Ontario, Canada, we also have an online casino product.

## Importance of Observability

So why is observability important to us? You can compare a wagering platform to a trading platform. It is a very fast-paced, high-octane environment, especially during an incident. When you are in an incident, moments matter; every second counts. The longer your system takes to detect an issue, the longer it takes to triage and apply mediation for that issue. The impact grows exponentially, not only from a revenue perspective but also from a customer branding point of view. There are plenty of competitors out there, and customers will simply go to one of those if you cannot provide a reliable system for your end users.

Let me paint a little mental image for you. It's 2:00 AM. You receive an alert. You're cold, it's dark, and it's gloomy. This is what your desktop might look like before you've even found a single answer or started to triage. You can see here we have Jira for our incident management tool, PagerDuty for alerting and paging, Application Insights for app monitoring data, Datadog for infrastructure monitoring, and our Azure Managed Grafana instance—because why not? More dashboards are better. At the end of the day, you're not just debugging your system; you're also debugging your tools. Multiple sources of truth and multiple entry points.

## Identifying the Cracks

The cracks we identified that we needed to patch as an organization included scattered tooling. Our telemetry was split across Application Insights, Datadog, and Azure Managed Grafana dashboards. We were locked in; our telemetry was tied not only to our application but also to the vendor. We had blind spots—no RUM, no profiling, no SLOs. PagerDuty and Jira were bolted on the side, and we had obscure costing with multiple bills and no clear attribution. We could not identify which team, which signal, or which service was driving this.

## The Decision to Version

Why did we decide to version it? I first heard about Observability 2.0 probably about a year, year and a half ago, I think from Charity Majors. What was being said about Observability 1.0 was extremely relatable to us. We resonated with it. Our current environment and platform had many sources of truth and siloed tooling. We often debugged by intuition. Every organization has that kind of Oracle triage engineer who has been part of so many incidents that they are just great at triaging. We had obscure costing, but importantly, observability was always an ops afterthought. That was something we wanted to change.

With Observability 2.0, we wanted one platform—a single pane of glass with all the context brought into it: application, infrastructure, and business metrics. I used to say "correlate," but given the agentic world we're living in, "context" is a much more fitting term. We wanted one protocol with OpenTelemetry, clear cost and attribution, and observability that shipped with the feature and the product. At the end of the day, we didn't want to buy a tool for the applications; we wanted a platform for the entire operation—telemetry, alerting, costing, synthetics, incident response, profiling, whatever it might be.

## Why Grafana Cloud?

We did our due diligence and conducted a POC with New Relic, Datadog, and even revisited our Application Insights setup. Grafana Cloud came out on top. First of all, it is open by default, with OpenTelemetry and Prometheus native. There was no proprietary agent, and the exit ramp for us always stayed open if we ever needed it. Cost became a feature, not a surprise. We could break down spending and attribute it to a service, signal, or team. The use of Adaptive Telemetry gave us that transparent feedback loop—what we are using and what we're not using. We could bring in all that context into that single pane of glass to correlate everything: metrics, logs, traces, profiles. Now we're building one single story, not four different tabs. This also leads into AI that is shipping—an assistant to help us write queries and create dashboards, as well as conduct the first pass root cause analysis. We also get to choose the trade-offs. There will always be external data sources out there, whether from your cloud provider, Cloudflare, or Datadog, but we get to choose if we want to ingest this or simply query it.

## The Role of OpenTelemetry

Every great telemetry story starts with OpenTelemetry, and so did ours. OpenTelemetry provided the exit ramp; it decoupled how you instrument code from where you actually end up sending it. More importantly, it provides a shared protocol for all your different types of applications—.NET apps, Rust apps, Go apps, whatever it might be. OpenTelemetry is fundamentally a protocol, which was super important to us because it allowed our telemetry to break free from our vendor. 

As I mentioned, we are a .NET shop, all hosted on Azure. The Application Insights SDK was baked into every single one of these services, meaning that any tool change required us to re-instrument everything. So how did we do this? We were already on the journey and taking a manual instrumentation approach. However, we needed to move quickly and efficiently while providing some instrumentation consistency between applications. We decided to do this via an OpenTelemetry and OTel defaults package. I'm not going to say this is a recommended approach, but it is the approach that worked for us as an organization. Delivery teams were able to write this single...

line of code and we had variance for this between ASP.NET Core apps, isolated in-process function apps. But what they got for free was traces, metrics, and logs all exported. They got runtime, HTTP, and process metrics all instrumented. It was also dual export ready, which I'll touch a little bit on later. 

I would highly recommend everyone take a manual instrumentation approach when doing this because remember, to be observable also means to be intentful. True observability means that you are instrumenting with intent and you're instrumenting with purpose. If you don't have time to do this via the manual approach, that's fine. All the instrumentation is readily available. If you're running Kubernetes clusters as well, just use the OpenTelemetry (OTel) operator. It provides a very good foundation. 

But also take this time, if you are going down the manual approach, to review your telemetry. Remember, telemetry can never remain static. It needs to be iterated on as your source code changes. Telemetry that you wrote five years ago is probably not relevant today. So we also injected attributes at the deploy stage as well. Standards often do not fail if you're just writing them up in a Wiki page. I'm sure everyone has those Wiki graveyards lying around. So if you can inject things and enforce them, I highly recommend doing that. 

See here we've got OTel service name. We've got a service namespace as well. Now this relates back to our system name, our backstage catalog or service catalog, your service version, deployment environment, and our instance IDs as well. This is super critical for consistencies. A team cannot ship telemetry without a good labeling strategy. A team can also not ship telemetry that isn't attributed to a service, a system, or a version. This is what makes having dashboards, alerts, and cost attribution come for free and come automatic. 

Your attribution strategy might also differ depending on your hosting type. For example, if you're running Kubernetes clusters, you might want to enrich your telemetry for both app and infrastructure with those Kubernetes attributes. This is what provides a good user experience. When you provide that linkage between your application telemetry and your infrastructure telemetry, especially if you're using a tool such as Grafana.

So, the migration strategy: How do you migrate between one vendor to another without a flag day or a D-Day? You still need to set a deadline, but you don't need to set a hard cutover period. You can provide an overlapping period, providing a graceful rollout period for your delivery teams. This is what we did with that dual export approach. 

You can see here we have a single service running that OTel package, and all of our services were pushing telemetry to both Application Insights and also Grafana Cloud. This allowed teams to upskill and build at their own pace. The last thing that you want is teams waking up in the middle of the night triaging an incident on a tool that they do not know how to use. It also provides teams the opportunity to do a comparison between their old tooling and the new tooling as well. They can review and make adjustments if they need.

So, I want to touch a little bit on the collector and the collector layer as well. I highly recommend everyone implement the OpenTelemetry Collector. We originally didn't have the OTel Collector when we were pushing data to Application Insights, and we found a little bit of issues not being able to control these pieces of telemetry there. The Collector allows you to have full control of your telemetry. 

At this stage, we are enriching those pieces of telemetry with the Kubernetes attributes. It also provides a separation of concerns from your application and the processing of the telemetry. So all your processing for enriching, transformation, and sampling can all be hosted in the collector itself. We also did this with Fleet Management. Fleet Management provided us with a very strong user experience for that centralized navigation. We could see all of our pipelines, our connectors, config load statuses happening in real time, component health, and any config areas as well. 

A hot tip: If you are using Adaptive Telemetry and you have the Collector set up, take the rules from Adaptive Telemetry and implement them into your Collector because you will also save on your egress costs as well. 

So, how did we scale the Collector? Or more importantly, how did we scale the Alloy receiver? We did a few ADRs on this. We thought we were going to have a receiver per team, per deployment. But we decided to start off real simple: a single instance of the Alloy receiver, and it worked great. One Alloy receiver daemon was running a single endpoint. All apps were being ingested via that single cluster, the single collector. It worked really well until we started to run into a config management problem when we had multiple teams wanting to make updates to the collector at the collector layer. 

Now we realized we needed to scale the config. Instances themselves were fine, but how were we going to scale this config or the config management? We did this by implementing a separation of concerns. We, as the infrastructure team, would own the shared receiver pipelines and the shared exporter pipelines. As I mentioned before, we use service namespace as a labeling strategy so the individual teams could manage their own service namespaces for their own ownership. 

With this config, because we were also going on a GitOps journey, this allowed teams to have the config live alongside the application. You can kind of see where I'm going here with this: by enabling teams and empowering them to become fully autonomous. As their source codes change, they can also make updates to the collector layer as well if they need to.

So, what have we achieved so far as an organization? We've achieved a fair bit. We've done our application telemetry, metrics, logs, traces, profiles. We've ingested our cloud metrics. We've done our Kubernetes monitoring. We've also done our cost and attribution. At the end of the day, we want one platform that can answer three questions: What went wrong, why, and what did it cost? 

Speaking of cost, we have also estimated a 35% reduction in observability spend as well. Mind you, this is a conservative number. I think it's more around that 45% mark, but we always give ourselves a 10% buffer. More importantly, what we got was a mindset flip or a mindset shift with the feature of Adaptive Telemetry. Being able to provide us that transparent feedback allows us to either cut costs in areas that we don't need and either take those cost savings or reinvest them in areas that we do need. 

Developers were super concerned about the costing before they even started to ingest their telemetry into their new product. With the new tooling, we're actually encouraging developers to instrument the pieces of telemetry that they are unsure of regarding usefulness. Because again, you can just instrument it, check in the week. If you're using it, great. We found ourselves another unknown unknown. If you're not, then you can just drop it. 

For us as an organization, the hardest part wasn't about getting the data in. The technical side of things was actually the easiest part. The hardest part was the adoption phase. Culture change is hard. Complacency is a real thing, even with legacy tooling, especially if the tooling has been there for a couple of years. We weren't asking a single team to migrate over, which is a couple of teams. We're asking the entire organization to do a complete migration. 

With this comes patience. It will take time. It will take effort. You'll do sessions, you'll do workshops, and you'll likely have to repeat those same sessions and repeat those same workshops. Treat observability as a product. As users, as onboarding, as docs, as golden paths. Make sure that you run it like a product and help allow teams to treat observability as a feature of their own product.

Cool. So how did we do this? Well, what we did was we instilled observability champions. We had one champion per team, and these champions became our entry points or influence multipliers to all the rest of the delivery teams that we had. It's just human psychology as well that a team is probably more likely going to be influenced by an internal member than by external members.

With this, we did Grafana upskilling, alerting and dashboarding, coaching, OpenTelemetry (OTel) training, and documented golden paths. We also provided these champions with elevated permissions. We brought them along the journey with us. Champions scaled the coaching, and they made their adoption theirs.

One of the challenging parts for us was the alert migration, or rather operationalizing Grafana. Again, we needed to be ready for that on-call state. So we took a similar approach to the OTel package that I just showed you, and we created a set of plug-and-play templates. As an SRE team, we are often the observability SMEs. We managed a set of golden standard alerts or an alerting strategy, and we handled the complex queries in the background. 

What the delivery teams were able to do was leave a simple manifest file, input their service name, team name, the rules they wanted, and the severity as well. Things like error rate, latency, crash looping, whatever it might be. Now, the purpose of this isn't to write alerts for your developers or for your delivery teams. That's not what you want to do. The purpose of this is to save time for the delivery teams to get onboarded. It's to enable them with a smooth migration period and provide them a foundation and a starting point for them to build upon.

With this, we also took the same approach from our alerts to our dashboarding. Again, we've taken a set of templates. We've got a triage style dashboard and a retro style dashboard as well. With the retro dashboard, of course, we're looking at long-term trend analysis, trend patterns, and overall system summary. You've got shading in there during your busiest periods. For us, it's weekends, so you can analyze these patterns.

We took the same approach with these golden paths as we did with the alerts. However, this would not have been possible without a labeling strategy. Because we had attribution consistent across all of our services, we could simply have one dashboard with a whole set of filters in there. They could filter by cluster, service name, and service namespace. All the delivery teams can take this template, implement it, scope it directly to their services, and then use it as a foundation for them to build on. 

Again, the whole idea of this is to provide a starting point for your delivery teams while they upskill and tune or refactor at a later stage. Now, I've got a triaging dashboard over here as well. However, I do suspect that triaging dashboards might soon become obsolete. Rather than us looking at a dashboard like we traditionally have, we will probably just be having a conversation with the agent, which leads us to our next topic: AI, the newest adoption lever. 

Use AI as much as you can to your full advantage. It does the work for you. It can not only teach you but also help you find what you've missed. The capability for the Assistant to turn plain language into PromQL is very powerful. One of the biggest concerns we had was that if we migrated over to an observability platform, we would have to relearn the entire querying language. That tax no longer exists. You can use skills to teach your teams or teach your delivery teams. 

Something that we've been trialing is skills to review dashboards and alerts and provide recommendations based on the alerts that it's reviewing. There are a lot of resources out there for best standards and best practices. Allow the AI to look at those, and it can help you find what you're missing. Connect your MCP servers, or I'm sure you would have seen GCX being released at AI week. Also, connect it to the source code. Help it surface the telemetry and alerts that you lack. Help it find the unknown unknowns in your applications.

So before, I mentioned the querying tax; the triage tax is a lot worse. There's always going to be a delay from the time your systems detect there's an issue, to when you receive that alert, and then to when you get out of bed and look at your monitoring tools. The 20 minutes you spend at 2:00 AM deciding where to even look—Is it application? Is it infrastructure? Was it a recent deploy?—jumping between the tools just to form one hypothesis. Use the Assistant Investigations to do the first pass for you. You can even automate this as well. 

When you have a P1 alert that fires off, you can have that automated for you, but do be cautious with that. Tokens are a scarce commodity. If you have a noisy alert, it will just burn through all of your usage. Back in the days, triaging was a dashboard that we learned to read. It was a UI that we learned to navigate, look at spans, look in that waterfall view, and be able to draw the dots together. Instead, now I think it's becoming a conversation that you actually have with the agent itself. Dashboards will still remain, but they will serve as evidence.

So, the callback: This is where we are now. We've got the Grafana investigator running. It's walking through the telemetry, application infra, or any recent deploys. It's creating a cause hypothesis as well. At the end of the day, I'm not debugging my tools anymore. The investigations work great out of the box, but write rules, write skills, and have it fine-tuned to your service and to your system to provide that additional context. At the end of the day, now you're never debugging alone.

So what's next for us at PointsBet? Well, more signals, same pane, same single pane of glass, and same paved road. We're looking into doing RUM, front-end monitoring, database observability, Grafana Incident Response Management (IRM) as well from PagerDuty, and our business metrics data sources and our SLOs as well. 

I'll wrap it up with this: observability isn't just an ops afterthought that we should be bolting on after the page. It's a product feature that needs to be shipped with the code. Build a platform that the teams love, and they'll do the rest. That is it.

## Raw YouTube Transcript

I am here to talk to you all about
PointsBet's journey to observability 2.0, but more importantly, being able to break vendor lock-in
with OpenTelemetry and also making observability a first class
citizen within our org. So quick introduction. Who am I? What
do I do? Why am I here? My name's Adam. I am a Staff Site Reliability
engineer here at PointsBet, and I have been at PointsBet for
about five, five and a half years. I am part of the infrastructure team. Infrastructure team is that
similar to our platform team. You may have guessed it. We
own the shared infrastructure, shared internal tooling, and
we are really an enabling team. We not only are there to empower the
developers or the delivery teams to ship code to production, but we're here to empower them to ship
code confidently and reliably as well. I of course specialize more on the
observability and reliability front, hence the SRE title.
And here at PointsBet, we are a very heavy Azure-oriented tech
stack. Majority of our services are. NET applications and majority of
these as well are hosted in the Azure Kubernetes service. We do have a few Rust applications
running around there in the wild as well. And we do have a small subset of our
applications running on the PaaS ecosystem for things like app service
plans, container apps, et cetera. So who are we at PointsBet?
What do we do? Well, PointsBet is part of the
wagering industry. We are
an online gambling product. We offer this product to our customers. We operate nationwide in Australia and
we also operate in Ontario, Canada. In both Australia and Canada,
we have a sports book offering; specifically to Australia. We have a
racing offering, spring racing carnival, business period for us. And
in Ontario, Canada as well, we have a online casino product as well.
So why is observability important to us? Well, you can make a comparison of a wagering
platform to that of a trading platform. It is a very fast paced,
high octane environment,
especially during an incident. When you are in an incident,
moments matter, every second counts. The longer your system takes
to detect there is an issue, the longer that you take to triage
and apply mediation for that issue. Impact grows exponentially. Not only
from a revenue impact point of view, but also from a customer
branding point of view as well. There are plenty of competitors out there. Your customers will simply go and use
one of those if you cannot provide a reliable system for your end users. So I want to paint a little bit of a
mental image over here. It's 2:00 AM. You receive an alert. You're
cold. It's dark. It's gloomy. This is what your desktop might look like. This is what your desktop will look like
or what mine looked like before I've even found a single answer, before
I've even started to triage. So you can see here we've got Jira
for our incident management tool. We've got PagerDuty as well
for our alerting and paging. We've got Application Insights
here for our app monitoring data. We've got Datadog for our
infrastructure monitoring. And we've also got our Azure Managed
Grafana instance because why not? More dashboards are better.
At the end of the day here, you're not just debugging your system,
but you're also debugging your tools. Multiple sources of truth,
multiple entry points. Cool. So the cracks that we identified that
we as an organization needed to patch. Well, first of all, we had
that scattered tooling. Telemetry split across
application insights, Datadog, Azure Managed Grafana
dashboards. We were locked in. Our telemetry was not only
tied to our application, but it's also been tied to the vendor.
We had blind spots, no RUM, no profiling, no SLOs. Pager Duty and Jira
bolted on the side of this. And we had obscure costing as well.
Multiple bills, multiple tools, no clear attribution. Could not
identify which team, which signal, which service was driving this. So
why did we decide to version it? Well, I first heard Observability 2.0,
probably about year, year and a half ago. I think it was by Charity Majors. And what was being said
about Observability 1.0 was
extremely relatable to us. We really resonated with it. And this is what our kind of current
environment and platform was like. We had many sources of
truth. We had silo tooling. We often were debugging by
intuition. Often or not, I'm sure every org has that kind of Oracle
triage engineer that has been part of so many incidences that he's just a gun
at triaging. We had obscure costing, but importantly, observability
was always an ops afterthought. That's someone that we wanted to
change. Going over to observability 2.0, we wanted that one platform.
And with that one platform, we wanted that single pane of glass
with all the context bought into it. Application, infrastructure,
and business metrics. You noticed to use the word
context, probably if I had
done this six months ago, I would've used the word correlate, but just given the agentic
world we're living in, the context is a much small fitting term. We wanted that one protocol
with OpenTelemetry. We wanted clear cost and attribution, but we also wanted observability that was
shipping with the feature and shipping with the product. At the end of
the day for observability 2.0, we didn't want to buy a
tool for the applications. We wanted a platform for the entire
operation, telemetry, alerting, costing, synthetics, incident response,
profiling, whatever it might be. Cool. So why Grafana Cloud?
Well, we did our due diligence. We did a POC with New Relic, Datadog. We even revisited our Application Insights
set up and Grafana Cloud just came on top. First of all, open by default.
OpenTelemetry and Prometheus native. There was no proprietary agent and the
exit ramp for us always stayed open if we ever needed it. Cost became
a feature, not a surprise. We're able to break down spending and
attribute this to a service or a signal or a team. And also the use of Adaptive Telemetry
gave us that transparent feedback loop. What are we using? What we're not using? We're able to bring in all that
context in that single pane of glass to correlate everything, metrics,
logs, traces, profiles. Now we're building one single
story, not four different tabs. And that also leads
into AI that's shipping. Assistant to help us write the queries
for us and create those dashboards. And also the investigation does the
first pass root cause analysis. We also get to choose the trade offs. You're always going to have
external data sources out there, whether it be from your cloud provider,
Cloudflare, Datadog, sorry, Datadog, Databricks for business metrics. But we get to choose if we want to
ingest this or if we simply want to query this. Cool. So every great telemetry story kind of
starts with OpenTelemetry and so did ours. OpenTelemetry really
did provide the exit ramp. It really does decouple how you instrument
code from where you actually end up sending it. But also more importantly, it provides a shared protocol for all
your different type of applications. .Net apps, Rust Apps, GoApps, whatever
it might be. At the end of the day, OpenTelemetry really is a protocol. This was super important to us because
it allowed our telemetry to break free from our vendor. And that was super
important for us. As I mentioned, we're a .Net shop, all hosted on Azure. Application Insights SDK was baked into
every single one of these services. This meant that any tool change
required us to re-instrument everything. So how do we do this? Well, we were already on the journey and we
were taking a manual instrumentation approach. However, we needed to move
quickly and we needed to move efficiently. But at the same time, we wanted to provide some instrumentation
consistency between applications. And we decided to do this via a
OpenTelemetry and Otel defaults package. I'm not going to say this is
like a recommended approach. This is the approach that
worked for us as an org. Delivery teams were able to write this
single line of code and we had variance for this between ASP net core apps,
isolated improc function apps. But what they got for free was
traces, metrics and logs all exported. They got runtime, HTTP and
process metrics all instrumented. And it was also dual export ready, which I'll touch a little
bit on that later on. I would highly recommend everyone take
a manual instrumentation approach when doing this because remember
to be observable also
means to be intentful. True observability means that you are
instrumenting with intent and you're instrumenting with purpose. If you don't have time to do this
via the manual approach, that's fine. All the instrumentation
is readily available. If you're running Kubernetes clusters
as well, just use the Otel operator. Provides a very good foundation. But also take this time if you are going
down the manual approach to review your telemetry. Remember, telemetry
can never remain static. It needs to be iterated on
as your source code changes. Telemetry that you wrote five years
ago is probably not relevant today. So we also injected attributes
at the deploy stage as well. Standards often are not fail if you're
just writing them up in a Wiki page. I'm sure everyone has those
Wiki graveyards lying around. So if you can inject things and enforce
them, highly recommend doing that. See here we've got Otel service name.
We've got a service name space as well. Now this relates back to our system name, our backstage catalog or service
catalog, your service version, deployment environment,
our instance IDs as well. Super critical for consistencies. A team cannot ship telemetry
without a good labeling strategy. A team can also not ship telemetry that
isn't attributed to a service, a system, or reversion. This is what
makes having dashboards, alerts, and cost attribution come
for free and come automatic. Your attribution strategy might also
differ depending on your hosting type. For example, if you're
running Kubernetes clusters, you might want to enrich your telemetry
for both app and infra with those cube attributes. This is what
provides a good user experience. And when you provide that linkage between
your application telemetry and your infrastructure telemetry, especially
if you're using a tool such as Grafana. So the migration strategy. How do you migrate between one vendor to
another without a flag day or a D Day? You still need to set a deadline, but you don't need to set
a hard cut over period. You can provide an overlapping period, provide a graceful rollout
period for your delivery teams. And this is what we did with
that dual export approach. So you can see here we have a single
service running that Otel package and all of our services were pushing telemetry
to both application insights and also Grafana Cloud. This allowed teams to
upskill and build at their own pace. The last thing that you want is teams
waking up in the middle of the night triaging an incident on a tool
that they do not know how to use. It also provides teams to do a comparison
between their old tooling and the new tooling as well. They can review
and make adjustments if they need. So I want to touch a little bit on the
collector and the collector layer as well. Highly recommend everyone
implements the OpenTelemetry Collector. We originally didn't have the Otel
Collector when we were pushing data to App Insights and we found a little bit of
issues not being able to control these pieces of telemetry there. The Collector allows you to have
full control of your telemetry. And actually at this stage is where
we're enriching those pieces of telemetry with the Kube attributes. It also provides a separation of
concerns from your application and the processing of the telemetry. So
all your processing for enriching, transformation, sampling can all
be hosted in the collector itself. And we also did this
with Fleet Management. Fleet Management just provided us with
a very strong user experience for that centralized navigation. We could see
all of our pipelines, our connectors, config load statuses
happening in real time, component health and any config
areas as well. Hot tip as well. If you are using Adaptive Telemetry
and you have the Collector set up, take the rules from Adaptive Telemetry
and implement them into your Collector because you will also save
on your egress costs as well. So how did we scale the
Collector? Or more importantly, how did we scale the Alloy receiver?
So we did a few ADRs on this. We thought we were going to have a
receiver per team, per deployment. But we decided we'll
start off real simple. A single instance of the Alloy
receiver and it worked great. One Alloy receiver daemon
sit running single endpoint. All apps were being ingested via that
single cluster, the single collector. It worked really well until we started
to run into a config management problem when we had multiple teams wanting to
make updates to the collector at the collector layer. Now we realized
we needed to scale the config. Instances themselves were fine, but how were we going to scale this
config or the config management? So we did this by implementing
a separation of concerns. So us as infrastructure team would own
the shared receiver pipelines and the shared exporter pipelines.
And as I mentioned before, we use service name space as a labeling
strategy so the individual teams could manage their own service name spaces for
their own ownership. With this config, because we were also going
on a GitOps journey as well, this allowed teams to also have the
config live alongside of the application. So you can kind of see where I'm going
here with this by enabling teams and empowering them to become fully
autonomous. As their source codes change, they can also make updates to the
collector layer as well if they need be. So what have we achieved so far as
an org? We've achieved a fair bit. We've done our application telemetry,
metrics, logs, traces, profiles. We've done our cloud metrics all ingested.
We've done our Kubernetes monitoring. We've also done our cost and
attribution. At the end of the day, we want one platform that can answer
three questions. What went wrong, why, and what did it cost? Speaking of cost, we have also estimated a 35% reduction
in observability spend as well. Mind you, this is a conservative number. I
think it's more around that 45% mark, but we always give ourselves a
10% buffer. But more importantly, what we got was a mindset flipped
or a mindset shift with the feature of Adaptive Telemetry. Being able to provide us that transparent
feedback allows us to either cut costs in areas that we don't need and either
take those cost savings or reinvest them in areas that we do need. Developers
were super concerned about the costing before they even started to ingest
their telemetry into their new product. With the new tooling, we're actually encouraging developers to
instrument the pieces of telemetry that they are unsure of, of the
usefulness. Because again, you can just instrument it, check in
the week. If you're using it, great. We found yourself another
unknown unknown. If you're not, then you can just drop it. So for us as an org, the hardest part
wasn't about getting the data in. The technical side of things
was actually the easiest part. The hardest part was the adoption
phase. Culture change is hard. Complacency is a real thing,
even with legacy tooling, especially if the tooling has
been there for a couple of years. We weren't asking a single team to
migrate over, which is a couple of teams. We're asking the entire org
to do a complete migration. With this comes patience. It will
take time. It will take effort. You'll do sessions, you'll do workshops, and you'll likely have to repeat those
same sessions and repeat those same workshops. Treat observability as
a product. As users, as onboarding, as docs, as golden paths. Make sure that you run it like a
product and help allow teams treat observability as a feature
of their own product. Cool. So how did we do this? Well, what we did was we instilled
observability champions. We had one champions per team, and these champions became our entry
points or influence multipliers to all the rest of the delivery teams that we had. It's just human psychology as well that
a team is probably more likely going to be influenced from an internal member
than the external members. But with this, we did Grafana upskilling, alerting and
dashboarding, coaching, Otel training, documented golden paths. We also provided these champions
with elevated permissions as well. We brought them along the journey with us. Champions scaled the coaching and
they make their adoption theirs. So one of the challenging parts for
us was the alert migration or rather operationalizing Grafana. Again,
ready for that on-call state. So we took a similar approach to the
Otel package that I just showed you, and we created a set of plug and play
templates. We as a SRE team, obviously, majority of the time you're
the observability SMEs. So we managed a set of golden standard
alerts or an alerting strategy, and we managed the complex
queries in the back. And what the delivery teams were able
to do was leave a simple manifest file, input their service name, team
name, the rules that they want, and the severity as well. Things like
error rate, latency, crash looping, whatever it might be. Now, the purpose of this isn't to write
alerts for your developers or for your delivery teams. That's
not what you want to do. The purpose of this is to save time for
the delivery teams to get onboarded. It's to enable them with a
smooth migration, period. Provide them a foundation and a
starting point for them to build up on. With this, we also took the same approach from our
alerts also to our dashboarding as well. So again, we've taken a set of templates. We've got a triage style dashboard
and a retro style dashboard as well. With the retro dashboard, of course,
we're looking at long-term trend analysis, trend patterns, overall system summary. You've got shading in there as well
during your busiest periods. For us, it's weekends. So you can
analyze these patterns. We took the same approach with these
golden paths as we did with the alerts. However, this would have not been
possible without a labeling strategy. Because we had attribution consistent
across all of our services, we could simply have one dashboard with
just a whole set of filters in there and they could filter by cluster,
service name, service name space. All the delivery teams can take
this template, implement it, scope it directly to their services, and then use it as a foundation
for them to build on. Again, the whole idea of this is to provide a
starting point for your delivery teams whilst they upskill and tune
or refactor at a later stage. Now I've got a triaging dashboard
over here as well. However, I do soon suspect that triaging
dashboards might soon become obsolete. And rather than us looking at a
dashboard like we traditionally have, we will just probably be having
a conversation with the agent, which leads us to our next topic
as AI, the newest adoption lever. Use AI as much as you can to your full
advantage. It does the work for you. It can not only teach you, but it can
also help you find what you've missed. The capability for the Assistant to be
able to turn plain language into the PromQL is very powerful.
One of the biggest, not say challenges or I would say concerns
we had was if we migrate over to an observability platform, we're going to have to relearn
the entire querying language. That has been taken away from
you. That tax no longer exists. You can use skills to teach your
teams or teach your delivery teams. Something that we've been
trialing out with as well. We've got skills to review dashboards
and alerts and provide recommendations based on the alerts that it's reviewing. There's a lot of resources out there
for best standards and best practices. Allow the AI to look at those. And it
can help you find what you're missing. Connect your MCP servers, or I'm sure you would have seen GCX being
released at AI week. Also connect it to the source code. Help it surface
the telemetry and alerts that you lack. Help it find the unknown
unknowns in your applications. So before I just mentioned
about the querying tax, the triage tax is a lot worse. Okay? There's always going to be a delay by
the time your systems detect there's an issue, by the time you receive that alert, and by the time you get out of bed and
look on your monitoring or get onto your monitoring tools. The 20 minutes that you spend at
2:00 AM deciding where to even look, is it application? Is it
infrastructure? Was it a recent deploy? Jumping between the tools
just to form one hypothesis. Use the Assistant Investigations
to do the first pass for you. You can even automate this as well. So
when you have a P1 alert that fires off, you can have that automated for
you, but do be cautious with that. Tokens is a scarce commodity.
If you have a noisy alert, it will just burn through all of
your usage. But back in the days, triaging was a dashboard
that we learned to read. It was a UI that we learned to
read and navigate, look at spans, look in that waterfall view and be able
to draw the dots together. Instead, now I think it's becoming a conversation
that you actually have with the agent itself. Dashboards will
still remain there, but they will remain there as evidence. So the callback. This is where we are now. We've got the Grafana
investigator running. It's walking through the telemetry
application infra or any recent deploys. It's creating a cause hypothesis
as well. At the end of the day, I'm not debugging my tools anymore. The investigations work great out of
the box, but write rules, write skills, and have it fine true to your service
and to your system to provide that additional context. And at the end of
the day now you're never debugging alone. So what's next for us at PointsBet?
Well, more signals, same pane, same single pane of glass and same paved
road. So we're looking into doing RUM, front end monitoring,
database observability, Grafana IRM as well from PagerDuty, and our business metrics data
sources and our SLOs as well. So I'll wrap it up with this, that observability isn't just an ops
afterthought that we should be bolting on after the page. It's a product feature
that needs to be shipped with the code. Build a platform that the teams
love and they'll do the rest. That is it.

