# Inside InfluxDB 3 Core from the Creator Himself: Rust Rewrite, Object Storage, and More | GrafanaCON

Published on 2025-06-07T05:36:44Z

## Description

InfluxDB 3 Core is a complete rewrite in Rust with blazing-fast performance, diskless object storage, native SQL support, and ...

URL: https://www.youtube.com/watch?v=mKu1PIhl2Ms

## Summary

In this video, the speaker, a returning presenter from the first GrafanaCON, discusses the latest release of InfluxDB 3 Core, an open-source time series database. The talk covers the evolution of InfluxDB, highlighting its use cases in metrics and events monitoring across various industries, and emphasizes its new features like schema-on-write, an embedded Python processing engine, and a diskless architecture using object storage. The speaker explains the data model changes, query capabilities, and performance expectations, particularly focusing on recent data queries. Additionally, they introduce triggers for data processing and alerting, and address limitations in the open-source version regarding data compaction. The video concludes with a roadmap for future releases and improvements.

# InfluxDB 3 Core Release Presentation

Hello everybody! I'm excited to be here. I spoke at the very first GrafanaCON in the fall of 2015, which was held in Manhattan at the offices of Squarespace. Today, I'm going to talk about our latest release, **InfluxDB 3 Core**, the open-source version of InfluxDB 3. Here is the QR code for Q&A where you can drop your questions.

## Introduction to InfluxDB

Let's start with some introductory material. If this is review for you, I apologize, but I’ll keep it brief. 

**What is InfluxDB?**  
InfluxDB is a time series database designed for metrics and events. It serves as a backend for creating dashboards in Grafana, which we all know and love. The use cases targeted for InfluxDB and time series data in general include:

- Server and network monitoring
- Application performance metrics
- Sensor data from factories, power, mining, water, waste, agriculture, satellites, and vehicles
- Structured event data

We think about raw events going into the database and how they can be transformed into time series data. For example, logs can be treated as time series data. At its core, time series data consists of a collection of time-value pairs ordered by time, accompanied by some metadata such as sensor ID, host name, or region.

### Two Perspectives on Time Series Databases

1. **Storing Computed or Sampled Time Series**: This approach captures and summarizes data before it goes into the database, mainly for metrics use cases.
   
2. **Yielding Time Series on the Fly**: This perspective focuses on computing time series from raw event data based on queries.

## Data Model in InfluxDB 3

In InfluxDB 3, the data model consists of:

- **Logical Database**
- **Tables**
- **Columns** with various types, including:
  - Time (required in every table)
  - Tags (key-value pairs where values are strings)
  - Various data types: int64, float64, uint64, boolean, and strings

This differs from pure metrics databases, which typically only support labels or tags and a float value.

### Version Comparisons

For those familiar with InfluxDB, here’s how the version 3 data model compares to versions 1 and 2:

- **Version 1**: Used a database with retention policies.
- **Version 2**: Introduced buckets.
- **Version 3**: Uses more traditional relational database terminology, referring to these as databases and tables.

### Line Protocol

One feature of InfluxDB is the **Line Protocol**, a text-based protocol for writing data into the database as it arrives. For instance, in our example, we have:

- Table name: CPU
- Tag set: key-value pairs (all strings)
- Field set: different values collected at that time
- Timestamp

Together, the tag set and timestamp act as a unique identifier for each row.

## Use Cases and Performance Expectations

- **Schema on Write**: You don’t need to predefine databases or tables. When you start the server, it will create these on the fly.
- **High Volume, De-normalized Ingest**: Unlike relational databases, we prioritize performance for ingest and query.
- **Recent Data Focus**: Most users derive value from data less than 24 hours old.

Performance expectations are high, with users generally expecting query responses in tens to hundreds of milliseconds. Automatic data eviction is also a feature, allowing users to keep data for a specified duration and automatically remove old data.

## Evolution of InfluxDB

