# Visualize Jenkins CI/CD Pipelines: Introducing the New Jenkins Data Source Plugin in Grafana 12.2

Published on 2025-09-25T14:50:41Z

## Description

Grafana 12.2 introduces the new Jenkins data source plugin, giving you real-time insights into your Jenkins CI/CD pipelines.

URL: https://www.youtube.com/watch?v=JF9bAEsilXg

## Summary

In this video, the presenter introduces a new Jenkins data source plugin designed for Jenkins CI, a popular open-source automation server used for software development automation. The video covers the plugin's configuration, which involves entering the Jenkins instance URL and authentication details. The presenter showcases two dashboards included with the plugin: the Overview Dashboard, which provides real-time insights into the Jenkins cluster, including project statuses, node statuses, and build queues; and the DORA Metrics Dashboard, which tracks key performance indicators in software development such as deployment frequency, lead time for changes, change failure rate, and time to restore service. These metrics help teams assess their delivery efficiency and reliability. The video concludes with a thank you from the presenter.

# Quick Overview of the New Jenkins Data Source Plugin

Hi! Today, I'm going to give you a quick look at the new Jenkins Data Source Plugin we just launched. For those unfamiliar, **Jenkins CI** is a widely adopted open-source automation server. Think of it as a central hub for automating various stages of your software development, such as building, testing, and deploying software.

## Configuration

First, we're going to take a look at the configuration page for the plugin. You just have to put the URL of your Jenkins instance and the authentication information if required.

## Dashboards Overview

Now, let's explore the two dashboards that are bundled with the data source.

### Overview Dashboard

The first dashboard we will look at is the **Overview Dashboard**. It provides a real-time overview of the Jenkins cluster's current state.

#### Projects Panel

Let's start with the **Projects Panel**. Here, you can get a clear list of all the projects currently configured in your Jenkins instance. For each project, you can see the status and the latest build, which links directly to the Jenkins job itself.

#### Nodes Panel

Next, we're going to the **Nodes Panel**. This gives you an overview of all the nodes, also known as agents, connected to your Jenkins master instance. You can quickly see whether each node is online or offline. We also display the load percentage of how much each node is being used at the moment, along with the queue length indicating the number of jobs that are pending execution.

#### Build Queue Panel

Lastly, we have the **Build Queue Panel** at the bottom. This panel provides a view of all the builds currently waiting to be executed in the Jenkins cluster. For each queued build, we can see its build number, the associated project, the status, how long it has been queued, and extra information on what this build is waiting for.

## DORA Metrics Dashboard

Let's switch gears a little bit and take a look at another bundled dashboard, which is the **Jenkins DORA Metrics**.

For those unfamiliar with DORA metrics, DORA stands for **DevOps Research and Assessment**. The four DORA metrics—**deployment frequency**, **lead time for changes**, **change failure rate**, and **time to restore service**—were identified through industry research as key indicators of high-performance software development teams.

### Deployment Frequency

The first panel here is the **Deployment Frequency**. This chart shows the daily trend of successful deployments. Each bar represents a day, and the height indicates the number of successful deployments per day. Tracking this metric helps teams understand how often they're delivering value to their users.

### Lead Time for Changes

Next is the **Lead Time for Changes**. This panel displays the average duration of successful builds on a daily basis. It essentially measures the time it takes for a code commit to become a successful deployment. A short lead time often indicates a more efficient and agile delivery process.

### Change Failure Rate

The next metric is the **Change Failure Rate**. This panel shows the percentage of failed builds compared to the total number of builds each day. This helps gauge the stability and quality of the releases. A low failure rate signifies a more reliable delivery pipeline.

### Time to Restore Service

Finally, we have the **Time to Restore Service** panel. This panel displays the average time it takes to recover from a failed build to a subsequent successful build on a daily basis. This metric shows how resilient the team is and how quickly they can address and resolve issues.

That's all for today. Thank you!

## Raw YouTube Transcript

Hi. Today I'm going to give you a quick look
at the new Jenkins data source plugin we just launched. For those unfamiliar, Jenkins CI is a widely adopted
open source automation server, and think of it as a central hub for
automating various stages of your software development, such as building,
testing, deploying software. First, we're going to take a look at the
configuration page for the plugin. You just have to put the URL of your
Jenkins instance and the authentication information if required. Now, let's explore the two dashboards that
are bundled with the data source. The first dashboard that we're going
to look at is the overview dashboard. It provides a real-time overview of
the Jenkins cluster current state. Let's start with the projects panel. Here you can get a clear list of all the
projects currently configured in your Jenkins instance. For each project, you can see the status of the project
and the latest build that links directly to the Jenkins job itself. Next,
we're going to go to the nodes panel. This gives you an
overview of all the nodes, also known as agents connected
to your Jenkins master instance. You can take a look at a glance
whether each node is online or offline. We also have here the load's percentage
of how much this node is being used at the moment and the queue length with
the number of jobs that are pending execution. Lastly, we have the build
queue panel on the bottom here. This panel provides a view of all the
builds currently waiting to be executed in the Jenkins cluster. For each queue
build, we can see its build number, the associated project, the status, since when it's queued and
extra information on what
this build is waiting for. Let's switch gears a little bit and take
a look at another bundled dashboard, which is the Jenkins DORA metrics.
For those unfamiliar with DORA metrics, DORA stands for DevOps research and
Assessment. The four DORA metrics, which are deployment frequency, lead
time for changes, change failure rate, and time to restore service, were identified through industry research
as key indicators of high performance software development teams. The first
panel here is the deployment frequency. This chart shows the daily
trend of successful deployments. Each bar represents a day, and the height indicates the number
of successful deployments a day. Tracking this metric helps
teams understand how often
they're delivering value to their user. Next one is
the lead time for changes. This panel displays the average duration
of the successful builds on a daily basis. It essentially measures the time
it takes for a code commit to become a successful deployment. A short lead time often indicates a more
efficient and agile delivery process. The next one is the change failure rate. This panel displays the percentage of
failed builds compared to the total number of builds each day. This helps gauge the
stability and quality of the releases. A low failure rate signifies a
more reliable delivery pipeline. The next one is the time
to restore service panel. This panel displays the average time it
takes to recover from a failed build to a subsequent successful
build on a daily basis. This metric shows how resilient and able
to quickly address and resolve issues the team is, and that's
all for today. Thank you.

