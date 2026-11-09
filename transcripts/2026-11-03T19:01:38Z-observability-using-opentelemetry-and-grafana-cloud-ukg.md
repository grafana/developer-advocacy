# Observability Using OpenTelemetry and Grafana Cloud: UKG

Published on 2026-11-03T19:01:38Z

## Description

UKG planned its move to Grafana Cloud as a 15-month project and finished it in under four months. Srikar Mohan and Christian ...

URL: https://www.youtube.com/watch?v=_nAX4rYB488

## Summary

The show titled "Observability Using OpenTelemetry and Grafana Cloud: UKG" was published on November 3, 2026. The speakers, Srikar Mohan, a Senior Manager at UKG overseeing observability, and Christian Kruger, who has been with UKG for about 15 years, discussed their successful migration to Grafana Cloud, which was initially planned as a 15-month project but completed in just four months. They highlighted the use of OpenTelemetry for tracing, the implementation of synthetic monitoring, and the establishment of GitOps for managing observability as code. Key takeaways included the importance of prioritizing essential capabilities, standardizing labels, and fostering collaboration among teams to ensure a smooth migration process. 

Topics: Grafana Cloud, OpenTelemetry, migration strategy, synthetic monitoring, GitOps, observability as code.

## Chapters

00:00:00 UKG's migration to Grafana Cloud in four months
00:06:22 Building synthetic monitoring capabilities at scale
00:12:58 Implementing label standardization and GitOps for observability
00:19:16 Implementing sampling and span metrics in OpenTelemetry

Good afternoon. I want to take you all back to October 2025. At UKG, we had just finished consolidating all of our metrics from various platforms into Grafana Cloud, and we were building a 15-month phased approach to move traces, synthetics, profiling, custom metrics, along with dashboards and alerts from another platform into Grafana. 

Then, on a Friday morning, we received a call from our leadership with a question: "Could we do this in four months?" The financial stakes were in the millions. Heading into the holiday season with a very complex cross-functional migration in front of us, we paused for a moment. Then we changed our plan. Rather than trying to deliver everything at once, we were deliberate in choosing what capabilities we wanted to move for the cutover, what could follow, and the guardrails we would need to move fast while keeping the platform sustainable. That's the playbook we're going to share with you today.

My name is Srikar Mohan, and I'm a senior manager at UKG. I oversee observability. I'm on stage with Christian Kruger. Outside of work, my wife and I enjoy the outdoors and hiking. This is a real picture; it's not AI-generated. If you find me in the hall, I'll be more than happy to talk about that. Christian, over to you.

Thanks, Srikar. Hello everyone, my name is Christian Kruger. Most people call me CK, and I've been with UKG for about 15 years now. These are some of the photos I took while I was in Peru. If you're ever planning a trip there, come see me afterward, and I'll be more than happy to give you some recommendations on food and great places to visit while you're there. I'm going to hand it back off to Srikar to go over how we made the migration possible.

So, a quick word about who we are. UKG is an AI-powered workforce operating platform. We bring together HR, payroll, workforce management, and human capital management solutions to organizations with frontline workers. We're leveraged in over 80,000 organizations globally. 

Now, why the frontline? Research suggests that more than 80% of the world's workforce are frontline workers. Think about hospital floors, hotels, airports, etc. That's what makes the software mission-critical. If scheduling, timekeeping, or payroll has a problem, a nurse is not on a roster, or someone is not getting paid. Our mandate was clear: we had to pull the finish line from January of 2027 to February of 2026. We had to make the migration through the holidays, executing 15 months' worth of work in just four months.

Now, we didn't want to simply lift and shift. We wanted to modernize as we moved, which meant leveraging OpenTelemetry for all of our tracing, onboarding our collectors into fleet management, and also using GitOps for everything. We wanted Observability as code because that would then allow us to implement guardrails. 

By the end of February 2026, here's what we ended up migrating: over 7,500 synthetic checks, more than 25,000 collectors onboarded into fleet with over 13,000 VMs and nodes sending traces in OpenTelemetry. We migrated 50 of the most used dashboards and 100 critical alerts. We also onboarded millions of custom metrics, and then there was the satisfying part of decommissioning our legacy platform.

So, how did we do all of this in four months? It came down to two decisions and the way of working. The first decision was prioritizing what was required on day one. Everything that you see on the left had to move on day one: traces with OTel, synthetics, custom metrics, the most business-critical dashboards and alerts, and also enablement through training. The things towards the far right, like profiling, real user monitoring, and any other dashboards or alerts that the team felt were required, would just fast follow.

