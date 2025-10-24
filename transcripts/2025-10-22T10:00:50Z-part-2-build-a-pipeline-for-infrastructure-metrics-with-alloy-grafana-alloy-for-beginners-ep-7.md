# Part 2 : Build a Pipeline for Infrastructure Metrics with Alloy | Grafana Alloy for Beginners Ep 7

Published on 2025-10-22T10:00:50Z

## Description

Dive into Postgres metrics with Alloy Join Lisa Jung and Mischa Thompson from Grafana Labs as they show how to expose, ...

URL: https://www.youtube.com/watch?v=U_MWuJR76d4

## Summary

In this episode of the Grafana Alloy for Beginners series, hosted by Lisa Jung, the focus is on exposing, scraping, processing, and exporting metrics from a Postgres database using Alloy. The video builds on previous episodes, guiding viewers through the configuration of a pipeline to connect to a Postgres database using the prometheus.exporter.postgres component. Lisa explains how to scrape metrics with prometheus.scrape, process them with prometheus.relabel (adding and modifying labels), and finally export them to Mimir using prometheus.remote_write. Key tasks include simplifying the instance label by removing the postgresql:// prefix and verifying successful data export by checking a dashboard for Postgres metrics. The episode concludes with a preview of the next episode, which will cover using the Alloy UI for debugging pipelines.

## Chapters

Here are the key moments from the livestream along with their timestamps:

00:00:00 Introductions and overview of the episode  
00:01:30 Recap of previous episodes and prerequisites  
00:02:00 Overview of the learning environment and objectives  
00:03:15 Introduction to prometheus.exporter.postgres component  
00:04:00 Setting up the database connection with data_source_names  
00:05:30 Configuring prometheus.scrape to collect metrics  
00:06:45 Explanation of prometheus.relabel for processing metrics  
00:08:00 Adding and modifying labels on metrics  
00:09:30 Simplifying the instance label by removing the prefix  
00:10:45 Forwarding metrics to prometheus.remote_write for export to Mimir  
00:11:30 Verification of exposed, scraped, and processed metrics

# Grafana Alloy for Beginners - Episode 7

Hi, and welcome back to the Grafana Alloy for Beginners series. I'm Lisa Jung, a Staff Developer Advocate at Grafana. 

In the last episode, we used Service Discovery to find telemetry targets, scraped their metrics, and exported them to Mimir, our metrics backend. In this episode, we'll walk through how to expose, scrape, process, and export metrics from a Postgres database using Alloy.

Before we begin, make sure you've watched episodes one through six and completed configuration sections one and two. To get started, open the series repo and scroll down to section three: **Build a pipeline for infrastructure metrics with Alloy - part two**.

## Structure of the Section

Quick reminder: each section starts with starter code, followed by tasks to explain the configuration and what you'll need, and finally, a solution with a finished version. I'll skip the typing and walk you through the final configuration. You can still copy the starter code into `config.alloy`, try it yourself, and compare it with the solution. 

If you haven't already, fire up the learning environment and open `config.alloy`. 

## Objectives for Today

Here's what we're going to accomplish today:

1. We have a Postgres database in our learning environment.
2. We'll use `prometheus.exporter.postgres` to connect to this database and expose its metrics.
3. Then, we'll scrape those metrics using `prometheus.scrape` and process them with `prometheus.relabel`.
4. Finally, we'll use `prometheus.remote_write` to export metrics to Mimir, our metrics backend.

## Setting Up the Components

All right, let's do this. 

What you're seeing here is a `prometheus.exporter.postgres` component we labeled as **mythical**. This component connects to a Postgres database and exposes its metrics for scraping. To make that connection, we set `data_source_names` equal to the database URL, which is included in the repo.

Next, we'll use a `prometheus.scrape` component we labeled as **postgres** to scrape metrics from the Postgres database. We set both the `scrape_interval` and `scrape_timeout` to 2 seconds for demo purposes. Under `targets`, we specify the targets exposed by the `prometheus.exporter.postgres.mythical` component that we defined earlier.

Then, we use the `forward_to` argument to send the scraped metrics to the receiver of the `prometheus.relabel.postgres` component that we'll define next.

## Processing the Metrics

Here, we have the `prometheus.relabel` component to process the metrics. We're using this component to add and modify labels on our metrics before sending them off. 

We define three rule blocks here. Similar to the previous episode, we use the first two rule blocks to add two new labels: 
- **group** set to *infrastructure*
- **service** set to *Postgres*.

Let's zoom in on the last rule block. We'll use this block to clean up an existing label called **instance**. Right now, the instance label holds the full address. We want to simplify that label by removing the `postgresql://` prefix so that it looks cleaner.

Here's how we do that:
- We set `action` to *replace* to tell Alloy we want to replace a label's value.
- Then, we set the `target_label` to **instance** to indicate that the label we're updating is called instance.
- Now, `source_labels` set to **instance** means we're pulling the value from the current instance label. 
- This regex tells Alloy to look for anything with the `postgresql://` prefix and capture what follows.
- Finally, we tell Alloy to replace the value with just the captured part, leaving out the prefix.

### Forwarding the Metrics

