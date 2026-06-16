# When Observability Meets a Tamagotchi

Published on 2026-05-14T17:17:42Z

## Description

TamaGROTchi is Grafana's hackathon-winning digital pet — a Tamagotchi powered by Grot (Grafana's dinosaur mascot), built on ...

URL: https://www.youtube.com/watch?v=-taKRZWXdwQ

## Summary

In this presentation at GrafanaCON, Chris and Nick introduce TamaGROTchi, a modern twist on the classic Tamagotchi toy, designed to engage users while demonstrating observability concepts. They discuss how TamaGROTchi, built with an ESP 32 board, can send logs, traces, and metrics to Grafana Cloud, serving as a playful tool to help users understand observability in small, hardware-constrained environments. The duo highlights the importance of telemetry signals and the implementation of custom dashboards to track the health and status of the virtual pets. They also mention incorporating AI features into the experience, allowing for interactive learning about logs, metrics, and traces. The presentation concludes with an invitation for attendees to visit their booth at the science fair for hands-on interaction with TamaGROTchi.

## Chapters

00:00:00 Introductions to TamaGROTchi  
00:01:15 Overview of TamaGROTchi features  
00:02:30 Explanation of the hackathon project  
00:03:45 Discussing customer use cases and challenges  
00:05:00 Importance of sending raw Otel data  
00:06:20 Sharing personal stories about their roles at Grafana  
00:07:15 Deciding on telemetry signals for TamaGROTchi  
00:08:30 Custom entity for Knowledge Graph  
00:09:45 Introduction of custom dashboards for monitoring  
00:10:50 Integration of AI features with Grafana assistant  

# Introduction to TamaGROTchi

**Chris:** Hello GrafanaCON, I'm Chris.  
**Nick:** And I'm Nick.  
**Chris:** We're here to introduce you to TamaGROTchi. 

Now, show of hands, who had a Tamagotchi growing up? Who had a Tamagotchi that died? And who had a Tamagotchi that died, and you don't know why it died? [Chris chuckles] Yeah, that seems like most people who had a Tamagotchi had the same problem. 

Well, TamaGROTchi is the new 2026 version, created by us here at Grafana. Grot's our dinosaur mascot, and now you can take him with you. He even talks to you! We've given him a cell phone, so when he gets hungry, he can even send you a Slack message. 

Grafana runs quarterly hackathons, and we won the last one for the science fair. Most past winners have added something to the product. You may have heard of AI observability or the Grafana assistant. However, we decided to make a cute little pet. 

TamaGROTchi is built with an ESP32 board and transmits logs, traces, and metrics via OpenTelemetry. Whether you're feeding or playing with him, each interaction is sent as one of those data types.

## Observability for Small Devices

**Nick:** Cool. So it's all fun and games, but actually, a lot of our customers are not using Kubernetes. They can't utilize a Java SDK; instead, they are building observability onto small devices like this. 

We have customers with robots running around warehouses and building EPOS terminals. These environments are hardware-restrained, with limited memory, poor internet connections, and they can't afford to run things like the OpenTelemetry collector or a full SDK on those devices. We wanted to experiment and see how easy it is to send raw OpenTelemetry data. 

So, we're just creating a JSON packet, sending that over HTTP, and sending it straight to Grafana Cloud. 

## Explaining Our Work

**Chris:** The other thing we wanted to do is explain our roles to our families, as they don’t really know what we do at Grafana. 

**Nick:** I'm a data engineer, and I deal with data loading scripts.  
**Chris:** And I'm an Observability Architect, so I talk about observability all day. 

This was the only way we could actually tell our families what we do at Grafana. When building TamaGROTchi, we needed to decide what telemetry signals to use. The trap is to just send everything as a log or a metric, whatever you are used to. 

We went down the route of implementing metrics like our "drop sick" metric, which was a simple binary value. This allowed us to build a dashboard that counted how many sick TamaGROTchis we had. However, we weren't able to answer other questions like, "How did they get sick?" or "Who let them get sick?" 

So, we started implementing logs. Every button press is logged, and we also included tracing, which lets us build a much better suite of dashboards.

## Observing the Data

**Nick:** So how do we get this data? How do we observe it? Who here knows about Knowledge Graph or Entity Graph? Perfect! We have written a custom entity for Knowledge Graph. 

Typically, this would provide a top-down view of your full application stack, showing Kubernetes pods, nodes, application workers, etc. In our case, we just have TamaGROTchis, but we have SLOs that are custom to our use case. You can see things like when they're hungry or when they're ill, all custom built into the Knowledge Graph.

We also have tried and tested SRE conventions in place. For example, we track "meantime to feed," looking at how many times a TamaGROTchi requests food and how long it takes for them to get a response. We have our red metrics, which are obviously really important.

To dive deeper into the data, Knowledge Graph gives us that high-level overview. We also created custom dashboards that allow us to see individual metrics and logs coming through. We can even dive into a single pet's dashboard. 

