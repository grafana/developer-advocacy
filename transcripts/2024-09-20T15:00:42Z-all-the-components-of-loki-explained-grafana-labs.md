# All the Components of Loki Explained | Grafana Labs

Here are all the components of Loki explained so that you can figure out how many instances of each you need for a resilient Loki ...

Published on 2024-09-20T15:00:42Z

URL: https://www.youtube.com/watch?v=_hv4i84Z68s

Transcript: - Loki can be deployed
in microservices mode. In this deployment mode, Loki is broken down into
several different components, each of which can be horizontally
scaled if you need to. But before you decide how many instances of each component you need, you need to know what each one does. In this video, Jay and I are going to be letting you take a look
under the hood of Loki. We'll break down exactly
what every component does and how they all contribute
to keep Loki ticking. (upbeat music) - To ground our components
in a real world example, we'll use a log processing facility, treating our virtual
logs as real world logs. We will tie each of Loki's components to part of the processing line. Logs will arrive at the
facility, be processed and stored within a warehouse before customer requests come
in to retrieve those logs. So let's start with the components that make up the ingestion process. Where the collected via
collector, SDK or API, our logs arrive at the door of
our log processing facility. This is where our first component, the distributor, kicks in. When lorries of logs arrive, the distributor is our first
point of quality control, making sure our logs arrive as expected with no nasty surprises. It also ensures that
logs comply with a tenant or global limit set
within the Loki config. Essentially, the site
manager may employ rules to protect the performance
of the facility. For example, the lorry can only drop off a maximum number of logs at a
time, also known as batching, and the logs must not
exceed a certain length. After validation, the distributor then distributes these logs to our
next component, the ingesters. This is done via a hash ring. - Hang on Jay. Let's talk
about what a hash ring is. You can think of a hash
ring as a group of instances of the same type of component. Information in the form of log lines comes to this hash ring rather
than to specific instances. Then an algorithm is applied to determine exactly which
instance gets that information. That way, if one of
the instances falls off or a new one joins, then
the flow of data proceeds with minimal disruption. So you can kind of think of a
hash ring as a load balancer, except that a load balancer
typically distributes incoming requests or traffic, whereas a hash ring distributes data. Okay, Jay, now tell us exactly
how this algorithm works. - In our case, ingesters
join the hash ring indicating that they are ready to receive logs. We'll discuss exactly
what ingesters are next, but for now, imagine an
ingester as a production line of debarking and soaring machines. Let's say that we have three
of these production lines with unique IDs; 0, 25 and 50. The distributor then hashes a log stream, which consists of the tenant
and the unique set of labels associated with that log stream. For simplicity's sake, let's
say this hash is to be 15. Based on the hash ring rules, the log stream will be
allocated to the production line with the smallest token larger
than the log stream hash. Which means production
line 25 would get the logs. Now, we need to stretch our
imagination a little bit. Like most distributed databases,
Loki supports replication. Distributors send the same log stream to multiple ingesters
to mitigate data loss should one of the ingesters fail. Imagine our log processing
plant has a cloning machine that replicates logs according
to the replication factor. The hash circle rule applies
to the first ingester but then we move to the next
highest available ingester based on the replication value. With a replication factor of
three, our log stream of 15 would go to ingester
25 like it did before, but then to 50 and then back to 0 to complete the replication. Note that with replication, a quorum of successful writes is needed. For instance, a replication factor of three requires two
out of three ingesters to process the log successfully. Otherwise, the write fails and an error is returned
to the distributors. A load balancer is necessary to properly balance incoming
traffic to each distributor. In a Kubernetes deployment, this is managed by the
Kubernetes service LoadBalancer. Distributors are stateless components making it easy for them to scale and offload as much as
possible from ingesters. After quality control, our
logs arrive at the ingesters, one of the most critical components of our Loki architecture. As we mentioned earlier, imagine an ingester like a production line of debarking and soaring machines. They remove the bark and cut the logs into manageable pieces, preparing them for further
processing and storage. Essentially where we remove the metadata from the log payload and
create our index and chunks. Ingesters have four modes
when they join the hash ring: joining, active, leaving, and unhealthy. When a batch of logs
arrive, the ingester creates or updates a data format
type called chunk. Chunks are containers for
logs that are associated with a specific log stream. In our scenario, you can
imagine all of the logs have a label key called Wood Type, so the logs with the wood type pine are processed into the same chunk, and those of type oak are
processed into a different chunk. Chunks eventually turn
read-only, compressed and then written to object storage. This happens when the current
chunk has reached its capacity or too much time has passed,
or when a flush occurs. A flush is a mechanism for pushing all of the chunks into object storage, essentially clearing out
the entire production line. Flushes also have their
own specific conditions for being triggered,
such as a time interval or when the number of
chunks has reached capacity. When logs are flushed, they are bundled up and assigned a unique hash barcode comprising of the logs
label, start time, end time, and the content checksum. Now, imagine a scenario where
an ingester breaks down. All data that hasn't been
flushed could be lost. This is why replication is
crucial for Loki's durability. However, to further
safeguard against data loss, Loki uses a write-ahead log. The WAL acts like a safety net recording every log entry as it arrives. This log is stored on the
ingester's local file system, ensuring that even if
the ingester crashes, the data can be recovered upon a restart. The ingester essentially replays the WAL to restore all acknowledged logs before resuming normal operations. When using replication, it is worth noting that Loki has deduplication mechanisms that allow ingesters to sync. This synchronization allows 'em to process and cut chunks simultaneously. When all three replicas
have identical data, the chunks will be exactly the same, ensuring that only one copy
of the chunk is written to the object store. However, in the case that one
of the ingester is failing, then clones of the same
log chunks can be written to the object store. These clones are
de-duplicated at query time. Talking of queries, Nicole,
do you want to talk us through the query components? - Sure, Jay. At this point, we have
our logs nicely cut up and waiting for us. Now it's time to actually use them. When we want to retrieve logs or at least parts of those logs, we do a type of structured
search that's called a query. These queries can be
pretty resource intensive because you can imagine, it
would be really difficult to look through every single log for something that you're looking for. Now, in this section, we're gonna talk about three
different components of Loki that all have to do with making
this process more efficient. The query frontend, the query
scheduler, and the querier. It's worth noting though
that the query frontend and scheduler are optional components. Only the querier is technically required for Loki to function. However, we're going to be assuming that all three are
deployed in this example. You can imagine the query frontend is kind of like an order processing desk. When an order or a query comes in, that query goes first
to the query frontend rather than going
directly to the queriers. The query frontend then compiles a queue of all of these orders that have come in waiting for the queriers to work on them. Then for any of the more
complex or larger orders or queries, it breaks those
up into smaller, easier and more manageable bits of work. That way, multiple queriers
can work on them simultaneously or in parallel later. And then when all of this work is done, the query frontend is also what stitches all of those back together. The query frontend also does some caching, so it remembers the most recent orders that have come through in case those are going to be repeated. This is great for when a
user makes repeated queries and quick succession, and it reduces the load on the queriers from having to execute
that query repeatedly. Once a query frontend or
the order processing desk is done processing the orders, those are then sent to
the query scheduler. The query scheduler is kind
of like a production scheduler in that it maintains a production queue. The scheduler is what assigns
jobs to those queriers. Both the query frontend
and query scheduler are stateless components, but because of the in-memory
queue, we do recommend that you have more than
one replica of each for high availability. About two each should be
sufficient for most cases. Now, for the workers on the
query side, the queriers. After the query scheduler has this queue of all of the jobs that need to be done, the queriers go to the scheduler
and get assigned some jobs. Once assigned, those
queriers actually execute the log query language or LogQL. Queriers, they're the ones that
are kind of like the cutting and shaping machines in our facility, in the real world example we have. They process the log data to meet specific requirements, retrieving and shaping the pieces as necessary to fulfill the orders. Interestingly, when a
querier is looking for logs to fill a job, it doesn't go
to the object storage first. Instead, it goes through
the in-memory data of the ingester beforehand. In our real world example,
this would be kind of like going back through the
production line to the logs that have just been processed
before going to the warehouse and looking for the logs there. This improves the
performance and efficiency of how Loki returns
queries by quite a bit. Now, earlier Jay was talking about what happens when an ingester fails and how sometimes we can
end up with duplicate logs. This is when the secondary
role of queriers come in. Queriers also internally
de-duplicate data, which means that when a
log comes through them, they look at things like the
timestamp to the nanosecond, the log message, and the label set, and if all of those things
match for more than one log, then it will delete everything but one. That way, we don't ever
have exactly the same log to the nanosecond, and we only keep the ones that are unique. - We have now covered both the read and write path components of Loki. However, we are not quite done. Some of the components
operate in the background and serve automation roles. Let's take a look. Starting off, we have the index gateway, which you can imagine as the
inventory management system. It keeps track of all of
the processed log pieces. It is responsible for handling and serving metadata queries. Metadata queries look up
the data from the index. For instance, the query
frontend components request the estimated log volume to decide on how to shard user queries. The queriers also request chunk references for a given query
through the index gateway so they know which chunks to fetch. Index gateways can run in two modes. Simple, meaning all index gateways are available for all tenants and ring, which uses a similar mechanism to the ingesters hash ring. I'm now going to hot
potato you back to Nicole to explain what the compactor is. - Thanks, Jay. I guess the compactor in Grafana Loki is kind of like a system that organizes and compresses the inventory
records of a facility. What it's actually
compacting are index files. So what it does is it
downloads those index files that the ingesters made and
put into object storage. Then it merges all of them
into one big index file. It uploads that back to object storage, and then it deletes all of those
other separate index files. So it's doing a lot of tidying up. The secondary role of the compactor is in log retention and deletion. We'll cover those in another video later, but for now, think of it
as clearing out those logs that are past their sell by date or just removing logs that a customer no longer
wants in their warehouse. Next up is the ruler. - The ruler is an interesting component. It's like the quality control department. It monitors the stored logs in two ways. The first is alerting. We'll expand on this in another video, but for now, know that
alerting rules allow you to define alert conditions based on LogQL, and send notifications about firing alerts to an external service. For instance, we might see a high intake of logs containing the log level error that we might want to know about. The second role is recording rules. Recording rules allow you to
run intensive metric queries over your log data at given intervals. For example, they can give
you the current percentage of each log level over the last day. These metrics are pushed
into a time series database like Prometheus, so they
can be retrieved by Grafana. This reduces the overall load
on Loki for costly queries as these long range queries
have pre-calculated results that can be called upon from
this independent metrics store. Much like our log warehouse, keeping a database of
current inventory statistics. The ruler stores its rule
list within object storage and is interacted via an API. And with that, Nicole,
I think we are there. As you can see, Loki is a complex machine with many components and moving parts, working together to provide
an efficient log collection, storage, and query solution. Understanding these components and how they interact is crucial for deploying and scaling Loki. In our upcoming videos, we will dive into your
first Helm deployment, including the freeways
you can deploy Loki. - If you'd like to get started with Loki, then check out this video
where Jay and I walk you through the steps of
getting Loki up and running on your local machine via Docker Compose. Happy Logging.

