# How to Achieve Observability as Code with Grafana | LiveRamp at ObservabilityCON on the Road 2024

Leveraging Terraform alongside Grafana, Kubernetes, and Helm providers, the SRE team at LiveRamp has transformed every ...

Published on 2024-05-10T23:03:42Z

URL: https://www.youtube.com/watch?v=ZCZcqmNOW1A

Transcript: Good morning everybody. I hope everybody enjoy all the new
features that the Grafana team just showed us. And today, I have one question. Most of us have stood up a monitoring
stack - configuring agents, trying to pull metrics, logs,
traces and all that, right? And we know how repetitive and time
consuming that could be, right? And at LiveRamp, Raj and I, and other SRE engineers
did the same thing, right? And we did it at a little
bit of a bigger scale. We have to do it for many
teams, many applications, many systems, right? And
that becomes a lot of work. So before I jump in and talk
about Grafana observability as code at LiveRamp, I want to tell you what LiveRamp is. So LiveRamp is the data collaboration
platform of choice for the world's most innovative companies. Our best in class enterprise
platform offers complete flexibility to collaborate
wherever data lives, to support a wide range of data
collaboration use cases within organizations, between brands and across
our global networks of premier partners. But enough
about LiveRamp, right? We wanna get back to our
journey. So what did we do? So at LiveRamp, about a year ago, we started our journey to
onboard onto Grafana Cloud. We use all the major
products. We use Mimir, Loki, Tempo, k6, synthetic (monitoring) as well
as the Grafana alerting feature. And to do that for many
teams that we have, it's very time consuming. And at times,
it's getting a little boring, right? We don't want to continue to do that. So we want to create a
self-service model that any team can leverage and
onboard themselves without SREs at LiveRamp having
to go and do it for them. And I know that there are
many infrastructure as
code out there, like Chef, Puppet, Ansible, SaltStack,
you name it, right? However, at LiveRamp our infrastructure
as code of choice is Terraform. So instead of
setting up all the other stacks, we decided to use Terraform along
with the Kubernetes provider, mainly the helm provider
for this project as well. So I wanna walk you through our journey in implementing this observability
as code at LiveRamp. So first I'll talk about our main
objective, what we set out to do, and then I will show you the
data pipeline that we created and implemented to meet one of those, or two of those objectives. And then I'll show you the
agent that we created in Terraform to meet the other
set of objectives as well. And then Raj here will talk to you, or show you synthetic
monitoring from Grafana, synthetic feature, k6 browser testing for
performance testing and user emulation in a way. And then also alerting.
And remember all of these, we are doing it as code, right? That's
the topic of this talk, right? We, we try not to do anything
manually or repetitively. And so we have two main objectives. Our main objective number one
is to minimize cost, right? We understand that metrics, we are charged by metric series. So a metric series is
a metric name with all of its labels and the different
values of those labels make up a metric series. And a multiplication of all that
make a metric cardinality, right? And a lot of metric cardinality, we
get bigger bill and we don't want that. That's one of the things that the
Grafana team has mentioned earlier, that they want to cut costs for our
customer or their customer as well. And we are their customer.
And, not just metrics. We have logs, right? We
have debug, log error logs, application stack traces. Mainly
we worry about error logs, right? Info and debug and stack traces
are just taking up a lot of storage that, you know, a lot of
time we don't look at. So it's a little bit wasteful and
it costs money to store those, those things that we don't use. And, and so that, that's number one. But we have a small compliance
requirement as well. We wanna make sure that all the
data we send to logs, metrics, traces and everything that flow
to Grafana Cloud doesn't have PII or confidential information
that we have and some, you know. So that's the
number one objective. Number
two objective is usability. We have a lot of teams and
we wanna make sure that when we set this up, it's
a self-service model. So we want it to be simple. Simple for teams to learn and use and
repeat without having to have SREs explain every single thing. The number
two is composable, right? Compostability is having
many smaller components combined together to create a bigger
system or a more complex system - that's composability and then
extensibility - extensible. We wanna make it easy and simple, however, we don't wanna make it so, so extensibility kind
of limits flexibility. We have to encapsulate a lot of
stuff. So when we encapsulate things, it tends to make it harder for a team
to configure it for their own use case, especially use case for example. And
then the fourth one is maintainability. Since it's a self service model, we set up in a way that is
simple. So when it's simple, we have to have a lot of agents.
And when there's a lot of agents, it will become less maintainable. However, I think we fixed that with what
I'm gonna show you next. So to achieve our number one goal is
to cut costs as well as (achieve) compliance. I'm gonna show
you our data pipeline, okay? So you see here on the left is LiveRamp,
and on the right is Grafana Cloud. And at the LiveRamp side, we created, or we stood up a bunch of collectors
,and this collector we're taking metrics. So any kind of metric - cluster,
pod, you know, application metrics, etc. And then we have logs and
all those logs, application logs, container logs, they all go to these
collectors. Same thing with traces. And we have several other agents as well
that collects metrics from Prometheus endpoints, GCP monitoring, API, and
legacy application like (inaudible). And when it go through the collector, the collector's job is to
filter all the data, right? So to meet compliance requirements
and lowering costs for metrics, we whitelist the metrics if they're not
allowed in the white list or they will not be flowing into Grafana Cloud. And also it drops all the labels
that are not allowed as well. Same thing with logs. We drop all the logs that
are PII or debug logs or applications, stack trace logs. It doesn't make sense to send them over
if we are not gonna use it. Similarly, same thing with traces. We remove the data inside of the trace itself, as well as query
parameters that might have name, address information and
etc. So that is our cost minimization as well as
compliance data flow. And to meet the second objective,
which is usability, right? I'm gonna show you how we
design our agent so that it's easy, right? So the number one
is simplicity. I mentioned earlier, simplicity, right? So we wanna
make it easier for teams. So we have these agents as well.
Again, one more time, metrics, logs, traces and all that, right?
And it's several other agents. I think we have about 10 now, but all of them only need three data
points: environments, teams, and region. So with these three data points, they are able to use Grafana UI to dissect their data, to create dashboard query, and make a distinction between
all of those for that team. And simplicity, right? So it's
short. I just showed you simplicity, but this is how it looks as code,
right? So just the call to the, the agent code and then the three
variables, and that's it. Simple. The second pillar of usability
I mentioned is extensibility. Simplicity is good. I mentioned earlier
when it's simple, we encapsulate a lot. So when we encapsulate things, it limits the thing that we can customize. However we do give the teams the ability to add more
metadata so that they can drill it down easier or quicker and
more labels do help with performance. Of course, when you have excessive,
then it'll be costly. But you know, we're not doing that. So we do have
give them ability to say, "Hey, what GCP project?" in this instance. And then also what cluster this is?
What Kubernetes cluster. However, if that is not enough, we gave them the ability to specify
any other metadata they want, right? Through an attribute variable. And we even gave them the ability to customize everything about
helm, right? Helm release, helm repository helm version,
helm tags and all that stuff. And then we also give them the ability
to override everything about the helm chart itself, like inside of that thing. So whatever we pre-canned for
them and they don't like it, or they want to customize portion
of it with the way helm works, any values that come after
the prior ones take precedent. So with this override
variable, they will be, be able to override everything
that we already did that does not meet the use case. And here what
it looks like in code. All right? Same thing again:
environment, team and region. All those are the three required
variables. And then project, cluster, and attribute. They can name it,
give whatever value they want, and then the helm release
information as well as the overrides. So the overrides, they can put whatever they want in
there and it will take over whatever we already predefined. And then the third pillar
is composability, right?
So I mentioned earlier, composability is when you
merge smaller components and it make a bigger system. We have
a lot of agents. So metrics, logs, traces, statsd for the
legacy application metrics. Prometheus to scrape from
HTTP endpoint as well as the various agents. However, the team
doesn't have to use all of this, right? They can choose whichever one
they want. "Hey, I don't need metrics, I don't need logs, I just wanna support my
legacy application." So
they just install the statsd agent. I just wanna pull from Prometheus
endpoints, just install the prom agent. So some of you were like,
probably think, "Chung, why so many agents, right? Why so many agents using up
too much resources?"The reason we chose to do it this
way is for two reasons. One, we're running in Kubernetes. So we
following the microservices paradigm. And that means one process does one
thing and does it really well, right? And number two is separation of concerns. So what that means is when we
have different agents here, if metrics agent falls over my logs
and my traces or my other agents are not affected, but if we put everything into
one and that guy falls over, everything stops, right? And
to answer the question about, you know, using up too many resources, we created all these agents with very low resource requests, CPU and memory and the
bare minimum for it to run. We do give it a limit of higher so
that it can climb us as much as it needs, but usually we
don't see that problem. And the last pillar of
usability is maintainability. I mentioned earlier we have a lot of
agents. So that would be a lot of code, a lot of things to remember and
updates and things like that for SREs. So what we did is we
created something called Common, right? So Common is everything
that all these agents use. Secrets, all the outputs, all the variables, everything about helm
and things like that. They all have it. So once we put it into Common and
we symlink it to the agent itself, all the agents have the feature,
we don't need to redefine them, we wanna use the, the dry, which is
don't repeat yourself convention, however, every agent is not configured
the same way, right? So what do we do? Each of the agent
has its own sets of files as well. So if a particular thing
is needed for this agent, then we can define that
file and put the required features or configuration for
that agent into that file. And then we also gave them the
ability to override whatever is in Common with the Terraform
features called Override by appending the underscore
override into the file name. And that will override whatever
that we have defined in Common. So this is how we structure
our agent under Common. Everything you see in green there,
are shared between all agents, right? We symlink them into the agent
itself, which is in purple. You can see the only thing
is we name it differently. I give it a Common name in
front. Terraform doesn't care what the file names are or whatever.
It can calculate everything, every file in a folder and create
an execution plan from that. So as long as the file names are different
it will just consume them all and create an execution plan and run from
there. And then we can see the date, the files n black there is
specific to that particular agent. And then the variable override or whatever
underscore override is to override whatever we created in Common. And this is another
screenshot of the other agent, like logs agent and traces agent as well. So that is how we design our agent module to satisfy the second
requirements, which is usability, simplicity extensibility, manageability, as well as composability. And with that, I will pass it over to Raj to talk about
synthetic monitoring as code as well. Thanks Chung. So as Chung mentioned, we are part of the SRE
team. So at LiveRamp, one of our main goal as SREs is to
make it easier for our engineering team to adopt best practices. And
this is not always an easy task. So on one hand, you have engineering teams that do not
really have the knowledge on all the internal components, and that makes up the infrastructure
for a proper observability stack. On the other hand, you
realize that different teams, they have different priorities, so they don't want to know how to
authenticate a task or any particular like Slack channel or Pagerduty
integration with Grafana. They just want to know, or they
just want to code their application, have all the resources they need to
create synthetic checks or alerts or dashboards, and get alerted when something
goes wrong with their application. As simple as that. So that's why we invested
a lot of time and resources to create the tooling
necessary for many teams to get their applications monitored
in less than a single day. So Chung already spoke about how
easy it was for our engineering team to collect metrics and export to
Grafana Cloud. So same experience, we want to give to engineering
team when we create synthetic checks or any
other observing components. So let's talk about synthetic monitoring. So we know synthetic monitoring
offers insight into the behavior of any service from an external perspective. It accesses the availability, performance and correctness of a service. So the targets can be a
simple URL or it can be a website URL, I mean, or it can
be a server you want as well. So for an example you wanna
check out grafana.com, whether it is available or not. So we
can set up synthetic monitoring for that. And in Grafana Synthetic Monitoring, they're even providing
the SSL cert expiry also, which is great. So let's talk about more
on the challenges part. So when we're exploring
the synthetic monitoring, we identified that there are a
lot of challenges for our team, and those became our requirement
as well. So let's see, what other challenges were there? So we have like lot of teams
and they're in a lot of regions, and each team manages multiple endpoints. Standardization. We seek to establish standards
for creating synthetic
checks that are easy for the engineering team so that
they can easily follow too. Ui not preferred. So
as a company and team, we prefer to employ infrastructure
as code approach whenever feasible, rather than relying on
UI-based methods. And the last, we wanna make recovery faster.
So in case of any disaster, you must ensure safe recovery
procedures are in place. So let's see what we have done
to work on these challenges even for our engineering team to make
their life easier so that they don't have to code a lot or they don't have to
know a lot of components. So Grafana, they have really good support. Good Terraform support
for synthetic monitoring. So what we have done, we have created
all these modules for synthetic checks, which use the Terraform
or Grafana-based Terraform modules. And if you see on the right, so the engineering team, they have to just provide minimal
information like job, target, methods, probes, and they'll just create a pull request and boom,
they have the synthetic check created. So it's like very easy for engineering
team to just supply whatever they actually need. And behind the scenes, all the the complexities -
we are taking care of that. So secondly, even to further expedite
the process for engineering team, we have implemented a make file script. So this script prompts for a team name, and ultimately it'll generate
the folder structure. Which will have all the necessary files. So engineering team doesn't have to
worry about all the supporting files required. So you can see an example wherein we
have given the team name as DevOps, and what it'll do is it'll
create the folder DevOps, and then it adds the required
files. And with that, we have DevOps_prod.tf, which will actually have
the implementation part. I mean the endpoints what the
DevOps team they had to provide. So it's very simple. I
mean that's the reason, that both strategies make our
engineering team work very simple. So when we are creating
the synthetic checks, it is essential to validate the endpoints, either using public probes or
private probes depending upon the service functionality.
So probes, what is probes? Probes are black box agents, which are actually responsible
for executing the configured
checks on a specific target, as I mentioned, like
URL or any service endpoints. So public probes, they're
already provided by Grafana, but there are some internal endpoints
which are required to be validated from inside the shared VPC. So for
that, we need private probes. So when we are like checking it out, we
find out we have a lot of shared VPCs, so we need lot of private
probes. So what we did, we have actually like modeled even the
private probe functionality as well. So teams are only required to
provide the minimal information. So you can see here, they're just
providing source, environment, region, and then how many instances of the probe they need, and they'll
just create a pull request. And then the probes are already there. So they have provided two instances
and then two probes are there. So behind the scenes, I mean, if
you see for the engineering team, it's like very simple, just provide
some information. But behind the scenes, we are actually doing a lot of stuff, which is creating the API tokens. We create the probe in the Grafana Cloud, and then we deploy the
synthetic agent on the cluster, which communicates to the probes and
provides result. And that it comes online. So now let's move a little
bit from service endpoint to k6 browser test. So we aim to conduct basic browser
test and perform assessment on services using Grafana Cloud k6. So what we did: we devised a customized
approach for creating k6
browser test and scaling Chrome jobs as we didn't have
any Terraform solution. So what we did to achieve this, we operate for GitHub action
workflows as it offers greater flexibility and automation capabilities. So we established our
foundational GitHub repository accessible to all the teams who
want to create and run tests on the Grafana Cloud k6. So engine team, they have to just provide
the JavaScript file, which contains the actual functionality
of the browser test. Behind the scenes, we are
using the GitHub Actions. And what it'll do is if
we have a pre-commit hook to automatically generate
the workflows and which will have exuding periodic execution also. So these workflows actually
execute the k6 cloud on command, and it creates the browser
test in the Grafana Cloud k6, as well as all the information
with what was required, like metrics, all these things
will be available in k6. And furthermore, they can even configure alerting based
on what all the the information or I would say the metrics which
are exposed by k6 to have like enhancing, like the proactive monitoring and
then even the response capabilities. So now let's actually see
what exactly we have done. So here we can see the actual code. So we have the browser test
wherein actually the team will be creating the JavaScript file. So as
soon as they create the JavaScript file, we have a pre-commit, which
is inside the hooks folder, and that script will create
the workflow file for each test. So on the
right side of the screen, if you see we have the code or I would say the
template which is created while this pre-commit. So it is using the k6 base workflow file. And
it uses even the file, which was added by the developer, and it take yourself even
scaling the job also. So if you talk about the base
workflow file that actually contains the k6 cloud run action, which actually executes and
creates the browser test in Grafana Cloud k6. So again, just want to highlight
that the engineering team, they don't have to worry
about a lot of stuff. They have to only create the
browser test script and automation behind will take care of all
the things, what was required, and it'll run periodically cloud k6. So very easy for the engineering
team to set up. Next. Now, let's talk about another
important observability component, which is alerting. And as you know, the contact points and
the notification policies, they are the pillar for alerting. So for alerting as well, we want to make a better experience
for the engineering team. So we would like to be consistent
in our approach. So what we've done, we provided the make file script
so that automatically it'll create the folders and it'll copy all
the required files automatically. Also, we want to provide the engineering
team a very simple structure. So that they have to just
provide minimal information and it'll take care of creating contact
points, notification policies, all the stuff. So team can just
simply list all their contact points. So it can be like Slack channels or
emails and PagerDuty - all these things they can just add as a list. You can see inside the local on the top portion. And it'll automatically
create all the contact points, and they don't have to worry about all the things which is
happening behind. I mean, like authenticating the
contact points with Grafana. Or even they don't have to worry about
creating the web hooks or any other tokens which was required to set it up. So team will just give this minimal
information and it'll be be right there. The same way for
notification policies as well. So we have default notification policies, which will have the label as team, and it'll send all the the notifications
to that particular Slack channel. And they can even define
the child policies. Which can have something
specific to severity: critical and that they want that
to be sent to the high priority PagerDuty that will be done. So all this information is there. In addition to the contact points and
notification policies, we have even customized the template,
the message templates. So if they want to change
the message templates, they can change it or they can use
the default template that is provided by the module. And
usually like maximum team, they uses the default ones.
And in addition to that, even they can create the mutes, so over the weekend they don't want
any pager for any particular alert. They can mute it. So all these things
are done inside the Terraform project. So when we talk about like, creating
all these components via code, it offers a number of advantages that
enhances efficiency, scalability, and reliability. So let's see,
like what advantages? We got it. First - Automation. So using code to configure Grafana
components automates repeated tasks. Which reduces the time and the effort
required for setup and maintenance. So the team, they have to just focus on the strategic
activities where they wanna do it rather than all other stuffs. Consistency. So code-based configurations
ensure consistency across different environments and deployments. So this reduces the risk of errors
that are actually very common in manual configurations. Version Control. So by defining Grafana configurations as code, you can leverage the
version control system like Git. So this provides a
historical record of changes, facilitates all the, I mean, in case you want to like move back
to the previous configuration, you can do that even, it'll help in tracking who made
the changes and when they made it. Scalability. So configuring
Grafana via code, it simplifies even the
process of scaling monitoring solutions as your system grows. So you can easily replicate configurations
across multiple environments and/or even a different
geography region as well. So and the next one is
Reduce Human Errors. So automating the configuration of
alerts and notifications minimizes the potential for human errors, leading to more reliable monitoring
system and faster response time. And last but not least, Disaster
Recovery. So, I mean, this is very, very important. With all the
conversions stored as code, it's easier for backing up and restoring
configuration and replicating them in disaster recovery scenario. So this ensures continuity of monitoring
capabilities in case of system failure. So I mean, we have tried our
best to minimize the work, even I would say, like
easier for engineering team. And we believe we did a better, or I
would say a good job in doing that part. And I think, the engineering team, they, they're quite happy with whatever
work we have done. So with that, I'll pass back to Chung
for a final closer. Thank you, Raj. So looking forward. We started this journey
about a year ago, right? So Alloy wasn't available, Adaptive
Metrics wasn't available. Adaptive Logs wasn't available, right? So we had to come up with
something to accommodate or make it easier for our engineering
team as well as us reducing our toil a little bit, right? So with Alloy and other adaptive
features and ML and AI,. we're looking forward to adopting those
new features, especially in Alloy, where configuration can be
pulled from HTTP or Git. So we no longer have to manually or have to apply the changes
that we make to the agent module using Terraform. Because right
now, if we make any changes, the team have to still have to apply
those Terraform states into the cluster or into Grafana Cloud. So that
is how, that's what we did to, to meet our two objectives of
cost minimization as well as compliance, as well as usability. And I would like to thank Daniel
and Lisa for helping us with this presentation and our CSM, Matt Talarczyk for being
our voice at Grafana. Thank you everybody for being here.

