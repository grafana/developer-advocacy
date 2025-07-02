# Grafana Alloy Deep Dive: Unifying OpenTelemetry &amp; Prometheus Pipelines, Fleet Management, and More

Published on 2025-06-07T05:38:01Z

## Description

Grafana Alloy is more than just a successor to the Grafana Agent—it's your new observability Swiss Army knife. Learn how it ...

URL: https://www.youtube.com/watch?v=Iqf_eRK3cAg

## Summary

In this YouTube talk, Ted Young, co-founder of OpenTelemetry and Developer Programs Director at Grafana Labs, alongside Johanna Öjeling, a Senior Software Engineer at Grafana Labs, discusses the integration of Grafana Alloy, OpenTelemetry, and Prometheus. They introduce Grafana Alloy as a high-performance telemetry processing tool that serves as an alternative to the OpenTelemetry Collector, detailing its features such as telemetry normalization, the ability to create new metrics, and the management of telemetry pipelines. The discussion emphasizes the importance of portability between different collector implementations and how Alloy supports native Prometheus pipelines for optimal performance. They also showcase the Grafana Fleet Management tool, which allows for centralized management and configuration of multiple Alloy instances, supporting efficient updates and troubleshooting. The presentation includes a demonstration of configuring Alloy to manage system metrics using remote configuration, highlighting its user-friendly interface and advanced debugging capabilities. Overall, the video emphasizes the evolving landscape of observability tools and the significant features that Grafana Alloy brings to the table.

# Grafana Alloy, OpenTelemetry, and Prometheus

Hello and welcome to our talk! Today, we’re discussing **Grafana Alloy**, **OpenTelemetry**, and **Prometheus**, and how we’re bringing them all together. Just a reminder, feel free to ask questions at the end.

My name is **Ted Young**, one of the OpenTelemetry co-founders and the Developer Programs Director here at Grafana Labs. Joining me is **Johanna Öjeling**, a Senior Software Engineer at Grafana Labs, working on the Fleet Management team.

## What is Grafana Alloy?

If you look at the back of the box, you'll see that Alloy is described as a **high-performance telemetry processing tool** and a successor to the Grafana Agent. But what does that actually mean, and why should we care?

The answer is that telemetry processing is a natural part of any observability system. As applications evolve from a **greenfield** state to **legacy**, our systems continuously grow and change, making telemetry a moving target. Over time, this leads to outdated formats and new services or data sources coming online with different formats. 

You may want to:

- Change and combine formats
- Normalize data emitted by libraries that have updated versions
- Address privacy and regulatory concerns, such as GDPR
- Create new metrics from existing data sources like logs and spans

Telemetry itself resembles a big data system. Large systems can produce a significant amount of telemetry, requiring us to operate that pipeline effectively with tasks like buffering, sampling, and load balancing. 

In essence, Grafana Alloy serves as an **observability Swiss Army knife**—a single tool that manages multiple facets of telemetry.

## Grafana Alloy and OpenTelemetry Collector

Grafana Alloy is also an alternative implementation to the standard **OpenTelemetry Collector**. To clarify, OpenTelemetry has a similar component that provides telemetry pipelines and processing, known as the Collector. 

To understand the relevance of Grafana Alloy as a collector, we need to explore the history of the OpenTelemetry Collector project. The terms “OpenTelemetry Collector” and “OpenTelemetry Collector distribution” have often been used casually, leading to some confusion. We decided to create a more rigorous definition to allow for alternative implementations like Alloy.

The challenge lies in what constitutes a collector. Is it strictly the codebase in the OpenTelemetry GitHub organization? In reality, many entities tweak or modify that codebase to suit their needs. We don’t want to limit the definition to just that codebase because it wouldn’t be practical.

Our goal is **portability**—to allow users to move between different collector distributions without a lot of work, fostering a coherent ecosystem rather than a fragmented landscape of competing projects.

### What Makes a Collector?

To qualify as a collector, it should support:

- **Collector components**: These are plugins, and users should have the freedom to choose which plugins they run, regardless of support contracts.
- **Configuration files**: Users should be able to carry their configurations when switching distributions, ensuring consistent behavior across pipelines.

