# How to Query Span Events with TraceQL | Tempo Tutorial | Grafana Labs

Span events provide many benefits and can help you improve your distributed tracing game. In this video, the Grafana Tempo ...

Published on 2024-08-15T16:57:01Z

URL: https://www.youtube.com/watch?v=bgQblHktS78

Transcript: Hey everyone, this is Jennie
Pham from the Grafana Tempo team. Today we're gonna talk about span
events and how to query for them using TraceQL. What are span events ? As the name goes span
events are part of a span. Take a look at this generic span that I
borrowed from OTel. As we can see here, events is a field inside the span schema. Also note that in the event schema
there are three fields, name, timestamp and attributes. But
why should we use span events? Can't we just add more spans
or more span attributes? Well, unlike span attributes span,
events have timestamps and span. Events are much more
lightweight than spans. This means you can add more span events
without worrying about bloating the size of your trace. So when should
we use span events? Well, there are many creative ways to use
span events. Here are some common ones. You can track your errors by
recording an exception event. Take a look at this trace. While
you can always log your errors. Recording an exception event means it
is part of a trace allowing you to track the error along the path of the request. While you can monitor
performance with span as well. Remember that events are much more
lightweight and can also be useful to monitor interactions with
external services. In this trace, we have two events to track a database
query and it looks like it only took around 60 nanoseconds, but we can use span events to also
track connection type to monitor network latency or read locks to determine whether
there's a locking issue in our path. OTel says that we can think of events
as structured logs and the advantage events have over traditional logging
is trace sampling which has more capabilities. Let's say that you have a bug
in your very complex algorithm. You notice that it only happened in
the first path going from service A to B, then to C and D. If you were to put log
lines in service C and D, you would see logs not only for
the path that service A takes, you'll also see logs for the
path that service X takes as well. Because service C and D
are shared by the two paths. Imagine there are tens of other
paths that share service C and D. You'll end up logging things that
you're not actually interested in and unnecessarily increasing your
logging usage. Not only that, but the extra logging without context
might make it even harder for you to track your bug. What if instead of
traditional logs we use span events, we can use head sampling to sample
only the path that service A takes. By doing that we can control where
and how much data we want to capture. Okay, we are on the explore page. If you're already familiar
with the TraceQL language, you might have already seen
the two scopes that we have, which is span and resource, right?
For example, resource.service.name. In the latest version of TraceQL, we have now also introduced
the event scope,.Pulling the OTel schema for events. There
are two intrinsics for events, which is timestamp and name To search by event name,
use the syntax event, colon, name. The colon here is for us
to specify that this is an intrinsic, the intrinsic
name and not an attribute. So the most common event
that we have seen so far are exception events. And exception events by definition
should have the name set to exception. So here we are, we are going to search for event
name is equal to exception. Please ignore the red swiggly line here. We have not yet updated the UI
to support the events scope, but trust me it it is
already working. So let's go. Wow. So we can see that this
synthetic data has a lot of events that have the name exception.
Let's look at a few of them. Okay, let's look at this one. Remember by clicking on the trace this
span ID here we can jump straight to the span with the event. And here we can see there
is one event with the name exception and we can see the
exception message and the stack trace printed up right here for us. Let's look at another example. Let's choose this one. Another
exception, another error, right? So in here again we can
see that there is an event here with name as exception.
Exception type number eight. And again we can see the stack
trace of how this error came to be. And something that engineers tend to keep track of is response type, right? So,
and I don't know exactly what the entire name of this event is, but it should probably have
something with response on them. So we are simply going to do
a partial match for a response and of course we got a match. Okay, here we go response end. It looks like in this
trace we are fetching a document and following this we can see that
there is a timestamp for when we start the fetch. Oh, and here is the response start
and the response end time. As you can see here, we have a connection start time and the
connection end time which we can use to monitor latency between services. And here we have the response start time
and the response end time which we can use to monitor the performance
of whatever operation is in here. Okay, now let's
move on to event attributes. Let's say that searching for
event name equal to exception gives us way too many results. Let's say you already looked at the
log lines and it tells you exactly what the error is. We
can simply search for the error using event dot and if we follow the
exception event schema, the exception message is where
the error should be reported. So let's see what is a common exception, exception error that we
could have? Let's see, something exhausted maybe oh, watch paint sauce. We can see here we have two
events and one of them matches what we are searching for,
which is exception message, resource or we searched for
exhausted and it matched partially with this event. So it seems like this service
needs someone to scale it up because we have already maxed
out all the resource on the service. Now that we know how to query for events, how can we make this
information even more useful? As you may or may not know, we
have an experimental metrics query that we can run. So let's say we are looking
for all of the errors that is happening right now. Okay, so why don't we search for all of the exception events and see what exactly the errors are. So we are
going to search for first, we are going to filter it down by name exception to find only the events that are erroring aka the exception event. The now we're going to pass
this in the new rate by experimental feature where
we are going to rate by the event exception message. Like now we should see the
rate of spans with at least one exception events in the span and
we are going to drill it down even further by having a
rate by function against event exception message And viola, right? And now we can see that in the
last hour we've had quite a few connection refused error
messages in our spans. How cool is that? So as you can see, querying for span events using TraceQL
is now available for our Grafana Cloud Traces users, but for our tempo, OSS users worry not as it will
be included in the next release. Thank you so much for listening
to me talk about benefits. I hope you find the demo useful
and I will catch you next time. Take care everyone in. Go Tempo.

