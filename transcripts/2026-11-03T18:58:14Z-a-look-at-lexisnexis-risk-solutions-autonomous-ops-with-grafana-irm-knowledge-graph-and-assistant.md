# A Look at LexisNexis Risk Solutions&#39; Autonomous Ops with Grafana IRM, Knowledge Graph, and Assistant

Published on 2026-11-03T18:58:14Z

## Description

When an alert fires at LexisNexis Risk Solutions, an incident is opened, ServiceNow syncs, a Grafana Assistant investigation ...

URL: https://www.youtube.com/watch?v=nEDLjuRMaK4

## Summary

The show titled "A Look at LexisNexis Risk Solutions' Autonomous Ops with Grafana IRM, Knowledge Graph, and Assistant" was published on November 3, 2026. The speaker, Neil Wilson, a Senior Director of Software Engineering at LexisNexis Risk Solutions, discussed the company's journey in implementing Grafana for observability and incident response. Key topics included the transition from on-premises systems to Azure, the use of Grafana's Incident Response Management (IRM) and Knowledge Graph, and the importance of context in incident management. Wilson emphasized that understanding data and relationships is crucial for effective automation and incident resolution, leading to significant improvements in response times.

Topics: Grafana, LexisNexis Risk Solutions, observability, incident response, automation, context, Azure, Knowledge Graph.

## Chapters

00:00:00 The journey of observability at LexisNexis Risk Solutions
00:06:11 Understanding system alerts and context
00:11:47 Improving telemetry with Grafana Fleet Management
00:18:08 Improving alert management with a monorepo approach
00:23:45 Understanding incident resolution with Grafana Assistant

My name's Neil Wilson. I'm a senior director of software engineering at LexisNexis Risk Solutions. Today, I'm also on Grafana's customer advisory board. Some of what you will see today, we had the opportunity to help guide and build, and we also learned a lot of hard lessons along the way that I'm going to share with you.

LexisNexis Risk Solutions shows up anywhere that risk is part of the question that customers are trying to answer. This could be in healthcare, insurance, government, business services, banking, and many other areas. Let me tell you a little bit about what that actually looks like in my part of the world. In the minute or so that I've been talking here, about 2,000 insurance transactions have flowed through our systems and hit our front door. That's a typical Tuesday at five o'clock Pacific, which means the East Coast has already started to slow down, get off work, and enjoy their evenings. Almost all of that traffic is tied to a real person making a live transaction, perhaps needing to get an auto claim because they were in an accident, or a decision being made by a healthcare provider. The point is that all those transactions involve a real person waiting on a response that's accurate and also quick. 

But that's just one of our markets. In reality, we have products that span 190 different territories and countries globally. As we expand, the demand on our systems gets quite a bit more intense. The bottom line is that behind each of these transactions is a real person like you and me, waiting on a decision that could change the way their life is going to go. So when we're slow or inconsistent, a quote, a claim, or maybe a medical decision could be impacted. That's why, to us, seconds matter during an incident.

I was asked at the last minute to put in a personal interest slide. I've seen a lot of things about being outside and active, so I thought I'd go a different direction. If you want to go down the Magic of the Gathering rabbit hole with me sometime, you're more than welcome to, but we would burn the whole session if I do it now. So you can talk to me about that or this session later on if you see me around.

Now, I want to start with something that happens in our environment today: an alert fires. Here's what happens next. An incident gets created in Grafana, ServiceNow gets synced to it, we have an assistant investigation kickoff, and our on-call team gets paged. We also have a Microsoft Teams Bridge open, but no human triggered any of that. This sounds like it's a story about automation, but it isn't. The hardest part of autonomous operations is not the automation; that's the easy part. The hardest part of an investigation is rarely a lack of data; it's having the correct context for making the decisions that you're trying to make.

I want to rewind about four years ago. We were running on-prem and getting ready to move to the cloud. We had logs that we were sending to an ELK stack that we self-hosted, and we were trying to move to Azure with all of our services. The plan was to migrate to Azure Log Analytics as our observability platform. After that, we did a one-month proof of value with Grafana, and it changed the course of our observability from then on. We made a really hard pivot on our observability strategy in the middle of our cloud migration. 

The question you might be asking is, why does that matter? Why did we do anything? Back then, the question we were trying to answer was really, can we see what's happening in our own systems? The six steps here that are faded out represent the journey we went on over the last four years with Grafana, and we'll come back to them at the end of the talk. The thing I want to keep in mind for all of you is that we skipped a couple of steps along the way.

We started at step one. We onboarded with Grafana, got logs, metrics, and traces, and added correlation, so things were going well. Then we did part of step two, where we added some of the labels that give our services their identity. At the time, we had some custom labels from our ELK stack days, and we just carried those forward without realizing the impact that would have. Then we jumped all the way ahead to step six: incident response.

