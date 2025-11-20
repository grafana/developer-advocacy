# Inside USA TODAY&#39;S Observability Stack for Breaking News Scale with Grafana Cloud

Published on 2025-11-17T21:52:42Z

## Description

Discover how Gannett (USA TODAY) ensures website reliability at breaking-news scale using Grafana Cloud observability. Senior ...

URL: https://www.youtube.com/watch?v=usMNFVJXGRg

## Summary

In this video, Joseph Kregloh, Senior Manager of the Cloud Engineering team at the newly rebranded USA Today Co, shares his extensive experience in IT and the company's transition to using Grafana for cloud monitoring. He recounts the origins of the partnership with Grafana, which began at a cloud conference, and details the evaluation process that led to its selection. Joseph discusses challenges faced during vendor management, user permission management, and the importance of infrastructure-as-code, particularly using Terraform for managing Grafana configurations. He highlights the initial setup, onboarding, and integration of Grafana with external systems, as well as the implementation of alerting and on-call solutions. Throughout the presentation, he emphasizes the significance of effective user roles, clear documentation, and adaptability in monitoring strategies, ultimately concluding that the foundational work with Grafana has positioned the team to handle future requirements efficiently.

## Chapters

Here are 10 key moments from the livestream along with their timestamps:

00:00:00 Introductions and personal background  
00:02:30 Overview of Gannett and its rebranding to USA Today Co.  
00:04:15 Beginning of the partnership with Grafana  
00:06:40 Challenges in vendor management and user management  
00:09:00 Importance of user roles and permissions in Grafana  
00:12:15 Implementation of infrastructure-as-code with Terraform  
00:15:30 Transitioning to Grafana: initial setup and onboarding  
00:20:00 Monitoring usage and setting up alerts for metric ingestion  
00:24:15 Integration with external systems and documentation efforts  
00:28:00 Introduction of IRM (Incident Response Management) and on-call solutions  

Feel free to refer back to these moments for specific topics discussed during the livestream!

# Introduction

Let me start off by introducing myself. My name is **Joseph Kregloh**, and I've been passionate about technology since the early days of the internet. It all started back with the Ford 86 and a 56K modem that my dad had. Fast forward about 20 years, and I've had the opportunity to wear nearly every hat in the IT world—from database developer to PHP programmer, Perl programmer, administrator, CI admin, DevOps engineer—you name it, I've done it. 

For the last 8 years, I've been part of Gannett, and I currently serve as the Senior Manager of the Cloud Engineering team. It's been an incredible journey, and I've been able to work alongside a lot of talented individuals, facing new challenges every day. Since you're getting to know me a little bit, I'll share a little something about myself: my favorite hobbies include home automation, working on cars, and woodworking. So, if you ever want to talk about rebuilding a Ford 429 engine or anything tech-related, please feel free to look me up on LinkedIn.

## About Gannett

A little bit about Gannett: we are the leading media, digital, and marketing company dedicated to empowering communities across the nation and locally. Through the USA Today Network, we reach about **200 million unique visitors** a month, and with Newsquest in the UK, we deliver essential journalism and digital experiences. Our local IQ brand offers innovative marketing solutions for small and medium-sized businesses, and we are committed to providing high-quality, unbiased content that helps audiences and businesses connect and thrive.

A change that I didn't get a chance to put in the slides because it just happened yesterday is that we are no longer Gannett; we are now known as the **USA Today Co**.

## Partnership with Grafana

Our partnership with Grafana started the way many great partnerships begin—late night at a bar. While attending a cloud conference, one of our colleagues brought along their Grafana representative, and the conversation quickly turned into, "What does your monitoring setup look like? Let me tell you a little about the open observability cloud solutions that Grafana has to offer." 

As fate would have it, about 6 months later, we were in need of a new cloud monitoring platform. We evaluated several vendors, arranged reference calls, and held meetings to determine which one best fit our needs. Grafana consistently received the strongest feedback. Their team was responsive, flexible, and able to meet all of our requirements. We launched a proof of concept in short order, with a clear goal of transitioning to Grafana as soon as possible.

