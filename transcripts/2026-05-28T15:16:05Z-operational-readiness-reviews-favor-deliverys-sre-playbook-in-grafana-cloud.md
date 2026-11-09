# Operational Readiness Reviews: Favor Delivery&#39;s SRE playbook in Grafana Cloud

Published on 2026-05-28T15:16:05Z

## Description

Kevin Panahi, Senior Site Reliability Engineer at Favor Delivery, walks through the Operational Readiness Review (ORR) ...

URL: https://www.youtube.com/watch?v=WO9y2jn4qWk

## Summary

The show "Operational Readiness Reviews: Favor Delivery's SRE playbook in Grafana Cloud" was published on May 28, 2026, featuring Kevin Panahi, Senior Site Reliability Engineer at Favor Delivery. Kevin discussed the Operational Readiness Review (ORR) process implemented at Favor, focusing on how Grafana dashboards facilitate monitoring and improve service reliability. Key topics included the use of service level objectives (SLOs) and indicators (SLIs), the integration of metrics from Kubernetes services, and the importance of cross-team communication in enhancing operational efficiency. The ORR has led to better SRE adoption, reduced alert fatigue, and improved incident management within the engineering teams.

Topics: Operational Readiness Review, Grafana dashboards, service level objectives, SRE adoption, incident management.

## Chapters

00:00:00 Overview of Favor Delivery's SRE and monitoring challenges
00:05:32 Understanding service level objectives and error budgets
00:11:00 Discussing SLOs and error budgets in ORR meetings
00:17:17 Benefits of operational readiness reviews for SRE teams

Hi, my name's Kevin Panahi, and I'm here from Favor Delivery. I want to thank Grafana for hosting me and my team here today. I'm the Senior Site Reliability Engineer at Favor. I've been at Favor for a little over a year now, but I've been in the DevOps platform space for about eight years. 

Today, we're going to talk about the Operational Readiness Review (ORR) that we do here at Favor and how we use Grafana dashboards as the starting point for many of those conversations. 

For those of you who don't know what Favor Delivery is, we are a home grocery and food delivery service operating under the HEB umbrella. We're Texas-only and proudly unavailable in 49 states, which is one of our fun taglines. In the Austin area, you've probably seen the big billboards advertising Favor Gold or our Cowboy ads that promote our Texas Two-Stop service. So that's who we are.

Let me give you a little bit about the team here. We have 12 squads in our engineering department, two of which are the SRE and DevOps teams. Both of those teams have four people on them: a principal, two seniors, and a mid-level engineer. I point out our DevOps team because we work super closely with them. A lot of what SRE discusses comes from DevOps as well. The rest of the teams are our normal software engineering teams.

Now, let me set the stage for where our monitoring position was when I started. We had just migrated a lot of our services onto Kubernetes. Historically, we were kind of a big monolith shop, but we moved to Kubernetes and adopted a microservice architecture. Around the same time, we also had a significant headcount increase in the engineering department. We went from small concentrated teams to adding 10 other software engineering teams, including an SRE team. The SRE team was a little over a year old when I joined, and that’s kind of where we were.

There were a lot of growing pains, the biggest being noisy alerts that weren't very helpful and just paged people without anyone knowing what to do with them. When I was interviewing, I asked one of our Senior Software Engineers, "Hey, SRE is this new thing here. Why do you want an SRE department at your company?" He replied, "I kind of just don't know what's going on." That was an alarming thing to hear.

So we were trying to find a way to implement a good solution for most of our services and get that visibility. We had Istio be our superhero for this. Istio is a service mesh that operates inside your Kubernetes cluster. It manages all of our Layer 7 networking traffic within the cluster. Along with Istio, you get metrics, which you might have heard of at a Grafana conference. These metrics communicate the most important things to us, such as request response codes (like your 200s, 400s, and 500s) and application latency (how fast your service responds to requests).

Istio is injected as a sidecar into our pods, and that sidecar produces the metrics that we report and alert on. Those metrics are then consumed by Grafana Alloy and shipped to Grafana Cloud, where all of the recording rules and alerts are set up.

Now that we have these metrics, we can turn them into service level objectives (SLOs). To have an SLO, you need a service level indicator (SLI). Thinking about the four golden signals in the SRE world, we started with the two easiest ones: availability and latency. Most of our services are API services, so this is a good fit for them.