Now, I mentioned that we were trying to go live in Azure. We had a go-live day communicated to customers and were ready for it. The thing is that our on-prem data centers picked a different day for us. So we actually made a strategic failover to Azure and never came back. There's a great story there if you want to talk to me about that later too, about why you practice your go-lives.

Once we got into Azure and had our incident response pretty well dialed in, we went back to step two and started filling in the gaps. We moved to OpenTelemetry Semantic Conventions, which is an ongoing journey, and filled in the knowledge graph. We started being able to get the context about which customers were being impacted by the incidents we were having. Getting GitHub into the mix for the knowledge graph was also really important to us. Finally, we focused on investigations.

With all that in mind, for us, that changed the question. What we needed was to be able to answer, can the system understand what's happening and tell us? So we sat down and mapped out what we would actually need to do to be able to answer that question consistently. We categorized our findings into signals, context, reasoning, and action. 

Signals tell us what is actually happening in the system. The context layer tells us what any of that means. Reasoning is about what we should investigate, and finally, action is what we do next with all that data. Within those buckets are the same six steps I had on the previous slide. The important point here is that context has three of those steps; it's a much larger bucket. This is crucial because we found that this is where you really need to invest your time and effort in order to achieve truly resilient automation.

When we look at how we prioritize work, we follow the pattern of detection, understanding, and decision. Do we know what's happening? Do we know what it means? What does that lead us to actually do? It's tempting to skip the middle, going from signals to action, but understanding your data and your relationships is table stakes, and the rest of these fall down without it. 

So that's what this talk is really about: the middle and how we actually built it step by step. As we moved into Grafana, I mentioned we had to jump to action, which is the last step of the process. Our services were live running in Azure now, so operations and action had to take priority. We were running in a net new environment, and it was a little bit ahead of schedule. 

In the early days of the cloud, when something broke, it would take us roughly 10 minutes just doing logistics: getting the right people on the call, figuring out who owns the service, getting them on the call, making sure ServiceNow tickets were open, and getting an investigation going once that was introduced by Grafana a couple of years ago. We had the alerts firing, but the thing that was missing was the context for that alert. We knew what pod was crashing or what service was having issues, but that sometimes isn't the whole picture or the only issue that you have to mitigate that night.

To solve this, our ITSM engineering group built what we call our first responder. Ultimately, what it does is start with the alert rules themselves, which live in a centralized alerts repository. The labels that we...

**Apply to Alerts**

The alerts are very structured, allowing us to know specifically who owns the alert and which service is having a problem. It includes the environment, the severity of the alert using a curated list of values, and ultimately, the annotations carry information like the runbook, which is a resolvable URL, dashboards, and other fields that get mapped into ServiceNow. We use our labels as the routing table for how we kick off all of our automations. However, at the end of the day, this isn't making decisions on how we fix the problem; it's solving our logistics, which was really where we were feeling the most pain.

The labels route it, Grafana Incident Response Management (IRM) opens the incident, pages the on-call team, and we end up having ServiceNow tickets opened and synced with Grafana's incident through the invitations on the alerts. This process gets people on the bridge in one to two minutes now, reducing our response time by eight to nine minutes, which is a significant improvement. However, having a bridge open doesn't mean that the teams have the context they need to be effective. 

Now, if the people in the bridge need context, so does AI, and that starts with the data. Just a quick show of hands—have you ever worked with an engineer or been that person who said, "My service is unique for some reason. Yeah, we do things this way for valid reasons, right?" Me too. But while your service may be a unique snowflake, that doesn't necessarily mean it's a good thing; it's usually not in IT. 

Here's the thing about snowflakes: they're all built on the same six-sided structure. They're unique on the inside, but if you zoom out, they all look the same, right? No two are alike. The takeaway here is that unique doesn't need to mean unstructured. If you consider unique services, you have different code, teams, architectures, release cadences, and so on, but underneath each of them is the same six-sided structure. In our world, that became a common telemetry language.

If I were to do it again, this would have been day one—focusing on getting rid of our custom labels and aligning to OpenTelemetry (OTel) semantic conventions first and foremost. We don't need every service to behave identically; we just need to ensure that every service describes itself reliably and consistently.

**How We Fixed the Data**

Ultimately, this comes down to a two-part answer: how did we fix the data, and what capabilities did that unlock for us? To fix the data, we used Grafana Fleet Management to apply labels in bulk across our entire fleet consistently. We started with collectors—this was before our current setup. Our collectors were being set up by hand, with a human involved in that process, leading to inequitable config drift despite our best attempts. Our pipeline changes for some of our more complex or larger environments could take weeks to get through to production, making it a very slow process to iterate and find new opportunities for improvement.

