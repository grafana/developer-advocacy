# Instrumenting Java with eBPF: TLS, Threads, and OBI (OpenTelemetry eBPF Instrumentation)

Published on 2026-05-14T17:18:12Z

## Description

Instrumenting Java with eBPF has long been a hard problem — dynamically compiled JVM code, thread pools, and Java's own ...

URL: https://www.youtube.com/watch?v=M2t0xkjT-os

## Summary

The community call titled "Instrumenting Java with eBPF: TLS, Threads, and OBI (OpenTelemetry eBPF Instrumentation)" was held on May 14, 2026, featuring Nikola Grcevski, a software engineer at Grafana Labs, and Endre Sara, a co-founder at Causely. The discussion focused on the challenges of instrumenting Java applications using OpenTelemetry and eBPF, particularly around TLS encrypted traffic and the complexities of Java's dynamic compilation. Key takeaways included the introduction of a Java agent for TLS instrumentation, the benefits of using eBPF for zero-touch instrumentation, and the complementary nature of the Java agent and eBPF solutions for comprehensive application monitoring. 

Topics: OpenTelemetry, eBPF, Java instrumentation, TLS, Grafana Bela.

## Chapters

00:00:00 Challenges of instrumenting Java applications
00:06:13 Instrumenting Java applications with eBPF and OpenTelemetry
00:11:38 Instrumenting Java applications with eBPF and TLS
00:16:59 TLS-based context propagation challenges in Java instrumentation

- Hey everyone, how are things going? Good, I see people leaving already, so. 

- **Endre**: All that Java. 

- **Nikola Grcevski**: All that Java, nobody cares about Java. My name is Nikola Grcevski, I'm a software engineer at Grafana Labs, and here I'm with- 

- **Endre Sara**: I'm a co-founder at Causely. We are providing a causal reasoning platform on top of semantic data. If you're interested, feel free to find me afterwards, but here we are talking about- 

- **Nikola**: Yeah, talk about Java, yeah. And OpenTelemetry eBPF Instrumentation. Okay, let's go. 

- **Nikola**: So, why are we here? I think Java is still the most popular programming language, especially in large enterprises and financial institutions, with many popular frameworks like Hibernate, various asynchronous messaging libraries, Spring Boot, Quarkus, and also the OpenTelemetry Java SDK is probably the most comprehensive and the most mature instrumentation library. However, it is not easy to get it into production all the time. There are several challenges that we want to talk through in terms of why we are discussing Java, what are the specific challenges around Java, especially diving deep into TLS encrypted traffic, and an overview of OBI. Then we will move on to a couple of examples that we share on how to actually try this out if you want to explore this further.

- **Endre**: Yeah, so tell us about some of the problems that you encountered trying to instrument Java applications.

- **Nikola**: One of the most obvious things is how do you get the native auto instrumentation into production. For example, we have one of our large customers; as we engaged with them, within weeks they had Java instrumentation in their staging environment. However, it took several months, more than six months, to get the first production application instrumented. This was not due to any technical reason, but simply operational reasons of how to change the code. Additionally, there are a number of other customers with third-party applications that you simply cannot touch because you don't have the ability to rebuild them or to change the way they start. Similarly, with legacy systems and older versions of JVMs, we are also working with a number of financial customers where injecting code into the runtime of the application is difficult due to the risk and impact of those changes. So for many of these situations, while I think it is an amazing capability to be able to use native auto instrumentation, sometimes people simply don't have the luxury to do so.

- **Endre**: Yeah, and on top of that, there's a whole ecosystem of people running GraalVM native, where they want to shave, I don't know, a couple of hundred milliseconds off a JVM startup, so they build their applications into native from Java, and the agent cannot be loaded.

- **Nikola**: Okay, so let's talk about eBPF and Java. This has been a sore point for a project that I worked on since the beginning, Grafana Bela, and Java; we were never able to do well. There are a couple of reasons for this, but primarily it has to do with how to instrument user space. In eBPF, which is a technology that allows us to build probes into existing running Linux kernel and existing running applications, you can set user space probes. However, for that to happen, you need to have a file. Everything is a file in Linux. Unfortunately for us, Java-generated code sits in anonymous memory regions; they're not files. 

