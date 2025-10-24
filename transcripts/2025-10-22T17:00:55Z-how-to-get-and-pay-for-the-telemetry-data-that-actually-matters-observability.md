# How to Get (and Pay For) the Telemetry Data That Actually Matters | Observability

Published on 2025-10-22T17:00:55Z

## Description

At ObservabilityCON, Dee Kitchen, Sean Porter, and Rich Kreitz share how Grafana Cloud helps teams scale observability ...

URL: https://www.youtube.com/watch?v=ZhMvR8uaJ8w

## Summary

In this video, Sean Porter and Rich from Grafana discuss the advancements in telemetry and cost management within SaaS economics, focusing on the introduction of Adaptive Telemetry, Adaptive Traces, and Adaptive Profiles to enhance observability and reduce costs. Sean presents the concept of Adaptive Telemetry, which aims to filter out unnecessary data while retaining valuable insights, thereby saving costs and improving system efficiency. He explains Adaptive Traces and their intelligent sampling techniques that allow users to focus on high-value traces while reducing noise. Rich then shifts the conversation to cost management, emphasizing the importance of visibility and accountability in spending, and introduces Grafana's new cost management features that enable teams to set alerts for spending thresholds, allocate costs to specific teams, and unify billing data across different platforms. The overall message encourages organizations to optimize their telemetry and cost management practices to foster a culture of accountability and efficiency.

## Chapters

Here are the key moments from the livestream along with their timestamps:

00:00:00 Introductions and Overview of the Session  
00:01:30 Introduction to Adaptive Telemetry and its Importance  
00:03:00 Sean Porter’s Keynote Recap on Adaptive Telemetry  
00:05:45 Deep Dive into Adaptive Metrics: Usage Statistics  
00:08:15 Announcement of Adaptive Traces and Profiles  
00:10:00 Explanation of Tracing and its Benefits  
00:12:30 Challenges with Traditional Tracing and Noisy Data  
00:15:00 Introduction of Adaptive Traces Sampling Techniques  
00:20:00 Demonstration of Policy Creation for Adaptive Traces  
00:25:00 Overview of Adaptive Profiles and Its Significance  
00:30:00 Rich's Segment on Cost Management and Billing Strategies  
00:35:00 Explanation of Cost Attribution and Its Importance  
00:40:00 Introduction to Focus: An Open Standard for Cost Data  
00:45:00 Summary of Key Takeaways and Closing Remarks  

These timestamps provide a clear guide to the major topics discussed during the livestream.

# Transcript Cleanup

I'm actually only going to be up here for a few minutes because they asked me to speak. They wanted me to tell you all about the databases, adaptive telemetry, and a lot of the cost attribution of things as well. I'm covering the topic of **SaaS Economics Reimagined**—how to run at scale and do this in an efficient way. 

However, I didn't want to come up here as a manager trying to tell you things because, honestly, who cares? So, I wanted to bring up two practitioners. We’re going to hear from one and then the other.

First, we have Sean Porter, who you heard from yesterday in the main keynote. He discussed Adaptive Telemetry and Adaptive Profiles. He will give you a deep dive into what that is, how it works, how you can use it, and how it will be valuable to you.

There is an underlying theme to this: in Sean's startup, he had a phrase that resonated with us—**"Every trace worthy of your attention."** And as soon as we saw that, we thought, "How about all telemetry?" Right? All telemetry is worthy of your attention. You should only pay for what is valuable to you, and the rest should not incur costs. 

With that in mind, here's Sean to give you the lowdown.

---

**Sean Porter:**

It's great to be up here again. Thank you, Dee, for that nice intro. I want to apologize upfront; some of the things I say may be almost verbatim from yesterday's keynote, but it'll really stick this time.

**Adaptive telemetry** is the grand vision we're all working towards. It's about eliminating noise, extracting the signal, and making every byte stored worthy of attention, whether that's metrics, logs, traces, or profiles. 

Adaptive Metrics kicked it all off. We have over 3,900 organizations already using it, and in total, we've dropped 16 billion active series—on average, 1.4 billion a month. That's a big number! Last year, Adaptive Logs went generally available. We built Adaptive Logs twice as fast as we built Adaptive Metrics. Already, over 380 organizations are using it, and we've dropped a total of 12 petabytes of less valuable log lines.

Today, we are here to announce—well, yesterday we announced—**Adaptive Traces** and **Adaptive Profiles**, and we will dive into those solutions in depth. 

Tracing is powerful; it provides end-to-end visibility as requests traverse your complex and distributed systems. It's a telemetry signal for deep visibility. 

**Story time:** It’s 3:00 AM, and a team member is paged. They wake up, groggy, and check their traces. They see that the checkout system is succeeding only about 12% of the time. They can look through that trace, see the whole request narrative, and identify that the fraud detection component is timing out or experiencing a high number of errors. They discover there's a call to a third party, which made a very small change to the API at 2:45 AM. After a simple code change and deployment, the incident is resolved. 