And I think no talk at GrafanaCON would be complete without a bit of AI in there. We've also given the Grafana assistant some capabilities. We've made some custom scenes where it understands what a TamaGROTchi is and knows that we need to keep it alive. He even gets pretty annoyed when you neglect him! 

**Chris:** Yeah, it really gives a new meaning to postmortem. [Chris laughs]

## Conclusion and Invitation

**Nick:** So, come by and see us at our booth at the science fair. You can also stop by the IoT booth for a chance to take one home via the NFC raffle. We want to show you how the dashboards work. It's a great learning tool, as Nick has already said. 

**Chris:** This is how I taught my mom what logs, traces, and metrics are! [Nick chuckles] 

**Nick:** So come by and play with them. They are sure to be a lot of fun. 

**Chris:** Any questions? We'll be down at the science fair, and we hope to see you there. 

**Nick:** Cool, thank you!  
**Crowd:** [Cheers]  
**Chris:** Thank you!

## Raw YouTube Transcript

- Hello GrafanaCON, I'm Chris. - And I'm Nick. - And we're here to
introduce you to TamaGROTchi. Now show of hands, who had
a Tamagotchi growing up? Who had a Tamagotchi that died growing up? Who had a Tamagotchi that died, and you don't know why it died. [Chris Chuckles] Yeah, that seems like most
people that had a Tamagotchi had the same problem. Well, TamaGROTchi is the new 2026 version, that is from us here at Grafana. Grot's our dinosaur mascot, now he can take him with
you and he talks to you. We've given him a cell phone
so when he gets hungry, he can even slack you. Grafana runs quarterly hackathons. We won this last hackathon
for the science fair. Most past winners have maybe
added something to the product. You've maybe heard of AI observability, or the Grafana assistant. Well, we decided to
make a cute little pet. TamaGROTch is built with an ESP 32 board and transmits logs, traces and metrics via hotel. Whether you're feeding
or playing with them, each interaction is sent as one of those. - Cool. So it's all fun and games, but actually a lot of our customers, they're not actually using Kubernetes, they can't use a Java SDK, they're actually building
observability onto small devices like this. So we have customers who have robots running around warehouses. They're building EPOS terminals. They're fairly hardware
restrained environments with limited memory. They might not have great
internet connections and they can't afford to be running things like the hotel collector or alloy, and a full SDK on those devices. So we kind of wanted to experiment and see how easy is it
just to send raw Otel data. So we're just creating a JS on packet, sending that over HTTP and sending that straight
to Grafana Cloud. Yeah. So the other thing that
we wanted to kind of do is our moms don't know
what we do at Grafana. So I'm an Observability Architect, I talk about observability all day. - I'm a data engineer, I deal
with data loading scripts. - Yeah, but this was the
only way we could actually tell our families what we do at Grafana. So when we were building
these, one of the things that we needed to decide
was what telemetry signals we were gonna use. So the trap is just
send everything as a log or just send everything as a metric, whatever you are used to. So we went down that route and we had our drop sick metric, and that was a zero or one, and we could quite easily
build a dashboard that counted how many sick TamaGROTchis we had, but we weren't then able to
answer other questions like, how did they get sick? Who let them get sick? So we actually started
implementing things like logs. So every button press that is a log. We've got tracing as well, and that let us build out a
much better suite of dashboards. So how do we get this
data? How do we observe it? So who here knows knowledge graph or entity graph? Perfect. So yeah, we have written a custom entity for Knowledge Graph. Usually this would be a
top down view of your, full application stack. So you'd see your
Kubernetes pods, your nodes, your application workers, et cetera. We just have TamaGROTchis, but we have SLOs that are
custom to our use case. So you can see things
like when they're hungry, when they're ill. Those are all custom built
into knowledge graph. Other things we've got, so
we've got tried and tested, sort of SRE conventions in place. So SLOs, we have meantime to feed. So we're, we're looking at
how many times TamaGROTchi is requesting to be fed and how long it takes for them to actually get responded to, and then we've got our
red metrics as well, which are obviously really important. So to dive deeper into the data. So Knowledge Graph gave us
that high level overview. We've also got a bunch of
custom dashboards that allow us to see the individual metrics, the logs that are coming through, and then we can dive into
a single pets dashboard, and I think no talk at
GrafanaCON would be complete without a bit of AI in there. So we've also given
the Grafana assistance, some capabilities, we've made some custom, custom scenes in there
where it understands what a TamaGROTchi is. It knows that we need to keep it alive, and actually he gets pretty
annoyed when you neglect him. - Yeah, and it really gives
a new name to postmortem. [Chris Laughs] Yeah, so come by and see us at our booth at the science fair. you can stop by the IoT
booth as well for a chance to take one home via the NFC raffle. We want to show you how
the dashboards work. It's a great learning tool,
as Nick has already said. So how I taught my mom what
logs, traces, and metrics are. [Nick Chuckles] Yeah, and come by and play with 'em. They're sure are a lot of fun. - Yeah, any questions? We're down at the science fair, I hope to see you guys there. Cool, thank you.
[Crowd Cheers] - Thank you.