You might think, well, maybe you can do some hacks such as ptrace into Java, stop it, and remap its memory regions into memory map files. That's doable. We've actually attempted it, and it works to some extent, but Java is a dynamically compiled language, which means that run to run, Java does not have the same code. The reason for this is that it starts by interpreting the bytecode, and at this stage, it collects profiling information about what's important to optimize, which drives the compiler that optimizes the code in multiple stages. Therefore, your code is actually never the same from run to run on any Java application. 

Building instrumentation at the assembly level, essentially at a binary level, would make us cast a really wide net of where we have to put these probes. I don't want to get into a situation where I ran this application once and it worked, but the next time I ran it, there was no instrumentation. So it was an approach we never saw as viable. 

We wanted to solve primarily a TLS problem that Endre mentioned. Initially, when this problem was brought up around Java, I said it wasn't that important. There aren't many Java servers that run TLS. I was wrong. Not Java servers, but anytime you touch any cloud service, let's say you are getting a cloud-managed service from your favorite cloud vendor, that's going to go over TLS. Even though many people terminate TLS at load balancers, there are still quite a few who may even use Java TLS on the server. Additionally, most client calls to external services are done through TLS, so it's a very big problem. 

For a long time, we needed to solve this to be able to do this with eBPF in an environment where you can just plug stuff in without having to modify any configuration or any environment variables. It should just work out of the box, with no restarts. 

So this is a summary of what we ended up doing. Let's walk you through the steps of how we achieved this. This can get pretty technical, so bear with me. 

**OpenTelemetry eBPF instrumentation at a glance**: This used to be known as Grafana Bela; that product still exists. We just donated it to OTEL about a year ago, and we built Bela on top of this. It uses eBPF, installs kernel probes, network programs, and user probes to try to capture as much telemetry at the kernel level, and then converts this telemetry into traces and metrics after enriching it from various signals, such as Kubernetes. Now we have cloud metadata, and we're enriching it with host-level information and so on. 

This data can then be transformed further by using the OpenTelemetry Collector or Alloy, if you wish. The next picture is sort of a diagram of how this works in practice. Essentially, this software is installed as something on your Linux kernel, like a system process, which translates to something like a daemon set in Kubernetes. Once it plugs into all levels of your favorite applications, it can monitor multiple applications at a time. 

Once this telemetry is enriched, you can either send it to an OTLPN point somewhere in the cloud or enrich it yourself and keep it local, further into your own on-prem databases and so on. 

So how does this instrumentation happen? This is what we were able to do a year ago. When I presented something similar to this at GrafanaCON last year, we had this scenario. In this case, I'm talking about a Java server that's handling HTTP REST APIs, and at the backend, it's talking to Postgres. 

With the instrumentation we typically do, we get the protocol to show up in the kernel buffers. We read those and can say, "Oh, that's HTTP on the incoming side." We extract the route, the method, the payload, the headers, all this information, and then we have HTTP. On the backend, we see, "Oh, that protocol looks like Postgres." We parse and extract the SQL statement. From the SQL statement, we find the operation, the database name, and so on. 

This is all good. For the last bit over here, I'm assuming a very simplistic scenario where it's the same thread that handles the incoming request and the outgoing Postgres request. In that scenario, we're able to correlate between the two, incoming and outgoing. 

Now, unfortunately for us, this is not a situation that most Java applications actually run in. It looks like this in most cases. So first and foremost, I'll talk about the threads. It's rare that an incoming request is handled by the same thread as the outgoing request. Java applications typically have thread pools. So we have an...

