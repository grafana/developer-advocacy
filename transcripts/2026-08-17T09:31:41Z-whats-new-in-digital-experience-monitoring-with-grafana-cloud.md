# What&#39;s New in Digital Experience Monitoring with Grafana Cloud

Published on 2026-08-17T09:31:41Z

## Description

Grafana Digital Experience Monitoring (DEM) brings Frontend Observability and Synthetic Monitoring together, so teams can go ...

URL: https://www.youtube.com/watch?v=PfqcVVu_whg

## Summary

The video titled "What's New in Digital Experience Monitoring with Grafana Cloud," published on August 17, 2026, features Pakola, a senior developer advocate at Grafana. The discussion focuses on Grafana's Digital Experience Monitoring (DEM), which integrates front-end observability and synthetic monitoring to enhance user experience analysis and issue resolution. Key features highlighted include session replay for visualizing user interactions, proactive detection of issues, and the integration of synthetic monitoring with front-end observability for seamless data correlation. The main takeaway is that these tools empower engineering teams to quickly identify and resolve user-impacting issues, ultimately improving recovery times and user satisfaction.

Topics: Digital Experience Monitoring, front-end observability, synthetic monitoring, session replay, user experience analysis.

## Chapters

00:00:00 Introduction to Grafana digital experience monitoring
00:02:21 Overview of session replay features in Grafana Cloud
00:03:58 Integrating synthetic monitoring with front-end observability

Hi, I'm Pakola, a senior developer advocate at Grafana. When something breaks in production, the hard question usually isn't what broke; it's who was impacted, what they experienced, and how fast we can fix it. That's the gap Grafana Digital Experience Monitoring (DEM) is built to close.

Grafana Digital Experience Monitoring brings Grafana tools like front-end observability and synthetic monitoring together into one solution, so engineering teams can go from a symptom to a root cause without bouncing between tools or teams. In this video, I'll walk you through a few of the newest Digital Experience Monitoring features and give you a quick demo of each one.

Across the demo, you'll see how Digital Experience Monitoring can help your team. You get:

- **Real user visibility** so you know what people are truly experiencing.
- **Proactive detection** so you can catch problems before users do.
- **End-to-end correlation** connecting a front-end signal all the way to the backend trace behind it.
- **Faster resolution**, cutting your mean time to recovery from hours down to minutes.

Best of all, it's built on open standards, so there's no vendor lock-in.

Let's start with the first feature: **session replay**. Session replay lets you visually replay what a user saw and did inside your web application. Your teams can see exactly what users experience and correlate it with real user monitoring signals like Core Web Vitals, user actions, and traces. This makes it a powerful tool for investigating bugs and running root cause analysis.

Let's dive in and see how to use it. We start by adding the **Faro** web SDK to your application. Faro is Grafana's JavaScript instrumentation library that collects real user monitoring data. When we initialize Faro, we add the replay instrumentation alongside the Faro web instrumentation. During initialization, the default configuration is privacy-first, but you can tweak the masking, privacy, and sampling options to fit your needs.

Once your application is instrumented, we can see it in action. For this example, we'll use **Quick Pizza**, our demo web app that lets you create pizza combinations. On the website, we'll click a few buttons and experiment with the app the same way a real user would. All of that information is being recorded and sent to Frontend Observability, which is where you'll find session replay.

Now, we'll head into the Frontend Observability app. Open sessions and scroll down to find our session recordings. After a few minutes, our sessions are populated. Let's dig in and explore.

To view session recordings, you have two options. You can open a session directly from the session detail page. However, we recommend clicking the green button on the player in a new tab. This lets you watch your recording side by side with the full user journey, which always stays synchronized with the player state. Notice that private information is masked client-side, and this private information is never sent to Grafana. But you can still clearly follow mouse movements and DOM actions.

The replay player gives you full control over playback. You can now play, pause, and skip 10 seconds forward or backward. You can adjust the speed from 0.25x all the way to 16x, which makes it easy to scan longer sessions. The skip inactivity toggle jumps past the quiet parts of the recording, so you stay focused on what really matters. The share button copies a link to a specific moment in the replay, so you can send a teammate the exact second an issue happens.