The second decision was around the guardrails. First, we wanted to ensure that we had GitOps and Observability as code. The second was the use of standard labels. You define them once, but then you use them in many different areas like fleet management, dashboards, alerts, etc. The third was onboarding into fleet management itself because it's a central way of configuring and managing your collectors as well as Alloy.

Then there's how we work. This is not technical; we had to work as one team, which meant engineering, SRE, support, and even our vendor partner, Grafana, were all working as one team. We had daily sync-ups, escalations, chat channels, etc. I'll be honest, it took real commitment. We had to work weekends and late hours through the holidays to make this happen. We also didn't want to gatekeep; we wanted to enable our users. One way to do that was through self-service capabilities. 

So that was the strategy around how we focused on the migration. Now, we're going to get into how we built some of these capabilities one signal at a time. I'll start with synthetics and hand it over to CK.

Thanks, Srikar. One of the most critical areas we had to migrate at scale was synthetic monitoring. The goal was to define, deploy, and operate these checks consistently across all of our products. The main problem was repetition. For just one product, we had 485 clusters, and it all needed synthetic coverage. 

We decided to build out a centralized repository where we would house our K6 JavaScript templates that we created and translated from the previous platform's synthetics. Here’s how this would work: we would run our workflows and pass a list of clustered URLs that would then get defined as YAML in the repo. Terraform would then kick off and create these checks from within the Grafana UI. 

The output of this was 485 checks per template, each having the standard set of labels that we needed to build out our dashboards and synthetic alerts. We also had to take into consideration that teams were using internal synthetics, so we used Kubernetes to deploy private probes in each of the regions where applications resided. 

Most importantly, our templates in our repository became our source of truth, our gold standard. If we needed to improve the flow or fix a bug, we only needed to do it once in the repository, rerun the workflows, and redeploy. 

Once we defined the checks in the repo, we had to standardize how these checks behaved. Browser checks are sensitive to three things: cost, timing, and UI changes. So we defined six rules that we would use consistently. 

1. **Wait for the object**: We didn't want to use "wait for timeout" because this could artificially inflate how long it would take for your synthetic to run and finish, which is a cost factor. Instead, we used "wait for selector" and waited for the page to respond before continuing.
   
2. **Finish inside of a minute**: Billing rounds up per minute, and at our scale, cost mattered. A check that would run for 61 seconds would be billed at 120 seconds, so we put a PR review process in place to flag any checks that were taking longer than 60 seconds for review.

3. **Two results, then alert**: We wanted to alert on two consecutive failures and not one to avoid a situation where a flaky synthetic or a flaky run could cause a page for the on-call.

4. **Let cadence follow cost**: Simple browser checks can run every five minutes, while multistep journeys would run every 15 minutes because they took longer and cost more.

5. **Log on purpose**: Naming check assertions and having a log line per step were crucial for debugging synthetics from within the UI.

6. **Select by text and not by ID**: On modern browsers, IDs tend to regenerate across builds, so we wanted to use something that was more resilient to UI changes. We used visible text in the get by role so that if a developer decided to make a change in the UI, it wouldn't affect our checks.

You can see here by the numbers the amount of coverage and engineering work that...

this all took 7,500 checks migrated: over 4,000 browser checks, over 2,000 HTTP checks, and another 2,000 multistep scripted checks. We ended up with 360 k6 templates and about 25 checks per template. 

We did run into a few challenges throughout the process. The first was the reliability of some of these browser checks, and the second was resource utilization across our probes. Screenshots were also a non-negotiable, as we were already accustomed to using them on the previous platform. So, we partnered with the Grafana product team and the support team. They helped us overcome these challenges and put us into a private preview for screenshots within our environment.

Internally, we also faced a few challenges. We still had long-running checks that were driving up our costs. As mentioned before, we had the billing report and the PR review process that would flag these checks, and we would go back and try to enhance them to make them fit within the minute if possible. We also had to build out a centralized dashboard for the NOC to monitor the checks, as this was what they were used to on the previous platform as well.

The results of all this were more than just moving checks one by one. We built a GitOps platform for defining, deploying, and operating synthetic monitoring at scale, and we learned a lot through the challenges we faced. Now, after standardizing synthetics through our reusable templates and the GitOps repository, we wanted to apply the same approach across our Alloy configurations. This is where we introduced fleet management.

Before the migration, config ownership and management were decentralized. The observability team would push out the Alloy-based config using Ansible and Tanium, while engineers would push out their custom configs using their own scripts and repository workflows. This led to three challenges: 

