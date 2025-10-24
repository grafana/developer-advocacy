# Using eBPF and OpenTelemetry to Build a Resilient Observability Architecture | Finastra

Published on 2025-10-22T16:42:38Z

## Description

See how Finastra's deployment of Grafana Alloy, Grafana Beyla, and the OpenTelemetry Operator, powered by eBPF and ...

URL: https://www.youtube.com/watch?v=pjzfwbVtcvw

## Summary

In this video, Vladmir Babichev and Maciej, both from Finastra, discuss how eBPF technology was utilized to enhance observability within Finastra's Fusion Fabric Cloud (FFDC) platform. Their presentation highlights the challenges faced with tracking issues in a large distributed environment, particularly connection timeouts and build failures, which affected multiple teams. They explain how they initially struggled with observability due to low adoption of existing metrics, logs, and traces. By integrating Grafana's eBPF profiler and later OpenTelemetry for auto instrumentation, they significantly improved their ability to monitor and troubleshoot applications. They share specific instances where enhanced observability allowed them to resolve timeout issues and improve performance, ultimately enabling their teams to work more efficiently and collaboratively. The session emphasizes the importance of observability in modern software development and the lessons learned from their experiences in implementing these tools.

## Chapters

00:00:00 Introductions by Vladimir and Maciej  
00:03:00 Overview of Finastra and its services  
00:06:30 Introduction to Fusion Fabric Cloud (FFDC) platform  
00:10:00 Discussion of the challenges faced with pipeline failures  
00:14:30 Analysis of connection timeouts and 400/500 errors  
00:20:00 Introduction of Grafana Beyla and its impact on observability  
00:24:30 Transition to OpenTelemetry and auto instrumentation  
00:30:00 Specific examples of issues resolved using observability tools  
00:38:00 Observability stack changes and improvements  
00:45:00 Lessons learned and future outlook for observability at Finastra  

# eBPF for OpenTelemetry: Solving Problems at Finastra

Hi everyone. Today, we're going to talk about eBPF for OpenTelemetry and how it has solved some of the problems within Finastra. The title of this talk is much shorter than what you see on the agenda, as it simply doesn't fit the slide. 

My name is **Vladimir Babichev**. I am a platform architect at Finastra, focusing on building resilient and reliable solutions that underpin the financial services provided by our company. I am a travel addict, a Kubernetes expert, and a home enthusiast. This means I can switch on and off all lights in my home by editing YAML files while sitting comfortably in my chair. I have also mastered high availability with four nines SLAs and zero downtime deployments, as I can't really explain to my kids why they have to go to sleep at 6:00 PM during the winter.

Now, let me introduce my colleague.

Hi everyone, my name is **Maciej**. I am an expert software engineer at Finastra and a member of the FFDC Poland team. Most of my time is spent traveling around the world. For example, you can see a picture of me in Bryce Canyon, USA, rendered in Pixar style, which proves that AI can help save some really bad selfies. Also, keep in mind that this is my first time on stage, so I am quite nervous. Sorry if this presentation looks more like improvisation than a formal talk. I will try my best, so please stay with us; the topic is really worth it.

## About Finastra

Before we move on, allow me to introduce the company we both work for: **Finastra**. Finastra is one of the world's leading financial software companies, serving over 8,000 customers, including many of the top global banks. Our solutions cover corporate and retail banking, payments, lending, treasury, and capital markets. With a strong focus on open platforms and collaboration, we empower our clients to connect, scale, and deliver better experiences for their customers. We call this **"innovating finance together."**

**Fusion Fabric Cloud (FFDC)** is Finastra's platform-as-a-service solution. It fosters collaboration across the financial services ecosystem by exposing Finastra's core systems through the Fusion Fabric Platform API. To put it simply, you can think of it as a gateway that gives you access to banking products locked within bank infrastructure, enabling fintechs, independent developers, or even students to create a wide range of innovative financial services that were previously out of reach.

I have prepared some numbers to help you visualize the scale of the FFDC platform. Every day, we process more than **2 million CoBank requests** and handle more than **8 million internal API calls** between our 20+ microservices. With such a large and distributed environment, it is really challenging to track down issues, especially timeouts.

Have you ever faced problems that are difficult to understand? One of the biggest challenges for me has always been networking. If someone tells you, "It's not the network," it usually is. Networking issues are particularly problematic when they are hard to reproduce.

