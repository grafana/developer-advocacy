# AI Week: Wednesday announcements

Published on 2026-07-29T19:00:26Z

## Description

Wednesday is about operations and maintenance. Here's what we're announcing today! Check out grafana.ai for more details on ...

URL: https://www.youtube.com/watch?v=5P7qSKIRSek

## Summary

The community call titled "AI Week: Wednesday announcements," published on July 29, 2026, featured an overview of new operational features in Grafana Assistant. The speaker discussed two key features: Assistant Automations, which helps manage recurring operational tasks by summarizing service health and notifying users, and Assistant Investigations, which aids in diagnosing issues by correlating metrics, logs, traces, and profiles to produce structured reports. These features aim to reduce the manual workload involved in monitoring and maintaining production systems while emphasizing that accountability remains with the user. 

Topics: Grafana Assistant, Assistant Automations, Assistant Investigations, operations and maintenance, service health monitoring.

## Chapters

00:00:00 Introduction to Grafana Assistant features for operations and maintenance
00:00:46 Overview of operations and maintenance features
00:01:32 Offloading vigilance in operations and maintenance

[music] 

Welcome to day three of AI Week! Wednesday is all about operations and maintenance. Once your code hits production, the work required to keep it running is often surprisingly manual. Someone still has to watch those dashboards, decide whether that error spike is real or actionable, and document everything that happened that day, every single day.

Today, we are announcing two features of Grafana Assistant that are designed to take that burden off your plate. 

**Assistant Automations** and **Investigations** are now generally available. 

- **Assistant Automations** handles the recurring work required in operations and maintenance. You can save an Assistant prompt and run it on a schedule. Think of it like a morning briefing that summarizes the operational health of your service over the last 24 hours. Every run keeps its own conversation and history, and it can notify you in Slack when it's done or if it needs approval.

- **Assistant Investigations** is for when something actually breaks. It can perform a deep dive and correlate your metrics, logs, traces, and profiles. It can develop and test its own hypotheses, and at the end of the day, it hands you a structured report. You can follow along in a workspace, see what it has ruled out, and add guidance while it works.

An important thing to note here is that for both of these features, you're offloading vigilance, not accountability. The reasoning and the evidence are still there for you to review, and at the end of the day, you're still the one making the call.

Head over to grafana.ai to see all the details of everything we're announcing this week, and check back in tomorrow for day four.

## Raw YouTube Transcript

[music] >> Welcome to day three of AI week and Wednesday is all about operations and maintenance. Because once your code hits production, often the work required in keeping that running is surprisingly manual. Because somebody still has to watch those dashboards and someone has to decide whether that error spike is real or actionable and then someone has to document everything that happened that day, every single day. So, the two features that we have today are both features of Grafana Assistant that are designed to take that burden off of your plate. Assistant automations and investigations are now generally available. Assistant automations handles the recurring work required in operations and maintenance. So, you can save an Assistant prompt and then you can run that on a schedule. So, think of like a morning briefing that summarizes the operational health of your service across the last 24 hours. Every run keeps its own conversation and history and then it can notify you in Slack when it's done or if it needs approval. Now, Assistant investigations is for when something actually breaks. It can do a deep dive and correlate your metrics, logs, traces, and profiles. It can develop and test its own hypotheses and at the end of the day, it just hands you a structured report. You can follow along in a workspace, see what it's ruled out, and add guidance while it works. Now, an important thing to note here is that for both of these features, you're offloading vigilance, not accountability. Because the reasoning and the evidence is still there for you to review. And at the end of the day, you're still the one that's making the call. Head over to grafana.ai to see all the details of everything we're announcing this week and check back in tomorrow for day four.

