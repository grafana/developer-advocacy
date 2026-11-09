# How to use Grafana Assistant with the AWS CloudWatch data source

Published on 2026-07-17T14:00:26Z

## Description

Grafana Assistant meets AWS CloudWatch! In this video, Staff Software Engineer Ivana Huckova shows how to use Grafana ...

URL: https://www.youtube.com/watch?v=t4Gv0XFaOSI

## Summary

The show is titled "How to use Grafana Assistant with the AWS CloudWatch data source," published on July 17, 2026. The speaker, Ivana Huckova, is a Staff Software Engineer on the Grafana Assistant team. In this session, Ivana demonstrates how Grafana Assistant can be utilized with AWS CloudWatch to explore metrics and build dashboards using natural language queries. Key takeaways include the Assistant's ability to automatically discover metrics, suggest queries, and create dashboards based on best practices, making data exploration faster and more intuitive for users. 

Topics: Grafana Assistant, AWS CloudWatch, natural language queries, dashboard creation, metrics exploration.

## Chapters

00:00:00 Using Grafana Assistant with AWS CloudWatch
00:01:35 Building a dashboard with Grafana Assistant
00:02:24 Creating a dashboard with Grafana Assistant and AWS CloudWatch

Hello, I'm Ivana, a software engineer on the Grafana Assistant team. We are building Grafana Assistant with a big tent approach, and today you can use it to query more than 20 different data sources using natural language. 

Let's have a look at how you can use it with CloudWatch and how you can get insights and build dashboards using natural language. 

Here we have a new window with Grafana Assistant. As you can see, you can use it to explore and understand what kind of metrics or telemetry you have in your data source. This is especially helpful if you are new to a data source or just joining a team and trying to understand what's available. 

In this case, I'm asking it to describe what's available in CloudWatch. The Assistant automatically discovers the metrics, groups them into logical categories, and shows us what we can query. It also suggests a quick option, so you can either pick from the suggestions or just describe what you're looking for in your own words. 

Here, I'm selecting AWS metrics for instance CPU, network, and disk. From there, it gives me more specific options, and I'm going to choose CPU utilization across my instances. Behind the scenes, the Assistant is composing the query, running it against CloudWatch, and generating and visualizing the insights. You can see the graph here along with annotations that highlight key events, like where CPU usage peaked and what the value was. 

From here, I can continue the conversation, ask follow-up questions, or go deeper into the data, but instead, I'll ask it to build a dashboard. Now, the Assistant uses its understanding of best practices to create a dashboard for me. It queries CloudWatch, builds panels, and organizes everything into a useful layout. 

And just like that, we get a ready-to-use dashboard that we can save and continue working with. So, if you are using CloudWatch, give it a try. Grafana Assistant makes exploring your data a lot faster and easier. 

>> [music]

## Raw YouTube Transcript

Hello, I'm Ivana, a software engineer on Grafana Assistant team. We are building Grafana Assistant with a big tent approach and today you can use it to query more than 20 different data sources using natural language. Let's have a look on how you can use it with CloudWatch and how you can get insights and build dashboards using natural language. So here we have a new window with Grafana Assistant. As you can see, you can use it to explore and understand what kind of metrics or telemetry you have in your data source. This is especially helpful if you are new to a data source or just joining a team and trying to understand what's available. In this case, I'm asking it to describe what's available in CloudWatch. The Assistant automatically discovers the metrics, groups them into logical categories, and shows us what we can query. It also suggests a quick option, so you can either pick from the suggestions or just describe what you're looking for in your own words. Here, I'm selecting AWS metrics for instance CPU, network, and disk. From there, it gives me more specific options and I'm going to choose CPU utilization across my instances. Behind the scenes, Assistant is composing the query, running it against CloudWatch, and generating and visualizing the insights. You can see the graph here along with annotations that highlight key events like where CPU usage peaked and what the value was. And from here, I can continue the conversation, ask follow-up questions, or go deeper into data, but instead, I'll ask it to build a dashboard. Now, the assistant uses its understanding of best practices to create a dashboard for me. It queries CloudWatch, builds panels, and organizes everything into a useful layout. And just like that, we get a ready-to-use dashboard that we can save and continue working with. So, if you are using CloudWatch, give it a try. Grafana Assistant makes exploring your data a lot faster and easier. >> [music]

