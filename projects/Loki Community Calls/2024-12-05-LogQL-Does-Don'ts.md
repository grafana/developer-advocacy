# 2024 / 12 / 05 - LogQL Does and Don'ts

Hosts -  Nicole & Jay

Loki Engineer - Cyril Tovena

## Community Questions

- Results cache. What is actually cached and when? Critireas to enable the cache. How to tune cache configiration and behavior, how to measure the impact of config changes? How does Grafana configure caches for SaaS?
- Any plan for LoqQL to support nested queries?
- How do we optimize loki read path where regex matching timesout with loki Microservice.
- I am looking for a query to get me all non-JSON logs as I am looking to make my logs format compliant in my organization, we parse the json fields and generate labels from it so this non-JSON logs are a missing piece of information during troubleshooting.
- For loads around 70-100Gb logs per day, Which loki is feasible simple scalable or distributed
- About Querying and Cost per query, Is Chunks per Query a good metric to track the cost? I am assuming that Chunks are S3 Objects and the pricing to fetch are few cents for a thousand requests.
- I am looking to get my most expensive queries and whether they are efficient or not (for example, 1GB of logs that fetch 100,000 Chunks is not great)


## Jay and Nicole Questions