- **Version 1 (2016)**: Introduced InfluxQL and a custom storage engine.
- **Version 2 (2020)**: Focused on enabling different use cases with the Flux query language.
- **Version 3 (2023)**: Launched a hosted version built on the FDAP stack (Apache Flight, DataFusion, Arrow, and Parquet) with Python integration.

We rewrote the entire database in Rust, moving away from the Go architecture of versions 1 and 2.

## Key Features of InfluxDB 3 Core

1. **Infinite Cardinality**: Users can write data without worrying about cardinality constraints.
2. **SQL Support**: InfluxDB 3 supports both InfluxQL and SQL, addressing user requests for a fully capable SQL engine.
3. **Diskless Architecture**: All data is stored in object storage, facilitating multi-AZ durability and reducing costs.

### Performance and Scalability

- InfluxDB 3 Core is designed for simplicity and speed, making it easy to install and run.
- The architecture allows you to scale independently for ingest, query, and compaction tasks.

## APIs and Querying Data

- We support both V1 and V2 write APIs and have introduced a new V3 write API.
- For querying, you can use both InfluxQL and SQL with various response formats supported, including JSON, CSV, and Parquet.

### New Features in Version 3

- **Last Value Cache**: A fast way to get the last recorded value of time series data.
- **Distinct Values Cache**: Optimized for user interface interactions, allowing quick access to metadata.
- **Processing Engine**: Integrated Python support for data collection, monitoring, and alerting.

## Limitations of InfluxDB 3 Core

Currently, there is no compactor in the open-source release, and while you can write and query data for any historical period, the default query range is limited to 72 hours.

## Conclusion and Future Plans

In the coming months, we will release updates every month, focusing on retention periods, performance improvements, and deployment management tools. We aim to enhance capabilities and flexibility in data types.

That is all I have for you today! Thank you for your attention, and I look forward to your questions!

## Raw YouTube Transcript

