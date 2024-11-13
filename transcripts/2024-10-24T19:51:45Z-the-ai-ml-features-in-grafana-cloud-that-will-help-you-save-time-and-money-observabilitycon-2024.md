# The AI/ML Features in Grafana Cloud That Will Help You Save Time and Money | ObservabilityCON 2024

The Grafana Labs team believes that AI/ML can be used to help save toil, time and money. In doing so, we're able to help ...

Published on 2024-10-24T19:51:45Z

URL: https://www.youtube.com/watch?v=HPH8RW6VnI0

Transcript: All right. So hey everybody.
My name is Jen Villa, director of product here for
databases. And I'm Edward, an engineer on the AI/ML squad. And we're gonna be talking to you about
how we're applying AI and ML in Grafana Cloud to save time to and money. This is our QR code for Q+A.
So please give it a snap. We'll have some time at the end hopefully
more time than at the keynote where we, we ran a bit over, but
time at the end for questions. All right, so let's start by talking just kind
of high level framing the problem. I think of automation as about
freeing up human potential, right? As about taking time that we used to
spend on rote tasks and free giving us time to instead spend on more
creative, innovative work. The example I've laid out here in the
images is if you think about information distribution, we started
with monks in monasteries, copying text by hands, and we came up with a printing press
allowing for mass distribution of printing materials. Fast forward
another a hundred years, we automated even further and
we invented the internet, right, which gave us global instant
distribution of information. I won't say that we fully automated
away of the need for written materials 'cause I still love a good
book or my Sunday crossword, but you can still see kind of the
progression that we have managed through automation. Now, when we think about
AI/ML, I think of that as a tool, a technique for automating, automating things that we
never thought possible before. New problems that we can
tackle with automation. And we see this happening in so
many demands, right? In healthcare, we see it analyzing imagery
to give us diagnoses. We see it helping us understand
how proteins are gonna fold. We see it in finance to
detect fraudulent activity. We experience it daily as consumers, giving us better customer service
interactions, better recommendations. And yes, I use it to help
me write the many, many, many emails that I write
as a product manager. Since I'm unlike Edward, I, I do not do
anything effective like writing code. I, I just write emails and
slacks . Now, when it comes to observability, we talked yesterday about how we
think the main impact of AI/ML in our industry specifically, is that it's gonna allow you to scale the
promise and the power of observability across your entire organization
so that it's not just specifically localized to the couple
of expert practitioners, the couple of veterans that you have. You make that power and that
promise available to all engineers. And I think what's especially unique and
specific about how that's gonna happen is that it's going to help
engineers identify and fix problems in complex distributed systems.
And that change, I think, honestly couldn't come fast enough
because at the same time that we're seeing this trend, we've also seen over the past few years
the trend where more and more companies are moving away from a monolith
to a distributed system. And why has that been happening? That's been happening because we want
to make software engineering teams more and more effective
and efficient than ever. We wanna empower them to ship changes
to all of your customers faster so that those customers have a better experience. So we've taken these large monoliths, we've started breaking them apart into
many different decoupled services, and that allows each team
to move much more quickly. But there's a trade off there, right? As we've made that move to
these more distributed systems, we've introduced more complexity.
So look at this node graph, right? With all these different entities
and connections between them. And what that means is that
when something goes wrong, it can be a lot harder to figure
out what's going on, right? A single request may ping through
services owned by tens of teams may ping between cloud and an on-prem data center. So there is a lot to
figure out about, you know, where's this problem coming from? And so that's where we think AI/ML is
gonna be a critical tool and technique in helping engineers take in that ever
increasing complex complexity and figure out what's going wrong. Now, now that I've blabbed at you about
the theoretical impacts for a while, I'm gonna pass it over to Edward, who's actually gonna give you some
examples of how we're applying AI/ML in Grafana Cloud to help you all
root cause problems faster. Thanks, Jen. So building off of the
AI/ML theme of saving toil, we've been building features throughout
Grafana that will make your day-to-day easier. So many of our time spent within
Grafana is troubleshooting and put simply. Troubleshooting
is complicated. Looking for that signal in
a sea of telemetry data is a big challenge sometimes. So I'm here to share some new and
existing AI/ML features within Grafana that helps essentially help you identify
and fix problems faster. So these features are available throughout
the new explore apps as well as sift. They're both available free in
cloud and some are available in open source as well. So the first challenge we have is that
our logs are often noisy and verbose. It's not fun scrolling through
pages and pages of the same thing, looking for that needle in a haystack. So here's an example of some logs
I was looking at the other day. You can see maybe there's three
or four distinct patterns, but it kind of sucks having to look at
every pattern repeated all the time. So we're introducing log patterns
to group similar logs together. So you only have to look at each pattern
once instead of looking at the same thing repeated. So this also allows us to keep a
trend over time so we can pick out the logs with high value when we are
actually looking for an issue. This feature is available
in one of two places. First in explore logs, we are highlighting the patterns so
you can find what you're looking for easier. We surface logs that has
log patterns within a given time range. So you can pick
and choose for the logs you're, you're actually looking for.
The second place is inside sift. So we surface log patterns with errors
when you're not sure what to look for yet, and we highlight the logs that have
had a large change in the 20 last 24 hours, as these are potentially new
error logs you want to be looking at. So the second challenge is that it's
kind of hard to understand time series. To understand time series, we
need to answer two questions. One, is this series behaving abnormally
compared to other series or two? What is a good threshold
for abnormal values in a series? Simply by looking at the series
themselves, it's hard to draw conclusions. And even when you spot a pattern, it's not always obvious whether
or not that's important. So our dynamic learning feature
consists of forecasting an outlier tries to pinpoint the anomalies
in the series you give it. You can find these in the machine
learning section under alert center. So alert detection helps answer the first
question by highlighting the abnormal series. In a group of similar series forecasting answers the second
question by trying to predict a plausible range of each series. So then you can use these range to
then apply dynamic thresholds for alerts. So these features
have been out for a while, but we're still making
constant improvements. One of the newest improvement we're
trying to make is to help you create forecasts easier. So on screen, you see as soon as you make
any changes to the model, the UI reflects that change. So third challenge we're gonna talk
about is looking for trace spans. So traces allows you to follow a
request as it traverses your stack, and each span gives you
represents one operation in this request, it offers things like duration
errors and any metadata traces offer great insights
into your application. But the best kind of traces are often
the ones that have tons of spans. And looking for that important
spans in a deep trace is a big challenge sometimes. So to help you find that
interesting span without digging, we've enabled our Sift feature to
track spans of interest, for example, spans with errors or high latency spends, Sift will then highlight any spans
with a big change in behavior. So this is done by comparing the, the the volume of spans in
the investigation period
against the volume in the last 24 hours. So slow spans and area
pans are still a working in progress, but should be available
in the near future. The fourth challenge is
understanding profiles. So profiles measure the use
the resource usage, say CPU, and memory of an application over time. We visualize profiles using flame graphs, which are stacked bar graphs highlighting representing function calls
and their resource usage. Flame graphs are great to look at, but
there's a lot of information to unpack. So we built a flamegraph
explainer inside of Explore Profiles to help you
quickly get started with profiles. This explainer will highlight any
issues, root causes, bottlenecks, and recommend fixes. So flamegraph, explainer first processes, the profile
only keeping the important bits, feed that into an LLM and ask it to
digest it and provide recommendations. So flamegraph explainer is
available open source inside of Explore Profiles. Now extracting insights from
raw telemetry data is valuable. We're even more excited about AI/ML
capabilities that we can build on top of these insights. So let's
start with alert. You get, you get an alert, you
suspect something is wrong. We currently have a ton of tools to
help you figure out what's wrong, but as Jen mentioned earlier,
your system gets complicated. There's so many signals, so many
noises, can we do better using ML? So here's a sneak peek of something we've
been working on internally and testing we call it service level explanation. So we get an alert saying
that the machine learning prediction service is having issues. So our model immediately starts
scanning all the observability signals. So by the time you start
looking at the issue, we've already displayed something. So first we're displaying a surface
dependency graph and each component is highlighted with a value
of zero to one highlighting the probability of contributing
to the current issue. So this model has highlighted celery
worker and Redis as two internal dependencies as well as off API
and gcom as external upstream dependencies. So below the graph, we show potentially top metrics
that contribute to the error. We can click on the metric
to see the time series, or we can click on the service
name to go to the logs. So let's quickly take a look
at logs for the celery worker. So we noticed some errors
in the past 20 minutes, and we look at the errors
and it shows that Redis the, the worker has issue
connecting with Redis. So let's try to verify this by
looking at the logs for Redis. And we can see that Redis
has shut down recently. And looking at the Redis metrics, we can see that the metric
stopped emitting completely . It's dead. So essentially this the model
was able to narrow down where the issue is without us having to dig. We're currently only showing the
surface graph and, and the top metrics. We're hoping to incorporate other
signals in the service as well. We're seeing promising results
internally and hope to release it in Grafana cloud in the near future. So now I'll pass to Jen to talk more
about how we're using AI/ML to make observability more affordable than ever. Thanks Edward. All right, Edward got the cool stuff about how
we're using AI/ML to improve root cause analysis. I get the more boring
stuff about saving money, but I'm also kind of weird and, you know, I think that the saving money part
can also be pretty fun and exciting. And so I'm gonna talk to you about is
a little more depth into what we went yesterday. And the keynote is about how we're
applying AI/ML via our Adaptive Telemetry strategy to help everyone adopt
observability at greater and greater scale because we're making it more
and more affordable than ever. And touching back on
what we hit on yesterday, not only do we want to increase
the cost effectiveness of observability, we want to empower all engineers at
your organization to participate in that mission of improving
your costs, right? We don't just want that to be
in the hands of a select few. Adaptive Metrics. So you would've seen the stats yesterday
at the keynote but just calling, calling them out again, we've really been impressed with the
amount of adoption that we've seen around this feature. If you translate
that 640 million into series saved, that's gonna be tens of
millions of dollars saved
across our customer base every year. Now, what's really cool is that since the
launch, we've continued to improve, in particular our recommendation service
that is the service in which we are identifying metrics that are
candidates for aggregation. And so when I say improve, I
think it's really in two areas. So one is around the sophistication
of the recommendations that we're able to make. Most recently, for example, we've introduced the use of ML
to calculate confidence scores, which actually allows us to figure out
if a particular query that was run at your organization, should we really consider that when we
think about whether or not a metric can or can't be aggregated, right? Because sometimes you might query a metric
just to like kind of know what it is a little bit or see what it exists and
maybe it doesn't make sense then to say, Hey, I can't aggregate this metric
at all because of that one query. We're also making the recommendation
shop more and more real time. Now we can detect changes in your
usage. Maybe someone adds a dashboard, someone adds a new alert within the hour, and we will immediately regenerate
our recommendations from there. In fact, internally we have developed so much
confidence in the recommendations that we apply them ourselves. Any new ones that come up
daily with no human in the loop that means that we're dynamically
aggregating and disaggregating our metrics as a company. Now we totally understand different
customers may choose different approaches. They might want more manual control. But another thing that I think we've
developed to really help human operators feel like they're still able to use
their intuition to influence the recommendation service is
our exemptions concept. So while the machine
intelligence is suggesting, Hey, here's what I think you should aggregate
based on the patterns I'm seeing, we also have this concept of
exemptions where you can say, Hey, this particular metric or this particular
label is very important to me as a company. I do not care what the
usage patterns are never aggregated. And so we apply that concept internally
and that's another part of the reason that we have felt confident to apply
these recommendations with no need for review anymore. Now we've made this automation available
to customers as a GitHub action. So we encourage those of you who
are interested to take a look, scan the QR code, it'll take you to our repo and see if
you wanna join us in the brave new future of auto applying your recommendations.
All right, I see some, some phones up. I'll give
you another five seconds. Alright, and now what I'm gonna do is go into
a little more depth on Adaptive Logs which yesterday we mentioned
is generally available, which means any of you can go into your
Grafana Cloud account and start using it today. Now let's start with
the numbers, right? Our, our early access cohort of customers
is already cutting log volumes. We're seeing anywhere from 10 to 60%. I think you looked at my number
in the keynote yesterday. We said expected 40 to 60. That's because we see most of the
customers kind of gravitating towards that larger number. Internally we're reducing
our own log lines ingested by 40%. What you see here is actually
a time series graph showing the rate at which we've been
reducing our ingestion volumes. You can see when we started, we started pretty conservatively
trimming the ingestion rate by about 10%. We got a little bolder,
we gone up to about 15, then we had to turn it off 'cause
something broke. But you know, that's software development.
Some time went by and then, you know, after we were like,
Hey, this seems to be working, no one else has really
shouted at us too much. You can see we cranked it up
to about 40 45 ish percent, which is where we are now. You can see obviously that number is
not constant because the log volume that our applications are throwing off right
is also gonna vary in response to load on the system. Now I talked about the results.
Now for those who are curious, we're gonna pull back the covers
a bit and go into how it works. This is a fake image that is not actually
the machine running Adaptive logs. Alright, so let's start
with the right path. So what's happening is
that on the right path, we are analyzing all the incoming logs
that you are sending to Grafana Cloud and we're using the ML algorithm
known as drain to extract patterns. We're running what we're calling a pattern
minor service and that that service function is to do that
extraction, those patterns, then get stored in object storage. What's really interesting is that Edward
talked about how drain is being used in both our sift feature and in explorer
logs. So it's the same algorithm, but we've actually changed the
parameters slightly, like you, you tune drain when you run it. Whereas with Explorer logs we've kind of
focused on trying to get a smaller set of patterns, right? You're in an incident, you're trying to look at what's
changing. With adaptive logs, we've actually tuned it to allow for
a longer set of patterns because there we're, see we wanna identify more potential
savings and you can kind of analyze and apply those savings over time, right? It's not gonna be a time
critical situation where
you're trying to quickly scan. So that's what it looks
like on the right path. And then what we land on is
a set of patterns and then a rough count of what is the volume
represented by that pattern. Now what happens on the read path, right? We wanna understand both how
much volume is coming in, but then what is the usage? How are you interacting with your
log lines that are coming in there? We are actually looking at the results
returned in every single log query you run, whether that's a database running it, whether that's an alerting
or recording rule running it, or whether it's just
someone using Explore Logs. We are looking at all of those
queries and then we're looking at the returned lines and we're counting, say I'm returning a hundred
lines in your query, how many of those lines match the
particular set of patterns that I have? And it's very important to note that what
we're looking at is not scanned lines but actually returned lines,
right? If you think of a log query, you may scan terabytes and
terabytes of possible lines, but you only end up returning the results
that say have some certain string, right? So there again, we're using this pattern minor service
that's gonna also update our patterns to say not only here is the
number of ingested lines, but also here's how many times that
pattern is returned in a query. And this becomes our basis for
generating recommendations. With a kind of rough rationale. How they come about is if you see a
pattern that is returned a lot in queries, we think that means it's
probably valuable to you. If you see on the other hand a pattern
that's generating a ton of volume but it never ends up getting
returned in any query you run, probably not that important.
I'll speed through that. And now I'm gonna take you through
our UI for working with adaptive logs. So here's what it looks like. You're gonna see Adaptive Logs
under the cost management section of Grafana Cloud. Let's start with
the patterns I talked about. So here's all of the extracted
patterns. You can see we have 600 or so. The next thing you can see is the volume. So that's the volume associated with
that pattern over the last 15 days. That's what we're analyzing right now. Then we're showing the query to
ingest ratio of that pattern. So in this case I ingested
3.4 terabytes of lines matching this pattern. And by the way, in terms of queries run
over the last 15 days, I returned roughly 350
x that volume in query results of lines that match this
pattern. So in that particular case, we're not recommending doing any sort
of dropping of log lines matching this pattern because we're seeing it
returned in queries so frequently. Then I could sort of scroll down to say
a pattern like this where we have the opposite kind of relationship where
we've ingested about over a terabyte, but we haven't done say
as much querying of it. Now there's kind of two ways that
you could possibly approach applying these recommendations. So one option
is you could say, I wanna do a quick, like let's do a batch apply. I love
this philosophy. I'm all bought in. YOLO. Let's do it  there at least we
have one thing that we think is a super helpful guardrail, which is that
you can set a maximum drop rate. So let's say 25% that lets you
set a ceiling on how much dropping we'll do. So say that we're recommending,
you know, in this case drop 79%. Well by using the max drop rate, we're actually gonna kind of have
25% as the ceiling. So if I set that, you'll see here it's 25% and
odd 79. So this allows you some, again, control as an operator. Like
what is it that I'm comfortable with? You know, maybe you don't like that.
Let's apply everything at once. You wanna be a little bit more cautious. Then I think we offer a bunch of nice
little features in the UI that makes it easier for you to review the
recommendations one at a time. So for example, we'll actually
break down for a particular pattern. Where are we seeing that pattern coming
from in terms of the specific service that is generating it, right? So it turns out a hundred percent of the
log lines with this pattern are coming from Loki, right? Same here, a
hundred percent are coming from Loki. You can actually then apply that
filter at the top level. You can say, show me all patterns coming
from the Pyroscope distributor. That's helpful. If you say no, "Hey, I really care about the
Pyroscope distributor. Maybe I recently introduced some changes
there and I wanna make sure I made, I keep most of those logs." You can also filter by
text in the pattern itself. So I only wanna look for patterns
that have the string request in it. That's helpful if you're an
engineer and you're like, hmm, I think maybe I introduce like a
chatty log line a couple weeks back. Let me see if that's showing
up in any of my patterns. So then it's kind of up to you. Let's say I wanna apply a
couple of recommendations here. I'm gonna just type in some
numbers random, somewhat randomly. You can quickly get a preview of your
projected savings by making these changes and you can then
go ahead and click apply. I would say the changes tend to take
effect in about five or so minutes. I'm not gonna make us wait here for
five minutes while those changes take effect. So instead I did this on Sunday. It was a trial run and what you can
see kind of roughly here over this five minute period is this was before I
applied a bunch of these recommendations. You can see this is a, you
know, bytes received total. So that's an ingest rate and you
can see how they're a dropdown my ingest rate from about 25 million
bytes per second to roughly, you know, 18 million bytes per second. Alright, can we go back to the slides? Alright,
I think that's pretty much all. I have my whirlwind tour. This is a QR code that would take you
to our blog post where we talk a little more about adaptive logs. And we would love to get your
feedback find Steven Dungan, he is our PM and Quentin our from
product marketing here and can talk to you more about the future in depth. And we're excited to continue to build
out the Adaptive Telemetry suite. So we have two already in ga and we're
actively starting on development of adaptive traces. All right.

