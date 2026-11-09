# Grafana MCP OpenSource + Cloud

Published on 2026-09-24T12:00:00Z

## Description

The open source server connects any AI assistant to everything in your Grafana - dashboards, metrics, logs, alerts, on-call, ...

URL: https://www.youtube.com/watch?v=JHCa6RRIesQ

## Summary

The show is titled "Grafana MCP OpenSource + Cloud," published on September 24, 2026. Yana Amurti, a software engineer at Grafana Labs, discusses the Grafana MCB server, highlighting both the open source and hosted versions available in Grafana Cloud. Key features include the ability to connect AI assistants to Grafana dashboards, metrics, logs, alerts, and on-call incidents, with a focus on ease of setup and integration. The presentation demonstrates how to investigate and resolve issues using Grafana tools, emphasizing the seamless interaction between the open source server and Grafana Cloud MCB. 

Topics: Grafana MCB server, open source, Grafana Cloud, AI integration, incident management.

## Chapters

00:00:00 Introduction to Grafana MCB server
00:01:30 Investigating elevated error rates in Grafana
00:02:17 Closing the gap in alerting with Grafana MCP

[music] 

Hello. My name is Yana Amurti. I'm a software engineer at Grafana Labs, and today I'll walk you through the Grafana MCB server, both the open source version and the new hosted one in Grafana Cloud. 

Let's start with the open source server. MCB Grafana has been around since early 2025 and is widely used. It connects any AI assistant, whether it's short cloud or whatever you're using, to your Grafana dashboards, your metrics, your logs, your alerts, and on-call incidents. It doesn't just read; it can make changes for you too. Setup is a few lines of JSON, and you choose exactly which tools are exposed. 

Now, there's a hosted version: Grafana Cloud MCB. It has the same tools plus a few extras that light up with Grafana Assistant. The difference is that there's nothing to install, nothing to maintain, and no service account tokens. The documentation compares both, and for Keshur, setup is literally one click. For Cloud Code, it's one command. 

I'll click install in Keshur. Keshur opens with everything pre-filled. I just hit install. Authentication is all set; I signed in with my own Grafana account, and the agent gets exactly my permissions—nothing more. And we're connected. 96 tools are ready. 

Now, let's put it to work. I'm getting paged about an elevated error rate on our checkout pipeline. So, I run the full investigation from Keshur. This calls describe infrastructure, a cloud-only tool built on infrastructure memory, and it maps our actual stack: checkout call fame. 

Now, what's actually failing? This one is querying Prometheus from the open source server, and there it is: roughly one in three orders isn't completing, and "out of stock" is by far our biggest failure mode. That's interesting, right? Are we even watching for this error? 

I'll hand this to the Grafana system with Ask Assistant, which is another cloud tool. It queries all the context it has in your Grafana stack. So, in one pass, it surfaces everything around checkout: infrastructure, dashboards, alerts, and related incidents. That's how it catches the gap as well. Our biggest failure mode has no alert and isn't on any dashboard. 

So, let's close this gap with the right tool from the open source server again. One prompt, and the alert rule is created: "Out of stock above 5% for 5 minutes." Here it is in your fun. The query, the threshold—it's already evaluating. It's real. 

And one more thing. The metric told us that orders fail, but not with high confidence that they're out of stock. So, I asked the agent to fix the service itself. It labeled the metric per item right in the editor—nothing for me to do. I review the diff and accept. That's the fun loop: detect, investigate, alert, and eventually fix the code. 

So, the open source server runs anywhere with any Grafana. The cloud server is hosted, it's all secured, and uses code with nothing to run locally. Grafana Cloud MCP is now GA. Give it a try. Your agent already knows what to do. Thank you. 

[music]

## Raw YouTube Transcript

[music] [music] >> Hello. My name is Yana Amurti. I'm a software engineer at Grafana Labs and today I'll walk you through the Grafana MCB server, both the open source version and the new hosted one in Grafana Cloud. Let's start with the open source server. MCB Grafana has been around since early 2025 and is widely used. It connects any AI assistant, their short cloud, whatever you're using to your Grafana dashboards, your metrics, your logs, your alerts, on-call incidents and it doesn't just read, it can make changes for you too. Setup is a few lines of JSON and you choose exactly which tools are exposed. And now there's a hosted version, Grafana Cloud MCB. Same tools plus a few extras that light up with Grafana Assistant. The difference is nothing to install, nothing to maintain, no service account tokens. The docs compare both and for Keshur, setup is literally one click. For Cloud Code, it's one command. I'll click install in Keshur. Keshur opens with everything pre-filled. I just hit install. Authentication is all. I signed with my own Grafana account and the agent gets exactly my permissions. Nothing more. And we're connected. 96 tools ready. So now, let's put it to work. I'm getting paged about elevated error rate on our checkout [music] pipeline. So, I run the full investigation from Keshur. This calls describe infrastructure, a cloud only tool built on infrastructure memory and it maps our actual stack, checkout call fame. Now, what's actually failing? This one is query Prometheus from the open source server and there it is, roughly one in three orders isn't completing and out of stock is by far our biggest failure mode. That's interesting, right? Are we even watching for this error? I'll hand this to the the Grafana system with Ask Assistant, which is another cloud tool. It queries all the context it has in your Grafana stack. So, in one pass, it surfaces everything around checkout. >> [music] >> Infrastructure, dashboards, alerts, related incidents. That's how it catches the gap, as well. Our biggest failure mode has no alert and isn't on any dashboard. So, let's close this gap with the right tool from the open source server again. One prompt and the alerts rule is created. Out of stock above 5% for 5 minutes. Here it is in your fun. The query, the threshold, already evaluating. It's real. And one more thing. [music] The metric told us that orders fail, but not with high confidence they're out of stock. So, I asked the agent to fix the service itself. It labeled the metric per item, right in the editor, nothing for me to do. I review the diff and accept. That's the fun loop. Detect, investigate, alert, and eventually fix the code. So, the open source server runs anywhere with any Grafana. The cloud server is hosted, it's all secured, and uses code with nothing to run locally. Grafana Cloud MCP is now GA. Give it a try. Your agent already knows what to do. Thank you. >> [music]

