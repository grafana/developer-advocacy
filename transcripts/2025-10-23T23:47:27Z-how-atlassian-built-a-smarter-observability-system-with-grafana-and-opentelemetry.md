# How Atlassian built a smarter observability system with Grafana and OpenTelemetry

Published on 2025-10-23T23:47:27Z

## Description

Discover how Atlassian built OpsDeck, an observability platform powered by Grafana, to automate incident detection, improve ...

URL: https://www.youtube.com/watch?v=okSBofcpY58

## Summary

In this YouTube video, Al, an engineering manager at Atlassian, discusses the company's efforts to enhance observability within their systems. Joined by colleagues Jim and Anthony, Al emphasizes the importance of open-source tools, particularly Grafana, in improving incident management and troubleshooting efficiency. He shares insights from his experience as an incident manager, highlighting challenges such as siloed knowledge and the complexity of troubleshooting across multiple services. By collaborating with various internal teams, Al's team developed a solution called Obsdeck, which focuses on opinionated workflows to streamline problem-solving during incidents. He elaborates on the implementation of tracing data to create a more integrated view of service dependencies and the establishment of real-time alerting to proactively address customer impacts. The video concludes with Al outlining future plans, including the integration of machine learning for further automation of insights in incident management.

## Chapters

00:00:00 Introductions and opening remarks  
00:01:15 Speaker introduction and background  
00:02:30 Overview of the Observability Insights team at Atlassian  
00:04:00 Discussing the challenges of incident management  
00:06:15 Importance of reducing troubleshooting time  
00:08:00 Introduction to OpenTelemetry and data quality issues  
00:09:30 Reasons for choosing Grafana as a solution  
00:12:00 Presentation of Obsdeck and its purpose  
00:14:00 Use case: Support workflow for troubleshooting  
00:16:30 Second use case: Incident troubleshooting improvements  
00:19:00 Future plans: Automation and machine learning in troubleshooting  
00:21:00 Conclusion and invitation for afternoon tea

## Transcript Cleanup

Do we have observability here? Hopefully. 

Alright, thank you, Jim and Anthony, for that wonderful session. That was awesome! The only thing I would say is please keep making your products open source; we love them! That's great for us. 

Look, I don't do this a lot, actually. This is probably only the second time, so I was a bit nervous. But Chris promised me a lot of awesome swag, and that's why I'm here. I got the swag, and I was about to leave, but then they stopped me at the door and said, "No, you have to do this." I'll try to be quick since I know there's a lunch break coming up. 

### About Myself

A little bit about myself: I'm part of Atlassian, a little company. I'm an engineering manager there, and I look after a team called Observability Insights. This team focuses on observability—not just as a platform, but on how we can solve some actual user problems. 

We started looking at the kind of issues teams run into and began partnering with some internal teams at Atlassian, like the engineering team, the SRE team, and the support team. Our goal was to reduce the time it takes to troubleshoot issues. That was the main focus and impact we wanted to have. 

### Challenges in Observability

Before I continue, may I see a show of hands? Have you ever found yourself in the middle of an incident without a clear idea of what the problem is or where it lies? (Show of hands.) Almost everyone, right? 

When I joined Atlassian three and a half years ago, I volunteered to become an incident manager. I jumped onto an incident in the middle of the night, and my God, I had no idea what was going on. There were all these weird names, and the graph displayed about a thousand microservices because Atlassian moved from on-prem to cloud very quickly. The speed of delivery, as you were talking about, made it a mess. Even getting the right team took almost an hour, and before you could find the right team, they took their own time trying to figure out where the problem was.

That's what we started focusing on. We wanted to make it faster for teams to reduce all the MTT metrics: time to engage, time to alert, time to mitigate, and the golden one, time to root cause. Our strategy was to partner with certain teams rather than just building something in a bubble because Atlassian is a big company with people doing different things. 

### Standardization and Data Quality Issues

There were a couple of challenges I won't go through all of, just to keep it short. The main ones were that there are a lot of business units within Atlassian, and they could go and do their own stuff, leading to reinventing the wheel and siloed knowledge. This made it extremely hard, especially during incidents or for support users trying to figure out what's wrong. It could be a frontend error caused by a backend service eight or nine layers deep. 

We wanted to break those silos by providing a standardized set of dashboards and workflows. Data quality issues were another big problem. We talked about OpenTelemetry; we had to do a lot of work to get it implemented across all services and pipelines. We're still working on this because there’s a lot of legacy code, as is usually the case with many companies. 

