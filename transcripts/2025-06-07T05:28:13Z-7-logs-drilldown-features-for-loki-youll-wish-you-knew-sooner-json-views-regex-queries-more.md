# 7 Logs Drilldown Features for Loki You&#39;ll Wish You Knew Sooner | JSON Views,  RegEx Queries &amp; More

Published on 2025-06-07T05:28:13Z

## Description

Learn about 7 powerful new features that transform how you explore logs in Grafana Loki. From JSON views and regex to ...

URL: https://www.youtube.com/watch?v=DS3tRR71RJE

## Summary

In this GrafanaCON presentation, Matias and Trevor, both staff engineers at Grafana Labs, discuss "seven features to make more out of Loki with Logs Drilldown." They highlight enhancements to Loki's log visualization capabilities, focusing on features such as Shard Splitting for faster querying, improved landing page flexibility, regular expression support for log searches, advanced sorting mechanisms, and new visualization options for JSON logs. Trevor demonstrates these features in action, showcasing how they enhance the user experience when navigating log data. The presentation underscores the importance of structured logging and introduces future developments, including a new storage format for Loki aimed at improving analytical capabilities. Attendees are encouraged to engage with the team for questions and further feedback.

# GrafanaCON Presentation Transcript

Hello everyone! It's a great honor for me to be here speaking at GrafanaCON. My name is Matias, and I'm a staff engineer taking care of logs visualization and Logs Drilldown. I'm here with my good friend Trevor.

**Trevor:** Thanks, Matias. Hi everyone! I'm Trevor, a staff engineer and Loki maintainer at Grafana Labs. Over the past couple of years, I have had the wonderful opportunity to be the point person from Loki, ensuring that our fabulous front-end team has all the data and APIs they need to make Drilldown an amazing product. 

We thank you for that. Please take a moment to scan this code to ask us as many questions as you want. If we run out of time, you can always find us anywhere, so feel free to reach out and talk to us.

## Introduction

Today, we are here to talk about **seven features** to make more out of Loki with Logs Drilldown. Since our initial launch last year, we've seen a steady increase in the usage and adoption of our queryless experience for Loki. From there, we've been busy addressing missing pieces, making enhancements, and adding new features to help you find logs more efficiently and extract insights from them.

In this talk, we'll focus on a subset of these features that we believe will help you get more out of Loki. After our presentation, Trevor will follow up with a demonstration so you can see these features in action.

## Fetching Data: Shard Splitting

Let's start with an essential piece of the drill down experience: **fetching data**. **Shard Splitting** is a new way of querying Loki for metrics. It is particularly important when querying high volumes of data and wanting to see partial results faster. 

In early 2023, we introduced time splitting, which turns a single multi-day query into multiple individual one-day queries, providing faster results for each of these partial responses. But what if you're not querying more than a day and still want to see faster partial results? In Logs Drilldown, we utilize a feature called **automatic stream sharding** to split them even more.

Automatic stream sharding works at ingestion time by adding a new label to your stream called **Stream Shard** that takes a numerical value. This value is increased to keep the logs within your stream below a desired rate. When querying Loki for metrics, we first ask for values of `stream_shard`. If we receive values, we group them and start querying them individually, progressively enhancing the time series.

So, we now have a great way to get faster partial results. Now, let's move to the next step of our drill down exploration.

## Landing Page: Always See Logs

One of the main objectives of the drill down experience across different apps is to **never see an empty screen**, which for us means always seeing logs. In the initial version of Logs Drilldown, we focused heavily on the services concept to organize the logs on the landing page. While this proved helpful for some users, we soon learned that we needed more flexibility to accommodate the vast number of use cases our users have.

Now, you can start from a service label, a combination of labels, or even a completely different label. You can use any number of labels as well as multiple values within a single label. This flexibility enhances your experience on the landing page.

## Details and Breakdowns: Regular Expression Support

Now that we've selected the source of our logs, we’re ready to move to the details and breakdowns page, where we will discuss the next feature: **Regular Expression Support**. Regular expressions are essential when searching for logs. 

As you can see in this screenshot of our line filters, you can enable a toggle to use regular expressions to search through your logs. This capability is not limited to line filters; you can also use regular expressions in other filters for fields, parsed fields, and structured metadata for labels.

## Sorting Logs

After applying various filters, including regular expressions, it's time to focus more on the logs and see what we can do with them—perhaps sorting them by some criteria. In Logs Drilldown, we utilize a new query attribute called **direction**, which can take two values: **forward** and **backward**, when logs are sorted with the newest first.

