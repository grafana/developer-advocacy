# How Dropbox Scaled Loki to 5 Petabytes: Lessons in Observability at Massive Scale | Grafana Labs

Published on 2025-06-07T05:29:33Z

## Description

Dropbox scaled Loki to support 5+ PB of logs and 6 GB/s ingest. Chris Hodges, software engineer at Dropbox, shares how they ...

URL: https://www.youtube.com/watch?v=XimqMfLBfrI

## Summary

In this presentation at GrafanaCON, Chris Hodges, a software engineer at Dropbox, discusses the implementation and scaling of Loki, the company's centralized platform for unstructured logs, after its launch in 2022. He shares a significant incident involving a data center outage that affected Loki and highlights the importance of robust incident detection, diagnosis, and prevention strategies. Chris elaborates on Dropbox's unique log storage solution using an S3 abstraction layer and the necessity of redundancy to ensure log accessibility. He outlines the challenges faced during the rollout of Loki, including managing logging volume, ensuring multi-tenancy, and reliability issues, and emphasizes the importance of thorough testing and monitoring. The talk concludes with insights on future improvements for Loki and the overall logging system at Dropbox, with a current logging volume of about five to six gigabytes per second. Chris invites attendees to engage in further discussions at the Ask the Experts booth.

# GrafanaCON Talk by Chris Hodges

Hello everybody. My name is **Chris Hodges**, and I'm a software engineer at **Dropbox**. Although I have not landed anything on the moon recently, I'm excited to share some interesting insights into what we're doing. It's fascinating to see the various ways that **Grafana** is utilized across different industries. 

I work on a team that provides logging, tracing, error monitoring, and dashboarding for our main production environment. I collaborate closely with another team that manages our custom metrics stack called **Vortex Two**. Both of these teams are here at **GrafanaCON**, and whether you're interested in our observability stack or want to discuss best practices, we’d love to speak with you.

In **2022**, we launched **Loki** as our centralized platform for unstructured logs. Since then, we have learned a lot about maintaining and scaling it. I'm eager to share our experiences, including both our successes and challenges. I will try to save some time at the end for Q&A, and I hope that whether you are a user, contributor, maintainer, or in management, you will leave this talk with a better understanding of what it takes to operate an observability platform at scale.

## A Story About Incident Management

To start, I want to share a story. I apologize for my AI-generated book cover, but as a dad, this story reminds me of a particularly gloomy children's book. 

This story takes place about a year after we launched Loki. We had a new engineer going on call for the first time. Being "on call" means holding a pager and being available 24/7 for a week to respond to incidents or alerts for the different services we manage. Shortly into this on-call rotation, two alerts came in quick succession: the first stated, "Loki is unavailable," and the second indicated that "our error monitoring system is down." 

This situation escalated quickly, and we suspected there was a more significant issue at play. Upon checking the Slack channel where we monitor incidents across the company, we were horrified to discover that the **network team** had lost connectivity to the data center hosting Loki. We had considered a data center outage when rolling out Loki, but it had not prioritized enough to implement multiple data centers. Now, we were paying the price for that oversight.

It was a tough situation because with the data center down, many engineers needed access to their logs. Loki was down, and we were providing them with inadequate workarounds to access their log data. This was a low point for us.

### Post-Incident Analysis

As for our post-incident analysis, we follow a standard approach that examines four areas. 

1. **Detection**: How did we find out the service was down? In this case, we were promptly alerted that everything was terrible, so we scored well on detection.
  
2. **Diagnosis**: This looks at the time taken from when we were alerted to when we identified the root cause. Ideally, you receive an alert accompanied by a playbook that guides you when you're groggy at three in the morning. Unfortunately, we did not have a playbook for this scenario.

Before diving into how we resolved the issue, I want to quickly explain how we manage log storage at Dropbox, as it differs from traditional methods. Being a storage company, we do store logs in **Dropbox**. We have what we call an **S3 abstraction layer**, which presents an S3-compatible API to Loki. It intelligently routes logs to the appropriate storage, primarily to our **Magic Pocket**—our highly scalable exabyte-scale storage.

