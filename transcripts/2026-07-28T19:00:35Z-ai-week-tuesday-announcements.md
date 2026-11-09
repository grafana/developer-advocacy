# AI Week: Tuesday announcements

Published on 2026-07-28T19:00:35Z

## Description

Tuesday is about Building and implementation. Here's what we're announcing today! Check out grafana.ai for more details on ...

URL: https://www.youtube.com/watch?v=Y3QtH94f77U

## Summary

In the community call titled "AI Week: Tuesday announcements," held on July 28, 2026, the speakers discussed two major announcements: the general availability of GCX (Grafana CLI) and the Grafana MCP server. These tools are designed to enhance the integration of coding agents with Grafana telemetry, facilitating tasks such as dashboard management and metrics querying. The MCP server offers ready-made tools for common use cases, while GCX provides a more flexible approach, allowing agents to create custom workflows with built-in safety features. The key takeaway emphasizes the importance of telemetry-driven development, ensuring that agents can effectively interact with Grafana without guesswork. 

Topics: AI tools, Grafana MCP server, GCX, telemetry-driven development, coding agents

## Chapters

00:00:00 Announcing GCX and Grafana MCP server
00:00:46 Introduction to Grafana Cloud stack and GCX
00:01:31 Telemetry-driven development in Grafana

[music] 

It's day two of AI Week here at Grafana Labs, and Tuesday is all about building AI tools that help you build software with confidence. Today, we have two big announcements: GCX and the Grafana MCP server are now both generally available.

Both of these connect your coding agents, think Cloud Code or Cursor, to your Grafana telemetry. So, what's the difference? 

Well, the Grafana MCP server gives your agent opinionated, ready-made tools to handle the most common use cases. This includes tasks like reading and updating your dashboards or querying your metrics and logs. You can run it yourself, or you can use the hosted MCP version with your Grafana Cloud stack. It's now working for both OSS and Grafana Cloud.

On the other hand, GCX is the Grafana CLI, and you can think of it as the less opinionated but more flexible option. Agents can explore it and build their own workflows. GCX was actually built with agents in mind from the ground up, featuring read-only guardrails so that your agent can't touch anything that you don't explicitly approve. GCX is also available for both Grafana Cloud and self-managed instances, and it even ships with a bundle of agent skills.

So, why does this all matter? When an agent is writing your code, it really shouldn't be guessing. It should learn to speak Grafana fluently and look at actual telemetry in production. You can think of it as telemetry-driven development.

Head over to grafana.ai to see all of the things that we're announcing this week, and I'll see you tomorrow for day three.

## Raw YouTube Transcript

[music] >> It's day two of AI Week here at Grafana Labs, and Tuesday is all about building AI tools that help you build software with confidence. Today, we have two big announcements. GCX and the Grafana MCP server are now both generally available. Now, both of those connect your coding agents, think Cloud Code or Cursor, to your Grafana telemetry. So, what's the difference? Well, the Grafana MCP server gives your agent opinionated, ready-made tools to do the most common use cases. So, things like, you know, reading and updating your dashboards or querying your metrics and logs, that kind of thing. You can run it yourself or you can use the hosted MCP version with your Grafana Cloud stack. So, yeah, it's now working for both OSS and Grafana Cloud. Now, GCX is the Grafana CLI, and you can think of it as the less opinionated but more flexible option. Agents can explore it and build their own workflows, and GCX was actually built with agents in mind from the ground up. So, it has things like read-only guardrails so that your agent can't actually touch anything that you don't explicitly approve. GCX is also available for both Grafana Cloud and self-managed instances, and it even ships with a bundle of agent skills. So, why does this all matter? Well, because when an agent is writing your code, it really shouldn't be guessing. It should learn to speak Grafana fluently. It should be looking at actual telemetry in production. You can think of it as telemetry-driven development. Head over to grafana.ai to see all of the things that we're announcing this week, and I'll see you tomorrow for day three.