Over the years, I've worked with many vendors and onboarded many of their tools. Challenges are often the same, regardless of vendor. With Grafana, I was committed to perfecting vendor management, particularly as it relates to observability tools. Common issues can arise early or sometimes even years later. Learning from our past challenges, we set out to improve and prevent any future issues.

## User Management Challenges

User management can get messy. It's not always a customer's fault; often, users are grouped together by teams or organizations, making it difficult to restrict access or manage specific group permissions. Many vendors still lack SCIM implementation, which complicates the onboarding and offboarding of users. Even after SCIM implementation, nobody ever goes back and cleans up old users.

With SAML integration, user provisioning is usually one-way—the user is added, but removing them often lacks an automatic process. It's critical to set up proper user roles and permissions from day one. Start with the essential roles: **admin** and **users** at a minimum. Restrict admin to a single team if possible. Use infrastructure-as-code to manage permissions so you can review any changes and reset configurations that may have been done manually from the console. As users become more familiar with the system and business needs evolve, be sure to adjust permissions accordingly.

## Dashboard and Alert Management

For dashboards and alerts, nothing bothers me more than "Bob's alerts," testing dashboards, or production uptime alerts labeled "Do Not Touch." As we all know, developers are the best at coming up with names. With dozens of development teams, dashboard clutter is inevitable. Some dashboards and alerts may be important to a specific team, while others may not care about them. This is where naming and metadata become really important. 

I've seen SSL and Synthetics alerts going off for years, only to realize they were pinging an IP address that isn't ours. We're essentially giving them uptime checks. Dashboards that trigger on generic data may look busy or important, but often they're just forgotten junk. My personal favorite is the failed alert that has been going off since 2017, in hopes that somebody will see it and eventually revive that old WordPress site.

## Infrastructure-as-Code and User Permissions

Infrastructure-as-code is essential for our team. Whenever we start a new project, my first question is, "How can we Terraform it?" This is quickly followed by, "How can we automate this?" With Grafana, we've applied Terraform to every aspect of management, from stacks and user roles to teams, data sources, plugins, synthetics, and more. This approach enables us to collaborate more effectively; changes undergo peer review, and knowledge is shared across the team instead of being siloed with one individual.

Additionally, we maintain a stable version of our configuration, which can easily detect drift. Our external auditors appreciate this transparency, and personally, I find it much easier to look at our environment's configuration-as-code than to navigate through the user interface.

One important lesson we've learned is the value of carefully managing user permissions. While it may be tempting to onboard a user and give them admin editor permissions for self-management, this can quickly lead to unintended consequences. With Grafana, our default permission is **viewer**. We've established three custom roles: **admin**, **developer**, and **IRM**. You might wonder how these roles are set if everyone becomes a viewer by default. We assign permissions to roles at the group level, and group membership is managed through Active Directory—one custom role per group. When a user is assigned to that group, they are granted the role. These custom roles are maintained with Terraform using simple JSON to define the permissions for each role. 

The reason we use JSON is that it is easy to read, and Grafana's API already returns the permission data in JSON format, so we just copy and paste it. When a user requests access to Grafana, the process is straightforward. They fill out a form that collects basic information, like the user's name and their organizational group. If the user needs access to an existing group, we just add them to the appropriate AD role group. Single sign-on (SSO) is then automatically added to the user, making it quick and easy. 

If a new group is required, we first provision it. Terraform is our tool of choice for this. While this isn't Terraform, it's actually YAML because it's much easier to automate with YAML than with Terraform. In our case, the Terraform module takes in the YAML information and provisions the new group. If you don't want to automate it, all you need to do is open up a Pull Request with five lines of code, and you have a new group.

