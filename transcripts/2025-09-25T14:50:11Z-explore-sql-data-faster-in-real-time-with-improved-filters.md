# Explore SQL Data Faster in Real-Time with Improved Filters

Published on 2025-09-25T14:50:11Z

## Description

Grafana 12.2 improves ad hoc filters, unlocking a new workflow with SQL data sources. You can now query a dataset in one panel ...

URL: https://www.youtube.com/watch?v=dF8JrYvw1WA

## Summary

In this video, Natalia, an Engineering Manager on the DataViz team at Grafana Labs, discusses the latest enhancements to ad hoc filters introduced in Grafana version 12.2. She explains that these changes were made to improve the reliability of ad hoc filters on SQL data sources by adding support for the dashboard data source. Natalia demonstrates how users can now create a dashboard that queries a dataset from one panel and utilize ad hoc filters to refine the data across multiple panels. She showcases a practical example of filtering flight information for Indiana and encourages viewers to explore the new feature further through Grafana's documentation.

# Introduction to Ad Hoc Filters in Grafana 12.2

Hello, I'm Natalia. I'm an Engineering Manager on the DataViz team at Grafana Labs. Today, we're going to discuss our latest enhancement to ad hoc filters, which are available in all Grafana editions starting with version 12.2.

## Why the Changes?

So, why did we make these changes? Ad hoc filters couldn't be reliably implemented on SQL data sources. By adding support for the dashboard data source, we are unlocking a new workflow. You can now query a dataset from a first panel using a SQL data source, build the rest of your dashboard on top of that dataset, and then use ad hoc filters to refine and drill down into it.

## Demonstration

Let me show you how it works. Here we have a panel with a set of tabular data and an ad hoc filter variable set up, pointing at the dashboard data source. We also have another three panels, each of them pointing to that source panel and using the dashboard data source. Two of these panels have ad hoc filters enabled, while the third one has ad hoc filters disabled.

Now, let's say I want to see the flight information for Indiana. I could click here, add a filter, and all the configured panels will filter automatically. I can also remove this filter and, for example, filter by the amount of flights.

## Conclusion

Thank you for watching! Check out our documentation to learn more about this feature and try it out yourself starting with Grafana 12.2.

## Raw YouTube Transcript

Hello, I'm Natalia. I'm an Engineering Manager on
the DataViz team at Grafana Labs, and we're going to talk about our
latest enhancement to ad hoc filters, which are available in all
Grafana editions in 12.2. Now, why did we make these changes? Well, ad hoc filters can't be reliably
implemented on SQL data sources. So, by adding support to the dashboard data
source, we're unlocking a new workflow. You can now query a dataset from a
first panel using a SQL data source, build the rest of your dashboard
on top of that data set, and then use ad hoc filters to
refine and drill that into it. Let me show you how it works. Here we have a panel with a set of
tabular data and an ad hoc filter variable set up, pointing at the
dashboard data source. We also have another three panels, each of them pointing to that source
panel and they're using the dashboard data source. Two of them have ad hoc
filters enabled, as you can see, and the third one has ad
hoc filters disabled. Now, let's say I want to see
the flight information for
Indiana. I could click here, add a filter, and all the configured
panels will filter automatically. I can also remove this and let's
say filter by the amount of flights. So thank you for watching. Check out our docs to learn more about
this feature and try yourself starting Grafana 12.2.

