# What is the Grafana Knowledge Graph and How Does It Help AI Agents? (Demo)

Published on 2026-09-29T17:13:10Z

## Description

Grafana's Knowledge Graph builds a contextual layer on top of your telemetry data, automatically extracting entities and ...

URL: https://www.youtube.com/watch?v=dj0NUYSsPJg

## Summary

The show is titled "What is the Grafana Knowledge Graph and How Does It Help AI Agents? (Demo)" and was published on September 29, 2026. The speaker discusses the Grafana Knowledge Graph, which builds a contextual layer on telemetry data by extracting entities and their relationships to provide insights during incidents. Key features highlighted include the entity graph interface, the ability to visualize dependencies, and the integration with AI agents like Claude Code for querying and analyzing data. The demonstration emphasizes how the Knowledge Graph simplifies incident investigation and enhances decision-making by providing a comprehensive view of system interactions and potential causes of issues.

Topics: Grafana Knowledge Graph, telemetry data, incident analysis, AI integration, entity relationships.

## Chapters

00:00:00 Introduction to the Knowledge Graph in Grafana
00:02:29 Using the Knowledge Graph in Grafana's GCX
00:05:38 Understanding the Grafana Knowledge Graph's incident analysis capabilities

We're going to talk about the **Knowledge Graph**. So what exactly is the Knowledge Graph? The idea is that when you have all your telemetry data coming into Grafana, we can actually construct a contextual layer on top of your telemetry data. 

The way we do it is by parsing your metrics, extracting entities and relationships between these entities, and presenting them in a nice graph format. At the same time, we also analyze your metrics to surface interesting insights. So whenever you have an incident, you can look at these insights to make better decisions.

Now, let's take a look at how this looks in the UI. Here we have the **entity graph interface**. You might be wondering what kind of entities we have, right? In your case, let's just say what we have. Here, we have a schema that gives you the entities in the system. For instance, we have **namespace**, **volume**, **frontend**, **service**, **pods**, etc. 

Suppose you have a system built for an e-commerce application. Most likely, you are going to ask, "How is my frontend performing?" because the frontend is the interface to the user. So, let's check the frontend at this moment. I have the e-commerce frontend, and in the last 24 hours, it seems something is happening. I see some issues with user actions, which is something we might want to investigate. 

First, I can show you that this frontend has a dependency on the backend service, which is apparently a frontend service. From here, you can also keep exploring to see more services in the backend. It’s actually going to be a very complex graph eventually. I’ll show you a different way to look into this later on. 

Now, suppose you want to investigate further. You can add this frontend to what we call the **workbench**. Once it's in your workbench, you will get a more interesting view because you have a timeline of what has happened. In this case, you notice that at three o'clock in the morning, we had some error ratios breaching. You probably want to investigate this. 

You can try to determine the potential causes for this incident. The graph in the backend will try to figure out the related signals. From here, you can make sense of the graph. At some point, you might realize, "Oh, we have some feature flag change in the system, which is most likely the cause of the incident." 

These are the user experiences, but now we live in the age of AI, and the same kind of capability for the Knowledge Graph also exists in our own **Grafana CLI**, the **GCX**. 

Let’s say the different workflow from now on will be how to leverage the Knowledge Graph in an agentic workflow like using GCX. I'm going to switch to **Claude Code**. If you start the Claude Code session from scratch, it doesn’t really know what the GCX is. So, I’m going to tell the agent to copy this prompt into Claude Code: "With GCX, show me the dependency chain from my e-commerce application all the way to the database." 

This may actually go quite deep into the graph because, as I just showed, there are many services in the system, and usually, the database will be at the bottom. Right now, Claude is going to read our GCX instructions and figure out the best way to find the answers. 

As you can see, it’s going through a list of things. It’s going to first find out the entity. It will run through the schema and determine that the frontend is a core service. The service is going to call another service, which will eventually reach the database. It’s going to figure out a very elaborate set of queries to actually query the graph, and then it’s going to give you the answers. 

I’m just going to wait here for the agent to finish. This will take a little while, so I’ll show the result from a different conversation. Once we have the question in place, it runs a bunch of commands to figure out the graph topology and eventually determine a very complex dependency from the frontend all the way to the services and the databases. 

It’s quite complex in the system, but what I’m showing you is that the Knowledge Graph gives you the capability to reach the answer relatively easily because we have all the information encoded in the graph. In addition to that, you can also ask questions. 

Let me check the health because I know something's happening. I’ll check how my e-commerce frontend has performed in the last 24 hours to see what might have caused it. This will also try to pull more insights data from the graph. It will take a little bit of time too, so I’ll show a different result from another session. 

It’s going to try to pull all insights for the frontend. At the same time, because it already knows all the dependencies, it will also check all insights on these dependencies. Not only will it tell you what happened to the frontend in the last 24 hours, but it will also give you a plausible theory on why it happened. 