When sorted with the oldest first, we query in the forward direction. This guarantees that every time you're looking at logs, you’re essentially looking at either the newest or the oldest. This can be easily seen in the logs volume panel, indicated by a blue shade called the **visible range**.

## Visualization Options for Logs

Now, let's focus on the logs themselves and discuss log visualizations. Logs serve a variety of use cases and are created under many different circumstances. You might be responding to an alert, dealing with an incident, or simply exploring your data. 

To visualize the logs effectively, we provide multiple options that cater to these varying use cases. In Logs Drilldown, we have the **logs view** and the **table view**. The logs view emphasizes the content of your log lines and has display options to utilize your viewport effectively. The table view has a columnar structure where you can add, move, and remove columns and change their sort order.

We are also introducing a **third experimental visualization** specifically designed to display and filter JSON logs. This is a great example of Loki and Grafana working together seamlessly.

**Trevor:** I can tell you that nobody enjoys looking for a field in a squished line of JSON. We're excited to announce this new view, which allows you to inspect any field, add them to your query to filter by them, expand nested objects, and change the root node.

This required a small change to our JSON parser in Loki, allowing us to keep track of the JSON path to every node as we parse it. This way, when you change the root node in the view, we rewrite the query to show just that one nested object across all the results.

## Patterns for JSON Logs

Another exciting feature for JSON logs is **patterns**. Initially, we couldn't implement patterns for JSON because of the complexity and length of JSON logs. However, our solution was to stop trying to tokenize the entire structure. 

A lot of JSON logs have fields such as message, event, or summary. We have a default list of fields that we will automatically run patterns on, but if your field is different, you can configure that using a specific configuration value.

We're thrilled to bring patterns to JSON logs, as they are a great way to quickly find interesting insights.

## Advanced Sorting Mechanisms and Numerical Filtering

Lastly, I want to discuss our **advanced sorting mechanisms** and **numerical filtering**. Our breakdown tabs for labels and fields offer high-level visualizations of your logs, such as product metrics of different values they contain to aid in further drill down.

If you're unsure about what you're looking for, our advanced sorting mechanisms can help. We offer various sorting options for time series data, such as those with the highest spikes, lowest dips, or widest spreads, which calculate standard deviation. You can even use machine learning algorithms to sort your time series based on change point detection or outlier detection.

When your fields contain numerical data, such as durations or sizes, you can filter by specific intervals. This is particularly useful for diagnosing slow operations.

## Conclusion and Demo

These are the seven features I wanted to showcase today, and now we are ready to move to the demo.

**Trevor:** Thank you, Matias. This is some impressive work. As a Loki maintainer, I feel comfortable writing LogQL, but even I feel supercharged by what Logs Drilldown empowers me to do. It’s my first go-to for logs.

In this demo, I aim to show the importance of structure in log data. Logs Drilldown is the best way to drill into your logs, regardless of their source. Grafana, as you all know, is a big player in the observability community, and we're excited about the portability that OpenTelemetry is bringing to logs.

Let’s switch to the demo.

As you can see here on the landing page, these little green dots represent the sharding work. The data is progressively loading, allowing you to start seeing patterns before all the data is back. 

Currently, we are displaying services, which is the default layout. However, you can change the dimension you want to start with. For example, if you are interested in searching by Kubernetes namespace, you can select that.

Here, we have two instances of the same application, one with additional metadata from the logging framework and one without. Clicking on the one without additional data shows a typical logging pattern. 

Even without structured logs, patterns are still useful, as you can see when I click on the patterns tab.

Now, let's make a small change to the code to add some structure and see the difference. Here’s the same log line, now with added variables as attributes. When I click on a log line, I can see all sorts of attributes specific to that log line.

This allows for much more detailed drill down. The structured data enhances your ability to analyze logs significantly.

In the table view, you can customize your columns to display only the relevant data you care about.

Switching back to the logs tab, you can see how we automatically detect data types and present them differently. For instance, prices are shown as averages over time.

I hope this demo highlights the features and capabilities of Logs Drilldown. Everything you saw today is available at play@grafana.org, where you can explore these features with tailored data.

## Future of Logs Drilldown

**Matias:** Now, what can we expect from Drilldown in the coming months to year? We are creating a brand new version of our logs visualization with many new features like highlighting and new filtering methods. We're also working to improve the default visualization for logs coming from telemetry to ensure no important data is lost.

