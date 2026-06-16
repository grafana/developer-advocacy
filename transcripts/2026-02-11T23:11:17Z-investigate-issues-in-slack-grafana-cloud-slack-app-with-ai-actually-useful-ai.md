# Investigate Issues in Slack: Grafana Cloud Slack App with AI | Actually Useful AI

Published on 2026-02-11T23:11:17Z

## Description

The Grafana Cloud app for Slack brings observability and incident response closer to where you and your teams already ...

URL: https://www.youtube.com/watch?v=PxxqBFEvFuQ

## Summary

In this video, the speaker discusses a new feature from Grafana that integrates AI capabilities into Slack, aimed at improving log data monitoring, particularly for sensitive user information. The speaker highlights the challenge of identifying personally identifiable information (PII) leaks within large volumes of log data and demonstrates how the Grafana assistant can efficiently search for such vulnerabilities across multiple production services. By using the assistant, the speaker was able to quickly identify PII exposure in their logs and receive actionable recommendations to sanitize the data. This development is positioned as a significant advancement for teams relying on alerts rather than constantly monitoring dashboards.

## Chapters

00:00:00 Introductions to the new Graphfana feature  
00:01:15 Importance of integrating AI with daily tools like Slack  
00:02:00 Challenges of monitoring sensitive user data  
00:03:30 Introduction of the Graphfana assistant for PII detection  
00:04:00 Demonstration of how to use Graphfana to find PII leaks  
00:05:15 Explanation of Graphfana's backend processes for log analysis  
00:06:00 Response time and results of the PII search  
00:06:45 Details on identified vulnerabilities in logs  
00:07:30 Discussing the sanitization of sensitive data  
00:08:00 Next steps for rolling out fixes to the production environment  

I have been waiting for someone to release a feature like this, and thankfully, Grafana did just that. They are bringing the AI experience closer to the tools that we work with on a day-to-day basis, specifically Slack. 

This is particularly nice because most of us aren't living in dashboards 24/7 anymore; we are really relying on alerts that usually funnel into Slack. If you are building a product that stores sensitive user data, such as bank accounts, social security numbers, or passwords, the odds are that you're probably not catching PII leaks across gigabytes or even terabytes of log data. This is not due to negligence; it's simply a problem that we've all been dealing with for quite some time.

Now, we can use the Grafana Assistant to solve this exact problem. For instance, I can add Grafana and say, "Find any logs that might contain PII in production and give me a React component to patch it." 

What's awesome is that the Grafana Assistant works behind the scenes. It looks across all my production services, including multiple microservices, a caching service, and a database. It creates the proper patterns and LogQL queries to run on the backend and then returns any React patterns I need to patch the issue.

Once we get a response, which actually took no time, it found PII exposure in my offer logs. It looks like there were 18 vulnerabilities identified. Fortunately, there was no front-end PII found, which is good. Additionally, it provided me with a React component to sanitize the email addresses, allowing me to roll it out to my collector so we can effectively solve the problem.

## Raw YouTube Transcript

I have been waiting for someone to release a feature like this and thankfully Graphfana did just that. They are bringing the AI experience closer to the tools that we're working with on a day-to-day basis, that being Slack. Now, this is nice because most of us aren't actually living in dashboards 24/7 anymore. We're really relying off alerts that are usually funneling into Slack, right? So if you are building a product that stores sensitive user data like bank accounts, social security numbers, passwords, the odds that you're probably catching PII leaks across gigabytes or even terabytes of log data is probably very slim. And that's not because you're bad. It's just because that's a problem that we've all been dealing with for quite some time. But now we can use the Graphfana assistant to solve this exact problem. So, I'm going to add Graphfana and I'm just going to say find any logs that might contain PII in production and give me a reax to patch it. What's awesome is the Graphfana assistant is working behind the scenes and it's going to look across all my production services. It knows that I have multiple microservices, uh, a caching service, a database, and it's going to look through all of that and it's going to create the proper patterns and logql queries to actually run on the back end and then return me any reax patterns I need to actually patch this up. So once we get a response here, which actually took no time, it actually found PII exposure in my offer logs. It looks like there was 18 uh vulnerabilities there. Uh there's no front-end PI found, which is good. But it's also giving me a reax to sanitize the easy email addresses so I can then roll it out to my collector and we can solve the problem.

