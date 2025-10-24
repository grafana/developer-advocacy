# From Zero Budget to Complete Observability with Grafana Cloud &amp; OpenTelemetry | AXA Germany

Published on 2025-10-22T16:42:18Z

## Description

When a five-person team at AXA Germany set out to build a no-cost monitoring stack, they never expected it would evolve into full ...

URL: https://www.youtube.com/watch?v=slylwkcCErw

## Summary

In this video, Sebastian and Julia from AXA Germany share their journey of adopting Grafana Cloud for their monitoring needs, which initially was not their intention. They discuss their small team's challenges in creating a monitoring solution amidst budget constraints and a lack of developer support for building metric endpoints. By integrating middleware components and utilizing open-source tools like Prometheus and Grafana, they successfully established a user-friendly monitoring stack that encouraged developers to engage with observability. The presentation highlights their innovative solutions, including a Prometheus Management Agent and a self-service web UI for alert management. Ultimately, their success led to increased recognition and budget allocation for monitoring, prompting their migration to Grafana Cloud to streamline infrastructure and enhance observability efforts.

## Chapters

00:00:00 Introductions to the speakers and their roles at AXA Germany  
00:02:30 Overview of their team structure and initial challenges faced  
00:05:00 Discussion on the need for a monitoring solution and inspiration from Gene Kim  
00:08:15 Explanation of how they decided to build a monitoring stack using open-source software  
00:11:00 Introduction of custom exporters for middleware components  
00:14:00 Decision to use Prometheus and Grafana for visualization  
00:17:30 Launching their MVP monitoring stack and initial user engagement  
00:20:00 Development of the Prometheus Management Agent for easy configuration  
00:24:00 Introduction of the Conflict Management Backend for metadata enrichment  
00:28:30 Transition to Grafana Cloud and discussion of future improvements and features needed

# Journey to Grafana Cloud: Our Experience at AXA Germany

Hi everybody, my name is Sebastian, and this is Julia. We are from AXA Germany, and today we want to share how we ended up in Grafana Cloud, despite initially not intending to go that route.

## Team and Context

To give you a bit of context, we are part of a small team of around five people focused on operations topics. I'm the product owner, and Julia is one of the engineers. While our overall team size is slightly larger than five, this smaller group was the most relevant for our project at AXA Germany. 

AXA as a whole is quite large, but our German entity is relatively small, with only about 400 developers. We faced several challenges that led us to consider building a monitoring solution. 

## Initial Challenges

In 2021, our team was working on a log management stack, and once that was completed, we began to think about our next steps. At AXA, we follow DevOps practices like many companies today, and our development teams were encountering numerous challenges in running their applications in cloud environments. 

We came across a quote from Gene Kim in "The Three Ways of DevOps" that inspired us to focus on metrics. We believe that monitoring serves as a feedback loop for IT operations, allowing development teams to understand how their applications are performing and where improvements can be made. Thus, the idea of enhancing our monitoring capabilities took root.

## Building the Monitoring Stack

Initially, we had existing tools for monitoring, but they were outdated and used mixed technologies, which is common in many organizations. 

### Core Challenges

1. **Budget Constraints**: When I discussed our monitoring initiative with management, they were supportive but stressed that we had no additional budget for this project. The budget for observability had to remain the same.
2. **Developer Involvement**: They also asked us to implement monitoring without requiring developers to do extra work, which made our task even more challenging. 

Given these constraints, we had to think creatively about how to start our observability journey without heavily investing in infrastructure or demanding extra work from developers.

### Open-Source Solution

With limited funds, we decided to build our entire solution using open-source software. However, we faced another hurdle: our team was not allowed to spend time on this project. At that time, only a few applications had metric endpoints, meaning we had limited targets to monitor.

To overcome this, we began integrating middleware components by building custom exporters from access logs. These exporters converted access logs into HTTP metrics. Middleware components, such as proxies and gateways, are utilized by a wide range of applications, allowing us to gather data without needing developers to create metric endpoints.

### Tool Selection

Once we had the data, we needed a monitoring tool. Some teams at AXA were already using Prometheus, which seemed like a promising solution. It made sense for us to use Grafana for visualization alongside Prometheus. We started developing standard dashboards for the HTTP metrics obtained from middleware, allowing users to log into Grafana and access monitoring right out of the box.