Incoming thread pool handles all the HTTP requests, and we have an outgoing thread pool that manages the JDBC connections. Now, what about the traffic that a kernel sees? We can no longer see the actual payloads because it's just gibberish; it's TLS encrypted. While previously, for other languages, we could tap into LibSSL or BoringSSL, Java implements TLS in Java. There are exceptions where people purposefully use OpenSSL or BoringSSL through JNI, but the norm is to use the Java TLS encryption libraries built into the Java JDK itself. Therefore, we can't see anything—no instrumentation for these applications.

In OBI, we looked for a while at the ability to instrument with Uprobes, but we gave up because of the complexities I explained. So, we decided to build a tiny Java agent that can be dynamically injected. It could be a running process that accepts this agent, and we will load it with a very small number of probes that would be able to fill in the gaps we can't see at the kernel level. 

What does this mean? This Java agent only instruments TLS and the thread pools in Java. It's bare bones and doesn't instrument any application libraries. We wanted to keep the same concept as the rest of OpenTelemetry instrumentation—try to keep it as generic as possible so that we can instrument the world without having to instrument every individual library. It doesn't matter if it's built on top of Spring Boot, using Netty Reactor, or using Apache something. At the end of the day, it's still HTTPS. If we can tap into the protocol and add the TLS time, we could actually capture and get all of that data.

We've added one other piece of technology on top of this where we harvest the routes embedded into the symbols of the generated Java classes. For example, you may have in Spring Boot a path that says `/users/{curlybracesid}`. When you see that route coming on the buffers from the kernel, it appears as `users/123`. So we do that matching; we understand that this `123` matches to the Spring Boot path just like Spring Boot would do.

How does this actually work in practice? I know it's a lot to consume, but the two pieces of information to make OBI work really well with any programming language are: we need connection information, so we need to know who's talking to whom to find the IP addresses and ports, and then from there, try to enrich this information from Kubernetes. We also need the buffers so we can analyze the protocol and figure out if it's HTTP or Postgres on these sides.

Let's take one example we needed to do. Java internally, once we added the probes, has two modes to handle TLS. One is synchronous, where it's the secure socket—the class internally that everybody uses—and there are plenty of Java libraries that use that approach. It's the same class that handles both the communication with the peer and the SSL encryption. Great! We could extract both the connection information and the unencrypted buffers from the same instrumentation.

However, other implementations of SSL encryption in Java use two separate paths. For example, Netty has its own high-performance socket implementation but uses the SSL engine from Java to do the encryption. The actual work here is asynchronous; one part does the encryption, and the other part does the actual communication to the other side. So how do we correlate these buffers? It was actually an innovation by my manager, Fabian Staberg, who brought us the idea. He said, "You can track all the threads you want, but you'll end up in a situation where you miss and cannot correlate. However, if encryption is done right, the actual encrypted buffer should be unique enough for you to create a key. If the buffer is the same all the time, then what you end up with is encryption that can be broken into."

What we do is take a sufficient number of bytes of the encrypted text at the time of encryption and use that as a key in an in-memory map to the actual buffer that we want to read. That happens at encryption time. When this encrypted text is sent over the wire to the other side, we extract the key again, look up the map, and at that point, we have both the connection information and the buffer that we want to read.

Now that we have this information, how do we pass it to the eBPF side? It's all great; we found it in Java. This agent now does a very fast system call, `sysioctl`, where it communicates a Java buffer that has been created for us to read. This `sysioctl` call happens in the kernel, and this is our chance to set a K-probe with OBI that will intercept that call, read the information, and pass it to the rest of the OBI machinery to produce the telemetry that we need. We just filled in the missing pieces that we needed to get Java to work.

Endre here has been playing with this for the time we've been developing it. So why don't you tell us a little bit about the things you've done with this?

- Sure! We are working with a number of customers. For example, there is one customer running an edge security application with various Java clients, Spring Boot clients that are talking to Keycloak. Now, Keycloak is natively instrumented, but obviously, it's more important how the clients are interacting with Keycloak, which is over HTTPS. We have other customers in the digital marketing space that extensively use Google Pub/Sub, also over SSL, and then a large betting company that has a number of Java applications. Most of our applications are in Java, and they're using managed Postgres, as well as other managed databases over TLS, and Kafka.

