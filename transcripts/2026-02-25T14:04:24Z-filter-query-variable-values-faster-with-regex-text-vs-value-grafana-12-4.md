# Filter Query Variable Values Faster with Regex (Text vs Value) | Grafana 12.4

Published on 2026-02-25T14:04:24Z

## Description

Query variables can return a lot of values—when you only need a subset, regex filtering is the go-to move. The problem: ...

URL: https://www.youtube.com/watch?v=Czfh1u13xfw

## Summary

In this video, the presenter introduces a new feature related to a demo dashboard that showcases improved functionality with variable filtering. The key focus is on the region variable, which previously had limitations with Regex filters applying to underlying IDs instead of display text. The new feature allows users to choose whether the Regex filter applies to the value or the display text, making it easier to filter the relevant data directly in the user interface. The presenter aims to highlight how these updates enhance usability and provide a more intuitive experience for users.

## Chapters

00:00:00 Introductions  
00:00:30 Demo of new feature  
00:01:00 Overview of the demo dashboard  
00:01:30 Explanation of the region variable  
00:02:00 Importance of filtering values  
00:02:30 Update on Regex filter functionality  
00:03:00 Filtering applied to value vs. display text  
00:03:30 User interface improvements for Regex filters  
00:04:00 Demonstration of applying the new filter  
00:04:30 Closing remarks and hope for usefulness  

Hi everyone,

I wanted to quickly show a new feature we've built. This is a demo dashboard we created to showcase it. 

As you can see, we have a couple of variables up here and a few panels that depend on them. Let's take a closer look at the **region variable**. It returns quite a few values, but in many cases, we are only interested in a subset of them. So, let's go ahead and update it.

Previously, when using the **Regex filter**, the filter was applied to the value, not the display text. Since the UI shows the text alongside the underlying IDs, this made it difficult to apply Regex filters. There wasn't an easy way to know which IDs to target. 

Now, you can choose whether Regex is applied to the value or to the text. By selecting **text**, the filters apply directly to what's visible in the UI.

Now, let's go back to the dashboard. There we go! Hope you find this helpful.

## Raw YouTube Transcript

Hi everyone. I wanted to quickly
show a new feature we've built. This is a demo dashboard we created
to showcase it. As you can see, we have a couple of variables up here
and a few panels that depend on them. Let's take a closer look
at the region variable. As you can see, it returns
quite a few values, but in many cases we are only
interested in a subset of them. So let's go ahead and
update it. Previously, when using the Regex filter, the
filter was applied to the value, not the display text. Since the UI shows the text
another underlying IDs, these made it difficult
to apply Regex filters. There wasn't an easy way to
know which IDs to target. Now you can choose whether Regex is
applied to the value or to the text. By selecting text, the filters apply
directly to what's feasible in the UI. Now, let's go back to the
dashboard. There we go. Hope you find this helpful.

