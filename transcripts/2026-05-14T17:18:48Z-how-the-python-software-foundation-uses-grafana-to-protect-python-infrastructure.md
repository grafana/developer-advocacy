# How the Python Software Foundation Uses Grafana to Protect Python Infrastructure

Published on 2026-05-14T17:18:48Z

## Description

Jacob Coffee is the sole infrastructure engineer keeping Python's global infrastructure online — including PyPI, which handles ...

URL: https://www.youtube.com/watch?v=HEn0Jrg1UWA

## Summary

The show titled "How the Python Software Foundation Uses Grafana to Protect Python Infrastructure" was published on May 14, 2026. Jacob Coffee, the Director of Engineering at the Python Software Foundation, discussed the challenges of maintaining Python's global infrastructure, including PyPI, which handles nearly 5 billion requests daily. He explained how the PSF transitioned to a self-hosted observability stack using Grafana, Loki, Mimir, and Alloy to improve visibility for community projects and reduce reliance on external monitoring tools. Key takeaways included the importance of structured logging, the benefits of open-source observability tools, and how the new system allows community members to troubleshoot issues independently, ultimately enhancing the efficiency of the infrastructure team.

Topics: Python Software Foundation, Grafana, observability stack, community projects, self-hosted infrastructure.

## Chapters

00:00:00 Discussion
00:06:16 Building a monitoring stack for Python infrastructure
00:11:39 Using Grafana and Loki for community self-service in Python infrastructure
00:17:01 Using Grafana for Python infrastructure visibility

Hola, buenas tardes, Barcelona! How are you doing? I'm very happy you've all made it this far into the day. My name's Jacob Coffee, director of engineering at the Python Software Foundation. My last name really is Coffee, and I don't work at Starbucks, but this week I have gotten a ton of questions about that.

I joined the PSF, the Python Software Foundation, in July 2024. Before me, Ee Durbin ran all of Python infrastructure with intermittent help from volunteers, effectively alone. With Python's scale, that's pretty surprising to most people. In July, I became the second person on the infrastructure team, but now it's just me on the infrastructure side. You'll hear a little bit later that we are hiring, and I'm in desperate need of someone in the audience's help.

Today, I wanted to tell you about how we ended up building a self-hosted observability stack with Grafana. This includes things like Loki, Mimir, and Alloy. The reason might surprise you, because it's not really because our old tools were bad; there's a story here, and it starts with the size at which we run.

To give you a little context, here's the surface area. This is usually where people spit out their water or stop chewing their food or something. We have PyPI, which is the package index that most people install packages from on the planet. It sees almost 5 billion requests a day and hosts over 750,000 packages, tens of millions of files, and over a million users now. PyPI handles more requests per second than Google handles Google searches per second, which is mind-boggling to me, especially considering our team size.

When PyPI has a bad day, GitHub Actions has a bad day. Your Docker file probably has a bad day. Open source projects and world governments alike are all going to have a bad day. We also have more community-focused things like Python.org, our Python docs, where you need to learn how to use the runtime, build bots, and lots of benchmark tooling and other things. Each one of those is a different code base and tech stack that we have to deploy. Nothing's the same, which is fun at times. Python.org is a Django app, and Mailman—well, we shouldn't really talk about that because it scares me. We have some Golang sprinkled in there and TypeScript repos. We didn't really choose to be a polyglot shop; that's just what happens when you have over 20 years of volunteer-driven infrastructure.

The part that matters for this talk is really the community. There are a lot of community-run projects that live on our clusters and our infrastructure, and that continues to grow. I really want it to grow, to be able to have people use our infrastructure without having to fork over their own credit card. This includes things like working groups and PyLadies chapters, which is an international group that promotes women in tech and mentors them. We also have PyCons all over the world and packaging teams. All of these people deploy things on the PSF infrastructure, and they all need to know when those things break.

With this scale and only a handful of people on the engineering side, observability really matters to us. It’s the difference between catching a problem in a few minutes versus finding out on Reddit or Hacker News on some thread three hours later. 

