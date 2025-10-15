# Why Prometheus 3.0 Will Change How You Do Observability: OTel Support, Remote Write 2.0, and More

Published on 2025-06-07T05:30:13Z

## Description

Learn about the biggest updates to Prometheus in 7 years: a revamped UI, native histograms, remote write 2.0, and ...

URL: https://www.youtube.com/watch?v=YubGvtyFJG8

## Summary

In this presentation on Prometheus 3.0, Carrie Edwards, a staff software engineer at Grafana and Prometheus maintainer, and Goutham, a product manager at Grafana Labs, discuss the major updates and features of the latest version of the monitoring tool. They highlight the history of Prometheus, which originated at SoundCloud, and its evolution to the current version, including a complete UI overhaul, the introduction of native histograms, OpenTelemetry compatibility, UTF-8 support, and remote write 2.0. The presenters delve into the improvements brought by the new UI for easier navigation and query building, the efficiency of native histograms over classic ones, and the enhancements in remote write capabilities. They also touch on breaking changes in version 3.0 and ongoing governance improvements to encourage community involvement and leadership within the project. The session concludes with an invitation for audience engagement and contributions to the Prometheus project.

# Talk on Prometheus 3.0

Welcome to our talk on **Prometheus 3.0**. If you have any questions, feel free to scan the QR code, and we will answer them at the end of this presentation. 

My name is **Carrie Edwards**. I'm a staff software engineer at Grafana, and I'm a Prometheus maintainer and team member. 

Hey everyone, I'm **Goutham**. I'm a product manager at Grafana Labs, and I'm also a Prometheus team member. 

## Audience Engagement

We're going to start off with a show of hands: 
- Who here has heard of Prometheus?
- And who here has tried out Prometheus 3.0? 

Since everyone seems to be pretty familiar with Prometheus, we’ll skip over the basic introduction and go over the history. 

## History of Prometheus

Prometheus started off at SoundCloud with the first commit about **12 years ago**. In **2016** and **2017**, it became the second project to join and graduate from the **CNCF**. Version **2.0** was released in **2017** with major updates to the TSDB. Last November, we had our first major release in seven years: **Prometheus 3.0**, which will be the focus of our talk today. 

I was just looking back at when I did the **2.0 release**, and 2.0 was how I started my career. I'm really glad to be here talking about 3.0. 

Today, we’re going to discuss some of the features released as part of Prometheus 3.0, which include:
- The new UI
- Native histograms
- OpenTelemetry compatibility
- UTF-8 support
- Remote write 2.0
- Some breaking changes

There have also been several updates and minor version bumps since Prometheus 3.0 was released, so we will talk a little about those new introductions, as well as what’s to come in the future. 

## Features of Prometheus 3.0

### New UI

Let’s start with one of the most discernible changes introduced in Prometheus 3.0: **the new UI**. The UI was completely rewritten by **Julius Voltz**, introducing a less cluttered, more consistent, and easier-to-navigate layout. This QR code will take you to a demo so you can try it out for yourself.

The old Bootstrap-based system has been replaced with **React** and the **Mantine framework**, aiming for a more modern look and enabling better development and easier maintenance.

Several new features have been added as part of the new UI:
- **Metrics and Label Explorer**: This helps you build queries, view, and search through available metrics and metadata for each metric. You can select a metric and use the label explorer to drill down into the label names and values of the specific metric, adding label matching filters to narrow down your desired results.
- **Query Tree View**: Adapted from **PromLens**, this allows you to break down any **PromQL** query into subexpressions and includes inline documentation and metadata, so you can see what each part of your query is doing. You can click on each node to see its evaluation and the label data associated with each subexpression.
- **Explain Tab**: This provides even more context on a node within your query with explanations, insights, and visualizations. It visualizes how you're joining the series together, describing the match groups on the left and right-hand sides of the binary operator, making debugging much easier.

This feature currently does not exist in Grafana, but hopefully, it will in the future.

Looking ahead, continuous work is being done on the UI, with improvements already made to graph views, such as adding vertical lines and clipboard functionality. More work is still to come, including UTF-8 quoting, auto-completion, and rendering native histograms and heatmaps.

### Native Histograms

Next, let’s talk about **native histograms**. Generally, histograms store distributions of data points rather than raw data by storing counts of values that fall within certain ranges. They are often used for quantile estimation.

Historically, to measure things like latency of requests in Prometheus, classic histograms were used. These require predefined bucket boundaries and are represented as multiple time series in Prometheus, one for each bucket, along with one for the count of data points and one for the sum of data points.

