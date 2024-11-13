# Migrating to Grafana Cloud: Observability with Dashboards as Code at ASAPP | ObservabilityCON 2024

ASAPP staff SRE engineers Pato Arvizu and Ramiro de Zavalia share their journey of migrating to Grafana Cloud to unify ...

Published on 2024-10-24T19:52:15Z

URL: https://www.youtube.com/watch?v=9Ge0OmWyNtg

Transcript: Thank you very much for being here.
We know it's a little bit late. We know there's a, there's a break
right after this. We're trying to keep, keep you entertained. So my name is
Pato. I have Ramiro with me here. We both work for a company called ASAPP.
I'm gonna talk about it in a minute. It's called ASAPP. That's
how we pronounce it. We're both in the SRE team,
we're both staff SRE engineers. I noticed that people have been putting
their contact information at the end. We should have done that, but here's our Instagram and LinkedIn
contact information if you want. So a couple people stole my
joke about this yesterday, but we can't go 2024 without mentioning
AI in a tech conference, blah, blah, blah, whatever. But in this case, we are talking about the company
that we work for. So ASAPP. We are a company that creates, or has Gen AI solutions for contact centers, for companies that have to
have end customer contact. So think about when you've talked to your
bank, your airline, hotel, et cetera. So instead of having to call and
have an analog call with one human, try to make that more digital,
more smarter and, you know, kind of have a different, different
way of interacting with it. So this is not a pitch for the company, but just there's a couple of
numbers here of, of you know, the successes we've had with our
customers. And just so you get an idea, a little bit of what kinds of
challenges and problems we, we deal with and we have to
address, right? So, a little, very short agenda of what we're
gonna talk about today. So, the sort of larger topic is our migration
to Grafana Cloud from our previous observability vendors and like kind
of fragmented observability stack into Grafana Cloud. Then we're gonna address or talk a
little bit about the main problem, or the main thing that we're gonna
address here, or talk about in this, in this talk, which was the, the creation
of the dashboards. But first of all, paint the picture of what the
problem was, how we solved it, and getting a little bit of technical
details on, on that solution, and then a demo to kind of
tie everything together. Okay. So let's start talking about how
we moved to Grafana and why we did it. Many of the reasons have already
been covered in this conference, but let's go through them really
quickly. So, basically, over the years, we have like accumulated a number of
problems and issues and things that we wanted to improve. One was that we were actually
having many vendors for our solution. So if you wanted to check
metrics, you will have to use one UI, but then if you wanted to check logs
or traces, it was like a different UI. It was painful to use and really hard
to correlate between those. So for us, Grafana was like a perfect
fit here because we can see
everything in one place, but also it supports
a lot of data sources. So it's a little bit related with the the integration and how we wanted
to abstract and grow our system. The fact that it supports many data
sources actually allow us to, for example, have our own system with we have
integrated with the JSON data source, so we can keep adding more stuff
into our observability stack. Then of course, cost was an issue. We wanted to get like the most
value of out of each dollar that we spent, but also like the model pricing that we were
having was based on host or number of services, and we were
running on Kubernetes. So we have like a ton of
hosts and a ton of services. So moving to a model pricing based on
volume was really a good fit for us. And then again, adaptive metrics, we
ended up using that and, and save us. It was like a quick win for us to
show. So yeah, use adaptive metrics. Then team onboarding was hard. Again,
multiple vendors, multiple different UIs. So the system was a little bit
complex having just one vendor make it a all easier. But we also like the philosophy that
Grafana is using for the query language. Like, if you know PromQL then there
is some things that at least you can apply on, on LogQL and TraceQL. So it make it a little bit easier to
transition from one query language to the other. And also there is like a ton of
documentation and information online, so it's simpler to get
onboarding. And lastly, vendor lockin. This has already been
covered already on the conference. I'm not gonna talk a lot about that.
But one of the things that we like is, since many of the products Grafana
is using is for cloud are actually open source we can actually choose which
part of the stack we run in Grafana Cloud, and which was we run on-prem. So let's go quite fast over the, what, how architectures look like now that
we are in using Grafana Cloud. So most of our services running
in Kubernetes are instrumented. So they are producing all the signals, metric log and traces and we
have agents for each of those. We were already using Loki for
logs internally in in our own on-prem stack. And we keep it that
way because we were happy with it. It's working. We didn't
want, didn't want to move it. But then we choose Mimir and Tempo
both running in Grafana Cloud for our traces and metrics. But we also run Prometheus
and Thanos internally. And we basically do that because
for our lower environments, like test and station environments
we actually don't need such a high SLA or like a long retention period. So we have like a smaller setup
there where we can set our metrics. And one of the nice features, that's the instance that we have
running in Grafana Cloud. The, the Grafana instance that
we have in Grafana Cloud is
actually able to talk with all those backends, even the
ones that we run on-prem. So it's like a unified
view for, for our users. So let's talk a little bit
about the migration. And again, I'm gonna be quite fast, and to be honest, there is a ton more that we
could say about the migration, but we're trying to focus the talk
about dashboards. So keep that in mind. So we have like 3 million active series
that we have to move into Grafana Cloud, and then we have like six
60 terabytes of traces. We were able to reduce that
number a lot by using sampling. But then we have like 400
dashboard, which was sort of a mess, and we're gonna talk a little
bit more into detail for that. We did reduce that number a lot
over the migration. But yeah, let, let's go over those in
a, in a little bit. So, some of the challenges that we have at
the moment were that some of the tools that we wanted to use for the process
that we have envisioned were not there yet. So we wanted to manage our dashboards
through Kubernetes using the controller, but there was
no, no controller available
at the moment. Nowadays, you can actually use the
Grafana operator for this, but since there was nothing there at,
at the moment that we were demoing it, we actually created our own. And then we wanted to
simplify the process. So we built our, our own CLI to manage
most of the lifecycle of dashboard creation and update. And then we build a little
visualizations and tools that allow our developers, which are the users
of the, of obsevability stack just to see if there is, there was any error or why their
dashboard was not created or what's, what's going on there. And then let's talk a little bit about
onboarding and moving from one system into Grafana Cloud. With all these change,
I mean, besides the migration itself, we were also changing the process and
the tools that teams will have to use. I think many of these things
have already been covered, but basically we have
documentation in place. We did try to simplify the process as
much as we could so that it was easy to adopt, and that's why we build all the
tools that we could think about to make it easier. And then since this, this was a process that we were
gonna use for the migration, but we also wanted to keep it
using after the migration and, and make it the standard way
to interact with the system. We actually used the migration as a
selling point for the whole process. So if you follow the process
and you use the tools that, that we have put in place, the migration was actually a lot easier
because teams will have to translate the dashboard that they have in the old
provider into Grafana Cloud, and PromQL. And so using the tools that we have in
place make it a lot easier. And finally, of course, we have demos and office hours so that
you not only read on how to do the things, but you can actually see it
in action and, and see it working. Alright. So, like I mentioned earlier, one of the main things
one main pillars of, of this migration was the ability to
for service owners to still have that observability, that visibility into the performance
of their systems as they were live, as their incidents happen and whatnot. So because we have a lot of other things within the company and
in general as declarative
definitions like infrastructure as code and, and some other things, wanted to kind of have the same concept
with dashboards. As most of you know, it's nearly impossible
to write dashboard, it, like the whole JSON model from
scratch manually. You can use, you know, SDKs or other things, but the idea of having people create
their dashboards from scratch the same way, or, or with the equivalent dashboards that
they had in the previous vendor was impossible. So I wanted to have
something that was more of a full workflow from scratch to visualizing
and sharing the dashboard. So we created this, it's
not a revolutionary concept
of dashboard as code, but we want to take
that concept to this. So one of the main problems
within that, that realm of, of dashboard management was the dashboard
dispersion what we're calling. So there was no clear process or
definition, how to create a dashboard, how to contribute to a
dashboard, how to share it. The organization or the hierarchy
within directories was kind of, there's non-existent. It was hard to
trace who the owner of dashboard was, what service it was monitoring. We ended up with dashboards with
names like PatosDashboardCopy2-extra or something like that.
And it was hard to like, create or follow the progress of the
evolution of a dashboard asset was modified and often people would find it
hard to contribute to a dashboard that was almost what they wanted, but not
quite. So they ended up copying it. So all these things that, that
caused diversions and not, like the lack of convergence of dashboards
led us to try to solve this problem. So, so we wanted to create, again, not just the dashboard definition as code, but have a full life cycle of
managing it from creating it to deploying it or visualizing it in, in a shared manner that was
as automated as possible. We ended up with this kind of Grafana
- git - Grafana sort of cycle. The, the main part of this, the
first part of this rather, is give users a tool for creating
dashboards visually so that, because that's basically the main, the main way that everybody that uses
Grafana ends up creating a dashboard or creating any visualization. It's much easier to create visually
than it is to create it or, or to try to find a way of doing
a writing the JSON definition. So have a tool to be able to
build that dashboard visually, and then capture that as code,
not as stored in Grafana, but as code, put it in git and then from
git push it to Grafana Cloud. Via have the dashboards API, so that it's be able to visualize it
and share it with the other people. So we're gonna get into a little bit more
detail about that. So how we did this, I'm gonna try to keep it high level and
sort of get into some tech technical details if needed. But these are the, the five main components
of the solution. Obviously, Grafana Cloud is at the
top, 'cause you know, we're building everything on top of this. It's not nothing critical
that it's about Grafana Cloud, but we are migrating to the Grafana Cloud.
So that's, that, that was, you know, at the top of the solution. So
Kubernetes, we already have most of our, I guess 99% of our workloads on
Kubernetes. We have a lot of, not just running the workloads
from Kubernetes, but configuration, injection deployment, pipelines,
integration, et cetera. So like Kubernetes was the, the ideal platform on top
of which build a solution. ArgoCD not getting into a lot of
detail, but if you're familiar with it, is a it's not quite a CICD platform, but it's more like a continuous gitops
platform of sorts runs on top of Kubernetes and it can deploy
Kubernetes objects through its its API then we wrote a custom controller.
This is going back to Kubernetes, that those a automated controller or
a controller that was automatically synchronizing definitions of dashboards
to the Grafana Cloud dashboards, API. We did that using a
framework called operator SDK, and then a custom CLI for like
managing the first part of it, which is creating the,
the dashboards visually. Without getting into a lot of detail, that's kind of what the
process ended up looking like. So on the bottom of user
is managing a dashboard. It didn't have to have that name, but it's dashboard.YAML file that
contains the definition of it. User would run the graph command,
which is the, the tool that we created. We're not talk about double
click on it a little bit later. Static dashboard. It would show a temporary dashboard in
a kind of sandbox area of Grafana Cloud. Then instead of storing it as
a dashboard in Grafana Cloud, the graph tool would download the
JSON model, put it in it in a file, and then the user would commit it
to git. The changes in git would be, would be picked up by ArgoCD. ArgoCD
would deploy them to Kubernetes. Within Kubernetes, the operator the
automated controller was running, and it was talking to the Grafana
Cloud API on a production area, and creating the dashboard
by itself that was shared with the rest of the organization. Stepping back a little bit before
we started with like producing a or creating this, this large case solution, we wanted to make sure that we
were solving the right problems, and we wanted to have some document
or some guideline that we can turn and say, we did solve these problems. We didn't want to like go start getting
creative and then start solving problems that went in there. We wanted to
fix or address this five things. So one thing is, because we
were deploying this as code, we wanted to have the, or deploying
dashboards as code. We wanted to, to keep the code for the dashboards as
close as possible to the application code, and to the extent as
possible to the configuration, which is the Kubernetes deployments
and Kubernetes manifest and all that. So the ideal goal was that it would be, it would live in the exact
same repository you know, being in the same branch and versioning,
et cetera. So that was one thing. Other thing is we wanted to,
we didn't want to get on a, on a wrong foot and start without a
process for creating dashboards and end up with the same mess that we ended
up with the previous vendor. So we want to establish
a clear process for this. And it wasn't obvious at the beginning
where the process was gonna be, but we always knew that we wanted to
have something that was clear, unique, no edge cases, no conditional,
et cetera. Anybody, regardless of what their stack
or what their programming language was, would create
the dashboard the same way. Read Only access is part of the process, because we wanted people to be able to
visualize anything that they deployed and keep it open to the entire
company to the extent that's possible, but only be able to create dashboards
through the established process, which is not through Grafana Cloud,
or not through like the Grafana UI, but rather through the workflow
that we ended up creating. So, with the also the other
problem that I mentioned earlier is tracking the ownership of dashboard, whether to a specific person or to a team, or to a microservice or
microservice owned by a team. It was almost impossible before because
we were not imposing any standards. We were not doing any kind
of automated tracking, but now we wanted to fix that. So
that's where we ended up with, but we, it was clear to us that we wanted to
have that as one of the main goals. And kind of tying everything together, make git the source of truth
so that what's defined in git is what's deployed and only
that's deployed. There's, there's no way of modifying things
externally. There's not way of, of like cheating and working
around the, the process. That is the only thing
that gets created. Okay, getting a little bit technical here.
I hope you know, you stay with me. So the controller, this,
they're different names for it, but controller and operator, they're,
they're kind of interchangeable, but it's a service or a
workload that's running within Kubernetes, that's running in a loop that is
reconciling some definition with some API. It might not be clear for, you know,
be as, as kind of broad as possible, but hopefully it'll
make sense in a minute. So don't wanna get into a lot of details
because this is outside of the scope of the talk, but Operator SDK
is a framework for creating workflows like this. So operators
like this that runs in Kubernetes abstracts out a lot of the complexity
of talking to the Kubernetes API, such as authenticating,
listening for events, generating metrics off
the operator itself, and all those things so that the
only thing that's left is for you to implement the logic of the thing that
you want to, to synchronize or to, you know orchestrate between APIs. Because it's meant to be run for
Kubernetes, this is obviously like a, a great fit for us. So this, doing the, doing this this way enable
this to be a continuous gitops operation, rather than have something that's pipeline
based that would only guarantee that things are synced at the
moment that you're on the
pipeline. But with this, the, the definition is continuously
being synced and continuously being, being reconciled. So that guarantee that the
definition was what was there, and there's no cheating, no, no kind
of going around the, the the pipelines. And the Operators SDK allows you to
integrate with external APIs as well. It doesn't need to be something that
runs within Kubernetes. In our case, we were able to integrate
Kubernetes objects and
Kubernetes definitions with the Grafana dashboards API. Very briefly, this is what the reconciliation loop
ended up looking like. This is a, a more genetic model of how Operator
SDK works, but in our specific case so this at the bottom is the
operator or the controller. This is what's running the logic. Back
up a little bit. The user is modifying, if you're familiar with Kubernetes, we have a config map which is basically
just a key value pair document with a key value store of things, wind up storing the entire dashboard
definition there in a config map object. So the user, I'm simplifying it here, but the user's not modifying the config
map, the user's modifying the config. It's not modifying the config map with
the Kubernetes API directly is modifying it through the established
process sourced in git. So once it's in git the
operator, well, once it's git, ArcoCD deploys it then the operator watches
for changes to config maps or the creation of new config maps, parses that the contents of that were
actually just takes the whole definition and then talks to the dashboards, API in Grafana Cloud cloud to either
create a new dashboard or modify an existing one. And as long
as the oh, as long as the, the config map is deployed to a specific
namespace and has specific annotation, then operator would would
do that. And then lastly, just update the status of the config map
tube so that it's more for feedback and visibility purposes of to be able
to know when something was created. So the end result that we
had was that we were able to turn something that's
as ugly as this. Obviously, this is far from the full definition
of a dashboard. You can see it's the, like the first whatever, 20
lines of 30, 40 of whatever, 200, 300, 400 lines,
probably way more of your, if your dashboard's more more complicated. So turn something like this
that's impossible or all
almost impossible to write by hand into this. That's something,
you know, nicer and prettier. Obviously the numbers there don't
look pretty, but forget about that. This is like the visualization itself is
what's pretty, and this is, by the way, this is exactly what the author
of the dashboard created visually. It was stored in git and
it was deployed like this. Okay, so let's go over the
CLI tools that we call that. We call it graf because we
are, we suck at naming things. But basically why we did it,
we wanted to remove friction, so that adoption was easier. So we tried to remove any manual
step or automate it as much as possible. But then we were also doing
like this huge migration, and we wanted teams to
own their own dashboards. So they will have to do
the migration themself. And doing it manually will take a
lot of time, and it will, it will be, there will be a lot of errors. So there was no tool to do
this automatically at the time. So we build our own, and basically the graf CLI tool
has the logic to do the translation from our old vendor into
Grafana Cloud and PromQL. And also it was nice to have a
place to enforce some defaults so that variables and, and folders and the things that
we have in Grafana Cloud don't, don't become mess. So basically a tool, what it's doing is managing the
workflow in the sandbox environment. So it's going to talk with
the Grafana API so it reads the definition from your YAML file, and it will create a copy of that
dashboard in a sandbox environment. Then you can do any change there, save it, and it will sync back those
changes into YAML file. And it will remove the
version on the sandbox. But then it also had the
feature to actually migrate dashboards from our old
vendor into Grafana. So it will translate the
schema of the dashboard itself, but it also will handle
renaming the metrics because
we were using StatsD and we switched to Prometheus. So
we had to rename everything. And it will also be able to actually
translate the query language so that you get a, a fully working PromQL expression. This was hard to do, and
it worked most of the time, but sometimes we just break the
expression and users will have to actually check and fix
those. Usually it was, was sort of an edge case, or
most of the time, this work. And at the end of the day, you only have to fix one or two
expressions instead of having to write like 20 expressions to
create your dashboard. So this make the process
a lot faster for us. Okay, let's try to do a demo. So this is ArgoCD. This is like a dummy environment, so
we don't have a lot of stuff here, but basically this is ArgoCD.
It's already watching a git repo, and it has two dashboards
out of that git repo. So basically here we have like the
definition that ArgoCD is watching. So this ArgoCD is actually
creating those config maps into a Kubernetes cluster. And then we have the operator
reading that config, that config map, and it's actually creating these
dashboards out of those definitions. So here we have the dashboard.
Since we are in Grafana Cloud, it's really easy to use RBAC in this case. Like our sandbox environment is just
a folder inside the same instance. But we can use RBAC to actually make
everything read only for the user, it except for the sandbox, right? So they will be able to make
changes inside the sandbox, but they will not be able to
change the real dashboard. And we are storing those definitions
in a GitHub repo. So we have them here Everything is here. Okay. Now, how
do we do a change? In this case, in this case, we already
have the dashboard there, but let's say we want to make a change. So we run this graf command, and basically what it's gonna do is going
to create a new copy of the dashboard into the sandbox environment graph.
It's gonna create this panel, this text panel by default,
just to provide some feedbacks. But this panel is not gonna get
exported into the YAML file, so I'm just gonna remove it. And
basically we have the same dashboard. This is like a copy of the dashboard, and we can make any
change here that we want. So let's make some silly
changes to make it clear. We can even change like
the PromQL expression. Okay, so now that we have made changes
to our dashboard let's save it. Okay, all good. Then we can
go back to the graf CLI, it's gonna show us what has
changed. We can quit it. And now I'm, I mean, this is
already a clone of the git repo, so I can check here and I
can see that there were, there was actually some
changes on the dashboard. So let's go ahead and
add those changes to the repo. Okay. And let's push the changes. Okay, so now we have, if we go back into the git repo, We Can create the PR. Someone can, could come and like review this PR
and see that the changes actually make sense. So we can see here what
has changed. But in this case, we're just gonna merge it. Okay, all good. So now that we have the changes committed, we can go back into ArgoCD, let's refresh. So ArgoCD has already realized that
there was a change in the git repo and has already seen those
changes in the cluster, and the controller should have picked
those changes. Oh, I think I screwed the, the expression, right? But you can see that the changes
that I made are actually here, let me check. I think I, I
broke the expression, probably
I did something wrong. I swear we practiced
this 10 times. . Now someone can come and fix this and
make a PR to actually fix it. So now when, when you close the
running instance of graf, actually this dashboard
shouldn't exist anymore. Let's see if that works at least. So yeah, it's showing an error
because the dashboard was
removed by graf. And so yeah, that's our workflow and that's how we
manage dashboard. And that's the demo. Yeah. Thank you very much.

