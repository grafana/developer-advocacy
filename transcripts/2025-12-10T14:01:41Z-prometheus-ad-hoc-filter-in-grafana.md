# Prometheus Ad hoc filter in Grafana

Published on 2025-12-10T14:01:41Z

## Description

Learn about the new Ad-hoc filter for Prometheus Data source in Grafana as Carl Bergquist shows how it works. Watch the ...

URL: https://www.youtube.com/watch?v=t3XeC0AWWmA

## Summary

In this video, the presenter discusses a new filtering feature in Grafana for Prometheus, highlighting its ability to dynamically load times or labels for filtering purposes. This update allows users to see only relevant labels for the time series in their dashboards, in contrast to the previous version that displayed an overwhelming number of options. The presenter demonstrates how the filtering works, emphasizing its compatibility with keyboard navigation and the progressive narrowing of options as users drill down into the time series. The main points of the video focus on improving user experience and data relevance in Grafana's ad hoc variable feature.

## Chapters

00:00:00 Introduction to the new filtering feature in Grafana  
00:01:15 Dynamic loading of times and labels for filtering  
00:02:30 Explanation of how labels are displayed based on existing time series  
00:03:45 Improved user experience with keyboard navigation  
00:04:10 Limiting options to relevant ones from the data source  
00:05:20 Comparison to previous version of ad hoc variables  
00:06:00 Benefits of drilling down to time series with fewer options  
00:07:30 Demonstration of filtering in action  
00:08:15 User feedback and usability improvements  
00:09:00 Conclusion and future enhancements in Grafana

With a new filtering feature in Grafana for Prometheus, we dynamically load the times or the labels you can filter by. When you click on this, we determine which labels actually exist for the time series in the dashboard. We then only show them as options here, as opposed to the thousands of labels that were previously suggested.

When you select one of these options, by the way, all of them work really well with the keyboard. So, I'm going to use the keyboard for this demonstration. When you pick one of these options, your choices will be limited to those that actually exist in the primary data source. 

In the previous version of ad hoc variables, it pulled all of the different options instead of just the ones that are truly relevant for you. As you continue to drill down into the time series, you will notice that the number of options decreases. This makes the filtering process more efficient and user-friendly.

## Raw YouTube Transcript

With a new filtering feature in Grafana for Prometheus, we load the times or the labels you can filter by dynamically. So when you click on this, we figure out what labels actually exist for the time series in the dashboard. And then we only show them as options here instead of the thousands of labels that was earlier suggested. And when you pick one of these, by the way, all of these works really well with the keyboard as well. So I'm just gonna use the keyboard. When you pick one of these, your options is also going to be limited to the options that really exist in the primitive data source. And in the previous version of ad hoc variables, it pulled all of the different options instead of just the one that is really relevant for you. And when you keep drilling down to the time series like this, you also get fewer and fewer options. So this