For availability, we looked at all responses that were not 500 responses, viewing those as successful, while 500 responses were viewed as failed requests. We measured those from the perspective of the caller. If a client is getting 500s, the application didn't work, regardless of what the application thought it did.

For latency, we measured that from the server perspective because we didn't want to penalize a service's performance based on the wire between the client and the server.

Now that we have our SLIs, we need our objectives. At Favor, we have three tiers: tier one being the highest. We set service level objectives based on the tier the team decides their service belongs to. We believe that squads should own their services and how they are defined. If a squad thinks they have a tier three service and I think they have a tier one service, they have a tier three service. It's their decision, not mine.

Depending on the tier they pick, the objective they get varies: two nines for a tier three, three nines for a tier one, and two and a half nines for a tier two. For latency, we set targets from 99% down to 90%, and again, the latency target is picked by the squad. If a squad thinks it's acceptable for a service to respond in one second, then their latency target is set to one second. For a tier one service, 99% of the requests need to happen within that one second.

Now that we have an objective, we can create a burn rate or an error budget. With an error budget, you can create a burn rate alarm. I recommend looking at Google's documentation and their SRE workbook for more details, as they explain the math very well. To briefly cover it, your error budget is how many mistakes you're allowed to make in a given evaluation window. Favor chooses a four-week evaluation window. Depending on how quickly you're consuming that error budget, we set an alarm of proportionate severity. If you're going to burn through your error budget in two weeks or less, that's when we start alerting you.

There is a ceremony that I will go over later that we do every two weeks, so we don't alert based on burning through faster than two weeks. We have an operational process in place to look at services that are degrading without having to page you at 2:00 AM about it.

Now we have our indicators and SLOs, and we need people to actually use them because we want our squads to own their services and the reliability of those services. This led to the ceremony we're covering today and the dashboard we're discussing. 

We have 12 teams covering about a hundred services. We did a kickoff call with all of them, repeating the same call 12 times. We went over what I just shared with you, but in much more detail, and communicated the why and the expectations going forward for this process. 

That kickoff call then led to a biweekly meeting that we do every two weeks. SRE also has a meeting with themselves, and we have one with DevOps because we have that big "dogfood" mentality—if you don't want your product, why would anyone else want it? 

We started this cadence and needed to name the meeting. My boss was very smart and called it the Service Level Operational Readiness Review. Everything in tech needs an acronym, so we chose ORR for Operational Readiness Review.

missed it and my boss was like, "Whatever. It's ORR now." 

So this Operational Readiness Review (ORR) centers around a big dashboard that serves as the single pane of glass and the active report card for all of the services that belong to a team. Of course, being in Grafana Cloud, we have access to Prometheus and AlertManager data, but we can also use something like the Infinity data source to reach out to third-party APIs and get that data serviced as well.

Now, I'm going to go through a little mini ORR with you all so you can see what we're talking about and what conversations are happening there. 

### Incident Follow-Up Screen

This is the first panel we go over with all of our squads. This is just the incident follow-up screen. It reaches out to our third-party Incident Response Management (IRM) tool, connecting to Jira to see the incident follow-ups that are assigned to the squad we're discussing. We ask, "Hey, do you have a Jira ticket for it?" Because if they don't have a Jira ticket, they're not going to put it in their backlog, and they're not going to address it, right? 

We also check if the incident follow-up is about to go past due. Does everyone on this team know that this incident happened, that there's a follow-up for it, and what that follow-up is going to achieve? These are the conversations we're having at this very first panel. 

It may seem like a silly little thing, like, "Oh, here's a list of tickets you need to do," but these tickets are pretty important. When you have an incident, you find a shortcoming, and how many of us have seen a shortcoming not addressed? It often just gets backlogged, forgotten, or deleted. It's not unimportant; that's why we wrote it down.

### Active SLOs for the Squad

The next panel we go to is the active Service Level Objectives (SLOs) for the squad. A few things here: the first one is just the list of SLOs they have configured. You can see two of them are boxed in; those are hyperlinked to an SLO detail panel, a completely different dashboard that breaks down a lot more information about those SLOs. 

You'll also see a panel showing services that are missing SLOs. If a team doesn't have SLOs set up for a service, you want to know why. In this case, they have an API service that's marked as generally available but has no SLOs on it. Probably not a good thing, right? So we put this in front of them, and they go, "Oh, that's a good point. We need to turn them on." 

