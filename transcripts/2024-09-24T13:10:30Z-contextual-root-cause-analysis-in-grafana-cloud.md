# Contextual root cause analysis in Grafana Cloud

In this video, you will learn how to troubleshoot your application faster with Grafana Cloud Asserts, which provides contextual root ...

Published on 2024-09-24T13:10:30Z

URL: https://www.youtube.com/watch?v=gBXJAwwag5E

Transcript: Hi, this is Vijay Tolani. In this video, I'll show you how Grafana Cloud Asserts
puts your app anomalies in context to help you find the root
cause of issues faster. One of the biggest challenges with
troubleshooting today's complex microservice-based applications is just
understanding all the components of the application and infrastructure
and how they're all connected. And we all know the situation
when a bunch of alerts fire at once and you know something's wrong, but you're left asking
yourself questions like, how big's the blast radius
and what's the root cause? With Grafana Cloud Asserts, you can help prevent alert fatigue
by setting up SLO based alerts. When an alert is triggered, you'll be directed to a curated RCA
workbench to help you determine root cause of the issue. This workbench
features a timeline of assertions, which are checks on critical system
metrics that are automatically set up for you. These assertions are categorized
into the SAAFE model for saturation, amend, anomaly, failure and error. The timeline view gives you a quick
look into the assertions across your applications and infrastructure and
functions as a heat map to help you understand which components
are most affected. At a glance, we can see the product catalog service
is at the center of this issue. The summary view of the RCA Workbench
provides a holistic view of these assertions. By sorting by time, we can quickly establish
the order of events. First, we see a feature was enabled. Then we can see the Kubernetes pod
supporting the product catalog service started crash looping, and shortly after we started to see
a high number of connections on the database. Then simultaneously, the list products functions
on the product catalog, service front end, and recommendation service all
started failing and the front end couldn't list recommendations.
Looking at the graph, we can see how all the components
of the app are connected. We can see the feature flag service is
connected to the product catalog service and the recommendation service, both of
which are connected to the front end. Our furthest downstream component is
this Postgres database connected to the product catalog service. We'll
continue our troubleshooting there. Here we see those high connections from
earlier, we see spikes in connections, which means something's likely
failing and getting restarted. Grafana Cloud Asserts automatically
identifies the most relevant dashboards powered by our observability
solutions. In this case, Grafana Cloud Asserts identifies
this as a Postgres database. We can see that spike in
connections, but beyond that, our database looks healthy. The product catalog service is
the next upstream component, so we'll continue there. Here we can see
the crash looping pods we saw earlier. Grafana Cloud app observability
shows a spike in response duration and a pretty high error rate. We know
the Kubernetes pods are restarting, so let's take a look at
Kubernetes monitoring. It doesn't look like a memory issue, so let's take a peek at
the logs and sure enough, looks like we're running
into a null pointer. This must be the root cause
of our Kubernetes restarts
and the drop connections on the database. We'll validate this by taking a look
at those connections and crash looping pods. Sure enough, they're
happening at the same time. Looks like we found our root
cause and we know what to fix. We'll roll back this feature to
restore the app to a stable state. Here we see the feature flag was disabled, and shortly after the app returns to
normal Grafana Cloud Asserts is powered by an entity graph, which provides context to your application
and infrastructure to telemetry. It helps you understand all of the
components of your app and infrastructure, how they're connected,
as well as their health. This helps you determine
the Blast radius of issues, and where to focus your Troubleshooting. Asserts is available for users of
Grafana Cloud Advanced. To get started, navigate to asserts from
the Grafana Cloud menu.

