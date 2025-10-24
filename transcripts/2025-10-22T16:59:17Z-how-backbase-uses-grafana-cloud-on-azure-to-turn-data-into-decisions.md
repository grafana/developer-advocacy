# How Backbase Uses Grafana Cloud on Azure to Turn Data into Decisions

Published on 2025-10-22T16:59:17Z

## Description

Powered by Grafana Cloud, Backbase built a fully automated observability experience. Discover how rapid onboarding, Metrics ...

URL: https://www.youtube.com/watch?v=1vU2ewX25rg

## Summary

In this video, Manu and Andrei from Backbase discuss their digital banking software solutions, focusing on the company's managed hosting and observability services. Manu, the product director, and Andrei, a systems engineer, introduce Backbase's unified banking suite, which streamlines customer acquisition, servicing, and retention for banks. They highlight the importance of customer-centric digital banking and the transition to AI-powered solutions. The discussion emphasizes the technical aspects of managed hosting, including infrastructure automation with Terraform, Kubernetes deployment, and 24/7 monitoring using Grafana for observability. They explore the significance of security, compliance, and the benefits of their partnership with Grafana, which has enhanced their observability capabilities and overall service delivery. The presentation concludes with a commitment to maintaining high service levels for their financial institution clients.

## Chapters

Here are the key moments from the livestream with timestamps:

00:00:00 Introductions by Manu and Andrei  
00:01:15 Overview of Backbase and its products  
00:02:30 Explanation of Managed Hosting capabilities  
00:04:00 Introduction to Backbase's observability platform  
00:05:45 Core value proposition of Backbase's unified banking suite  
00:08:15 Importance of customer-centric banking  
00:09:30 Security measures in Managed Hosting  
00:12:00 Technical aspects of Managed Hosting with Terraform and Kubernetes  
00:15:30 Observability platform and its significance  
00:18:00 Conclusion and summary of partnership with Grafana  

These timestamps highlight the flow of the presentation and the key topics discussed.

# Backbase Presentation Transcript

**Hello everyone!** My name is Manu, and I will introduce myself in the upcoming slides as we walk you through today's agenda. We work at Backbase, a company that provides digital banking software to banks. 

## Agenda
1. Introductions
2. Overview of Backbase
3. Managed Hosting
4. Backbase Observability
5. Key Takeaways
6. Q&A

### Introductions
I’m very happy to be here and nice to meet you all! As mentioned, I’m Manu, the Product Director for the Backbase Managed Hosting product line. I have been with Backbase for almost four years and I live in the Netherlands with my wife and kids.

**Thanks, Manu.** I'm Andrei, a Systems Engineer working in the observability team. At the last Backbase Engage conference in the US, we launched our AI product line. As the industry shifts towards AI-powered products, Backbase is also transforming from a digital banking platform to an AI-powered banking solution.

### What Backbase Does
Let me walk you through the core value proposition of Backbase. We offer a **unified banking suite** that serves as an end-to-end platform, starting with **onboarding and origination**—the standard banking journeys used to acquire customers. 

Following that, we provide digital banking solutions, which include retail banking, business banking, lending, and investing. Our platform includes human-assisted touchpoints, leveraging AI, and facilitates activation and expansion. A customer might start with one product line and later expand into multiple product lines on the same platform, which is what we call the unified banking suite.

The customer journey begins with acquiring a customer, activating them, and then focusing on retention and expansion.

### Engagement Banking Platform
In today's rapidly changing environment, we believe that traditional banking cannot survive without rearchitecting around the customer. This means creating a customer-centric model that encompasses various workflows, transactions, payments, and approvals. We aim to cover all customer needs through a seamless experience, helping banks excel and grow at every step of the customer lifecycle—from acquisition to servicing, retention, and cross-selling—all within one platform.

On the left side of our platform, we focus on delighting the customer with digital onboarding and retail banking solutions. On the right side, we empower bank employees through digital assist and engagement solutions. Our goal is one platform for any journey, ensuring a future-proof and smooth digital transformation journey for banks.

### Managed Hosting
Backbase Managed Hosting alleviates the burden from banks and credit unions by deploying the engagement banking platform on a battle-tested Backbase reference architecture within the Microsoft Azure environment. Managed hosting ensures 24/7 monitoring, alerting, and maintenance, delivering value to our customers.

