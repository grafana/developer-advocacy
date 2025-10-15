# Visualize Trends &amp; Future Data Points | Creating Trendlines in Grafana | Grafana 12.1

Published on 2025-07-28T13:57:27Z

## Description

Now available in Grafana 12.1 — regression analysis transformation aka trendlines. This new feature allows you to visualize ...

URL: https://www.youtube.com/watch?v=BQDvxWX0cmw

## Summary

In this video, Kristin Durivage, a software engineer at Grafana, introduces the regression analysis transformation, which has recently been made generally available after being in beta for two years. She explains how to easily apply this transformation within visualization panels using test data, allowing users to map their data to various statistical models. Kristin highlights the flexibility of the transformation, including options to change fields and select polynomial model types with different degrees. She also showcases a regression analysis dashboard that illustrates the functionality with multiple graphs and tables for better understanding. The video encourages viewers to experiment with the transformation on their own datasets.

Hello, I'm Kristin Durivage, a software engineer on the data processing team at Grafana. 

Let's talk about the regression analysis transformation. This transformation was actually introduced two years ago behind a feature flag, and now it is in general release. It's very easy to use. 

In any visualization panel, you can simply use test data, which generates something like this. Under transformations, you can click on 'add transformation,' and just like that, it will map your data to a statistical model. Anytime your data changes, you can see it generates a different series with the corresponding line.

There are different types of transformations available. First off, you can change the various fields that it maps to. There's also the option for polynomial model types with different degrees. For example, let's find a degree that makes the curve more dramatic. You can see how the curve changes, and as you adjust this, it will introduce more curves depending on the data.

I've also added in Play, where you can go to the regression analysis dashboard. This will show you an example of a graph with all the models displayed at once, and then it breaks it down into each one with both a chart and a table. The table shows the generated data alongside the regression analysis data.

You can refresh the dashboard if you want to find a dataset that best demonstrates the transformation. The great thing is that you can add this transformation to any data you have, regardless of its type. 

So, have fun!

## Raw YouTube Transcript

Hello, I'm Kristin Durivage, a software engineer on the data
processing team at Grafana. Let's talk about the regression
analysis transformation. So this transformation was actually
introduced two years ago behind a feature flag. And what this does is
put it into general release. It's very easy to use. So in any sort
of visualization panel you've got, we'll just use test data, which
generates something like this. Under transformations, you can do 'add transformation'
and just like that, it will map the data
that you have to a model - statistical model, that
anytime your data changes, you can see here it puts a different series with that
line on it. So there's different types. First off, you can change the
different fields that it maps to. There's also the option for
polynomial model types with different kinds of degrees here, so let's find [inaudible] to
make it more dramatic. Yeah, you can see the curve here
and when you change this, it will introduce more
curves depending on the data. I've also added in Play, you can go to the regression
analysis dashboard. This will show you an example of a graph with all of them on it at once, and then it breaks it down into
each one with both the chart and then a table showing - here's the
data that's generated and here's the regression analysis data
that is also for there. So you can kind of see how
it all works. And again, you can just keep refreshing this if
you want to try to find a data set that shows it off the easiest, but you can add this transformation
to any data you've got. It doesn't matter at
all. So yeah, have fun.