A few months back, Maciej's team at Fusion Fabric Cloud reached out to us, saying they had a problem with their pipelines. At that time, we understood that roughly **20%** of the builds were failing, but we couldn't pinpoint the issue. Some days, none of the builds succeeded; other days, only one build failed while another five succeeded, so we were left puzzled.

Looking back, we later realized that the team was operating on a four-day work week instead of full-time. They conducted their analysis and identified that connection timeouts were a recurring issue. A connection timeout occurs when service A tries to communicate with service B, but fails to do so, resulting in service B never receiving the connection request. They also identified that the problem was related to the retail modes. When service A communicated with service B, service B attempted to reply, but service A never received the response.

As technical people, we understand that different issues lie on different sides of the story. The team also mentioned that the problem surfaced when they saw **400** and **500** errors on their graphs. Everything marked orange was good, and anything that wasn’t orange indicated some type of error. However, not every 400 or 500 error is necessarily bad; some are legitimate, such as application token failures.

The most frustrating aspect was that the issue occurred in one of the environments out of five. The integration environment not only affected this team, but also many other teams trying to integrate with Fusion Fabric Cloud using the APIs. This led to fingers pointing in our direction, implying it was our responsibility to fix it since everything worked fine elsewhere.

It's similar to a patient going to a GP. They typically know their symptoms and expect the doctor to prescribe exactly what they want. However, the doctor may just give them paracetamol because they need time to assess if the patient actually knows what they're talking about. We found ourselves in the same situation.

Initially, we thought we had a solution. As a platform, we had implemented the three pillars of observability: metrics, logs, and traces. However, the team wasn't using them, as they were mature in tracking down problems with their systems. They rarely encountered issues in production, and when they did, their MTTRs (Mean Time to Recovery) were quite low. This was our first learning: if you do your observability tracking, ensure it is adopted by users. Without that, there is no guarantee that the value you provide will be recognized.

We were stuck and scratching our heads. To gain insights into why this application was failing, we realized we would need to rebuild every single application to add tracing annotations and metric exposures to the code. This would take time, but the problem was that one day out of five, the team was gone.

In our search for options, we discovered that **Grafana Labs** offers an excellent open-source solution called **Grafana Beyla**. If you're not aware of it, Beyla is an eBPF profiler that auto-instruments tools. Long story short, it provides basic tracing, which helps you understand which applications communicate with each other—crucial in a microservice distributed environment. Additionally, it provides basic red metrics: requests, errors, and duration.

This was fantastic! Beyla acted as our paracetamol; it was the silver bullet we thought would fix all our problems. We obtained a service map, which gave us a clear understanding of application interactions, behaviors, and failures. We had a real-time service map and could go back in time to determine who communicated with whom, rather than relying solely on knowledge passed between engineers or outdated documentation.

We also received standard metrics, allowing teams to talk the same language, regardless of the programming language their applications were written in—be it Node.js, Java, or Go. Suddenly, teams were observing their applications at the same level.

However, we expected Beyla to provide tracing capabilities to help us understand the flow of requests through the system. Unfortunately, we encountered issues with context propagation, which didn’t work well. While Beyla provided some insights, we kept searching for better solutions.

Next on our list was **OpenTelemetry**. It's a widely discussed topic these days, consisting of a collection of APIs and tools that help instrument applications to obtain metrics, logs, and traces. Initially, we were hesitant to explore OpenTelemetry due to its mention of APIs. We thought it was similar to Prometheus and Tempo, requiring us to rebuild our applications and check annotations, and we pushed it aside.

However, after reading the documentation, we were pleasantly surprised to find that it took us only two pages to discover it supports **auto-instrumentation**. This meant that in order to get all the microservices facing issues, we just needed to create one manifest inside Kubernetes, restart our applications, and we would start receiving the same red metrics in a more appealing format.

With OpenTelemetry, we gained more drill-down capabilities into the system, allowing us to understand the behavior of specific parts. We finally achieved context propagation, enabling us to trace incoming requests, see how microservices A and B interacted, and understand database calls. The cherry on top was that we could visualize the request flow down to the exact functions in the code responsible for processing requests. That’s where we gained real traction.

### Observability in Action

