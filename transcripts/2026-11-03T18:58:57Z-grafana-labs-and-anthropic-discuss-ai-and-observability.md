# Grafana Labs and Anthropic Discuss AI and Observability

Published on 2026-11-03T18:58:57Z

## Description

What does it take to observe AI agents, and how are agents changing observability itself? In this ObservabilityCON 2026 fireside ...

URL: https://www.youtube.com/watch?v=mWYv38p8tjY

## Summary

The show "Grafana Labs and Anthropic Discuss AI and Observability" took place on November 3, 2026, featuring Tom Wilkie, CTO of Grafana Labs, and Katelyn from Anthropic. The discussion revolved around the intersection of AI and observability, focusing on how AI agents are transforming the landscape of monitoring and managing systems. Key topics included the integration of OpenTelemetry in Anthropic's API suite, the shift towards agent-driven observability, and the evolving role of human oversight in automated processes. Both speakers emphasized the importance of safety and compliance in deploying AI systems, as well as the need for robust monitoring to ensure quality and security.

Topics: AI, Observability, OpenTelemetry, Grafana, Anthropic, Automation, Safety, Compliance

## Chapters

00:00:00 The relevance of AI and Observability
00:05:40 The role of OpenTelemetry in AI observability
00:11:14 The role of agents in software verification and observability
00:16:48 Monitoring agent behavior and audit trails in regulated industries
00:23:08 The impact of agents on observability and decision-making

Okay, so for our last session today, we're going to do a little bit of a fireside chat. We're going to bring out Tom Wilkie, our CTO, and Katelyn from Anthropic. Harry will be asking the questions while Tom and Katelyn provide the answers. So, come on stage, guys. Got me running to keep up! This is my last thing of the day, so I'm excited to get this going.

So, real quick question: Who here thinks maybe we should watch AI just a little more closely? Raise your hand. Oh, there's at least five of you. Great. Fantastic! All right, this is the panel for you.

So, Tom and Katelyn, first, I guess just for this audience, how is what you do relevant to this group of people who care about Observability? Tom, let's start with you in case they don't know you.

I mean, I think you'll know who I am at this point. You had to listen to me this morning. How is what I do relevant to AI and Observability? I lead the engineering team at Grafana Labs, and we build AI Observability tools as one of the many things. We also build a ton of agents for you guys to use, and that's, I guess, the short answer.

Perfect. Katelyn?

Cool. So, I lead Platform at Anthropic. Platform is our API suite, all of our developer tools, and we run our product infrastructure and core services and things like this. We are supporting many people who are building agents that need to be observed, but we are also building some pretty crazy at-scale systems right now that also themselves need to be observed.

Okay, so first I just want to get across how you use and understand each other's tools. Tom, let me start with you. When did you figure out how Claude and Anthropic fit into your thinking, to shipping products, and whether they're heading in the same direction about Observability?

I'm known to give really long answers, so please— 

I'll cut you off.

Cut me off. I think we're relative latecomers to this whole game, to be brutally honest. We've been experimenting with LLMs for a very long time, but the early stuff we did was very much generative, one-shot, like, "Title this dashboard for me," or, "Explain this flame graph." It didn't really move the needle. It was about 18 months ago when Matt and the team— you've all met Matt— when they started showing off some of the agentic capabilities, like what you can do when you give these models tools to interact with the rest of the platform, that we really drank the Kool-Aid at that point. So, it was 18 months ago. I think we were a latecomer, but honestly, now we're all in. 

Now, seeing this shift, as we talked about this morning, to giving more and more powers to these agents, the sandboxes, and having them run more and more of Grafana Labs operations internally. From Anthropic's perspective, most of what we do model-wise uses Anthropic's models in the product. And then— 

You're welcome.

Most. And then— what a coincidence that she happens to be here. We have a great relationship with Anthropic. We love their models, and I think they were the ones that had the best tool hauling support and the best support for our products very early on. Internally, we're also just huge Claude Code users. I think every single one of my engineers is using Claude Code on a daily basis. We don't just use Claude Code; we also use other ones, but Claude Code is the most popular one internally.

Nice. Love it. Love it. Huge fans. How do you guys use Grafana?

A lot of ways, but primarily within our own systems. It's pretty cool because I think this is obviously starting to shift over time for us the way that it is for everybody else. We have less humans looking at dashboards and more agents monitoring systems still on top of Grafana, which is great. 

I was actually thinking about some interesting stories recently where we've had some sort of Grafana-assisted situation that could have been bad but wasn't. One of the more interesting ones that happened recently was that we run safety classifiers on all of the tokens that are flowing through Claude. It's interesting because these are inherently non-deterministic systems. We recently had one very specific classifier where we were seeing one out of every 100 requests that were coming through where Claude was kind of getting a low confidence answer on, "Is this safe or unsafe?" 

Anomaly detection is hard, and these things can fly under the radar, but the team was alerted relatively quickly, and we were able to go figure out what was going on. Just like probably every single one of you has a story like that, there's an interesting shift happening where in the past, maybe we got an alert and a human got woken up, and something happened. We're seeing more and more that sort of thing happens, and an agent finds out first and is doing something about it, which is a crazy shift. It's nice that the tools continue to plug in really nicely even throughout that shift towards agents.

You guys just rolled out a new OpenTelemetry product, right? Was it because there was an opportunity you saw, or was it a failure that you wanted to prevent in the future? Why?

Well, we were actually pretty slow on that. We should have done it a long time ago. But yeah, as of last week, we have OTel support in the Claude Platform, so our API suite. This is generally just because people are building agents on top of our APIs. They need to be able to monitor those traces and see what's going on. 