However, classic histograms have several drawbacks:
- Defining bucket boundaries can be challenging, and changes require re-instrumentation and re-deployment.
- They are expensive to store because each bucket results in a new time series, leading many users to define only a few coarse buckets, which can cause inaccuracy in quantile estimation.
- Classic histograms can only be aggregated if the bucket boundaries match exactly.

With **native histograms**, many of these issues are addressed. Instead of predefined bucket boundaries, the boundaries are calculated based on an exponential scale, allowing native histograms to be aggregated and merged more easily. 

The key benefit is that they are stored as a single complex sample that encompasses all the necessary data. Here’s an overview comparing classic histograms and native histograms: native histograms are a vast improvement in efficiency for both cost and space.

Here’s an example of querying native histograms in the Prometheus UI, showing the bucket counts and boundaries of a native histogram, along with an example of quantile estimation.

Note that there are slight differences in querying native histograms versus classic histograms; for instance, you don’t need to use the **LE** or less than or equal to label when querying native histograms.

Looking ahead, exciting developments are still in progress for native histograms. Updates are being made to the text format, operators, function refinements, and heatmaps in the UI. 

Another exciting new feature in progress is **custom buckets** for native histograms. This addresses scenarios where a native histogram might not fit your data very well, allowing for predefined bucket boundaries without losing accuracy or data at scrape time.

### Remote Write 2.0

Next, we’ll discuss **remote write 2.0**. Remote write is a protocol that allows Prometheus-compatible senders to forward scraped metric data in real time to receivers. Prometheus can send and receive this data, and other monitoring tools such as **Thanos**, **Cortex**, and **Mimir** can ingest the data and write it to their own TSDBs.

The initial version, **Remote Write 1.0**, sends data using snappy encoded protobuf messages over HTTP. Remote write 2.0 improves on this by enhancing efficiency and network bandwidth and supports newer Prometheus features. 

It still uses protobuf over HTTP but sends data by string interning all of the label data, dramatically reducing the request size. The specification includes fields for new features in Prometheus, such as native histograms and created timestamps. 

It also supports handling situations with partial write failures, allowing receivers to respond with partial write error statistics using HTTP headers, enabling senders to log errors and retry accordingly.

Here you can see the significant improvements in efficiency regarding bandwidth and serialization levels with remote write 2.0 compared to remote write 1.0. To ease adoption of remote write in the long run, we’ve built an experimental library in **client-golang**, allowing for easier construction of remote write 2.0 compatible senders and receivers.

Looking ahead, the goal is to soon mark it as non-experimental, with ongoing work for sending creative timestamps and addressing efficiency issues with metadata. This flexible new protocol allows for experimentation with various compressions and future formats like **Apache Arrow**.

## OpenTelemetry Support

Now, I’m going to turn it over to Goutham.

Thank you, Carrie. So, I haven’t actually written any code for 3.0, but I did some other work, like spec work, and **OpenTelemetry (OTel) support** is one of those. We’ve made a significant push to support OTel natively in Prometheus over the past year.

You can now push metrics into Prometheus from applications instrumented with OTel. However, we don’t want to default on this, as it could allow people to push random data into Prometheus. You have to explicitly enable it with this feature flag, but it is stable.

That said, the spec for converting **OTLP** data into Prometheus is still in flux. By default, if you follow the spec, resource attributes like namespace and cluster name are sent as a different metric that you have to join on, making queries complicated. 

To ease this, we added a config option called **promote resource attributes** that allows you to copy over resource attributes into labels, enabling easier queries. 

We’re also excited about **UTF-8 support**. OTel uses dots, which we didn’t support, so we added dots, and then we found out that OTel also supports slashes and anything UTF-8. Prometheus can now handle UTF-8 metric names, label names, and label values, including emojis. 

This is implemented on the server and in a few client libraries, but we want UTF-8 support everywhere. The Ruby maintainers are looking for help, so if you’re a Ruby expert, we would love your assistance. 

We also want to utilize type and unit metadata in OTel effectively. For example, if you’re trying to do a rate over a gauge, we want to alert you that this is not advisable. We also aim to understand **semantic conventions** better, such as automatically generating insights around HTTP metrics.

Additionally, we want to support **Delta temporality**. Currently, Prometheus only supports cumulative data. There’s a need for support for deltas, similar to how StatsD and Datadog push deltas. We’ve kind of hacked this into Prometheus with a feature flag, but we want to natively support deltas and are still figuring out how to implement this.

