# No Cloud? No Problem. Air-Gapped Observability at the Edge | ZEDEDA | Grafana

Published on 2025-06-07T05:33:24Z

## Description

What happens when your devices are in air-gapped, remote, or radio-silent environments? ZEDEDA's Ruslan Dautov shares ...

URL: https://www.youtube.com/watch?v=TvCmgP0iye8

## Summary

In this video, Ruslan Dautov, a Senior Site Reliability Engineer at ZEDEDA, discusses the challenges of cloud-based monitoring and the importance of edge observability, particularly in environments with limited connectivity. He highlights the issues faced by customers in the oil and solar industries, such as the need for "radio silence" in oil trucks to prevent triggering hazardous environments and the long periods of downtime for solar panel trackers before telemetry is available. Ruslan explains ZEDEDA's solutions, including their SaaS platform for managing edge deployments and their open-source edge virtualization engine. He also outlines their observability stack, which includes tools like Prometheus, Grafana, and Thanos, and emphasizes the necessity of localized monitoring systems that can operate independently of cloud connectivity. The session concludes with a Q&A and an announcement of ZEDEDA's partnership with Maersk for deploying their technology on ships.

# Air Gap Observability on the Edge

Hello everyone, my name is Ruslan, and today we'll talk about not putting everything in the cloud. We'll discuss air gap observability on the edge and provide a QR code for questions. We'll have a Q&A session at the end, and don't worry, we'll include the QR code again then.

I am Ruslan Dautov, based in Berlin, Germany, and I work as a Senior Site Reliability Engineer (SRE) at ZEDEDA. I have been in this role for almost four years, participating in on-call rotation and operations engineering.

## Agenda

Here's what we'll cover today:
- Problem statement: Why cloud-based monitoring doesn’t work.
- Cases of edge observability, including several customer cases from an oil service company and a solar tracker.
- Solutions and takeaways.

## Problem Statement

We often depend on the assumption that everything is in data centers with stable connectivity, but that’s not always the case. **Connectivity is key.** When a large enterprise provisions thousands of devices, they can face data waves of workloads that create bandwidth hogs, latency issues, and security risks. Transferring valuable logs, which are critical, must be localized. The air gap becomes a blind spot in these scenarios, making it impossible to provide a cloud-based solution and telemetry on the spot.

### Case Study 1: Oil Service Company

Let’s look at our first case: one of our largest oil service companies and one of our first enterprise customers. They operate fantastic workloads on edge devices mounted on trucks that move to oil well facilities. Once a day, they came to us with a technical requirement: **radio silence.** 

Initially, we were puzzled, but they explained that their trucks visit facilities handling explosives. Radio silence is critical to avoid triggering anything unintentionally. The technical requirements were mind-blowing. They run Windows virtual machines alongside a Kubernetes cluster and AI models utilizing GPUs—all on a moving truck. 

Due to radio silence, once the trucks enter this state, they completely disappear from telemetry. There are no logs or information until the trucks come back online. This presents interesting challenges, such as how to notify the device when it’s okay to return online after being in radio silence mode. 

### Case Study 2: Solar Tracker Company

Our second case involves PV hardware, one of the largest solar panel tracker companies with hundreds of deployments worldwide. Recent news from Spain and Portugal highlighted that downtime in these facilities is critical for energy production. 

This leads to new challenges: provisioning devices and deployment can take six months to a year. The first sign of telemetry may only appear once monitoring systems are in place, leaving devices offline for an extended period. Additionally, there are no dedicated IT specialists in the field, making it difficult to troubleshoot or power cycle the edge devices.

To illustrate the scale of our deployments, I’ll show a map of edge devices connected via satellite connectivity to our production systems. This is just a sample from one customer, but it showcases the distribution of our solution.

## Solution Overview

ZEDEDA, founded in 2016, provides a SaaS solution that helps orchestrate, manage, and control edge deployments on hardware. We have a global marketplace with thousands of workloads and over a hundred certified edge devices, ensuring stable operation without issues.