The YAML contains five entries: 
- **Name**: the name of the group displayed in Grafana.
- **Email**: the point of contact associated with the group's configuration.
- **Vault Path**: if anyone's not familiar with Vault, it is a secrets engine; when this value is populated, the code automatically provisions a service account within Grafana and provides the API token to that team through Vault.
- **AD Role Group**: the role group to match the user when they log into Grafana.
- **Custom Role**: one of the three roles I previously mentioned.

By implementing namespacing, custom roles, groups, and teams, we've achieved true traceability and ownership within Grafana. Assigning roles at a group level rather than to individual users enables us to control where dashboards and alerts are placed in Grafana. To avoid inevitable clutter, users are restricted to creating dashboards and alerts only within their group's designated folder. This structure makes it easy to identify responsibility. When an application is eventually shut down, it's immediately clear which team owns it in case there are any remaining ping alerts or dashboards that are just going nowhere. This clarity streamlines cleanup and accountability across the organization.

## Transition to Grafana

Our transition to Grafana was fast-paced. After the contract was signed, we had about three weeks to onboard everyone in the company, which meant my team only had one week to do it. We began our journey in sandbox clusters. Initially, we wanted to send data out to multiple endpoints, so we chose to start with OpenTelemetry deployment. This meant we intentionally sent metric and trace data to three or four different endpoints, allowing teams to experiment and determine what would work best for their needs. 

After some time, we refined the approach by separating each exporter, so data would only go to one endpoint, which was the one that the team preferred. Most teams went with Grafana, while one or two teams wanted to stick with GCP. To manage data volume, metric sampling was enabled to prevent ingesting all data. If a team requires more than a 70% sampling rate, they can deploy their own OTel collector in their namespace.

Our setup is as follows: standard Prometheus is running in its own namespace and handles Kube State Metrics and node-exporter. The Grafana agent consumes metrics from Prometheus and OpenCosts. Logs are handled by Loki for annotated deployments, and finally, OpenTelemetry is in its own deployment, allowing us to override exporters or for teams to override configurations on their end.

On the second day, we deployed Grafana to all our GKE clusters and quickly realized our mistake: we were exceeding our metric ingest quota. Upon reviewing the clusters, we discovered that most of our production clusters had multiple KSM instances and Prometheus. Grafana was doing its job by grabbing all the metrics it could find, including remnants from previous monitoring tools and some oversight on our end. 

As mentioned earlier, we prefer to run our own independent Prometheus installation because every monitoring tool out there wants to install its own version. We ensured Prometheus was running KSM and node-exporter, ingesting only the metrics we actually needed. The Grafana agent was pulling those metrics from the Prometheus namespace. By the end of the day, we redeployed and brought our metric ingestion back under control.

## Monitoring and Alerts

Next up, our top priority for day three was monitoring our usage and setting up alerts. As much as Grafana encourages usage, exhausting our total metric ingest quota in just one week would not sit well with our finance team building on the billing dashboard. We adapted key queries to track our consumption and set up alerts to notify the team whenever we exceeded our monthly quota for any service. These alerts were, of course, managed with Terraform, and we periodically adjusted them as our needs grew or shrank. We implemented these alerts about two years ago, and they have been working reliably ever since.

Most recently, Grafana introduced **Usage Alerts**, which gives teams full visibility and observability costs with out-of-the-box billing dashboards and proactive usage alerts. This helps us stay ahead of spikes, forecast future usage, and optimize metrics and logs to avoid waste. While I can't take credit for what Grafana did, I wonder if they took any inspiration from my dashboards.

On the fourth day, we slowed down the pace a little and integrated Grafana with our external systems. Our first external data source was GCP Cloud Monitoring, allowing teams to merge their Grafana metrics with GCP metrics. Next, we set up standard alerting endpoints like Slack and Microsoft Teams, along with incoming and outgoing webhooks. Finally, on the last day, our focus was on ensuring thorough documentation and establishing internal procedures. The Grafana Professional Services team did an excellent job providing training and resources to our teams. We published guidance in our internal blog, including where to find more information, support, sample code, and alerts to get teams up and running.