Typically, when we're doing these reviews, we look at any SLO that has less than 80% of its error budget remaining. That's the guideline for the SRE leading the call to take a closer look at it with the entire squad. We see this team has three services that are below 80%. 

I'm going to go through the two that are boxed in real quick and tell you what we would discuss with them. The first service that had a 37% remaining error budget is for a latency SLO. You can see here that around the 23rd or 24th, something happened; this application slowed down, and it started burning through its error budget. I would ask, "Hey guys, what happened here?" 

Someone will probably say, "Oh, there was a database that was under-provisioned. We had to get more whatever gigawatts to it, and that made it run faster, and now we stop burning through our error budget." That's great. It's a really simple answer, but what's valuable about these conversations is that maybe the two people who fixed it know about it, but the other five people on the team didn't, and now they do. 

Again, it's like a mini postmortem for the whole team, which I think is pretty great. The next SLO we're going over is the availability SLO with them. This one's at 78% of its error budget, but we can all see that the graph is trending upward, which is the right direction. 

A conversation like this might be, "Hey, why did it start going up on the 13th? That's really great." Then someone might say, "Oh, well, we were throwing 500s when we should have been throwing 300s, or we had an unhandled condition that was causing 500s. We added that fix, and now it's throwing valid responses and recouping its error budget." 

This is another instance where someone may not have known on the team, and this conversation now happens amongst the whole team, sharing knowledge about the issue and its resolution.

### Active Alerts

Now we're going back to the ORR dashboard, the main dashboard, and this is the next section we always cover with them: active alerts. Usually, if there's an active alert, the person on call for the team is already aware of it, but sometimes they're not. So we'll go over any actively following alerts for the squad. 

This squad, at this time, has an active alert for one of their custom alerts. Their shopping detector isn't working; that's a cron job that just wasn't running on the schedule they needed to be notified about. The second alert is actually a Grafana out-of-the-box alert. Whenever you implement all of Grafana's features in your Kubernetes cluster, you will get some helpful out-of-the-box alerts. 

In this case, this alert is just saying, "Hey, I'm configured to scrape something for metrics, and it's not there." That could be either on the pod that's presenting the metric or a service monitor that's scraping something that doesn't exist. It just leads to a little follow-up: "Hey, there's some configuration we need to check out."

In the same panel, but in the segment underneath it, we also review past alerts. Alert fatigue is a real thing, and I think we all know that. This is how we proactively try to get in front of it. We look at how many alerts and how many pages the on-call team has received in the past month and ask, "Was this actually helpful? Did you do anything when this went off, or did you just kind of ignore it? How many times have you been ignoring this alert that goes off 30 times a month?" 

If they say, "Every time," I ask, "Can we turn it off? Is there a more helpful version of that alarm that you were trying to accomplish when you made this one initially?" That is the conversation we have there. 

A great stat about alert fatigue that I can share about Favor is that if you look at the past year, our alert volume has gone up 7%, which sounds bad, but our number of services deployed in the cluster has gone up 25%. So our alerts per service have actually gone down quite a bit. 

I'm going to go over the impact on incidents later, but just remember that we are getting fewer alerts per service, and that is helping people sleep through the night, literally. 

### Conclusion

So that's kind of your first little mini ORR. That's not everything we cover in the ORR, but those are the key things that have always been there. Over the past year, we've taken things out and added things in as we've had different priorities in the organization, but those are the meat and potatoes for sure. 

One of the big things the ORR process has helped accomplish is SRE adoption across the organization as a whole. We were a newer team; when I joined, we were only a year old, and now we're about 2 to 2.5 years old. This has gotten all of the engineers in our organization aware of what SRE is, what we're advocating for, what these practices are, and all that good stuff. 

I think another great point to mention is that we only have four SREs against a hundred engineers. I shouldn't say "against," but we have four SREs and a hundred engineers. We don't have the headcount to do the embedded SRE model. That would be really fun, but we don't.

Really, we have the capacity. So this is, I think, the best bang for your buck method that we've kind of found for getting SRE to talk to every team and for every team to talk to SRE. We have SREs on call; whoever is on call that week leads the Operational Readiness Review (ORR) that week. This cycle gets every SRE in front of every squad and vice versa, which helps build that relationship.

From the engineer's perspective, this has probably been one of our most successful cross-team ceremonies in our organization. The data I can share as to why it's successful is that it's still happening over a year later, and people keep showing up. If you do a boring, useless meeting that nobody wants to attend, nobody goes to it. The fact that we still have full teams showing up every other week for this meeting is a pretty good sign that they find what we're presenting to them as valuable.

