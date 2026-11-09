# AI Agent Observability with Grafana Cloud: Debugging, Evaluations, and Guardrails

Published on 2026-11-03T18:53:58Z

## Description

How do you monitor, debug, and evaluate AI agents? In this session, see how Grafana Cloud's Agent Observability solution helps ...

URL: https://www.youtube.com/watch?v=m-3pHXpWwWw

## Summary

The show is titled "AI Agent Observability with Grafana Cloud: Debugging, Evaluations, and Guardrails," published on November 3, 2026. The speakers are Devin, a product director at Grafana, and Jack, a software engineer on the agent observability team. They discuss the importance of observability in AI agents, highlighting features of Grafana Cloud's Agent Observability solution, including instrumentation with OpenTelemetry, quality signal creation, CI/CD for agents, and integration with Grafana's broader capabilities. Key takeaways include the need for specialized metrics for AI agents, the ability to turn failures into test cases, and the importance of monitoring and debugging to improve user trust in AI systems.

Topics: AI agents, observability, Grafana Cloud, OpenTelemetry, CI/CD, debugging, quality signals.

## Chapters

00:00:00 Observability for AI agents
00:05:31 Overview of Grafana Assistant and agent observability
00:11:03 Setting up evaluators for AI agent observability
00:16:32 Evaluating AI agent performance and test cases

Hey everyone, I'm Devin, one of the product directors here at Grafana. 

Yeah. Hey everyone, I'm Jack. I'm a software engineer on the agent observability team. 

Okay. So we're going to talk to you for the next 25 minutes about why observability is the key to trusting your AI agents. We'll start with a little post-launch icebreaker. My favorite ice cream is Ben & Jerry's Half Baked, the absolute best. I'll also accept Fish Food if you like that one. And Devin, it looks like you like M&M's Vanilla Light.

No, this is not bougie enough for me. I'm actually more partial to Strauss. Folks in the Bay Area will know that. And some bougie M&Ms? Unreal. So very nice.

All right. So for this morning, you've been hearing about how agents and agentic operations can help you with observability. This session is going to be focused on observability for agents. We know that many of you are thinking about shipping agents or already have agents in production, and there's been an explosion of agentic use cases over the last year. We have customers that are building everything from booking agents, coding agents, even using agents for marketing campaigns. 

But from the outside, these agents can be a black box, every one of them. So what is an agent? We've had LLMs for a number of years, and we often use this metaphor of the LLM as a brain. You have the LLM for thinking. But with agents, we now have tools where that LLM can actually take action on external or internal systems. They can call an API, call a database, generate code, or even run a search. 

Perhaps most critically, what makes it an agent is that it can take multiple steps autonomously without a human approving each one. It can plan and it can reason. But with this power comes new ways that it can fail. An agent, or an LLM more importantly, is non-deterministic as we all know. What that really means, though, if you're building an agent or an agentic experience, is that your customer or user could ask the same question within seconds and get a different answer. 

It's many steps. Like we said, it can run autonomously. It can act on real systems, which can up the pressure, and it can also fail quietly. In fact, your agent can be available, it can be fast, but it can still be wrong. You could have your more traditional observability metrics like latency, uptime, error rate, and throughput all green, and you could be an engineer on call for, let's say, a banking app. Your support team starts to message you saying, "Gosh, the customers are saying the agent has locked their card, the chat agent is broken," and all your more traditional telemetry signals are green. So that's not a great place to be in.

We actually learned this when we launched our own agents over the last few years. Grafana Assistant, our flagship AI product that you've heard a lot about today, helps you build dashboards and investigate incidents. We learned along the way of building Grafana Assistant the challenges of observing agents. Part of the challenge is when you really scale these agentic systems. We went through that with Grafana Assistant. We pretty quickly went from a hackathon to GA, and now we have over 18,000 organizations that are actively using Grafana Assistant. We have over a hundred plus folks contributing to Grafana Assistant and tens of thousands of users. 

At the start, we were using kind of bespoke dashboards, spreadsheets, very manual or more traditional observability practices. You could maybe call it vibes. A core insight that we learned as we scaled Grafana Assistant is that vibes don't scale. That's why we built Grafana Agent Observability, and that's what we're going to walk you through for the rest of the talk around what the product does.