When we were first starting to build more and more capabilities around agents, models can run for longer, and people are trying to build cloud-based agents. Here's infrastructure that helps you do it. We had built in some Observability tooling around these things, but the very first thing that everybody told us was, "We don't care about your Observability tooling. We want to use the Observability tools that we already know and love." 

I think we were kind of slow with it, but we did it, and we now have OTel support for our APIs and partnered with Grafana. Now you can observe your agent traces to your heart's desire.

I love this story as well because I can remember I opened a PR against the Cassandra Project to add Prometheus instrumentation, and it immediately got closed as, "No, we don't want to pick a particular vendor." They don't want to pick sides. I'm like, "Well, Prometheus is open source." But that's the whole point of OpenTelemetry. It is vendor-neutral. By Anthropic baking in OpenTelemetry support, they're not blessing any one vendor, and it's for everyone's gain. That's what we're about at Grafana Labs as well. Obviously, it helps us because we're OpenTelemetry-native, but it helps the whole ecosystem.

So, Tom, you said in your keynote that AI was kind of a cheat code. I guess, give me an example of something that you can do now or is being done throughout Grafana today that was difficult or impossible, let's say, 18 months or two years ago.

So the cheat code— we actually changed that messaging at the very last minute. I think we now call it the not-so-secret weapon. The cheat code stuff didn't translate to Japanese or something. The story there is how the open-source community we have of users generates so much content on the Open Web about our products. Of course, most of our products and technology are open source. The Anthropic models just know how to use our software for whatever that means nowadays, for whatever intelligence means nowadays. They just know how to use our software. 

When we were building, when Matt, Cyril, and co were building the first version of the Assistant, we were blown away at the emergent capabilities if you just gave a model some tools to interact with Grafana and data sources and Prometheus and so on. That was the aha moment for us. But even you saw the pages... Or you haven't seen the Pages demo.

I've got to show it to you. The Pages demo is the next generation of dashboards for us and how you build way more interactive and beautiful visualization systems. But honestly, so much of that is model capabilities. The new generations of models for Anthropic are just so much more visually pleasing in the interfaces that they generate. That's why we're such a fan.

So, I don't have to be a system administrator to understand the data?

Yeah, not just that, but you don't have to be a system admin. You don't have to be a graphical artist to build a beautiful visualization either, right? 

Is there a place where, I guess a question for both of you is, what is the line that you would draw at AI to alter? I mean, would you let it go and change something in production? Is it a step before that? Given the volume of changes that might be made, how do you strike that balance between when the human should intervene and when the software can do it by itself?

Let me start with you. I think a lot of this comes down to just how you think about guardrails and how you think about monitoring. It's about putting an agent in an environment where it can't do anything that's catastrophically bad, or if it were going to, you'd know before something actually happens. 

When it comes to our team and how we're actually building and maintaining our systems, all of our code is written by Claude—literally all of it. When it comes to the automation that we're building around the edges, a really great example is we run an agent that's monitoring CI. If CI goes red, then the agent does something about it. Right now, the thing that the agent will do with no humans in the loop is just fix a flaky test or fix a test. It'll touch the test if that's what's actually broken and causing a problem.

But now we're starting to get into how we get comfortable with no humans in the loop, that agent making a change to the actual services codebase. I think it's going to be really interesting where and how we experiment. It's the same thing with a page hitting an agent before it hits a human. We have some teams that are starting to experiment with Claude getting paged before humans do. Right now, it's a same-time sort of thing. But we're just starting to see that half the time, by the time a computer wakes up and opens a computer, the agent has made a lot of progress. So, did the human need to wake up? I don't know.

I think these things will just kind of get better as model capabilities get better. For us, we're just seeing the line. As engineering leaders, we're terrified, and we're like, "Let's be really careful about this." But I think the line is starting to push. Had you said to me six months or a year ago that we'd be in a place where there's any type of change that zero human in the loop—nobody is touching it and we feel comfortable with it—I would've been like, "No, we need more time. We're not really getting there yet." But the models have gotten really good, and we're getting there.

We're super strict about this. Currently, at Grafana Labs, every change has to be human-reviewed. For our security and compliance footprint, this is really important to us. We definitely need to start thinking about what kind of changes we can allow to be automatically merged, but we're going to have to start really small with very specific changes—like docs changes, maybe test changes. These kinds of things we can experiment with.

One concrete example: we run 30 regions of Grafana Cloud around the world, all completely isolated from each other. We have deterministic software checks in every change to make sure that changes only touch a single region. That's a great way to say, "Okay, that's giving us a lot more confidence if that check passes that at least the blast radius is smaller." 

It's not going to be enough for us to automerge agent changes for sure. But maybe if we can determine that they're only rolling back a version or if they're only tweaking some whitelist set of flags within known boundaries, we need to definitely experiment on this. But right now, the status quo is like, "No, every change has to be human-reviewed." 

That doesn't mean we can't use agents to pre-review everything. It doesn't mean most teams in Grafana Labs have to get to a green agent review before they even ask a human to look at it. Because the agents have all had their go at it, the amount of attention I think the human needs to pay to each change can go down, and the confidence can go up. It also means agents are driving huge amounts of increases in test coverage for us, which again makes it much easier for us to—I'm not going to say wave through changes—but minimally review them.

So, abstractly, if agents are checking the work of other agents checking the work of other agents, is it just turtles all the way down? How at that core first level, explain that to somebody maybe who's not in this world.

I think the way that we think about it is our systems are designed by humans. At a high level... I was telling these guys this yesterday, we, as of a couple weeks ago, fully rolled out our entire API in Rust. It used to be a Python monolith, and we ported the entire thing to Rust because we needed to for scale and efficiency purposes primarily. But we didn't start with a single Rust developer on our team; it was the right choice, and Claude knows what it's doing.