On the side, you can see the user journey with timestamps showing what both the user and the browser were experiencing. You can also see errors from this view. You can skip straight to them and filter and sort by errors. This is where session replay really gets powerful. Because replays are correlated with your existing Faro telemetry, you can jump from a front-end error in your dashboard directly into replay for the session. You can watch what the user was doing when the error occurred and then dig even further into the correlated traces. This allows for real user visibility, faster resolution, and proactive detection.

Another new feature is the integration between synthetic monitoring and front-end observability. If you haven't used these two tools before, here's what each one does: 

- **Synthetic monitoring** runs automated browser checks against your critical user journey, so you can catch issues before real users ever see them.
- **Front-end observability** captures what your real users are experiencing, turning your front-end performance into something you can measure and act on.

Until now, these two products lived in separate worlds. You could see the synthetic monitoring checks in one dashboard and your real user front-end data in another, with nothing connecting them. That changes with this integration. You can now move between your synthetic checks and your front-end observability sessions, finally breaking down silos in your data.

Here's how it works: Every time a synthetic browser check runs, it now creates a matching front-end observability session. This is a passive integration that works out of the box once Faro is instrumented in your application, without requiring any additional user action. That session is a fully controlled, repeatable run of a real user journey. So from inside a check, you can now pull front-end observability data right there as context and jump straight into that exact session that run created.

Once you're in that session, you have access to the session replay, the user journey, and the traces. Your synthetic checks are no longer just a pass or fail; you get visual feedback from every single run. So when a check fails, you can see exactly what happened. This means you can finally answer the question every on-call engineer asks: Is this check failing a real user problem? And how many users were impacted?

Let's see it in action and jump into synthetic monitoring. I've already set up a synthetic monitoring browser check that mimics a typical Quick Pizza user flow. We head straight to our dashboard. Down in the timepoint explorer, we can see each individual execution. We'll select one. When we scroll down, we will see a button that says "view front-end session." With one click, it opens up the front-end observability session for this exact run.

This view has a lot of important information. We need the session replay, which is a step-by-step visual replay of every action the check performed, the user experience metrics from the run, the full user journey, and the traces behind it. So, in just a few clicks, we went from an alert to a failed execution to watching exactly what happened during the check.

These are a few of the new features we have for Digital Experience Monitoring, and we have so much more on the way. If you're interested in learning more, please visit the Digital Experience Monitoring page linked in the description box down below. To explore each solution in greater depth, please make sure to visit our documentation page. If you found this demo helpful, please remember to like and subscribe to keep up with the latest Grafana Cloud updates. And I'll see you in the next video. 

[music]

## Raw YouTube Transcript