Throughout the process of developing Grafana Assistant, we came up with four phases and sort of a framework for building agent observability trust. We'll go into each of these areas a little bit more in depth, but we'll start out just by the same way you would instrument a traditional application—by instrumenting it and spot-checking the agent conversations. 

You start out with OpenTelemetry. We can use OpenTelemetry's new GenAI semantic conventions that were released, or we also have an SDK that plugs into different popular agent frameworks. You bring those together into the conversation view, and you get a full picture of how your agent is doing. You can actually get surprisingly far just by instrumenting and looking at a couple of the conversations manually. We learned that firsthand with Grafana Assistant.

Some of those immediate first payoffs you can get are: how much does it cost to run this agent? This comes down from leadership and product—how much is this all costing? Jack, how much are you spending on these tokens?

I'm not going to answer that. 

But yeah, things like also which tools are you running and how often? For Grafana Assistant, it actually has a ton of tools that cover a bunch of different functionality. What if there are tools that are being used like never? Or what are the most popular tools that are being used that we can really focus our efforts into? You can get those insights just by instrumenting. 

Lastly, it's nice to have a system of record for conversations, especially if it's in a very important production system like finance or healthcare. If a customer reports a bad conversation, you need to be able to pull it up and see what happened. 

A really cool example that we learned from Grafana Assistant is that our cache rate actually drops after one pull request, almost to zero. This cost us a ton in tokens because we weren't getting the cache advantages that you get for a cache hit rate. We learned that the issue was we had to introduce a dynamic variable into the very top of the system prompt. We weren't sending a similar request every time. 

We noticed this in agent observability. We were able to move the system prompt further into the conversation and then get huge gains from cost because we were able to restore our cache hit rate. That's something that you can get out of the box just by instrumenting. 

The same thing applies to being in Grafana Cloud. You're instrumenting your services already, so you can trace your agents' requests from the tool call all the way down to the backend service. If there's an issue with your agent, you can immediately tell if it was a backend service issue or if it was an issue with your agent. If it's with the downstream banking service, you might bother that team and say, "Hey, the downstream service is failing. I know my agent is good. Here's the trace to prove it."

So let's take a look at what this looks like. Thanks, Jack. 

Okay. So you've probably seen the banking app already today. I'm going to go in and ask what my balance is. 

Okay, so that is the banking app. They're using an agent in the background to serve this, and let's see what that looks like in agent observability. This is our analytics view. This is kind of the starting point. We give you an opinionated dashboard that gives you headlines around request rate, eval, latency—just a really nice kind of starting point as you're getting started with understanding how your agents are performing. 

Also, there's powerful filtering around models, agents, and even the providers. You can also see here things like the cache hit rate, like Jack mentioned, that you get out of the box. 

What was that? 

I was going to say it just dropped. 

It dropped, yeah. 

Okay. Let's go back to the banking app and ask a slightly different question: What's my pending balance? 

So we ran into an error, and let's see how that shows up. Now I'm going to go into the conversations view. This is a separate view based around a conversation. It's kind of what it sounds like—just sort of a unit that we use to help you organize the interactions with your agent.

I'm going to select the banking general agent because I know that that's the agent where I just saw the error. I'm going to click into this conversation that just happened a minute ago. Here, I get a more detailed view of the chain of events that are happening. I can see the actual user's input and the agent's response. I can also see things like the tool calls, etc. 

I see here that this is probably where the error happened, indicated by that little red dot. I'm going to click into Tempo here. This is an example of the power of using our agent observability because it's based on top of the Grafana Cloud platform, and I get traces. I can actually drill into the full trace for this call and see that there's been an error with the banking service. Sorry, I'm going to scroll down here, and I can actually see that it's a gRPC issue. This has really helped me, in a couple of clicks, go all the way down to the specific call where the agent ran into issues.

Awesome! So that's the first phase of your agent observability trust journey, where you're just starting out by instrumenting. The second phase is building quality signals that are not exposed by traditional engineering metrics. As we mentioned earlier, these baseline metrics might be green, but your agent could be doing things that customers don't like or not working in other ways. So how do we detect those quality signals, and how do we really build our library of signals?

