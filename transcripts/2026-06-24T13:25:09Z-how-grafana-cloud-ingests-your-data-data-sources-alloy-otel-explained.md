# How Grafana Cloud Ingests Your Data | Data Sources, Alloy &amp; OTel Explained

Published on 2026-06-24T13:25:09Z

## Description

Learn the two main ways to get data into Grafana Cloud. In this video, we break down how Grafana Cloud connects to over 150 ...

URL: https://www.youtube.com/watch?v=VtiEWdOzm_I

## Summary

The show is titled "How Grafana Cloud Ingests Your Data | Data Sources, Alloy & OTel Explained," published on June 24, 2026. The speaker discusses the various methods for ingesting data into Grafana Cloud, emphasizing the use of Grafana as a visualization layer that connects to over 150 external data sources without storing the data. Key features highlighted include Grafana Alloy, an open-source data collector that integrates tools like OpenTelemetry and Prometheus, and Grafana Beyla, which utilizes eBPF for capturing telemetry data with no code changes. The session underscores the flexibility and optionality of Grafana Cloud, allowing users to manage their data pipelines effectively while leveraging open standards.

Topics: Grafana Cloud, data ingestion, Grafana Alloy, OpenTelemetry, Grafana Beyla, eBPF, telemetry data.

## Chapters

00:00:00 Overview of data ingestion methods in Grafana Cloud
00:01:33 Integrating OpenTelemetry and Prometheus with Grafana Cloud
00:02:21 Understanding Grafana Cloud's data ingestion and OTLP endpoint

Hey everyone! In the last video, we gave you the rundown as to what Grafana Cloud is and how open standards give you and your team the flexibility and optionality to work the way you want. So today, we're going to talk about just that: optionality. Specifically, the different ways you can get data into Grafana Cloud. 

Whether you're tapping into your existing tools or shipping raw telemetry from your apps and infrastructure, we've got you covered. But before I jump straight into showing you a bunch of tech without any context and overwhelming you, I want to give you a visual model—a simple way to understand how data flows into Grafana Cloud.

At the core of Grafana Cloud is, well, Grafana—the same open-source Grafana you may already know. It's the visualization and alerting layer that powers dashboards, visualizations, and alerts. Grafana connects to data through what's called the data source model. This means Grafana can pull in data from over 150 external tools like Salesforce, Postgres, Prometheus, CloudWatch, and more, all without needing to store that data again. Your data essentially stays where it is; Grafana just queries it when you need it.

Now, Grafana Cloud also gives you the option to send raw telemetry data into fully managed databases for logs, metrics, traces, and profiles. It's important to note these are still data sources, but they're hosted, scaled, secured, and maintained by Grafana for your specific cloud stack. This means you don't have to worry about the overhead of maintenance and patches.

So how does telemetry data flow into those databases? The recommended way is **Grafana Alloy**, which is a fully open-source data collector, combining the strengths of tools like OpenTelemetry and Prometheus all into one place to make integrating with Grafana Cloud much more streamlined. Grafana Cloud provides easy and configurable Alloy deployment options for MacOS, Windows, Linux, Kubernetes, and a heck of a lot more.

If you are running your apps and infrastructure using cloud-native tools like Kubernetes for orchestration and hosted on Linux VMs or servers, you can easily configure **Grafana Beyla**, which is powered by eBPF, to capture trace and metric data from your applications with no code changes needed. Alloy also comes with an option to toggle on fleet management, giving your team the power to manage your collectors at scale much easier. This gives you the control and flexibility to handle centralized configuration, which means you can update, activate, or adjust pipelines remotely, monitor the health of your Alloy instances, and control costs by turning data streams on or off to reduce noise and manage your spend.

But we're talking about optionality, and the beauty of Grafana Cloud is that it's built on open standards. This means every Grafana Cloud stack includes a dedicated OTLP endpoint, so you can send telemetry directly using the core OpenTelemetry collector or any OTLP-capable client. Just note that this path requires a bit more of a manual setup, like adjusting your resource attributes and the labels to adhere to what Grafana Cloud expects.

Okay, so I hope that cleared some things up. In the next video, we'll begin getting hands-on with the keyboard and even implement by connecting a data source and sending telemetry signals into Grafana Cloud. I hope to see you guys there, and as always, please like and subscribe. We'll see you in the next video!

## Raw YouTube Transcript

Hey everyone! In the last video, we gave you the rundown as to what Grafana
Cloud is and how open standards give you and your team the flexibility and
optionality to work the way you want. So today we're going to talk about
just that... optionality. Specifically, the different ways you can
get data into Grafana Cloud. So whether you're tapping into your
existing tools or shipping raw telemetry from your apps and infrastructure,
we got you covered. But before I jump straight into showing
you just a bunch of tech without any context and overwhelming you, I
want to give you a visual model. Sort of a simple way to understand how
data flows into Grafana Cloud at the core of Grafana Cloud is well Grafana
the same open source Grafana you may already know. It's the visualization and
wording layer that powers dashboards, visualizations, and alerts. Grafana connects to data through what's
called the data source model. This means Grafana can pull in data from over
150 external tools like Salesforce, Postgres, Prometheus,
CloudWatch, and more, all without needing to
store that data again. Your data essentially stays where it is. Grafana just queries it
when you need it. Now, Grafana Cloud also gives you the option
to send raw telemetry data into fully managed databases for logs,
metrics, traces, and profiles. It's important to note these are still
data sources, but they're hosted, scaled, secured, and maintained by Grafana
for your specific cloud stack. This means you don't have to worry
about the overhead of maintenance and patches. So how does telemetry data flow into
those databases? The recommended way is Grafana Alloy, which is a fully
open source data collector, combining the strengths of tools like
OpenTelemetry and Prometheus all into one place to make integrating with
Grafana Cloud much more streamlined. Grafana Cloud provides
easy and configurable alloy
deployment options for MacOS, Windows, Linux, Kubernetes, and heck of a lot more. If you were
running your apps and infrastructure using cloud native tools like Kubernetes for
orchestration and hosted on Linux VMs or servers, you can easily
configure on Grafana Beyla, which is powered by EBPF to capture trace
and metric data from your applications with no code changes needed. Alloy also comes with an option
to toggle on fleet management, giving your team the power to manage
your collectors at scale a lot easier. This gives you the control and flexibility
to handle centralized configuration, which means you can update, activate,
or adjust pipelines remotely, health monitoring to understand the
health of your Alloy instances and cost control to turn data streams on or off
to reduce noise and manage your spend. But we're talking about optionality and
the beauty of Grafana Cloud is that it's built on open standards. This means every Grafana cloud stack
includes a dedicated OTLP endpoint, so you can send telemetry directly using
the core Open Telemetry collector or any OTLP capable client. Just note that this path requires
a bit more of a manual setup, like adjusting your resource attributes
and the labels to adhere to what Grafana Cloud expects. Okay, so I hope that
cleared some things up. In the next video, we'll begin getting hands-on keyboard
and even implement by connecting a data source and sending telemetry
signals into Grafana Cloud. I hope to see you guys
there and as always, please like and subscribe and
we'll see you in the next video.