Now, every one of our collectors is configured through a single monorepo using a GitOps approach. Our core Site Reliability Engineering (SRE) team owns that common pipeline. This means that 95% of our Alloy configs are consistent and kind of immutable. The remaining 5% allows each team to update the config for their specific services. Today, we have over 40 teams that can configure their own namespaces, apply filtering, and apply the labels that matter for them while still allowing us to maintain a consistent language to describe our services.

Every change goes through a pull request (PR) automation workflow where it links, validates, and provides a preview of what's going to be deployed into the fleet of collectors along with a scope. If that PR fails, it simply doesn't deploy. Once it does, Fleet Management takes that config, builds it for each of our teams, and ultimately deploys it out into our set of collectors. Those collectors are set up to hot reload their configs every 60 seconds, meaning we have no downtime for changes to our collectors, unless we've missed something in configuration.

Everything lands in Grafana Cloud, speaking one consistent telemetry language, which is what the knowledge graph ultimately builds on. Because my core SRE team owns that common pipeline, that's exactly where we fixed the labels. We took the custom labels, kept them, but dual emitted the OTel semantic conventions for service name, namespace, and so on. This doesn't increase our cardinality at all because it's a one-to-one mapping, and that's how we're going to slowly and safely migrate our teams over to a more structured language. This gives them a lot of freedom; they can continue to work and iterate without breaking the stuff that everyone relies on at 4:00 AM.

What this really meant for us is that our pipeline changes went from taking weeks in some cases to just a couple of minutes. This is a huge win for us because not only do we have much more control over the pipelines, but we can rapidly roll them out and also roll them back. We stopped paying a configuration tax on every new feature we wanted to enable. If we wanted to add a node exporter, that's a simple config change, a PR, human approval, and a push, and within a couple of minutes, it's out there.

**What This Bought Us**

Before all this, we had the same service showing up as maybe different entities. Nothing would tell those platforms where those things actually ran. Afterwards, with consistent naming and labels in place, Grafana can now recognize those entities, how they connect, and ultimately that's the knowledge graph. Services, databases, connectivity, data transfer—all that comes in out of the box. 

Where we're going next is completing some of the metadata, mapping ownership to the correct on-call teams. We currently have our own ownership registry, and we're moving it to Backstage. The goal is for the graph to always know what is having a problem and who owns it, ensuring that we have every team impacted on the call, not just the first.

**Takeaway**

If I can go back, the takeaway is that our telemetry didn't suddenly become more accurate; it became more understandable. This is a blown-up view—a real slice of our knowledge graph in production. Not shown here are the 54,000 entities we have, 90 Kubernetes clusters, almost 14,000 services, and so on. Actually, I checked this; it's about two weeks old, and we're about 10% more than that today. Nobody on a bridge call can hold that much information in their heads, but the graph does, and so does the assistant. By feeding the graph good clean data, we get actionable insights from it, but we also have to ensure that our alerts are up to the same standard.

We took a very similar approach for our alerts as we did for our telemetry. We established one standard and moved it to a monorepo to enforce this at the source. We used to manage our alerts with Terraform, which seemed like a good idea at the time, but Terraform is kind of like a Swiss army knife. It's good for certain things, but it can cause other downstream issues if you're not careful, and it can be pretty lengthy.

By having these Terraform repos spread out for each individual team, we had a lot of pipelines, a lot of reviewers, and a lot of different ways to label our alerts. Now, with a monorepo, we have one alerts repo with a folder per team. The takeaway is that the app teams and leads still own these repos and have responsibility for them, but we have the ability to help them make changes in bulk and ultimately put guardrails in place that ensure they align with the standards we need them to meet.

So imagine it's what, 5:30, so maybe in 11 hours or so, it's 4:00 AM tomorrow, and one of you gets paged. The page is from one of the alerts that you're managing within your ecosystem. In our world, our alert repository ensures that we have all of the context and all of the information that you're going to need at 4:00 AM available out of the box because it won't deploy otherwise. 

That means that you have **Runbook URLs** that actually will resolve. You have the correct ownership assigned to it, attributed, and you have the correct service name and namespace, so it ties back to the graph. You get a summary of what is failing and what the alert actually is as that little blurry short line that you're reading as you're waking up. 

Getting there meant that we had an opportunity to clean up as well. So as we went to this monorepo, we went from having about 6,000 custom alerts. We reduced it by 2,000 and counting. What we found is we had a lot of duplicates, a lot of things that were maybe misconfigured or old, and a lot of paused alerts, which was a surprise. Ultimately, that means less noise, more signal, and we can find opportunities to get better.

