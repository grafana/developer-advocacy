# Alert fatigue, AI triage, and incidents: Lessons from observability experts at Cyera, PlayHQ &amp; NAB

Published on 2026-08-24T23:33:50Z

## Description

Observability looks perfect in a slide deck – in practice, it's messier. In this panel, engineering leaders from Cyara, PlayHQ, and ...

URL: https://www.youtube.com/watch?v=V8ID7STTO9g

## Summary

The community call titled "Alert fatigue, AI triage, and incidents: Lessons from observability experts at Cyera, PlayHQ & NAB" was held on August 24, 2026. The panel featured Dean, who manages partnerships at Grafana, and engineering leaders Brendon Ghumman from Cyara, Shak Tiwari from PlayHQ, and Dan from National Australia Bank. They discussed the challenges of implementing observability, including alert fatigue, data silos, and the importance of cultural shifts within organizations. Key takeaways included the value of leveraging Grafana's observability tools, the use of AI for root cause analysis, and the necessity of maintaining governance over telemetry data to manage costs effectively. 

Topics: observability, alert fatigue, AI triage, Grafana, OpenTelemetry, incident management, data governance.

## Chapters

00:00:00 Overcoming cultural challenges in observability adoption
00:07:04 Using AI to improve observability and reduce alert fatigue
00:14:12 Reducing data noise in observability
00:20:25 Using Grafana for effective incident resolution

Hi everyone. How are you going? I'm Dean. I run Grafana's partnerships across Australia and New Zealand. I'm joined today by a panel of our experts that I'll allow to introduce themselves. 

What we're going to focus on is that observability always looks picture perfect in your mind. We'll come in and tell you about what the world could be, everything tracing perfectly. But in reality, that's not always what happens. Sometimes it can be a bit disjointed, it requires a massive culture shift, and it can lead to unexpected cloud bills and other things that might pop up. We'll talk about some of the challenges, some of the ways that we got past them, and hear from people who are actually using it today. 

So I'll pass the mic along and let people do an intro, say where they're from, and share a little bit about themselves. I'd also like to make sure that you have a one-sentence icebreaker about the strangest thing you found in any of your telemetry data.

**Brendon Ghumman:** Thanks, Dean. Hello all. My name's Brendon Ghumman. I work for Cyara as a senior director. We're the leading CX assurance provider in the world. The key remit for my teams is around cloud architecture, cloud engineering, cloud security, and also AI in the cloud. The key work stream that binds all of this together is observability and monitoring. I'm happy to be here to share my experiences with all of you. 

The strangest thing that we found? Well, to give you a bit of background, we run thousands of servers in the cloud across the globe. While storage is cheap in the cloud, it adds up across thousands of servers. Soon after implementing Grafana, we got a single pane of glass that showed us not just what we provisioned in the cloud, but our utilization of disk across all of these thousands of servers. We saw that, okay, we had provisioned this much, but across the majority of the servers, we weren't really hitting the 80% limit. So when they say a picture's worth a thousand words, this picture was worth thousands of dollars to us. That was really important for me.

**Shak Tiwari:** Thanks. Hi everyone. I'm Shak Tiwari. I'm the CTO for PlayHQ. We are a community sports management platform. We work with national government bodies like AFL, Cricket Australia, and Basketball Australia to organize community games across the country. If you see kids playing on the weekend in the ovals, there's a one in two chance that it is organized on the PlayHQ platform. There are about 50,000 games being played every week in the country, and we help organize them. There are about a million participants that use our platform every week. We're running in four countries at the moment on AWS, operating north of 10,000 workloads with a very small platform team. So we rely heavily on Grafana's observability suite. It's unified for us and manages it end to end. Those are the experiences I'll share with you today. 

In terms of what we found in there, it happened before my time. I've only been here for a little bit. We serve about a billion plus requests every month, and one of the changes made it through with the entire request being logged into our logs. As usual, a big bill came out of it, but it was a learning we took away pretty quickly.

**Dan:** Thanks, Jay. I'm Dan from National Australia Bank. I'm one of the engineering managers. I look after the observability platforms, the design aspects around it, and the operation side of it. We manage, as a central platform, all of the network loads and how they monitor. There are so many microservices and a lot of data, on-premise, cloud, everything there. It's very critical applications, everything. We look after them as a central team. 

One key highlight would be that, as a bank, there's a lot of data everywhere, data silos, and many tools. One of the key things we are after is a central single pane of glass and everything in an easily manageable way. That's one of the big aspects that we use Grafana.

Cool. Thank you for that. Perfect segue as well because we all just heard about some great challenges that they're facing and some unexpected things. Everyone loves buying observability tools; we wouldn't be here if we didn't. My question is, after you've purchased it, obviously the hardest thing is making sure that as a culture you're adopting and getting quality data. How do you approach that challenge, and what have you seen that has worked for you in the past?

