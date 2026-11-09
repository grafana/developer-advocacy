# How to view dashboard JSON diff when using Grafana Assistant  | AI

Published on 2026-09-23T11:30:09Z

## Description

When using AI, you do need to see what changes had been made whether it is code, text or command. Grafana Assistant do ...

URL: https://www.youtube.com/watch?v=h_6a1brsCmk

## Summary

The show is titled "How to view dashboard JSON diff when using Grafana Assistant | AI," published on September 23, 2026. The speaker discusses the capabilities of Grafana Assistant in identifying and fixing issues within Grafana dashboards, specifically focusing on how it can automatically detect missing metrics and ensure all panels reference the correct variables. Key features highlighted include the assistant's ability to edit panels, provide visibility into changes made through a diff view, and streamline the dashboarding process without manual intervention. The session emphasizes the efficiency and automation that Grafana Assistant brings to managing dashboards.

Topics: Grafana Assistant, dashboard JSON diff, metrics, automation, panel editing.

## Chapters

00:00:00 Using Grafana Assistant to fix dashboard panel issues
00:01:32 Viewing changes made by Grafana Assistant
00:02:21 Understanding the dashboard JSON diff in Grafana Assistant

The panel has no data. Let's see if it's able to figure this out. Now it's reading the panel. You can also see all the tool calls, all the things that it's trying to do to figure out what it's asked to do. Now it's searching the data source and pulling the metrics. It says that the metric I'm referencing in this panel doesn't exist, and the name of the metric is actually different. So it's suggesting how we can fix it. 

Let's fix it. Now the assistant is switching to the dashboarding mode. It knows that it's a dashboarding task, so it brings in the right tools for it. It's editing the panel, and now the data is back. It was so quick; I didn't have to do anything manually. 

Before we get into the features, I also want to make sure that all the panels I have on this dashboard reference this variable. Let's ensure every panel references this variable. In this case, instead of telling the assistant exactly what to fix, I'm pointing it at one thing and just letting it sort it out. I'm not specifying which panel is wrong or where to look; it's just going to read queries for all these panels and figure out if any of them are missing the reference. 

At the bottom of the dashboard, we also have this little panel for logs. It's a different data source, and the system needs to read the metrics names and figure out how to reference the variable correctly. Nice, so now it's thinking. It should have all the metrics names by now. Yes, it's editing the panels. There are quite a few that are not referencing that variable, so we can see all the calls it's making. 

Another nice feature that I really like is that we added it pretty recently. You can see the diff, which shows exactly what the assistant changed. This gives you visibility into what the system is doing for you. For example, if we look into these two tool calls, one of the metric names for the Prometheus panel is a Kubernetes namespace name and for Loki's namespace. The system was able to read it and figure it out by itself. 

This diff panel view is basically the dashboard JSON, or is it different? Yes, it's pretty much the diff that's going into your dashboard JSON, into the dashboard spec.

## Raw YouTube Transcript

panel has no data. Let's see if it's able to figure this out. So now it's reading the panel. You can also see all the tool calls, all the things that it's trying to do to figure out what it's asked to do. Now it's searching the data source, pulling the metrics. And yeah, so it says that the metric that I'm referencing in this panel doesn't exist. And the name of the metric is actually different. So it's suggesting how we can fix it. Let's fix it. Yeah, now the assistant is switching to the dashboarding mode. It knows that it's a dashboarding task, so it brings in the right tools for it. So it's editing the panel, and now the data is back. And yeah, it was so quick. I didn't have to do anything manually. And another thing, again, before we get into the features, I also want to make sure that all the panels that I have on this dashboard, they reference this variable. So let's say make sure every panel references this variable. So in this case, instead of telling the assistant exactly what to fix, I'm pointing it at one thing and just let it sort it out. So I'm not telling which panel is wrong, where to look at. It's just going to read queries for all these panels and figure out if any of those is missing the reference. And we also have at the bottom of the dashboard, we also have this little panel for logs. So it's a different data source. And the system needs to read the metrics names and figure out how to reference the variable correctly. Nice, so now it's thinking. It should have all the metrics names by now. And yeah, it's editing the panels. There's quite a few that are not referencing that variable. So we can see all the calls that it's making. And another nice feature that I really like, it's there. We added it pretty recently. But you can see the D if you can see what exactly the assistant changed. So you get visibility into what the system is doing for you. So for example, if we look into these two tool calls, one of the matrix names for the Prometheus panel is a Kubernetes namespace name and for Lockheed's namespace. So the system was able to read it and figure it out by itself. And this diff panel view is basically the dashboard JSON or is it different? Yeah, it's pretty much the div that's going into your dashboard JSON, into the dashboard spec, yes.

