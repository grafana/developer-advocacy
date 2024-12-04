# Actian & Grafana Cloud: The Search for a Customizable Observability Tool | ObservabilityCON 2023

Over the past few years, Actian has shifted from offering a solely on-premises data integration, management, and analytics product to supporting hybrid and multi-cloud environments as well. To keep up, the team needed a customisable observability tool, and found it in Grafana Cloud. Lead Cloud Operations Engineer Suleyman Kutlu will share his team’s journey, starting with metrics and logs, and venturing into load testing, frontend observability, IRM, and more.

Published on 2024-12-03T00:52:07Z

URL: https://www.youtube.com/watch?v=YrilbvWrvLM

Transcript: Hi everybody. This is my first time speaking
to that amount of crowds. I hope I won't faint. . So a short introduction about me. I'm
living in Cork, very close to here. The same weather, the same traffic on the right side based
opposed to what I am grow up. I am . And after all
the work of the week, I'm generally having time
with my family and if the weather helps, do
some garden work and DIY. Today I will talk about who am I
and who we are as a company and our journey with Grafana,
what we had, what we have now, and what we are planning
to do for tomorrow. So, a bit about myself originally from
Turkiye with the new name Turkiye living abroad since 2008 in Netherlands
for 11 years, and then Ireland. I'm in the sector for 30 plus years and six plus years in the Grafana world. I started in long time
ago, 2016, I guess '16-'17, building our own "Grafana
Cloud" in our own private cloud. In the company that I was
working in the Netherlands, we would that separate islands
for our customers at that time. And this is why I am known as
Mr. Grafana in my companies and SNK due to my full name in
the, in the public community. And who is Actian? In a nutshell, we solve the data challenges
for our customers and
enables our customers to have confidence in their
data. We make data easy. The companies generally have
all the data volume growing up, and according to research by IDC, 68% of data available to
enterprises are unused. So Actian is a trusted
advisor when customers need
a smarter approach for their data analytics parts. Actian is now a data and analytics
division of HCL Software and the fastest growing one in the company. Over 600 employees around the globe and servicing mid-market and
enterprise customers, with 95% of customer satisfaction. We have the roots of, with data back to 1970s with the Ingress database developed in UC Berkeley. And then throughout the time we continued an investment in innovation in that area and all the
acquisitions and innovations. Now we have a broad portfolio
of data products that solve challenges for more than 10,000
customers around the globe and in every industry we can think of. This is a short history timeline, starting back in 1970s
with the ingress database in UC Berkeley. And in 2011, we changed the name to
Actian, and now we are a data analytics, data analyst
division of HCS Software. With all that brought number of different data
solutions for customers. What we have yesterday
in our infrastructure
generally we have the virtual machines, a small portion
of it, but mostly, I will say 90% is all
in Kubernetes clouds, Kubernetes clusters among all
three major cloud providers. We have our applications
running and for observability, we have different tools in the
past for synthetic monitoring, for metrics and logs monitoring, and we have different agents
for these different tools. In our clusters, we have almost, we have more than 70
clusters around the all cloud providers. And you know what I'm talking with
that gray boxes in the previous slide, the old tools that we were using, I
don't want to mention the names,  and what we have now, the infrastructure is more or less
the same with a slight difference. We only have one agent
running everywhere and we have LGTM Stack with k6 included. We started our journey with a
simple POC in a Grafana Cloud Free Tier with one cluster from each
provider and one VM to see how things are working with our
infrastructure. And then we have, we were happy we upgraded our tier
to include all clusters and all VMs and the synthetics. And then
we got the Grafana Cloud k6 later into the pictures.
Everything is with a single agent, single tool easy to
maintain, easy to handle, and everybody's happy at the end. Our journey started with April
'22 with Grafana Cloud. As I said, we have two stacks for GDPR purposes. One is for the European Union clusters.
One is non-European Union clusters. We have mainly Loki and Mimir for the metrics and logs, and we
have synthetics. As I said, we added the [Grafana]
Cloud k6 to the picture and end of '22 we decided to go
with Grafana open source. We added Grafana open source to our
picture for non-production clusters to have the same level
of observability and monitoring alerting for our
non-production environments as well. And then we added Tempo
to our open source part, and now the engineering teams and
developers are adding distributed tracing to their codes in order to get tracing
from the development environment, starting from development. And then we added Grafana Faro to the
picture for real user monitoring from the browser-based applications. And engineering teams are performing
a POC to get that into the picture properly. Everything is - both open source and cloud - is
integrated with single sign-on, so everybody can log into any stack with
their rights based on their team and their responsibilities. Before Grafana agent, as I said, we have different agents from other
vendors and we have old cluster had a Prometheus server and Prometheus
operator for their internal observability per cluster and for the
horizontal post scaling link. But then we introduced Grafana
Agent in static mode at the beginning. Main goal is to use same agent and same
configuration everywhere for logs and metrics. So from development
up to production, we have the same level of observability. We develop our own custom Helm
Chart to deploy static mode agent and k6 clusters and k8s sorry, Kubernetes clusters and
Ansible playbooks for the VMs. We have a Harness CI/CD pipeline
to deploy this Grafana Agent static mode to clusters. By nature it is static by name. So the Harness pipeline detects
everything running on the cluster, adjust the graph an agent configuration
properly and then deploy the Grafana Agent. But when you add a new
application or a new workload, you need to redo that in order to
detect it. But in order to do that, you need to adjust your code to detect
that application, adjust configuration, et cetera. Very tedious work to do. And we at, of course, as I said, we have Faro
in the picture as well, but it's not as fast
as we expect. And our, in our journey after this
deployed to everywhere we start to evaluate our options. The Grafana operator
was one of the things, but it's not, it was a no go for us
because at that time, the future of that Grafana Operator
operator was not that clear. And then we met with Grafana flow,
Grafana Agent flow mode, and the river, same goal, everything the same, but
with quite a lot of difference. First, we start to use official Helm Chart from
Grafana Labs without any modification. We are just using whatever
provided by the team. We changed our Harness pipeline to
a simple Argo CD application set. So everything is deployed without in a
customization. It's a dynamic flow mode. Everything is running perfect. And we inspired and
implemented Grfana Agent modules repository with some
minor modifications for our environments. And I want to thank the Professional
Services team for that help during that journey for the implementation of
agent modules and the flow mode. At the end, we have everything deployed. We have everything ready and we
deployed agent flow mode in dev and test environments. Now, teams are working on verifying the
results because of all the naming change, job name change, et cetera, to verify that our alerting
and dashboards are working as expected with Grafana flow as well.
When this is done, we will move to of course up to production And journey continues. Of course, we have our cloud integrations
on all three major cloud providers. We integrated with Grafana Cloud and
Grafana open source with the same way. We have converted our alert
definitions into a code repository, so JSONet for Mimir, Loki based alerts and a
Tereform plan for especially the alerts for the cloud integrations
for the Grafana managed alerts. We have our our synthetics monitoring
for the API endpoint with Grafana and k6 for the browser-based test. There is a minor note here. We evaluated [Grafana] Cloud k6 six and
k6 open source and [Grafana] Cloud k6 pricing model was not that suitable for
us at that time because the browsing based, browser based testing
works only less than a minute. So we choose to go with
the k6 open source. We are running our own
clusters around the globe and running scripts periodically to test our browser-based applications
between all the logging into the application, clicking
screens, et cetera, and ending up at the final page
and to verify we get what we wanted. And now we are evaluating black
box exporters to do the same as synthetics does for production
environment in Grafana Cloud. To do the same with black box exporter
and non-production environments. Probably we will go with
black box of course. And of course journey never stops. And thanks to the announcements
yesterday, it'll continue with a, with a high velocity with all
the new new features added. We have we are working on
converting anything as codes, everything about Grafana configuration
and Grafana resources to be coded in a repo. So nothing
as much as possible, nothing to be done via UI, so it can be repeatable
in all environments and
manageable by everybody via updating the repo. By that I'm
talking about cloud integrations, synthetic monitoring configurations,
alerting configurations, alerting rules, data source definitions, and dashboards, especially for most of
them. We are almost done. Everything is in properly coded into repo. Dashboard part is recently
started with with Grafonnet. We are working on it to
convert our current dashboards
by some simple secreting to Grafonnet and then deploy it
in all the environments via source code. We are planning some trainings for
our engineering and DevOps teams, so they will be able to understand
what is in the code with that, anything as code feature. And they will be able to update when
necessary via standard pull request flow. For example, they may have a new release
with a log record changed, and we are using this in alerting, so they will see that their
environment start to alert for that log record. They'll be able to create a pull
request to update the alerting rule. They will apply it on their environment
and then it'll propagate to production with the release as well. So we don't lose observability
on any environment during that release of that new, new product. And we have our agent and Grafana open source already in automation pipelines,
but not for the k6 open source. We need to work on that. We need to handle upgrading
Grafana open source and k6 open source better. They are updating fast and we are very
slow in upgrading our environments to the latest versions. We are working on, on-call managers and our non-production environment. So engineering teams
will be able to receive alerts for non-production environments, the
event test, especially earlier, and they will fix problem
there before releasing their codes to production. With that on-call manager and
incident response together, we are planning to replace our on-call
solution that we are using today with [Grafana] OnCall
and Incident Response. We are planning to use
[Grafana] k6 for performance, stress and reliability testing and
some quality assurance testing, working on that with the QA team as well. Of course, during that journey we have
our lessons learned on major areas as I listed here. First of all, the Grafana
Agent, we started with static mode, but YAML is hard to read after
a while. In a day or three, you may forgot what, why you coded that regular expression
there with the all parenthesis question marks, stars, et cetera. And River helped a lot on that part.
More human readable, more understandable, and the flow makes you easily understand the way of it's working. With the flow, we had some issues like as, as I said, we implemented Grafana Agent
agent modules repo provided by Grafana Labs, but the modules was used
via Git reading from a Git repository and that hit
our Git providers. We, we had some issues and with
number of calls from all clusters to Git provider and they
start to throtlel our requests for everything. And then we
changed this with a small script, all the modules.git to modules.file
to read it from a config map in the clusters. But overall
agent flow mode is awesome. We had our issues with log based-alerting. We are directly using log
records and Loki in the alerts, but it's better to convert most
of them into recording rules. So we convert them into metrics and alert based on those metrics. It'll be cheaper for us and better
for the Loki side as well for all the environments. With open source parts, we had our share of issues
with sizing, OOM kills, hitting the limits for number
of metrics and number of logs. It's a continuous process to
increase our limits, our sizing, but also we are preparing some k6 tests, stress tests on our Mimir and Loki
in the open source side to properly size our environment for
our clusters and VMs. For k6, as I said, we are very slow
in updating the versions. We are, trying to implement automation
on k6 side as soon as possible. So we will update, we will keep up to date with the k6 side. Yeah, the edit values, of course,
the first major thing is cost. We have a dramatic cost reduction
by moving to Grafana Cloud from other three vendors, but the cost story continues
with Adaptive Metrics we are implementing. We are adapting Adaptive
Metrics in our environment, so removing unused metrics, labels and reducing by
aggregation as we all get the talks about them yesterday and today. Our team is an analyzing the
results of Adaptive Metrics and we will implement the rules very soon. I can show you a sample
output from our environment. We have almost 22 pages
like that, but the first, I mean, this page will be enough
to reduce most of the cost. We are working with the team
to analyze whether we may need these metrics in the near future. Do we have any plans to use them
in a dashboard or alerts? If not aggregate and reduce or even maybe
we will think of removing them at the source from Grafana Agent not to get into environment. The next major edit value
is single pane of glass, one tool for anything and
everything about observability. We don't need to switch between
consoles in order to analyze a crisis or an incident.
We are one single tool. We are preparing our own dashboards from every data source. Another one is observability
from development. We have the ability with Grafana
to implement the same level of observability in every
environment. In the past, it wasn't possible because
of the cost issues. Now we can implement the same level
and development tests and stage and production without any change.
The same code, the same agent, the same level of
observability dashboards. So we can see problems
earlier in development environment and fix it before
going to production with a release. And also this enables a shared
responsibility with the development teams so they can help, they can own the same
responsibility as we are as cloud operations team. They can
update the configurations, dashboards based on their releases
and development environment. And it can propagate up to production with the release. And that's all for the
journey that we had in Actian. And thanks you for listening.

