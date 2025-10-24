# What is Alloy and when does it make sense to use it? | Grafana Alloy for Beginners Ep 2

Published on 2025-10-15T10:33:42Z

## Description

You want to use Grafana Alloy but what is it exactly and when does it make sense to use it? Join Lisa Jung, Staff Developer ...

URL: https://www.youtube.com/watch?v=bFyGd_Sr5W4

## Summary

In this episode of the Grafana Alloy for Beginners series, Lisa Jung, a Staff Developer Advocate at Grafana, introduces Alloy and its role in observability architecture. She explains how Alloy simplifies telemetry data collection by replacing the need for multiple collectors with a unified solution that integrates various data sources like Prometheus and OpenTelemetry. The video discusses the complexities of real-world telemetry setups and highlights Alloy's features, such as native pipelines and enterprise-ready capabilities, which help manage logs, metrics, traces, and profiles efficiently. Lisa concludes by mentioning that the next episode will focus on the fundamentals of Alloy configuration language.

## Chapters

00:00:00 Introductions to the Grafana Alloy for Beginners series  
00:01:15 Overview of Alloy and its role in observability architecture  
00:02:30 Explanation of telemetry data collection and its complexity  
00:03:45 Example of a user transitioning from infrastructure observability to app observability  
00:05:00 Introduction to Alloy as a solution for simplifying data collection  
00:06:20 Benefits of using Alloy, including reduced resource usage  
00:07:10 Managing multiple telemetry sources with Alloy  
00:08:00 Overview of enterprise features and modular design of Alloy  
00:09:00 Teaser for upcoming episodes on Alloy configuration language  
00:09:30 Closing remarks and next episode preview  

# Grafana Alloy for Beginners – Episode Overview

Hi, welcome back to the Grafana Alloy for Beginners series. I'm Lisa Jung, a Staff Developer Advocate here at Grafana. 

In the last episode, we covered what you can expect from this series and all the resources you will need to get started with Alloy. Today, we're diving into the big questions: **What is Alloy and when does it make sense to use it?**

To understand what Alloy is, it's helpful to look at where it fits in the observability architecture. 

## Observability Architecture

Let's say you're observing your infrastructure, applications, or both. You collect data from these sources using a collector or an agent and send it to the observability backend of your choice. In this context, the backend refers to databases such as Loki, Mimir, Tempo, or others. From there, you connect the backend to a visualization frontend, like a Grafana dashboard, where you can query and explore the data that matters to you.

Collecting, processing, and exporting telemetry data is where Alloy comes into play. However, telemetry collection in the real world can get pretty complex. Everybody has different setups, and their needs keep evolving.

### A Real-World Example

For example, imagine a user focused solely on infrastructure observability. They might use a Prometheus node exporter to collect, process, and export metrics data, then send the data to the Prometheus database and visualize it using the Grafana dashboard. 

But down the road, they want to add application observability and start analyzing traces. The problem is that they can't use Prometheus for that. Since OpenTelemetry (OTel) is a leader in distributed tracing, they decide to use the OTel Collector. Now they have to learn, configure, and manage two different types of collectors. The more collectors you have to juggle, the greater the chances for errors.

### The Need for Simplification

This is just a simple example of what telemetry collection looks like in the wild. In reality, you'll often run into much more complex setups with multiple collectors, data format conversions, and various challenges. 

If we're looking to simplify our data collection setup, **Alloy is a great open-source solution to consider**. It comes with native pipelines for Prometheus, OpenTelemetry, Loki, Pyroscope, and more, combining the best collectors into one solution. 

With Alloy, we can gather logs, metrics, traces, and profiles all in one place. This means less memory use, lower CPU overhead, and fewer headaches for our teams. Whether we're keeping an eye on infrastructure or applications, Alloy helps us manage it all without the hassle of juggling multiple collectors. We have one solution to learn, configure, deploy, and maintain.

### Advanced Capabilities

As our systems grow more complex, managing telemetry gets harder. When we need more advanced capabilities, like managing fleets of Alloy instances or balancing workloads, Alloy has enterprise-ready features to support us. Plus, Alloy is built with modular components like LEGO blocks, allowing us to snap these pieces together to build exactly the pipelines we need.

## What's Next?

In this episode, we tackled the big questions: **What is Alloy and when does it make sense to use it?** Next up, we'll jump into the fundamentals of Alloy configuration language, the building blocks for everything ahead.

Thank you for hanging out, and I'll see you in the next episode!

## Raw YouTube Transcript

Hi, welcome back to the Grafana Alloy 
for Beginners series. I'm Lisa Jung, a Staff Developer Advocate here at Grafana. In the 
last episode, we covered what you can expect from this series and all the resources you will need 
to get started with Alloy. Today, we're diving into the big questions. What is Alloy and when does it 
make sense to use it? To understand what Alloy is, it's helpful to look at where Alloy fits 
in the observability architecture. Let's say you're observing your infrastructure or 
applications or both. You collect data from these sources using a collector or an agent, 
and send it to the observability backend of your choice. In this context, the backend 
refers to databases such as Loki, Mimir, Tempo, or others. From there, you connect 
the backend to a visualization frontend, like a Grafana dashboard where you can query 
and explore the data that matters to you. Collecting, processing and exporting telemetry 
data is where Alloy comes into play. Now, telemetry collection in the real world can 
get pretty complex. Everybody has different setups and their needs keep evolving. For 
example, imagine a user who's focused solely on infrastructure observability. They might use 
a Prometheus node exporter to collect, process, and export metrics data, then send the data to 
the Prometheus database and visualize using the Grafana dashboard. But down the road, they want to 
add app observability and start analyzing traces. The problem is that they can't use Prometheus for 
that, and since OTel is a leader in distributed tracing, they decide to use the OTel Collector. 
Now they have to learn, configure, and manage two different types of collectors. The more you 
have to juggle, the more chances there are for errors. Now, this is just a simple example of 
what telemetry collection looks like in the wild. In reality, you'll often run into much more 
complex setups with multiple collectors, data format conversions, and all kinds of 
challenges. If we're looking to simplify our data collection setup, Alloy is a great open 
source solution to consider. It comes with native pipelines for Prometheus, OpenTelemetry, Loki, 
Pyroscope, and more, combining the best collectors into one solution. With Alloy, we can gather 
logs, metrics, traces, and profiles all in one place. That means less memory use lower CPU 
overhead and fewer headaches for our teams. And whether we're keeping an eye on infrastructure or
applications, Alloy helps us manage it all without the hassle of juggling multiple collectors. 
We have one solution to learn, configure, deploy, and maintain. And as our systems grow 
more complex, managing telemetry gets harder. When we need more advanced capabilities like 
managing fleets of Alloy instances or balancing workloads, it has enterprise ready features to 
support us. Plus, Alloy is built with modular components like LEGO blocks, so we can snap these 
pieces together however we want to build exactly the pipelines we need. We'll be diving into 
how to do just that throughout the series. In this episode, we tackle the big questions. What 
is Alloy and when does it make sense to use it? Next up, we'll jump into the fundamentals of 
Alloy configuration language, the building blocks for everything ahead. Thank you for hanging 
out and I'll see you in the next episode.

