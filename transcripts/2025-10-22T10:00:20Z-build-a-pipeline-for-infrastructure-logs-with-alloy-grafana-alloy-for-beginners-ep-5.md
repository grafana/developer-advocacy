# Build a Pipeline for Infrastructure Logs with Alloy | Grafana Alloy for Beginners Ep 5

Published on 2025-10-22T10:00:20Z

## Description

Collecting, processing, and exporting infrastructure logs with Grafana Alloy is as easy as 1-2-3! Join Lisa Jung and Mischa ...

URL: https://www.youtube.com/watch?v=FFtvoc6iQVE

## Summary

In this episode of the Grafana Alloy for Beginners series, Lisa Jung, a Staff Developer Advocate at Grafana, guides viewers through the process of collecting, processing, and exporting infrastructure logs using Alloy. Building on previous episodes, she emphasizes the importance of having a configured learning environment before diving into the content. Key points include using the logging block to customize log formats and levels, applying the loki.relabel component to add labels to logs, and exporting logs to a local Loki database using the loki.write component. Lisa also discusses the sequence of relabeling rules and the necessity of reloading the configuration after changes. To verify successful log collection and processing, she demonstrates how to utilize a pre-configured Grafana dashboard. The episode concludes with a preview of upcoming content focused on infrastructure metrics.

## Chapters

Sure! Here are the 10 key moments from the livestream with their respective timestamps:

00:00:00 Introductions and overview of the episode  
00:01:30 Reminder to watch previous episodes and set up the learning environment  
00:02:10 Overview of the series repository and configuration file  
00:03:00 Explanation of the logging block for collecting logs  
00:04:00 Setting log format to logfmt and level to debug  
00:05:30 Introduction to the loki.relabel component for filtering logs  
00:06:45 Adding labels (group and service) to logs using rules  
00:08:00 Overview of the loki.write component for exporting logs to Loki  
00:09:30 Recap of the steps taken in section one  
00:10:45 Instructions for reloading the config and verifying logs in Grafana  

# Grafana Alloy for Beginners - Episode 5

Hey there! Welcome back to the Grafana Alloy for Beginner series. I'm Lisa Jung, a Staff Developer Advocate here at Grafana. 

Last time, we set up our learning environment. Today, we're diving into **collecting, processing, and exporting infrastructure logs** using Alloy. Before we begin, make sure you've watched episodes one through four and set up your learning environment. That way, you're all set to follow along. Afterwards, head over to the series repo; the link is in the video description. 

Scroll down to **section one, Build a Pipeline for Infrastructure Logs with Alloy**. If you haven't already, start up the learning environment and open the `config.alloy` file. We went over how to do that in the last episode. 

## Overview of the Process

Each section begins with the starter code, followed by tasks explaining what the configuration does and the information you'll need. Finally, there's a solution that you can expand to see the complete config. To keep this episode short and sweet, I'll walk you through the final config instead of typing it out. You can copy the starter code into your `config.alloy`, try building the config yourself, then check the solution to see if you nailed it. 

In section one, we'll learn how to **collect, process, and export infrastructure logs** using Alloy. We will be collecting logs from Alloy itself by using the logging block. Here's what we'll do:

1. **Add labels** to the logs with the `loki.relabel` component.
2. **Export** the logs to Loki, the log database, using the `loki.write` component.

On screen, you'll see my `config.alloy` file with the final pipeline for infrastructure logs. Let's break this down.

By default, Alloy automatically generates its own logs. We'll use a logging block to customize how those logs are created, like setting the log format and log level. In our config, we set the format to `logfmt` and the log level to `debug`, which means that we'll capture all logs, including debug level ones. You probably wouldn't do this in production since it can get noisy, but for this series, it helps us see logs flowing in real time. 

After that, we'll send the logs to the receiver of the `loki.relabel.alloy_logs` component, which we'll define next.

## Understanding the Components

### Loki Relabel

This component is most commonly used to filter log entries or to standardize labels that get passed onto one or more downstream receivers. In our case, we'll be using the rule block to add the label **group** set to **infrastructure**. We will use another rule block to add another label called **service** set to **alloy**. Just a heads up: these rules run in the order they're written, so pay attention to the sequence.

Now, anytime we do something to our data, chances are we'll want to send it somewhere else afterward. In our case, that destination is the `loki.write.mythical` component. To specify that, we'll use a `forward_to` argument and send the relabeled logs to the receiver of the `loki.write.mythical` component. This component receives the processed logs from the `loki.relabel` component and exports the logs to our locally running Loki database. 

We do that by using the endpoint block and setting the URL to the destination we want to send the data to. In the repo, we've included the URL for our local Loki instance, so just copy and paste it right here. 

## Recap

Alright, let’s do a recap. In section one, we:

- Used a logging block to configure Alloy's logging format and level.
- Used the `loki.relabel` component to add the group and service labels to incoming logs.
- Used the `loki.write` component to export logs to Loki.

On my screen, we have the series repo. If you ever want to double-check your work or see the finished version of a section, you can expand the solution and check your config.