Tracing in this case provided the full context, making it easy to pinpoint the problem and fix it quickly. However, the issue is that traces are often very noisy, producing an overwhelming amount of data that can be cost-prohibitive. Most of these traces represent normal successful operations, which generally are not of much interest. The real insights come from the small percentage of traces that indicate errors, performance issues, or unusual patterns. 

With **Adaptive Traces**, we focus on only keeping the valuable ones—those worthy of your attention. You send all your traces to Grafana Cloud, and we intelligently sample them. This gives you immediate cost savings and reduces noise, making it easier to navigate your traces and understand what's going on. This greatly reduces the toil for the day-to-day operator. 

A significant benefit is that it also simplifies system instrumentation. Auto instrumentation is fantastic, but about 70% of that information is likely unnecessary. Let Adaptive Traces handle that toil for you. Engineers will spend far less time sifting through traces, helping them identify issues faster. 

Essentially, **Adaptive Traces** unlocks the true potential and value of traces for you. Distributed tracing relies on sampling as a fundamental necessity due to the sheer volume of data. Do you really need all that data? Most organizations use a sampling technique known as head sampling, which makes a decision at the start of the request without understanding the request's outcome. 

**Adaptive Traces**, on the other hand, use **tail sampling**. At the end of a trace, we bring everything together, inspect the complete context, and make an informed decision. Additionally, we can utilize AI and ML capabilities to analyze these full traces, which can be very beneficial for various techniques and models.

With Adaptive Traces, you're shifting from random sampling to intelligently sampling what truly matters—what has value. Thankfully, we have a recommendation engine to assist in creating sampling policies. This sampling policy determines which traces are kept, stored, or dropped. 

When you start using Adaptive Traces, it will provide foundational policies. These are broad strokes, not overly interesting, but they give you an idea of how Adaptive Traces works. Here are three examples:

- Capture a probabilistic representation of 5% of everything. This provides your baseline, including some successful operations so you know what the good data looks like.
- Capture errors and slow traces to compare with that baseline.

We continuously analyze your adaptive traces after you start, using the trace data to recommend additional policies. For example, if you have a service consuming 80% of your spend without providing much value, we can adjust that. Conversely, if a service produces traces only once an hour or once a day, we might increase its sampling frequency.

If your teams are already familiar with OpenTelemetry and tail sampling, those policies will work out of the box with Adaptive Traces. Shortly after creating your first policy, you'll see a dramatic reduction in the number of traces stored in Tempo.

The numbers displayed on the screen are from our internal ops cluster, which represents our average rates per second. We're processing 2.5 gigabytes per second and storing just shy of 400 megabytes per second—an 84% reduction. There are times we see spikes up to seven gigabytes per second, but this gives you an idea of the scale and effectiveness of Adaptive Traces in action.

As mentioned earlier, we continuously analyze your traces and produce recommendations for you. We also use AI and ML capabilities to monitor your services for unusual behavior and anomalies. 

For instance, we can examine P90 latency for a service. You have your normal operation, which starts to thrash and then spikes, triggering an incident. We have systems automatically analyzing all your services for this type of anomalous behavior, capturing the relevant traces preemptively.

Here’s an example of how this works. If you start using Adaptive Traces today, you will see policy details showing anomaly policies. We use machine learning models to forecast P90 latency and focus on capturing traces when that threshold changes. 

We have a deep investigative workflow, making it easy to see if an anomaly policy was triggered. You can click the drill-down button to view relevant traces, facilitating investigative triage.

Now, let’s discuss how to get started with Adaptive Traces. It’s straightforward. Initially, we recommend a single policy called **First Policy**, which captures a probabilistic sample of everything. You simply click this button to apply the recommendation.

By applying this first policy, we will start to see a reduction in traces. We recommend foundational policies that can be applied with just a click. For example, we can set a policy for capturing slow traces—anything over 10 seconds—and apply it. If 5% seems too high or low, you can easily edit that policy. 

For instance, you might want to change it to 10%—but please, rename the policy to something more descriptive, like **Sample 10%**, and update it. By editing, the policy is immediately applied across all samplers in the background. 

Adaptive Traces is incredibly robust and reliable. While OpenTelemetry is fantastic, it can be challenging to create a robust pipeline with those components. We've built a robust system that can take live updates without dropping or losing data.

When we return to the overview page, we can apply new policies. For instance, we can create a policy to capture traces containing errors. This could result in an impressive reduction, nearing a 99% reduction rate, which will stabilize and depend on the policies in play.

In another stack already running with several policies, including a current anomaly, we can analyze how the system behaves. In this case, we are using the OTel demo stack to produce data. 

As we observe the forecasts, we see that peaks correspond with captured traces. If we click drill down, we can continue the investigative workflow to see the services involved with that anomaly and examine the traces. 

