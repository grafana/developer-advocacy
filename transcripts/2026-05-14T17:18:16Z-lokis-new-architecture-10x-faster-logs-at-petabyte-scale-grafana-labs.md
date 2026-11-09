# Loki&#39;s New Architecture: 10x Faster Logs at Petabyte Scale | Grafana Labs

Published on 2026-05-14T17:18:16Z

## Description

Loki's original architecture was designed for one job — and it excelled at it. But petabyte-scale structured logging demands ...

URL: https://www.youtube.com/watch?v=0yJPA_xwON0

## Summary

The show titled "Loki's New Architecture: 10x Faster Logs at Petabyte Scale" was published on May 14, 2026. The speakers included Poyzan, Ben Clive, Jason Nochlin, and Trevor Whitney, all members of the Loki team at Grafana Labs. They discussed the new architecture of Loki, focusing on improvements in log ingestion and querying capabilities, including the introduction of a columnar storage format called DataObjects and a new query engine that significantly enhances performance. Key takeaways included the ability to handle petabyte-scale structured logging more efficiently, achieving up to 20 times less data scanned and 10 times faster query execution, as well as the implementation of a new indexing system to improve the speed of "needle in the haystack" queries. 

Topics: Loki architecture, DataObjects, query engine, log ingestion, indexing, performance improvements.

## Chapters

00:00:00 Overview of Loki's new architecture and its evolution
00:06:16 Overview of Loki's new write path with Kafka
00:11:50 Improvements in Loki's query execution and storage format
00:18:04 Overview of the new query engine in Loki
00:23:29 Features of DataObjects in Loki's new architecture
00:29:38 Improving LogQL and log ingestion for better performance
00:35:04 Introduction of new indexing technology for Loki
00:41:15 New Loki architecture and features

Thank you, Mat. Hi everyone, it's me again. I'm Poyzan. Today, we have Ben Clive, Jason Nochlin, and Trevor Whitney with us. We all work for the Loki team. In this session, we will walk you through the internals of our new architecture. If you were in the keynote, you got a preview and have probably seen this slide earlier, but today, in this hour, we want to unpack what exactly we are changing and, more importantly, why we are changing.

Let's do a quick look back. How did we end up here? In the good old days, we used to have plain text files on servers. We would SSH into the box, try to find a file, try to find the line, and hope that after a certain time, we were in the right box. Then came phase two, where we started aggregating those logs on a dedicated server and graphing over the lines. This made it simpler to search, but it was impossible to scale because it was limited by the size of the box.

Next, we entered phase three with dedicated specialized logging services, and this is where Loki entered the picture. Now, we are already in phase four, where structured logging is the default. As I mentioned before, OpenTelemetry adoption is also accelerating this. Now we have meaningful key-value pairs that represent something about infrastructure or our business logic.

But let's take a pause here. In phase three, Loki changed the game. The core principle was that we didn't have to index every line. Instead, we would select a subset of streams and then search within them. These design decisions made Loki incredibly easy to operate and cheaper to run compared to the alternatives. And it worked. The numbers show it: nearly 30,000 stars and over 400,000 deployments in the wild. Loki is the backbone of observability in many organizations. However, this success is bringing new demands and questions, such as "How many failures did each user experience in this time period?" This is a fundamentally different workload than what Loki is designed for. 

That's why we're changing the fundamentals. We group our current bottlenecks into four categories, and each of us will walk you through one of these today. Loki has outgrown the initial trade-offs of the write path design. The three times the application and ReadWrite coupling had a reason for it, but now they are becoming operational bottlenecks for us. To answer queries in the new structured logging world, we have to read multiple dimensions from every log line. "Dimension" is a generic term here; we mean fields and key-value pairs. 

Again, back to the question: "How many users experienced a failure in this time period?" This requires two answers: the responses and users. However, Loki has to parse the entire line, and we know that up to 97% of the log message is not needed to answer this question. Loki is doing a lot of work to answer the question in the way it's designed, and we are also trying to reduce the work that it's doing at a time. Finally, looking for a specific log line with no direction to look in—no stream selectors—is slow by definition; it's like searching for a needle in a haystack. We are also going to present new perspectives for this.

Here are our four solutions. In a second, I'm going to walk you through the new write path. Ben and Trevor will tell you all about the columnar format and the new query engine, and Jason will give us new perspectives on how we can solve the needle-in-a-haystack lookups.

Let's do a mini deep dive. This is Loki today: writes come into the distributors, and they get fanned out to three zones. Ingesters will buffer logs in memory, compact them, and flush them to object storage. On the read side, the front-end query charts query into smaller bits of work, and then it either queries them against the object storage or caches in between or forwards the queries to ingesters to be executed. Notice that the ingester sits on both paths.

So, let's revisit why Loki is designed this way. To make it highly available, Loki chooses to serve reads from memory, so they are immediately available the moment you send them. However, at the scale we operate now, a heavy query hits and it will slow down writes, resulting in 500 errors for the end user. A heavy query can also move ingesters if it's asking too many streams at the same time.

Moving on to the second point: making it durable. Loki decided to replicate data three times and aims to flush them at the same time using the timestamp. However, when the ingesters go out of sync—and if you remember, they have a tendency to do that quite frequently—it results in duplicates in the object storage. These duplicates have to be deduplicated at query time.

The third point is a difficult one to reason around. Currently, Loki distributors are distributing the streams by hash ID. This results in high throughput chunky streams on the same ingesters sometimes, creating imbalances in the workload. We have mitigations around this, like auto stream tuning, but it's hard to tune even for highly skilled operators like ourselves at Grafana. So it's also hard to manage for us. Remember, these are not bad decisions for what Loki was designed for; it was optimized for the write path, but pushing it to its scales means these trade-offs now compound.

Now, for the new write path: we introduced Kafka to our write path. Distributors are now writing to the durable stream layer, Kafka, and each partition is now consumed by an ingester. As writes are acknowledged before the ingesters, we now have the option to completely separate the read and write paths without compromising high availability. Kafka allows us to replay data with an "off-star" right, so data is processed once and exactly once without compromising durability. We can now move the replication to Kafka and remove it from ingesters. 

Finally, unlike hash stream ID-based hashing, Kafka gives us the option to partition by volume. It provides us with a lot of configurability, enabling more uniform workloads among the ingesters. We have to be honest here: we resisted any major dependencies for a long time. Loki's identity has always been its simplicity, and we are aware that adding Kafka introduces significant operational complexity. However, at the scale we are pushing to, running the existing Loki is not any easier comparatively. 

So, reconsidering the design trade-offs we just discussed, we believe this complexity is now justified. To recap, the new world on the new write pipeline gives us complete write isolation from reads. There are no moving ingesters and no compute overheads. We can already see our liabilities even better, and we are not compromising on high availability. The new Loki can partition by volume, making capacity planning quite predictable instead of being reactive. Kafka gives us more knobs to play around with different partitioning models, allowing us to further optimize how much responsibility we give to the write path or the read path to put each data together.

