# What&#39;s New &amp; Next in Grafana Alloy: The Official OpenTelemetry Collector Distribution

Published on 2026-05-14T17:18:09Z

## Description

Grafana Alloy is now an official OpenTelemetry Collector distribution — with a native OTel YAML engine, a dual-engine ...

URL: https://www.youtube.com/watch?v=v8ukwFUh8PU

## Summary

The show "What's New & Next in Grafana Alloy: The Official OpenTelemetry Collector Distribution" was published on May 14, 2026. Speakers Marko, a software engineer on the Fleet Management team, and Bejal, a software engineer on the Alloy team, discussed the advancements in Grafana Alloy, which is now an official OpenTelemetry Collector distribution featuring a native OTel YAML engine. Key highlights included the introduction of the OpenTelemetry engine, which allows for a vendor-agnostic workflow and seamless integration with existing OpenTelemetry components, as well as the capabilities of Grafana's Fleet Management for centralized control of telemetry collectors. The session emphasized the importance of open standards and the flexibility offered by Alloy for both new and existing users.

Topics: Grafana Alloy, OpenTelemetry, YAML engine, Fleet Management, vendor-agnostic workflow.

## Chapters

00:00:00 Introduction of Alloy's OpenTelemetry engine
00:06:54 Overview of Grafana Alloy features and OTel integration
00:13:08 Overview of Grafana Alloy and OpenTelemetry engine
00:18:35 Introducing OpAMP server in Grafana Fleet Management

- Okay, hi everyone. Welcome to our talk. We're going to talk about Alloy's OpenTelemetry Engine. We're going to discuss what's new and what's next. My name is Marko. I'm a software engineer here at Grafana Labs, working on the Fleet Management team.

- And I'm Bejal. I'm a software engineer working on the Alloy team.

- Yeah, and we're super excited to present to you all of the OpenTelemetry capabilities we've been working on for the past year. But before we talk about what's new, let's actually take a look back at how we got here. Two years ago at GrafanaCON, we announced Alloy as a collector that supports both Prometheus and OpenTelemetry Protocol formats. Last year, we did a deep dive into Alloy where we proved this integrated approach by unifying a high-performing Prometheus pipeline with OTel Collector workflows in Alloy. Now, this year, we continue to pave the way forward by making Alloy an official and fully compliant OTel Collector distribution with native YAML support.

Why? You might be wondering why. There are a few reasons for that. 

1. The upstream community actually tightened what it means to be an OTel Collector distribution. In the spirit of being community-first and adopting open standards, we really wanted to put out a product that fits that definition entirely. 

2. More and more customers are demanding a vendor-agnostic workflow. Ideally, they would like to use a configuration language that's transferable across vendors. 

3. We took a look at not only the current state of the OTel Collector but also the future developments. Our goal is that Alloy develops and evolves as the OpenTelemetry Collector evolves and gets those changes by default, with no developer effort required on our end.

So why does this matter to you, folks? It matters a whole ton because Alloy is Grafana's most widely distributed software and most widely deployed. It's one of the most popular OTel Collector vendor distributions. OpenTelemetry has now become the industry standard for generating, instrumenting, and exporting telemetry data. Alloy's new engine will give you native access to the broader ecosystem of OpenTelemetry.

Now, I've talked about the why. Let's talk about the what. Bejal, can you tell us how this works?

- Yes, absolutely. I'm actually going to start with something slightly unorthodox. I'm going to kick off a demo right now, and you'll all see what I'm running in about five minutes. But I just want to give that a bit of time to calibrate. While that's running, just a general vibe check question for the crowd: Could you raise your hand if you've already used the OpenTelemetry Collector before or are even familiar with it? 

Okay, yeah, lots of hands, cool. So if you have already used the Collector before, I think a lot of the terms that we're using throughout this presentation are going to sound really familiar. But if you haven't raised your hand, no problem. You don't have to be an expert to follow along. 

