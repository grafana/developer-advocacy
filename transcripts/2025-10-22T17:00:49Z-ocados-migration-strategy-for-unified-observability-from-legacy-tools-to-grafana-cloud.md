# Ocado’s Migration Strategy for Unified Observability — From Legacy Tools to Grafana Cloud

Published on 2025-10-22T17:00:49Z

## Description

Watch how Ocado replaced legacy tools with Grafana Cloud to cut complexity and costs. Mirek Wierzba reveals how smarter ...

URL: https://www.youtube.com/watch?v=cUXVqOJ_OSQ

## Summary

In this presentation, Mirek Wierzba, the Engineering Director at Ocado Technology, discusses the company's journey to consolidate its observability tools around Grafana Cloud. Ocado, a global technology company specializing in robotics and automation for grocery delivery, faced significant challenges due to a fragmented observability landscape, relying on numerous vendors and tools which complicated operations and increased costs. To address these issues, the company set goals for improved cost efficiency and reduced incident response times while aiming to unify observability under one platform. After thorough market research, Grafana Cloud was chosen for its capabilities. Mirek explains the migration process for metrics and logs from New Relic to Grafana, highlighting the importance of a centralized approach and the challenges faced during the transition, including increased support requests and dual running costs. He concludes by emphasizing the ongoing journey to optimize observability and the need for continued collaboration with Grafana to leverage the platform's full potential.

## Chapters

00:00:00 Introductions and overview of Ocado Technology  
00:03:30 Explanation of the Ocado Smart Platform (OSP)  
00:06:00 Challenges faced with fragmented observability landscape  
00:09:45 Goals and principles for improving observability  
00:12:15 Market research and selection of Grafana Cloud  
00:15:30 Overview of the migration strategy  
00:18:00 Discussion on the Ocado Technology Platform (OTP)  
00:21:30 Introduction to FinOps and its importance  
00:25:00 Metrics migration from New Relic to Grafana  
00:30:00 Logs migration architecture and process  
00:35:00 Review of challenges faced during migration and support strategies  
00:40:00 Future directions and ongoing migrations with Grafana services  
00:44:00 Conclusion and invitation for questions  

# Consolidating Observability at Ocado Technology

Welcome everyone. I'm Mirek Wierzba, the Engineering Director at Ocado Technology. Today, I want to share a story about how we consolidated our core observability around Grafana Cloud. I’ll discuss the challenges we faced, the strategy we built for observability, and our journey of moving from several different vendors and services into one consolidated platform.

## Context on Ocado Technology

Ocado has evolved from a UK startup to a global technology company that powers some of the most forward-thinking grocers around the world. We provide an end-to-end platform built on pioneering robotics, automation, and AI. 

### What We Built

We developed the Ocado Smart Platform (OSP), which addresses everything from e-commerce, where users shop for food online, to supply chain logistics, where products are delivered to warehouses. 

In our highly automated warehouses, hundreds of robots and robotic arms pick and complete orders to prepare them for delivery. Finally, we ensure that products reach customers' homes.

While many in the UK may be familiar with Ocado, those outside the UK might use our technology without realizing it, as we have 12 partners across the globe, from North America to Europe, Asia, and Australia.

## Challenges in Observability

To keep our platform running reliably, we rely heavily on observability. However, the complexity of the OSP, combined with the rapid growth of our company—many of our partners went live in the last few years—resulted in a fragmented observability landscape. 

At one point, we were using 13 different observability tools from seven different vendors, three in-house solutions, and over a hundred applications. We were sending 15 terabytes of logs and 18 terabytes of metrics daily to New Relic.

### Issues Faced

Several challenges arose from this fragmentation:

- **Architectural Complexity**: Maintaining our observability ecosystem required significant time and effort.
- **Operational Fragility**: We experienced incidents and issues that stemmed from this complexity.
- **Unsustainable Costs**: Managing seven different vendors made cost optimization difficult, leading to increased bills.
- **Developer Friction**: Engineers had to switch between different tools and UIs, impacting their ability to troubleshoot and respond to issues quickly.