### Reloading the Config

Now, whenever we make changes to the Alloy config, we need to reload it. To do that, hit the reload endpoint either in your browser or using a tool like `curl`. We'll copy this command and open our terminal. Make sure you're in the project directory, paste, and run the `curl` command. If everything looks good, we'll see a **config reloaded** message confirming it worked.

## Verification

Now, let's make sure everything's working as expected: that our logs are being collected, processed, and sent to Loki. The good news is our learning environment already includes a pre-configured Grafana dashboard, so we can easily visualize the logs stored in Loki. 

To get there, scroll down to the verification section of the repo. Then click on the link to the dashboards. Once you get there, click on **section 1 verification**. Now you'll see the logs coming in, and if you expand one of the log lines, you'll see the labels that we've added to the logs called **group** set to **infrastructure** and **service** set to **Alloy**.

In this episode, we walked through how to collect, process, and export infrastructure logs with Alloy. In the next two episodes, we'll learn how to build pipelines for infrastructure metrics. 

Thanks for watching! I'll see you in the next episode.

## Raw YouTube Transcript

Hey there. Welcome back to the Grafana Alloy 
for Beginner series. I'm Lisa Jung, a Staff Developer Advocate here at Grafana. Last time 
we set up our learning environment. Today we're diving into collecting, processing, and exporting 
infrastructure logs using Alloy. Before we begin, make sure you've watched episodes one through four 
and set up your learning environment. That way you're all set to follow along. Afterwards, head 
over to the series repo. The link is in the video description. Scroll down to section one, Build 
a Pipeline for Infrastructure Logs with Alloy. If you haven't already, start up the learning 
environment and open the config.alloy file. We went over how to do that in the last episode. 
Now each section begins with the starter code, followed by tasks explaining what the 
configuration does and the information you'll need. Finally, there's a solution that 
you could expand to see the complete config. To keep this episode short and sweet, I'll walk 
you through the final config instead of typing it out. You can copy the starter code into your 
config.alloy, try building the config yourself, then check the solution to see if you nailed 
it. In section one, we'll learn how to collect, process, and export infrastructure logs using 
Alloy. We'll be collecting logs from Alloy itself by using the logging block. Add labels to the logs 
with the loki.relabel component. Export the logs to Loki, the log database using the loki.write 
component. On screen, you'll see my config.alloy file with the final pipeline for infrastructure 
logs. So let's break this down. By default, Alloy automatically generates its own logs. 
We'll use a logging block to customize how those logs are created, like setting the 
log format and log level. In our config, we set the format to logfmt, and we'll set 
the log level to debug, which means that we'll capture all logs including debug level ones.
You probably wouldn't do this in production since it can get noisy, but for this series, 
it helps us see logs flowing in real time. After that, we'll send the logs to the receiver 
of the loki.relabel.alloy_logs component, which we'll define next. Let's move on to loki.relabel. 
This component is most commonly used to filter log entries or to standardize labels that get 
passed onto one or more downstream receivers. In our case, we'll be using the rule block 
to add the label group set to infrastructure. Use another rule block to add another label called 
service set to alloy. Just a heads up, these rules run in the order they're written, so pay attention 
to the sequence. Now, anytime we do something to our data, chances are we'll want to send it 
somewhere else afterward. In our case, that destination is loki.write.mythical component.
To specify that, we'll use a forward_to argument and send the relabeled logs to the receiver 
of the loki.write.mythical component. This component receives the process logs from the 
loki.relabel component. Then export the logs to our locally running Loki database. We do that 
by using the endpoint block and setting the URL to the destination we want to send the data to. 
In the repo. We've included the URL for our local Loki instance, so just copy and paste it right 
here. Alright, let's do a recap. In section one, we use a logging block to configure Alloy's 
logging format and level. Then we used the loki.relabel component to add the group and 
service labels to incoming logs. Then we used the loki.write component to export logs to 
Loki. On my screen, we have a series repo. If you ever want to double check your work or 
see the finished version of a section, you can expand the solution and check your config.
Let's scroll down to Reloading the config section. Now, whenever we make changes to the 
Alloy config, we need to reload it. To do that, hit the reload endpoint either in your browser or 
using a tool like curl. We'll copy this command and open our terminal. Make sure you're in the 
project directory. Paste and run the curl command. If everything looks good, we'll see a config 
reloaded message confirming it worked. Now, let's make sure everything's working as expected: 
that our logs are being collected, processed, and sent to Loki. The good news is our learning 
environment already includes a pre-configured Grafana dashboard, so we can easily visualize the 
logs stored in Loki. To get there, scroll down to the verification section of the repo. Then click 
on the link to the dashboards. Once you get there, click on section 1 verification. Now you'll see 
the logs coming in, and if you expand one of the log lines, you'll see the labels that we've added 
to the logs called group set to infrastructure and service set to Alloy. In this episode, 
we walked through how to collect, process, and export infrastructure logs with Alloy. In 
the next two episodes, we'll learn how to build pipelines for infrastructure metrics. Thanks for 
watching. I'll see you in the next episode.