What mattered the most was we designed the system. The team designed the system and knew, "Here's all the right components, here's how all these things need to fit together, here's all the properties we need to adhere to," and all these sorts of things. But then when it comes to implementation, we don't need a human pressing keys in order to get the lines of code written. It's fine for Claude to do that.

But then I think what the humans did was not just design the system, but design the verification system that got us comfortable with doing that. The way that we rolled this out was we were like, "Okay, we're going to have Python running and Rust running, and we don't look at prompts, we don't look at completions, we don't see any data, so how do we make sure it's working correctly?" We actually did it based on token counts. If the same number of tokens was coming out of the Python system and the Rust system, then that was pretty good verification that it was going to work.

How could we think about that system and running all the shadow traffic through that second system to see if it was going to perform at high quality? That was all human thinking that went into all of that. But the grunt work of building the pieces and actually monitoring the pieces and actually making sure that we felt good about it—that was agents all the way down.

Wow. I mean, as Tom said, that's not just changing an airplane engine; that's designing, building, and changing an airplane engine while you're flying over the Pacific. That's really...

So, Tom, I guess now the way she's saying that, is the verification and observability now part of just generally the safety conversation? I mean, it used to be something in a totally different category.

Yeah, 100%. I mean, there's always been this argument that observability is an extension of testing. I kind of alluded to it this morning: the way we qualify software releases is by running them and checking all the alerts on firing and checking they're within SLO and within cost and so on. 

So there's definitely unit testing, but when we don't do a ton of automated integration testing, we rely on the integration environments, deploying to them and checking the properties are the same. There's definitely an extension of that in the agentic era. It's not just the very easy-to-measure...

**Properties of Latency, Error Rates, and CPU Consumption**

There's now the scores we get out of our evaluations, telling us if our agents are behaving in a similar way or getting better or worse. These two aspects have always been a spectrum, but even more so now. A good example is our focus on agent safety and security—not just because that's why we exist, but also because everyone is a little concerned about agents breaking out of sandboxes. 

How do we think about these problems? We break it down into two main areas: safety in the sense of training the models to do good things and not bad things, and the safety classifiers that we're running on the tokens being produced. Then, there's the layer of the problem that's about agent infrastructure—the engineering of the system. 

One interesting area we're starting to explore is monitoring and observability around what an agent might be trying to do and how we can get alerted on that. For example, most of the time, an agent breaking out of a sandbox really just means you have network egress turned on in your sandboxes. The agent writes some code that executes in the sandbox, and that code is doing something over the internet—calling a tool, calling an API, or whatever it is. 

What we've started to do is monitor certain shapes of tool calls that are essentially network egress attempts. Even if you have a domain allow list, you can only exit the sandbox to hit specific domains. If the agent tries to call other tools or hit other APIs, you can monitor and say, "We saw three instances in this one session of the agent trying to talk to an external tool that it wasn't meant to be talking to." Even though nothing bad happened, that tells you a lot about how you've prompted that agent or how that agent is set up. 

There are many interesting monitoring problems emerging when it comes to ensuring that security is where it needs to be with agentic systems. This is the same signal we look at from an overall quality perspective. The way we've made the observability agents in Grafana Cloud fast and relatively cost-effective is by optimizing the tool calls so they don't fail three times with the wrong parameters. They just know the right thing to call first, mostly because we changed the parameter names to match what the model would have guessed. 

How good can you stay at that guessing game? It's a constant battle. I know Anthropic strives to have compatibility across model versions, but as we're upgrading and using different models, we have to constantly tweak and tune this. 

**Audit Trails in Different Industries**

You both have visibility into different sectors and industries. What kind of audit trails do these different companies and industries want to feel comfortable running different systems? I don't know if you've heard feedback from vendors saying, "Oh, I would try this, but I am in a highly regulated industry and I need to have... If you're telling me this happens every three milliseconds, I don't even know where to store that and how to read that data. But if you're telling me, 'Okay, once a day I get an email that says something weird happened,' that's what's going to be used against me in a court of law in Australia or the United States."

We have tons of audit controls on Grafana Cloud. From the agentic perspective, a lot of our logs serve as an audit trail for what the agent has done. The observability of the agent conversations is essentially the audit trail of what the agent has done. Audit concerns don't often come up from a "I'm in a heavily regulated industry" perspective. Instead, we often hear from heavily regulated industries that they need to have it running inside their firewall, under their control, and in their data center or on their platform. 

For the really risk-averse ones, we have a FedRAMP offering for Grafana Cloud. It's a trimmed-down version of the product, operated in the U.S. by U.S. personnel with all the right accreditations. This tends to be more about deployment than getting the right level of audit control, which has been relatively straightforward. 

For example, NASA is watching rockets go up into the sky. We have videos with different rocket companies using Grafana, but most of those are using our open-source technology and running it inside their boundary, which is a well-defined problem.

**Safeguards and Compliance**

So, what is Anthropic doing here to preemptively say, "Here are the safeguards we've built in. This is why we know you can deploy it well"? With our OpenTelemetry (OTel) launch, we leaned into the generative AI open standard. We thought, "We could shape our traces however, but let's try to make this easier for people and go with something open and see if the industry converges around it." 

Our thinking is to give people the data and let them use tools like Grafana to figure out how they want to monitor those things or what they might want to do on top of that. For our most regulated customers, they need compliance regimes in place and all the data in a place where they can run whatever they want on it. 

