# Now GA: Full-stack Observability with the Grafana Cloud Knowledge Graph (Formerly Asserts)

Published on 2025-10-22T16:35:27Z

## Description

See how Grafana Cloud's Knowledge Graph (previously Asserts) turns complexity into clarity. In this demo from ObservabilityCON, ...

URL: https://www.youtube.com/watch?v=sUTx90rWI-g

## Summary

In this video, Cedric, a product manager at Grafana Labs, along with Manoj, the VP of Engineering, discusses the introduction of the Knowledge Graph in Grafana Cloud, which aims to enhance root cause analysis by addressing the complexity of modern application development. They highlight the challenges posed by disparate data sources and the need for a unified experience to facilitate observability. The Knowledge Graph transforms raw data into structured insights, connecting various entities like services, databases, and infrastructure to deliver meaningful, contextualized information for users. Key features include a consolidated entity catalog, contextual insights, and the ability to integrate custom knowledge into the system. The video also showcases a demo where Manoj effectively utilizes the Knowledge Graph for root cause analysis, emphasizing its capability to simplify complex investigations and improve user experience. The Knowledge Graph is now available to all Grafana Cloud users, including free tier subscribers.

## Chapters

Here are the key moments from the livestream with timestamps:

00:00:00 Introductions and overview of the session  
00:02:30 Discussing the complexity of modern application development  
00:04:45 Introduction of Asserts and its impact on Grafana Cloud  
00:06:00 Announcing the Grafana Cloud Knowledge Graph  
00:08:15 Explanation of what a Knowledge Graph is and its purpose  
00:10:45 Insights into how the Knowledge Graph works with various data sources  
00:13:30 Unified experience through the consolidated entity catalog  
00:16:00 Proactive insights and their importance to users  
00:19:30 Demonstration of root cause analysis using the Knowledge Graph  
00:23:00 Introduction of Grafana Assistant for automated insights and investigations  
00:26:30 Recap of the demo and concluding remarks on the Knowledge Graph's benefits  

These timestamps capture the key moments discussed in the livestream, highlighting the introduction of new features and concepts.

# Faster Root Cause Analysis with Grafana Cloud and the Knowledge Graph

Hello everyone, and welcome to London. My name is Cedric, and I’m a product manager at Grafana Labs. Joining me is my friend and the VP of Engineering, Manoj. Today, we’re going to discuss the Knowledge Graph and how it enables faster root cause analysis.

## The Problem: Complexity in Modern Systems

Before we dive in, let’s talk about the problem we’re trying to solve. As highlighted in the keynote, the primary issue is **complexity**. Modern application development and deployment scenarios involve multiple layers of complexity, including:

- Kubernetes
- Containers as a service
- Functions as a service
- Virtual machines
- Bare metal
- Dozens of programming languages and containerization

All these elements in your systems emit events, signals, data logs, metrics, traces, and profiles. The challenge is that most of these signals reside in silos, making it hard to get a complete picture of your system. This disjointed experience impacts users and those who depend on the system when problems arise. 

## The Solution: Grafana Cloud and the Knowledge Graph

Now that we understand the problem, let’s discuss our solution. Last year at ObservabilityCON, we announced the general availability of **Asserts** in Grafana Cloud. Up to that point, Grafana Cloud was primarily visualization-centric, helping you visualize your data and navigate your systems. Asserts took it a step further by introducing proactive insights through a curated root cause analysis workflow, enabling much faster root cause analysis.

Asserts created a graph across all layers of the application and infrastructure, helping users understand the network effects between the two. It provided out-of-the-box UI dashboards for known object types, driving Service Level Objectives (SLOs). However, we realized we hadn’t fully exploited its potential as a standalone product.

With the **Knowledge Graph**, we are changing that. Today, we’re introducing the Grafana Cloud Knowledge Graph, which you can activate in your Grafana Cloud instance. Asserts is now integrated into the Knowledge Graph.

### What is a Knowledge Graph?

A Knowledge Graph is a network of connected entities and relationships that transforms raw data into structured and meaningful knowledge. This is precisely what the Knowledge Graph does; it takes the data sent to Grafana Cloud, transforms it into a graph, and provides insights about health and performance to help accelerate workflows and solve problems faster.

The Knowledge Graph becomes a foundational building block in Grafana Cloud for all our products. It consumes data from various solutions, including:

- Kubernetes signals
- OpenTelemetry signals for application observability
- Frontend observability signals
- Cloud provider observability for managed services
- Database observability

This enables the Knowledge Graph to learn about databases and understand how distinct elements in your system are connected, inferring their relationships. 

### Unified Experience

The Knowledge Graph creates a unified experience for all discovered entities, making them accessible through a central interface. You can explore services, Kubernetes pods, and databases on AWS, and understand the relationships between these components. This allows you to traverse from infrastructure to application and back, facilitating root cause analysis across both layers.

### Contextualized Insights

The Knowledge Graph also provides contextualized insights. It understands the significance of each entity and its metrics, adding valuable breadcrumbs to your investigations. It informs you when something is wrong and helps guide your analysis.

### Sustainability and Integration

Importantly, the Knowledge Graph doesn’t require you to rebuild your Grafana Cloud experience. Once you integrate your custom elements into the Knowledge Graph, they will coexist with other entities in the system, ensuring sustainability and evolution from your existing Grafana Cloud setup.

### Bringing Your Knowledge

Organizations have built significant knowledge around their monitoring setups. The Knowledge Graph makes it easy to integrate your unique experiences and insights into the graph. For example, you can hook up your custom dashboards to any entity, ensuring that the most relevant KPIs are front and center.

You can also onboard custom entities that may not be observed by others, such as a specific message bus or GPU sets. The Knowledge Graph will discover these elements, model their relationships, and integrate them into the catalog.

## Demo: Root Cause Analysis in Action

Now, let’s switch gears and hand it over to Manoj for a demo of the Knowledge Graph in action.

---

**Manoj:** Thank you, Cedric. Let’s see how the Knowledge Graph works. I’m currently in Slack, where I received an alert: **Initiate Checkout User Action Latency High**. Naturally, I want to investigate this using frontend observability tools.

By utilizing the insights provided by the Knowledge Graph, I can identify that my user action is taking about one second, with some JavaScript errors. The system has automatically tagged this alert, allowing me to access insights related to it.

Next, I open the **Root Cause Analysis (RCA) workbench** to dive deeper. In the RCA workbench, I can visualize the thresholds based on historical data, which dynamically adjusts based on the system’s performance over the past week.

I can also explore the graph to identify the causes of the latency issue. It highlights all connected services, allowing me to understand the relationship between the frontend and backend services.

### Augmenting Knowledge

One key feature is the ability to bring my own knowledge into the system. For example, I can track feature flag state changes and add this information to the RCA workbench. This allows me to see how changes in feature flags may be impacting user actions.

As I explore the data, I can view custom dashboards that I’ve integrated, which show relevant KPIs and metrics. This helps me quickly identify that the checkout service is experiencing issues due to database interactions.

I can delve into database observability, where I see CPU metrics and other performance indicators. The Knowledge Graph allows me to drill down into specific queries and identify problematic SQL statements.

### Conclusion of the Demo

In summary, we’ve demonstrated how the Knowledge Graph enables seamless transitions from frontend observability to root cause analysis. We were able to identify the exact query causing issues, showcasing the end-to-end flow users can execute.

But what if we could automate this investigation? Enter the **Grafana Assistant**. 

The assistant can autonomously explore the graph and conduct root cause analysis, streamlining the process even further. It can generate insights and suggest actions based on the interconnected data.

---

**Cedric:** Thank you, Manoj. What we’ve highlighted today is how the Knowledge Graph simplifies complexity in Grafana Cloud. It integrates disparate data into a cohesive graph, making root cause analysis more accessible.

The best part is that the Knowledge Graph is available to all Grafana Cloud users today, including those on the free tier. We can’t wait for you to explore it and provide feedback. Thank you!

## Raw YouTube Transcript

