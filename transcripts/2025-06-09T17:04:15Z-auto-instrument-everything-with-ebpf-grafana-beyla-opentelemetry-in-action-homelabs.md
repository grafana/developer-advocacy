# Auto-Instrument Everything with eBPF: Grafana Beyla + OpenTelemetry in Action | Homelabs

Published on 2025-06-09T17:04:15Z

## Description

Grafana Beyla is a powerful eBPF-based auto-instrumentation tool for application and network observability. In this session, see ...

URL: https://www.youtube.com/watch?v=W6_wWrfvRIg

## Summary

In this presentation, Nikola, a software engineer at Grafana Labs, and Goutham, a product manager at Grafana Labs (soon transitioning roles), introduce Grafana Beyla, an auto-instrumentation tool designed for application and network metrics leveraging eBPF technology. They explain that Beyla can instrument services regardless of programming language, making it particularly useful for monitoring Kubernetes-based applications. The discussion highlights Beyla's capabilities for generating distributed traces and network metrics, which can correlate performance issues with resource utilization. Goutham shares his personal experience using Beyla in a home lab setup, emphasizing its ease of deployment and effectiveness in auto-instrumenting various services compared to traditional manual instrumentation methods. The presentation outlines the benefits of Beyla, including its community-oriented development and future as an open telemetry project, while also comparing it to native instrumentation approaches.

# Grafana Beyla Presentation

Hello everyone. My name is Nikola, and I am a software engineer at Grafana Labs. Today, we will discuss our product, **Grafana Beyla**. I'm here with my colleague, Goutham. 

**Goutham**: Hey everyone! I'm Goutham, a product manager at Grafana Labs, but only until the end of the week, so you'll see why soon. We aim to make this talk engaging, even though it deals with a deep technical topic. 

Alright, you probably know the drill; we have a Q&A section at the end. You can use this QR code to access the slides.

## What is Grafana Beyla?

For those who don’t know, Grafana Beyla is an **auto-instrumentation tool** that can handle instrumentation for both application and network metrics. I will explain what these terms mean and what they can do for you. Importantly, Beyla is built using **eBPF**. 

While the acronym eBPF means something specific, it's often just referred to as eBPF. I like to say the "F" stands for "F-yeah!" We support instrumenting all services, regardless of the programming language. We have lofty goals here: all programming languages, a variety of protocols, and it's Kubernetes-aware, meaning it can pick up all your labels and export them in your metrics and traces. Sounds promising, right?

### How Does This Work?

On one side, I have a k9s screenshot of a cluster with multiple services running. With Beyla, you can easily get **red metrics**, build attractive graphs, and even visualize how upstream and downstream services connect and communicate. With Beyla 2.0, we can easily get **distributed tracing** for HTTP (no gRPC for now) out of the box. 

This means one tool and one installation does it all. The distributed traces are interesting because, for example, if you have an Istio-wrapped service, we capture not only the application traces but also the traces for Istio itself. You can see how much delay it adds sometimes. 

We can also gather network metrics, which is important because we can correlate them with previous metrics, such as red metrics. This allows us to determine if slow responses are related to extra load or maybe correlate them with CPU utilization. 

Because we pick up all those nifty labels from Kubernetes, we can identify things like the AZ zone in which the service is set up. If you have a misconfigured service communicating with a remote database, causing unexpected cloud costs, you can detect it with this tool.

### What is eBPF?

So, how does this all work? eBPF is a technology built into the Linux kernel. It acts as a virtual machine where you can create programs that attach to various aspects of your application stack. 

When an application runs, regardless of the programming language or whether it uses managed runtime, it eventually interacts with the Linux kernel. With eBPF, we can tap into any aspect of this stack and extract signals, which we then turn into telemetry. We can send this telemetry in an open telemetry format or export it directly to Prometheus.

### Why is eBPF Better?