We also open-sourced our edge virtualization engine, an operating system under the Linux Foundation and Apache license. Since 2016, we have contributed to open source, allowing users to run virtual machines, containerized workloads (like Docker containers and Kubernetes), and more. This is secure because we do not allow console or SSH connectivity to edge devices; all communication goes through our API, known internally as ZEDcloud.

### Air Gap vs. Radio Silence

To clarify the terminology, an **air gap** refers to a system completely isolated from other networks, especially the internet. In contrast, **radio silence** relates to temporarily shutting down all radio wave communications until given specific orders to return online. 

We encounter cases where edge devices operate in air gap environments or radio silence mode, completely losing connectivity with ZEDcloud. Even in these scenarios, the edge devices do not stop or disrupt workloads; they continue working without issues and will come back online when connectivity is restored.

### Observability Stack

Now, let’s discuss our observability stack. We migrated from Datadog two years ago and currently use **Prometheus**, **Grafana**, and **Thanos**. Prometheus tracks all applications running on our production systems, while Grafana offers integration with various tools and data sources, providing a unified experience across different deployments. Thanos allows us to execute global queries across all our production deployments.

We track EKS deployments in the cloud across AWS, GCP, and Azure, and we use InfluxDB to manage high cardinality data, especially for analytical requests. 

**OpenSearch** operates as multi-node clusters in our deployments, handling different workloads. One cluster collects logs from devices while another handles internal applications. This creates a simplified picture of our observability stack, which includes EKS logs, Istio, InfluxDB, OpenSearch, Prometheus, Grafana, and Thanos.

We utilize Prometheus Alert Manager to send alerts to Opsgenie and FireHydrant. As Opsgenie has decided to stop selling their service, we are prepared for this migration.

### Air Gap Environment Challenges

In air gap environments, where there is no connectivity with a centralized observability stack, we maintain virtual clusters within our infrastructure to keep track of cluster details. We ensure we know the version, configuration, and that a real cluster is running somewhere. 

To provide security updates, new versions, and configuration changes, we package our container registry, Helm charts, and vault secrets, encrypt them, and ship them to the air gap environment. From there, we can extract logs and metrics.

### Takeaways

In conclusion, here are some key takeaways:
- **Store everything locally.** All observability stacks should be localized.
- Ensure deployments and clusters are self-sufficient, providing full monitoring capabilities to troubleshoot devices on-site without transferring data back.
- **Mind the gap.**