With each managed hosting installation, we provide a dedicated setup for every bank, ensuring complete isolation between different customers. We host around 70 customers on the Backbase Managed Hosting platform, which includes banks, credit unions, and financial institutions. We guarantee a **99.9% uptime**, with deployments spread across all three availability zones provided by our cloud provider. Our infrastructure is scalable, adjusting automatically to user behavior and unexpected events.

**Security** is paramount for us, and we embrace a zero-trust architecture. We verify everything instead of treating certain sources as trusted. Compliance is crucial; we provide our customers with a SOC 2 attestation annually. Database backups are always running in the disaster recovery (DR) region across all three availability zones, ensuring connectivity to on-prem legacy systems via site-to-site VPN.

### Technical Aspects of Managed Hosting
Now, I’ll hand over to Andrei to discuss the technical aspects of managed hosting.

**Thank you, Manu.** From a technical perspective, managed hosting consists of infrastructure code modules surrounded by automation, enabling us to provision customer environments quickly. At the core of our managed hosting solution is Terraform, which we use for most of our code base. Recently, we migrated to Open Tofu, and our infrastructure is hosted on Azure, with Backbase services deployed on Kubernetes.

We utilize GitHub Actions to orchestrate the deployment of Terraform modules across all customers. Once the infrastructure is in place, we use ROCD to deploy the Backbase services stack. For incident response, we rely on PagerDuty, and Grafana Cloud is central to our observability platform.

### Observability at Backbase
Observability is crucial to our managed hosting offering because we must maintain uptime and meet our SLAs. We require deep visibility into application performance and infrastructure health, providing seamless user experiences for our customers.

Observability can be broken down into two segments: the technical aspect, which involves infrastructure monitoring, and the business side. For banks, insights about user activity—such as daily active logins and login failures—are essential for understanding where to invest in customer journeys and product offerings.

A typical scenario involves a customer applying for a loan and dropping off at various stages. Understanding these drop-off points helps banks retain customers. We provide business dashboards that equip banks with efficient metrics to expand their customer base.

### Technical Details of Observability
We deal with two major sources of telemetry signals: Kubernetes workloads running on EKS and logs generated by Azure services. We collect these signals using Grafana Alloy and monitoring Helm charts developed by Grafana.

On the Azure side, we use Grafana Cloud to scrape Azure Monitor metrics and transform them into the Prometheus format. For log ingestion, we employ a pipeline configured at the resource level, pushing logs to Event Hub and using the Lucky Forwarder function to send logs to the Grafana stack.

Security remains a high priority; we isolate customer environments to mitigate risks. Grafana Cloud offers features such as single sign-on, user access management, and resource allocation insights, which help us optimize our platform.

### Conclusion
In summary, our partnership with Grafana has been exceptional. We began our engagement in early 2024 with a proof of value process that lasted seven months. The pre-sales discussions were promising, but the post-sales experience has exceeded our expectations. 

Managing observability for 70 banks is no small feat, and Grafana has been instrumental in allowing us to deliver on our SLAs and uptime commitments. We appreciate the ongoing technical support from the Grafana team.

Thank you for your attention! If you have any questions, feel free to ask.

## Raw YouTube Transcript

