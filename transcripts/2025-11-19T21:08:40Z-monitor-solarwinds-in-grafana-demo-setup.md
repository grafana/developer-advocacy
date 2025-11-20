# Monitor SolarWinds in Grafana: Demo + Setup

Published on 2025-11-19T21:08:40Z

## Description

Matt from Grafana's Enterprise Data Sources team demos the SolarWinds plugin: URL/credentials setup, TLS options, health ...

URL: https://www.youtube.com/watch?v=JrXP0WNWpD4

## Summary

In this video, Matt from the Enterprise Data Sources Team introduces SolarWinds, a network and infrastructure monitoring platform. He explains how to configure the SolarWinds data source, highlighting essential fields such as URL, username, and password, as well as optional TLS settings. Matt demonstrates how to ensure the configuration is working by saving and testing the connection, and presents built-in dashboards like "SolarWinds top 10" and "SolarWinds Alerts." He discusses the use of SWQL queries to retrieve data and encourages viewers to refer to SolarWinds documentation for additional information. The video serves as a guide for setting up and utilizing SolarWinds within their enterprise data sources.

## Chapters

Here are the key moments from the livestream along with their timestamps:

00:00:00 Introduction to SolarWinds  
00:01:15 Overview of the SolarWinds data source configuration  
00:02:00 Required fields for configuration: URL, username, password  
00:03:00 Optional TLS settings and health check  
00:03:45 Introduction to built-in dashboards: SolarWinds top 10 and Alerts  
00:04:15 Exploring the SolarWinds top 10 dashboard  
00:05:00 Explanation of panels in the dashboard  
00:05:45 Discussion on SWQL queries and their usage  
00:06:30 Resources for learning more about SWQL  
00:07:00 Conclusion and additional resources for SolarWinds data source

# Introduction to SolarWinds Data Source

Hi, I am Matt from the Enterprise Data Sources Team, and I'm here today to talk to you about a new enterprise data source: **SolarWinds**. SolarWinds is a network and infrastructure monitoring platform that provides tools to monitor and manage network performance, server health, and application availability.

## Data Source Configuration

Let's start by taking a look at the data source configuration page. Once we open the SolarWinds data source, we can see there are a few required fields:

1. **URL**: This would be the URL of your SolarWinds instance.
2. **Username and Password**: These would be the same credentials that you use to log in to your SolarWinds instance.
3. **Optional TLS Settings**: If they apply to your instance, you can check the appropriate checkbox below.

Finally, we can ensure that our health check is passing by clicking **Save and Test**.

## Built-in Dashboards

We have also provided a couple of built-in dashboards: **SolarWinds Top 10** and **SolarWinds Alerts**. Let's go ahead and take a look at the SolarWinds Top 10 dashboard.

In this dashboard, we can see there are a few panels. The first one shows the top 10 volumes by space used. We can click on the edit button to get more information about how we created this dashboard. 

In the **SWQL Query** section, we can input an SWQL query and display the results above. Currently, we only support this SWQL query for displaying SolarWinds information. If there are other feature requests, we are happy to accept those and possibly work on them in the future.

## Additional Resources

If you want more information on SWQL, you can refer to the SolarWinds documentation. Here's an example that shows a few simple SWQL queries. You could also go to your SolarWinds instance and look at the **Hubble** section, which is usually found at the top of the page. Once you click that, it shows a few different queries that you’ve run on your instance, which you can use as a starting point.

That's all we have for now on the SolarWinds data source. If you want more information on this data source, you can check our **Grafana documentation** on the SolarWinds data source plugin.

Thank you!

## Raw YouTube Transcript

Hi, I am Matt from the
Enterprise Data Sources Team, and I'm here today to talk to you
about a new enterprise data source: SolarWinds. SolarWinds is a network and infrastructure
monitoring platform that provides tools to monitor and manage
network performance, server health, and application availability. Let's start with taking a look at
the data source configuration page. Once we open up the
SolarWinds data source, we can see there are a few required
fields. The first one is URL. This would be the URL of
your SolarWinds instance. Next we have username and password. These would be the same credentials that
you use to log in to your SolarWinds instance. And finally, we have
some optional TLS settings. If they apply to your instance, then you can check the appropriate
checkbox down below. Finally, we can make sure that our health check
is passing by clicking save and test. We have also provided a couple
of built-in dashboards here. We have SolarWinds top
10 and SolarWinds Alerts. Let's go ahead and take a look
at some of those dashboards. We'll take a look at SolarWinds top 10. So here we can see there are a
few panels in this dashboard. The first one is showing top
10 volumes by space used. We can click on the edit button and get
a little more information about how we created this dashboard. We can see here that we have the
SWQL query section where we can put an SWQL query and we can
display the results up above. Currently we're only supporting this
SWQL query for displaying SolarWinds information. If there are
other feature requests, we're happy to accept those and
possibly work on in the future. If you want some more information on SWQL, you can get that from the
SolarWinds documentation. Here's an example that shows
a few simple SWQL queries. You could also go to your SolarWinds
instance and look at the Hubble section, which is usually here at the top
page, and once you click that, it shows a few different queries
that you've ran on your instance, so you can use that as a starting point. That's all we have for now on
the SolarWinds data source. If you want more information
on this data source, you can look at our Grafana documentation
on the SolarWinds data source plugin. Thank you.