An interesting example comes from a fintech customer involved in underwriting. They were concerned about being audited by regulators on how they did their underwriting. If they were going to have an agent underwriting people for a loan instead of a human, they needed to get their auditors comfortable with this. We worked with them on a suite of evaluations that showed their underwriting agent was performing at the same quality level as a human. They have that evaluation data ready for auditors who might ask, "You have agents running underwriting; how are you maintaining quality?" They can respond with, "Here are our continuously running evaluations," which is crucial for model upgrades to ensure the agent continues to perform at a high quality. 

**Cloud Economics and Query Patterns**

So, Tom, how do the cloud economics change as people start to have more agents doing more tasks? Have you ever had a scenario where someone rings up a sizable bill? 

Oh, this is a fascinating topic. The biggest thing we see is completely different query patterns from agents against the telemetry data. They look nothing like human queries. For the longest time in Grafana Cloud, we charged based on the amount of data we stored. After adaptive, we take out the stuff you don't need and then charge you for the amount you need. That worked...

Really well. That got us to where we are today. But with the shift to agentic and that, let's face it, massive increase in query load, that is shifting the economics. Our approach here is to have a really, really generous included query allowance in every bit of data you read. However, for a very small number of customers who are seeing 1,000 times more reads than the average customer, there are going to be some increases in query costs coming their way. This is a tricky one for us, and obviously, we talk to the customer and help them optimize their workloads.

There's a company, or a name, but they started building an agent on top of Loki, and it just blew out the query cost. We worked closely with them to shape that, and some of the query optimizations that we announced today really helped them. But they just don't look like humans. 

The other thing about agents is that if you go and ask an SRE to respond to an incident, that SRE is going to have some biases. Maybe they prefer metrics or logs and will use those predominantly more than other signals. Agents don't have those biases. They may have different biases for sure, but they tend to use all the sources they can access. They have this nice property of using anything they can get their hands on to figure out what happened. This, in turn, has driven a lot of adoption of traces, profiles, and other signals that were maybe not as preferred by humans.

As we wrap up here, some rapid fire. Oh wow, I was just getting into this. Exactly. What is something you believe today that you expect to change in six months, and you wouldn't be surprised if you were like, "Well, obviously I got that wrong"? 

I mean, I do think that we're going to see more and more of us changing our line of where we feel comfortable letting agents do work and make decisions. One of the really interesting things is that there are situations where letting an agent have more agency is safer and more secure than not. A really good example is that we really recommend, both in Claude Code and in our managed agents architecture, that for tool calling, you turn on auto mode. This means letting Claude ask another Claude, "Should I approve this tool call or not?" 

Every single test that we could possibly run shows us that you're getting better and more secure outcomes if you let Claude decide rather than a human who is impatient and just smashing the button or running with dangerously skipped permissions or whatever it is. Having Claude literally just go ask another Claude is one of the most secure things that you can do. This is something that's counterintuitive for a lot of people. 

So, for me, my own line of where I feel good about my team saying, "Okay, great. No human actually looked at this thing that happened, but it's okay," I think it's probably going to shift and it'll probably shift further and faster than I am expecting it to today. 

Tom? 

I'm going to step outside of the whole Observability stuff for a minute and just talk about my other passion, which is home automation. I do a lot of work with Home Assistant. I forgot the name of the system, but when the first autonomous home agents came out, I had it start managing my hot water. I live in the U.K., and we don't have always-on hot water; it has to go on for an hour so that you can have a shower. 

Here, we call it the "geezer." You have to press the button on, and this might sound weird, but I sometimes have to get up at 3:00 AM to catch a flight. So that was the problem I gave the agent, and it figured it out. It did a really good job. It turned the hot water on nice and early so I could have a shower at 3:00 AM before I go and catch my flight. It also figured out I wasn't in the house after that, so it turned the hot water off for the week. My wife got really upset about that. 

This was a year ago, and that got turned off pretty quickly. But now I'm using Claude Code with my Home Assistant, and I'm developing deterministic automations. The level and quality of my home automation is through the roof, to the point where I have this thing called WAF, the wife acceptance factor. If my wife likes it—she's an eval. Yeah, exactly. I'm not going to say that out loud again. 

Even my wife has commented on how good the home automation is getting. So I think, I guess the prediction I'll make is that we're talking about agentic right now as it's the new shiny thing, and we notice when it's clever. This is going to blend into the everyday. Even in six months' time, the rate of change is so quick. 

Now, I had a holiday—I mean, I had to work for most of the holiday—but I took a holiday and I planned it with Claude. I didn't let Claude book the hotels; I did that manually. But honestly, for the next holiday, Claude is just going to be booking everything for me. It's just going to blend into the everyday, and you're not even going to think about the fact that this is an agent doing it for you. This is just going to be expected. 

Okay. We'll have you back in six months to check on these predictions. Thank you all. 

See if my hot water is working. 

Exactly. Tom, Katelyn, thank you all. Thank you.

## Raw YouTube Transcript