1. Duplicate metrics across configurations, which was a cost factor as we were double dipping.
2. A lack of visibility and management over cardinality and the data points per minute that these configs had, another cost factor.
3. We didn't have the insight or knowledge ahead of time to know if a poorly written config was being pushed out that would cause our Alloy agents to crash or fail.

This is why we introduced fleet management as our centralized control plane. Configurations could now pull configs from a centralized location instead of waiting for us to run our scripts and push out to the hosts. Our configs became smaller, more manageable, individual pipelines that we could troubleshoot easier and include or exclude on deployments. Our collectors and pipelines were now labeled, so within the fleet management UI, we could associate the configs with the host based on the labels.

Now, how did we implement this? The first and most important thing was label standardization. We partnered with the SRE and engineering teams and defined a set of standard labels—eight of them—that we would use across our observability platform. The next step was a GitOps repository where we had our Alloy configurations defined, and we established a PR review process where observability now had control. Finally, we used Terraform to handle deployment details such as versioning and secrets, and to publish the Alloy configurations out into fleet management as pipelines and matchers.

As a byproduct of all this, the repo also gave us two additional capabilities. The first was version tagging and control, allowing us to roll back to a previous stable version if the current version had issues. The second was a PR review process where we could see the impact of cost and metrics ahead of time before publishing to production. 

The most important takeaway from all of this is that fleet management gave us one delivery mechanism for our current and future Alloy configurations. You can see by the numbers that this became more of an operating model than a one-time migration script or project. The migration was scoped and targeted; we didn't want to boil the ocean, so we focused only on the machines that had custom configs and trace configurations on the previous platform for the four-month window. 

By the end of February, there were over 50 pipeline templates per environment and over 25,000 collectors in fleet management. Fast forward to October, we now see over 100 pipeline templates per environment across four environments—over 400 pipeline templates—and over 80,000 collectors distributed among VMs and Kubernetes.

A key lesson I wanted to share is that if you plan on using Kubernetes and ephemeral resources, make sure to add the Kubernetes attribute and label so that fleet management knows to clean up any stale or stopped collectors from the inventory. It's just proper hygiene of your inventory, maintaining it up to date.

Today, all of our configurations are centrally governed, version matched by machine metadata, and no longer independently pushed out by the SRE and engineering teams. With fleet management as our delivery mechanism, we can now turn our attention to ingestion and deciding which metrics we wanted to keep and which ones we wanted to drop. 

We made a deliberate trade-off on the first day: we would ship everything from the previous platform and methodically prune using Grafana's adaptive metrics. We enabled the OTel receivers on our collectors and leveraged the OTel gateway because we ran into an issue where converting the metrics on the host was causing our memory to spike and our CPU to grow. We also applied a consistent 60-second scrape interval and the eight mandatory labels I mentioned previously, which cascaded down to our metrics and traces. This allowed us to use them for aggregation, filtering, building dashboards, and building alerts.

Then we waited. We observed for about a month and enabled Grafana's adaptive metrics and a GitOps repository so that we could aggregate away high cardinality, unique labels, and drop any metrics that we didn't use across dashboards or alerts. This helped us avoid developer changes; developers didn't need to redeploy the application, restart their services, or drop metrics or labels on their end. Instead, post-ingestion, we could use Grafana's adaptive metrics to decide what we wanted to keep. 

We also had a GitOps repository where we had the rules defined, so teams could come in, see the rules, and let us know if there were metrics we were dropping that they needed in future dashboards or alerts. Across the four stacks, we managed to reduce over 200 million series, and we have a weekly PR review process that notifies us of any unused metrics so that we could prune them.

That completes the metric side of the migration. I'm going to hand it back off to Srikar so that he can walk you through tracing and how we made trace collection selective and cost-conscious. Tracing was one of the most involved processes of the migration, and this is the one we engineered the most. 

Now, there were six problems we had to solve, starting with what standard to use for our trace library. Historically, we've been leveraging a lot of vendor proprietary trace libraries, which, as you all know, causes vendor lock-in. So, we wanted to use this as an opportunity to migrate to OpenTelemetry. We used OpenTelemetry across our Java, .NET, and Python applications. 

To move fast, we leaned more on auto instrumentation. The developers had a choice; they could leverage custom instrumentation to augment, but that was not required. Second, we standardized shared environment variables for things like service name, service function, environment, etc.

That you define it once and then you use it across all the different capabilities. 

**Third was controlled rollout.** Now, we instrumented a lot of services with OpenTelemetry across our production and non-production environments, but we were selective in capturing the traces. So, production environments were class citizens; we captured the traces. Non-production, by default, we would not capture them even though the application was configured with it. However, because we were using fleet management, if a certain team wanted tracing to be enabled on a set of VMs, it was very easy because we could just push that configuration from fleet management.