You might have heard before about LLM as a judge or online evaluations. Essentially, every time a conversation is ingested, we run the conversation content through an LLM judge where we can give it a rubric for something like helpfulness. We can say, "Give this conversation a score of one to ten based on what the agent did and how the user reacted to it." You can also do things like true or false, such as whether this conversation used a specific tool. Then, you can route that into a collection to see conversations that used that tool. 

You can do all kinds of cool categorization and scoring with LLM judges. These scores, just like the initial analytics we showed, show up in Prometheus. You can build custom dashboards on these helpfulness scores or LLM judge scores and then do things like alert or build SLOs on top of these. You can treat agents the same way you would traditional software, having these metrics and then alerting on them. If you have something like a prompt change that introduces some weird patterns that you weren't expecting, these scores will catch it, and then you can alert on them. 

Let me jump into a demo to show how this works in agent observability. I'm going to reset this conversation and ask something a little bit different. I'm going to give it something more complicated, like "What's my spending history and any advice?" Okay, and let's go through and lock my card for my own good. Jack, what have you been doing? What kind of spending are you doing here? Okay, let's go ahead and see how we can detect this and prevent it next time.

Let me go into the conversations view and find my conversation that I just had. Awesome! We can see what was my spending history, any advice, and then the freeze card tool activated. You can set up these evaluators manually, but my preferred method is to use Grafana Assistant or something like GCX. If I paste in a prompt here, "Create and enable a helpfulness score for this banking agent," and then also an evaluator that routes tool calls to a collection so I can see all of the conversations where the agent has frozen cards before. 

This is super nice to set up these kinds of routing mechanisms, especially in critical use cases like finance and healthcare, where if things go wrong, you want a human reviewing those types of conversations. You can see it's reviewing the judge catalog, operating your Grafana here. Let me jump into the evaluations page while I approve the things that it's creating. Nice! You can see it's creating these evaluators for me. 

As I mentioned, you can also create them manually here, and we have a library of templates out of the box that you can use. However, often creating custom evaluators is going to be what you want to do because not every agent is the same. Okay, I think that should be the last little rule that it needs here, and then it should give me a nice summary of what it created. Awesome! It created a helpfulness score for me and then freeze card routing.

Let me go ahead and create a new conversation here and try it again. "What are my spending habits? Don't judge." And it still locked my card anyway. Let's see what happens now in the conversation view. If I pull up the most recent conversation, you can see that in evaluations here, there's a little pill that shows that the freeze card call was true. It detected that this freeze card tool was called. 

If I go into conversations and then I go to my saved conversation, "Frozen cards chats detected," I have chats showing up here that are from my frozen card tools. Let's see here. I think I might have named it something different. Frozen. I guess I've been trying this a lot, huh? Okay, yeah, here's mine from just now. If you had tools that you were worried about or if they were really critical use cases that the agent can do, you'd want to route them somewhere like here and then monitor this queue.

Awesome! You can see that after a period of inactivity in the conversation, a conversation-level evaluator showed up scoring it a helpfulness of one, which is something that I could alert on if I didn't have this freeze card thing set up too. Evaluators are super flexible and super powerful. 

Now that we have some of these quality signals set up that we can use, we want to move into the third phase, which is CICD for your agents. This involves turning failures into test cases and proving these changes before they go to production because ideally, we would have caught that issue beforehand. 

I'm going to jump in right back and do another quick demo to show you. In the meantime, my good friend Stephanie has been creating a fix for this agent, and she sent me a pull request. I can see that our agent started shaming people. Okay, blah, blah, blah. Files changed. She changed the system prompt and then she also changed the tool. Great! She added an approval step for this tool, etc. 

But how do I know this change is actually going to work, and how do I have the confidence to approve and merge this? She sent me that she added a new test case to our suite covering card locking behavior and an experiment link. If I open this up, I can see that she sent me two different versions of the agent running over test cases that she's created. 

You can see here that the new version of the agent she created has a higher pass rate because of this one test case she added: "Bank does not irrationally freeze card." The new one didn't judge me at all; it just kind of pulled the request and then gave me some advice, while the other one fabricated a wellness lock policy that is super judgmental. 

These experiments are what you can use as evidence in your pull requests to make changes to your agent and ship confidently. You can also do things like, you might be pretty confident where your agent is right now, but six months from now, whenever they deprecate the model that you're using, how do you know that the new models are going to work with your agent? 