Okay. So for our last session today, 
we're going to do a little bit of a fireside chat. So we're going to bring out Tom 
Wilkie, our CTO, and Katelyn from Anthropic, and we'll have Harry who is going to ask 
the questions while Tom and Katelyn give the answers. So come on stage, guys. Got me running to keep up. This is my last thing of the 
day, so I'm excited to... Let's get this going. So real quick question. 
Who here thinks maybe we should watch AI just a little more closely? Raise your hand. Oh, there's 
at least five of you. Great. Fantastic. All right, this is the panel for you. So Tom and Katelyn, 
first, I guess just for this audience, how is what you do relevant to this group of people who 
are here, care about Observability? Tom, let's start with you in case they don't know you.
I mean, I think you'll know who I am at this point. You had to listen to me this morning. How 
is what I do relevant to AI and Observability? I lead the engineering team at Grafana Labs 
and we build AI Observability tools as one of the many things. So we also build a ton 
of agents for you guys to use and that's, I guess the short answer.
Perfect. Katelyn? Cool. So I lead Platform at Anthropic. Platform 
is our API suite, all of our developer tools, and we run our product infrastructure and 
core services and things like this. And so, we are supporting many people who are building 
agents who need to be observed, but we are also building some pretty crazy at-scale systems right 
now that also themselves need to be observed. Okay. So first I just want to get across how 
you use and understand each other's tools. Tom, let me start with you. I mean, when did you 
figure out how Claude and Anthropic fit into your thinking, to shipping products, and 
then also whether they're heading in the same direction about Observability?
So I'm known to give really long answers, so please-
I'll cut you off. Cut me off. I think we're relative late comers to 
this whole game, to be brutally honest. We've been experimenting with LLMs for a very long time, but 
the early stuff we did was very much generative, one shot, like, "Title this dashboard for me," or, 
"Explain this flame graph." And didn't really move the needle. It was about 18 months ago when Matt 
and team, you've all met Matt, when they started showing off some of the agentic capabilities, 
like what you can do when you give these models tools to interact with the rest of the platform 
that we really drunk the Kool-Aid at that point. So it was 18 months ago. I think we were a 
late comer, but honestly, now we're all in. And now seeing this shift, as we talked about this 
morning, to giving more and more powers to these agents, the sandboxes and having them run more 
and more of Grafana Labs operations internally. From Anthropic's perspective, most of what we do 
model-wise uses Anthropic's models in the product. And then... You're welcome. Most. And then-
What a coincidence that she happens to be here. We have a great relationship with Anthropic. We 
love their models. And I think they were the ones that had the best tool hauling support and the 
best support for our products very early on. And then internally, we're also just huge Claude Code 
users. I think every single one of my engineers is using Claude Code on a daily basis. We don't 
just use Claude Code. We also use other ones, but Claude Code is the most popular one internally.
Nice. Love it. Love it. Huge fans.
Love it. How do you guys use Grafana?
A lot of ways, but primarily within our own systems. And so, it's pretty cool because 
I think this is obviously starting to shift over time for us the way that it is for everybody else. 
We have less humans looking at dashboards and more agents monitoring systems still on top of Grafana, 
which is great. I was actually thinking what are some interesting stories recently where we've 
had some sort of Grafana-assisted could have been a bad situation and wasn't. And one of the 
more interesting ones that happened recently was some of our... So we run safety classifiers on 
all of the tokens that are flowing through Claude. And it's interesting because these are inherently 
non-deterministic systems. And we recently had one very specific classifier where we were seeing one 
out of every 100 requests that were coming through where Claude was kind of getting a low 
confidence answer on, "Is this safe or unsafe?" And it's one of those things that's anomaly 
detection is hard and these things can fly under the radar, but the team was alerted relatively 
quickly and we were able to go figure out what was going on. But I think just like probably every 
single one of you that has a story like that, there's an interesting shift that's happening 
where in the past, maybe sure we got an alert and a human got woken up and something 
happened. We're seeing more and more and more that sort of thing happens and an agent 
finds out first and is doing something about it, which is a crazy shift, but it's nice that 
the tools continue to plug in really nicely even throughout that shift towards agents.
You guys just rolled out a new OpenTelemetry product, right? And was it because there was 
an opportunity you saw or was it a failure that you wanted to prevent in the future? Why?
Well, we were actually pretty slow on that. We should have done it a long time 
ago. But yeah, so as of last week, we have OTel support in the Claude Platform, so 
our API suite. And this is generally just because people are building agents on top of our APIs. 
They need to be able to monitor those traces, see what's going on. When we were first starting 
to build more and more capabilities around agents, models can run for longer, people are trying to 
build cloud-based agents, here's infrastructure that helps you do it. We had built in some 
Observability tooling around these things, but the very first thing that everybody told us 
was like, "We don't care about your Observability tooling. We want to use the Observability 
tools that we already know and love." And so I think we were kind of slow with it, but we did 
it and we now have OTel support for our APIs and partnered with Grafana and now you can observe 
your agent traces to your heart's desire. I love this story as well because I can 
remember, I opened a PR against the Cassandra Project to add Prometheus instrumentation 
and it immediately got closed as, "No, we don't want to pick a particular vendor." 
They don't want to pick sides. I'm like, "Well, Prometheus is open source." But that's the whole 
point of OpenTelemetry. It is vendor-neutral. By Anthropic baking in OpenTelemetry support, 
they're not blessing any one vendor and it's for everyone's gain. And that's what we're about 
at Grafana Labs as well. Obviously it helps us because we're OpenTelemetry-native, 
but it helps the whole ecosystem. So Tom, you said in your keynote that AI was kind 
of a cheat code. I guess give me an example of something that you can do now or is being done 
throughout Grafana today that was difficult or impossible, let's say 18 months, two years ago.
So the cheat code, we actually changed that messaging at the very last minute. I think 
we now call it not-so-secret weapon. Not-so-secret weapon.
The cheat code stuff didn't translate to Japanese or something. The story 
there is how the open source community we have of users generates so much content on the 
Open Web about our products and, of course, most of our products and technology is open 
source. The Anthropic models just know how to use our software for whatever knows means nowadays, 
for whatever intelligence means nowadays, they just know how to use our software. So we did not, 
when we were building, when Matt and Cyril and co were building the first version of the Assistant, 
we were blown away at the emergent capabilities if you just gave a model some tools to interact 
with Grafana and data sources and Prometheus and so on. And that was the aha moment for us.
But even you saw the pages... Or you haven't seen the Pages demo. I've got to show it to you. The 
pages demo is the next generation of dashboards for us and how you build way more interactive and 
beautiful visualization systems. But honestly, so much of that is model capabilities. So much 
of that is the new generations of models for Anthropic just are so much more visually pleasing 
in the interfaces that they generate. So just all over the place is why we're such a fan.
So I don't have to be a system admin to understand the data?
Say again? I don't have to be a system 
administrator to understand the data? Yeah, not just that, but you don't 
have to be a system admin. You don't have to be a graphical artist to build a 
beautiful visualization either, right? Is there a place where, I guess a question for 
both of you is, what is the line that you would draw at AI to alter? I mean, would you let 
it go and change something in production? Is it a step before that? I mean, given 
the volume of changes that might be made, how do you strike that balance between when the 
human should intervene and when the software can do it by itself? Let me start with you.
I think a lot of this comes down to just how you think about guardrails and how you think about 
monitoring and how you think about just putting an agent in an environment where it can't do anything 
that's that catastrophically bad, or if it were going to, you'd know before something actually 
happens. But I think when it comes to our team and how we're actually building and maintaining 
our systems, all of our code is written by Claude, literally all of it. And I think then, when it 
comes to the automation that we're building around the edges, a really great example is we run an 
agent that's monitoring CI, and if CI goes red, then the agent does something about it. And 
right now, the thing that the agent will do with no humans in the loop is just fix a flaky test or 
fix a test. It'll touch the test if that's what's actually broken and causing a problem.
But then, now we're starting to get into, how do we get comfortable with no humans in 
the loop, that agent making a change to the actual services code base? And I think it's 
going to be really interesting where and how we experiment. I think it's the same thing with 
a page hitting an agent before it hits a human. We have some teams that are starting to experiment 
with Claude gets paged before humans do. Right now it's same time sort of thing. But we're just 
starting to see that half the time, by the time a computer wakes up and opens a computer, 
the agent has made a lot of progress. And so, did the human need to wake up? I don't know.
And so, I think these things will just kind of get better as model capabilities get better. 
But for us, we're just seeing the line. As engineering leaders, we're terrified and we're 
like, "Let's be really careful about this." But I think the line is starting to push. Had you 
said to me six months or a year ago that we'd be in a place where there's any type of change 
that zero human in the loop, nobody is touching it and we feel comfortable with it, I would've 
been like, "No, we need more time. We're not really getting there yet." But the models have 
gotten really good and we're getting there. We're super strict about this. I think we have 
to... Currently, at Grafana Labs, every change has to be human-reviewed. For our security and 
compliance footprint, this is really important to us. We definitely need to start thinking 
about what kind of changes we can allow to be automatically merged, but we're going to have to 
start really small with very specific... Like docs changes, maybe test changes. These kind of things 
maybe we can experiment with. One of the concrete example, we run 30 regions of Grafana Cloud 
around the world and all completely isolated from each other. And we have deterministic 
software checks in every change to make sure that changes only touch a single region.
And that's a great way to say, "Okay, that's giving us a lot more confidence if that 
check passes that at least the blast radius is smaller." Not going to be enough for us to 
automerge agent changes for sure. But maybe if we can determine that they're only rolling back 
a version or if they're only tweaking some white list set of flags within known boundary, we need 
to definitely experiment on this, but right now the status quo is like, "No, every change has 
to be human-reviewed." Doesn't mean we can't use agents to pre-review everything. It doesn't 
mean most teams in Grafana Labs have to get to a green agent review before they even ask a human 
to look at it. And then, because the agents have all had their go at it, the amount of attention 
I think the human needs to pay to each change can go down and the confidence can go up. It also 
means agents are driving huge amounts of increases in test coverage for us, which again, makes it 
much easier for us to, I'm not going to say wave through changes, but minimally review them.
So abstractly, if agents are checking the work of other agents checking the work of other 
agents, is it just turtles all the way down? How at that core first level, explain that 
to somebody maybe who's not in this world. I think the way that we think about it is our 
systems are designed by humans. At a high level... I was telling these guys this yesterday, we, as 
of a couple weeks ago, fully, fully rolled out our entire API in Rust. It used to be a Python 
monolith and we ported the entire thing to Rust because we needed to for scale and efficiency 
purposes primarily. But we didn't start with a single Rust developer on our team, but it was the 
right choice and Claude knows what it's doing. And I think what mattered the most was we designed 
the system. The team designed the system and knew, "Here's all the right components, here's 
how all these things need to fit together, here's all the properties we need to adhere 
to," all these sorts of things. But then when it comes to implementation, it's we don't need a 
human pressing keys in order to get the lines of code written. It's fine for Claude to do that.
But then I think what the humans did was not just design the system, but design the verification 
system that got us comfortable with doing that. Because the way that we rolled this out was we 
were like, "Okay, we're going to have Python running and Rust running and we don't look 
at prompts, we don't look at completions, we don't see any data, so how do we make sure 
it's working correctly?" We actually did it based on token counts. So if the same number 
of tokens was coming out of the Python system and the Rust system, then that was pretty good 
verification that it was going to work. But how could we think about that system and running all 
the shadow traffic through that second system to see if it was going to perform at high quality? 
That was all human thinking that went into all of that. But the grunt work of building the 
pieces and actually monitoring the pieces and actually making sure that we felt good 
about it, that was agents all the way down. Wow. I mean, as Tom said, that's not just changing 
an airplane engine, that's designing, building and changing an airplane engine while you're flying 
over the Pacific. That's really... So Tom, I guess now the way she's saying that, is the verification 
and Observability now part of just generally the safety conversation? I mean, it used to be 
something in a totally different category. Yeah, 100%. I mean, there's always been this 
argument that Observability is an extension of testing. And I kind of alluded to it this 
morning, the way we qualify software releases is by running them and checking all the alerts 
on firing and checking they're within SLO and within cost and so on. So there's definitely unit 
testing, but when we don't do a ton of automated integration testing, we rely on the integration 
environments, deploying to them and checking the properties are the same. There's definitely an 
extension of that in the agentic era. It's not just the very-easy-to-measure properties of 
latency and error rates and CPU consumption and so on. There's now the scores we get out of 
our evals, and so on, telling us if our agents are behaving in a similar way or getting better 
or getting worse. So 100% these two things have always been a spectrum, but even more so now.
I think a good example, we're thinking a lot about agent safety and security not just-
I wonder why. Not just because that's why we exist, but also 
I think everyone is a little... There's agents breaking out of sandboxes. How do we think about 
these problems? And the way that we break it down, we think a lot about, there's the safety in 
the sense of train the models to do good things and not bad things. And then there's the safety 
classifiers that we're running on the tokens that are being produced. But then there's this layer 
of the problem that's just agent infrastructure, the engineering of the thing. And one of 
the interesting things that we're starting to think about is monitoring and Observability 
around what an agent might be trying to do and how you think about getting alerted on that. And 
so, a really good example is, most of the time, an agent breaking out of a sandbox really just 
means you have network egress turned on in your sandboxes and the agent wrote some code that's 
executing the sandbox and then that code is doing something out over the internet. It's calling 
a tool, it's calling an API, whatever it is. And so, what we've started to do is say, 
"Okay, you can monitor certain shapes of tool calls are really just like network egress 
attempts." And even if maybe you have a domain allow list or something, you can only exit the 
sandbox to hit these specific domains, but if the agent is trying to go call some other tools 
or hit some other APIs, you can monitor and say, "Well, we saw three instances in this one session 
of the agent trying to go talk to some external tool that it wasn't meant to be talking to." Even 
though nothing bad happened, that tells you a lot about how you've prompted that agent or whatever 
it is about how that agent is set up. And so, there's a lot of really interesting monitoring 
problems I think that are coming into play when it comes to how do we just make sure that security 
is where it needs to be with agentic systems. I mean, this is the same signal we look at just 
for an overall quality perspective. The way we've made the Observability agents in Grafana 
Cloud fast and relatively cost-effective is by optimizing the tool calls so they don't fail 
three times with the wrong parameters. They just know the right thing to call first, mostly 
because we changed the parameter names to match what the model would've guessed.
So I mean, how good can you stay at that guessing game?
I mean, it's a constant battle. And I know Anthropic Strive to 
have compatibility across model versions, but as we're upgrading and using different models, 
we have to constantly tweak and tune this. So you both have visibility into different 
sectors, different industries. What kind of audit trails do these different companies, industries 
want just to get them comfortable with running different systems? I mean, I don't know if you've 
heard that in feedback with vendors are saying, "Oh, I would try this, but I am in a highly 
regulated industry and I need to have... If you're telling me this happens every three milliseconds, 
I don't even know where to store that and how to read that data. But if you're telling me like, 
'Okay, once a day I get an email that says something weird happened,' that's what's going to 
be used against me in a court of law in Australia or the United States." Right?
Yeah. Yeah. We have obviously tons of audit controls 
on Grafana Cloud. From the agentic perspective, a lot of our logs are used as an audit trail 
for what the agent has done. Literally a lot of the Observability of the agent conversations 
is the audit trail of what the agent has done. I don't think audit comes up a lot from a, "Oh, 
I'm in a heavily regulated industry." Often the thing we hear in the heavily regulated industry 
is like, "We just have to have it running inside our firewall. We have to have it under our 
control. We have to have it running in our data center or on our platform," or whatever. 
Especially the really risk-averse ones, we have a FedRAMP offering for Grafana Cloud. So it's 
a trimmed down version of the product for sure, but it's operated in the U.S. by U.S. personnel 
with all the right accreditations and everything. And that more tends to be about how it's deployed 
than getting the right level of audit control. It's actually been relatively straightforward.
But like NASA, while they're watching rockets go up into the sky?
I mean, we had in some of the videos with the different rocket companies that are using 
Grafana, but most of those, to be really clear, are using our open source technology and then 
they're running it inside their boundary and it's a nice, well-defined problem, right?
Yeah. So what is Anthropic here and how do you end up preemptively saying, "Okay, here 
are the safeguards that we've built in. This is why we know that you can deploy it well"?
Well, so it's interesting with our OTel launch, we did lean into the gen AI open standard on... 
We were like, "We could shape our traces however, but let's try to make this easier for people and 
go with something open and see if the industry converges around something like that." And 
so, really our thinking is just give people the data and then let them use tools like 
Grafana to go figure out how do they want to monitor those things or what might they want 
to do on top. And so that's, for the most part, I think how we're thinking about it for now. But 
otherwise, I just think, when it comes to some of our most regulated customers that we work with, 
in order for them to get comfortable with agents, obviously it's like all the stuff you're talking 
about, you need the compliance regimes in place and these sorts of things. Then they need 
to have all the data in a place where they can run whatever they want to run on it.
But the most interesting thing we see from people is, if they're in a regulated industry, 
here's a good example. We were working with a fintech customer that was doing something to do 
with underwriting and they're like, "Okay, we're going to get audited by these regulators on how we 
did our underwriting. And if we're going to have an agent underwriting people for a loan instead 
of a human, how do we get our auditors comfortable with this?" We actually worked with them on 
having a suite of evals that showed that their underwriting agents was performing at the quality 
that a human would perform underwriting at. And they have that eval data ready so that if they get 
spoken to by an auditor about, "You have agents running and doing this underwriting, how are 
you maintaining quality or whatever?" it's like, "Well, here's our continuously running evals."
Which is important for stuff like model upgrades and things so that they can make sure their agent 
continues to perform at high quality. But it's also like, "And we're going to keep this data 
right here so that if someone comes knocking, we're able to show we have really high confidence 
in this agent." And so, I think that's some of the stuff that we're starting to see more 
from people who have these regulated areas where they have to be really careful.
So Tom, how do the cloud economics change as people start to have more agents do more 
tasks? I mean, have you ever had a scenario where somebody rings up a sizable bill?
Oh, this is one that's fascinating. Yeah. The biggest thing is we see completely different query 
patterns from agents against the telemetry data. They just look nothing like human. And so, 
for us, for the longest time in Grafana Cloud, we basically just charged based on the 
amount of data we stored. And after adaptive, we take out the stuff you don't need and then 
we just charge you for the amount you need. And that worked really well. That got us to where we 
are today. But with the shift to agentic and that, let's face it, massive increase in query load, 
that is shifting the economics. Our approach here is to have a really, really generous included 
query allowance in every bit of data you read. But for a very small number of customers that are 
seeing there's just 1,000 times more reads than the average customer, there's going to be some 
increases in some query costs coming their way. This is a tricky one for us, and obviously we 
talk to the customer and help them optimize their workloads. There's a company or a name, but 
they started building an agent on top of Loki. And it just blew out the query cost. And we worked 
closely with them to shape that and some of the query optimizations that we announced today 
really helped them. But they just don't look like humans. The other thing, agent, if you 
go and ask an SRE to respond to an incident, that SRE is going to have some biases. Maybe 
they like a no metrics or they like a no logs and they'll use that predominantly more than the 
other signals. Agents don't have those biases. Maybe they have different biases for sure. But 
they tend to use all the sources they can get access to and they've got this nice property of 
they'll use anything they can get their hands on to figure out what happened. And so, that in the 
other hand has driven a lot of adoption of traces, of profiles, of other signals that were 
maybe not as preferred by humans. Okay. As we wrap up here, some rapid fire.
Oh wow. I was just getting into this. Exactly. What is something you believe today 
that you expect to change in six months and you wouldn't be surprised if you were like, 
"Well, obviously I got that wrong." I mean, I do think that we're going to see more 
and more just we're all going to change our line of where we feel comfortable letting agents do 
work and letting agents make decisions and make calls. And I think one of the really interesting 
things is, there's a bit of counterintuitive... There are situations where letting an agent 
have more agency is safer and more secure than not. A really good example is we really, 
really recommend both in Claude Code and in our managed agents architecture that for tool 
calling, you turn on auto mode, which is just let Claude ask another Claude, "Should I approve 
this tool call or not?" Every single test that we could possibly run shows us that you're 
getting better and more secure outcomes- Yes, [inaudible 00:25:41].
... if you let Claude decide rather than a human who is impatient and just 
smashing the button or running with dangerously skip permissions or whatever it is. Having 
Claude literally just go ask another Claude is one of the most secure things that you can do. 
And that's something that's counterintuitive for a lot of people. So I think, for me, my own line 
of where I feel good about my team saying, "Okay, great. No human actually looked at this thing that 
happened, but it's okay," I think it's probably going to shift and it'll probably shift further 
and faster than I am expecting it to today. Tom?
I'm going to step outside of the whole Observability 
stuff for a minute and just talk about... My other passion is home automation. And so, 
I do a lot of work with Home Assistant. I forgot the name of the system, but when 
the first autonomous home agents came out, I had it start managing my hot water. I 
live in the U.K. and we don't have- Managed what?
My hot water. I live in the U.K. and we don't have always-on hot water that has to go on for an hour 
so that you can have a shower. And I wanted- Here we call it the geezer. You have 
to press the button on and then... And this might sound weird, but I sometimes have 
to get up at 3:00 AM to catch a flight. And so that was the problem I gave the agent and it 
figured it out. It did a really good job. It turned the hot water on nice and early so I could 
have a shower at 3:00 AM before I go and catch my flight. It also figured out I wasn't in the house 
after that and so it turned the hot water off for the week. My wife got really upset about that. So 
I mean this was a year ago and that got turned off pretty quickly. But now I'm using Claude Code with 
my Home Assistant and I'm developing deterministic automations, and the level and quality of my 
home automation is through the roof and to the point where I have this thing called WAF, 
wife acceptance factor. If my wife likes- She's an eval.
Yeah, exactly. She's an eval.
Yeah. I'm not going to... I'm not going to say that out loud again.
Exactly. And even my wife has commented that how good the home automation is getting. So I 
think, I guess the prediction I'll make is we're talking about agentic right now as it's the new 
shiny thing and we notice when it's clever. This is going to blend into the everyday. Even in six 
months' time, the rate of change is so quick... Now, I had a holiday, I mean, I had to work for 
most of the holiday, but I took a holiday and I planned it with Claude. I didn't let Claude book 
the hotels. I did that manually, but honestly the next holiday, Claude is just going to be booking 
everything for me. It's just going to blend into the everyday. And you're not even going to 
think about the fact that this is an agent doing it for me. This is just going to be expected.
Okay. We'll have you back in six months to check on these predictions. Thank you all.
See if my hot water is working. Exactly. Tom, Katelyn, thank you all.
Thank you.

