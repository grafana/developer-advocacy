# The Future of OpenTelemetry Deployment: Grafana’s Instrumentation Hub

Published on 2025-10-22T16:37:17Z

## Description

Deploying OpenTelemetry at scale is hard — too many configs, too much YAML, and not enough time. In this ObservabilityCON ...

URL: https://www.youtube.com/watch?v=OUE6ElVFjzk

## Summary

In this video, Ted Young, a developer programs director at Grafana Labs, and Edwin, a product manager, discuss the challenges and solutions surrounding the deployment of Open Telemetry at scale. They emphasize the complexities of integrating observability into large systems, noting that many teams struggle with the time-consuming process of installing and configuring Open Telemetry components. The speakers propose a framework for addressing these challenges, introducing a hierarchy of observability needs from infrastructure visibility to custom application logging. They highlight the development of tools like Alloy for infrastructure monitoring and Beyla for service visibility, and introduce the new Instrumentation Hub, which aims to simplify the deployment process through a point-and-click interface for instrumenting applications. The session concludes with a sneak preview of forthcoming features and encourages viewers to join a waitlist for early access to the Instrumentation Hub.

## Chapters

00:00:00 Introductions and welcome  
00:01:30 Who is excited about Open Telemetry?  
00:02:45 Challenges in deploying Open Telemetry at scale  
00:05:00 The complexity of monitoring large systems  
00:07:15 Framework for Observability needs  
00:10:00 Infrastructure visibility as the foundation  
00:12:30 Introduction of Alloy and its capabilities  
00:16:00 Overview of baseline service visibility with Beyla  
00:19:30 Importance of library-level instrumentation  
00:24:00 Announcement of Instrumentation Hub and its features  
00:28:00 Future plans for extending Fleet Management and OpAMP integration  

# Observability at Scale with Open Telemetry

**Hello and welcome to our talk!** 

How's everybody doing? How was lunch? Okay, it sounds like we just ate lunch. I am Ted Young, a Developer Programs Director here at Grafana Labs, and I'm also a co-founder of the Open Telemetry project.

And my name is Edwin, and I am a Product Manager here at Grafana Labs for all things instrumentation and collection. 

### Open Telemetry Enthusiasm

Who here is excited about Open Telemetry? Who has played with Open Telemetry? Show of hands, please! I hope to see all hands up! Great! We share the same enthusiasm, especially Ted. However, that excitement must translate to deployments at scale, and that’s where many teams find themselves struggling. It often takes months, if not years, to roll out Open Telemetry properly. 

This challenge is at the heart of our talk today. We’re going to discuss a framework for thinking about the problem, breaking it down, and suggesting some solutions. We hope to wrap it all up neatly.

### The Complexity of Installation

Let’s face it: installing everything by hand is frustrating. It’s confusing and has an inherent catch-22. You want the system to work, but you’ve never used it before, so you don’t know what “correct” looks like. You have to install it first to understand what correct is, but if it’s not correct, how can you possibly get there?

To add to that, the systems we’re dealing with today are vast and composed of many pieces. For each part of your system, you need to find the corresponding piece of Open Telemetry that observes it and then connect them together. This is akin to a big box of Legos for observability, but it’s tricky because there’s no one-size-fits-all solution. 

### The Need for Comprehensive Coverage

It's critical to have comprehensive coverage. If you lack this, tools like distributed tracing won’t provide their full advantages. If you’re a system operator needing observability and have to rely on application developers to roll it out, you risk a patchwork rollout. This can delay the benefits you’re aiming for.

Let’s say you figured out which pieces of Legos you need. Now you must deploy it at scale. Team A has this stack, team B has another, and you need to roll out the necessary configurations across all teams and environments. Maintaining this at scale becomes quite complex due to the evolving nature of applications and environments.

YAML files can be a nightmare. You need to track all configuration changes as they happen, which makes it chaotic and challenging to manage costs. 

### Solutions in Open Telemetry

So, are there solutions in Open Telemetry or elsewhere that can simplify this chaos? The answer is yes, it is possible to have a zero-touch, zero-code experience for Open Telemetry, but it’s not complete yet. We are actively working on it.