Now, I will show you a couple of examples of how observability helped us solve issues. As a development team, we tried tracking down which services were experiencing timeouts, but in our distributed environment, it was not easy. However, with the observability tools deployed by Vladimir and his team, with zero code changes from our side, we were able to narrow down one of the issues to a lack of proper timeout configuration.

With **Grafana Tempo** enabled, we could see a beautiful request span graph. Unfortunately, I had to blur some internal implementations, but you get the point. We observed that the initial request times out after five seconds, which is acceptable since that's the configuration for our API gateway. However, requests to underlying services continued for several seconds, and some even for minutes. Such long-running requests had zero chance of success because by the time the response arrived, the connection was already closed. This wasted resources and led to an exhausted thread pool, freezing the environment.

As a result, we pinpointed the exact location in the code where we needed to make fixes. All I had to do was add a timeout to our Spring Boot implementation. By doing so, the long-running requests were terminated, eliminating dangling connections. This simple two-liner significantly increased the stability of our environment.

However, after some time, we faced another issue, but again, observability enabled us to identify and fix it. This issue was related to **cache stampede**, which occurs when multiple processes simultaneously attempt to regenerate a missing cache entry. Each thread performs an expensive operation independently, overwhelming the underlying resource with redundant requests, such as database operations or large queries.

In our example, we had two endpoints: **JWKS** (used to fetch the JSON Web Key Set) and **token** (used to obtain tokens). Both endpoints were used by our customers and our microservices. When the first request came, it was served from the cache, and we got a response. However, when another request came in (with an invalidated cache value), it attempted to regenerate it by calling the cache and then the database. If another request also tried to regenerate the missing value, while simultaneously utilizing a connection from the pool, the pool would become fully depleted.

Even though those database requests would eventually finish, we ended up with a pile of blocked requests. The result? The environment froze again. Thanks to observability, we obtained proper thread metrics, revealing that the HTTP worker pool was exhausted due to an overwhelming number of requests, with all threads in a blocked state.

We could have increased the number of threads, but that would have cost us more resources and concealed the actual root cause. We continued digging and examined other metrics, specifically database connection metrics. We noticed that the number of connections spiked abruptly and remained high for around 30 minutes before returning to normal due to Kubernetes health checks restarting services until they returned to an operational state.

Interestingly, this situation happened almost every 24 hours, leading us to believe there was some time-based event occurring, like a job in the cluster. After conducting code analysis, we discovered that we were using a cache that regenerates the value every 24 hours. The fix was simple: adding `sync = true` within the cacheable annotation would allow proper synchronization. Consequently, when cache entries expired, requests were kept at the token service level while waiting for the value to be regenerated, allowing other token requests to continue without being blocked.

### Key Learnings and Changes

So, what has changed after resolving these problems? We learned that observability should be useful. Here is an overview of our previous stack before the problems arose. It was quite standard: dedicated metrics instances running in chain mode, trace instances, and logs.

From our platform perspective, we run multi-tenant Kubernetes clusters, with different product teams deploying their products on the same cluster and sending data to their dedicated Grafana Cloud stacks. We needed flexibility instead of combining everything, which worked fine until situations arose where we had dedicated nodes running for Prometheus or Grafana Agent, capturing all data and becoming costly.

With this analysis, we decided to delay our migration to **Alloy**. Initially, we were using **Grafana Agent**. What we learned about Alloy is that it can do everything for you; it’s like an Uber application that handles open telemetry metrics, logs, and traces all in one box. 

Instead of having dedicated Alloy configurations for metrics and other components, one agent now does everything, serving all pods within the same node and capturing all information. This has helped us isolate failure domains, making our environment more stable while reducing our memory footprint. We no longer faced the issue of our Prometheus consumer using 30 GB of memory.

However, we encountered a challenge with Alloy's configuration. It required around 800 lines of code just for one product, and we had several products deployed in the cluster. Maintenance became a concern, particularly regarding day-two operations and introducing changes. 

We deploy our systems through **Helm charts**, and we decided to distribute the Alloy configuration into multiple chunks. The main Alloy helm chart deploys core components, while product-specific configurations are deployed in their respective namespaces. This grants us more granular control over who does what.

To manage everything effectively, we used a **mutate method controller** (like Kyverno) to read the configuration from different products' environments, merge it into one configuration file, and allow Alloy to watch for changes in the config map, digest it, reload, and implement the necessary adjustments.