**Brendon:** Go for it. 

Okay, look, this question was answered previously by Adam for me. We went through the same sort of cultural challenges we had in the organization with having a previous tool that people were used to and getting them across to using a tool that is more open, one that people don't have to learn custom skills for. When new people come in, it's easy to onboard them. So getting people across that journey was important, getting leaders from various engineering teams to buy into that. 

We also opened it up to the various teams on what they felt was the right tool to use. Grafana was in the mix along with Datadog, New Relic, and a few others. Eventually, the majority landed on Grafana. Now, that meant that a few others who weren't part of the majority had to be brought across the journey as well. We gave them analogies like, "Hey, you're driving an Audi; we're asking you to drive a Merck. Now the dashboards might be different here and there, but soon you'll get used to it." 

There was a very small minority for whom the challenge was the way they were writing logs, which was in a very custom format, not the JSON format used by Grafana. We had to do some training for them, but also the logs were very verbose, and Grafana is limited to 5,000 lines at a time. We had to build in a hybrid approach for them to say, okay, most of your use cases will be done within Grafana, but for those 5 or 10% where you need those verbose logs, we'll keep them in S3. Anytime you need them, the SRE or NOC teams can pass those logs on to you. So yeah, that was my experience.

For us, we've been with Grafana for about three years, so we are quite into the journey of moving on from Datadog and so forth. However, whoever has worked with Grafana would have noticed that PromQL is not the easiest way to work inside Grafana. So that option challenge has always been how do you bring new engineers on board and get them comfortable with the new query language and new way of accessing information. 

What's really changed, I would say, in the last sort of six to nine months is the use of an AI-assisted way to actually go ahead and access all this information. If I look at how our engineers are using it now, they come in and look at these dashboards later, but they will probably be in their code console asking questions there. We use MCPs and interrogate logs and so forth. It does a better job in terms of looking at all the data sources coming through. That option is a lot easier now because people don't really care as to where the data lives or how it looks. They just talk in natural language, and you get the answers back to them.

For us, I think we're still on the journey pretty much. We do have a lot of tools, but one of the big reasons we are going with Grafana is that we're trying to adopt. There is a term called "olden days observability" and "modern era observability." We're trying to get into that modern-day observability pretty much. Back in the day, it was all about monitoring, like certain golden signals and all these things. But now we are going into that journey of adopting OpenTelemetry and then going to that uplift path. So for that journey, Grafana really helps us in getting to that target.

standardizations, that governance bit in previous slides as well that you guys have seen. We're trying to do that governance using the observability, OpenTelemetry standards at this stage. That's the whole journey that we're trying to get in with Grafana. Rather than cutting down all these data silos and then silo work and then different toolings, et cetera. With that proper adoption of these governance, we're trying to achieve that single pane of glass and with the proper standard across the board in observability. That's what we do.

Awesome. So yeah, sounds like a big part of it is just bringing together all the data sources and also making sure that you leverage kind of the AI Assistant to break down the language barrier of PromQL. So I guess that opens the next question. Happy for anyone to jump on this one. It's a bit pointed, but when people start using the product more, obviously that leads to a rise in telemetry coming into the environment. How do you deal with the costs there and what's your strategy to make sure that it's sustainable moving forward? 

And secondary to that, with more telemetry comes more events and alerts. How do you deal with the alert fatigue that people might get there? 

Yeah. The first one's really easy. Adaptive Telemetry is the answer. The good thing is that, like Jim was saying before, it doesn't cut metrics for you to give you suggestions. It's up to you as a team to review that and stop what you don't need. Alert fatigue is real. As we bring in more logs, more metrics, as a product matures, as we do M&As, as more product lines are built, more features are built. Initially, yes, teams add more and more alerts. And over time, the teams that are first handling those alerts, they do get white noise coming through as well. 

The strategy that we've adopted to reduce alert noise is to say, okay, every alert that we have is now going to have a runbook behind it, whether it's manual, whether it's automated, or a hybrid approach. The other thing we've done is bring our runbooks from Confluence into Grafana itself. We're using the skills feature in Grafana now. So every time we come across an event or an incident, we ask the SRE and NOC teams to say, go and update the skills area to say, okay, this was a problem statement. The customer was trying to do X, Y, and Z, and they were blocked at this point. What did you do to resolve it? So the next time a similar thing happens, someone can put a question in the AI Assistant and it'll tell the person exactly what to do. 

So yeah, the key to reduce alert fatigue for us has been to review your alerts on a quarterly basis. Drop alerts that you cannot assign a runbook to as well and automate as much as you can. Our strategy is very similar to what Brendon just put forward in terms of having some governance and rules and being ruthless about having runbooks allocated to alerts. 