At any time, you can create a new policy, such as **Important Service**, which allows for a more focused sampling approach. 

If you're familiar with OpenTelemetry and its tail sampling processor, we support all those policies. You can create an **AND policy type**, which combines multiple policies together. 

If you want to learn more about these individual policy types, we have a booth outside, and we can delve into those details.

Alright, I don't want to use up all the time now. Rich has a whole segment to cover as well. Let’s switch back to the slides, and I’ll talk about **Adaptive Profiles**.

---

**Rich:**

Awesome! It wasn’t enough to do just one. Previously, we transitioned from metrics to logs in a year, and now we’re tackling the last two in the final year—profiling. Profiling is an underutilized signal, and most of you probably don’t use it. However, it’s incredibly powerful because it enables you to go from a signal to a specific line of code. You can identify optimization opportunities—changing a single line could reduce CPU usage by 5%. 

With **Adaptive Profiles**, you can send all of your profiles from either Pyroscope SDKs or Alloy collectors to Grafana Cloud, and we will intelligently sample them. By default, we apply a cost-effective baseline sample rate of only 10%. This aggressive rate does not compromise the structure of the traces, meaning your heat graph will appear as it should. 

When there’s significant change within the shape of a profile over time, we react by increasing the sample rate to 100%. This anticipates the need to closely examine that profile and kicks off a workflow where we conduct LLM analysis to identify what’s wrong, what’s interesting, and what the optimization opportunities are.

The true value lies in these insights. If we trigger a resolution bump, we run the workflow. This is an example of the output. Again, this is from a demo stack, so it may not be the most captivating profile, but we can make specific recommendations for improvements. For example, if a function calls too often, reducing the frequency can lead to significant cloud cost savings.

With **Adaptive Profiles**, teams can deploy continuous profiling at scale as never before, at a lower cost than ever seen. This will enable you to optimize your cloud spending and simplify debugging.

Now, let’s do a quick demo before I hand it over to Rich. This is what you will see when you enable Adaptive Profiles. All you need to do is click a button to enable it, ensuring that the LLM plugin is configured for your stack. That’s all it takes. You’ll immediately see roughly a 90% reduction. 

You can apply a higher sampling rate for specific services if needed. At any point, if you want to increase the sampling rate for a brief period, you can do so with just a click. 

This is what an insight typically looks like—it provides a flame graph and makes several recommendations on how you might want to change your application. If you click the drill-down button, you can see the sample rate applied over that time. 

Overall, **Adaptive Profiles** enable continuous profiling, looking for anomalies and generating insights. If you’re interested in Adaptive Profiles, I hope you are, you can use this QR code to sign up for the private preview. I would love to discuss how this can help you!

Now, I’d like to hand it over to Rich, who will talk about cost management and billing.

---

**Rich:**

Thank you, Sean. Observability is usage-based, which is both a strength and a risk. One chatty service, one debug flag left on, or one high cardinality label can cause your costs to spike overnight—perhaps on a Friday deployment. 

Come Monday, Finance pings Engineering and asks, "Did we really mean to spend this?" The answer is usually, "We don’t know yet." By the time you know, it’s too late—the money has already been spent. These surprises erode trust; Engineering feels blindsided, and Finance feels exposed. Conversations that should be about reliability become conversations about budgets. Nobody wants that.

So, what’s the real problem here? Latency has dashboards, errors have SLOs, but costs usually only show up on an invoice. If the first time you see a spike is on a billing statement, you’ve lost the most important thing you have—time to react.

We want to make costs a first-class signal. If we can alert when latency exceeds 500 milliseconds, we should also alert when logs surpass 500 gigabytes. If we can route incidents to service owners, we should be able to route spend to the teams that created it. If we can normalize metrics and traces, we should be able to normalize bills so that everyone is looking at the same numbers. 

This is the shift we want to make with Grafana Cloud. We call it moving from **cost chaos to cost clarity**, and it happens in three steps:

1. **Prevent:** We send cost and usage signals to the control loop you already trust. We provide easy, human-readable alerts sent to Slack, email, or your preferred webhook, allowing you to build your bill while there’s still time to act.
   
2. **Assign:** When costs are visible, behaviors change. We use the labels you already have to break one big bill into slices by team and service. Every dollar has an owner, and owners can act.

3. **Unify:** Every vendor has a different billing language—AWS, GCP, Grafana Cloud. This fragmentation costs your Finance and FinOps teams hours to reconcile. With **Focus**, a cost-based open standard, there’s one schema that both Engineering and Finance can use to view the same numbers in the same way—apples to apples across all your vendors.

As we saw with Sean’s presentation on Adaptive Telemetry, we want you to get the right data at the right resolution so you only pay for signal and not noise. The real win here is cultural. When costs become visible, behaviors change. Teams can budget, optimize, and analyze their spending just as they manage latency and reliability. Costs become observable, assignable, and open.