**Four, sampling with intent.** Now, tracing is subject to sampling. We started with a conservative approach. We wanted to use a combination of head and tail-based sampling. First, we kept 70% of the traces using head-based sampling. Then we implemented three policies for the tail-based sampling. The first policy keeps errors, the second policy keeps traces that are taking more than five seconds, and the third policy does a probabilistic 40% sampling. For all three policies, there was one common condition: a trace must have five spans because we didn't want to keep any trivial spans.

**Number five, our span metrics.** Now, there are two ways to calculate span metrics. One, you can use Grafana's Tempo-generated span metrics, but the problem for us is we're doing sampling. So, if we are generating metrics once it reaches Grafana, it's based on sample data. The second approach was to use Alloy and the OpenTelemetry Collector's native span metric generator. Here, we did three things. First, we defined the span name using the URL. The URL could contain query strings, UUIDs, and alphanumerics, which would drive up your cardinality. So, the span name would also undergo sanitization where those types of things are removed. 

Second, we only calculated span metrics on the route span because, as you know, a trace is made up of multiple spans, and the traces can get big; they could have thousands of spans. So, we only calculated span metrics on the route. We also defined one more rule where the span metrics would only get calculated for the type server. 

Then, the last challenge was around histograms. With span metrics, you also get histograms. If you don't define the buckets by default, OpenTelemetry will generate way too many buckets, which again drives up the cardinality. So, we explicitly defined anywhere between 6 to 7 buckets, ranging from a quarter of a second all the way to 300 seconds.

**So, here's a look at how our pipeline looked like within Alloy.** An application instrumented with OpenTelemetry will send its spans to a receiver. We would first drop unwanted spans, like health checks, etc. Then, the span name gets defined, and this will undergo the sanitization process I talked about. The stream is split into two. The top one will do the span metric calculation, where, if you notice, after it does the calculation, we again clean up the attributes—things that we don't need. Then it gets written to Prometheus via the OTLP gateway. 

The bottom pipeline talks about traces. After the head and tail-based sampling, we again undergo an attribute cleanup, dropping things we don't query or need. Then it gets written to Tempo. The key takeaway here is we sampled with intent and applied rules for the span metrics.

**Now, dashboards and alerts were the final two pieces of the puzzle.** We didn't export everything; we were also deliberate with these. We generated a prioritized list of dashboards, and the top 50 were chosen for conversion. Shout out to Grafana Professional Services for working very closely with our SREs and engineering partners on the AI-assisted dashboard migration. 

Dashboards had two challenges. One, the only way to validate is if you have telemetry flowing in, but we're in an active migration, so we had to wait for the data to show up. The second challenge is that because we're converting a dashboard from another platform into Grafana, the metric names and labels that are used will differ. So, you have to undergo a label mapping exercise, which required some rebuilds to be done. 

With alerts, it was slightly easier because we were already doing alerts through GitOps. But the same challenge of not being able to validate and the label mapping existed even with alerts. 

**So now that we have data coming in, how do you increase adoption? How do you enable your users?** Well, one obvious way is training, but this is where Grafana Assistant played a big role. Initially, Grafana Assistant was leveraged mostly within the Observability Team. We used it for asking questions about the platform, a lot about fleet management. But then, as users got onboarded, they found a lot of value. 

There was a great example from Rapid7 where an intern was able to figure out queries, or they didn't need to know the query; Grafana Assistant would help them build it. So, we went from analyzing data and understanding PromQL to now teams building entire dashboards with complex panels. They're able to do correlation. So, when there is an incident, even without launching investigations, you get a lot of value just by asking Grafana Assistant to figure out why something broke. 

As the volume grew, so did the value. So, four months, one platform, and pretty much everything a PR review away. That's the part we're most proud of. 

**If there are five things you want to take away from here:** 
1. If you're doing a migration this size, the reality is you can't get everything done at once. You have to prioritize the capabilities that you need on day one, what can follow, and most importantly, what are the guardrails required to keep it sustainable. 
2. Everything in GitOps, Observability as code. 
3. The standard labels: you define once and use it across many different capabilities. 
4. Designed for the bill: use sampling with intent, adaptive telemetry, and remember the six rules for synthetics. 
5. Probably one of the most important ones: you have to work as one team, have one cadence, involve your Grafana partner, and plan to be patient. 

So, to the folks at UKG, we have three team members here: Grafana accounts team, Grafana professional services team, the ObsCON team, and you, the audience. Thank you so much for being part of our journey. 