It will list out a timeline of the whole incident. For instance, at one o'clock fifteen, the feature flag was turned on, which caused high connections to the database, which in turn impacted the frontend, causing error ratios in the frontend. 

As you have seen, the agent has already reached the conclusion just from a few very simple questions. This demonstrates the value of a Knowledge Graph because it not only provides a topology for which the agent can walk through, but it also provides all its insights right away for the agent to stitch together to give you a very good analysis of the incident.

## Raw YouTube Transcript

We're going to talk about Knowledge
Graph. So what exactly is Knowledge Graph? The idea is when you have all your telemetry
data coming into Grafana, we can actually construct a contextual
layer on top of your telemetry data. The way we do it is we
actually parse your metrics, then we try to extract entities
and relationships between these entities and give you a nice presentation
of a graph. At the same time, we also try to analyze your
metrics to surface interesting insights. So whenever
you have an incident, you can actually look at insights
to make better decisions. So now let's take a look at how
this looks like actually in the UI. Here we have the entity
graph interface. So you're probably wondering what
kind of entities do we have, right? So in your case, suppose let's
just say what we have. Here, we have a schema which gives you - these
are the entities we have in the system. For instance, we have namespace and
we have volume and we have frontend, we also have service and
pods and et cetera. Suppose you have the system built to
be the e-commerce application. So most likely you are going to say, "Oh, how is my frontend performing?" Because
frontend is the interface to the user. So I'm just going to check
my frontend at this moment. So okay, I have e-commerce
frontend. In the last 24 hours, it seems to be something happening. Oh, I see some issues with user actions. So that's something we might want
to investigate. But first of all, I can show you like, "Oh, this actually has a
dependency on backend service, which apparently will be
a frontend service." Now, yeah, so this goes a
little bit. Then from here, you can also keep exploring to
see more services in the backend. So it's actually going to be a
very complex graph eventually. So I'll show you a different
way to look into this later on. But now suppose you want to investigate
and then you can actually add this frontend to what we call workbench.
Once it's in your workbench, then you will get a more interesting view because you have a timeline of
what's happened. In this case, you notice what happened is
three o'clock in the morning, we have some error ratios.
Error ratio breach happening. So you probably want to investigate. In
any case, you can actually try to say, "Oh, what are the potential cause for this
incident?" Which then the graph in the backend will try to figure out what's
related signals. And from here on you can probably try to make sense of graph.
Then at some point you realize, "Oh, now we have some feature
flag change in the system, which most likely will be the cause
of incident." So these are the UX, but now we live in the age of AI and the
same kind of capability for Knowledge Graph also exists in
our own Grafana CLI the GCX. So let's say different workflow
from now on will be how do I use leverage knowledge graph in
agentic workflow like using GCX? I'm going to switch to Claude Code. Now if you start the Claude
Code session from fresh, it doesn't really know what the GCX is. So I'm going to tell
the agent to copy this prompt into Claude Code saying with GCX show me the dependency
chain from my e-comms from all the way to the database. So this may actually go quite deep
into the graph because as I just showed many services in the system and usually
the database will be the one at the bottom. So right now Claude is going to
read our GCX instructions and figure out what's the
best way to figure out the answers. As you can see, going
through a list of things, it's going to first find out the entity. It's going to run through,
oh, I have a schema. I say, oh, front end is a core service.
Service is going to call our service, which eventually will reach to a database. So it's actually going to figure out
a very elaborate site for queries to actually query the graph, then
it's going to give you the answers. I'm just going to wait here
for the agent to finish. So that one will take a little bit while
I'm just going to show the result from a different conversation. So as you can
say, once we have the question in place, it does run a bunch of commands
to actually figure out the graph topology and eventually
figure out a very complex dependency from the frontend all the
way to the services to the databases. It's actually quite complex in the system, but what I show you is the knowledge
graph gives you the capability to actually reach the answer relatively easy
because we have all the information encoded in graph. And in addition to that, you can
also ask questions. Okay, so I don't know if that
session was returned. Let me just check the health because
I know something's happening. So let me just check how my e-commerce
frontend in the last 24 hours to see what happened and what might have caused it. So this also is going to trying to
pull more insights data from the graph. It's going to take a
little bit of time too. So I just go to show a different
result from different session. It's going to try to pull all
insights for the front end. And at the same time, because it
already knows all the dependencies, because we have dependency in the context, it's also going to check all
insights on all these dependencies. And not only tells you what happened
to my front end in last 24 hour, it also give me a plausible theory on why
does it happen. And it actually listed out a timeline of a whole
incident. For instance, at one o'clock 15, the
feature fact came on, which caused high
connections to the database, which in turn impact all the way
back to the front end causing error ratios in the front end.
So now like you have seen, the agent has already reached the
conclusion just in a few very simple questions. So this is actually demonstrate
the value of a knowledge graph because it not only provides
a topology for which the agent can walk through, it also provides all its insights right
away for the agent to stitch together to give you a very good analysis of incident.

