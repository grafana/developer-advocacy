# How C Spire Migrated Their Observability platform

Published on 2025-09-08T21:03:14Z

## Description

Join C Spire as they share their journey migrating from fragmented legacy observability tools to Grafana Cloud and ...

URL: https://www.youtube.com/watch?v=TSwxBjhCB8Q

## Summary

In this YouTube video, Zachary Sistrunk, a Software Developer III at C Spire, discusses his role on the Systems Integration team, particularly focusing on the implementation of Grafana and Open Telemetry for observability within the company. He explains the challenges faced with their previous monitoring solutions, such as AppDynamics and Splunk, which were expensive and inefficient. Zachary outlines the decision-making process that led to selecting Grafana due to its open-source nature, excellent documentation, and compatibility with Prometheus and Open Telemetry standards. He describes the successful proof of concept and subsequent rollout across the organization's services, emphasizing the benefits of Grafana’s user-friendly interface and the ability to integrate various data sources. The video also touches on the transition from on-premises to cloud solutions for better performance and stability, and future plans to expand Grafana’s use across different teams within C Spire.

# Introduction

Hello, my name is **Zachary Sistrunk**. I work as a **Software Developer III** at **C Spire**. My role is on the **Systems Integration team**, which many of you may know as middleware. We write the services that connect the front-end web and store clients to the backend billing systems, provisioning systems, vendors, and so on. 

I graduated from **Mississippi State University** with a Bachelor's degree in Computer Science, and I've been working at C Spire since I graduated in 2018.

# Middleware Team Responsibilities

As part of the middleware team, we have the largest code base and the most responsibility when things break. As such, **observability** is a major part of our work. In my role, I am the subject matter expert on **Grafana** and **Open Telemetry** for C Spire. This means I assist other teams with their observability solutions, helping them set up their systems in Grafana. Additionally, I have made contributions back to both Grafana and Open Telemetry.

# About C Spire

C Spire is a privately owned telecommunications company located in Mississippi, based out of Ridgeland. We have three lines of business:

- **Wireless**: Provides service to the entire state of Mississippi, as well as Memphis, Tennessee, and the greater Mobile, Alabama area.
- **Home Services**: Offers fiber internet across Mississippi, Alabama, and parts of Tennessee.
- **Managed IT Services**: Provides IT to 47 different states and is the sole provider of VoIP and connectivity for all state universities in Mississippi, as well as the long-distance and internet provider for all government entities in the state.

# Transitioning to Grafana

Before we adopted Grafana, we relied on a variety of different services:

- **AppDynamics** was used to measure our application health.
- **LogicMonitor** was used to monitor our VMs.
- **Splunk** was used for logging.

However, none of these services were satisfactory. AppDynamics struggled with Scala, our primary programming language, meaning we only had JVM metrics and no traces. Both AppDynamics and Splunk were expensive and did not integrate well, making it difficult to diagnose issues without extensive manual digging.

When we removed the AppDynamics Java agent, our CPU usage dropped by 30%. Their support recommendation was to de-instrument our entire code base, which was not feasible. We initially considered fixing AppDynamics ourselves but ultimately decided against it due to the risk of being locked into a specific version.

Our first alternative was Splunk APM, which also disappointed us due to its dashboards and pricing. We considered **Datadog** and **New Relic**, but both were cloud-only solutions. Given a recent major outage with AppDynamics, we were particularly interested in staying on-premises. 

We also looked into the **ELK Stack**, which met our requirements but had a poor user interface compared to Grafana. Ultimately, we chose Grafana because it allowed us to try it for free and was open-source, enabling us to contribute back to it.

# Implementing Grafana

We began by installing the full open-source stack, setting up instances of Loki, Grafana, Tempo, and Mimir. At that time, Pyroscope did not exist, so profiling was not a consideration. We created a proof of concept by updating three to four of our largest services. By using Spring Boot, we could automatically expose a Prometheus metrics endpoint and attach the Open Telemetry Java agent to collect the necessary traces.

During this proof of concept, we configured our Grafana agent instance with standard locations and API paths across our stack, allowing for a generic configuration file that could find all our services. This eliminated the need for unique IDs for every service, simplifying our monitoring setup.

