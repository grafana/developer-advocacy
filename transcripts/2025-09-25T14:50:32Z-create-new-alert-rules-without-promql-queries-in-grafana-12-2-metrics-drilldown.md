# Create New Alert Rules Without PromQL Queries in Grafana 12.2 | Metrics Drilldown

Published on 2025-09-25T14:50:32Z

## Description

Grafana 12.2 makes alert creation simpler by integrating the Metrics Drilldown app with the Alert Rule Query Editor. Instead of ...

URL: https://www.youtube.com/watch?v=CoCvELwQh6c

## Summary

In this video, Brendan O'Handley from the Observability Metrics Squad introduces a new feature that integrates the Metrics Drilldown app with the Alert Rule Query Editor, enhancing user experience by allowing a queryless approach. He demonstrates how users can navigate the Metrics Drilldown app using Prometheus data sources, select metrics, and apply labels without needing to create a query manually. The feature streamlines the process of setting up alert rules by enabling users to easily explore metrics and filter results, ultimately facilitating a more intuitive workflow in managing alerts.

# Integrating the Metrics Drilldown App with the Alert Rule Query Editor

Hello, I'm Brendan O'Handley from the Observability Metrics Squad, and I'd like to show you a new feature integrating the Metrics Drilldown app with the Alert Rule Query Editor.

First, let's look at the Metrics Drilldown app, which uses Prometheus data sources. Here, we see the **Go Query** and **Go Queryless** buttons. From this interface, we can navigate to the Metrics Drilldown app and enjoy a queryless experience while exploring our metrics. 

### Key Features:
- **Adding Labels**: Users can select a metric and add labels.
- **Opening in Explore**: From the selected metric, we can open it in Explore to retrieve the query.
- **Applying to Alert Rule**: This query can then be directly applied to our alert rule.

This is the first workflow where a user may not have a query but has a metric and labels. When you click the **Go Queryless** button, it will parse the query and take you directly to the metrics scene page for the Metrics Drilldown app. 

Here, you can see the selected metric and the filters that you chose. You can break down by series and metric, and from this point, you can select more labels. With this information, you can again open it in Explore, copy the query, and apply it to your alert rule.

This feature allows users to have a queryless experience when creating a new alert rule.

Thank you very much!

## Raw YouTube Transcript

Hello, I'm Brendan O'Handley from
the Observability Metrics Squad, and I'd like to show you a new feature
integrating the Metrics Drilldown app with the Alert Rule
Query Editor. So first, this is the Metrics Drilldown app,
which uses Prometheus data sources. So we look for our Prometheus data source, we see the go query, go queryless button, and from here we are able to
navigate to the Metrics Drilldown app and have a queryless experience
looking through our metrics, adding labels, and we can select a metric. And from here we can open
this in Explore to get the query and we can apply
this query directly to our alert rule. So this is the first workflow
where a user does not have a query, but maybe you have a metric and labels. When you click the Go
queryless button now, this will parse the query
and take you directly to the metrics scene page for the
Metrics Drilldown app. Here, we can see the metric and
the filters that you chose. We can break down by the
series and the metric. And, from here we can select more labels. And with this information, we
can again open and explore. We can copy the query and we
can apply this to our alert rule. So this allows users to have a queryless
experience when creating a new alert rule. Thank you very much.

