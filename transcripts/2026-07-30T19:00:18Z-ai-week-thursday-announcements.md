# AI week: Thursday announcements

Published on 2026-07-30T19:00:18Z

## Description

Thursday is about testing and evaluation. Here's what we're announcing today! Check out grafana.ai for more details on ...

URL: https://www.youtube.com/watch?v=FOHdEm-_DEQ

## Summary

The show "AI week: Thursday announcements" was published on July 30, 2026. The speaker discussed the new features related to agent observability and k6 Identic testing. Key announcements included the general availability of agent observability, which allows users to instrument their agents for better testing and evaluation, and the public preview of k6 Identic testing, enabling natural language descriptions for testing without scripting. The speaker emphasized the importance of trusting AI agents and highlighted the integration of evaluator metrics with Prometheus for monitoring quality metrics. 

Topics: agent observability, k6 Identic testing, AI agent evaluation, Grafana Assistant, Prometheus integration.

## Chapters

00:00:00 Introduction to agent observability
00:00:46 Announcing k6 Identic testing in public preview
00:01:31 Building an AI agent: lessons learned

[music] 

Welcome to day four of AI Week. Thursday is all about evaluating and testing your agents because building an agent is actually the easy part. The hard part is trusting it.

The big news of the day is that **agent observability** is now generally available. This is the system that we built for ourselves to test **Grafana Assistant** when we realized that unit tests just weren't cutting it. Here's how it works: 

Instrument your agent with the SDK, and your conversations, tool calls, traces, latency, token use, and cost all become observable in the same place. Then you can add evaluators, LLM judges, plus deterministic checks to score quality on live traffic. You can even add experiments to let you compare a candidate version against the baseline before you ship. And you can make that a CI gate, too. 

Because all evaluator metrics end up in **Prometheus**, you can get paged if a change in the system prompt tanks quality metrics. 

But I think my favorite part of today is the public preview of **k6 Identic testing**. This is a way to describe what you want to test in natural language, and then k6 actually drives the browser for you to do just that without creating any script. It sounds like it wouldn't make much of a difference, but check out the video we have where we get it to beat Wordle. That one is worth watching. 

By the way, if you're at **KubeCon Japan** today, come see my talk at 4:00 p.m. I'm talking about what we learned from building an AI agent. 

Check back in tomorrow to see what's happening on our finale of day five, and as always, go to **grafana.ai** to see everything that we've announced this week.

## Raw YouTube Transcript

[music] >> Welcome to day four of AI Week. Thursday is all about evaluating and testing your agents because building an agent is actually the easy part. The hard part is actually trusting it. The big news of the day is that agent observability is now generally available. This is the system that we built for ourselves to test Grafana Assistant when we realized that unit tests just weren't cutting it. Here's how it works. Instrument your agent with SDK and your conversations, tool calls, traces, latency, token use, and cost all become observable in the same place. Then you can add evaluators, LLM judges, plus deterministic checks to score quality on live traffic. You can even add experiments to let you compare a candidate version against the baseline before you ship. And you can make that a CI gate, too. And because all evaluator metrics end up in Prometheus, you can get paged if a change in the system prompt tanks quality metrics. But I think my favorite part of today is the public preview of k6 Identic testing. This is a way to just describe what you want to test in natural language, and then k6 actually drives the browser for you to do just that without creating any script. Sounds like it wouldn't make much of a difference, but check out the video we have where we get it to beat Wordle. That one is worth watching. And by the way, if you're at KubeCon Japan today, come see my talk at 4:00 p.m. I'm talking about what we learned from building an AI agent. Check back in tomorrow to see what's happening on our finale of day five, and as always, go to grafana.ai to see everything that we've announced this week.

