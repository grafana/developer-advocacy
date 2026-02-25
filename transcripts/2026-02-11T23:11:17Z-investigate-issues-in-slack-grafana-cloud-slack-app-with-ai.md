# Investigate Issues in Slack: Grafana Cloud Slack App with AI

Published on 2026-02-11T23:11:17Z

## Description

The Grafana Cloud app for Slack brings observability and incident response closer to where you and your teams already ...

URL: https://www.youtube.com/watch?v=PxxqBFEvFuQ

## Summary

In this video, the presenter discusses a new feature released by Grafana that integrates AI capabilities into Slack to enhance monitoring for sensitive user data, particularly concerning PII (Personally Identifiable Information) leaks. The speaker highlights the challenges developers face in detecting such leaks across large volumes of log data and demonstrates how the Grafana assistant can efficiently search for PII exposure in production logs. By using the assistant, they were able to quickly identify vulnerabilities in their logs and receive actionable recommendations for sanitizing sensitive information. The video emphasizes the importance of integrating AI into everyday tools to improve data security and response times.

## Chapters

00:00:00 Introduction to Graphfana's new feature  
00:01:15 Importance of AI integration in daily tools like Slack  
00:02:00 Challenges of detecting PII leaks in large datasets  
00:03:30 Introduction to Graphfana assistant for PII detection  
00:04:00 Demonstration: Finding logs with potential PII in production  
00:05:15 Overview of Graphfana's capability to analyze multiple microservices  
00:06:00 Explanation of how Graphfana constructs log queries  
00:07:00 Response time for detecting PII vulnerabilities  
00:08:00 Findings: PII exposure in logs and proposed solutions  
00:09:30 Conclusion on resolving PII issues with Graphfana's tools  

I have been waiting for someone to release a feature like this, and thankfully, Grafana did just that. They are bringing the AI experience closer to the tools that we use on a day-to-day basis, specifically Slack. 

This is significant because most of us aren't living in dashboards 24/7 anymore; we really rely on alerts that usually funnel into Slack. If you are building a product that stores sensitive user data, like bank accounts, social security numbers, or passwords, the odds of catching PII (Personally Identifiable Information) leaks across gigabytes or even terabytes of log data are probably very slim. This isn’t due to poor performance; it's a challenge that many of us have been dealing with for quite some time. 

Now, we can use the Grafana assistant to solve this exact problem. For instance, I can add Grafana and simply say, "Find any logs that might contain PII in production and give me a React to patch it." 

What's awesome is that the Grafana assistant works behind the scenes. It examines all my production services, including multiple microservices, a caching service, and a database. It creates the proper patterns and LogQL queries to run on the backend and then returns any React patterns I need to patch this up.

Once we get a response, which actually took no time at all, it found PII exposure in my offer logs. There were 18 vulnerabilities identified, but fortunately, no front-end PII was found, which is good. Additionally, it provided a React to sanitize the email addresses, allowing me to roll out a solution to my collector and effectively resolve the issue.

## Raw YouTube Transcript

I have been waiting for someone to release a feature like this and thankfully Graphfana did just that. They are bringing the AI experience closer to the tools that we're working with on a day-to-day basis, that being Slack. Now, this is nice because most of us aren't actually living in dashboards 24/7 anymore. We're really relying off alerts that are usually funneling into Slack, right? So if you are building a product that stores sensitive user data like bank accounts, social security numbers, passwords, the odds that you're probably catching PII leaks across gigabytes or even terabytes of log data is probably very slim. And that's not because you're bad. It's just because that's a problem that we've all been dealing with for quite some time. But now we can use the Graphfana assistant to solve this exact problem. So, I'm going to add Graphfana and I'm just going to say find any logs that might contain PII in production and give me a reax to patch it. What's awesome is the Graphfana assistant is working behind the scenes and it's going to look across all my production services. It knows that I have multiple microservices, uh, a caching service, a database, and it's going to look through all of that and it's going to create the proper patterns and logql queries to actually run on the back end and then return me any reax patterns I need to actually patch this up. So once we get a response here, which actually took no time, it actually found PII exposure in my offer logs. It looks like there was 18 uh vulnerabilities there. Uh there's no front-end PI found, which is good. But it's also giving me a reax to sanitize the easy email addresses so I can then roll it out to my collector and we can solve the problem.