So I'm going to actually check back in with my demo right now because I want to make sure that it is running properly. Just give me one second to sort that out. Great, okay, I think that's running. 

Now back to the slides. Before we get into the juicier details of the OpenTelemetry engine, I want to actually start by defining what we mean by "engine." When we say "engine," we're referring to the underlying runtime in Alloy that is wiring together the components that you define in your configuration and allowing telemetry to run through them. 

Alloy, as it stands, ships with the default engine. If you've used Alloy, this is probably the engine you're most familiar with. It comes with many different components that span across multiple ecosystems. We wrap upstream OpenTelemetry components, we wrap Prometheus components, and we have lots of different Loki components as well, and so forth. It's designed to work with many different sources and destinations of telemetry in many different formats. It's really a Swiss Army knife in that way. 

The language that the default engine speaks is Alloy configuration syntax, or the .alloy file that you would pass into a running Collector. That syntax was developed in-house and was chosen for a reason. It's very rich and descriptive, and it pairs well with the underlying complexity of the default engine. They work really quite well together.

What we're introducing now is the OpenTelemetry engine. That's the primary focus of this talk. The OpenTelemetry engine is essentially the upstream collector runtime embedded entirely within Alloy. That has some really cool implications, namely that it is automatically compatible with anything OTel. So it understands OpenTelemetry components, OpenTelemetry YAML configuration syntax, and so forth right out of the gate. You get the native experience from within Alloy. 

Both of these engines live side by side. Last year at GrafanaCON, there was a talk about what an OpenTelemetry Collector distribution is and why that's important. Just to hash a key takeaway there, a Collector distribution is a collector that is able to ingest and understand OpenTelemetry YAML configuration syntax. It needs to be able to wire together the receivers, processes, and exporters that you define, which gives you something really important: a vendor-agnostic collector experience. 

There are many different distributions out there, but they all share the same language. This is sort of the ethos of OpenTelemetry: these open standards can be implemented by different vendors but used together. With the introduction of the OpenTelemetry engine in Alloy, we now officially meet this upstream definition of a collector distribution. That was really important for us to do because, as Marko was saying before, OTel is becoming the de facto standard for how we want to describe and ingest telemetry. You want to be using a collector that sits well in that ecosystem and that also speaks that language. Alloy gives you that.

So now, what's actually included? It was released a couple of minor versions ago in version 1.14 with experimental stability, and it's still in experimental stability. The main feature is a new OTel sub-command. It behaves similarly to the run sub-command that exists in Alloy. It allows you to define one or more configuration files or configuration sources, validate them, and then kick the Collector into action. If you raised your hand before that you've used the OpenTelemetry Collector, it actually exposes the entire upstream Collector CLI experience, so it's going to look really familiar to you.

We're also introducing a new Alloy engine extension. This is really interesting, and I'm going to demo that in a second. It allows you to run an instance of the default engine pipeline alongside the OTel engine pipeline. You can run them both in parallel from a single Alloy instance. 

We also made sure to include an embeddable health dashboard because if you're running your collectors in production, you really want to understand how they're performing, ensuring they're using the correct amount of resources and that data is coming in and going out. It was important for us to include that detail in the experimental release as well.

This is less of a feature and more of an architectural decision that we made, but the OTel engine is based off of OCB, or the OpenTelemetry Collector Builder tool. That's a tool from upstream that allows us to define the components that we are going to bundle into our distribution in a declarative manifest file, and it will generate the core collector logic that's run. This is sort of the secret source to how we get it to be automatically native because we're using upstream.

able to do that without having to redeploy your collectors. 

So, with that in mind, we are working on a solution that will allow you to manage your OTel engine instances at scale effectively. This will help you maintain the health of your collectors and ensure that they are running optimally. 

To summarize, the key benefits of using Grafana Alloy as your OpenTelemetry Collector distribution include:

- **Upstream Code Integration**: Automatically receive upstream code into Alloy.
- **Standard Compliance**: Components included in Alloy adhere to specific standards, making them accessible to other collector distributions.
- **Backwards Compatibility**: Existing users can opt-in to use the new OpenTelemetry engine without disrupting their current setup.
- **Easy Migration Path**: Users can easily switch between the OpenTelemetry engine and other distributions.
- **Custom Builds**: Open-source nature allows users to modify and rebuild Alloy to suit their specific use cases.
- **Performance**: The default engine is optimized for Prometheus components and offers strong performance for distributed tracing with OTLP.

In the demo, I showcased a small-scale example running on Docker Compose, but Alloy is also capable of handling large-scale environments, as evidenced by our deployment in one of our largest dev clusters. We are currently processing over 12 billion spans in a 24-hour period, demonstrating Alloy's scalability and reliability.

As we move forward, we are committed to enhancing the OpenTelemetry engine and ensuring that new features are OCB-able and accessible to other collectors. We are excited about the potential for remote management of the OTel engine at scale, which will simplify the management of multiple telemetry collectors and improve overall efficiency.

Thank you for your attention, and I look forward to your questions!

Able to do that at the click of a button. Now, fortunately for you, we at Grafana have felt that pain. So what if I were to tell you that we have a solution that already does this and then more? Who here has heard of **Fleet Management**? Nice, I see a couple of hands. 

Okay, so **Fleet Management** is our collector management solution for **Alloy**. What it does is it provides this centralized control plane where all of your **Alloy** collectors register, and you can check out their health, roll out new configuration changes, all from the same place. 

Now, to give some numbers at you for its success, we have over **7,000 organizations** actively using it; over **100,000 custom configuration pipelines** enabled currently; and over **360,000 active collectors** receiving configurations from our servers at this very moment. 

Now, naturally, given how popular **Fleet Management** is, we wanted to extend that experience to other **OpenTelemetry Collectors** as well, not just **Alloy**. To that end, we've implemented an **OpAMP** server in **Fleet Management**. For those of you unfamiliar, **OpAMP** stands for the **Open Agent Management Protocol** and it's the **OpenTelemetry** standard for remote management of agents. 

Now, our solution is currently in private preview but it's on its way to general availability, and you will be able to try it out shortly. Once it's out, you'll be able to use **Grafana Fleet Management** with any **OpenTelemetry Collector**. And the best part of all is it's completely free to use, no charge to you whatsoever. 

Let me show you how it works. Okay, we can go back to my laptop. So this is the **Fleet Management UI**. As part of the demo, I've connected two collectors and I have a local service running that's creating logs. Now, what I would like to do ideally is create a configuration to pick up those logs and send them to **Grafana Cloud**. 

I have my collectors here, I can click on one, and I can see its health metrics in the dashboard at a glance. I can check out the collector's own logs, and I can also view the collector's attributes. This is particularly important because these attributes are what you use to match different types of configuration to this particular collector. 

Now, let's actually pick up the logs from my locally running service. I'm going to go on my **Remote Configuration** tab and I'm going to create a new config pipeline. I can choose the **OpenTelemetry** config language, and there are some integrations built out of the box for common use cases, but let's just go with a custom one for now; it's easier. 

I'm going to give my pipeline a name, and I am going to drop this configuration in there. Now, at a high level, what this does is I'm configuring an **OTLP** receiver to just pick up telemetry at these two ports. I'm going to send that out to my local **Grafana Cloud** account, and I am only creating this pipeline for logs. Currently, we don't care about metrics and traces. 

Then, I can test it out. Syntax is correct. Let's go Next. Now, let's say I'm a user here and I am not exactly sure about this configuration. Maybe it's good, maybe it's not. I'd like to test it out first. Well, okay, I have a dev environment and I have some collectors running there. Let's send it out to them. 

How can I find them? Let's just search for environment. Look at that. We do have a dev environment, and we have two collectors running in our dev environment. Well, that's not enough. I mean, you don't want to send this out to every single one of those. At the end of the day, you want to trim it down further. 