### Why Does Alloy Want to Be a Collector?

Many users are already running OpenTelemetry and using the collector for their pipelines and processing needs. We want to support them by making it easy to switch to Alloy without significant effort. Alloy offers features not available in the upstream collector and aims to upstream some of them in the future.

One standout feature is **live debugging**, which we will demonstrate shortly.

## Demo of Grafana Alloy

Now, let’s switch over to the laptop for a demonstration. 

We'll explore the **OpenTelemetry demo project**, which you can find on [opentelemetry.io](https://opentelemetry.io). This demo includes various services loaded into a **Docker Compose** file, including the OpenTelemetry Collector. 

Here’s the Docker definition for the collector and its configuration file, which organizes receivers, processors, and exporters into a straightforward pipeline. All data from the demo application passes through this collector to the backend.

Once we start the demo, we can access it via `localhost:8080`, where we can see an observability store, which is a great tool to understand how OpenTelemetry works. We can observe services running in different languages.

While checking the collector, we can see logs indicating that data is being processed. However, interpreting these logs can be challenging. To gain a clearer understanding, we can replace the collector with Alloy.

### Replacing the Collector with Alloy

This is a drop-in replacement—we simply change the image to `grafana/alloy:1.8.2`. The command line differs slightly from the collector’s, but we're pointing it to the same configuration file. 

After redeploying, we can check the logs again to confirm that Alloy is running. One of the enhancements Alloy provides is a handy diagnostics tool that displays all currently loaded plugins, along with a graphical view of the pipeline. 

This graphical representation shows how data flows through the pipeline, allowing us to click into components to inspect their health and configurations. This feature is especially useful when developing and modifying pipelines.

## Features of Grafana Alloy

Now that we've seen how Alloy supports OpenTelemetry as a collector, let’s explore some additional features.

### Native Prometheus Pipelines

Alloy allows you to create **native Prometheus pipelines** for optimal performance. If your infrastructure exposes metrics in Prometheus format, you can send them directly to a Prometheus backend without needing to convert the data.

Alloy supports various popular Prometheus exporters, including:

- **Postgres**
- **MySQL**
- **Node Exporter**

To build a Prometheus pipeline, we use the Alloy Prometheus components. For instance, to export local system metrics, we can configure the `prometheus.exporter.unix` component and set a scrape interval.

### Fleet Management

Managing hundreds or thousands of Alloy collectors across different environments can be challenging. That’s where **Alloy Remote Configuration** and **Grafana Fleet Management** come in handy. 

With the Alloy `remotecfg` option, collectors can fetch configurations from a remote endpoint, allowing for centralized management. Grafana Fleet Management provides an interface to monitor collector health, inspect logs, and configure them remotely.

For example, if you need to adjust the scrape interval from 10 seconds to 60 seconds, you can do this centrally without reconfiguring each instance individually.

One of the standout use cases is **data collection on demand**. You can prepare configuration pipelines for detailed data collection and activate them as needed for troubleshooting, then easily switch them off afterward.

### Live Demo of Fleet Management

Now, let’s demonstrate how to configure a pipeline to export local system metrics from my MacBook using Fleet Management. 

After starting Alloy and connecting it to the Fleet Management UI, we’ll create a new pipeline similar to the previous example for local system metrics. 

Once we verify the configuration syntax, we can deploy it based on specific attributes. After activating the pipeline, we can refresh the Alloy page to see the new pipeline appear and its components’ health.

We can also verify that metrics are being sent to Grafana successfully.

## Future Improvements

We’re excited to share that we have plans to introduce further improvements to the Alloy UI and debugging experience. This includes:

- A live graph in Fleet Management for remotely configured components.
- A new tool called **Alloy Diagnosis** to analyze configuration pipelines for errors and optimizations.
- Continued investment in OpenTelemetry capabilities.
- Introduction of **OpAMP** capabilities for remote management of telemetry agents.

These are just a few of the features we’re excited to bring you—there's so much more to come!

Thank you for joining us today!