You can run these experiments over different versions of your agent that are each using different models and then compare. For example, you might want to look at how it does with Haiku, Sonnet, Opus. Maybe Opus does the best out of any of the models, but it might be the...

Most expensive and take the most time. So if you can make do with Sonnet and then have it be faster and then cost less, these are kind of the trade-offs that you'd want to look at, and then you can evaluate within experiments. So it's super nice.

Lastly, these test suites that you're creating—so we have this banking capability suite with all the test cases that Stephanie created. If I go into conversations and I pick the one that I just had that was really bad, I can actually promote it to a test case and either capture the input prompt or treat it as a golden final answer. I don't want to do that, but you can really close the loop on catching conversations and then turning them into test cases that you want for no regressions.

Awesome. All right. Thank you, Jack. 

So just to recap, you saw that Jack showed how we can use agent observability to do online eval and to capture when the banking app was locking the card. We then put that into a review queue that a human could look at. We kept that as a test case, and then we can promote it actually into the overall test suite that we're using to make sure that our agent's performance doesn't regress.

One of the other powers of agent observability in general, and we've seen it actually at Grafana, is increasing the ability of subject matter experts at Grafana and then within your organization to write their own evals. Because we have this powerful opinionated tool, more and more product managers at Grafana are able to write their own evals. They are, for example, the dashboarding team. The dashboarding team is the experts in creating dashboards with agents. They've been able now, with agent observability, to write their own evals, and this is just going to give a better experience for our team and then obviously for the end users. Dan from the dashboarding team is going to do a lightning talk on this tomorrow.

Oh yeah. Okay. So I'm going to wrap up with the fourth phase, which is agentic operations. This is really how we can combine the power that you've seen with agent observability with all the other capabilities that we've launched today and recently, including things like watchers. 

One of the benefits that you get with using agent observability within Grafana Cloud is that we're actually writing agent observability data to the knowledge graph. You can get quickly from the data from your agents back to your actual underlying services. For example, like I showed earlier, where you're jumping from perhaps an error that the agents encountered with a tool call, but it's actually an issue with an underlying service. The rest of Grafana also works on your agents. You could have watchers watching your agents. You can obviously interact with agent observability with Grafana Assistant, like Jack showed, and benefit from things like GCX and investigations.

In fact, I think a really powerful pattern is using watchers to observe your agent data, which then can trigger an alert, which triggers an investigation, and then using managed sandboxes. Today, you could have an engineer that would wake up in the morning and have a PR waiting for a review to improve the performance of the agent without them having to do anything. Not only that, but I know a lot of folks have been excited about pages. It's really powerful. Pages is connected to the data within Grafana Cloud, including your agent data. So let's say you're trying to present the ROI on your agent to your leadership. Perhaps your engineers want a different view into the agent experience. You can use pages today to do that.

Nice. So maybe not everyone here is actually building and deploying a production agent. So what if you're not building agents? I can pretty much guarantee that you are building with agents. We also have specialized views for coding agent observability, so things like spend across teams, cost per feature branch. You can really kind of dig into the return on investment you have from the coding agent spend that your org is using. 

We also have built-in PII redaction, and you can see things like MCP and tool usage statistics. If you have an org-level MCP with all the tools for your company, you might want to see who's actually taking advantage of them. Are there ones that we can improve on? These metrics can be used through coding agent observability, and it works out of the box with the popular coding agents. We also have a local version of this that's open source. So if you wanted to put a local tool in your developer's hands to see how their local coding agent workflows are going, that has guard and safety packs that you can take advantage of. 

For example, for myself, I like to have guards over my agent reading M files so it never gets exposed to any secrets. You can do that with this local coding agent observability and then optionally forward to the cloud if you choose to do so.

Awesome. So to recap what we kind of talked about today: the first phase is just the instrument and spot check, and you can get surprisingly far doing just that. Then you want to build some quality signals over the things that your engineering metrics aren't going to cover. Then you can move on to CI/CD, benchmarking your agent, testing new models, making sure that the agent is working before production. Finally, integrate with the rest of Grafana agentic operations to really bring the whole thing together and be proactive about how you're monitoring your agents.

