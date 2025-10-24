# How IGS Scales IoT Observability for Vertical Farming with Grafana Cloud

Published on 2025-10-22T16:55:58Z

## Description

IGS (Intelligent Growth Solutions) runs industrial-scale vertical farms powered by IoT. Head of Platform Engineering, Owen Bower ...

URL: https://www.youtube.com/watch?v=fUygTe0PFVU

## Summary

In this video, Owen Bower Adams, Head of Platform Engineering at Intelligent Growth Solutions (IGS), discusses the challenges and advancements in observability within the context of vertical farming and industrial IoT. He introduces IGS as a provider of modular vertical farming systems and emphasizes the importance of observability in managing complex systems that include hundreds of crop-growing towers. Adams shares insights on their journey from using basic monitoring tools to adopting Grafana Cloud, highlighting the integration of various technologies to improve customer alerting, testing for scalability, and addressing intermittent connection issues. He underscores the significance of fostering a shared language among teams, enabling cross-departmental collaboration, and empowering customer support to utilize data effectively. The video concludes with reflections on the lessons learned and the incremental improvements that have heightened confidence in managing future projects.

## Chapters

00:00:00 Introductions and overview of the presentation  
00:02:15 Introduction to Owen Bower Adams and his role at IGS  
00:05:20 Overview of Intelligent Growth Solutions (IGS) and their vertical farming approach  
00:08:45 Explanation of the engineering teams and their diverse backgrounds  
00:12:30 Discussion of the architecture and observability journey at IGS  
00:17:10 Transition from Azure App Insights to Grafana Cloud for observability  
00:21:00 Challenges faced with scaling and customer support due to increased complexity  
00:25:00 Customer alerting implementation using Grafana  
00:30:00 Testing for scale and performance bottlenecks with Grafana Cloud  
00:35:00 Collaborative problem-solving and addressing intermittent connection drops  
00:40:00 Key takeaways on using tools and community support for future confidence and incremental improvements  

# Vertical Farming and Industrial IoT Observability

Oh, absolutely. It's very strange being up here seeing everyone, particularly as I'm aware this is kind of a dry title. So, I want to thank everyone for being here. I also need to pick up my clicker; otherwise, this is going to go very badly.

Today, I will be talking about vertical farming and industrial IoT, but to set the scene, a lot of what we're discussing revolves around universal observability problems. We have specific challenges when dealing with industrial IoT—it's just the nature of the business. However, the observability challenges are pretty universal, so hopefully, everyone will gain something from this discussion, even if not many people work in the industrial space.

## Introduction

Quick introduction to me: that's my face, in case you can't see it here. Same eyeliner, same hair—not much has changed. My name is Owen Bower Adams, and I'm the Head of Platform Engineering at IGS. Since I've been with IGS since quite early on, my role covers a lot of areas. I oversee the SE team, the S-Step function, some software engineers, as well as areas like IS and procurement. Anyone who's worked in startup or scale-up culture will appreciate that you end up wearing many hats.

I have over 20 years of experience—21, to be exact—but I like the way "over 20" sounds better. My journey with observability at IGS has been ongoing for quite some time.

## About IGS

Now, a quick introduction to the company: Intelligent Growth Solutions. I will consistently refer to it as IGS because it’s a bit of a mouthful. We are in the vertical farming business, but specifically, we are an infrastructure provider. We don't really grow crops outside of research and development; instead, we build and deploy modular factory systems for our customers. Some customers have four towers, while others have over 200. These towers stand nine to twelve meters tall and each has 50 to 70 snooker table-sized trays in them. This is the industrial-scale side of growing crops.

In this environment, we face some interesting challenges, which I'll discuss shortly. We have scaled out to various locations and have a very busy year ahead. This model is working successfully, but we do encounter customer outages, which is an important aspect to highlight.

## Engineering Teams

One of the unique aspects of working in this space is the number of people I work with who have engineering backgrounds but haven't really dealt with software before. We have the Platform Engineering side and below that, there’s IoT, which sits as a bridge between everything. There’s our User Apps team, which focuses on customer-facing products, as well as data teams. 

In addition, we have people working in R&D, HVAC engineers, and deployment engineers who build and commission our systems at customer sites. We also have customer support teams, some of whom come from field engineering backgrounds, while others have more software experience. 

A key point I want to emphasize during this discussion is how having a shared language has been invaluable in our efforts to build and roll out Grafana Cloud across the organization.

## Tooling and Architecture

