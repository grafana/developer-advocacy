# What is Grafana Cloud? Fully Managed Observability Built on Open Standards | Grafana Labs

Published on 2025-07-29T13:01:41Z

## Description

Grafana Cloud helps teams detect, investigate, and resolve incidents faster—thanks to AI, open standards, and seamless ...

URL: https://www.youtube.com/watch?v=tBjEUUys7YE

## Summary

In this video, a representative from Grafana discusses the benefits and functionalities of Grafana Cloud, emphasizing its development on open standards for improved data integration and incident management. The demonstration features a simulated e-commerce store operating on multiple microservices, showcasing how Grafana Cloud quickly identifies and addresses issues such as high latency during product searches. The process includes declaring an incident via Slack, utilizing the RCA Workbench for root cause analysis, and leveraging AI features to streamline investigations. The video highlights the seamless integration of various data sources, like OpenTelemetry and Prometheus, and concludes with a call to action for viewers to explore Grafana Cloud for free, underscoring the platform's capacity for faster problem resolution and enhanced business insights.

At Grafana, we believe the best software develops when people can move fast, share ideas openly, and aren't locked in. **Open just works better.** That's why we built Grafana Cloud on open standards, bringing all your data together in one place so you can see what's really going on and solve problems faster.

Let me show you how Grafana Cloud cuts through the noise when things go wrong. Here, we're running a live, distributed e-commerce store made up of over **10 microservices**, allowing customers to browse products, see recommended products for them, and complete purchases just like a real business. These apps and services are actively emitting data from tools like **OpenTelemetry**, **Prometheus**, **Loki**, and even **Salesforce**.

You can see here that we are experiencing high latency when searching for products on our product catalog service. The alert includes options to declare an incident, investigate, acknowledge, or even show a timeline of events, all from **Slack**. This is all possible as Grafana Cloud provides a full end-to-end incident management and on-call workflow for teams to stay closer to their data. 

Since this has potential business impact and is causing poor user experience, let's declare an incident. We will quickly fill out the details for our incident so we can get to finding the root cause. This incident creation will create a **Slack** or **Microsoft Teams** channel, link relevant dashboards to the incident, and can be interacted with through the mobile app as well.

Now that we have that created, let's jump into the investigation. This alert dropped us into Grafana Cloud's **RCA Workbench** because an **SLO-based alert** fired. That means it's focused on real user impact and not just noisy CPU spikes or random blips. Under the hood, Grafana Cloud is doing a ton of heavy lifting to make this feel effortless. It inspects signals coming from **OpenTelemetry**, **Prometheus**, and other sources, then builds a real-time knowledge graph of your environment. This graph shows which pods run on which nodes, how services talk to each other, and even how all this ties back to your business metrics.

But let's get back to the core issue here. Switching into our summary view and sorting by time shows that we are experiencing some sort of feature flag change causing a lot of issues with our frontend and other services. Now, we can do this investigation manually by following this timeline and diagnosing the upstream impact, but with Grafana Cloud's **AI Workbench**, we can speed up analysis drastically.

Here, you can see Grafana Cloud is completing analysis across multiple services, then returning hypotheses of what went wrong. The hypothesis is that there was a feature flag change, which caused a database connection issue leading to pod crashes on the product API, and increased errors in our recommendations being served up to our customers. This checks out visually and is what the timeline shows.

Now, you may all believe this was magic, but Grafana is working hard under the hood to take signals being surfaced in various views like application observability, Kubernetes, frontend RUM data, and correlating them all together. We can finally tie this all back to our business outcomes by looking at our checkout service and viewing our embedded business dashboard. All of this data is being pulled from **Salesforce** directly, where we can see a good amount of lost revenue.

To quickly mitigate this, we just need to toggle off that feature flag, verify that everything's stable again, and close out this incident. 

And here's the real kicker - we're able to move this fast because Grafana Cloud was built and trained on open standards. **OpenTelemetry**, **Prometheus**, and other open signals give us the flexibility to plug in data from across our stack and the confidence that everything would just work together. That's the power of open: faster answers, fewer silos, and clearer paths to resolution.

So there you have it, Grafana Cloud is a seriously powerful end-to-end observability platform. And the best part is you can get started for free. Head on over and learn more at **Grafana.com**.

## Raw YouTube Transcript

At Grafana, we believe the best software
develops when people can move fast, share ideas openly and aren't locked
in. Open just works better. That's why we built Grafana Cloud on open standards, bringing all your data together in one
place so you can see what's really going on and solve problems faster. Let me show you how Grafana Cloud cuts
through the noise when things go wrong. Here we're running a live, distributed
e-commerce store made up of over 10 microservices, allowing
customers to browse products, see recommended products for them, and complete purchases
just like a real business. These apps and services are actively
emitting data from tools like OpenTelemetry, Prometheus,
Loki, and even Salesforce. You can see here that we are experiencing
high latency when searching for products on our product catalog service. The alert includes options to declare
an incident, investigate, acknowledge, or even show a timeline of events all
from Slack. This is all possible as Grafana Cloud provides a full end-to-end
incident management and on-call workflow for teams to
stay closer to their data. Since this has potential business impact
and is causing poor user experience, let's declare an incident. We will quickly fill out the details for
our incident so we can get to finding the root cause. This incident creation will create
a Slack or Microsoft Teams channel, link relevant dashboards to the incident
and can be interacted with through the mobile app as well.
Now since we have that created, let's jump into the investigation. This alert dropped us into Grafana
Cloud's RCA Workbench because an SLO-based alert fired. That means it's focused on real user
impact and not just noisy CPU spikes or random blips. Under the hood, Grafana Cloud is doing a ton of heavy
lifting to make this feel effortless. It inspects signals coming
from OpenTelemetry, Prometheus, and other sources then builds a real-time
knowledge graph of your environment, showing which pods run on which nodes,
how services talk to each other, and even how all this ties back to your
business metrics. But let's get back to the core issue here. Switching into our summary view and
sorting by time shows that we are experiencing some sort of feature flag
change causing a lot of issues with our frontend and other services. Now, we
can do this investigation manually. By following this timeline and diagnosing
upstream impact, but with Grafana Cloud's AI Workbench, we can
speed up analysis drastically. Here you can see Grafana
Cloud is completing analysis
across multiple services then returning hypotheses
of what went wrong. The hypothesis is that there
was a feature flag change, which caused a database connection issue
leading to pod crashes on the product API, and increased errors in
our recommendations being
served up to our customers. This checks out visually and is
what the timeline shows. Now, you may all believe this was magic, but Grafana is working hard under the
hood to take signals being surfaced in various views like application
observability, Kubernetes, frontend RUM data, and correlating them all together.
We can finally tie this all back to our business outcomes by looking at our
checkout service and viewing our embedded business dashboard. All of this data is being pulled from
Salesforce directly where we can see a good amount of lost revenue.
To quickly mitigate this, we just need to toggle
off that feature flag, verify that everything's stable
again, and close out this incident. And here's the real kicker - we're able
to move this fast because Grafana Cloud was built and trained on open
standards. OpenTelemetry, Prometheus, and other open signals give us the flexibility to plug
in data from across our stack and the confidence that everything
would just work together. That's the power of open. It's faster
answers, fewer silos, and clearer paths to resolution. So there you have it, Grafana Cloud is a seriously powerful end-to-end observability platform. And the best part is you can get started for free. Head on over and learn more at Grafana.com.