We are still cost-efficient. Data is written once. Imagine when you replicate data; you have to pay for the compute, memory, and network of replicating that data in running components. Then, in the object storage, with the dimension problem of duplicates, you duplicate data and pay for it. In the read path, you again have to pay for the compute to deduplicate. Even after the new costs of running Kafka, when we remove the cost of duplicates and deduplication together, we can see up to a 30% reduction in our largest clusters. This is significant and transformative for large-scale deployments.

There's more we can list here. Kafka enables us to experiment and iterate faster by adding more topics and exploring different processing and partitioning models. The new streaming layer is the foundation of the new flexible data pipeline. Thank you for walking with me through the new write path, but this is only halfway; we just...

discussed how the data gets in. Now I want to hand it over to Ben Clive and Trevor Whitney to tell you all about how the data gets out. 

(upbeat music) 

(audience applauding) 

- Nice job. 

- Right, thank you Poyzan. So now you've heard all about the write path. Trevor and I would like to talk to you about the query path, in particular, the queries that Loki processes today that are inefficient and how we improve them using a new query engine and storage format. 

We've seen an increase over the last few years of users looking for more business insights from their logs. What are business insights? They are looking for more information related to your business from your logs rather than related to your systems. You can see a simplified example here of a question that might be asked: how many failures did a user experience? You can see the LogQL metrics query that would get you an answer to that question. 

These queries today are expensive for Loki to execute, but we have improved them. We'll dig into exactly how in a second. But first, let's look at the improvements we've made. We have 20 times less data scanned and 10 times faster query execution for these kinds of business queries. This is a really big achievement for Loki. I also want to say that it's just the beginning. We're still working on this area, we're still doing research, and these numbers should improve over time. 

First, let's dig into each of these different pieces and see how we improve them, starting with the data reduction. There are a lot of factors that go into this, but we'll just look at the main one, which is challenges with Loki's current storage format. Loki today stores this log data in a format called chunks. We can see that up to 97% of chunks are storing log lines. That leaves just 3% of the data being things that are not log lines; they're timestamps and any structured metadata you send us. 

This is the heart of the storage challenge for Loki because today it will download and process all of this data regardless of whether it's needed or not. The domination of the log lines within the chunks means that queries can't easily target a subset of the data that we have. A typical chunk contains around eight megabytes of uncompressed data, leaving around 200 to 300 kilobytes of non-log data, which includes the timestamps and the structured metadata. 

Even if we could pull all of that data into one place and read it out, we still make a lot of requests from a lot of small files, and that's not very efficient. Unfortunately, chunks are a row-based format as well, which means this data is interspersed with the log lines. So we can't even do that. Based on all of those factors, we decided that Loki would perform better if it had fewer larger files that could store the timestamps and the metadata separately in contiguous blocks that could be downloaded and processed independently. 

So that's exactly what we did, and these are all features of columnar storage. I want to introduce DataObjects, a new columnar storage format for Loki built specifically for logs. We'll go into a bit more detail on what makes the DataObjects good for Loki, but first, we're going to pass over to Trevor, who's going to talk to you about the query execution times. 

- Thanks, Ben. So I want to talk about the other performance improvement Ben mentioned, which is 10 times faster query execution, and we're going to tell you how we achieve that with the new query engine. But before we do that, let's refresh our memories on how the current query engine works. 

So before I dive into this, who in the audience has struggled with cardinality in Loki before? I have. So definitely some of you. Cardinality has always plagued us because it impacts density, and that in turn impacts the amount of data that Loki needs to scan to answer a query. 

Today, reads come into the query front end, they get split by time and charted, sent to the scheduler where they're picked up by a querier. These queriers operate on chunks, and these chunks can have significantly different density. What I mean there is how many of the log lines in that chunk are relevant to the query that you are running? Often, the log lines aren't pertinent to the query, but Loki still needs to read that log line in many cases to determine that. So the size of the log line dominates the performance of the query. 

As we have seen in the evolution of logging, as Poyzan mentioned in the keynote, we are seeing an increasing number of dimensions in logs today. Now the query path must scale up to keep up with those increasing dimensions. 

You do not need to read this slide. It is a lot of words, I understand that, but I did want to include this because this comes straight out of the 2018 design document that Loki was originally designed around. I wanted to talk about the original design for Loki because I wanted to highlight that despite these challenges of the log line dominating the query and the current architecture, Loki is still an efficient performing and scalable database. 

We have scaled it to what some might say, using an embarrassing degree of parallelism to scale to the loads that we need to be able to handle with our open source and our cloud customers. In this paragraph, as you can see, there was a discussion about storing structured event-based data, about answering analytical type queries, and then specifically concluded with this is not something we are targeting with the system. 

So I bring this up to highlight that the query engine of today is not broken, but the query engine of tomorrow will unlock so many new use cases. This is going to open my conversation about the new query engine, the Loki that we have today. The query engine of today is designed to operate at the level of the log line. The new query engine is going to be able to operate below the log line. This means its performance will no longer be tied directly to the size of that log line. It's going to allow us to answer more questions at a bigger scale. 

And this is all possible thanks to DataObjects and the way that they're structured, allowing Loki to do less work. So here's the new query engine. It looks a lot like the old one, but there are some significant differences here. So let's talk about those. 

When a query comes in, the first thing that we do is write a comprehensive query plan. This includes a logical plan, a physical plan of how to actually read that data, and a clear execution strategy. What this allows us to do is pull out optimizations and then push them as far down the stack to exactly where they can be the most useful. 

The plan is split into fine-grain tasks for scheduling with these optimizations pushed down into them. This allows the DataObject scan work to scale out elastically and read less data during scans. Finally, this work is distributed via a tenant-aware queue, so the system is protected from any noisy neighbor queries that another tenant might be running. 

The key optimization to this whole new query engine was to read less data. By detecting predicates early, we can push them exactly where they're needed, allowing us to filter early and only process the dimensions needed for that specific query. 

I may use the word dimension a few times; I might have already. So just real quickly, what I mean there is just any queryable property of a log. In this example, service, response, user, those are all the queryable properties here and dimensions. 

Okay, so how do we do this? Let's walk through the new query engine using this query as an example, and we're going to show off how we achieve that 20x reduction in data and those 10x faster query executions. 

So the query comes in. The first thing we did, as I mentioned, is plan. So today, with chunks, you often have to read the whole log line to answer any query about it. And log lines can be broken up into many different parts. So for example, in this log...

the detected fields. So we want to improve that experience by pre-parsing and storing this data in columns.