Here's the part that kind of confuses people: we have observability, and it's pretty good. I don't know if I'll get yelled at later, but we have Datadog for monitoring some of our services, Sentry for others, and PagerDuty—lots of things. All of these are donated through their open source programs or through special agreements because a lot of these companies, most companies in the world, rely on Python. We are very grateful for these donations, but while they solve our problem well, they don't really solve the community's problems.

When you exist to serve a community of millions of Python developers globally, it matters a lot to us. I hope we here today at one of the best open source observability conferences in the world can understand that. To recap, what was working well for us was not the same as what was working well for our community. The gap between what a few of us could use and see versus what our community could see is basically what this whole talk will be about.

The PSF hosts infrastructure for the broader Python community. For example, we want PyCon organizers—our Python conference—to be able to see their conference platform logs, or PyLadies chapters around the world to debug their event services or their Discord bots, or whatever they may have. We also have the core team that develops the Python runtime working on build bots, and they need error traces and all kinds of other groups that need their own thing.

When something breaks at 2:00 AM Pacific time, which is a perfectly normal working hour for people in Europe or Asia, those people have to message me or one of my colleagues on Slack and hope that I'm awake, or file a ticket, or wait until the morning until I wake up—probably late—and then lose hours of important debugging context. They can't really log into Datadog. We can't hand out seats to 500 community members. I don't think the in-kind donation would cover that. And if it did, it doesn't really fit the access model that we want. So it's not really a Datadog problem; it's our problem.

We had this great observability locked behind a door that only a few of us could see, and everyone else was on the other side, unable to see. The second part that was nagging me was that every piece of our infrastructure is donated. What would happen if, in some boardroom somewhere, they decided that a budget cut was coming or something else happened and they wanted to pull that? Well, that's going to be a big bill that we get.

So we built our own observability stack. We needed a few things. At a minimum, we needed self-hosted logs for those people to jump in and see. We needed metrics with decent retention, and it would be nice if we had things like shareable dashboards and multi-tenant access, along with having a single collection agent to make things simple and not have some crazy configuration. That's a big plus.

Loki, Mimir, and Grafana, through Alloy, all of those check the box so far. A big check was that it was open source and designed to work together very seamlessly. I'm super impressed by how the team has made everything flow well, and it's backed by a company that ships real features to open source editions. You see a lot of people lately who had open source editions or still have them, but they're feature-gated super hard. They're not developing features anymore; it's just security updates. That was a big deal for us.

We could start small, which was another important aspect. First, we started with logs, then we added metrics, and we're still working toward tracing with Tempo. That incremental path with a super small team has allowed us to grow into this new stack.

A little bit more about our clusters: the PSF cluster handles things like Python.org and PyCon. These are Kubernetes clusters, by the way, along with community projects. It uses Alloy for the collection, Loki for the logs, Mimir for the metrics, and some dashboards with Grafana, along with basic configuration with a few replicas of Loki. We have Mimir in production, and it's backed by MinIO for S3 storage—hopefully not MinIO for long. 

Then we have our PyPI cluster, which handles the warehouse at that massive scale I talked about earlier. It has the same monitoring stack, just with independent storage. It has the same manifests; it's separate because PyPI has a bigger blast radius, and we don't want any noisy neighbor problems.

has a little bit of different security requirements due to the scale and who uses it. All of these clusters run on **Cabotage**, which is our open-source platform as a service. Cabotage manages Kubernetes deployments with **Vault** for automatic MTLS, **Consul** for service discovery, and **Buildkite** for our container builds. Every pod in both clusters gets their certs automatically, including the monitoring stack itself. Everything is wired up, so when we add a new cluster, whether it's a third or a fourth, the monitoring just comes up with it. It's all the same customized manifests and the same config, with nothing extra to wire up. It's super simple; it just flows very well. We treat observability as a resident on the platform; we don't have it as an afterthought, and we love that.

Cabotage is source available, and you can deploy it in your own home lab—I do that. But you can also host it in your company internally. It's also a platform as a service that you can pay for. If that interests you, you can grab me in the hallway.

As far as our metrics, we have **Alloy** that runs a daemon set. This is a pod on each of our nodes and a few pipelines, just some really basic config. We didn't go super fancy just for the metrics. We scrape **cAdvisor** and have 40 metrics per node, along with **Traefik** for all the requests and things like CPU requests and latencies. We filter out anything that we don't want because that cardinality control really matters, especially when you're running on donated credits from great sponsors like **AWS**.

