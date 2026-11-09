# How SailPoint cut log investigations from hours to minutes with Grafana Cloud Assistant

Published on 2026-05-28T15:16:09Z

## Description

Juan Carlos Ramirez, Senior Staff DevOps Engineer at SailPoint, shares how his Periscope observability platform team migrated ...

URL: https://www.youtube.com/watch?v=6QSgbzKJpAI

## Summary

The show is titled "How SailPoint cut log investigations from hours to minutes with Grafana Cloud Assistant," published on May 28, 2026. The speaker, Juan Carlos Ramirez, is a Senior Staff DevOps Engineer at SailPoint, leading their observability practice. He discussed SailPoint's migration from SQL to ClickHouse and Grafana Cloud, emphasizing the benefits of using Grafana tools for log management and observability. Key takeaways include significant reductions in log investigation time, improved user experience, and the integration of Grafana Assistant, which enhances productivity by streamlining data analysis. The migration not only simplified log management but also aligned with industry standards and improved overall efficiency for the Access Risk Management team.

Topics: Grafana Cloud, ClickHouse, log management, Grafana Assistant, observability.

## Chapters

00:00:00 Migration from SQL to ClickHouse and Grafana
00:04:42 Migrating logs to ClickHouse Cloud at SailPoint
00:08:35 Grafana Assistant improves log investigation efficiency

Howdy, everybody. Thank you all for coming out, and I'm very excited to tell you a story today. But first off, introductions. My name is Juan Carlos Ramirez, and I am a Senior Staff DevOps Engineer at SailPoint. I'm actually the lead of our observability practice. We're a team called Periscope, and we're a team of nine people responsible for providing a platform. What I mean by that is any of the telemetry that moves through the pipes at SailPoint; we want to ensure our engineers can self-service and manage that telemetry. We're just going to provide the tools for them.

I've been here at SailPoint for about six years and have been very involved with stack modernization. I have a lot of experience moving Prometheus Federation, if you're familiar with that, to Cortex and to Grafana Cloud. That's actually the start of our great relationship with Grafana, adopting Grafana Cloud, as well as recently migrating to Tempo. You're going to hear a little bit about that during the talk as well. Alongside that, I'm a big fan of smart homes, Home Assistant, EVs, gaming, and tech. I've got my LinkedIn QR code there if you wanted to give it a scan.

So, who is SailPoint before I get into our actual project? We're an identity security leader, and just to boil that down, all it means is that we're going to help your company determine who gets access to what, right? Making sure that we don't over-provision any privileges to someone who shouldn't have them. We're definitely starting to lean into how AI and other automation tools utilize those provisioned access. Our headquarters is here in Austin, Texas. Fun fact: we actually IPO'd twice, which was pretty interesting to be involved in since I came in in 2020.

So, what are we talking about today? We're going to be talking about a migration we did from SQL to ClickHouse and Grafana. The big thing I want you to get out of this talk is how better tools, Grafana's tools, make your life easier and make things simpler. Quality of life just gets better once you adopt the right tools.

Before we get into that, some background. I want to tell you a bit about our observability stack at SailPoint before I dial it down into what we actually migrated out of. For a little bit of context, we have metrics, traces, and profiling with Grafana Cloud. All of that exists in the cloud right now, but we also do logs with OpenSearch, and logging is going to be what we're talking about today. We do about 30 terabytes of logs per day, which is pretty big for our organization right now, and it's consistently growing. We also do routing for on-call, and as I said before, observability as a platform. We don't want anything bespoke; we want to be able to provide the tools. We don't want our teams to be burdened by the tools.

So, let's get into who we helped migrate. We have a team internally called ARM, Access Risk Management, who helps protect organizations by monitoring and checking out any risks. They use logs to detect risky access, investigate events, and support the remediation. A fun fact about them is that they were an acquisition, which means I believe around 2021 or so we acquired them and brought them into the SailPoint fold. If you've ever acquired a smaller company, it has its challenges, right? It's a different culture, different people; they're set in their ways. When you want to bring them into a new platform, that platform has to be attractive. You want them to want to come over. If you're going to take away the tools that they've spent years cultivating, you need to give them something good.

