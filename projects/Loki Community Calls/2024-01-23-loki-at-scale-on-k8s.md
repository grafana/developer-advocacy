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

* What's the problem we're trying to address? Why do we need a guide for scaling Loki? Don't you just embiggen everything?
	* Tradeoff: Loki is light on ingest, but more expensive to query at scale.
	* Risks if too small
		* What's small? About 30GB a day, a few TB a month
		* OOM, dropping logs, slow query performance, HTTP 5xx
	* Risks if too big
		* Cost: FinOps
* Scale of our own Loki deployment
	* The range of our clusters (2 PB/month, multitenant and single tenant)
	* We query 100x/200x of what people ingest (if a customer does 300 TB/day, they can do 100x/200x for querying that)


### Sizing and Scaling Loki

* Is there a specfic deployment version of Loki that users should be using at scale?
	* Monolithic and distributed
	* Note: We're deprecating SSD. You should use distributed mode now.
	* Why is distributed the best architecture for scaling Loki?
		* Allows you to scale read and write paths independently from each other.
* When we look at scaling Loki for a customer, what key metrics do we need to consider?
	* Amount of logs ingested and queried
	* Number of users that will be querying Loki at the same time
	* Cost and complexity of running and maintaining (self-hosting vs SaaS)
* Talking about Ingest first:
  * What key aspects of ingest effect sizing? Throughput, payload size. 
  * What particular components of Loki will we scale to handle large ingest scenarios?
    * (Check out our infrastructure video - add YouTube card later)
    * Ingesters
    * Distributors: should be half the number of ingesters as a rule of thumb
  * Is there a particular time period they should aggregate this over? For example: estimated amount of logs per day?
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
- Check it out [in the docs here](https://grafana.com/docs/loki/latest/setup/size/)
* What is it?
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
