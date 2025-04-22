# Open Source Observability Explained - The Grafana Stack

Wish you could have open source observability explained to you? Senior Developer Advocate Nicole van der Hoeven explains ...

Published on 2024-04-16T15:59:15Z

URL: https://www.youtube.com/watch?v=WSW1urIXsfA

Transcript: - It's not enough to just build the system and hope it works. We have to make sure
that it meets the goals of the people who use
it, that it works well, and that we have the confidence that it'll withstand expected and some unexpected situations. In other words, the software
systems that we build must be continuously reliable. In this video, I'm gonna
go over what we can do to work towards continuous reliability and also about how some open
source Grafana Labs projects fit into that picture. When it comes right down to it, there are a few main
concerns in observability. First is identifying the data to collect. There's lots of different types of data, different components, different levels, frontend and backend, among others. How do we know what's important? Secondly is collecting the data. Different types of data
have different requirements about how they're stored
and how they're aggregated, if they even can be. And number three is
doing stuff about data. After we have all that data, what does it all mean and
what can we do about it? We're gonna go over all of these. When we're identifying data to collect, we need to think about what
we're actually observing, what types of data exist
and where do we store them? Observability really is about
different types of data, what we call telemetry signals. I'm gonna go over a few in this
video, namely logs, metrics, traces, and profiles. Each type of data has
unique storage requirements and if we don't optimize for the specific type of
data signal that it is, then storage can get costly
either from a dollar perspective or from a computing resources
perspective, or likely both. So I'm gonna mention some databases for the different signals, but they're gonna have
a few things in common. Each database is optimized
for a specific signal. It's possible to use one for all, but it's not the best way to do it. The databases also have to
be horizontally scalable and multi-tenant, so you can have multiple instances of it when your usage exceeds having
a single instance of it. All the databases I'm
gonna mention are built for scalability and multi-tenancy. And lastly, each database has a slightly different query language that again is optimized
for letting you find stuff for that specific telemetry signal. First up is logs, logs are
chronological records of events or other output while
a component is running. They're kind of like a
running feed of context about what's happening in
a particular component. There are a few concerns with logs. First, there's the difficulty in parsing because you can pretty much
send everything to logs and that can be kind of difficult when you're trying to find out
certain things within them. There's also increasing storage needs because there's a lot to a log, so where do you keep it so that you're still
keeping what's useful, but you're also not
just storing everything? And then there's the complexity of the retrieval from ephemeral sources. If you have logs within a
Kubernetes pod, for example, that specific pod may
not be there tomorrow, so how do you make sure
that you get it out of there and still store them
somewhere that persists? And then lastly, there's aggregation, with something like logs that can be lots of different things, how do you sort of combine them and roll them up in a meaningful way? Grafana's solution for that is Loki. Loki is a database for logs. Some of the cool things about it are that Loki only indexes the metadata instead of the full text of a log. So not only are queries faster, but the storage requirements are reduced since it effectively
stores in object storage, a table of contents rather
than the entire book. You might have also heard
that Loki is like Prometheus, but for logs, we'll
get to Prometheus soon. But what you need to know is that the query language, LogQL, is very similar to PromQL, the query language for Prometheus, and it works with
Prometheus Alert Manager. So there's a lot of integrations there that really tie it to Prometheus for those who are already using it. Now we're getting to metrics. Metrics are numbers that tell us something about the system at
specific points in time. They're good for getting
a quick quantitative read into how a system's doing, and because they're numbers, you can aggregate them across multiple components or over time. Some of the concerns about
metrics are that metrics are not as good at explaining
why a number is what it is or troubleshooting an issue. There's also no context, just numbers, so you kind of have to
find that elsewhere. And then lots of numbers on
their own don't mean anything, so you need to do some sort of aggregation for a number to mean something, and that aggregation can take a long time or take a lot of resources. Prometheus solves a lot of these problems. It is a database for metrics, but instead of using file
structures to store data, like traditional databases, it uses labels and that
makes it really performant. It works well with
microservices and Kubernetes, and the query language is called PromQL. PromQL is a multi-dimensional
query language, so you can query along
a lot of different tags. Prometheus also has exemplars, so you don't need to rely on just the high level
aggregated overview numbers. But you can look at an exemplar, so a sample of a specific period in time, so you can look at the real data. And Prometheus also supports
push and pull-based monitoring. So Prometheus can exist
and then receive data that your application
components push to it or Prometheus can actively go and pull that data over to the database. Now Mimir is kind of like
an addition to Prometheus and there are two main
things that it does. The first is that it
provides long-term storage, object storage for Prometheus, and it's also natively multi-tenant, which is something that
Prometheus is not as good at. So if you need more than
one instance of Prometheus, then Mimir is your best bet. Mimir is like Prometheus, but horizontally scalable and reliable. The third telemetry signal is traces. Distributed traces are kind of like logs, but instead of being about
a service or component, traces are like logs about
a single transaction, like a request as it's
processed by multiple services. So tracing builds the story of where that request went
and how long it took where. Some concerns about tracing are that it can be quite expensive because there's a lot
of information to store. Tracing is also meaningless if you can't correlate
it with other information about what else was happening
in the system at the time. It's an in-depth view,
not a bird's eye view. And then tracing also only works if all the components are instrumented, which means that there's
quite a bit of setup that you need to do before
you are able to get traces that actually mean something. Tempo is the database
for distributed tracing. The query language for Tempo
is something called TraceQL, which is different from PromQL and LogQL in that those two are really based around
streams or key value pairs, but traces need more
information than that. They can be numbers, strings, arrays, or even something like maps of arrays of maps of strings. TraceQL is more pipe-based and is better suited to
the information you need for distributed traces. While metrics and logs
are still important, traces and Tempo are awesome
at drilling down very deep and following the path of one transaction. So they're very good for
troubleshooting in general. The fourth telemetry signal
is continuous profiles. A continuous profile is information about how much computing
power or resources are used by an application, and that's collected at
specific intervals over time. It's kind of like a bunch of metrics in that it can tell you, for example, the CPU or memory utilization
of an application, but it's also kind of like a trace because you can also drill down from the overall utilization down to the specific function
calls that are involved. The concerns for continuous profiling are that, traditionally, this process took up a lot of overhead. Collecting information
about the CPU, for example, can sometimes add work to the CPU and that extra bit of
work can make a difference to the overall functioning
of the component. And then comparing CPU
utilization can be difficult because when you're trying to decide on whether a new build used
up fewer or more resources, it's kind of hard to tell
what to compare exactly. Do you get the average? Do you plot the data
on a logarithmic scale to reduce outliers? It can get a little complicated. Pyroscope is a database
for continuous profiles and it's built for performance. Depending on the complexity
of your application, you can expect an overhead
between one to 10% for the collection of continuous profiles, which is pretty cool. Pyroscope doesn't store everything, it samples by default at
an interval of 15 seconds, but you can change that. It doesn't store individual metrics. Instead, it only stores
just enough information to show the shape of the entire profile, and it also uses object storage to do it, making storage costs lower. To solve the comparison problem, Pyroscope helps visualize
this shape as Flamegraphs, and you can even do diffs of Flamegraphs so that you can figure out when a function that you modified in the last build is taking up way more
memory than it used to. You can also query profiles
using a language called FlameQL, so you can quickly find
profiles based on tags. So there are four different types of data, but they're spread out
in different places. So where do you actually
get the data from? One approach is to capture information that's already being generated. This is called instrumentation, and there are a few ways
that you can do this. You can do source instrumentation, which means adding code
that saves the information that you require during
runtime in a specific format. Usually this means using things like SDKs, libraries and other tools that are based on the
language that you're using. On the front end side, Grafana Faro is a collection of SDKs that let you do real user
monitoring of an application. You put some JavaScript in your web app and that lets you see how
your users experience it. You can think of this as a sort
of front end observability. It looks at things like
the Google Core web vitals, so it looks at the
loading, the interactivity, and even the visual stability
of elements on the page. And then on the backend side, there's something called OpenTelemetry, which is a collection of APIs, tools and SDKs that have
become the industry standard for how different telemetry
signals are collected. And this is all to do with the backend. You can also do what's called
binary instrumentation, which means modifying the
binary of the application or infrastructure component without modifying the underlying code. Now this could involve adding an agent to the components that
you want to monitor. This agent then sits on that component and then collects the information and then communicates that information to the rest
of the observability stack. So we talked about OpenTelemetry earlier. There is an OpenTelemetry Collector that is an agent that does this. However, we also have
something called Grafana Alloy, which is kind of like
an opinionated version of the OpenTelemetry Collector that happens to work well with the rest of the Grafana stack. So it's a telemetry collector for Mimir or Prometheus for metrics, Loki for logs, Tempo for traces, Pyroscope
for continuous profiles, and other OpenTelemetry endpoints. Alloy is really important
because instrumentation can be a real pain, and Alloy is kind of like the plumbing. You sure miss it when it's gone and you want it to always be working. Alloy also has a new flow mode, which is turning it into a
bit more of a data pipeline. It's more of a modular approach where you can have better
flexibility on routing and transforming the
data that Alloy collects. Some approaches to instrumentation don't modify either the
code or the binary itself, and we can loosely lump these
into external instrumentation. For example, in a language like Go, you can attach to the
binary without modifying or instrumenting the binary itself and just listen for signals at breakpoints or established safe
periods within the program. Grafana Beyla is a new EBPF
auto-instrumentation tool, and it employs a mix of approaches depending on the programming
language and the protocol. EBPF is a technology
that allows developers to run programs in an
operating system kernel, so at a much lower level without having to change the
kernel source code itself or use kernel modules. There are usually two
sides to an EBPF program. First, there's codes on the
kernel side written in C, and then there's code on the
user space side written in Go, or some other language. Beyla captures signals for
application monitoring, not infrastructure monitoring. And right now that means information about the HETP and GRPC protocols. For example, you can deploy Beyla as a sidecar container
in a Kubernetes cluster, and you can just start capturing
HTTP and GRPC information. So that means it can
tell you typical things you might expect like response time, but it'll also be able to tell you things like the length of time before a Go routine actions or request, which you can only really
see at a kernel level. So all of these approaches to instrumentation are
about collecting data that's already being generated, but sometimes there's no data to collect, such as when something hasn't
even gone to production yet. What do you do then? I mean, you could just
wait until it's live or you could trigger it earlier so that you know what to expect. This is called software testing. Some concerns around testing are how to make this synthetic environment of a test environment more realistic so that the data that it generates is useful and mappable to production, and also how can we make this entire process
systematic and repeatable? k6 is an open source
reliability testing tool. It is written in Go, but the scripts themselves
are written in JavaScript, and it provides a framework with which to design tests
to very exact specifications. It's more than just hitting end points. It's also simulating user
flows on the protocol and browser levels, defining
independent scenarios with differing load schedules, even injecting faults into
components on purpose. With k6, you can get
information on the network or protocol level or even
on the browser level, like a lot of the core web vitals that we were talking about with Faro. You can also do synthetic
monitoring with k6. Synthetic monitoring is a way to use a very low level
of load in production to test different endpoints. It's called synthetic because
they're not real users, but it's still monitoring because it's a way of kind of putting your finger on the pulse of your system while it's live. So that's how you collect information, either through instrumentation or by generating the data using testing. But what do you do when you get that data? Because you can end up with a lot of it. How do you actually assess
the impact on your system and make that actionable? Let's talk about doing stuff with data. The first is visualization. All the data in the world
won't do you any good if you don't have a way
to make sense of it. Everything I mentioned, every project that I mentioned can send information to Grafana. Grafana is a visualization tool, but it can take almost any form of input and then display it in a
way that you can configure. So there are plugins to
get data into Grafana called data sources, and then plugins to display that data in different ways called panels. Then there are also apps that can be combinations
of data sources, panels, and even other actions to fulfill a certain need or use case. So it's super flexible for
whatever you're using it for. It's not actually just for observability. You can also set up rules to alert you based on the data that you get. For example, maybe you wanna know when the CPU utilization of a component exceeds a certain threshold, and that gets us into the
next topic of what to do with all of that data, and that's incident
response and remediation. Alerting can be dangerous because too many alerts are
just as bad, if not worse, than no alerts. When alerts are going off all the time and sometimes for things
that aren't important, our tendency is to eventually ignore them. To combat this, alerts must
be unambiguously useful, timely, and appropriately routed. OnCall is an open source tool that makes sure real issues
are properly addressed. It manages OnCall schedules so that you know who's available to help. It automates escalations
when something goes wrong so that the right people and only the right people are notified and in the right way. You can use OnCall to get
notified via Slack, Telegram, phone, email, and even a mobile app. Just like everything, OnCall
works with Grafana too. So Grafana is really at the center of this entire stack of tools. Grafana is the one-stop shop for everything you need to know about your application's current state and also what you need
to do to improve it. So observability is really
about building systems in such a way that its
outputs can be studied. It involves identifying
what type of information would actually be useful to collect so that you can answer not just expected questions
about your system state, but also unexpected ones. It is about exposing and
collecting that information in a way that is unobtrusive, performant, and flexible enough to transform
that information if needed. But we're not observing just to observe, or at least we shouldn't be. We're observing so that we can make our
systems more reliable. So observability also requires that we present all the information in a way that is
understandable and actionable, and that ensures that the right people can do something about it. Only by doing all of this can we make sure that our systems are
continuously reliable. If you'd like to learn more about Grafana, then check out this playlist
for Grafana for Beginners, or check out the links
below for documentation on how to get started with any
of the projects I mentioned.