Hello. Hi everyone, myself, Manu will introduce ourself in the
upcoming slides and we'll walk you through today's agenda. So we work at Backbase, which sells banking, digital banking software to banks. What we are going to speak about today
is a bit of introductions about ourself. Then we would introduce
what Backbase does. We'll talk about manage hosting
from a technical perspective, but that's a product line
which with which we allow the capability to the banks that we can
host the Backbase software for them on cloud. Then we'll talk a bit
about Backbase observability, and of course the reason for that is
we are doing our observability platform with Grafana and we'll talk about a few
takeaways and in the end if you have any questions, we are happy
to take that as well. Let's talk about the introductions.
Very happy to be here. Nice to meet you all myself, Manu. I'm the product director for
Backbase manage hosting product line. I've been working with Backbase
close to four years now, live in the Netherlands
with my wife and kids. Thanks Manu. And I'm Andrei. I'm a systems engineer working
in the observability team. Like we saw on the first slide, right? AI powered banking platform. And this was in US. We are in the last
Backbase Engage conference. We launched our AI product
line and now as everyone is shifting to some AI back up products, similarly, Backbase is also transforming
from digital banking platforms to AI powered banking. Okay, let me walk you through regarding the
core value proposition of what Backspace does. So it's a unified banking
suite end-to-end platform, which starts with
onboarding and origination. These are the standard bank
journeys with which you acquire customers. Then comes the digital banking side of
things, which can be retail banking, business banking, lending, investing,
all these different solutions. Then comes a human assist touch
a bit on the AI side and then the activation and expansion, right? So a customer could start
with one product line, but later on they would
expand into multiple product
lines on the same platform and that is what we call
the unified banking suite. So the whole journey
starts with acquiring a customer, activating them, because once a customer signs on Backbase, it takes time to get them completely
live on production because the whole end-to-end systems connecting to the core
banking of different banks also takes some time and then comes the
retention and the expansion part of the whole journey. Let's talk about engagement banking platform.
So what we say here is that the traditional banking will not survive, so we need to rearchitect
the entire banking around the customer. So make it customer centric and
then comes multiple different things that need to orchestrate
around the whole digital banking suite. So it all starts with enhanced security
because we are talking about financial institutions here. It talks
about different workflows, transactions, payments, approvals and things like that. So centered around the customer
covering all their needs in our seamless experience, help bank excel and grow at every
step of the customer lifecycle from acquiring, servicing,
retaining, and cross-selling, and all of these things in one platform
that allows bank to future proof their operating model. One platform, any journey here what I was explaining
that it all starts with delighting the customer on the left-hand side with
digital onboarding, retail banking, lending solutions, two on the right side of digital
assist and engage solutions, which empowers the employees of
the bank to cater in a good way for the end customer needs. So we bring together all customer
facing journeys and the employee facing journeys. So we continue to expand
with our north star in mind. That is one platform, any journey, it's an end-to-end solution
that seamlessly connects
with our various ecosystem layers. Ensuring banks' digital transformation
journey is future-proof and also smooth back manage hosting, Backspace, manage hosting, unburdens, the end customer or say
the banks and credit unions from deploying the
engagement banking platform, which is the core proposition on
a battle tested Backbase reference architecture, Microsoft Azure environment
manage hosting ensures that there is 24 cross seven monitoring
and alerting and maintenance on the platform which we can deliver
value to the customers. So what we get with a
managed hosting installation, so it's a dedicated
installation for every bank. Isolation is key and of paramount
importance for us because we want to ensure complete segregation
between different customers. We host close to around 70 customers
on Backbase managed hosting platform. And when I say customers,
these are banks, credit unions, financial institutions, we guarantee a 99.9% uptime. That means all our deployments
are spread across all three availability zones provided
from the cloud provider. And we also run a replica on the DR side always running and the infrastructure
is completely scalable. Doesn't matter how many active users or
the behavior changes every second are infrastructure is designed to adjust
itself and responds automatically with respect to unexpected
events that might occur. So like I was mentioning, security is very important
to us as these are banks and we have the principle of zero trust
architecture. It's embedded in our way of working instead of treating
certain sources as trusted, not trusted, we never trust anything, we just verify anything and everything. Compliance is a very important
part for our customers, for our banks because
we adhere as part of our contractual obligations that we will
provide them with a SOC two attestation every year. Database
backups are always there. They are running in the DR region in all
three availability zones and we provide connectivity to on-prem because the
legacy systems, the core banking systems, we connect via site to site
VPN based connectivity to them talking about the geographical
deployment locations, of course primary location, all three availability zones running
in active active and in the disaster recovery region we always
have the databases running. So it's only a matter of time you need
to point your application in case of a DR event. And to be honest, I can tell you in order to
adhere to our RTO and RPO, it is very crucial and essential that
all the eyes are on the system of the observability platform. You have a thorough monitoring
and alerting as soon as
there is event you need to make a choice then and there that you
need to point the application on the DR side. And then I'll hand over to Andre to
talk about the managed hosting technical aspects. Thank you, Manu. So we talked
about managed hosting as a product, but what managed hosting is in fact
from the technical point of view. So from a technical perspective, managed hosting is just a
bunch of infrastructures, code modules surrounded by
some additional automation. And this recipe allows us to provision
customer environments in a matter of minutes double digits. At core of our managed hosting
solution, we have Terraform, we manage everything
we can with Terraform. Most of our code base is developed
in Terraform, in Terraform, and recently we migrated to
Open Tofu for obvious reasons, our infrastructure is hosted on Azure. The back based services applications
are deployed and hosted on Kubernetes. We are using GitHub actions
to orchestrate the managed hosting Terraform modules deployments
across all the customers. And once the infrastructure
part is deployed, we are using ROCD to deploy
the Backbase services stack. PagerDuty is our IRM system
and Grafana Cloud is at core of our observability platform. So let's
talk a bit more about observability. Yeah, observability as a platform is very, very crucial to Backbase manage
hosting offering because what we are providing to our customers, the uptime and the SLAs
we have that always need that we have deep visibility
into the application performance, infrastructure, health because we are
providing infrastructure as a
service to our customers and a seamless user experience. By this, I would break the entire observability
into two different segments. One is the technical aspect, which
is the infrastructure monitoring, and second would be the
business side of things. On the business side of things, I'll just try to explain
it with an example. Mostly if a bank, CTO, they want to have insights
about their end user base. What they would like to understand maybe
on a daily basis how many users are actively logging in, whether they're
logging in with which channel, whether it is web or
mobile, if it is mobile, iOS or Android.
Are there login failures happening because of biometrics
something wrong that will give them key insights in order to invest
in the right journey, right step of the product offering
in order to find out where they're lacking and that will also
help them expand their business. Let's talk about a very
small simple scenario. As of all of you guys would have
experience with any banking platform, you would have gone to become a
customer or apply for a loan and then at some point at different stages in multiple
questions you lose interest or you drop off. And then the bank really wants to
know at which stage did the end user drop off. So that was a customer they could
have retained but they dropped off. So these are the few business dashboards with efficient metrics
which we create and offer them to our customers and that helps our
customers, which are banks, expand their customer base. And we also of course
24 across seven incident management we are running and we
heavily rely on Grafana as a product. So let's talk even more about
observability at Backbase. In our scenario, we are dealing with
two major sources of telemetry signals. First one is are the Kubernetes
workloads running on EKS? And the second one are the
logs and metrics generated
by the Azure services that we are using on Kubernetes. We are collecting the telemetry signals
using Grafana Alloy and we are using the Kubernetes Monitoring Helm charts
developed and maintained by Grafana to manage the Grafana Alloy deployments. We chose this path
because of its simplicity, flexibility and modularity. It's relatively easy to manage. It allows us the flexibility
to extend the configurations in case we need some custom integrations and it also allows us to conditionally
enable or disable certain features based on certain customer
needs because some customers may need application availability, some other
customers may need continuous profiling, some customers may need both. And with Kubernetes
Monitoring Helm charts, it's really easy to
juggle with this features. On the Azure telemetry side of things,
the situation is a bit different. We are collecting the Azure
services metrics using the Grafana Cloud Cloud provider
observability of the Azure integration. It scrapes the Azure Monitor metrics
and probably some other stuff from Azure Resource Graph and transforms
them into Prometheus format stores them in the Prometheus data source for log ingestion, we are using a pipeline
composed of diagnosis settings configured on each resource level. The diagnosis settings are pushing
the logs to event hub and from Event hub these logs are being picked
up by the Lucky Forwarder function, which is also developed
by Grafana. It's open source and it takes care of sending the
logs to their Grafana stack logs and point off the specific customer. And probably important to mention that
we are using the serverless versions of both metrics scraping and
log streaming because we want to decouple these flows from
our physical infrastructure. As Manu mentioned, security is of high importance for
us as for any other organization and most of the security concerns
are mitigated by completely isolating the environments
of each customers. But we still feel important to share
some highlights of our experience addressing some security aspects using Grafana Cloud. The first one is single sign-on.
It's a well-known concept. Probably everyone of you is using
single sign-on to access your Grafana stacks. Yet on our previous
observability provider, it was a pain to automate
the setup of single sign-on. We had to raise support tickets with our previous provider support
and ask them to implement some changes that would serve as a
prerequisites for our single sign-on configuration automation. And it took weeks sometimes for them to
implement those changes. With Grafana, we don't have these limitations at all. Another aspect is the user access. In our scenario we are dealing with
different stakeholders. So Grafana Cloud stack and the access by both
Backbase employees who are supporting the applications and from people
from the customer organization. And each of those stakeholders
may require different level of privileges. And we are managing these privileges
with the combination of role-based access and label based access control when running a platform. At scale research
optimization is of even higher importance and we're using
the Grafana Kubernetes observability to get insights about our resource allocation to the
Backbase services workloads. It helps us identify cases of severe over provisioning and we are using this insights
for further optimization. This is an ongoing process because
there is no one size visible all configuration. We have
customers of different volumes. Some customers may require less resources, some customers may require more resources. This is where this feature helps us. Another dimension or another
source of insights which drive the optimization is the open cost
integration with Azure billing, which gives us accurate
cost of an understanding of the price of running our workloads. And sometimes seeing
currency instead of CPU or megabyte, it can be sobering. Another dimension for optimization
is the cost control or better say cost right sizing. Historically we've been dealing
with quite some expensive telemetry signals and one of
the most notorious ones are the logs generated by Azure
services due to different reasons, including compliance. We have to collect quite a
lot of quite high volumes of Azure logs. And previously we didn't
have a way to drop everything that we don't need
because for our use cases, quite often we need only a fraction
of the logs that we collect. And with Grafana Cloud
and with Grafana Cloud, we are using the Loki event. Forwarded to some extent optimize this flow. So it allows us to filter
out some unnecessary logs. Another approach we use is Adaptive
Metrics. We like this feature a lot. The biggest thing we like about it,
well besides the cost optimization, is the fact that it has
a Terraform provider. So for us it's pretty easy to automate the application of recommendations
provided by open cost and also applying some custom rules. And the last feature that we use, maybe some of you are not aware of it, are the log quotas or
log ingestion policy. So for us it is important
to set up hard caps on log ingestion for different
environments. For instance, for lower environments to
prevent sudden bursts of logs, for example, when someone forgets to disable debug
logs and leaves them running for a few days and maybe running some tests. So to mitigate these risks, we are using this functionality where
we are setting up hard cap on log ingestion per environment. And
actually it's quite flexible, it's much more flexible than on our
previous observability provider and it allows us to set up ingestion policies on label base. As a managed hosting team, it is important for us to be
able to quickly understand and see the current state of the platform across
all of our customers. So as previously mentioned, we are running quite a lot of
individual stacks for each customer and it's simply not feasible to log
into each one of them to retrieve some information. And for this, we are actively implementing the
concept of centralized Grafana stack with a really simple
idea of reading the metrics from the spoke Grafana
stacks and using them to build a single pane of glass dashboards. Even today, if you guys are not aware, or I don't know if some
of you is using Azure, Azure had quite a nasty outage
today on front door service and we actually used our
centralized Grafana stack to validate the status of our customers. One of the major reasons I missed most
of the sessions because I was just explaining to each and every customer, every bank of an outage that
is from the cloud provider, it is very difficult to explain
because for Azure also it takes time before they do first round of analysis
and then update the status page. So this really helps because then we
have a centralized view to check out the latency for every customer. And our customers are
deployed in different regions. We host from us, Europe, middle
East, Asia, Pacific, Australia, everywhere. Yeah, it's not a silver bullet,
it's not super flexible, but still it already delivers
quite a lot of value for us. And the nice part about it,
when working with metrics, it comes with no additional cost. We
don't need to reingest any telemetry, we are just reusing what we already have. And to conclude our
experience with Grafana Cloud, especially in the context of
migrating from another vendor, proved to us that it fits
really well into our automate everything scenarios. It provides ways to control the costs and avoid surprises. And of course none of this would've
been possible without the exceptional technical support that we receive on
a daily basis from the Grafana team. So thank you from the observability
team to the Grafana support team. Yeah, overall, I'll try to sum up
the partnership with Grafana, right? Andre has been quite modest
in explaining the whole stack, but we are talking about having
150 organizations in Grafana with around 1500 users. So anytime anything can really
explode and shoot the bill. But to be honest, the partnership
with Grafana has been really nothing short but exceptional. We started our engagement in
2024 where we ran a POV for seven months and then we
finally agreed that few of the things which are necessary for
us to move to Grafana were delivered actually before time. And how I call it that the
pre-sales discussions with any vendor is like a honeymoon period and
then comes the post-sales experience. But I can really call out
that the post-sales experience
with Grafana has been great. They have engaged with us at
every step and made the entire journey quite seamless. And it was done quite in
collaboration. And to be honest, it's a very crucial product for
us because having the entire incident management and keeping
eyes on 70 banks is not easy. And we really cannot deliver that
commitment of SLAs and uptime without having proper observability. And we need to architect that
as well around a good product. And Grafana has delivered that. So
a good partnership in our opinion. Thanks. Thanks everyone. Yep.