## Rollout and Monitoring

After a long and hectic week, my team finally put our pencils down and waited for the weekend to pass. Two days later, on Monday, teams were ready to start using Grafana's services, migrating their applications, setting up alerts, and transitioning from the legacy monitoring platform to the new one. It had been a long weekend, but as Monday arrived, we were prepared for the next chapter. And nothing happened. No alarms, no issues, no reports of, "Hey, this doesn't work." It was a pretty uneventful week.

We encountered a handful of access issues for teams and users that we had missed. A few users wanted to explore additional areas of Grafana, so we adjusted permissions accordingly. Finally, we handled some support questions, but overall, the rollout was remarkably smooth. Over the next few weeks, we closely monitored our usage. A month later, we had established a baseline and adjusted our alerts for consumption accordingly.

During this period, we reviewed and enabled **Adaptive Metrics**. Leveraging Adaptive Metrics and the cardinality dashboards helped us reduce overall consumption, and we even found a team that was inadvertently inflating our cardinality. Adaptive Metrics is just one component of the broader Adaptive Telemetry suite, which includes Adaptive Logs, Adaptive Traces, and Adaptive Profiles to intelligently classify, aggregate, drop, or sample low-value telemetry while maintaining full visibility and cutting costs.

## The 2024 Presidential Elections

Then a few months later, our biggest day in news arrived. You may have heard about it: the **2024 presidential elections**. As a news company, this is one of our biggest nights, and it is critical that we are up and running without any issues. Although we had our own internal load testing tools, we wanted to go the extra step and test under real-world conditions. We looked at **k6**, which brings performance testing into the observability stack. It's developer-friendly, scalable to millions of users, and supports modern protocols like HTTP, gRPC, and WebSocket.

With Grafana complementing our existing tools, we were able to scale up our clusters and identify any weak spots in our APIs or front ends. Despite having no prior experience with k6, we had it up and running in about three hours, and over the next four days, we experimented and tested using k6, managing to spend only a couple of hundred bucks.

## On-Call Solution

About a year later, a new need emerged within the company. Our contract for our on-call vendor was coming up for renewal, and my manager approached me and said, "Hey Joseph, can you take a look at what's available these days for an on-call solution?" I assured him I would get right on it, but in reality, I just went back to my desk and looked busy for two weeks. Eventually, I came back and said, "Hey boss, we can use Grafana. They have an on-call solution called **IRM**. No need to go through procurement because we are already giving them money for other stuff, and it would allow us to consolidate with one vendor."

Incident Response Management unifies alerting, on-call, and incident workflows in one place, integrated directly with the observability data. Teams can collaborate, document, and resolve issues faster, all with AI-powered summaries and a flexible pay-as-you-go license. He responded enthusiastically, saying, "Joseph, you're the best employee that I have. I know I just gave you a raise, but here's another one." Or at least that's how I remember it.

On day one, we were already familiar with alerting, so the main task was just setting up on-call rotations and configuring incident triggers within Grafana. With the integrations to Slack, Microsoft Teams, and webhooks already in place, half of the work was already done. We updated the custom roles to include the IRM-related permissions, quickly implementing these changes with Terraform and introducing our third custom role.

On day two, our account team informed us that there was a migration tool we could use to quickly migrate from our old vendor to our new one. To streamline our process, I tested the tool right away. Unfortunately, the tool didn't work as expected. I complained to our account team, but as it turns out, it wasn't really Grafana's fault; it was the old vendor whose APIs weren't very helpful. I modified the tool enough to import team names and got all the important information I needed.

On day four, I created a script to provision the new AD role groups and the corresponding Terraform code to match the important teams, ensuring consistency with the existing Grafana setup. I also assigned the IRM custom roles to all these new groups. Finally, on day five, the Professional Services team organized a demo and showcased all the features that IRM has to offer. After that demo, we opened it up for consumption.