### Minimum Viable Product

Our initial monitoring stack was low-cost yet powerful, easy to use, and scalable. We aimed to make monitoring simple for our users, who had limited time to invest in setup. As they began to see the value in our initial stack, they became interested in building their own metric endpoints without needing extensive knowledge of Prometheus.

To facilitate this, we developed the Prometheus Management Agent, which runs alongside Prometheus and automates configuration, handling all root and target files without requiring user intervention.

### Standardization and Metadata Management

We also focused on standardization to simplify data discovery. For instance, we enabled auto-labeling in our rules and target files, allowing users to easily identify the stage their application is in by looking at a stage label with consistent values.

A crucial component of our monitoring stack is the Conflict Management Backend, which enriches alert labeling with high-quality metadata and provides configuration data to the Prometheus agent.

### Alert Management

Initially, we found that Grafana's alerting rules did not meet our needs, so we built our own alert management system with simple rule management. This also included a self-service web UI for users to manage alert rules, allowing developers to set up monitoring with minimal effort.

## Technical Architecture

Our architecture integrates all these components, with the self-service UI allowing developers to create and manage alert rules and set up targets easily. The Prometheus Management Agent continuously checks for changes, ensuring that configurations remain up-to-date.

### Incident Management Automation

At AXA, it is crucial to inform the Incident Manager when a business-critical application experiences issues. We automated this process by integrating with ServiceNow, allowing users to configure incident alerts directly from the self-service UI.

## Measuring Success

We measure the success of our monitoring stack by the number of targets being monitored. Initially, we had very few applications with metric endpoints, but as users engaged with our stack and created more endpoints, the number of components started to grow significantly. 

Since implementing Grafana Cloud, we have continued to add new components at a rate of about 1.8 targets per workday. 

## Transition to Grafana Cloud

As our monitoring stack gained traction, management recognized its value, leading to an increased budget for our initiatives. Metrics became an expected part of the development process, and we were ready to move to Grafana Cloud.

The decision to migrate to Grafana Cloud was driven by the need for advanced features that our small team could not develop, such as Incident Response Management. We also transitioned to Tempo from Jaeger for tracing and introduced Loki for log management.

The migration took two to three months, and we are currently in the process of optimizing our infrastructure and adopting Grafana Cloud features like Fleet Management.

## Future Improvements

Moving forward, we aim to enhance our tracing capabilities and improve the quality of our monitoring by working closely with development teams. We are evaluating individual applications and providing suggestions for improving their monitoring setups.

In conclusion, what began as an unplanned journey toward building a monitoring stack turned into a successful implementation of Grafana Cloud. We are now excited about the future and the possibilities that lie ahead with enhanced observability at AXA Germany. Thank you for your attention!

## Raw YouTube Transcript