If you want to learn more, please visit [zededa.com](https://zededa.com) and check out our open-source project EVE. 

I’m excited to announce that one of our significant achievements includes partnering with Maersk, a major logistics company with hundreds of vessels worldwide. We will now also deploy our technology on ships.

Thank you for your attention!

## Raw YouTube Transcript

Hello everyone. My name is Ruslan and today we'll talk
about the not put everything in the cloud. So we'll talk about the air
gap observability on the edge and QR-code for the questions. We'll
have Q&A session in the end. Don't worry, we'll put this
QR-code in the end again. So my name is Ruslan
Dautov I based in Berlin, Germany and working as a SRE
engineer senior site relability engineer at ZEDEDA almost four years and I participating in on-call rotation
and operation engineering. So let's talk about the agenda. We'll have a look on a problem statement, why the cloud-based monitoring
doesn't work and the cases of the edge observability. We'll consider the several customer
cases for the oil service company and the solar tracker and we'll have
a look on a solution and takeaways. So problem statement, we have dependency and we
expecting that everything in data centers and you have stable
connectivity but it's not always available.
So connectivity is a king. When the customer or the big enterprise
is provisioning thousands of devices, you have the data waves of
the workload which can come on a production system and
can create the bandwidth hogs, latency issues and especially security. When you transfer something like
valuable in the logs, which is critical, it's important to be localized, air gap is completely blind
spot in that cases you not able to provide the cloud-based
solution and provide the telemetry on a spot. So let's talk about the first case. It's one of our largest
oil service company. It's one of our first enterprise customer fantastic workloads which running on
a edge device on a tracks and this tracks moving on oil well facilities. So they're running fantastic
workloads and in once in a day they came to us with technical
requirements. Guys, you need to implement the radio silence.
And we're like, why? So they start explaining that
this trucks visiting the oil facilities and some
facilities handling explosive. So radio silence is a critical to not
trigger what you shouldn't trigger. Yeah, I will say the
technical requirements, it kind of mind blowing, but to see that what kind of
workloads they're running, it's a Windows virtual machines
together with Kubernetes cluster and AI models which utilizing the GPUs
and imagine all these things running on a truck and this truck is moving. So in the same time
because of radio silence, trucks completely disappear from the
telemetry and you will not get any logs, any information from the trucks
till the trucks back online. So radio silence came with the
interesting challenges. First, you need to implement radio silence
and the second when you send a signal, a device go to a silent mode, how to tell device that now
it's okay to go back online because device sitting in radio silence
mode. This is one of a critical, I would say challenge which we have. And we saw that with local utilities
too when the engineer turned on back online, the system. Second case, it's a PV hardware, it's one of our largest solar
panel tracker company with hundreds of hundreds
deployments around the world. And if you have seen the news, latest news from the Spain and Portugal, downtime in this type of facilities
is quite important and I'll say critical for the energy production system. This come with new challenges, the provisioning of device and deployment and between these two events
can be happening like six months or one year. It means that first sign of
telemetry you'll see immediately on your monitoring and observability
systems and for the half year this device will disappear. In that case, it's one of a challenge
and second challenge. It's no IT dedicated specialist
on the field. It means that you're not able to break
device or damage or make it unusable. No one will come
and powercycle the edge device. This is hard. This is a lot
of challenges. But yeah, and to understand how
distributed this type of deployments can be I
showing second the map of the edge devices, which connecting via satellite
connectivity to our production systems. It's only the sample of one of a customer, but you need to give the view of the
scale how distributed our solution, how distributed our deployments, and how big it is. So let's
talk about the solution. ZEDEDA founded in 2016
and providing one of a SaaS solution which help you
to orchestrate and manage and control the edge deployment
on your hardware. It's come together with the global
marketplace where we store the thousands of different
workloads and we also have more than a hundred edge devices, which we certified and we make sure that
everything running stable and without any issues. And the second product
which we open source, it's edge virtualization engine, its operation system
under the Linux Foundation under Apache license. And from 2016 we contributing to open source where this
engine give you the ability to run the virtual machines, containerized workloads like docker
containers, Kubernetes workloads, and any others. And this is really secure because we're
not allowed any console connectivity or ssh connectivity to the edge devices. Everything goes through the eve API, we call that our ZEDEDA cloud.
Internally we call that ZEDcloud. So usually I might use that term. And what the difference between the
air gap and radio science? So air gap, it's a term from the computer
networks when certain system complex or data completely is
isolating from the other networks and especially internet
while the radio sign its term when related to
radio wave communications. And when you temporarily shutting
down all communication till the special order to back online
and how it's related to us. We have cases when the edge device in
the air gap environment or in the radio silence mode and completely losing
connectivity with the ZEDcloud in that case edge device, not stoped not disrupting the workload, it's continue working and without
any issue we'll back online when the connectivity will be restored. Second case when all deployment
of controller and edge devices inside the air gap environment. This is one of a complex case
for our deployments and we today will share how we handling both
cases with our observability stack. So when we start talking
about the observability, I'll introduce our teammate, Umka Umka, one of our user watchdog accounts. So it's usually
tracking all the CPU spikes, barking for the opsgenie
alerts. Fantastic teammates. So let's talk about our
observability stack. We actually migrated from
the Datadog two years ago. That's why this stack was, I'll
say not relatively new, but we migrated. So Prometheus,
Grafana and Thanos. Prometheus we usually use for our
backend system to track all the application which running
on a production system. Grafana fantastic product with a lot
of integration with different tools, different data sources
which give us unified experience between the different
production deployments and thanos. Because we receiving tons of
logs and tons of telemetry, it's important for us to make
the global queries across all our production deployments. And this free tools is
not the complete set. So we tracking the EKS. If we deploy it in the cloud,
we're actually deploying in AWS GCP and Azure. That's why to get the telemetry from the
managed at Kubernetes environment for us important InfluxDB, we using the second version
and we keeping the higher, and I will say bigger virtual
machines for this type of workloads because we have a high
cardinality of the data and this type of data when you construct
an analytical request for the many time series can
spike this CPU and memory. That's why we keeping the
bigger VMs and I'm happy to see the presentation today That's
influx 3.0 zero solving a lot of performance issues. OpenSearch. OpenSearch is not just
one instance. Actually. OpenSearch are presented in
our deployments by clusters, multi-node clusters. And we have two multi-node clusters
which handling different workloads. One, it's for the logs which coming from
the devices and one for the internal apps which working on our
production system altogether, it's represent this type of
simplified picture of our observability stack.
So this unified, it's one cluster. Of course we have tons of
micros which running beside, but overall it's EKS logs, Istio influx to be open search,
Promeus, Grafana and thanos, which we are actually using the Prometheus
alert manager with sending the alerts to opsgenie and fire hydrant
because opsgenie decide in the 4th of June to stop selling the opsgenie. We prepared for this type of
migration. We choose the firehydrant. So this type of deployment represent
the one unified cluster which we can deploy in a air gap environments
or inside our systems, which would present our, I would
say, multi cluster environment. This is picture of, I would say briefly introduction to
our multi cluster deployments when we deploy in GCP AWS and Azure. And we also deploy in different
regions and different countries. That's why for us it's I
will say really distributed deployments where the edge nodes can be
connected and disconnected from the each deployment and the air gap environment
can be completely isolated. So we're using the log for
our IT ops and the security operations when we sending the
logs from our internal IT systems. For example, like CloudFare, Okta, when we tracking all the
access to the device logs data, for example, engineer
goes to the deployment, have a look on what kind of logging
existing related to that customer and we tracking all this connectivity
authorization to the log thanos give us ability to not transfer tons of
data to the centralized observability stack and we can make the queries
across the old production system and deployment Grafana Grafana give us
a unified experience between all the deployments because we're using the
ArgoCD and the Gitops frameworks to deploy
the production systems. It means that when the developers
log into the each cluster, it's give them unified experience
between the deployments. And let's talk about the
one of a complicated part and complicated part.
It's air gap environment. When we don't have connectivity with
centralized observability stack and cases when this devices, it's only working in that
enterprise environment. So in that case, we keeping the virtual cluster
inside our infrastructure to keep the all information
about this cluster details. We know that which version,
which kind of configuration. And we know that somewhere there the
real cluster is running and we need to provide the security updates, new
versions, configuration changes, and extract the logs back to
track the all information. What's going on there. So we first of all pack
our container registry, helm charts, hel helm museums, vault secrets, packed and encrypted,
ship it to the air gap environment, deploy that and extract the logs
and metrics on the back way. So this exactly represent our
multi cluster deployment and centralization give us ability to
unify all alerting system to one place and send the alerts to
the slack and the fire hydrant. And of course Thanos give us ability
to store that data for the longer time because we have terabytes of logs, which coming from the edge devices and
we have different retention period for the device informations because it can be terabytes and we store
that up to 30 days or 90 days or for the certain cases we
can store it for the one year. That's why for us it's critical to store
that for the longer time and also to track all the changes in
this deployments. Also, let's, I will say continue to takeaways. What takeaways in our cases you need to store
everything in a local all observability stack should be localized. Also deployment and the cluster
should be self-sufficient to provide all monitoring stack to provide the
all ability to troubleshoot devices on place without the
transferring data back. And also I will say mind the gap. If you want to learn more, please visit zededa.com and
visit our open source project EVE. Also today I can announce
something new of one of our, I'll say achievement, one of the
big logistic company called Maersk, which have a hundreds of vessels around
the world and shipping containers choose us as technology partner. And that's why we also will be deployed
not only tracks, not only trains, and we also will deploy on ships. So I want to say thank you. I want to say thank
you for your attention.

