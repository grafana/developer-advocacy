# How to Investigate a Production Issue Using Claude, Cursor, gcx, Grafana Cloud MCP, or Slack

Published on 2026-11-03T19:03:39Z

## Description

Investigate a production issue with the agent of your choice, from Claude on your phone to Cursor in your IDE to a self-hosted ...

URL: https://www.youtube.com/watch?v=u4yIIwEIPfI

## Summary

The community call titled "How to Investigate a Production Issue Using Claude, Cursor, gcx, Grafana Cloud MCP, or Slack" was held on November 3, 2026, featuring Cedric, a product manager, and Gianni, a product designer at Grafana Labs. They discussed the integration of various agents like Claude, Cursor, and Hermes with Grafana Cloud, showcasing how these tools can streamline the investigation of production issues in real-time. Key features highlighted included the Grafana Cloud MCP server, which allows agents to access interactive visualizations and telemetry data, and the gcx command line interface that enables deeper investigations. The session emphasized the flexibility of using different agents and the importance of seamless workflows in observability.

Topics: Grafana Cloud, Claude, Cursor, Hermes Agent, gcx, observability, production issue investigation.

## Chapters

00:00:00 Investigating production issues with Grafana Cloud and agents
00:04:06 Investigating production issues with Grafana Cloud MCP
00:08:48 Using Hermes agent for production issue investigation

Hey everyone. My name is Cedric. I'm a product manager at Grafana Labs, and this is Gianni, a product designer at Grafana Labs. Today, we'll show you how you can use your own agent wherever you work and how Grafana Cloud is the open agentic observability platform that supports you and your agents. If you find us on the floor, ask us about boats. Although I have to admit that Gianni has much nicer weather in Italy and definitely a much more fun boat.

Oh, that's rude, man. That's a fact.

All right. Agents are already part of our everyday work. We use them to write code, open PRs, review these PRs, deploy changes, and investigate what's happening in our systems. But there are still gaps. Getting the right context into an agent or moving between tools can interrupt that flow. Today, we'll look at a few of these gaps and show how Grafana Cloud helps bring these pieces together.

Yes, because with Grafana Cloud, you can use any agent. Of course, you can use Grafana Assistant, which is built into Grafana Cloud, but you can also connect your ChatGPT, Claude, Codex, Py, or literally any other agent through either the Grafana Cloud MCP server, or you can just use gcx with your coding agent so that it gets insights from the telemetry that you have in your Grafana Cloud environment.

To show you what that looks like, let's look at a real-life scenario. Imagine I'm working from a coffee shop. It's late morning, and I haven't had my first coffee of the day yet. I'm third in line in the coffee queue when I receive a message on Slack. It's Besart, our director of engineering. He says that fewer customers are completing money transfers and asks me to take a look. Now, I don't want to leave the coffee queue; it's almost my turn, but I want to start doing something from the coffee queue. My laptop is still in my bag, right? So I wonder if there's something I can start using from my phone.

All right. I'll open Claude, start a new chat, and I'm just going to ask, "What's up with my transfer service?" Now, Claude is connected to Grafana Cloud through MCP. This gives it the possibility to check things in Grafana Cloud for me. Of course, we need to give it permissions, and I can see that I get interactive Grafana visualizations inside the conversation I'm having with my agent. I can check the service health, the transfer service health, and here I get the KPIs for my backend service. I can see that orders are pretty low, latency is okay; there's nothing really that stands out here, but I'm starting to rule out some hypotheses. So my backend service is okay. I wonder if maybe the problem is on my front end. 

Let me ask, "Is the front end okay?" Once again, Claude, through MCP, will connect to Grafana Cloud and pull up an interactive visualization for me. Here I can check the web vitals and see what is happening on my front end. In this case, I see no errors. Nothing really stands out, but very importantly, I'm starting to rule out some hypotheses.

So back to the slides. What are these views, these interactive views that we saw on my mobile? They are MCP apps. The Grafana Cloud MCP server brings them into the conversation. It gives us an interactive way to interact with Grafana along with the agent response. Now you can check things like service health, as we just did, right in the conversation, right where you're working. 

We are announcing them today as an experimental feature, and we are planning to add more of these views. If there's one you find useful, we would love for you to come and talk to us. 