For our logs, we have the **Traefik** access logs. If anyone has migrated from **Nginx** ingress recently, Traefik made it very easy. I was very scared of it, but we parsed the JSON logs and extracted those structured **Loki** labels, things like status code and service theme. This decision made everything downstream work. I'm no observability expert, so if I get any of this wrong, I'm sorry. But being able to query by label instead of scanning raw text is the big difference between querying something in under a second versus inflating it by minutes. If you take one technical thing from this talk, it's to get your structured labels right at collection time.

For app logs, all of our community projects get their logs collected and tagged with the Kubernetes metadata, including things like the namespace and pod name. When they log into Grafana, they just see all of their stuff that they need, which is great, and only their stuff, which is even better because our security people would yell at me if that did not happen. All of this is like 200 lines of config the last time I looked in total. It's super simple, and I can understand it all without having to have a degree in observability or YAML. It's all in one file, with a few pipelines. 

If you're starting from scratch, we didn't start with Alloy, but we did move to it, and I'm really loving it. Loki stores our logs, indexes metadata—not the full content. It's cheaper for us to run, both in write and read operations, and the backend topologies are backed by **MinIO**. Right now, we have set a seven-day retention for our infrastructure logs, and for our tenants, like our community people, just 48 hours. Although we are trying to experiment with increasing those, as some security researchers would like more historical data, it's just the cost, and we don't want to burn through credits faster. So we're working our way up.

Being able to use **LogQL** for queries is great. If you know **PromQL**, you already know most of it. With structured labels from Alloy, you can query by the service and get all that in seconds. That label extraction was very important in the decision to go to the stack. Just a few member numbers: we have set a basic ten-second log scrape interval. So when something breaks, we get an update pretty fast. Again, we have those 40-plus metrics from cAdvisor available.

To quote Grafana here—if it's wrong, it's your guys' fault—**M** Query reduces the peak memory usage by up to 92%. When you're running on a tight budget, having these big memory hog services and agents running beside your apps is a big deal. So having that memory reduction is really good; we don't have to scale up nodes. We also do things like pre-compute some latency histograms for P99 and P95, so those panels load faster because the math is already done.

Grafana itself solved the original problem and the big problem: community projects needed to be able to deploy their app on Cabotage and see their own data automatically. Since each namespace maps to a Loki tenant, the PyCon folks can see PyCon things, PyLadies can see PyLadies, and no one sees what they shouldn't. We also picked Grafana because it's easily shareable. The hundred contributors can access their dashboards, and it costs us just a little bit of compute, but not really license seats because that's not the model here. For a nonprofit, that's like the whole ball game. The access model also made the migration worth it, although the technology is super great.

What we found is that the community is now self-serving. Logs are flowing, metrics are flowing, and dashboards are very pretty. We like pretty dashboards, although I've seen some this week that make me think mine are not so cool because you all have done some great work. We started noticing things that we hadn't before. 

As an example, this is a moment that showed me that we made the right call, and it wasn't a technical one. It was hearing from someone who had their own problem and fixed it without my involvement. I never heard about it; I wasn't paged, which is wonderful—I like my sleep. A PyLadies organizer logged into Grafana, found their service dashboard immediately, and saw the 500 error in the Loki logs. They traced it to some misconfigured environment variable, fixed it, deployed it, and no one on the infra team was involved. I only heard about it because the next day in a Slack thread, they mentioned, "Oh yeah, I fixed that last night," due to a message from a bot in Slack. 

To think about how the old workflow looked: when someone's service broke, they couldn't see why. They would message me and say, "Hey Jacob, can you check the logs?" I would have to stop what I was doing. With someone with severe unmedicated ADHD, the context switching is severely bad. I would have to open up our monitoring service, whatever that may be, find it, search through the logs, find the error, screenshot it, paste it to Slack, and explain it. Maybe they wouldn't really understand, so I would have to wait for them to try and fix it, and then repeat that process. Since our community is so large, that's just one community project. What do I do if I have four of those in a day? Well, I'm not getting anything done.

