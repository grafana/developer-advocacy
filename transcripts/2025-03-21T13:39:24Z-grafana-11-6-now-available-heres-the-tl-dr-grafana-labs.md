# Grafana 11.6 Now Available! Here&#39;s the TL;DR | Grafana Labs

Welcome to this update on Grafana 11.6! This release brings exciting enhancements to dashboards, visualizations, alerting, and ...

Published on 2025-03-21T13:39:24Z

URL: https://www.youtube.com/watch?v=iF7yxO4nUXQ

Transcript: Welcome to this update of what's
new in Grafana, version 11.6. This release includes several
exciting enhancements to dashboards, visualizations, alerting,
and security. I'm Bukola, a developer advocate at Grafana, and let's take a closer
look at these key updates. The first update is that Canvas
one-click data links and actions are now generally available.
Previously in public preview, this feature lets you open a data link
or trigger an action with a single click. With this update, the one-click switch has been moved into
the dialogue box where you configure the data link or action at
element level. But keep in mind, you can only have one-click data
link or action per visualization. So if you enable it for one element,
it's automatically disabled for others. In addition to Canvas
one-click links in action, we've also added one-click data
links to more visualization types, including time series,
bar chart, candlestick, state timelines, status history, trend, and XY chart.
Again, only one, one-click feature can be active at a time, keeping interactions
simple and streamlined. Another exciting update is that
visualization actions are now generally available. This means you can now trigger
basic unauthenticated API calls directly from dashboard panels. Supported visualizations include
time series, bar charts, candlestick, state timelines, status
history, table, trend, and XY chart visualizations. You can now find actions under the data
link and action section of the panel editor. Grafana has also improved
time region controls and annotations. Users can use Cron syntax to set
more precise schedules with queries like the second Tuesday of every other
month at 9:00 PM or weekdays from 9:00 AM to 5:00 PM to try it
out, create an annotation, toggle the advanced switch, and enter your cron based schedules
for even greater flexibility. We've also introduced a new action
cell type for table visualizations. This allows you to trigger
actions directly from table cells, making it easier to integrate external
workflows right from a table column. Grafana has also improved
geomap visualizations. Grafana now uses WebGL for marker layers, bringing huge improvements
in speed and stability, especially when working
with large data sets. Grafana has also extended support
for dashboard variables for all transformations. Now, all text input fields and
transformation accept variable syntax. So when you dashboard
variables in transformation, the variables are automatically
interpolated before
the transformations are applied to the data. Grafana managed
alerts now include version history, which means you can view
past versions of an alert, compare changes over time, restore
previous versions if needed. Head over to any Grafana manager alert
rule and click the version tab to check it out. Managing multiple data
sources can sometimes be a challenge, especially when different teams
need access to the same data. Grafana instances can become cluttered
and confusing with hundreds of data sources. That's where LBAC, label based access
control for data sources, Mimir metrics comes in. This
experimental feature allows teams to view the same data source, but filter
based on the team's label permissions. This makes collaboration easier while
keeping dashboards clean and organized. Finally, let's talk
about security updates. API Keys have now been fully
deprecated, but don't worry. All existing keys have been automatically
migrated to service accounts. There's no action needed on your part. Your API integrations will continue to
work seamlessly while benefiting from improved security and management features. And that's a wrap on every
update in Grafana 11.6. To get more details about this
release, check out the change log, which is linked below. For the specific steps we recommend
when you upgrade to version 11.6, check out our upgrade
guide also linked below. Thanks for watching and don't forget to
like and subscribe and I'll see you in the next video.

