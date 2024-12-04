# How Pipedrive switched its observability stack to OpenTelemetry & LGTM | ObservabilityCON 2023

The cloud-based CRM company Pipedrive has been relentlessly modernising its observability stack, first adopting Grafana visualisation and Grafana Mimir for Prometheus metrics, then recently completed a migration of its distributed tracing from a third-party SaaS provider to OpenTelemetry and Grafana Tempo, and its logging stack from Graylog to Grafana Loki. 

Along the way, the team developed its own in-house library to include OpenTelemetry in its roughly 750 microservices. 

Observability Platform Team Lead Karl-Martin Karlson shares Pipedrive’s journey migrating to the LGTM Stack in an infrastructure spanning 8 data centres, 5 physical locations, and over 20k Kubernetes pods.

Chapters
0:00 Introduction to Karl-Martin, Pipedrive, and Pipedrive's infrastructure
1:39 Pipedrive's observability stack before LGTM and OpenTelemetry
3:32 The challenges that Pipedrive faced with their previous stack 
5:47 Pipedrive's distributed tracing use cases 
6:28 What led Pipedrive to choosing OpenTelemetry and the LGTM Stack
7:14 The timeline to get it all done
8:50 Enabling OpenTelemetry
9:19 Pipedrive's architecture
10:34 Implementation challenges 
11:46 Recorded metrics vs. raw metrics
13:26 Label cardinality: Understanding log and metric labels
14:00 How we made the data useful (visualizations!)
18:09 LGTM infrastructure by the numbers
19:19 Pipedrive's future plans with Grafana

Published on 2023-11-20T06:53:15Z

URL: https://www.youtube.com/watch?v=0IKkD235mEc