We have a bit of a meta approach to alerts in the sense that we alert on alerts. In the sense that we have a bot that's operating, that's looking at the alerts that are coming through. It's looking at repetition. It's looking at whether something needs to be done about these things. Do we need to tweak the thresholds? Or do we need to get rid of them? Or is the SRE engineer actually responding appropriately to these alerts coming through? And so for me, that is like a meta monitoring on the alerts themselves. And that's what we use to try and keep the alerts to a minimum within our teams. 

The other thing that we have done is, before Grafana's kind of product took off on AI observability and so forth, we built our own bot. And that bot's actually integrated with our code base as well. It has our own context. So when the alert comes in, similar to Adam's experience, while the SRE gets on board and starts to triage it, the bot's already gone in. It's going to look at the deployments, the logs, the metrics, and then actually code as well and has a hypothesis on where it's coming from. So it makes life a lot easier. 

From a fatigue perspective, you're reducing the amount of effort that the on-call needs to be across. Again, we have a very small team, 150 plus odd services. So the surface area is way too big for the people to be across. Another learning we had while working on this was that we had to give the bot a bit of memory. Again, context. Like everything else, the business context is changing all the time. How can we quickly, based on the alert coming through the triage and on the bot, give it further context at that point in time so the next time it's triaging it, it has that context? 

For example, we know that at a certain point in time, EKS decides to rotate out the master nodes and we can tell the bot, "Hey, don't wake us up for this event happening in Canada at this hour at two o'clock in the night," as an example. For us, actually, the journey is more resonant with what Adam was explaining about their journey. So it's more around the issue that we had, which is a lot of noise, data noise. There are many data noise. 

So the first thing we are trying to do is the governance part of it. Make it stricter. For example, in the OpenTelemetry world, you have something called semantic models. So we are trying to use heavily those semantic models to govern the data at the collection layer itself and then trying to cut down on more of the noise data. We're using the Alloy Agent pretty much. The Alloy Agent is a really good capability. It has a lot of configurations that we can do for data, like reducing that noise and filtering part, et cetera. 

And then that sort of mechanism we're trying to implement. The inbuilt capabilities within Grafana, we're trying to use that to cut down on a lot of data noise. So ultimately, we're going to end up with less cost pretty much because low data means less cost. So we're trying to go in that journey pretty much. I can really resonate with Adam's journey that they have gone through. 

So it's pretty simple. A lot of challenges we are also facing, cultural challenges and all these things. Yes, we all do. 

Yeah. Thanks for sharing some of the difficulties you've managed to get past. It shows everyone it's not just shiny dashboards and we all have our moment in the sun. But yeah, moving on to the next part, wanting to make sure that we kind of look at what we've just looked at there. Have you had any moments where you've had a big win where all of the pieces that you've put together at the moment have saved you time? 

So there's been an incident that's happened. It would usually take you, prior to having Grafana, maybe hours, days, so forth to diagnose and recover from the issue where you've been able to pinpoint it and recover faster because of Grafana? 

So standard monitoring, normally what happens when an issue comes, incident, maybe most of you have gone through this process. When an incident comes, everyone just comes into a bridge. Everyone just jumps into the bridge. Everyone just passing the fingers, finger-pointing, et cetera. So the main problem is can't find the root cause where it happens. 

So one good thing that we have by adopting the OpenTelemetry built in with Grafana, what we're trying to achieve is, and what we have achieved is with that tracing capability that's really critical and that's really needed. Because what traces do is, for example, from a banking perspective, all you have like banking applications when you log into something, that's where the interaction starts, the service context starts. And then so many things, backend systems, so many things can break. 

So that tracer gives us where it really fails. And that really saved a lot of the efforts and time when it comes to the MTTR, the mean time to recover part and the meantime to discover part pretty much. So that's one of the big things that we have gone through. 

Yeah. I'll probably share another recent incident that happened. So most of the...

User of our platform is on the weekend, and the weekend is when on-call is on call and everybody else is not there. We had one of our core databases spike. We detected the spike and the utilization of resources pretty quickly. On-call got paged, and by the time they came online and started to look into it, our agent had looked at the Grafana logs, triaged it to a query that was actually consuming the database resources, traced it back to a recent change, and then figured out, "Hey, it's missing an index that should have been there." 

I think it took another 20 minutes for us to add the index back in, and then we recovered the database within 30 minutes. So, yeah. Awesome. 

I have multiple similar stories to share, but I'll share something completely different. We had this customer that was working with three different vendors on an integration project and testing across all three. They came to us and said, "We're sending you these requests on a 15-minute interval for these integration points, 10 minutes here and eight minutes there. You don't always respond to us in time, and that's causing issues upstream." 