There's a lot of data and noise that we need to instrument and fix, and concerns like UGC and PII reduced the solutions we could use. So, we opted for a self-hosted solution to store the data within Atlassian. 

### Why Grafana?

Now, why Grafana? It’s an interesting journey. We've been partnering for over three years now. We started with a small open-source project with just four or five of us and decided to try Grafana. 

We chose Grafana because of its flexibility and open-source nature. You don’t have to start with, "Hey, I want to buy this product and go through a complex contractual agreement." It integrates really well with existing tools; we use almost everything you can think of at Atlassian. Grafana is also highly scalable, and we’ve been scaling it like crazy. 

Internally, what we've built on top of Grafana is what we call **Obsdeck**, short for observation deck. We also have a logo for it, which I should have shown here. Obsdeck is about building opinionated workflows instead of just having dashboards. 

### Use Cases for Obsdeck

We want our users to look at specific workflows and take them through a journey to figure out where the problem is happening, thus reducing their troubleshooting time. 

The first use case we picked was for support, which may seem strange when you think about observability. Support was looking to reduce their troubleshooting time, which used to take them a long time to triage issues and identify the right team. We partnered with them to build a solution on top of Grafana, using tracing data to help troubleshoot faster. 

We rolled it out last year for Jira, JSM, and Confluence, and we are seeing measurable impacts on the reduction of troubleshooting time. Our plan is to roll it out to the rest of Atlassian products. 

### Incident Troubleshooting

The second use case is our ambitious project, currently in progress, to solve troubleshooting during incidents. We aim to reduce the time to engage, mitigate, and root cause. 

I’ll share a couple of screenshots (though they may not look as fancy as those from Grafana). We use tracing data to stitch together the services and critical dependencies on the call path of an experience—like when you view or edit an issue in Jira. We pull in various metrics, telemetry information, logs, and SLO burn alerts. 

For example, if customers complain that "Jira issue view is broken," you can check this dashboard to see what services are down and dig deeper into the potential problems. This is where domain knowledge is useful; you can reach out to the team that owns that specific service and ask them to investigate. 

### The Incident Process

Earlier, when there was a customer impact, we didn’t even know if there was one until customers called us. Now, using high cardinality metrics stored in our system, we can have real-time alerting. When there's a customer outage, we get alerted before the customer does. 

We kick off a process called impact analysis to determine the impact, how many experiences are broken, and how many regions are affected. Based on this information, we create an auto-incident with the right severity, usually for Sev2 and above. 

We then look at the blast radius by examining infrastructure events, SLO errors, service level alerts, and tracing data. We stitch this together using a dependency graph to identify the top services that need attention, and we page them before any human is involved. 

### Conclusion

This process used to take us around an hour to find the right team, but we’ve cut it down to less than a minute, just using this data. Of course, the human element is still necessary. We’ve built workflows on top of Obsdeck and Grafana, including an **Incident Portal**, which serves as a one-stop-shop for everything related to an incident. 

Finally, we have the **tenant impact dashboard**, showing customer impact, and the **site scan**, which helps identify the root cause of issues. 

### What's Next

In terms of what's next for us, we are looking to automate a lot of these insights using machine learning and AI. Our goal is to make the process even smarter. When a human logs into the site scan, they will see not just that a service has a problem but also potential causes, like high CPU usage due to a recent deployment or an enabled feature flag. 

That’s our vision—reducing troubleshooting time even further. We still have to focus on standardization; this only works if we have really good data. We also want to create richer service dependency graphs to answer deeper questions about our systems.

Thank you very much! 

Just a note: we're going to have afternoon tea outside, and we’ll return to this room at 3:40 for the next session.

## Raw YouTube Transcript