Regarding Loki, the most exciting thing we are working on is a new storage format to replace chunks. This new columnar-style data format will enhance key-value searches and hopefully expand our query language to empower analytical use cases.

We want Loki to be the best logs database for observability and analytical use cases. Stay tuned for more updates, and we hope to discuss these features further at next year's GrafanaCON.

Please reach out through our repositories and community Slack channels (#Loki for Loki and #logs-drilldown for the queryless experience). We look forward to your feedback and feature requests.

That's all! Thank you!

## Raw YouTube Transcript

Hello everyone. It's a great honor for
me to be here speaking in GrafanaCON. My name is Matias and I'm a staff
engineer taking care of the logs visualization and Logs Drilldown, and I'm here with my good friend Trevor. Thanks Matias. Hi everyone. I'm Trevor, staff engineer and Loki
maintainer at Grafana Labs. During the past couple of years, I have had the wonderful opportunity to
be the sort of point person from Loki to make sure that our fabulous front
end team has all the data and the APIs that they need to make drill
down such an amazing product. And we thank you a lot for that. Please take a second to scan this
code to ask as many questions as you want if we have time, otherwise
you can find us anywhere. So just feel free to
reach out and talk to us. So we are here to talk about
seven features to make more out of Loki with Logs Drilldown. Since our initial launch last year, we've seen a steady increase in the
usage and adoption of our queryless experience for Loki. And from there we've been super
busy addressing missing pieces, making enhancements, and adding new features in order for
you to first have great tools to find the logs that you may be
looking for. And second, have tools also to understand the
data and extract insights from it. In this talk we're going to focus on a
subset of these features that we believe they will actually help you for
this specific purpose of getting more out of Loki.
When you use Log Drilldown after we introduce these features, Trevor is going to follow
up with a demonstration so
you can see them in action. So let's start with an essential piece for the drill down experience,
which is fetching data. Shard Splitting is a new way
of querying Loki for metrics. It's of special importance when you're
querying high volumes of data and you want to see partial results faster. In early 2023 we
introduced time splitting, which turns a single multi-day
que into multiple individual one day queries, getting faster results for each
one of these partial responses. But what about other scenarios? Maybe you are not really using
more than a day and you want to see partial results faster. In Logs Drilldown we make use of a
Loki feature called automatic stream sharding to split them even more. Automatic stream sharding
works at ingestion time, by adding a new label to your
stream called Stream Shard that takes a numerical
value, which gets increased, keeping the logs within your
stream below a desire rate. So when it's time to
query Loki for metrics, the first thing that we do is we
ask Loki for values of stream_shard, which can be none, in which case we fall back to the time
splitting method that I mentioned. But if we do get values, we group them
and we start querying them individually, progressively enhancing the time
series as you can see in this image. So great, we now have a great way
to get faster partial results. So we are ready to move to the
next step of our drill down exploration, which takes us to the landing of
logs drill down where we're going to talk about the next feature. One of the main objectives of the drill
down experience of the different apps is to never see an empty screen. And for us that means to always see logs. In the initial version of logs
drill down we focused heavily on the services concept to organize
the logs in the landing page, which proved to be helpful for some users. But soon enough we learned that we
needed to have more flexibility in our landing page to accommodate to the
huge number of use cases that our users have. So you may want to start from a
service label or a service label and another label or a completely different
label or any combination of them, which is now possible by the changes
that we made in the landing page. But not only you can use
any number of labels, but also multiple values
within a single label. Fantastic. So with this and
we are on the landing page, we selected the source of our logs, so we're ready to move to the next
step in every drill down journey, which takes us to the details
and breakdowns page where we're going to talk
about the next feature. Regular expression support is a
must-have when searching for logs. Here you can see a screenshot
of our line filters, which is our way to search
for strings within your logs. And now by enabling that toggle, you get access to use regular
expressions to search through your logs. But not only in line filters. You can use regular expressions
in other filters for fields, parsed fields and structure
metadata for labels and the line filters that I mentioned. So like I said, we selected the source of four
logs, we applied many filters, maybe using regular
expressions so it's now maybe time to focus a little bit more
on the logs and see what can we do with them, maybe sort them by some criteria. In logs, drill them when you use sort orders.
We make use internally make use of new query attribute called direction, which can take two values
forward and backward when the logs are sorted with newest. First we query in the backward direction, which means to your newest to the oldest. And when you change it to
oldest first we do the opposite. We query in the forward direction and we
query from your oldest to your newest. That way we guarantee that every
time you're looking at logs, you're essentially looking
at your newest or an oldest. This can be easily seen in the logs
volume panel with this blue shade that we call the visible range. The visible range shows the range of
the logs that are on display over your logs volume. So when the sort order is new with first
you will find it on the right and it will grow to the left. When you use infinite scrolling
and when the sort order is oldest first, you will find it on the left side and
it will grow to the right when you use infinite scrolling. So now I will like to move to focus
on the logs and talk about logs, visualizations, logs, storing log key serve a huge variety
of use cases and are created under many different circumstances. You
can be responding to an alert, you can be on an incident or you
can just be exploring your data. So for visualizing the logs, we wanted to have many options
that better accommodate you. Each one of these use cases, we have two ways of looking
at logs. In logs rhythm, we have the logs view and the table. The logs view focuses on the content
of your log lines on the body and has display options to make the best
possible use of your view port. The table has a colo nerve
structure when you can add, move and remove columns and
change the sort order of them. And we are now introducing a third
new and experimental visualization that has been specifically designed
to display and filter JSON logs. And this is a great example of Loki and
Grafana working really well together. So Trevor, what can you
tell us about JSON logs? Well, I can tell you that nobody has ever
enjoyed the experience of looking for a field in a squished
line of JSON altogether. So we're very excited
to announce this view. It allows you to, oh, can we go
back one slide there? Oh sure, no worries. So yeah, so in
this view, as you can see now, JSON the way that it's meant to be seen, you can inspect any one of the fields, you can add them to your
query to filter by them, you can expand nested
objects and you can also change the root node,
which is very exciting. So this required a small change
to our JS ON parser and Loki allowing us to keep track of the JSON
path to every node as we're parsing it so that as you change the root node
in the view here where we actually rewrite the query and we can show
you just that one nested object across all the results in your query.
But another exciting thing for JSON logs is patterns. So patterns we are very excited
to announce that this is now available for JSON as well in drill
down if you want to go to the next slide there, Mattias, when we
originally launched Drill Down, we couldn't do patterns for JSON because
JSON logs tend to be long and they have a lot of structure to them
and it blew up our tokenization for finding patterns. And so our solution to that was to
just stop trying to tokenize the whole thing. So a lot of JSON logs have a
field that's maybe the message or the event or the summary. You can see the default list of fields
that we will automatically run patterns on there, but if your field
is something different, you can configure that using
this configuration value. And so this is very exciting for
anyone who hasn't got a chance to use patterns yet because you have JSON logs, patterns are really great way to quickly
find interesting things in your logs. And so we're so excited to
bring those to JSON as well. Fantastic, thank you. And this takes us to the last thing
that I wanted to talk about today, which are our advanced sorting
mechanisms and numerical filtering. Our breakdown tabs for labels
and fields offer a high level visualization of your logs, like product metrics of the different
values that they contain to help you further drill down to find the
logs that you're looking for. But what if you don't really know
what you're looking for here is where our advanced sorting
mechanisms come to help you. We have many different sorting options
for our time series such as those with the highest spikes or the lowest
deep or the widest spread, which calculates standard deviation. And you can even use machine learning
algorithms to sort your time series, for example, most relevant uses change point detection
to sort your time series by dose that present the most changes and
outlier values. Use outlier detection to sort by those with the
most aligned values. I highly encourage you to
try them all. And finally, when the contents of your
fields are of numerical nature, such as durations sizes or
just numbers in general, you can be looking for specific values, but more often you're interested on
filtering by intervals. For example, you may be wanting to diagnose
a slow operation and now through our numerical comparison filters, you can do that and filter
by specific intervals. So these are these seven features
that I wanted to showcase today, so we are ready to move to the demo. Thank you, Matias. This is
some really impressive work. As a Loki maintainer, I feel very comfortable
writing LogQL as you probably, it doesn't surprise you, but even I feel supercharged by what logs drill down the powers that it
gives me and it's my first place to go for logs as well. So in this demo, actually could we go back to the slide
for just a quick second and we'll go to the next, if you could go
forward too for me. Awesome. So in a way to show off all these
new features I should say, I'm also hoping to show how
structure is important with logs data and logs. Drill down means the best way to drill
into your logs regardless of where they come from. Grafana, as you all know, is a big 10 company. And so we're really excited
about this sort of portability that the open telemetry is bringing
to the observability community and with this new standard, which is a great way to add structure to
your logs data and make your drill down come alive.
But with the new standard comes a transition. And some of us may be at various stages
of this transition to the new standard. And so that's what I want to
show off today and show a few different apps that are at various
stages of their hotel transition to tell a story about how we progressively
add more and more structure to our logs and bring drill down to life. If
we could switch back to the demo, do this live, hopefully it goes well. Awesome. So as you can see
here on the landing page, these little green dots,
this is that sharding work. So we can see that, I mean this is
fast because it's a small data set, but the data is progressively loading.
So as you have larger data sets, you can start to see patterns
before all the data is back. Right now on the landing
page we're showing services, which is the default sort of layout, but maybe you want to start by a
different dimension. Maybe for example, you're interested in searching for
things by Kubernetes namespace. So we can come in here and
we'll say case namespace name there and there's the e-commerce
namespace that I'm looking for. So let's go ahead and click that. Awesome. So I've now drilled into this and what I see here is two instances
of the same application and I have instrumented one with
additional metadata from the logging framework and one without. So
let's start with the second, the one without the additional data,
and that would be my shopping cart, hotel service. And there we go. So how many of you in the
audience are Java devs? Anyone? All right. That was me a few years ago, so you might recognize this
sort of logging pattern. That's how we used to log before we had
structured in our logging framework. And so that's how this app
is instrumented right here. And so when I click on a line, you can see that there is some metadata mostly coming from our
environment and stuff like that, but there's nothing specific
to that line itself. However, even for these types of unstructured logs, patterns are still very useful. So when I click on the
patterns tab, you can see, oh, here's payment method and
shipping method pulled out. Let's look at some of our
American Express orders. I can go ahead and include that pattern
and now when I look at the logs, I suggest those orders. Awesome.
So even without structure, the very beginning of this sort of
progression to adding structure, there's still value
there with the patterns, but let's make a small change to the code to add some structure and see
what that does for us and drill down. So here's an example of that exact
same log line where I've added all of the variables as attributes in
addition to having them in the log line. And so this can be seen
in our shopping cart. Structured hotel service
i's change over to that and I'll clear this pattern
now when I click on a log line, you can see that I have all sorts of
attributes that are specific to the log line such as price here or you have
shipping method, payment method. This gives me way more
dimensions to drill into. So when I go to something like the tab, I now have a lot to drill
into that I didn't have before when the data was not structured,
it was not enriched with metadata. Excellent. So going back
to the logs tab here, now that I have this additional data, I can pull out the
fields that I care about. So here's the table view. I can
go here and change my columns. Let's say I don't care
about that line anymore. Let's say I want to see the payment
method and maybe I want to see the shipping method. So then I can
go here and I see just those. And then what's cool is once you've
pulled this out in your table view, you go back to your logs view and
now you see just those fields. So this is really powerful if you might
have a lot of metadata coming into your logs and it's not all that you care about. Maybe as an app dev you
care about certain bits, you can of configure it to
be exactly what you want. One other thing I want to show over
on the fields tab is notice how we automatically detect what
type of data is in a field and we present it differently. So our price, instead of showing a plot of discreet
values, we show an average over time. And that's really nice And we can
also do some interesting filters. So let's say we have a problem with
large orders and you're dealing with it in an incident. So you're saying,
hmm, is this affecting everyone equally? Well, I don't know, let's look at
all of my orders over $700 let's say. And now let's see,
does any trend pop out? Whoa, look at this. Suddenly my
shipping country went just to us, so it looks like I'm only having a
problem with large orders to the us. So again, sort of this metadata really
enhances your ability to drill down. I did want to note in this example I
did have to repeat all that data between the log line and the attributes. This is something that we are actively
working on and hope to bring to drill down very soon. A more first
class experience for oel logs, being able to configure exactly what
parts of that log do you care about and you want to see. Alright,
switching gears a bit, let's clear all these filters. So some of you might already
have some structure to your logs. Maybe you are logging
in something like JSON. And so we can see some apps doing
JSON logging here in this GrafanaCON namespace. So the easiest thing to do if you have
JSON logs is just send 'em to Loki and we'll parse that structure
out at query time. And so if I were to look at the GrafanaCON and JSON OTel service, that's this one. That's what this one is
doing right here. Okay, so here we just have the JSON loglines
and this is where our fantastic new JSON view comes in. Much better way to view that
JSON we can filter by a specific method. So the patch method
just got added there. We can expand these nested objects. And then my favorite part is
you can change the root node. So now, and this was that sort of JSON parsing
feature I talked about earlier. So you see just that
across all of your logs, which in some JSON
environments that's huge. So I'm really excited about
that. Alright, and so yeah, this is actually rewriting the
query behind the scenes there, so you just get that log line. Awesome. So now one other thing I wanted to show
is that even though that these are JSON logs, we are indeed getting patterns. So you can go over here and this is
because I have a message field in here, but again that is configurable
to whatever your JSON like have so excited for
patterns to be there. Alright, another way that you can do JSON is
if you're using something like the hotel collector, you can parse
the JSON during the actual collection stage. And so this is how I have another service here, the GrafanaCON OTel service here. And the main difference here is it
allows you to sort of pull out a field, for example, during collection so it really can make
your log lines look a lot prettier. And then when you click on a logline, you see you still got all that same
metadata pulled out of that JSON. And so either way you choose to do
it, the metadata will be the same. Okay, cool. Let's dig into
these logs a little bit. So I'm going to go over to the fields tab. Let's see if we can
find any patterns here. Let's look at maybe the method pattern. And I will say this is demo data that is clearly repeating. So this may not be the most interesting, but by default we start with
the most relevant. Let's see, how about widest spread? Can
we see any difference there? Or maybe we want to look
at lowest dip. There we go. So it's changing the order of the
graphs and if you had real production data, this can be useful. Again, this is can data, but hey, I'm just happy that the demo
has worked so far up to now, so I'm not going to complain
about that. Great. So again, zooming back out, here's another example with the
bites field of us detecting this as a numeric. So we're going to show you an average
over time and then also give you the ability to add a comparison filter. This is great if you're searching for
something like with low latencies, high throughputs, low throughput, something like that.
So I can change this. It automatically recognizes
that these are bytes. So it gives me human readable values and
does all the conversions of behind the scenes. So you don't
need to remember, wait, am I multiplying by one E six or one E
three because I never remember any of that. Awesome. Okay, back to the logs tab and let's show off regex here. So I'm going to click
to enable a regex query. Let's look for all log
lines about teapots, look at all those teapots. And then the last thing
to show you right now, let's get rid of this
filter so we have less logs. You can see up here how many logs in
my total timeline am I actually seeing. So I just made that window smaller so
that I could show you that when I change to show right now I'm showing the oldest the
newest logs first and I just changed to show the oldest logs first. This actually rewrites the query changes
the direction parameter and the low key query so that you, it's not just
a UI treatment of we sorting them, you are actually getting the logs
from the beginning of the time range. So that went better than
expected. Everything worked. I don't know what was going on. I mean we made it! Everything I just showed you is
available on play@grafana.org. If we could go back to the
slides, there's a QR code there, it'll take you to Drilldown
with this data source selected. It's the explorer logs data source
play around with these features. The data there has been sort of
tailored to highlight some of this stuff that I just showed you. So play
with it. Let us know what you think. And in the meantime, Matias, what can we expect from Drilldown
in the coming months to year? Well, many things, but I wanted
to focus on two in particular. So like David said, we are creating a brand new version
of our logs visualization with many new features with highlighting,
with new ways of filtering logs. And it's now virtualized to get
the best possible performance. And we are already designing
log details and much more. So we're super excited about
this new upcoming new panel. And in addition, we are working to improve the
default visa decision of logs when they're coming from telemetry
so you don't lose any important data and what's coming to Loki. I'm going to try to go over this real
quick so we do have some time for questions, but the most exciting thing that we are
working on on Loki right now is a new storage format. This storage format, it's going to replace chunks and we're
really leaning into something that's more of like a column or style data format. And so what we hope is that
it's going to allow those key value searches by
selecting just a column, really empower those that will
hopefully lead to some query language expansion. And what we
really want there is, I mean right now Loki is the best logs
database for observability use cases. We also want it to be the best
database for analytical use cases. And so we're really targeting
that area. And then finally, Loki's never been great about finding a
very specific string in a very sort of wide stream selector. This sort of additional key value search
support will hopefully improve those needle in a haystack searches. So stay tuned and hopefully we'll be
here talking about all these features next year at GrafanaCON. Looking forward to that. And finally, please do reach out. You
know our repositories. So please ask question open issues. We really love talking to you and we
look forward to your feedback and feature request. And obviously a reminder to our
community Slack. We have two channels, #Loki for Loki and #logs-drilldown
for the queryless experience. So please looking forward to
see you there. That's all.