It's probably the first time that someone really sat down with a team and said, "Here are these principles, and here's how they directly apply to your services." For example, going to a team and saying, "Hey, did you know 95% of your requests take 3 seconds?" and they respond, "It's supposed to take half a second." That's a pretty relevant thing for them to know. It's also really helpful to find out that 10% of your requests are responding with 500s. Again, these are some things that maybe squads didn't know about when we started this process, and it put it in front of them to help them improve.

The decrease in alert volume is also pretty substantial. We've had similar amounts of incidents but fewer critical incidents. I think that's a pretty good thing to acknowledge because a critical incident has a very large business impact. We're talking about the financial impacts of these things. A critical incident has a quantifiable number associated with it internally at Favor, so having fewer of those means we are losing less money.

Another thing that has come out for our engineers with this process is that when we started, one-third of our alerts or incidents were internally reported by the engineering department, and two-thirds were coming from external sources, like customer support or runner support calling us and saying, "Hey, this is broken. Can you fix it?" We've actually flipped that number since then, which I think is pretty huge. Now, if there's an incident happening, there's a two-thirds chance that we found it before a customer or some other third party did.

Another great outcome of this is just general education across the organization. We have an Ask SRE channel. We're a Slack house, and we have an Ask SRE channel where everyone comes to us with their questions. We've gotten in the habit of tracking who's reaching out to us, how frequently, and about what. With this process and by setting aside time to talk about all these principles, we get in front of them with initiatives that are coming out of DevOps, where SRE is very involved, and then we forward the message out in the setting. They get to ask questions about it or about Grafana, or how to set up an alert or a push gateway. All that has resulted in a 30% decrease in questions to our Ask channel, which are all interruptions for the SRE on call. This helps SRE stay more focused on their engineering work and is also a testament to how our teams are more able to self-service than they otherwise would have been.

Okay, that's kind of the benefits that have been there for SRE and the engineering teams. I think another good value for the SRE team is just the feedback loop we've been getting from our engineers with this ceremony. One of the immediate things that was asked from us was, "Can we have more granularity on these SLOs?" Think about a service that has an API endpoint with both a GET and a POST method. The POST method is for uploading data and writing to the database, which may take one to three or one to five seconds, and that's okay. The GET method needs to be around 150 milliseconds latency; it needs to be fast. Our engineers wanted a way to say, "I want to know when the fast API endpoint is slow." Originally, we were just measuring the whole service, and the slow calls were penalizing the fast calls in terms of the SLO evaluation. 

One of the first things we pushed out as a result of these meetings was per endpoint, per method SLOs for latency in particular. Just a quick list of other things that have come out of this includes Front End Observability. I talked a lot about backend stuff and API stuff, and our front end team was getting jealous. They said, "We want some fun Grafana toys." So we set up Faro for them for front end observability.

We also established private load zones for k6 testing. We would go to a team and say, "Hey, your service is too slow under load." They'd ask, "How do we fix it?" and I'd respond, "You do a k6 load test." They'd say, "Okay, but it's a private internal application; it's not accessible to the internet. How do we use that?" So we set up an internal private load zone for them to run these tests and improve the performance of their applications under load without having to test in production.

Other SLOs have also come out of this, such as Kafka consumer groups. Does anyone here have Kafka? Does anyone here think it's super easy to monitor and that you have no problems with it and always know what's going on? Yeah, we got that problem kind of solved as well, at least from a consumer group perspective, because that was a huge ask coming from our engineers.

Lastly, another big thing is some more advanced alert routing, so that if something important happens at 2:00 AM and it can wait until 6:00 AM, it waits until 6:00 AM instead of waking you up at 2:00 AM to write a note and then forget what the note was, Jerry Seinfeld's style with your joke, if you get that reference.

So that's it for me. I hope this helps everyone understand how we use this dashboard as the starting point for a lot of other conversations. It's both a place where our engineers can go and get that initial report card, but it also keeps that intimate feel of a small engineering institution even as it's growing. Thank you all again for having me and bringing my crew over.

## Raw YouTube Transcript

