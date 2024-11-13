# New: XY Chart is Generally Available in Grafana 11.1 | Grafana

We're excited to announce that the XY chart is generally available in Grafana 11.1! XY charts provide a way to visualize arbitrary x ...

Published on 2024-06-25T19:47:24Z

URL: https://www.youtube.com/watch?v=3d3Lx-Jz_kM

Transcript: Hi, my name is Leon. I'm a frontend engineer
on Grafana’s dataviz team, and today I'm excited to show off our new XY Chart Panel
that's rolling out of beta in version 11.1. This panel is designed
for creating scatterplots and bubble charts that help
find correlations and detect outliers within raw data sets along
dimensions that are not time. While community developed plugins like Plotly exist for visualizing scatter datasets, they require complex manual configuration and struggle to render more
than a few hundred data points. In contrast, XY chart tries
hard to just work with little to no configuration, as you've come
to expect from Grafana’s core panels. Additionally, we've gone to great lengths
to deliver high performance rendering with half a million points
without freezing or crashing your browser. Here we have the result of an influx time
series query that shows multiple sensors, each reporting carbon monoxide,
humidity, and temperature over time. Let's say we wanted to see
if there's any correlation between humidity and temperature
on a per sensor basis. Let's start by adding a visualization. We'll pick
our dataset from the dashboard datasource. We'll select XY Chart. And then we'll change the X field to be
temperature and the Y field to be humidity. And we're done. For our next example we have a single
dataset that's typical of SQL queries. The table has performance data for different makes
and models of vehicles, with their country of origin. Let's plot the horsepower versus miles
per gallon for each country. We repeat the same
steps as we did before. Now that we have a plot for the entire
data set, we need to split it up by country. To do this, we're going to use our
partition by values transformation. We'll select the origin field. We can easily change the colors by
clicking on the legend and changing it here. When hovering any data point,
the total contains every column for that point, as well as supporting
data links and template variables. XY Chart has additional features that we
cannot cover in this short demonstration. You can explore all of these panels
and more on play.grafana.org. Just type XY Chart
into the search bar. Thank you for watching and we hope you enjoyed
Grafana’s ever-expanding visualization capabilities.