### Prometheus Governance

Putting everything together, you can see a native histogram from OTel. There are dots in the metric name, and we are evolving to make everything consistent. You can push OTLP semantic conventions and native histograms into Prometheus and graph them with PromQL, which is really cool.

Now, regarding breaking changes: I kind of want to say we have no breaking changes, but then I’ll get to the next slide, and we’ll have a huge page full. However, these are only breaking changes that we thought affected extremely few people, and they can easily change them. 

For instance, how many of you here use the **holt winters function**? There you go, we broke it. Similar cases exist, such as queries that get a data point for every minute and then select the last one minute.

Previously, queries included both the first and last point. For consistency and efficiency, we decided it didn’t matter if the last point was included, but this led to issues, especially for users relying on precise timing with Grafana.

The other change involves how we scrape, specifically regarding the protocols we support. We used to default to **PrometheusText0.0.4**, which is very old, but we’ve updated this to avoid breaking users using specific protocols, such as **Sinatra**.

### Governance Changes

The next topic has nothing to do with Prometheus 3.0; it has been my pet project for the last two years. I thought it would take three months, but here we are. 

The graphs show the number of commits from 2.5 to 3.0, indicating that Prometheus is still an active project. However, while we have a healthy project, we’ve struggled to attract new leadership. 

Changing governance requires a two-thirds majority, making it increasingly challenging to add new members as the team grows. Therefore, we’ve worked on **Prometheus Governance 2.0** to create a more inclusive structure.

We’ve added 22 new members who have been consistently contributing for many years. 

**Contributors** are anyone who has made any contributions, and if you have 10 contributions over a 36-month period, you will be added to the GitHub org as a **member**, with more say in the project. 

**Maintainers** have commit rights and maintain different parts of Prometheus. The members will elect a steering committee of five to seven people who can change governance, allowing for a larger number of contributors to have a say without deadlocking on governance.

This governance change is approved, and we are still figuring out how to vote for the steering committee. 

With that said, I don’t think you should wait for the new governance to get involved. We are still adding maintainers and new members to the team, and there’s a lot of work to be done, especially with the ongoing developments since 3.0. 

If you’re interested in contributing, check out the various channels on the **CNCF Slack** for Prometheus, and feel free to reach out and say, “Hey, I have some free time. How can I contribute?” We can guide you through this process.

## Raw YouTube Transcript

