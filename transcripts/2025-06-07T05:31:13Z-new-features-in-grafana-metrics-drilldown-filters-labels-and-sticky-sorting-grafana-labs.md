# New Features in Grafana Metrics Drilldown: Filters, Labels, and Sticky Sorting | Grafana Labs

Published on 2025-06-07T05:31:13Z

## Description

The Grafana Metrics Drilldown App just got a powerful upgrade. Explore new features for filtering, grouping, and sorting metrics ...

URL: https://www.youtube.com/watch?v=Nd84by7IFEI

## Summary

In this video, Brendan O'Handley, a software engineer at Grafana Labs, discusses new features in the Grafana Metrics Drilldown App, including the automatic promotion of OpenTelemetry resource attributes as metric labels, which will lead to the deprecation of custom joins. The presentation highlights the challenges users face with a large volume of metrics and introduces a revamped user interface that includes features for filtering, grouping, and sorting metrics to facilitate targeted investigations. Brendan provides a live demo featuring a scenario where an SRE named Sarah utilizes these new functionalities to efficiently navigate and analyze metrics related to her ad service. He concludes with future plans for the app, including enhanced integration from alerts and dashboards, and expresses gratitude to his colleagues involved in the project.

# Grafana Metrics Drilldown App Announcement

Hello everyone, I'm Brendan O'Handley, a software engineer at Grafana Labs. I'm part of the Observability Metrics Squad, and today I'm excited to share some new features in the Grafana Metrics Drilldown App.

## Exciting Announcement

First, I’d like to make an exciting announcement: Grafana Cloud will be automatically promoting OpenTelemetry resource attributes as metric labels. Originally, this talk was going to focus on the Grafana Metrics Drilldown App and complex join queries. However, due to the automatic promotion of resource attributes as metric labels, we will be deprecating custom joins. 

This doesn’t mean we’re not interested in custom joins with info metrics; we do have an issue open regarding making those join queries for any info metrics. Please feel free to talk to me afterwards at the Ask the Experts booth if you have questions.

## Introducing the New UI

Now, let's move on to the most exciting part: the Grafana Metrics Drilldown App in reducing the sea of metrics. We found that our users often approach the app with a significant number of metrics, which makes it challenging for them to narrow down their list. They want to see only the most meaningful metrics, the ones they truly care about.

### New Features

I would like to introduce the new UI and feature set from the Metrics Drilldown App, which provides a navigable system for filtering, grouping, sorting, and creating targeted, efficient investigations.

#### Sidebar Menu

The first part of the new UI is the **sidebar menu**. The top three features in this menu are:

1. **Filters**
   - **Rules Filters:** Allows you to include or exclude recording rules. If you choose non-rule metrics, you can see the original data from your applications or exporters.
   - **Metric Prefix Filters:** These filters provide clues into categorization and organization.
   - **Suffix Filters:** These can indicate the type or unit of measurement.

2. **Group By Labels Feature:** 
   - When you select a label, all of its values will be presented in a list, along with a collection of metrics for each value. You can sort through the metrics by pagination and select a label value to add to your filters.

3. **Sorting:** 
   - Our default sort is **sticky metrics**, which automatically sorts any metrics you select to the top. This feature already exists in Logs Drilldown.
   - We also have **dashboard usage sorting** and **alerting usage sorting**. Metrics that are frequently monitored or used in alerts will be sorted to the top.

## Live Demo Use Case

Let’s move into a live demo to illustrate how this could work for someone. Imagine Sarah, an SRE at a large e-commerce company. She receives alerts for the ad service, knowing that this can impact her business.

Upon entering Grafana, Sarah finds the Grafana Metrics Drilldown App and sees she has 639 metrics. The first thing she does is select the non-rule metrics to view the actual raw metrics for her applications, services, and exporters. 

Next, she applies the prefix filter, selecting the infrastructure level and reducing her metrics to 66. She then continues with the suffix filters, choosing a suffix like "bytes" to indicate memory or disk metrics. Recognizing that this is for the ad service, she selects the service name and sees it sorted at the top of her list, along with other services.

Sarah can then view the metrics associated with the ad service and select a label to add to her filters. Sorting by default shows the most recently selected metric (the sticky metric), and she can also sort by dashboard usage and alerting usage to see which metrics are being monitored most frequently by her team.

Additionally, bookmarks have been moved into the sidebar menu, allowing Sarah to have a more targeted investigation.

## Conclusion

To summarize, Sarah has effectively utilized the Grafana Metrics Drilldown App for a targeted investigation. She used the sidebar filters (rules, prefix, and suffix), grouped by labels, and sorted sticky metrics, dashboard usage, and alerting usage.

### What’s Next?

Looking ahead, we would like to introduce extension points that allow users to access the metrics drill down from alerting or dashboards. For example, for dashboards with panels that have high cardinality, we could open up into metrics and facilitate a drill down. We also plan to onboard users to identify the most used labels to reduce the set of metrics.