Awesome. So we have a blog post on best practices. You can look at it to keep going, start sending some of your Claude code traces to agent observability. And then also come see us at the AI booth. We're happy to demo any of this more in depth and talk about what you are interested in. 

All right. Yeah. Thank you.

## Raw YouTube Transcript

Hey everyone, I'm Devin, one of the
product directors here at Grafana. Yeah. Hey everyone, I'm Jack. I'm a software engineer on
the agent observability team. Okay. So we're going to talk to you for the
next 25 minutes about why observability is the key to trusting your AI agents. So we'll start with a little post-launch
icebreaker. My favorite ice cream, Ben & Jerry's, half
baked, the absolute best. I'll also accept fish food if
you like that one. And Devin, it looks like you like
M&M's vanilla light. No, this is not bougie enough for me.
I'm actually more partial to Strauss. Folks in the Bay Area will know
that. And some bougie M&Ms, unreal. So very nice. All right. So for this morning, you've been hearing about how agents
and agentic operations can help you with observability. This session is going to be focused
on observability for agents. And we know that many of you are thinking
about shipping agents or already have agents in production and there's
been an explosion of agentic use cases over the last year. We have customers that are building
everything from a booking agent, coding agents, even using
agents for marketing campaigns. But from the outside, these
agents can be a black box, every one of them. And
so what is an agent? We've had LLMs for a number of years
and those we often use this metaphor of the LLM as a brain. So you
have the LLM for thinking. But with agents, we now have tools where that
LLM can actually take an action on external or internal systems.
So they can call an API, can call a database, generate
code, or even run a search. And perhaps most critically, what makes it an agent is that it
can take multiple steps autonomously without a human proving each one.
It can plan and it can reason. But with this power comes new
ways that it can fail. So an agent or an LLM more importantly
is non-deterministic as we all know. What that really means
though, if you're building an agent, an agentic experience, your customer or user could ask the
same question within seconds and get a different answer. It's many steps.
Like we said, it can run autonomously. It can act on real systems so that
can up the pressure and it can also fail quietly. In fact, your
agent can be available. It can be fast. It can
still be wrong though. So you could have your more traditional
observability metrics like latency, uptime, error rate, throughput. They can all be green and you
could be an engineer on call for, let's say a banking app and your support
team starts to message you saying, "Gosh, the customers are saying
the agent has locked their card, the chat agent is broken and all your
more traditional telemetry signals are green. So that's not a
great place to be in." So we actually learned this when we
launched our own agent or agents over the last few years. Grafana Assistant, our flagship AI product that you've heard
a lot about today. It helps you build dashboards, investigate incidents. We learned along the way of
building Grafana Assistant, the challenges of observing agents. And part of the challenge is when you
really scale these agentic systems. And yeah, we went through
that with Grafana Assistant. We pretty quickly went
from a hackathon to GA, and now we have over 18,000 organizations
that are actively using Grafana Assistant. We have over a hundred plus folks
contributing to Grafana Assistant and tens of thousands of
users. And at the start, we were using kind of bespoke
dashboards, spreadsheets, very kind of manual or more
traditional observability practices. You could maybe call it vibes. And a core insight that we learned as
we scaled Grafana Assistant is that Vibestone scale. And so that's why we built Grafana Agent
Observability and that's we're going to walk you through the rest of the
talk around what the product does. Yeah. So throughout the process
of developing Grafana Assistant, we came up with four phases and sort
of a framework for building agent observability trust. And we'll go into each of these
areas a little bit more in depth, but we'll start out just by the same
way you would instrument a traditional application just by instrumenting it and
spot checking the agent conversations. So you start out with OpenTelemetry. So we can use OpenTelemetry's new
GenAI semantic conventions that were released, or we also have an SDK that plugs into
different popular agent frameworks. You bring those together
into the conversation view
and you get a full picture of how your agent is doing. And you can actually get surprisingly far
just by instrumenting and looking at a couple of the conversations manually. We learned that firsthand
with Grafana Assistant. And so some of those immediate first
payoffs you can get is how much does it cost to run this agent? And I guess this
comes down from leadership, product, how much is this all costing? Jack, how much are you
spending on these tokens? I'm not going to answer that. But yeah, things like also which tools
are you running and how often? So for Grafana Assistant, it actually has a ton of tools that
cover a bunch of different functionality. What if there are tools that are being
used like never or what are the most popular tools that are being used that
we can really focus our efforts into? So you can get those insights just
by instrumenting. And then lastly, it's nice to have a system
of record for conversations, especially if it's in a very important
production system, finance, healthcare. If a customer reports a bad conversation, you need to be able to pull
it up and see what happened. So a really cool example that we learned
from Grafana Assistant is that our cash rate actually drops after one
pull request almost to zero. And so this cost us a ton in tokens
because we weren't getting the cash advantages that you get for a cash hit
rate. We learned that the issue was we had to introduce a dynamic variable
into the very top of the system prompt. So we weren't sending a similar
request ever every time. So we noticed this in agent observability. We were able to move the system prompt
kind of further into the conversation and then get huge gains from cost because we
were able to restore our cash hit rate. So that's something that you can get
out of the box just by instrumenting. Same thing, a benefit of being in Grafana Cloud is
that you're instrumenting your services already. So you can trace your agents requests
from the tool call all the way down to the backend service. So if there's
an issue with your agent, you can immediately tell
if it was a backend service
issue or if it was an issue with your agent. So if it's with
the downstream banking service, you might bother that team, say, "Hey,
the downstream service is failing. I know my agent is good.
Here's the trace to prove it." So let's take a look at
what this looks like. Thanks, Jack. Okay. So you've probably
seen the banking app already today. I'm going to go in and
ask what my balance is. Okay, so that is the banking app. They're using an agent in the background
to serve this and let's see what that looks like in agent observability.
So this is our analytics view. This is kind of the starting point. We give you an opinionated dashboard
that gives you headlines here around request rate, eval, latency, just a really nice kind of starting
point as you're getting starting with understanding how your
agents are performing. Also powerful filtering around models,
agents, and even the providers. You can also see here things like the
cash hit rate, like Jack mentioned, that you get out of
the box. What was that? I was going to say it just dropped. It dropped, yeah. Okay. Let's go back to the banking app and
ask a slightly different question. What's my pending balance? So we ran into an error and
let's see how that shows up. So now I'm going to go into
the conversations view. So this is a separate view based
around a conversation is kind of what it sounds like, just sort of a unit that we use to help
you organize the interactions with your agent. I'm going to select the banking general
agent because I know that that's the agent that I just saw the error in and I'm going to click into this conversation
that just happened a minute ago. So you can see here I get a more detailed
view on the kind of chain of events that are happening. I can see the actual
user's input, the agent's response. I can also see things like the tool
calls, et cetera. But I see here, this is probably where the error
happened, that little red dot. And I'm going to click into tempo here. And this is an example of the power of
using our agent observability because it's based on top of the Grafana
Cloud platform and I get traces. So I can actually drill into
the full trace for this call and I see that there's been an
error with the banking service. Sorry, I'm going to scroll down here and I can
actually go in and see that's actually a GRPC issue. So this has really helped me in a
couple clicks go all the way down to the specific call where the
agent ran into issues. Awesome. So that's the first phase of kind of
your agent observability trust journey where you're just starting
out by instrumenting. The second is building quality signals
that are not exposed by traditional engineering metrics. So as
we kind of mentioned earlier, these baseline metrics might be green, but your agent could be doing things that
customers don't like or not working in other ways. So how do we detect those quality signals
and how do we really build our library of signals? So you might have heard before about
LLM as a judge or online evaluations. So these are essentially every
time a conversation is ingested, we are running the conversation content
through an LLM judge where we can give it a rubric for something like, for
example, helpfulness. We can say, give this conversation a score of one to
10 based on what the agent did and how the user reacted to it.
You can also do things like true or false, like did this conversation use this tool? And then you can route that into a
collection to see conversations that used that tool. So you can do all kinds of
cool categorization and also
scoring with LLM judges. And these scores, same as the
initial analytics that we showed, show up in Prometheus. So you can build custom dashboards on
these helpfulness scores or LLM judge scores and then do things like alert
or build SLOs over top of these. So you can treat agents kind of the
same as you would traditional software, having these metrics and
then alerting on them. So if you have something like a prompt
change that introduces some weird patterns that you weren't expecting, these scores will catch it and then you
can alert on them. So it's super nice. And let me jump into a demo
to show how this works in agent observability. So I'm going to reset this conversation
and ask something a little bit different. I'm going to give it something
more complicated like
what's my spending history and any advice. Something like that. Okay. And let's go through and
lock my card for my own good. Jack, what have you been doing? Okay. What kind of spending are you doing here? Okay. Okay. Let's go ahead and see how we can
detect this and prevent it next time. So let me go into the conversations view
and I'll find my conversation that I just had. Awesome. And so we can
see what was my spending history, any advice, and then the
freeze card tool activated. So you can set up these
evaluators manually, but my preferred method is to use
Grafana Assistant or something like GCX. So if I paste in kind of a prompt here, create and enable a helpfulness
score for this banking agent, and then also an evaluator that routes
tool calls to a collection so I can see all of the conversations where
the agent has frozen cards before. This is super nice to set up
these kinds of routing mechanisms, especially in critical use
cases, think finance, healthcare, where things going wrong, you want a human reviewing those types
of conversations. So you can see it's kind of reviewing the judge
catalog, operating your fana here. Let me jump into the evaluations page
while I approve the things that it's creating. Nice, you can see it's
creating these evaluators for me. And so as I mentioned, you can also create them manually here
and we have a library of templates out of the box that you can use, but often creating custom evaluators is
going to be what you want to do because not every agent is the same. Okay. I think that should be the last
little rule that it needs here. And then it should give me a nice
kind of summary of what it created. Awesome. So it created helpfulness score
for me and then freeze card routing. So let me go ahead and create a new
conversation here and try it again. What are my spending habits? Don't judge. And it still locked my card anyway. So let's see what happens
now in the conversation view. So if I pull up the most
recent conversation, you can see that in evaluations here, there's a little pill that shows
that freeze card called was true. So it detected that this
freeze card tool was called. And if I go into conversations and
then I go to my save conversation, frozen cards chats detected, I have chats showing up here
that are from my frozen card tools. Let's see here. I think I might
have named it something different. Frozen. I guess I've been trying
this a lot, huh? Okay. Yeah, here's mine from just now. So if you had tools that you were worried
about or if they were really critical use cases that the agent can do, you'd want to route them somewhere
like here and then monitor this queue. Awesome. So let's see here. And you can see that after a period
of inactivity in the conversation, a conversation level evaluator showed
up scoring it helpfulness of one, which is something that I could alert on
if I didn't have this freeze card thing set up too. So evaluators are
super flexible and super powerful. So awesome. So now that we have some of these
quality signals set up that we can use, we want to move into the third
phase, which is CICD for your agents. So this involves turning failures into
test cases and proving these changes before it goes to production because
ideally we would have caught that issue beforehand. So I'm going to jump in right back and
do another quick demo and show you. So in the meantime, my good friend Stephanie has been creating
a fix for this agent and she sent me a pull request so I can see that our
agent started shaming people. Okay, blah, blah, blah. Files changed. Okay. So she changed the system prompt
and then she also changed the tool. Great. So she added an approval
step for this tool, et cetera. But how do I know this change is actually
going to work and how do I have the confidence to approve and merge this?
So she sent me that she added a new test case to our suite covering card locking
behavior and an experiment link. So if I open this up, I can see that she sent me two different
versions of the agent running over test cases that she's created. So you can see here that the new version
of the agent that she created has a higher pass rate because of
this one test case she added, bank does not irrationally freeze card. And you can see that the new
one didn't judge me at all. It just kind of pulled the request and
then gave me some advice while the other one fabricated a wellness lock
policy that is super judgemental. So these experiments are what you can
use as evidence in your pull requests to make changes to your agent
and ship confidently. You can also do things like you might
be pretty confident where your agent is right now, but six months from now, whenever they deprecate the
model that you're using, how do you know that the new models are
going to be working with your agent? So you can run these experiments over
different versions of your agent that are each using different models
and then compare. For example, you might want to look at how it
does with Haiku, Sonnet, Opus. Maybe Opus does the best
out of any of the models, but it might be the most
expensive and take the most time. So if you can make do with Sonnet
and then have it be faster and then cost less, these are kind of the trade offs that
you'd want to look at and then you can evaluate within experiments. So
it's super nice. And then lastly, these test suites that you're creating, so we have this banking capability suite
with all the test cases that Stephanie created. If I go into conversations and I pick
the one that I just had that was really bad, I can actually promote it to a test case
and either capture the input prompt or treat it as a golden final answer.
I don't want to do that, but you can really close the loop on
catching conversations and then turning them into test cases that
you want for no regressions. Awesome. All right. Thank you,
Jack. So just to recap, you saw that Jack showed how we can
use agent observability to do online eval and to capture when the
banking app was locking the card. We then put that into a review
queue that a human could look at. We kept that as a test case
and then we can promote it actually into the overall test suite
that we're using to make sure that our agent's performance doesn't regress. And one of the other powers of
agent observability in general, and we've seen it actually at Grafana, is increasing the ability of subject
matter experts at Grafana and then within your organization to
write their own evals. So because we have this
powerful opinionated tool, more and more product managers at Grafana
are able to write their own evals. They are, for example,
the dashboarding team. So the dashboarding team is the experts
in creating dashboards with agents. They've been able now with agent
observability to write their own evals, and this is just going to give a
better experience for our team and then obviously for the end users. Dan from the dashboarding team is going
to do a lightning talk on this tomorrow. Oh yeah. Okay. So I'm going to wrap up
with the fourth phase, which is agentic operations. And this is really how we can combine
the power that you've seen with agent observability with all the other
capabilities that we've launched today and recently, including things like watchers. One of the benefits that you get with
using agent observability within Grafana Cloud is that we're actually writing
agent observability data to the knowledge graph. And so you can get quickly
from the data from your agents back to your actual underlying
services. So example, like I showed earlier where you're jumping
from perhaps an error that the agents encountered with a tool call, but it's actually an issue
with an underlying service. The rest of Grafana also
works on your agents. So you could have watchers
watching your agents. You can obviously interact with agent
observability with Grafana assistant like Jack showed and benefit from
things like GCX and investigations. In fact, I think a really powerful pattern is
using watchers to observe your agent data, which then can trigger an alert, which triggers an investigation
and then using managed sandboxes. Today, you could have an engineer that would
wake up in the morning and have a PR waiting for a review to
improve the performance of
the agent without them having to do anything. Not only that, but I know a lot of folks have been
excited about pages. It's really powerful. Pages is connected to the data within
Grafana Cloud, including your agent data. So let's say you're trying to
present the ROI on your agent to your leadership. Perhaps your engineers want a different
view into the agent experience. You can use pages today to do that. Nice. So maybe not everyone
here is actually building
and deploying a production agent. So what if you're
not building agents? I can pretty much guarantee that
you are building with agents. So we also have specialized views
for coding agent observability, so things like spend across
teams, cost per feature branch. You can really kind of dig into the
return on investment you have from the coding agent spend that your org is using. We also have built in PII redaction and
you can see things like MCP and tool usage statistics. So if you have an org level MCP
with all the tools for your company, you might want to see who's
actually taking advantage of them. Are there ones that we can improve on? These metrics can be used through coding
agent Ollie and it works out of the box with the popular coding agents. And we also have a local version of this
that's open source. So if you wanted to put a local tool in your developer's
hands to see how their local coding agent workflows are going, that has guard and safety packs that
you can take advantage of. For example, for myself, I like to have
guards over my agent reading. M files so it never gets
exposed to any secrets. You can do that with this local coding
agent observability and then optionally forward to the cloud if you
choose to do so. Awesome. So to recap what we kind
of talked about today, the first phase is just the instrument
and spot check and you can get surprisingly far doing just that. Then you want to build some quality
signals over the things that your engineering metrics aren't going to
cover. Then you can move on to CI/CD, benchmarking your agent,
testing new models, making sure that the agent
is working before production. And then finally integrating with the
rest of Grafana Agentic operations to really bring the whole thing together
and be proactive about how you're monitoring your agents. Awesome. So we have a blog post on best practices.
You can look at it to keep going, start sending some of your Claude
code traces to agent observability. And then also come see us at the AI booth. We're happy to demo any of this more
in depth and talk about what you are interested in. All right. Yeah. Thank you.