Transcript: My name is Karl-Martin. I'm
a observability platform
team lead in Pipedrive. And this is my first time doing a
presentation for a crowd this big, so please go easy on me, .
So a little bit about me. I am from Estonia, and this is a picture of an Estonian
flag colors taken from Estonian landscape, so quite clever.
And on my free time, I like to go racing, and this is a picture of me in my
race car at a track racing event. So, yeah, first to set the stage a
little bit about Pipedrive. So Pipedrive is a CRM designed
to help small businesses grow. For over 10 years we've been
committed to building the best CRM, CRM by and for salespeople.
The result is an easy to use, effective sales tool that
centralizes your data, helping you visualize your entire
sales process, and win more deals. A little bit about our infrastructure. We have eight live product regions
running in private cloud and AWS We have about 4,400 virtual
machines running 750 microservices. And our containerization
platform of choice is Kubernetes, which holds about 26,000 Kubernetes pods. About some of the technologies we
use. We use MySQL Kafka, CouchDB, Elasticsearch, which are the bigger
ones, and of course many smaller ones. So now I will go back a few
years and talk about or show how our observability stack
looked back in 2021 before we implemented LGTM and OpenTelemetry. So onsite Grafana has been in Pipedrive
for six plus years together with Prometheus. And it has always been the standard
to visualizing metrics exported by microservices. We had GrayLog
in all of our product regions and Zabbix for hardware and
operating level monitoring, which back in the day we also
used for microservice monitoring. So we did those web checks back
there, but that didn't scale. Then we have always had a SaaS APM vendor, which we have switched back and
forth between over the years, which of course I'm not gonna name,
but we have been to most of them, most of the biggest ones Now a diagram how it looked
like. So starting from top, we had the Grafana and
aggregation Prometheus running
in our management region. Down at the bottom we have product
regions where we had Graylog stacks Prometheus Federators. And five years ago, Pipedrive was a single region product. So our app was running in only
one data center on one location, and over the years it started to
growing and now it's at eight, so eight of these boxes down there. And with Pipedrive growing
this observability approach
really didn't scale, and we started running in those
single instance limits for Prometheus. And it was really, to be honest, a pain to build a Graylog
stack in every product region. And then to add those Grafana data
sources and reconfigure alerts and so on. Some of the other
challenges that we had, so logs, metrics, and APM data was spread out
between different platforms. We were dependent on third parties
making pricing policy changes which made it difficult or even impossible
to forecast our observability budget. There really was no single UI. All of the platforms use
different query languages, and they had different
visualization capabilities. It was really difficult for anyone
to do any kinds of investigations, so you first needed to know
where and what to look for, and in even some cases in which
region you had to look to. There was no connection to internal
platforms like our CI/CD pipelines and back office where we hold our
client data. And of course, the entire stack was falling behind on
scaling capabilities compared to how fast Pipedrive was growing. So we definitely had the need of
better performing and better scaling of observability platforms. And now onto how the LGTM
helped us out with this. The components we chose .so Mimir to
replace our recreation Prometheus in the management region. It's a highly scalable metrics backend
and we are not even close to any of the limits that Mimir can handle. We deployed Loki to manage or to
aggregate all of our logs from all the Pipedrive regions. So with Loki, users don't need to log into every
regions' UI and they don't need to switch between, between data
sources. So with this, we will have less alerts
missed and less problems when new Pipedrive regions pop up. We deployed Tempo for storing the
final traces and for the entire APM or distributed testing platform, we had the goal from the beginning to
provide a similar or better functionality, what we had with third party platforms. And finally we used OpenTelemetry
collectors and developed our own wrappers for upstream OTel libraries, which provide the necessary configuration
and installation steps for automatic instrumentation. Similarly,
how the third party vendors did it. So the use cases we have
for distributed tracing, so it's not just some industry passwords, we actually do need it
to make Pipedrive better. So we need to understand where
why and to who Pipedrive app is not performing as expected. We need
it to solve production incidents. And also it provides us with
unified metrics which will have, which will set the paces for SRE to have
standardized alerting for all of our services. And really deploying onsite Loki and
Tempo laid the ground work for having it all onsite in the inside
of our data centers. Why we chose OpenTelemetry and LGTM. So OpenTelemetry is widely
supported and invested into by CNCF, and as the name states, it's open. So we can keep the instrumentations
in place while changing UIs and backend platforms. Using Grafana OSS, we could build our own UI and
really tell our own story. We didn't want to be locked into
some uncustomizable and generic UI, and of course we could link to our
internal data sources for additional context for our dashboards, and maybe really important
also we could predict costs and really pay for what we
used, so for CPU, memory, networking and storage About the timeline. So we kicked it off in
January 2022 with a team of four engineers, including
myself and two, two developers. So in January we deployed Mimir
and one month after that Tempo and Loki while integrating Mimir
as our metrics backend. In March first traces or first
trace for like a demo web was received in Tempo and Loki. In June, three months after that
initial OpenTelemetry pipeline was deployed
to one of our regions, so we could actually get the
telemetry data from some test services in Pipedrive. Then four months after that, already 10 live services
were using OpenTelemetry. But this was more like to
generate some load to understand how our pipeline survived the
pressure. And during that time, I think we overhauled it or changed it up, like three or four times
at least, completely. And like started from zero because
what worked for like one service or 10 service didn't work for 20
service. Five months after that, we had 125 live services
using OpenTelemetry. And after that, two months later, we about 200 where we already
had created the UIs and we had actual use cases from live environments
where developers were using our UIs. So to enable OTel for a Pipedrive service. So all the previous APM platforms
had libraries that were quite easy to implement, so we wanted to keep the same
simplicity by creating auto wrappers for Pipedrive services. These are the three steps you need to
take to keep your service or to get your service instrumented. And everything else is automatically
populated in the backend with some Grafana Mimir and Tempo magic Architecture. So how does
our pipeline look like? So at the top we have a Pipedrive
microservice instrumented with a wrapper, which generates some OTel data
and it's received by a OTel collector. So this is open
telemetry collector contribution, or I don't know, what's the exact name. And it's running in daemon in Kubernetes. So to the left we have a
dedicated Prometheus instance, which is which will receive the
raw metrics generated by OTel collectors. And in there we are running
recording rules and sending the final recorded metrics to Mimir. I'm gong to talk about recording the
metrics recording part in detail in the upcoming slides in the
middle the final and filtered, and then rich traces get sent to
Tempo. And on the right hand side, we have a small workaround
to generate logs from spans. So we also have Grafana Agent running
side by side with OTel collector, which generates logs from spans, and they get sent to Loki for
searching and other purposes. Some of the challenges we faced during
the implementation. So when we set off, I would not have thought that metrics
would be the most problematic for us. So label and metric cardinality, which
directly links to query performance. So we really needed to understand the
meaning of those log labels and metrics that are being generated to actually
have some value out. From there. Then optimizing query
performance for end users. So visualizing seven days of OTel data
really should not take like a minute or two to run, so no one
has time to wait for that. Then applying the knowledge that we
have learned to real use cases where, for example, a Pipedrive service
is slow, then which metrics, logs, or how should they visualize it? And so on for our users
learning another query language and figuring out UI and for
observability team understanding, as I mentioned, understanding the actual business
cases and implementing them in our stack. So by adding or removing labels
or summarizing and so on, or even optimizing queries. So the recording or the metrics
recording, why are we doing it? So as I mentioned, metrics was one of the most
complicated problems for us to solve. So having too much and
not having enough of them. So we decided to spend
the computation resources, durning the metrics ingestion
by running recording rules and which enables us to cherry pick the
metrics that we actually want to see. And we were able to also keep the
labels that we know that we need for the dashboards that we have
graded. So running histogram, quantile functions is really a painfully
heavy and painfully resource heavy process. So we really didn't want to
leave all the Loki and Mimir pods just idling and waiting
for those queries to run. So this was like a super critical step
in making the UI usable while loading 10 plus panels on a single Grafana
dashboard. So our users don't wait, have to wait for those small
spinning wheels to load all the data. With Mimir and Loki, of course they
could be scaled up by, you know, throwing more money at it.
And by money I mean resources, but we didn't think it was like
really reasonable to leave this, everything idling and waiting
for those queries to run. So by using recording rules
we could reduce our initial metrics data set by 97%. So from
1 million active time series, only 30K consumable metrics
were left and we actually know that we are using them. Label cardinality, so understanding log and metric labels. And it really all became down to balancing
resources and observing query times, and of course, our user feedback. So we needed to decide where
we use metrics and where
we use logs for querying. So the lowest level that we have
decided to create metrics is one single HTTP transaction, throughput,
and transaction latency. So if we need anything
more detailed than that, we should already turn to logs
for more complex querying. And now we have all this data, we are gathering it we know
the cardinality how can it, how can we make it useful
for our developers? For that, we decided to create
a bunch of dashboards. I think it's around 10 to
really visualize this data. So starting from the top, we have a
dashboard called Pipedrive Overview where, for example we can monitor
the performance of entire Pipedrive app in one product
region. Moving down from there, we have stack an infrastructure overviews
where we can monitor the performance of, for example, one
stack. So by one stack, I mean like a combination
of services, for example, how search function and Pipedrive is
functioning and how automation is doing and so on. Moving down we have service and database
overview where we st where we are still using metrics. And after that we have already HTTP
and async transaction breakdowns, where we are already starting to
combine logs and metrics in the queries. So if you want to see like
high level throughputs, we are still asking Mimir for
metrics. But if, for example, we want to see already maybe
per like authentication method metrics or graphs, then
we need to turn into logs. And finally down at the bottom layer, we already have like a single user
or company performance in Pipedrive, where most of the data
comes from Loki logs, and from span logs and these
dashboards we call Company Profile. All of the dashboards that we have created
have unified variables look and feel. So with, with these dashboards this enables us
to really extend the context to data sources, which are not related to at
all. So, for example, back office, where we hold our client data, Zabbix where we still do some
operating system level monitoring, and other internal tools. And if things take a if it
really turns for the burst, then we also have deployment
annotations to see what and when was deployed. This is a second example of a company
database overview. So it's a, again, a really good example where we combine
at least four or five different data sources on one single dashboard. So here we have some metrics
from our back office. We have data from Zabbix
also from Loki Logs, and some from Prometheus metrics. So really really this dashboard is
a really good starting point for any support engineer starting
the investigations. So if we have a customer complaint, they
can open up this dashboard and like, get only at this company
ID and get all the, like, basic information they need
and verify all the high level metrics from this company. So when we kicked off our project, we were still running Grafana version
8 in our production environment. So we really needed a way to
improve the user experience. So what we decided to do is
to build our own small plugin that that creates a basically a easily
accessible and always visible green button on the right hand
side of every OTel dashboard. And with this it pops up
a menu with all the listed dashboards. So if you click
on, for example, if you
start on Pipedrive Overview, you can click on the next let's say
stack overview and all the labels which you have selected, and all the variables will be kept
and you can you can navigate on the next one. So it really helped us to improve
the user experience with those OTel dashboards. By now we have already
upgraded to version 9 of Grafana, and we are looking into replacing this
custom navigation with Grafana scenes function. Some of the numbers from our LGTM stack. So we have everything running
on about 1000 containers consuming 360 CPUs about
1.3 terabytes of memory and 2 billion logs per day. We have about 27 million
active time series. So this is combined together
with OpenTelemetry and
with our entire monitoring stack, so all the metrics that
our services also exposed. And we are consuming about
300 terabytes of storage. So we are actually nowhere near of what
some other presenters have presented, so like tens of thousands of terabytes. Yeah. and we also noticed that
once we implemented OpenTelemetry, we had some services producing
traces, which contain about let's say 30 to 40,000 sub spans. So our maximum trace
size is, is 64 megabytes. And sometimes we still hit the limits
of our, of the like maximum trace size Future plans. In the future, we are planning to have all Pipedrive
services instrumented with OpenTelemetry. We are always looking into
how to improve efficiency. So to reduce the resources, the entire stack consumes as I mentioned
already move to Grafana Scenes where possible then have standardized alert
alerting for all the OTel metrics that we have are right now
generating and of course improve performance for the users. So making the UI better and where possible
as Tempo is getting better and better each day. Then implement TraceQL to
replace LogQL on where we can. Conclusions. So did we actually
achieve what was planned? And I'm really glad to say that
yes we did, and we have like, really well working platforms with
Loki, Tempo, Mimir, and Grafana, and I hope that this presentation
is an encouragement to anyone who is planning to head down a similar path. And it really is all possible
to do with open source and of course a great team. Thank you.