Next, we'll scroll up to the `forward_to` argument. We'll use this to tell Alloy to send our cleaned-up metrics to the receiver of the `prometheus.remote_write.mimir` component that we defined in section two.

In this section, we used the `prometheus.exporter.postgres` component to connect to and expose metrics from a Postgres database. We then scraped those metrics using the `prometheus.scrape` component. With the `prometheus.relabel` component, we added group and service labels and cleaned up the existing instance label. Finally, we forwarded the processed metrics to `prometheus.remote_write` to export them to Mimir. 

As always, remember to **reload `config.alloy`** after any changes. The command is in your repo. Run it and wait for the *config reloaded* message before moving on.

## Verification

Next, we'll verify that we've successfully exposed, scraped, processed, and exported metrics to Mimir. To do so, go to your series repo, scroll down to the verification section, click on the link here, and select **section 3 verification**. You should see the dashboard filling with Postgres metrics. Notice that the instance label now just shows the host and port without the `postgresql://` prefix.

## Conclusion

In this episode, we covered how we can expose, collect, process, and export infrastructure metrics with Alloy. Next up, we'll explore how to use the Alloy UI to debug the pipelines we've built. 

Thank you for watching! I'll catch you in the next episode.

## Raw YouTube Transcript

Hi and welcome back to the Grafana Alloy for 
Beginners series. I'm Lisa Jung, a Staff Developer Advocate at Grafana. In the last episode, we 
used Service Discovery to find telemetry targets, scraped their metrics, and exported them to Mimir, 
our metrics backend. In this episode, we'll walk through how to expose, scrape, process, and export 
metrics from a Postgres database using Alloy. Before we begin, make sure you've watched episodes 
one through six and completed configuration sections one and two. To get started, open the 
series repo and scroll down to section three, Build a pipeline for infrastructure metrics with 
Alloy - part two. Quick reminder, each section starts with starter code, then tasks to explain 
the config and what you'll need, and finally a solution with a finished version. I'll skip the 
typing and walk you through the final config. You can still copy the starter code into config.alloy, 
try it yourself, and compare with the solution. If you haven't already, fire up the learning 
environment and open config.alloy. Here's what we're going to accomplish today. In our learning 
environment, we have a Postgres database. We'll use prometheus.exporter.postgres to connect to 
this database and expose its metrics. Then we'll scrape those metrics using prometheus.scrape 
and process them with prometheus.relabel. Then we'll use prometheus.remote_write to export 
metrics to Mimir, our metrics backend. All right, let's do this. What you're seeing here is 
a prometheus.exporter.postgres component we labeled as mythical. This component connects to 
a Postgres database and exposes its metrics for scraping. To make that connection, we set the 
data_source_names equal to the database URL. This URL is included in the repo. Next, we'll 
use a prometheus.scrape component we labeled as postgres to scrape metrics from the Postgres 
database. We set both the scrape_interval and scrape_timeout to 2 seconds for demo purposes. 
Under targets, we specify the targets exposed by prometheus.exporter.postgres.mythical 
component that we defined earlier. Then we use the forward _to to send the scraped metrics 
to the receiver of the prometheus.relabel.postgres component that we'll define next. Here. we have 
the prometheus.relabel component to process the metrics. And we're using this component 
to add and modify labels on our metrics before sending them off. We define three rule 
blocks here. Similar to the previous episode, we use the first two rule blocks to add two new 
labels. Group set to infrastructure and service set to Postgres. All right, let's zoom in on the 
last rule block. We'll use this block to clean up an existing label called instance. Right now, the 
instance label holds the full address. We want to simplify that label by removing the postgresql:// 
prefix so that it looks like this. And here's how we do that. We set action to replace to tell 
Alloy we want to replace a label's value. Then we set the target_label to instance to mean that 
the label we're updating is called instance. Now, source_labels set to instance says we're pulling 
the value from the current instance label. And this regex tells Alloy to look for anything with 
the postgresql:// prefix and capture what follows. Next, we tell Alloy to replace a value with just 
the captured part, leaving out the prefix. All right. Then, we're going to scroll up to the 
forward_to argument. We're going to use this to tell Alloy to send our cleaned up metrics to 
the receiver of the prometheus.remote_write.mimir component that we defined in section two. In this 
section, we use the prometheus.exporter.postgres component to connect to and expose metrics 
from a Postgres database. Next, we scrape those metrics using the prometheus.scrape component. 
Then with the prometheus.relabel component, we added group and service labels and cleaned up 
the existing instance label. Finally, we forwarded the processed metrics to prometheus.remote_write 
to export them to Mimir. As always, reload config.alloy after any changes. The command is in 
your repo. Run it and wait for the config reloaded message before moving on. Next, we'll verify that 
we've successfully exposed, scraped, processed, and exported metrics to Mimir. To do so, go to 
your series repo. Scroll down to the verification section. Click on the link here and select section 
3 verification. You should see the dashboard filling with Postgres metrics. And notice the 
instance label now just shows the host and port without the postgresql:// prefix. In this episode, 
we covered how we can expose, collect, process, and export infrastructure metrics with Alloy. 
Next up, we'll explore how to use the Alloy UI to debug pipelines we've built. Thank you for 
watching. I'll catch you in the next episode.