Now, I can't bring their applications here, so I thought I'll write something that represents their information, and all of them are public or open source. Each of these can be deployed by a simple Helm chart in your own Kubernetes cluster. If you want to try any of this combination on how they work with Beyla, I actually have a branch that does native OTA instrumentation on each one of them, and then a branch that removes all the OTA instrumentation so that you could see how they work with Beyla or without Beyla with the native instrumentation. Have a lot of fun! Please tell me if there is anything that I could do differently about them, but try it if you want.

- We've had a number of bug reports from him coming in. He always tries some new framework and some new protocol, and whatever breaks, he says, "Hey, I tried this, and it didn't work." Then we make it better. So, a lot of trial and error, but we have a bunch of trade-offs still. Why don't you tell us what works and what doesn't?

- A number of things work very well. I tried several scenarios along the examples I mentioned for both HTTP and gRPC communication over TLS. A number of these applications are Spring Boot, the way they communicate with each other. I tested both with a managed Postgres service in AWS and an MSK broker in AWS over TLS. In general, the trace context propagation works across these components, except with TLS.

- Right? One of my examples is really in Quercus. So if you want to try it out, you could also compile it in different ways. I think that the thing we still have to work on is the TLS-based context propagation.

- Yeah, that doesn't work yet.

- The other thing that Nikola was alluding to is that this is a bit detailed, but if you are running the latest version of the Kafka library and the latest version of the Kafka broker, they negotiate a V13.

The protocol between them and the current released Vela supports V12. I think that your PR is out. I'm not sure if it has been merged for V13, but it will be soon in Vela as well. These developments are pretty cool as we're checking the protocols. 

What's really important about all of these is that while they look like separate features, what Nikola mentioned about writing this once and then allowing all kinds of libraries, frameworks, and communication to be instrumented at the same time is pretty powerful. You don't have to pick a special Vela version for each messaging protocol, whether it's Confluent, MSK, Google Pub/Sub, or others.

We did add thread support, but there are reactive libraries that we don't support. We wanted to keep it JVM specific, so for JDK alone, we haven't added any of the reactive libraries. If you use RxJava or any of that stuff, thread correlation may not work. 

Now, should we choose this eBPF versus Java agent? Sometimes they're not directly comparable. While this looks like a comparison, we really think about this as complementary rather than competitive. As we look at our existing customer base, we encounter customers who have some instrumentation but not everything, or have nothing, but want to move somewhere. 

The combination of these choices allows customers to be successful in instrumenting their applications. There are a couple of cases where if you want to fully instrument every single library, especially if you have custom business metrics, then the Java agent is probably a better choice. Conversely, if you cannot modify the code, if you're running third-party applications, or if you want zero-touch, day-zero instrumentation of all your applications, then Obi and Beyla is probably the best choice.

What practically happens in most of our customer cases is that we roll out Beyla everywhere. Then they say, "Well, this particular application, I think I can instrument this better," either because it's too chatty or there are specific business metrics or communications they want to instrument. 

What's really cool about Obi and Beyla is that it recognizes if an application has native instrumentation and does not instrument it again. So what we end up with, almost organically, is the combination of all the things that you really care about instrumented as accurately as you wish with the Java agent, while everything else is broadly and instantly instrumented using Obi and Beyla.

Of course, many of our customers don't only run in Java or a single language. They might say, "Okay, fine, I know how to instrument Java, but I have this Python code, and now I have this Node.js code." With Beyla, you get full, semantically consistent instrumentation of all your applications.

### Key Takeaways
I think it's an amazing possibility to use Beyla in your environment, especially where you cannot deploy your own Java agent. Try it; it's really cool that it focuses on application instrumentation. People care about network-level statistics, but understanding the behavior of the system and the interaction between services, even down to the API, Kafka topic, and SQL database table query level, is crucial. You get this out of the box with Obi, including with TLS.