Next, let's talk about the challenges with log retention. As we scale up, the amount of data we need to retain becomes a concern. We want to ensure that we can keep logs for the necessary duration without overwhelming our storage capabilities. This is where our retention policies come into play. We are working on making these policies more flexible and easier to manage, allowing users to define how long they want to keep their logs based on their specific needs.

Another area we are focusing on is improving the user experience with our query language, LogQL. We want to make it more intuitive and powerful, enabling users to write complex queries with ease. This includes better documentation, examples, and potentially new features that can simplify common tasks.

Lastly, we are also looking into enhancing our observability features. As we continue to grow, having visibility into the performance and health of our systems becomes increasingly important. We want to provide users with the tools they need to monitor their logs effectively and gain insights into their applications.

In conclusion, while we have made significant strides with the new query engine and DataObjects, we recognize that there are still challenges to address. We are committed to continuously improving Loki and providing our users with the best possible experience. Thank you for your attention, and we look forward to your feedback and questions.

the fields in your log lines. Pre-parsing those would allow that endpoint to perform and be exhaustive, comprehensive, and performance scale. But part of the reason we haven't done this yet is because it's going to exacerbate another problem we have, which is the problem of ambiguity.

So here we have a few different statements you might see in a LogQL query. And before I go into this section, let me first say, LogQL is great. I use it every day to find the exact logs that I need. So, you know, we have no plans to add complication to that language. However, LogQL was built during the specialized logging services stage that Poyzan mentioned in the keynote, and it was not built for this expansion of dimensions that we're seeing in logs today. As a result, LogQL has no way to allow the user to specify specific types of metadata, like where is this field? Oftentimes, the query engine can determine it, and that's great; we can push those optimizations down to our scanning nodes. But when we can't determine it, we have to read any possible column that it could be referencing, and that increases the amount of work we need to do. 

So we look forward to solving this and further improving the performance of analytical queries. Stay tuned for improvements in that space.

Another area we're still working on is log ingestion and defining an optimal read layout for the log data. One of the big things we wanted to solve with DataObjects was avoiding a lot of small reads from a lot of objects. Unfortunately, if you're not careful, we still have that problem in DataObjects, and that kind of starts naturally at ingestion time. We need to spread out the incoming logs into many different machines in order to handle the incoming load. That means we get a lot of different DataObjects of a fixed size to spread out the data. However, when we want to query that data, the query engine actually prefers fewer files that are larger and have more relevant data in each one. 

We do want to figure out how to put those together, but at the moment, they're not really working together; they're at odds with each other. To make this problem worse, all the users of Loki are different. You can imagine different tenants have very different data, but also different teams within the same company will query their logs differently. They might have a different key that they use a lot; maybe they'll search by a different service. All those things mean that there is no one optimal layout, which is why this is still an ongoing research area. But we are making progress here, and we hope to get better at it, and it will improve over time.

Okay, so that brings us to the end of the new query engine and storage section. Loki was built to search your logs, but the next version of Loki that we're bringing today is built to analyze them. We've implemented a new query engine and a new storage format to do that, bringing sublinear query times as your dataset grows. All of these will bring more insights from your logs, more queries, and more scale. 

But there is still one type of query that Loki struggles with, and that is the needle in the haystack we mentioned already. Now luckily, we have Jason here who's going to talk to us about needle in the haystack and the advances that he's bringing to Loki next.

---

Good job. Thank you. Thank you, Ben and Trevor. I'm Jason Nochlin. I recently joined Grafana a few months ago, which I'll talk more about in a second. I'm excited to talk about how we're bringing needle in the haystack query acceleration to Loki.

Traditionally, adding indexes to petabyte-scale log storage required picking between two bad trade-offs. Either you go with the low-cost, easy-to-operate solutions like Loki, but that puts a lot more work on the end users that are making the queries in order to have efficient queries. So you end up with situations like you're trying to debug an incident at 2:00 AM, and you can't remember the right label selectors to use to actually find the request UUID that you need to solve the incident. 

On the other side, there are solutions out there that offer full indexing, but that comes with a much higher cost, which leads to stress for the person paying the bills. Not only was this situation making our users sad, but this was also holding Loki back from becoming the product that Grafana wanted it to be. 

We can boil it down to three requirements on this problem: we want to offer indexing that brings low-cost overhead, high precision, and is object storage native. That has not existed before, but there have been some attempts to solve this. 

Who knows what this is? Bloom filter, that's right, a probabilistic data structure. This is what got me interested in this story. I've spent a lot of time with Bloom filters. At a previous startup, I used Bloom filters and some state-of-the-art variations of them to bring a novel approach to change data capture for database replication. 

So when I learned about the observability challenges and how people were trying to use Bloom filters to build data skipping indexes over logs, that immediately got my attention and nerd sniped me into this problem space. 

Now, Bloom filters are a very clever solution, and they have a lot of power, but they have some fundamental limitations that show up when you try to bring them to scale. Based on my prior experience, it was clear to me that they were not the right foundation to use to solve this problem. That really came down to these three things:

1. Bloom filters are typically thought of as a compact data structure, but at this scale, you end up having indexes that were nearly the size of the original dataset, leading to high storage overhead.
2. They are expensive to query; the random nature and the hash function computations associated with Bloom filters can lead to significant CPU usage and poor cache locality.
3. The typical architectures for this type of skipping index will build a Bloom filter per some section of the data, resulting in a number of Bloom filters to search that is proportional to the size of your data, which means higher query latency with larger amounts of data.

So, very expensive to query. On a related point, the random nature makes them not suited for object storage. The poor cache locality results in an inability to read them directly out of object storage with things like efficient remote reads. Typically, to bridge that gap, you need to put in more expensive infrastructure in front of object storage to serve Bloom filters efficiently.

And that's where Logline entered the story. Logline was a company I founded around two years ago, and we ended up coming up with a novel solution to this problem. Grafana got very interested in that solution, and in December, I joined through the acquisition of Logline to bring fast needle in the haystack searching to Loki while maintaining the low-cost profile that everyone has been accustomed to.

So we are introducing a new index to accelerate needle in the haystack queries to Loki. The Logline technology is powering this and was a natural fit for Loki's architecture, primarily around being written in Go, which helped. 

On an operational basis, the new indexes are completely decoupled from the Loki write path. So there's no operational coupling, which is great for keeping Loki easy to operate. It also allows us to organize data in the indexes in a way that's best for searching and keep data organized in the primary query engine in a way that's best for all of its operations. 

This gave us a great way to create these indexes. It's object storage native, so Loki builds these index files and then uploads them to object storage. At query time, we do efficient range reads directly into the index files without needing any additional infrastructure. We've put a lot of effort into tuning these indexes to be highly precise.