## Raw YouTube Transcript

Hey, hello, hello, hello. Welcome to our talk. Yes, this talk is going to be about Grafana
Alloy, OpenTelemetry and Prometheus, and how we're bringing 'em
all together. Just a reminder, you can ask questions at the
end. My name is Ted Young. I'm one of the OpenTelemetry co-founders, and I'm a Developer Programs
Director here at Grafana Labs. And I'm Johanna Öjeling. I'm a Senior Software Engineer at Grafana
Labs working on the Fleet Management team. Cool. Okay, so what is Grafana Alloy? If you look on the back of the box, it'll say that Alloy is a high performance
telemetry processing tool and a successor to the Grafana
Agent. So that's nice, but what does it actually do and
why should we be bothered to use it? And the answer is telemetry
processing is a natural part of any observability system, and that's because we
take these applications, we start in this sort of
beautiful greenfield world, and then they slowly move across
their life cycle into legacy. So our systems are constantly growing
and evolving and because of that, our telemetry is a bit of a moving target. And over time there's some cruft and
modifications and things that builds up, right? You have old formats, but then new services or applications or
data sources come online and they have a different format. So you
want to change formats, combine formats. You might have a library
that changes versions and the data, it emits changes a little bit, but you
still want the old dashboards to work, so you want to normalize
that data and massage it. You might also have privacy or regulatory
concerns that you're trying to deal with. And PPI is a really important concern
these days and all of these things are things you do in a telemetry pipeline. You also want to create
new data from old data. The most common thing here is creating
new metrics from other data sources like logs and spans. And then there's the fact that telemetry
itself is kind of a big data system. Big systems can produce a lot of telemetry
and you end up having to operate that telemetry pipeline and do all of the
normal things you would do with the big data system around buffering, reducing the amount of data you're
sending through sampling, load balancing, all of that stuff. And you want to
do all of those things in one tool. You don't want to have a bunch of
little tools all doing different things. Having one big tool that can manage
all of this for you is really helpful. So essentially Grafana Alloy is like
an observability Swiss Army knife. I mean you could call it an
observability Swedish fish knife, a little bit more accurate but
doesn't quite roll off the tongue. The other thing that it does though is
it works as an alternative implementation to the standard OpenTelemetry Collector. Why does it do that and what
does that actually mean? So OpenTelemetry has something
that's very similar to Alloy. It provides telemetry, pipelines and
processing and all of that stuff, and it's called the Collector. So how is it that Grafana Alloy is
also an OpenTelemetry Collector? To understand that I need to give a little
bit of a history of the OpenTelemetry Collector project. So
this is a little abstract, but I think it's actually important to
understand because you're going to hear the words OpenTelemetry Collector and
OpenTelemetry Collector distribution get thrown around. And it can be a little confusing about
what those terms mean because we've been using them somewhat casually
and colloquially in the past. And we decided a while back that we needed
to actually lock down this definition and make it rigorous so that we could
allow for alternative implementations like Alloy to exist. But it turns out when
you start to ask what a collector is, it's a little bit fuzzy. Same thing
with a collector distribution. The reason why we didn't have a strict
definition for these terms is it turns out it's not so easy to come up with one
that works exactly the way we want it to. You could just point at the collector
code base in the OpenTelemetry GitHub organization and say like,
that's the collector. But then when we look in the real world, there's all these things that we'd like
to call a collector that have had to take that code base and tweak it or
modify it in some way in order to make it work for them. So we don't want to say it has to be
exactly that code base that wouldn't be helpful to us. Is it a set of APIs? Another model
we could look at is the Kubernetes certification program where they
say if it quacks like Kubernetes, then it must be Kubernetes. So they
have a set of rigorous API tests. Anything that can pass this
API tests is Kubernetes. That doesn't exactly work for us though
because the OpenTelemetry Collector is a collection of plugins, we don't really want to say you have
to support exactly this plugin or that plugin. Even things that are
core to OpenTelemetry like OTLP, OpenTelemetry is native format. We don't want to say a collector
has to have OTLP embedded in it. There's plenty of reasons
why it wouldn't. For example, if you're running on
Lambda talking to X-Ray, you don't necessarily need OTLP. So we don't want to say that thing isn't
a collector just because it didn't have that particular API. What we've landed on was we want
portability. We want people to be able to move between these different
collector distributions without having to do a lot of work or feeling like
they're stuck on one distribution versus another one, right? We want it to
feel like one coherent ecosystem, not a fractured landscape
of competing projects. So we decided the goal here for
our definition was to allow these different collectors to be drop
in replacements for each other. As long as something could drop in
and replace another collector with the collector functionality, it was fine for it to offer additional
functionality that they didn't all have. So what is this functionality
that we want to support? The first are these collector
components. These are the plugins. Now, if you go to different vendors, you'll notice that they often say they
only support a certain subset of plugins, and what they're usually talking about
are SLAs or support contracts. They're saying if you use these plugins,
we'll provide you support. If it's just this random plugin you
found on the internet, not so much, and that's totally fair. But we do want users to be able to choose
which plugins they run regardless of that support contract. So it's very important that people
can write their own plugins, have their own set of
stuff that they're using, and if they switch collector distributions
to be able to bring those plugins with them. Related to that
is the configuration file. You're taking all of these plugins
and you're configuring them into these pipelines, and that can
get pretty complicated. You want those pipelines
to come with you as well. So it needs to be the case that if you're
moving from one collector distribution to the other one, that configuration
file is supported. And most importantly, the behavior stays the same between
these different pipelines. So as long as something can do both of those
things, that makes it a collector. That's our current running definition.
We're going to see how it goes. So that's great. That's what
a collector actually is. But why is it that Alloy
wants to be a collector? And the reason is lots of
people are running OpenTelemetry
and they're using the collector to handle a lot of these
pipelines and processing problems that we were talking about earlier, and we want
to support people where they're at. We don't want them to have to do a
lot of work to adopt Grafana Labs, so we want to go where
they are and say like, Hey, if you're already using the collector, it's easy to switch to
Alloy at the same time. We have a bunch of features that aren't
available in the upstream collector and it would be nice if we can
upstream some of them eventually, but currently they only exist in Alloy, and so we want to offer
those features as well. So one of these features
is live debugging, and I'd like to give a demo of this
along with showing how OpenTelemetry actually works, or sorry, how Grafana Alloy actually works as
an OpenTelemetry Collector. Alright, so let's switch over to the laptop here. All right, here we go. I'm just
going to run this as a video. Hope you don't mind. So what we're doing here is we are
looking at the OpenTelemetry demo project. By the way, if you're trying
to learn more about OpenTelemetry, this demo project is a great way to do it. You can find it on the
website opentelemetry.io. And so the way this works is it's a whole
bunch of different services that are loaded up into a Docker Compose
file, including this here, which is the OpenTelemetry Collector. So here we can see the Docker
definition for the collector, and then here is the configuration
file for that collector. So this is the standard OpenTelemetry
Collector Contrib distro for the collector. It's
got a couple of receivers, processors and exporters, and they're organized into a
relatively simple pipeline. All of the data coming out of this demo
application is going to run through that collector on the way to the backend.
So we're going to start the demo up. We're going to wait for
OpenSearch as usual. Okay, now it's running. So we can go to localhost:8080 and
have a look at what this demo actually does. And it is an observability
store where you can find all of your observability needs. So here we have a solar
system color imager. Definitely need at least three of
those and it's your usual kind of out processing pipeline. So this is a great little tool to
understand how OpenTelemetry works. We've got services and all these
different languages running. So if you're wondering how to set up
OpenTelemetry in a particular language, I actually recommend
looking at this project, but here we're going in and checking out
the collector and we can see that data is getting processed through the
collector because we can see the logs, but it's a little hard to
understand what's actually going on. You can read these logs, but it's hard to get a coherent
view of what that configuration file actually turns into in the real world.
So to get a better sense of what's actually going on, we're going to
swap the collector out with Alloy. All we're doing here because
it's again a drop in replacement, we're changing the image to grafana/alloy
1.8.2 is the latest version that supports these features. Then we're going to grab
the Grafana command line. It's a little bit different from
the collector's command line, but just to walk through it,
you're using the run command, you're setting the configuration
format to the OTel Collector format. We're going to start the
diagnostic server up. We have to set the stability
level to experimental to support these features because
they're relatively new. And then we're going to point it at
that same collector config file. Okay, so we're going to redeploy the collector, draining the old one, starting
the new one. There we go. Now we're going to go have
a look at the logs again, and you can see there are logs coming in.
They're slightly different. So we know it really is Alloy running
instead of the regular collector. But now because it's Alloy, we can go have a look at this handy
diagnostics tool that tells us all of the different plugins that
we're currently running. So here you can see
everything that's loaded up, but there's also this awesome graph view. So what this has done is it's taken that
config file and it's shown the actual pipeline that's being generated out of
it. You can see data flowing through it. You can click into each
one of these components. You can see how it's been configured.
You can see whether it's healthy or not. You can see its dependencies,
what it's connected to. This is a really handy graphical
way to understand what's going on. I find this is especially useful when
you're in development actually modifying and creating these pipelines to kind of
double check whether or not what you did actually is what's expected. And when
you're seeing the data flow through it, that can give you a clue as to whether
or not it's actually processing the data the way you'd want it to process. Okay, that's the end of the demo.
Let's go back to the slides. Great. So that's what we do when we want
to support OpenTelemetry as a collector. But what about all those other
handy features we were talking about? Well, the first thing I want to talk about
is native Prometheus pipelines. If you want to observe your
infrastructure and you expose metrics in a Prometheus format, and want
to send those to a Prometheus backend. Then you may not want to convert the
data between different formats when it's Prometheus all along.
So for these use cases, Alloy offers the possibility to
create native Prometheus pipelines to give you the best performance. And Alloy supports a number of
popular Prometheus exporters. Whether you want to export metrics
for your databases like Postgres, MySQL, or you may want to use the Node
Exporter for exporting system metrics, or even metrics from other monitoring
systems like those offered by cloud providers. Just to mention a few of
the exporters that Alloy supports. And to build a Prometheus pipeline, we use the Alloy Prometheus
components. In this example, we want to export our local
system metrics using the embedded Node Exporter. So we use the
prometheus.exporter.unix component. We scrape those metrics with
a prometheus.scrape component, set the scrape interval to 10
seconds and forward them to a prometheus.relabel component. And here we apply some filtering
where we drop the metrics for our dev environment and forward the other to the prometheus.remote_write component. And this takes care of writing the
metrics to our Prometheus compatible database. So by combining the Alloy
Prometheus components like this, we can construct our
native Prometheus pipeline. Next, I want to talk to you about one
of the news from this recent year, and that is Fleet Management. Now imagine that you're running hundreds
or thousands of Alloy collectors that are run in different environments
and used by different teams. That can be quite challenging
to manage and it can be a tedious task when you need to roll
out any new configuration changes. Let's say that we have deployed a
number of Alloy collectors using the Prometheus pipeline that
I showed you earlier, and we set the scrape
interval to 10 seconds. But we notice that this generates too
much data and we actually only need to scrape the metrics every 60 seconds.
So we decide to change this. Now we need to go in and reconfigure
every single Alloy instance where we deployed this. Wouldn't it be convenient if
we had a central place to go to where we could get an overview of all
of our collectors and configure them remotely? This is exactly why we introduced
Alloy Remote Configuration and Grafana Fleet Management. When using the Alloy remotecfg option, we can configure Alloy to instead
of reading configuration from a local file, fetch it from a remote endpoint and
continuously look for updates and load these to a running Alloy instance. And this communication between
Alloy and the remote server, it's based on an open source
protocol available in the alloy-remote-config GitHub repository. So you could build your
own remote server and use, but we also provide a managed
service for this in Grafana Cloud, and that is Grafana Fleet
Management, which is free of use. What Grafana Fleet Management does is
that it provides an interface that gives you an overview of all of your
collectors and their current status. So you can monitor their health, you can inspect the logs and
you can configure them remotely. You can assign your collectors
attributes like which team that owns them or which environment they're run in, and you can apply configuration pipelines
to your entire fleet of collectors based on the attributes. This can save a lot of time when you
don't need to configure the collectors individually and also allow for safer
rollouts since you can apply the configuration in stages and also
easily roll it back if something didn't go as expected. One of my favorite use cases
is data collection on demand. Under normal circumstances you may
not collect logs on a debug level, and if you collect traces then
you may apply some sampling. But when there is an issue
that you need to troubleshoot, sometimes it would've been nice to
have that detailed data after all, and Fleet Management can give you that. So you can prepare configuration
pipelines for data collection. You can have those logs on
debug level and traces like 100%. And when you need that, you
just activate those pipelines. Once you're done with your investigation, you can easily switch them off without
having to redeploy any collectors. So this gives you control over the costs
while at the same time gives you access to the data that you
need when you need it. Okay, so we talked about Prometheus
pipelines and Fleet Management. Let's have a look at how
this works in action. And I will show you how to configure this
pipeline that I showed you earlier to export the local system
metrics from my MacBook. We start with configuring Alloy
to use the remotecfg option, we set the Fleet Management endpoint
and we give this collector an ID. I'll call it grafanacon-2025.
We start Alloy. We can see that it's running, and we can go to the Alloy UI to see
which pipelines it has picked up. We check the Remote Configuration tab, and we see it's currently
using two remote pipelines. These are enabled by default to monitor
Alloy itself and export its metrics and logs. If we have a look at
the Fleet Management UI, we can refresh the page
and we see that our GrafanaCON collector has connected. We can get more details about its health, we can check the logs, and we see here that it picked up
the self-monitoring logs and metrics pipelines. We can check the
collector attributes like its ID, OS and the Alloy version
that it's running. And to create a new pipeline, we
go to the Remote Configuration tab. Here we can also see all the pipelines
that we currently have and what their matching attributes are. If we want to create a new pipeline, we can either choose from a template
or create a custom configuration. And I prepared a pipeline here which
is very similar to the one that you saw earlier to export the
local system metrics. So we copy this configuration pipeline and we paste it to the
Fleet Management UI. And we also need to give this
pipeline a name, so I'll call it node_exporter_macos. We can verify the configuration
syntax. Looks good. And now we need to select which
collectors to deploy it to based on the attributes. So I choose os=darwin, and we can see that it will be rolled
out to our GrafanaCON collector. Finally, we need to activate the pipeline. Now this should be picked up by
our locally running Alloy instance. So if we refresh the page, we can see the node_exporter_macos
pipeline appear here. We can have a look into its individual components and whether
they're healthy or not. And if we look at this scrape component, we will see here that we set this
scrape interval to 10 seconds. If we want to change this,
we need to do it remotely. So we go to Fleet Management,
edit our pipeline, and we change the value. I'll set
it to 30 seconds this time. We test the syntax. And it will still be deployed to
our GrafanaCON collector. Okay, looks good. So now Alloy should detect
these changes and if we refresh, we see that it will now export
metrics every 30 seconds. Finally, let's verify that we're
actually sending these metrics. So we go to Metrics Drilldown, check the last five minutes and
filter on the node_ metrics. And we can see that data is being
sent to Grafana successfully. So our pipeline works as expected. Okay, so we can go back
to the presentation. You have heard about some of the features
that are already available in Alloy. Then what comes next? First, we're happy to introduce further
improvements to the Alloy UI and debugging experience. The live
graph that Ted showed you, we will make that available also in
Fleet Management for remotely configured components. And in the Alloy UI,
we're going to introduce a new tool, Alloy Diagnosis. This will analyze your configuration
pipelines and identify errors and bottlenecks and advise you on
optimizations for your pipelines. And we will continue to invest in the
OpenTelemetry capabilities of Alloy. And for Fleet Management, we will
introduce OpAMP capabilities, that is also part of the OpenTelemetry
ecosystem for remote management of telemetry agents. And these are just some of the features
that we are excited to bring to you. There is so much more.