So, okay, how do we prove that you guys are not sending everything on the right interval? The quickest and easiest win for us there was, firstly, to ask, "Hey, can we jump on a call with you guys and your other vendors to diagnose this together?" The answer was, "No. Just no, that's it. We don't have time for you guys. Fix your problem. We've told you there's a problem." 

It's like, "Okay, what do we do?" We looked at edge logs in Grafana. All the AWS edge logs get ingested into Grafana as well. We just looked at the logs coming in from this customer and plotted it on a time series. We said, "Okay, generally the interval is 15 minutes for this, but here's a gap here. For this other integration, yeah, they say it's eight minutes, but look, during the day we can see all of these gaps." 

So we were quickly able to build those pictures. And again, going back to the analogy before about a picture being worth a thousand words, this time literally it was. We were able to share multiple pictures with them and say, "Look, this is where all the gaps are. So what are upstream vendors supposed to be sending us as API requests at those 15-minute intervals? They're not on these times, so you need to go talk to them." 

Our customer took that picture, spoke to those vendors, and we were off the hook. Awesome. 

It sounds like the thing that solved your problems pretty consistently is having an open and consolidated view across all your different products, having some decent tracing in place so you can understand where the problem's happening, and just making sure everyone's looking at the same data. Some good lessons to take away there. 

Mindful of time, we're going to smash through the next two, but they're more fun questions, I promise. The first one being, in a couple of sentences, with all of the changes in what Grafana's doing and what the industry is doing around AI-driven root cause analysis and other emerging trends like continuous profiling, where do you feel that? What capability out of the emerging products is one that you're actively testing or interested in? 

Something that I mentioned before is getting all the runbooks from Confluence into Grafana and having that context for the Grafana AI to be able to help us get to the root cause quicker. From there, being able to build automation on top of those runbooks is something that I'm really excited about. 

For us, we have a slightly different take at the moment. We are actually looking at how, as we do more and more agentic development in the SDLC, I'm not sure what others are experiencing, but we are also experiencing increased defect rates and increased incidents happening in production as well. So our focus is to get the Grafana metrics and alerts integrated into the SDLC. 

When the engineers or the agents are actually working on a task, it clearly defines what healthy looks like for that specific change going in at a granular level. When it gets deployed, the alerts and metrics get deployed along with that within the SDLC. It's a bit of an experiment; we don't know where it's going to go, but we are collaborating with Grafana at the moment on making it part of the agentic SDLC within the business. 

Actually, to point to Shak's point, we are also going through similar activities. We are very tightly following a lot of SRE principles within the development space. We're really trying to make developers' lives easier every time. That's the main thing. Observability should come from the developer's end, so that's where we can resolve issues. We're trying to integrate with all the SRE principles and CI/CD pipelines, everything that the developers do. Observability is built in, and we are starting the journey from there itself. We're not done yet, but that's one of the big things we are trying to do right now. 

Thank you for that. 

Final question for everyone: for any engineering managers that might be in the room exploring observability or expanding what they're doing in the space, what would be your one takeaway or biggest learning from your experience that you could share with the team? 

I can say, don't stop. Just do whatever you're doing because observability keeps changing. Something you had yesterday keeps changing. Today is something different. It's like if you are into AWS, AWS services keep changing, right? So the same way, observability keeps changing. The biggest challenge is the culture changes, etc., the adoption of things. There are a lot of hurdles, but don't stop. 

I'm going to say get a copy of Adam's presentation and just see which part of the journey you are on and follow it because our learnings are very similar to Adam's, and I think he presented it quite well. 

Yeah, plus one to that. Please review Adam's presentation. But also, I'll add onto that and say, think of two personas: think of your customer and think of yourself. You want your customer to have a great experience out of your product, and you want to be able to sleep at night. So peacefully, I must say. Keep those two things in mind and then go watch Adam's presentation. 

Okay, thank you all for your time. I just want to recap a few of the trends that we heard throughout the presentation. It sounds like with a lot of the challenges that you face, the approaches that you've taken have been quite similar, which is just extending visibility, bringing everyone along on the journey, maybe finding some compromises for teams that can't do things in the exact same way that they would like to. 

Then leveraging things like workflows or runbooks for incidents to streamline your processes, leveraging Adaptive Telemetry to make sure your bills don't get out of control, and also leveraging the AI Assistant to make that onboarding process a bit more seamless for those people who may not be able to learn PromQL at the drop of a hat. 

