# Migrating to Grafana Cloud: Observability at Planet Labs (Grafana Labs Customer) | ObservabilityCON

Jacob Straszynski, Staff Engineer at Planet Labs discusses the company's observability journey. This talk covers how Planet Labs ...

Published on 2024-10-24T19:52:01Z

URL: https://www.youtube.com/watch?v=0UaM_yyUD2w

Transcript: Hey everyone. I'm Jacob Straszynski,
staff engineer at Planet Labs, and I'm here to talk about
our observability journey
from a suite of disparate tools to largely centralizing on
Grafana Cloud and their platform. I'll be discussing our motivations
for migrating our vendor evaluation process, technical and
project management strategies, as well as what we're looking
forward to in the future. Forgot this guy. If you're not familiar with Planet Labs, we're an Earth observation company
with a constellation of satellites, capable of imaging the entire surface
of our planet every single day. We have both medium and high resolution
satellites capable of imaging large vehicles, but not people. We like to emphasize that
because of privacy concerns, and I'll tell you that physics makes it
impossible with the satellites that we have the size of them to do that. In the media, you may have seen our images in various
news organizations surrounding events like the War in Ukraine or
the Nepal earthquake of 2015. Our imagery is used by companies
around the world for analysis, ranging from monitoring port
activity for economic markers, identifying illegal
mining and deforestation, and agricultural monitoring. So what was my role in this whole process? So I was closely and still am associated
with the platform operations team at the time. In fact, I was the tech lead. I was responsible for a lot of the
design, implementation, plumbing, and configuration of
the underlying systems. And I was heavily involved in the
migration planning in conjunction with my technical program manager
and engineering manager, A little bit of size and scale about
our organization to help provide some context. So we produced about 45 million
times series before the migration; produced about 110 terabytes
of log data per month. We've got a dozen Kubernetes
clusters, plus or minus a few. If we had to stand one up. And we run about a hundred
thousand instances at peak. A little bit more detail
with respect to the metrics, that number might be somewhat shocking
for folks or maybe somewhat pedestrian for others. But you know, you've got your cAdvisor
and kube-state-metrics data
that sort of comes along with all of your Kubernetes pods. And
then with the hundred thousand instances, I think it's interesting to note that we
peak at about 10,000 in our Kubernetes environment, and we have a
separate batch processing system, affectionately known as the job
system where we peak at about 90,000. And importantly the
organizational scale as well. This is another kind of like
dimension in the whole migration. We've got around 200 engineers, 24 teams, 120 GCP projects, and yes we
are a Google Cloud customer, and 50 plus ish microservices. All right, so let's set this stage around
2022 when this kind of idea of like, we gotta go and migrate to something
better than our status quo. There's broad community and Planet
Labs adoption of Prometheus. So this is really nice. There's broad community and Planet
Labs adoption of Kubernetes. So this is gonna be an important
leverage point for us when it comes to migrating. Grafana is in use
internally for our Kubernetes systems. So we've got our internal Grafana, they're deployed adjacent
to each Kubernetes cluster. There's limited adoption of
tracing within Planet Labs, and then there are other observability
and IRM tools like Sentry and PagerDuty in use at the company. So this is like a really simplified
diagram of our topology at the time. We're using Google Cloud Monitoring.
Just as a Google Cloud customer, you get this data. We're using
Google Cloud logging for logs. I mentioned our internal Prometheus, and we're using StatsD for quite a few
older services that were deployed at the, you know, early onset of our company. And those are typically running through
some kind of CollectD Telegraf agent before forwarding them to Splunk
observability where we visualize them. And then of course, we send alerts
to PagerDuty, which, you know, hits me on my cell phone
at 2:00 AM unfortunately. So that, that looks great. Except, we have a few kinks in
this whole puzzle here. First of all between Google Cloud
Logging and Splunk observability, we don't really have this
connection established. So if you need to go and look at
your log data because you're seeing a 500 error spike in
one of your dashboards, you have to go and jump
into Google Cloud Logging, get that time window aligned just
right, reformatting timestamps, and often times by then you might have
just lost your, your context entirely. We have our internal Prometheus metrics
but we're sending a limited subset to Splunk at the time or SignalFx.
And they're highly aggregated. So if you really need to kind of
drill down you find yourself jumping into the localized
Grafana instance as well. So that kind of brings us
to this decision point. We can continue to expand
our commit with Splunk. Maybe we should go and
adopt Grafana. We're, we're using it internally so we
have some experience with it, and maybe we could self-host, and this is the self-hosting
guy right here, . All this also kind of brings me to this
term of art in our industry of like, what's a single pane of glass? We've
heard that term quite a bit. Well, I've kind of described
what it isn't, right? We've got logs in Google Cloud Logging, and you have to make that
expensive context switch. We have metrics in both Splunk
and Grafana and tracing. Well, what's that? We're
not really using it. So we set about improving
the status quo and yeah. I'm here talking to you all today. So we clearly decided to buy instead
of build and we're using Grafana. So this is straight from one
of our product requirement
documents as we kind of engage in this process. The central
goal, right at the top of the doc. "Wanted to consolidate the three pillars
into a single cohesive user experience. Logs, metrics and traces should be provided
in a single view and minimize context switching." And that kind of brought us
to an evaluation process. So there was a period where we
started to do a publish metrics and logs to both Splunk and Grafana. Importantly we just fanned out the data
to multiple vendors under evaluation contracts. We took advantage of
high leverage integration points. So we had uniformly deployed
remote write configurations and Google Cloud Logging
sync configurations. So this made it fairly straightforward
to basically fan out metrics to both the providers. Once we were doing that, we wanted to support some
internal teams with adoption. So first we identified teams with
eager engineers that will act as early adopters and champions. Now, importantly, the relationships established in
this phase remain strong into the migration process. So this is like a really great
just migration strategy to use, leverage those early adopters. Once those teams had kind of gone and
kicked tires with the two products, we conducted user interviews. So basically an exit interview
after having used the product. Important note here, you want to be systematic in how you
gather your feedback so that you can quantify it. I've linked to a SurveyMonkey
article. It's like, you know, pretty, pretty basic, but the
advice there is awesome. And then of course we funneled those
results into the vendor selection documentation. So we wanted to, you
know, basically ratify our decision. And the process we tend to use for
some of these things as a architectural decision record. Again,
I've got a hyperlink there. I've kind of characterized it as a
concise alternative to RFCs or maybe more like full fledged design docs. One
of the things I like about ADRs is, you know, any kind of instance where somebody might
wanna retrace your steps and in 2028 be like, "why are you guys using
Grafana? Honeycomb is out there, it's the new hotness." Well,
you get a lot of air coverage, just point them at the ADR and, you
know, continue going on your business. So let's talk about why we chose
Grafana in the end. And again, this was feedback from
actually one of our documents. So "there's seamless and responsive
frontend for combined log, metric and tracing views, which reduced friction
during troubleshooting and
performance monitoring. The ability to leverage logs for ad
hoc metrics with the progression to recording rules for longer timescales." So it's just really nice that you can
start with a LogQL query that you haven't yet converted into a time
series necessarily; experiment
with it, validate it, and then if you find you want to evaluate
it over like a six month time span in the future, you can progress it to a recording role
and get that metric time series that's a lot more efficient. "The use of standard query languages
reduce the barrier to entry as we grow the software organization." So, and
I feel a little bit validated in, in this one in particular like
Google recently deprecated their MQL query language and is kind of
converging on PromQL as well. You know, like superficially, maybe like TraceQL
and LogQL are similar to PromQL, but you know, it still helps to kind of dive into
the syntax 'cause it's not a completely different syntax when you do that. And we found like really positive
results from active collaboration with Grafana's product teams
and, and key engineers. So I don't want to oversell this, I don't know if everybody else is gonna
have this support experience based on your spend commit. But talking to the actual contributors
of the open source product while you're having issues with their cloud
offering, having them tune it, having them kind of give us advice so
we could meet each other halfway was, was really important. We found
a lot of value there. And then, and also alluded to this briefly, but the commitment to the open source
and big tent mindset for their community. And again, open source software, you
can really feel that. And the whole, you know with enough eyes, all
bugs are shallow, you know, it's nice to be able to
source that periodically. So we're now onto the migration.
We've made the decision. We've got 24 teams to migrate some
with half a dozen services and others with dozens of dashboards
and just total alerts. Kind of brings me to the importance of, of change planning and kind of the thing
that you're trying to manage is, well, basically your innovators and your early
adopters during any migration are gonna be easy. They're just gonna almost want to hop in
once you offer the product in some kind of early access capacity. So the late majority and the laggards
that this process is really helpful with. And no judgment. As engineers, I think we all have competing priorities
and some folks are gonna be more excited about observability than
others within a big organization. I've kind of characterized this
as the goal being a smoothly orchestrated migration through a
process that surfaces unknown unknowns, builds momentum with early adopters, provide sufficient resources for
the thornier cases, IE the laggards, while providing coverage for the migration
in the form of business justification and infrequent internal communications. And another thing you're kind of trying
to avoid is an obligatory XKCD comic, although I think this is the
first one I've seen today. You don't want to introduce
Grafana Cloud, for example, and still have Splunk and
Datadog somewhere in the, in the guts of your infra. Alright, so a little bit
on migration, scoping. Roughly two dozen teams within the
organization to migrate. Mentioned that. There's a variety of shapes of
workloads that publish metrics. So web services probably the
most familiar to many of us, but we got scheduled tasks and batch
processing workloads as well that tend to be instrumented. We're a polyglot
org with lots of Python and Golang. So in our case, that means, you know, sometimes you have to write
wrappers and client libraries twice and teams are already subscribed to
operational and non-operational work. I guess like, you know, again, you really want give people a little bit
more time than you think they're gonna need or that you would
need. So the early adopters, they might do it in a sprint or two, but
realistically for a project like this, for a big organization, six months
gives you a lot of headroom. So a little bit on project management and
communication strategies that we used. Over communicate. I think
this is probably the, the best lesson you can learn about just
like communication within a software company over communicate, kinda want to cast a wide net and meet
people where they're at or where they happen to be at a point in
time. So Slack, email, and Zoom. A little bit more on that. So early on in the process we
conducted interviews and these stakeholder interviews were
conducted with a shared rubric. That shared rubric ensures repeatability
and fidelity in the process. So I wasn't the only one you
know, running these interviews. We had a team I had a team
behind me and it was, you know, really good that we could collaborate
on this rubric and make sure that we're offering a similar level of
support, asking similar questions. And as a Google doc, we could
collaborate on it and, and refine it. And the data in that Google document
that we created during the interview process fed into the ticket
creation that followed. And I'll have a few screenshots
of the Google Doc that we used. We also offered office hours, so this is sort of a manifestation
of the Zoom communication style, and that was an opportunity to
build community and talk shop, which is really fun. And also it gives engineers
permission to utilize your time. Some folks are shy when they see my
calendar with the Swiss cheese of meetings just scattered throughout. So having
that time set aside is, is really, really helpful. And then
bimonthly Slack updates, so broadcast to those that use
Slack as their productivity IDE instead of email. And here's an example of the interview
interview rubric that basically created for the process. So just a
few bits of like data entry. We've got clear meeting goals outlined
here. This is really important. I think, you know, just within the document, but
also within your, your calendar invites, I feel guilty inviting
people to a meeting. And when we're doing this
across two dozen teams, you want to kind of let people know why
are you talking to me and occupying 90 minutes of my time? And then within the document we sort
of like bootstrap people's migration process with like some inline tips
links for more in-depth content. I've kind of included a lot of the like
content in this like little image that we actually had in a more normative
document that was part of our internal knowledge base. And you kind of see here after kind
of going through the interview, you'd fill out these rows and kind
of take an inventory of your various dashboards and so on. And this is important in the sort of
uncovering the unknown unknowns aspect. Like there were a lot of
just interesting use cases. I discovered like systems that published
maybe a few data points per day that would otherwise get TTL's by some
of our like metrics aggregators. So their data would just disappear
before it had a chance to, to increment. And of course, after , everybody's showing cool
demos and I've just got a, a picture of some Jira tickets . But after going through
that interview process, like producing this list of
epocs, it was really easy. Just kind of ran a CSV
import on some of the data. A little bit on technical strategies
as well. And I alluded to this briefly, but you want to a minimize
point-to-point integrations. So use high leverage points. In our
case as a Google Cloud customer, we're using Cloud Logging syncs and
fleet wide remote write configurations. So we deploy all of our
Prometheus using gitops. Makes it easy to go and
update the configuration and
just deploy it fleet wide. Logging syncs. If you're
a Google Cloud user, you can set those on an organizational
project or folder level. Infrastructure as code where applicable. This maybe is more accurately termed
configuration as code but specifically with teams folders and contact points
and the notification policy as well. We wanted to make this repeatable
when we were onboarding teams. So we've just got a data-driven
YAML file. We add a team there, it splats out their,
their team, their folders. It does the LDAP sync for us and sets
up some contact points for them so that they can get paged. Yay. With notification policies these I
think can be a little bit brittle. So we wanted to offer some
guardrails. By brittle, I mean, you don't want to basically leave it wide
open and let one configuration shadow the entire notification policy and consume
all the alerts. And then with alerts, we've decided as an organization to
implement this as configuration or IAC as code depending on your diction. And that offers providence for alert
configuration and reconfiguration in our case. So why did we change
this from high to low? Are we sweeping it under a rug
or is there some kind of a, is it just a noisy alert or what have you? And then internal libraries these
were quite useful for us as well. So we created a few
opinionated thin wrappers. And these facilitated an improved DevEx
in, in our case. And now mind you, I think a lot of what we saw earlier
today might kind of succeed some of these this approach in the migration. Migration was an opportunity to
drive the adoption of these libraries as well. So if you weren't using Prometheus
before you might as well adopt like your Prometheus client, but use kind of our thin wrapper around
it if you're going to do the work anyway. And we offered
some compatibility layers. So examples of this, if you're
a StatsD user, you know, you've got StatsD exporter,
there's Vector Telegraf, and probably Grafana Agent as
well. But for whatever reason, we didn't use it for,
for StatsD specifically. And here's an example of a shared service
dashboard that we created that was, you know, powered by the fact that
we had consistency around
this service name attribute thanks to the client
library that we were using. A little bit on the migration
pains that we faced. Performance issues with Mimir and Loki
except these were resolved by Grafana through collaboration and tuning. So a little bit of validation of the
whole by decision instead of build. They're really quick and I
couldn't imagine having to
go through this myself and with my team. The Terraform provider. Infrastructure as code exposes some of
the impotence mismatches between the underlying APIs. So Grafana
really is a, you know, an aggregation of a variety of products, and you can see a little bit of that
when you use the IAC to configure things. So like Loki versus Mimir recording
rules require different tooling. And then Grafana.com's organizational
authorization rules versus the like stack specific grafana.net authorization. You kind of see how
that's different as well. With cost management we ran into
a few kind of like issues as well. So the infra we couldn't minimize
it as much as we had anticipated. Like ideally we're not running
Prometheus servers or agents at all, but you still have to forward metrics. And because of running things
in agent mode and updating our Prometheus servers, we yielded about a half to a quarter
reduction in resource utilization. It didn't get us down, you know,
to maybe like a 90% reduction. Cardinality often crops up with
corrective action taken on our part. So if folks around for Omar's talk, he mentioned bringing their time series
from like 70 million to around 50 and we crept up to 60 million and we're able
to get it back down to 45 million using Adaptive Metrics. And nobody
complained after I applied those rules. So awesome experience there.
And then the whole, like, we were kind of maybe in this awkward
transition where Grafana Agent was going and then they added Grafana Agent flow
mode and then they just switched Grafana Agent flow to, to Alloy. So that required
a little bit of, yeah, , yeah, you know, that it's
not as bad as SignalFx. They had like a dozen agents it seemed
so like this is still better and it looks like we're largely centralizing
on Alloy at this point, and they offered you know, like CLI
command to go and port your configuration, which I think worked quite well
for us. Migration successes. And this is just a quote
from one of our engineers. I I didn't ask him for
permission to quote his name, so let's leave it anonymous for now. But "Grafana Cloud significantly
improved my team's ability to observe and triage the systems we own. We've been able to greatly decrease
fragmentation in observability tooling and achieve consistency in how we monitor
on alerts and key signals across our systems. Being able to easily
triage issues across metrics, logs, and traces has helped us improve
system performance as well as operator confidence when on-call." Sounds
like we met that goal at the outset. It also helped us it also equipped us
to quickly sketch out dashboards or queries which answer product questions
leading to better understanding of not only how our systems perform, but how
our users are interacting with them and what's next for us. So k6, we're looking into that. I, I'd been a k6 user prior to their
sort of adoption by Grafana. A strong combination of
load and acceptance testing
capabilities makes it pretty useful. We're using the
fledgling k6 operator as well, which makes it easy to scale. Basically your load generation beyond
what you can do within a single instance. So if you've ever kind of done this in
a large systems you'll kind of exhaust what like a single Kubernetes pod can do. You have to go and repeat
that to a few more replicas. Pyroscope with tracing, we're
starting to do a lot of that, but if you're a Python user
and you're kind of like, I'm just going to monkey patch every
function call and like add tracing to it, don't do that. You're probably
looking for profiling instead. With Grafana Incident and Grafana
OnCall we need to still wean ourselves off of PagerDuty. So if we do that if
we move to Grafana Incident and OnCall, we'll have tighter
integration to boot as well. This just hasn't been this big of
an issue because the, you know, call and engineer and
page them functionality, functionality is largely worked for us. And Grafana SLO has shown promise as a
forcing function for interdependent teams to agree on contracts between their
services. I think like informally, we've sort of been doing Grafana SLO
before they introduced it by like creating alerts with appropriate labels,
and then linking panels together. But if you do it with Grafana SLO, you
kind of have a nice turnkey experience. Cool. I, that's my talk. And thanks
everybody for, for attending. This is my GitHub. If folks want to
like kind of check out my profile, you'll see this picture. And
I get a lot of comments on it. I'm like up here in Yosemite on the
northeast buttress of Higher Cathedral at that point in time. Awesome.