**We take some questions.**

## Raw YouTube Transcript

Good afternoon. I want to take you 
all back to October 2025. At UKG, we had just finished consolidating all of our 
metrics from various platforms into Grafana Cloud, and we were building a 15 month phased 
approach to move traces, synthetics, profiling, custom metrics, along with dashboards 
and alerts from another platform into Grafana. Then on a Friday morning, we get a call from our 
leadership with a question, "Could we do this in four months?" Now, the financial stakes were in 
the millions. Heading into the holiday season with a very complex cross-functional migration 
in front of us, we paused for a moment. Then we changed our plan. So rather than trying 
to deliver everything at once, we were deliberate in choosing what capabilities we wanted to 
move for the cutover, which could follow, and the guardrails we would need to move 
fast while keeping the platform sustainable. That's the playbook we're going to share 
with you today. My name is Srikar Mohan, I'm a senior manager at UKG. I oversee 
observability. I'm on stage with Christian Kruger. So outside of work, my wife and I, we like the 
outdoor. We like hiking. This is a real picture. It's not AI generated. So if you find me in the 
hall, I'll be more than happy to talk about that. Christian, over to you. Thanks, Srikar. And hello everyone, my name 
is Christian Kruger. Most people call me CK, and I've been with UKG for about 15 years now. 
These are some of the photos I took while I was in Peru. So if you're ever planning a trip there, 
come see me afterwards and I'll be more than happy to give you some recommendation on food 
and great places to visit while you're there. I'm going to hand it back off to Srikar to go 
over how we made the migration possible. So a quick word about who we are. UKG is 
an AI powered workforce operating platform. We bring together HR, payroll, workforce 
management, and human capital management solutions to organizations with frontline workers. We're 
leveraged in over 80,000 organizations globally. Now, why the frontline? So a research suggests 
that more than 80% of world's workforce are frontline. So think about 
hospital floors, hotels, airport, et cetera. And that's what makes the software 
mission-critical. So if scheduling or timekeeping or payroll is having a problem, a nurse is 
not on a roster, someone is not getting paid. So our mandate was clear. We had to pull 
the finish line from January of 2027 to February of 2026. We had to make 
the migration through the holidays, so 15 months worth of work to 
be executed in four months. Now, we didn't want to simply lift and shift. We 
wanted to also modernize as we moved, which meant leveraging OpenTelemetry for all of our tracing, 
onboarding our collectors into fleet management, and also GitOps for everything.
So we wanted Observability as code. Because that will then allow us to implement 
guardrails. So by the end of February 2026, here's what we ended up migrating. Over 7,500 
synthetic checks, more than 25,000 collectors onboarded into fleet with more than 13,000 
VMs and nodes sending traces in OpenTelemetry. 50 of the most used dashboards and 100 critical 
alerts were migrated. We also onboarded millions of custom metrics, and then the satisfying 
part of decommissioning your legacy platform. So how did we do all of this in four 
months? Well, it came down to two decisions and the way of working. So the first decision 
was prioritizing what was required day one. So everything that you see on the left had 
to move day one. So traces with OTel, synthetics, custom metrics, the most 
business critical dashboards alerts, and also enablement through training. Now the things towards the far right, 
like profiling, real user monitoring, and any other dashboards alerts that the team 
felt were required, that would just fast follow. The second decision was around 
the guardrails. So number one, we wanted to make sure that we have 
GitOps, we have Observability as code. The second was a use of standard labels. 
So you define them once, but then you use it in so many different areas like fleet 
management and dashboards, alerts, et cetera. And then the third was onboarding into fleet 
management itself because it's a central way of configuring, managing your collectors as 
well as Alloy. Then there's how we work. Now, this is not technical. We had to work as one team, 
which meant engineering, SRE, support, even our vendor partner, Grafana, we're all working as one 
team. We used to have daily sync ups, escalations, we had chat channels, et cetera. I'll be honest, 
it took real commitment. We had to work weekends, late hours through the holidays to make this 
happen. We also didn't want to gatekeep. We wanted to enable our users. And one way to do 
that was through self-service capabilities. So that was the strategy around how we focused on the migration. Now, we're 
going to get into how we built some of these capabilities one signal at a time. So I'll 
start with synthetics and hand it over to CK. Thanks, Srikar. One of the most critical areas we 
had to migrate at scale was synthetic monitoring. The goal was to define, deploy, and operate these 
checks consistently across all of our products. The main problem was repetition. For just one 
product, we had 485 clusters and it all needed synthetic coverage. We decided to build out 
a centralized repository where we would house our K6 JavaScript templates that we created and 
translated from the previous platform synthetics. Now, how this would work? We would run our 
workflows and pass a list of clustered URLs that would then get defined as YAML in the repo. 
Terraform would then kick off and create these checks from within the Grafana UI. The output 
of this was 485 checks per template that each had the standard set of labels that we needed to 
build out our dashboards and our synthetic alerts. And we also had to take into consideration that 
teams were using internal synthetics, so we used Kubernetes to deploy out private probes in 
each of the regions where applications resided. Most importantly from all of this, our templates 
in our repository became our source of truth, our gold standard. If we needed 
to improve the flow or fix a bug, we only needed to do it once in the 
repository, rerun the workflows and redeploy. Now, once we defined the checks in the repo, 
we had to standardize how these checks behaved. Browser checks are sensitive to three things, 
cost, timing, and UI changes. So we defined six rules that we would use consistently. 
The first of these was wait for the object. We didn't want to use wait for timeout because 
this could artificially inflate how long it would take for your synthetic to run and 
finish, which is a cost factor. Instead, we used wait for selector and waited for the page 
to respond before continuing. The next was finish inside of a minute. Billing rounds up per minute 
and at our scale, cost mattered. A check that would run for 61 seconds would be billed at 120 
seconds, so we put a PR review process in place to flag any checks that were taking longer 
than 60 seconds so that we could review them. The third one was two results, then alert. We 
wanted to alert on two consecutive failures and not one to avoid a situation where a flaky 
synthetic or a flaky run could cause a page for the on-call. The fourth was, let cadence follow 
cost. Simple browser checks can run every five minutes while multistep journeys would run every 
15 minutes because they took longer and cost more. The fifth rule, log on purpose. Name check 
assertions and a log line per step were crucial for debugging synthetics from within the UI. 
And the last one, select by text and not by ID. On modern browsers, IDs tend to regenerate 
across builds, so we wanted to use something that was more resilient to UI changes. We 
used visible text in the get buy roll so that if a developer decided to make a change 
in the UI, it wouldn't affect our checks. You could see here by the numbers, the amount of 
coverage and engineering work that this all took. 7,500 checks migrated over 4,000 browser checks, 
over 2,000 HTTP checks, another 2000 multistep scripted checks, and we ended up with 360 K6 
templates and about 25 checks per template. We did run into a few challenges though throughout 
the process. The first was the reliability of some of these browser checks, and the second 
was resource utilization across our probes. Screenshots were also a non-negotiable as we were 
already accustomed to using them on the previous platform. So we partnered with the Grafana product 
team and the support team. They helped us overcome these challenges, and they put us into a private 
preview for screenshots within our environment. Internally, we also had a few challenges. We still had long-running checks that were 
driving up our costs. So as mentioned before, we had the billing report and the PR review 
process that would flag these checks, and we would go back and try to enhance them and 
make them fit within the minute if possible. We also had to build out a centralized 
dashboard for the NOC to monitor the checks, because this is what they were used to 
using on the previous platform as well. The results of all this was more than 
just moving checks one by one. We built a GitOps platform for defining, deploying, 
and operating synthetic monitoring at scale, and we learned a lot through 
the challenges that we faced. And now after standardizing synthetics through 
our reusable templates and the GitOps repository, we wanted to apply the same approach across 
our Alloy configurations. So this is where we introduced fleet management. Now, before the 
migration, config ownership and management was decentralized. The observability team 
would push out the Alloy-based config using Ansible and Tanium while engineers would 
push out their custom configs using their own scripts and their own repository workflows. 
This led to three challenges. The first was duplicate metrics across configurations, 
which is a cost factor we were double dipping, and the second was a lack of visibility 
and management over cardinality and the data points per minute that these configs had, 
another cost factor. The final challenge was we didn't have the insight or knowledge ahead of 
time to know if a poorly written config was being pushed out that would cause our Alloy agents 
to crash and fail or not stirred up properly. This is why we introduced fleet management as 
our centralized control plane. Configurations collectors, sorry, could now pull and pull configs 
from a centralized location instead of waiting for us to run our scripts and push out to the hosts. 
Our configs became smaller, more manageable, individual pipelines that we could troubleshoot 
easier and include and exclude on deployments. And our collectors and our pipelines were 
now labeled so within the fleet management UI, we could associate the configs 
with the host based off the labels. Now, how did we implement this? The first and 
most important thing was label standardization. We partnered up with the SRE and engineering 
teams and defined a set of standard labels, eight of them, that we would use 
across our Observability platform. The next one was a GitOps repository where 
we had our Alloy configurations defined and we had a PR review process where 
Observability now had control. And finally, we used Terraform to handle 
deployment details such as versioning and secrets, and to also publish the Alloy configurations out 
into fleet management as pipelines and matchers. As a byproduct of all of this, the repo also 
gave us two additional capabilities. The first was we now had version tagging and control, and 
we could roll back to a previous stable version if the current version was having issues. And 
the second thing was a PR review process where we could see the impact of cost and metrics ahead 
of time before publishing out to production. The most important thing from all of this is that 
fleet management gave us one delivery mechanism for our current and our 
future Alloy configurations. Now, you can see by the numbers that this 
became more of an operating model than a one-time migration script or a project. The 
migration was scoped, it was targeted. We didn't want to boil the ocean, so we focused 
on only the machines that had custom configs and trace configurations on the previous platform 
for the four-month window. By the end of February, there was 50 plus pipeline templates per 
environment and over 25,000 collectors in fleet management. And you fast-forward to October this 
month, we see now over a hundred plus pipelines, pipeline templates per environment across four 
environments, so over 400 pipeline templates, and over 80,000 collectors distributed amongst VMs 
and Kubernetes. A key lesson I wanted to share is that if you plan on using Kubernetes and ephemeral 
resources, make sure that you add the Kubernetes attribute and label so that fleet management 
knows to clean up any stale or stop collectors from the inventory. It's just proper hygiene 
of your inventory, maintaining it up to date. Today, all of our configurations are centrally 
governed version matched by machine metadata and no longer independently pushed out 
by the SRE and the engineering teams. With fleet management as our delivery mechanism, 
we can now turn our attention over to ingestion and deciding which metrics we wanted to 
keep and which ones we wanted to drop. We made a deliberate trade-off on the first 
day. We would ship everything from the previous platform, and we would methodically prune using 
Grafana's adaptive metrics. We enabled the OTel receivers on our collectors, and we leveraged the 
OTel gateway because we ran into an issue where converting the metrics on the host was causing 
our memory to spike and our CPU to grow. We also applied a consistent 60-second scrape interval and 
the eight mandatory labels I mentioned previously, which cascaded down to our metrics and our 
traces so that within the Grafana UI, we could use them for aggregation, filtering, building 
dashboards, building alerts, and then we waited. We observed for about a month and enabled 
Grafana's adaptive metrics and a GitOps repository so that we could aggregate away high cardinality, 
unique labels, and drop any metrics that we didn't use across dashboards or alerts. This helped 
us avoid developer changes. Developers didn't need to redeploy the application, restart their 
services, drop metrics or labels on their end. Instead, post ingestion, we can use Grafana's 
adaptive metrics to decide what we wanted to keep. And we also had a GitOps repository where we 
had the rules defined so teams could come in, see the rules, and let us know if there was 
metrics we were dropping that they needed in future dashboards or alerts. So across the four 
stacks, 5,270 adaptive rules as code, we managed to reduce 200 million series, it's actually 
more than 200 million series now, and we have a weekly PR review process that notifies us of 
any unused metrics so that we could prune them. That completes the metric side of the migration. 
I'm going to hand it back off to Srikar so that he can walk you through tracing, and how we made 
trace collection selective and cost conscious. Tracing was one of the most involved processes of 
the migration. So this is the one we engineered the most. Now there were six problems we had 
to solve, starting with what standard to use for our trace library. Now historically, we've 
been leveraging a lot of vendor proprietary trace libraries, which as you all know, causes 
vendor lock-in. So we wanted to use this as an opportunity to migrate to OpenTelemetry. We used 
OpenTelemetry across our Java, .Net, and Python application. Now to move fast, we lean more on the 
auto instrumentation. Now, the developers had a choice. They could leverage custom instrumentation 
to augment, but that was not required. Second, shared environment variables. For things 
like service name, service function, environment, et cetera, we wanted to standardize 
on that so that you define it once and then you use it across all the different 
capabilities. Third was controlled rollout. Now we instrumented a lot of services 
with OpenTelemetry across our production and non-production environments, but we 
were selective in capturing the traces. So production environments was class citizen, so 
we captured the traces. Non-production by default, we would not capture them even though 
the application is configured with it. But because we were using fleet management, if 
a certain team wanted tracing to be enabled on a set of VMs, it was very easy because we could 
just push that configure of fleet management. Four, sampling with intent. Now 
tracing is subject to sampling. We started a conservative approach. We wanted to 
use a combination of head and tail-based sampling. So first, we keep 70% of the traces 
using head-based sampling. Then we implement three policies for the tail-based 
sampling. The first policy keeps errors, second policy keeps traces that are taking 
more than five seconds, and the third policy just does a probabilistic 40% sampling.
Now for all three policies, there was one common condition. A trace must have five spans, 
because we didn't want to keep any trivial spans. Number five, our span metrics. Now there 
are two ways to calculate span metrics. One, you can use Grafana's tempo generated span 
metrics, but the problem for us is we're doing sampling. So if we are generating metrics once 
it reaches Grafana, it's based on sample data. So the second approach was to use Alloy and 
OTel Collector's native span metric generator. Now, here also we did three things. One, 
we defined the span name using the URL. Now the URL could contain query string, 
it could contain UUIDs, alphanumerics, that will drive up your cardinality. So the span 
name would also undergo sanitization where those types of things are removed. The second, we 
only calculated span metrics on the route span because as you know, a trace is made up 
of multiple spans and the traces can get big. It could have thousands of spans. So we only 
calculated span metrics on the route. We also defined one more rule where the span metrics 
would only get calculated for the type server. Then the last challenge was around histogram. So 
with span metrics, you also get histogram. Now, if you don't define the buckets by default, OTel 
will generate way too many buckets. And that again drives up the cardinality. So we explicitly define 
anywhere between 6 to 7, ranging from quarter of a second all the way to 300 seconds. So here's a 
look at how our pipeline looked like within Alloy. So an application instrumented with 
OTel will send its spans to a receiver. We would first drop unwanted spans, like 
things like health checks, et cetera. Then the span name gets defined, and this will 
undergo the sanitization process I talked about. Then the stream is split into two. So the 
top one will do the span metric calculation, where if you notice, after it does the 
calculation, we again clean up the attributes, things that we don't need. And then it gets 
written to Prometheus via the OTLP gateway. The bottom pipeline talks about traces. 
So after the head and tail-based sampling, we again undergo a attribute cleanup. So things 
we don't query or we don't need, we drop them. And then it gets written to Tempo. The key 
takeaway here is we sampled with intent and then we also applied 
rules for the span metrics. Now, dashboards and alerts were the final two 
pieces of the puzzle. Now we didn't export everything, we were also deliberate with these. 
So we generated a prioritized list of dashboards, and the top 50 were chosen for conversion. 
Shout out to Grafana Professional Services for working very closely with our SREs and engineering 
partners on the AI assisted dashboard migration. Now, dashboards had two challenges. One, the 
only way to validate is if you have telemetry flowing in, but we're in an active migration, 
so we had to wait for the data to show up. The second is because we're converting a 
dashboard from another platform into Grafana, the metric name, the labels that 
are used will differ. So you have to undergo a label mapping exercise. So 
this required some rebuilds to be done. With alerts, it was slightly easier because we 
were already doing alerts through GitOps. But the same challenge of not being able to validate 
and the label mapping existed even with alerts. So now that we have data coming in, how do 
you increase adoption? How do you enable your users? Well, one obviously is training, but 
this is where Grafana Assistant played a big role. Initially, Grafana Assistant was leveraged mostly 
within the Observability Team. We used it for asking questions about the platform, a lot about 
fleet management, but then as users got onboarded, they found a lot of value. There was a great 
example from Rapid7 where an intern is able to figure out queries, or they don't need to know 
the query, Grafana Assistant will help them build. So we went from analyzing data, understanding 
PromQL, to now teams building entire dashboards with complex panels. They're able to do 
correlation. So when there is an incident, even without launching investigations, you get 
a lot of value just by asking Grafana Assistant to go figure out why something broke. So 
as the volume grew, so did the value. So four months, one platform, and 
pretty much everything a PR review away. That's the part we're most proud of. If there 
are five things you want to take away from here, number one, if you're doing a migration this 
size, the reality is you can't get everything done at once. You have to prioritize 
the capabilities that you need day one, what can follow, and most importantly, what are 
the guardrails required to keep it sustainable. Two, everything in GitOps, Observability as code. Three, the standard labels. You define once and 
you use it across a lot of different capabilities. Four is designed for the bill. So that means use 
sampling with intent, adaptive telemetry, and then remember the six rules for synthetics. And then 
lastly, probably one of the most important ones, you have to work as one team, have one cadence, 
involve your Grafana partner, plan to be patient. So to the folks at UKG, we 
have three team members here, Grafana accounts team, Grafana professional 
services team, the ObsCON team, and you, the audience. Thank you so much for being part 
of our journey. We take some questions.

