# Grafana 11 Features for Users | Grafana

Grafana 11 is now GA! In this video, we do a deep dive exploring all of the new features for our users. In this video, learn more ...

Published on 2024-05-15T08:07:52Z

URL: https://www.youtube.com/watch?v=ThfFcRETxCs

Transcript: Welcome to Grafana 11 for
the users. In this video, we'll deep dive into
all of the new features, which are important to new beginners
and power users of Grafana. Grafana operators and
developers, don't panic, there are dedicated
videos for you as well. Let's jump straight into one of the most
exciting new features. Explore Metrics PromQL. For some, it brings joy and for others it
sends shivers down their spine. Explore Metrics is a new feature that
allows you to bypass writing PromQL entirely. The new queryless interface provides a
bird's eye view of all metrics stored within your Prometheus data
sources. In Grafana 11, you should see a new entry underneath
Explore within the navigation menu called Metrics. Selecting this takes
you to the Metrics Explore app. Let's create an initial
exploration together. After clicking new Metric Exploration, we can now start to visually navigate
metrics for each Prometheus-compatible data source you have available. Why don't we start by selecting a
metric taken from our new data collector called Alloy? From there, we can start to navigate through different
panels to understand our selected metrics, whether this be filtering by a label
or looking at associated metrics. Let's filter by a label called
Service. Once we are happy, we can move this result into Explore
Panel, which auto generates the PromQL. We can then either move this into
a dashboard directly or add further PromQL transformations. Next on our list is
Scenes-powered dashboards. Migrating our Grafana dashboards over
to scenes provides us with more stable, dynamic, and flexible dashboards.
You will notice some early benefits, including faster loading
times and edit mode, which can be found in the top right
corner of your dashboard. When toggled on, this puts you in dashboard edit mode
and provides a new menu with asset creation options such as
ad visualization and row. We hope this new home will help
clean up the dashboard menu bar. You can also see as we scroll
throughout our dashboard, that the time picker and dashboard
variables snap to the top as we scroll, a much requested feature
within our Grafana community, and this is just the beginning. Scenes will provide the foundation
for what we envision the future of Grafana dashboards to be.
Talking about dashboards, let's take a deeper look
into our dashboard changes
coming within Grafana 11. The first stop stop our
tour is the Canvas panel. We've improved the overall experience
when creating and updating canvases. In this example, we are going to update a diagram
showcasing data being taken from a wind turbine. The wind turbine data is
now being sent to the cloud, so we are going to add
the cloud icon asset. Cloud is one of the newly added
assets alongside parallelogram and triangle. Next, let's add an arrow and run through
some of the new midpoint controls. We can select our new arrow from the
middle and snap this into a corner shape. We can also add a radius to our arrow
to smooth out the sharp corners within our diagram. This can also be done for
shape assets like rectangle. Lastly, we'll inspect
our windmill via a drone, so let's add that icon and
utilize the new rotation feature. This, alongside with a button feature
provides you with a far more immersive experience building out network
maps or SCADA solutions in Grafana. You can now also color full rows
within the table visualization. This makes it easier to quickly find
outliers within your table view. To apply this feature, we're going to
highlight all beholder beasts in red. We have pre added a value mapping already. Next on our list is to
add a field override. We will do this by name and
select the beast name. Finally, add a property, select cell type and
select colored background. Select toggle to entire
row, and there you have it. We can then sort to
find the beholder beast. Let's also take a look at the LLM
app now available within Grafana OSS, which allows you to utilize large
language models such as OpenAI to generate titles and descriptions
on your behalf. To start, make sure you enable the LLM app.
This can be done via administrations, plugins and data plugins. You
can then search for the LLM app. Once here, you can select your
chosen LLM from the dropdown, provide your connection
credentials, and then save and test. Once we've done this, we can then jump into our chosen
visualization a time series graph, which is currently named foo. We can update this to something
a little bit more descriptive. What we're going to do is click
auto generate and OpenAI does the rest. That looks pretty good, but let's see if we can improve it by
having a conversation with our LLM. I'm going to provide more
information about the query, and with that I'm pretty happy.
So let's also update the title. We hope this feature will help to provide
an improvement to your productivity as you scale with your Grafana dashboards. Remember to check out our other
visualization updates such as a fantastic community contribution, allowing you to
set threshold colors based on a query. The filter data by value transformation
has also been updated to enable partial string matching, and our x and Y chart is now officially
supported with documentation. So last but not least, let's talk
about improvements to alerts. We have improved the alert detail view
to provide a more comprehensive view of alert rules. This includes helpful metadata at the
top and the namespace and group are now shown as part of the
breadcrumb navigation trail. You can also refer to the query being
used to trigger the alert as well as the standard visualizations of
time ranged based queries. We also have a new option
for the configure, no data
and error handling rules. Keeping the last state allows Grafana to
retain the last known value before a no entry or execution error. This is a particularly powerful feature
as it provides you with a historical context on why a potential error
or timeout might have occurred when the error was last triggered, and that's it for our
Grafana 11 user walkthrough. There are also more features that
we didn't showcase here today, such as a massive time reduction within
the PDF exports for our cloud and enterprise users. Make sure to check out our Grafana 11
for the operators and developers videos when they release for more
great features on Grafana 11. Once again, a massive thank you to our Grafanista
developers and our community members for making Grafana 11 possible.

