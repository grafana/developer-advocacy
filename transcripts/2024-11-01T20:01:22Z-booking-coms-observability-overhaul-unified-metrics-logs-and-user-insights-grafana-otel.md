# Booking.com&#39;s Observability Overhaul: Unified Metrics, Logs, and User Insights | Grafana &amp; OTel

Murugesan and Ahmadali from Booking.com's Observability Team as they dive into the journey of modernizing observability.

Published on 2024-11-01T20:01:22Z

URL: https://www.youtube.com/watch?v=vy-EEzYcYtM

Transcript: Good afternoon, everybody. Hi. Before we get started, I think
I have one small request. I have my colleague, Ali, it's a first
time for him. He's a bit stressed, so can we have a big round
of applause for him please? Thank you very much. All right.
Why we are here today? Maybe before I talk about why we are here today, I think I want to show our cool
logo that we designed for our observability team in Booking. I think if we look closely,
it talks about the blue eye, that's basically us. So we are the observability
platform team in Booking. How many of you use Booking.com today? Oh, wow. Thank you. So, my name is Murugesan. If you want to practice a tongue
twister, you can say that. Otherwise people call me Muru, which
is a first four letters of my name. I work as a solution architect
within Booking. Most of you already know what Booking is. We are
one of the leading travel company. Booking.com wants to make it easier
for everyone to experience the world, you know, diversity, right? . And I'm Ahmadali. I am an SRE in
Booking.com's observability team. Cool. So why are we here today. , we wanted to basically talk
about our observability journey, how we are redefining observability from
what we had yesterday to where we are today, and then what is the
future ahead of us. Along the way, we have gained a lot of insights.
There are lessons that we learned. We thought this is good to share for your future use cases, for if you
are on a similar journey like us, it could be useful. And then
we will take some questions. We'll try to answer as much as possible.
If I do not know, I do not know, but I will make sure, you know, how to
reach out to me and also my colleagues. Then we can basically help you answer as usual. So please send us questions. We are happy to answer all your questions. So let's see, what we were,
where we were and what we had. And, this has been our
observability stack in the past. We had multiple different
observability solutions coming from different business units. And basically we had multiple telemetry and storage UI and alerting
solutions. And this, although it was working,
has its own problems. The main problem was that the majority
of our observability stack has been homegrown. And with our new developments, we needed to invest more
time and effort to also maintain and develop
new solutions for that. And for the external part of our
observability stack, we were locked in, remember the cables in the older tech? We actually had a set of our own cables
in addition to the other cables that people were using. Which was not sustainable at all in
terms of toil, in terms of cost, and we had a fragmented
observability stack at the end. Absolutely, so how many of you can relate to what
he was showing before? To say, hey these guys are sharing
some of the stories, like what we have today, right? So
if you look at our presentations, we have a lot of enormous
amount of telemetry agents because we run our service on
prem, but also on the cloud, right? We also run lots of observability package systems
for metrics, logs, traces. So this is when we thought
as an observability group we decided to step back and go back
and work on the vision and strategy. So as part of our new vision and strategy, we wanted to put together centralized
telemetry pipeline that should be interoperability out of the
box, should be able to embrace agnostic ways to observe, but also be able to ingest the
telemetry of the backends and supports the centralized telemetry pipeline. And instead of having multi
centralized metrics system or logging system or tracing system, is there a way to unify metrics into
one single system that can scale across Booking needs, but also
similar to metrics. Can we bring some solution for
the rest of the two pillars? That's logs and tracers as well. So on one side we wanted to
unify metrics, logs, and, traces into a specific system
that can scale for the today, but also the future needs. And we
are also, as part of the vision, we look into some of the areas
where we did not invest so far. One of them is profiling and
also the real user monitoring. These are two important
pieces as well. One, Profiling can help us to solve and
shift left approach in the software development lifecycle, which
we never used to do it. So we wanted to enable our
engineering teams to bring the profiling solutions,
instrument your applications, and collect the data so you can
look at your application performance in the pre-production during the
software developer lifecycle. So you're grouped with all the data that
you need so that you can make informed decisions. We are an
internet company, right? So it's important to understand customer
experience, customer sentiments. So without real user monitoring
we will not be able to do it. We do some part of real user
monitoring but we lack on many areas, which we will
talk about in a few minutes. Similar to our real user monitoring,
we had a boring non-intuitive legacy UI and alerting solutions. So how do we unify and
provide unified experience for UI as well as the alerting solutions. So this is our simplified modernized
futureproof observability, vision, and strategy. We as
a group put together. And why did we do that? Because we wanted
to basically be vendor agnostic, want to be able to centralize, modernize so that we don't observe only
on the cloud, also only on-prem. But, you know, irrespective of where we build our
applications or run our applications, we should be able to observe,
but also to scale, right? And the other thing is cost,
which we will talk about in the upcoming session, but
we are not applying it today. We don't know how much we are
spending on observability solutions? Where are we spending?
Why are we spending, is there a cost optimization strategy? Are we able to scale and make it
relatable for Booking needs today, but also the future needs, right? So let's talk about our journey
to modern observability. If you see the logo in the
right, Grafana is not new to us. This is Grafana's logo
in the first versions. And we've come a long journey from 2014 to right now that we are in the cloud. And for every version
that we were upgrading from version one, we had to go through the process to
make sure that these upgrades are not affecting our users, but we are able to provide them the
new values of each Grafana version. And for that we were basically
upgrading Grafana in our lower environment, making sure that everything
would've worked the same way that it should work, including
panels, plugins, data sources, and alerts. And in case
things didn't go as planned, we would've worked with our customers
to make sure that they are upgrading or they're changing their
resources to be compatible. And for the past two years, our focus was to make this unified
observability vision happen. And for that to happen, similar to
the deployment procedure we had, we needed to make sure that we are
cleaning up some legacy systems that we were using, which was the migration
to Unified Alerting and the Angular plugins. And another thing was
that we didn't only have one Grafana ui, but we had three, and these three instances have been
widely used across our business units. So another transition that we had to
make was to make sure that there are only one instance, and at
the end, we successfully migrated to Grafana Cloud in
which we made sure that our internal and external
integrations are working properly, which is a challenge by itself
because Grafana is no longer in your infrastructure. And for
the past few months, we've been successfully using Grafana
Cloud and our users have been happy. Absolutely so, you know, not just on the UI journey
that we modernized, we also want to be able to modernize
the rest of the observability. Right? How many off us today uses
OpenTelemetry on production? Wow, that's a lot more than I expected so what we are doing today is,
like I said, we have a platform, on applications that's running
OnPrem, but also on the cloud. So we are a multi-cloud company. Our application's running on AWS
but also on Google, and on-premise, within Kubernetes, also on EKS, we have a machine learning
platform, we have a gen AI platform. We have a data platform.
You call it what you want. So we are a technology
driven travel company. So, that's one of the reasons
if you look at it, there are a lot of telemetry agents.
We have some of them in Telegraph, we still use them, Victoria
Metrics, we use them. , Nanokube, which comes with Graphite, we still use
them. There are homegrown solutions, like even Proxy, which is
marked in green color there. It's a Vender from one of the home grown
system. So we have a home grown system, we have expensive AppDynamic systems,
we have some of the open source system. We run one of the biggest
Graphite instance in the world. I can say that we have about 800
million active series, that's really huge. We are running more than, 300 parametal missions where the
Graphite basically horizontally scaled, right? So this is when we decided we want
to basically bring our vision into reality. We started going
towards OpenTelemetry. The reason we went towards OpenTelemetry
is we believe in the strategy, but also we believe in our
company strategy. So both
are aligned. For example, we want to build a solution.
They are interoperability, able to scale for the Booking
needs, also able to collect process, enrich the telemetry, and then put them inside any of the
packings so that we are not vendor locked in. Right? Today we work
with one of the partners. Tomorrow we decided to go someone else
because of strategy, because of cost, because of security, whatever the reasons
we should not be locked in, right? So this is where we brought
in the OpenTelemetry and
we were able to already get rid of our one friend AppDynamics. So AppDynamics was one of the
expenses solutions we got rid of. We were able to onboard all the
users into OpenTelemetry and then we were also able to get rid of
the other system that is Thanos as well. So what we are trying to do is we, first
thing that we did is OpenTelemetry. We scaled OpenTelemetry
across all the platform. So we had the OpenTelemetry running
as a demo on all the VMs, Palm Metals, but on the Kubernetes, it's
running as a demo site, but we also enable our few
FinTech piece to customers to run it as a sidecars because
of some security reasons. We basically provide OpenTelemetry
as a service within Booking. So, which means we uplift lots of
dependency for our customers. What customer does is
just an instrumentation
piece. It can be preferred. The instrumentation packages per
language, they just need to instrument. We take all the telemetry
data, we scan through them, we apply rate limiting so
that we avoid the cardinality, we scan for PIIs and then we ensure
it goes to one of the backends. But how we are redefining, and that's where we are working closely
with one of our partner Grafana Labs. The reason we went to
Grafana Labs, not because, you know, they're cool,
of course they're cool, it's because they align with our strategy
and also company strategy that is they natively support OpenTelemetry, right? So we want to work with some vendors
who natively support OpenTelemetry, and we want to work with somebody
who built a product for cloud who was born on the cloud for cloud. In other
words, that's what I wanted to say. So one of them is, like
I talked about, Graphite. It's basically used as a
block storage. It's very, very difficult to scale
if you really want to, you can of course scale vertically, but we wanted to build a solution
that we can scale horizontally, right? So Grafana Mimir supports
block storage, for example. So we believe bringing Grafana Mimir,
being able to scale it on cloud, that's one of the reasons why
we went to Grafana Mimir. Today, we store about 85 million metrics on Grafana Mimir. They are natively
integrated OpenTelemetry, and we were able to get rid of
AppDynamics and also Thanos. All the metrics are now
coming into Grafana Mimir, the one that are marked in red, they are basically some Prometheus
instances running, in few places. Also the Graphite. So
that's our upcoming, , strategy to get rid of our Graphite
system in Prometheus so that we centralize all the metrics into a
single solution that's Grafana Grafana Mimir.
Now, similar to Metrics, we also want to unify all the logs
into one centralized system. Again, we are already running one of the
biggest instance on Elasticsearch, which is about 800 plus Parametal servers. We are already deprecated
few numbers of clusters, everything has moved into Grafana
Loki. It was a big decision, we still use this elastic search
in the form of open search for full text search capabilities. But specific to observability
logging use case, we thought Grafana Loki is a better
because it's built for that particular system. In other words, it's a purpose
built logging observability solutions. And similar to Grafana Mimir, it can also scale horizontally
built on cloud for cloud. So we can basically solve some of
the scalability issues that we have encountered with, ,
Elasticsearch. Like for example, if you're somebody who
uses Elasticsearch today, you know the pain of scalability.
You need to predefine the indexes. You need to ensure that if you want to
scale, you need to scale vertically. So you will basically ended up
having performance problems. So we solved that problem
with the Grafana Loki. We have seen massive adaptions there as
well. I don't wanna talk about tracing. We don't use the tracing
solutions from Grafana today, but we use this honeycomb for the
reason that we've been working with that vendor for more than five years. So it's not an easy change
as we can do it right now, but we still work with them because they
support OpenTelemetry out of the box. So it's easy for us to bring
the OpenTelemetry, which
is a new telemetry agent, but also legacy ways to
bring the telemetry into Honeycomb. So basically they can
coexist. Profiling, like I talked about, we use Grafana Pyroscope. We
introduced it very recently, we see a good adoption. Good success stories with
our customers and create benefits, create values in terms of ensuring and
building a quality software for all of Booking customers. We
were into Rum before, but we were blindfolded on some places. More than 50 percentage of
revenues come from mobile, the mobile app. So it's important for us to observe
end to end customer journey on web as well as on mobile so that we
are able to connect that frontend observability with the backend. So we can provide that
end-to-end distributor tracing. And also able to measure
the customer satisfaction, the customer sentiments using Rum
solutions. We are in the early phase. We are working with one of our Grafana
partners for mobile observability, probably for next year. We will
have some cool success stories, but it's too early to disclose
anything on Rum and Synthetic. I think he talked about
user, how, how are we, how did we do the user interface
unification and alerting, , similar to other areas, we
had a lot of conflicting UI and then also alerting solutions. Now we can confidently
say that we follow, we, we follow the pick 10
philosophy of Grafana ui. So our code to user interface
is now Grafana UI for alerting visualizations as well. And with that being said,
here we are right now. So for the past, , year and a half, we've seen great success in
onboarding our customers in our OpenTelemetry pipelines, , which are heavily relying on
Grafana products, as you can see. And right now we've been focusing on providing the automation
values to our users. Right now we are focusing on observability
as code to make sure that our alerting dashboards, panel definition, everything would be as
automated as possible. We've seen huge interest, as my
colleagues said on profiling, which is something we are focusing on, and we are evaluating different
machine learning solutions to replace our homegrown anomaly
detection services that have been around for ages. And in this transition we've had some lessons. Absolutely. I think this is where I want to
spend a bit more time to share some of our lessons, when it comes to the transformation
or transition journey in my opinion. But based on whatever
I experienced so far, technological challenges is always
looked at as a major thing. But for me, technology comes last, right? What comes first is the strategy. So like I talked about before, one of the very first
thing that we did was, we stepped back as a group, we defined a three year
strategy with a vision in 2023. It's been one and a half
years. We have achieved many things, right? We brought in centralized
metrics solution based on Grafana, centralized logging solutions on Grafana
Loki OpenTelemetry for about 3,200 services being today observed. And being able to monitor, which is
a massive, massive thing I think, I think behind the strategy that we put together and making
sure the strategy basically, is not top town, but it's going from
the bottom up approach, right? When we put together a strategy,
we align with the team, aligned with the leadership and
make sure that the company vision and the observable division, they coexist.
They talk about the same language. And that's, I think the biggest reason why we are here
today and talking about it. When it comes to any new adoptions more than technology, I think human is
the biggest obstacle in my opinion. I'll give you a real example, right? When we decided to replace OpenTelemetry
with one of the legacy system that was built decade ago, it
works still today, it does the job. Think about the people
who been using the system, who was the pillar of building
the system a decade ago. Now he needs to, or her/she
needs to work on a new system. So there was a lot of chaos, right?
So we need to be really honest, there was a lot of
questions. And the thing, what we did is, you know, we, we were honest and we were humble, but we were also transparent to say, well of course the technology
is going away, but not you. 'cause we need you, you understand better about the
Booking.com as a company and Booking.com, the technology landscape that we use, but the new technology is going to
come. You tell us what you need, you tell us what you want us to
do from a leadership perspective. So we basically enable
what the team needs, we allow the time to digest
and make sure we enable the right things, the right tools
for them to do the job, right? And then bring them to our vision
and strategy for the alignment. Next thing is teamwork, for me, when, when it comes to transformations, again, it's not about one team
who can own everything. So we want to basically build
the observability platform, but at the same time enable enough
autonomy for engineering teams, right? We want the platform, not
the end-to-end journey. So there is a collaboration required,
right? We need to be transparent, we need to be proactive in communicating. We also need to distribute the work
that we need across the company. So we ask for observability champions. We identified observability
champions based on specific interest. We formed a group specific to
each verticals that we support. And then we worked as a community, we worked as a team to contribute
to some of the open source product, like OpenTelemetry for example. And that's how we were able to see
a massive adaptions then the cost, just a quick thing that
I wanted to understand. How many of you today do a total cost
ownership analysis for your observability platform? Let's be honest. Oh wow. Alright, this is one of the project
my boss asked me to take over, and this is, this is a great learning,
learning for me as personally, but also for the rest of
the leadership, right? We were able to understand that
there is nothing free in this world, that including the open source
product that you use in order to scale OpenTelemetry. We know that OpenTelemetry
is an open source community provided, but in terms of the platform cost, in terms of the resourcing required to
scale that solutions, everything is cost, right? So this is when, you know, we decided to work on
total cost to ownership, otherwise we don't want our
company to be bankrupted, right? So it gave us a lot of insight in
terms of how much are we spending for observability platform?
Where are we spending? How much amount are we spending there? Is there a possibility of deprecating
something as we are ramping up? How are we going to do the
ramp down of the legacy, the existing solutions, which is
not doing the job for us, right? So we use the data to
identify some of the places, some of the technologies to retail and
put together ramp up plan and also the ramp down plan together. Again, learning and educating when
it comes to transformation, when we are adapting to the new
things. , we worked on many things. We created a talkathon, which basically where we invited
all the observability champions along with our observability
group to revamp the training, to revamp the observability
recommendations to be up to date so that our talk recommendation trainings
are up to date for customers, also the internal teams to use it
and increase the adoptions as well, irrespective of how good the
talk recommendations are, your trainees and customers are
still going to ask questions? So we did set up a good support process. The incident management process
also we enabled feedback loop. That's I think is one of
the most important things
as well is to make sure we collect the continuous feedback
and improve as we progress. And me being a technical person, I'm
talking about technical challenges, but actually this is not
about technical challenges, it's more about communication. So when you have a dedicated team
to manage a technical product, you are getting used to
having a hands-on approach in troubleshooting stuff and being OnPrem and even like harder,
when we went to Grafana cloud, , we were used to troubleshooting the issues we were seeing in Grafana. And what we learned and what we
improved throughout these past two years was the way we communicate
with Grafana folks. And we learn to be more
persuasive. We learn to be able to have the right
communication channels to fix our problems. We don't have the complete perfect
communication channels yet. But throughout the past two years, we've worked with Grafana and
streamlined many aspects of our communication channels, which helps us very much in
the process of resolving our technical challenges, which has been many
during this transition. Alright, so a lot being
said, just a quick takeaway, vision and strategy or foundation.
Embrace the change, embrace the failure, learn from it. Remember learning and
development is a growth opportunity. I don't think that there
is a threat to be feared. If your observability doesn't help
answering when something happened, what happened, why was it happen? If they do not answer any four W Ws, then I think it's a time to change the
observability platform and the strategy, not the questions. So with that being
said, thank you for listening to us. , if there are any questions,
we are happy to answer.