Hi everybody, my name is
Sebastian. This is Julia. We are from AXA Germany and we
are telling you today how we finally ended up in Grafana
Cloud, although we never
had the intention to do so. It's the beginning at least. So to
give you a little bit of context, we are from a small team of
around five people working on operations topics, a small product
team. I'm the product owner. Julia is one of the engineers. The overall team size is
a little bigger than five, but five people is the smallest. The group of people that was
relevant for what we were doing in AXA. To give you some
ideas, we are from AXA Germany, so AXA overall is quite large. The Germany entity is not that big. We have only 400 developers compared
to what we have heard today. We are relatively small.
We had other challenges, you will see it in a minute.
So what were these challenges and how did we came to the idea of
building a monitoring solution, which was at the very beginning,
not at all, the goal that we had, so to go a little bit, backs a team was building a lock
management stack at the very beginning and this was around 2021
where we finished this one and then we were thinking about,
okay, what should we do now? And we, in AXA, we are doing DevOps, like most of the companies are doing
these days and people are facing a lot of challenges in running the applications.
We are going to cloud stacks. And we were thinking of, okay, what can we do to help the
development teams to run their stuff? And we came across this
quote from Gene Kim, this is from the "Three Ways of
DevOps" that somehow inspired us to do something about metrics because we
believe at the end monitoring is somehow the feedback loop for IT
operations to give some feedback to development teams, how the
applications are doing of course, and to improve. So this is the
initial idea from 2021 where we decided "okay, we need to do something about monitoring."
Of course we had already tooling in place, but this was quite old and
mixed technologies like many companies have. And so we said, okay, let's do something about it. These
are the figures where we are today. So like 5.5 million time
series, not too many. We have like 500 users
on Grafana Cloud and we have very many small tiny applications actually at the end. So what were the core challenges
and why is this a little bit special? What we did and how
we ended up in Grafana Cloud. We had special challenges, so when we decided we wanted to go
for building a monitoring stake, I was talking to the management team
and everybody said, "Yeah, great, do it...but" okay, but it was, oh you don't have a budget so you
can do something. But the overall budget will be the same that we
are investing for observability. And so, okay, so what do we do? If
you cannot invest something, okay, we're not going to Grafana Cloud
in the first place. That's clear. The other challenge was, okay, it's
also great if you do the monitoring, but can you do this please without
asking the developers to do something. Okay, so even more difficult. So we needed to think smart about
what can we do to start with observability and metrics. So in the beginning this was
mainly about metrics without asking developers to build
metric endpoints and without
investing too much in infrastructure. And
this is how we started. Okay, now quite something
about our background. We had no money. So to talk about
buying licenses was really short. As Sebastian mentioned
we started deciding we will build the entire solution
on open-source software, but there was another challenge. The team was not allowed to invest time. So as mentioned we couldn't ask them
to build your own metric endpoints and only a few applications at that
time had their own metric endpoints. So when we're going to do monitoring,
we had only a few targets to monitor. That's not a way where you get a lot of
users using monitoring when you have no information about the applications. And that's why we started
integrating middleware components. We did that by building custom
exporters based on excess logs, which took the excess logs
and built own HGDP metrics. So middleware components like proxies
and gateways get used by a lot of applications. And so we had
information about a lot of applications without needing to go to
the users and ask them to integrate the metric endpoints. So that's how we got the data.
And once you got your data, the next question is where do you start? There are some tools and a few
teams that AXA at that point were already using Prometheus. And at that time it seemed like
a promising solution and we just thought okay, we will go with it. And of course once you make
the decision to use Prometheus, it's like an easy one to also use
Grafana for visualization, right?. And that's where we started building
also standard dashboards for the HGTP metrics we got from the middleware. So as a user you can just, when you have an application which
is using a proxy or gateway can just log in into Grafana, open the dashboard and it will
work right out of the box. So it's very easy to do monitoring.
And this got us to our MVP. We had a very low cost but quite
powerful initial monitoring stack, which was easy to use and ready to grow with us, but like it is with initial versions, you like to improve. And for us improvement meant
making monitoring simple because it had to be simple in order
to be successful. As you remember, our developers, our users had only little time to
spare so they couldn't afford to put much effort into finding
out how to set up targets, how to edit YAML files so that Prometheus
will take the targets and file a service discovery will work. They quite liked our initial
stack and got the idea, "okay, I can actually do something with
this." This brings real value to me. I have a lot of better understanding
on what is going on in my application and they wanted to get more
information out of it. So they started building their own metric
endpoints and required a solution which didn't require any
Prometheus skills and that's why we started building the
Prometheus Management Agent. This is an agent which runs
next to Prometheus and handles all the configuration automatically. What I mean by that it handles all the
root files and the target files without the user to have knowledge about
what is going on in the background, how the YAML file looks. Another part we put effort
in is into standardization. We wanted to make finding things easy, so we want to know our data. What I mean by that is that we enabled auto-labeling on our
rules and target files. Like if you want to
know in which stage your application is running your target,
you can just look at a stage label, it'll have one of three possible values
and those values are always written in capital letters. Everywhere
you look, this is the standard. And so it goes with other labels
so you don't have to guess on which kind of data you will find. And this also makes integration
into other components more simpler because you know what
kind of data you're looking at and you need to do a lot of
error handling because one value you expect to be there isn't there. A very central component
in our monitoring stack is the Conflict Management Backend. It feeds this alter labeling by adding metadata so it asks other services
and ensures a high quality metadata. And it also provides
configuration data to the Prometheus agent and
metadata to our own alert management. The alert
management we did build, because of course Grafana
has its own alert rules, but at the time we started
building our stack, it didn't quite fit our requirements
and we thought this is not the easiest solution we could give our users. So we built our own alert management
with simple rule management. Now you've got an idea what challenges
we had and what solutions we built for that, but I also want to show you how
the components work together and that's why I want to show you
our technical architecture of our simple user-friendly
monitoring stack. Okay, I ended up with a last
slide talking about how our alert that we built an
own alerting solution, our own alert management solution. And part of this solution
is the self-service web UI. So a user, in this case it's a developer
can just log in into the UI and manage rules like update,
create, delete them, and set up targets. So when I am a developer and have just set up my own metric endpoint, I of course know my target URL
can enter the URL to the website and by one click just set up monitoring. All the labeling in the background
is handled automatically. So the user just needs to know
what query do I need for the alert rule and do this entering of the URL and one-click activate and monitoring
and also deactivate monitoring. So it's very easy. And with this management API refer to before as conflict management backend. This is the central component
which stores the alert within targets but also enables
the auto-labeling. So the standardization for the
service, self-service web UI. So that's where the UI
gets the label values from the management API ask other services like ServiceNow, Kubernetes, Puppet for more information to feed the metadata enrichment
and also stores targets, as I mentioned it before.
But the Prometheus API, this is our Prometheus management agent, which runs next to Prometheus. It goes once a minute and asks
the management API if anything has changed. So if so it'll update its
internal configuration automatically. And with the labeling, all the rules and the targets get to
derive Prometheus instances because of course we have a lot of instances
in different stages and different platforms. So we don't need to care
about how this is handled. When we're talking about alerting rules.
So we have an alerting rule, we get the alert and of course
it goes to the alert manager. And then we build another component, it's the ServiceNow
webhook because at AXA, if you have a business critical
application and this application runs into problems, we take it seriously. You have to inform the Incident Manager
and you have to inform them by going to another website, doing some manual
effort to declare the incident. And we automated this process. So now as a user with a
business critical application, you have your alert query, just configure the alert
rule in ServiceNow, in self-service web UI, and there's an option to
just activate the ServiceNow incident. So when the alert
gets to the Prometheus API, it already has all the necessary
information attached in the labeling to create this incident. So the user has to do very
little to actually set up monitoring, get the ServiceNow incident and
configure the alerting rules. That's what I call a user
friendly monitoring stack. But what did we achieve with that and how successful is our stack? And
once we're talking about success, how do we measure it? For us, a good measurement is the number of
targets because when you think back at the beginning on the initial stack with
only a few applications with on metric endpoints, of course the
number of targets were really low. And by users using more and more our stack building more and more endpoints, of course the number of
components was growing. And in the graph you see, we started counting the number
of components and alert rules. And by components I mean targets
and monitoring somewhere in October 2022, so after our initial
stack was already in use. And this graph shows that we
see that there was a continuous growth in both numbers. And even today with
Grafana Cloud in place, new components are getting added
on a daily basis. So it's around 1.8 targets a workday which gets added. But how would we think what
made up our success? I think at the beginning it was
really important to get users engaged with our stack. So we
integrated those middleware components, we built standard dashboards, and we made it very easy
to just enable the user to explore monitoring. And as users built their
own metric endpoints, we made it easy for them
to set up the targets. And one really helpful
thing for us was the self-service UIs because we
enabled the user to do the little effort which needs
to be done by themselves. And as you can imagine
with a five person team, we didn't even want to
set 1.8 targets per day. Management was quite happy with
this graph, you can imagine. We could show that with
minimal investment and minimal effort, we were able to deliver
real value and this helped build further support for
further development and how
this went...Sebastian will take. Okay, so this was a little bit of a
deep dive into how we came to the point of having something valuable in
monitoring always open source with minimal effort. And due to the overall
success of what we did, things got changed. You remember from
the beginning there was no budget, suddenly there was budget.
Suddenly people were seeing, especially the management
team, were seeing okay, this is not just some experiment and
then some guys are doing Prometheus and Grafana and they are being happy, but I don't see an overall
impact on the organization. No things are going to change because
of the success of the open source stack that we had. So money was there suddenly. And also the priorities for the
development teams got changed. So at the beginning it was like you
need to beg for somebody getting the time to implement the metric endpoint.
And this was not the developer who didn't want to do it, it was more like business was having
other priorities and the IT management was not strong enough or let's say it didn't see the immediate benefit so that
they would over prioritize the business projects. And now it's different. Now it's an expectation to have a
metric endpoint. It's quite natural. Nobody's asking anymore whether
we can spend effort on this one. That's how it should be, right? And after that point where now
everybody is convinced that metrics is what you should have and
you should invest in, now we got the option
to go to Grafana Cloud. So that's why many are here.
Everybody is the customer I guess, or will be a customer maybe one day. And so as we now have some, let's say a bigger attention on the
observability topic in the company. So we thought about what to do next and we already optimized a lot of stuff and
a lot of things that might not be valuable for you but have been important
for us to get where we are today. But some stuff we will never do. And this is especially what is about
all the enterprise features in Grafana Cloud. And we got very interested, especially in Incident Response
Management and what Cedric just showed, the nodes graph and all these topics, we will never do it with a five
person team so there's no chance. So this was the main driver why we
decided then to go to Grafana Cloud while we are building
the monitoring stack. We also migrated to Tempo
from Jaeger tracing and we introduced Loki and even did some
multi-tenancy features on the open source deck and a lot of stuff in addition. So we were anyhow already
on Grafana tooling. So the natural improvement was
moving to the Grafana Cloud and of course doing so will
reduce your complexity if you're running this all by yourself. There is a huge amount of infrastructure
running there. And this is also quite good for our team because
nobody wants to maintain a huge amount of infrastructure. Everybody
wants to do the new cool stuff. So this was great and we decided
to move to Grafana Cloud. It took us two to three
months to move everything over and we are still in a phase
where we are going to improve. So we finished our migration
somewhere in March this year I think. And now we are going to
replace quite some amount of infrastructure that
we have still onsite, especially the old automation
stuff that Julia showed you before. Of course there's some stuff you don't
need anymore if you have Grafana Cloud, I mean now there's Fleet Management. It's a relatively new feature and we
are going to replace a lot of the custom management tooling that we
have with Fleet Management. Also the alert management UI
that we have will go away. We are already using Grafana Managed
Alerts as a backend service today. So there's still this super easy
UI because the Grafana Alert UI is not easy and it's not always
like we would like to have it, but if we want to utilize
features like IRM and so on, there's no way around
getting rid of our own UI. And so once we have done this, I think most of our custom
infrastructure's gone, a little bit will be remaining. And apart from the
infrastructure optimization part, we are going to work more on tracing. Tracing is the signal that
has the weakest quality. It might be for many of you. So we have pretty good data
quality and metrics and logs. Julia explained about the order labeling. We are really taking care of correct
service name spaces and service names and consistency across signals for tracing. We still need to fix this.
So this will be done soon. And this is important for getting the
knowledge graph and everything working quite well. Apart from that, we are optimizing the
usage of open telemetry, especially when it comes
to common conventions. We have our own labeling rules today. So we are right now in the phase
where we are migrating or adopting labeling rules that are more like standard rules like in Mimir and Prometheus, you should label service name
spaces and service names. We are also going to
adopt open telemetry logs. Very likely we have an internal
Kafka backend with a custom JSON log format and we will replace this with
open telemetry logs also in order to utilize more of the standard
features of Grafana Cloud. And in addition to the
more technical topics, we are working with the development
teams nowadays to help them to improve the quality of their monitoring. We are doing this by assessing
each individual application, checking how the dashboards look
like, what about the large rules, where can they improve? And we are writing little reports and
suggestions on how to improve their individual monitoring solution. And now then I think we're done with
everything with what we wanted to share today. This is how we ended up in Grafana
Cloud. Like I said at the beginning, this was not the intention
at the beginning, we just wanted to get a cheap stack
and now we are quite happy in the Grafana Cloud.