## Our Strategy for Improvement

To address these challenges, we established user- and business-focused outcomes, along with technical guidelines to guide our approach. Our goals included:

- **Improving Cost Efficiency**
- **Reducing Mean Time to Recovery (MTTR) and the impact of incidents**
- **Reducing Cognitive Load for Users**
- **Empowering Users to Leverage Observability**

To achieve this, we aimed to simplify our architecture, unify observability on a single platform, and standardize on open-source solutions for better control and flexibility.

## Choosing Grafana Cloud

We conducted market research to find a provider that could meet our needs, running tests, trials, and proofs of concept. Ultimately, we concluded that Grafana Cloud was the right choice. 

However, migrating from multiple vendors would depend on our engineering culture, company culture, and tech stack. Three key factors helped simplify our migration:

1. **Ocado Technology Platform (OTP)**
2. **FinOps**
3. **OT Data**

### Ocado Technology Platform (OTP)

Our internal developer platform includes components for running applications, data intelligence, observability, and developer tools. The goal is to allow engineering teams to focus on solving business needs instead of technical problems.

This platform helped automate and centralize migration steps at scale, as we host around 1,200 applications and over 1,500 primarily engineering users. We conduct hundreds of deployments daily and process approximately 4.5 billion business events each day.

### FinOps

FinOps is structured around three pillars: **Form, Operate, and Optimize**. We gather costs from third-party services and allocate them to applications, teams, or individuals, providing real-time visibility. We also have a recommendation module to identify cost efficiency improvements, allowing leadership to make informed decisions about tool usage and spending.

### OT Data

OT Data, or Technology Data, is a centralized data warehouse that gathers data from various enterprise applications across Ocado. It provides well-governed, high-quality data for users to build dashboards and conduct analyses, further enabling data-driven decision-making.

## Migration Process

We approached the migration in two main segments: **Metrics Migration** and **Logs Migration**.

### Metrics Migration

For metrics, we transitioned from New Relic to Grafana, focusing on enabling our platform for users through central configuration repositories and Terraform providers. We incentivized user adoption by sharing the benefits and providing comprehensive migration documentation. Regular meetings with stakeholders helped monitor progress and address issues.

### Logs Migration

The logs migration was more complex, utilizing a log shipper we hosted ourselves to push logs to OpenSearch clusters on AWS. We implemented a new log shipping method using Fluent Bit sidecar, which directed logs from applications to Grafana Loki.

We scheduled our migration for each environment, allowing rapid adoption during application redeployments. Within a couple of weeks, nearly all applications had migrated to the new logging solution.

## Results and Reflections

In summary, our migrations were categorized as either platform-driven or user-driven. While platform-driven migrations were more automated and required minimal effort from users, user-driven migrations required manual code changes and incurred dual running costs.

### Achievements

- Simplified architecture, resulting in reduced maintenance for platform teams.
- Significant cost savings for some services.
- Accelerated troubleshooting with all signals consolidated in one place.
- Reduced cognitive load for users by eliminating the need to switch between different UIs and tools.

## Challenges Faced

Despite our successes, we encountered challenges during the migration, including a 300% increase in support requests. To address this, we implemented the OTP Assistant, which provides guidance and support to users.

### Lessons Learned

- Comprehensive documentation is crucial for covering both common and complex use cases.
- Dual running costs can be significant, requiring planning and budgeting.
- Ongoing training and support are essential for successful adoption.

## Next Steps

While we have completed the migrations for metrics and logs, we still have ongoing work transitioning from PagerDuty to Grafana IRM. We are also evaluating further architectural simplifications and verifying our business assumptions regarding costs and performance metrics.

We aim to leverage our consolidated observability platform further and work closely with Grafana to enhance our capabilities.

Thank you for your attention! If you have any questions, feel free to approach me at the venue or reach out to me on LinkedIn. Safe travels!

## Raw YouTube Transcript