Another thing I'll call out that this gave us the opportunity to do: Grafana has some amazing out-of-the-box alerts for some of their integrations. They really do. The but here is that some of the pending periods are not quite what we want them to be. They're a little bit longer than we'd like. So what we've done is take those out-of-the-box alerts. They're all in open source, and we have an automation that will pull them down and allow us to configure the things that we need to be customized. 

If you change them in Grafana, the next time that the integration gets updated, we found it would get overwritten, and it happened once or twice to us. What we're doing next and actively is using AI, including their investigation, to go and pull our previous investigations and say, "Where do we have blind spots? Where do we have gaps? What's missing that we aren't looking for yet?"

To dig in that a little bit, we also looked back at our prior investigations, and while they were already bringing a lot of value, we found that there was still some room to improve. Ultimately, that meant that we found gaps in our data. Systems investigations had access to metrics, logs, and traces. It had the knowledge graph, which was great. We're cleaning it up, we're getting better data feeding in, but we had some blind spots around specifically our database layer and Azure Monitor. 

So we partnered with Grafana on database observability and we asked for Azure Monitor to be made available in the assistant. Grafana shipped it within about a month, which was a really quick turnaround. Once that data was in the mix, we immediately started seeing things getting easier to line up. The dots were connecting faster, and our root cause came a lot more quickly. 

The incident I'm about to show you is a good example of why that mattered. We had a wave of latency alerts across several of our products, plus a max connection warning that was flaring up on Database A. We had two different alerts in two different domains, so to speak, and our teams were starting down two different paths to investigate. We suspected that Database A was the problem; that's where the alert was. 

Meanwhile, the assistant checked too. Database A really was saturated, and that was tied to our product alerts, but it was only the symptom. The answer was hiding where none of us were looking yet—in Database B. In reality, the total connections made to Database B were up by 86%, and our database observability data is what surfaced that insight for us. The app logs are what connected the dots for us. 

What the assistant found during the investigation was that Database B was timing out, and retries were piling up, which was causing the real issue that was connected back to Database A—something that our alerts missed. We had essentially a retry storm. It was feeding on itself, and when we threw the assistant at it, it took six minutes for the assistant to find what probably would have been an hours-long investigation for us. 

We started asking follow-up questions after the incident. Could we have caught this sooner? What would have exposed it? What we found is that we had an alerting gap, and the assistant helped us fill it. 

Snowflakes: every service is unique, and they're all built in the same structure. Related services get pulled together and called a snowball, so to speak, and that's what we consider maybe a larger platform. But the snowmen in this analogy is the relationship across those platforms. That's the incident, and that's the type of structure that the knowledge graph is giving us the ability to derive. That bonding has a name; it's called centering, so that's your fun fact for the day. 

The thing I also want to call out is that the flakes are staying individual; they're just now connected. So Database A was the snowman for us, and it was on the snowman, and it was where everybody was looking, but that wasn't what held up the whole incident. 

Now, this is the actual Grafana timeline from that incident. This is a real thing that happened to us earlier this year. On the left here is what was actually alerting: Database A. Connections are climbing from 6,000 to 8,000, and warnings were firing right alongside of it. On the right is what wasn't alerting: Database B. That's where the connection growth was hiding. 

Here's the retry storm. So confirm two things: Database A's alerts were actually firing, and they were real, but they were just the symptom. Database B is what caused our product alerts. Here's the actual investigation and the hypotheses that were being disproven, a couple of names redacted. 

Context lives outside of Grafana as well. We're big fans of Grafana's big tent philosophy. You connect to your data where it lives without moving it, but some of the most useful context doesn't live there, and in our case, it can't. GitHub's a good example of where we've now connected through GitHub MCP, our GitHub source repo to our investigations. So releases and other product activities show up right alongside the telemetry. 

But that data that can't be part of Grafana is things like WorkIQ, which is Microsoft's knowledge graph, so to speak, or some of the data that comes out of Copilot. So instead, we turn the big tent kind of inside out. By using GCX from tools like GitHub Copilot, we're able to utilize GCX as a tool and bring the Grafana data to us locally. 

So back in 2023, an alert gave us a signal. Today, that starts a response, and it's the middle that makes a difference: identity, reasoning, relationships. Now, when we started our journey, most of that middle didn't exist yet. We were aligning our data to shared standards while Grafana was building the tools often with customers like us. 

Now that the middle is there, our engineers arrive with context already in hand. They are engaged immediately when on-call is paged, and we are eight minutes faster remediating our incidents. 

Now, I've been talking about snowflakes like it's Christmas time, but Christmas is not coming up. Halloween is. The takeaway is that this has actually brought in a costume the entire time. What I really want you to take away is that without having full context for your data, you're going to miss the thing that might be right in front of you, and that could be the thing that actually matters during an incident. 