Now, they can just log in, see it, fix it, and I sleep through the whole thing. We went from being the bottleneck to being the platform. That scales in a way that a few people answering Slack messages at midnight never could. With this, we have zero vendor lock-in. Grafana, Loki, Mimir, Alloy, and soon Tempo are all open source. We own every component, and no one can pull the rug. Not saying that any of our current providers would, but having that sovereignty is peace of mind that I enjoy. 

We have that on the two clusters with our independent monitoring. If one goes down, the other is still up. Thanks to **Fastly**, we have a pretty high cache hit ratio. So that's almost, I did the math, it scared me—like $5 million in...

Kind donations at the market rates have allowed us to better measure how well our infrastructure is performing. However, with that visibility came some harder questions. When you finally see the scale of what you run, you can't look away from it. Fastly donates tons of money a year through their in-kind service, and it's a huge shout out to the whole Fastly team for that, as well as AWS for the cloud infrastructure. This amounts to many hundreds of thousands of dollars a year for us, along with Google providing storage, all of which is donated.

If you total the market rate for everything that the Python Software Foundation (PSF) uses, we would probably be, well no, we would definitely be in the tens of millions of dollars annually, and most Python developers would have no idea. They really shouldn't, but we see things like community projects and traffic patterns that hit us hard lately, such as bots, CI pipelines, and dependency scanners. We used to guess at how much our traffic was for things that aren't PyPI, which are heavily instrumented. But now we have very nice dashboards.

The Grafana stack gave us the ability to put a real number on what it costs to run Python's infrastructure, not just a rough estimate, but actual figures we can point to. This changes conversations with sponsors and discussions in boardrooms, which is great. 

On the infrastructure side of things, in September 2025, the PSF co-signed a statement with the folks at the Apache Foundation, the Eclipse Foundation, the Russ Foundation, and others titled, "Open Infrastructure is Not Free." The message is straightforward: the services millions of people rely on cost real money to run, and the organizations behind them need sustainable funding. We signed that because we had the data to back it up. 

Now, with the Grafana dashboards, we have real traffic numbers and Loki logs showing the request volumes and metrics. This gives us concrete numbers to reference for future discussions, not rough guesses but actual measurements. Before the Grafana stack, we would have said, "We think this is expensive." We knew it was, but now we can exactly say how expensive it is, or the stress on APIs, or anything like this. We can put a dashboard in front of a sponsor and say, "This is what your donation is enabling. Thank you. By the way, this is what our infrastructure handles, and this is what happens if those donations stop." 

So, observability did not just help us keep the servers running; it gave us the language to defend the resources for the continued donations that keep them running. 

Here's a quick, rough roadmap of where we'd like to head. Of course, I mentioned Tempo with distributed tracing to get that full LGTM stack. When something is slow, we want to see exactly what that is. We want more projects onboarded; we want more and more communities on our infrastructure. That may sound antithetical to my whole cost-saving thing, but our mission as the PSF, the nonprofit, is to expand and grow Python for the community. 

We need to be able to say, "Here's your dashboard; you can see what happened to my service." Now they can look for themselves. Hopefully soon, we will have some great insights for the public, like public dashboards to see more than just status.python.org shows, which is uptime. We would like to show overall health or infrastructure capacity. Imagine going to a URL and having a real-time health check of the entire Python ecosystem. That transparency is what the community deserves to have.

To recap: own your observability. Don't build things that people can take away. Host it with open source; we love open source. That's our whole mission, and we proved that it works with a small team of two. Thanks to my ex-boss, I love you. Share with your community. If people run things on your infrastructure, let them see their own logs and don't be the bottleneck; be the platform. Grafana enables this for us. 

Build the evidence up. Sponsors respond to numbers, not just vibes. Unfortunately, boards respond to data, so dashboards give you that backing. I mentioned earlier that the PSF is hiring. We're growing my team, so if you want to come work with me, hopefully, you're better at observability than I am. We're hiring an infrastructure engineer and a software engineer to work on PyPI. The impact is enormous; I've told you the scale of what we do. So come see me or apply online at python.org/jobs.

Also, we have PyCon US, our annual conference, in three weeks. So when you all go back home to the US, if you're not from here, check it out. It's in Long Beach this year, from May 13th through the 19th. I'll be there, hopefully with better dashboards. Maybe you can help me; send me a message. 

