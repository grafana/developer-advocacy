# How Grafana Alloy Works: Demo | Grafana

Watch this Grafana Alloy demo video to learn how you can get started. Grafana Alloy is an OSS telemetry collector that is 100% ...

Published on 2024-04-09T09:04:40Z

URL: https://www.youtube.com/watch?v=NrnLyDXpfq0

Transcript: Hello everyone. Today we're gonna
be discussing Grafana Alloy, doing a quick overview of it. Grafana
Alloy is a tool used to collect, enrich, and send telemetry data. It is compatible with a wide range
of telemetry types and backends, including Prometheus, OpenTelemetry, Loki, Pyroscope and Tempo. It is Grafana's OpenTelemetry
collector distribution. What it does and what sets it apart
from other collectors is we add what we call the Alloy Runtime on top of it. This allows us to take
parts of different projects, say Prometheus and OpenTelemetry,
that normally wouldn't work together, but we add them to our system,
wrap them in Alloy syntax, and create what we call components.
Let's take a look at a configuration. Here I have an Alloy configuration. Components are the basic building blocks.
They can have arguments and exports. You chain them together to build what
we call the programmable pipeline. At the top here we have
prometheus.exporter.self
with a label of agent, prometheus.exporter.unix
with a label of OSX. The dotted notation at the beginning
is the type of component and the second value is the label. That
creates a unique name. Each component must have a unique name. Top two components do
not have any arguments, but if we move to the
prometheus.scrape."scraper",
it has two arguments: targets and forward_to. Targets tells the scraper
what to scrape. In this case, we are using the exports from
the two Prometheus exporters, which would be the targets field. Then we forward that data to the
prometheus.relabel component, which has a rule where we add
processing server as an app name, and then we forward that
to the remote.right. If we
look at the remote.right, we have an endpoint direct to
Grafana Cloud. We have basic_auth, which is a username which we're pulling
from environment variable and a password that we're pulling from local.file.
Local.file has some arguments, a file name and then is_secret
because sometimes you may want to pull data to parse with JSON, or sometimes it's a secret and you don't
want to accidentally expose it in the UI. And then I have set the
poll frequency to one second for demo purposes. Normally
this is one minute. This means that every second it's
going to check that Alloy password and see if it's changed.
If it has changed, it will notify
prometheus.remote_write that, "Hey, I've got a new value for you!"
And it will update its basic_auth. Then if for some reason the Prometheus
remote.right had descendants that depended on it, it could
then tell those components. "Hey, I've got a value update," and it
would walk the graph of dependencies. And this is what gives
Alloy a really responsive, reactive nature to changes -
allows it to have a runtime configuration that's not simply static. I talked a little bit about the UI a
second ago, so let's take a look at it. You can see I've got something unhealthy. So this gives you a very high level view
of how your components are doing and what's going on. In this case, you can see a local file
password is currently unhealthy. Let's take a look at that. So at the top we have a local file
password. That's the type we can see. It's unhealthy. We have
a link to documentation. So if you need to look up any arguments,
and probably most importantly for us, you can see we have the latest health
message - which component is exposed, and give you debug information
about what's going on. In this case, we can see that I'm unable to read a file. I was playing around with files earlier
and I must have messed something up. Lemme go fix that. Okay,
I found the problem. I'm gonna give it just a few
seconds here to see the new value, find it and update it. Now, one great thing is the components
are built to be fault tolerant. So even though we didn't find this file, we did find it earlier when we started up, and that meant that that good value
persisted. We don't persist bad data. So let me update this. You
can see we are healthy again, and if I go to our list of components,
you can see everything is back to good. We can see that there is a graph here
that shows how all the components work together. There's also additionally, a cluster in here that's an
advanced topic for a different day. That's a very quick overview
of what Alloy is used for, the configuration and some of the
features of it. I thank you for your time.