Make the right choices between where you want to use the Java SDK. Please join us! Any feedback, contributions, or issues are very much welcome. 

Here are some links and resources if you want to get a link to the project and participate. That's it. Thank you! (audience applauds)

## Raw YouTube Transcript

- Hey everyone, how are things going? Good, I see people leaving already, so. - [Endre] All that Java. - All that Java, nobody cares about Java. My name is Nikola Grcevski I'm a software engineer at
Grafana Labs, and here I'm with- - Endre Sara, I'm a co-founder at Causely. We are providing a
causal reasoning platform on top of semantic data. If you're interested, feel
free to find me afterwards, but here we are talking about- - Yeah, talk about Java, yeah. And OpenTelemetry BPF Instrumentation. Okay, let's go. - So, why are we here? I think Java is still the most
popular programming language, especially in large enterprises,
financial institutions, with many popular
frameworks like Hibernate, various asynchronous messaging libraries, Spring Boot, Quarkus, and also the OpenTelemetry Java SDK is probably the most comprehensive and the most mature
instrumentation library, but it is not easy to get it
into production all the time. There are several challenges
that we want to talk through in terms of why are we talking about Java, what are the specific
challenges around Java, especially diving deep
into TLS encrypted traffic and an overview of Obi, and then moving on to a couple of examples that we share on how to
actually try this out if you want to try this out around this. - Yeah, so tell us about
some of the problems that you encountered trying to
instrument Java applications. - So, one of the most obvious thing is how do you get the native auto instrumentation into production. For example, we have one
of our large customers, as we engaged with them, within weeks they had Java instrumentation in their staging environment, and then it took several
months, more than six months, to get the first production
application instrumented, not because of any technical reason, just simply operational reasons
of how to change the code. And then a number of other customers, there are a bunch of
third-party applications that you simply cannot touch because you don't have the
ability to rebuild them or to change the way they start. Similarly with legacy system,
older versions of JVMs, and then we're also working with a number of financial customers where injecting code into the
runtime of the application is difficult, just being
able to measure the risk, the impact of those things. So for a number of these things, while I think it is an amazing capability to be able to use native
auto instrumentation, sometimes people just simply
don't have the luxury to do so. - Yeah, and on top of that, there's a whole ecosystem of
people running GraalVM native, where they wanna shave, I don't know, a couple of hundred
milliseconds of a JVM startup so they build their applications
into native from Java and the agent can now be loaded. Okay, so let's talk about eBPF and Java. This has been a sore point
for a project that I worked on since the beginning, Grafana Bela, and Java, we were never able to do well. And there's a couple of reasons for this, but primarily has to do with
how to instrument user space. And in eBPF, which is a technology that allows us to build probes into existing running Linux kernel and existing running applications, you can set user space probes. But for that to happen,
you need to have a file. Everything is a file in Linux. And unfortunately for
us, Java generated code sits in anonymous memory regions. They're not files. So you can say, well, okay,
maybe you can do some hacks such as ptrace into Java, stop it, remap its memory regions
into memory map files. That's doable. We've actually attempted
and it works to some extent, but Java is a dynamically
compiled language, which means run to run, Java
does not have the same code. And the reason for that
is because it starts by interpreting the bytecode. And at this stage, it
collects profiling information about what's important to optimize that drives the compiler
that optimizes the code in multiple stages. So your code is actually
never same from run to run on any Java application. So building instrumentation
at assembly level, essentially a binary level, will make us kind of
cast a really wide net of where we have to put these probes. And I don't want into a business of, oh, I ran this application
once and it worked. Next time I ran it, there
was no instrumentation. So it was an approach we never saw viable. So we wanted to solve
primarily a TLS problem that Endre mentioned. And initially when this problem
was brought up around Java, I said, it's not that important. There's not many Java
servers that run TLS. And I was wrong. Not Java servers, but anytime
you touch any cloud service, let's say you are getting
a cloud managed service from your favorite cloud vendor,
that's gonna go over TLS. So even though that many
people terminate TLS at low balancers, there's
still quite a bit of people that will maybe even use
Java TLS on the server, but as well, most client
calls to external services are done through TLS. So it's a very big problem. So for a long time, we
needed to solve this to be able to do this with eBPF. An environment where you can
kind of just plug stuff in, don't have to modify any configuration or any environment variables
or anything like that. It should just work out
of the box, no restarts. So this is a summary of
what we ended up doing. And let's walk you through the steps of how we achieved this. This can get pretty
technical, so bear with me. All right, so OpenTelemetry eBPF
instrumentation at a glance. This used to be known as Grafana Bela, that product still exists. We just donated to OTEL about a year ago, and we just built Bela on top of this. And it uses eBPF, it
installs kernel probes, network programs, user
probes to try to capture as much telemetry at the kernel level, and then converts this telemetry
into traces and metrics after enriching it from various signals, such as Kubernetes, now
we have cloud metadata, we're enriching with host-level
information and so on. This data then you can transform further by using the OpenTelemetry
Collector or Allo, if you wish. And so this next picture
is sort of a diagram of how this works in practice. But essentially, this software you install as something on your Linux
kernel, like a system process, which translates to
something like a daemon set in Kubernetes. And once it plugs into the all levels of your favorite applications, it can monitor multiple at a time. And then this telemetry,
once it's enriched, you can either send it to an OTLPN point somewhere in the cloud,
or enrich it yourself, keep it local further into
your own on-prem databases and so on. So how does this instrumentation happen? This is what we were
able to do a year ago. When I presented something
similar presentation to this, like GrafanaCon last year,
we had this scenario. And in this case, I'm
talking about a Java server that's handling HTTP, REST APIs, and at the backend is talking to Postgres. So if you will, with the
instrumentations we do typically, we get the protocol show
up in the kernel buffers. We read those and we can say, "Oh, that's HTTP on the incoming side. We extract the route,
we extract the method, the payload, the headers,
all this information, and then we have HTTP." On the backend, we see, "Oh, that protocol looks like Postgres." We parse, we extract the SQL statement. From the SQL statement,
we find the operation, we find a database name and so on. This is all good. And for the last bit over here, I'm assuming a very simplistic scenario where it's the same thread that
handles the incoming request and the outgoing Postgres request. In that scenario, we're able to correlate between the two, incoming and outgoing. Now, unfortunately for us,
this is not a situation that most Java applications
actually run in. It looks like this in most cases. So the first and foremost,
I'll talk about the threads. It's rarely that an incoming request is handled by the same thread
as the outgoing request. Java applications typically
have thread pools. So we have an incoming thread pool that handles all the HTTP requests, and we have an outgoing thread pool that handles the JDBC connections. Now, what about the
traffic that a kernel sees? We no longer are able to
see the actual payloads because it's just gibberish. It's TLS encrypted. So while previously for other languages, we can tap into LibSSL
or BoringSSL and so on, Java implements TLS in Java. So there is exceptions to this rule where people actually
use purposefully OpenSSL or BoringSSL through JNI, but the norm is you use the
Java TLS encryption libraries built into the Java JDK itself. And therefore, we can't see anything, no instrumentation for these applications. So what we've done in Obi is we sort of looked at for a while at the ability to instrument with Uprobes, and we gave up because of
the complexities I explained. So we decided to build a tiny Java agent that can be dynamically injected. So it could be a running process that will accept this agent, and we will load it with a
very small number of probes that would be able to
just fill in the gaps we're not able to see at the kernel level. So what does this mean? This Java agent only instruments TLS and the thread pools in Java. It's bare bones, doesn't instrument any application libraries. We wanted to keep the same concept as the rest of OpenTelemetry
instrumentation. Try to keep it as generic as possible so that we can instrument the world without having to instrument
every individual library. So it doesn't matter if it's
built on top of Spring Boot or it's using Netty Reactor or
it's using Apache something. It doesn't really matter.
At the end of the day, it's still HTTPS. If we can tap into the
protocol, add the TLS time, we could actually capture
and get all of that data. And we've added one other piece
of technology on top of this where we actually harvest the routes embedded into the symbols of
the generated Java classes. So for example, you may
have in Spring Boot a path that says /users/curlybracesid. When you see that route coming on the buffers from the kernel is users/123. So we do that matching. We understand that this 123
matches to the Spring Boot path just like Spring Boot would do. So how does this actually
work in practice? And I know it's maybe a
lot to kind of consume, but the two pieces of information to make OB work really well with any sort of programming language is we need two pieces of information. We need connection information. So we need to know who's talking to who so we can find the IP addresses and ports and then from there try to
kind of enrich this information from Kubernetes and we need the buffers so we can actually analyze the protocol, figure out its HTTP and
Postgres on these sides. So let's take this one
example we needed to do. So Java internally, once we
actually added the probes, has two modes to handle TLS. One is synchronous where
it's the secure socket. It's the class internally
that everybody uses and there's plenty of Java
libraries that use that approach. It's the same class that
handles both the communication with the peer and it's the same class that does the SSL encryption. Great. We could extract both the
connection information and the unencrypted buffers
from the same instrumentation. However, other implementations
of SSL encryption in Java use two separate kind of paths. For example, Netty. They have their own high
performance socket implementation but they use the SSL engine
from Java to do the encryption. And so the actual work
here is asynchronous. One part does the encryption, the other part does the
actual communication to the other side. So how do we correlate these buffers? It was actually an
innovation by my manager, Fabian Staberg, who actually
brought us the idea. He said, "Well, you can track
all the threads you want "but you'll actually end up
in a situation where you miss "and then you cannot correlate. "However, if encryption is done right, "the actual encrypted buffer
should be unique enough "for you to create a key. "If it's a buffer is
the same all the time, "then what you end up
is actually encryption "that can be broken into." So what we do is we take
sufficient number of bytes of the encrypted text at
the time of encryption and use that as a key
in a map, in memory map to the actual buffer that
actually we wanna read. That happens in encryption time. When this actually encrypted text is sent over the wire to the other side, this is when we extract the
key again, look up the map, and at that point we have both
the connection information and the buffer that we wanna read. So we looked into how do we, now that we have this information, how do we pass this
information to the eBPF side? It's all great, we found it in Java. So this agent now does
a very fast system call, sysioctl, where it
communicates a Java buffer that has been created for us to read. So this sysioctl call
happens in the kernel and this is the chance
for us to set a K-probe with OB that will intercept that call, read the information and pass it to the rest of the OB machinery to actually produce the
telemetry that we need. So we just filled in the missing pieces that we needed to get Java to work. So Endre here has been playing with this for the time that we've
been developing it. So why don't you tell us a little bit about the things you've done with this? - Sure, so we are working
with a number of customers. For example, there is this one customer that's running an edge
security application and they've got various Java clients, Spring Boot clients that
are talking to Keycloak. Now, Keycloak is natively instrumented, but obviously it's more important how the clients are
interacting with Keycloak, which is over HTTPS. We have other customers in
the digital marketing space that extensively uses Google
Pub/Sub, also over SSL, and then a large betting company that has a number of Java applications. Most of our applications are in Java and they're using managed Postgres, actually other managed databases
over TLS as well as Kafka. Now, I can't bring
their applications here, so I thought I'll write something that represents their information and all of them are public or open source. Each of these can be deployed
by a simple ham chart in your own communities cluster. If you want to try any of this combination on how do they work with
Bela, I actually have a branch that does native OTA
instrumentation on each one of them, and then a branch that removes
all the OTA instrumentation so that you could see
how they work with Bela or without Bela with the
native instrumentation. Have a lot of fun. Please tell me if there is anything that I could do differently about them, but try it if you want to. - And we've had a number of
bug reports from him coming. He always tries some new framework and some new protocol and whatever, and it breaks and says, "Hey, I tried this "and it didn't work." And then we make it better. So a lot of trial and error, but we have a bunch of trade-offs still. Why don't you tell us
what works, what doesn't? - So a number of things
that works very well. I tried a number of
scenarios along the examples that I mentioned for both
HTTP and gRPC communication over TLS. A number of these
applications are Spring Boot, the way that they
communicate with each other. I tested both with a managed
Postgres service in AWS, an MSK broker in AWS over TLS. And in general, the
trace context propagation works across these
components, except with TLS. - Yeah. - Right? One of my examples is really in Quercus. So if you want to try it out, you could also compile
it in different ways. So I think that the thing
that we have to still work on, one of them is the TLS-based
context propagation. - Yeah, that doesn't work yet. - And then the other thing
that Nikola was alluding to is that this is a bit detailed, but if you are running
the latest, latest version of the Kafka library, and you're running the
latest, latest version of the Kafka broker, they negotiate a V13 protocol between them and the current released
Vela supports and V12. I think that your PR is out. I'm not sure if it has
been merged for V13. It will be soon in Vela as well. So these things are pretty cool that they are coming up as we're checking basically the protocols. But I think that what's really
important about all of these is that while they look
like separate features, what Nikola mentioned
about writing this once and then allowing all kinds of libraries, all kinds of frameworks,
all kinds of communication to be all instrumented at the
same time is pretty powerful. That you don't have to
pick a special Vela version for each Confluent versus
MSK versus Google Pub/Sub versus other messaging protocols. - Yeah, and I was gonna say,
like we did add thread support, but there's reactive libraries
that we don't support. Like I said, we wanted
to keep it JVM specific. So JDK alone, we haven't
added any of the reactive. So if you use RxJava or any of that stuff, thread correlation may not work. So why don't we see where, should we choose this
EBP versus Java agent? And sometimes they're not. - So first of all, I think while this looks like a comparison I think that really we
are thinking about this as complimentary to us
and not competitors. As we look at our existing customer base, we walk into customers where
they have some instrumentation but not everything, have nothing, but they want to move somewhere. So really what I see
is that the combination of these choices is what allows customers to really be successful in
instrumenting their applications. Now, there are a couple of cases where if you want to fully
instrument every single library and especially if you have
custom business metric, then the Java agent is
probably a better choice. But on the conversely, on the other side, if you cannot modify the code, if you're running third-party applications and probably even more interestingly, if you just want a zero-touch, day-zero instrumentation of
all of your applications, then Obi and Bela is
probably the best choice. What practically actually happens in most of our customer cases is that we roll out Bela everywhere. And then they say like, well,
this particular application, I think I can instrument this better either because it's either too chatty or there are these
specific business metrics or specific communications
that I want to instrument. And what's really cool about Obi and Bela is that it recognizes if an application has native instrumentation
and it doesn't instrument it. So what we end up almost
organically and naturally is the combination of all the things that you really care about instrumented as accurately as you
wish with the Java agent and everything else just broadly and instantly instrumented
using Obi and Bela. And of course, there are the cases where most of our customers
don't only run in Java, don't only run in a single language. So like, okay, fine, I know
how to instrument Java, but I have this Python code,
now I have this Node.js code. And with Bela, you basically
get the full consistent, semantically consistent instrumentation of all of your applications. - [Nikola] So key takeaways? - Yeah, so I think it's
an amazing possibility of using Bela in your environment, especially where you cannot
deploy your own Java agent. So try it, I think it's really cool that it's really focusing on
application instrumentation. I mean, people care about
network level statistics, but what I think is really important is to be able to understand
the behavior of the system, the interaction between the services, even down to the API, Kafka topic, SQL database table query level. And you basically get this
out of the box with Obi, including with TLS. And then make the right choices between where you want
to use the Java SDK. And please join us. Any feedback, contribution, issues? - Yeah, issues, deal pull requests, very much welcome to anyone. Yeah, that's it. These are some links and resources we have if you wanted to get a link to
the project and participate. But yeah, that's it. I think we're good. Thank you. (audience applauds)