Now back to Besart's message. I got my coffee. I'm not in the coffee queue anymore. I can sit at the table, pull up my laptop, and have a closer look at what is happening in Grafana. That's right. Because I've been using Claude on my phone, I can easily go back to Claude on my desktop. Because of the continuity, I can pull up the same conversation here and get the same insight as before. We see the MCP apps rendered here in the desktop app. It's a seamless experience because of the MCP app standard. 

But as Gianni pointed out, there's really nothing that stands out here in the apps. So what I can do is click the button here to go to Grafana Cloud to inspect what's going wrong. This is front end observability. We are observing real users with Grafana Cloud, and it has this really useful feature called user actions. User actions is basically a concept for you to throw an event whenever a user performs a key action so that you can record key steps in your user journeys. 

What stands out to me here is the submit transfer action. It is red and has an elevated error rate. I could dig into the issue in Grafana Cloud, of course, but what I want to show you is the Sparkle icon here because everything has Sparkle buttons now. It brings up this model and can send the context from the panel to a bunch of agents. I could send it to Grafana Assistant or Claude, but we already used Claude, so let's try Cursor. 

I select Cursor and click "Send to Agent." What it does is send the context of the panel directly into Cursor, and I can ask the agent, "Can you inspect the transfers and what's wrong with them?" Of course, my text-to-speech app died. Can you check the transfer actions and what's wrong? 

All right, so Cursor has my code. That is my development environment, and Cursor is also connected to Grafana Cloud via gcx. That means it can execute gcx locally. gcx ships a bunch of skills, giving the agent the information on how to investigate the issue with Grafana Cloud. We should see a bunch of gcx commands being fired here. It would check the context to understand which Grafana Cloud environment it is connected to. It uses the front end subcommand to understand which front end apps are available in this environment. 

It can now query logs, query the user actions, and since it had access to my code, it should be able to help me. So we're not going to look at the generation here further. 

Back to the slides. So Gianni, how does Cursor do this? How does Cursor investigate with Grafana Cloud? It uses Grafana gcx, our command line interface. gcx comes with a set of curated agent skills that guide common investigations, but the agent can also discover all the available commands and use them to query data, inspect services, or look at front end sessions as we did. We are giving Cursor the context from Grafana. gcx gives it a way to follow up, gather more evidence, and work out what to check next.

Yeah. So let's put it all together. We checked Grafana from Claude on the phone, then we sent it to the Claude desktop app. From there, we went to Grafana, and from there, we went to Cursor. But what if I want to work differently? 

There's this very useful open-source project called Hermes Agent. It's literally an agent that you can host on your hardware, and it's very flexible. It actually learns from its interactions, and you can give it all sorts of tools. So what I did in preparation for this demo was connect Hermes Agent to Slack, give it the Grafana Cloud MCP server, and also gcx, locking it into Grafana Cloud. 

So let's see what we can do. This is my Slack. You can see I'm in the war room channel, and I can now directly interact with Hermes. I can tag Hermes here and ask, "Hey, something is wrong with my transfer service. Can you check why transfers are slow?" Hermes starts working. It's very interactive. It lives in Slack like all the other agents that we can connect there. 

We should briefly see that it has understood my intent and it says, "Hey, sure. I'm going to dig into this for you." Then it starts checking the firing alerts, the services, recent latency...

Error rates, et cetera. And it's investigating in the background. It's actually using gcx to drill deeper and deeper until it has an answer. 

To show you what an example looks like, I have set up a bunch of scheduled checks. It basically watches the telemetry in the connected Grafana Cloud environment. Let's look at this one here. I interacted with Hermes before. I told you that it's an agent that can learn from you and how you want to do things. I teach it how I want my root cause analysis to be done. First, it should investigate, of course, but then it should give me a report on what happened, and it did so. 

It said, "Hey, the Watchdog rate was 7% something, something," and it pulled up the evidence. Where useful, it also linked back to Grafana Cloud so that I can validate because still agents and LLMs, we want to go check on things. I can also see impact versus my baseline. What I really find helpful is that I can also check what's next, so suggested follow-ups that Hermes tells me I should do. I really like this feature of Hermes. 

Let's see what our agent came up with here. It actually dug up quite a bit, but it talks about perceived user performance. It understood what the telemetry means. By the way, this is connected to an open model via an open provider, so it's GLM under the hood. This also means that with your agent, you're going to choose the model, but Grafana Cloud will still be there, and you can connect any agent to Grafana Cloud. 