So if I could give you one piece of advice: don't jump to step six; don't skip to action. You have to make sure that you get your context right. The difference between detection and decision is context. Consistent telemetry creates context. Context enables reasoning, and reasoning enables useful automation. Thank you very much.

## Raw YouTube Transcript

My name's Neil Wilson. I'm a senior director of software
engineering at LexisNexis Risk Solutions. And today I'm also on Grafana's
customer advisory board. So some of what you guys
are going to see today, we had the opportunity
to help guide and build, and we also learned a lot of hard lessons
along the way that I'm going to share with you. LexisNexis Risk Solutions, we show up anywhere that risk is part of
the question that customers are trying to answer. That could be in
healthcare, insurance, government, business services, banking,
a lot of other areas. But let me tell you a little bit about
what that actually looks like in my part of the world. In the minute or
so that I've been talking here, there's been about 2,000 insurance
transactions that have flowed through our systems and hit our front door. That's a typical Tuesday
at five o'clock Pacific, and that means the East Coast has already
started to slow down and get off work and start to enjoy their evenings. Almost all of that traffic is tied
to a real person making a live transaction, some decision about needing
to get perhaps an auto claim, maybe they were in an accident, or there's a decision being
made by a healthcare provider. The point is that all those transactions
is a real person waiting on a response that's accurate and also quick. But that's just one of
our markets. In reality, we have products that span 190 different
territories and countries globally. So as we expand, the demand on our systems
gets quite a bit more intense. But again, the bottom line is that behind each of
these transactions is a real person like you and me that's waiting on a decision
that could change the way that their life is going to go. So when we're
slow or inconsistent, a quote, a claim, maybe a medical decision could
be impacted. So that's why to us, seconds matter during an instant. Now, I was asked at the last minute to kind
of put in a personal interest slide and I've seen a lot of things
about being outside and active, so I though I'd go a
different direction. So if you want to go down in the Magic
of the Gathering rabbit hole with me sometime, you're more than welcome to, but we're going to burn the whole session
if I do it now. So you can talk to me about that or this session
later on if you see me around. Now, I want to start with something
that happens in our environment today, an alert fires. But
here's what happens next. An incident gets created in Grafana.
ServiceNow gets synced to it. We have an assistant
investigation kickoff. We end up having our on-call team
getting paged and we have Microsoft Teams Bridge open, but no human
triggered any of that. So this sounds like it's
a story about automation. It isn't. The hardest part of autonomous
operations is not the automation. That's the easy part. And the
hardest part of an investigation, it's rarely a lack of data. It's having the correct context for
making the decisions that you're trying to make. I want to rewind about four years
ago. We were running on-prem. We were getting ready to move
to the cloud. We had logs. We were sending them to an ELK stack
that we self-hosted and we were trying to move to Azure with all of our services. The plan was then to migrate to Azure
log analytics as our observability platform. After that, we did a one month proof of value with
Grafana and it changed the course of our observability from then on. We made a really hard
pivot on our observability
strategy in the middle of our cloud migration. But the question might
be asking is why? Why does that matter? Why did we do anything? Back then, the question we were trying
to answer was really, can we see what's happening in our own
systems? I mean, it makes sense, right? The six steps here that are faded out
are really kind of the journey that we went on over the last
four years with Grafana. And they were going to come
back at the end of the talk. The thing I want to keep in mind for
all of you is that we skipped a couple steps along the way. So
we started at step one. We onboarded with Grafana. We
got logs, metrics, and traces. We added correlation, so things were
going good. Then we did part of step two, where we are adding some of the labels
that give our services their identity. At the time, we had some custom
labels from our ELK stack days, and we just carried those forward and
didn't realize the impact that was going to have. And then we jumped
all the way ahead to step six, incident response. Now, I mentioned
that we were trying to go live in Azure. We were moving from on-prem. We had a go-live day communicated to
customers and we were ready for it. The thing is that our on-prem data
centers picked a different day for us. So we actually made a
strategic failover to Azure and we never came back. And there's a great story there if you
want to talk to me about that later too, about why you practice your go-lives. Now, once we got into Azure and we had our
incident response pretty well dialed in, we went back to step two there
and we started filling in the gaps. We moved to OpenTelemetry
Semantic Conventions, and that's an ongoing journey and
filled in the knowledge graph. We started being able to get the
context about which customers are being impacted by the incidents
that we're having. Getting GitHub into the mix
for the knowledge graph as
well was really important to us. And then finally,
investigations. With all that in mind, for us that changed the question. What
we needed was to be able to answer, can the system understand
what's happening and tell us? So we sat down and we mapped out what
would we actually need to do to be able to answer that question consistently?
And we map into these categories. Signals here, they tell us what is
actually happening in the system. The context layer tells us
what does any of that mean? Reasoning is what should we investigate? And then finally action is with
all that data, what do we do next? Now within those buckets are those same
six steps that I had on the previous slide. But the thing I want to point out here
is that context has three of those steps. It's a much larger bucket and that's
really important because for us, we found that that's where you really
need to invest your time and your effort in order to get truly
resilient automation. And when we look at how we
think about prioritizing work, detection, understanding, decision, that's kind of the pattern that we follow
for everything that we do. Do we know what's happening? Do
we know what it means? What does that lead us to actually do? Now it's kind of tempting to skip the
middle, going from signals to action, but understanding your data and
understanding your relationships is table stakes and the rest of
these fall down without it. So that's what this talk is really about, the middle and how we
actually built it step by step and snowmen sort of. So as we moved into Grafana, I mentioned we had to jump to action
and that's the last step of the process. Our services were live
running in Azure now, so operations and action
had to take priority. We're running in a net new environment
and it was a little bit ahead of schedule. In the early days of
the cloud when something broke, it would take us roughly 10
minutes just doing logistics, getting the right people on the call,
figuring out first who owns the service, then getting them on the call, making
sure ServiceNow tickets were open, getting an investigation going once that
was introduced by Grafana a couple of years ago. We had the alerts firing and the thing
that was missing was the context for that alert. We knew what pod was crashing or
what service maybe was having issues, but that sometimes isn't the whole picture
or the only issue that you're going to have to mitigate that night.
So the way we solve for this, our ITSM engineering group built
what we call our first responder. Ultimately what it does is it starts
with the alert rules themselves and those live in a
centralized alerts repo. The labels that we apply to these
alerts are very structured so that we know specifically who owns the alert
and the service that's having a problem. It includes the environment, the severity for the alert
using a curated list of values. And ultimately the annotations
will carry things like the runbook, which actually is a resolvable URL, dashboards and other fields that
then get mapped into ServiceNow. So we use our labels as the
routing table for how we kick off all of our automations.
But at the end of the day, this isn't making decisions
on how we fix the problem. It's solving our logistics, which was really where we
were feeling the most pain. So the labels route it, Grafana IRM
opens the instant, pages are on call. We end up having ServiceNow tickets
being opened and synced with Grafana's incident through the
invitations on the alerts. And that gets people on the
bridge in one to two minutes now. So we reduce our response
time by eight to nine minutes, which is a pretty good improvement. But having a bridge open doesn't mean
that the teams have the context that they need to actually be effective.
So let's dig into that. Now, if the people in
the bridge need context, so does AI and that starts with the data. So just quick show of
hands and I'll raise mine. Have you ever worked with an engineer
or been that person that has said, "My service is unique
for some reason. Yeah, we do things this way because
valid reasons, right?" Me too. But while your service
is unique snowflake, that doesn't necessarily mean it's a
good thing. It's usually not in IT. But here's the thing about snowflakes. They're all built on the same six-sided
structure. They're unique on the inside, but if you kind of zoom out, they all
look the same, right? No two are alike. The takeaway here is that unique
doesn't need to mean unstructured. So if you consider unique services,
you have different code, teams, architectures, release cadences and so on, but underneath each of them is the same
six-sided structure. And in our world, that became a common telemetry
language. And if I were to do it again, this would have been day one what we would
have focused on is getting rid of our custom labels and aligning to Otel
semantic conventions first and foremost, because we don't need every
service to behave identically. We just need to make sure that every
service describes itself reliably and consistently. So how do we actually get there? Ultimately, this comes down to a two-part answer. The first is how did we fix the
data and then what capabilities that unlocked for us? So to fix the data, we use Grafana Fleet Management
to apply labels in bulk across our entire fleet consistently. We started with collectors,
this is before times, right? Our collectors are being set up by hand. There's a human involved in that process. Then ended up having inequitable
config drift despite best attempts. And then our pipeline changes for
some of our more complex or larger environments could take weeks
to get through to production. So iterating and finding new opportunities
to improve was a very slow process. Now every one of our collectors
is configured through to get one monorepo using a GitOps approach. Our core SRE team owns
that common pipeline. And what that means is that 95% of our
alloy configs are consistent and kind of immutable. The 5% that remains is where each team
gets hooks to update the config for their specific services. Today, that means that we have over 40 teams
that can configure their own name spaces, they can apply filtering, they can apply the labels that matter for
them while still allowing us to have a consistent language to
describe our services. Every change goes through a PR
automation workflow where it links it, it validates it, and you get a preview of what's going
to deploy into your fleet of collectors along with a scope. If that PR fails, it just simply doesn't
deploy. But once it does, fleet management takes that config,
it builds it for each of our teams, and it ultimately deploys it out
into our set of collectors. Those collectors are set up to hot reload
their configs every 60 seconds, and that means that we have no
downtime for changes to our collectors, just only if we've missed
something in configuration. So everything lands in Grafana Cloud
speaking one consistent telemetry language, and that's what the
knowledge graph ultimately builds on. The other takeaway is that because my
core SRE team owns that common pipeline, that's exactly where we fixed the labels. So now we took the custom
labels, we kept them there, but we're dual emitting the hotel
semantic conventions for service name and name space and so on. It doesn't increase our cardinality at
all because it's a one-to-one mapping and that's how we're going to slowly and
safely migrate our teams over to a more structured language. And that
gives them a lot of freedom. They can continue to work and iterate
without breaking the stuff that everyone's going to rely on at 4:00 AM. What this really meant for us is
that our pipeline changes went from taking weeks in some cases
to a couple of minutes. And that's a huge win from us because
not only do we have a lot more control over the pipelines, but we could rapidly
roll it out and also roll it back. So we stopped paying a configuration
tax on every new feature we wanted to enable. If we wanted to add node
exporter, that's a simple config change, a PR and human approval and a push
and within a couple of minutes it's out there. So here's what that actually
bought us. Before all this, we had the same service showing
up as maybe different entities. Nothing would tell those platforms
where those things actually ran. Afterwards, with consistent
naming and labels in place, Grafana can now recognize those
entities, how they connect, and ultimately that's the knowledge
graph. Services, databases, connectivity, data transfer, all
that comes in out of the box. Where we're going next is
completing some of the metadata, mapping ownership to the
correct on-call teams. And ultimately we've got
our own ownership registry today. We're moving it to backstage, but the goal is that we want the graph
to always know what is having a problem and who owns it so that we can make sure
that we have every team that's being impacted on the call, not just the first. Takeaway, if I can go back. Takeaway is that our telemetry
didn't suddenly become more accurate. It became more understandable. So this is a blown up view. It's a real slice of our
knowledge graph in production. Not shown here is the 54,000
entities that we have, 90 Kubernetes clusters, almost
14,000 services and so on. Actually I checked this,
this is about two weeks old. We're about 10% more than that today. Nobody on a bridge call can hold
that much information in their heads, but the graph does, and
so does the assistant. So by feeding the graph good clean data, we get actionable insights from it, but we also have to make sure that our
alerts are up to the same standard. So we took a very similar approach
for our alerts as we just did for our telemetry. We have one standard and we moved it
to a monorepo so that we can enforce this at the source. We used to manage our
alerts with Terraform and it
seemed like a good idea at the time, but Terraform is kind
of like a Swiss army knife. It's good for certain things, but ultimately it causes other downstream
issues at times if you're not careful and it can be pretty lengthy. So by having these Terraform repos
spread out for each individual team, we had a lot of pipelines,
a lot of reviewers, a lot of different ways
to label our alerts. Now with a monorepo, we have one
alerts repo with a folder per team, but the takeaway is that
the app teams, the leads, they still own these repos and
they have responsibility for them, but we have the ability to help
them make changes in bulk and ultimately put guardrails in place that
means that they align to the standards that we need them to align to. But what's the point?
So imagine it's what, 5:30, so maybe in 11 hours or so, it's 4:00 AM tomorrow and
one of you gets paged and the page is from one of the alerts that
you're managing within your ecosystem. In our world, our alert repo ensures that we have
all of the context and all of the information that you're going to need
at 4:00 AM available out of the box because it won't deploy otherwise. That means that you have Runbook URLs
that actually will resolve. You have a correct ownership assigned
to it, attributed, you have the correct
service name and namespace, so it ties back to the graph and you get
a summary of what is failing and what the alert actually is as that little
blurry short line that you're reading as you're waking up. Getting there meant that we had an
opportunity to clean up as well. So as we went to this monorepo, we went
from having about 6,000 custom alerts. We reduced it by 2,000 and counting. What we found is we had
a lot of duplicates, a lot of things that were
maybe misconfigured or old,
a lot of paused alerts, which was a surprise, but ultimately that means
less noise, more signal, and we can find
opportunities to get better. Another thing I'll call out that
this gave us the opportunity to do, Grafana has some amazing out of the box
alerts for some of their integrations. They really do. The but here is that some of the pending
periods are not quite what we want them to be. They're a little
bit longer than we'd like. So what we've done is take
those out of the box alerts. They're all in open source and we have
an automation that will pull them down and allow us to configure the things
that we need to be customized because if you change them in Grafana, the next
time that the integration gets updated, we found it would get overwritten
and it happened once or twice to us. What we're doing next and actively is
using AI, including their investigation, to go and pull our previous
investigations and say, "Where do we have blind
spots? Where do we have gaps? What's missing that we aren't looking for yet?" So to dig in that a little bit, we also looked back at our prior
investigations and while they were already bringing a lot of value, we found that
there was still some room to improve. And ultimately that meant that
we found gaps in our data. Systems investigations, it had
access to metrics, to logs, traces. It had the knowledge graph, which
was great. We're cleaning it up. We're getting better data feeding in, but we had some blind spots around
specifically our database layer and Azure Monitor. So we partnered with
Grafana on database observability and we asked for Azure Monitor to be
made available in the assistant. Grafana shipped it within about a month,
which was really quick turnaround. Once that data was in the mix, we immediately started seeing
things getting easier to line up. The dots were connecting faster. Our
root cause came a lot more quickly. And the incident I'm about to show you
is a good example of why that mattered. So we had a wave of latency alerts
across several of our products, plus a max connection warning
that was flaring up on Database A. We had two different alerts in two
different domains, so to speak, and our teams were starting down
two different paths to investigate. We suspected that Database A was the
problem. That's where the alert was. Meanwhile, the assistant checked two. Database A really was saturated and
that was tied to our product alerts, but it was only the symptom. The answer was hiding where none of
us were looking yet in database B. In reality, the total connections made to database
B were up by 86% and our database observability data is what
surfaced that insight for us. The app logs are what
connected the dots for us. What the assistant
found, the investigation, was that database B was
timing out and retries were piling up and that was causing the
real issue that was connected back to database A, something
that our alerts missed. We had essentially a retry storm. It was feeding on itself and when we threw the assistant at it, it took six minutes for the assistant
to find what probably would've been an hours long sort of investigation for us. We started asking follow up
questions after the incident. Could we have caught this
sooner? What would've exposed it? What we found is that we had an alerting gap and the
assistant helped us fill it. So snowflakes, every service is unique and they're
all built in the same structure. Related services get pulled together
and called a snowball, so to speak, and that's what we consider maybe a larger platform. But the snowmen in this analogy
is the relationship across those platforms. That's the incident and that's the type
of structure that the knowledge graph is giving us the ability to
derive. That bonding has a name. It's called centering, so that's
your fun fact for the day. And the thing I also want to call out is
that the flakes are staying individual. They're just now connected. So database A was the snowman for us and it was on the snowman and
it was where everybody was looking, but that wasn't what
held up the whole incident. Now, this is the actual Grafana
timeline from that incident. This is a real thing that
happened to us earlier this year. On the left here is what was
actually alerting Database A. Connections are climbing
6,000 to 8,000 and warnings were firing
right alongside of it. On the right is what
wasn't alerting database B, that's where the connection
growth was hiding. Here's the retry storm.
So confirm two things. Database A's alerts were actually
firing and they were real, but they were just the symptom. Database
B is what caused our product alerts. And here's the actual investigation
and the hypothesis that were being disproven, a couple names redacted. So context lives outside
of Grafana as well. We're big fans of Grafana's
big tent philosophy. You connect to your data where
it lives without moving it, but some of the most useful
context doesn't live there, and in our case it can't. GitHub's a good example of where we've
now connected through GitHub MCP, our GitHub source repo
to our investigations. So releases and other product activities
show up right alongside the telemetry. But that data that can't
be part of Grafana is things like WorkIQ, which is Microsoft's
knowledge graph, so to speak, or some of the data that comes
out of Copilot. So instead we turn the big tent kind of inside out. By using GCX from tools
like GitHub Copilot, we're able to utilize GCX as a
tool and bring the Grafana data to us locally. So back in 2023, an
alert gave us a signal. Today that starts a response
and it's the middle that makes a difference, identity,
reasoning, relationships. Now, when we started our journey,
most of that middle didn't exist yet. We were aligning our data to shared
standards that while Grafana was building the tools often with customers like us. Now that the middle is there,
our engineers arrive with
context already in hand. They are engaged immediately
when on-call is paged and we are eight minutes faster
remediating our instance. Now, I've been talking about
snowflakes like it's Christmas time, but Christmas is not
coming up. Halloween is. And the takeaway is that this is actually
brought in a costume the entire time. What I really want you to take away
is that without having full context for within your data, you're going to miss the thing that
might be right in front of you, and that could be the thing that
actually matters during an incident. So if I could give you one piece of
advice, don't jump to step six, don't skip to action. You have to make
sure that you get your context right. So the difference between
detection and decision is context. Consistent telemetry creates context. Context enables reasoning and
reasoning enables useful automation. Thank you very much.

