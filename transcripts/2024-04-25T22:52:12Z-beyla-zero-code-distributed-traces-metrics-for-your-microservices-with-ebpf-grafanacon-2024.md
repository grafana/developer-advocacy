# Beyla: Zero-Code Distributed Traces &amp; Metrics for Your Microservices with eBPF | GrafanaCON 2024

Instrumenting applications to capture observability requires technical effort and cultural changes, especially when dealing with ...

Published on 2024-04-25T22:52:12Z

URL: https://www.youtube.com/watch?v=Fe4MG1UxAl4

Transcript: Thank you a lot for the
introduction. So my name is Mario. I am one of the engineers
of the Beyla team at Grafana, and I will explain today, briefly what Beyla's all about
and how to use it to instrument your running services without extra configuration or
redeployments from your site. This is a short talk. There will be
no questions, but after the talk, you can find me at the Grafana booth. So come say hello and ask whatever you want. So what do we mean by
auto-instrumentation? Let me just put some
context. Auto-instrumentation already existed before Beyla, of course, and it was based mostly on injecting an agent between your application
and its runtime. For example, the Java virtual machine or
.NET or any other runtime. Those run times usually
provide mechanisms to inject an agent that is able to
listen for some events, intercept them, and then, for
example, provide or export metrics and tracers. Beyla is not here to change
that. So if that works for you, keep using it because
they usually work like a charm, namely the OpenTelemetry
agents or the Grafana language agents, they work pretty
well, but there are some cases that you could have some problems
with auto-instrumentation. So what happens with
auto-instrumentation, for example, if your runtime is too old? If you're using an old
Java virtual machine or from a given implementation of the
Java virtual machine that does not support most of the modern language agent, or what happens if your runtime, is in an interpreted language and the instrumentation agent is written in
this language agent and adds some of overhead to your service? Or
even if you cannot auto-instrument, you cannot inject any agent because
your application is a compiled binary, a Go binary, a Rust binary. In that case, you could instrument it manually
inserting the probes into your code, but you need to redeploy your code. Maybe you don't have the
resources or maybe the, the code is legacy and nobody
wants to, to touch it. To cover those cases. Beyla uses eBPF. eBPF is a virtual machine that modern Linux kernels
provide that allows you to inject some  that is compiled just in
time and alerts you attaching programs efficiently at your
application runtime or at the kernel runtime. It alerts
you peeping the memory of, of your, of your run times, applications and modify or just read it to get insights about what's going on. So Beyla uses eBPF is
deployed as a privileged process in your host. And without having to reconfigure
or redeploy anything from your applications, Beyla attaches to some eBPF
hooks to provide metrics and traces about your application, mostly focused on web application. Beyla then exports this
information as metrics or traces via standard endpoint,
like OpenTelemetry endpoints, Prometheus, or even you can send
the data directly to Grafana Cloud. So Beyla is vendor neutral. What metrics provide Beyla? The language with the most complete support
is Go currently. With Beyla, you can instrument your applications
and get out of the box. HTTP, HTTPS, HTTP2, and gRPC metrics. More protocols will be
supported in the future. We need to clearly
enumerate what we support, because many people might think that eBPF is like magic. You put
everything there, say, "Hey, tell me everything." And eBPF returns
you the information. But with eBPF, you need to work at the binary level. So adding new protocols mean
knowing how those protocols are organized at the binary level. How a given language is
also organized at the binary level. So you can read
their variables at runtime. So protocols need to be added one by one. For Go, Beyla hooks into the Go
libraries and runtime. But Beyla is also able to
hook and listen to some kernel libraries. That way, it's able to provide also
basic metrics for almost any other language. For example, it's able to provide
HTTP and HTTPS metrics. HTTP for virtually any
language that can run in in Linux and HTTPS for
any language, but Java. Java brings its own TLS library, which
is compiled at the Java by called. Its it's much more complex. We are also able to provide traces For Go applications, Beyla provides fully distributed tracing.
That means context preparation, so you can see your traces, and how they are related with other
traces for all the protocols we already mentioned, HTTP, HTTPS, HTTP2, and gRPC, and for the rest of
programming languages at the moment, it's able to provide single spans or partial support for distributed
tracing only if the processes with the same context are in the same
host. This difficulty comes because for providing distributed
tracing, Beyla needs to not only read your HTTP information, but also being able to modify
it, modify your , and that comes with a lot of security restrictions and support. That's why in the rest of programming
languages it's still limited. I will do a quick demo just
to show how Beyla works. I deployed a distributed application. The application is written in Go. We have a load generator that
sends data to a frontend. The frontend sends data to a
backend and that backend distributes the load across workers. And Beyla. One of the, the points we focused on Beyla was try, even if it's highly configurable, try to let Beyla run with minimal
configuration and with minimal configuration, have something working. So Beyla just needs two
configuration options. One is ssome coordinates, some indications
about where to instrument, what application to instrument. You could say Beyla instrument all the
process in your host in a given host, but maybe you don't want that, and
you want to instrument a subset, automatically instrument a subset
of applications because the other applications might already be
instrumented. So in this example, Beyla can run in any host
physical or it doesn't require Kubernetes to run. It can run in
bare metal. But in this example, oh, it's okay. In this example, we are providing
a yaml configuration telling Beyla In the demo it's deployed in Kubernetes. This simple configuration
we're telling Beyla: instrument all the applications
that are either in the demo namespace or either in
the it's block namespace, it's just a namespace in the example. So Beyla will look for all
the processes running or, or all the processes belonging to
pods running in such name space. But you can also provide extra
configuration in order to have a richer experience.
So you can, for example, tell Beyla to get the HTTP roots, the roots of your HTTP or gRPC service, and to avoid having a
cardinality explosion grouping those routes heuristically.
That will mean that, for example, it will try to identify
any user ID or any ID the some gibberish words into
your roots and group them as IDs. All the routes
having the same pattern as the same route. You can also
provide manually your own routes, so you make sure it will capture the
roots as you want. And we will tell, for example, also decorate the metrics and traces
with Kubernetes attributes. The other, the other mandatory configuration
option of Beyla is tell Beyla how to export the information.
You can tell Beyla, okay, just open a Prometheus
port, or in that case, send this data. Send this data to the OpenTelemetry endpoint. Here we just provide two
standard OpenTelemetry configuration variables to point
to Grafana Cloud with some secret that obviously we are not sharing here. And then Beyla will, out of the box, send the data to Grafana as queries, or as metrics and/or traces. Here in this example you can see a dashboard we already provide. It's
free to download. It's freely available, in which you can see some basic metrics
information about your applications like slowest HTTP, route or methods. Can you see this factorial asterisk. This factorial was followed
by a number that could vary depending on the invocation. And Beyla automatically has
grouped it as an asterisk. And there you can see
all your applications, the backend, the frontend. This load gen is empty because it
simply doesn't have inbound traffic. So you can see the inbound traffic of
your services and the outbound traffic. Beyla also works with other other parts of Grafana
Cloud, like the application, our application observability.
You can see here all the services, how they are partially integrated.
Not all the parts work, but you can also see here the
traces and how the traces are distributed. You see here,
the backend, the worker, so every trace that Beyla has
captured propagate the context of the color and the . And even you can see also the,
the service map of the frontend, the backend and so on. So that's all about what I wanted to to share with you. So what are the future plans of Beyla? On one sidem we want to
support more protocols like SQL message queues. This SQL will depend on the
different bunch of SQL libraries, message queues, protocols and so on. We would like to extend and improve
and provide distributed tracing. So you can get distributed traces for
more languages and in more context, not only for Go. And the last version
of Beyla also provides experimental support for
L2, L3, and L4 metrics. So in your cluster, you will be able to see
from two endpoints how many bytes and all this information
being decorated with metadata like hosts,
Kubernetes, metadata and so on. Thank you for your
attention. As I said before, you can find me outside if you
have any questions or any comment. Thank you very much. Very much.