Hi, my name's Kevin Panahi,
I'm here from Favor Delivery. I want to thank Grafana for
hosting me and my team here today. I'm the Senior Site Reliability
Engineer here at Favor. I've been at Favor a
litle bit over a year now, but I've been in the DevOps platform
space for about eight years. And so today we're going to talk about
the operational readiness review that we do here at Favor and how we use Grafana
dashboards as the starting point for a lot of those conversations. So for those of you who don't
know what Favor Delivery is, we are a home grocery and
food delivery service. We operate under the HEB
umbrella. We're Texas only. We're proudly unavailable in 49
states as one of our fun taglines. In the Austin area, you've probably seen the big billboards
advertising like Favor Gold or our Cowboy ads that are going around for
our Texas Two-Stop so that's who we are. Okay. We have a little
bit about the team here. We have 12 squads in our
engineering department, two of which are the SRE and DevOps teams. Both of those teams have four people on
them. A principal on ours, I put Staff, sorry, boss. We have a principal,
two seniors and a mid level, and then we also have our DevOps team, which I point out just because
we work super closely with them. So a lot of what SRE is discussing and
these things is kind of coming from DevOps as well. The rest of them are just our normal
software engineering teams and yeah. Okay. So about Favor. So let me just kind of set where our
monitoring position was when we started or when I started really. We had just gotten
a lot of our service onto Kubernetes, services onto Kubernetes. We were historically kind of a big
Bing stock shop and we moved to Kubernetes and kind of adopted
the microservice architecture. Around the same time we also just
had a huge headcount increase in the engineering department. So we went from
like really small concentrated teams to like the 10 other software
engineering teams adding an SRE team. SRE was a little over a
year old when I joined. And so that's kind of where we went
to. There was a lot of growing pains, big one being just kind of noisy alerts
that weren't very helpful and kind of just paged people and no one know what
to do with them. When I was interviewing, I actually interviewed with one of our
Senior Software Engineers and I just asked like, "Hey, SRE
is this new thing here. Why do you want an SRE department
at your company?" And he said, "I kind of just don't
know what's going on. " And then it's kind of an alarming
thing to hear from somebody. So that's kind of where we were at. So we were trying to find a way to
kind of implement a good solution for most of our services and
get that visibility in there. So we had STO be your superhero for this. STO is a service mesh that operates
inside your Kubernetes cluster. It manages all of our Layer 7
networking traffic within the cluster. Along with SEO, you get
fun things like metrics, might have heard of them
at a Grafana conference. And these metrics communicate the most
important things to us for today is requests response codes. So like
your 200s, 400s, 500 response codes, and also your application latency. So how fast is your service
responding to requests sent to it? SDO is kind of injected as
a side car into our pods, and then that side car is what produces
these metrics that we are reporting and alerting on. Those metrics are then consumed by Alloy
and then shipped to Grafana Cloud where all of the recording rules
and alerts are set up. So we have these metrics and so now we're
going to turn these into service level objectives. So to have an SLO, you need
an SLI or a service level indicator. So thinking about like the four golden
signals that you look at in the SRE world, we started with the two easiest
ones, which are availability and latency. Most of our services are API services,
so this is a pretty good fit for them. For availability, we just looked at all
responses that were not 500 responses. We viewed those as successful and then
500 responses were viewed as failed requests. We measured those from
the perspective of the caller. So if you think of like a client
server, we measured the clients, what the client received. That's just
because if a client's getting 500s, the application didn't work. I don't
care what the application thought it did, this is what it actually did. So that's
the perspective for the availability. For the latency, we actually measured
that from the server perspective. And that was because we didn't want
to penalize a services performance measurements based off
of the wire, so to speak, between the client and the server. There you go. There you go. Okay. Okay. Sorry, it's a little out
of sync. So we have these SLIs, so now we need these objectives.
So at Favor, we have three tiers, tier one being the highest and we set service level objectives
based off the tier the team decides their service belongs to. We really believe that squads should
own their services and they should own how their services are defined. If a squad thinks they have a tier three
service and I think they have a tier one service, they have a tier three
service. It's their decision, not mine. But depending on the tier they
pick is the objective they get. So two 9s for a Tier 3, three 9s for a Tier One and two
and a 1/2 9s for a Tier Two. For the latency, we do 99 all the way down to 90 and again, the latency target itself is also picked
by the squad. So if a squad thinks it's acceptable for a service
to respond in one second, then their latency targets set to one
second. And if it's a tier one service, 99% of the requests need to
happen within one second. Now that we have an objective, we can
then make a burn rate or an error budget. And then with an error budget,
you make a burn rate alarm. Go look at Google's
documentation and their workbook, the SRE work book about this because
they go into all the math and they do it very well. But just to
kind of briefly cover it, your error budget is how many mistakes
you're allowed to make in a given evaluation window. Favor chooses
a four week evaluation window. And then depending on how fast
you're consuming that error budget, we throw an alarm of a
proportionate severity. So if you're going to burn through
your error budget in two weeks or less, that's when we start alerting you. There is a ceremony that I'm going to
go over later that we do every two weeks so we don't alert based off of burning
through faster than two weeks because there's kind of an operational process
in place that we can kind of look at services that are degrading without
having to page you at 2:00 AM about it. So that's kind of what we do there. Okay. We have our indicators. We have our SLOs and now we
need people to actually use it because again, we want our squads to own their services
and own the reliability of their services. So that led to the ceremony we're
covering today and the dashboard we're covering today. Again, we have 12 teams
covering about a hundred services. We did a kickoff call with all of them. We did the same call 12 times and we went
over what I just went over with y'all, but in a lot more detail and then
also communicated like the why and the expectations going
forward for this process. That kickoff call then led to a biweekly
meeting that we do every two weeks. SRE also does one with themselves. We also do one with DevOps because
we kind of have like that big dogfood mentality, like you eat your own dogfood at Favor
to make sure that if you don't want your product, why would anybody else want it? So we started this
cadence, we had a meeting, we needed to name the meeting
and my boss was very smart. He called it the Service Level
Operational Readiness Review and everything in tech needs an acronym. And so you can think
we're talking about SLOs. We have a service level operational
readiness review and the acronym we chose was ORR for Operational Readiness Review. Completely missed it. Everyone missed
it and my boss was like, "Whatever. It's ORR now." So this operational readiness review centers
around a big dashboard that kind of is the single pane of glass and like
the active report card for all of the services that belongs to a team.
Of course, being in Grafana Cloud, we have access to like the
Prometheus and the AlertManager data, but then we can also use something like
the Infinity data source to reach out to third party APIs and get
that data serviced as well. So now I'm going to go through a little
mini ORR with y'all so you can kind of see what we're talking about and what
conversations are happening there. So this is the first panel we
go over with all of our squads. This is just the incident
follow-up screen. So this actually is reaching out to our
third party IRM, reaching out to Jira, seeing the incident follow-ups that are
assigned to the squad we're talking to and then saying like, "Hey, do
you have a Jira ticket for it? " Because if they don't
have a Jira ticket for it, they're not going to put it in their
backlog and they're not going to do it, right? Is your incident
follow-up about to go past due? Does everyone on this team know that
this incident happened and that there's a follow-up for it and what that follow-up
is going to achieve?" These are like the conversations we're having
at this very first panel. So it seems like a silly
little thing like, "Oh, here's a list of tickets you need to do. " But these tickets are pretty
important because you have an incident, you find a shortcoming and how many of
us have seen a shortcoming not addressed? It kind of just gets backlogged and never
talked about or forgetting or deleted or it's not important. It's
like, no, it's important. That's why we wrote it down. The next panel we'll go to is
the active SLOs for the squad. So a few things here. The first one is just the list
of SLOs they have configured. You can see two of them are boxed in. Those are hyperlinked
to an SLO detail panel, a completely different dashboard that
breaks down a lot more information with those SLOs. We're going to
cover those here in a second. The other panel you'll see on here is
actually services that are missing SLOs. So if a team doesn't have
SLO set up for the service, you kind of want to
know why. In this case, they have an API service that's marked
as generally available and has no SLOs on it. Probably
not a good thing, right? So putting this in front
of them and they go, "Oh, that's a good point when
you go turn them on. " We kind of have an
automated setup for them. Let me actually go back.
Typically, when we're doing these, we look at anyone, any SLO that has less
than 80% of its error budget remaining. That's kind of the guideline for the
SRE leading the call to take a look at it in more detail with the entire squad. So we see this team has three
services that are below 80%. I'm going to go through the two that are
boxed in real quick with y'all and kind of tell you what we would
talk about with them. The first service that had a 37%, 38% remaining error budget
is for a latency SLO. So you can see here that around
the 23rd, 24th, something happened, this application slowed down, it started burning through its error
budget and I would be like, "Hey guys, what happened here?" And then
someone will probably say, "Oh, there was a database that
was under provisioned. We had to get more whatever
gigawatts to it and that made it run faster and now we stop
burning through our error budget." And that's great. It's
a really simple answer, but I think what's really valuable about
these conversations is that maybe the two people that gave it the
gigawatts know about it, but the other five people on
the team didn't and now they do. And again, it's like that mini postmortem for the
whole team to have there that I think is pretty great. The next SLO we're going over is
the availability SLO with them. This one's at 78% of its error budget, but we can all see that
graph's going up to the right, that's the right direction. A
conversation like this might be, "Hey, why did it start going up
into the right on the 13th? That's really great." And then some
guy comes in and he's like, "Oh, well, we were throwing 500s when we
showed throwing 300s or we had an unhandled condition that we were receiving
and it was throwing 500s and we added that fix and now it's throwing
valid responses and it's recouping its error budget." So again, this is another time where someone
maybe didn't know on the team and this is like a conversation that now
happens amongst the whole team of like there was this issue, it was resolved
and it's a knowledge sharing thing. So now we're going back
to the ORR dashboard, the main dashboard and this is the
next section we always cover with them. We cover active alerts. Usually
if there's an active alert, the person on call for the
team is already aware of it, but sometimes they're not. So we'll go over any actively
following alerts for the squad. This squad at this time is having an
active alert for one of their custom alerts. Their shopping
detector isn't working. That's a chron job that they have that
just wasn't running a schedule that they needed to be notified about. And then the second alert is actually
like a Grafana out of the box alert. So whenever you implement all of
Grafana's fancy stuff in your Kubernetes cluster and everything, you will get
some helpful out of the box alerts. In this case, this
one's just saying, "Hey, I'm configured to scrape something for
metrics and it's not there." And that could be either on the
pod that's presenting, the metric isn't presenting
it when it should be, or we have a service monitor that's like
scraping something that doesn't exist, but it just leads to a
little follow up, "Hey, there's some configuration
thing we need to check out." And then same panel, but the segment
underneath it, we also review past alerts. Alert fatigue is a real thing.
I think we all know that. This is how we proactively
try to get in front of it. We look at how many alerts, how many pages the on-calls for the
squad we're talking to has gotten in the past month and we just say,
"Was this actually helpful? Did you actually do anything when this
went off or did you just kind of ignore it? How many times have you been ignoring
this alert that goes off 30 times a month?" And they're like, every time
I was like, "Can we turn it off? Is there a more helpful version of that
alarm that you were trying to accomplish when you made this one initially?"
That is the conversation we have there. A great stat, I think about alert fatigue that I can
tell you about Favor is if you look at the past year, our alert volume's
gone up 7%, which sounds bad, but our amount of services
we have deployed in cluster
has gone up 25%. So our alerts per service has
actually gone down quite a bit. I'm going to go over the
impact on incidents later, but just kind of remember that we are
getting less alerts per service and that is helping people sleep
through the night, literally. So that's kind of like
your first little mini ORR. That's not everything we cover in the ORR, but those are the key things that have
always been there in this past year. We've taken things out. We've added things in as we've had
different priorities in the organization, but those are the meat
and potatoes for sure. One of the big things the ORR process
has helped accomplish is just SRE adoption, the organization as a whole.
We were a newer team. When I joined, we were only a year old and now
we're only about two, 2.5 years old. This has gotten all of the engineers
in our organization aware of what SRE is, what we're advocating
for, what these practices are and just all that good stuff. I think another great thing to point
out is we only have 4 SREs against a hundred engineers. I shouldn't
say against, but 4 SREs
and a hundred engineers. We don't have the headcount to do the
embedded SRE model. That'd be really fun, but we don't really have the
capacity. So this is, I think, the best bank for your buck method that
we've kind of found out of getting SRE to talk to every team and
every team to talk to SRE. We have SREs are on call. Whoever is on call that week
is who leads the ORR that week. So that cycle gets every SRE
in front of every squad and vice versa, kind of helps
build that relationship. From the engineer's perspective, this has probably been one of our most
successful cross-team ceremonies in our organization. I think the data I can tell you as
to why successful is that it's still happening over a year later and people
keep showing up because if you do a boring useless meeting that nobody
wants to go to, nobody goes to it. So the fact that we still have full teams
showing up every other week for this meeting, I think is a pretty good sign that they
are finding what we're presenting to them as valuable. It's probably the first time that someone
really sat down with a team and said, "Here are these principles and here's how
they directly apply to your services." Going to a team and saying, "Hey, did you know 95% of your requests
take 3 seconds?" And they're like, "It's supposed to take half a second."
That's a pretty relevant thing for them to know. It's also really helpful to
find out that 10% of your requests are responding with 500s. Again, these are some things that maybe squads
didn't know about when we started this process and it put it in front of them
to help them make a lot of that better. The decrease in alert volume is also
pretty substantial. We've also had similar amounts of incidents
but less critical incidents. I think that's a pretty good thing to
acknowledge there as well because a critical incident has a
very large business impact. We're talking about the financial
impacts of these things earlier. A critical incident has a quantifiable
number associated to it internally with Favor and so having less of those
means we are losing less money. Another thing that's kind of come out
for our engineers with this process is when we started it, 1/3 of our alerts or 1/3d of our
incidents were internally reported by the engineering department and 2/3s
were coming from external sources. So think like customer support or runner
support calling us and saying, "Hey, this is broken. Can you fix it? " We've
actually flipped that number since then, which I think is pretty huge. So now if
there's an incident that's happening, there's a 2/3 chance that we found
it before a customer or some other third party did. Another great thing that's coming
out of this is just general education across the organization. We have an Ask SRE channel. We're a Slack
house and we have an Ask SRE channel. Everyone comes to us,
asks us their questions. We've gotten in the habit of
tracking who's reaching out to us, how frequently and about what. And with this process and kind of setting
out the time to talk about all these principles and get in front of them with
maybe an initiative that's coming out of DevOps and SRE is very involved
with DevOps and then forwards the message out in the setting. They get to ask questions about it or
they get asked questions about Grafana or how do I set up an
alert or a push gateway? All that stuff has resulted in a 30%
decrease in questions to our ask channel, which are all interrupts for the SRE on
call. So that's kind of helping SRE stay more focused on their engineering work. And it's also kind of a testament to how
our teams are more able to self-service than they otherwise would've been before. Okay, that's kind of like the benefits that's
been there for SRE and the engineering teams. I think another good value for the SRE
team is just the feedback loop that we've been getting from our
engineers with this ceremony. So one of the immediate things
that was asked from us is, can we have more
granularity on these SLOs? Think about a service that has an API
endpoint that has both a get and a post method. The post method is like uploading data
and it's like writing to the database and maybe it takes one to three, one
to five seconds and that's okay. The get method needs to be like 150
milliseconds latency. It needs to be fast. Our engineers wanted just
kind of a way to say, "I want to know when the fast API
endpoint is slow without..." And whenever we originally were just
measuring the whole service, the slow calls were penalizing the fast
calls in terms of the SLO evaluation. So one of the first things we pushed out
as a result of these meetings is just per endpoint per method SLOs
for latency in particular. Just a quick list of other
things that have come out of this Front End Observability. I
talked a lot about backend stuff, a lot about API stuff. Our front end
team was getting jealous. They said, "We want some fun Grafana toys." And
so we set up FARO for them front of observability through that.
Private load zones for K6 testing, we would go to a team, you say, "Hey, your service is too slow
under load." They're like, "How do we fix it?" And I'm like, "You
do a case six load test." And they say, "Okay, but it's a private
internal application. It's not accessible to the
internet. How do we use that? " So setting up an internal private
load zone for them to run these tests through and improve the performance of
their applications that are load without having to test in prod. Other SLOs have also come out
of this, Kafka consumer groups, anyone here have Kafka, anyone here think it's super easy to
monitor and you have no problems with it and you always know what's going on? Yeah. So we got that problem
kind of solved as well, at least from a consumer
group perspective, because that was a huge ask
coming out of our engineers. And then lastly, the other big thing is some more advanced
alert routing so that way if something important happens at 2:00 AM
and it can wait till 6:00 AM, it waits till 6:00 AM instead of
you having to wake up at 2:00 AM, write a note and then
forget what the note was, Jerry Seinfeld's style with your
joke if you get that reference. So that's it for me. I hope this kind of helps
everyone understand how we
use this dashboard as the starting point for a lot
of other conversations. It's both a place where our engineers
can go and get that initial report card, but also just kind of keeping
that intimate feel of a small engineering institution
even as it's growing there. So thank you all again for having me
and bringing my crew over and yeah.

