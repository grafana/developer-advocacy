# Building AI Into Observability Workflows:  Automating Dashboards, Alerts with MCP &amp; Agents | Grafana

Published on 2025-06-07T05:37:15Z

## Description

Grafana's Yasir Ekinci takes us behind the scenes of building AI into observability workflows. Learn how LLMs, the MCP protocol, ...

URL: https://www.youtube.com/watch?v=qipWEGaTWsg

## Summary

In this video, Yasir Ekinci, also known as Yas, discusses the integration of AI into Grafana and its evolution from simple text responses to more interactive functionalities. He begins by highlighting the historical context of data modeling and curve fitting, leading to the development of large language models (LLMs) like ChatGPT. Yas explains how Grafana is enhancing LLMs' capabilities through a new tool-calling feature that allows LLMs to access private data and perform actions within Grafana, such as querying data, managing incidents, and updating dashboards. He introduces the Model Context Protocol (MCP), which standardizes interactions between LLMs and applications, making it easier for developers to integrate AI into their systems. Yas also demonstrates how to create Grafana dashboards and add metrics using the MCP server, emphasizing the potential of LLMs to assist in observability workflows. He discusses the challenges of creating reliable LLM agents and their ability to adapt to user queries, ultimately leading to a multi-agent architecture that streamlines task management within Grafana. The video concludes with a call to action for viewers to explore the MCP and sign up for a private preview of the new agent functionalities.

# AI at Grafana - Yasir Ekinci

My name is Yasir Ekinci, or Yas for short, and today I'm going to be talking about AI at Grafana. Before I start, I should not forget my clicker, which is here. I'm going to need that.

## Introduction to the Session

Before we dive in, we have a QR code for Slido. If you want to ask any questions, you can scan the code and add your questions there. We'll try to answer as many as we can at the end. I will show this slide again at the end, so don't worry if you don't have it now. You can also add your questions at the end as well.

### A Bit About Me

Very quickly about me: I'm Yas, based in Belgium. This should be the Belgium flag, but it says "BE," which are the first two letters. Also, I want to make the case for stopping calling French fries "French fries" because they're actually "frites," and we should give a shout-out to the Belgians, as that's where they're from. One person likes that.

Lastly, I enjoy being under the sea as much as being on the surface, which is why I live in Belgium—the best place to dive. Just kidding, that's me!

## Today's Agenda

Let's have a look at what we'll be discussing today. In the next 25 minutes, I'll talk about how we're transitioning from using AI just for text responses to actually getting things done in Grafana using AI. Yesterday, we gave you a glimpse of this with the Grafana assistant and our thoughts on building agentic LLMs (Large Language Models) directly into Grafana. Today, I want to delve a bit deeper into the journey of how we got there.

## A Historical Perspective

Let's go all the way back to the beginning—1800 BCE, when Babylonian astronomers were trying to model the movement of the stars. Every day, they looked at the stars and recorded their positions, likely on stone tablets. Eventually, they had enough data points to start fitting curves to predict where the stars would be next. This was the first known instance of curve fitting.

Fast forward a few thousand years and add a bunch of NVIDIA GPUs, and you gather data on all of humankind. After a metric ton more curve fitting, we arrive at the ChatGPT moment—our first LLM. These LLMs have been incredibly useful, providing developers a way to access a static snapshot of internet context using natural language in a single API call. This capability enables new experiences, such as in Pyroscope, where we can feed profile data to an LLM and receive a human-understandable explanation.

However, LLMs only know what they've seen in training. They don't have knowledge of your specific Grafana instance, dashboards, or how to query data from Prometheus or Loki—at least, they didn't until recently.

## Enabling LLMs to Speak Grafana

Imagine this: if you go to ChatGPT today and ask about your active incidents, it obviously won't be able to answer because it doesn't have access to your instance, alerts, or dashboards. Although, to be honest, that won't stop it from making something up sometimes!

To address this limitation, we introduced **tool calling**, giving developers a way to define a set of tools—like API calls, functions, and custom actions—and allowing the LLM to choose which tools to use to answer questions. This is useful because it allows the LLM to:

- Go beyond internet context and call APIs with private context.
- Perform actions that go beyond mere chat responses, such as creating a PR in your private repository or triggering actions in other systems.

Initially, tool calling was a bit of a wild west, as each integration had to be built in a custom way. However, a new OSS project from Anthropic proposed the **Model Context Protocol (MCP)** standard, designed to simplify AI interactions with apps and data sources—think of it as USB-C for AI apps. It allows product owners to define interactions with their app while letting developers focus on the experience rather than implementing individual tools.

### Grafana MCP Server

We were early to adopt this standard. Shortly after we open-sourced our Grafana MCP server, OpenAI also decided to use MCP, solidifying its position. The Grafana MCP server is open-source and exposes core parts of Grafana to LLMs, enabling them to:

- Search and update dashboards.
- Query data sources.
- Manage incidents, find alerts that are firing, and much more.

This is just the beginning; you can expect us to add more capabilities in the future.

## Practical Application of MCP

Going back to our initial question, now when we ask about active incidents, the Grafana MCP server signals to the LLM what tools are available. The LLM can then choose the appropriate tool and parameters to get the necessary information from Grafana.

### Getting Started with MCP

To get started with MCP, it's straightforward. You can install the binary or use our prebuilt Docker image to set up the MCP server. Then, configure your MCP client (like Cursor or Claude Code) to use Grafana MCP. Just point it at your instance with a token, and you're good to go. The MCP clients will discover the tools available to them. You can even stack multiple MCP servers, allowing them to work together—for instance, using Grafana alongside a GitHub MCP server.

## Demo: Making Changes Using Observability

Now, let me show you how you can use the Grafana MCP server to make changes using observability. 

1. I have a simple Node app that displays "Hello World" and randomly errors out. It exports basic metrics, including HTTP requests, and is connected to a Prometheus instance and an empty Grafana instance hooked up to the Grafana MCP server.

2. I will pull up the Cursor agent and ask it to create a dashboard based on the metrics in this code. The agent will search for available data sources and metrics. 

3. After listing some Prometheus metrics, it will ask for confirmation to create the dashboard. Once confirmed, it creates the dashboard based on the code.

4. Now, I want to add latency metrics to my code and the dashboard. I'll ask the agent to do this. It will recognize that there's no latency metric in my code and create a plan, which I will confirm.

5. Once the app has hot reloaded with the new metric, I can ask the agent to add this to the dashboard. The LLM understands "that dashboard" refers to the one we just created, and it will update it accordingly.

### Conclusion

This demonstration illustrates how we're enabling LLMs to interact with Grafana, bringing Grafana context to your environment—whether that's your IDE, CLI, or chat client. This capability can significantly speed up development and enhance observability.

## Next Steps: LLM Agents

What if we could take it a step further? We did single-call LLMs and tool-calling LLMs, but what if LLMs could drive Grafana directly? Imagine an LLM navigating Grafana, running queries, editing dashboards, and assisting you in your observability workflows.

### Why We Need LLMs to Drive Grafana

Observability is about understanding and operating complex systems, which is challenging. Many people have never used Grafana or created a dashboard. There are various solutions attempting to solve this issue, but LLMs have a unique advantage: **natural language interaction**. Language is how we think and express our desires.

Imagine a system where you can ask questions like:

- How can I get started with SLOs?
- Who's on call today?
- What's wrong with my system?

However, simply connecting a box to a tool-calling LLM isn't enough. Observability questions can be complex and multi-step, and Grafana setups vary widely. We need something capable of handling this complexity.

### Introducing Agency

To solve these challenges, we need to give our LLMs **agency**—the ability to decide what to do, which tools to call, and how to adapt to incoming information. This is the promise of LLM agents: based on a task, the LLM takes actions, queries data sources, receives feedback, and continues until it has everything it needs to solve the task.

### Challenges and Solutions

We started exploring this at a hackathon, combining the LLM agent concept with our tools and instructions for using Grafana. The results were impressive, but challenges remain:

1. **Quality Assessment**: We need to evaluate how well the agents perform using reproducible tests.
2. **Token Optimization**: LLMs can generate large outputs and consume many tokens. We aim to reduce token noise by using more natural outputs rather than structured formats like JSON.

### Agent Architecture

To create a more modular and extensible architecture, we moved from a single agent to multiple smaller agents. This multi-agent approach allows for delegation based on the task. Each agent can handle specific queries without overloading a single conversation thread.

## Wrap-Up

In conclusion, we have made significant strides with quick actions, quick assist, and MCP. We invite you to try it out and build your own integrations on top of MCP. If you're interested, you can sign up for the private preview of some upcoming features.

### Future Directions

- **Expanding MCP**: We plan to increase the number of tools available.
- **Specialized Observability Agents**: We are exploring how knowledge graphs can help agents find relevant information inside Grafana.
- **Community Contributions**: We aim to open up some of our evaluation processes for community input, particularly around query generation.

Thank you for your attention!

## Raw YouTube Transcript

My name is Yasir Ekinci or Yas for short, and today I'm going to be talking
about AI at Grafana. Now before I do, I should not forget my clicker, which
is here. I'm going to need that. But let's start. So before we
start, we've got the QR code again. So we'll be using Slido. If
you want to ask any questions, you can scan the code,
add your questions there, and we'll try to answer as much
of them as we can at the end. I will show this slide again at the end, so don't worry if you don't have it now. You can also add your questions at the
end as well. So very quickly about me, I'm Yas. I'm based in Belgium.
This should be the Belgium flag, but it says BE which is
the first two letters. The other thing is I want
to make the case for: stop calling French fries French fries, because they're actually fresh fries
and you should give a shout out to the Belgians because that's where they're
coming from. One person likes that. And the last thing is I like to be under
the sea as much as I like to be on the surface, which is why I live in Belgium.
Best place to dive. Just kidding, that's me. Let's have a look at
what we'll be talking about today. In the next 25 minutes, I'm going to talk about how we're going
from using AI just as a text response to actually getting things
done in Grafana using AI. And now yesterday we showed
you a glimpse of this. We showed you Grafana assistant, and it's like how we're thinking about
building agentic LLMs straight into Grafana itself. Today I want to talk a bit more about
the journey of how we got there. So let's go all the way
back to the beginning. It's 1800 BCE and Babylonian
astronomers are trying to model the movement of the stars. And
they did this by every day they looked at the stars and they wrote where
the star was, I'm assuming, on some kind of stone tablet. And at some point they had a bunch
of points on this stone tablet. And then they tried to look at, okay,
what if we fit something in between? What if I draw a line in between and
see where the start is going to be next? And that was the first known
instance of curve fitting. Now this might have
been a bit too far back, but if you fast forward a few thousand
years and you add a bunch of NVIDIA GPUs, you gather data on all of humankind
and finally do a metric ton more curve fitting. You get the ChatGPT
moment, we get our first LLM. And these LLMs have been super useful. They gave developers a way to
access the context of the internet, albeit like a static snapshot of it
using natural language in a single API call. And that's super useful, because we can feed some
predefined context and
instructions to the LLM and get a natural answer back. And this enables
some new experiences. For example, in Pyroscope, we can feed profile data to an LLM and
get a human understandable explanation out. And because the LLMs,
they have internet context, we can get recommendations
based on the code, the methods, and even the open source libraries
that are used in the profile. So this really helps us
accelerate the understanding. It lowers the barriers to understanding
profiles and that's single call LLMs. But LLMs, they only know
what they've seen in training. They don't know about your Grafana,
they don't know about your dashboards, they don't know how to query data.
Your Prometheus, your Loki. Well, I should say they
didn't know until recently. So let me talk about how we're
making LLM speak Grafana, so that they can interact with your
observability. Now imagine this, if you go to ChatGPT today and you
ask which active incidents I have, obviously it won't be able to answer that. It doesn't have access to your instance,
it doesn't know about your alerts, your incidents, your dashboards
and so on. Although if I'm honest, it's not going to stop it from
trying to make up one sometimes, but that's just ChatGPT.
But to go beyond this, tool calling was introduced.
And tool calling, it gave developers a way
to define a set of tools. Like think about API calls, functions, custom actions and then give those tools
to the LLM and give the LLM a choice to choose which tool it can use. If it
deems its helpful to answer a question. And that's quite useful because it
allows the LLM to do two things. It allows it to go
beyond internet context. It can call APIs with private context, it can search a dashboard and get
back that your private private context dashboard from your instance. And also it can take actions that
go beyond just the chat response. You can create, for example, you can
create a PR in your private repo. You can trigger other
actions and other systems. And this was something that
LLMs previously without
tool calling couldn't do. Now this all started
relatively as a wild west. It was very vendor specific for every
kind of integration you needed to build it yourself in a custom way. If you wanted
to add GitHub support or Slack support, you needed to do all of that from scratch.
But very quickly, a new OSS project came out from
Anthropic and they proposed the model context protocol
standard or short for MCP. And it was really designed
to make it easier, to make it easier for AI
to interact with your apps, with your data sources. And you can kind of think of it
like it's like USB-C for AI apps. And it's really useful, because it simplifies the
development and usage of these tools. As a product owner, if I own Gmail or if I'm
the product owner of Slack, now instead of having each developer
define their own way of how to interact with Slack, Slack can
actually own that interaction. They can own the MCP server. They can define this is how
you interact with Slack, these are the actions that are available, these are the tools that
are available in Slack. The other thing as an app developer, if
I'm developing an app that uses tools, now I don't need to build all of this
myself. I can just use a Slack MCP, I can use the Gmail MCP and then I can
just focus on the experience and rather than the implementation of the
individual tools. And finally as a user, if you're using Cursor
or cloud code or ChatGPT, you can bring these MCP
servers to your MCP client. And that means you can now just
extend the capabilities of your local development experience,
your local chat experience. Now we were very early to adopt this.
So very early on we were like, okay, this makes sense to us. We adopted
it and we got a bit lucky OpenAI, I think a month after
we open sourced this, OpenAI also decided to
use MCP as a standard. So that kind of solidified its
position. And the Grafana MCP server, it's open source and it exposes
the core parts of Grafana to LLMs. It really tells LLMs, this is how you can interact with
the observability context. And you can do things like you can
search and update dashboards, you can query data sources,
you can manage incidents, find alerts that are firing and so
much more. And this is just a start. You can expect us to add
much more coverage of all
the other things that you can do in Grafana. But yeah,
that's Grafana MCP. So if we go back to the question at the
start, this is now how it looks like: now when we ask that question
for which active instance I have, the Grafana MCP server
will signal to the LLM, like these are all the
tools that are available. Then the LLM can make a decision: okay, based on this question I'm going
to choose the get incidents tool. It can even set parameters like
only give me the active incidents. That goes to Grafana. Grafana gives a list of incidents to the
LLM and then the LLM can finally answer this question. And let me just show you
very quickly how you can get started with MCP yourself. It's
pretty straightforward. You can install the binary or you can
use our prebuilt docker image to set up the MCP server. Then you just configure
the MCP client, whether that's Cursor, Claude Code or anything
else to use Grafana MCP. And then you just point at your instance
with a token and you're good to go. And you can see that MCP servers
like your clients, sorry, will discover what they can do. They will discover here are
all the tools available to me. And you can even do stuff like you
can stack multiple MCP servers and let them work together. For example, you could have the Grafana server
together with the GitHub MCP server. But we can do more than just
answer simple questions. So let me show you a demo of how you can
use the Grafana MCP server to actually make changes using observability.
So if we can swap back to my screen, what we have here is just to give you
an idea, I have a simple Node app, it says hello world and randomly it will
error out just to make it a bit more interesting. It is exporting
a bunch of metrics here, just basic ones and the HTTP requests. I have a Prometheus instance and I have
a Grafana instance that has nothing in it. And just to show you, this is hooked
up to the Grafana MCP server. So again, you can see all of the tools that
we have there. So if I go back, what I want to do first is I'm
going to pull up the Cursor agent. I'm going to try to see if this make this
a bit bigger. And I'm going to ask it, okay, based on, can you create a dashboard
based on the metrics in this code? There's nothing like
custom going on here, by the way. There's nothing, no custom
Cursor rules or anything. This is all just like I took Cursor, I just hooked it up to the MCP and
then just trying to see what it does. So you can see it searches like,
okay, what data sources do I have? Is there a dashboard already available? You can see it's listing out certain
Prometheus metrics to see what metrics are available and what values
do they have. And then finally it goes, okay, I've got something. Do you want me
to create the dashboard? And I'm like, okay, go ahead. And hopefully fingers crossed that
will and should create the dashboard. This might take a while
depending on internet, depending on if Anthropic is happy. Okay, so it says it used the update dashboard
tool and it says your Grafana dashboard has been created. So if I refresh this, I get a dashboard fully
created based on my code. Thank you. Okay, so now this
dashboard is looking good, but I'm missing latency metrics. So I'm going to ask it to actually add
latency metrics to my code and then also add it to the dashboard.
So I can just ask like, can you add latency metrics to this? Let's see. Now what it should be doing
now is that it's going to go, okay, well actually there is no latency metric
in your code. So it's going to go, I need to do this. Sometimes
I need to confirm its action. And so it came up with a plan
and now it needs confirmation. So I'm just going to say,
yeah, add it to the code. And that should create a code change
that allows, adds the metric to it. My app is hot reloading.
So as the code changes, so it's now going to the index file, it's making a change.
And if my app has hot reloaded, I can refresh this and you can
see now I have a new metric. Cool. Now I can actually ask, okay, can
you also add it to the dashboard? And the nice thing about LLMs is it's
smart enough to know when I say "that dashboard", it's referring to the
dashboard we just created before. So now that should, using
the change that we just did, it's going to update the
dashboard. And if I go back, refresh this and we have a latency metric, I can maybe zoom this in
a bit. And there we go. That's making changes with observability. So let's go back to the slides. Let's go back to the
slides please. There we go. So I just showed you how we're making
LLMs speak Grafana and bringing Grafana context to your environment,
whether that's your IDE your CLI, your chat client and so on. And they can be quite powerful because
having the knowledge of your code making changes to your code, but then also being able to use that to
make changes to your observability can really help both speed up our development
and also make our observability better as well. But what if we could
take one more step beyond this? We did a single call LLM, I
talked about the tool calling LLM, but what if we could do one step more
and actually have LLMs actually drive Grafana? What happens if an LLM can
use Grafana in the same way that we do? In the same way we can navigate
and go places, we can run queries, we can edit dashboards, make changes and even more. And ultimately
have something that can assist you in your observability workflows, but also solve a bit more
complex tasks on your behalf. So let's talk about
it. Let's explore that. Let's talk about what agents are and
how we're building agents that can drive Grafana. But before I do, why
do we actually want to do this? Why do we need something
that can drive Grafana? And really it's about observability. Observability is about understanding
and operating complex systems, and it's not easy. It takes a lot of time, it takes a lot of effort and takes
a lot of knowledge to do this. Think about how many people that have
never even used Grafana before or the amount of people that have
never created a dashboard, the amount of people that don't know about
the Prometheus query language or even people that have just joined your team
and they don't know about your system or your expertise. And there are a lot
of other solutions that are trying to solve this question, this
problem in a different way. But LLMs have one trick up their
sleeve, which is natural interaction. Natural language interaction. And the natural interaction is
a key part because language, when you think about it, it's how you
think. It's how you express our thoughts, how you express what you want to do. So imagine we have a box where we can
just ask anything about your system and actually get things done in Grafana,
for example, you can ask it, how can I get started with
SLOs, who's on call today? You can add something to your dashboard
or even you can ask what's wrong with my system? This gives you a way to
naturally interact with Grafana, but just hooking up this
box with a tool calling LLM, it's not enough and it's not enough
because well, observability is hard. Observability questions are hard to answer
because everybody's using a different way. Everybody has a different
Grafana setup. Some people have logs, some people don't have logs, some
people have dashboards set up already. Some people are just starting
out. And some of these questions, they take multiple steps. Think about
when you're trying to debug a problem, how many steps you're taking to
actually solve that question. So doing this in a simple
click is not straightforward. So we need something that can
solve complex multi-step tasks. The other thing is: LLMs, like I
said, they know about the internet, they can handle general
questions about the internet. And Grafana is open source. So it can
actually handle things about Grafana, general questions about Grafana, but
it doesn't know about your context. And being able to solve these tasks means
we need to be able to find relevant Grafana context for every question.
What Grafana context do we need? And this is not as simple as a simple
search because you can have so much things in Grafana, you can have so
many thousands of dashboards. If you think about metrics, you can have millions of
series and finding the ones
that are actually relevant to the question, that in itself is
also a hard problem. And then finally, this is an open text box, so people
can put anything they want in this box. This essentially means
you have infinite variety, you need to be able to handle
any question in any way. And also there's no single standard
way that people use Grafana. So whatever we build, we
need to make sure that it needs to be fully dynamic and practically
it needs to be general purpose. It needs to be able to adapt to every
environment. So to solve this, we need to give our LLM one
more trick and it's agency. Agency to decide what to
do, which tool to call in, what order, and also adapt
as more information comes in. And this is the promise of LLM agents:
based on a task that you give them, the LLM can then take an action, for
example, it can query a data source, then get feedback from its
environment, for example, get the results of that query,
and then based on those results, it can decide what to do next. If
it can answer the question, cool, it can stop there, answer
the question case done. But sometimes it needs to do more. It
maybe might also need to go to your logs. So you can then decide, actually I need to call another tool again
and stay in this action feedback loop until it has everything it needs
to solve your task. This is quite cool because essentially it's
like allowing it to come up with a new recipe for every single request. And that means also we can
handle that massive infinite variety of questions we need to handle. So we wanted to see how this would
play out in the Grafana world. And it really all started with
hackathon. We spent a week, we combined this concept of the LLM agent. We combined it with all of
the tools that we built, like I've shown you with MCP and also we
used our years of experience to put all of the instructions on how to
actually use Grafana into this agent. And all of this resulted in a really
impressive demo and it was built in a single week. But making these agents
really reliable and effective, it does come with some
significant challenges. So I just want to show you two of these
things in particular and how we're tackling them. The first main
question is, is it any good? Now in ML, you never have binary, it's yes or no answers to this question. It's more about how good
is it actually, is it good? Nine times out of 10 is a good one,
time out of 10. So to figure this out, we need to start with evals. We need to
test this thing and we have vibe coding, so we could also obviously do vibe
testing as well and just test the agent manually with some random
inputs and see what we get. And basically if it looks good
enough, take that at face value. But this only gets you so far. If you
want to iterate on this with confidence, we need to make sure that we can reproduce
and test these LLMs with what we call evaluations or evals for short. And let me show you an example of some
of these iterations. So the first one is we started with just checking,
okay, we have these tools, but are these tools being used
as we expect them to be by LLMs? And we found that sometimes it can fail
in interesting ways. So for example, here we are asking the LLM show me some
logs. So what I expected to do is like, okay, it should find the data
sources that have to do with logs. In our case Loki. So even though
it's calling the data sources tool, it's not adding the type filter. Now
the benefit of these reproducible tests, is we can run them, we can
change the instructions, we can update things and actually fix it, and then we can run the test again
and everything passes that way. The other thing we can do is we're
optimizing for lower cost and latency. These tools, they can generate a lot of large outputs
and consume a lot of tokens. So we're trying to see: what can we do about this? And we try to reduce this
by what I'll call reducing token noise. And let me explain that
because if you think about APIs, APIs respond typically
in a structured format. They'll use things like JSON and that's
really great if you're building systems that interact through code. But
when you're interacting with LLMs, they're optimized for natural language.
So all of these things that JSON adds, like all of these symbols, they
just A) add tokens, they add noise. And also if you think about it, there's no semantic explanation
of what's going on in that output. So we found that by turning this output
into something that's more natural, as you can see in this
example, we can do two things. One is we can both optimize
cost and latency. This example, we're using four times less tokens.
So that really makes a dent. Obviously, less tokens also means less
processing and less latency. But finally we also found that it actually
improves the quality of the outputs because it's semantically easier for
the LLM to parse something that's more natural than something that's
built for interacting with code. And then finally, if we
bring it all together, we also observe and test the
entire end-to-end flow. We do this, we have some reproducible scenarios and
expectations that we set up and then we just mock and we have a controlled
environment essentially where we control Grafana, control the responses that it can get
from the data sources where it is. And that's quite cool that we can mock
the environment. We don't mock the LLM, you still need to test with real LLMs, you still need to get them to
actually run these completions. But we control the environment where
we can test them in so that we can reproduce them. And these tests,
we can run them on multiple levels. We can run them fully end
to end like the whole agent. We can call up the whole agent, we can run them at the individual tool
level and even in what I'll call sub agents, which I'm going to
talk about in the next section. So that was evals. Let's
talk about the agent, or maybe I should say
agents. Agent architectures, they're still relatively
new and there's many, many different approaches popping up of
how you can set up these architectures. For us, the main driving force has been around
how do we make this a bit more modular? How do we make it extensible? Because Grafana has so much
new features popping up, Grafana itself changes
and evolves over time. And there's new things like new features, new data sources that are
being added every month. So how can we make something that's a
bit more accessible? We started with a single agent, a single
general purpose agent. We gave it a lot of instructions
to give you an idea. I think one of those first situations, we're talking about more than 10,000
tokens in a system prompt that's like 40 pages worth of instructions. And obviously anytime you change
something in those 40 pages and you try to iterate on it, it's really hard to
debug because it can fix one flow, but it can break 10 other flows. And
that's where those evals come in as well. The other thing is we give it all of
the tools. We started with one, then 10, then 20, then 30. But you can see as we scale up the
number of tools that we give to the LLM, it's also going to get a
bit more confusing for the
LLM to choose the right tool for the answer that it needs to give.
And we have a single conversation history. So everything that you ask about it
just keeps getting added to the history. And that also means all of those tokens
need to be carried to the next and the next message in the prompt. So to kind of get around
this, we thought, okay, out instead of having one big agent,
we have multiple smaller agents, we try different approaches.
We landed on this approach, which is the multi-agent with delegation. And this kind of means we have a single
coordinator agent that has a much smaller system prompt, and that's
the one that the user interacts with. And then for every task, the
coordinator agent can then decide, oh, somebody's asking about, they have a support question about how
can I add a certain data source? Cool, I'll pass that to the support
agent. Then a support agent can go, it has this support specific
tools, it can search the docs, gets an answer and then gets back.
And same if you ask about dashboards, it can use the dashboard agent to
edit, modify, update your dashboard. And the nice thing is now
it's a bit more modular. All of these agents
individually are smaller. The conversation threads
happen separately. So anything
that support agent does, it still stays in only that thread
and not in the main conversation. And it's a bit more modular,
so it's easier to expand. There's only one downside: it's
that there is some overhead. Every time the coordinator has to
hand off or route to another expert, that means it needs to pass a task and
also at the end it needs to get back an answer. So that does add a bit of overhead
and we're still working on how can we optimize that a bit further
as well. I'm aware of time, so I'm just going to very quickly skip
the recap, but this is what we did. Quick actions, quick
assist, MCP, go try it out. You can also build your own stuff on top
of MCP. Go do that, give us feedback. And then finally, the
agent, if you're interested, you can sign up for the
private preview very briefly, on some things that are coming. So MCP obviously one of the first
things is how can we expand that more? How can we have more
tools? On the agent side, one thing is about
finding things in Grafana. So we are thinking of
how can we use Grafana, knowledge graphs to help the agent
find things inside of Grafana. You can expect more specialized
observability agents, things that also will help you
with your alerts. And finally, we talked about evals. I'll be happy to say we are thinking
of how can we also open this up, help open up some of these evals, especially for things like query
generation and have both the community contribute to that as well.