Welcome everyone. I'm Mirek Wierzba. I'm engineer director at
the Ocado Technology and
I'm here to tell you a story of how we consolidated our core
observability around Grafana Cloud. I'll talk about some
challenges that we've been facing, the strategy that we built for
observability and the journey of moving from several different vendors
and services into one consolidated platform. To start, a
bit of context on us. So Ocado technology Ocado has evolved from
a UK startup to a global technology company that
powers towards most forward thinking grocers around the world, powers them with end-to-end
platform built on pioneering robotics, automation and
ai. But what does it mean? So we built an Ocado smart platform, an OSP that addresses everything from the e-commerce where users are shopping
for their food online to the supply chain where all the products
are getting delivered to the warehouse. Fulfillment that in our
highly automated warehouses, hundreds of robots and robotic arms
are picking and completing the orders and prepare them to be ready to be
delivered and to the last mile where it actually gets delivered
to the users homes. Those of you who are from UK, you might be familiar with what Ocado is, but if you're outside of the UK, you might still use our technology
but not be aware of that as we have 12 partners across the globe outside of
the UK from the North America to Europe, Asia, and Australia. So
running this platform, keep it up and running,
making sure it's reliable. We need to rely heavily on observability. But the complexity of the OSP as well
as the rapid growth of our company, you can see that many of our
partners went live in last few years. It all resulted into a pretty
fragmented observability landscape. Those data are from a couple of years ago. So we've been using 13
different observability
tools and services from seven different vendors. We had three in-house build
solutions and over a hundred applications. We're sending 15 terabytes
of logs every day, 18 terabytes of metrics volume
in this particular case to the New Relic. So one of the other reason why we had
such a fragmented landscape was that few years back there wasn't really that
many providers that were offering a comprehensive end-to-end
observability platform. So we've been facing some
challenges because of all that. So there was an architectural complexity. We had to put a lot of effort
and time and energy to keep the whole architecture and whole
observability ecosystem up and running. It was sometimes resulting
in operational fragility. We've been suffering from some
of the issues and incidents, unsustainable costs. As you can imagine, managing seven different vendors was
difficult. Different pricing models, paying for licenses to
all of those providers, optimizing for cost efficiency
was basically difficult and the bill was increasing.
We've been using, in some cases closed source
products like JVM agents to send data to New Relic and so on, which limited our ability to
control the data and developer friction.
One of the most important aspects. So our users engineers across Ocado
had to switch between different tools, different UIs that impacted the ability
to troubleshoot and quickly respond to issues. So we thought
about how to solve that, but we didn't want to address
just one of the problems. We thought about how we
can address all of them. So we came up with a set of
user and business focused outcomes, some sort of
goals as well as principles, a technical guidelines
that would guide us there. The goals were to improve
cost efficiency, reduce MTTR, number of incidents and incidents impact,
reduce the cognitive load for users as well as empower our users to
leverage the observability more. And to achieve that, we wanted to simplify our architecture
and make it more reliable. We wanted to unify observability in
one single platform and we wanted to standardize on open source to get a
little bit more control and flexibility in the future. So actually let's go back then. We've done market research to
find a provider that could satisfy all those needs. We've run a bunch of tests,
trials, proof of concept and so on, and we concluded the Grafana Cloud
could be a provider that can satisfy all needs. So all that left is actually migrate
from all the vendors to the other one. But the migration will differ, depend on the company because it will
depend on the culture of the engineering culture, company culture,
tech stack, et cetera. But I think there are three things
that in our case helped us with the migrations, made it simpler, not simple, that I would like to spend a
couple of minutes sharing with you. Those things are the technology platform
finops and something that we call OT data, starting with Ocado
technology platform. This is our internal developer platform. It consists of few components, service platform for running an
operating application. This is built on top of the AWS data intelligence
platform where we provide a tooling and services and best
practices for managing business data, data ingestion, processing, consumption
sharing, as well as machine learning. Of course the observability component so
that users can easily instrument their application and use the
observability tech stack, a set of developer toolkit and all
that and ensure the guarantees, the governance and security. Essentially the goal is to make
sure that our engineering teams can spend as much time as possible on
solving business needs and delivering business value to our customers rather
than solving technical problems over and over again. And why that's important. In terms of the migration, it helped us automate and centralize
some of the steps into migration, the scale that we're operating. So we are hosting around
1,200 applications, over 1500 users that
are primarily engineers. We are doing hundreds of
deployments every day. We have millions of jobs processing
data and we are processing four and a half billion
business events every day. The second aspect is finops. So
finops has three pillars in form, operate and optimize. So we gather the cost from all third
party services that we are using. We gather costs about all
the application operation, we ingest it into one place and we
allocate those costs to a single application and or team or individual. And we try to do it as real time as
possible as the vendors allows us to. Then you have a mechanism to alert when
we spot some anomalies so we can let the engineering team that, hey,
last day or last couple days, your cost increased more than you
would expect. So just take a look. We also have recommendation
module that spots some cost efficiency improvements opportunities
so that we can alert and inform for instance that you have overprovision some
of the resources or you have some data that no one is using. So maybe you should remove that or put
some retention tag on it, et cetera. And why it's important is
important because providing
the visibility on the cost allow engineering teams and engineering
leadership to make decisions about what tools they're going
to use and whether their spend is on the okay level. And the third aspect is OT data. They say that there are two big problems
in computer science and naming things in one of them. So that's why you haven't
come up with a better than OT data. It stands for technology data. So it's basically a centralized
data warehouse where we gather data from different enterprise
application that we are using across Ocado and we provide a well-governed and high
quality data to the rest of the people in the organization. At the moment we are like 20
different services that we seeing data from. Those are things like Jira,
Workday, ServiceNow, GitLab, et cetera, right? And we try to make it easy
for users to use that data, build some dashboards, run
some ad hoc analysis and so on, and teach them how to do
that. How to define metrics, how to measure metrics as one of the
mission of my department is enable data-driven decision
across the organization. And why that is important is again, because providing the transparency and
access to the data allows leadership and teams make decisions and progress, monitor the progress of
different activities such as
migrations and also monitor impact of those actions. So let's move on to the migrations. I will talk you through two
types of migration that we had, metrics migration and logs
migration for metrics migration. We've been moving from
New Relic to Grafana, primarily from New Relic
Metrics and New Relic APM. So first thing that we had to do was
to enable our platform and allow our users to use Grafana Cloud
services via two ways, either a central configuration
repository or through the Terraform providers.
Then we wanted to try to incentivize our users to actually adopt those and migrate, sharing a value of it, provide clear information about
the cost benefits and so on. We also provided a
comprehensive documentation, how to migrate, guide, and some assistance to do the actual
migration as this migration had to be manual due to New Relic agent that
had to be removed from the code waste. And also we had a regular meetings with
our stakeholders and users where we were monitoring the progress of the
migration, spotting issues, discussing what's important
to be focusing on. Now we were learning that we need to
enable a little bit more Grafana services such as Faro and K6, et cetera, to enable users to actually
fully migrate off of New Relic. This is the architecture, which is not really any specialist
permit to use scraping data from the applications exposed endpoints
and push that data to Grafana Cloud. The second migration is about logs
and our login architecture solution looks a little bit more complicated. So it's based on the log star log
shipper that we host ourselves. And we are pushing logs to
open search clusters on AWS, which is managed or semi managed. It still requires a lot of
effort to properly configure
it, scale it, et cetera. So there was a lot of effort
into hosting those clusters. We have around 70 different environments, so this had to be set up 70 times
for each of those environments. So it was a pain in provisioning
all that and then supported. So what we've done, we again implemented centrally
a new way of log shipping. We base that on fluent bid sidecar. So now the logs were directly shipped
from the application to the Grafana Loki. Then we created a schedule plan. So for each environment that I
mentioned, we had a date and a time, at which point all the
application after the next redeployment we'll start using
the new log shipping solution. And because we are
fairly mature with CICD, we do redeploy our application
pretty often due to new feature upgrades of libraries,
security fixes and patches and so on. So it gave us an
opportunity to actually have a very rapid adoption. In
some cases within 24 hours, 50% of the application were redeployed
and picked up the new way of sending the logs to the Grafana Loki. So we were able to do that
migration fully centrally. However, still users had to know what Loki is and
was the user interface with the query language, et cetera. So we run some workshops and estimating
sessions with Grafana regularly so that user can learn that tool. So we moved from that architecture
to something like that. So fireline sidecar using unique
socket to connect to application at the cluster task lever in ECS in
AWS and sending those logs to Grafana Loki. And this is an example of the
adoption at one of our environments. And you can see we enabled a new way of log shipping 31st of August
and within a day or two, the adoption increased by over 50% and
there is some long tail of adoption for rest of the application, but
still within a week or two, like almost 100% of apps were migrated. We could have forced redeployment, but we didn't want this one
or two weeks were acceptable. So there were two different
types of migration. One kind of platform driven
and the other one user driven. The platform driven one
could be executed centrally, almost fully automated. It required
minimal effort from our users. There was no dual running or
very low dual running costs. We were able to have aggressive
timeline as I mentioned, we could actually make it even quicker. We could force through
deployed application, we can do each environment every day. We give ourselves time first of course
we migrate in environments that are tests and dev, et cetera, et cetera. And we followed with production one
after a couple of weeks after we get confidence that everything
works as it should. However, we weren't taking that much
into account everyone's needs. So at that point your application will
start sending logs somewhere else. We gave an opportunity to
put your application on
exclude list if you had really a reason why you shouldn't be using Loki.
And one of the main reason was the size of your logs as Loki has pretty
well low for some of the application, low limit on the size of the single
log line that you can send to Loki. And we had couple application that
didn't want to go Loki because of that reason. We could
automatically detect that, but we wanted this to
be opt out on request so the users really have reason to do that. Otherwise we would truncate the log and
just sent not the entire message to the log just to speed up the migration. The other type of migration was more
user-driven because it was difficult to automate it. It required
code changes, it was manual. There was a significant dual running cost. So we observed that some of the users, some of the teams set
up the Grafana setup, started sending data to Grafana, but then still keep New Relic for some
time just to make sure that everything, everything is the same, et cetera. And that could last
four weeks or even a couple months. So there is that risk of dual
running cost and they gave a generous deadline so that the teams
could migrate whenever they feel ready for it, take into account other priorities
in their backlogs, et cetera. So was it worth it? We did simplify our architecture
and we made it more reliable. Absolutely. We have now much less maintenance
on our platform teams. We did achieve significant
cost savings at least for some of the services. And we're definitely interested in all
of the Adaptive metrics, traces, logs, et cetera to get even more to be more cost efficient. But what's important we get
are ways to manage the cost and optimize it. What Grafana does, it provides you that opportunities, which very important for us because we
can then make a decision whether we want to invest more and spend
more on observability or we
want to decide to optimize a little bit more.
Its cost. We accelerated troubleshooting. So having all signals in one place is
much easier and convenient for users. And we reduced this cognitive
load that I was mentioning before. Right now everything is one place. Users don't have to switch
between different UIs,
different tools, search copy, paste some request ID and move it to
the different tool to look for it. We eliminated closed source. So we
feature proof with Open Telemetry, micrometer and Grafana. So the logging migration
that I was explaining, now we can do that also for
metrics and other signals as well, right? If we have to. So it gives us more flexibility
and opportunities and we empowered our engineers to be more proactive rather
than reactive firefighting. When I'm talking to engineers, they are saying that what they notice
is that Grafana is actually kind of a framework and toolkit where
you can really do much more having all the signals in one place, you just need to learn the tool a
little bit more and spend some time to actually know how you
can leverage Grafana. But they see already and they're
playing with ML modules to other on some metrics in a much smarter way so that
they get alerted if something's going not as expected much, much quicker before actually
users are impacted by the issue. But it wasn't all great, it wasn't a smooth sailing. We had of course a set of
problems and challenges. As we said yesterday, there
are some technical challenges, but if you put talented
people and give them time, that will solve that technical issues. So I'm not going into
details on those ones. However, the support burden during the
migration was much bigger than expected. We knew it'll be bigger, we just didn't think it'll be 300%
increase in our support requests. So that was a problem because the same
team that was enabling next Grafana services in our OTP had to provide
a support for already existing old stack as well as
people that are migrating. So what we've done is we have
something that is called OTP Assistant that has old knowledge for
documentation about the OTP and can help you. You can ask that assistant how
I do this and that in OTP or was it the most efficient way of
doing this? And it gives you a answer that is compliant with OTP and how
to achieve that using our tools, our libraries, et cetera. It has a
cool feature which is a support mode. So we can add that assistance to the
Slack channel because we doing support internally through the Slack
channels and that assistant can work in two modes, shadowing
modes or direct mode. So it can either suggest an
answer to the person that is on support, you can try this answer or
just answer directly to the user. And what we also do is the assistant
is sharing that answer only when it has high confidence it's the right answer. So something that Grafana shared
with the AI assistant about this confidence indicator is really, really cool feature because we
know from experience that's very, very important aspect
of any AI assistance. So there is never enough
trainings in documentation. There will always some kind of use cases
that you didn't think about and don't put in the documentation because it was
too obvious or you didn't think about it. So think about it in front and try to
provide as comprehensive and documentation as possible is also important. Be prepared for difficultly
complex use cases. Many of the use cases were fairly simple
and teams were adopting Grafana and migrating from re to Grafana very easily. But some were a little bit more complex
that we had to provide some extra support, enable some
additional services, et cetera. And we try to identify those in advance, but it's difficult. We could have spend a bit more time
on it and try to identify them upfront to have a bit more time
into supporting them. And the dual running costs as was
explaining earlier, can be expensive. So taking that into consideration
and make people aware of that and plan for that and
budget for that as well. So that's not the end of our journey. We still have one migration
ongoing that is more manual. It's PagerDuty to Grafana IRM. We are around one third done,
two third still ahead of us, but we migrated metrics and logs, we adopted traces and Faro and K6 and
deeplinks and mail module and bunch of other Grafana services we need to implement
solution for some edge cases. And one example is those long log lines, how to support it in OTP in an efficient
way so we don't have to keep those open search clusters running for those cases. We plan to do some further
architectural simplification, especially around the metrics and we are
evaluating the sidecar approach that we have for logs also for
metrics. And in that case, well it solves some authentication
problems that we have between pro materials and
the endpoints, but as well it will remove the need for
maintaining some additional architecture. We still need to do the final verification
of some of our business assumptions so we know already what happens with
the costs and whether the assumptions regarding the costs were
correct or not. However, MTTR number of incidents
and incident impacts, it's still a bit too early but also
it is really difficult to isolate what impacts those metrics, right? We are doing a lot of stuff to make
sure that OSPA is reliable and up and running. So identifying and isolating
how Grafana helps with that versus other activities that we are doing. It's a little bit difficult but we
need to figure out how to do that. And as I mentioned, we try to
be as data-driven as possible, so really want to look at those numbers
and make sure that we see the positive impact. But as I was saying, it's not the end of our journey. It's actually the first step
because right now when we have all signals in one place, we can look at how we can further leverage
the one consolidated observability platform. So we are now working together with
Grafana to see what we can do to leverage it even more
and get more value out of it. And I believe that's it
what I prepared for today. So thank you very much for attention. Have a great the rest of the day
and if you have any questions, please try to find me at the venue
and approach me and talk to me. I'll be more than happy to have a
conversation, chat, answer any questions. You can reach me on
LinkedIn as well. And yeah, safe travel to your homes.
Thank you very much.

