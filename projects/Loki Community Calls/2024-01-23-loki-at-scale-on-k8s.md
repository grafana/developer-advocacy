# 2024 / 01 / 23 - Running Loki at Scale on Kubernetes

[url](https://www.youtube.com/watch?v=lAr0GwuZHiw)

Hosts -  Nicole & Jay

Loki Engineer - Poyzan Taneli

## Talking points

* Introductions
* Setting the stage
* Sizing Loki and Scaling Loki
* Announcement: Loki Sizing Guide
* Monitoring Capacity of your Loki Cluster

### Introductions

* Nicole and Jay introduce themselves
* Introduce Poyzan Taneli
* What is our topic for today?

### Setting the stage

* What exactly do we mean by running Loki at scale on Kubernetes?
* To set the stage can we talk about the scale of our own Loki deployment?


### Sizing and Scaling Loki

* Is there a specfic deployment version of Loki that users should be using at scale?
* Why is this is this the best architecture for scaling Loki?
* When we look at scaling Loki for a customer what key metrics do we need to consider?
* Talking about Ingest first:
  * What key aspects of ingest effect sizing? Throughput, payload size. 
  * Is there a particular time period they should aggregate this over. For example estimated amount of logs per day?
  * What particular components of Loki will we scale to handle large ingest scenarios?
* Querying:
  * Is there a differnce to how we size querying vs ingest?
  * What components of Loki do we look to scale for scenerios where large amounts of querying is required?
  * Internally we treat queriers like emphemeral stateless components. Can you explain why this is the case?
* Does scaling ingesters impact querying and vice versa?
* Backend Components:
  * Ruler, Index Gateway, Compactor do we need to scale these components differently?
* Cost:
  * Is there a minimum cost to run Loki at scale?
  * How do we measure the cost when running Loki in our own infrastructure?

### Announcement: Loki Sizing Guide

This section talk about the work Poyzan has been doing on the Loki Sizing Guide. 
* what is it?
* Why did we create it?
* How have we used it?
* Demo / Overview
* What should users keep in mind when using the sizing guide?
* When can they ger their hands on it?

### Monitoring Capacity of your Loki Cluster (Optional -  time permitting)

* How can users monitor the current state of their Loki cluster?
* What are the telltale signs that you need to scale your Loki cluster?
* Are there any key safe guards that users can put in place to prevent their Loki cluster from becoming overwhelmed under heavy load?
  * Autoscaling?
  * Alerting?

### Community Questions