Welcome to our talk on Prometheus 3.0. If you have any questions, feel free to scan this QR code and we
will answer questions at the end of this presentation. My name is Carrie Edwards. I'm a staff software engineer at Grafana, and I'm a Prometheus
maintainer and team member. Hey everyone, I'm Goutham. I'm a
product manager at Grafana Labs. I'm also a Prometheus team member. We're going to start off with a show of
hands. Who here has heard of Prometheus? Okay, and who here has tried
out Prometheus 3.0? Okay, a couple of people. Since everyone seems to be
pretty familiar with Prometheus, we'll skip over the basic
intro and go over the history. Prometheus started off at SoundCloud
with the first commit about 12 years ago, and in 2016 and 2017, it became the second project
to join and graduate from the CNCF. Version 2.0 was released
in 2017 with major updates to the TSDB. And last November we had our first
major release in seven years. Prometheus 3.0, which will be
the focus of our talk today. I was just looking back
at when I did the 2.0 release and 2.0 was how I started
my career and I'm really glad to be here also talking about 3.0. So today we're going to talk about some
of the features that have been released as part of Prometheus 3.0,
which includes the new UI, native histograms, OpenTelemetry
compatibility, UTF-8 support, remote write 2.0, and
some breaking changes. There have also been several updates
and minor version bumps since Prometheus 3.0 was released, so we will also talk
a little bit about some of those new introductions as well as
what's to come in the future. So let's start off with one of the
most discernible changes introduced in Prometheus 3.0, which is the new UI. The UI was completely rewritten
by Julius Voltz and it introduces a less cluttered, more consistent and
easier to navigate layout. This QR code will take you to a demo
so you can try it out for yourself. The old Bootstrap-based system has
been replaced with React and Mantine framework with a goal of a
more modern look and enabling better development and easier maintenance. There's also been many new features that
have been added as part of the new UI. One of the key features is the
new metrics and label explorer, which can help you build your queries. You can view and search through available
metrics and metadata for each metric. Then you can select the metric
and you can use the label explorer to drill down into the label
names and values of the specific metric and add label matching filters to
narrow down your desired result. This is also a feature that exists in
Grafana, if you use the Grafana UI. You can also use the query tree view,
which was adapted from PromLens. This allows you to break down any PromQL
query into subexpressions and includes inline documentation and metadata so
that you can see what each part of your query is doing. You can
click on each of the nodes, and see what it evaluates to and
also what label data exists in each subexpression. The explain tab can give you even
more context on a node within your query with explanations,
insights, and visualizations. Here, the explain tab is visualizing how
you're joining the series together by describing the match groups on the
left and right hand side of the binary operator. And the explain tab can also make
debugging a lot easier by providing explanations and visualizations of what
is going wrong with each part of your query. This is a feature that
Grafana does not yet have, but hopefully will in the future. Looking ahead, there's continuous work being done on
the UI and there's been a lot of work on graph views already to improve them, such as adding vertical lines
and clipboard functionality, and there's still more work to come here. And there's also some in progress
work on UTF-8 quoting and auto-completion, and rendering
native histograms and heatmaps. And next we're going to talk
about native histograms. So in general, histograms store distributions of
data points rather than raw data by storing counts of values that
fall between certain ranges, and they're often used for
quantile estimation. Historically, if you wanted to measure things like
latency of requests in Prometheus, you would use classic histograms. Classic histograms require
predefined bucket boundaries and they're represented and stored as
multiple time series in Prometheus. One for each of the buckets as well
as one for the count of the data points and one for the
sum of the data points. But there's quite a few
drawbacks to classic histograms. When it comes to defining
the bucket boundaries, it can be difficult to determine
ahead of time what would be appropriate bucket
boundaries for the data, and you may have to change it over
time, and when you do have to change it, it requires re-instrumentation
and re-deployment. It's also quite expensive to
store buckets because each one results in a new time series and
they also take up a lot of space. And because of this, many users will define only a few coarse buckets, and this can cause
inaccuracy in quantile estimation. Also, classic histograms can only be
aggregated if the bucket boundaries match exactly. We now have native histograms which
address a lot of the issues that classic histograms present. Instead of having
to predefine the bucket boundaries, the boundaries are calculated
based on an exponential scale, and this allows for native
histograms to be aggregated and merged together more easily. And the other big benefit is that
instead of being stored as multiple time series, they're stored as a single
complex sample that encompasses all of the data that you need. Here is a overview comparing
classic histograms and native histograms, but the key takeaway is that native
histograms are a huge improvement in efficiency for both cost and space. Here's an example of querying native
histograms in the Prometheus UI. This graph shows the bucket counts of a
native histogram and the boundaries of each of the buckets. And here's an example
of quantile estimation. This graph shows the 50th
percentile of a native histogram sample. Note that there's slight differences
in querying native histograms versus classic histograms. For example, you don't need to use the LE or less than
or equal to label when you're querying native histograms. Looking ahead, there's a lot of exciting
things to come for native histograms. There's also been a lot of updates
since the release of 3.0 and there's still refinements being
made in the text format and the operators and function refinement, and heat maps in the UI is
another feature to come. And there's another exciting new
feature that is in progress with native histograms, and
that is custom buckets. Native histograms with custom buckets
address the scenario where you might have a native histogram that
doesn't fit your data very well. It could be the exponential
scale won't fit the data, or it could be that you have legacy code
you cannot change the instrumentation of. So native histograms with custom buckets
allow for storing data in a single time series, but also using
predefined bucket boundaries. And this means that you can
convert classic histograms into native histograms with
custom buckets without losing any accuracy or loss, any loss of data.
And this can happen at scrape time, so you don't need to instrument. Alright, next we're going to
talk about remote right 2.0. Remote write is a protocol that
allows Prometheus compatible senders to forward scraped metric data
in real time to receivers. Prometheus can send and receive this data, and other monitoring tools
such as Thanos, Cortex, and Mimir can ingest the data
and then forward it to their own TSDBs or write it to their own TSDBs. This protocol has been widely adopted
by other open source projects and vendors, and it's been very useful
for realtime metrics streaming. The initial version was Remote Write 1.0, which sends data using
snappy encoded protobuf messages over HCTP and also uses back-off retry semantics based on the
receiver's response codes. Remote write 2.0 improves on
the efficiency and network
bandwidth and supports newer Prometheus features. It
still uses the protobuf over HTTP, but now it sends data by string
interning all of the label data and this dramatically reduces the request size. The spec also includes
fields in the data for new features in Prometheus, such as native
histograms and created timestamps. And there's also support for handling
situations where there's a partial write failure. So receivers can respond with the partial
write error statistics for different types of samples using HTTP headers, and senders can use these response
headers to log the errors and retry according to the code. Here you can see the massive improvements
in efficiency on bandwidth and serialization levels with remote write
2.0 compared with remote write 1.0. And in order to make remote write
easier to adopt in the long run, we have built an experimental library
in client-golang and this allows you to construct remote write 2.0 compatible
senders and receivers more easily without having to manually
ensure compliance to the spec. Looking ahead for remote write, the goal is to soon mark
it as non-experimental, and there's continuous work being done
for sending creative timestamps and addressing efficiency
issues with metadata. And one of the benefits of this flexible
new protocol is that we can experiment with various compressions and even
formats like Apache Arrow in the future. Alright, now I'm going to
turn it over to Goutham. Thank you Carrie. Yeah, so I haven't actually
written any code for 3.0, but I did do some other work like
spec work and OTel support is one of those. Yeah, again,
OTel gaining an option. We really like OTel, and
if you go back just a year, using OTel with Prometheus was
not great. Well, it was painful, but over the past year we've had a
huge push to support or OTel natively in Prometheus. And yeah, you can now push metrics into
Prometheus and I'm having weird feelings when I said that, but you can basically just post the OTel metrics
from your applications that are instrumented with OTel into
Prometheus. However, again, we don't want to default on this
because that will allow people to push random data into Prometheus. So you have to explicitly enable it with
this feature flag, but it is stable. Having said that, the spec for converting OTLP
data into Prometheus is still in flux and by default if
you just follow the spec, everything that's a resource attribute,
like namespace, cluster name, and things like that are sent into a
different metric that you have to join on to group things.
And this makes queries really hard. So we also added a nice config option
called promote resource attributes that you can kind of pick to just copy over these
resource attributes into labels. And then you can use these labels
normally just like you do with Prometheus data. For now, you just copy paste the snippet and all
the most common OTel resource attributes will just be copied as labels, but we are working on making the spec
better and actually doing it automatically without any configuration. The other thing is something
that Matt alluded to, which is UTF-8 support. So we really like OTel
and in OTel they use dots, which we did not support. So we were
like, okay, let's just add dots. And then we read the spec for
OTel and they said, no, no, we also support slashes
and anything UTF-8. So Prometheus can now
do UTF-8 metric names and label names and label values. You can see use emojis
and labels. However, you can also use emojis in metric names, which means you can have a metric that
is the graph emoji and then you can graph the graph emoji. I really like OTel, but sometimes to follow the spec we
have to do things that I don't like, but yeah, yeah. So again, this is implemented in the server
and a few of the client libraries. We need to enable UTF-8
support everywhere. The Ruby maintainers are looking for
help. So if you're a Ruby expert, we would love your help. We also want to use the type and
unit metadata in hotel very well. For example, if you are trying to do a
rate over a gauge, we want to tell you, "Hey, this is a rate over a gauge,
don't do that", and things like that. And we also want to understand
Semantic convention. So if you see a HTTP metric, we want to automatically
generate some insights around it, for example. We also want to
support Delta temporality. In Prometheus, the only thing that we
support is cumulative. So if
you're graphing the number of requests, it is basically we always store the total
number of requests that we've seen so far. However, if you're familiar
with StatsD, it just pushes deltas, or like Datadog, they push Deltas and OTel has
the ability to push deltas and we want to support them. Well, we kind of hacked it into Prometheus
with the feature flag. Well, we are not really happy about that
implementation and we want to natively support deltas. We still don't know how
to do that, but we're figuring it out. Yeah, putting it all together, you can see a native histogram from OTel.
There's a few dots in the metric name. There's also an underscore in
the metric name just because, and yeah, we are kind of evolving
all of this to make it consistent, but today you can push OTLP
semantic conventions and native histograms into Prometheus
and graph them with promQL. I think that's really cool. And here
comes everyone's favorite feature. I kind of want to say we
have no breaking changes, but then I'll get to the next slide
and we'll have a huge page full. However, these are only breaking changes
that we think or we thought affected extremely few people and these few
people, they can easily change them. So these are not really stop
the world breaking changes. And we wanted upgrades to
be seamless. For example, how many of you here use the holt winters
function? There you go. We broke it. So things like that. And then we actually ended up breaking people. So how many of you understand
what this does? Okay, very few people. Well, we broke you too. So essentially what this does
is it just the first one minute says, get every kind of run a query
that gets full for every one minute, get a data point for every one minute
and then select the last one minute, and then you can do a rate of
it, rate on it. Before we used, we used to kind of include
both the first and last point. And in rate you need two points
to calculate the rate. Before, these queries used to work. And
then for consistency and efficiency, we kind of said, oh, actually it doesn't really matter if
the last point is included because how often is it to kind of have a one minute
window and one minute scrape interval and it all just lines up
to the milliseconds? Well, if you use Grafana for caching, it
lines it up to the milliseconds. So things that used to
work before did not work. Well, this we have no fix for, just don't do this where
everything is lined up. Just one minute, one minute
or five minute, five minutes. The other thing is we have something
basically we, when we scrape, we say, Hey, what protocols do you support? And if
we find something that we did not really understand in the answer, we just used
to default to PrometheusText0.0.4, and we were like, oh, actually
that's very, very old. Let's just default to something else. And then only if we don't understand
the protocols that are supported. Turns out Sinatra, I think,
which is a Ruby client, sent us commas instead of semicolons. And before it used to work
and then it didn't work. So we kind of broke those
users, they fixed it. But if you run into
this issue with Sinatra, you can still kind of
configure this. Alright, the next thing has nothing
to do with Prometheus 3.0. It has been my pet project
for the last two years. I thought it'll take me three months.
Well, two years later, here we are. So if you kind of look at it, this is the number of commits over
many multiple versions from 2.5 to 3.0 in 3.0. We have a lot of things. One thing is that these graphs
are more or less consistent, and this just shows that
Prometheus is still a very active project. But again, I became a PM and I
was like, all my metrics need to go up. So one of the things that we noticed is
while we have a very healthy and active project, we have failed to attract
new leadership into the project. This was basically limited
by our current governance, which just says to change the governance, we need two thirds of the majority
to kind of agree to this change. So as we kind of increase
the size of the governance, achieving this majority becomes harder
and harder. So just as the number grew, the bar got higher. So for the
longest time we added very few people. And again, I wanted to change that and
get to a million maintainers. We'll see if we'll get there. But yeah, first thing we did was we actually
looked at all the active maintainers and added them so that they can vote for
the new governance. It's kind of funny. It's like, Hey, come on in, in three
months, you're not part of team anymore. But yeah, well, it's been
six months I think now, and they're still part of team. But yeah, we have 22 new members and
they're not new. Actually, they have been consistently contributing
to Prometheus for many, many years, and we've just decided
to just add them all. Well shout out to every single person
and all the contributions that you've and everyone has made. Cool. So yeah. Yeah, I've been working on Prometheus Governance
2.0 that kind of looks like this. Everyone who's did anything including
doing a thumbs up on the release page is a contributor. You are
a contributor to Prometheus. If you've contributed clap
for yourself. And then, yeah, there you go. And then, yeah, anyone who is kind of maintaining
repos or sub-projects or folders, they are maintainers. No, wait, no, wait.
Okay. Sorry, I missed the member part. Yeah, if you have 10 contributions
over a 36 month period, we will add you to the GitHub
org so you can become a member. You can have a lot more say in the
project and you can also brag about it. So we want to increase the number of
people that can call themselves Prometheus org members. And this is something that's important
to us to have a nice stepping stone before you become a maintainer. And then
maintainers are those that have commit rights and push rights, and basically
they maintain the different exporters, client libraries, and different parts of the
Prometheus and alert manager server. And then the members will elect a steering
committee of five to seven people. And the steering committee basically has
the right to change the governance so we can have a thousand members
having a say in everything without actually deadlocking on
the governance. Well, this is kind of approved, however, we are still figuring out how to
vote for the steering committee, so we're going to have a vote to figure
out which voting mechanism to use. Yeah, so that's kind of where I'm stuck. It's like the last 5% is taking
95% of the time. With that said, I don't think you should wait for
the new governance to get involved. Get started now. We are
still adding maintainers, we are still adding new
members into the team, and we have a lot of work for you, especially all the work that we've
started with 3.0 and we actually never finished any of those. So there's a lot of work and
a lot of different channels on the CNCF slack, just search
for Prometheus. In the CNCF Slack, you'll see a lot of different channels. If any of these sound interesting to
you, basically just reach out and say, "Hey, I have some free time.
I would love to contribute. How can I contribute?" And we can
kind of walk you through this.