Hello. Hello everyone. Welcome to London. Now I'll talk about faster root cause
analysis with Grafana Cloud and the Knowledge Graph. My name is Cedric.
I'm a product manager at Grafana Labs. With me as my friend and the
VP of Engineering, Manoj. And we are going to talk about
the Knowledge Graph. Alright, before we dive in, let's
talk about the problem first. What problem are we trying to
solve? And I think it's pretty easy. We came across in the keynote,
the problem is complexity. Modern application development and
deployment scenarios are just sheer complexity. You have Kubernetes,
you have containers as a service, you have functions as a service,
virtual machines, bare metal, dozens of programming languages
and containerization. That's a lot, right? And all of these living
elements in your systems, they are emitting events or signals, data logs, metrics, traces, profiles. And the challenge is that
most of these signals, they just come in and then they're
living in silos. It's hard to get the full picture of the full stack. And ultimately this results
in a disjointed experience
for you, for your users, for the people that depend on the system
when it's critical to solve a problem for you and your business. Right? Now that we understand the problem, and
I think this is core to observability, we have so much data, let's talk about what we
think could be the solution. A brief look back. Last
year at ObservabilityCON, we announced the general availability
of Asserts in Grafana Cloud. And up till that, Grafana Cloud
was mostly visualization centric. We had experiences that took
your data, visualized it. We did our best to correlate and
help you navigate your systems, but Asserts really leveled that
up. It changed it big time, right? Asserts introduced a concept of
proactive insights through the concept of assertions and a curated root cause
analysis workflow that you could use to drive root cause analysis much, much
faster than you were able to do before. And Asserts created a graph across
all of the layers, application, infrastructure, and it helps your users or helped your
users to understand certain network effects between the two. How services
communicate when they are in trouble, when the infrastructure needs some
help. And for known object types, Asserts provided out-of-the-box UI
dashboards that were battle-proven, a curated experience to drive SLOs, but we didn't quite fully
exploit the potential here. Asserts was a standalone product
and we tweeted it like that. With the Knowledge Graph.
We're changing that. We are introducing the Grafana
Cloud Knowledge Graph today. It's available in your
Grafana Cloud instance today. You can go there and activate it and
Asserts is becoming the Knowledge Graph in Grafana Cloud. But what
is a knowledge graph even? Luckily there is a definition,
right? If you go by the book, then a knowledge graph is a network of
connected entities and relationships that turns raw data into knowledge
that is structured and meaningful. And that's exactly what the
Knowledge Graph does, right? It takes the data that you send into
Grafana Cloud and it transforms it into a graph and knowledge about health
and performance to help you accelerate your workflows, help
you solve your problems faster. So if you look at this diagram, it's actually pretty interesting because
the Knowledge Graph is becoming a foundational building block in Grafana
Cloud for every single product that we build, all of our opinionated solutions. It consumes data from all
of the solutions - we have Kubernetes signals, we have OpenTelemetry
signals for application observability. We have frontend signals
from frontend observability, there are integrations in Alloy. We have cloud provider observability for
data for all of your managed services that you're using and
the new kid on the block, which is database observability.
We know the Knowledge Graph learns about databases now, and this way the Knowledge Graph becomes
aware of the distinct elements in your system and it can infer what they are
and it can understand how they are connected, right? This way it can understand how entities
interact with each other. For example, how services communicate
and how infrastructure is
supporting your applications. And thanks to the graph and the KPIs,
for example, RED and use metrics, the graph can then derive insights
about health and performance. Once the graph is built, we create a unified experience that is
deeply connected all across Grafana Cloud Observability that leverages the
derived insights and helps your users to explore their signals in context.
And then if you need it, you can drive root cause
analysis. I'm standing on stage, I'm obviously pretty hyped about the
Knowledge Graph, but why should you care? I think there are three distinct
elements here. First of all, it's the unified experience, right? The Knowledge Graph creates an experience
for all of the discovered entities and it makes them accessible through
certain elements that are central. So you can go to the new entity catalog
that is available in your instance now, and you can find the elements that
you care about. Manoj showed on stage, how you can see services, how you can explore your pods in
Kubernetes or your databases managed services on AWS, all through a
single unified interface, right? And you can understand the relationships
between these things because there is a map and we explicitly
encourage you and allow you, and we want you to use the connectedness
of the graph to traverse it. Traverse from infrastructure
to application, vice versa, to learn what is wrong with a
thing that you care about. And then once you're ready, you can start the root cause analysis
and it works across infrastructure and application layers. The Knowledge Graph also creates
contextualized insights for you. It understands the entities
that it's looking at, right? It understands what is
important about an entity, what is important about a database, what does it mean when a
certain metric goes up or down. It's not just a movement on a
graph. It's also meaningful for you. And thanks to the knowledge that we
have built into the Knowledge Graph, it understands when something is wrong. So it adds valuable breadcrumbs
to your investigations. It understands entities and technologies
that you're looking at and it tells you when something is wrong, adding these
breadcrumbs along your investigations. Lastly, the Knowledge Graph doesn't require you
to completely rebuild your Grafana Cloud experience. You have invested time, money, and effort into building your Grafana
Cloud experience. You have to build dashboards, alerts, and all
of that good stuff, right? And once you hooked up your custom
thing into the Knowledge Graph, which it totally can, then it will live alongside the other
entities in the system and that makes it really sustainable and a useful evolution
from where most of our customers are today. The graph has
progressively enhanced the
more data that it can discover. So in order to make the connection
between infrastructure and application, obviously you need both.
But once you have it, we hope that we can make
the connection for you. We can understand what are the Kubernetes
pods that are powering your services. Let's talk about the unified
experience for a second. One of these elements here is
the consolidated entity catalog. I already talked about it, but it automatically discovers every
entity in your system, every pod, every service, every front end, and these entities are accessible
through the same UI that you can use. It highlights the most
important KPIs from the get go. We show you the RED metrics that are
important for your thing or if it's an infrastructure thing, we highlight
you the use metrics for this thing. The entity catalog also understands how
entities relate to each other, right? So for example, when a backend is
causing issues in a frontend service, and once you're zoomed into a
certain entity that you care about, the Knowledge Graph will highlight you
the most relevant dashboard from its out-of-the-box catalog.
From the example on screen, we have application observability with
very prominent RED metrics and a front end observability dashboard for insights
into the user layer - how your users are using your front ends. But
born in the full stack world, Knowledge Graph blends these different
sources of data together and you can look at traces for service, navigate to a backing Kubernetes pod or
find out how the front end is doing. But how do you know the
entities are healthy? Well, this brings us to proactive insights
and they're really at the core of the Knowledge Graph. We make insights
available everywhere, always on, and continuously in Grafana
Cloud Observability. Insights are specific observations
about an entity and its behavior, right? Examples are issues with the user
experience of front-end apps, garbage collection issues in the JVM or
an anomaly in the request pattern of an application service. With Knowledge Graph, users don't have to be the subject matter
experts for every technology that's impacting the performance
of what they care about. Knowledge Graph provides insights
out of the box for a lot of different things. Once an organization
adopts the Knowledge Graph, we're continuously deriving these insights
for all the entities that we discover and we surface them to you in a way that
makes them easy to consume in the user experience.
Thanks to these insights, users will know at every level of the
stack what impacts the performance and health of the energies
that they care about. Insights can be used to drive SLOs and
serve as breadcrumbs for your root cause analysis. And with our
new shopping cart pattern, Manoj already showed it in the keynote. You can add more entities
to your investigation while
you're exploring the blast radius of a certain
thing. Once you're ready, you can click the button and dive straight
into root cause analysis workbench and drive through root cause analysis. The last bit that I want to highlight
is augmenting your own knowledge, right? Let's talk about that for a second. Organizations have built large bodies of
knowledge for their monitoring estate. You all have invested time, money, and effort to making your Grafana
experience unique and to surface what's important for your teams when they are
working with it. The Knowledge Graph makes it very easy to bring your own
experience and tightly integrate it as knowledge into the graph. One
example here is dashboards. You can hook up your own
dashboards to any kind of entity, to any kind of scope so that the
aspects that you care about are front and center. The example here from our demo
environment is a businessy dashboard that surfaces other KPIs than just performance
related criteria such as the RED metrics. You build these things out
and you want to make good use of them. And with Knowledge Graph, you can just tie this dashboard to an
entity and that sustains your investment and creates better context for your users. You can bring your own entities, right? Maybe you're observing something
that nobody else is observing. That could be a custom message
bus or a set of GPUs, for example. With Knowledge Graph, you can onboard these things as entities
and model the relationships to other elements.
How does it do it? Well, you just describe how the
graph can discover the thing. You can describe how the KPIs
are modeled as metrics and then the graph will do its thing and
hook it up to the rest of the experience. The Knowledge Graph does the heavy
lifting for you and then integrates these entities into the catalog. You can also bring your own alerts
as insights into the system. Organizations have invested huge amounts
of work into creating the right alerts for the right thing. Once something
is hooked up to the graph, insights become important. What you see on screen here is you can
add a few annotations to existing alerts and then the Knowledge Graph would
surface these as insights in the whole system. So something
that only you know about, a certain anomaly that you
have codified as an alert, is now available to everyone
that is using this system. But that was a lot of talk. Let me
hand it over to Manoj for a demo. Thank you Cedric. Okay, I've been playing
with the demo here. It's all working. Nice. Let's do it. Okay, I will actually go out of
this thing and I will go to my favorite place in the
world. It's called Slack. So I guess this is where we live
and it's generally pretty noisy. So I guess a lot of the stuff that
Cedric was talking about, right, these insights, the idea
of SLOs and insights. I mean they've been around since
the Google guys wrote this SRE book. The main theme here is that do not turn
off all these insights that are really your breadcrumbs to figure
out what the real deal is. Why is this problem happening? So I'm going to start with the
company troubleshooting here. So I got an alert here. Call Initiate Checkout
User Action Latency High. And I mean naturally, I want to look at my frontend
observability. You guys
are probably using Faro, so if you don't, just start
using it. It's pretty cool. So this is the new kid in the block
too, in the user Faro world - actions. So what's the user action? I mean
it's literally like a milestone. You have all your webpages
and they're already tracking, but user action is literally
you say that, okay, I want to track these key
milestones in my frontend journey. So I have initial checkout and
all those different actions here. And then one of them is
having a high latency issue. My user action is taking about
one second here and there's some JavaScript errors happening, which I do not know if it's
really the cause or not. But then I also can quickly
look at my HTTP overview. This is the newest feature
also in the Faro world. I can see my request
rate is kind of dropping. And my latency is rising up. Okay,
so that saves some trouble here. And we took the idea of the insights. So the system has automatically
identified the alert that we saw there that's tagged this insights button you'll
find everywhere to every solution in Grafana cloud. So a quick tip, okay,
let's just go and figure it out too. So I'm going to say, okay, open
the RCA workbench for doing this. So let's just quickly walk through it
what exactly this insight thing is by just thinking at this specific alert here. So as I expand here, I can see that. So I mean in the world of
alerting it's been a big trouble. What should be my threshold, right? It's like this question
that nobody has answers to. Well the answer is in math
and statistics I believe. So we literally take the
data and compute a P 75 last_over_time. I mean quantile over
time, over seven days, figure out, okay, this is where it generally
trends. You can see that this, I definitely did invent 6.11.6 as my
threshold. Trust me, I didn't write that. It's dynamic. It's generating,
it's constantly evolving. Your system gets better, it'll come
down, if the system gets worse, it'll rise up. We're
looking over seven days. So that's a pretty long time
to make it stable. So yeah, I have a [inaudible] saying for
10 minutes if this goes bad, wake me up dude and
interrupt me. I've done that. So this is showing up. That's
the idea of an insight. Don't write all this alerts,
this is the boring work, just leave it to the frontend
observability to take care of that. And then I want to ask, okay,
what should I look at, right? I'm kind of in a bind here.
So let me ask the graph, go walk the graph and find out what
are the causes. And we are doing that earlier today. So when I did that, it actually brought in a
bunch of other services, like everything that is connected
to the frontend observability. So it kind of walked the graph on a
multiple levels. It has a different, it looks for different patterns.
Come and meet us at the expert booth, we'll walk you through how does it
decide what to bring, right? But yeah, so I mean TL;DR, there's a lot of microservices that my architecture has built out. This is the
OpenTelemetry app. I do have a database, the new kid that I was talking
about earlier year and yeah, they're all connected.
So it brought it in. But let's just talk about the augmenting
the knowledge part of it because that's really key here. So I want to zoom into the beginning
of this incident because that's how it happened.
So there is a feature flag service. I'm going to switch to
the summary view here, which just kind of flattens the tree.
It's like a tree structure we have here. So there is a feature flag
state change that attract. Now how the hell the Grafana team knows
about a feature flag service that I'm running. They don't. That
answer is very simple. And so this is literally
"bring your own knowledge." So I'm going to quickly show you here. So there is literally a rule that we have. It's like bring your own wine to a
restaurant. Bring your own rules. So we have a rule here that
says that I have a bunch of rules that I've brought in here and
one of them is saying that, okay, I want to track a feature flag state
change that I have a service and when it happens, show me this value, this metric, this is the value of the feature
flag and I want to see that. And this is a classic alert
you probably had in the system, but then you add a few extra labels to it. So now this is part of the workbench.
Literally you can reuse your API or UI, whatever it is, you wish to
bring your own knowledge into the system. And similarly with the
graph and everything else. But let's go back to the
workbench here, back to previous. So yeah, so we were in the workbench, we looked at the feature state
change and now I'll look at, we talked about building
dashboards. So if I open it here, and this is not a classic
RED metric service, so I want to see the graph that is
literally showing a custom dashboard here that we have plugged in again through
the "bring your own knowledge" here. So now I'm looking at this
data, this is interesting. I'm seeing my checkout service again
dynamically figured out a bunch of reset sessions happening to SQL. Obviously we manufacture to
invite the new kid to the town. We are causing trouble in database world
and the checkout services are having trouble. There are multiple
checkout services in different
regions of the world. And then as I scroll down here, I do see my database service, but what if I want to see where is the
most problem? So let me just start by score. I kind of personally like this view
where it starts by - think of a severity score, which services
are having most problems? Obviously the front end is
having a lot of problems, but then the recommendation
service is also at the very top. And we have the database here. So I want to take a look at the database. So let's just do a deeper drilldown
at the database observability here. What it is doing is it's pulled
out my CloudWatch metric. Like we talked earlier, it's showing how the CPU spiked
up to almost a hundred percent. And I mean is it a read issue, write
issue? What's causing the trouble? I can see the read
throughput is high here. I want to now go into the -
this is the classic metric view, every integration which was there. But
what we did is the graph now knows that, okay, who is it talking to?
I mean there are two things we can do. You can literally look at who are the
services even using this database. The graph is telling you what it is. But I'm more interested in deep
diving into the query part. So I'll go to the orders-db here. Now this is where it's
showing me the word SQLs in the system and it's sorting
by the weight events. But I am looking for the
word query by duration. So I'm going to sort by
duration here and bring the query that comes to the top
right, clicking over 55 seconds. That's really bad. Okay,
so let's just zoom in. And did we run out of time? Not
yet, right? No, I'm in time. Okay. Yeah. So this is the full view
of database observability, how this specific query, looking
at the duration, the RED metrics, the rate events, the how many,
what's all the stats here. But I'm going to dive into the query
samples. This is a classic example view. So we are capturing some of
the worst query examples here. I'm going to pick one here and then
start driving into it. And trust me, I'm not as SQL expert
at all by any standards, but I'm going to pretend one for a
moment and let's see how much of Grafana AI can help me here. So this is the big SQL that it is firing. I have no idea what it is doing and
why is it doing so much stuff here. So it's taking a lot of time. Okay, so let me ask our assistant
to optimize this query, right? And it's going to take some
time. So I'm going to leave it to it. I will come back to look at like okay,
what else it can do? Oh, explain plan. I understand, explain plan. Okay, so
explain plan is like, let me explain you, what are you doing here? So
you can already see a lot
of table scans happening, just the depth of information
available with the tool. Now you literally, if you go look at the exporters, like the classic open Grafana Cloud, we have put in the MySQL
exporter now enhanced to capture all the data I'm showing
you sitting in open source. You guys can go take a
look and install it today. And then once it comes to the cloud, we have all this data
fully visualized for you. So looking at the explain plan and I can
go back to the AI helper to see that. Oh wow, okay, it's already come back here asking me
to that I should build a composite index on product ID, order
ID because I'm doing a query that goes across the two columns
and obviously it looks like I don't have an index and I give a bunch of other
recommendations, right? So yeah, no, that is all exciting stuff and I want to
go back to the workbench here and then should I call it a win already
yet? Did we figure out the problem? I think we found the root cause, right?
I think that's it. Database query, that was it. And the AI
integration helped Manoj, who's not a SQL expert, to create
an optimized version of the query. And I can now go in and I can change the
query in my app and that should resolve the performance problem. But yeah, There is
something else. Yeah. Okay, let's go back to the
slides for one second. So to recap the demo, what we just saw
was Manoj started in the front end. There was an issue that was user
facing, a part of a critical journey, did not complete successfully. He then transitioned seamlessly into
the root cause analysis workbench. Found a correlated database entity
through the database integration with the Knowledge Graph. And then
in database observability, which is brand spanking new. It's
in public preview, it's awesome. He was able to find the exact
query that was causing the issue. That is an end-to-end flow that
Manoj as a user can execute. But hey, there was one more thing
that we want to highlight here, right? That's a human doing this thing and
actually still a lot of workflow to execute. So what if Grafana Assistant could
drive the investigation for you or not? Do you think it can do
that? I think it can, right? I think Grafana Assistant is here to
not just empower users but also copilots like Grafana Assistant. And it can
use the same context, insights, and relationships between stuff in your
system as the user and then autonomously explore the graph and drive root cause
analysis for you. Should we show it? Yeah, let's do it. And so switching
back to my laptop here, okay, we'll start with the exact same place and
this time I want to enjoy my coffee on my laptop so far. I'm going launch the RCA
workbench straight because
I've built confidence in the product already. I just want
to go to RCA workbench. Okay. I mean this is where I will just ask the
assistant to just tell me what's going on. That's it, right? And
we were speaking earlier, we basically fed the entire
graph information into the LLMs as tools. We wrote a system
prompt, gave it all the tools, go browse the graph, go find logs and traces and health signals
to everything that we have provided, whether it's insights that is shipping
by us or insights that you guys can bring on board. So it's actually
doing it in real time as we speak. And let's see how long it takes. And before I think we have still a little
more time and let's see where it comes back with. But I mean if
you think about it, right? It's like we are constantly
enhancing this with all the data that you're putting to
Grafana cloud, like your previous alerts, I was just talking to Lalith who
was from BMW somewhere in the crowd. You can provide your runbooks
as rules to the system. So when this guy comes
back with an analysis here, it can even possibly
execute the runbook for you. I'm going to see that if it's, oh
yeah, it did come back, thank you, assistant. And like LLMs, it every
time, it comes up with the new output. So I have no idea what it's
going to say. Actually no, because I have given it
the context. So let's see. So it's actually saying that the browser, it's its initial checkout of the cart
page and request elevated duration service calls. Oh yeah, it did find
my queries. So if you remember, I have not pulled the databases
and everything to the workbench. Basically we have given it as LLM calls. It's just making tool calls behind
the scenes and to figure out all this insights and as I scroll down, oh yeah, it's even suggesting
what should I do next. So this is where we have
not gone full agentic. And our team was talking
about investigations. Investigations plus Knowledge Graph I
think is going to do something wonderful here for us very soon.
But you can ask it to her. Okay? Either you can just type it or you
can say check all the entity health or analyze the checkout length. So it's basically just assert
on all this data that you have. And I did that literally I
think earlier today morning. An investigation, right? So yeah, so today morning at 6:45 AM I
was awake early to make sure is going to be here
today with me. So yeah, you can see here it's actually when I
asked this thing, it goes and runs the, makes all the tool calls, it builds
a plan, it makes all the tool calls. It then comes with different
multiple hypothesis of what are the possible causes of it,
provides a sequence diagram. So if I'm a new engineer who
just joined your company. I think this is just
rocket fuel for me, right? To come to become your experts are
giving the knowledge and my engineers can now become experts in my current
system very quickly and learn from it and then start making good
suggestions on how we should be fixing it. Because when I asked
it to - earlier, we saw the bad SQL. Now I do have traces, Sean, I dunno
if he's still there, loves his traces. He wants to look at the
query from the trace side, otherwise he doesn't trust
it. So we asked it, okay, "Can you analyze the trace and find me
the bad SQL?" It actually did, right? So it wrote at this hairy TempoQL, I have no idea how to write
TempoQL. I only know PromQL, but it does such the tempo tabs. It wrote a TempoQL to my
duration, everything else, and found out all the bad traces and
then went on and on and found the bad SQL. Yeah. So anyway, TL;DR, the database observability already will
also become a tool to this product. We will combine all this intelligence
and bring it all to you. Thank you. Awesome. One more time,
back to the slide please. That is a fantastic moment. Thank you
Manoj. I think it's a great example, the Knowledge Graph and how we
integrate it with Grafana Assistant, how we are simplifying complexity
in Grafana Cloud for our users. We literally took a
data that was disparate, joined it up in the Knowledge Graph, and then joined in Grafana Assistant
to make the root cause analysis even easier, more accessible to
everyone. And that's our pitch. The best thing about this is the Knowledge
Graph is available to all Grafana Cloud users and customers today. Even the free tiers holding up to
our promise of an actual useful free plan and we can't wait for you to
use it and provide feedback to us. Thank you so much. Thank you.

