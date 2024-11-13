# Explore, Beyla, Asserts, Loki 3.0, AI/ML: ObservabilityCON on the Road Keynote 2024 | Grafana

In this talk, RichiH (Office of the CTO) discusses the latest updates on our announcements from our flagship ObservabilityCON ...

Published on 2024-05-13T01:18:06Z

URL: https://www.youtube.com/watch?v=7HRuppA-8Q8

Transcript: Welcome everyone. It's really
great to be here in the Bay Area, being able to give every one of
you the latest and greatest from ObservabilityCON London
directly during this keynote, we are going to be sharing a few things
about what we did the last year or so and the product releases,
which we've been working on. But first I wanted to reflect a
little bit on what brought us here. I get to travel a lot. You can see by the beginning of my
neckbeard that I'm on week three of my travels. And while I really,
really do get to travel a lot, one of the absolute highlights
are GrafanaCON and and ObsCON where we are really able to
connect with the actual people and get to shape and get to talk to the
people who really care about all of this. We turned 10 years old recently and
we maintained and even accelerated our growth through the
current macro situations. While others did layoffs, we actually grew and I feel extremely fortunate and proud
that we have both a thriving business and culture at Grafana Labs. And this is in large part because
of you - due to our users, our community, our customers. Without the continued support of all the
people in this room and people not in this room, we would not be where we
currently are. So really heartfelt, thank you. And we always do things a
little bit different at Grafana. And one of the things which makes
us differentiated in the open source observability space is
our Big Tent philosophy. Big Tent for us means we prioritize
interoperability with the wider ecosystem over our own short term interests. Most companies make you send all the
data into that one thing and then you get to make use of it. And then only if you're really done with
everything then you're going to get the value. We are different. We know that our customers and users have
many vendors and teams using different technologies and we actively
encourage and support that. Our approach allows our customers to
own their own observability story, not forcing them into any one thing. During the first part of this keynote,
we have three themes, open source, cost control, and ease of use.
Let's talk about open source first. Open source is at the heart
of what we do at Grafana Labs. It is essential to both our ethics
and to our go-to-market strategy, and we used to look up to all of those
big open source vendors trying to replicate their success and quite
a few of them faltered over time. These days, we are the big
open source vendor who's left. We are really charting a new course
through rough waters with the current market conditions. And
if I do say so myself, we are doing so quite successfully. When we say that open source
is at the heart of what we do, we mean two different things, the
external and the internal projects. If you look at Grafana, we have more than 1 million open
source instances with over 20 million users and our monthly active users
are actually higher than many mobile games. We employ 11 of the 29
Prometheus maintainers and
we sponsor pretty much all of the feature work on it. If you look at any of the features
over the last two or three years, sponsored by Grafana For OpenTelemetry, we are consistently in at least 11th
place in contributions up to sixth place recently. And we are ahead of many larger players
who would have more resources to commit if they chose to. But we don't
only sponsor the technical work. We also sponsor all the
soft stuff like for example, who sits on the governing committee
on work time or we how we are leading the Prometheus and OpenTelemetry
compatibility work and how we are spearheading profiling as a new
signal type within OpenTelemetry. And speaking about the wider
CNCF ecosystem where we
have and had various hats and roles, seats on the governing board
on the technical oversight committee, on the technical advisory group for
observability and for sustainability. Some of us have been
members since day one, But we don't just support
external open source. We are also committing to continuing to
invest to make our own core offerings open source and keep them open source. LGTM - what developers put into PRs.
Looks good to me, but also logs, graphs, traces and metrics stored in Loki
visualized with Grafana stored in Tempo Mimir. But not only
those, we have so much more, which we've introduced recently. Pyroscope
for profiles, k6 for load testing. Beyla for eBPF, Oncall
for incident response, Faro for front end observability
and most recently, Alloy, which is the only full OpenTelemetry
distribution, a collector distribution, which also encompasses the complete
code base of 10 years of battle proving, testing, and performance
gains of Prometheus. And we will continue to invest into
both the third party and the first party open source. Let's talk Cost Control next. A lot of companies, a
lot of business models, a lot of operating principles the
last few years have been built on zero interest rate on the idea
of functionally, free money. We've always been different about this. We always found a careful balance
between implementation speed and being prudent with our spending. And trust me when I say that this was
quite a culture shock for a few managers and engineers when they first
joined. But the thing is, if you do cost control right, not only does it make you more
efficient and effective at your job, it also is more fun 'cause you're not
being dragged down by all the overhead and by all the stuff which you
should be getting rid of, you actually slim yourselves down. You
can be more nimble in the operations. It's much more fun for the engineers. So over the last few quarters, we invested heavily in productionizing
our internal techniques and created new technologies on top. To be
very blunt, about a point, you'll find plenty of
vendors with mediocre and
deliberately unactionable cost overview. You'll also find a lot which help you
scale up your usage but never help you meaningfully reduce your spend. I invite you to find any other
vendor which not only gives you actionable insights into
your costing structure, but also invests heavily in
your ability to pay us less. Let's talk about the Cost Management hub. This brings together all the
brilliant cost management features, which we already built and have been using
in production internally for ages and stuff like Adaptive Metrics
and Log Volume Explorer. But also it gives you things like the
cardinality management dashboards and billing usage groups. This
centralizes everything into one place, into Grafana Cloud, making it really easy
to find, making it really easy to use. You're able to use the analysis tools
and the visualization tools and the reporting and everything which you're
already familiar with from your observability to really drill
into your costing structure. So we took all of those
tools, built new ones, and we put them into a single toolbox
for you to use and optimize your spend. We launched Adaptive Metrics
at the previous ObsCON in
New York City roughly one and a half years ago. As of right now, we have 150 customers and
we have folded away over 200 million time series
across all our clusters. If you look at the pricing, this equates
millions and millions of dollars, saved millions of millions of
dollars, which we chose not to earn. And this becoming a very fundamental
and unique strategy for Grafana Labs. We only store metrics which are needed
to answer the questions which you are actually asking and deriving
business value from. This is a good example of our long-term, greedy strategy where we strongly
believe that we must only incur cost on you, where you actually derive business
value from and align those two very, very closely. It shouldn't be a huge surprise that
we're also working on Adaptive Logs. It's the direction we are going into with
all our telemetry systems and we have an active research project to identify
the logs you need and either fold them away or even sample or drop them. Initial progress has been really good. There are differences in the
different fundamental data types, so it's taken some time, but we are working on this and if you
are interested in this and if you are a customer, we have a closed beta.
So if you want to try this, come to the Ask the Experts booth
later and, and talk to us and we can, we can talk about it. Staying with logs, we announced Loki 3.0 at GrafanaCON
in Amsterdam a few weeks ago. Loki has been accepted by the wider
developer and operator community. We've got over 100,000
installations in open source alone. And this group of people likes the
engineering choices and the trade-offs and the experience which we have built, but also we learned a lot
over the last five years. We've learned from customers that log
aggregation in particular in large companies isn't just for
developers or just for operators. There's a support use case where last
line support needs to really dig into the structure and into the logs of your
application to find that one lost order or the needle and haystack use
case in the wider sense, which really did not align with the
design goals and the initial design decisions of Loki. And to
be very blunt about this, this used to be a pathologically
bad use case for Loki really slowing you down. That's until now with Loki 3.0. We introduced this and we fixed it by
using bloom filters or we introduced bloom filters and you know what I mean? And we did see up to
1000 x speed improvement, not 1000%, 1000 x. And with this Loki is
finally best of both worlds. Where it maintains the speed
and the huge price advantage, but also enables you to quickly look
through all your data if you need to. And there is ease of use. All
of this is great technology, but you have to be able
to use and consume it. Observability is becoming infrastructure,
water, electricity, internet. They just come out of the wall. If
they stop coming out of the wall, you call someone they fix, it starts
coming out of the wall. Again. This is how we think about observability,
about becoming infrastructure, about being easy to use. We go
away, we stay in the background. You can use and leverage the tooling, but you don't have to think about the
why and how you just get to read the benefits and get on with
your own business problems. Most of you will be familiar
with the term crossing the chasm. Our projects have been really, really
popular with this early adopter crowd. The people who kind of like it when it's
a little bit hairy and maybe has a few rough edges, but you get the
absolute bleeding edge of technology. And this group keeps evangelizing
on our behalf and this is great, but we also see significant adoption by
the early and by the late majority. And those people are not as
successful as we'd like them to be. Those people don't have the time, the expertise or maybe just access to
raw talent to get the best out of our products. And it's up to us to make our products
easier to use for this early and late majority. So we introduce
things like, for example, Explore Metrics. I'm a Prometheus
maintainer myself. I find writing PromQL easy
to sometimes pleasant, but I'm also very much in this
early adopter demographic. So don't take me as the canonical example. Explore Metrics surfaces data
and trends automatically. You don't need to write a
single query to find outliers, interesting patterns or other
data worth investigating. We surface this to you and you accept
or dismiss the suggestions which we are making. And interactively have a fully
click path based way to build an analysis into your data without ever
having to write a single PromQL query, but also to be clear, at any time you can flip back into expert
mode and you see the actual queries you can learn from it and have a good
feedback cycle to help you improve with the technology if you so
choose. But you never have to. We have the system of Hackathons at
Grafana Labs three times per year. Any Grafanista can take a whole
week and work on whatever they want. The only condition is at the end you
have to submit a video talking about what you did. And then we have voting and
we have the winner and everything. And last hackathon happened
a week before KubeCon. We had something to basically
build an Explore Logs feature and the video was so good
we're just sharing it. Hello, I'm Matt Ryer. Welcome
to Grafana's Log Quest, a game show where we put new
Loki features to the test. Two contestants will go head to head. One will show us how you would solve a
problem today with current Loki tech. The other will show us how you use
innovations in this hackathon to solve those same problems. Meet Cyril. Cyril been working on Loki since
2019. Cyril Hello. Hello Matt. Let's meet our other contestant Jonathan. Jonathan is new to tech and he got his
job here only because his uncle has got some dirt on Tom. I am also
gonna have to play Jonathan. Alright. Hey Jonathan. I'm
Jonathan. To be honest, I'm not really into computers,
not really my thing, right? So it's safe to say that you
don't know LogQL, Jonathan. Couldn't even spell it. Oh, ,
that's . That's good isn't it? In round one, our contestants need
to find out the misbehaving pod. Within the Mimir ingestor service. It's
Cyril to go first. Off you go, Cyril. So this is gonna be super simple. So first we're gonna go to explore. Well I can see why Loki is so
popular. Let's see how Jonathan fares. How would you do it with the new
UI, Jonathan, over to you. Right. Well I'll just pick the
service then filter by labels. This is done automatically for me.
Level is what I want, and I want errors. So have a look/ There you go.
That's the pod with all the errors. Okay, thank you very much. The results
are in. Well, Cyril, you used many years, three or four years of LogQL experience. Jonathan didn't use any and only took
a few seconds and is in the idiot. So for round one,
Jonathan takes the point! In round two, right? We found the pod, but there's been an incident and we need
to find out which users were impacted by a particular incident. Cyril, it's
you to go first. What do you got for us? We found the pod. Again, very simple.
We just need to remove everything. Excellent. Thank you very much.
Congratulations! Jonathan, how are you gonna cope with this? Well I'll just do one
click here. And then I'll just go and do another
click here. Look, that one, that one took me two clicks for round
two. The point again, goes to Jonathan in the final round. We are looking
for the version number of a service, but the trouble is the logs
are very noisy. Cyril to play. No, I'm not gonna play. I know that I have to keep excluding
things one by one and it's gonna take too long. And what if I accidentally
exclude the line that I'm looking for? I think Jonathan can just do it easily
by pausing the extracted pattern. He doesn't even see the noise. He can
jump right to the river and logline. Well. I think it's, congratulations again
Jonathan and thank you for watching. So hopefully this gives you a little bit
of an indication of how quickly you can delve into stuff with just visual aids. because we are really good at pattern
detection with humans without having to write all the complicated and
having to learn about Loki at all. And you're going to be shocked and
surprised that we are exploring the same thing for traces. There's always a nuance between the
different fundamental data types. So this is again, taking
some research work, but we are working on this and we are
very confident about releasing this in the future. So you might have heard
about our act three, where in act one we built best in
class visualization and in our act two as a company we focused on building
best in class database engines for all the different fundamental data types. Now Act three is about
making things easy to use, about creating complete
end-to-end solutions. We've built a series of opinionated, integrated and easier solutions
on top of our LGTM Stack for infrastructure monitoring. We
have curated dashboards and alerts. We have the Kubernetes
application for testing. We have things like k6
and synthetic monitoring. And for IM we have solutions like
alerting on-call incident and we are improving all of these solutions. Tying back to an earlier theme, we recently launched the cost
monitoring within the Kubernetes app. So you can actually crosslink between
the two and start moving even more seamlessly between all the data which
makes up the knowledge about your business. And also recently we announced the
general availability of our SLO management tool, allowing you to
easily configure, manage, and defend your error budget based SLOs. Let's delve into application
observability for a bit. We started the public preview in
August and thank you to all the close beta customers who helped us make
this a really good product for everyone. Some of them might be in
the room, I don't know. Application observability is an
open-end opinionated solution. You instrument your applications with
the open source OpenTelemetry SDKs and send that data into our infrastructure
using OTLP, the OpenTelemetry Protocol, all using open standards. The data are then hosted in our backends
where we visualize them from the new application observability plugin.
And again, tying back to earlier, this is act three, just taking the thing, making it easy to use and enabling the
engineers to immediately derive value from the data without having
to do any of the hard work. We announced Faro at the previous ObsCON
as the solution for our monitoring front ends. Faro is an SDK and it captures the front
end of your applications. Again, you can send the data into Grafana Cloud
or you can just store it in your own open source backends if
you, if you prefer. But if
you're running Grafana Cloud, you can also visualize all of this
in our frontend observability plugin. We can really understand the performance
of your application as your customers actually perceive the application
to be running. If you use traces, this means you can actually follow your
complete stack through your complete stack if you have an issue somewhere
from the front end to the backend and everywhere in between. For backend developers, we also have great solutions applications
written in Java, .NET, Python, similar languages can easily be
instrumented with open source, OpenTelemetry SDKs. And we are also contributing to the
.NET and the C# and Java as the case for OpenTelemetry based on what our customers
tell us where we need to go and what they need. OpenTelemetry makes it possible for us
to offer you the breadth for all of those instrumentation produced by
the OpenTelemetry community
and improves ours and your speed of execution. But it also gives you confidence that
the work you put into instrumenting your applications is going to
be paying forward for itself. Because You're not locked in.
You're fully on open source, fully on open standards. But that doesn't solve everything. There
are hard to instrument applications. For example, if you're developing
in a weird compiled language, if you don't have access
to the source code, if you have many conflicting versions
of that one library and you have an absolute hodgepodge of different
deployments in your infrastructure, all of those situations can
make it hard to impossible, to properly instrument your code. But you can still use Application
Observability because we also put out a solution based on eBPF.
eBPF doesn't require you to
instrument any of your code. It just relies on the Linux and soon
the Windows kernel to analyze and send data about the cause which your
applications make into the kernel APIs. And we derive the data from that. So we built on this cutting
edge technology of eBPF to
create Grafana Beyla for you. Again, Beyla leverages OTLP. So you can send all your data to all the
OpenTelemetry-compatible observability solution like ours.
It's fully open source, licensed under Apache license
version two. For those who missed it, we announced our acquisition
of Asserts AI in last November. And as we got to know the team better, we were really impressed by the
technology stack, by how they worked, how smart and focused they were on solving
the problem of getting an oversight over all your data. And we immediately
hit it off. And we are really, really looking forward to keep integrating
deeper and deeper and deeper with all of this technology. I dare say you might be blown
away by what you're about to see. So it's my absolute pleasure to
introduce a new coworker of mine, Manoj to the stage. Thank you. It's great to see you
all. I am a local Bay Area resident, so I like to travel like Richie,
,  and all, all other coworkers
very excited to be here. Let me tell a little bit of
story about myself and my team. So before I started Asserts I was
at a company called AppDynamics. I moved to the Bay in 2009
when I joined AppDynamics. I was the fifth employee there and was
part of that for 10 years and building all the application APM products
there. But through those times, me and my team, we were obviously
heavy users of AppDynamics, inside AppDynamics. We had trouble. We had a fairly complex architecture and
we were pretty good at building alerts from our systems, but those alerts were just fired nonstop
and we didn't know how to correlate them, you know, how to figure
out what the root cause is. We often had to call our best
engineers. So me and my coworkers, you know, eight of us kind of left AppD
to start Asserts to build this product. And last year, October, we joined
Grafana Labs and I'm very excited to, to show you how it's now
working inside Grafana. So just to make sure I'm not fooling you, please welcome the newest member to the
Grafana Left Navigation, called Asserts. It's not available to everybody yet, but we are already onboarding our
first 10 customers and starting to work with a lot more people who are
already on Grafana and Grafana Cloud. So the way Asserts works is, let me quickly bring up
this screen here. So you ... So when you send your
data to Grafana cloud, your metrics and traces, the metrics and traces in Prometheus and
OpenTelemetry world already have a lot of metadata built into them. So they have labels and in the
OpenTelemetry specification, they have resource attributes. So what we can do is we can join these
labels and discover a service graph. I use the word service graph. When
I use the word service, you know, oftentimes you know, APM tools
provide you different views. You know, you wanna look at your infrastructure, go to this other section or look at
network, go to the other part, right? But when we conceived
Asserts from ground up, we had the opportunity
to think through it. What if we could build all this data
together and store it in a graph database? So when you are looking
at Asserts, you know, it'll already discover your,
depending on your environment, it'll discover your namespace and parts
and nodes and you know how they'll link to each other. So for example,
I can look at the service here, they're connected to this part here and
this part is connected to this node. So it's like one massive graph that is
getting built here and kept it in for you, but you don't have to worry about it. You know how it is stored
and everything else. Now let me switch your attention
to this application that I am the tech lead for called Robot Shop. So when I type Robot shop services, essentially what I did
is I have saved a query, which is saying that all the services
that belongs to Namespace Robot Shop, I wanna see them and how
they're talking to each other. Now this is interesting I can see the
connections and those connections could be derived from your service mesh
data from your OpenTelemetry traces or the newest addition to
Grafana family, the Beyla agent, where we can actually instrument
below layer seven, you know, look at actual network bytes, bytes
flowing between different systems. So you can see those green lines
here are actually coming from Beyla. So when I switch this time
range from five minutes to 24 hours, what you'd notice is that suddenly
this looks way more colorful. Now it's more interesting. So all of
you who have used APM tools, you know, you probably understand
this idea of like, you know, APM tools have automatic
knowledge, you know, built in knowledge of
what is important to you. So Asserts is fundamentally
built to the same concept. It's just that it is completely
agentless. So for example, here these services are now
stack ranked with my Nginx and risk controller on the very top, followed by my shipping service because
they are exhibiting what we are calling as a lot of assertions. So the idea
of assertion is a lot like, you know, we are engineers, we write
code and write tests. So what if you could try and
test or checks on your runtime, on your runtime telemetry
data? So for example, here the system is automatically
detected like a new version was deployed and some anomalies have happened
here. Now I'm getting curious, I wanna start looking into more. So by just clicking this
button called troubleshooting workbench. What Asserts
did, is behind the scenes, it went and scanned the graph
and identified only the services connected to shipping and the infra
at which is running and built a flame graph of all the different alerts. Now RichiH was talking about
writing PromQL. Now PromQL is fun, interesting when you're into the zone, but once you're outta the zone
it's not fun anymore. So , so it's like what if we don't
have to write PromQLs? You know, what if we could codify all
this PromQL into a system? So for example, we look out for
saturations and admins being changed, new deployments, anomalies
here and failures and errors. The stuff that we always look out for
when we're troubleshooting, right? So there's this codified all this
knowledge for different ecosystem. Like in this case when I zoom in, I'm looking at now the shipping service
at the very top here showing that there was a new deployment happened and
there was a massive spike in garbage collection and there is a latency
anomaly in two different endpoints. Now these baselines that are getting
created are all automatic for you. So we know the metrics, we know the baselines and we are
generating the assertions for you so that when you're troubleshooting
they're just, just readily available. You are not have to get alerted
on each and every one of them. You can see it all in
one place, in one group. Now let me quickly jump into the
summary view where I can see a mini graph of like how these things
are connected. So you can see that the ingress controller here is the
load balancer receiving traffic, talking to shipping
service and going to MySQL. And then a new version was applied. So
we know Kube container info metrics, we know a new container ID was generated. So we automatically watching
the labels, we figured out okay, new version was deployed. So we are observing every
endpoint and creating baselines. So that's why we know there's a latency
anomaly on this specific endpoint. So, and as we scroll down here, you can see the MySQL has a spike in
the buffer pull request and network bytes. Now what's interesting is that you have
your infra metrics from Prometheus, from Kube State Metrics,
from MySQL exporter. You have a traces from OpenTelemetry
or Beyla is sending your . So we are able to combine all the data
in a one single cohesive fashion and show you all the signals without, you have to worry about writing rules
or building dashboards for each one and every one of them. Now with that said,
you know, I love my Grafana dashboards, so I definitely, I'm
seeing a JVM spike here. I'm getting curious and I wanna look
into the garbage collection metrics here. So when I click on the KPI, what we do is we automatically recognize that this is a JVM
micrometer running Spring Boot service. So you have pulled in the right dashboard
for you and showing you the relevant metrics for that instance, for that time. So you don't have to construct this
dashboard or remember where it is kept in which folder. It's all organized for you, all kept for you so that you
can access it in a single click. Now if I am looking at
my latency anomaly here, now I'm really curious now which
line of code, what exactly happened? Maybe there's a call to SQL
database, can I see the query? So typically all this information
will not be in metrics, but they're very much in the
traces. So I can jump into traces. Then Asserts will automatically filter
out the service name, the endpoints, and pull in the slow traces for you
and showing you the classic tempo trace view that you're very familiar with. But it's contextualized for
you and pulled in for you. Now the one last thing I'll add
here is that when you are looking at all this data, you're looking at
all the level one connections, but the graph can be
really long and wieldy. So if you really get curious now to
see does this affect anything else, you can start asking all
kind of interesting questions
to this graph saying, "Show me other problematic
connections." You know, what else happened because this
application was having this outage. So you can ask this question and it'll
instantly start querying the system to bring you the level two connections
and level three connections. And there's a lot more
to tell about Asserts, but I'll love to show you at
the Ask the Experts booth. So please come and see
us. Thank you so much. So there is a lot going on
with ML in the industry. And to be clear, a lot of
unsubstantiated hype. To date, machine learning hasn't
proven to be a magic bullet. We are very much focused
on a pragmatic approach. We make targeted investments like for
example, adaptive thresholds forecasting, outlier detection. We see GenAI as yet another
tool to help you solve problems. For example, LLMs and Vector DBs offer new
opportunities to understand your systems. We set ourselves three
main goals with our our endeavors into ML/AI. The first
main goal is to minimize toil. We are accomplishing this by building
solutions like Application Observability or like Asserts to give you a little bit
of assistance when you need it the most or to give you a real boost
when you really, really need it. Second, it is to provide key insights to your
team to accelerate their understanding of changes in the system. Part of this is bringing those key
insights into your team's investigation processes. Also, part of this is to just aid
engineers who are looking across the different observability signal types
for connections across all of them. Metrics, logs, traces, profiles. And finally we must reduce
noise in the system. A lot of the current solutions generate
more noise for people to filter through and this actually starts to drag
engineers down. It makes you slower, not clicker. Unnecessary noise reduces
your velocity and that means you don't get to solve the problems
of your customers and solving business needs. You just have to deal
with all the extra noise. We are doing all of this to Grafana way
- open source, Big Tent, transparency. Open source and Big Tent and transparency
are key to everything we do. Talking about open source, other vendors
are repeating mistakes from the past. They build black boxes, they build proprietary
solutions where clearly open source will win. Open
source is in our DNA. We've been developing in the
open since day one, Big Tent. In this case we mean giving you a
choice about what LLMs you want to be using. Today, we support OpenAI and Azure and we're
actively working on supporting more. We really want to give your teams the
flexibility to hold the keys and choose your own direction in your
LLM story and transparency. Many enterprises have fears about what
is being sent into those black box large language models. At Grafana we
default to open: open data sets, open prompts, open development. This allows your team confidence
in this emerging space. And to be very clear on something we
never, ever train on customer data. If you want us to, we can fine tune
in on it, we can fine tune on it. So let's look at the LLM App. We've built GenAI directly
into our Grafana open source. By this, we have a fully open and shared framework
which everyone can use to build on top of the LLM features within Grafana,
not just our internal Grafanistas, everyone in the open
source community as well. This is a great example of a small
assist and this can quickly make teams more efficient and
effective at their jobs. What you see here is us using an
LLM as a helper to add titles and descriptions to dashboards and panels.
This is not a huge game changer, but it helps engineers with small
hurdles. It helps them get started. It helps you build a common
language throughout all of your teams, throughout all of your org without having
to do all the synchronization work on the social level. And this, by extension, makes your dashboards more
robust and more easy to consume. For other parts of the org, what we see here is we are using the
context of a discussion around an incident to boost the team, building
a summary for a set incident. Solutions like this can really start the
learning and the communication process for teams which might not always
be doing post incident reviews. And then they can augment
this as as they see fit. In the end, this improves the level of detail and
the timeliness of informing stakeholders. In our tests, we found that if you start with this, you have a 3% on average higher score in
semantic similarity scoring than if you start with a human generated summary. And this also allows you to really quickly
just update other stakeholders about the current status of an
incident. And finally, we can use LLMs to jumpstart
more challenging tasks.
Like again, for example, writing PromQL. Here, we've built a vector model based on
thousands of open source PromQL queries and we can use those alongside OpenAI
to allow users to write more effective theories more quickly. And
also they get feedback. So there is a cycle built in of
reinforcement learning and actually again, building tools which make subject matter
experts more efficient and effective at their jobs, not pretending
we can just replace them. And finally, there's Sift. Sift helps you quickly identify
connections to accelerate
understanding when you need it the most during an incident. Sift uses all of the data, all of
the context to accelerate your team. We extend IRM on top of the
observability data you already have. You can trigger a Sift check from any
change in your system, from an alert, from oncall, from an
escalation, from a dashboard, from Explorer It doesn't
matter, but you are in control. You choose to go that path and
then we do the hard work for you. And one of the things which is often
overlooked in most companies these days, Grafana has the most context
about your business already. So we have the most powerful ways to
get insights from all of the that data. We can look across all the different
signals to find correlated changes. Again, once you trigger this as
the subject matter experts, we really accelerate engineers in
understanding system behaviors. When systems change, what we see here are resource
connections from Kube state metrics. There's a slow request from the tracers. There's an error patterns from the logs. So we drill down automatically
into the error pattern, log objects using drain, basically expanding and massively reducing
the search space at every single step and doing this automatically in the
background for you. In this case, we found logs which the surrounding
Kubernetes service has and found several patterns in this. And four
of those patterns correlate
with significant changes. When drilling into the arrows, we see the exact log lines which represent
the pattern and also we see the rate changes during the incident. Thank you. . And we already accelerated the engineers
with better understanding of the system, but we can take
this one step further. We can integrate with the LLM and with
the GenAI and describe typical problems and resolutions which correlate
with this type of error log. Again, not pretending it's going to be perfect, but kick starting people and
giving them a path to start at if they're out of options. All of
this is available on cloud already, so you can just use it. So to summarize, first we looked at how we make
things easier with the help of of Explore. Went through all
our new launches, including
Loki 3.0, Beyla, Asserts, and finally ,we walked through how a
deliberate and respectful engineering approach to LLMs and GenAI
might actually look like. Thank you very much.

