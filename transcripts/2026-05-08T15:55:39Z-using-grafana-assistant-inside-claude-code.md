# Using Grafana Assistant Inside Claude Code

Published on 2026-05-08T15:55:39Z

## Description

Shawn Pitts demos how you can use Grafana Assistant inside Claude Code to get an analysis and code recommendation to fix an ...

URL: https://www.youtube.com/watch?v=viEVAcpu23M

## Summary

In the video titled "Using Grafana Assistant Inside Claude Code," published on May 8, 2026, Shawn Pitts demonstrates how to utilize the Grafana Assistant within Claude Code for troubleshooting application issues. The session showcases how the Grafana Assistant can analyze telemetry data to identify problems, specifically in generating follow-up recommendations, and provide code recommendations for fixes. Key takeaways include the seamless integration of Grafana Assistant with Claude Code, allowing developers to diagnose issues without manually sifting through logs. This integration enhances the development workflow by enabling real-time analysis and code adjustments directly within the coding environment.

Topics: Grafana Assistant, Claude Code, telemetry analysis, code recommendations, troubleshooting

## Chapters

00:00:00 Using Grafana Assistant with Claude Code for troubleshooting
00:00:45 Using Grafana Assistant for code recommendations

Did you know you can pair the Grafana Assistant directly with Claude Code to troubleshoot issues so you never even have to leave Claude Code? I'm actually using it here in real-time to figure out why my app isn't generating follow-up recommendations. You can see it above. It should be providing three recommendations, but it's not.

The cool part here is that I'm not digging through log files or copy-pasting anything directly into Claude Code. What I did was go into Claude Code and kick off a skill through my codebase. By prompting that follow-up questions are not being generated for conversational prompts, it actually knew, based on my skill, to call the Grafana Assistant CLI to specifically check the telemetry.

Now, we can see that the analysis was run, and the telemetry confirmed that follow-ups are generated on the server-side, which is good. Three follow-ups were actually generated, but this is clearly a front-end rendering issue. So, it's going to check the relevant code. Now, Claude Code is acting as the developer while the Grafana Assistant is sort of the telemetry expert.

Okay, beautiful. It has the full picture. I'm going to lean out of frame, but it actually did make a code recommendation for us. Let's toggle the agent off, and we can see that we were stripping all this out. Now, we're going to remove all that code since it's not needed. Then, we're just going to approve this change, open a PR, and push that up to production, and we'll be all good.

## Raw YouTube Transcript

Did you know you can pair the Grafana assistant directly with Quad Code to troubleshoot issues so you never even have to leave Quad Code? So, I'm actually using it here in real-time to figure out why my app isn't generating follow-up recommendations. You can see it above. It should be providing three recommendations, but it's not. But, the cool part here is I'm not actually digging through log files or copy-pasting anything directly into Quad Code. So, what I did is if we go into Quad Code, you can see I just kicked off a skill through my codebase. And by prompting simply that uh follow-up questions are not being generated for conversational prompts, it actually knew based on my skill to go and call the Grafana assistant CLI to prompt it specifically to go check the telemetry. Now, we can see that the analysis was actually run and the telemetry confirmed follow-ups are generated on the server-side, which is good. So, three follow-ups were actually generated, but this is clearly a front-end rendering issue. So, it's actually going to check the relevant code. So, now Quad Code is actually acting as the developer where the Grafana assistant was sort of the telemetry expert. Okay, beautiful. So, it has a full picture. I'm going to lean out of frame, but it actually did make a code recommendation for us. So, let's toggle the agent off and we can see that we were actually stripping all this out, but now we are going to remove all that code so it's not needed. And then we're just going to approve this change. We're going to open a PR and push that up to production and we'll be all good.

