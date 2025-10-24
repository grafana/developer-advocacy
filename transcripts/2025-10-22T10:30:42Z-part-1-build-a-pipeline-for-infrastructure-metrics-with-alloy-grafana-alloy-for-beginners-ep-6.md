# Part 1: Build a Pipeline for Infrastructure metrics with Alloy | Grafana Alloy for Beginners Ep 6

Published on 2025-10-22T10:30:42Z

## Description

Time to level up your metrics! Join Lisa Jung and Mischa Thompson from Grafana Labs as they demo how Grafana Alloy ...

URL: https://www.youtube.com/watch?v=tT2r5gHFqzY

## Summary

In this episode of the "Grafana Alloy for Beginners" series, hosted by Lisa Jung, the focus is on building a pipeline for infrastructure metrics using Alloy. The video builds on previous episodes, emphasizing the importance of Service Discovery in dynamic environments where server names and addresses frequently change. Lisa explains how the discovery.http component queries systems like the Kubernetes API or AWS EC2 to automatically track telemetry sources, allowing for seamless collection of metrics. She demonstrates the configuration process, including the use of prometheus.scrape to gather metrics and prometheus.remote_write to send them to Mimir. Viewers are guided through the setup and verification of the configuration, ensuring metrics from targets like Loki, Tempo, and Pyroscope are successfully scraped. The episode concludes with a preview of the next topic, which will cover exposing and processing infrastructure metrics.

## Chapters

00:00:00 Introduction to the Grafana Alloy for Beginners series  
00:01:30 Overview of previous episode on infrastructure logs  
00:02:15 Introduction to today's topic: Building a pipeline for infrastructure metrics  
00:03:00 Explanation of Service Discovery in dynamic environments  
00:04:30 How Service Discovery components work with systems like Kubernetes and AWS  
00:05:45 Introduction to the discovery.http component for querying telemetry sources  
00:06:30 Overview of scraping metrics using prometheus.scrape  
00:07:15 Setting up prometheus.remote_write to send metrics to Mimir  
00:08:00 Instructions to access the starter code and configure the Alloy instance  
00:09:00 Verification of successful metric scraping and next steps in the series  

# Grafana Alloy for Beginners: Episode on Building a Pipeline for Infrastructure Metrics

Hi, welcome back to the **Grafana Alloy for Beginners** series. I'm Lisa Jung, a Staff Developer Advocate here at Grafana. 

Last time, we explored how to collect, process, and export infrastructure logs with Alloy. Today, we're diving into building a pipeline for infrastructure metrics.

Each episode builds on the last. Before starting this section, make sure you've watched episodes one through five and completed section one of the Alloy configuration. 

## Service Discovery with Alloy

Today, we're introducing how to perform **Service Discovery** using Alloy. When monitoring infrastructure or applications, we often work in dynamic environments where things are constantly changing. There could be thousands of servers or containers starting and stopping, with their names and addresses frequently changing. 

We want to avoid keeping up with an ever-changing list of sources that we need to collect telemetry from. But what if we didn't need to hardcode all the names and addresses of these telemetry sources? What if there was a system that automatically tracked all the telemetry sources in our environment, allowing Alloy to query it to discover what to collect from?

That's exactly what **Service Discovery** components do. They're configured to query systems like the Kubernetes API or AWS EC2, which already track your infrastructure. Then they retrieve and format the list of discovered targets, exposing them to other Alloy components for telemetry collection.

In our learning environment, there's an HTTP endpoint that lists the telemetry sources or targets in our infrastructure. These include backends like Loki, Tempo, Mimir, and Pyroscope, which expose the metrics we want to collect. We'll use the `discovery.http` component to query that endpoint and discover those targets. Then, we'll use `prometheus.scrape` to scrape their metrics and `prometheus.remote_write` to send those metrics to Mimir, Grafana's Prometheus-compatible backend.

## Getting Started

To get started, open the series repository and scroll down to section two: **Build a Pipeline for Infrastructure Metrics with Alloy - Part One**. 

### Quick Refresher

Each section kicks off with starter code, followed by tasks that explain what the config does and what you'll need to know. Then there's a solution where you can peek at the finished config. 

For this episode, I'll walk you through the final config to keep things short. Feel free to copy the starter code into your `config.alloy`, give it a try yourself, and then check the solution to see how you did. 

If you haven't already, start up your learning environment and open the `config.alloy` file. 

### Configuration Steps

1. **Discovery Component**: First, we'll use the `discovery.http` component to find the infrastructure targets we want to scrape. This HTTP endpoint is aware of all instances of Loki, Tempo, Mimir, and Pyroscope databases currently running in our environment. The endpoint is included in the repository, so you can copy and paste the URL here.

2. **Refresh Interval**: Set the `refresh_interval` to **2 seconds** for demo purposes.

3. **Scraping Metrics**: Next, we'll use `prometheus.scrape` to scrape metrics from the targets we just discovered. Set both the `scrape_interval` and `scrape_timeout` to **2 seconds** for this demo. Under targets, point to the targets of the `discovery.http.service_discovery` component that we just defined.

4. **Exporting Metrics**: Finally, use a `forward_to` argument to send the scraped metrics to the receiver of the `prometheus.remote_write.mimir` component that we'll define next.

5. **Configuration of the Last Component**: We'll use this component to export the scraped metrics to our locally running Mimir. This is similar to what we did in the last episode. Use the `endpoint` block and set the URL to the destination for the scraped metrics. The URL to Mimir is included in the repository, so you can copy and paste it here.

