# How to Send Prometheus Metrics to Grafana Cloud Using Alloy | Ask the Experts | Grafana

"How do I push metrics using Grafana Alloy?" William Dumont from the Grafana Alloy team answers the question by showing you ...

Published on 2024-08-06T13:12:44Z

URL: https://www.youtube.com/watch?v=_MbB8IVKMfw

Transcript: Hi, my name is Will. I'm a software engineer at Grafana Labs
and I've worked on Alloy for about a year now. And we got a question in the YouTube
comments about how to send metrics to Grafana Alloy. So in this video, I will show a little demo on how
to collect Prometheus metrics and send them to Grafana Cloud
using Alloy. Yeah, for this, I have a little app which is
exposing some Prometheus metrics in the Docker container. And here, I have my Alloy config that
I already prepared a little bit and we'll make use of a new
feature called Live Debugging to edit this config. So for now, there are only three
Prometheus components. There is the prometheus.scrape component, which is collecting the
metrics from our target. These metrics are collected every three
seconds and are forwarded to another component called the prometheus.relabel. This component is used to edit
the set of labels attached to the metrics. In our case here, there is no rules attached to
our prometheus.relabel component. So it's only forwarding the metrics
directly to prometheus.remote_write. So right now it's acting only
like a pass-through component. And our prometheus.remote_write
is sending our metrics to Grafana Cloud using
some basic auth to pass the credentials. And finally,
we have this little block, which is enabling the
Live Debugging feature. This feature will help us to build
the rules for the prometheus.relabel. So before I run this config
I will do a little trick. I will break the pipeline actually. So I don't want the
prometheus.relabel component to send my metrics to the
remote_write directly because
I want first to be able to shape the labels the way I want before
they are stored to my database. So let's run this. So the
command is very simple, alloy run. Then I pass the path
for my config file and I set the stability level to
experimental. Now I can go to the debug UI that Alloy has. I see my three components.
I can check the graph. The scrape is connected to the relabel, but it's not connected to the
remote_write so I'm not sending anything, but I can check the relabel
one and open the Live Debugging tab. And here I see live the metrics
passing through the component so I can hit stop. And the way it works for this
component is that I see the set of labels before the
transformation, then a little arrow, and then I have the set of
labels after the transformation. So right now the set of labels
are the same before and after because I have no rules. But let's change this so
I can filter the data and I can see that on some of my metrics. So the golang_counter and
the golang_histogram metrics. I can see this that there is
a label foo and I don't want to start the metrics with
this label to my database. So I'm gonna add here a little rule and the action will be
simply to labeldrop. And the regex is foo. I save the file. And here I don't need to
restart my Alloy instance. Actually I can simply hit
this endpoint and this reloads the config. So the config is reloaded. I go back here. Here, I also
don't need to refresh or anything. I can just resume all clear
to make it easier to see. And now if I stop, I can check, for example the counter metric. So I see the foo label
before the transformation, but after the transformation,
the foo label is gone. So it was right after the address. It's
not there anymore. So that worked well. Let's see if I can do another rule. So I have a lot of metrics and maybe
I don't want to send everything to the cloud. So let's say I don't want
all these go_memstat metrics. So here I'm gonna add a new rule. And the way this component
works is that if a metric has no label after the transformation,
then it's filtered out. So I can do this by using the
drop keyword for the action. The regex is go_memstat. And here I'm gonna do a little mistake
on purpose because this happens a lot when you write rules
for the prometheus.relabel. So because yeah, regex is not always easy.
So I'm gonna forget a dot. And now source_label. So
let me check the label. So the go_memstat value
is on the name label. So I can just put it there name. And
now if I run this. Resume. Here, the go_memstat are still there, so it didn't work. So I
can go back to my rule, see what's wrong, forgot
the dot, save it, reload. And now if I clear, resume, now I can see that all these go_memstat
metrics are filtered out because after the transformation the label set is empty. So now I'm happy with my pipeline. I can simply
connect the component again. So remote_write.default.receiver. And now I reload one more time. I check the graph, they're
connected. Perfect. And now I can just go to Grafana Cloud. And after a few seconds I
should be able to see the metrics. And there it is. So the golang_counter metrics is there, and I can see that the foo label
that was there before is gone. And if I check the list of metrics, I can see that the go_memstat
metrics are not there. So the pipeline worked as expected. And that's it for the little demo on
how to build a Prometheus pipeline using the live debugging feature.