Hello everybody. So
I'm excited to be here. I actually spoke the
very first GrafanaCON in the fall of 2015, I think it was in
Manhattan, in the offices of Squarespace. So very different endeavor than this, but today I am going to be
talking about our latest release, InfluxDB three core, which is the
open source version of InfluxDB three. Here is the QR code for
Q&A to drop your questions. So I'll just start off getting
through a little bit of introductory material. So if this is
review for you, I'm sorry, but I'll try to make it
quick. So what is InfluxDB? It is a time series database
for metrics and events. It's a backend so that you can have
dashboards that look like this in Grafana, which we all know and love,
metrics, events, whatever. The use cases that we target for
InfluxDB and time series in general. Server network monitoring, obviously
application performance metrics, sensor data of all kinds, which
is factories, power, mining, water and waste rockets,
agriculture, satellites, vehicles. We've seen all of these
things and structured event data, right? We are not thinking
just about metrics, but we're actually thinking about
raw events going into the database. Tracing perhaps? is
tracing time series data? What about logs are
logs? Time series data. I think you can create time
series from logs obviously. So time series at its core is
this a collection of time value pairs ordered by time with some
metadata associated with it, right? It could be a sensor id, a
host name, a building a region, so a tag key and a value or a label. So two ways to think about
time series databases. The first I think everybody
in the room is familiar with, which is you store computed or sample
time series along with some metadata, right? So this is metrics use cases where you're
capturing this data and you're storing those things. But what
I'd say is that use case, basically you're summarizing data
before it goes into the database. What you're actually
capturing is a summary of some
underlying raw event stream or distribution. The other way to think about time series
databases is you want a database that will yield time series on the fly
based on queries that you have, right? You want to compute time
series from raw event data. So the data model in InfluxDB
three at the top you have a logical database and then you have tables. And then beneath that you have columns
and you have different column types. We have time, which is required in
every single table. In InfluxDB, we have tags which are key value
pairs where the values are strings. And then we have int64, float64, uint64, Boolean and strings. So this is where InfluxDB
differs from say, pure metrics databases. Most of those only support
labels or tags and a float value. We actually support
all these other kinds. Now, if you're already familiar with InfluxDB, this is how the version three data
model compares to both version one and version two. So in version one we had this
database retention policy thing, version two, it was called
a bucket. In version three, we decided to just go with more
relational database terminology. So you have a database
in version one and two, you add a measurement in version three, we just call it a table again to be
more in line with traditional database terminology. And then beneath all of that you
have columns and we can map the schema of version one and
two onto version three. So we have columns and we have
tags as a specific type fields, which are those different
value types. And then time. So one other feature of
InfluxDB is Line Protocol. So it's a text-based protocol that
we created for database writing data into the database as it arrives. So basically pushing up live
streaming real-time data. So in this example we have the
table name on the left, CPU, we have a tag set, which is key value
pairs where the values are all strings. Then we have the field set, which are the different values that
you're collecting at that time. And then the timestamp itself, if you look at the tag
set and the timestamp, you can think of those two combined
as essentially the primary key for the table, the unique tag set and time
basically identifies it's the row ID for all of the field values. So some of the properties
of use cases for InfluxDB. One thing that we do that I think
makes it easier to use is we have schema on write.
When you start up the database, you don't have to create a database, you don't have to create
tables or anything like that.
You start up the server, you start throwing data at it and it
will create the logical database on the fly. It will create the
tables and create the columns. But once you've defined that, subsequent requests will validate
against the schema that you've created. It's high volume, it's
de-normalized ingest. It's not like in a relational database
where you want to get the third normal form and all this other stuff. We're looking for performance on
ingest and on query for this data. We've found that for our
customers and our users, most of the value that they
derive is from recent data, right? Data that's less than 24 hours. They're monitoring and alerting workloads
basically exclusively target data within the last hour. And then dashboards are frequently
in this time range. It's a very performance sensitive
query workload, right? Everybody is using either for real-time
dashboards where they want the responses to be in under a hundred milliseconds, or they're using it for monitoring
and alerting and automation. So generally queries that
take multiple seconds to return are bad for our users. I mean, it's okay if you're doing
that ad hoc here and there, but many of our users expect performance
in the tens of milliseconds to hundreds of milliseconds. We
have automatic data eviction. So you can say, I want to keep this data around for
seven days and I want to have it evicted from the database automatically so that
I free up space and keep my costs down. This is kind of in line with that
thing where most of our workloads are focused on recent data, and that's
where people get their value. So the performance expectations
that we have is that the data can be ingested in seconds or milliseconds.
So if you look at data warehousing, it's frequent to have this ingestion
pipeline where things won't arrive in the data warehouse and show up in queries
for five minutes or 10 minutes or something like that. For our use
cases for operational time series, they need the data to be queryable
within ideally hundreds of milliseconds of actual
generation of that data. Most of these queries are
needle in a haystack queries, so they could be writing a billion
rows of data in a day and that query is asking for a thousand of those rows back, or it's asking for an aggregation
across 10,000 of those rows. So it's really a tiny bit of the data
that you're asking for in every single query, whereas large scale analytic
queries are basically like table scans that churn out statistical
summaries for a bunch of different things. Usually for InfluxDB customers, they handle those elsewhere
in other third party tools. So I wanted to touch on the evolution
of the database really quickly. I am talking about version three, and I know some people are
familiar with the other versions. So we released version one in 2016, and the big things we
had there were InfluxQL, which is a query language that
looks kind of like SQL but isn't. And we had our own custom storage
engine for time series data, and that database was a really
great metrics database. In 2020, we launched version two, and our focus there was not
on the core database itself, but on enabling different use cases
using a query language called Flux that made it possible to push down
a bunch more complex queries and processing into the database itself. And then we went on this journey
building a multi-tenant usage based cloud system, which is the subject of
a whole other talk I could give. So in 2023, we launched the
first part of version three, which was basically a
hosted version of it, of a distributed version of version three. It was built on something
called the FDAP stack, which is Apache Projects
for Flight DataFusion Arrow and Parquet. It uses object
store as the primary data store, and I'll talk about that in a second. And now with the new
version we've just released, it has Python embedded into the database. So you can push down
processing into the database, which I'll talk quite a bit about. So we released this three weeks
ago, just over three weeks ago. Here you can see April 15th, and I
highlighted this other piece here, which is the culmination of a four
and a half year journey of rebuilding InfluxDB. So this has been
a long and difficult road. We rewrote the entire database in Rust. Version one and two were written in Go. So the question everybody has I sometimes
ask myself is why do a big rewrite even though I'm the person who motivated
this whole thing? And the truth is, we wanted to solve three big problems in
the database that everybody, like many, many people were asking us to solve. So the first is this idea
of infinite cardinality. People didn't want to have to think about
the cardinality of the data that they were writing into the database. This metadata here that
describes the time series, these are the drivers of cardinality, but they're also the things that give
you greater and greater precision into the things that you're observing, right?
If you want the ultimate precision, you're going to have
more of these dimensions, they're going to be more unique values, and you're going to have greater and
greater cardinality in your observational data. And we wanted a backend, a storage engine that would be able to
handle this without driving up costs and being totally difficult to
manage and all this other stuff. Now, I mentioned our two other query
languages, InfluxQL, and Flux. And a common request that we had
was people wanted to use sql. They wanted a fully capable SQL
engine that could do things. So this is an example, influx QL query. You can kind of look at it
and it looks kind of like sql. There are a few differences. The nice thing about influx QL is
you can express time series queries, certain kinds of time
series queries very easily. Expressing this in sql, it's not very fun.
This is easy. But the thing is InfluxQL is a language
and as an implementation didn't have all the features that you
get out of a full SQL engine. And for people who are
really familiar with sql, it was different in
sometimes frustrating ways. So we wanted to add support for that. So InfluxDB three supports
both InfluxQL in the V one query, API and sql. And then the last thing we wanted to do
was we wanted to separate compute from storage, both versions one and two, tied compute and storage together. And you had to have a locally attached
SSD for everything that you are storing. But remember I said most of
the values in 24 hours of data, people wanted to have the
historical data available for query, but they didn't want to pay for it
on the most expensive storage medium available. They wanted to use object store.
So we built InfluxDB three around what I
call a diskless architecture. I put it in quotes and now air quotes
because it's diskless in the same way that serverless is serverless, there
are discs ultimately, right? But all the data is an object
storage. This is the write ahead log. This is the actual historical data files. InfluxDB three can run without
a locally attached disc at all. Now you can run it just with a disc. You can specify file
system as the object store, but the benefits of this architecture, you get multi AZ durability for free. It's cheap object storage is
cheap. You have spinning disks. It's also cheap if you want a multi AZ
solution and you're in AWS and you're paying the mobster protection fee
that they charge you for cross AZ network traffic. So it's $23 per terabyte per month. It's 40 cents per million
requests. It's broadly available. We as part of the
process of creating this, we actually developed the
object store rust crate, and we contributed that to the
Apache Software Foundation. And that abstracts away either S3, Google, Azure, and you can use
Minio and Ceph, right? So it's basically object store available
almost in most environments that you're in. And there are
multi-region options, right? Because it's just object store. You can use all the tooling that
works on object stores, which is nice, right? If you want
multi-region, you turn that on. And the really, I mean, one of the great things is we
end up having stateless servers. Now obviously the servers load
up a bunch of state in RAM, but ultimately they're stateless because
you can boot up a new one, a new vm, and just load all the
state from object store. And this makes it operationally simple. It makes it trivial to run a
database inside of Kubernetes, and then you don't have to do stateful
sets and all these other nightmare things that you have to do in
Kubernetes to run databases. You basically just offload all of that
to object store and not worry about it. And this was kind of a
game changer as well, which is Amazon finally
added PutIfAbsent in the fall just this last fall to S3. And that enabled us to build some
things in our enterprise offering that basically make it so that we
use S3 or our object store. Google and Azure already
supported this for years, but we can use the generic
object store abstraction to deal with server management
and state management. So InfluxDB 3 Core is built for
simplicity and speed. As I mentioned, we had a version three
that we released in 2023, but that one was like this distributed
services based thing that was only ever meant to be a hosted platform that
we ran Core and the open source release, we designed it from the ground up to be
something that you could just have on your laptop in a few seconds
or on a server or whatever.
It's easy to get going. It's a one command line install native
SQL and InfluxQL out of the box. As I mentioned, it's optimized for these recent
queries and it has the embedded python processing engine, which we'll get into. So really quickly I'll go through
some of the APIs in the database so you can see the basic
stuff about how to use it. So writing data into the database. So we support the V one and the V two
right APIs so you can point to the database as if it were
influx V one and two, and it will just accept those
writes. We also added a new V three, write API for writing line protocol. And it has a slightly different format
for, well, the format's the same, but it has this accept partial argument
so that you can get better errors back from the API if you have
lines that are not accepted. The other additional piece in V
three is this no sync argument. As I mentioned, it's a diskless architecture where we
actually put the right ahead log in object store. And because of that,
when you make a request, it can wait anywhere from a millisecond
to up to a second by default to write that data and then send
a response back to the client. If you put the no sync option in, it doesn't wait for the flush out to
object storage to return a response. It will do authentication
validation of the data, and then it will put it in the in-memory
buffer to be flushed within a second. So here's an example of doing a
partial write. You can see at the top, we have a write that we've
done and we see okay, there's an error and we get back the
original line that caused the error and what the error is, right? And
you can, in a write request, you can put like 10,000 lines and
one of those lines could be good. And then for the rest you get all these
errors back or you can say false for except partial. And if any one of those lines is
invalid based on the schema validation, it will return an error for the entire
thing and not accept any of them. Everything that's available in the API
also has a command line interface for it. So the actual server acts, the server binary also acts
as a command line interface, A CLI for interacting with the
server. So here we're calling, write specifying a database called Server
metrics and a file that we're reading data from and it posts that up. So for querying data,
we have, as I mentioned, we have the V one query,
API, which is InfluxQL, and that has the same format. So you can point at a V three server
as though we're a V one server for both rights and queries, but we have new HTTP endpoints for
querying either in SQL or in influx ql. You have the different
parameters, the query, the database, you have parameters, so you can
have SQL Parameterize queries. And then finally you have the
format. What format do you want, get the response back in.
We support JSON, JSON lines, CSV, pretty print and parquet. So you can basically send a query query
to the server and get a parquet file back, which is really easy to read, obviously in a variety of data
science work tools and stuff like that. So here's an example. Issuing a query using curl against the
database and getting back JSO lines pretty print is nice. We use this by default in the command
line tooling so that when you execute queries and stuff like that, you'll
get something that looks like this. One of the interesting things we've done
with version three is for all of the APIs where you want to get
information about the server, about say the schema of the data in the
server or the operations of the server, we've exposed all of that
through tables that you query. They're called system tables. So here on the right you can
see this example at the top is this table schema called IOx. That was actually the original
code name of this project, IOx for iron oxide because it's
written in rust, haha nerds and system tables, which I said are like, those are basically state about the
configuration of the server or say the parquet files that we've
stored in an object store. That's our persistence format,
processing engine logs, what queries have run on the server.
And then lastly, the information schema, which gives you information about what
tables exist, what their schemas are. So here we can see we're querying
the query system table to see what queries are running on the server information schema to get
information about the schema. So this is obviously a completely
new feature in version three. I feel like people have been
asking for this feature since 2015, since before 1.0 even came out, which is a fast way to get the last value
of an individual time series or some grouping of time series, right? Just give me whatever the last recorded
value is and I want it to be very, very fast. So we have this now built into the
database called the Last Value Cache. And you can define this and
you can define a hierarchy. So you can say this column is
the first level of the hierarchy. This column is the second level,
and this column is the third level. So in our example here, we have
building then machine, then sensor, and you can execute a query against the
last value cache to get back one sensor or all the sensors for machine A
or all the sensors in a building. So to create the last value cache
here, we have the CLI them using, but this is also accessible through
the API. You specify what the database, what table, the name of the cache, the columns that are actually going
to be the things that the hierarchy is based on, and then the
values you want to store. So querying this. So here we're saying get me the app
and the status columns from the lash cash for the CPU table
and the name apps stat, and then you can see these
results come back. The goal, our performance target for the last
value cash was to return these values in under 10 milliseconds. So
if you're getting one value, if you're getting a hundred,
if you're getting a thousand, we want it to be in under 10 milliseconds. There's obviously going to be
some sort of limit to that. If you say you want a million values
back in under 10 milliseconds, the network is going to want to have
a word with you. But that's the goal. The distinct values cache
is the same kind of thing, but instead of for the most
recent data based on timestamp, this is for keeping metadata, and this is the use case I think of
here is at the top of your Grafana dashboard, you have selectors to drill
down in various things and
you want those selectors to be very, very fast. This is what the
distinct value cache is designed for. Actually, we have a bug, I think logged against Grafana right now
because there's something in flight SQL that it doesn't like, which is the string view that
we're returning the data back. So this hopefully will
work very soon in Grafana. It works in the API and stuff like that. But that's the intention is that it
will enable those kinds of builder experiences to be very, very snappy. And our performance target for
the distinct value cache is under 30 milliseconds. So again, ideally faster than it'll feel
instantaneous to you the user. So here's an example of querying from
the distinct value cache. Alright? The processing engine, this is a big one. It's kind of a blank slate
right now because we just
released it and people have yet to create things. But conceptually what we wanted to do
was we wanted to take the things that people were using.
These are previous parts of InfluxDB, of various versions of the stack, right?
Continuous queries was in version one. Capacitor was the processing
agent we had for the V one stack. It still works with V two and V
three. Flux tasks was part of V two. And then Telegraph obviously
is our data collector, which we still support
and will for a long time. But we wanted something that was embedded
into the database using a language that people already know that's widely
accessible and that quite frankly, every LLM can write for you
anyway. And that's Python, right? And the idea is it would turn the database
into something that could be used for data collection. You could pull data into
the database, you could do monitoring, alerting, you could do all
sorts of different things. So we have triggers. You can create plugins for these three
different kinds of triggers. So there's WAL flush, which is as data arrives, you execute this trigger and
you evaluate the row by row data for something. There's a scheduled task, which is basically like cron or Telegraf
telling it to run every second or 10 seconds or minute or hour or
a day, and then a new one, which is on request. So you can bind to an HTTP endpoint
and execute some arbitrary, some python to find in your plugin and
the return or response to the user. So I am short on time, but I will
try to quickly go through these. So this is an example of the WAL trigger. I don't expect you to totally understand
all of this. And the truth is, over time, hopefully you won't
have to write one yourself, you'll be able to just use one. But you have this specific function
definition called process wall. You get these arguments and then
you can loop through them. You can pass arguments into the plugin. In this case we're saying we're doing
something based on some threshold. So this is basically like a
threshold alert. We do something, there's an API to write
data back into the database, or you can use basically the entirety
of the Python ecosystem to call out to third party services. Right beneath the code example is an
example for how to create the trigger using the CLI. And there you can see we're passing
in arguments that get passed into the function there. The
schedule trigger, again, there's a definition you can
pull arguments out that get passed in through the trigger definition. We can build a query using
the parameterized query, and then you can see the
API where we're actually executing the query and then
looking at the values to do things. This schedule trigger is meant to be
an example of using a plugin to do deadman alerting, to basically execute a query on
some interval and to look for if some sensor or thing stopped
reporting in that interval of time. And this is an example of what it would
look like to create a schedule trigger. So you can see the different arguments
that you're passing in and you can pull that stuff out in the Python
code and a request trigger you can use to basically do ETL. So basically, obviously if you're writing data into
InfluxDB, that's in line protocol, but say you wanted to be
able to accept JSON and you transform that JSON into data
that gets written into InfluxDB, you could create a request plugin
and then bind it to an endpoint and then do that transformation
and write the data in. You could also have it serve out
some static webpage or static asset for this. This is a
little too in the weeds, but the one thing I wanted to
show on the request trigger here is the trigger spec there at the top.
So it says path: json_ingest. So what that will do is it will bind
this trigger to slash api slash v three slash engine slash
and then json_ingest. So everything after slash
engine is basically the
namespace where you can define request triggers and bind
to specific endpoints. There's also a built-in in-memory
cache in the plugin API. And this cache exists on a per trigger
basis. And also there is a global cache. So you can use this for caching
results. You can use this for say, having alert cool downs
or alert rate limiting, that kind of thing. So we've created a public repo
influxdata/influxdb3_plugins where we have some examples and we'll
accept poor requests from people. Everything in this is
just Apache 2.0 licensed, but anything in this repo can
actually be installed really easily. At the command line, you
can create the trigger. And there I'm showing the
file name is actually, instead of looking at
the local file system, it's looking on GitHub in
that repo under examples. And this is actually one
that you could install, which then starts collecting
system metrics CPU, disc RAM network at that time. Alright, really quickly, one of the things I should talk about
is one of the limitations of InfluxDB 3 Core. So we did not create a
compactor inside the open source release.
Unfortunately, like I said, the open source release is focused on
recent data and being a highly performed database for that recent data.
And what that means is, as data is written into the database, we create files in 10
minute blocks of time. So you can do that for any
period of time. In January, we had announced that it was
going to be a 72 hour limit. That doesn't exist anymore. So you can
write data for any historical period, you can query it for
any historical period, but where you are limited is in the total
range of time that you can query for by default. We have set that to 432 files, which is 72 hours worth of time.
You can change that configuration, but as you do that, it will explode the amount of RAM and
all this other stuff that it can use. Now our enterprise offering
is the commercial offering. It has compaction in it. We also have basically a
free for at-home use license. So if you're just using this to track
your boat that's going around the world or using it for your home network or
your home sensor data or whatever, you basically just specify that you're
doing that and there's a free forever license and you can download that and
get started without talking to anybody from influx. One last thing I just wanted to mention
just because I think it's kind of cool, is this Diskless architecture enables
us to create something like this, right? So basically in our Enterprise setup, we actually are able to
completely decouple ingest from query from compaction and have those
pieces be independently scalable from each other. These nodes do not
talk to each other at all. They only communicate or
work together by sharing data in object store, which I think operationally
makes it really interesting. And even if you're using
the open source version, what that means is if you point at object
store and it's running in a container and it goes down, just spin it
back up and you're good to go. You don't have to worry about EBS, you
don't have to worry about managing state. So what's next? So over
the next few months, we're going to do a point
release every month. We'll probably do this for
about six, five or six releases, and then we'll move to quarterly releases. So we'll have 3.1 in mid to late
May with 3.2 in June and 3.3 in July. We're going to be adding retention periods
because we don't currently have that improving performance and adding
tools for deployment management. And we are working on
storage system improvements that will kind of enhance the capabilities
and bring more performance and more schema flexibility and new
data types into the database. That is all I have for you today.