To break this down, we need to think about observability in terms of needs. What do we actually need when observing our system? 

### Hierarchy of Needs for Observability

If we consider a hierarchy similar to Maslow's hierarchy of needs, we can establish a framework for observability needs. At the bottom, we have **infrastructure visibility**, followed by **baseline service visibility coverage**, and at the top, **custom instrumentation and business logic**.

You might dive deep into custom logs and instrumentation, but when an incident strikes, if you lack broad coverage, you won't be able to isolate the issue effectively. 

Let’s explore this hierarchy layer by layer, starting with **infrastructure**.

### Infrastructure Visibility

The foundation of our observability framework is infrastructure visibility. If I had to choose only one tool for observing a system, it would be infrastructure visibility. This universal model encompasses hardware and resources driven by computer processes. 

With the addition of containerization, cloud providers, and data services, this layer becomes a strong starting point. Our solution for this need is **Alloy**. 

Open Telemetry’s collector is a critical component, collecting metrics, logs, metadata, and traces from your host and containers. Alloy extends this by incorporating resources from existing communities such as Prometheus and Loki.

### Baseline Service Visibility

The next essential layer is **baseline service visibility**. You need to know how all your services are performing quickly. You don’t want to wait for custom instrumentation to gather these signals. This is where we recommend using Open Telemetry's eBPF instrumentation, known as **Beyla**.

Beyla allows you to achieve service-level health without redeploying applications, quickly identifying service-to-service dependencies. However, it won’t address all root cause issues, which is why we need to go up a layer.

### User Land and Application Insights

The next layer involves understanding what the system does for users, not just how it consumes resources. This is the "love and understanding" layer. Here, we need at least library-level instrumentation, focusing on database clients and web frameworks to connect everything seamlessly.

As systems evolve from monolithic to microservices architectures, understanding user interactions becomes increasingly complex. Distributed tracing through language-level libraries is crucial to connect user actions with backend processes.

However, installing this instrumentation can be challenging. You need to identify which libraries you’re using, find the right instrumentation packages, and manage dependencies—this is not straightforward.

### Automating Instrumentation

To address this, we’ve created a new Special Interest Group (SIG) in Open Telemetry called the **OTel Injector**. This uses the traditional Linux LD preload method to automate instrumentation injection into your runtimes. It aims to work with various languages, excluding Go for now. 

### Custom Instrumentation and Self-Actualization

Finally, there’s the **self-actualization** layer, which involves custom instrumentation. While library-level instrumentation covers standard use cases, unique business needs require you to utilize Open Telemetry SDKs and APIs for deeper insights.

It’s easy to get started with documentation, but doing this effectively at scale can pose challenges, such as inconsistent attributes across teams. We recommend leveraging OTel APIs and existing traces to enhance data quality.

### Recap of Our Framework

To recap our hierarchy of needs and solutions:
- **Infrastructure Monitoring**: Covered by Alloy
- **Baseline Service Visibility**: Addressed by eBPF with Beyla
- **Application Level Instrumentation**: Via Open Telemetry language libraries
- **Custom Application Logging**: For nuanced use cases

### Introducing Instrumentation Hub

Now, how do we tie all this together? We are excited to introduce a new solution called **Instrumentation Hub**. It offers a point-and-click experience for deploying the entire stack we’ve discussed. 

Instrumentation Hub automatically discovers under-instrumented applications and infrastructure, making it easy to select what you want to instrument and implement best practices. 

Imagine you’ve used your infrastructure-as-code (IaC) tooling to deploy your collectors. In Instrumentation Hub, you can discover uninstrumented Kubernetes clusters, select them, and begin instrumentation. 

After deploying, you can monitor metrics, logs, and key events from your clusters. You can scale this up easily to cover all your Kubernetes clusters, ensuring broad instrumentation quickly.

### Scaling Up Service Monitoring

Next, you’ll want to instrument your services for baseline visibility. You can do this by selecting services in your environment, capturing essential metrics and service-to-service links. 

You’ll receive a summary of your instrumented services, helping you visualize connections and performance metrics effortlessly.

### Fine-Tuning Instrumentation