Thank you to everyone who has worked hard on this project, especially Catherine, Kat, Miguel, Marc, and Nick. Thank you for listening. I'm Brendan O'Handley.

## Raw YouTube Transcript

Hello everyone. I'm Brendan O'Handley,
a software engineer at Grafana Labs. I'm part of the
Observability Metrics Squad, and today I'm excited to share with
you some new features in Grafana Metrics Drilldown App. But first I'd like to make
an excited announcement about Grafana Cloud will be automatically
promoting open telemetry resource attributes as metric labels. And originally this talk was going to
be about the Grafana metrics drill down app and complex join queries and such. But due to this automatic
promotion of resource attributes as metric labels, we're
going to be deprecating, the custom joins. But this doesn't mean that we're not
interested in custom joins with info metrics, but we do have an issue for
making those join queries for any info metrics. So please talk to me afterwards
at the Ask the Experts booth. And we have an issue here for that.
But onto the most exciting part, the Grafana Metrics Drilldown App
in reducing the sea of metrics. So we found that our
users can approach the metrics drill down app and have
a significant amount of metrics. So users struggle to narrow down
their list and it's not helpful for them to see metrics that
they're not interested in. They want to see the most meaningful
ones, the ones that they care about, that they're very sensitive about. And I would like to introduce
the new UI and new feature set from the metrics drill down app. It will provide a navigable
system for filtering, grouping, sorting, and can create a
targeted efficient investigation. The first part of the new
UI is the sidebar menu. And in the sidebar menu, the
top three things are filters. First rules, filters, so that you can include or
exclude recording rules. This means if you choose non-rule metrics, you can see the original data
from your applications or exporters. The next filter is metric prefix filters. And why are metric
prefixes important? Well, they can give you a clue into
categorization or organization. The third filter is suffix filters
and metrics suffixes can indicate type or unit of measurement. The next item in the sidebar menu
is our group by labels feature. So if you select a label, all of those label values
will be presented at a list. And for each label value, there
will be a collection of metrics. With all the data for those metrics, you can sort through the metrics by
pagination and you can select that label value to add to your filters. As we move from the sidebar menu, we get into sorting. So with sorting, our default sort is sticky metrics,
and we're very excited about this. This is something that exists already in
Logs Drilldown. So with sticky metrics, any metrics that you select will be
automatically sorted to the top by default. But we also have dashboard
usage sorting and alerting, alerting usage sorting. So if a team is monitoring
metrics a lot and a lot of dashboards, those can be sorted to the top. And the
same goes for metrics that are used in alerting. So with all of those features, let's move into the live demo to
see a use case of how this could work for someone. Okay, so imagine Sarah an SRE at a large e-commerce company. And Sarah has gotten
alerts for the ad service. So she knows that this
can impact her business. And so she originally comes to Grafana and finds the Grafana metrics drill down app. Now she can see she has 639 metrics, but the first thing
that she does is select the non rules metrics to see the actual
raw metrics for her applications, services and exporters. She can choose the prefixes. Next, where she selects the
infrastructure level and selects the node metric,
reducing her metrics to 66, she could then continue into the suffix filters where
she could choose a suffix such as bytes to indicate
memory or disk metrics. But she also recognizes that this is for the ad service, and she knows that the open telemetry resource attributes
have been promoted as metric labels. And so she
chooses the service name and she can see sorted at the top of her. Sorted at the top of her list of values is the service here and a variety of other services for each one. She can through those metrics shown. And yes, if my eyesight works,
this is the add service, which she can select as a label to add to her filters. And I
just selected a metric, but for the group by labels, she can select that. All right, so upon looking at some of these metrics, she can also move to the
sort and sorting by default will show the most recently selected
metric. That's sticky metric. She can sort to show
dashboard usage to show which metrics are being monitored
mostly by her team. And we can see the number here. She can also do this
for alerting usage, and she can see metrics that being
that are in alerts right now. So one last addition for this is that bookmarks have also been
moved into the sidebar menu. And so we can see how Sarah can
have a targeted investigation. And let's move back to
the slides. Thank you. So Sarah has had a targeted investigation
with the Grafana metrics drill down app. She's used the sidebar
filters from rules, filters, prefix and suffix. She's seen
the counts of metrics change. She's grouped by labels and selected
label values and seen the metrics for those specific label values. She's also sorted sticky metrics, dashboard usage and alerting usage. And with all of this, I'd like to say what's next for
Grafana metrics drill down app? Well, we would like to have extension points
or ways to get into metrics drill down from alerting or
dashboards. For example, for dashboards with panels
with high cardinality, we could open up into metrics
and have a drill down. We would also like to do
onboarding to find most used labels to reduce the set of metrics. So these are a few of the things that we
will be working on next for the metrics drill down app. And I would like to say thanks for all
the folks that we've worked on this very hard. Thanks to Catherine,
Kat, Miguel, Marc, and Nick. And thank you from me. I'm Brendan
O'Handley. Thank you for listening.

