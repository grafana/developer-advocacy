# 2024 / 12 / 05 - LogQL Does and Don'ts

[url](https://youtube.com/live/d61nQX-n91c)

Hosts -  Nicole & Jay

Loki Engineer - Cyril Tovena

## Talking points
- Introductions



### LogQL basics
- What is LogQL?
- How is LogQL structured? What does it look like?
- What does "schema at query" mean?
	- How is data stored in Loki for query?
- Where can you run LogQL?
- What is the LogQL simulator?
- What is LogCLI?
- What are the different types of queries and how are they different?
	- Log queries
	- Metric queries
- How do you handle unstructured log data in LogQL?
- *Community question:* Any plan for LoqQL to support nested queries?
- Considerations for what a good query is
	- Functionality
	- Performance
	- Cost
		- In Grafana Cloud, how do we charge for Loki queries?
		- *Community question:* About Querying and Cost per query, Is Chunks per Query a good metric to track the cost? I am assuming that Chunks are S3 Objects and the pricing to fetch are few cents for a thousand requests.

### Query best practices

[docs](https://gra.fan/lokiquerybp)

- When preparing to write a logQL query, what factors should you consider?
- How can Loki users clean up unused or redundant labels?
- [x] What are your top 5 common mistakes when writing LogQL queries?
- Functionality
	- How do you validate the correctness of a LogQL query?
	- How can you test and benchmark Loki queries before deploying them in production?
- Performance
	- What are the key factors that impact Loki query performance?
	- How can you troubleshoot slow LogQL queries?
	- How does caching work?
		- *Community question:* Results cache. What is actually cached and when? Critireas to enable the cache. How to tune cache configiration and behavior, how to measure the impact of config changes? How does Grafana configure caches for SaaS?
	- How does the deployment mode of Loki affect query performance?
		- What usually needs to be scaled up?
		- *Community question:* For loads around 70-100Gb logs per day, Which loki is feasible simple scalable or distributed
		- *Community question:* How do we optimize loki read path where regex matching timesout with loki Microservice.
	- Is it better to format my log line first before running filtering by a field or is it better to use line filters?
	- Can you provide some examples of when and when not to use regular expressions in LogQL queries?
		- *Community question:* I am looking for a query to get me all non-JSON logs as I am looking to make my logs format compliant in my organization, we parse the json fields and generate labels from it so this non-JSON logs are a missing piece of information during troubleshooting.
- Cost
	- *Community question:* I am looking to get my most expensive queries and whether they are efficient or not (for example, 1GB of logs that fetch 100,000 Chunks is not great)

- Can you explain the unwrap function and how it can be used in queries?
- What are some lesser-known LogQL features that users often overlook but can be game-changers?
- What are count_over_time, rate, and bytes_over_time, and how do you decide which to use?

### Specific query scenarios

- Can you write a LogQL query that detects downtime by analyzing log gaps?
- How can you use LogQL to do a count of all unique user IDs or find all logs related to a specific user ID?

## Community Questions

- Results cache. What is actually cached and when? Critireas to enable the cache. How to tune cache configiration and behavior, how to measure the impact of config changes? How does Grafana configure caches for SaaS?
- Any plan for LoqQL to support nested queries?
- How do we optimize loki read path where regex matching timesout with loki Microservice.
- I am looking for a query to get me all non-JSON logs as I am looking to make my logs format compliant in my organization, we parse the json fields and generate labels from it so this non-JSON logs are a missing piece of information during troubleshooting.
- For loads around 70-100Gb logs per day, Which loki is feasible simple scalable or distributed
- About Querying and Cost per query, Is Chunks per Query a good metric to track the cost? I am assuming that Chunks are S3 Objects and the pricing to fetch are few cents for a thousand requests.
- I am looking to get my most expensive queries and whether they are efficient or not (for example, 1GB of logs that fetch 100,000 Chunks is not great)


## Jay and Nicole Questions

### LOGQL

- What are your top 5 common mistakes when writing LogQL queries?
- When preparing to write a logQL query, what factors should you consider?
- Is it better to format my log line first before running filtering by a field or is it better to use line filters?
- Can you provide some examples of when and when not to use regular expressions in LogQL queries?
- What are the key factors that impact Loki query performance?
- How can you troubleshoot slow LogQL queries?
- How do you handle unstructured log data in LogQL?
- Can you explain the unwrap function and how it can be used in queries?
- How do you validate the correctness of a LogQL query?
- How can you test and benchmark Loki queries before deploying them in production?
- What are some lesser-known LogQL features that users often overlook but can be game-changers?
- What are count_over_time, rate, and bytes_over_time, and how do you decide which to use?

### Query

- How can Loki users clean up unused or redundant labels?

### Scenarios
- Can you write a LogQL query that detects downtime by analyzing log gaps?
- How can you use LogQL to do a count of all unique user IDs or find all logs related to a specific user ID?