Now let me show you how we do this in Grafana Cloud. This is our new cost management and billing app, which was released just last week in GA. The team has done an amazing job visualizing how we view your bill today. 

The front page offers a high-level view of your spend, commitments, month-to-month trends, and a breakdown by product. I’m going to click into the usage alerts tab. We’ve made alerting for billing really easy, all contained within the cost management app. 

I’m going to create a new usage alert. You can now alert on your total spend or on usage, and I’ll choose logs. As I do this, the graph will shift to display my current logs usage for the month. I can also look back to see historical trends or set a budget if I know what it is. 

I’ll set the budget to two terabytes of logs. We now have a yellow line indicating my budget for the current billing period. We provide predefined alerts based on different thresholds, and I’ll create alerts to notify me when my spend reaches 95%, 85%, and 70% of my budget. 

I can choose where I want these alerts to go, and I’ll send them to Slack. Once created, I now have cost management alerts that will notify me of my spend levels throughout the month, giving teams real-time insights. 

**Step 2: Assign.** For Assign, we have cost attributions, which let you define labels across all your signals, mapping them to one team or service. You can configure this for metrics, logs, and traces. 

If I scroll down, I can see the different breakdowns for metrics, logs, and traces. We see the usage values, dollar values, and these are mapped to the labels I’ve defined. The goal is for these attributed values to match your actual bill cent for cent, enabling reconciliation with Finance. 

**Step 3: Unify.** Today, every vendor has a different billing language and values. This costs the team time to reconcile spreadsheets, moving data, and spending hours trying to match your spend across CSPs and observability products. 

**Focus** is an open standard for cost and usage data. Grafana Labs supports open-source initiatives, making this integration a no-brainer. This provides a common schema so all your data comes into one format within the tools you already use—no more spreadsheet wrangling or one-off sheets. 

In summary, all your costs become observable, actionable, and fair. As we saw with Sean, **Adaptive Telemetry** allows you to pay for signal, not noise. Alerts help you prevent surprises, so you can catch spending early and take action. Cost attribution lets you assign costs to different teams for accountability. Finally, Focus provides a unified view of billing data, enabling your teams to understand and optimize spend effectively. 

Thank you very much!

## Raw YouTube Transcript