So, let's look at how they were doing things before. You can see they had ARM services sending data to a service bus, all Azure, by the way, sending it to a microservice code written in .NET, and then finally to an SQL server. As I've put there, they had some issues. They had to configure that MySQL server and manage retentions. One of their team leads was telling me that two or three times a year, they had to reduce storage by getting rid of logs, and that actually caused a P2 at one point. So, they're spending some toil here, and there's also just developer friction, right? No native visualization tools. They were telling me how they had to export logs into Excel. It's just not the place we'd want them to be.

So, why did we move them to ClickHouse? Why did we move them to Grafana? There are two main points I want to identify here. ARM is a separate bespoke team, so it's not our total services that we need to move over, and they're hungry for a better offering. You already know that if you have a team that doesn't want to move, it's going to be hard to even get them to move to something that could be better for them. Not only that, SailPoint internally is very big on OpenSearch, and we like it. But as I mentioned before, I'm big on modernization. It seems like the industry's moving to ClickHouse. Does ClickHouse have a role at SailPoint? How do we get that tested? Maybe a bespoke team with fewer logs in our total login test could be a good proof of concept here.

ClickHouse itself offers columnar speed, compression, faster queries, and cheaper storage. And then, of course, Grafana—I don't really have to go too in-depth here—provides unified access to logs, metrics, and traces in one bucket. We've got a great relationship, and we just got Tempo. A lot of things are lighting up for this migration.

So, what do we want to actually see for the ARM team? What I have here is a pipeline for how we plan to get their logs to ClickHouse Cloud. We said we have some sources, so services, and the first thing we want to do—this is a big project I'm actually working on this year—is aligning our services with semantic conventions and logging standards. We want to align them with OpenTelemetry (OTel). You can't just deploy whatever you want in whatever shape you want it; we want to line it up with the OTel standard.

Second, we want to implement Vector. Now, I could run a whole talk and tell you a story after this about how we moved from Fluentd to Vector, resulting in a 90% reduction in our resource usage. It was actually a really good project that we saw great things out of. So, we don't want to give them anything bespoke. We're going to continue using Vector, which we've already proven across SailPoint, and we're going to use Cribl, which, if you're unaware, is a middleman processing layer where all your logs arrive, and you can look at them in real-time, do your edits, and apply changes to them in one central place. Once we have that, we're going to send them off to ClickHouse Cloud, get it wired up in Grafana, and hit the races.

So, what does our migration plan look like? We want to set a foundation first. We can't just move everything over. The first thing we ought to do is bridge any gaps. You can see I modified that previous graph to show a second dual-write path because we don't just want to take SQL from them without proving it's worth it. We added some custom code that's actually going to take data from that service bus and write it to standard out so Vector can collect it. The reason we have to do this is that not all of their services are running in Kubernetes yet. That is something that they're working on. Once they have that, we likely won't need that anymore, but that's going to bridge the gap. It's going to implement dual writes so that we don't just take away SQL, and we get the benefit of using our existing Cribl and Vector configurations.

After we perform that, we're going to gather feedback, tune the database, and make sure it's actually working very, very well. We want to actually survey because, as you've heard a lot during these sessions, getting feedback and getting surveys is really important to making sure you're doing not just the right thing but also the best thing for the team.

only a good job, but actually proving that it was worth the effort. And then finally, we're going to migrate all of the services. 

So what are the results? These next slides are the ones I'm most excited to tell you about because this one is pretty close to my work here: getting a unit cost for your logs. 

See, one thing we struggled with, especially with all of the migrations and modernizations I've been working on, is how do I prove to our executive team and everyone else above me that the work we did was valuable, that it actually reduced costs? The problem is that if I optimize our database to reduce costs by 10%, but then my services generate 30% more logs, I have to scale again, and it doesn't look good when next month our logging database costs more than the previous month. 

So what they got out of this migration was our existing cost per log model. What we do is we want to surface these unit costs per service so we can actually tell you how much a service cost over the previous 24 hours or the previous week. We use Grafana's mixed data source capabilities to look at our Athena costs, which we get out of AWS Cost Explorer, and our logs ingested, which we actually get from Vector and the Prometheus metrics it emits. 

Using that data, I can actually tell you what that service cost to generate their logs, which is really, really good because we can actually detect spikes in costs this way. For example, ARM is doing about 18 gigabytes a day, which compared to the rest of SailPoint isn't very much, but if they increase their costs by 30, 50, or 60%, I can visualize that down at that level. 