Back to the slides, Gianni. All right. So we started with a message in the Configure, right? Sorry. Then we checked Grafana Cloud using Claude on my phone. After that, we moved to Cursor with the context from Grafana Cloud, and we brought the investigation into Slack with Hermes. That's what we mean by bringing Grafana into your workflow. You choose the agent, the model, the provider, and where you work. Grafana Cloud gives your agent access to the context and tools it needs to help. That's Grafana's big tent for agents. Thank you.

## Raw YouTube Transcript

Hey everyone. My name is Cedric. I'm 
a product manager at Grafana Labs, and this is Gianni, a product 
designer at Grafana Labs. Today, we'll show you how you can use your own agent 
wherever you work and how Grafana Cloud is the open agentic observability platform that supports 
you and your agents. If you find us on the floor, ask us about boats. Although I have to admit 
that Gianni has much nicer weather in Italy. And definitely a much more fun boat.
Oh, that's rude, man. That's a fact. All right. Agents are 
already part of our everyday work. We use them to write code. We use them to 
open PRs, review these PRs, deploy changes, and we use them to investigate what's happening 
in our systems. But there are still gaps. Getting the right context into an agent or moving between 
tools can interrupt that flow. Today, we'll look at a few of these gaps and show how Grafana 
Cloud helps bring these pieces together. Yes, because with Grafana Cloud, you can use any 
agent. Of course, you can use Grafana Assistant, which is built into Grafana Cloud, but you can 
also connect your ChatGPT, your Claude, Codex, Py or literally any other agent through 
either the Grafana Cloud MCP server, or you just use gcx with your coding agent so that 
it get insights from the telemetry that you have in your Grafana Cloud environment.
To show you what that looks like, let's look at the real life scenario.
Imagine I'm working from a coffee shop. It's late morning and I haven't had my first 
coffee of the day yet. I'm third in line in the coffee queue when I receive a message on 
Slack. It's Besart, our director of engineering. He says that fewer customers are completing 
money transfers and asked me to take a look. Now, I don't want to leave the coffee queue. It's 
almost my turn, but I want... And my laptop is still in my bag, right? I'm in the queue. So I 
wonder if there's something I can start using, start doing from the coffee queue. 
So maybe I can start with my phone. All right. I'll open Claude. I'll start 
a new chat and I'm just going to ask, "What's up with my transfer service?" now, 
Claude is connected to Grafana Cloud through MCP. This gives it the possibility to 
check things in Grafana Cloud for me. Now, I can see, of course we need to give 
it permissions and I can see that I get this interactive Grafana visualizations inside the 
conversation I'm having with my agent. I can check the service health, the transfer service health, 
and here I get the KPIs for my backend service. I can see that orders are pretty low, latency is 
okay. There's nothing really that stands out here, but I'm starting to rule out some hypothesis.
So my backend service is okay. I wonder if maybe the problem is on my front end. So let me ask, 
is the front end okay? And once again, Claude, through MCP, will connect to Grafana Cloud and 
pull up an interactive visualization for me. Here I can check the web vitals. I can check 
what is happening on my front end. And also, in this case, I see no errors. Nothing 
really stands out, but very importantly, I'm starting to rule out some hypothesis.
So back to the slides. So what are these views, these interactive views that we saw on my 
mobile? They are MCP apps. The Grafana Cloud MCP server brings them into the conversation. 
It gives us an interactive way to interact with Grafana along with the agent response.
Now you can check things like service health, as we just did, right in the conversation right 
where you're working. Now we are announcing them today as an experimental feature and we 
are planning to add more of these views. So if there's one you will find useful, we 
will love for you to come and talk to us. Now back to Besart's message. I got my coffee. 
I'm not in the coffee queue anymore. I can sit at the table, pull up my laptop and have a 
closer look at what is happening in Grafana. That's right. All right. Because I've been using 
Claude on my phone, I can easily go back to Claude on my desktop. And because of the continuity, I 
can pull up the same conversation here and I get the same insight as before. We see the MCP apps 
rendered here in the desktop app. It's a seamless experience because of the MCP app standard. But 
as Gianni pointed out, there's not really nothing that stands out here in the apps. So what I can 
do, I can just click the button here. I can go to Grafana Cloud to inspect what's going wrong.
This is front end observability. So we are observing real users with Grafana Cloud 
and it has this really useful feature that is called user actions. User actions is 
basically a concept for you to throw an event whenever a user performs a key action so that 
you can record key steps in your user journeys. And what stands out to me here is this one, the 
submit transfer action. It is red and it has an elevated error rate. I could not dig into the 
issue in Grafana Cloud of course, but what I want to show you is the Sparkle icon here because 
everything has Sparkle buttons now and it brings up this model and it can send the context from 
the panel to a bunch of agents. I could send it to a Grafana Assistant. I could send it to Claude, 
but we already used Claude. So let's try Cursor. I select Cursor and I click Send to Agent and 
what it does, it sends the context of the panel directly into Cursor and I can ask the agent, "Can 
you inspect the transfers and what's wrong with them?" Of course, my text to speech app died.
Can you check the transfer actions and what's wrong? All right, so Cursor has my code. That 
is my development environment and Cursor is also connected to Grafana Cloud via gcx. And that means 
it can execute gcx locally. gcx ships a bunch of skills and that gives the agent the information on 
how to investigate the issue with Grafana Cloud. We should see a bunch of gcx commands being 
fired here. It would check the context to understand which Grafana Cloud environment it is 
connected to. It uses the front end sub command to understand which front end apps are available in 
this environment. And then it goes on and on and on and on. It can now query logs. It can query the 
user actions. And since it had access to my code, it should be able to help me. So we're not 
going to look at the generation here further. Back to the slides. So Gianni, 
how does Cursor do this? How does Cursor do this? How does Cursor 
investigate with Grafana Cloud? It uses Grafana gcx, our common line interface. gcx 
comes with a set of curated agent skills that guide common investigations, but the agent can 
also discover all the available commands and use them to query data, inspect services 
or look at front end sessions as we did. We are giving Cursor the context from Grafana. 
gcx gives it a way to follow up, gather more evidence and work out what to check next.
Yeah. So let's put it all together. We checked Grafana from Claude on the phone, then we sent it 
to the Claude desktop app. From there we went to Grafana and from there we went to Cursor. 
But what if I want to work differently? There's this very useful open source project. It's 
called Hermes Agent and it's literally an agent that you can host on your hardware and it's very 
flexible. It actually learns from its interactions and you can give it all sorts of tools.
So what I did in preparation of this demo, I connected Hermes agent to Slack and I gave 
Hermes agent the Grafana Cloud MCP server and I gave Hermes agent also gcx and locked it into 
Grafana Cloud. So let's see what we can do. This is my Slack. You can see I'm in the war 
room channel and I can now directly interact with Hermes. I can tag Hermes here and I can ask, 
"Hey, something is wrong with my transfer service. Can you check why transfers are slow?" And Hermes 
starts working. It's very interactive. It lives in Slack like all the other agents that we can 
connect there. And we should briefly see that it has understood my intent and it says, "Hey, sure. 
I'm going to dig into this for you." And then it starts checking the firing alerts, the services, 
recent latency, error rates, et cetera. And it's investigating in the background. It's 
actually using gcx to drill deeper and deeper and deeper until it has an answer.
To show you what an example looks like, I have set up a bunch of scheduled checks. 
So it basically watches the telemetry in the connected Grafana Cloud environment. 
And let's look at this one here. I interacted with Hermes before. I told you that 
it's an agent that can learn from you and how you do want to do things. And I teach it how I want 
my root cause analysis to be done. First, it should investigate, of course, but then it should 
give me a report on what happened and it did so. It said, "Hey, the Watchdog rate was 7% something, 
something," and it pulled up the evidence. Where useful, it also linked back to Grafana Cloud 
so that I can validate because still agents, LLMs, we want to go check on things.
I can also see impact versus my baseline. And what I really find helpful is that I 
can also check what's next. So suggested follow-ups that Hermes tells me that I should 
do. And I really like this feature of Hermes. Let's see what our agent came up with here.
It actually digged up quite a bit, but it talks about perceived user performance. It understood 
what the telemetry means. And by the way, this is connected to an open model via an open provider. 
So it's GLM under the hood. So that also means with your agent, you're going to choose the model, 
but Grafana Cloud will still be there and you can connect any agent to Grafana Cloud.
Back to the slides, Gianni. All right. So we started with a message in the 
Configure, right? Sorry. And then we checked Grafana Cloud using Claude on my phone. Then we 
moved to Cursor with the context from Grafana Cloud and we brought the investigation 
into Slack with Hermes. That's what we mean by bringing Grafana into your workflow.
You choose the agent, the model, the provider, you choose where you work. Grafana 
Cloud gives your agent access to the context and tools he needs to help. That's 
Grafana's big tent for agents. Thank you.

