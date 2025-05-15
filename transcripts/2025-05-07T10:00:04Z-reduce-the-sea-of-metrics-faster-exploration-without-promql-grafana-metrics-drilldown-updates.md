# Reduce the Sea of Metrics: Faster Exploration Without PromQL: Grafana Metrics Drilldown Updates

The updated Metrics Drilldown app in Grafana helps you reduce the sea of Prometheus metrics faster—no PromQL needed.

Published on 2025-05-07T10:00:04Z

URL: https://www.youtube.com/watch?v=2tVo7gX87fU

Transcript: Hi, I am Brendan O'Handley, a
software engineer at Grafana Labs. Today I want to show you our updated
Metrics Drilldown app and give you a quick demo. We built this app because we know how
overwhelming it can be to navigate through countless Prometheus metrics, especially when you're
trying to fix urgent issues. Let me walk you through a scenario that
shows how Metrics Drilldown reduces the sea of metrics and lets you explore your
data without having to write a query. Okay, let's imagine Sarah an SRE at
a large e-commerce company. It's during the holiday shopping season
when her phone buzzes with an alert. There are issues with the ad service. Every second of delay
can mean lost revenue, so Sarah needs to
identify the problem fast. When she goes to Grafana, she can select the main menu and
look for the drill down section. She looks for metrics, clicks it, and
is taken to the Metrics Drilldown app. This shows her Prometheus metrics for
her organization and she can see her data right away. She confirms that she is using the
correct data source for Prometheus. She selects the last three
hours for her time window and adjusts the refresh interval
to every 15 minutes. She scans the metrics again and
she feels momentarily overwhelmed. She recognizes this is precisely the
scenario where Metrics Drilldown filtering capabilities will save
her significant time. She begins her investigation by
leveraging the sidebar menu and using the filtering options
first. The rules filter. She filters to select
only non rules metrics. She chooses non rules
because this is the raw data. This is different than recording rules, which are aggregations
and transformations. Her experience has taught her that
recording rules often mask underlying patterns when troubleshooting
complex issues. She needs visibility into the actual data. Now she's reduced it to 523 metrics, and she decides to use the
prefix filter node to focus on infrastructure metrics. To
further refine her search, Sarah goes to the suffix
filters right here and provides bytes. This focuses her search on
memory and disc metrics. Now she's just looking at 49 metrics.
Sarah considers though that the issue could be at the application
level since it's affecting the ad service specifically. She removes her suffix
filters and prefix filter, and selects the group by labels feature. She selects the service name label and this shows her all the values
for the service name label. At the top of the list, she sees
the ad service. Within this, she sees metrics for this filter
and she can paginate to look at more metrics. Here she can
select the ad service, service name filter, and
add it to her filters. She can scan the metrics again and
sees it's reduced to six metrics. Sarah next leverages the
sorting capabilities. The default sort will show her her
most recently selected metrics. She chooses dashboard usage to see
which metrics her team typically monitor closely. She can see this metric has been
used in four dashboard panel queries. Next, she sorts by alerting usage
to identify which metrics are approaching alert thresholds.
After looking through filtering, grouping, and sorting processes, Sarah's attention lands on the traces_span_metrics_duration_seconds_bucket.
Clicking
on
this
metric, Sarah enters the detailed
metric scene view. She can first look at the breakdown tab. This shows all the labels on the metric,
and she can scan through each label. The next tab is related metrics, which shows relevant metrics based
on the current filters related to her selected metric by name. The third tab is related logs, which are related Loki data
sources connected by the filters in the Prometheus
instance and the Loki instance. From this tab, Sarah can open the query
for this panel and Explore. And from Explore, she can add
this query to a dashboard. Sarah realizes that this entire process
could have taken her an hour or more using traditional methods, but
with the Metrics Drilldown app, she identifies the issue and is able
to add it to a dashboard without writing any queries. In addition to this, Sarah can bookmark this page or
copy the URL to share with others. To see the bookmarks, Sarah can return to the main view
and in the sidebar menu open the bookmark tab to see her saved bookmarks. And the next time Sarah
opens Metrics Drilldown, her recent exploration will appear
at the top of the default sort. This metrics she selected is now
sorted to the top by default. What's remarkable here is how Sarah
investigated a complex problem in minutes without writing
a single PromQL query. This is the power of the Metrics
Drilldown app - transforming, troubleshooting workflows for
teams of all experience levels. I'm Brendan O'Handley and thank you.