I'm actually only going to be up here for
a few minutes because they asked me to speak and they asked me to come up here
and actually tell you all about the databases and adapt to telemetry and a
lot of the cost attribution of things as well. And I'm covering the SaaS
economics reimagined and this is how to run at scale and how to
actually do this in efficient way. But what I didn't want to do is be up
here as a manager and trying to tell you things because who cares? So I actually wanted to actually bring
up two practitioners and we're going to hear from one and then the other.
Sean Porter, you heard from yesterday, he was in the main keynote talking
about Adaptive Telemetry and Adaptive Profiles, and he's going to come up first and
give you a deep dive into what that is, how it's going to work,
how you can use it, and how it's going to be valuable to you. There is an underwriting thing to this, which is in Sean's startup, he had a phrase and a
phrase resonated with us, and the phrase was every trace
worthy of your attention. And as soon as we saw that,
we were just like, yeah, but how about all telemetry? Right? All telemetry worthy of your attention. You should only sort of pay for that
which is valuable to you and the rest you should kind of like. You
shouldn't have the cost of that. So with that in mind, here's
Sean to give you a low down. Alright, it's great to be up here again,
thank you Dee for that nice intro. I'm going to go ahead and
first I'm going to apologize. Some of the things are going to be kind
of almost verbatim from yesterday's keynote, but it'll really stick this time. Adaptive telemetry, this is the grand
vision we're all working towards and it's really about getting rid
of the noise, extracting the signal, and making every bite stored worthy of
attention, whether that's metrics, logs, traces, or profiles. So Adaptive Metrics kicked it all off. We have over 3,900
organizations already using it, and in total we've dropped
16 billion active series on average 1.4 billion a month
now, and that's a big, big number. Last year, Adaptive Logs
went generally available. We built Adaptive Logs twice as
fast as we built Adaptive Metrics. Already, there's over 380 organizations
using it and we've dropped a total of 12 petabytes of less valuable log lines.
Today we're here to announce, well, yesterday we announced Adaptive Traces
and Adaptive Profiles and we're going to dive into those solutions in
depth. Tracing is powerful. Again, it provides end-to-end
complete visibility as requests. Traverse your complex
and distributed systems. Really it's a telemetry
signal that's for deep visibility. Story time, it's 3:00 AM a team member is paged.
They wake up, they're all groggy. They go to their traces. They see that the checkout system
is only succeeding about 12% of the time. They can look through that
trace, that whole request narrative. They can see the fraud detection component
is timing out or experiencing a high amount of errors. With that, they
see there's a call to a third party. They look at that and it turns out the
third party made a very small change to the API at, say, 2:45 in the morning. Small change to the code, deploy
it, incident is over and resolved. Tracing in this case gave you
that full context of that, made it really easy to dial in and where
you need to address the problem and you could fix it quickly. Problem
is, traces are very noisy. They produce an overwhelming amount
of data that is also very cost prohibitive. Most of these traces represent
normal successful operations. You really generally don't
give a hoot about these ones. The real insights come from the small
percentage of traces that are around errors, performance issues,
unusual patterns and so forth. Extracting the signal from those and
paying attention to those is what you need to do with traces. So, Adaptive Traces, we're focused on keeping
only the valuable ones, the ones worthy of your attention. You send all of your traces to Grafana
Cloud and we'll intelligently sample them. You get immediate cost savings and it
gets rid of all that noise and makes it a lot easier to go through your traces
and figure out what's going on. Really reduces the toil for
the day-to-day operator. A big benefit of this is also it makes
it a lot easier to instrument your systems. Auto instrumentation
is absolutely fantastic, but boy, it's like 70% of that information
you probably don't even need or use. So you can let Adaptive Traces take
care of that toil and reduce it for you. Engineers spend far less time
sifting through their traces, helping them identify
issues faster. So really, Adaptive Traces is unlocking
the true potential and value of traces for you. So, distributed tracing
inherently relies on sampling. It's a fundamental necessity.
There's just too much data. Do you really need all the data? No. So most organizations actually employ a
sampling technique referred to as head sampling. This is making a decision at the very
beginning of the request without any understanding or knowledge of what's
going to happen for that request. It's just a sophisticated
random method of sampling. Adaptive Traces used, what's
referred to as tail sampling. We basically at the end of a trace, we bring it all together and we
have all that complete context. We can inspect the whole trace
and make a decision then, when you know everything about it. What's also cool about
Adaptive Traces is we can use AI ML capabilities to look
at these full traces at the end. All that context can be very beneficial
for these kind of techniques and models. With Adaptive Traces, you're essentially shifting
away from sample randomly and pray and hope, to intelligently
sample what actually matters, what has value. So thankfully, we have a recommendation engine to help
with the creation of sampling policy and Adaptive Traces. Sampling policy is
what's determining what traces are kept, stored, or dropped. So when you start using Adaptive
Traces, out of the gate, it'll give you these kind of foundational
ones. These are very broad strokes, not so much interesting, but it certainly helps you get an idea
of how Adaptive Traces works and how to create policies. So,
here's three examples. Let's just capture
probabilistic representation. 5% of everything. This
gives you your baseline. This will include some of the successful
operations so you know what the good stuff looks like, and then we have these other policies
to capture errors and slow traces so you can compare with that baseline. What's really neat is that
we'll continuously analyze
your adaptive traces after you start with these ones
and from that trace data, we'll determine what other policies
we should recommend to you. Perhaps you have a service that's
consuming 80% of your spend and you're not really getting that much value out of
it. So let's adjust that, reduce it, and perhaps you have a few services
that only produce traces once an hour or once a day or a week or month. Perhaps
we should sample those more often. Of course, you can always use custom
policies to really laser focus. You and your teams know what's important
to you and you can represent that as policy. Now, if you and your teams are already
familiar with OpenTelemetry and you're attempting to do tail sampling, all of those policies will just work
out of the box with Adaptive Traces, copy paste, away you go. These are few types we
support and gives you an idea of what capabilities
are there for you to utilize. Shortly after creating your first policy, you'll see a dramatic reduction
in the amount of traces stored in Tempo. These numbers on the screen are
actually from our internal ops cluster. They represent kind of our
average rates that's per second. So we're doing 2.5 gigabytes
per second in this internal cluster and restoring just shy of 400 megabytes a second, so
that's an 84% reduction. There are times we get spikes where we
go up to seven gigabytes per second, but this is the average. This is an idea of the scale and
also the effectiveness of Adaptive Traces in action. So as mentioned earlier
and during the keynote, we continuously analyze your traces
and we produce recommendations for you, but we also use AI and ML
capabilities to monitor your services for weird behavior, for service anomalies. This infographic, if you will, represents
like a P 90 for latency for service. You have your kind of normal
operation and then its steady state, started thrashing, started changing and then spiked and
then you had an incident triggered. So we have systems that are automatically
at scale looking at all of your services for this kind of anomalistic
behavior so that we can have it automatically capture the relevant traces, preemptively assuming that this behavior
is going to eventually lead to an incident. So here's an example of one in action, and
if you go to use Adaptive Traces today, this is what you'll see under policy
details. For anomaly policies, the top is a little hard to see on the
size of the screen here, but we're using, in this case a machine learning
model for forecasting P 90 latency and we're not so
interested about capturing traces above that threshold. We're interested in capturing
traces when that threshold changes. So when it spikes, we automatically create a policy that
will capture traces with spans with those attributes and then we'll cap
it. So we're not going to, maybe an anomaly actually
equates to 80% of your trace volume. You wouldn't want to capture everything
and then blow up your bill or make Tempo cripple and fall over. So we actually
limit the intake so you can see, we can forecast anything that falls
out of it we're going to capture. And what's really neat is we have this
kind of deep investigative workflow, so it's really easy to see, hey, I
have an anomaly policy or I had one. Click the drilldown button, takes you into drilldown traces and you
actually see the relevant traces that were captured. It makes it really easy to do
investigative triage with traces. Alright, so I'm going to just first show you
what it looks like to get started with Adaptive Traces. It is very
straightforward. Out of the gate, we're going to just recommend a
single policy called First Policy. I know not very creative, but it's
going to do a probabilistic sampling, so it's going to capture
a baseline of everything. All I have to do is click this
button, apply recommendation. Unfortunately somebody hijacked
my stack earlier today, so there's a little
bit of weird data here, but we'll see now with that first policy, we're going to start to have a
reduction from our traces going through. Now out of the gate we recommend those
foundational policies and I can apply them with a click of a button.
So if I look at this one here, it's just recommending, hey,
let's just get slow traces. So anything greater than 10 seconds, if I click apply, it created the policy, I
can go look at my policies. So there's that first policy we
created by turning on Adaptive Traces. So we're capturing 5% and then
we're capturing slow traces. What's really important to note,
I'm sure you're looking at like 5%, that's either far too high or
far too low for us. No problem. It's quite straightforward to edit
that policy and make a change to it. Let's say 10%, but please
for the love of God, rename the policy something
more interesting like sample 10% and update. There we go. And what's interesting
is that by that editing, it's immediately applied to your sampling.
So in the case of our ops cluster with that one,
I showed the numbers earlier, we're doing 2.5 gigabytes per second. Some fun nerdy tidbits there. There's several hundred
samplers behind the scenes, and when you edit that policy, we're
immediately applying to all of them. What's also fantastic
about Adaptive Traces, is it is extremely robust and reliable. If you and your teams are
familiar with OpenTelemetry, while it's fantastic and
has all these capabilities, it is hard to make a robust
pipeline with those components. While we're leveraging OpenTelemetry
standards and componentry. With Adaptive Traces, we've made an incredibly robust system
that can take these live updates without dropping and losing data. If I
go back to the overview page, I can go apply, let's
just dismiss that one. That's an artifact of a weird bug. And this one I'll apply to
grab traces containing errors. Wow, that's an impressive reduction. So we're at almost 99% reduction rate. This will change and settle in
and it really depends on what my policies in play. So I have
another stack already running. This one has a few more
policies and including a current anomaly that's been detected. So what's happened here with this stack, this is using the OTel demo
stacked to produce data. But here if I look at here, that
one, let's choose an interesting one. We can just click through. Alright, this one works pretty good.
So this is a checkout cart. You can see the forecast down below. So you can see we're doing them all
and anytime things have kind of fallen outside of what we
expected and these bands, you can see that these peaks
on the forecast correspond
with us capturing traces that are relevant to it.
If I click drilldown, I can continue that investigative
workflow and I can see what the breakdown looks like, what services were actually
involved with that anomaly, and I can look at the traces themselves. This is a very boring trace,
not a good one to look at, but you get the sense of
the capabilities here. So at any time as well,
you can go in here, you can create a new policy and let's do important service. I like
the name of that one. So again, if you're familiar with OpenTelemetry
and the tail sampling processor that exists there, we support
all those policies. Most often in the not, you're going to be doing what's
called an and policy type. This allows you to combine
multiple policies together. So here in the example, it's giving me a string
attribute policy that's matching off of service name. So perhaps you have a aspect of your
infrastructure or your services that are just too critical to sample too
aggressively or they're too noisy. You can drill in on specific service. And here the example is saying let's just
apply a probabilistic sampling policy in addition to that. So the traces have to be touching
that service and we'll do a 20%. There are a number of
policy types in here. You could do rate limiting.
You can do, again, if you're really familiar and
really deep in the weeds with OTel, OTTO conditions. You may
not like yourself that much, but that's what we have to do. But yeah, so you can really just drill in. If you want to learn more about
these individual policy types, we have the booth outside, please come by and we can get into the
nitty gritty of those details. Alright, I don't want to use up
all the time now, Rich. You've got a whole shtick to do as well. Let's switch back to the slides and I'm
going to talk about Adaptive Profiles. Awesome. So yeah, it wasn't
enough to do just one. Previously we went from
metrics to logs in a year. We had to outdo ourselves and do
the last two in the final year. Profiling. Profiling is a
very underutilized signal, and most of you probably don't use it, but it's incredibly powerful because
it gives you the ability to go from a signal to a line of code. You can point at this is the
optimization opportunity, changing this line or
reduce CPU usage by 5% by continuously profiling across
your infrastructure all the time, not just looking for optimizations
and shutting it down, but run it all the time, it can be
an incredibly useful and viable tool. So with Adaptive Profiles, you can send all of your profiles
from either Pyroscope SDKs or Alloy collectors to Grafana Cloud and we'll
intelligently sample them. By default, we apply a cost-effective
baseline sample rate of only 10%. We found this fairly aggressive
sample rate to not compromise the structure of the traces, meaning you can look at your heat
graph and everything looks as it should. Now when there's enormous change
within the shape of a profile over a window of time, we react to that and increase the
sample rate to a hundred percent. Basically we anticipate the
need to look at that profile. It also kicks off a
workflow that we run LLM analysis of it and we can
look at what's wrong with it, what's interesting about it, what are
the opportunities that relate to it? Did somebody introduce a
regression and so forth. I think the true value of this
is definitely in these insights. So if we trigger that resolution bump, we run the workflow. This is an
example of the output. Again, this is from a demo stack, so it's
not the most interesting profile, but we can make very specific
recommendations of the
improvements you should make. This one, yes, find nearest vehicle. This is just calling time too often. Maybe you should just do
it once and do assignment. It's silly things like this that actually
equate to huge reductions in cloud costs though. Seems some overly simple, but these regular
expressions most of the time. So with Adaptive Profiles, teams can deploy continuous
profiling at scale as never seen before, at a lower cost
than ever been seen before. This is going to give you the ability
to optimize your cloud spend and simplify debugging. Alright, quick demo
and then I'll hand it over to Rich. Save myself the trouble of having to have
a separate stack for showing you this disclaimer. This is a screenshot, but this is what you'll see when it
comes to turn on Adaptive Profiles. What you need to do it is
you basically click a button, enable and make sure the LLM plugin
is configured for your stack, and that's all it takes to enable it. And immediately you'll see roughly a
90% reduction, greater than the 85%. Why I say the average is an
85% reduction is to give buffer for that anomalistic behavior, so spikes in resolution to
support that insights workflow. Here you can see two days
ago there were some insights, but I think I'll go and we'll
get another service. So, I've applied that 10%
baseline to everything, but you can also get more
specific per service. So if you feel like it's
either compromising the
shape of your profiles or you just want a higher resolution
on the get-go or the regular, you can accomplish it. So let's
do already have checkout service, fraud detection, and we can add it here. Now at any time, if I am not going to wait
for an anomaly to occur, I can click a button to increase the
sampling rate and you can say I want to increase it for say one
minute and then it's the demo as a reason. I'm just
going to increase it. So just like Adaptive Traces can
dynamically apply policy across Adaptive Traces, clicking that button will immediately
impact the sample rate for the ingestion of these profiles. Now within one minute
we'll get some fresh insights in here, but while we're waiting, let's just
look at what they can look like front. There we go. So this is what an
insight typically looks like. So it basically gives you the flame
graph and then makes a number of recommendations of how
you might want to change your application. If I click
the go to drill down button, you can see it had this sample rate
applied to it over this period of time. By any point, I can look
at function details, just wait for a minute and then I can
view on GitHub if I had the integration working for this component. But in a gist, that's what Adaptive Profiles looks like.
So you turn it on, does that baseline, looks for anomalies when
there's anomalistic behavior, you get insights. Insights tell you how to change
your application to improve the performance of your app. If you're
interested in Adaptive Profiles, and I hope you are, you can use this QR code to sign up for
the private preview and I love to have conversations with you, find out why you're interested with
profiles and how this can help you and yeah, it's incredibly exciting.
If you don't profile today, Adaptive Profiles is a
great excuse to start today. I would like to hand it over to Rich
and he is going to talk about cost management and billing. Thank you Sean. Observability is usage based. This
is both a strength and a risk. One chatty service,
one debug flag left on, one high cardinality label and
your costs can spike overnight. Maybe it happens on a
Friday deploy. Monday, Finance pings engineering and asks, "Did we really mean to spend this?" The
answer is usually we don't know yet. And by the time you do know it's too
late, that money's already spent. These surprises are more than just
about numbers. It erodes trust. Engineering feels blindsided,
finance feels exposed. Conversations that should
be about reliability, become conversations about
budgets. Nobody wants that. So what's the real problem
here? Latency has dashboards, errors have SLOs, but costs
usually only show up on an invoice. If the first time you see a
spike is on a billing statement, you've lost the most
important thing you have, time to react.
So we want to make costs a first class signal. If we can alert when
latency passes 500 milliseconds, we should be able to alert
when logs cross 500 gigabytes. If we can route incidents
to service owners, we should be able to route spend
to the teams that created it, and if we can normalize
metrics and traces, we should be able to normalize bills
so that everyone's looking at the same numbers. This is the shift we
want to make with Grafana Cloud. We call it moving from
cost chaos to cost clarity, and it happens in three
steps. Step one is prevent. We send cost and usage signals to
the control loop you already trust. We have easy human readable
alerts sent to Slack, email, or the web hook of your choice so you
can get alerts to build your bill where there's still time to act. Step two is assign. When costs
are visible, behaviours change. We use the the labels you already have
to break one big bill into slices by team and service. Every dollar has an owner and owners
can act. And step three is Unify. Every vendor has a different
billing language. AWS, GCP, Grafana Cloud. This fragmentation costs your finance
and FinOps teams hours to reconcile. With Focus, a cost-based open standard, there's one schema that both engineering
and finance can use to look at the same numbers the same way. Apples to
apples across all your vendors. As we saw with Sean
with Adaptive Telemetry, we want you to get the right data at
the right resolution so you only pay for signal and not noise. But the
real win here is cultural. When costs become visible,
behaviors change. Teams can budget, optimize and look at their spend the
same way they deal with latency and reliability. Costs become observable, assignable, and open. So I'm going to show
you a little bit of how we do this in Grafana Cloud. So this is our new cost
management and billing app. This was released just
last week now in GA. And the team has done an amazing job
of visualizing how we look at your bill today. So this is the front page kind of gives
you a high level view of your spend, commit, what your trending month to month, and a bird's eye view of
your breakdown by product. I'm going to click into
the usage alerts tab. We've made alerting for
billing really easy, all contained within
the cost management app. I'm going to go ahead and create
a new usage alert and you can now alert on your total spend or on usage, and I'm going to choose
logs. Now as I do this, the graph here is going to shift to
what my current logs usage is for that month. I can also go back in time to see
what this trend has been historically, or if I know what my team's budget
is, I can put that in as well. So I'm going to choose two
terabytes of logs here. Now we'll put that in. We get the yellow line up there that
shows this is what my budget is for this current billing period. So that's
what this is for this month, and we have predefined alerts for
you based on different thresholds. You can add your own here, but I'm going to create alerts because
I want to know when my spend gets to 95, 85 and 70% of my alerts, and we see the lines show
up in the graph here, scroll down and I can choose where I
want the alerts to go and I'm going to choose to send this to
Slack and I create alerts and that's all it takes. I now have cost management alerts that
are going to alert me when my bill gets to these different
thresholds within the month. So this gives your teams time to act
rather than waiting for the end of the month when the bill's already spiked. They can react in real time to
address what these are doing. Step two is assign. For Assign, we have cost attributions. Cost attributions lets you define
labels across all your signals. So they map to one team, one service. We let you configure that differently
for metrics, logs, and traces. All these products use different semantics
and different ways they kind of use labels. We can map that to
one team. So if I scroll down, I can see here that here's all my
different breakdowns for metrics, logs and traces. We see the usage
values, we see the dollar values, and these are being mapped to the
different labels that I've defined. This is ordered by dollar
value and we see at the very top, this is unattributed. So the goal here is we want
these attributed values
to match cent for cent to your actual bill. So you can
actually reconcile this with finance. If you're doing show backs or chargebacks, then it's super important to
understand how this works. If you have a bucket of
money in unattributed, then you're going to want to look at your
labeling strategy so you can actually get teams to label properly
so that you can charge them. We also support different months. So
this is the month to date billing period. You can go back in time to see what your
attribution was in different periods. And of course we do have an export to CSV. So if you want to import this into
spreadsheets or different tooling, we've made this really
easy as well. The whole goal with cost attribution is to give
teams visibility into their spend so they can manage it, so they can know where
they're at and actually budget for it. If we go back to the
slides, the third step is Unify. So today, every vendor
has a different billing language, different values, different
ways they roll things up. This costs the team lots of
time to reconcile spreadsheets.
They're moving data, they're transforming it. Spending hours and hours trying to
match what your spend is between CSPs, between observability and
all your SaaS products. Focus is an open standard
for cost and usage data. And Grafana Labs loves open source. So this was a no-brainer for us to adopt. This gives you a common schema so that
all your data's coming into one format in the tools that you already use. No more
spreadsheet wrangling, no more parsers, no more one-off sheets. This gets you all the data together
so that your teams can spend less time trying to manipulate data, and spend more time understanding your
spend and optimizing how that works. So let's bring all this
together. As we saw with Sean, Adaptive Telemetry lets you
pay for signal and not noise. Alerts help you prevent surprises
so you can catch spend early and actually do something about it. Cost attribution lets you assign cost
to different teams so that they can own what that cost is. And focus is an open standard that lets
you look at all of your billing data in the same format so you can concentrate
on optimizing your spend rather than manipulating data. The outcome of this is all of
your costs become observable, actionable, and fair. That's Grafana Labs. Thank you very much.