## Conclusion

While I can't predict what tomorrow will bring, I can share where we stand today. When we began our journey with Grafana, our primary focus was on metrics and traces. As our needs evolved, we discovered that Grafana could offer much more. Thanks to the foundational work we did upfront, we were able to quickly provision users and services with the right guardrails in place. Throughout the journey, we expanded our capabilities, adding k6, IRM, and even a bit of logging. 

As we look ahead, I'm confident that whatever new requirements arise, we'll be able to meet them swiftly and effectively. Thank you.

## Raw YouTube Transcript

Let me start off by introducing
myself. My name is Joseph Kregloh and I've been passionate about technology
since the early days of the internet. It all started back with
the Ford 86 and 56 K modem that my dad had, and then fast forward about 20 years, I've had the opportunity to wear nearly
every hat in the IT world-from database developer to PHP
programmer, Perl programmer, administrators, CI admin,
DevOps engineer-you name it, I've done it. For the last 8
years I've been part of Gannett and I currently serve as the Senior
Manager of the Cloud Engineering team. It's been an incredible journey and I've
been able to work alongside a lot of talented individuals with
getting new challenges every day. So since you're getting
to know me a little bit, I'll share a little
something about myself. Favorite hobbies: home automation, working on cars and woodworking.
So if you ever want to talk about rebuilding a Ford 429 engine
or anything tech related, please feel free to
look me up on LinkedIn. So a little bit about Gannett.
Gannett is the leading media, digital and marketing company dedicated
to empowering communities across the nation and locally through
the USA Today Network, we reach about 200 million unique
visitors a month and Newsquest in the UK. We deliver essential
journalism and digital experiences. Our local IQ brand offers innovative
marketing solutions for small and medium sized businesses, and we are committed to empower
to providing high quality, unbiased content that helps audiences
and businesses connect and thrive. A little change that I didn't get a
chance to put in the slides because it just happened yesterday.
We are no longer Gannett, but we are known now as the USA Today Co. Our partnership with Grafana started
the way many great partnerships start...late night at a bar. So while attending a cloud
conference, one of our colleagues, they brought along their Grafana rep, and the conversation quickly turned
into "what does your monitoring setup look like? And let me tell you a little
about the open observability cloud solutions that Grafana has to offer".
And then as fate would have it, about 6 months later, we were in need
of a new cloud monitoring platform. We evaluated several vendors,
arranged reference calls, meetings to determine which
one best fit our needs, and then Grafana consistently
received the strongest. Their team was responsive, flexible, and
able to meet all of our requirements, and we launched a proof of concept
in short order with a clear goal of transitioning to Grafana
as soon as possible. Over the years I've worked with many
vendors and onboarded many of their tools. Challenges are often
the same, regardless of vendor. With Grafana, I was committed to
perfect the vendor management, and particularly as it relates
to observability tools, common issues that can arise. They show up often and early, but sometimes they can
show up years later. So learning from our past challenges
we set out to improve from the past issues and prevent any future ones. User management can get messy.
It's not always a customer's fault. Often users are grouped together by
teams or organizations and it makes it difficult to restrict access or
management to specific group permissions. Many vendors still lack SCIM
implementation that makes it difficult to manage
onboard and offboard users. And even after the SCIM
implementation is made available, nobody ever goes back and
cleans up those old users. With SAML integration, user provisioning is usually
one way the user is added, but removing them, there is no
really automatic way of doing that. It's critical to set up proper user
roles and permissions from day one. So start with the essential roles: admin and users at a minimum, restrict admin to as a
single team if possible. Use infrastructure-as-code to manage
permissions so you can review any changes and reset configurations that may have
been done manually from the console. As users become more familiar
with the system and business needs evolve, be sure to adjust
your permissions accordingly. For dashboards and alerts, nothing
bothers me more than "Bob's alerts", testing dashboard or production
uptime "Do Not Touch". As we all know, developers are
the best at coming up with names, with dozens of development teams, dashboard clutter is inevitable
with some dashboards and alerts that may be important
to a specific team, but others they may not care about it. So that's where naming and
metadata is really important. I've seen SSL and Synthetics
alerts that have been going on for years and years. Only when somebody
had a chance to look at it, we realized that it's actually pinging
the IP of a company that is not ours. We're giving them uptime
checks essentially. And then dashboards, especially if they're
triggering on generic data, they may look busy or important or used, but often they're just forgotten junk. And then my personal favorite
is the failed alert that's been going off since 2017 in hopes
that somebody will see it and eventually revive that old WordPress site. Infrastructure-as-code is
essential for our team. Whenever we start a new project, my first question is "how
can we Terraform it?". Quickly followed by, "How can we
automate this?". With Grafana, we've applied Terraform to every
aspect of management from stacks, user roles, teams, data sources,
plugins, synthetics, and more. This approach enables us to
collaborate more effectively, changes our peer review and knowledge
is shared across the team instead of siloed with one individual.
Additionally, we maintain a stable version
of our configuration, which can easily detect drift. Our external auditors really
appreciate this transparency, and personally I find it a lot
easier looking at our environment's configuration-as-code than navigating
through the user interface. One important lesson we've learned is
the value of carefully managing user permissions. While
temping to onboard a user, give them admin editor
for self-management, this approach can quickly lead
into unintended consequences. With Grafana, our default
permission is "viewer". We've established three custom
roles: admin, developer, and IRM. And you might wonder how these custom
roles are set if everybody becomes a viewer by default. The answer is we assign the permissions to roles to groups, and group membership
is managed through Active Directory, one custom role per group. And when
a user is assigned to that group, they are granted the role. These custom roles are of course
maintained with Terraform. We use simple JSON to define the
permissions for each role. And the reason we use JSON is because
it's easy to read and Grafana's API already returns the permission data in
JSON format, so we just copy and paste. When a user requests access to
Grafana, the process is really simple. They just fill out a form. The form collects basic
information like who's the user, which organizational group they belong to. If the user needs access
to an existing group, we just add them to the
appropriate AD role group. Single sign-on (SSO)is then
automatically added to the user, and that's quick and easy.
If a new group is required, then we must first provision it. The Terraform is our tool of choice. As
you can see on the screen here, this, it's not actually Terraform, but it's YAML. It's YAML because it's a lot easier
to automate with YAML than it is with Terraform.
And in our case, the Terraform module takes in the YAML
information and provisions the new group. If you don't want to automate it, all you need is to open up a Pull
Request with 5 lines of code, and you have a new group. As it stands, the YAML contains 5 entries. Name, which is the name of the
group being displayed in Grafana. Email, the point of contact of that email also
assigned to the group's configuration. Vault Path, if anybody's
not familiar with Vault, it is a secrets engine, and
when that value is populated, the code automatically provisions
a service account within Grafana as well and provides the API token
to that team through Vault. AD Role Group, is of course, the role group to match the user
when they log into the Grafana. And then the Custom Role is 1 of
the 3 roles I previously mentioned. By implementing namespacing,
custom roles, groups and teams, we've been able to achieve true
traceability and ownership within Grafana. Assigning roles at a
group level-rather than to individual users-it allows us to control
where dashboards and alerts are placed in Grafana. To avoid
that inevitable clutter, users are restricted to
creating dashboards and alerts
only within their groups designated folder. The structure makes it easy
to identify responsibility. When an application is
eventually shut down, it's immediately clear which team owns
it in case there are any remaining ping alerts or dashboards
that are just going nowhere. This clarity streamlines cleanup and
accountability across the organization. Our transition to Grafana was fast
paced. After the contract was signed, we just had about 3 weeks to get
everybody onboarded in the company, which actually meant that my
team only had 1 week to do it. We began our journey in sandbox clusters.
Initially, we wanted to send data
out to multiple endpoints, so we chose to start
OpenTelemetry deployment. This meant that we intentionally
sent metric and trace data to 3 or 4 different endpoints,
allowing teams to experiment, and they're determining what will work
best for their needs after some time. We refine the approach by
separating each exporter. So data would only go to one endpoint, which is the one that
the team would prefer. Most teams went with Grafana while we had
1 or 2 teams that wanted to stick with GCP. To manage data volume, metric sampling is enabled to
prevent ingesting all of the data. And if a team requires more than 70% sampling rate, they can deploy their own
OTel collector in their own namespace. And our setup is as follows, standard Prometheus is running in its
own namespace and handles Kube State Metrics and node-exporter. The Grafana agent consumed metrics
from Prometheus and OpenCosts. Logs are handled by Loki for
annotated deployments. And finally, OpenTelemetry is in its own deployment, which then allows us to override
exporters or for teams to override configurations on
their end. On the second day, we deployed Grafana to all our GKE
clusters and quickly realized our mistake: we were exceeding
our metric ingest quota. Upon reviewing the clusters, we discovered that most of our
production clusters had multiple KSM instances and Prometheus. So Grafana was doing its job, it was grabbing all the
metrics that it could find. This included remnants from
previous monitoring tools and some oversight on our end.
As mentioned earlier, we prefer to run our own
independent Prometheus installation. This is because every
monitoring tool out there is always going to want to install
its own version of Prometheus. We ensured Prometheus was running KSM
and node-exporter and was ingesting only the metrics we actually needed. The Grafana agent was pulling those
metrics from Prometheus namespace, and then by the end of the day, we redeployed and brought our
metric ingestion back under control. Next up, our top priority for day 3
was monitoring and usage, monitoring our usage
and setting up alerts. As much as Grafana encourages usage, exhausting our total metric
ingest quota in just 1 week would not sit well with our finance
team building on the billing dashboard. We adapted key queries
to track our consumption, set up alerts to notify the team
whenever we exit our monthly quota for any service. These alerts were of course managed with
Terraform and we periodically adjusted them as our needs grow or shrink. We implemented these alerts about 2
years ago and have been working reliably ever since. Most recently,
Grafana introduced "Usage Alerts", which gives teams full visibility and
observability costs with out of the box billing dashboards and proactive usage
alerts. It helps stay ahead of spikes, forecast future usage of AI and optimizes
metrics and logs to avoid waste. Well, I can't take credit
for what Grafana did, but I wonder if they took any
inspiration from my dashboards. On the 4th day, we slowed down the pace a little bit
and integrated Grafana with our external systems. Our first external data source
was GCP Cloud monitoring. It allows teams to merge their
Grafana metrics with metrics from GCP. Next, we set up standard alerting endpoints
like Slack and Microsoft Teams and incoming and outgoing webhooks.
And then on the last day, our focus was on ensuring
thorough documentation, establishing internal procedures. The Grafana Professional Services team
had done an excellent job providing training and help with
resources to our teams. We published guidance
in our internal blog, including where to find
more information, support, sample code and alerts to get
teams up and running. Finally, we provisioned the remaining users and
prepared for the following week when everybody was set to begin actually
using Grafana. So after a long and hectic week, my team finally put our pencils down
and we waited for the weekend to pass. 2 days later, Monday arrived and teams were ready
to start using Grafana's services, migrating their applications,
setting up alerts, transitioning from legacy
monitoring platform to the new one. It had been a long weekend,
but as Monday came, we were prepared for the next
chapter. And nothing happened. No alarms, no issues, no reports
of, "Hey, this doesn't work". It was a pretty uneventful week. We encountered a handful of access
issues for teams and users that we had missed. A few users wanted to
explore additional areas of Grafana, so we adjusted permissions
accordingly. And finally, we handled some support
questions, but overall, the rollout was remarkably smooth. Over the next few weeks, we
closely monitored our usage, but a month later, we had a baseline established
and we adjusted our alerts for consumptions accordingly.
During this period, we reviewed and enabled Adaptive
Metrics. Leveraging Adaptive Metrics, and the cardinality dashboards
helped us reduce overall consumption, and we were even able to find a team
that was inadvertently blowing up our cardinality. Adaptive Metrics is just one component
of the broader Adaptive Telemetry suite, which includes Adaptive
Logs, Adaptive Traces, Adaptive Profiles to
intelligently classify, aggregate drop or sample
low value telemetry, so you keep full visibility
while cutting costs. Then a few months later, our
biggest day in news arrive. You may have heard about it, but it
was the 2024 presidential elections. As a news company, this is one of our biggest
nights and it is critical that we are up and running without any issues. So although we had our own
internal load testing tools, we wanted to go that extra step and
extremely test the real-world conditions. So we looked at k6, which brings performance testing
into the observability stack. Its developer friendly, scalable to millions of users and
supports modern protocols like HTTP, gRPC and WebSocket. We've got Grafana complementing
our existing tools. We were able to scale up our clusters
and identify any weak spots in our APIs or front ends. Despite having
no prior experience with k6, we had it up and running in about 3
hours, and then over the next 4 days, we experimented and tested
using k6 and only managed to spend a couple hundred bucks. About a year later, a new need
emerged within the company. Our contract for our on-call
vendor was coming up for renewal, and then my manager approached
me and said, "Hey Joseph, can you take a look at what's available
these days for an on-call solution?". I assured him, I get right
on it, but in reality, I just went back to my desk and
looked busy for 2 weeks. Eventually, I came back and said, "Hey
boss, we can use Grafana. They have an on-call
solution. It's called IRM. No need to go through procurement because
we are already giving them money for other stuff, and it would allow
us to consolidate with one vendor. Incident Responsive Management unifies
alerting on-call and incident workflows in one place and integrated directly
with the observability data. Teams can collaborate,
document resolve faster, all with AI powered summaries and
flexible pay-as-you-go licensee". He responded enthusiastically
by saying, "Joseph, you're the best employee that I
have. I know I just gave you a raise, but here's another one". Or at
least that's how I remember it. So on day 1, we were already
familiar with alerting. So the main task was just
setting up on-call rotations, configuring incident triggers within
Grafana. With the integrations to Slack, Microsoft teams and
Webhooks already in place, half of the work was already done. We updated the custom roles to
include the IRM-related permissions, quickly implementing these changes with
Terraform and introducing our third custom role. For day 2, our account team informed us that there
was a migration tool that we could use to quickly migrate from our
old vendor into our new one. Quickly to streamline our process,
I tested the tool right away. Unfortunately, the tool
didn't work as expected. I went and complained to our
account team, but as it turns out, it's not really Grafana's fault. It was this vendor whose APIs
weren't really that helpful. I was able to modify the tool
enough to import team names and got all the important information
that I needed out of it. For day 4, I created a script to
provision the new AD role groups, the corresponding Terraform code to
match the important teams ensuring consistency with the
existing Grafana setup. I also assigned the IRM customer
roles to all these new groups. And then finally on day 5, the professional services team
organized the demo and showcased all the features that IRM has to
offer. After that demo, we open it up for consumption. Now, while I can't predict
what tomorrow will bring, I can share where we stand today. When
we began our journey with Grafana, our primary focus was on metrics
and traces. As our needs evolved, we discovered that Grafana
could offer much more. Thanks to the foundational work we
did upfront we were able to quickly provision users and services with
the right guardrails in place. Throughout the journey, we
expanded our capabilities, adding k6, IRM, and even a little
bit of logging. As we look ahead, I'm confident that whatever
new requirements arise, we'll be able to meet them swiftly
and effectively. Thank you.

