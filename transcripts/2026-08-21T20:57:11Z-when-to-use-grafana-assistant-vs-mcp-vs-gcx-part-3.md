# When to Use Grafana Assistant vs. MCP vs. gcx: Part 3

Published on 2026-08-21T20:57:11Z

## Description

When should you use gcx? If Grafana Assistant is the brain and Grafana MCP is the easy hand, gcx is the power hand. Built for ...

URL: https://www.youtube.com/watch?v=bWtlNE8GdAI

## Summary

The show is titled "When to Use Grafana Assistant vs. MCP vs. gcx: Part 3," published on August 21, 2026. The speaker discusses the differences between Grafana Assistant, Grafana MCP, and GCX, describing GCX as the powerful command line interface (CLI) designed for AI agents. Key points include when to use GCX, such as for terminal coding agents, accessing comprehensive Grafana Cloud features, and automation in CI/CD environments. The speaker emphasizes that while Grafana Assistant and MCP serve specific roles, GCX is essential for advanced functionalities and automation without requiring a subscription. 

Topics: Grafana Assistant, Grafana MCP, GCX, command line interface, automation, Grafana Cloud.

## Chapters

00:00:00 Understanding GCX and its use cases
00:00:47 Understanding when to use GCX
00:01:34 Understanding the roles of Grafana Assistant, MCP, and GCX

I'm differentiating between Grafana Assistant, Grafana MCP, and GCX. In this segment, I'm focusing on GCX. If Assistant is the brain and Grafana MCP is the easy hand, then GCX is the power hand. It is the CLI that's built for AI agents. 

**Quick refresher:** A CLI is a command line interface, meaning no clicking—just type commands. GCX is the Grafana CLI designed for an agent to drive. 

So, when would you use GCX? 

1. **When using terminal coding agents** like Cloud Code, Cursive, or Codex. It writes your code, pulls the exact log or metric that you're looking for, and verifies against it—all without you having to leave your editor. 

2. **When you need absolutely everything.** GCX wraps the entire Grafana Cloud. We're talking SLOs, synthetics, K6, and IRM. If you need some of those esoteric things that the MCP server can't reach, GCX is what you should reach for. 

3. **When you want to do automation in CI/CD.** GCX has dry run mode, JSON outputs, and exit codes that an agent can act on. It's built for GitOps. 

Now, do you need Grafana Assistant for GCX? No, not even a subscription. Metrics, logs, alerts, and dashboards all work on just a service account token. The only reason you would use Assistant is if you were calling GCX Assistant directly. That taps into Assistant's reasoning, and so it's billed separately. 

So, that's your map: Assistant is the brain, Grafana MCP is the easy hand, and GCX is the power hand. It's not really Assistant versus MCP versus GCX; they actually work really well together to give you the best choice in how to access your Grafana stack.

## Raw YouTube Transcript

I'm differentiating between Grafana Assistant, Grafana MCP, and GCX. And in this one, I'm talking about GCX. If Assistant is the brain and Grafana MCP is the easy hand, well, GCX is the power hand. It is the CLI that's built for AI agents. Quick refresher here, a CLI is a command line interface. So, no clicking, just type commands. And GCX is the Grafana CLI that's built for an agent to drive. So, when would you use GCX? First, when you're using terminal coding agents like Cloud Code, Cursive, or Codex. It writes your code, pulls the exact log or metric that you're looking for, and verifies against it, all without you having to leave your editor. Second, when you need absolutely everything. GCX wraps the entire Grafana Cloud. We're talking SLOs, synthetics, K6, IRM. And so, if you need some of those esoteric things that the MCP server can't reach, GCX is what you should reach for. And third, when you want to do automation in CI/CD. Because GCX has dry run mode, JSON outputs, and exit codes that an agent can act on. So, it's built for GitOps. Now, do you need Grafana Assistant for GCX? No. Not even a subscription, because metrics, logs, alerts, and dashboards, they all work on just a service account token. Now, the only reason that you would use Assistant is if you were calling GCX Assistant directly. That taps into Assistant's reasoning, and so it's billed separately. So, that's your map. Assistant is the brain. Grafana MCP is the easy hand, and GCX is the power hand. It's not really Assistant versus MCP versus GCX. They actually work really well together to give you the best choice in how to access your Grafana stack.

