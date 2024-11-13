# Beginners Guide - How to Configure a Heatmap Visualization | Grafana

How is a heatmap different from a histogram visualization, and how do you configure one? Join Senior Developer Advocate Marie ...

Published on 2024-04-18T09:00:31Z

URL: https://www.youtube.com/watch?v=SGWBzQ54koE

Transcript: Hi! My name is Marie Cruz, and I’m a Senior 
Developer Advocate at Grafana Labs. In this   beginner-friendly video tutorial, I’ll walk you 
through what heatmaps are and when to use them. By the end of this tutorial, you should also know   how to configure a heatmap to 
visualize your data in Grafana. In one of the previous video tutorials, I spoke 
about histograms. While histograms look at the   value distributions over a specific time range, 
they don’t allow you to see any trends or changes   in the value distribution over a period of 
time. This is where heatmaps can be useful. To understand heatmaps, imagine that you 
have a table full of numbers. It could be   the temperatures recorded for a specific city. 
What if you want to see the hottest and coolest   areas at a glance? A heatmap can take those 
numbers and turn them into different colors.   Hotter areas might be red or orange, while 
cooler areas might be blue or green. So,   with a heatmap, you can quickly see where the 
hotspots are without looking at many numbers. In Grafana, a heatmap is essentially a histogram 
but represented over time. Each time slice or   cell you see here is a histogram on its own. 
Instead of using different bars or buckets,   a heatmap visualizes your data 
as different cells, with each of   the cells representing different colors to 
interpret your data's distribution easily. To help you in this tutorial, I’ll be 
using the Grafana TestData data source,   which comes built-in with Grafana and is 
particularly useful if you are a Grafana beginner. With that explanation out of 
the way, let’s get started! First, I’ll add a new visualization to 
a dashboard, and then I'm going to make   sure that the grafana-testdata-datasource is 
selected. Then, I'm going to select the linear   bucket heatmap data. Under the visualization 
drop-down, I’m going to choose heatmap. One   thing to note about heatmaps in Grafana is 
that they work best with time-series data. To investigate the underlying time 
series data for this scenario,   let’s click query inspector followed by data. Looking at the visualization, the times that you 
see here are displayed on the x-axis. In contrast,   the different columns, which we can imagine 
for now as the temperature, have been displayed   on the y-axis. Each of the values that 
you see here has been plotted as cells. To customize the heatmap, I'm going to add a 
title, first which I will call Temperature. Next, under the heatmap options, there 
is a setting here called calculate from   data. This setting determines if the 
data is already a calculated heatmap   from the data source or one that should 
be calculated in the panel. The linear   bucket heatmap data is already a calculated 
heatmap, so I will leave this option as no. As a recommendation, it’s better to do 
the heatmap calculation during metric   collection or store the data 
in Elasticsearch, Prometheus,   or any other data source supporting 
histogram bucketing on the raw data. To customize the y-axis. I can also add the 
temperature unit and set it to Fahrenheit. Now, since heatmaps use colors, Grafana provides   different color schemes that you can 
choose from. Under the colors options,   you can see different schemes and for this 
tutorial, I’m going to select the reds scheme. To determine the number of colors to 
use, you can configure the steps. So,   for example, if I set this back to 2, you 
can see that there are only two colors   displayed in my heatmap. As I increase the 
number of steps, more shades of red appear. Moving over to the cells, if you want to hide 
specific values, you can provide which values   you want to hide. So, for example, if 
I want to hide any 0 or empty values,   I can set this option to 0, and I'm 
going to see it as a gap in my histogram. Since heatmaps are just histograms 
over time, you also have the option   to show the histogram when you 
hover over any cell. To do so,   under the tooltip option, I’m going to 
toggle the show histogram option. Now,   when I hover over the cells, I can see 
how the histograms change over time. I can also toggle the color scale to represent 
the mapping between the cell value and the color. And there you have it! In this 
beginner-friendly video tutorial,   I’ve shown you how to configure a heatmap 
to visualize your data in Grafana. Check out our documentation 
to learn more about heatmaps,   which you can find in the video description below. I hope you found this video useful, and if you do,   please let us know in the comments 
and as always, happy visualizing!

