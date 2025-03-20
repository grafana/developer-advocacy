# Demo: Profiles Drilldown (Previously Explore Profiles) — A Queryless Experience for Profiling Data

Update: As of Feb. 20, 2025, the Explore apps (Explore Metrics, Explore Logs, Explore Traces, Explore Profiles) are now the ...

Published on 2024-07-18T19:40:09Z

URL: https://www.youtube.com/watch?v=_8SbNN5DRmQ

Transcript: Hello everyone. My name is Ryan, and today I am excited to introduce
something new - an evolution of what used to exist as the
Pyroscope app or the Pyroscope UI. If you've been using
Pyroscope for a while, particularly either a year
before now or earlier, you're probably familiar with this UI, which was something that we really
iterated on a lot in order to provide some value in people being
able to analyze their profiling data, group it by your entire system, be
able to see how it performs over time, look at labels - all of these
things that have become very important to continuous profiling. And this used to exist as a standalone
app that came with the Pyroscope server when you started running
it. And as of a year ago, we were acquired by Grafana. We joined the Grafana team where
now we have basically moved this Pyroscope app. We have
improved it in many ways, but moved it into Grafana, where
now it is alongside your metrics, logs, traces, load tests, the other
data that you have in Grafana. And this was one of the main reasons that
we decided to join Grafana because we really saw a lot of value in being able
to have your profiling data alongside all your other observability
data. And so this is the new UI. We also have kind of
revamped the flow of how you explore your profiling data, and hence why we have called
it the Explore Profiles app. And basically what this means is that
now whether you're going in for a very targeted approach for something
that you know is wrong, an incident you're debugging,
something along those lines, or if it's more of a proactive approach
where you're just exploring some areas where you can cut CPU costs
or some areas where you can save on memory resources. Regardless of which direction you're
going or, or which use case you're using. profiling for, this app allows you to
kind of go inany of those directions. And so I wanted to really quickly
go through what's different here. First of all, the concept that you'll notice is that
you're always sort of starting with the bird's eye view of something and presented
with some data that will allow you to choose where you want to drill
into. And so in this case you know, I've selected this rideshare
application as my favorite. Let's say there is an incident going
on in this rideshare application I can either choose profile types, labels, or the flame graph for this
application to drill into. Let's start with profile types. So basically what this allows you to see
is it allows you to see all the various profile types for this
application alongside each other. And this is something that we got a
lot of feedback on that a lot of people wanted to do 'cause let's say
for example, you're debugging. A memory leak, but memory leaks aren't
always totally isolated to memory. Maybe there's something going on in the
garbage collection that's affecting CPU or there's you know, some other
profile type that's affected. This allows you to kind of see all of
these either in grid form, in row form, see them all side by side in order to look into exactly what's
going on. And so in this case, let's say we are looking at CPU profiles
and we want to see if there's any particular labels that are important.
Now we can click on this labels button. Now we're looking at CPU profiles broken
down by the various labels for this application. In this case, we see
we have three. There's the region, the span name. This is an example where we are actually
integrated with our span profiles integration that lets you connect
trace spans with profiles. We also have the vehicle
tab here, whatever. But this really allows you to
see what's going on, again, from a high level view, see that the north region is consuming
more resources than the other two. We can select this, we can
drill in and we can even, still as we could before, compare
things. And so here I can, you know, compare two of those regions
side by side and in this case, get a diff flame graph and be able
to understand exactly what's going on. We also have our
explain flame graph feature, which uses the LLM map
in Grafana in order to provide LLM you know, provide explanations about what's
going on in the application. And so all of these things take
advantage of the various pieces that are already included in Grafana. And that's why we have
decided to release this here. So definitely try it out. It's available today and looking forward
to hearing your feedback. Thanks.

