# Grafana Agent Observability for Coding Agents

Published on 2026-09-21T12:00:39Z

## Description

In this video, Alexander shows how to monitor your organizational use of Coding Agents. Claude Code, Cursor, Codex - they all ...

URL: https://www.youtube.com/watch?v=fwfRVp-CxJY

## Summary

In the video titled "Grafana Agent Observability for Coding Agents," published on September 21, 2026, Alexander from Grafana Labs discusses how to monitor the usage of coding agents like Claude Code, Cursor, and Codex using Grafana's agent observability features. He explains that this tool allows users to track usage metrics such as requests, error rates, latency, and estimated costs without compromising data privacy, as it captures only metadata by default. Key takeaways include the ability to analyze usage across different agents and Git branches, providing insights into costs associated with specific features and team contributions. 

Topics: Grafana Agent, agent observability, coding agents, usage metrics, cost analysis.

## Chapters

00:00:00 Introduction to agent observability for coding agents
00:01:31 Grafana Cloud observability for coding agents
00:02:17 Coding agents observability

[music] [music] 

Hi, I'm Alexander. I work on agent observability at Grafana Labs. Today, I will show you how to monitor your organization's use of coding agents. Claude Code, Cursor, Codex - they all report usage of their own tools. But agent observability allows you to see all that in the same place. 

Let me show you how it works. I start my coding agents through agent observability, and it wraps the tools I already use, so nothing about the way I work changes. It's local by default, so nothing leaves the computer. But for our demo, let's select Grafana Cloud. 

During the manual login, I need to enter a token, but it can be automated. Two settings matter here for a team: 

- **Content capture** is metadata only by default. No prompts, no responses, no tool input or output. Conversations stay on the machine. 
- What leaves is the model, the token counts, tool names, timings, and automated tags. They add tags for the user, repository, and branch, so you can see the cost per branch. 

Let's ask the agent to do something. Now, token usage information of this session is sent to your Grafana. 

Let's open observability agent analytics. Here's what usage for a team looks like after a day: requests, error rate, latency, estimated cost across every provider and every agent. You can break down the charts by agent, model, and provider. You can see agents sorted by highest requests, and you can see estimated cost and token usage, also breaking down by Git branch. 

So that's how we can answer how much one feature costs across every provider and every person who worked on it. And that's coding agents observability. 

Thanks for watching.

## Raw YouTube Transcript

[music] [music] >> Hi, I'm Alexander. I work on agent observability at Grafana Labs. Today I will show you how to monitor your organization's use of coding agents. Code code, cursor, codex, they all report usage of their own tool. But the agent observability allows you to see all that in the same place. Let me show you how it works. I start my coding agents through agent observability and it wraps the tools I already use, so nothing about the way I work changes. It's local by default, so nothing leaves the computer. But for our demo, let's select Grafana Cloud. During the manual login, I need to enter a token, but it can be automated. Two settings matter here for a team. Content capture is metadata only by default. No prompts, no responses, no tool input or output. Conversations stay on the machine. What leaves is the model, the token counts, tool names, and timings. And automated tags. They add tag for the user, repository, and branch. So you can see cost per branch. Let's ask the agent to do something. Now, token usage information of this session is sent to your Grafana. Let's open observability agent analytics. And here's what usage for a team looks like after a day. Requests, error rate, latency, estimated cost across every provider and every agent. You can break down the charts by agent, model, provider. You can see agents sorted by highest requests. And you can see estimated cost and token usage. And also breaking down by Git branch. So that's how we can answer how much one feature cost across every provider and every person who worked on it. And that's coding agents observability. Thanks for watching.

