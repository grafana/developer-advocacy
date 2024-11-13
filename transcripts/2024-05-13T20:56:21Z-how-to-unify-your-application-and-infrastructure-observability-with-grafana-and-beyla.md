# How to Unify Your Application and Infrastructure Observability With Grafana and Beyla

In this video, learn how Grafana simplifies observability with our Application Observability solution, streamlining monitoring for ...

Published on 2024-05-13T20:56:21Z

URL: https://www.youtube.com/watch?v=0LQQ-CIkfys

Transcript: How many of y'all feel like you work on
some hard problems? , come on, let's get some hands up. I know that that you're not necessarily
working on observability problems. You've got your own domains that you're
working in, right? Commerce, banking, B2B, B2C. Some of those problems are hard. You wanna focus on those problems, right? Today we're gonna be
talking about unifying your
application and infrastructure observability. I am going to be introducing application
observability with a bit more detail. I also have a nice demo for y'all, and we're gonna talk about Beyla in a
little bit more detail as well. First, let me tell you who I am.
My name is Myrle Krantz. I'm a director of engineering at Grafana
Labs. I am also open source-passionate. In my free time, I'm also the VP of
Infra for the Apache Software Foundation, and I split my time between Germany and
the U.S. This picture is actually in the  in Germany.
It's in the the . I grew up in Colorado. I love
mountains. This is a mountainous area, a little bit south of the place where
where I have a house in Germany. You can go swimming there. You can
hike the mountains there as well. But currently I'm living
in Stephenville, Texas, which some of you may have heard of
if you're from the, the Texas area. So go Texas. All right, quick overview. Modern systems have a lot of moving parts. Y'all have hard problems you're solving, and some of those hard problems
are distributed into hard systems. We can monitor most of those moving parts, but it can be easy to lose
sight of the bigger picture. We tie that together for you all with
our new application observability solution. And we also have made it easier
to ingest data into our application observability solution for you. This is an example application here. This is actually the OpenTelemetry
demo that that we've given a, an architectural diagram
for the OpenTelemetry demo. How many of y'all were here for the
Eclipse? Yeah, that was pretty cool, right? The OpenTelemetry
demo is selling telescopes. So if y'all want to set up a, a
web shop, then check that demo out. This is an example where
there are multiple services in multiple languages. We've got a
front end service talking to a proxy. We've got APIs, we've got backend
services, we've got a cache, we've got a queue. Some of the communication protocols
we've got HTTP, gRPC, TCP. It's just a very complex landscape. Now,
this is a relatively small application, which is why we can get
it all into one screen. I doubt any of you are working
on an application where
you could actually get it into a single screen like this. If you're trying to instrument
one of these applications. The current state or before
application observability, the state of instrumentations
was we had some automatic stuff. So we had released frontend observability. We had the ability to create a nice plugin with the dashboards.
For frontend observability, we've got integrations. So if
you're using Spring for example, you could you could use an integration, which includes dashboards and alerts,
but a lot of it's manual, right? So you'd be doing
instrumentation manually. You would be trying to figure
out maybe the dashboard. Most of this stuff has
standardized on Prometheus metrics, but the semantics aren't
necessarily standardized. So you'd be building a dashboard for
semantics, for a set of semantics, and maybe that changes and you
have to keep the dashboard updated. And we just determined some of
y'all are working on hard problems, hard problems that aren't
necessarily these problems, and you'd rather focus maybe
on your business problems. What this ends up meaning is you have
a whole landscape of dashboards too, right? Maybe you've got one
dashboard for your Node.js stuff, you've got a different dashboard for
Go, maybe another dashboard for Redis. And all of this sort of comes
together maybe into a lot of tabs. If you're trying to debug a problem
that crosses across multiple systems. You might be able to make
these dashboards yourself. Maybe you're downloading them, but you're probably going to end up
having to maintain them if the underlying systems change as well. But
does it have to be this way? What if instead of all these dashboards, we could derive the metrics from traces
and then correlate between those signals from our application with the ones also
provided by our infrastructure by like, by the Kubernetes or by Docker. And do all of this while still relying
on open source technologies so that we're not tying anybody into a
specific vendor solution. And in fact, OpenTelemetry
gives us possibilities here. Application Observability is an
open opinionated solution based on OpenTelemetry and Prometheus. This
is an out of the box solution. You don't have to build
the dashboards yourself. It is designed to minimize your mean
time to resolution in your modern, complex application problems
that y'all are dealing with. This should make it easier
to get faster to value, because you don't have
to create the dashboards. You can use the dashboards that we have. You don't have to work out workflows and
memorize them or share them with your colleagues. You can use the workflows
in our opinionated solution, and it unifies metrics. It unifies logs and traces and
profiles across the software stack. So let's talk a little bit
about how we got there. RichiH also introduced this concept
that we have at Grafana of the Big Tent. We also call this our Act One. This was the first step of Grafana
into the observability space. We built the possibility to
visualize data from any source in place. So you don't have to move your
data from InfluxDB or from Splunk. You can visualize it where it's
at on the Grafana dashboard, giving you that single pane of
glass. Once we had that in place, we had learned a lot about the data
sources that we were pulling data from, and we started thinking, Hmm, some
of these things we could do better. So we started out with
Mimir. It's at the end here, but it was the first thing we worked
on. We started out with Mimir, which is a database
for Prometheus metrics, which can store hundreds of millions
of active series in more than a year of storage. We took what we
learned from working on Mimir, and also we employ roughly half of
the Prometheus committers as well. We took what we learned from Mimir and
Prometheus and we applied it to logs and we built Loki, which is a Prometheus-like
approach that works at large scale. This replaces traditional aggregation,
reduces indexing overhead, and Loki has been a very successful open
source project for us. Next up, Tempo. And with Tempo, we added a
Prometheus-like approach. We took the things that we learned from
a time series database and Prometheus and applied it to traces. Now you can do trace requests of cross
components of distributed systems. And then we learned and acquired a company
called Pyroscope and merged with some of the things we were working
on internally and applied
all of this time series database know-how to profiling so that
you can use profiling to discover your performance bottlenecks. So in order to feed all of that data, we've also introduced Grafana
Alloy announced last week as a continued iteration on
our ingestion strategy. Grafana Alloy is an OpenTelemetry
collector distribution. Now because all of these things are
open source and use open protocols, Prometheus protocols, and
OpenTelemetry protocols, this reduces your vendor lock-in as well. So you can instrument your
systems and export your data into these systems and be confident that you
get to choose where you're going next from there. You own your data. You make
the use of them for your use cases. Once we had those databases in place, the next thing we moved into was our
Act 3 solutions. Our Act 3 solutions. Well, we determined that some
of y'all, we keep saying it, some of y'all have hard problems and you
don't necessarily want to be spending your time on the observability problems. So we built some opinionated
solutions for y'all. We took those those Legos and we put
together some nice Lego kits and built you a Death Star or an Eiffel Tower. We built for you. We built
performance testing solutions with k6, we built infrastructure
observability solutions, especially Kubernetes Monitoring is one
of the most interesting ones in this category. We built incident response
management. So we built Oncall, we built alerting and
we built an SLO product. And this is where we're getting to
the meat of the matter for this talk. We built Application Observability and
Application Observability also includes front end observability. And in this, we also created Beyla in order to
make it possible to ingest data from almost any source. So this is a little bit
more of a technical overview
of the architecture here. Ingesting data into Application
Observability can work either directly via OpenTelemetry to our
OpenTelemetry gateway, or you
can also use Grafana Alloy, which can also consume data from the
OpenTelemetry collector because it is itself an OpenTelemetry
collector distribution. And consume data natively from Prometheus. It can also consume logs and it can
export these data directly into Mimir, Tempo, Loki and I should
have added Prometheus here. Grafana Alloy then takes that data that
it sees in these backend databases and visualizes it. Sorry, Grafana Application Observability takes
this data from these data sources and visualizes it. And I would like to give you a
view of what that looks like. So what we see here is the service
overview of Application Observability. This is the first place you're gonna
go when you get into application observability. The application we're
looking at is, as mentioned earlier, the OpenTelemetry demo. And one thing you're going to notice about
this application is that it has a lot of different languages.
You'll see go, you see Java, you see .NET and Ruby, Node.js. All of these are languages that can
be instrumented with OpenTelemetry SDKs. So this is the OpenTelemetry demo, and we are basing this off
of the OpenTelemetry SDKs. That means that nothing here is is
vendor locked or vendor associated as far as the instrumentation side goes. And you can see that there's a wide
range of languages available here. We also in Grafana Labs contribute
to the OpenTelemetry SDKs for .NET, for Java. And we are starting to contribute also
on Node as well. So we go in here, you can see some of these seem fine. You've got an overview of duration
errors and rates, the errors, which is the middle column
there, the pink column. Some of these services seem
to be struggling a little bit. And if this was your service landscape, this is probably one of the
first places you would look, especially when you see
something like checkout service. 'cause That's typically where you earn
your money. You want that to be working. So let's go into the checkout
service. We can see the duration, we can see the errors in rate.
We can see that as an overview, but now we can also go in
and see which operations are part of this service. In this case, there's only one operation
on this microservice. Some of us have microservices
that have a few more. Some of us have microservices
that aren't really microservices, and you would be able to see here the
errors for this service broken down by those end points. And you can also see which services
are affected by this service. So this service is having some errors. You can see that the front end
service is affected by this. This might be a point at which you
would go to the team next door and say, Hey you know, that alert you're getting we're working
on it so that people know what's going on right now. Another thing you're gonna notice here
is that the duration distribution is a little weird. We've got 16
milliseconds for some of those. But most of them are between two seconds
and four seconds. That's a problem. That's probably too long on the durations. So if we're going to go in and investigate
this problem, what we're gonna do, probably one of the first things we're
gonna do is hit the traces, right? So we'll go in and I've actually
already got the search set for this. Normally I would come in here and I'd
go into the status and I'd select error. I personally prefer this edit help
over editing directly in TraceQL. This means that I don't have to
learn another query language. I can just go straight in here. And then I can see all of the
traces that contain errors. So I can click on one. And we see here this trace, the head
of the trace is in the front end. That makes sense. And we see errors all
the way down into the checkout service, and we see that the checkout service
get product endpoint is failing. And we can even see here, look,
there's an error description. While dialing a TCP, there's
a connection failure. We could also go in and check the logs
for this for this span specifically and go through and see if there's something
that we can learn or discover from those logs. And if we prefer
the visual representation, we can also go and see which services
this service is calling locally. So this is a service map focused
around just this service. You'll just see the upstream and
downstream of just this service that we're looking at right now. This will
give you a faster overview of, of which services might be causing
the problem and also which services might be affected by this problem. So we're gonna pretend that I've
handed this problem off to Tom, to my colleague Tom. And we're gonna go look and see if there
are other problems that we can identify in the service overview. And immediately
we look and we see, okay, well, we know that front end's probably
being affected by the checkout service. Let's put that aside. But here's
the product catalog service, which is also having problems. So we dig into the product catalog
service and we can see that not all the durations look okay, but
there's also an awful lot of errors. And we can see also like these
errors broken down by operations. It doesn't seem to make a difference.
Which of the the endpoints is, is being called, like the
errors are still still coming. So it seems to be kind of a service-wide
problem. That's a minor indicator. Maybe it's an infrastructure problem.
We can check out and see if there is, we can go into Kubernetes
and now this, this comes up, like maybe y'all have new people on
your team that don't know your naming conventions and might struggle to figure
out which pod belongs to which service. They don't have to memorize that. They can come up here and they
can hit Kubernetes and say, oh, the Kubernetes pod name is this. And they can just go straight
into Kubernetes monitoring.
And here we see, oh, this is restarting a lot, and we can pull down and we
see look at the latest logs, look at the latest events,
and we see that it looks like probably there's a problem
with the number of connections. Maybe we need to scale this service up. Maybe we need to change
the connection pool. And we can hand that problem
off to maybe to a colleague. I'm gonna say that the colleagues, Jerry, and we can let Tom and Jerry
figure this one out together. So this gives us an overview of what
Application Observability can do, but you might also be asking, how do I
get the data into this? How do I pull, how do I get the data out of my systems,
which are complex and, you know, maybe have some contradictory versions. Maybe it's hard to do
the instrumentation part. Can we move back to the slides please?
And this is where Grafana Beyla comes in. Grafana Beyla was announced in
general availability last November, and we have continued to iterate on this. Grafana Beyla is fully open source and
it is licensed in the Apache license v2. So you should feel completely
safe deploying this on any
infrastructure that you want to because it is
OpenTelemetry-based that is, we use the OpenTelemetry protocol
to transport all of the data. That means it's also vendor neutral. So anything that can accept
OpenTelemetry protocol, this can send that data to
that. Because it's eBPF, that also means that it's zero
code for you. This is interesting, especially for C++ or Go or other
compiled languages that can sometimes be difficult to instrument. We're also though increasing
coverage for other languages as well. We're continually testing this
and improving it around Java, PHP, Ruby we've had an interesting
experience, for example, where one, where one company was struggling to
instrument their Ruby stuff because it had contradictory library versions that
made it impossible to use OpenTelemetry SDKs. They just popped in Beyla
and immediately got some insights. It was actually pretty cool. Beyla, as I said previously, makes it possible
to do this with just one command. So this can work in your
Kubernetes clusters, it can work in your docker containers.
It can even work on your bare metal. And it achieves that while getting at
some information that would otherwise be completely impossible to get because
it's eBPF. You'll see also, for example, if you've got a duration
in your Java applications, that duration often doesn't
include the time in the queue. But eBPF can include the time from
the point where it hits the outer boundary of that service to the time where
it returns from the outer boundary of that service. So it gives
you a more accurate picture. Some of you probably don't
know what eBPF is, and that's, that means that I get the privilege of
being the first person to tell you about that. eBPF is a technology that allows a privileged
process to load probes into the Linux kernel. Those probes are triggered after certain
events that are specified in the probe. So, as an example if a function is
invoked in the instrumented application, it can be decorated with a user
probe or if a kernel API function is called, it can also be
decorated using a kernel probe. Probes can read memory, they can modify memory of the observed
application and of the kernel function. And eBPF also provides communication mechanisms
between the probes and the user space program. So this way the eBPF probes can
share information with the user space program. In this case, it's
Beyla that is the user space program, about the observed events. So what Beyla does is it
loads these multiple probes
into different parts of the system that include application
functions, the application runtime, the Linux kernel, the TCPIP stack,
and some libraries like OpenSSL. Those probes then collect and
report back basic events to Beyla, then coordinates and
collates that information and takes, so for example, an HTTP service
was invoked. It's started in time, the status code the request
patch, things like that. And it can take all of
that. It aggregates it, and then it sends it on out using the
OTLP protocol decorate it with all of the relevant metadata and reports
it as spans or as metrics. So here's where I'm gonna show
you a little demo of Beyla. This is a recorded demo because there
is a time slot in the middle of that. We would lose a lot of time if I
waited for it. For this demo, we instrumented the services at the
top here. We instrumented the, the services in the demo name space.
So there's a front end service, a backend service, a worker service,
and a load generator service. We're going to instrument these
with a helm chart. But before we, before we start that helm chart, we want to change some of
the configuration to use
some of the newest features. For example, in Beyla 1.4, we've
added some networking observability. Once we've got got that, we've also got
we want to specify that it's just the, the services in the demo name
space that we're instrumenting. And we want to tell Beyla
to include the metadata for Kubernetes. And we also want to tell Beyla to
group the endpoints on a heuristic to make sure that we get
similar endpoints together. Now, Bayla can send data to
Prometheus or to OpenTelemetry. We're gonna tell here to
send to the OTLP gateway. And we are giving it some of
the authentication information
that it needs to get the data into Grafana Cloud. Once we have that altogether with the
authentication information and everything, now we run the helm chart
and we give it a second, and then we check to see if it's worked. Once we've got that going,
we can see, okay, we've, we've instrumented a couple
of processes. That has worked. We've got the worker process,
we got the, the load generator. We've also got some of the
network interfaces captured. And now this is the point where we would
normally need to wait a little bit for some data to come. So we have some
pretty graphs. So time lapse here. Then we jump into Application
Observability and we can
see that all of these services are fully observable within
Application Observability that I just demoed to you. You can see the
duration, you can see the errors, you can see the rate for all
of these services. You can also dig into the service map. You can see the upstream and
downstream of each of these services. And we can also dig into
the traces even for Go. So we can see fully distributed
traces from top to bottom. Click on one of these, you can see
all of the function calls, right? With each of these services.
And on top of all of that, and I just mentioned it in Beyla 1.4, we also have added networking
observability features. So we can, we've added a new metric. It is
called Beyla Network Flow Bytes. We can just query it
directly as we see here. The Beyla team has built a nice
little dashboard for this as well, although I expect we'll probably be also
integrating this into our opinionated workflows at some point in the
future. So you can see with this, this dashboard that the Beyla team built, which we need to adjust it to the last
few minutes. We can see all of the, the bytes per second that are
emitted by each service outbound. And we can also check out the bytes per
second that are emitted by each service inbound as well. And we can also see
the way that these services interrelate. So we see that the, the front end
service, this is not surprising, has sent an awful lot of bites
to the low gen service, right? And we can sort that and we can see like
which services are producing the most data. This might be interesting
to y'all, for example. If you've got a lot of if you've got
a large ingress bill or a large egress bill, you can figure out like
which service is causing that. That's to wrap it up. Now we've got
several things that I'm proud of here. We've mentioned Faro in passing. We've got application observability going
and we've got Beyla. And altogether, I think that makes an
absolutely fabulous solution. I am enormously proud of all of the
Grafanistas who have helped us to build this. We've got the Beyla team, we've
got the OpenTelemetry SDKs team, we've got the teams working on
data ingestion on the Alloy team. We've got the Application Observability
Visualizations team, and also this work, the things that we've learned from doing
all of this has also impacted other open source projects at Grafana. So we've learned things that have that
have helped us to make Dcenes in Grafana better. We've improved spark lines
and contributed to spark lines, and we are enormously grateful to the
Grafana team for building out the features that we needed in order to create
these solutions. And that's not all, it's not just the Grafana team. The Tempo team gave us an enormous
amount of support added features that we needed. And the metrics that we're displaying
here would not be possible without the Tempo team. And all of this, of course, is not possible without our
customers and users. So y'all, so thank you all again for the support
and the feedback that we've gotten from y'all while we've built these
solutions you have made, helped us to make application
observability. Say it again. Fabulous . Thank you.

