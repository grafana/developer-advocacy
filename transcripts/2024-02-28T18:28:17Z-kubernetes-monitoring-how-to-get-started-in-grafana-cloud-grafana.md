# Kubernetes Monitoring: How to Get Started in Grafana Cloud | Grafana

Start monitoring your Kubernetes cluster in less than 3 minutes! This is a quick but comprehensive guide for getting started with ...

Published on 2024-02-28T18:28:17Z

URL: https://www.youtube.com/watch?v=x-7DYgDs9Kw

Transcript: Hi everybody. My name is Pete Wall and I am gonna show
you how easy it is to start monitoring your Kubernetes clusters using
Kubernetes Monitoring in Grafana Cloud. So here's my Kubernetes cluster.
It's a three node bare metal cluster, and because it's bare metal, I care about the health of the cluster
and of the nodes and of the deployments running on the cluster. I'm
the one who's managing that, so it's important to me to
understand what's going on. Right now I don't have any sort of
monitoring infrastructure on this cluster, but I wanna change that. So if I go to the Kubernetes
Monitoring page in Grafana Cloud, then I can click onto the configuration
page into cluster configuration. And on this page, I can set up the deployment that
I want to put onto my cluster. So let's name the cluster,
we call it petes-cluster, and the namespace, we're gonna
put this into the monitoring namespace. It's a standard Kubernetes
cluster, so that doesn't change. As for features, I'm gonna
try to collect everything. So I'm gonna leave those all on.
Now to get the metrics, logs, and traces into Grafana Cloud, I do
need to create an access policy token. I can reuse an existing one, but we're
gonna make a new one for this demo. We're gonna call it Pete's Cluster
Token. And we'll create it. Alright, now that the access
policy token has been created, I can go down here to the next step. Now, this field here has a single click
terminal command that will deploy the Kubernetes monitoring health chart. So
I'm just gonna click copy, go back here, make a new terminal, and
just paste everything. And now it's starting to deploy
Kubernetes Monitoring on my cluster. Let's go back and see the changes. Okay, looks like Kubernetes
Monitoring has finished deploying. Let's go back to Grafana Cloud
and see how it looks. Back here, I can go to the cluster status
page and see that the metrics for the cluster are coming in. And
I can go to cluster navigation. And I see my cluster down here along with
the other clusters that I've deployed already. And I can start to look at some
information that's comparing against the different clusters,
the different name spaces, different workloads that are
running on here and drill down and see all of this great information
that's available with Kubernetes monitoring. So, that's it. One command gives you everything that
you need to start monitoring your Kubernetes infrastructure in Kubernetes
Monitoring on Grafana Cloud. Thank you.

