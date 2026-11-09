# When to Use Grafana Assistant vs. MCP vs. GCX: Part 2

Published on 2026-08-19T18:00:14Z

## Description

When should you reach for Grafana MCP? ✋ It's one of the two “hands” in Grafana's AI toolkit — and the easy one at that.

URL: https://www.youtube.com/watch?v=HDmJyo9cyf8

## Summary

The video titled "When to Use Grafana Assistant vs. MCP vs. GCX: Part 2," published on August 19, 2026, features a speaker discussing the Grafana MCP (Model Context Protocol) as part of Grafana's AI toolkit. The speaker explains that MCP allows AI clients to interact with Grafana, offering an easy way to access its features through hosted or self-hosted options. Key takeaways include when to use MCP, such as with hosted chat tools lacking a terminal, integrating Grafana into existing workflows, and benefiting from enhanced tool discovery. The speaker also contrasts MCP with other tools, indicating that while MCP is curated, it may not cover all Grafana functionalities.

Topics: Grafana MCP, AI toolkit, tool discovery, hosted solutions, self-hosting

## Chapters

00:00:00 Introduction to Grafana MCP
00:00:46 When to use Grafana MCP
00:01:33 Discussing the differences between Grafana MCP and GCX

There are three Grafana AI tools that people regularly confuse: Grafana Assistant, Grafana MCP, and GCX. In the last video, I talked about the brain, Assistant. In this video, I'm going to be discussing one of the two hands, in particular, the easy hand, Grafana MCP.

Grafana MCP, or Model Context Protocol, is a way to let an AI client reach into Grafana. In MCP, there are two parts. The first is the client, which is the AI app that you're using, such as ChatGPT, Claude.ai, or Cursor. The second part is the server, which acts like the door into Grafana that exposes those tools.

For the server, there are two ways to go about getting it. Honestly, the easiest way is to use the Grafana Cloud hosted version because it's already running, authentication is built-in, and you can just connect to it and go. However, if you prefer, you can also self-host the open-source version on your own infrastructure.

So, when would you use Grafana MCP? 

1. **When you're using hosted chat tools that don't have a terminal**: This includes tools like Claude.ai or ChatGPT, or even when using your phone. Since no shell means no CLI, MCP is pretty much your only way in.
   
2. **When you want to integrate Grafana into a tool that you already use**: For example, if you're already using Claude or Cursor, you can simply add the server without changing your workflow.

3. **When you want the best tool discovery out of the box**: In MCP, tools describe themselves up front. So, even if you're using a smaller and cheaper model, it will still know what it can do without any trial and error.

So, why would you use anything other than Grafana MCP? Well, Grafana MCP is deliberately curated and does not reach into every corner of Grafana. If you want something a little bit more esoteric, that's what the power hand is for. 

Next up is GCX.

## Raw YouTube Transcript

There are three Grafana AI tools that people regularly confuse, and that's Grafana Assistant, Grafana MCP, and GCX. In the last video, I talked about the brain, Assistant. In this video, I'm going to be talking about one of the two hands, in particular, the easy hand, Grafana MCP. Grafana MCP, or Model Context Protocol, is like a way to let an AI client reach into Grafana. In MCP, there are two parts. The first is the client, that is the AI app that you're using, so ChatGPT or Claude.ai or Cursor. Then, there's the server, which is kind of like the door into Grafana that exposes those tools. For the server, there are two ways that you can go about getting that. Honestly, the easiest way is to just use the Grafana Cloud hosted one because it's already running, auth is built-in, and you just connect to it and go. But, if you want to, you can also self-host the open-source one on your own infra. Okay, so when would you use Grafana MCP? First, when you're using hosted chat tools that don't have a terminal, so that's Claude.ai or ChatGPT or your phone because no shell means no CLI, so MCP is pretty much your only way in. Second, when you want to bolt Grafana onto a tool that you already use. So, let's say you're already using Claude or Cursor, then you can just add the server and you don't have to change your workflow. And third, when you want the best tool discovery out of the box. In MCP, tools describe themselves up front. So, even if you're using a smaller and cheaper model, it'll still just know what it can do without any trial and error. So, why would you use anything other than Grafana MCP? Well, Grafana MCP is deliberately curated. It doesn't reach into every corner of Grafana. So, what if you want something a little bit more esoteric? Well, that's what the power hand is for. Next up is GCX.

