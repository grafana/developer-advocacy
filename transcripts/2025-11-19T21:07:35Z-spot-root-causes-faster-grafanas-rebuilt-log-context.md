# Spot Root Causes Faster: Grafana’s Rebuilt Log Context

Published on 2025-11-19T21:07:35Z

## Description

Grafana's Log Context now integrates the redesigned logs panel, full filtering, and a customizable window (100 ms–2 h). Tweak ...

URL: https://www.youtube.com/watch?v=SIxzQRS8ZB0

## Summary

In this video, Matias from the Observability Logs Squad introduces the new iteration of the Log Context component, designed to enhance log analysis by displaying logs occurring before and after a specified logline. This feature is particularly useful for users who want to contextualize interesting log entries after applying multiple filters. The updated Log Context integrates new logs visualization and includes filtering controls, along with a customizable time window ranging from 100 milliseconds to two hours. It maintains its previous functionalities, such as customizing queries with Loki and centering log lines around a reference log.

## Chapters

00:00:00 Introductions by Matias  
00:00:15 Overview of the new log context component  
00:00:30 Explanation of the log context feature  
00:00:45 Importance of viewing logs before and after a specific logline  
00:01:00 Integration of new logs visualization  
00:01:15 Overview of filtering and visualization controls  
00:01:30 Introduction of the new time window customization control  
00:01:50 Options for time window selection (100ms to 2 hours)  
00:02:05 Features maintained from previous versions  
00:02:20 Customizing underlying queries when using Loki  

Hi, I am Matias from the Observability Logs Squad, and I wanted to show you the new Log Context component. 

This is a new iteration on the Log Context feature, which displays logs occurring before and after a given log. This is particularly helpful when, after applying multiple filters, you find an interesting log line and want to see what happened around the time that log line occurred. 

In this new version of Log Context, we integrated the new logs visualization, including all the filtering and visualization controls that are available elsewhere. Additionally, we added a new control that allows you to customize the time window before and after the reference log. You can select a time range between **one hundred milliseconds** and **two hours**. 

Furthermore, the component maintains the features it has always had. For example, if you're using Loki, you can use this component to customize the underlying query by adding and removing filters. There is also a button that allows you to center your log lines around the reference log. 

That's all. Thank you for listening!

## Raw YouTube Transcript

Hi, I am Matias from the
Observability Logs Squad, and I wanted to show you the
new log context component. This is a new iteration on
the Log Context feature, which shows you logs occurring
before and after a given log. This is helpful when after
applying multiple filters, you find an interesting logline and you
want to see what happened around the time that particular logline occurred. In this new version of Log Context, we integrated the new logs
visualization and including all the filtering and visualization
controls that it has elsewhere. And additionally, we added a new control to customize
the time window before and after the reference log. You can select between a hundred
milliseconds and two hours. After that, the component maintains
the features that it always had. For example, if you're using Loki, you can use this component on
top to customize the underlying query, adding and removing filters. And you have this button if you want
to center your log lines around the reference log. So that's
all. Thank you for listening.