### Wrapping Up Section Two

We just wrapped up section two where we used the `discovery.http` component to query an endpoint to discover targets to scrape from. Then we set up the `prometheus.scrape` component to scrape metrics from those targets. Finally, we used the `prometheus.remote_write` component to export the metrics to Mimir.

If you're configuring your Alloy instance as you watch this video, don't forget to check the solutions in the series repository. As always, reload the config after making any updates to `config.alloy`. This command is included in your repository. Make sure that you see the **config reloaded** message before you move forward.

### Verification

Let's go back to the series repository and scroll down to the **verification section**. Click on the link to the dashboard and select the section 2 verification dashboard. Here you can see metrics coming in from our discovered targets: Loki, Mimir, Pyroscope, and Tempo. You should see a value of one for each database, indicating that they're being successfully scraped. If you see a zero, that indicates there's been an error somewhere.

In this episode, we learned how to discover, scrape, and export infrastructure metrics with Alloy. Next up, we'll go even further and learn how to expose, scrape, process, and export infrastructure metrics. 

Thank you for watching, and I'll see you in the next episode!

## Raw YouTube Transcript

Hi, welcome back to the Grafana Alloy 
for Beginners series. I'm Lisa Jung, a Staff Developer Advocate here at Grafana. 
Last time, we explored how to collect, process, and export infrastructure logs with Alloy. 
Today, we're diving into building a pipeline for infrastructure metrics. Now, each episode 
builds on the last. Before starting this section, make sure you watched episodes one through five 
and completed section one of the Alloy config. Today, we're introducing how to perform Service 
Discovery using Alloy. When we're monitoring infrastructure or applications, we're often 
working in dynamic environments where things are constantly changing. There could be thousand 
servers or containers starting and stopping, whose names and addresses are constantly 
changing. We want to avoid keeping up with ever-changing list of sources that we need to 
collect telemetry from. But what if we don't need to hardcode all the names and addresses 
of all the telemetry sources? What if there was a system that automatically tracked all the 
telemetry sources in our environment and Alloy could query it to discover what to collect from? 
That's exactly what Service Discovery components do. They're configured to query systems like 
the Kubernetes API or AWS EC2, which already track your infrastructure. Then they retrieve 
and format the list of discovered targets, exposing them to other Alloy components to collect 
telemetry from. In our learning environment, there's an HTTP endpoint that lists the telemetry 
sources or targets in our infrastructure. These include backends like Loki, Tempo, Mimir, and 
Pyroscope which expose the metrics we want to collect. We'll use the discovery.http component 
to query that endpoint and discover those targets. Then we'll use prometheus.scrape to scrape their 
metrics and prometheus.remote_write to send those metrics to Mimir, Grafana's Prometheus compatible 
backend. To get started, open the series repo and scroll down to section two, Build a pipeline for 
infrastructure metrics with Alloy - part one. Now, a quick refresher from last time. Each section 
kicks off with starter code, followed by tasks that explain what the config does, and what 
you'll need to know. Then there's a solution where you can peek at the finished config. 
For this episode, I'll just walk you through the final config to keep things short. Feel free 
to copy the starter code into your config.alloy, give it a go yourself, then check the solution 
to see how you did. Now, if you haven't already, start up your learning environment and 
open the config.alloy file. All right, you can see mine on the screen. First, we'll 
use the discovery.http component to find the infrastructure targets we want to scrape. Now, 
earlier we mentioned that there's a service that exposes those targets for us. This HTTP endpoint 
is aware of all instances of Loki, Tempo, Mimir, and Pyroscope databases that are currently running 
in our environment. This endpoint is included in the repo. You can copy and paste a URL here. Next, 
we set the refresh_interval to 2 seconds just for demo purposes. Next, we'll use prometheus.scrape 
to scrape metrics from the targets we just discovered. We set both the scrape_interval and 
scrape_timeout to 2 seconds for this demo. Then, under targets, we'll point to the targets of the 
discovery.http.service_discovery component that we just defined. Finally,, we'll use a forward_to 
argument to send the scrape metrics to the receiver of the prometheus.remote_write.mimir 
component that we'll define next. Okay, let's configure the last component. We'll use 
this component to export the scraped metrics to our locally running Mimir. To do so, it's very 
similar to what we did in the last episode. We'll use the endpoint block and set the URL to the 
destination that we want to send scraped metrics to. Now the URL to Mimir is included in the repo. 
So you can copy and paste it here. All right, we just wrapped up section two where we use the 
discovery.http component to query an endpoint to discover targets to scrape from. Then we set 
up the prometheus.scrape component to scrape metrics from those targets. Finally, we use the 
prometheus.remote_write component to export the metrics to Mimir. Now, if you're configuring 
your Alloy instance as you watch this video, don't forget to check the solutions in the series 
repo. As always, reload the config after making any updates to config.alloy. Now, this command 
is included in your repo. Make sure that you see the config reloaded message before you move 
forward. Let's go back to the series repo and scroll down to the verification section. Click on 
the link to the dashboard and select the section 2 verification dashboard. Here you can see metrics 
coming in from our discovered targets Loki, Mimir, Pyroscope, and Tempo. Now you should see a 
value of one for each database. This means that they're being successfully scraped. If you 
see a zero, that indicates that there's been an error somewhere. In this episode, we learned how 
to discover, scrape, and export infrastructure metrics with Alloy. Next up, we'll go even 
further and learn how to expose, scrape, process, and export infrastructure metrics. Thank you for 
watching, and I'll see you in the next episode.

