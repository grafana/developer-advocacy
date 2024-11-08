# Grafana Alloy, Grafana Beyla, and OpenTelemetry Demos | ObservabilityCON 2024

This recorded session from ObservabilityCON 2024 provides a a live demo of Alloy, Beyla, and OpenTelemetry. Our Grafanistas ...

Published on 2024-10-24T19:52:30Z

URL: https://www.youtube.com/watch?v=n3UjjT08Njk

Transcript: Hi everyone, my name is Nikola Grcevski. I'm a software engineer at Grafana
Labs working on Grafana Beyla, which you're gonna hear about in a sec. I'm Matthew Durham and I'm also at
Grafana Labs and an Alloy developer. Hi, I am Carrie Edwards. I'm also a software engineer at Grafana
Labs and I work on migration tooling and OpenTelemetry and Prometheus. Alright, so let's get started.
Now, this is a QR code for Slido. If anybody wants to ask any
questions in the Q&A session, I promise it's not a Bitcoin mine or
a virus that will steal your phone's resources. No, it's for
Q&A at the end. Alright, so there's a couple of things
we're gonna talk about today. Most importantly we're gonna talk about
OpenTelemetry and how we t Grafana are building on top of it. We are
gonna talk about something new, which is a command, single command line that will get you
from zero to one with OpenTelemetry for any programming language. We are gonna talk about how you can
easily migrate across vendors with OpenTelemetry. And finally we're gonna
show you how to manage all that scale. It's a big thing, but let's see. Alright, so anybody old enough to remember this
story like from the late nineties and you know, the early 2000s where we
had these connectors and I
still remember at a box of these jumbled wires and trying to pick
the right charger for my devices. Well, not anymore. I think we have
something like this and this thing, this USB-C charges my headphones,
charges my earbuds, my phone, my laptop, then even my printer,
which is kind of cool, right? Well this is where we are today with
our vendor lock-in we have all this competing standards and it's not
easy to move across vendors or to even get the same
telemetry data across. And we believe this is OpenTelemetry. We are gonna get away from that mess
that we had 20 years ago with the phone chargers. We are gonna get to
something really slick. Alright, so OpenTelemetry and Grafana.
We are all about this. We love this because I'll be honest, we don't have another
sort of proprietary mode. We're new to this and we're lucky that
we started doing this when OpenTelemetry became a thing. So this means no vendor locking if we
had managed to pull it off and then it would be easy to extend your telemetry
collection with new signals just like that. Standards are there. Easily swap
our products, swap out the vendors. It's a great future and we believe we've
built some really good products based on OpenTelemetry for
application observability. And some of those you saw in the, in the keynote presentation by the first
one we already have in Grafana Cloud, which is Grafana Cloud
Application Observability, a single pane of glass that gives you
an insight into what your service looks like, their health, it's prebuilt dashboards the stuff you
need to kind of quickly have an overview into your service health. And then
we have Grafana Cloud Asserts, which they have a
presentation right after us. I don't wanna steal their thunder, but this tool lets you go really
deep with debugging production issue. It's really awesome. Okay, so now we
got these tools. The main question, the one of this talk is about
is how do we get started? How do we get these applications
to work for us? We've built them, they're ready to accept this OpenTelemetry and there's a couple things we need to do. So we need to instrument our application.
Okay, so what does that actually mean? The the answer is it depends, depends on what you have
in your application. Cluster could be as easy as putting
auto instrumentation on with a with the app. I don't know, a jar for Java or it could be difficult
because your frameworks you're using or the application technology that's
built with is not supported or it's, you know, a couple years behind
and it needs to be upgraded and so on. This becomes a problem sometimes and it
means that just like everything else in life, it will require some
learning, some effort, some time, which will compete with your existing
timeline for building the product you're building which serves your customers
instead of tele match, right? So does this mean we actually created
a new headache for everyone by creating this brand new standard now everybody's
gonna migrate to and it's gonna be slow and so on. So we like
to change this outcome. We like to make OpenTelemetry
available to everyone, because we really believe in this, like I don't know how many of
you are actually developers, but if those of you that may have done
job application development with SQL in the past were before JDBC, it was nightmare because as soon as you
got all the dependencies in your code with the vendor specific SQL database
and yeah change in database is tough luck. But with introduction of
JDBC, this is no longer a problem. So same thing will happen with
telemetry. Introduction of OpenTelemetry. We have a standardized way how we operate
with telemetry. So I wanna ask you, what if we could give you a way to get
started with OpenTelemetry with zero effort? You don't even have to know what it is
and it also means that what if you could just extend that further with
everything that is OpenTelemetry in the community without having
to jump right into it. You can take your time and slowly
add instrumentation for the stuff you need. More instrumentation like
business logic, anything else? So today we're gonna talk about a
couple of tools that we've built to do just this. Alright, so I'm gonna hand over to my colleague
Matt here who's gonna talk about the first. Thank you. All right, I want to
talk about Grafana Alloy. Now, if you're unfamiliar with Grafana Alloy, it is our distribution of the
OpenTelemetry collector and it is the foundation of everything we're gonna
talk about today in this session. So when we talk about Big Tent, we mean that that integrates with the
community and Alloy is built on that, that it integrates with Prometheus
and it also integrates with OpenTelemetry and we
announced it back in April and it's gotten some drive.
And to take a step back, you may remember Grafana Agent,
which was a very Prometheus-oriented solution. And when we wanted to look
at where we wanted to take the agent, we saw a rise of OpenTelemetry, but we also found that
people were using both, they were using OpenTelemetry
in their application metrics, but using Prometheus to
generate their infrastructure. So we built Alloy to
combine the two into one. Now I don't have a lot of time to talk about all the features of Alloy, but we have great native
Kubernetes support. We have scaling from pulling data from
a single node to running in a clustered environment, programmable pipelines, and we have answers for
configuration management, which we'll talk about just a
little bit later. All right, and I'll turn it back over to you. All right, thank you. Alright,
so that was pretty cool. And how does that actually go
back to this single command line? That's something I'm talking
about. Instrument everything.
No effort whatsoever. We introduced the easy
instrumentation button. As Alloy is a platform which we can
build components. We took Grafana Beyla, which was something we announced
last year atObservabilityCON. It was a brand new product then,
it's evolved quite a bit since. But if for those that
don't know what Beyla is, it's a really low overhead, our instrumentation tool built
with eBPF as a technology, which means it works at the
offering system level. Linux only. Until Windows catches up. But technically it supports
instrumenting any programming language. And I'll tell you,
we have customers that use
this OSS product with R. I did not know that R has a REST
library that you can build web services with R. I thought it
was a language for data science, but apparently people do this in R. And so if your application does
speak the protocol of the internet, like HTTP, HTTP/2 gRPC, SQL, Redis, Kafka, we are able to pull instrumentation
data tied together and provide the signals, metrics
and traces to limit and support. It's Kubernetes and container aware. And so let's just before
I, I'll stop talking here, let's see a demo and see if
actually I'm making this up or not. Alright, first demo please. Okay, so what we're gonna do here is we're
gonna get a Kubernetes cluster going from scratch. This is running
on my laptop by the way. Everything we're gonna see
here is prerecorded because
some of these images are gonna take a while to download.
So what we're gonna do here, we're gonna install in this
cluster a suite of applications. They're built by the
OpenTelemetry demo community. They actually have a full
website for e-commerce built with microservices architecture.
They use uses on purpose, large number of different
technologies to accomplish this thing. And what we've done in this particular
demo, we've stripped ot of all telemetry, all the hard work these people have done, we've took it all out and over here
I'm showing you with this K9s cluster that is gonna here I'm just gonna
disable all the observability components. Just to be honest here. There's no telemetry data
escaping this cluster whatsoever. So we're gonna kill co the OpenTelemetry
collector, Prometheus, Yeager, Grafana all gone. Nothing. This is
a dark cluster. We have nothing, we don't have no knowledge what it does, what technology is actually
this service is built in. We know there's some load generator
here pretends to generate web traffic. Okay? We have an application set going. So what we wanna do here
is now use this zero effort instrumentation tool to
see if we can get the data out. That's what we're gonna do. So we're gonna get this cluster and
we're gonna add instrumentation to it. But for all these services we don't
even know what technology there are. To do that, we're gonna use the
Kubernetes Infrastructure Monitoring. They've actually recently added
support for application observability. So we can use their integration
tile on the web to actually not have to even type Helm commands. So
we're gonna pick a Kubernetes cluster, which this already is preselected for me. I'm gonna enable
application observability. We're using Helm here/ I'm gonna
pick a key that I've created for Grafana Cloud for easy integration
and it gives me this nice little script here that I can just copy+paste
into my terminal and get going. This is my single command line.
Instrument everything in my cluster. So what people that are familiar with
Kubernetes Monitoring in Grafana Cloud know that this does
infrastructure monitoring. But now in the end I've injected this
additional Beyla section which enables it and gives us a little bit of introduction
that you can configure it to your heart's content here. And in this case, what we've chosen here to do is we
are gonna instrument everything. Kubernetes deployment name dot means all. We are gonna say we don't want instrument
Alloy because it's our actually collector And I've enabled
something called network monitoring. I'm gonna get to that in a second, but let's just remember here that I'm
enabling network monitoring too. Alright, so see this does this thing.
Installs a bunch of components. As you can see my cursor sped
up here so we don't wait. And let's see what happened
to a cluster. Alright, so this supposedly is command ran, it
should have instrumented added something. So what we see here is the
typical Kubernetes monitoring
that we have today for race refresher monitoring components. But
if we switch to the Damon Set section, we are gonna see there's a component
called Grafana Beyla here installed. Alright? This is the tool that is
monitoring this at application level, doing application level signal
telemetry instrumentation. Alright, we got something going,
what happened? Let's see, go back to our Grafana Cloud and see
what happened with that command line. Alright, so first thing we're gonna do, we're gonna see if data is coming through. Can I see my cluster in
infrastructure monitoring? Okay, yeah it seems like I got
one here and yeah some, some charts are popping up it, it's running for the last five minutes
so there's really not much data to look at. So yeah, we got CPU, that knows I have 20 cores on my system
and I've got a bunch of memory and CP utilization happening. Cost data
takes about five minutes to show up. But here we have all the pods,
you can jump into logs here, all the good infrastructure monitoring
stuff, but that's not all anymore. If we switch to application monitor
on the side and I see all my services. Now when I first did this, I see coredns in there and you're
wondering what the hell is that? Well that's part of a Kubernetes
we said instrument everything. I didn't know that coredns actually
had a rest endpoint where it has an application written and go and
it does have a health endpoint. So Beylor tracks it. We see all these services
build different technologies, all instrumented. We have
charts populated, we're
tracking requests per second. We know latencies, we know everything. Now let's see, there's a second page here.
We can see we detect the language too. So this tool does instrument
deeper certain languages.
It does recognize better. So we see there's some
applications in PHP, some Go, Rust, all different technologies.
We see all the data. We didn't have to build any of
these dashboards, it just showed up. That's where we say zero
effort, one single command. Let's dig deep into one of these services. So I'm gonna pick on this checkout
service and we see I artificially actually made it slower to show for the
demo there's a spike in latency. Can we debug this to some level here on
the spot with this data we've collected? And mind you, I'm only collecting
here metrics data. There's no traces. This purely metrics you can
enable trace if you want. For this demo it's purely just metrics. We see that this has P 99 latency
increase but also average. So something's going on with this service, but on the right side we see there's
no request for second increase. So something is slowing down the service. Can we find out if we scroll
down to the bottom of the page, we see the detected that this service
has only one endpoint, one rest API, but on the right side you see that it
does have a lot of other downstream services it calls. So maybe the
problem is with our service, maybe it's one of the downstream
services, what we can do, we see we're impacting that
front end with ten seconds P95. Alright, so with the same
data we collected over here, no longer we see rest endpoints but
we're gonna see a service graph. This also gets populated. So if we switch
to the service map for this service, we see a distribution also
show up and we see how much of the latencies for some of these
services contribute to the overall 500 milliseconds on average. With quick kind of like spotty here, maybe we can notice that is likely the
shipping service contributing to that slowness over here. Based
on the connectivity graph, the rest of the services are doing
pretty well compared to that, right? Again, pre-populated zero effort
to get to this point. I didn't have to do anything. I don't
even know what OpenTelemetry is. This is all backed by OpenTelemetry
ingested by our tooling. But this is not all, remember I mentioned
something about network observability? With this same command,
with network observability, we enable Grafana Cloud Asserts. The
thing you saw in the keynote presentation, we have a full connectivity graph. This is done collecting data
about connectivity based services. People use this to debug if a service is
actually really disconnected from their system or across region traffic. This actually can capture data
regardless of the protocol. And we can open our service here and
see what kind of data we can get deeper information, right? So last five minutes,
I gotta select my time window here, but you can see how I can correlate
now the network flow in and out of the service and see if maybe that
is the reason why my latency's higher because I'm delivering more traffic and
I can correlate that with the request per second happening here
and how the latency works. Now this tracks also UDP, if you have
DNS problem, it will show up here. So again, doesn't actually
have to be an HTTP service. And finally over here we can have the
breakdown of the APIs upstream and downstream and you can clearly see the
shipping service is causing a problem here. That's it folks.
This is for the demo. How cool is this single
command everything. And I'm gonna show you a quote of our
customer that's actually doing this in their setup. Various
technologies, gRPC/HTTP, it all works with one single
installation of a Grafana Beyla. And together in this presentation
was bundled with Grafana Alloy. So having said this, showing you
how to get started from zero to one, I wanna talk about how do we switch? And for that I'm gonna hand over the
clicker to my colleague Carrie who's gonna walk us through that. Thank you. So migrations and
re-instrumentation can be complex, challenging and time consuming. And as part of OpenTelemetry's
commitment to vendor neutrality, the OpenTelemetry collector
offers a series of exporters, processors and receivers to get telemetry
data into and out of OpenTelemetry format. And currently the OpenTelemetry
collector has many different, has support for many different
telemetry data formats. But today I'm going to highlight a new
component that we developed in order to make migrations from
Datadog easier and faster, which is the OpenTelemetry Datadog
receiver for metrics which integrates with Alloy. The story behind this project is that we
had a large customer who wanted to make the switch from Datadog to OpenTelemetry
and use Grafana Cloud as a backend. But they had a very complex ecosystem
and knew that re-instrumentation would take some time and in the meantime they
wanted to be able to continue to use the Datadog agent to send data while
they went through the process of re-instrumentation. At the time there was a Datadog
receiver in the OpenTelemetry collector, but it only offered support for
traces data and not metrics data. So we decided to build this
and open source it so that the rest of the community can use it as well. So if you have applications such as this
one that are instrumented with Datadog, you can use the Datadog receiver and
continue to use your applications and have data sent to Grafana Cloud or any other
OpenTelemetry compatible backend without having to make changes
to your application code. We still recommend re-instrumentation
for the long-term solution, but this can help get you started faster. Getting started with this tool is easy. With Alloy you can continue writing the
Datadog agent and forward your metrics to Alloy. The Datadog receiver will translate your
Datadog metrics into the OpenTelemetry format. And then if you're sending the data
to Grafana Cloud or a Prometheus space backend, you'll want to use the Delta to cumulative
processor to get the metrics into the correct temporality before
sending it to the backend. All this takes is a couple of
small configuration changes. You just need to configure the Datadog
agent to forward metrics to Alloy and then configure Alloy to
run the Datadog receiver, the Delta cumulative processor
and the OTel HTTP exporter. And just like that you can visualize
your Datadog metrics and Grafana dashboards. And now I'm gonna turn it over to Matt
to talk about how to manage all of this. Thank you. All right, so we've talked about how
you can instrument your
applications without touching them and how easy it is switch
from some other vendor test, but that generally only
solves half of the problem. You've probably got configuration
that needs to enrich or transform or filter out data as it's coming
through some sort of telemetry. Now that's hard to manage at scale
because you could have configurations across tens or hundreds of thousands
of instances and that can be baked in when you're building a virtual
machine or deploying and that's hard and it doesn't support if you're a large
organization that has observability as a service internally. And this is a lot of workflow
that's painful for our users. So we took a step back and we said
what can we do to make it better? So one thing I'm really
excited to announce is we're
having a public preview of what we're calling Grafana
Alloy Fleet Management. And this is a tool built within Grafana
Cloud that allows you to manage your Alloy instances at scale
with custom configurations. So rather than reading all through this, let's take a look at what
that actually looks like. So we have here the single pane of glass
that kind of gives you the viewpoint. We can see we have our collectors
on the left, we have some status, the version of Alloy that is
running the operating system. And then we have custom attributes. And this is what really let's you narrow
down configuration to what you need by maybe team or purpose or
environment dev versus prod. You can also see the
health of a collector. Click on it and get instant
feedback, metrics, logs, alerts. You can even dig into the alert, maybe click on a runbook if you wanted
there and and really be able to see what's going on with the
health of your fleet. Now here you can see we're just
digging around a little bit, kicking around and then this is
where the configuration screen is. So we have some configurations here. You can see what they apply to based on
those attributes that you can set up. Plus some like operating system, this active flag that you may create a
configuration but you don't necessarily want to release it right away or
you want to be able to roll it back. So toggling that on or off
can control that behavior. Now let's say we wanted
to create a configuration. We're gonna make a Beyla
configuration here. I've conveniently got it
ready to copy and paste. You notice that it gives me an error at
the bottom and this is because there's a slight syntax error. So we have some guardrails to help you
write good configurations and not deploy things that will just immediately fail. And then you can see in real time
what collectors this configuration is going to apply to based
on those attributes that
you have defined and given. So you know, we only want this to run
on Linux and we wanna run it on team A. So you can see in real time exactly
how that is going to roll out. So we're going to save that and then
we're gonna click to send it out. So within minutes, all
the Alloy instances, will check for a new configuration
and pull it back down. And then if you decide there's a problem, you can simply deactivate
that toggle and it will roll back the change. Alright, to finish this up Nikola. Thank you. Alright, so before we recap our presentation
let's give you an opportunity to ask the questions one more time. But just
to confirm what we talked about today, we showed you our future we believe in
with OpenTelemetry and we're building tools on top of it. We showed
you how you can get there, get started without any
effort from zero to one. And then on top of that you can extend
at your own pace with OpenTelemetry using the community built as the case
supported by Grafana and others in the community. We showed you how we can easily migrate
from different vendors by giving you an insight into how we actually build a
Datadog receiver for OpenTelemetry. And finally, how you soon be able to manage all
this at scale with Grafana Alloy Fleet Management. Thank you. That's it.