Next, Grafana Assistant. This one is very near and dear to me as well because it's personally saved me a ton of time, and this is what they're going to get with their move to Grafana. Their LLMs can cut your investigatory hours into minutes and it takes your full attention into multitasking. I can just ask Grafana a question, leave it in that tab, go do something else, get Slack, get some coffee, and come back to a full investigation. 

It's personally helped me find spikes in logs before the assistant that would've taken me maybe 15 to 20 minutes down to maybe five, and that's while I'm doing other things. And mind you, it's not just me; it's everyone else on the team. I'm actually going to dig into how ARM started using it. Mind you, they are new to Grafana. 

So this is what they got right after onboarding: ways where it helps you create dashboards, leverage general and natural language whenever talking to this AI, and just makes the onboarding experience faster. Previously, you'd have to host some lunch and learns, host some trainings, and actually get people to get on board. 

So let's deep dive into what they did. This was actually something their team lead brought to me. A little bit after migrating, they went and asked Grafana, "Can you create a bar chart of the top seven failures for the auth services over the past two hours? They're currently undergoing an issue in that environment." Grafana Assistant just generated that bar chart for them on the fly. 

Mind you, this is a brand new team that doesn't necessarily know how to work with ClickHouse and Grafana yet, and they got that bar chart in seconds. When they actually asked what the cause of failure was, it deduced the issue: 83% of the errors were due to an invalid token, 50% from a single service. When I asked their team lead how long this would have taken for someone to normally do in SQL land, it would've been two to four hours down to 20 minutes. 

And mind you, that was just immediately after the migration. As we onboard more services and get them more used to the system, it's very likely they're going to save a lot more time. 

So overall, what were our productivity improvements? What did we actually get out of this small migration? Well, one, ClickHouse is pretty easy to configure, at least in the cloud. Data ages out automatically, so no more incidents, right? And then ARM is now on the same platform. This is really important because, as I mentioned earlier, the semantic conventions I'm working on, they're going to get that out of the box because they're working with Vector and Cribl, which means I don't have to worry about them being siloed off when I implement new standards or a new process; they're just going to get it. 

I already proved the MTTR with Grafana Assistant, that 2-4 hour analysis down to 20 minutes, and then just a better user experience, right? Their metrics and traces are already there. They actually get proper visualizations, right? No more exporting to Excel. It's just overall better. 

So what are our next steps? What are we going to do after this? Well, we still have to finish the migration. We can't just leave it where it is. There are still some more services to get to, so we're going to knock that out. 

We also want to get more key metrics: feedback, benchmarks. We want to be able to prove that things are actually faster and better now. And then finally, once we have that, we got to give them some new toys, right? We want anomaly detection, SLO dashboards, and auto-scaling where we can. 

That being said, thank you for listening to this story, y'all, and I appreciate your time.

## Raw YouTube Transcript

