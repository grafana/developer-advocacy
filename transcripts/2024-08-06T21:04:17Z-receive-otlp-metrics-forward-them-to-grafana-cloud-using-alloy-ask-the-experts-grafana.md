# Receive OTLP Metrics &amp; Forward Them to Grafana Cloud Using Alloy | Ask the Experts | Grafana

"How do I push metrics using Grafana Alloy?" In this part two video, William Dumont from the Grafana Alloy team answers the ...

Published on 2024-08-06T21:04:17Z

URL: https://www.youtube.com/watch?v=IRqQEzc0kvA

Transcript: Hi, it's Will again from
Grafana Labs. In the last video, we looked at how to send
Prometheus metrics from Alloy to Grafana Cloud. And in this
one we'll cover how to receive OTLP metrics from
your applications and send them to Grafana Cloud using Alloy. The setup that I have is that
I have an app instrumented with OTel, which is pushing some metrics to my Alloy. And Alloy will be sending the
metrics to Grafana Cloud. For this, I have four OTel components. I
have an OTel called receiver,.otlp, which is receiving
metrics in OTLP format via HTTP and forwarding the metrics to an OTel called processor.attributes, which can be used to transform
the attributes associated with a metric, but for now it's not doing anything
but passing through the metrics to an OTel called exporter.otlphttp, and this one will simply send the
metrics to Grafana Cloud using credentials exposed by
this OTel called auth.basic component. And finally, I have
a Live Debugging block, which is set to enable = true. And this is a new feature
that we will use to be able to build the transformations that we
want for the attributes processor, because I don't want to
send my metrics before I'm happy with the
attributes to the cloud. And when I comment out the endpoint. And I'm just gonna set
it to foo. This way, this component will not work
because there is no endpoint foo but it's not important because right now
I want to work on this part of the pipeline. So let's just run
this. The command is very simple, so it's Alloy run and here
I have to edit the path. So it's otel-ex. I set the stability to experimental
because the Live Debugging is an experimental feature. There we go. Now if I go to the Alloy UI, I can see my four components. So with
the graph, they're all connected. The metrics are received by the OTel
called receiver and then through the processor attributes,
through the exporter. And the exporter is using this auth.basic. So we want to work on this processor. And here I can click
on the live debugging. And here I see the metrics
passing through my component. So when I hit stop and I will take a look at the metrics.
So I have one called example_histogram, which is a histogram with
two attributes there and have another metric
called example counter, which has two other attributes. What we can do is we could
try to insert a new attribute. So for this, I want to add a new action. And the action is called insert. And the attribute will be called demo. And let's put the value, Alloy. Now I don't need to restart my Alloy. I can simply hit this reload endpoint to reload the config. Here,I don't need to refresh or anything
I can just resume clear to see better. And if I stop, I can see that I added
the attribute to the example_counter metric, and I also added this attribute
to the example_histogram metric. We could add a new rule to actually only add this attribute to the example_counter. So for this I would need an include block here match_type = "strict". Here I can choose between regex or strict, but I'm gonna just put strict
and I'm gonna specify which metric name I want to include. So in our
case, it would be the example_counter. There we go. And I made a little typo there, but if I reload, I can see through the live debugging that this didn't work. Because
now because of the typo, the attribute is not on example_counter
and it's not on example_histogram either, because I'm only including
the metric example_counter written like this. So
I can edit it, reload. Now, after I clear, I can see that my example_counter
metric has the attribute demo set to Alloy. And the metric example histogram
does not have this attribute. So this is the transformation I wanted and now I'm happy with my
pipeline. So I can simply uncomment my endpoint, remove this one, reload the config. Now
the errors should be gone and I can simply check my Grafana Cloud instance, look for the
example_counter metric. And if I run and the query
and wait a little bit in a few seconds, there should be
the, the metric appearing. And there it is. So example_counter
total has the attribute demo Alloy, which is what we wanted.
And now if I take one of the histogram metric, this one does not
have the attribute demo. So the pipeline did
exactly what we wanted. Thanks for watching this episode of
Ask the Experts. If you find it useful, leave a like, subscribe and leave
some feedback in the comments.