The S3 abstraction layer can redirect logs to S3 if our on-prem storage becomes unavailable. This capability became crucial during the incident when connectivity was restored after about 30 minutes, but it took longer to reconnect to our on-prem storage. Thankfully, all logs were being sent to S3, allowing us to provide our developers access to the relevant logs, albeit with some delays in retrieving historical logs.

Once the on-prem storage came back online, we were able to backfill all the logs stored in S3 back into Magic Pocket, maintaining a continuous line of logs without interruption.

### Root Cause Analysis

Up to this point, I’ve left the cause of the data center connectivity loss as speculation. The reasons could range from natural disasters like earthquakes or floods, but in our case, it was a more mundane power outage. While tier four data centers are designed for 99.995% uptime, translating to about 26 minutes of downtime per year, this incident was a freak accident in which multiple redundancies failed.

This experience was a valuable learning opportunity for us. We recognized the need for better preparation to prevent similar incidents in the future. The fourth step of our incident analysis is **prevention**, which involves identifying the root cause and implementing action items to ensure it doesn’t happen again. It’s crucial to follow through on these action items to maintain control long-term and address the root causes of incidents.

### Moving Forward

We recognized the necessity of having Loki in multiple regions. The plan was to use DNS to point **Promtail** at Loki, enabling us to switch regions quickly if needed. A critical part of this was conducting a disaster readiness test, as testing is essential to ensure functionality.

To elaborate, all our production hosts are hybrid cloud systems, each equipped with an agent (Promtail) that reports logs to Loki. On the user side, we utilize **Grafana** and **Log CLI**, both configured to communicate with Loki in region one. We also share object storage between both sides for availability and redundancy.

After running the test and switching over DNS to region two, we observed logs converging. However, we noticed that logs still in memory in region one had not yet been flushed to the object store. We manually restarted the pipeline in region one to facilitate a mass flushing of logs, which required coordination with our on-prem storage team to manage rate limits effectively.

### Why Loki?

Now, let’s rewind to why we chose Loki in the first place. Historically, our developers relied on SSH and VI or transferred files off hosts, which was not sustainable. As we locked down production access and migrated to Kubernetes, we needed a solution for ephemeral logs that come and go.

1. **Object Storage**: Loki's reliance on object storage made it easier for us to understand and scale.
  
2. **Strong Multi-tenancy Support**: This feature allows us to segment logs, ensuring developers only access what they need while maintaining overall reliability.

3. **Integration with Grafana**: We sought a unified observability solution for logs, metrics, and traces, and Grafana has proven to be the best solution for this.

### From Plan to Production

To summarize our journey from plan to production, we started with a **request for comments** document to gather feedback on major changes. We conducted thorough investigations into various SaaS platforms and indexed logging solutions, ultimately concluding that Loki was the best fit for our scale.

A key aspect of our design was ensuring high availability. We maintained strict control over labels, focusing on the unique combinations of service and host. We started with a seven-day retention policy and enforced limits on query windows and ingestion rates to prevent overwhelming our system.

**Mutual TLS (MTLS)** was implemented for privacy, ensuring secure authentication between clients and servers. We also added a tenant ID to logs for efficient management of our approximately one thousand services.

### Rolling Out to Production

When rolling out Loki to production, the speed was contingent on how many hosts we deployed Promtail to at a time. We monitored higher write volumes to ensure we weren't sending more data to S3 than anticipated. 

During the rollout, we discovered some services were logging data so rapidly that they filled up the disk. We implemented runtime configuration to allow Promtails to ignore logs from specific labels, protecting Loki from overload.

One significant challenge we faced was **head-of-line blocking**, where one service’s log throttling impeded others. We addressed this by opening up lanes in Promtail to ensure that one service could throttle without affecting others, a vital principle of multi-tenancy.

### Final Thoughts

Ultimately, we faced challenges in rolling out Loki to production. We worked closely with **Grafana Labs** colleagues, who were developing a solution to improve performance on label queries. Once we transitioned to using **Prometheus** for time series data in Loki, we experienced significant improvements.

We communicated our rollout through emails, and we saw our number of weekly active users begin to rise as we opened access to more developers. Our internal documentation guided users on how to utilize our label schema for queries.

To monitor Loki's effectiveness, we not only set alerts for SLA breaches but also informed service teams if their logs were being rate limited. This transparency allowed them to address sudden spikes in logging volume promptly.

