# Introducing Watchers: agentic alerting for Grafana Cloud

Published on 2026-11-04T16:14:03Z

## Description

Watchers are a new Grafana Assistant capability that add an agentic option alongside your existing alerts. They’re built for the cases that are hard to express as a traditional rule: sometimes you can’t spell out every way something can go “wrong,” but you know exactly what “right” looks like. Ask the Assistant to set up a Watcher, describe what healthy looks like, and it keeps watch for when reality starts to drift.

Watchers work with Prometheus and Loki in Grafana Cloud today, so you can watch the real signal directly with no copying data somewhere else first. That’s especially handy for logs, where new error patterns tend to show up but alert rules you haven’t written yet can’t detect them. A Watcher runs continuously in the background, catching “right” turning into “wrong” so you don’t have to.

You can also close the loop in one motion: hand a firing Watcher straight to the Assistant or Assistant Investigations and start remediating right away.

👍 Was this video helpful? Like and subscribe to our channel for more videos.

Connect with Grafana Labs: 
X: (https://www.twitter.com/grafana)   
LinkedIn: (https://www.linkedin.com/company/grafana-labs/)
Facebook: (https://www.facebook.com/grafana)

#Grafana #Observability

URL: https://www.youtube.com/watch?v=HMpp1DNlW8c

## Summary

The video titled "Introducing Watchers: agentic alerting for Grafana Cloud," published on November 4, 2026, features a discussion on the new Grafana Assistant capability called Watchers. The speakers explain how Watchers provide an agentic alerting option that allows users to define what "right" looks like in their systems, enabling continuous monitoring without the need for traditional alert rules. Watchers work seamlessly with Prometheus and Loki in Grafana Cloud, allowing for real-time monitoring of logs and other telemetry. Key takeaways include the ability to set up Watchers for new features, their lightweight nature, and the option to initiate investigations directly through the Assistant when anomalies are detected.

Topics: Watchers, Grafana Assistant, Grafana Cloud, Prometheus, Loki, agentic alerting, monitoring.

## Chapters

00:00:00 Introduction to Watchers and their capabilities

Watchers is another area that provides fantastic always-on capability. What happens is you calibrate the Watcher; that's when you burn the tokens up front. The Watcher is then lightweight and will continuously monitor whatever telemetry it has determined is necessary to observe.

For example, if there is a brand new feature, we may want to watch it as it goes into production and keep an eye on it for a couple of weeks afterward. The agent can intelligently notice what is normal and alert you when something changes. From there, you can easily launch an investigation. You can do it yourself, or you can receive a Slack DM or set it to automatically fire off and start investigating.

## Raw YouTube Transcript

Watchers is another area that this kind of fantastic always on capability. What happens is you calibrate the watcher. That's when you burn the tokens up front. That watcher is then lightweight and it will just keep looking at whatever telemetry it's figured out it needs to look at. So it could be, you know, brand new feature. We want to watch this as it goes into production. Keep an eye on it and maybe for a couple of weeks after we want to keep watching it. The agent can then intelligently notice what's normal and tell you when something changes. And from there, you can just launch an investigation. You can do it yourself or you can get a Slack DM or tell it automatically to fire off and start investigating.