### Conclusion

So, why was it a problem in just one environment and not in production? The answer is simple: we were over-provisioned. Our instances were four to five times larger than needed, which prevented us from facing the same issues. The requests were processed faster, effectively averting denial-of-service situations in production environments and unblocking our pipelines.

Teams returned to a normal five-day work week. We learned that we can implement zero-code observability, which is extremely powerful. Instead of working with every single developer team to educate them on observability standards, we took ownership of the entire stack. Teams can add anything else to their default setup if they wish, but if they don't, they receive a standard set of metrics.

Now, there is a common language spoken by different teams across various geographies and continents. They have red metrics and traces in place at no additional cost. We gained clear service and request maps, eliminating the confusion of spaghetti code. Empowering our teams has transformed us from problem owners to solution providers, which has been incredibly powerful.

Ultimately, we improved the resilience and scalability of our solution while reducing the cost of ownership for our Alloy deployments. We are constantly learning and improving how we track the adoption of our services by different teams.

Thank you very much for your attention!

## Raw YouTube Transcript

Hi everyone. Today we're going to talk about the eBPF
for OpenTelemetry and how it actually solved some of the problems
within the Finastra. The title of this talk is much shorter
than what you see on the agenda. That is because it just doesn't
fit the slide to start with. My name is Vladimir Babichev. I'm a platform architect at Finastra
doing all the platform stuff, but generally speaking,
building the resilient, reliable solution that underpin financial
services provided by our company. I am a travel addict, Kubernetes expert, and home enthusiast. So practically that means is that I can
switch on and off all lights in my home by editing YAML files by
sitting somewhere in the chair. I also mastered the high
availability like four nines SLAs and zero downtime deployments
because I can't really explain my kids why they have to go to sleep at
6:00 PM during the winter time. Hi everyone. My name is Maciej. I'm an
expert software engineer at Finastra. I'm a member of FFDC Poland team. Most of the time I spent traveling
around the world here. For example, you can see picture of
myself in Bryce Canyon, USA rendered in Pixar style, which is proof that AI doesn't
just help us developers code, but it can also help save
some really bad selfies. Also, keep in mind that this is my first
time on stage and I'm quite nervous. Sorry if this looks more
like improvisation than
presentation. I'll try my best, but stay with us. I think
the topic is really worth it. So before we move on, allow me to
introduce the company we both work for, which is Finastra. So Finastra is one of the world's
leading financial software companies serving over 8,000 customers including many of the top global banks. So our solution cover corporate
and retail banking, payments, lending, treasury and capital markets.
So with strong focus on open platform and collaboration, we empower our clients to
connect scale and deliver better experience for their customers and we
call that innovating finance together. Fusion Fabric Cloud or
FFDC in short is Finastra platform as a service solution. So it fosters collaboration across
the financial services ecosystem by exposing Finastra core systems
through Fusion fabric platform. API to put a simple, you can think of it as a gateway
that gives you access to banking products locked within
bank infrastructure, which enables fintechs, independent developers or even
students to create wide range of innovative financial services
that were previously out of reach. I have prepared some numbers to help
you visualize the scale of this FFDC platform. So every day we are
processing more than 2 million CoBank requests. At the same time we're handling
more than 8 million internal API calls between our
20 plus microservices. So with such large and distributed
environment it's really challenging to track down issues,
especially when it comes to timeouts. So have you ever faced the problems that
are really difficult to understand and just understand what people want from you? So one of the biggest problems
for me is always network. If somebody tells you it's not network, it's so usually a network and
it's always a problem when the problem you can't really reproduce and
networking is just one of those things. So a few months back, the Maciej's team Fusion Fabric Cloud
reached out to us saying that they have a problem with their pipelines. Now we understand that roughly 20%
of the bills at the time were failing and yeah, we couldn't understand
where it's coming from. Sometimes there were really bad days
where none of the builds were succeeding sometimes where just one build failed, another five succeeded and it was
absolutely fine so we couldn't understand. Now looking back we can understand that
it was like actually the team was doing four day working week instead
of a full-time. So it was good whenever they were explaining problems,
they done their obvious analysis. One of the things that was popping
up is the connection time out. So connection time out is when the
service A tries to talk to service B. However, they failed to do so. So
service B never received the connection. They also identified the problem
was related to the retail modes. When service A talks to service B,
service B tries to reply back. However, service A never receives the
response. Again, if you are technical, you understand also different things
lie on different side of the stories. To add more to the mix effectively team mentioned
that the problem is surface
when you see like 400 500 errors just on this graph,
everything is orange is good, everything not orange is
actually some type of error. It's kind of okay, you
can see some patterns, you understand where you potentially
can look at it, but there is a catch. Not every 400 to 500 error is good,
bad and some of them are actually good. So some legitimate, right? They use
a application token failed and so on. So how do you understand? So that
was a thing and the best thing, it was just working in failing in
one of the environments out of five. The worst thing it was the integration
environment where not just this team had problem and their built were failing but
rather many other teams experienced the same problem. So who tried to integrate
with the fusion for big cloud, use the APIs and so on and
in way it leads to it kind of fingers pointing in your direction
saying well you better fix it because it works everywhere else. The stories where you have a
patient coming to gp, right? They're very well known about what
their problem is, how to address it. So they explain their symptoms and
effectively expecting doctor to write that prescriptions exactly what they want
but instead doctor gives them just paracetamol and that is just simply
because doctor needs time just to digest is this guy actually
knowing what he's talking about? Is this the real stuff or not?
And we needed the same stuff. One, we thought we
actually have this pill. We as the platform, we implemented
three pillars of the observability. So metric locks and traces
as the service long time ago, the caveat though team didn't use it, that is because they were so mature, they were very good in terms of their
tracking down problems with their systems and they usually don't have any problems
in their production environments and even they do, their MTTRs are quite low. So they never really looked in what that
platform team provides and that was our first learning. If you do your
observability track adoption, because without that there is no guarantee
of people actually you provide any value to them. So we were actually
stuck, we were scratching our heads. Now in order to get any insights
about why this application is failing, we had to go ahead and rebuild
every single application, make sure we add the tracing annotations, we add the metric exposures to the code.
That would take us time. But the problem is here is now the one
day out of five, the people are gone. So we look for the options and
we realized, well first of all, Grafana Labs provide a fantastic open
source solution which is the Grafana Beyla. If you're not aware of what it is, it is EPPF profiler that auto to
instruments tool. Long story short, why it is beneficial to you because
it gives the basic tracing so you can understand which application
talks to which very important in the microservice distributed world and
on top of that it provides the red metrics. So requests, errors and duration, kind of the basics about how you
should observe your environments and that was fantastic. That was actually our paracetamol
because that was a silver bullet that we thought they will fix all our
problems. We got the service map, we have a clear
understanding what is what, who's talking to how
the applications behave, which of them are failing.
We had the real time service map. We could go back in time and understand
at that specific moment who talked to who, not just relying on the knowledge that
was passed between different engineers or documented and sometimes the
recommendation can be outdated and we got the standard metrics. So this is the example of the dashboard
that you can download from the importing your Grafana Cloud instance from the
Grafana Cloud marketplace and what is important, you have the same set of
metrics irrespective of the
language your application is written on. So that's no js, that
would be Java, that would be goal length, whatever that is. Suddenly your
teams talk the same language. They observe the applications same level. What we also expected from this,
we expected to get tracing, understand how we can trace
the actual requests that the passing through the system, but unfortunately it didn't work for us.
We faced the problem where the Beyla faced the issue with the context
propagation and didn't work well. It gave us some input. So with
the team started investigating, we started understanding what
happened there but we kept looking. So the next thing on our
list was the OpenTelemetry. So it's a common thing now everybody
talking about OpenTelemetry these days, but it's a collection of APIs
and this is the case and tools. They help you to instrument
your applications and get
metrics box and traces. So same thing over and over again. The reason why we didn't
look in OpenTelemetry in
the first place is that word APIs and is the case. When we thought
about it, we actually considered, well probably it's the same stuff as
Prometheus and Tempo with the tracing we have to rebuild our applications and
check those annotations and have things happening and we just push it back.
But time came, we read the documentation, they have
massive documentation if you go in there, it just really, really difficult. But we were surprised that it took
us maybe two pages to read and they support auto instrumentation. So in order
to get all the microservices that were facing the problem, we just need to create one
manifest inside of the Kubernetes, restart our applications and we suddenly
were getting same red metrics like in much nicer view. So this is Application Observability
service provided by Grafana labs. We got more drill downs into the system
so we can understand which specific parts, how they're behaving,
et cetera. And we got tracing. We finally got that context propagation
understanding here is the traffic coming in request coming into the system. This is the res control of this
microservice A, microservice B, how it talks to the database and
so on and the cherry on the cake. We were able to see not just the service
map between different components, but we could see the request
flow so pinpoint to the
exact functions in the code that was responsible for processing that
request and that's where we got real traction. Okay, so now I'll show
you a couple of examples. Two actually that observability
helped us to solve. So as a dev team we've been trying
to track down which services are getting those timeouts, but in this distributed
environment it was not that easy. But with all the observability
deployed by Vladimir and his team with zero code from our side, we're able to narrow down one
of them and it happened to be lack of proper time of configuration.
So with Grafana tempo enable, we're able to see this
beautiful request span graph. It's not that beautiful here because
I had to blur down some internal implementation, but you get the point. What we can see here is that the
initial request times out after five seconds, which is okay because that's
the configuration we use for the client, which is API
gateway. In that case, however, request to underlying services, those ones mark with green kept going, some of them for a couple of seconds
and some of them even for a couple of minutes.
So such requests have zero chance of success because
by the time the response arrives, the connection is already closed. So it's like wasted resources and those long-running requests led us to exhausting pool of threats which
were able to handle incoming requests. So what was the result of it? The environment was completely frozen and Grafana tempo includes
class name and method name in the Java code. So we're able to pinpoint
exact point in code where we need to place the fix.
As for the fix itself, all I had to do was to add time out
to our spring boot implementation. And with this setting, the requests long running requests
were terminated and there were no more dangling connections. So just simple two
liner helped us increase the stability of the environment. However, after some time we kept
getting another issue, but again, observability helped us
to identify and fix it. I'm talking about custom
speed. So what is this? It's basically a performance issue
that occurs when multiple processes simultaneously attempt to
regenerate missing cache entry. As a result, each threat performs expensive
operation independently overwhelming the underlying resource
with redundant requests. So underlying resource be database and some operation can be large
query. To read the data in the examples I have prepared for you, we'll consider two kinds of
endpoint JWKS and token end points. So basically the token
is as it says, it fetch, it's used to get the token and JWKS is used to fetch the Json web key set, which is basically set of public set keys required to sign the token. I mark them with different arrows
so you can distinguish them. What is important to mention is
that those endpoints are used both our customers and our microservices. So when the first request comes, it's immediately served from the cash, we get the response, we get another. Then in the meantime
we can get some authentication. Request response is quickly served. Same for the other one,
everything is working fine. What is important here is none of the JWKS requests touches the database.
Everything is served from the cache. So now the scenario with
invalidated cache value to simplify, let's assume that connection pool
of our database is free so we can handle only free
connections at a time. Okay, so the request comes, the cache is expired, so request tries to regenerate it, calling the kick log first
and then the database. When another request comes,
it does exactly the same. It also tries to regenerate
the missing value. In the meantime, we have some token request which also
takes one of the connection from the pool, which is now fully depleted. So even though those request, those database requests
will eventually finish, we end up with pile of stacked request and you know what the result is?
Yeah, environment is frozen again. So the applying observability
allows us to get some proper threat metrics. Here we can see pool of HDTP workers, which has been exhausted due to
overwhelming number of requests. So all of those threats
are in blocked state, which means they're basically
queued up waiting for some executor. We could just increase
the number of threats, but that would cost us more
resources basically and would also conceal the actual root
cause instead of fixing it. So we decide to keep digging. We looked into other kind of metrics,
which is database connection metrics. You can see on this slide that
the number of connection spikes up abruptly. Then it's on the top for around 30 minutes and then it goes back to normal.
And why it goes back to normal, it's because our friend Kubernetes, which comes with the health
check and keeps restarting the services until it gets
back to operating state. What is funny, sorry, we noticed that this situation
is happening almost every 24 hours. We've had an impression that there
must be some time-based event which is running like some pipeline,
some job in the cluster, whatever. But it happened roughly every 24 hour. I did some code analysis and I
found that we are using cash that is regenerating the value every 24 hours. So the fix is simple, it's adding this think set to true within the cacheable
annotation. So simple thing, but to implement it you
need to find the root cause. Okay? And then how it works with proper sync mechanism, the cache entries expired.
So as in previous example, it tries to regenerate it. Other requests are kept
at the token service level waiting for the value to be
regenerated. In the meantime, we can have some token requests
which are not blocked anymore. Everything is working
correctly and all of this. Thanks do observability. Thank you. So what has changed? Well after we resolve the problem
is we learn our lesson as a platform team that observability
should be useful. This is, for example, our current stack, or not current,
the past stack before the problem. It's very standard. You have dedicated metrics instances
that are running in the chain mode. You have the traces
instances, and you have logs. What is important from our platform
perspective that we run multi-tenant Kubernetes clusters. So you have different
product teams deploying their
products on the same cluster and they're sending data to their
dedicated Grafana Cloud stacks. So we need to make sure we have this
flexibility instead of mashing everything together. It kind of works fine. A part of the situations where we have
dedicated notes running for Prometheus or Grafana Agent or Alloy, just capturing all the data and then it
becomes very costly. So what has changed with this analysis, what
we've done, first of all, we delayed our migration to
Alloy. We were using Grafana Agent and what we learned with Alloy that
you can actually deploy and it will do everything for you. So
it's like Uber application, it does your open telemetry metrics,
logs, traces just in one box. It also can do Beyla, it can also
do profiling. Just fantastic. So what we do, instead of having again dedicated
alloys for metrics and so on, one agent does everything
so it serves all the ports within the same node and
capture all the information. This way it help us to
isolate our failure domains, making sure we have more stable
environment and we also reduce our memory footprint. So we no longer have this problem why
our Prometheus consumer 30 gig of memory and like we investigated or probably
one of the teams have added some extra data. It was all good until when
we came into the point trying to platformise it and get it running. So the problem that we faced with
Alloy and run it in Uber mode was the configuration. It was like 800 lines of code just for
one product and we have five of them, for example, deployed on the
cluster. So it's kind of good, right? You put it in place, it's just working
there. The trouble is the maintenance. How do you do your day two operations,
how you introduce a change and et cetera. So we looked a little bit into
thing and the way how we cook our systems is we deploy it through the
helm charts and what is important. We package all the components related
to the system within that environment definition helm chart. So in our case we distributed the alloy configuration into multiple chunks.
So the Alloy itself, the helm chart for Alloy deploys the
main core components of the configuration and then any product
specific configurations, they're deployed in their respective
namespace just over here on the top and somewhere on the bottom. And that way you have this
more granular control. Who does what and how do you do Then
to manage all these things together, we use the mutate method controller, like in this case we use Kirna that will
actually read the configuration from the different products environments,
Alloy configuration itself, merge it into the one Uber configuration
file and then the Alloy will watch for any changes into that
config map, digest it, reload, and will implement things. So what did we learn from
this thing? First of all, I guess the most important question, why was it the problem
just in one environment, why it wasn't like in production, why
it wasn't deaf Dance is very simple. We've been over provisioned. We were like four or five
times big instances that we
needed and that's why the problem was never faced. We never faced and the requests
were processed much faster. But what also we did, we prevented the effectively denial
of service in the actual production environments and we unblocked
our pipeline. So the teams
got back to the five, normal five working day week. We
shouldn't have done it actually, but whatever we learned that we can do the zero quote
observability and that is extremely powerful. So instead of working with every single
developer team and chasing them and educating them how this is the
observability, this is how you do it, this is the standards and so on, we actually shifted it to the left
and we own the entire stack. So if the team wants to add anything
else to their default setup, they're more than welcome to do
it. They just need to learn it. But if they don't, they get the standard set of metrics and
then suddenly you have the same common language spoken by different teams in
different geographies and different continents. They have red, they have traces in place and it
costs them absolutely zero to do, as I mentioned, standard metrics
dashboards, what is important? We got this service and request maps.
There are no more spaghetti balls, it's just very clear understanding
what's coming, where it is, et cetera. We empower our team. There is no more finger pointing
like this is not my thing. Especially with the remote working
and it's very common in our company. You get people to the
same table and instead of being problem owners, we
became the solution providers. That was very powerful for us. We obviously improved the resilience
and scalability of our solution. So we reduced the cost of ownership
for our Alloy deployments and we learned our lesson. We looking, we improving in the way how we
tracking the adoption of the services by different teams. Thank you very much.