Maybe some of them only collect metrics. Maybe some of them only collect logs. I created a log pipeline, so let's look for collectors that only pick up logs. Maybe something like this: `collect_logs = true`. Nice, there is one. Okay, awesome. 

So at this point, I'm happy it's one collector. Let's just roll it out and see what happens, right? So I'm going to click Save. I'm going to save my pipeline. And by default, we keep it turned off. But to activate it, all I need to do is click one button. 

Now, what this is going to do is our server is going to send this new configuration to my locally running collector, and I will be able to see those logs if everything works well. Now, I hope some of you are familiar with our logs drilldown. But if I go to my logs drilldown, look at that, I'm seeing a service here, right? 

So it's sending out the metrics from the last 10 minutes. It started 13 minutes ago. This is roughly when Bejal started the demo. So it's kind of, okay, so now we've picked up the logs and we're seeing them in **Grafana Cloud**. If I set the refresh rate to five seconds, we're going to start seeing the logs come in in real time. 

So this is 13 and yeah, 14 minutes and 10 seconds ago. Wait five seconds, we're going to see a 10, 15 right there. And so our logs are coming in in real time. What have we done? We didn't have to meddle with local config files. We didn't have to manually restart any collectors. We did it all remotely from **Fleet Management**, and it just worked. 

So our goal for this is now to bring the same first-class experience to **Alloy's OTel engine**. Stay tuned for that because we have some really, really exciting stuff coming up there. We can go back to the slide, please. 

Great, so I think probably at this point, it's pretty clear that at **Grafana**, we really want to adopt and embrace **OpenTelemetry** standards into our products. What that looks like for **Alloy** is making sure that we are meeting this definition of a collector distribution and that we are providing a native experience to the users that really care about that. 

For **Fleet Management** as a product, we are extending it to not only manage the **OTel engine**, but also be able to manage any collector distribution. The design principles for both are the same. We want to embrace open standards, and we want to avoid vendor lock-in. 

So if you're interested in getting your hands dirty with the **Fleet Management** experience, you can come find us after and ask for access to the private preview. As I said, the **OTel engine** is available now. So, please do play around with it. Let us know if you have any questions. We'll be around to chat with you. We're really excited about this, and we hope you are as well. 

Thank you so much for being here, and thank you for listening. 

Thank you. (audience applauding)

## Raw YouTube Transcript