Howdy, everybody. Thank you all for coming out and I'm
very excited to tell you a story today. But first off, introductions, although
the slides are giving me ... There we go. My name is Juan Carlos Ramirez and I
am a Senior Staff DevOps engineer at SailPoint. I'm actually the lead
of our observability practice. We're a team called Periscope and we're
a team of nine people responsible for providing a platform. And what I mean by that is any of the
telemetry that moves through the pipes at SailPoint, we want to ensure our engineers can
self-service and manage that telemetry. We're just going to
provide the tools for them. I've been here at SellPoint
for about six years. Very, very involved with stack modernization. I had a lot of experience
moving Prometheus Federation, if you're familiar with that,
to Cortex, to Grafana Cloud. That's actually the start of our
great relationship with Grafana, adopting Grafana Cloud, as well as recently migrating to Tempo.
You're going to hear a little bit about that during the talk as well. Alongside
that, I'm a big fan of Smart Homes, Home Assistant, if you guys
have that, EVs, gaming, tech, and I've got my LinkedIn QR code
there if you wanted to give it a scan. So who is SailPoint before I
get into our actual project? We're an identity security leader
and just to boil that down, all it means is that we're
going to help you, your company, determine who gets access to what, right? Making sure that we don't over-provision
any privileges to someone who shouldn't have it. And we're definitely starting to lean
into how AI and other automation tools utilize those provisioned access.
Our headquarters is here in Austin, Texas. And fun fact, we
actually IPO'd twice, which was pretty interesting to be
involved in since I came in in 2020. So what are we talking about today? We're going to be talking
about a migration we did
from SQL to ClickHouse and Grafana. And the big thing I want you to get
out of this talk is how better tools, Grafana's tools, makes your life
easier and makes things simpler. Quality of life just gets better
once you adopt the right tools. So before we get into
that, some background. I want to tell you a bit about our
observability stack at SailPoint before I dial it down into what we
actually migrated out of. So for a little bit of
context, we have metrics, traces and profiling with Grafana Cloud. So all of that exists
in the cloud right now, but we also do logs with open search
and logging is going to be what we're talking about today. We do about
30 terabytes of logs per day, which is pretty big for our organization
right now and it's consistently growing. And we also do routely
for on-call and as I said before, observability as a platform.
We don't want anything bespoke. We want to be able to provide the tools. We don't want our teams to
be burdened by the tools. So let's get into who we helped migrate. So we have a team internally
called ARM, Access Risk Management, who helps protect organizations by
monitoring and checking out any risks. So they use logs to detect risky
access, investigate events, and support the remediation. And a fun fact about them is
that they were an acquisition, which means I believe around 2021 or so
we acquired them and brought them into the SailPoint fold, which if you've
ever acquired a smaller company, it has its challenges, right? It's a
different culture, different people, they're set in their ways. And when you
want to bring them into a new platform, that platform has to be attractive.
You want them to want to come over. If you're going to take away the tools
that they've spent years cultivating, you need to give them something good. So let's look at how they
were doing things before. You can see they had ARM services
sending data to a service bus, all Azure, by the way, sending it to a
microservice code, written in.net, and then finally to an SQL server.
And you can see, as I've put there, they had some issues, right? They
had to configure that MySQL server. They had retentions. One of their team leads was telling me
that two or three times a year they had to reduce storage by getting rid of logs
and that actually caused a P2 at one point. So they're spending some toil here and
there's also just developer friction, right? No native visualization tools. They were telling me how they had to
export logs into Excel. It's just not the place we'd want them to be. So why did we move them to ClickHouse?
Why did we move them to Grafana? And there's two main points
I want to identify here. ARM is a separate bespoke team, so it's not our total services that
we need to move over and they're hungry for a better offering. You already know that if you have
a team that doesn't want to move, it's going to be hard to even get them
to move to something that could be better for them. And not only that, SailPoint internally we're very
big on open search and we like it. But as I mentioned before,
I'm big on modernization. It seems like the industry's
moving to ClickHouse. Does ClickHouse have a role at
SailPoint? How do we get that tested? Maybe a bespoke team with fewer logs
in our total login test could be a good proof of concept here.
So ClickHouse itself, we have columnar speed, compression,
faster storage or faster queries, cheaper storage maybe.
And then of course Grafana, I don't really have to go too in
depth here. Unified access, logs, metric traces in one bucket, right?
We've got a great relationship. We just got Tempo. A lot of things
are lighting up for this migration. So what do we want to
actually see for the ARM team? So what I have here is a pipeline
for how we plan to get their logs to ClickHouse Cloud. Now what we did is we
said we have some sources, so services, and the first thing we want to do, this is a big project I'm
actually working on this year, which is aligning our services
with semantic conventions
and logging standards. We want to align them with OTEL, right? So you can't just deploy whatever you
want in whatever shape you want it. We want to line it up with
the OTEL standard. Second, we want to implement Vector.
Now, I could run a whole talk and tell you a
story after this about how we moved from Fluentd to Vector resulting in like
a 90% reduction in our resource usage. It was actually a really good
project that we saw great things out of. So we don't want to give
them anything bespoke. We're going to continue using Vector, which we've already proven across
SailPoint and we're going to use Cribl, which if you're unaware what that is, it's a middleman processing layer where
all your logs arrive there and you can look at them in real time, do your edits and actually apply
changes to them in on central place. Once we have that, we're going to
send them off to ClickHouse Cloud, get it wired up in
Grafana and hit the races. So what does our migration plan look
like? We want to set a foundation first. We can't just move everything over. So the first thing we ought
to do is bridge any gaps. You can see I modified that previous
graph to show a second dual right path because we don't just want to take SQL
from them without proving it's worth it. And we added some custom code there that's
actually going to take data from that service bus and write it to standard
out so Vector can collect it. Now the reason we have to do this is that
not all of their services are running in Kubernetes yet. That is
something that they're working on. And once they have that, we
likely won't need that anymore, but that's going to bridge the gap. It's going to implement dual rights so
that we don't just take away SQL and we get the benefit of using our existing
cribble and vector configurations. After we perform that, we're going to
gather feedback, tune the database, make sure it's actually working very,
very well. And we want to actually survey, because as you've heard a
lot during these sessions, getting feedback and getting surveys is
really important to making sure you're doing not only a good job, but actually
proving that it was worth the effort. And then finally, we're going
to migrate all of the services. So what are the results? And these next slides are the ones I'm
most excited to tell you about because this one is pretty close to my work here, getting a unit cost for your logs.
See, one thing we struggled with, especially with all of the migrations and
modernizations I've been working on is how do I prove to our executive team and
everyone else above me that the work we did was valuable, that it actually reduced costs because
the problem is that if I optimize our database to reduce costs by 10%, but
then my services generate 30% more logs, I got to scale again and it doesn't
look good when next month our logging database costs more than the previous
month. So what they got out of this migration was our existing cost
per log model where what we do is we want to surface these unit costs
per service so we can actually tell you how much a service costed over the
previous 24 hours or the previous week. And we use Grafana's mixed data
source capabilities to look at our Athena costs, which we get out of AWS Cost
Explorer and our logs ingested, which we actually get from Vector
and the Prometheus metrics it emits. So using that data, I can actually tell you what that
service costed to generate their logs, which is really, really good because we can actually
detect spikes in costs this way. For example, ARM is doing
about 18 gigabytes a day, which compared to the rest
of SailPoint isn't very much, but if they increase their
costs by 30, 50, 60%, I can visualize that down at that level. Next, Grafana Assistant. This one is very near and dear to me as
well because it's personally saved me a ton of time and this is what they're
going to get with their move to Grafana. Their LLMs can cut your investigatory
hours into minutes and it takes your full attention
into multitasking. I can just ask Grafana a question, leave
it in that tab, go do something else, get Slack, get some coffee, and
come back to a full investigation. It's personally helped me find spikes in
logs before the assistant that would've taken me maybe 15, 20 minutes down to maybe five and
that's while I'm doing other things. And mind you, it's not just me, it's everyone else on the team and
I'm actually going to dig into how ARM started using it. Mind you,
they are new to Grafana. So this is what they got right after
onboarding in ways where it helps you create dashboards, leverage general and natural language
whenever talking to this AI and just makes the onboarding experience faster because
previously you'd have to host some lunch and learns, host some trainings,
and actually get people to get on board. So let's deep dive into what they did. This was actually something their team
lead brought to me where a little bit after migrating, they
went and asked Grafana, "Can you create a bar chart of the top
seven failures for the auth services over the past two hours? They're currently undergoing an issue
in that environment." And Grafana Assistant just generated that bar
chart for them on the fly. Mind you, this is a brand new team, doesn't necessarily know how to work
with ClickHouse and Grafana yet and they got that bar chart in seconds. And when they actually asked
what the cause of failure was, it actually deduced the issue. 83% of
the error is due to an invalid token, 50% from a single service.
When I asked their team lead, how long would've this taken for just
someone to normally do this in SQL land? It would've been two to four hours
down to 20 minutes. And mind you, that was just immediately
after the migration. As we onboard more services and
get them more used to the system, it's very likely they're
going to save a lot more time. So overall, what was our
productivity improvements, right? What did we actually get out of
this small migration? Well, one, ClickHouse is pretty easy to
configure, at least in the cloud. Data ages out automatically,
so no more incidents, right? And then ARM is now on the same platform. This is really important
because as I mentioned earlier, the semantic conventions I'm working on, they're going to get that out of the box
because they're working with Vector and Cribl, which means I don't have to worry about
them being siloed off when I implement new standards or a new process,
they're just going to get it. I already proved the MTTR
with Grafana Assistant, that 2-4 hour analysis down to
20 minutes and then just a better user experience, right? Their
metrics and traces are already there. They actually get proper
visualizations, right? No more exporting to Excel.
It's just overall better. So what are our next steps? What
are we going to do after this? Well, we still have to finish the migration.
We can't just leave it where it is. There's still some more services to get
to, so we're going to knock that out. And then also we want to get more key
metrics, right? Feedback, benchmarks. We want to be able to prove that things
are actually faster and better now. And then finally, once we have that, we
got to give them some new toys, right? We want anomaly detection, SLO
dashboards, and auto scaling where we can. That being said, thank you for
listening to this story y'all, and I appreciate your time.

