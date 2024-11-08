# Demo: Explore Metrics — Browse Prometheus-Compatible Metrics Without Queries in Grafana 11 | Grafana

We built Explore Metrics to make it easier for our users to work with their Prometheus data without having to write queries (ahem ...

Published on 2024-04-09T12:11:23Z

URL: https://www.youtube.com/watch?v=JbaPufQs5LY

Transcript: Hi, I am Mary, a design
manager at Grafana, and I'm going to talk you through a new
feature we're building that's called Explore Metrics. So the reason we built this feature
is because we know that it's really difficult for many of our customers,
many of our users to write PromQL, and we want to give people the ability
to work with their Prometheus data without having to write queries. So this is a new query-less experience
for exploring and drilling into your Prometheus metrics. So let me
talk you through it. Right here, what we have is our main landing page
and the way that you would get here is in our main navigation under Explore
and then you'll see Metrics. So what we have here is
a big list of our time series visualization with all
of our Prometheus metrics. So you can see all the metrics in this
specific Prometheus instance on this main page. So we give you the ability
to drill into your metrics. So you can add specific label value pairs,
and you can also do keyword searches. In addition, you can do many of the things that
you can do on a Grafana dashboard, like adjust the time
range or do auto refresh or adjust some of your settings, right? So let's say that I am responding to an
incident and I think there's potentially an issue with my CPU, right? So I can use the keyword search for CPU
and see any of the metrics that contain that keyword in their name. But let's say maybe it's not
CPU, maybe it's something else. Let's say I know that there's an
issue with a specific node, right? So if I know that this node is the issue, what I can do is come in and what
happened here is all of the nodes with this specific label value pair
are going to show up right here. So let's say I know the issue
happened a little while ago, so I'll just zoom out a bit. So
what you'll see here is again, the list of the graphs adjusted for
the specific period in time that I was looking for. And what I can do is
say, "Oh, this looks interesting, right?" So I can drill into it
again right here. And this again, adjusts the time range similar
to our dashboards. And then say, if I know this is the one that I
wanna look at, I can select it. So once I go in, I can see a
general overview of that metric. And I can also see here - related metrics. And these are metrics with
similar keywords in the names. The really interesting
part here is the breakdown, and this is where I can see relevant
label value pairs that are associated with that metric. And as I'm scrolling through and even
just taking a quick look visually, I can see that here with Container,
there's a similar pattern here. So if I select Container, what happens is I get
more information and as I scroll through, as I look up here, I can start to see this pattern visually. So I can even add this into my filters
and I can start to look through in more detail where the issue could be. So in addition to providing you
with a query-less experience, what we also have given you is
the ability to move to explore. So what you see here is a
graph with the visualization that I see that I created in
the Metrics Explorer here in our standard Grafana Explorer. So I
can adjust the query if I need to, I can add other queries, and then I can take any of the other
actions that I would take and explore. So for example, if I wanna create a
new dashboard with this visualization, I just did that and I did that
all with without writing PromQL. We also give you the ability to copy
the URL so you can share it with your colleagues. So if you'll see here
that URL I just copied will - if I put it into the browser - display the
exact same graph that I saw before. And we do give you the ability
to bookmark or save your explorations as well. So
here if I do a bookmark, you'll see it's been added, and then I can go back to my main page
and this is where I would see this bookmark. So if I click back in here, you'll see I'm back again. So it
allows you to save this as well. Going back to the main page, you'll see that we have bookmarks
saved as well as recent explorations that you've done. So that's
a really quick overview. We're excited to get this out and we
can't wait to hear what you think. Thank you.