As we moved forward, we relaxed some initial limits, expanding retention to **30 days** and improving query speeds. We also subdivided larger tenants into subtenants to manage the increased complexity of their logs.

We engaged with developers through quarterly surveys to gather feedback on their experiences with Loki. This feedback has been instrumental in guiding our ongoing improvements.

In conclusion, the transition away from our old logging system was challenging, as it’s impossible to satisfy everyone. One specific user need we are still working to address is efficient querying over large data sets. We are excited about upcoming features in Loki that will enhance our querying capabilities.

Finally, here’s a Grafana panel showcasing our logging volume from **2022 to present day**. We’ve seen a steady increase, currently handling about **five to six gigabytes per second**, with **four to five petabytes** of logs at any given time.

Thank you for your attention! I look forward to your questions and discussions at the **Ask the Experts booth**.

## Raw YouTube Transcript

Hello everybody. My name is Chris Hodges.
I'm a software engineer at Dropbox. I have not landed anything
on the moon recently, but hopefully we can give you some
interesting insights to what we're doing. It's really cool to see all the different
ways that Grafana is used across so many different industries. I work
on a team that provides logging, tracing, error monitoring and dashboarding
for our main production environment. And I work closely alongside another
team that owns our custom metrics stack called Vortex Two. Both of these teams are here today at
GrafanaCON and whether you're interested to learn more about our observability
stack or you'd like to talk best practices, we'd love to
speak with you. Back in 2022, we launched Loki as our centralized
platform for unstructured logs. And since then we've learned
a lot about maintaining it and scaling it. And I'm excited to
share our experiences with you, both the successes and the challenges.
And I will try to save some
time at the end for Q&A, but I hope whether you are
a user, a contributor, a maintainer, or in management, you'll come away from this talk with a
better understanding of what it takes to operate observability platform at scale. Okay, I want to start with a story, and I apologize for my AI
generated book cover here, but I'm a dad and this
particular story reminded me of a particularly gloomy children's book. So to give you the background, this was about a year
after we had launched Loki. We had a new engineer going
on call for the first time and what "on call" means is holding
a pager and being available 24/7 for a week to answer incidents or alerts that are coming in for the
different services that we own. And so pretty short into
this on-call rotation, a couple alerts come real quick
next to each other. One is, "Loki is unavailable" and two is, "Our error monitoring system is
down." So this gets escalated and we are very quickly thinking there's
probably something bigger going on here than just with our services. So we go check the Slack channel
where we monitor incidents across the company to our abject horror. What we found was that the network
team was telling us they'd lost connectivity to the data center
where we were hosting Loki and we had considered a data center outage
as a possibility when we were rolling out Loki, but it just never, doesn't not been in priority enough
to get put into multiple data centers. And now we were paying the price for that. And so it felt it was hard
because we have data centers down, we have a lot of engineers who need
access to their logs, Loki is down, we're giving them not so great workarounds
for how to get to their log data. And so yeah, this was kind of a
low point. Didn't feel that great. Alright, so as far as
post-incident analysis, we do this in a pretty standard way and
look at it across four different areas. So the first two detection
and diagnosis detection is: How did I find out that
the service went down? Did a user have to tell me about it? Did I happen to stumble upon it
myself or was there a little alert? And in this case, we were very promptly
alerted that everything was terrible, so we were good with
detection. On diagnosis, this is from when I'm alerted to when I figure out what the root cause
is, how long does that take? This one, in an ideal scenario, you get an alert and it comes with a
playbook so that when you're up groggy at three in the morning, you look at the playbook and at least
it gives you a direction to head in. We did not have a direction or a
playbook for this particular scenario yet. Before we dive into how
did we fix the issue, I want to show real quick how we do log
storage at Dropbox because it's a little different because we are a storage
company and we do in fact store logs in Dropbox. So we have what we
call an S3 abstraction layer. And what it does is it presents
an S3-compatible API to Loki and it's smart enough to know for
a particular service where the logs should be sent. So for most of the logs, they go to this block here
at the bottom that says MP. MP stands for Magic Pocket. And it's our highly scalable exabyte scale storage that we run on-prem. The S3 abstraction layer sends
other data like indexing data to S3. We also have to be careful that we
don't store magic pockets logs in magic pocket because that would not be
good for people investigating incidents with that service itself.
So one benefit we get here is on the S3 abstraction layer, if for whatever reason that
on-prem storage was unavailable, it'll automatically fall back
to writing the logs to S3. And we were definitely going
to need that capability here because about 30 minutes into the incident connectivity was restored, but it was taken a little bit longer for
us to connect to our on-prem storage in that data center. And so what was good about that is that all the
logs for all the services were going to S3. So we were able to give our
developers access to the logs that mattered now from post-incident forward at the cost of having a little bit of
delay in getting to those historical logs. So we run this and what ends up happening is the on-prem
storage comes back up and we were able to backfill all the things that were in
S3 into Magic Pocket and have that just continuous line of uninterrupted logs.
So that was really nice to have that redundancy kind of
built in for us. Up to this point, I've really left to guessing as
far as why did the data center suddenly lose connectivity. I've come up with some examples
here that might be misfortunes. It is in fact just a physical building. So earthquakes or fire or flood,
our case was a little more mundane. It was a power outage and
I say just a power outage, but the most highly reliable data centers considered tier
four data centers are 99.995% uptime. And that translates to 26
minutes a year of downtime. And this is despite all the built-in
redundancies that come with these. So they usually have redundant feeds
from the utility company for power, redundant connections to
the internet generators, redundant cooling systems, battery
backups, like all these things. So this was a really freak accident where
enough of these things had failed that all of our servers in this data
center went down for 30 minutes. And really it was a good
learning experience for us. I wish we'd been better prepared for it, but it really gave us an
idea of what we needed to do to make this better in the
future if this happens. And so that's the fourth step of
incident analysis that we look at and I think is the most important,
which is prevention. Prevention is about figuring out what
was the root cause and then let's come up with some action items to
make sure that doesn't happen again. And actually then doing
those action items. I feel like the road to ops hell
is paved with good intentions. So doing this allows us to keep things under control in the long
term by addressing the root causes of incidents as we go, keeping
things sustainable. So we
knew what we needed to do. We needed to have Loki in multiple
regions. So the idea and the plan was to region Loki, we were going to use
DNS to point Promtail at Loki and this DNS would
have a configuration switch
where we could basically switch it over to a different region and
have very quickly all that converged to a different region. And a key part of this was we wanted
to perform a disaster readiness test because if you haven't tested it, it's probably broken and I'd rather
the first time we run this not be when a data center is down. And so we came up with a nice playbook
of like this is how to kind of orderly do this test such that
our users wouldn't really notice, but we would get a better understanding
of how it would perform in that situation. So just to give a little more
detail here about how we did this, we have all our production
hosts on the left kind of hybrid cloud. So each one of these
hosts has an agent on it, which we've talked about - Promtail. We're working on the
Alloy migration right now, but each host could have multiple services
on it and they're all reporting their logs through Promtail to Loki.
On the other side, the user side, we have Grafana and Log CLI that are
both using DNS to talk to Loki in region one. And then we have the object storage here
and that's going to be shared between both sides. So for the S3 side we get some
location diversity through S3 availability zone, and then on the magic pocket
side we get some free cross region replication. So we didn't want to
duplicate all the data in storage that would be
expensive. So we run the test, we switch it over DNS to region two, and then we are able to see very quickly
logs converging. But one
thing that's interesting here is that in this case
where region one did not lose power, you've still got a good bit of logs that
are still in memory that haven't been flushed to object stores. What we do is we manually kind of kick and restart the pipeline in region one, and this causes a mass flushing of logs, which we had to kind of make up with our
on-prem storage team a little bit and get some rate limits put in place
because when we do that, it is quite the torrent of logs. Okay, so let me rewind back to the
beginning. Why did we choose Loki? Historically, our developers have been
using like SSH and VI or transferring files off of a host
and this just wasn't going to be sustainable going forward. We were locking down production
access and we were migrating to Kubernetes, which has much more
ephemeral logs with pod logs, which can easily come and go.
So number one reason is Loki is based on object storage
and that's something we can easily understand. We know how to scale, we know what the price kind of
dimension is there. So that was huge. Second is the strong
multi-tenancy support. So this gives us a couple things. One, it lets us segment what logs
developers have access to. Privacy is super important, so we want to make sure that developers
only have access to logs where they have a need to know. Second, it gives us the ability for each tenant
to set different limits and this helps us protect the reliability
of Loki overall. Okay, and finally, tight
integration with Grafana. We've been using Grafana
a really long time. Our metrics system has a custom
data source plugin for it and we definitely wanted to have
a single place for observability - logs, metrics and traces.
Grafana just seemed like it's going to continue to be the best
solution for that. That was why Loki. Let's go real quick through a
whirlwind tour of plan to production. The plan - we started with a
request for comments document. These are documents we do internally to
get feedback on major changes that we're going to make and it also allows us to kind lay out here are the different alternatives we
considered and why we did not choose those alternatives. So we did a really thorough investigation
into different SaaS platforms and heavier indexed logging solutions. And Loki just really stood
out as the solution for our scale in what we were trying to do.
So it made it a pretty easy choice. A key part of the design was
making sure it was highly available. We wanted it to be something
our developers could trust in. So part of that is taking really
tight and strict control over the labels. So our label schema is based on
where a process is running in our network, like a service,
what host it's on, those kind of things. And the key
there is that we're maintaining total control over cardinality
of labels that come in. Cardinality being like the
combination of unique labels. If you have an explosion in cardinality, it can very quickly overwhelm
your ingestion pipeline
cause things start running out of memory and ruin
the fun for everybody. So we started with some pretty
strict limits that weren't the most popular. So we started with a seven-day retention
and some really restrictive query windows, like six hour max query
windows across logs and Loki. And we had limited amount of chunks
that you could fetch per query. And then we were also enforcing
limits on the ingestion side. So a particular service
has a global cap on the number of logs that it can send us before
we start rate limiting as well as a per stream limit. That stream is roughly a file in this
case where we will limit them that way. We've talked a little
bit about privacy already. MTLS was a big part of
that from the beginning. So mutual TLS is where a
client and a server send a certificate to each other, so you're authenticating
on both sides and we had our Promtail pipeline set
up to add a tenant ID to the logs the design had chosen that
that would be the service name. We've got roughly a thousand services
in Dropbox and this was a good tenant for us to kind of break things down
by and there's good ownership there. A key for us adding this tenant ID was the ability - we wanted to have
a single data source that would serve all of the different services logs. We didn't want to have to manage a
really long list of Loki data sources. So what we did is we came
up with a custom proxy in Go and it sits in between Grafana and
the Loki query front end. So for each query that comes in
from a user in Grafana, we look to see does it
have a service label? If the service label is
missing, we mandate it. So we send them back a nice message
that says, please specify a service. If the log does have a
service, we will then look, does the user have access to the logs
for this service against our custom permission system? If it does have access, then we will add the tenant HTTP header to the log message and send it onto the
Loki query front end so it knows which tenant we want to query
if they don't have access, what's nice about a custom proxy is we
can put in our own error message that points to documentation for how
you get access to these logs. As far as rolling this out to production, our main lever of the speed of that was
how many hosts were we putting Promtail on at a time? And so we would be
deploying to like 10 or 20,000 hosts at a time with Promtail and trying to see, let it soak a little bit, at least a day, sometimes more and observe how
is Loki handling that load. We had some alerting in place to detect
higher right volume because we wanted very quickly to know if we were sending
a lot more data to S3 than we thought we were going to be. And yeah, one of the things we found as we were
rolling this out is that some services were writing logs to disc so
fast that it was filling up the disc. And so we realized we needed
some runtime configuration where all the Promtails would be listening for
this configuration and we could switch it and immediately have
Promtail ignore like the logs from this particular label set
or whatever. And that allows us to protect Promtail and protect Loki
more broadly by giving us the ability to just quickly shut something off. Okay, I got busy with the AI again. So in this example, let's say that the lanes represent a service and the cars are logs. There's one service that's
having a bit of a problem. Let's say that's like, I don't know, rate limiting 429 error
message or something. So in Promtail, when that happens, it will do exponential back off
and then retry to send that log. The problem was a problem called head
of line blocking where when it was doing that, none of the other
services could send logs. We put up a pull request
that in this analogy, opened up all the lanes so that one
service could be heavily throttled and the others could continue
sending their logs. And a core tenant of multi-tenancy is that one badly behaving
tenant doesn't ruin the experience for everybody.
Okay? This was an issue that very nearly
kept us from rolling out Loki to production. And so in the video
here you can see we drop down, we get that required
service label selected, and then we click on the next thing in
Query Builder and it's just spinning for a real long time. And it was timing
out most of the time and this was like, this isn't going to cut it
for our user experience. Fortuitously, we had a colleague introduce us
to some folks at Grafana Labs, Owen Diehl and Ed Welch
and like wow, the timing, they were actually working on a solution
to this very problem when we talked to them, which was to pull the Prometheus time
series database in to replace Bolt DB in Loki. And when we transitioned to that, we saw an order of magnitude improvement
in our performance on label queries. So they saved our bacon and we're very
appreciative to them for the timing at which they were implementing that feature. Once we were able to get past that, we felt like we could roll it out
more broadly. So we send out emails, we see our number of weekly
active users starting to tick up. We allow everybody into
Loki where it had been previously, kind of early adopters being
manually added before that. We have internal documentation ready
that really explains what the labels are and how to build your query with the
label schema that we have in place. And then really important, we have
extensive monitoring in place, those alerts that went
off on the very bad day. So it's not only for when
we're breaching SLA on Loki and Loki's not acting right, but we also have alerts in place
that automatically inform the teams that own a service that their
logs are being rate limited. And so what that allows them
to do is look and see is there something recently that's been added that
made my logging volume spike? We give 'em a nice dashboard to see where the
source of the logging increase is, or it gives them the ability
to request a limit increase if that's what's needed. So we knew we weren't going to be able
to anticipate a hundred percent of how this was going to go after we rolled
it back. Those limits were very, very unpopular. So we
were able to relax those. Bringing in our on-prem storage as a
second backend really helped us with that, gave us better query speed and we
were able to expand retention out to 30 days and relax a bunch of other limits. Some tenants were much larger than others, both in terms of number of hosts,
volume of logs, number of streams, and there was kind of that same label
query speed issue with these because there was just so many combinations of
labels in a single tenant. It was the same problem again. So what we did was we subdivided
these really large tenants into subtenants for the service,
which really helped with that. A really critical way that we
tried to get feedback as we were rolling this out was developer
experience surveys that we sent out one a quarter and that
helped us get some very targeted feedback onto unfiltered thoughts on what people thought
of Loki and the experience with it. And we've been able to make steady
progress here in increasing, and that's been a huge way for us to
figure out where to invest in future work on our Loki cluster. I'll touch briefly on a
couple of reliability issues
just because they were kind of tricky. One was we were using etcd
for our ring membership because we deploy Loki distributed so
that we can independently scale query and ingestion side. And
with this etcd cluster, we had such a large deployment that we
were very quickly reaching the limits of what that etcd cluster could do, and we were running into limits
on much we could scale it. And so we switched over to member list option for that from HashiCorp. That's part of the Loki config, and that really increased
the reliability of Loki. Another reliability issue
that we had was with, I'm going to skip for time, sorry. Okay, so at the end it's time to shut
down the old logging system. This is the hardest part of the migration
because you're never going to make a hundred percent of the people happy. And so one of the difficult use
cases that we still have a little bit of trouble with is the needle
in a haystack query. So some users are like, "I want to be able to scan multiple
terabytes of data for a unique id, like a request id, and I want that query to come back in a
reasonable time." This is something that we're really looking forward
to in coming features of Loki, to be able to give us better
ways through bloom filters or whatever, be able to very
quickly look up by an id like that. Okay. Finally a Grafana
panel or it didn't happen. This shows logging volume
from 2022 to present day. Slow increase, but now we're up to about five to
six gigabytes per second for scale. And with our 30 day retention, we have somewhere between four and five
petabytes of logs at any given time. Yeah, excited for what's
coming forward with Loki. Looking to transition to the helm
chart. If you have questions, we'll answer some now and be happy
to talk at the Ask the Experts booth. Thank you.