Now, let's talk about tooling, architecture, and our observability journey. Our architecture covers the end-to-end process, which includes the physical site—HVACs, irrigation systems, lighting, and the PLC (Programmable Logic Controller). We also have edge devices that handle Wi-Fi access and gather various bits of sensor data.

When we speak about observability at IGS, we refer to nearly everything down to the PLCs, which expose data from our sensors throughout the environment. This involves large telemetry problems; for example, with 200 towers, we have about 16,000 trays and all that sensor data coming through.

I've included a diagram in the next slide, which I hope no one can read—otherwise, I’ll be in trouble. Despite its complexity, it represents a microservice architecture. The end user side is on the right, while field engineers and front-end developers work on the left. In the middle, we have various microservices, stateless applications running on Kubernetes, and state stored in databases. 

These observability problems are not new. As complex as it may seem, it likely resembles systems familiar to many in this room.

## Observability Journey

Our observability journey began on Azure App Insights when I joined, primarily because it was already available. We then had a brief stint with Grafana Open Source, which I genuinely enjoyed. However, considering the size of our team, I had to decide whether to build or buy a solution. We opted to buy because aligning our small team with tools that deliver business value was crucial.

We briefly used New Relic, which provided good experiences, but as we scaled, it became clear that it wasn't the right platform for us. About a year and a half to two years ago, we evaluated alternatives and ultimately chose Grafana Cloud. I’m pleased to say that today, we are 100% on Grafana Cloud without any lingering New Relic or other observability tools in place.

## Scaling and Challenges

As I mentioned earlier, our customer base is scaling significantly over the next year. This scale is not B2C; rather, we’re working with much more complex sites, which brings a host of challenges. 

For instance, downtime can have a uniquely high impact on our operations. If we have an outage, it may not be worse than others, but it can still affect crop yield and growth consistency, which are critical for our customers. Additionally, if operations back up on a factory floor, it can lead to delays in crop harvests going out.

We also faced various data silos and a lack of integration among our tools. While we had an observability solution, we didn’t have a comprehensive view across our systems, and our small team lacked the time to address this.

## Use Cases and Observability Solutions

Now, let's move on to some specific use cases where we've implemented solutions that deliver value. 

### Customer Alerting

First, let's discuss customer alerting. Creating alerts is challenging, especially when we need to customize them for our clients. For many of our customers, the ability to know if temperature thresholds are exceeded is essential.

We decided to use Grafana for the alerting part for our customers. Implementing a baseline of alerts through infrastructure as code allows customer support to create new alerts while ensuring that we maintain a consistent source of data. This has empowered customer support teams to manage alerts without requiring extensive software engineering assistance.

### Testing for Scale

Next, we have testing for scale. As we grow in complexity, we realized that our testing systems had gaps that wouldn’t scale with our increasing number of trays and event handling needs.

To address this, we leveraged the Grafana community and the tools available within Grafana Cloud. We can now use Grafana Cloud as our k6 runner for performance testing, which helps us identify performance bottlenecks quickly.

### Intermittent Connection Drops

Lastly, let's touch on intermittent connection drops. These can be quite complex to diagnose, especially when dealing with industrial protocols and physical PLCs. We encountered persistent issues affecting significant customers, which required collaboration across teams to resolve.

Thanks to our full-stack observability, we could create custom tools and tests that helped identify the root of the problem. This experience highlighted the value of having a shared language across teams, which sped up our resolution process.

## Conclusion and Future Confidence

In summary, we’ve learned some valuable lessons. Giving teams access to tools and data enables them to discover use cases you might not have expected. We now have more confidence in our upcoming projects, knowing we can reach out for support when needed.

As we continue to evolve our observability capabilities, we're focused on incremental changes rather than revolutionary shifts. Our approach to future projects will be flexible, allowing us to adapt to emerging challenges.

Thank you for your time, and I welcome any questions!

## Raw YouTube Transcript