It's been great to hear from you all. I hope everyone here has learned something because I definitely have. If you have any questions or you'd like to talk to any of us afterward, I'm sure we'll all be wandering around. I spoke to Frankie earlier. If this has triggered any light bulb moments where you'd like to understand what your observability maturity is, find some of us. We can easily direct you in the right approach there, and we can start having a conversation about how we can set you on a similar journey. 

Thank you all.

## Raw YouTube Transcript

Hi everyone. How you going? I'm Dean. I run Grafana's partnerships
across Australia and New Zealand. And I'm joined today by a panel
of our experts that I'll allow to introduce themselves. But what we're going to be
focused on is observability is always picture perfect in
your mind. We'll come in, we'll tell you about what the world
could be, everything tracing perfectly. But in reality, that's
not always what happens. Sometimes it jumps
between a bit disjointed, it requires a massive culture shift, can lead to unexpected cloud bills
and other things that might pop up. And so we'll talk about
some of the challenges, some of the ways that we got past them
and hear from people who are actually using it today. So I'll pass the mic along and I'll let
people do an intro and say where they're from, a little bit about themselves. And I'd also like to make sure
that you just have a one sentence icebreaker of the strangest thing
you found in any of your telemetry data. Thanks Dean. Hello all.
My name's Brendon Ghumman. I work for Cyara as a senior
director. We're the leading CX assurance provider in the world. So the key remit for my teams
is around cloud architecture, cloud engineering, cloud security,
and also AI in the cloud. The key work stream that binds all
of this together is observability and monitoring. And I'm happy to be here to
share my experiences with all of you. The strangest thing that we found,
well, to give you a bit of a background, we run thousands of servers
in the cloud across the globe. And whilst the storage
is cheap in the cloud, it adds up across thousands of servers.
So soon after implementing Grafana, we got a single pane of glass that showed
us not just what we provision in the cloud, but our utilization of disk across all
of these thousands of servers. And we saw that, okay, we'd provision this much.
But across majority of the servers, we weren't really hitting the 80% limit. So when they say a picture's
worth a thousand words, this picture was worth
thousands of dollars to us. So that was really important for me. Shak. Thanks. Hi everyone. I'm Shak Tiwari. I'm the CTO for PlayHQ. We are a community sports
management platform. So we work with national government
bodies like AFL, Cricket Australia, Basketball Australia to
organize community games across the country. So if you see kids
playing on the weekend in the ovals, there's one in two chance that is
organized on the PlayHQ platform. There's about 50,000 games that
are being played every week in the country. We help them organize them. There's about a million participants
that use our platform every week. We're run in four countries
at the moment on AWS, operates north of 10,000
workloads with a very small platform team. So we rely heavily on
Grafana's observability suite. It's unified for
us, manages it end to end. And those are the experiences
I'll share with you guys today. In terms of what we found in there, it happened before my time. So I've
only been here for a little bit of time. So we serve about a
billion plus requests every month. And one of the changes made
it through with the entire request coming through and being
logged into our logs. So as usual, a big bill that came out of it, but it was a learning we
took away pretty quickly. Thanks Jay. I'm Dan. I'm from National Australia
Bank representing. So I'm one of the engineering managers. I look after the observability platforms, the designing aspects around it
and the operation side of it. And we look after, as a
central platform, all of the networkloads and how do they monitor? There are so many microservices and
a lot of data, on-premise, cloud, everything there. It's very
critical applications, everything. So we look after them as a central team. The one key thing, the
highlight would be like, as a bank, there's a
lot of data everywhere, data silos and everything. And
a lot of tools are there. So one of the key thing which we are after
is the central single pane of glass and everything in an easily manageable way. So that's one of the big
aspects that we use Grafana. Cool. Thank you for that. Perfect segue as well because we all just
heard about some great challenges that they're facing and some unexpected things. Everyone loves buying observability
tools. We wouldn't be here if we didn't. My question is, after you've purchased it, obviously the hardest thing is making
sure that as a culture you're adopting and you're getting quality data. How do you approach that challenge and
what have you seen that has worked for you in the past? Go for it. Okay. Look, this question was
answered previously by Adam for me. So we went to the same sort of cultural
challenges we had in the organization with having a previous tool that people
were used to and them getting them across using a tool that is more
open that people don't have to learn custom skills for. And when new people
come in, it's easy to onboard them. So getting people across
that journey was important, getting leaders from various
engineering teams to buy into that. We also opened up to the various
teams on what they felt was the right tool to use. So we had Grafana
was in the mix. It was Datadog, New Relic and a few others. And
eventually the majority landed on Grafana. Now that means that a few others
that weren't part of the majority, we had to bring them across the journey
as well and give them analogies like, "Hey, you're driving an Audi, we're asking you to drive a Merck.
Now the dashboards might be different here and there, but soon you'll get used to it." And
then there was the very little minority that the challenge for them was
the way that they were writing logs was again in a very custom format,
not the JSON format used by Grafana. So we had to do some training for them, but also the logs are very verbose and
Grafana is limited to 5,000 lines at a time. We had to build in a hybrid
approach for them to say, okay, most of your use cases will
be done within Grafana, but for those 5 or 10% where you need
those verbose logs, we'll keep them in S3. And anytime you need them, the SRE or
NOC teams can pass those logs on to you. So yeah, that was my experience. For us, we've been with
Grafana for about three years, so we are quite into the journey of
moving on from Datadog and so forth. However, whoever has worked with Grafana, you would have noticed that PromQL
is not the easiest way to work inside Grafana. So that option challenge has always been
how do you bring new engineers on board and they get comfortable
with the new query language, new way of accessing information
and so forth. What's really changed, I would say, in last sort of six to nine months
is the use of sort of AI assisted way to actually go ahead and
access all this information. So if I was to look at now how
our engineers are using it, I would say that they would come in
and look at these dashboards later, but they will probably be in their Claude
Code console and they'll be asking for questions in there. And we'll be using
MCPs and interrogating logs and so forth. Actually it does a better job in terms
of looking at all the data sources that are coming through. So that option is a lot easier now because
people don't really care as to where the data lives or how it looks. They just talk in natural language
and you get the answers back to them. For us, I think we're still
in the journey pretty much. We do have a lot of tools, but one of the big reasons that we
are going with Grafana is we're trying to adopt. So there is a term called like olden
days observability and the modern era observability. So we're trying to get into that
modern day observability pretty much. Back in the day, it's
all about monitoring. Monitorings like certain golden
signals and all these things. But now we are going into
that journey of adopting OpenTelemetry and then going
to that uplift path. So for that journey, actually Grafana really helps us
into getting into that target. So it's more around, I
would say standardizations, that governance bit in previous slides
as well that you guys have seen. We're trying to do that governance
using the observability, OpenTelemetry standards at this stage. That's the whole journey that we're
trying to get in with Grafana. Rather than cutting down all
these data silos and then silo work and then different
toolings, et cetera. With that proper adoption
of these governance, we're trying to achieve that single pane
of glass and with the proper standard across the board in
observability. That's what we do. Awesome. So yeah, sounds like a big part of it is just
bringing together all the data sources and also making sure that you leverage kind
of the AI Assistant to break down the language barrier of PromQL. So I guess that opens the next question. Happy for anyone to jump on
this one. It's a bit pointed, but when people start
using the product more, obviously that leads to a rise in
telemetry coming into the environment. How do you deal with the costs there and
what's your strategy to make sure that it's sustainable moving
forward? And secondary to that, with more telemetry comes
more events and alerts. How do you deal with the alert
fatigue that people might get there? Yeah. The first one's really easy.
Adaptive Telemetry is the answer. The good thing is that
like Jim was saying before, it doesn't cut metrics for
you to give you suggestions. It's up to you as a team to review
that and stop what you don't need. Alert fatigue is real. As we bring in more logs, more
metrics, as a product matures, as we do M&As, as more product lines
are built, more features are built. Initially, yes, teams add more
and more alerts. And over time, the teams that are first
handling those alerts, they do get white noise
coming through as well. The strategy that we've adopted to
reduce alert noise is to say, okay, every alert that we have is now
going to have a runbook behind it, whether it's manual, whether it's
automated or a hybrid approach. The other thing we've done is bring
our runbooks from Confluence into Grafana itself. We're using the
skills feature in Grafana now. So every time we come across
an event or an incident, we ask the SRE and NOC teams to say,
go and update the skills area to say, okay, this was a problem statement. The
customer was trying to do X, Y, and Z, and they were blocked at this point.
What did you do to resolve it? So the next time similar thing happens, someone can put a question
in the AI Assistant and
it'll tell the person exactly what to do. So yeah, the key to reduce alert fatigue for
us has been review your alerts on a quarterly basis. Drop alerts that you cannot
assign a runbook to as well and automate as much as you can. Our strategy is very similar to what
Brendon just put forward in terms of having some governance and rules and be
ruthless about having runbooks allocated to alerts. We have a bit of a meta approach to
alerts in the sense that we alert on alerts. In the sense that
we have a bot that's operating, that's looking at the alerts
that are coming through. It's looking at repetition. It's looking at that something
needs to be done about these things. Do we need to tweak the thresholds?
Or do we need to get rid of them? Or is the SRE engineer actually
responding appropriately to these alerts coming
through? And so for me, that is like a meta monitoring
on the alerts themselves. And that's what we use to try and keep
the alerts to a minimum within our teams. The other thing that we have done is
before the Grafana's kind of product took off on AI observability and so forth, we built our own bot. And that bot's
actually integrated with our code base as well. It has our own context.
So when the alert comes in, similar to Adam's experience
that while the SRE gets on board, starts to triage it, the
bot's already gone in, they're going to look at the deployments,
they're going to look at the logs, the metrics, and then actually code as well and has
a hypothesis on where it's coming from. So it makes the life a lot easier.
So from a fatigue perspective, you're reducing the amount of effort
that the on-call needs to be across. Again, we have a very small
team, 150 plus odd services. So the surface area is way too
big for the people to be across. Another learning we had while working on
this was that we had it to give the bot a bit of memory. Again,
context. Like everything else, the business context is changing
all the time. How can we quickly, based on the alert coming through
the triage and on the bot, give it further context at that point in
time so the next time it's triaging it, it has that context. So for example, we
know that at a certain point in time, EKS decides to rotate out the master
nodes and we can tell the bot, "Hey, don't wake us up for this event happening
in Canada at this hour at two o'clock in the night as an example". For us actually, the journey is more resonate with
previously Adam was explaining all their journey. So it's more around the issue that we had is a
lot of noise, data noise. There are many of the data noise. So the first thing which
we are trying to do is the governance part of it.
Make it more stricter on. For an example, in OpenTelemetry world, you have something called semantic models. So we are trying to use heavily on those
semantic models to govern the data at the collection layer itself. And then trying to cut down
that more of the noise data. And then we're using
alloy agent pretty much. Alloy agent is a really good capability. It has a lot of configurations
that we can do data like reducing that noise and
filtering part, et cetera. And then that sort of
mechanisms we're trying to. The inbuild capabilities within Grafana, we're trying to use that to cut
down that lot of data noises. So ultimately we're going to end
up with less cost pretty much because low data means less cost. So we're trying to go in
that journey pretty much. I can really resonate with Adam's
journey that they have gone through. So it's pretty simple. A lot of
challenges we are also facing, cultural challenges and all
these things. Yes, we all do. Yeah. Thanks for sharing some of the
difficulties you've managed to get past. It shows everyone it's not just shiny
dashboards and we all have our moment in the sun. But yeah, moving
on to the next part, wanting to make sure that we kind of
look at what we've just looked at there. Have you had any moments where you've had
a big win where all of the pieces that you've put together at the
moment have saved you time? So there's been an
incident that's happened. It'd usually take you prior to
having Grafana, maybe hours, days, so forth to diagnose and recover from
the issue where you've been able to pinpoint it and recover
faster because of Grafana? So standard monitoring, normally what
happens when an issue comes incident, maybe most of you have gone through
this process. When incident comes, everyone just come into a bridge.
Everyone just jump into bridge. Everyone just passing the fingers,
finger pointing, et cetera. So the main problem is can't find
the root cause where it happens. So one good thing that we have by adopting the OpenTelemetry
built in with Grafana, what we're trying to achieve is, and what we have achieved is with
that tracing capability that's really critical and that's really
needed. Because what traces does is, for an example, from banking perspective, all you have like banking applications
when you log into something, that's where the, when
you click on something, that's where the interaction
starts, the service context starts. And then so many things, backend
systems, so many things can break. So that tracers gives us
where it really fails. And that really saved a
lot of the efforts and time when it comes to the MTTR, the mean time to recover part and the
meantime to discover part pretty much. So that's one of the big thing
that we have gone through. Yeah. I'll probably share another recent incidents that happened. So most of the user of our platform is on
the weekend and the weekend is where on-call is on call and
everybody else is not there. And we had one of our
core databases spike. We detected the spike and the
utilization resources pretty quickly. On-call got paged by the time they
came online, started to look into it. Our agent had looked at the Grafana
logs, triaged it to a query, actually consuming the database resources,
traced it back to the recent change, and then figured out, hey, it's missing
an index that should have been in there. I think it took another 20 minutes for
us to add the index back in and then we recovered the database
within 30 minutes. So yeah. Yeah. Awesome. Yeah. So I have multiple
similar stories to share, but I'll share something
completely different. We had this customer that was working
with three different vendors on an integration project and testing across
all three. And they came to us and said, "We're sending you these requests on a
15 minute interval for these integration points, 10 minutes here
and eight minutes there. You don't always respond to us in time
and that's causing issues up the stream. So okay, how do we prove that now you guys are
not sending everything on the right interval?" So the quickest and
easiest win for us there was, well, firstly to ask, "Hey, can we jump on a call with you guys
and your other vendors to diagnose this together?" And the answer
was, "No. Just no, that's it. We don't have time for you
guys. Fix your problem. We've told you there's a
problem." It's like, "Okay, what do we do?
Look at edge logs in Grafana. All the AWS edge logs get
ingested into Grafana as well. Just look at the logs coming in
from this customer and plot it on a time series and say, okay, generally
the interval is 15 minutes for this, but here's a gap here. For
this other integration, yeah they say it's
eight minutes, but look, during the day we can
see all of these gaps. So we were quickly able to
build those pictures. And again, going back to the analogy before about
a picture being worth a thousand words, this time literally it was. We were able to share multiple
pictures with them and say, look, this is where all the gaps are. So what are upstream vendors supposed to
be sending us as API requests at those 15 minute intervals?
They're not on these times. So you need to go talk to them.
And yeah, our customer took that picture, spoke to those vendors,
and we were off the hook. Awesome. So it sounds like the thing that solved
your problems pretty consistently is having an open and consolidated
view across all your different products, having some decent tracing in place so
you can understand where the problem's happening and just making sure
everyone's looking at the same data. Some good lessons to take
away there. Mindful of time. We're going to smash through the next
two, but they're more fun questions, I promise. The first one being
in a couple of sentences, with all of the changes in what Grafana's
doing and what the industry is doing around AI driven root cause analysis and
other emerging trends like continuous profiling and things like
that, where do you feel that. What capability out of the
emerging products is one
that you're actively testing or interested in? Yeah. Something that I mentioned before is
getting all the runbooks from Confluence into Grafana and having that context
for the Grafana AI to be able to help us get to the root cause quicker. And from there being able to build
automation on top of those runbooks. That's something that
I'm really excited about. Cool. For us, we have a slightly different take at the
moment. We are actually looking at how, as we do more and more agentic
development in the SDLC, I'm not sure what others are experiencing, but we are also experiencing
increased defect rates, increased incidents happening
in production as well. So our focus is to get the Grafana
metrics and alerts integrated into the SDLC. So when the
engineers are actually, or the agents are actually
working on a task, it clearly defines what Healthy looks
like for that specific change going in at a granular level. And then when
it gets deployed, the alerts, the metrics get deployed along
with that within the SDLC. It's a bit of an experiment. We
don't know where it's going to go, but we are collaborating with Grafana
at the moment on making it part of the Agentic SDLC within the business. Actually, point to Shak's point actually, we also going through
the similar activities. We very tightly following a
lot of SRE principles within the development space.
So we're really trying to make developers' lives easy every
time. That's the main thing. Observability should comes
from the developer's end. So that's where we can resolve issues. So we're trying to integrate with
all the SRE principles and CI/CD pipelines, everything
what the developers do. And then observability built in and
start the journey from there itself. So we really going through that
journey. We're not done yet, but that's one of the big thing
we should try doing right now. Yeah. Thank you for that. And
final question for everyone. For any engineering managers that might
be in the room that might be exploring observability or expanding what
they're doing in the space, what would be your one kind of
takeaway or biggest learning from your experience that you could
share with the team? I can say don't stop. Just do whatever you're doing
because observability keeps changing. Something you had yesterday is keep
changing. Today is something different. It's like if you are into AWS like
AWS services keep changing, right? So same way. Observability keep changing. And then the biggest challenge is
the culture changes, et cetera, the adoption of things. So there's
a lot of hurdles, but don't stop. I'm going to say get a copy of Adam's presentation and just see which part on the journey you are
and follow it because our learnings are very similar to Adam's. And I
think he presented it quite well. Yeah, plus one to that. Please
review Adam's presentation. But also I'll add onto that
and say, think of two personas. Think of your customer
and think of yourself. You want your customer getting a great
experience out of your product and you want to be able to sleep at
night. So peacefully, I must say. Keep those two things in mind and
then go watch Adam's presentation. Okay. Thank you all for your time. I just want to recap a few of the
trends that we heard throughout the presentation. So it sounds like with
a lot of the challenge that you face, the approaches that you've
taken have been quite similar, which is just extending visibility,
bringing everyone along on the journey, maybe finding some compromises for teams
that can't do things in the exact same way that they would like to. And then leveraging things like workflows
or run books and things like that for incidents to streamline your processes. Leveraging Adaptive Telemetry to make
sure your bills don't get out of control. And also leveraging the AI Assistant to
make that onboarding process a bit more seamless for those people who may not
be able to learn PromQL at the drop of a hat. Yeah, it's been great
to hear from you all. I hope everyone here has learned
something because I definitely have. And if you have any questions or you'd
like to talk to any of us afterward, I'm sure we'll all be wandering
around. And I spoke to Frankie earlier. If this has triggered any
light bulb moments where
you'd like to understand what your observability maturity
is, find some of us. We can easily direct you in the right
approach there and we can start having a conversation about how we can set you
on a similar journey. Thank you all.