Do we have observability here? Hopefully. Alright, look, thank you and thanks for that
wonderful session, Jim and Anthony. That was awesome. The only thing I would say is please
keep making your products open source. We love them. That's great for us. Look, I don't do this a lot actually.
Probably this is only the second time, so I was a bit nervous, but Chris
promised me a lot of awesome swag. That's why I'm here. I got the
swag, I was about to leave, but then they stopped me at the door.
They said, no, you have to do this. I'll try and be quick. I know
there's a lunch break coming up. So a little bit about myself. I'm part
of a Atlassian, the little company. I'm a engineering manager over there. I look after a team called
Observability Insights. So this was a team which is
where we started focusing on observability, not as a platform, but we started looking at how can we solve
some of the actual user problems over there.
We started looking at what are the kind of issues that teams running to, and we started partnering with some
of the teams over there internally at Atlassian, like the engineer team and
the SRE team and the support team. What our goal was to reduce the time
it takes to troubleshoot issues. That was the main focus that we wanted
to have or the impact that we wanted to have. Before I continue,
maybe just a show of hands, have you ever found yourself in the
middle of an incident where you don't have a clear idea of what the problem is
or where it lies? Maybe show of hands, right? Almost everyone, right? So when I joined Atlassian
three and a half years back, I volunteered to become an
incident manager and I jumped
onto an incident in the middle of the night and my God, I had no idea what the heck was going on.
There was all these weird names and the graph showed about a thousand
microservices because Atlassian moved from on-prem to cloud very quickly. Speed of delivery like you were
talking about and it was just a mess. So even getting the right team took
almost like an hour and before you could actually find, okay,
what is the right team? And then they took their own time trying
to figure it out where the problem is. So that's what we actually
started to focus on. We wanted to make it faster
for teams to be able to reduce all the MTT stuff, right? Time
to engage, time to hurt, time to reduce, time to mitigate and the
golden one time to root cause. And our strategy over there was we wanted
to partner with certain teams rather than just building something in a bubble
because Atlassian's big company people are doing different things.
That's why I'll more about how we partnered with them. There
were a couple of challenges. I won't go through all of this
slide just to keep it short, but the big ones over there were, there's a lot of business units within
Atlassian and they could go and do their own stuff. A lot of reinventing the wheel, siloed knowledge that made it extremely
hard when it came to when you're in the middle of an incident or when you're a
support user trying to figure out what's wrong. It could be a front end
error caused by a backend service, eight or nine layers deep. So we wanted to break those silos
by providing a standardized set of dashboards and workflows. Data quality issues was another big
problem. We talked about OpenTelemetry, Atlassian, we had to
do a lot of work to get OpenTelemetry implemented across all
the services, across all the pipelines, they're still doing it because there's
a lot of legacy code as usually the case with a lot of these companies.
There's a lot of data, a lot of noise that we again have to
go and instrument and fix and cost and UGC and PII made solutions like reduced what solutions could be used. So we had to go with the
self hosted solution that
where we could store the data within Atlassian. Why Grafana? So it's actually a very
interesting journey. I think we've been partnering
for over three years now. We started with a small open source
project with just four or five of us and we said, Hey, we're
going to try Grafana. Why we want to use Grafana
because of its flexibility, it's open source. You don't
have to start with, Hey, I want to buy this product and go
through a complex contractual agreement. It integrates really
well with existing tools. We use almost everything you can think
of at Atlassian and Grafana is really good and you can write plugins as well. Recently we've been scaling it like
crazy. It's extremely scalable. I'll talk a bit more about the high
cardinality metrics and the tracing data that we've been storing
at Atlassian. And again, a big plus is there's no vendor
lockin, right? You can move anytime. Not that we want to, but
that's again really plus point. So internally what we built on top
of Grafana is what we are calling Obsdeck, basically short for
observation deck. We also have a logo. I should have put it over here.
That would look very cool. So Obsdeck is basically,
instead of having dashboards, what we've been doing is
building opinionated workflows. So what we wanted to do is rather
than coming in and showing you a team, basically looking at specific dashboards, we wanted our users to go in and look at
certain workflows and take them through a journey so they can actually figure
out the problem is happening and cut down their troubleshooting time. So the two use cases that we picked,
the first one of them was support, which is a bit strange when
you think about observability. What does support have to do
with observability, right? So support at that time two years back, they were looking at reducing their
troubleshooting time. So they were looking at logs. It used to take them
a long time to triage issues, figure out what is the right
team, where is the problem. We were looking for a partner where
we had this vision. We said, okay, we're going to build this solution on
top of Grafana and use tracing data and other insights to help
troubleshoot faster. So that partnership was born and we
built a opinionated workflow for the support users where we used tracing
data to build them like an end-to-end transaction view. And we integrated
with our existing systems, we provided them error code mapping
so you could actually look at their record and you can actually
see the troubleshooting steps. And it was a huge success.
We rolled it out last, we started building on it last year and
we've just finished rolling it out for Jira, JSM, and Confluence. And we are seeing
really measurable impact on the reduction of troubleshooting time. So our plan is that we are now going
to roll it out to the rest of Atlassian products. One thing I wanted to call
out here is the Atlassian scale. Because of our nature of
the data and the systems, we have to build our own custom
tail sampling algorithms. So that's very important
when you do tracing, how much data do you want to sample? You can't sample all the data because
that just makes it too expensive and cost is a big factor always. So that's something we did and
we open sourced it as well. If any of you're interested, I think
that's a good thing to look at. The second use case is our
very ambitious use case, which we are currently working on. So we started working on this in late
FY 25 and we're still working on this, which is to solve the
problem of troubleshooting during incidents. So how can you get to the point where
you are reducing the time to engage, time to, time to mitigate,
and also time to root cause. So I'll just share a
couple of screenshots. They don't look as fancy
as the ones from Grafana. I had to remove a lot of the
stuff over there as well. But what we've tried to do
is we use the tracing data to stitch together the services, the critical dependencies on
the call path of experience. So think of an experience as
when you view an issue in Jira, when you edit an issue in Jira, what are the services that
are going to support that experience? And we pull in
different sorts of metrics, telemetry information, like
we pull in trace span metrics, we pull in telemetry data, we pull in logs and SLO burn alerts and
all this information be presented and of use. So when you are
an incident like me, you can actually go to this
dashboard. For example, the customers are complaining, "Hey, JIRA issue view is broken". You can go
over there and you can actually see what are the services that are broken and
then you can start digging deeper into what it could be the actual problem. And this is wher domain
knowledge could be useful. You might get a team which owns that
specific service and you can page them and say, look, I see higher
rates for your service. Can you please go and
investigate this? And again, they can have their own custom dashboards. We are not saying everybody
needs to have the flexibility. What we are trying to do is centralizing
this information in a standard base so teams don't have to go and build their
own dashboards or there's one place where they can go and look
at all the information. The last thing I wanted to show over
here is kind of like a workflow of how it all fits together because it's been
a journey just getting to this stage. So like I said, three years back
when there's a customer impact, we didn't even know if
there was a customer impact. Our customers would be calling us and
telling us, Hey, your JIRA is broken, right? Go and take a look at it. What we've been able to do is using the
high cardinality metrics stored in Mi mir, we have been able to
now have real time alerting. So when there's a customer outage, we actually get alerted
before the customer hopefully. And then we kick off a process
which we call impact analysis, where we go and try and
figure out what is the impact? Is it just located to a particular
customer? How many experiences are broken, how many regions?
And based on this information, we create an auto incident
with the right severity. So normally we do it for Sev2 and
above, which is high severity incidents. Then we go and take off another
process which starts looking at what is the blast radius. So we look at
what are the infrastructure events, are there any errors coming from the
SLOs, are there any service level alerts? And we also look at tracing data and
we stitch this together using the dependency graph from tracing
to now identify what are the leaf nodes which could be addressing out. And once we identify the
top three or four services, we actually page them as well before
any human is involved. So all of this, if you think about it,
like as mentioned earlier, this used to take us around an hour
to get to finding the right team. So we've been essentially able to cut
down that into less than a minute just using this data. And then obviously the human
element has to be involved, right? You can't do this without a human. So what we've gone is we've built
on top of Obsdeck and Grafana, we built certain workflows or portals. So we have something which
we call Incident Portal, this is your one place where you'll go
for everything related to an incident. You'll get all the links,
you'll get the chat messages, you'll be able to see who are
the teams that have been paged, who's involved on the incident,
what does the timeline look like, and what are the related incidents or
previous incidents that were related to this. We also have something which
we call tenant impact dashboard, which shows you the
customer impact. So again, you can look at how many
customers were impacted, is the impact increasing or decreasing? And this helps you make a call whether
you raise the severity or lower the severity of the incident. And finally
site scan, the one I told you about, which is what we are banking on, being able to go that deeper when
you're not sure where the problem is. So you'll be able to figure out
what is the root cause analysis and how do you troubleshoot
where the fault is coming from. I think that's all I had
almost what I had for today. So just in terms of what's next for us, so we are looking at automating
a lot of these insights. We've been using machine learning and AI. What we want to do is cut short
this process even further. So right now we want the human
element to be involved still, but we want it to be smarter. So when a human logs into or
side scan, they can actually see, hey, it's not just this
service that has a problem, but it's because of high CPU
count or threat saturation, which is caused by the
change that was deployed in the last hour or maybe because
of a feature flag that was enabled. So that's a dream or the north
star that we want to reach to. So it just reduces the
troubleshooting time completely. We still have to do a
lot of standardization. This only works if you have really good
data, even machine learning and AI. And we want to do richer
service dependency graphs. So being able to answer questions, how many of my call graphs are
coming from different regions or there is the highest latency
coming from and some more deeper things that we could look at. And I think that essentially
it. Thank you very much. Thank you Al. Just letting know, we're going to have afternoon tea outside
and we'll return back into this room at three 40 for the.