For needle-in-the-haystack type searches, we are really focusing on what information we need in the index to find UUIDs, IP addresses, and other unique types of identifiers. We are clearing out redundant information, like timestamps that appear on every log line, which typically clutter indexes. By removing them, we can keep the index much smaller while maintaining precision.

There are also some tricks to keep these indexes, enabling very fast searches while keeping costs low. We do not use Bloom filters for this; instead, we've implemented some custom approximate, probabilistic data structures based on bitmaps and custom hash maps associated with that. The result is an index that has less than 20% storage overhead, and the structure lends itself to predictable lookup costs. The cost to query the index, in terms of resources to read from object storage, is proportional to the size of the query in time. Longer queries will have a higher lookup cost, but it is not dependent on the size of the data. So, whether it's terabytes or petabytes, we will maintain low latency and low cost on the query path to add search capabilities.

This is how it will be integrated into Loki on the query flow. We have a function that detects exponentially expensive queries because there is some latency associated with the index. We want to ensure we're only invoking it in cases where it helps. When we identify one of those large queries, we parse it and probe the index with the search terms, which returns a list of likely matches of locations in the data where the query result may be. We then pass the likely matches off to the new columnar storage engine for efficient processing to find those log lines within the identified regions.

Does it work? We seem to be getting great results in the initial development environment. For example, I ran a query looking for a UUID with no label filters. With Loki today, the estimated data volume was 3.5 terabytes. When I executed this query, I encountered a client timeout, hitting the resource limits in this environment, which I believe was around 60 seconds. With the new indexing, we were able to filter the 3.5 terabytes down to only eight gigabytes of logs we needed to scan to find this UUID and return the result of finding that exact needle in just a few seconds.

As I mentioned, the technology was acquired in pretty early form, and we have been focused on integrating it into Loki to ensure it works at scale. The next step is to bring this into Grafana Cloud to verify the index for correctness and tune all parameters to optimize it for the various needle-in-the-haystack use cases that customers are using. Later this year or early next year, we will bring this into an OSS public target for the community. In addition to this new indexing, there are some other great things coming to Loki open source. 

Now, I’ll bring Trevor back up to talk about that. 

---

Hello again! As Jason just mentioned, everything we've talked about today is either already in the Loki repo, the open-source repo, or planned to be there as soon as we are able. I'm really excited for all these features to land in open source. 

One thing you may be wondering is how many people in the audience run their own Loki stack? Anyone here? That's a lot! That's awesome; I love that. Now, how many of you are wondering, "Do I need Kafka?" Let's talk about that. 

As Poyzan mentioned, we are committed to the monolithic mode, also known as the single binary installation. If you are running a small instance of Loki that can fit on a single machine, you will not need Kafka. That is our commitment to you. However, if you are running a distributed system, then you will need Kafka, as that will be our new orchestration mechanism for a distributed system. The trade-off is that, yes, it may add slightly more complication to your install, but you'll be able to handle much larger scale. As Poyzan mentioned, we're seeing 30% reductions in costs at equivalent scale, so I think the trade-off will be worthwhile.

We have been running this new architecture ourselves in both our internal operations environment and a few production cells. As a result, we have developed some tools to safely migrate and run this system. Those tools are also available in the open-source repository today. 

What this looks like is writing into Kafka and having two consumers out of Kafka. We have a consumer that writes chunks, which looks a lot like the ingesters of today, but it reads from Kafka instead. Then we have the new consumer that writes DataObjects. In front of these two different storage types, we have two different query engines. There are the queriers of today, which read from chunks, and then there's the new query engine that I just presented. 

By running both query engines, you can continue to query any chunks that your system might already have, and you can run the systems in parallel until those chunks age out of their retention period. Then you can switch to just using the DataObjects. To allow you to run both query engines, we have a new component in the open source called the Query T, which is configurable with a few different routing modes. You can configure it to always favor the chunks response, always favor the new response, or have the responses race and return whichever one is faster. This component has all sorts of metrics, so you can monitor the correctness between the two and ensure that the new engine is producing results similar to how the old engine worked.

That's it for the new Loki architecture. We are going to bring everyone back up on stage for questions, but before we do, I just want to let everyone know that all four of us will be at the Ask the Experts booth directly following this talk. If you have questions that don't get answered, please come find us. 

There is onplay.grafana, and there is a Loki data source called Loki DataObjects that is using the new architecture. This is still actively in development; not all queries are going to be faster, but some will. So, find the ones, especially those analytical ones, that are performing better and continue to look at that data source as we develop this. That's available in the demo, the self-serve demo booths that are all around. 

Finally, there's a Loki architecture banner; I think I saw one over there. I don't know if there are more than one, but go take a picture and then come find us at the Ask the Experts booth if you have any questions. 

With that, come on back up everyone! 

---

[Announcer] Trevor and the team, everybody, please give it up for them. Thank you so much, excellent!

## Raw YouTube Transcript