After testing our proof of concept, we automated the deployment using **Ansible**, allowing us to push changes to our virtual servers quickly. Once we gained more experience, we trained other IT teams on how to build dashboards and understand their data, maintaining a support group chat for ongoing assistance.

In under a year, our entire test environment had migrated to Grafana.

# Challenges with On-Premises

Despite our successful implementation, maintaining the on-premises Grafana stack became challenging. It required significant resources, and as we pumped more data into the stack, we encountered stability issues. Expanding the stack was also cumbersome due to our non-containerized environment.

After discussions with our sales team, we explored the option of moving to the cloud. Although we were initially hesitant due to past cloud issues, we were impressed by the features offered in the cloud, such as Application Observability, K6, Grafana IRM, and Fleet Management. 

In terms of cost, while the cloud was slightly more expensive on paper, it was more economical when accounting for the costs of maintaining the on-premises equipment. Ultimately, moving to Grafana Cloud was a no-brainer, and we do not regret the decision.

# Project Timeline

- **January 2022**: Started investigating Grafana.
- **April 2022**: Made the final decision to use Grafana.
- **June 2022**: Completed the full stack installation.
- **July 2022**: Finished the proof of concept.
- **March 2023**: Communicated with the sales team to purchase Grafana Enterprise.
- **July 2023**: Launched Grafana Cloud.
- **2024**: The entire App's Dev department was 95% migrated to Grafana.

This timeline is particularly impressive given we did not have a dedicated project team; the work was done alongside other responsibilities.

# Environment Scale

In our production environment, we manage over a thousand virtual machine and microservice combinations across development, integration, test, and production environments. We have multiple hundreds of virtual machines and microservices, creating thousands of individual services.

With Grafana, we eliminated the need for manual ID grouping and can simply use labels to filter. This has streamlined our alerting process as well, making it easier to diagnose issues.

# Grafana Features

Some of our favorite features in Grafana include:

- **Overview Dashboard**: Displays uptime, CPU stats, memory stats, disk stats, and network stats for our VMs, along with currently firing alerts.
- **Traces**: Provides end-to-end visibility of requests across multiple applications and teams, allowing us to trace issues back to their root cause.
- **Application Observability**: Automatically generates metrics for request error and duration based on traces, providing insights into service performance.

# Future Plans

Looking ahead, we plan to utilize more cloud features, such as **Grafana Asserts** and **Kubernetes observability**. We aim to integrate the JavaScript Grafana Pharaoh Library with our front-end teams for extended tracing into the browser. 

We also plan to expand Grafana to other departments, including our network team, to monitor network stats and alerts. The potential for customized metrics and traces is vast, and I look forward to exploring how Grafana and Open Telemetry can empower our business further.

## Raw YouTube Transcript