Oh, absolutely. Very strange
being up here seeing everyone, particularly as I'm aware
this is kind of a dry title, so I want to thank everyone for being
here. I also need to pick up my clicker, otherwise this is going to go very badly. So I'm going to be talking
about vertical farming a little bit. I'm going to be talking
about industrial IOT a little bit, but actually to set the scene on this, a lot of what we're talking about
is universal observability problems. We have specific challenges when
we're dealing with industrial IOT. It's just the nature of the business, but those challenges are more around
the protocols which are being used. They're more around some of the
outages, which we can uncover. The observability challenges,
they're pretty universal, so hopefully everyone will
get something from this. I know not many people will be
working in the industrial space. Quick introduction to me, that's my face in
case you can't see it here. Same eyeliner, same hair. Not much has
changed. Owen Bower Adams, Head of Platform Engineering at IGS, but because I've been at IGS
since quite an early employee, my role covers quite a bit.
So there is the SE team, there's the S-Step function, there's
some Software Engineers who report to me. I also oversee some IS stuff, some
Procurement, a whole range of things. And I think anyone who's worked in
startup scale up culture will be able to appreciate that. You end
up with a lot of hats. So 20 plus years of experience, that's a grandiose way of saying
I've got 21 years of experience, but I like the way that
sounded a bit more. And yeah, the observability side of things is
something I've been on a journey with IGS for a while now.
Quick introduction to the company. So Intelligent Growth Solutions. I will consistently call it IGS
because it's a bit of a mouthful. We are in the vertical farming business, but specifically we are an
infrastructure provider, so we don't really grow crops
outside of research and development, which we engage with our customers. We instead have this modular factory
system which we build and deploy for customers. Some customers
have four towers. We're also working on customers
which have 200 plus towers, and these towers are
nine to 12 meters tall. Each one of those will have 50, 60, 70 snooker size table trays in them. So this is the industrial
scale side of growing crops. In this kind of environment, we're not
talking about things like in a kitchen, which we see some of the customers do. That gives us some really
interesting challenges as well, which I'll come onto in a little bit. There's a quick little bit more
about IGS here. So this is, we have customers, we have grown, we have scaled out to various locations.
We have a very, very busy year ahead, but this is something which works. This is a model which we are actually
deploying successfully and one where we do have customer outages, which I think
is a really important thing to stress. I wanted to quickly talk
about the Engineering teams. So one of the things which makes working
in this space a little bit different is a number of people which I work with
who have an engineering background, but haven't ever really
dealt with software before. We've got the Platform
Engineering side as I mentioned, and underneath software
in general, there's IOT, which sits on a bridge between
everything. There's the User Apps team, which is our kind of customer
facing products team. You have data, but then outside of that we have people
working in R&D. You have HVAC engineers, you have Deployment Engineers who are
actually the people who go out to customer sites and build this and
commission it and get it online. And then we also have Engineering
adjacent teams like Customer Support who, some of them might come from a
Field Engineering background, which is doing things on site. Some of them might come from
more of a software background. And a really important thing I'm hoping
to talk about during this is how having a shared language has really been
valuable for us as we've begun to build, roll out, Grafana Cloud
across the organization. I'm going to take a moment
to talk about tooling. I'm going to talk about our architecture
and then where we've been on the journey of observability. And then after that we're going to go
through a handful of use cases where I can talk about how this has kind of
empowered us. So our architecture, and this is significant in my view, kind of covers the end-to-end. So we have the physical site
itself and this is the HVACs, the irrigation system, the
lighting all the way up to the PLC, and that's Programmable Logic Controller,
if I remember the acronym correctly. We also have edge devices which handle
Wi-Fi access and pulling in various bits of sensor data. So we
have a physical site, but then we also have a SaaS product. And that SaaS product is where
customers will log in to define how they want to grow crops.
So they'll control their lighting cycles, they'll manage users,
they will view telemetry, go and peek at photos of crops growing. And that's a large part of what we
offer and that is the end-to-end. And when we talk about
observability in IGS, we are talking about pretty
much everything there
primarily down to the PLCs, but the PLCs are just exposing data
coming from the actual sensors which are instrumented throughout the environment. So this is large telemetry problems when
we're talking about 200 towers through a single site that is 16,000-ish trays, all of that sensor data coming
through, all of those lift moves. So this is our kind of architecture.
I've included a diagram on the next page, which I'm hoping no one can read,
otherwise I'm going to get into trouble. However, while that is
a little bit complex, I actually had a new hire
recently create this for me, which was I think his worst
form of punishment he could
have imagined. But it's a microservice architecture. We have the end user side on the
right and the field engineers, we have people coming from the front end. All of that in the middle is
largely just microservices. We have stateless applications
running on Kubernetes. We have state running in databases.
These are not new observability problems. Some of the data we put in is new,
but again, as complex as that is, it's probably something
which looks similar to most
of the people in this room. In fact, it's probably nowhere near as complex
as some of the people in the room. And that's something I really want to
stress when we start talking about how we've adopted Grafana Cloud and what
we're kind of getting out of it. So our observability journey to date, we started out on Azure
App Insights when I joined. I think that was largely just because
of the fact it was there. I think a few people have probably ended up using
whatever the cloud provider was offering when they start with that. We then had
a brief stint with Grafana Open Source, and I love Grafana Open Source. I've
got a lot of experience with it. But reality is at that point in our
journey, we had a very small team. We still have a relatively small team
and I had to make a decision on do we build or do we buy? And we went with buy
because when you've got a small team, kind of aligning them to things which
are delivering value to the business is incredibly important. And having them deal with the complexities
of managing scaling Prometheus for large amounts of telemetry data isn't
something which I could justify investing their time in. So we went
to New Relic for a bit. I'm not going to bad mouth New Relic,
like we had good experiences with it, but what we were finding was as we were
scaling and as we had certain challenges we were facing, it wasn't the right
platform for us. So about year and a half, maybe two years ago, we started doing an evaluation
of alternatives and we
ended up on Grafana Cloud. And I will say today we
are 100% on Grafana Cloud. We don't have any lingering New Relic or
any other observability tools in place. We are fully on it and
which we used most of it, which I think I'm touching on shortly.
I mentioned certain challenges. This isn't a migration story. There was a great migration
talk earlier from Andy. I highly recommend going
and having a listen to that. This isn't a migration story, but I do want to set some context of
where we were to where we are now. As I mentioned, our customer base is scaling significantly
over the next year and that kind of scale is not B2C, where we're talking
about a large volume of new users, we're talking about much more complex
sites and may come with a whole host of knock-on effects. It impacts customer
support, it impacts deployment, onboarding new towers is so much more
complex when you're delivering 20 per month compared to a couple
in a 6-month period. So that scale brings with it a lot
of problems which we need to address. We also face quite unique high impact
from downtime. Now everyone in this room, if you have an outage, it's a
significant problem. Ours is not worse, but it is slightly different. We say 200 towers we crops are pretty
resilient because it turns out mother nature is not the most
consistent of things out there. However you can impact yield, you can impact crop growth and
consistency is very key for our customers. So we need to be able to respond
to outages quickly. Also, when you have a factory floor, if you have an outage where you've got
people moving trays back and forth across the floor, if that goes
on for several hours, you can back up operations for weeks.
You can delay crop harvests going out as they need to reschedule things. So outages are quite high impact and
have quite high human cost for us when that happens. And there's
a couple of bits on here, which I'm not going to go into too much, but we have various data
silos which were in place. We have a lot of moving parts and
while we had a lot of tooling, none of it was really integrated because
while we had an observability solution, we didn't really have the wider
range of access to these tools and bringing it all into one place and the
integrations which we were seeking small team, we also didn't have
the time to address that. This is a very quick slide.
Information and metrics. None of this will be strange for
anyone here other than maybe O-P-C-U-A, which is an Industrial Control
Protocol, which we use. This is what our stack looks like.
We're using OTel, we're using logs, we have SNMP for networking,
we've got Cloud integrations. All of this stuff is pretty
standard and that's again important. We want something which makes
it easy for us to hire as well. We don't want people to be scared off by
the fact we're doing Industrial Control and this is where we are now. What we've actually gone onto Grafana
Cloud and the reasons for going on to Grafana Cloud was we looked at
this and we're kind of like, okay, there's a whole range of
tools we can use here. This is a whole ecosystem we can use and
we make use of pretty much every part of it. Not quite, but I'm
pretty sure we will be soon. And this has been a year and a bit
worth of adoption and a lot of this like k6 was tools we were already using. So that's where we're at today and this
is going beyond the metrics for us into the whole ecosystem. So
this is the bulk of a tool. I'm going to be going through three use
cases and examples of where we found this delivers value. I'm hoping people will find
something interesting about this. And a lot of this is where we've gone
beyond just simple metrics into other parts of a stack and where
that's paid off. First thing, Customer Alerting, alerting is hard. It's also really, really hard when you're trying to
customize alerts for customers, which is something we have to do. Some of our bigger customers will
integrate directly with the factory floor. However, for the vast majority
of our customers to date, they want the ability to
know if temperature has
gone outside of a threshold which they want to set. There's entire companies whose
whole job is dealing with alerting. So we didn't want to try and reinvent
the wheel because that's a lot of time which we would lose. So we had the challenge of needing to
bring in alerting and when we had a solution already, it was difficult
to manage. It was very manual. We had to do a lot of kind of clunky
onboarding when we were starting up with a new customer and we wanted to have clear
ownership for customer support to be able to manage this going forward, and we wanted more granular
notification policies. So the way we solve this, and this
is a quick screenshot from the UI. So we actually use Grafana
for the alerting part for
our customers. We have as all Data Explorer and we're using the
Enterprise plugins to just query that directly. We then have Customer
Support create new alerts, but we have a baseline of alerts we've
done through infrastructure as code and then we feed that back into
the system through Service Bus. So we just use an endpoint and we send
an HTTP request with a message payload in there and then that flows
back into the system. So the reason why I'm mentioning this is
that the end result is actually pretty cool for us. We have alerting, which
is using the same source of data, which is being seen by the customers
in the UI for their telemetry. We haven't exposed any
personal information into
Grafana for mobile phones for example, because that's all in our
system. It just feeds back into it. But the big thing is this is now fully
owned by Customer Support who haven't necessarily used these kinds of toolings
before. We've framed them up in a bit of Custo, we have some UI and I'm
now finding use cases for this, which I didn't know existed. So I am, the other day I found out that they've
created an integration with Power BI, which they're using to do some
stuff in Jira Service Management. Empowering them and giving that tooling
enabled them to solve problems which never came across a Software
Engineering desk rightly or wrongly, but I'm still glad that they did it. The next thing I want to talk
about is testing for scale. So I mentioned earlier that we
are growing in complexity and that's a great problem to have. I'm really glad we do and we had a lot
of bits and pieces for addressing this. But with larger customers coming
online, we did have a simulator, we did have k6 in place. We
did have a Test Cube in place, but we knew we had gaps in our system, which wouldn't scale because we're not
just talking about the number of trays, we're talking about the event handling
loop for scheduling control logic, various bits across the databases.
There's a whole host of things here which have to go right for us to be able
to execute jobs at a large scale, including Wi-Fi. Like Wi-Fi
contention is an issue which we face. So we had these challenges and we
had a reasonably short timeframe to begin looking to address them.
And the way we've approached this, again very similar to a previous
challenge, we looked to the community. One of the advantages we found of being
on Grafana Cloud is there is such a wide community out there and I think that's
true regardless if it's open source or if it's on the hosted version. There's a
huge community out there, Test Cube, which is just really a test runner for
Kubernetes with some additional bells and whistles, has OTel support and integrates
with Grafana Cloud really well. We have cloud events coming out there, which we've been able to translate into
it. So we are able to start importing those test results into Grafana Cloud k6. We can now use Grafana
Cloud as our k6 runner, which actually helps because one of the
questions with some of our testing is, well, "is it that the testing is causing the
performance impact because we're running it from the same place as we're actually
running the system?" There's a whole bunch of things there we've been able
to bypass and because we've got this end-to-end instrumentation from the
simulator through to a front-end code, through to everything in between, when we are running into
performance bottlenecks, we can actually find that pretty quickly. We can go and have a look and
get a single dashboard on, "is it the databases facing contention?"
Because we need to up it under this scenario. And for this kind of testing where
it's not low testing on steady state, but it's low testing on where we
expect to be in a year's time, which is significantly different. Being
able to do that kind of exploration and quickly identify where there might be
problems in the stack has been a really big deal for us. And now this same process has gone
beyond using it for the scaling test. We have progressive delivery, we make use of Flux and Canaries and part
of that is an integration with Grafana to check the metrics feed. We now have the load testing
for some of our services. We run that as part of a
quick 15-minute window. When we bring something up we check, but it's not just going to
match the scale we have today, but the features we are releasing will
match the scale we're going to have in a year's time. Again, just worked.
We were able, there was a plugin, therefore we were using for Flux. It can integrate with a
Prometheus data source. We could wire it up in a few minutes.
This was not a big thing to get done. And I forgot to go
to the end result slide that's on me. This is basically everything I just
talked about but with a prettier graph. So I'll move on to the next one.
But essentially the end result: incredibly successful. Final bit, which I know someone was talking about
earlier, intermittent connection drops. Intermittent connection
drops are a nightmare. They become quite complex in any scenario
when you have industrial protocols, when you have physical PLCs
and VPNs in the way and also Istio and all of this kind of good stuff. They become very complex at the diagnosis
and we've had a persistent one for a while now, which was happening on some of our quite
significant customers where it would just hang and wouldn't reconnect. We've been able to solve that problem. And actually what was really cool with
solving this problem was seeing how many people could collaborate on it. So because we've got this
full stack observability, because we've got this
ability to run testing, we were able to create custom tools and
custom tests really quickly and feed them into the overall dashboards.
Some of this was EBPF, which was one of the few times I've been
allowed to write code in the last six months because I'm too busy in
meetings, simulating black holes. And having met forwarded
into Grafana Cloud, we were also able to quickly implement
an interim solution which would just restart the service. We
had the alerting there, we'd done that alerting earlier
with the Customer Alerting. We could see if a telemetry feed wasn't
coming through and use that to kick off restarts as part of the system.
While we were doing further investigation. What was really interesting is because
of the data we had there in the exploration, we also found some
additional risks we needed to deal with. So we discovered that there were some
memory leaks under certain situations, which if we addressed this thing
which was causing it to hang, we then discovered there were
a whole bunch of memory leaks, which we faced due to a wavy underlying
industrial protocol that wasn't releasing certain parts of the stack. But the coolest bit for me with this
was I was away when this issue started being looked into. I came back, I had people across the business creating
these little micro dashboards of just two panels. I had people in the
more control side going, "Hey, there's this variable name which
we use you might want to look at". They were able to go create a panel and
share that with a bunch of other people from Customer Support, from Software Engineering.
Everyone was speaking the same language, and as a result of everyone
speaking that language, we were able to get to the
bottom of this much quicker. There wasn't any need to translate
between different teams and the different toolings they use. Everyone was under the same banner because
one of the significant things we've done with Grafana Cloud is every
single person in IGS can log to Grafana Cloud because we
have monthly active users. We're not actually too
stressed about that. So people just get together
and work on things. There's a few other areas of success
I'm going to quickly touch on. So cost management, we make heavy use of Adaptive Telemetry
and Adaptive Logs across the board. We've seen that drive our
costs significantly down, which is a big thing when
it comes to our customers. They measure their success on their profit
margins on crop sale. The more we can drive down our OpEx, the
better we can do on that. We've run some hackathons which
have been really successful. I found out about this the other day
when I was preparing for this talk and I looked into a dashboard and saw a bunch
of ones I didn't know about because I didn't create it as part of a hackathon
between different parts of a business. That's awesome to see. And we
have more future confidence, which we're going to talk about in the
last slide or two before questions. So what we've learned and what's next, there's a whole bunch of things
on here about what we've learned, but I think there's a couple of things
I hope people can take away from this. One, if you give people access for
tools and you have the data there, they will come up with use
cases you didn't imagine, be it like the Power BI
integration I mentioned, or the kind of dashboards I've been seeing
or just across the board. Some of the stuff my S Steps are doing is phenomenal. So you can give them access
and the data's there. They will do things which you don't
expect and that can be really cool. And I love seeing that. The other big thing I
say is we have future confidence for the projects we've
got coming up over next year or two. I didn't know about a lot of
these problems a year ago. I'm not going to know about problems
which are coming up a year from now. The factor is that the big
community around Grafana, the fact that we have great relationships
with our Account Manager and Professional Services from Grafana. If we decide we want to move more of our
control system from being on the cloud to being local, I know I
can use that way for that. I know I can reach out and solve that
problem. I don't have to be stressed about how much work is that going to be
for the SRE team to counter that. We can just pick it up and run with it. So having this kind of tooling gives
access from as many people as you can, embrace these tiny little
dashboards. Don't stress about them. Let people have this shared
language. And for us, doing all of this and having that future
confidence is a really big lesson we've learned because I'm now more confident
to take on projects for the team and that is helping the business. This is probably largely irrelevant
after seeing the stuff about [Grafana] Assistant this morning,
just putting it out there. Very excited about what's coming
up with that. However, for us, one thing to take away from this is
we're not talking about revolutionary changes. We're talking
about incremental changes. We want to make more use of IRM, we want to make more use of sift
and we want to have niche protocols instrumented, but actually these are incremental
changes. They're not initiatives I need to run. These are feature tickets I can
ask someone to go and have a look at. And that's a really big place to be at. So that's kind of where I'm
at. Observability Industrial
IT is still evolving, but it doesn't look that different
to what anyone else is doing. And I think that's a really important
thing for people who are in that space is to not be too concerned about it. And
just try and use these open standards, these open tools and you'll get
there. We've been through it. So yeah, that's kind of that. And there's
questions as well. Maybe? Hopefully? Otherwise it's going to
be awkward. Very good.

