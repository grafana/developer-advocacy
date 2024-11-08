# Grafana Asserts Demo and BlackRock Case Study: Unified Application and Infrastructure Observability

Join Myrle and Goutham from Grafana Labs as they dive into the progress made with Asserts, a tool that unifies application and ...

Published on 2024-10-24T19:52:08Z

URL: https://www.youtube.com/watch?v=SC6dB0IYpAc

Transcript: Howdy y'all, my name is Myrle (for Mat, that rhymes with Pearl) and
this is Goutham Veeramachaneni There you go. Which is perfectly easy to pronounce
and I don't know what Matt's problem is. .  and
this is Baljeet Saini. And we will be talking with you about
the progress we've been making on Asserts since last year. I'm a
director of engineering. Gotham is product manager and Baljeet
is lead software engineer at BlackRock. One of our customers who's been
helping us to prove this out. So let's talk first about what this
looked like. before we started. Last year, we had just acquired Asserts and we
were looking at integrating it into our platform, but we had a different
world before this, right? What were people using to troubleshoot
their applications without Grafana Cloud? Let's start here. This is an alert. Let's pretend I'm a manager 'cause I am. We just got this alert on my team. Let's read it for a second. We've
got a search products latency. SLO burn rate is very high.
So what's going on here? It looks like search products, the service via which my customers
look at the products that I'm trying to sell them, is having a high latency period right
now this is a little problematic because this means that my business
may not be earning money right now. On my team I've got six full
stack devs who know how to manage and operate this service. However, three of them are in Europe. Let's see, it's about 10 30 at night.
They're at a birthday party. They might be drinking, I don't know. We've got two ladies in
NASA, we've got Elena, she's very experienced.
But she's on vacation. We've got Brian who unfortunately
and unexpectedly is out sick. And the second lady in NASA
in North America is Seema. She just started two months ago.
She's smart, she's ambitious, but she's new and she needs to
help us figure out how to fix this. So first thing she does is she goes to
that dashboard that Elena showed her during the onboarding process and she
sees that we've got a lot of front end errors coming up. It's what I said, the product servic is down and our
customers aren't able to reach our website to buy our products.
It's costing our business money. I've let my boss know what's
happening so she's in the loop, but pretty soon it's gonna
be the department head
calling me and asking for an update. So Seema digs
in, she finds an error, she looks at one of these errors, she looks at a couple more of these errors
she sees they all say pretty much the same thing. 500 errors
from the product's API. So which services are involved?
Well probably the product service, but which other services are involved? She goes to this wonderful architecture
diagram that Elena put together for her and actually Elena's really
good at keeping this up to date. She goes through every once
in a while and checks it, but sometimes people don't tell Elena
about the changes they're making and Elena can't change it like continuously.
So maybe it's up to date, maybe it's not. Even with
this architecture diagram, Seema is now going to have to find the
dashboards for all of these services too, right? Are these dashboards
high enough quality? Do they have the information
that Seema needs? Are they similar to each other or is
she going to have to work with different language every time she
switches between dashboards? Looks like Seema managed to find that
dashboard for the product service. She also found the dashboard for
the recommendation service and she's found the dashboard for
the feature flag service. Actually they look pretty good and
now she's found the dashboards for the SQL database. But which instance of the SQL
database does she need to look at? This is really hard for Seema. This is
really hard for almost any engineer, even if they're not new to the project. And we hear this from
a lot of our customers. They have all of the data they need,
everything they need to troubleshoot. It's there, it's in the system. They
even have dashboards for all of it. But finding the right dashboards, accessing it during an
incident - that's really hard. And it's especially hard because it
requires people to know where things are, even people who are new or people
who have switched between teams and that slows people down and it means
people, it means businesses lose money. So we've been working
on making this better, making this easier and Goutham is going
to show us what the Asserts team has been working on in order to integrate
all of these insights into one place. First, he's gonna explain how the system works
and then he is gonna give us a demo. Hi everyone, I'm Goutham Veeramachaneni.
Yeah, I'm the pm for Asserts. I'm also a Prometheus
maintainer and I really, really loved the product when I saw it
because it's very much built on top of Prometheus. So before we kind of look at how Seema
and Elena could now leverage Asserts to solve the same problems, let's kind
of understand how Asserts works. So Asserts looks at all your metrics to
understand all the components in your system. For example, if you have
node exporter metrics like Node, your name info or pro Prometheus
Kubernetes metrics like cube node info, we understand what nodes exist
in your system. Similarly, from kube pod info or
from kube deployment info, we understand what deployments
exist in your system. If we see RED metrics like HTTP, server
duration seconds from hotel, from flask, from all the popular Prometheus
frameworks or Prometheus instrumented frameworks, we understand what services are running
and like what RED metrics they have. If we see metrics from MySQL, we understand this deployment
is a MySQL deployment. Once we understand all the components
in your system, we then use traces, service graph, service mesh to understand the
dependencies between these components. We put together all of this into a graph
database and we produce something that looks like this. It looks super cool but
it's also super scary and super dense. This is not where Asserts ends but it
understands all the components and the relationships between these
components. It goes one step further. It not only discovers stuff in your
application and infrastructure. It also then starts to monitor key
KPIs and understand healthy states for services. For example, it knows that checkout service usually
gets 50 requests per second and it answers in 200 milliseconds. For example, it knows MySQ typically gets like a
hundred connections on a stable day and then the maximum limit is 500. If
anything close to that it's saturation. So once it understands the healthy
states, it starts highlighting changes, anomalies and issues in these systems, it then puts together all
of this information to help
you troubleshoot quicker. Alright, let's go back to the
documentation that Elena wrote. Well we all know engineers
love documentation because
they never need to update it. Yeah. Now let's switch to the demo. Let's see what happens
like just remember this, there's a product catalog service talking
to recommendations and feature flag. Now yeah, let's switch to the demo. We can go to Asserts in the
panel here and by default, Asserts will pull in all the
information for all your services. You can also scope it down. For example, if you are going to troubleshoot product
catalog service, you can just say, "Hey, just show me product catalog connected
services." And it automatically pulls in all the services
that are connected to the product catalog service. Again, there's
a bunch of services here, but for me this is already quite good
and I can see that the recommendation service is calling the product catalog
service not the other way around. Suddenly this becomes the runbook and
this becomes the documentation because it automatically is updated
always as the request change, the service graph changes and then
automatically assets understands the architecture. But where Assets really, really shines is the
troubleshooting workflow. Let's say Elena or Sesema has gotten
the same alert that we saw recently. The same product latency alert, you can add a link to your alerts that
can take you to the RCA workbench and Asserts automatically pulls in for
an SLO created on the product catalog service. It can pull in all the connected services
that are also having assertions or anomalies or changes in that period.
And if you kinda go look at the graph, it's a very similar graph but it has
a fewer components because the other components did not have any errors
or issues in that timeframe. So automatically it kind of scopes it
down to the more interesting components of the system. The timeline view kind of gives you a
heat map of all the issues and you can also use the summary view to kind
of expand out all these issues. It might be hard to see in the back, so just assume it's all cool
when I kind of talk through this. So this is the timeline view and we can
see that we are seeing some blue things which is like changes and looks
like a feature flag got deployed. It's called product catalog read from
Postgres feature flag state equals one. And then after that we see that the
Postgres connections are going haywire, like it's just up and down, up and down. And then we see that the first catalog
service has started crash looping. And then we also see that the list
products endpoint is having issues. The front end is not able to list
products or recommendations. And again, the recommendation service is
having issues listing products here. Again, we saw that again, recommendation service is talking
to product catalog service. If the product catalog
service is having issues, probably the recommendation
service is too. Now let's troubleshoot
this product catalog stuff. I'm gonna look at the database because
maybe it's a database issue and automatically we understand this is a
Postgres instance and we pull in the Postgres integration dashboard. We can see that the number of rows
being queried, there's some spikes, there's some QPS connections and there's
like a spike in connections and down and spiking connections and down
it generally looks quite healthy. If we look at the Kubernetes
monitoring context, again, we know this particular metric, this
entity is running in Kubernetes. So we will bring in Kubernetes monitoring. We see that there's spikes in memory
usage, but I did not set any limits yet. So it's probably okay I should
make a note to set that. Then let's actually go troubleshoot
the product catalog service. If you go look at the App O11y,
which is open to OTel power data, we can see that it is having high latency, it's having a bunch of errors and it's
having like requests coming and going, which is kind of consistent with it
dying and restarting. Maybe it's uming. We can also kind of check that
we see that there's 200 MB limit being set, but the service itself is
using like 1516MB. So it's a very, very efficient service that just ties. Now let's try to kinda like take a
look at our logs for the service. We see that basically there are some
null pointer exceptions. Oh wait, what is this this you need to see.
There are some errors that say sorry. And I would like all my errors
to say sorry from now on. So it says too many clients. There's a null pointer
exception essentially in Go
it's coming from database sql/sql.co. So it looks like somebody turned on
a feature flag to read from Postgres and there's some code level issue
that's basically killing the service. The first thing we need to do is like
roll back the change and we also can detect feature flag changes
being rolled back. In Kubernetes, we automatically detect version
changes when a deployment changes, when a new container image is deployed
and we kind of bubble up all of that information for you folks so that you
can correlate changes and issues very easily. Alright, that
is the demo that I have. Let's kind of go back to the slides. My manager wanted me to record the demo
just in case I did not. Worked out. So yeah, to summarize, Assets not only discovers all
the components in your system, it understands the healthy states and
highlights it and it puts together all of this information in the RCA Workbench,
which can easily help you troubleshoot. You've heard about Asserts last year
when we announced the acquisition. Well, we spent the last year integrating Asserts
with every part of Grafana Cloud and we are announcing GA integration
with Kubernetes O11y, App O11y and SLOs. And we are like a couple of months
away from frontend o11y and AWS o11y. We plan to put Asserts in
every corner of Grafana Cloud. So even if you're looking at a dashboard, we will automatically understand what
entities exist in the dashboard and kind of bring you to this context that helps
you kind of understand the dependency graph and helps you troubleshoot. Alright, does this sound too good to be true? Yeah, it, it does sound too good to be true, but I would like to invite my favorite
customer Baljeet to kind of share his journey with Asserts. Thank you Goutham. So my
name is Baljeet Saini. I'm an engineering lead
in the Observability team, which is part of the larger Aladdin
engineering group at BlackRock. Aladdin is BlackRock's
investment management platform
and it is provided as a hosted service and it covers all
areas of asset management like trading compliance and
portfolio management. And my team is responsible for providing
the tools and services which enable the observability of this platform. So as Goutham mentioned, and we also saw in the keynote
Asserts is intelligent enough to understand a lot of different metrics, these standardized metrics that come
from Kubernetes, which come from tracing. At BlackRock, we had a
slightly unique situation. We follow this overarching
principle at BlackRock, which is called One BlackRock. And the way it applies to software
development is that we try to have consistency in the way that we build,
deploy, and monitor our applications. So most of the applications that we have, they produce a rich set of standardized
metrics and these metrics then power internal dashboards and are
monitoring and alerting. When we learned about Asserts, what we wanted to know was whether
Asserts can use this existing set of metrics and
provide us new insights, these insights which we may not be able
to build on our own because it is like too difficult to do or not
possible with what we have. So we were delighted to
know and working with Goutham specifically, we were able to map all of these
existing metrics pretty easily into the Asserts model. So
Asserts has a safe model. We were able to get our existing
data into this model and then Asserts started providing
us new insights into it. So to give you an example of
how we are using Assets or starting to use Asserts actually, let's take an example of a
simplified trading workflow. So if somebody presses a
button to book a trade, there are a few things
that are gonna happen. So we need to get the security details, we need to get market
placement information, we need to run trade compliance
checks. And once everything checks out, we update the trade
information in the database. So in case something goes wrong, this is the kind of troubleshooting
workflow that would happen. So an operator would receive an alert
about slowness in trade booking. They would then reference
run books to figure out which area of the trading ecosystem
is having trouble or problems. And eventually they might figure out
that the problem is in the compliance workflow. Then they have to go and check existing
dashboards that exist for the various compliance services to figure out
what is going wrong over there. They will also check logs and they
might have to copy some information from the dashboards such as transaction
IDs over to wherever they're checking the logs to be able to
manually correlate all that information. And all of this correlation that is
manually done will eventually help them figure out how to troubleshoot
further. So as you can see, this requires the operators to
have a good understanding of these various workflows. And it's not easy for somebody who
is new to just pick this up and as Goutham also showed,
documentation might exist, but the documentation
might be out of date. So how does this change
with Asserts in the picture? Actually one slide to just show what
they would look at without Asserts. So there are a few different dashboards
that they're looking at and then there is another dashboard for logs and they're
copying information across to figure it out. Changes a lot with Asserts in the picture. So you receive an alert again, but
now instead of looking at Runbooks, which again may be outdated, you are able to pull up a live view of
the system and focus in on the trading segment. And hopefully like it shows
you right there that there is slowness in the compliance workflow. And then you can dig into the
trading compliance workflow itself and pull it up in the RCA workbench
where it is going to show you a list of prioritized
assertions and pull up all the connected services that may be
having problems at the same time. So this is much better than what we had
without Asserts because now you have all the relevant information in one view. It's all up to date and
you are looking at... Asserts is helping you correlate all of
this information without having to go anywhere else. So this is the kind of view that
you would see with Asserts. The, the screenshot on the left shows
a view of the entity graph. These are all the connected services
that are being used in that trading workflow. And there is a screenshot of the RCA
workbench where all of the assertions are now being prioritized and represented
and all of the connected services are being pulled in. So in summary, Asserts help us - helps us speed up
the analysis and troubleshooting, and it's doing this by
providing us all of this all of this contextual data and
automatically doing correlations which help us to resolve problems
faster. That's all I have, handing it back. Cool. So thank you Baljeet, that's fascinating what y'all have been
doing with Asserts and it helps make me feel a little proud
too. So thank you. You, you all may be wondering what you need
to do to get started with Asserts. So let me give you a
short overview. For now. You need to have Grafana Cloud Advanced. We are going to make this available
to everybody in 2025, but for now, this is only for Grafana Cloud advanced
customers who are using Kubernetes Monitoring and Application Observability. I hope that makes sense because we're
trying to correlate data from multiple systems and Kubernetes monitoring and
application observability send the kind of rich signals that help to make
this a useful product. Thank you. Thank you.