Hi, I'm Pakola, a senior developer advocate at 
Grafana. When something breaks in production, the hard question usually isn't what broke, it's 
who was impacted and what they experienced and how fast we can fix it. That's the gap Grafana 
digital experience monitoring is built to close. Grafana digital experience monitoring or DM brings 
Grafana tools like front-end observability and synthetic monitoring together into one solution so 
engineering teams can go from a symptom to a root cause without bouncing between tools or teams. 
In this video, I'll walk you through a few of the newest digital experience monitoring features 
and give you a quick demo of each one. Across the demo, you'll see how digital experience 
monitoring can help your team. You get real user visibility so you know what people are truly 
experiencing. Proactive detection so you can catch problems before users do. End-to-end correlation 
connecting a front-end signal all the way to the backend trace behind it. And faster resolution 
cutting your mean time to recovery from hours down to minutes. Best of all, it's built on open 
standards, so there's no vendor lock in. Let's start with the first feature, session replay. 
Session replay lets you visually replay what a user saw and did inside your web application. Your 
teams can see exactly what users experience and correlate it with real user monitoring signals 
like core web vitals, user actions, and traces. This makes it a powerful tool for investigating 
bugs and running root cause analysis. Let's dive in and see how to use it. We start by adding 
the Pharaoh web SDK to your application. Pharaoh is Grafana's JavaScript instrumentation library 
that collects real user monitoring data. When we initialize Faro, we add the replay instrumentation 
alongside the Faro web instrumentation. During initialization, the default configuration is 
privacy first, but you can tweak the masking, privacy, and sampling options to fit your needs. 
Once your application is instrumented, we can see it in action. For this example, we'll use Quick 
Pizza, our demo web app that lets you create pizza combinations. On the website, we'll click a 
few buttons and experiment with the app the same way a real user would. All of that information is 
being recorded and sent to Frontend Observability, which is where you'll find session replay. Now, 
we'll head into the front-end observability app. Open sessions and scroll down to find our sessions 
recording. After a few minutes, our sessions are populated. Let's dig in and explore. To view 
sessions recording, you have two options. You can open a session directly from the session detail 
page. However, we recommend clicking the green button on the player in a new tab. This lets you 
watch your recording side by side with full user journey which always stays synchronized with the 
player state. Notice that private information is masked client side and this private information is 
never sent to Grafana. But you can still clearly follow mouse movements and DOM actions. The replay 
player gives you full control over playback. You can now play, pause, and skip 10 seconds forward 
or backwards. You can adjust the speed from 0.25 speed all the way to 16x, which makes it easy to 
scan longer sessions. The skip inactivity toggle jumps past the quiet parts of the recording so you 
stay focused on what really matters. And the share button copies a link to a specific moment in the 
replay so you can send a teammate the exact second an issue happens. On the side, you can see the 
user journey with timestamps showing what both the user and the browser were experiencing. You 
can also see errors from this view. You can skip straight to them and filter and sort by errors. 
And this is where session replay really gets powerful. Because replays are correlated with 
your existing Pharaoh telemetry, you can jump from a front-end error in your dashboard directly 
into replay for the session. You can watch what the user was doing when the error occurred and 
then dig even further into the correlated traces. This allows for real user visibility and faster 
resolution and proactive detection. Another new feature is the integration between synthetic 
monitoring and front-end observability. If you haven't used these two tools before, here's 
what each one does. Synthetic monitoring runs automated browser check against your critical 
user journey, so you can catch issues before real users ever see them. And front-end observability 
captures what your real users are experiencing, and turning your front-end performance into 
something you can measure and act on. Until now, these two products live in separate worlds. 
You can see the synthetic monitoring checks in one dashboard and your real user front-end 
data in another with nothing connecting them. That changes with this integration. So you can 
move between your synthetic checks and your front-end observability sessions and finally 
break down silos in your data. Here's how it works. Every time a synthetic browser check runs, 
it now creates a matching front-end observability session. This is a passive integration that works 
out of the box once Pharaoh is instrumented in your application without requiring any additional 
user action. And that session is a fully controlled repeatable run of a real user journey. 
So from inside a check, you can now pull front-end observability data right there as context and jump 
straight into that exact session that run created. Once you're in that session, you have access 
to the session replay, the user journey, and the traces. Your synthetic checks are no longer 
just a pass or fail. You get visual feedback from every single run. So when a check fails, you 
can see exactly what happened. This means you can finally answer the question every on call engineer 
asks. Is this check failing a real user problem? and how many users were impacted. Let's see it in 
action and let's jump into synthetic monitoring. I've already set up a synthetic monitoring browser 
check that mimics a typical quick pizza user flow. We head straight to our dashboard. Down in the 
timeoint explorer, we can see each individual execution. We'll select one. When we scroll down, 
we will see a button that says view front-end session. With one click, it opens up the front-end 
observability session for this exact run. This view has a lot of important information. We need 
the session replay, which is a step-by-step visual replay of every action, the check performed, 
the user experience metrics from the run, the full user journey, and the traces behind it. 
So, in just a few clicks, we went from an alert to a failed execution to watching exactly what 
happened during the check. These are a few of the new features we have for digital experience 
monitoring, and we have so much more on the way. If you're interested in learning more, please 
visit the digital experience monitoring page linked in the description box down below. To 
explore each solution in greater depth, please make sure to visit our documentation page. If you 
found this demo helpful, please remember to like and subscribe to keep up with the latest Grafana 
Cloud updates. And I'll see you in the next video. [music]

