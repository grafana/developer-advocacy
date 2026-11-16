# New in Pyroscope: Call Tree view, Exemplars, and the gcx CLI

Published on 2026-11-12T22:19:45Z

## Description

Explore new Pyroscope features: the Call Tree view and Exemplars in Grafana, then find the same exemplars with gcx, the Grafana CLI, by hand or with an AI agent. Follow along on Grafana Play at https://play.grafana.org.

Timestamps:
0:00 Intro
0:15 Call tree view vs. flame graph and top table
2:16 Exemplars in Profiles Drilldown
2:59 Find exemplars with GCX
4:00 Use GCX with an AI coding agent

Links/resources:
Get started with the Grafana Cloud forever-free tier: https://grafana.com/g/cloud
Have a question? Ask Grot, your AI helper: https://grafana.com/grot/
Reach out in our community forums: https://gra.fan/communityyf
[Add Pyroscope/GCX docs and blog links]

Thanks for watching!

#Grafana #Observability #Pyroscope #ContinuousProfiling #GCX #Exemplars

---
Thanks for watching! 

👍 Was this video helpful? Like and subscribe to our channel for more videos.

Connect with Grafana Labs: 
X: (https://www.twitter.com/grafana)   
LinkedIn: (https://www.linkedin.com/company/grafana-labs/)
Facebook: (https://www.facebook.com/grafana)

#Grafana #Observability

URL: https://www.youtube.com/watch?v=NlBwPm-_1s0

## Summary

The show titled "New in Pyroscope: Call Tree view, Exemplars, and the gcx CLI" was published on November 12, 2026. The discussion featured new features in Pyroscope, including the Call Tree view and Exemplars, as well as how to utilize the Grafana CLI (gcx) to find exemplars. Key takeaways included the advantages of the Call Tree view for navigating profiling data, the role of Exemplars in visualizing individual profiles, and the integration of gcx with AI agents for enhanced data querying. The session emphasized the importance of these tools in improving observability and profiling efficiency.

Topics: Pyroscope, Call Tree view, Exemplars, Grafana CLI, gcx, Observability

## Chapters

00:00:00 Discussion
00:01:37 Discussion
00:03:10 Using GCX to find exemplars and profiles

Pyroscope has new ways to look at your profiling data. Let's explore the **call tree view** and **exemplars** in Grafana, and then see how to find the same exemplars in **gcx**, the Grafana CLI, either by running the commands yourself or by asking an AI agent. We'll use Grafana Play so you can follow along at [play.grafana.org](https://play.grafana.org).

Let's start with the **call tree view**. To see where it helps, let's first look at the checkout service in the views you might already know. On the left is the **top table**, and on the right is the **flame graph**. The flame graph shows which code paths use the most resources. Each block represents a function, and the wider it is, the more resources it uses. The top table lists each function once, allowing you to see which functions use the most resources overall.

We added the call tree view to make it easier to navigate your profiling data. It shows the same data as an expandable tree, so you can follow a call path one step at a time and see where a function is called from. Each row is a function, and when we expand it, we see the functions it calls. Here, we can see that about half of the checkout service's CPU time is spent in **place order** and the functions it calls.

Now let's compare **search** in the top table and the flame graph. In the flame graph, it's visible in just a few places. Now let's take a look at the same search in the call tree view. We can see that it finds more than 50 places where this function shows up. The top table only lists the function once, and in the flame graph, it's easy to miss the narrow blocks. Here we can use the arrows under the search box to go through each one. This looks related to garbage collection. We'd normally use memory profiles to look into garbage collection, so let's take a look at something else. 

Let's go for this **regex** one instead. That's a lot of regex functions. Go's regex code is recursive, so the tree keeps going. Let's go up the tree to see where it's being called from. Here, we find more regex functions, and we see that some are actually coming from the checkout service's own code and not a library. We have **validate order** with regex, and above that is **process order** and **place order**, which we saw earlier. At this point, we would go and look at the code to see how it's using the regex.

The call tree can also be useful to list all callers of a function. This is the equivalent to the upper half of the sandwich view but can be more readable since callers are listed in the table. The flame graph combines the profiles from every instance of the service over the time range, so a single busy process can be hard to spot.

**Exemplars** are individual profiles. In the Grafana UI, they show up as markers on the time series plotted at each profile's value. In **Profiles Drilldown**, they're on by default in the flame graph and labels views. Let's go and open one of the low ones first. We can see its profile ID, value, and labels. Then we can click **view profile**. Now the flame graph will only show that one profile, and we can see that there's a lot less going on.

Now let's go and take a look at one of the high ones. We can see that this profile is mostly regex, like we were seeing earlier. You can also go to **Explore**, and if we go to the options here, we can turn on exemplars. So far, we've been in the Grafana UI. We can also find these same exemplars from the terminal or with an AI agent using **gcx**.

**gcx**, the Grafana CLI, gives you and your AI coding agent access to your Grafana instance, including your profiles. Let's point gcx at the same Grafana Play instance we were just looking at by adding a Play context with its server URL and org ID. The gcx context uses the Play context for commands in this terminal without changing your default context. 

Let's use `gcx profiles exemplars` to list the 10 most expensive individual profiles for checkout service from the last hour. We'll also use the Play profiles data source, **Grafana Cloud profiles**. We can see that the most expensive individual profiles for checkout service are listed with the highest ones first. We can pass one of these profile IDs to `gcx profiles query` to see the top functions in just that profile. In here, we can see the regex and garbage collection functions near the top that we saw earlier.

gcx also works with AI coding agents and turns on agent mode automatically in many of them, like **Claude Code**. In agent mode, gcx returns JSON that the agent can read directly. Let's ask the agent to find the most expensive CPU profile for checkout service. We can see it ran `gcx profiles exemplars` and `gcx profiles query`. Like we saw earlier, most of the CPU time in that profile goes to regex and garbage collection.

Check out the blog, the docs, and the Pyroscope community calls to learn more about the call tree, exemplars, and gcx.

## Raw YouTube Transcript

Pyroscope has new ways to look at your profiling data. Let's look at the call tree view and exemplars in Grafana and then how to find the same exemplars in gcx, the Grafana CLI, either by running the commands yourself or by asking an AI agent. We'll use Grafana Play so you can follow along at play.grafana.org. Let's start with the call tree view. To see where it helps, let's first look at the checkoutservice in the views you might already know. On the left is the top table and on the right is the flame graph. The flame graph shows which code paths use the most resources. Each block is a function and the wider it is, the more resources it uses. The top table lists each function once so you can see which functions use the most resources overall. We added the call tree view to make it easier to navigate your profiling data. It shows the same data as an expandable tree so you can follow a call path one step at a time and see where a function is called from. Each row is a function and when we expand it, we see the functions it calls. Here we can see that about half of the checkoutservice's CPU time is spent in place order and the functions it calls. Now let's go ahead and compare search in the top table and the flame graph. In the flame graph, it's visible in just a few places. Now let's take a look at the same search in the call tree view. So we can see that it finds more than 50 places where this function shows up. The top table only lists the function once and in the flame graph, it's easy to miss the narrow blocks. Here we can use the arrows under the search box to go through each one. This looks related to garbage collection. We'd normally use memory profiles to look into garbage collection, so let's take a look at something else. Let's go for this regex one instead. That's a lot of regex functions. Go's regex code is recursive, so the tree keeps going. Let's go up the tree to see where it's being called from. So here's a bunch more regex and then here we are finding things that are actually coming from the checkoutservice's own code and not a library. So we have the validate order with regex and above that is process order and place order which we saw earlier. At this point, we would go and look at the code to see how it's using the regex. The call tree can also be useful to list all callers of a function. This is the equivalent to the upper half of the sandwich view, but can be more readable since callers are listed in the table. The flame graph combines the profiles from every instance of the service over the time range, so a single busy process can be hard to spot. Exemplars are individual profiles. In the Grafana UI, they show up as markers on the time series plotted at each profile's value. In Profiles Drilldown, they're on by default in the flame graph and labels views. Let's go and open one of the low ones first. We can see it's profile ID, value, and labels. Then we can click view profile. And now the flame graph will only show that one profile, and we can see that there's a lot less going on. Now let's go and take a look at one of the high ones. So we can see that this profile is mostly regex like we were seeing earlier. You can also go to Explore. And if we go to the options here, we can go and turn on exemplars. So far we've been in the Grafana UI. We can also find these same exemplars from the terminal or with an AI agent using gcx. gcx, the Grafana CLI, gives you and your AI coded agent access to your Grafana instance including your profiles. Let's point gcx at the same Grafana plate instance we were just looking at by adding a plate context with its server URL and org ID. gcx context uses the plate context for commands in this terminal without changing your default context. Let's use gcx profiles exemplars to go and list the 10 most expensive individual profiles for checkoutservice from the last hour. We'll also use the Play profiles data source Grafana Cloud profiles. We can see that the most expensive individual profiles for checkoutservice are there listed with the highest ones first. We can go and pass one of these profile IDs to gcx profiles query to see the top functions in just that profile. In here we can see the regex and garbage collection functions near the top that we saw earlier. gcx also works with AI coding agents and turns on agent mode automatically in many of them like Claude Code. In agent mode, gcx returns JSON that the agent can read directly. Let's ask the agent to find the most expensive CPU profile for checkoutservice. We can see it ran gcx profiles exemplars and gcx profiles query. Like we saw earlier, most of the CPU time in that profile goes to regex and garbage collection. Check out the blog, the docs, and the Pyroscope community calls to learn more about the call tree, exemplars, and gcx.