We had great tools that we couldn't share, and we built our own. Now the whole community can see. 

Thank you. Ciao. (audience applauds)

## Raw YouTube Transcript

- Hola, Buenos tardes,
Barcelona, how are you doing? Very happy you've all made
it this far into the day. My name's Jacob Coffee, director of engineering at the
Python Software Foundation. My last name really is Coffee
and I don't work at Starbucks, but this week I have gotten a
ton of questions about that. So I joined the PSF, the Python Software
Foundation, in July, 2024. And before me Ee Durbin ran
all of Python infrastructure with intermittent help and
volunteers, effectively alone. With Python's scale, that's pretty surprising to most people. In July, I became the second person on the infrastructure team, but now it's just me on
the infrastructure side. And you'll hear a little bit
later that we are hiring, and I'm in desperate need of
someone in the audience's help. So, today I wanted to tell you about how we ended up building a
self-hosted observability stack with Grafana. That includes things like
Loki, and Mimir, and Alloy. And the reason might surprise you, because it's not really
because our old tools were bad, there's a story here, and it starts with the
size at what we run. So just to give you a little context, here's the surface area. This is where usually where
people spit out their water or stop chewing their food or something. We have PyPi, which is the package index that most people install
packages from on the planet that comes through us. And that sees almost 5
billion requests a day. It hosts 750,000 plus packages. Tens of millions of files
and over a million users now. So PyPi handles more
requests per second now than Google handles Google
searches per second, which is mind boggling to me considering especially our team size. So all of that to say,
when PyPi has a bad day, GitHub actions has a bad day. Your Docker file probably has a bad day. Open source projects and
world governments alike, they're all gonna have a bad day. And then we have more
community focused things like Python.org, our Python docs, when you need to learn how to
use the runtime, build bots, and lots of benchmark
tooling and other things. And each one of those is
a different code base, different tech stack
that we have to deploy. Nothing's the same, which is fun at times. Python.org is the Django app and Mailman, we shouldn't really talk about
that 'cause it scares me. So we have some Golang sprinkled in there and type script repos. And we didn't really choose
to be a polyglot shop. That's just what happens
when you have over 20 years of volunteer driven infrastructure. So, and the part that
matters for this talk, really is the community. So there's a lot of community run projects that live on our clusters
and our infrastructure, and that continues to grow. And I really, really want it to grow, to be able to have people
use our infrastructure without having to fork
over their own credit card. And this is things like working groups and PyLadies chapters, which
is just an international group that promotes women in
tech and mentors them. We also have PyCons all over
the world and packaging teams. And all of these people deploy things on the PSF infrastructure, and they all need to know
when those things break. So with this scale and
only a handful of people on the engineering side world, well, when I say observability
really matters to us I mean, it's the difference
of catching a problem in a few minutes versus
finding out on Reddit, or Hacker News, on some
thread three hours later. So here's the part that
kind of confuses people because here's have observability
and it's pretty good, don't know if I'll get yelled at later, but we have Datadog for
monitoring some of our services, century for others, and
PagerDuty, all kinds of things. And all of these are donated through their open source programs or through special agreements because a lot of these companies, most companies in the
world rely on Python. And we still use them,
we're very, very grateful. But in kind donations solve
our problem really well, but they don't really solve
the community's problems. So when you exist to serve
a community of millions of Python developers globally,
it matters a lot to us. And I hope we here today at one of the best open source
observability conferences in the world can understand that. So just to recap, what
was working well for us was not the same as working
well for our community and that gap between what a
few of us could use and see, versus what our community could see, that's basically what this
whole talk will be about. So the PSF hosts infrastructure for the broader Python community. And some insight on
that, just as an example, we want PyCon organizers, which is, sorry, our Python conference, to be able to see their
conference platform logs or PyLadies chapters around the world to debug their event services,
or their Discord bots, or whatever they may have. And we also have the core team that develops the Python
runtime working on bill bots and they need ear error traces and all kinds of other groups
that need their own thing. And when something breaks
at 2:00 AM Pacific time, which is a perfectly normal working hour for people in Europe or Asia, those people have to message
me or one of my colleagues on Slack and hope that I'm
awake or file a ticket, or wait until the morning,
until I wake up, probably late, and then lose hours of
important debugging context. And they can't really log into Datadog. We can't hand out seats
to 500 community members. I don't the in kind
donation would cover that. And if it did, it doesn't really fit the
access model that we want. So it's not really a Datadog
problem, it's an our problem. And we had this great
observability locked behind a door that only a few of us could see, and everyone else was on the
other side unable to see. And the second part that was nagging me was that every piece of our
infrastructure is donated. And so, what would happen
in some boardroom somewhere, they decided that a budget cut was coming or something else happened
and they wanted to pull that. Well, that's gonna be
a big bill that we get. So we built our own. We needed a few things. At the minimum, we needed self-hosted logs for those people to jump in and see. We needed metrics with
some decent retention and it would be nice
if we had things like, shareable dashboards
and multi-tenant access, and having a single collection
agent to make things simple and not have some crazy configuration. That's a big plus. And so Loki, Mimir,
Grafana, through Alloy, all of those check the box so far. A big check also was
that it was open source. It was designed to work
together very seamlessly. I'm super impressed by how the team has made everything flow well, and it's backed by a company
that ships real features to open source additions. You see a lot of people lately
they had open source editions or they still have them, or they're like, feature gated super hard. They're not developing features anymore, it's just security updates. And that was a big deal. So, and we could start
small, it was another thing. First we started with
logs, then we added metrics and we're still working
toward tracing with Tempo. And that incremental path
with a super small team, that was very, very important and has allowed us to
grow into this new stack. A little bit more about our clusters. The PSF cluster handles things
like Python,org and PyCon. These are Kubernetes clusters by the way, and community projects. And it uses Alloy for the collection, and Loki for the logs,
Mimir for the metrics, and some dashboards with Grafana, and basic configuration
with a few replicas of Loki. And we have Mimir in production and it's backed by MinIO for S3 storage, hopefully not MinIO for long. And then we have our PyPi
cluster and it handles warehouse in that massive scale that
I talked about earlier. It has the same monitoring
stack, just independent storage. Has the same manifests, it's separate because PyPi
has a bigger blast radius also, we don't want any like
noisy neighbor problems. And it has a little bit of
different security requirements due to the scale and who uses it. All of these clusters run on Cabotage, which is our open source
platform as a service. And Cabotage manages Kubernetes
deployments with Vault for automatic MTLS, and
Consul for service discovery, and Buildkite for our container builds. And every pod in both clusters gets their certs automatically, including the monitoring of stack itself. Everything just is wired up. So when we add a new cluster
and we need to add a third or a fourth, the monitoring
just comes up with it and it's all the same
customized manifests, and same Config, and
nothing extra to wire up. And it's super simple,
it just flows very well. And we treat observability
as like a resident on the platform. We don't have it as like an
afterthought, and we love that. So Cabotage is source available and you can deploy it in
your own home lab, I do that. But you can host it in your
company as well, internally. It's also a platform as a
service that you can pay for. If that interest you, you
can grab me in the hallway. So as far as our metrics, we have Alloy that runs a demon set. This is a pod on each of our
nodes and a few pipelines, just some really basic Config. We didn't go super fancy
just for the metrics. We scrape cAdvisor, and
have 40 metrics a node, and Traefik for all the requests and things like CPU
requests and latencies, things like that. And we filter out anything
that we don't want because that cardinality
control really matters, especially when you're
running on donated credits from great sponsors like AWS. And then the second for our logs, we have the Traefik access logs. If anyone has migrated from
Nginx ingress recently, Traefik made it very easy,
I was very scared of it. But yeah, so we parsed the JSON logs and extract those structure Loki labels, things like status code and service theme. And this decision made
everything downstream work. And I'm no observability
expert, don't let me fool you. So if I get any of this wrong, I'm sorry. But being able to query by label instead of scanning raw text, is the big difference
between querying a thing in under a second versus, let
me inflate this by minutes. And if you take one technical
thing from your talk, it's get your structured labels
right at collection time. And then for app logs, all of our community projects
get their logs collected and tagged with the Kubernetes metadata and things like the namespace and pod name and things like that. And when they log into Grafana, they just see all of their
stuff that they need, which is great and only their
stuff, which is an extra great because our security
people would yell at me if that did not happen. And all of this is like
200 lines of Config the last time I looked in total. It's like super simple and
I can understand it all without having to have a degree
in observability or YAML. It's all one file,
there's a few pipelines. So if you're starting from scratch, we didn't start with Alloy,
but we did move to it and I'm really loving it. So like I said, Loki stores
our logs, indexes, metadata, not the full content. It's cheaper for us to run,
and the write and read, and backend topologies backed by MinIO. And right now we have set
just a seven day retention for our infrastructure
logs, and for our tenants, like our community people, just 48 hours. Although we are trying to
experiment with increasing those as some security researchers
would like more historics, it's just the cost and that we don't wanna
burn through credits faster. So we're working our way up. And then being able to use
LogQL for queries is great. If you know PromQL, you
already know most of it. So structured labels from
Alloy, then you just query by the service and get
all that in seconds. That label extraction
was very, very important in the decision to go to the stack. Just a few member numbers. We have set a basic ten
second log scrape interval. And so, when something breaks,
we get an update pretty fast. And again, we have those 40 plus metrics from cAdvisor available. And then this is just
to quote Grafana here. So if it's wrong, it's your guys' fault. M Query reduces the peak
memory usage by up to 92%. So when you're running on a tight budget, having these big memory
hog services agents running beside your apps, it's a big deal. So having that memory reduction
is really, really good. So we don't have to scale up nodes. And we also do things like pre-compute some latency histograms
for like P 99, P 95. And so those panels load faster because the math is already done. So Grafana itself, and this is the part that
solved the original problem and the big problem. Community projects needed to
be able to deploy their app on Cabotage and see their
own data automatically. And since each namespace
map fits to a Loki tenant, the the PyCon folks can see PyCon things, PyLadies can see PyLadies and no one sees what they shouldn't. And we also pick Grafana
because it's easily shareable. The hundred contributors
can access their dashboards and it costs us just a
little bit of compute, but not really license seats because that's not the model here. And so, for a nonprofit that's
like the whole ball game. The access model also made
the migration worth it. Although the technology is super great. So the stack is running. What we found is, the
community is now self-serving. Logs are flowing, metrics flowing, dashboards are very pretty,
we like pretty dashboards, although I've seen some this week that make me think mine are not so cool because you all have done some great work, and we started noticing
things that we hadn't before. So this is, as an example,
this is a moment that showed me that we made the right call
and it wasn't a technical one. It was hearing from someone
that had their own problem and fixed it, and I never heard about it. I wasn't paged, which just
wonderful, I like my sleep. And so, to get into this, a PyLadies organizer logged into Grafana, found their service dashboard immediately and saw the 500 error in the Loki logs and traced it to some
misconfigured environment variable. So they fixed it, they deployed it, and then no one on the
infra team was involved. So when I say no one,
obviously it's just me, so that's great. But only heard about it because the next day in a
Slack thread, they were like, "Oh yeah, I fixed that last night," because there was a
message from a bot in Slack just because we wanna see everything. But I never heard about
it, it wasn't paged. So to think about how the
old workflow looked like when someone's service
broke, they can't see why. They message me and say, "Hey Jacob, can you check the logs?" And I have to stop what I'm doing. And with someone with
severe unmedicated ADHD, the contact switching is severely bad. So I have to open up
our monitoring service, whatever that may be, and find
it, search through the logs, find the error, screenshot
it, paste it to Slack, tell them, explain it. Maybe they don't really understand, so I have to wait for
them to try and fix it. And again, repeat that. Since our community's so large, that's just one community project. What do I do if I have like
four of those in a day? Well, I'm not getting anything done. So now they can just log in,
they see it, they fix it, and I sleep through the whole thing. So we went from being the
bottleneck to being the platform. And that scales in a way that a few people answering Slack messages
at midnight never could. So with this we have zero vendor lock in. Grafana, Loki, Mimir, Alloy, and soon Tempo, all open source. We own every component and
no one can pull the rug. Not saying that any of our
current providers would, but having that sovereignty
is peace of mind that I enjoy. And we just all have
that on the two clusters with our independent monitoring. So if one goes down,
the other is still up. And thanks to Fastly we have
a pretty high cache hit ratio. So that's almost, I did
the math, it scared me, like $5 million in kind
donations at the market rates. And so now we can better measure
how well that's performing. So with that visibility though
came some harder questions. When you finally see the
scale of what you run, you can't look away from it. Fastly donates tons of money a year through their in kind service,
and it's a huge shout out to the whole Fastly team for that and AWS the cloud infrastructure. Many hundreds of thousands
of dollars a year for us, and Google with the storage,
and all this all donated. So if you total the
market rate for everything that PSF uses, we would
probably be, well no, we would definitely be
in the tens of millions of dollars annually and most Python developers
would have no idea. And they really shouldn't, but you see, things like community projects and traffic patterns for those two and things that hit us
hard lately like bots, and CI pipelines, and dependency scanners and all of this mess. We used to guess at how
much our traffic was for things that aren't PyPi
that are heavily instrumented. But now we have very nice dashboards. So the Grafana stack gave us the ability to put a real number on what it costs to run Python's infrastructure,
and not a rough estimate and the actual figures we can point to. And that changes
conversations with sponsors, that changes conversations in boardrooms. And that's great. So more on the infrastructure
side of things. In September, 2025, the
PSF co-signed a statement with the folks at the Apache Foundation the Eclipse Foundation, Russ Foundation and others titled, "Open
Infrastructure is Not Free." And the message is super straightforward. The services, millions of people rely on cost real money to run, and the organizations behind
them need sustainable funding. And we signed that because we
had the data to back it up. We had some data, now with
the Grafana dashboards, we have real traffic numbers and Loki logs showing the request volumes, and metrics, and all this great stuff. It gives us concrete numbers in the future to reference for more
discussions like this. Not rough guesses but actual measurements. So before the Grafana
stack, we would've said, "We think this is
expensive," we know it is, but now we can exactly say how expensive or like stress on APIs
or anything like this. And we can put a dashboard
in front of a sponsor and say, this is what
your donation is enabling. Thank you. By the way, this is what
our infrastructure handles and this is what happens
if those donations stop. So observability did not just help us keep the servers running,
it gave us the language to defend the resources
for the continued donations and things that keep them running. So here's a a quick, rough roadmap of where we'd like to head. Of course I said Tempo
with a distributed tracing to get that full LGTM stack. And when something slow, we
wanna see exactly what that is. More projects onboarded. We want more, and more,
and more communities on our infrastructure. That sounds like antithetical to my whole like cost saving thing. But our mission as the PSF, the nonprofit is to expand and grow
Python for the community. And that's what this allows. But we need to be able to
say, here's your dashboard, you can out what happened to my service. Now they can look for themselves. And then hopefully soon
is some great insights for the public, like public dashboards to see more than just
status.python.org shows, which is like uptime. We would like to show like overall health or infrastructure capacity. And imagine just going to see a URL and have like a real time health check of the entire Python ecosystem. And that's the transparency, I think that the community deserves to have. So just to recap, own your observability. Don't build things that
people can take away. Host it with open source,
we love open source. That's our whole mission, and we proved that it works
with a small team of two. Now, one thanks to my ex-boss, I love you. Share with your community. If people run thing on
your infrastructure, let them see their own logs and don't be the
bottleneck, be the platform. And Grafana enables this for us. And then build the evidence up. So sponsors respond to
numbers, not like vibes. Unfortunately, boards respond to data. So dashboards give you that to back it up. I mentioned earlier the PSF is hiring. We're growing my team. So if you wanna come work with me, hopefully you're better at
observability than I am. We're hiring an infrastructure engineer and a software engineer to work on PyPi. Some enormous impact, I've told
you the scale of what we do. So come see me or apply
online at python.org/jobs. Also, we have PyCon US. It's our annual conference,
it's in three weeks. So when you all go back home to the US, if you're not from here, check it out. It's in Long Beach this year. It's May 13th through the 19th. And I'll be there hopefully
with better dashboards. Probably, maybe not,
maybe you can help me, send me a message. And so yeah, we had great
tools that we couldn't share and we built our own. So now the whole community can see. All right, thank you. Ciao.
(audience applauds)

