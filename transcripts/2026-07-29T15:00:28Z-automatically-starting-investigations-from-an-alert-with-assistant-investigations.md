# Automatically starting investigations from an alert with Assistant Investigations

Published on 2026-07-29T15:00:28Z

## Description

Staff Software Engineer Alexander Sniffin demonstrates how you can use Assistant Investigations to automatically start an ...

URL: https://www.youtube.com/watch?v=v0MBsmP7bbU

## Summary

The show is titled "Automatically starting investigations from an alert with Assistant Investigations," published on July 29, 2026. Staff Software Engineer Alexander Sniffin demonstrates the capabilities of Assistant Investigations, particularly its integration with alerts to automate the initiation of investigations and root cause analyses. Key features discussed include the automatic creation of investigations from alerts, the detailed reporting of findings, and the ability to create loops for ongoing monitoring until issues are resolved. The process for setting up these integrations is straightforward, allowing users to define webhooks and collaborate with teams effectively.

Topics: Assistant Investigations, alerts, root cause analysis, automation, collaboration.

## Chapters

00:00:00 Automatically creating investigations from alerts
00:01:33 Setting up automatic investigations from alerts

One of the most useful features with Assistant Investigations is being able to wire it up to your alerts and your incidents. That way, when one gets triggered, it will automatically create the investigation and start doing a deep root cause analysis into the issue.

Here you can see that we have an active alert that's currently firing for a critical issue. In the timeline on the right, you can see that Assistant Investigations was automatically triggered and posted back with a potential root cause. I can get a high-level summary in this view, but I can also click through and see the investigation in the workspace directly.

Once in the workspace, you can see the conclusion that the investigation came to, but you can also see the reasoning, the steps that it took, the hypotheses that it created, and the evidence that it gathered. Finally, you can see a detailed view of what it actually did. This is a report that gives you a summary, a timeline, the blast radius, and other details or resources that are useful for you to figure out what actually happened.

One thing with the report is that any evidence that it gathers is also cited. So, you can see here that these citations are added into the report. This gives you confidence that whatever is claimed by the investigation is actually backed by real evidence.

Because this investigation was created from an alert, it doesn't always mean that the alert is completely resolved at the point when the investigation finishes. One thing that you can do is actually prompt the agent to create a loop. So, I'm going to ask it to create a loop and to continue monitoring the alert until it's resolved. This will create a loop that runs asynchronously and will continue to look into the issue.

Creating the integration to automatically trigger an investigation based on an alert is actually really simple to do. Come to the Assistant Settings page and under the IRM webhook settings, you can define webhooks that will automatically trigger from an alert group. This lets you set specific integrations, different severity levels, and you can also assign a team. 

If you're working with multiple people to look into a specific issue and you want everyone to have access to that investigation, simply add a team, and this will let you all collaborate and work together. Another option for setting up alerts with investigations is going directly to the alert rule itself. Here, you can find a setting called alert enrichment, and by creating a new enrichment, you can also create an investigation that will automatically trigger for that specific alert.

## Raw YouTube Transcript

One of the most useful features with Assistant Investigations is being able to wire it up to your alerts and your incidents. That way when one gets triggered, it'll automatically create the investigation and start doing a deep root cause analysis into the issue. Here you can see that we have an active alert that's currently firing for a critical issue. And in the timeline on the right, you can see that Assistant Investigations was automatically triggered and posted back with a potential root cause. I can get a high-level summary in this view, but I can also click through and see the investigation in the workspace directly. Once in the workspace, you can see the conclusion that the investigation came to, but you can also see the reasoning, the steps that it took, the hypotheses that it created, and the evidence that it gathered. Finally, you can see a detailed view of what it actually did. This is a report that gives you a summary, a timeline, the blast radius, and other details or resources that are useful for you to figure out what actually happened. One thing with the report is that any evidence that it gathers is also cited. So, you can see here that these citations are added into the report. This gives you confidence that whatever is claimed by the investigation is actually backed by real evidence. So, because this investigation was created from an alert, it doesn't always mean that, you know, the alert is completely resolved at the point when the investigation finishes. So, one thing that you can do is actually prompt the agent to create a loop. So, I'm going to ask it to create a loop and to continue monitoring the alert until it's resolved. This will create a loop that runs asynchronously and will continue to look into the issue. Creating the integration to automatically trigger an investigation based on alert is actually really simple to do. Come to the Assistant Settings page and under the IRM webhook settings, you can define webhooks that will automatically trigger from an alert group. This lets you set specific integrations, different severity levels, and you can also assign a team. So, if you're working with multiple people to look into a specific issue, and you want everyone to have access to that investigation, simply just add a team, and this will let you all collaborate and work together. Another option for setting up alerts with investigations is going directly to the alert rule itself. Here, you can find a setting called alert enrichment, and by creating a new enrichment, you can also create an investigation that'll automatically trigger for that specific alert.