- Thank you Mat. Hi everyone, it's me again. Up, yeah, I'm Poyzan. Today there will be Ben Clive, Jason Nochlin and Trevor Whitney. We all work for the Loki team. And in this session, we will
walk you through the internals of our new architecture. So if you were in the
keynote, you got a preview and you have seen this
slide probably earlier, but today in this hour, we wanna unpack what exactly we are changing and more importantly, why are we changing? Let's do a, you know, quick look back. How did we end up here? So in good old days, we used to have plain
text files on servers. We would SSH into the
box, try to find a file, try to find the airline,
and you kind of hope after a certain time you
were in the right box. And then came phase two, we started aggregating those
logs in a dedicated server and graphing over the lines. Yeah, it made it simpler to search but it was impossible to scale because it was limited
by the size of the box. And then there came phase two, dedicated specialized logging services. This is where Loki entered the picture. And now we are already in phase four where structure logging
is now the default. Like I said before, open telemetry adoption
is also accelerating it. Now we have meaningful key value pairs that either represent
something about infrastructure or our business logic in it. But let's take a pause here. In phase three, Loki changed the game. The core principle is we didn't
have to index every line. And on top, we would
select a subset of streams and then search within them. These design decisions
made Loki incredibly easy to operate and cheaper to run
compared to the alternatives. And it worked. The numbers show it, right? 30,000 stars nearly, over
400,000 deployments in the wild. Loki is the backbone of
Observability in a lot of organizations, but this
success is bringing new demands and questions like how many failures did each user experience in this time period is a fundamentally different workload than what Loki is designed for. So that's why we're
changing the fundamentals. So we group our current
bottlenecks into four and each of us gonna walk you
through one of these today. Loki has outgrown the initial trades off of the write path design,
three times the application and ReadWrite coupling
had a reason for it, but now they're becoming
operational bottlenecks for us. And then in order to answer queries with the new structure logging world, we have to read multiple
dimensions from every log line. Dimension is a generic word here. We mean fields, key value pairs. But again, back to the
question, how many users experienced a failure in
this time period requires two answers, the responses and users, but Loki has to parse the entire line and we know up to 97% of the
log message is not needed to answer this question. Loki is doing a lot of work to answer the question
in the way it's designed and we are also trying to reduce the work that it's doing at a time. And finally looking
for a specific log line with no direction to look
in, no stream selectors, is slow by definition, needle
in the haystack queries. So we are also going to present
new perspectives for this. So here's our four solutions, in a second, I'm gonna walk you through
the new write path. Ben and Trevor will tell you
all about the columnar format and the new query engine. And Jason will give us new perspectives on how we can solve the needle
and a haystack, lookups. So let's do a mini deep dive. This is Loki today. Rights come into the distributors, they get fanned out to three zones. ingesters will buffer logs and memory. They will compact them and
flush the object storage. And on the read side, front end query, front end charts query
into smaller bits of work and then it either queries
them against the object storage or cache in between or forwards the queries to
ingesters to be executed. Notice that the ingester
sitting on both paths. So let's revisit why Loki
is designed this way, to make it highly available, Loki choose to serve reads from memory so they are immediately available
the moment you send them, but in return at the scale we operate now, a heavy query hits and
it will slow down writes and will result in 500s to the end user. Or a heavy query, again,
can move ingesters if it's asking too many
streams at the same time. So moving on to the second
one, making it durable, Loki decided to replicate data three times and it aims to flush them at the same time using the timestamp. However, when the
ingesters go out of sync, and if you remember they have the tendency to do that quite frequently, it will result in duplicates
in the object storage and these duplicates have to be deduplicated at the query time. And the third one is a
difficult one to reason around. So Loki currently distributors are distributing the streams by hash ID. This results in high
throughput chunky streams on the same ingeters sometimes and it creates imbalances
in the same workload. We have mitigations around
us like auto stream tuning, but it's hard to tune even for highly skilled operators
like ourselves in Grafana. So it's also hard to manage for us. Remember, these are not bad decisions for what Loki was designed for. It was optimized for write path, but pushing it to its scales. These trade offs now compound. So the new write path, we introduced Kafka to our write path,
distributors are now writing to the durable stream layer, Kafka, and each partition is now
consumed by an ingester. As writes are acknowledged before the ingesters,
now we have the option to completely separate read and write path without actually compromising
on high availability. And then Kafka allows us to replay data with an off star, right? So data is processed once and exactly once without
compromising on durability. We can now move the replication to Kafka but remove them from ingesters. And finally, unlike a hash
stream ID based hashing, Kafka gives us the option
to partition bar volume. It gives us a lot of
configurability around us. So it enables more, you
know, uniform workloads among the ingesters. We have to be honest here, we resisted to any major dependencies for a long time. Loki's identity has
always been its simplicity and we are aware that
adding Kafka is a big operational complexity. But the scale as we push to , running existing Loki is not
any easier comparatively. So reconsidering the design trade-offs that we just talked about, we believe this complexity
is justified now. Let's recap, the new world on the new write pipeline gives us complete write
isolation from reads. So no moving ingesters,
no compute overheads. We can already see our
liabilities even better and we are not compromising
on the high availability. And new Loki now, can partition by volume and capacity planning
becomes quite predictable instead of being reactive. And Kafka gives us like
more knobs to play around with the different partitioning models so we can further optimize how
much responsible to we give to the write path or the read path to put each data together. We are still cost efficient. So data is written once, imagine when you replicate data, you have to pay the compute memory and network of replicating that
data in running components. And then in the object
storage with dimension problem of duplicates, you duplicate
data and pay for it. And then in the read path,
you again have to pay for the compute to deduplicate again. So even after the new
costs of running Kafka, when we remove the cost of
deduplication or duplicates and deduplication together,
we can see up to 30% of reduction in our largest clusters. This is significant transformative for large scale deployments. So there's more we can list here. Kafka enables us to experiment and iterate faster by adding more topics, exploring different processing
models, partitioning models. So the new streaming
layer is the foundation of the new flexible data pipeline. Thank you for walking with
me the new write path, but this is only the
halfway, we just discussed how the data gets in. Now I wanna hand it over to Ben Clive and Trevor Whitney to tell you all about how the data gets out. (upbeat music)
(audience applauding) - Nice job. - Right, thank you Poyzan. So now you've heard all about write path, Trevor and I would like to talk to you about the query path,
in particular, the queries that Loki processes today
that are inefficient and how we improve them
using a new query engine and storage format. So we've seen an increase
over the last few years of users looking for more
business insights from their logs. What are business insights? When it's looking for
more information related to your business from your logs rather than related to your systems. You can see a simplified example here of a question which it might be asked of how many failures did a user experience? And you can see the LogQL metrics query that would get you an
answer to that question. These queries today are
expensive for Loki to execute, but we have improved them. We'll dig into exactly how in a second. But first let's look at the
improvements we've made. So we have 20 times less data scanned and 10 times faster query execution for these kinds of business queries is,. This is a really big achievement for Loki. And I also wanna say that
it's just the beginning. We're still working on this
area, we're still doing research and these numbers should
improve over time. First, let's dig into each
of these different pieces and see how we improve them. Starting with the data reduction. So there are a lot of
factors that go into this, but we'll just look at the
main one which is challenges with Loki's current storage format. Loki today stores this log
data in a format called chunks. We can see that up to 97% of
chunks are storing log lines. That leaves just 3% of the
data that we saw being things that are not log lines, they're timestamps and any structured metadata you send us. This is the heart of the
storage challenge for Loki because today it will download and process all of this data regardless of whether it's needed or not. So that domination of the log
lines within the chunks means that queries can't easily target a subset of the data that we have. A typical chunk contains
around eight megabytes of uncompressed data and that leaves around 200 to
300 kilobytes of non log data. So the timestamps and
the structured metadata. Even if we could pull all
of that data into one place and read it out, we still make
a lot of requests from a lot of small files and that's
not very efficient. Unfortunately, chunks are
a row based format as well, which means this data is
interspersed with the log lines. So we can't even do that. Based on all of those factors, we decided that Loki would
perform better if it had fewer larger files that could
store the timestamps and the metadata separately
in contiguous blocks that could be downloaded
and processed independently. So that's exactly what we did and they're all features
of columnar storage. So I wanna introduce
DataObjects, a new column of storage format for Loki
built specifically for logs. We'll go into a bit more detail in what makes the
DataObjects good for Loki. But first we're gonna pass over to Trevor who's gonna talk to you about
the query execution times. - Thanks Ben. So I wanna talk about
the other performance improvement Ben mentioned, which is 10 times faster query execution and we're gonna tell you how we achieve that with the new query engine. But before we do that,
let's refresh our memories on how the current query engine works. So before I dive into this, who
in the audience has struggled with cardinality in Loki before? I have. So definitely some of you. Cardinality has always plagued
us because it impacts density and that in turn impacts the
amount of data that Loki needs to scan to answer a query. Today, reads come into
the query front end, they get split by time and charted, sent to the scheduler where they're picked up by a querier. These queriers operate on chunks and these chunks can have
significantly different density. And what I mean there is
how many of the log lines in that chunk are relevant to the query that you are running? Often, the log lines aren't
pertinent to the query, but Loki still needs to read that log line in many
cases to determine that. And so the size of the log
line dominates the performance of the query. As we have seen in the
evolution of logging as Poyzan mentioned in the keynote, we are seeing an increasing number of dimensions in logs of today. And so now the query path
must scale up to keep up with those increasing dimensions. You do not need to read this slide. It is a lot of words, I understand that, but I did want to include this 'cause this comes straight out
of the 2018 design document that Loki was originally designed around, the original design document for Loki. And I wanted to talk about
the original design for Loki because I wanted to highlight
that despite these challenges of the log line dominating the query and the current architecture, Loki is still an efficient
performing and scalable database. We have scaled it to what some might say, using an embarrassing degree
of parallelism to scale to the loads that we
need to be able to handle with our open source
and our cloud customers. And in this paragraph, as you can see where there was a discussion
about storing structured event-based data, about
answering analytical type queries and then specifically concluded with this is not something we are
targeting with the system. So I bring this up to
highlight that the query engine of today is not broken, but the query engine
of tomorrow will unlock so many new use cases. And so that's gonna open my conversation of the new query engine,
the Loki that we have today. The query engine of today is designed to operate at the level of the log line. The new query engine is gonna be able to operate below the log line. This means its performance
will no longer be tied directly to the size of that log line. It's gonna allow us to
answer more questions at a bigger scale. And this is all possible
thanks to DataObjects and the way that they're structured and allowing Loki to do less work. So here's the new query engine. Looks a lot like the old one, but there are some
significant differences here. So let's talk about those. So when a query comes in, the first thing that we do is we write a
comprehensive query plan. This includes a logical
plan, a physical plan of how to actually read that data and
a clear execution strategy. What this allows us to do
is pull out optimizations and then push them as far
down the stack to exactly where they can be the most useful. The plan is split into fine
grain tasks for scheduling with these optimizations
pushed down into them. This allows the DataObject scan work to scale out elastically and read less data during scans. Sorry. Finally, this work is distributed via a tenant aware queue. So the system is protected
from any noisy neighbor queries that another tenant might be running. The key optimization to
this whole new query engine was to read less data. By detecting predicates early,
we can push them exactly where they're needed and that
allows us to filter early and only process the dimensions needed for that specific query. I may use the word dimension a few times, I might have already. So just real quickly,
what I mean there is just any queryable property of a log. So in this example,
service, response, user, those are all the queryable
properties here and dimensions. Okay, so how do we do this? Let's walk through the new
query engine using this query as an example and we're
gonna show off how we achieve that 20x reduction in data and those 10x faster query executions. So the query comes in. The first thing we did
as I mentioned is plan. So today, with chunks you often have to read the whole log line
to answer any query about it. And log lines can be broken
up into many different parts. So for example, in this
log line, I've kind of grayed out the log line
'cause it's not as important and I'm highlighted the
stream labels associated with the log line as well
as some key value pairs that were included. A structured metadata with this log line. With DataObjects, we store these different
dimensions in their own columns. This allows us to selectively
read those columns. And at the planning stage is where we sort of figure out the pieces
that are gonna be needed and so we can push them down into the plan where they're needed. With chunks, the philosophy
was read everything and then filter. In the new query engine, we filter early, scan selectively and we only process the dimensions needed for that specific query,
which of course results in faster queries over less data. - If we take a look at the whole log line, we can actually see
there's more properties, more than just the stream labels and the structured metadata
that Trevor already mentioned. We also have the
timestamp, the log message, and detected fields. Each of those are a candidate to be pulled into a
column in storage in order to speed up these queries. But not all of these
dimensions actually get pulled into storage. Here you can see the same
data that we just had but pulled into a columnar format, you can see the timestamp, the
log message and the response and user structured metadata is all there. The notable exception
is the detected fields. We don't currently pull those
into columns in storage, but we still process them
as normal on the query path. We'll talk a bit more about that later about why we didn't do that. So let's work through this
data in a small example and see how do we execute a
log query over columnar data and how is that better? There's two main steps we would
take for a query like this. The first one is to
scan the response column for the string failure. And then for any matches, we will read out the relevant columns for that row. By not reading the other columns for rows which don't match
that response filter, we save ourselves bytes
that we need to process and ultimately saving on query time. But can we do any better? We can see that for a
metric query, we don't need to read the other columns at
all for any matching rows. We can simply filter the response column for the failure as before. But then we don't need to
read out the log message, the timestamp and the user, we simply count the number
of rows that matched. As we've seen previously,
a significant portion of our data is in the log message. So if we don't have to read that, we can save ourselves a huge
amount of bytes, a huge amount of compute, and ultimately
a huge amount of query time. Let's drop down now to
the storage layer itself and talk a bit about the DataObjects. Loki obviously is a object
storage friendly database. So our DataObjects are always
also object storage friendly. Some of the features we have that work well here are
front loaded metadata. That means that all of the
metadata about what's in a DataObject is at the front of the file. So that's the columns, the
pages, the byte ranges we have or any statistics that we need. And that means we can quickly read and discard a whole object's worth of data very quickly if it doesn't contain any data that we need. We also support multi-tenancy
as a first class citizen. That means that if you're running Loki in a cloud environment with many tenants against a shared bucket, you won't have any concerns with sharing your data between people. Finally, accessing data in a DataObject is low latency by design. You can read any range of bytes in just two round trips to object storage. The first one will read
the front loaded metadata, decide what byte ranges it needs, and then we fetch all the bytes that we need in another trip in parallel. Beyond those object storage features, DataObjects have a lot of
features that are common to many columnar file formats, but actually they're
also perfect for logs. The first one are various encoding and compression strategies
available on every column. This is particularly good in logs because we see that a lot of metadata keys have very similar values. You can think about the
Kubernetes pod name for example. They all tend to start with
the same few characters, which means we get very good compression. We've seen up to 1000x
column compression here. We also have full support
for sparse columns. Again, this is very important for logs because not every log line
will have the same key defined on it, which means a lot of log lines won't have a
value for a particular column. So by supporting sparse
columns via presence bitmaps, we can scan data very quickly and decide whether we need to read any data from those columns. Finally, we have paged access to the data, which means we can read a
small amount of data at a time and process it efficiently. It also means we can
cap the maximum amount of memory we need to use to do a read, but on the flip side, we
can allocate more memory, read more pages at once and get even faster
queries based on the amount of memory we have available. This level of control
means that we can avoid out of memory events in a lot of cases and it makes it much easier to
size our tasks to our queries that can run the actual queries. Right, so that brings us to the bottom of our query execution stack. I'll hand you back to Trevor to go back up and put it all together. - Great, thanks Ben. So yeah, this is just putting all
these pieces back together as we go back up the stack here. So as Ben just described,
we can selectively scan data so that for this query we
only need to know the user and the response column. So that's in blue. We can reduce the amount of
data that we read when scanning that data using those
predicate push downs, those logical bits that we
detected in the query plan, we pushed down to the scan nodes, these areas represented
by these gray lines where we only need to
actually pull the rows where the response is failure. And then finally we do
all this work in batches using the pages that Ben mentioned. So you can see here the
vectorized execution in red. We can do this sort of one
piece of data at a time. Going back up one level, and here you can see the query at the top. I have an admission,
Ben, this query is wrong. So someone who's been working
on Loki for five years, I screwed up a LogQL query. So the next time you screw
one up, just remember that. But we're missing the by
user aggregation here. So imagine that that's there. And here, we're in the aggregation phase. We reduced the data
that we need even more. We already evaluated the
response equals failed predicate when scanning data. So here we actually only
need the user column to aggregate over the user. This targeted IO reduces memory overhead as well as unnecessary computation cycles. This results in faster
queries for the users and more controllable load for operators. So that's DataObjects and the new query engine, which greatly improves the experience of running Loki at scale. And you know, you may be
thinking to yourself, wow, they thought about everything,
they solved every problem, but there are a few still out there. So I'd like to talk about, or we'd like to talk about a few of those. The first one being detected fields. So as Ben mentioned earlier, there is often structure
in the log line itself. And historically, Loki has always had to parse this structure at query time. So for example, right, the
duration and method here. In the new query engine,
I'm very excited to announce we still parse this information at query time, but we hope
to stop doing that soon. If we're able to pre-parse this data, put it into columns, we're gonna get all of
those columnar advantages we get from the other metadata. This would also greatly improve things like the detected fields endpoint. Anyone in the room use
log drill down before? Love log drill down. Awesome, excited to hear that. It relies on this endpoint, which is right now, a best effort sampling of the fields in your log lines. Pre-parsing those would allow
that endpoint to perform and be exhaustive, comprehensive
and performance scale. But part of the reason we
haven't done this yet is 'cause it's gonna exasperate
another problem we have, which is the problem of ambiguity. So here we have a few different
statements you might see in a LogQL query. And before I go into this section, let me first say, LogQL is great. I use it every day to find
the exact logs that I need. So, you know, we have no
plans to add complication to that language, but LogQL was built during the specialized
logging services stage that Poyzan mentioned in the keynote and it was not built for
this expansion of dimensions that we're seeing in logs today. As a result, LogQL has
no way to allow the user to specify specific types of metadata. Like where is this field? Oftentimes, the query
engine can determine it and that's great, we can
push those optimizations down to our scanning nodes, but when we can't determine it, we have to read any possible column
that it could be referencing and that increases the
amount of work we need to do. So we look forward to solving this and further improving the
performance of analytical queries. So stay tuned for
improvements to that space. - Yeah, another area
we're still working on is the log ingestion and
defining an optimal read layout for the log data. One of the big things we wanted to solve with DataObjects was avoiding a lot of small reads from a lot of objects. Unfortunately, if you're
not careful, we still have that problem in DataObjects and that kind of starts
naturally at ingestion time. We need to spread out the
incoming logs into many different machines in order to
handle the incoming load. That means we get a lot
of different DataObjects of a fixed size to spread out the data. However, when we want to query that data, the query engine actually
prefers fewer files that are larger and have more
relevant data in each one. We do want to figure out
how to put those together, but at the moment they're
not really working together. They're at odds with each other. To make this problem worse, all the users of Loki are different. You can imagine different
tenants have very different data, but also different teams
within the same company will query their logs differently. They might have a different
key that they use a lot, maybe they'll search
by a different service. And all those things mean that there is no one optimal layout, which is why this is still
a ongoing research area. But we are making progress here and we hope to get better at it and it will improve over time. Okay, so that brings us to the
end of the new query engine and storage section. Loki was built to search your logs, but the next version of Loki that we're bringing today
is built to analyze them. We've implemented a new query engine and a new storage format to do that. Bringing sublinear query
times as your dataset grows. All of these will bring more
insights from your logs, more queries and more scale. But there is still one type of query that Loki struggles with and that is the needle in the haystack
we mentioned already. Now luckily, we have Jason
here who's gonna talk to us about needle in the haystack and the advances that he's
bringing to Loki next. (upbeat music) - Good job. Thank you. Thank you Ben and Trevor. I'm Jason Nochlin. I recently joined
Grafana a few months ago, which I'll talk more about in a second. And I'm excited to talk about how we're bringing needle in the haystack query acceleration to Loki. Now, the traditionally adding indexes to petabyte scale log
storage required picking between two bad trade offs. Either you go with the low
cost easy to operate solutions like Loki, but that puts a lot more work on the end users that
are making the queries in order to have efficient queries. And so you end up with
situations like you're trying to debug an incident at 2:00 AM and you can't remember the
right label selectors to use to actually find the request UUID that you need to solve the incident. On the other side, there
are solutions out there that offer full indexing, but that comes with a much
higher cost, which leads to stress for the person paying the bills. And not only was this
situation making our users sad, this was also holding Loki
back from becoming the product that Grafana wanted it to be. There's really three requirements on this. We can boil it down to three
requirements on this problem. We wanna offer indexing that
brings low cost overhead, high precision, and is
object storage native. And that has not existed before, but there have been some
attempts to solve this. Who knows what this is? Bloom filter, that's right, a
probabilistic data structure. And this is what got me
interested in this story. So I've spent a lot of
time with Bloom filters. At a previous startup,
I used bloom filters and some state-of-the-art
variations of them to bring a novel approach
to change data capture for database replication. So when I learned about the
observability challenges and how people were trying
to use Bloom filters to build data skipping indexes over logs, that immediately got my attention and nerd sniped me into
this problem space. Now Bloom filters are
a very clever solution and they have a lot of power, but they have some fundamental
limitations that show up when you try to bring them to scale. So based on my prior
experience, it was clear to me that they were not the
right foundation to use to solve this problem. And that really came down
to these three things. Bloom filters are typically thought of as a compact data structure, but at this scale you
ended up having indexes that were nearly the size
of the original dataset. So they had high storage overhead. They are expensive to
query, the random nature and the hash function
computations associated with Bloom filters can lead
to significant CPU usage, poor cache locality. And then the typical
architectures for this type of skipping index will
build a Bloom filter per some section of the data. So you end up with a number
of Bloom filters to search that's proportional to
the size of your data, which means higher query latency with larger amounts of data. So very expensive to query. And on a related point, the random nature makes them
not suited for object storage. The poor cache locality
results in an inability to read them directly
out of object storage with things like efficient remote reads. And typically, to bridge
that gap, you need to put in more expensive
infrastructure in front of object storage to serve
Bloom filters efficiently. And that's where Logline
entered the story. So Logline was a company I
founded around two years ago and we ended up coming
up with a novel solution to this problem and
Grafana got very interested in that solution. And in December I joined through
the acquisition of Logline to bring fast needle in the
haystack searching to Loki and while maintaining the low cost profile that everyone has been accustomed to. So we are introducing a new index to accelerate needle in the
haystack queries to Loki. The Logline technology is powering this and was a natural fit
for Loki's architecture, primarily around, well, being written in Go with both of them helped. But on a operational basis, the new indexes are completely decoupled from the Loki write path. So there's no operational
coupling, that's both great for keeping Loki easy to operate and also allows us to
organize data in the indexes in a way that's best for searching and keep data organized in
the primary query engine in a way that's best for
all of its operations. So that gave us the great
way to create these indexes. It's object storage native. So Loki builds these index files and then uploads them to object storage. And at query time, we
do efficient range reads directly into the index files without needing any
additional infrastructure. And we've put a lot of effort
into tuning these indexes to be highly precise for needle in the haystack type searches. So really focusing in on what information we need
in the index to find UUIDs, to find IP addresses, to find any other unique
types of identifiers. And clearing out redundant
information like timestamps that appear on every log line that typically clutter indexes. But by removing them we can
keep the index much smaller while maintaining the precision. There's also some tricks
to keep these indexes, enabling very fast search
while keeping the cost low. So we do not useBloom filters for this, but we've used some custom approximate, so probabilistic data
structures based on bitmaps, or yeah, based on bitmaps and some custom hash maps
associated with that. And the result is we have an index that has less than 20% storage overhead and also the structure
of them lends itself to predictable lookup costs. So the cost to query the
index in terms of resources to read them from object
storage is proportional to the size of the query in time. So longer queries will
have a higher lookup cost, but it is not dependent
on the size of the data. So no matter if it's terabytes or petabytes, we'll keep a low latency, low cost on the query path to
add the search capabilities. This is how it'll be integrated
in Loki on the query flow. So we have a function that detects exponentially
expensive queries 'cause there is some latency
associated with the index. So we wanna make sure we're
only invoking it in the cases where it helps. When we identify one
of those large queries, we parse it and probe the
index with the search terms and then that returns us
a list of likely matches of locations in the data
where the query result may be. And then we pass the likely matches off to the new columnar storage engine and have efficient processing to find those log lines
within the identified regions. And does it work? We seem to be getting great results in the initial dev environment. So this was an example
query that I ran of looking for a UUI- with no label filters. We had with Loki today, you would look at, the estimated data
volume was 3.5 terabytes. And when I actually executed this query, I got a client timeout. So this hit the resource
limits in this environment, which I believe was like
something like 60 seconds. With the new indexing, we were able to filter the 3.5 terabytes
down to only eight gigabytes of logs we needed to
scan to find this UUID and return the result of finding that exact needle in a few seconds. So, as I said, the technology was acquired
in pretty early form. So we've been focused on the effort to integrate it into Loki and make sure that it's working at scale. The next step is we're gonna
bring this into Grafana Cloud. So can verify the index
to ensure correctness and also tune all of the
parameters to get it working as best as possible for
the various use cases that the various needle
in the haystack use cases that customers are using. And then later this year, early next year, we will bring this into
a OSS public target for the community. And yeah, that's in addition
to this new indexing, there's some other great things
coming to Loki open source. So I'll bring Trevor back
up to talk about that. (audience applauding) - Hello again. So as Jason just mentioned, everything that we've talked about today is either already in the Loki
repo, the open source repo, or planned to be there as
soon as that we are able. And so I'm really excited
for all these features to land in open source. One thing you may be run wondering how many people in the audience
run their own Loki stack? Anyone here? That's a lot. That's awesome, I love that. And so how many of you are now
wondering, do I need Kafka? So let's talk about that. As Poyzan mentioned, we are committed to the monolithic mode, also known as the single binary installation. So if you are running a
small instance of Loki that can fit on a single
machine, you will not need Kafka. And that's our commitment to you. If you are running a distributed system, then you will need Kafka 'cause that is going to be our
new orchestration mechanism for a distributed system. And the trade-off there is yes, maybe slightly more
complication to your install, but you'll be able to
handle much larger scale. And as Poyzan mentioned, we're seeing 30% reductions
in costs at equivalent scale. So I think the trade
off will be worthwhile. We have been running this
new architecture ourselves in both our internal
operations environment as well as a few production cells. And as a result, we have developed some tools to safely migrate,
to safely run this system. And those tools are also available in the open source repository today. What this looks like, how we're running it today is writing into Kafka and then having two
consumers out of Kafka. So we have a consumer that writes chunks, looks a lot like the ingesters of today, but it reads from Kafka instead. And then we have the new
consumer that writes DataObjects. In front of these two
different storage types, we have two different query engines. So there's the queriers years of today, which read from chunks. And then there's the new query engine that I just presented on. This allows you by
running both query engine, this allows you to continue
to query any chunks that your system might already have, and you can run the systems in parallel until those chunks sort of age out of their retention period. And then you could switch to
just using the DataObjects. In order to allow you to
run both query engines, we have a new component in
the open source we both called the Query T, and it is configurable with a few different routing modes. So you can configure it to
always favor the chunks response. You can configure it to
always favor the new response, or you can have the responses race and you can return
whichever one is faster. And that component has
all sorts of metrics. So you can monitor the sort
of correctness between the two and make sure that the new
engine is producing results similar to how the old engine worked. And that's it for the
new Loki architecture. We are gonna bring everyone
back up on stage for questions, but real quickly before we do
just want to let everyone know that all four of us will be
at the Ask the Experts booth directly following this talk. So if you have questions
that don't get answered, please come find us. There is onplay.grafana, there is a Loki data source
called Loki DataObjects that is using the new architecture. This is still actively in development. Not all queries are going
to be faster, but some will. So find the ones, especially
those analytical ones that are performing better and continue to look at that data source and watch as we continue to develop this. That's available in the demo, the self-serve demo booths
that are all around. And finally, there's a
Loki architecture banner. I think I saw the one over there. I don't know if there's more than one, but go take a picture and then, you know, come find us at the Ask the Experts booth
if you have any questions. So with that, come on back up everyone. - [Announcer] Trevor
and the team, everybody, please give it up for them, thank you so much, excellent.