In my opinion, eBPF is better than other solutions because it doesn’t destabilize your kernel. Unlike the kernel modules of the past, which could crash your machine, eBPF is built to plug in and out while your production systems are running without impact. This is made possible by a verifier that prevents loading potentially destabilizing programs. The programming language we use is similar to C, but it’s not complete; you can’t write a program with loops, for example.

### Practical Implementation

Let's look at a practical example. Imagine building a simple service that communicates with a Redis database via HTTP. You have many choices of programming languages and frameworks. Suppose you choose Python. 

On one side, you have various frameworks to build your service, and on the other, multiple libraries for Redis communication. 

As a software engineer, you start building this service. Months later, you realize you should monitor its performance in production. One way to add telemetry is by manually incorporating open telemetry, adding trace points and spans, and handling context propagation yourself. However, this approach quickly becomes tedious and difficult to maintain, cluttering your application code.

If you're lucky, the libraries you use support auto-instrumentation. But if you wrote this service years ago, you might be using an obscure library that isn’t supported by the open telemetry SDK. 

### The Insight Behind Beyla

We realized there’s a gap in open telemetry tooling: many users cannot instrument their applications due to various constraints, such as legacy software or lack of source code. This is where Beyla fits in; it acts as a **protocol instrumentation tool**. Beyla understands HTTP, regardless of the programming language or framework.

Beyla monitors the TCP stack—sending and receiving messages—allowing it to see the HTTP protocol even when SSL is involved. It taps into libssl to extract the necessary information. Beyla also monitors what happens in the application itself, how it manages threads, and interacts with the Linux kernel. 

By matching this logic, Beyla can achieve the same results as manual instrumentation without needing to know the specific programming language used. Of course, we do have special handling for Go and Node.js to manage asynchronous operations.

### A Look at Distributed Tracing

Here's a simple trace of what it looks like if you were to instrument an application with Beyla. You can see a GET request stacked under something like a Redis call. This is quite simple, but distributed traces can become much more complex.

### The Journey of Beyla

Developing Beyla was not easy; it took about two years to get it right. As we worked on it, we realized it wasn't just about Grafana. We built it for the community so everyone could try it. Initially, I wasn’t sure if this would be as effective as instrumentation with the open telemetry SDK. However, as we built it and had people use it, we discovered it filled a specific gap in the open telemetry tooling.

Ultimately, we donated Beyla to the OpenTelemetry community to extend its reach beyond Grafana. This project is now community-owned, with Grafana supporting it.

## Goutham's Experience with Beyla

**Goutham**: Thanks, Nikola, for all the hard work in creating Beyla. Now that we've seen how Beyla works, I will share my experience using it.

I’ve been an engineer at Grafana for five years, building products in Grafana Cloud. I was familiar with what was good, what was lacking, and I thought I could be a good product manager. However, after becoming a PM, I stopped using the tools I was involved in, which was disappointing. 

After five years, I decided to return to engineering because I miss being on call. To keep using the tools we were building, I collected a bunch of Raspberry Pis and random hardware to create a home lab. I ran Kubernetes on it and wanted to use our tools, but first, I needed to monitor some services.

### Self-Hosting

Self-hosting means running services on your own infrastructure instead of relying on a cloud vendor. I started this journey without much knowledge, but I found an amazing website called Awesome that lists potential self-hosted services. 

I began by self-hosting services like a habit tracker and an article bookmarking service. I even built a magazine for my friends to publish articles. Once I set up these applications, I wanted to monitor them. 

How many of you have a home lab? And how many of you get paged if one of your home lab services goes down? I wanted to go beyond traditional infrastructure monitoring with Node Exporter and Prometheus. I wanted APM capabilities, red dashboards, traces, and SLOs, but I quickly realized most applications have no metrics or inconsistencies, making it hard to manage alerts and dashboards.

### Monitoring with Beyla

Because I was self-hosting various applications, I needed an easy way to instrument them. I decided to use Beyla because it offers a consistent set of metrics and dashboards. Beyla allows me to instrument all languages and frameworks without the need for manual instrumentation.

