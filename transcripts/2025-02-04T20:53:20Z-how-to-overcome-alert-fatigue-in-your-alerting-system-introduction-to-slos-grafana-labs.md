# How to Overcome Alert Fatigue in Your Alerting System | Introduction to SLOs | Grafana Labs

Cut Through Alert Noise with SLOs! Tired of endless alerts that don't reflect real issues? SLOs (Service Level Objectives) help ...

Published on 2025-02-04T20:53:20Z

URL: https://www.youtube.com/watch?v=gQ0z4t7In-Y

Transcript: Do you feel like your alerting
system is constantly crying wolf, making it difficult to determine what
is an actual issue and what isn't? If your team is buried in
noisy alerts, you're not alone, and there's a better way to
approach alert prioritization. Hi, I'm Jake Swiss on the Grafana Labs
product marketing team. In this video, I'll show you how service level objectives
or SLOs can help you dramatically reduce noisy alerts and
focus on what really matters, keeping your users happy
and your services, reliable. Let's start by talking about why
you're experiencing noisy alerts. The main culprit is monitoring systems
that rely on raw metrics or overly sensitive thresholds. These alerts
notify us of server runtime behavior, but don't necessarily express
real user impact. For example, a spike in latency might trigger an
alert even if it only lasts a few seconds and has no noticeable impact
on the user. The result after this happens over and over again is the
eventual alert fatigue of your engineers. Here's how SLOs help solve the problem. Instead of focusing on
every minor fluctuation, SLOs help you define what good
reliability looks like by monitoring critical service indicators. These directly correlate with your
user's experience. For example, rather than alerting on
every small latency spike, you can set an SLO to ensure
that 95% of requests stay below 300 milliseconds. This way alerts only fire when
your SLO is at risk helping you focus on what matters most:
Your customer's experience. So how can you start using SLOs? Here
are a few tips on getting started. First, audit your current alerts.
Every time a situation does occur, what are the key alerts that are firing? You'll want to start to phase those out, which don't directly tie
into your user's impact. Less is more
when it comes to meaningful alerting. Align your SLOs with
business critical services. Focus on what your users care about most, like a fast checkout experience
or seamless video streaming. Set meaningful error budgets.
These act as guardrails, helping you prioritize technical
debt over innovation decision making. Finally, just get started. Pick one SLO to start with and
aim for continuous improvement. Reducing noisy alerts starts with
aligning your alerting strategy to SLOs and focusing on user
impact, not just raw metrics. Ready to get started? Start auditing your alerts today and
check out the blog and resources linked to in the description below for more
tips on implementing and adopting SLOs.