- Okay, hi everyone. Welcome to our talk. We're gonna talk about
Alloy's OpenTelemetry Engine. We're gonna talk about
what's new and what's next. My name is Marko. I'm a software engineer
here at Grafana Labs, working on the Fleet Management team. - And I'm Bejal. I'm a software engineer
working on the Alloy team. - Yeah and we're super
excited to present to you all of the OpenTelemetry capabilities we've been working on for the past year. But before we talk about what's new, let's actually take a look
back to how we got here. Two years ago at GrafanaCON, we announced Alloy as a collector that supports both Prometheus and OpenTelemetry Protocol formats. Last year, we did a deep dive into Alloy where we proved this integrated approach by unifying a high-performing
Prometheus pipeline with OTel Collector workflows in Alloy. Now, this year, we continue
to pave the way forward by making Alloy official
and fully compliant OTel Collector distribution
with native YAML support. Why? You might be wondering why. And there's a few reasons for that. Reason number one is that
the upstream community actually tightened what it means to be an OTel Collector distribution. And so in the spirit of
being community first and adopting open standards, we really wanted to put
out a product out there that will fit that definition entirely. The second reason is that
more and more customers are demanding a vendor-agnostic workflow. Ideally, they would like
to use a config language that's transferable across vendors. And last but not least, we took a look at not
only the current state of the OTel Collector, but also the future developments. Our goal is that Alloy develops and evolves as the
OpenTelemetry Collector evolves and sort of gets those changes by default, no developer effort required on our end. So why does this matter to you, folks? And it matters a whole ton because Alloy is Grafana's most widely distributed software out there and most widely deployed. It's one of the most popular OTel Collector vendor distributions. OpenTelemetry has now
become the industry standard for generating, instrumenting,
exporting telemetry data. And Alloy's new engine
will give you native access to the broader ecosystem of OpenTelemetry. Now, I've talked about the why. Let's talk about the what. Bejal, can you tell us how this works? - Yes, absolutely. I'm actually gonna start with
something slightly unorthodox. I'm gonna kick off a demo right now and you'll all see what I'm
running in about five minutes. But I just wanna give that
a bit of time to calibrate. And while that's running, just a general vibe check
question for the crowd. Could you raise your hand
if you've already used the OpenTelemetry Collector before? Or even feel familiar? Okay, yeah, lots of hands, cool. So if you have already
used the Collector before, I think a lot of the terms that we're using throughout
this presentation are gonna sound really familiar. But if you haven't raised
your hand, no problem. You don't have to be an
expert to follow along. So I'm gonna actually check
back in with my demo right now because I want to make sure
that that is running properly. Just give me one second to sort that out. Great, okay, I think that's running. Okay, so now back to the slides. I did just before we get
into the juicier details of the OpenTelemetry engine, I wanna actually start by
defining what we mean by engine. And when we say engine, we're referring to the
underlying runtime in Alloy that is wiring together the components that you define in your configuration and allowing telemetry
to run through them. And so Alloy, as it stands, ships with the default engine. And if you've used Alloy, this is probably the engine
you're most familiar with. It comes with many different components that span across multiple ecosystems. So it works with we wrap upstream
OpenTelemetry components, we wrap Prometheus components. We have lots of different loki components as well and so forth. It's sort of designed to work with many different
sources and destinations of telemetry of many different formats. It's really a Swiss
Army knife in that way. And the language that
the default engine speaks is Alloy configuration syntax or the .alloy file that you would pass into
a running Collector. And that syntax was developed in-house and it was chosen for a reason. It's very rich and descriptive and it pairs well with
the underlying complexity of the default engine. And so they work really
quite well together. And what we're introducing now
is the OpenTelemetry engine. That's the primary focus of this talk. And the OpenTelemetry engine is essentially the
upstream collector runtime embedded entirely within Alloy. And that has some really
cool implications, namely that it is automatically compatible with anything OTel. So it out of the gate understands
OpenTelemetry components, OpenTelemetry YAML configuration
syntax and so forth. And so, you get the native
experience from within Alloy. And both of these engines
live side by side. So last year at GrafanaCON,
there was a talk about what an OpenTelemetry
Collector distribution is and why that's important. And just to hash a key takeaway there because I think it's also
really relevant here, a Collector distribution is a collector that is able to ingest and understand OpenTelemetry YAML configuration syntax. So it needs to be able to wire together the receivers and processes
and exporters that you define and that gives you
something really important, which is a vendor-agnostic
collector experience. So there are many different
distributions out there, but they all share the same language. And this is sort of the
ethos of OpenTelemetry is these open standards
that can be implemented by different vendors but used together. And so, with the introduction of the OpenTelemetry engine in Alloy now, we officially meet this
upstream definition of a collector distribution. And that was really important for us to do because as Marko was saying before, OTel is becoming a defacto standard for how we want to describe
and ingest telemetry. And so you want to be using a collector that sits well in that ecosystem and that also speaks that language. And so, Alloy gives you that. So now, what's actually included? So it was released a couple
of minor versions ago in version 1.14 with experimental stability and it's still an experimental stability. And the main feature is
a new OTel sub-command. It behaves similarly
to the run sub-command that exists in Alloy. It allows you to define one
or more configuration files or configuration sources. You can validate them. And then, you can kick
the Collector into action. And if you raised your hand before that you've used the
OpenTelemetry Collector before, it actually exposes the entire upstream Collector CLI experience. So it's gonna look really familiar to you. We're also introducing a
new Alloy engine extension. This is really interesting, I'm gonna demo that in a second. But it allows you to run an instance of the default engine pipeline alongside the OTel engine pipeline. So you can run them both in parallel from a single Alloy instance. And we also made sure to include an embeddable health dashboard as well because if you're running
your collectors in production, you really wanna be understanding
how they're performing, making sure they're using the
correct amount of resources and data is coming in and going out. So it was important for us to include that detail in the experimental release as well. And this is less of a feature and more of an architectural
decision that we made, but the OTel engine is based off of OCB or the OpenTelemetry
Collector Builder tool. That's a tool from upstream and it allows us to define the components that we are gonna bundle
into our distribution in a declarative manifest file and it will generate the core
collector logic that's run. This is sort of the secret source to how we get it to be
automatically native because we're using upstream tooling, and so we automatically get upstream code into Alloy this way. And the second benefit or takeaway here is that the components
that we include in Alloy have to adhere to a certain standard. That's how they're able to
be used with the OCB tool. And so, any new components
that we introduce or that we currently have are not just glued to
Alloy as a collector, they're also accessible to any other collector
distribution as well. And so, that's a a lot of new features but it gives you a couple of things. The first is it's backwards-compatible. So if you are already
using the default engine and that experience really works for you, then it's entirely opt-in. You can use the extension to try out the OpenTelemetry engine in the same workloads or you can use a different deployment. So there's some room to try it out. But in general, nothing changes. It also gives you a really
easy migration path. So if you are already using an upstream OpenTelemetry Collector and you have OTel YAML configuration, you can just point that to
the OpenTelemetry engine and you can be off the ground. And the same applies in inverse as well. So if you're using the OTel engine and you want to try out
a different distribution, you can also go that way too. And another really interesting
benefit is custom builds. So we're using OCB, Alloy is open-source, you can check out the Alloy source code and you can edit that manifest yourself and you can very easily
spin up and rebuild Alloy. So you could remove a bunch of components, you can add different components, you could develop your
own and introduce them, but it's really easy to get started and so it allows you to sort of meld Alloy to be the collector
that suits your use case if it doesn't already
do so out of the box. So a ton of flexibility there. So now, we can move on to the demo. Great, cool, just a bunch of logs. I've kicked up a Docker
Compose application now and I'm running a single instance of Alloy and I've got the engine
extension enabled as well. So we should see both
engines running side by side and I've developed a
dashboard in the backend. Oh, seems like we're not
getting data through here, but I can actually just
explain it as we go. Ah, now we're getting data through. So this is a visualization
of the pipelines that I have configured. The OTel engine, I've configured with an OTLP receiver and I'm sending spans and traces from the services I have
to deployed locally. Those are getting batched. And then, they're getting
sent to the backend. And I've also included some
meta monitoring as well just so we can check how things are going. And if we scroll down a little bit, we can see some data. And if we scroll down some more, we can see that we have an instance of the default engine pipeline running. And this one, I've
configured to use Beyla. That's a really interesting feature that we have in the default engine. It allows us to auto
instrument applications that are running on the network. And then, I've decided to do that here, scraping those targets and writing it to the backend. And the main takeaway
that I want from this demo is that you can sort of pick and choose the strengths of either
engine to your liking. The choices that I've made here also reflect what we've
done internally at Grafana. So a lot of our metrics pipelines from monitoring our infrastructure are based on Prometheus exporters, and so we have Prometheus
native pipelines. And the default engine ships with really, really performant
Prometheus components. We have lots of other goodies in there like Remote Write v2 so we get tons of network savings. And in general, the default engine is a really strong choice for us. When it comes to
distributed tracing, though, we really like the way that OTLP describes spans and traces. It's very rich and structured in metadata, makes very powerful
visualizations in the backend. And so, that is a really
strong choice for us. And even before we
introduced the OTel engine, we were using wrapped upstream components in the default engine to
instrument our workloads. And so now, why not just
cut straight to the source? We can use those components and speak their language
directly in the OTel engine. So I think we can go back to the slides. What I just showed now is like
a really small-scale example. There's just a couple of applications that we're running in
a Docker Compose file. But we also have the engine deployed to one of our largest dev clusters as a dog-fooding exercise. And I have a slide here
that's aggregating some data over a 24-hour period. And you can see that in that time, we're receiving over 12
billion spans to the engine, which is a huge amount. In the second slide down, you can see that the amount of data is we have a spike of incoming
requests at a certain point. We can see that our pod count also responds really well to that. So we're scaling really
well to those requests. This is deployed in Kubernetes. And all throughout, we have a stable export rate too. So all that to say, you can run this engine locally, it's really easy to get off the ground, but it also works in
large-scale environments that have thousands of services and billions of data points as well. So a couple of things that make Alloy stand
out as a distribution: First, Alloy has been around
for a couple of years now and it's gotten a very positive
response from the community. To try and find a way to
put that into a number, we have around 8 million
Docker image pulls as of last week. So it's very well used and battle-tested. And with those millions of pulls also comes millions of
different environments that Alloy runs in. And it works in those environments, so it's incredibly versatile. And so now, when you introduce the OpenTelemetry engine into the picture, you also get the standardization
and portability of upstream alongside the huge amount of flexibility and the Swiss Army knife
that is the default engine and you get that all
in a single collector. So as I said, the engine is currently
in experimental status. We're slowly budging it
towards general availability. And as we do that, we are focusing on
identifying the strengths that we have in the default engine and finding ways to
contribute those upstream either via new OCB-able components or contributing to existing components. And likewise, when it comes
to introducing new features to the OTel engine itself, we wanna make sure that it's
done in a way that is OCB-able and is accessible to
other collectors as well and not just tied to Alloy. And something that we're
actively working on right now that we're really excited about is enabling remote management
of the OTel engine at scale. - So when we talk about scale, what we really mean is
running tens, hundreds, for some of you, even thousands of telemetry
collectors at a time. And managing those instances, making sure they're alive and healthy and pushing out new configuration changes can become a real pain. So much so that you would
probably need a dedicated solution just for collector management. Now, let's say you were to try
and create such a solution, there are a few capabilities
that you would want to see. Number one is that you should be able to standardize your configuration. So you create that once. And then, send it out to
any number of collectors. Number two is that you should
be able to control the rollout of that configuration. You don't want to have to define five configuration snippets. And then, every single
one of those gets sent out to every single collector. Instead, you can be smart about it and maybe choose something like matching by collector
attributes or a different method to really control the rollout
of your configuration. And finally, you should be able
to change your configuration dynamically on the fly whether that is by changing some values inside the config itself, adding or dropping a
component from your pipeline, or maybe even turning on or off an entire data collection pipeline. You should be able to do that
at the click of a button. Now, fortunately for you, we, at Grafana, have felt that pain. So what if I were to tell
you that we have a solution that already does this and then more? Who here has heard of Fleet Management? Nice, I see a couple hands. Okay, so Fleet Management is our collector management
solution for Alloy. What it does is it provides
this centralized control plane where all of your Alloy
collectors register and you can check out their health, roll out new configuration changes all from the same place. Now, to give some numbers
at you for its success, we have over 7,000
organizations actively using it; over 100,000 custom
configuration pipelines enabled currently; and over 360,000 active collectors receiving configurations from our servers at this very moment. Now, naturally, given how
popular Fleet Management is, we wanted to extend that experience to other OpenTelemetry Collectors as well, not just Alloy. And so to that end, we've implemented an OpAMP server in Fleet Management. For those of you unfamiliar, OpAMP stands for the Open
Agent Management Protocol and it's the OpenTelemetry standard for remote management of agents. Now, our solution is
currently in private preview but it's on its way to
general availability and you will be able
to try it out shortly. Once it's out, you'll be able to use
Grafana Fleet Management with any OpenTelemetry Collector. And the best part of all is
it's completely free to use, no charge to you whatsoever. Let me show you how it works. Okay, we can go back to my laptop. So this is the Fleet Management UI. As part of the demo, I've connected two collectors and I have a local service
running that's creating logs. Now, what I would like to do ideally is I would actually like
to create a configuration to pick up those logs and
send them to Grafana Cloud. Now, I have my collectors here, I can click on one, and I can see its health metrics in the dashboard at a glance. I can check out the collector's own logs and I can also view the
collector's attributes. This is particularly important because these attributes are what you use to match different types of configuration to this particular collector. Now, let's actually pick up the logs from my locally running service. I'm going to go on my
Remote configuration tab and I'm gonna create
a new config pipeline. I can choose the
OpenTelemetry config language and there are some integrations
built out of the box for common use cases, but let's just go with a custom
one for now, it's easier. I'm gonna give my pipeline a name and I am going to drop this
configuration in there. Now, at a high level, what this does is I'm
configuring an OTLP receiver to just pick up telemetry
at these two ports. I'm gonna send that out to my
local Grafana Cloud account and I am only creating
this pipeline for logs. Currently, we don't care
about metrics and traces. Then, I can test it out. Syntax is correct. Let's go Next. Now, let's say I'm a user here and I am not exactly sure
about this configuration. Maybe it's good, maybe it's not. I'd like to test it out first. Well, okay, I have a dev environment and I have some collectors running there. Let's send it out to them. How can I find them? Let's just search for environment. Look at that. We do have a dev environment and we have two collectors
running in our dev environment. Well, that's not enough. I mean, you don't wanna send this out to every single one of those. At the end of the day, you
wanna trim it down further. Maybe some of them only collect metrics. Maybe some of them only collect logs. I created a log pipeline. So let's look for collectors
that only pick up logs. Maybe something like this, collect_logs equals to true. Nice, there is one. Okay, awesome. So at this point, I'm
happy it's one collector, let's just roll it out and
let's see what happens, right? So I'm gonna click Save. I'm gonna save my pipeline. And by default, we keep it turned off. But to activate it, all I need to do is click one button. Now, what this is going to do is our server is going to
send this new configuration to my locally running collector and I will be able to see those logs if everything works well. Now, I hope some of you are familiar with our logs drilldown. But if I go to my logs drilldown, look at that, I'm seeing a service here, right? So it's sending out the metrics from the last 10 minutes. It started 13 minutes ago. This is roughly when
Bejal started the demo. So it's kind of, okay, so now we've picked up the logs and we're seeing them in Grafana Cloud. If I set the refresh rate to five seconds, we're gonna start seeing the
logs come in in real time. So this is 13 and yeah, 14
minutes and 10 seconds ago. Wait five seconds, we're gonna
see a 10, 15 right there. And so our logs are coming in in real time and what have we done? We didn't have to meddle
with local config files. We didn't have to manually
restart any collectors. We did it all remotely
from Fleet Management and it just worked. So our goal for this is now to bring the same
first-class experience to Alloy's OTel engine. And stay tuned for that
because we have some really, really exciting stuff coming up there. We can go back to the slide, please. - Great, so I think
probably at this point, it's pretty clear that, at Grafana, we really want to adopt and embrace OpenTelemetry standards into our products. And what that looks like for Alloy is making sure that we are
meeting this definition of a collector distribution and that we are providing
a native experience to the users that really care about that. For Fleet Management as a product, we are extending it to not
only manage the OTel engine, but also be able to manage
any collector distribution. And so, the design principles
for those both are the same. We want to embrace open standards and we want to avoid vendor lock-in. So if you're interested in
getting your hands dirty with the Fleet Management experience, you can come find us after and ask for access to the private preview. As I said, the OTel
engine is available now. So, please do play around with it. Let us know if you have any questions. We'll be around to chat to you. We're really excited about this and we hope you are as well. Thank you so much for being here and thank you for listening.
- Thank you. (audience applauding)