I set up Beyla using a simple Helm command, and once it started emitting metrics, I could use a dashboard created by my colleague to monitor everything in my Kubernetes cluster. 

### Live Demo

Let’s switch to the live demo. You can see the red metrics and the different operations happening on my archival service called Red. Beyla instruments everything in my Kubernetes cluster, even without traffic, which is impressive.

We get full distributed tracing from the black box exporter to Red, which redirects to other services. This all comes from Beyla, which is fantastic.

### Conclusion

In summary, I built an application to track my books using a supermarket ISBN scanner. I instrumented this application natively to compare it with Beyla’s instrumentation. I found that while native instrumentation requires additional boilerplate and context propagation, Beyla provides telemetry out of the box.

However, Beyla doesn’t allow for extending telemetry with additional context in the code. 

Ultimately, it’s not about Beyla versus native instrumentation; Beyla gives you a fast start, covering 80% of the workload. You can then focus your engineering efforts on the most critical applications for complete instrumentation.

Thank you!

## Raw YouTube Transcript

Hello everyone. My name is Nikola, software engineer at Grafana Labs. We're
working on this product, Grafana Beyla. That was announced here. This
presentation is about Grafana Beyla, and here I'm here with
my colleague Goutham. Hey everyone. Again, I'm Goutham. I'm
a product manager at Grafana Labs, but only until the end of
the week, so you'll see why. So we're going to try to
make this talk interesting, even though it's a little bit about
a really deep technical topic. So hopefully we'll succeed. It's an
exercise in doing that. So, all right, you probably know the drill. We
have a QA section at the end. You can use this QR code to
get the slide a link. Alright, so what is Grafana? Vela?
For those that don't know, it's an auto instrumentation tool
that can do instrumentation for both application and network metrics. And I'll talk about what they mean
and what they do for you and so on. But it's built importantly
with this technology. eBPF, and I was told I could say this,
but I'm going to tone it down a bit. The acronym eBPF means something,
but everybody talks just out eBPF, and I like to say about
the F stands for F-yeah, and we support instrumenting all services.
So it doesn't matter what programming language, we're going to set some lofty goals
here. All programming languages, variety of protocols,
it's Kubernetes aware, so it can pick up all your labels and
stuff you have and export them in your metrics and traces. Sounds very
promising, right? Okay. Alright, so what does that mean really? So on here, on one side, I have a k9s screenshot of something
that's a cluster with a bunch of services running there. And boom, you can
easily get red metrics out of it, build pretty graphs and even see
upstream and downstream services, how they connect and talk to
each other. It's kind cool, but with Beyla at 2.0, we can easily get distributed
tracing for HTTP, no gRPC for now, but HTTP distributed tracing
out of the box one tool, one installation of this
thing does the whole thing. And this distributed traces are kind of
interesting because here I have an Istio wrapped service, so we're not getting
only the traces for the application, we're also getting the
traces for Istio itself, so you can see how much that
adds delay sometimes. And we can also get network metrics.
And why is this important? Because we can correlate now this
network metrics with the previous, say the red metrics, and we can see if maybe our slow
responses are related to some extra bytes, loads and so on, or maybe correlate them to the CPU
utilization and all this stuff. And because we pick up all those
nifty labels out of Kubernetes, we can pick up stuff like the AZ
zone in which the service is set up. So if you have a misconfigured service, they're talking to remote database and
that's costing you on your cloud bill for the AZ zone traffic. You can detect it with this and find
out those misconfigured services. So how does this all work?
What have we done here? What is this eBPF, F-Yeah, so well, it's a technology built
into the Linux kernel. It's a virtual machine for which you
can actually build programs and you build these programs and what they do is
they attach to various aspects of your application stack.
So the application is running, written in some programming language.
Maybe it's using managed runtime, maybe it's just a binary, it's using any libraries on your system
and eventually it's using the Linux kernel. Well, with this technology, we can tap into any aspect of
this application stack and we can extract signals which we
then turn into telemetry. We send them to an open telemetry
format or we can export them directly to Prometheus. This is how
this magic happens. Now, why is this better than
everything else, in my opinion? Because one thing, this technology will never
destabilize your kernel. It's not like the kernel modules of the
past where you load a kernel and boom, your machine is dead. This is built for the purpose that
you can plug something in while your production systems are running. You can take it out and there should
be no impact on your system. And that technology is actually
real because of this verifier. It won't let me load a program that
could potentially destabilize the kernel, the programming language
we use here is C like, but it's not even pure and complete. You cannot actually write a
program with loops, for example. So with that said, let's look what this does in practice. So here I'm going to try to
build a very simple service. I don't know, maybe takes this one API through
HTTP and it talks to Redis database. We've all built something like this. And so what do I build this
in? I have lots of choices. I can build it in Python, I can
build it in Java, maybe node js, whatever is my favorite
programming language. And then once I build it in
that programming language, I have lots of choices about frameworks
that I can use to build this web. So I can choose the stuff that
fits my way of programming. Maybe I don't know what I'm doing. I'm going to use an LLM
and they suggest something, I'm just going to go with it.
But either way, for this purpose, let's look at something if we
did this in Python. All right, so on one side you can see all the
possible frameworks I could have chosen to build my service, whatever. I found something on the
internet looked good, I tried it. And on the other side, I have many choices that I can
actually build the Redis communication with. So how do I actually
get from this telemetry? I'm a software engineer. I
start building this service, I build it out and it's working. And then maybe a couple of
months later I realize, oh, I should be monitoring how this
performs in production. Well, how do I actually add telemetry? One
obvious way is maybe I'll manually start using the open telemetry as the
case and add my trace points and spans and do the context
propagation myself. But it gets tiring really quickly. It is difficult to maintain. It adds so much code now that it's not
actually related to the logic of the application service itself.
I would not want to do that. So then if I was really lucky, maybe the libraries that we're using
support auto instrumentation or the versions that I picked up, maybe it's
a service I wrote three years ago, and it's using some obscure library
that's not actually supported by the open telemetry SDK instrumentation. So these problems arise more than with
various people trying to implement this. And we've seen a lot of these
cases with Grafana as well, but it's not all doom and gloom. If we will actually look at
this and zoom out a little bit, not really.
There's only two protocols here, right? I mean there's HTTP and Redis. Could we not just instrument the protocols
and get the data there and figure out this? Why worry about what
the frameworks are doing? They're all speaking the same
language in the end of the day, and this is a sort of insight we
had when we began working on Beyla, because Beyla is essentially a
protocol instrumentation tool. It understands HTTP doesn't know that
this is running Python running on top of this framework.
Django, it doesn't care. So let's see how Beyla actually
does this instrumentation. So what we have here is
we monitor the TCP stack. So TCP send message, receive message. Therefore we're able to see the HTTP
protocol incoming, even if it's using SSL, Beyla taps into libssl, and it's able
to extract the information again. Then we monitor what's happening
in the actual application itself, how it's managing threads, how those interact with the Linux kernel
to pass the work around. And on the other side, we'll look at what the protocol Redis is
doing and extract information about the Redis protocol. Matching this
together through various logic, we're able to do the exact same thing
as you would do with your manual instrumentation. Again, we didn't care pretty much what
the programming language is, which is sort of true, not always. We do special things for say go to
handle goroutines and node JS to handle the async event loop, which is
different than running normal threads. With that said, here's a simple trace, what this would actually look like
if you were going to instrument this application with Beyla. Nothing to it. So we have the get request coming
in and then we see that it's stacked under something like a Redis call.
Now this's just pretty simple. Distributed traces can get a lot more
complicated, but this is the gist of it. Now it may seem like, okay, that
sounds good, let's go and do it. This was not easy to actually do. It
took about two years to get this right, more or less. We've been working this. I've personally since I started at Grafana
on this one project doing just this, it's been a lot of effort.
And having said that, we thought about, alright,
so this does a lot of things, but it's not about just Grafana. We're not going to build this so we can
run it with Grafana products and we're going to be bundling this with
Grafana. We built it for the community, we built it for everybody to try this. And initially when I started on this
journey of building the eBPF tool, I didn't know what to
expect. What was this about? Was this ever going to be as good as
instrument with the open telemetry SDK? But as we built it and we
actually had people use it, we realized there was
actually a specific gap in the open telemetry tooling that
this tool was covering. And that was places where people
could not instrument the applications or they wouldn't, let's say they just didn't have
enough time or people that used legacy software, which was
not easily instrumented with open telemetry as the case, or perhaps they didn't even have the
source code of these applications they wanted to monitor. They were just
binaries they were using using. And this is the case where Beyla
really fit and closed the picture. With that said, this made us kind of move to the next
step in the evolution of this product, which is we have actually
donated Beyla to open telemetry. That was a process that started about
six months ago that we worked with the Open Telemetry community and CNCF
to actually make this project go beyond just Grafana. It's
a community owned project, but it's known in that Grafana
will stand behind this new project. All the maintainers of Beyla
will work or the upstream project upstream first or Beyla will
eventually be just Grafana distribution of this open telemetry
eBPF instrumentation tool. And now thank you. Now I'm going to let my friend
Goutham here talk about the stuff he's been doing with this tool, which is a lot more
interesting than my spiel. No, thanks a lot for all the
work and for creating Beyla. Now we've seen how Bayla works. I'm going to talk about a little bit
about how I am using Beyla and what the experience of using Beyla
is. So for a little context, I've been an engineer for
five years in Grafana. I was building all of these
products in Grafana cloud. I was on call for these products and
I was using everything that I was building and I had a fair idea of what
was good, what was bad, what was missing. And I had this crazy idea that, oh, I can be a good product manager because
I know the product and I know what's missing. And then I became a PM and I
stopped using all my tools, which honestly kind of sucked.
So after five years, I've kind of decided to go back to
engineering. I realized I like building tools, but I also like being on
call and I actually soly miss being on call. So I also did not want to
wait to go back to engineering to use all the tools that
we were building at Grafana. So I decided to collect all the
raspberry Pi's and random stuff and build a home lab. Turns out I have a lot of different
random stuff just lying around and I was like, oh, I
might have a problem here, but now we have a solution
for the problem. So yeah, I collected all the raspberry pies and
all the different weird knucks and old things and I just hooked them up. I ran
Kubernetes on it and I was like, okay, now I want to kind of use all
the tools that we were building, but before I did that, I needed to monitor some services.
So I decided to start self-hosting and running a few services. So self-hosting is
basically the process of running your own service self-host
the service on your own infrastructure instead of relying on a cloud vendor
and paying them money or your data. And basically I had no clue. I just built up this whole home lab
and there's this amazing website called Awesome that gives you all the
potential things that you could self force. And I've scrolled this multiple times
and I started self-hosting a few things like my habit tracker
or this bookmarking service where every interesting
article I find, I archive it. Even if the original ring disappears,
I still have a copy of it. I can search through
things and stuff like that. I started slowly adding more and
more things to this home lab. For example, I quit Twitter
even before Elon Musk bought it, and I really missed tweeting out.
So I wanted to have a Twitter, but for myself. So there's this
amazing project called Memos, which is like Twitter, but for yourself. So I just started using
that and I had this, one of the ideas that I had was, what
if there's a magazine for random stuff? My friends write and yeah, a month later I have a
magazine for me and my friends. But now that I was running all of these
weird services, I now was like, okay, I'm ready to observe them. So
how many of you have a home lab? How many of you get paged if one of the
services in your home lab goes down? Okay, you brave souls.
Me too. Me too. Yeah, and of course there's the traditional
infrastructure monitoring with node exporter Prometheus. But I
wanted to kind of go beyond that. I was the PM for a the APM pmm. So I wanted something like this. I wanted red dashboards and traces
and all the cool stuff that we were working on. I also wanted
SLOs for whatever reason, but turns out they don't work.
When you don't have traffic, you have a hundred percent
of your requests succeed, so you never get paged until
you use it. But anyways, now that I was self hosting
all of these applications, I wanted to monitor them.
And turns out for traditional hobbyist use cases, most of the
applications have no metrics at all. Even if they do have metrics, there is
no consistency between applications. So essentially, if I were to kind of use the
metrics that the application I made, I need to have a set of alerts and
dashboards for each different application. And this is just too hard
to manage. And finally, I had this weird idea that I might
be able to contribute back if the applications were in go.
So I decided to run go. But then there is no auto
instrumenting for go. If it was Java, I could do the Java agent and maybe I
would have consistent sets, but well, I dug this hole myself. So I came up with a criteria
on how to monitor these. First it needs to be easy to instrument. No matter what I pick from various, I run self-hosted applications of various
languages and frameworks. They need to be easy to instrument. I need to have one set of alerts
and dashboards for everything. And I can use a dropdown to kind of
pick application A and application B. I run K three s, so anything that I
pick needs to work with Kubernetes. But I had the most important criteria.
I like public speaking and I was like, I need to build all of this with cool
tools that I can blog and talk about and get accepted conferences. So yeah, with this criteria, there's actually only answer for the
consistent set of metrics and dashboards, which is open telemetry
semantic conventions. So Otel semantic conventions I think
are its superpower. We just say, Hey, if you're monitoring HTTP, you need to basically have this
particular metric emitted with these particular attributes. And there's the
same across frameworks and languages. So if I rely on semantic conventions, then I can have one set of dashboards
and alerts. So how do I get semantic conventions out? So there's something
called the open telemetry operator, which helps you auto instrument
all your applications in Kubernetes. So it provides in-depth instrumentation
like almost native instrumentation where possible. However, it's not
always possible. For example, with Java it's possible,
but with go or rust, it's not very possible because there's
no auto instrumentation. However, if it is possible, you can kind of use auto instrumentation
but also extend it with additional attributes inside the
application code itself. So you don't need to fully instrument it. You can partially instrument
it and add context. However, you also need to tell it, Hey, this is a Java service and you need to
restart that service for all of this to work. On the other hand, we have Nikola and Beyla
who basically, yeah, it's just a demon set that you run. It's a simple helm chart and it gives
you everything out of the box for all the languages.
However, the drawback is that you
can't extend the telemetry. So whatever Beyla gives you is
the kind of final telemetry. You can't add additional context
in the code itself. Cool. Well, I chose Beyla because it has eBPF
and eBPF will get me to conferences. Alright, so how do I deploy? It's actually quite simple. Unless
you're running a Raspberry Pi. If you're running a Rasberry Pi, you
have to recompile the kernel. But yeah, if you're not running a Raspberry Pi, you just need to run this helm install. And it's super easy to get started. And once it started emitting
native semantic conventions, I could use this dashboard
created by my colleague to kind of instrument everything. So
let's quickly go through that. Can we switch to the live demo, right? Oh yeah. Wait, no. Switch to live demo. Yeah. I am mirroring, I think.
Yeah, I'm mirroring. Can we switch to the live demo? Alright. Okay. You don't need it.
It's a very cool dashboard. Oh yeah, it works now. Okay. Yeah. Okay. So yeah, you can see
kind of the red metrics. You can kind of see
the inbound operations, like the different kind of operations
that was happening on this particular archival service called red. It's like
you can choose a different service. It just instruments everything.
In my Kubernetes cluster, what is really also shows you
outbound requests and stuff like that. But what is really cool is the
traces, which you can see here. Again, I don't have traffic, I just
have a black box exporter probing it. But you get full distributed tracing
from the back black box exporter to red, which then redirects
it to the login thing. So there's like a 302 and then
that goes back to readeck. And this is neither black box exporter, nor readeck is instrumented with Otel.
All of this is coming from Bayla, which I think is really cool. If I
had a super cool, huge architecture, I think the trace would look
cool, but I don't, yeah. Okay, let's switch back to the slides. Okay. It's happening. It's happening. Okay, whatever. How many of you have the habit of
buying books but not reading them? Ooh la. Okay. Turns out
I have the same skill. There's a name for this skill.
It's called Sudoku in Japanese. And well, I have a lot of books and I don't
always read them and sometimes three times, maybe four. I
bought the same book twice and I was like, okay,
this needs to be solved. So I built an application to track all
my books and exactly which shelf they're on. And then to do this, I bought
a supermarket ISBN scanner. So yeah, so I have this application
where I scan a book, scan a shelf, and it belongs to that shelf
and I can buy a new book. I can just scan it and it looks up
the ISBN details and populates the information. So this is a very
simple service that I've written. I'm running it on my home lab with
tail scale and all the cool things. I even built a TUI for
it. I can't build UIs, so I wanted to have borrowing and stuff. So I decided to instrument this natively
to understand the difference between bayer's instrumentation and native
instrumentation. What is different? So yeah, so basically, essentially there's this 200 lines
of boilerplate that I copy pasted, maybe ask Chat GPT, do it, and then it basically set up
tracing for this Golang application. All it had to do was set up Otel, SDK,
and then put all the garbage here. And then it works easy with Bayla, there's a debug endpoint. What it
does is it gets this ISBN lookup, it sends a request to Google books, it sends a request to open library and
then merge just the data to kind look up the book details. So this
is what Bayla generates. You can see server address
HTTPs, all of this really cool. I did this with native instrumentation
and basically all I got was, oh, there's a request on this endpoint,
but none of the outgoing requests. Turns out there's this thing
called context propagation, which GPT did not do for me.
So I had to do it manually. So once I've done that, and once
I've changed HTTP to Otel HTTP, I could see the outbound
calls, which was really cool. But then instead of server address, I was looking at HTTP url and it's
like, wait, with semantic conventions, everything needs to be
the same. Technically yes, if you're on the same version
of the semantic conventions, turns out the SDK is on a way older
version of the semantic conventions. So the SDK generated telemetry and
be generated telemetry is different. Bayla on the latest version. I don't know
if that's a good thing or a bad thing, but I found that the, it's. A good thing on the stable one. Yeah. Cool. And the next thing was
I wanted to instrument SQL calls. So I do a lot of SQL calls into the thing. I look up all the books and
the shelves and everything, and I wanted to do SQL
instrumentation. I googled for it. Turns out there's seven
libraries that do the same thing, but in slightly weird ways. So you ask chat GPT to pick one of these
SQL instrumentation libraries for me and the chat GPT pick the third one.
I don't know why, but it's okay. And I instrumented the SQL
calls. It was quite simple. I just needed to say auto SQL
instead of SQL and register DB stats. And each SQL call was
its own trace. So again, Chat GPT did not pass the context. And so I had to kind of go
back and manually change every call to pass the context here.
And once I've done that, you can see that all the SQL calls are nicely
instrumented. So, oh by the way, there's like 2000 SQL calls every
time I do a lookup on books because Chat GPT wrote this and not me,
but I only have two 50 books, so it's not a performance
concern yet. So it's okay. What I found really interesting is you
get full details about the SQL query and the templated queries
that are being done. If you manually instrument
it while Baya looks at the kernel level, and it can
look at the whole SQL query, but it does not want to show it to you
because it might have secrets in it. So this is kind of what you get
between native instrumentation and auto instrumentation. It's a slight trade off. But what I realized was
it's actually not Beyla versus native instrumentation, but rather it took me
several hours to manually instrument a very simple go application. And if you suddenly have 20
applications, you tell your engineers, now you have to go manually
instrument everything. They're just going to go
on holiday together. So what Bayla gives you is within
one command you get 80% of the way and then you can use your
engineering bandwidth to say, actually these two applications
are the most important. Let's manually instrument them correctly. And then you can kind of go through this. So you can think of Beyla as a
fast start before you go to the whole full instrumentation.
Alright, that's everything.

