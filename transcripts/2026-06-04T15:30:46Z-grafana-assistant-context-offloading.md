# Grafana Assistant Context Offloading

Published on 2026-06-04T15:30:46Z

## Description

Context Offloading is a pipeline solution for managing Observability with AI Agents. If you are building AI Agents that work with ...

URL: https://www.youtube.com/watch?v=iUHnys9oTmM

## Summary

The show is titled "Grafana Assistant Context Offloading," published on June 4, 2026. The speaker discusses the concept of context offloading in the context of building AI agents that manage observability data. Key features of Grafana Assistant are highlighted, focusing on how it handles large JSON data by storing it in browser memory and only sending structured summaries to the language model, which improves efficiency and reduces costs. The speaker emphasizes that this method allows for faster responses and better reasoning by the model, making it a valuable approach for developers working with large structured data.

Topics: Grafana Assistant, context offloading, observability, AI agents, JSON data management.

## Chapters

00:00:00 Introduction to context offloading in AI agents
00:00:54 Context offloading in Grafana Assistant
00:01:43 Using context offloading with Grafana Assistant

If you are building AI agents that work with real data, you have probably hit this wall. Your agent calls a tool, and the tool result comes back with 200 kilobytes of raw JSON data, which is very popular in MCP servers. The problem is that you've blown a huge chunk of the context window with raw data that the model or the agent does not really need. This is especially painful in observability, where dashboarding configs, metrics, logs, traces, and profiles all consist of large amounts of raw data. The context window space is expensive, both in latency and in cost.

While building Grafana Assistant, we tried something called context offloading. The idea is simple: instead of sending the full JSON result to the LLM, we store the JSON result in the browser memory and only send back a structured summary of the JSON blob. The agent can then use a JQ tool to selectively query pieces of this whole data. This approach makes the LLM loop much quicker and keeps your context window small.

Let me show you how this looks in real life. In this case, I asked Grafana Assistant to describe the dashboard. It called the read dashboard information tool to get panels, variables, and metadata, but the response was 69 kilobytes, which was simply too large to put in the context window. Instead, it saved this JSON in memory and returned this artifact. The Grafana Assistant then called the JQ tool to get selective data from this JSON blob. In this case, it queried all the panels to get their IDs, titles, types, and descriptions. This selectively retrieves only one piece of data from the whole JSON blob.

It continued to gather more data, but in the end, it was able to answer my question without overwhelming the context. What surprised us is how naturally models work with this approach. You give them the schema, and they write reasonable JQ queries on the first try. It is like giving your agents a read-only database, except the database is browser memory and the query language is JQ. The model reasons better because its context isn't polluted with noise. Responses are faster, token costs go down, and you're not hitting context limits on the second tool call.

If you're building agents that deal with large structured data, consider this pattern. You can also see it in action with Grafana Assistant in Grafana Cloud.

## Raw YouTube Transcript

If you are building AI agents
that work with real data, you have probably hit this wall. Your agent calls a tool and
the tool result comes back
with 200 kilobytes of raw JSON data. Very popular
in MCP servers. Well, the problem is now you've blown a huge
chunk of the context window with raw data that the model or the
agent does not really need. This is especially
painful in observability.
Dashboarding configs, metrics, logs, traces, profiles. It's
all raw data and the data's big. The context window space is expensive,
both in latency and in cost. So while building Grafana Assistant, we tried something called context
offloading. And the idea is simple. Instead of sending the full
JSON result to the LLM, we will store the JSON result in the
browser memory and only send back the structured summary of the JSON blob. The agent can then use a JQ
tool to selectively query pieces of this whole data.
This makes the LLM loop much quicker and especially keeps your
context window small. Let me show you how this looks
in real life. So in this case, I asked Grafana Assistant
to describe the dashboard. It called the read dashboard information
tool to get panels variables and metadata, but the
response was 69 kilobytes, which was simply too large to just
put in the context window. Instead, it saved this JSON in a memory
and returned this artifact. The Grafana Assistant then called
the JQ tool to get selective data from this JSON blob. In this case, it queried all the panels to get its
IDs, titles, types, and descriptions. So this selectively only gets one
piece of data from the whole JSON blob. It continued to get some
more data, but in the end, it was able to answer my question
without blowing all the context. What surprised us is how naturally
models work with this. You give them the schema and they write reasonable
JQ queries on the first try. It is like giving your
agents a read-only database, except the database is browser
memory and the query language is JQ. The model reasons better because its
context isn't polluted with noise. Responses are faster, token costs go down, and you're not hitting context
limits on the second tool call. If you're building agents that
deal with large structured data, consider this pattern. You can also see it in action with
Grafana Assistant in Grafana Cloud.

