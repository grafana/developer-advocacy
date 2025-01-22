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

### Introductions (3 mins)

* Nicole and Jay introduce themselves
* Introduce Poyzan Taneli
* What is our topic for today?

### Setting the stage (7min)

* What's the problem we're trying to address? Why do we need a guide for scaling Loki? Don't you just embiggen everything?
	* Tradeoff: Loki is light on ingest, but more expensive to query at scale.
	* Risks if too small
		* What's small? About 30GB a day, a few TB a month
		* OOM, dropping logs, slow query performance, HTTP 5xx
	* Risks if too big
		* Cost: FinOps
* Scale of our own Loki deployment
	* The range of our clusters (2 PB/month, multitenant and single tenant)
	* We *query 100x/200x of what people ingest (if a customer does 300 TB/day, they can do 100x/200x for querying that)
* With all this mind we do expect you to follow the rules Loki (Best practises, etc)

### Sizing and Scaling Loki (15min)

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
       - Ingesters should show stable memory utilizations and CPU utilizations
    * Distributors: should be half the number of ingesters as a rule of thumb
      * - aggregate all logs together and share log stream based on hash to ingesters
  * How should should i calculate my ingestion?

* Querying:
  * Is there a differnce to how we size querying vs ingest?
    * Bad vs good queries
    * What scenario do I need my logs 
    * Loki brute forces
    * Query best practises need to be in play when querying longer ranges
  * What components of Loki do we look to scale for scenerios where large amounts of querying is required?
  * How do we scale queriers?
    * Queriers are stateless, ephemeral components
    * 20% on default nodes and 80% on spot instances. Help with costs and reactivity to heavier queries
    * Auto scale of queriers are based on the length of queue and number of workers vs ingest pipeline which is resource based. 
  * (Community Question) Our users sometimes query logs for very long time periods - there might be multiple months, 30 days at a time - for services which produce logs at around a terabyte per day. How can we autoscale the queriers so that the queries happen faster and the users don't complain about things being slow? Are there any other ways to increase query performance than scaling more aggressively?
  * (Community Question) Would love to go into depth around tuning of the chunks cache -- this seems to be the biggest bottleneck on the query side for us.
  
  
* Does scaling ingesters impact querying and vice versa?
  * actually querying will impact CPU preasure of the ingesters espically when running recent data queries as we run calculations within the ingesters
* Backend Components:
  * Ruler, Index Gateway, Compactor do we need to scale these components differently?
   *  Compactor verticaly scale
   *  Ruler depends on usecase and how heavily use them
   *  Index gateway depends on if you are running in multi tennant mode (really only maters at 5000+ tenants )
* Cost:
  * Is there a minimum cost to run Loki at scale?
  * How do we measure the cost when running Loki in our own infrastructure?
    * measure based in ingested GB 
* 

### Announcement: Loki Sizing Guide

This section talk about the work Poyzan has been doing on the Loki Sizing Guide. 
- Check it out [in the docs here](https://grafana.com/docs/loki/latest/setup/size/)
* What is it?
* Why did we create it?
* How have we used it?
* Demo / Overview
* What should users keep in mind when using the sizing guide?
* When can they ger their hands on it?
* Jay + Nicole make sure to post blog link: https://grafana.com/blog/2023/08/23/how-we-scaled-grafana-cloud-logs-memcached-cluster-to-50tb-and-improved-reliability/ 

### Monitoring Capacity of your Loki Cluster (Optional -  time permitting)

* How can users monitor the current state of their Loki cluster?
* What are the telltale signs that you need to scale your Loki cluster?
* Are there any key safe guards that users can put in place to prevent their Loki cluster from becoming overwhelmed under heavy load?
  * Autoscaling?
  * Alerting?
* 

### Community Questions

* We are running Loki in an EKS cluster in three availability zones. One of the main cost factors is the cross-AZ traffic caused by the multi-zone architecture. What are the best ways to minimize that cost?