If you need to tune your coverage, you can easily adjust configurations or remove instrumentation with just a few clicks, making it simple to manage your observability footprint.

### Under the Hood of Instrumentation Hub

Under the hood, Instrumentation Hub is a UI and SaaS service backed by **Fleet Management**, a control plane for Alloy. It connects to your system, scans for information, and manages configuration changes seamlessly.

Since launching Fleet Management in May, we have witnessed widespread adoption, with thousands of remotely configured pipelines and over a hundred thousand daily active collectors. This is fundamentally transforming how teams operate.

### Future Plans and Community Engagement

We aim to extend Fleet Management to work with Open Telemetry's protocol, OpAMP, allowing for functionality across all collector distributions. 

We are just getting started. Our ambitions extend beyond baseline coverage, aiming to automate SDK injection and implement AI-driven feedback loops for ongoing analysis and recommendations.

In conclusion, a simpler experience for Open Telemetry is not only possible but is actively being developed by the Grafana Labs team and the Open Telemetry community. 

The Instrumentation Hub will roll out in a few weeks as a public preview. You can get notified by scanning the QR code to join the waitlist.

Thank you for your time! We’ll now take questions.

## Raw YouTube Transcript

Hello. Hello. Welcome to our talk.
How's everybody doing? How was lunch? Okay. Alright, that sounds
like we just ate lunch. Yeah, we didn't. So I am Ted Young, as mentioned before. I'm a developer programs
director here at Grafana Labs. As well as a co-founder of
the Open Telemetry project. That's right. And my name is Edwin and I am a product
manager here at Grafana Labs for all things instrumentation and
collection. So who here, if you could be so kind,
give me a show of hands, is excited about Open Telemetry?
Has played with Open Telemetry, is keen on it. I'm hoping all the
hands go up. Yeah, yeah. Okay. Alright. Well we share the same
enthusiasm, Ted especially does. Do you think Ted shares the
enthusiasm? Yeah, I think so. Ted, yes. However, that excitement has to translate
to deployments at scale. And this is where we think a lot of
teams are stuck. They're struggling, it's taking months and no joke, years to get open telemetry
rolled out properly. That challenge is at the
heart of our talk today. We're going to go through a framework
for thinking about the problem, breaking it down. We'll suggest some solutions and maybe
a way to wrap it all up in a neat package. Absolutely. So yeah, the reality is installing
everything by hand sucks. It just completely sucks. It's confusing. There's an inherent
catch-22 with standing up a complicated system where
things can go wrong. You want it to work, but
you've never used it before. So you don't know what correct looks like, but you have to install it first before
you can understand what correct looks like. And if it's not correct,
how can you possibly get there? That's right. It's just definitionally hard, but it's even worse than that
because there are too many pieces. And when I say there are too many pieces,
I'm not talking about open telemetry, I'm talking about your system. Systems these days are huge and
they are made of a variety of pieces and for each piece
you have in your system, you have to find the exact matching piece
of Open Telemetry that observes that part of your system and then you
have to connect them together. So it is definitely a big box
of Legos approach to doing Observability, but that's hard because
there's no one way. It's not just -- clicking Legos together is nice because
all the Legos are the same and they all can click together -- but in this case you have to use different
techniques depending on the different part of your stack
you're trying to access. And hopefully at your large
organization there is no one person or team who has access to everything. So how can you do this, right? You want to have comprehensive
coverage. This is really, really critical. If you don't have
comprehensive coverage and you want to use some tools like distributed tracing, you're just not going to get the
full advantage out of your tools. And if you have to go to somebody
else in order to roll out the Observability that you need, if you're a system operator and you need
to go to an application developer team and say, please roll this out, I need
it. And they're like, "maybe later". You're going to have a kind of patchwork
rollout and it's going to take time to get to the point where you're really
seeing the value of the tools that you're trying to use. And let's say you did figure out the
pieces of the Legos that you needed. This team runs this runtime,
this team has this library, so we can put the pieces
together. You have to imagine, you have to get that deployed at scale. That means team A has this stack
and they need this config and it must be rolled out. Now repeat
that across all your teams, across all your varying environments and
maintaining that at scale becomes quite complicated. It's a whole mess of a management
challenge and that's got to happen continuously because the
applications are evolving, your environments are evolving.
So you got to keep on top of this. YAML. Nightmare, YAML nightmare. So
you have to stay on top of it. You have to track all the changes
to the config as they happen. The last talk was talking
about this as well, and this makes it very chaotic
to even just track and manage the costs. So this begs the question, are there solutions upstream in Open
Telemetry or in the world at large that kind of take all of this chaos,
bundle it up into a good experience? It'd be really funny if the answer was no. And this was just the end of the talk.
It is the end of the talk I'm off. The answer is absolutely yes, it
is possible to have a zero touch, zero code kind of experience
for Open Telemetry, but not yet. Yup. It's not yet complete, but we
are actively working on it. So if we're going to break this down
because it is a piecemeal and we want you to understand the different pieces, we have to think about
Observability in terms of needs. So what is it that we actually need
when we're observing our system? And if you kind of turn that into a
hierarchy and we look at other kinds of needs, like emotional
needs, personal needs, you have in psychology a
Maslow's hierarchy of needs. So the idea here isn't so much that one
layer is more important than the other, it's just that some layers are
more fundamental than others. Self-esteem is really,
really, really important. But if you don't have oxygen, you're not worrying about
self-esteem in that context. So you have these fundamental layers
kind of stacked on top of each other. Yeah, my favorite is you worry about your
haircut after you have some food in your belly, right? Yeah. So I think in the same way that
there's needs for human beings, we'd like to propose that there's a
framework of Observability needs that is in a parallel track with this. So at the bottom you've got
infrastructure visibility, then your baseline service
visibility coverage, and all the way at the top you've got
custom instrumentation and custom business logic. You definitely could go really deep
and have all sorts of custom logs and instrumentation, but come the time that an incident
strikes and you don't have broad coverage, and you can't isolate
the issue. Good luck. You could have all the
debug logs in the world, but if you can't isolate where the
issue was, you're not in good shape. So. Let's go through layer by layer
starting with infrastructure. So yeah, the fundamentals,
the foundation of the house. If I had someone weirdly put
a gun to my head and say, Ted, you have to observe this system, but
you only get one tool, what would I do? I would probably have to choose
infrastructure visibility. This is the broadest conception of your
system where we're just talking about hardware and resources being
driven by computer processes. That is a very universal model that we're
all familiar with and we all know how much you can do with that. So that is fundamental when you
add in all of the containerization, cloud providers and data
services to that layer, that is an amazing broad starting point. Everything else you're looking
at builds on top of that. So you go with that first. Our
solution to this need is Alloy. So Open Telemetry has a
concept of a collector. Who here is familiar with the collector. There we go. Yeah, this is definitely the most popular
part of Open Telemetry. It's awesome. This thing shockingly collects
metrics, logs and metadata, tracing, other things from
your host, from containers, everything on your system. And it can also take the other kinds
of telemetry that you're emitting and process all of them. So it's a
processing and pipelining tool. So this is kind of the base of operations
is the Open Telemetry Collector and then we are distro of that. Alloy, extends that set of
resources with stuff from prior communities. Like there's existing communities
in Prometheus and Loki and other places that have already done the work
to create instrumentation for a lot of these infrastructure sources
that we're interested in. So it's not Open Telemetry data,
but it is really good data. So we want that. So Alloy bundles, a lot of that in together with all
the other Open Telemetry goodness. This is something we're looking at
upstreaming and shout out to our Alloy team, everyone who's working
on the collector right now. Absolutely. So we've got the infra
level done. Let's go up the stack. So the next thing we think is essential
is baseline service visibility. So you want to know how all your services
are performing and you want to know this broadly and you
want to do this quickly. You don't want to wait to have custom
instrumentation in each of your apps to get these kind of signals because really
it's a game of figuring out how your services are doing so you can isolate
issues and quickly start debugging. And this is where we recommend
you go with Open Telemetry eBPF instrumentation,
a project known as OBI, but better known to you as Beyla. So Beyla was donated this
summer by Grafana Labs to OTel. And really what it ultimately lets you
do is without needing to redeploy your applications, you can get
that service level health, figure out the service to service
dependencies and do it very broadly, very quickly. Now that's fantastic, but it won't get you to all of the root
causes of issues and that's why we think you need to go up a layer. So getting to actual user land stuff so you have a user and they're
interacting with your system. So this is the layer where we
understand what the system is trying to do, not just how
it's consuming resources, but what is it attempting to
do on behalf of the users. So this is the "love and
understanding" layer of our stack. What are the
applications actually doing? And in order to get that information, we need to go into those applications. We need at minimum library
level instrumentation. So this is where we're looking
at your database clients, your web frameworks.
And we're connecting all of that together. And this is more important than ever
because as our systems grow and as we move away from the classic monolith to
these more tiered architectural systems like microservices and stuff like that, if you just have
disconnected network edges, if you just have network calls and
things like that and you're trying to understand the applications
as these isolated things, you can't see what the user's trying
to do. Back when you had a monolith, you could sort of see that. But as things have gotten broken
up into larger and larger systems, it becomes harder and harder to get
a complete story from one piece. So the distributed tracing through all
of these language level libraries is the critical thing to connect the
user putting the checkout button to the database blowing
up. So the problem is, in my opinion, this is hands down the hardest
part of Open Telemetry to install. It sounds easy on the surface,
just install this stuff, but this doesn't work the way
regular installations work. And it's not really Open Telemetry's
fault, it's just inherent in the problem. You have a bunch of libraries
in your application, so if you want to install this,
you have to figure out one, which libraries are you using? And
then you have to figure out, well, which instrumentation packages match
the libraries that I'm using and which versions match? And
once you've figured that out, you have to install those packages.
And then you have to wrap up these libraries in the instrumentation. Your dependency manager is not going
to help you with this task, right? This is a kind of cross-cutting concern
approach rather than your typical developer approach. So this is actually
really difficult to do by hand. So we want to automate it. Different languages have
tools today to automate it, but they all work a
little bit differently. They all have their own little limitations
and I think as they were saying in the last talk, it's like everyone's speaking a different
language and that makes it a lot harder for everyone to
communicate with each other. So what we want to do instead is
have some universal mechanism. So to that end, we've spun up a new SIG in Open
Telemetry called the OTel Injector. This is based on the traditional
Linux LD preload technique if you're familiar with that. So
automating at the kernel level, being able to inject this instrumentation
into all of your runtimes. So this is a universal approach. It works in basically
every language but Go. Java, .NET, Node.js, Python,
Ruby, PHP coming soon. All of this is under
development, it's not ready yet, but this is our plan going
forward for Open Telemetry. But the SIG has started and you
can join it if you're interested. Alright, so you've got infra layer
done, baseline service visibility. You've got some transaction
tracing for well-known libraries. So all that's left is
"self-actualization", right? Yes. Okay. So the library level instrumentation is going
to cover a lot of standard use cases. However, there are going to be bits
of your code that are custom to you, your company, your business, and this instrumentation will never
really be adequately covered by the layers below. And this is where you need to look beyond
those baseline layers and look to the Open Telemetry SDKs and
APIs to go deeper and start enabling. Now the thing is this
is fairly easy to get started with -- great documentation out there.
You can start producing this data. The challenge is doing this well at scale. Often times the challenge occurs
because you don't know exactly what the attributes are that you need ahead of
time. You all across different teams, maybe inconsistent in how you show
those attributes and dimensions up. So our recommendations are of course
take advantage of the OTel APIs it's great and easy to get
started with, but consider, maybe take existing traces and augment
them a little bit with the attributes that are interesting to you. When you look to add custom traces
and log messages, you may struggle, and this is where you can take a look
at the [OTel] semantic conventions themselves as a guide for
producing higher quality data. And then one emerging idea, from the
left field a little bit, could be, you may not need to produce application
logs because there are technologies like dynamic profiling which
could theoretically capture
a whole stack trace and make it completely unnecessary for
you to go application level by level. The challenge of course is doing this
at scale and making it cost effective. So that's why we think
it's still on the frontier. Right? So, that is our hierarchy of needs
matched up with our hierarchy of solutions. So just a quick recap of
everything we went over at the baseline, the air and water layer. We have infrastructure monitoring
that we do with alloy right above that, the kind of health and safety layer. We have eBPF with Beyla and OBI just above that, love and respect. We have the Open Telemetry language level
instrumentation and at the very top, the self-actualized, nirvana,
known as application logging. So how do we tie all this together? I don't know, Ted, how do
we tie it together? Well, we're very excited to
announce a brand new solution. It's called Instrumentation Hub. It
was teased earlier in the keynote. What it is, is a point and click experience where we
took that stack we just showed you and made it really easy to deploy. We automatically discover all
of your under-instrumented apps, your infrastructure. We make
that really obvious and clear to you. You can point and click, select what you'd like to instrument
and get going with well-defined patterns and best practices. Now we're going
to take you, first person view, and we're going to try
to do that whole stack. So I want you to imagine you've used
your infrastructure-as-code (IaC) tooling to get your collectors deployed.
That's what you've done so far. And now we're going to get
the instrumentation going
for the baseline. So we're going to start with your infrastructure. Here you come in and you discover that
there's seven Kubernetes clusters that are not instrumented. I've got a couple
Dev clusters, a Playground environment, and four Production clusters.
So I'm a little gun shy, so I'm going to start with the Playground
cluster and you just select it, click of a button and
you get some options. By default it covers Kubernetes metrics, but you can augment that with node
logs, pod logs, cluster events. And that's pretty much it, right? The instrumentation starts rolling out
and if you come back and you take a look at what's done, you can go into Kubernetes monitoring
in Grafana Cloud here you'll see the cluster, the Playground clusters instrumented
when you've done so you're getting your CPU metrics, your memory stats, some network information and logs
and key events from the cluster. Fantastic, that went well. Let's
ramp it up. Let's scale it up. And I'm going to go ahead and instrument
the rest of my Kubernetes clusters here. Pretty much I just go in here, point and click a few times and that's it. My instrumentation is on
its way. Same as before. You've got the summary view. You can make those optional
selections if you'd like and say "Instrument now" and the
pipelines start to get rolled out. And then before you know it, you can
come back into Kubernetes monitoring. And there you see there's data flowing
from seven Kubernetes clusters. Fantastic. So that was pretty quick.
I just finished my infra layer. Let's go up the stack. I'm going to go to my services now
and try to get my baseline service visibility. So here I've got a discovery with 134 services that are uninstrumented. Again, I want to get to my Production
clusters, but before I do, I'm going to start with the Playground
environment. Luckily the Open Telemetry demo is running there and that gives me
a great variety of services to test the technology out. So I'm going to select
all the services in that namespace, ask to instrument it, get a summary
for what's there. By default, we'll capture the "Golden signal" metrics
and some service-to-service links. But optionally you could
augment this with tracing, profiling and even process
metrics. And that's pretty much it. The instrumentation begins to roll out. Let's take a look at what
that looks like after. So you come back into Instrumentation Hub, you get a summary of your instrumented
services and you can choose one, perhaps the "Cart" service. And
there you go. Out of the box, you see the golden signals,
inbound / outbound connections, what the distributions are. Additionally, you get some distributed tracing
generated from the cluster thanks to eBPF. You can take a look at
the application logs, some CPU profiling, a map of
the service-to-service links, some OTel instrumentation reports, and even process stats. So that was
pretty great. Now let's scale it up. I had my Playground environment. I'm
going to do the same instrumentation, but I'm going to roll it out
across my Production clusters. The only caveat is I'd like to
deselect some namespace because they're particularly noisy. So
I've got this "Monitoring", "Networking" and "Security" namespace
that I'm just going to deselect from all of the namespaces. And same as before, I'm going to go ahead and get
to the instrumentation space and make the optional selections. So we're nearly there with
our namespace selection. And then we go to instrument it again, you get a summary view of all the
services. You can just get a quick gander and then you continue. And again, by default we're doing the
baseline service monitoring stuff, but you can get to higher level
stats. That's pretty much it. Those services are now going to
be instrumented. So let's say your instrumentation rolled out and
you wanted to tune your coverage. So here I've got 58% initial coverage. And let's say I wanted to
tune my playground cluster. I'm a little cost conscious. I could go down to the
"opentelemetry-demo" namespace, go into the settings and just take off
all of this additional telemetry that I was capturing. Alternatively,
to wind it down, I can just go back to the entire cluster
and select all the namespace and delete the instrumentation also with just a
click of a button. And that's it. Very, very easy. So what you just saw
is in about less than 30 minutes, we got your Pareto optimal
baseline coverage fully completed. And now you can invest the
time to go deeper where needed, where you have the cycles to invest to
get to the transaction tracing and to the custom logic. So how does this work, Ted? Right. Okay, so under the hood,
what does Instrumentation Hub do? Instrumentation Hub is
a UI and a SaaS service. Its backend is something
we call Fleet Management. Fleet management is a
control plane for Alloy. So you deploy Alloy into
your system and it connects automatically to Fleet
Management, it scans your system, sends all the information back, and Fleet Management can start pushing
out configuration and change requests down to Alloy. Absolutely, and the thing that gave us confidence
to build this abstraction layer is that since GA'ing Fleet Management
in May, we've seen very, very widespread adoption. We've come up to thousands of
remotely configured pipelines and now over a hundred thousand
daily active collectors. And it's fundamentally changing how teams
are working and it's allowing them to keep up with the moving demands of their
observability coverage and to really roll it out at scale. We believe that we can bring the same
magic to Open Telemetry workloads and really make that whole complexity simpler. And that's why we've been investing
in the Instrumentation Hub. So to that end, this currently works on top of Fleet
Management with the Alloy distro. But we want to upstream this. We want this to work with all collector
distributions, not just Alloy. That's right. So to accomplish that, we are going to extend Fleet
Management to also work with Open Telemetry's control plane
protocol, which is called OpAMP. So OpAMP will work with
the collector distros that are not Alloy and it's also going
to give us some additional features. And just to show you how this
would work, this is not a gimmick. We're actually doing this. Here's a working prototype and we'll
get this into your hands very soon. Here is Fleet Management and
you've got pipelines for Alloy. We have a bunch of templates and
we do the same for Open Telemetry. There you'll see that's OTel YAML
config. That's not Alloy River config. You get a visualization of the
pipeline as you develop it there is, shout out to the OTel bin team
for giving us that visual. And then there's full syntax validation, the whole nine yards so that your
pipelines can be developed risk-free, not just for Alloy, but also for your
canonical Open Telemetry distros. Similarly, if you come into the regular Fleet
Management Collector Observability view, you can see the health and state of
your Open Telemetry collectors and log messages right alongside the rest of
your Alloy collectors and even get a visualization of the live
pipeline that was deployed. Now the cherry on top is we get to do
some net new things because of OpAMP, like in-place collector upgrades. This is something we were not able to
previously do with just Alloy and the existing APIs. So I do want to pare this a
little bit by saying that we are just getting started. This was just the baseline coverage on
Kubernetes with some baseline service monitoring. Our ambitions
are to go up the stack, get those SDKs and libraries
automatically injected, take adaptive sampling to the edge. And ultimately we want to get to an
AI-driven feedback loop where we're constantly analyzing what we're collecting
and making recommendations for you. And you can just apply those as you go. So I just want to give you a sneak preview
of a hackathon project that our team just finished recently. And here is a sampling
config where the data was ingested. We analyzed the numbers and we thought
there was an opportunity to prevent some egress of telemetry and do
some sampling at the edge. And as that's discovered
and it's communicated, you can just deploy that with a single
click and it rolls out everywhere. So in short, I hope this makes it clear that a
simpler experience is possible and we are actively working on it, both in the Open Telemetry
community and here at Grafana Labs. That's right, and you've heard about this theme of
"Complexity Simplified" at the keynote and you will hear about it tomorrow as well. This is definitely our big
contribution to this area. Now the Instrumentation Hub itself
is going to roll out in a few weeks, so we're going to launch
it as a public preview. You can get notified by
taking a shot of the QR code. There's a wait list on the other side, and that's how you'll be able to
get access. And aside from that, we'll just take questions now.

