# Getting Started with gcx: A CLI for AI Agents and Grafana Telemetry | Demo

Published on 2026-05-26T21:16:32Z

## Description

AI agents are only as useful as the context they can access. With gcx, your coding agents can connect to Grafana and query ...

URL: https://www.youtube.com/watch?v=rMnXFsVl194

## Summary

In this video, the speaker introduces GCX, a new command-line interface (CLI) designed to enhance AI agents' ability to analyze real-time production telemetry within Grafana Cloud environments without overwhelming context windows. The speaker contrasts GCX with the previously used MCP, highlighting that GCX efficiently manages context by only utilizing resources when needed. The demonstration includes installation steps for various operating systems and showcases how to authenticate and execute commands using GCX. Additionally, the speaker illustrates how they set up skills to interpret production Kubernetes environments and how Claude Code can analyze queries based on the data fetched. Overall, the video explores the practical applications of GCX in streamlining data analysis for AI agents.

## Chapters

00:00:00 Introductions to the new AI capabilities  
00:01:15 Explanation of GCX CLI and its advantages  
00:02:30 Comparison of GCX CLI with MCP and context window issues  
00:03:45 Installation steps for GCX on different operating systems  
00:04:15 Demonstration of the GCX terminal commands  
00:05:00 Authentication process for GCX  
00:06:00 Prompting the assistant with GCX commands  
00:07:00 Overview of skills set up using GCX  
00:08:00 Using GCX to analyze Kubernetes telemetry  
00:09:30 Benefits of using Claude Code for production queries and analysis  

Did you know your AI agent can now analyze real-time production telemetry without blowing up your context window? Let me explain.

A few weeks ago, we released **GCX**, a CLI that provides your coding agents, like Codex, Claude Code, and Gemini, with context into your Grafana Cloud Enterprise or OSS environments. 

### Why Use GCX CLI Instead of MCP?

While MCP is another alternative, it can lead to context window bloating due to all the tools it loads upfront before you even send a prompt. The CLI approach sidesteps this entirely, offering **zero token cost** upfront until you actually need to use the queries.

### Getting Started with GCX

Getting started with GCX is super simple. You can follow the install steps for macOS, Linux, or Windows. Options include using `curl`, Homebrew, or directly grabbing the binary from the releases page.

I have already set up GCX, so let’s dive into the terminal and start interacting with it. By typing `GCX`, you’ll see all the available commands you can run against your Grafana instance. 

To authenticate yourself, just use the command `GCX off login`. This will open a Chrome window for you to authenticate against your stack. From there, you can run any command with GCX. For example, to prompt the assistant, you can simply type:

```
GCX GCX assistant prompt <your query here>
```

### Example Skills Using GCX

I have set up some skills with GCX. For instance, if we open **Cursor**, you’ll see a file named `K8s telemetry.md`. This file represents a skill on how to interpret my production Kubernetes environment. 

I had the assistant through GCX fetch all the data related to my Kubernetes environment in Grafana Cloud. It returned a comprehensive list, and now I have a skill based on that data.

Additionally, I have a GCX skill directly linked, which was created as Claude Code analyzed everything about the repository. It now knows how to build the necessary queries. 

The best part is that whenever I mention, "Hey, production's down or something's going wrong," it will know exactly what to query. Claude Code can then perform the analysis and inference on that data.

## Raw YouTube Transcript

Did you know your AI agent can now analyze real-time production telemetry without blowing up your context window? Yeah, let me explain. So, a few weeks ago we released GCX, which is a CLI that gives your coding agents like Codex, Claude Code, Gemini context into your Grafana Cloud Enterprise or OSS environments. Now, why use GCX CLI instead of MCP? This is another alternative, but as you know, MCP can give you some context window bloating with all the tools that it loads in up front before you even send a prompt. A CLI approach is side-steps this entirely, gives you zero token cost up front until you actually need to use the queries. So, getting started with GCX below is super simple. You can go down to the install steps. We have methods for macOS, Linux, or Windows. You can use curl, homebrew. You can even grab the binary directly from the releases page. Now, I've already gone ahead and set up GCX. So, if we go into the terminal, we can start to interact with this. If we just type in GCX, you'll see all the available commands you can run against your Grafana instance. To authenticate yourself, you can just go into GCX off login. This will open up a Chrome window to authenticate yourself against your stack. From there, you can start to run any command against GCX. So, if I wanted to prompt the assistant, I could already just say GCX GCX assistant prompt and then whatever I want here. Now, I've actually gone ahead and set up some skills using GCX. So, if we open Cursor, you can see that I have a K8s telemetry.md file. And this is really a skill on how to interpret my production Kubernetes environment. So, I had the assistant through GCX go and fetch all the data that knows about my Kubernetes environment in Grafana Cloud, return me that list, and now I have a skill based on it. I also have a GCX skill directly, which you see below. And this pretty much happened because Claude Code analyzed everything about that repo and created a skill so it knows how to build these queries. And what's nice and now every time I say, "Hey, production's down or something's going wrong," it'll know exactly what to query, and then Claude Code can do the analysis and inference on that.