So my name is Zachary Sistrunk. I work as a Software
Developer III at C Spire. My role is on the
Systems Integration team, which many of you may know as middleware. We write the services that
connect the front-end web and store clients to the backend billing
systems, provisioning systems, vendors and so on. I graduated from Mississippi State
University with a Bachelor's degree in Computer Science, and I
have been working at C Spire since I graduated in 2018. So as a part of the middleware team, we have the largest code base, but also the most responsibility
when things break. And as such, observability is a very big
part of what we have to be involved in. As a part of my role, I am the subject matter expert on
Grafana and Open Telemetry for C Spire. And that means I help assist
the other teams with their own observability solutions,
getting them set up in Grafana. And also as part of that, I have made contributions back to
both Grafana and Open Telemetry. C Spire is a privately owned
telecommunications company
located in Mississippi. They're based out of Ridgeland.
We have three lines of business. The wireless provides service to
the entire state of Mississippi, as well as Memphis, Tennessee, and
the greater Mobile, Alabama area. Our home services team provides fiber
internet across Mississippi, Alabama, and parts of Tennessee. And our managed IT services provides IT to 47 different states. It's also the sole provider of VoIP and
connectivity for all state universities in Mississippi, as well as the long distance and internet
provider for all government entities in the entire state of Mississippi. So at C Spire, before we had Grafana, we had a variety of different services. AppDynamics was used to
measure our application health. We had LogicMonitor to monitor our VMs, and Splunk was for our logs. But none of these services
were very satisfying to use. AppDynamics is completely
unable to handle Scala, which is our primary programming
language. So almost all of our stack, the only metrics we had
from it were JVM metrics, and we had no traces at all. Both AppDynamics and Splunk
are very expensive software and they don't connect in any way. We could not jump from
metrics to a trace to logs, trying to diagnose an issue, usually involved us setting timestamps
to the time of an alert to try to find the right thing in the logs. A lot of manual digging. On top of that, AppDynamics, their Java agent, very
poor in performance. When we removed it from our services, our CPU usage dropped by a
full 30%. We knew it was bad, but we didn't know it was that bad. And the support we got from them, just the fact when we asked about the
traces and our inability to see into our Scala services and about
their poor performance, their recommendation was
to de instrument our code, specifically deinstrument
the com.cspire package. But that's the entire code
base. There'd be nothing left. So at first, the first thing we thought about was
trying to fix AppDynamics ourselves. Their Java agent had an API that
we could have integrated with, and we would've been able to manually
instrument the services to add in the traces that we were missing. But we decided against that when
we realized it would lock us to a specific version of the
AppDynamics Java agent. And AppDynamics had just forced us
to move off of our own premises and onto their cloud. So an update to their cloud would've
required us to go through and update every single one of our services to
keep our monitoring in place. It was not feasible and we
had to have a replacement. The first replacement we
actually looked into was Splunk. Splunk APM has application monitoring, but it did not take long to look into it, we were not impressed by its dashboards and it was way too expensive
for what we wanted from it. We looked into both Datadog and New Relic, but they were both cloud only
products and at the time, with AppDynamics, having just had a major cloud outage
cutting off all of our monitoring, we were very interested
in staying on-premises. The last one we looked
at was the ELK Stack. It met all the requirements and
had its own premises version, but in the end we decided not to go
with it because it had a much poor user interface compared to Grafana. So after looking into all of those, we finally ended up choosing
Grafana to go forward with. The biggest draw was the fact that
we could freely try it with its on-premises version so that we could
actually trial it out for a length of time before having to spend any money. That was important to us at the time
because we were still locked in the AppDynamics contract
for another few years. The fact it was open source, we could contribute back to it and
the excellent documentation that they have available, as well as
excellent community support. But the most important thing was
the Prometheus and Open Telemetry standards. We found many, many recommendations saying that
Grafana was the best UI if you use Prometheus and Open Telemetry. And those are the two technologies that
we had very quickly decided we wanted to use. On top of the free tier, we were looking to the future
for when we paid for it. The enterprise plugins
that it had available, we used almost every single one of
them: Oracle Database, JIRA, ServiceNow, GitHub, Salesforce. All of
those are very important business processes that we would
love to have the ability to monitor. And as I said earlier, being able to be on-premises
was a very big draw for us. And lastly, "Looks Good To
Me". We love the naming scheme, not only the fact that it
actually makes a common phrase, but L for logs, G for graphs, T for traces and M for Metrics, you got to enjoy a clever naming scheme. So how we went forward
with implementing Grafana, we first started by installing
the full open source stack. We set up instances of Loki,
Grafana, Tempo, and Mimir. At this time, Pyroscope did not exist,
so profiles were not a consideration, but that is something
we are looking at now. But we then created a proof of concept
by updating three to four of our largest services. So we use Spring Boot, and we were able to update
Spring Boot to just automatically expose a Prometheus metrics
endpoint. And at the same time, we attach the Open Telemetry Java
agent to automatically collect all the traces that we needed. And using
these in this proof of concept, we were able to get our data into
Grafana fairly quickly and start creating dashboards using
real data instead of having
to use a demo environment with stuff that we didn't recognize,
didn't know what we were looking at. At the same time we were
configuring this proof of concept, we also configured our
Grafana agent instance. We have standard locations
and standard API paths across our stack. And thanks to that we were able to
create a generic agent configuration file that was able to find all
of our services without us having to modify every single service
beyond adding the endpoint itself. So one of the big parts of AppDynamics
that was a problem for us was every single service had to have a
unique. And so every single service, anytime we spun up a new virtual
machine or added a new microservice, we had to give it a unique
ID for AppDynamics to be
able to differentiate it. That was not a problem with Grafana. Agent later got migrated to Alloy, and so we updated our config file
accordingly, and we still use that today. After our proof of concept was
fully tested and functional, we configured our automation platform
Ansible to be able to deploy the entire Grafana suite of files
to our virtual servers at once. This included Grafana Alloy,
the OPIS entry Java agent, both of their config files and
later the Open Telemetry extension jar, which led us customize the metrics
and traces that Open Telemetry produce. This Deploy job allowed us to
push out changes in only minutes and we would make a change to
our config to start off the job and within 30 minutes, every single virtual machine we had was
fully updated to the latest version. Once our team got more in depth, we started expanding to
the other teams in IT. We trained them on how to build
dashboards, what the data meant, how to get their data into Grafana and let them poke around to
create dashboards with their data. We held for a little while, there was weekly training sessions with
at least one member of each other team in the department, and we still have a group chat in
our teams where anybody that has questions can ask us to get
help. And at the same time, the systems integration team continued
to expand that proof of concept to the rest of our services. It took, well, there's a timeline slide later, but it took a little while to get all of
our services because we rolled them out in batches. But in under a year, our entire test environment
had been migrated into Grafana. So when we started, we
wanted to stay on-premises. We did not want to use a cloud product. The problem is on-premises is hard. Maintaining a Grafana stack
practically takes an entire full-time position, and that is
a resource that we did not have. As we started pumping
more data into the stack, we started running into stability issues
because it couldn't handle the amount of data we were handing to it. And I know there were probably ways to
configure it to be able to handle it, to tune some config settings,
but at the same time, we were still working other projects
and we were not able to just dedicate days to tuning
the on-premise instances, so we just kept it running
as best as we could. And expanding it was also
difficult because we are not containerized. So having to expand it meant
spinning up a new virtual machine, getting the binaries installed,
getting SSH keys set up, moving the config files, having to modify the config files
on every other server in the cluster to add this new server so
they all know it exists. So we had discussions with our
sales team and they recommended that we move to cloud
and we were hesitant. We had had problems with cloud, but
we decided we'd at least look into it and we were honestly blown
away by what we found. The features that are
made available in cloud are tremendous Application
Observability, K6, Grafana, IRM. Nowadays, Fleet Management, all of these are things that they were
not available even in the paid enterprise version, which is what
we were trying to buy. But they all looked so useful that we couldn't pass them up, and they gave us a price comparison
between enterprise and cloud. I mean the cloud, it was a
bit more expensive on paper, but that paper didn't include the cost
of maintaining the on-premises equipment. Like I said, it required basically a full-time position
If you add a developer's salary on there, cloud was cheaper, but it really was a no-brainer in the
end and we do not regret that decision. So this was our timeline. We started off in January
of 2022 investigating and it only took us three months to
make the final decision to use Grafana and only another two months after
that to have the full stack installed. And our proof of concept was done by July, although we were working on that at
the same time as we were setting up the stack. And after the proof of concept, we continued upgrading our services
through the next nine months. And that's around the time we started
communicating with our sales team to purchase Grafana
Enterprise. A year later, we finally launched Grafana Cloud. Only a year after the proof of concept
systems integration team was fully migrated into Grafana. And then only two years after
the initial proof of concept, the entire App's Dev department
was 95% of the way there. We only had a small handful of hard
to update legacy services left over. And this two year timeline, it's even more impressive when you
realize that we did not have a dedicated project to do this. This was being done by developers
alongside their normal day jobs of other project work, adding new
features to our stack and so on. I'm very proud with the work that my
team and all the other teams in our application department pulled
off in getting all this set up. So to show the scale of our
environment in our production services alone, we have over a thousand virtual
machine and microservice combinations across all four environments, development, integration,
test and production. We have multiple hundreds
of virtual machines, multiple hundreds of microservices. The combined combinations of
those make up multiple thousands of individual services spread
across six separate application development teams. And like I said earlier in AppDynamics, each one of these had to have a unique
ID and had to be manually grouped into applications and tiers. But all that manual grouping goes
away with Grafana's label sets. The ability to define labels and have
the combinations of labels be what you filter on. We have one label for
instance, and one label for service. And then the unique ID is just the
combination of those two labels and we don't even have to configure that
because the instance is pulled from the server's host name and the service
is pulled from the services code. It's just already there. And on top of that, Grafana Alerting allows us
to create a single alert rule that's able to pick up every
single combination and alert when any one of them goes wrong.
And when that alert is fired, those same labels allow us
to know exactly which team it needs to be routed to, which we can route to directly to
their phone through Grafana On Call. It's a much smoother
process of diagnosing and figuring things out. So there's a few more
slides showing screenshots. So I know they're a little
bit hard to see in the here, but this is an overview dashboard
that we've created for our VMs. It's a table that has its
uptime, the CPU stats, the memory stats, the disc
stats, and the network stats. At the top left is a list
of currently firing alerts, and the top right is a list of quick
links to other important pages in our Grafana instance. So
this is our landing page. This is what everybody sees when
they first log into Grafana, and it just shows the quick information
that they can need at a glance. And you can actually see one of
our servers in this screenshot is currently highlighted red
because it's at 90% memory usage. So we know we need to add a few
more gigs of RAM into that service. Java may be convenient, but
it is very memory heavy. One of our favorite parts of moving to
Grafana and one of the big selling points was Traces. Full end-to-end traces powered
through the Open Telemetry Java agent. We get wide visibility, the ability to trace a single request
that goes through multiple applications and teams. This trace in this screenshot
goes through four different teams and I think 12 different
services if I remember correctly. But it's not just wide, it's
also deep inside each service. We can go all the way down and see the
exact SQL calls that we call into the database for the exact RED commands
that are used to retrieve the cache. It's more data than we
ever had in AppDynamics, and it makes it extremely
simple to find exactly how and when something breaks and traces because of Open
Telemetry, they're very customizable. You can integrate your services with
the Open Telemetry API to create your own traces and metrics. But the biggest and most
important part about this is Grafana Cloud's
Application Observability. Application Observability takes those, takes those traces and generates
metrics based off of them. And those metrics give you
request error and duration metrics for all of your services just
automatically based on the actual traces. And you can see them all in
this overview, which again, I know it's kind of hard to see, but we have the nice
little spark lines showing us our request rates, our average
durations, and the error rates. But you can then click into any service, any service at all and see
all those details down to an API by API basis, as well as seeing the upstream
and downstream services from the service you're
looking at. So for example, this screenshot I believe
came from our billing services platform, which upstream
is our customer services, and downstream is our billing system. So if we're seeing slowness in the stack, usually the first place
we look is this service, and 9 times out of 10 it's because
there's slowness coming in from the billing system layer. And we can see that in
both the API durations, the P95 is starting to trend above that upper anomaly bound. And if you look in the
downstream services, you can see that same pattern following
in the downstream service and click down into that and see what's downstream
from it to find the actual root cause of any slowness. This feature was what finally
100% sold us on moving to cloud because this is something
that was not available on-premises. As for what's next for us, we plan on continuing to move forward
with more cloud features such as Grafana Asserts, which is going to be an evolving
on application observability as we are starting the process
of containerizing our services. So we're going to be using
Kubernetes observability, we're working with our front-end teams
to get them to integrate the JavaScript Grafana Pharaoh Library to extend
those traces even into the browser. And we plan on moving
more into Grafana IRM. We already use alerting and on-call, but
there's incident to play with as well. And that has a big chance to integrate
with our ServiceNow instance. We also plan on, as I said earlier, using the open telemetry API to create
custom metrics and traces and these are going to be traces. We have an order processor and we
can see how long it spins in each individual step, and we can add in
an error happened in this step right here and we can generate
metrics from those traces. Our sales data we can insert
into our payment stacks to track payment rates, our account
stacks to track churn rates, all data that would be very valuable
to the business that we can just make available directly from
our applications instead of them having to build reports off
of a database like they do today. And we also plan on expanding
Grafana to more teams outside of our IT department.
At the moment, our network team, they are the team that manages the
cell towers and the fiber system. They are interested in seeing if
there's a way to use Grafana to monitor the network, to get network stats
and alerts when something goes down. That how with managed IT being the only provider of government internet
in the state and with C Spire being, I don't know for certain, but I believe we are the biggest
wireless carrier in the state of Mississippi, those kind of stats, being able to get proactive alerting
on those would be a big deal for our customers. But after network, our reporting teams, the
sales and marketing teams, we can put in the metrics
for payment stats. We can put in the metrics to
show what items sell the best. We can put in metrics to see what kind
of emails we send out so the marketing team can see click-through
rates. There's so much power in how customizable Grafana
and Open Telemetry are, and that's something that I
am really looking forward to, being able to investigate more.

