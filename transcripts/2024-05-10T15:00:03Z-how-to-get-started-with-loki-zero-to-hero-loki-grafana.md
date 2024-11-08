# How to Get Started with Loki | Zero to Hero: Loki | Grafana

If you were looking for how to get started with Loki, here's a video where Senior Developer Advocates Jay Clifford and Nicole van ...

Published on 2024-05-10T15:00:03Z

URL: https://www.youtube.com/watch?v=1uk8LtQqsZQ

Transcript: - If you wanna get started
with observability, but you only have the time or resources to get one thing done, here's what you should do. You should start with getting logs right. Hi, I'm Nicole van der Hoeven. - And I'm Jay Clifford. - And we're both senior developer
advocates at Grafana Labs. In this video, we'll go over
why you should start with logs and demonstrate exactly
what you need to do to start using a tool called Loki to process your logs right. - Logs play a pivotal role in
your observability arsenal, but they come with their
own set of challenges. In our Intro to Logging episode, we touched upon several of these issues. Firstly, the foremost concern
is storage and locality. Log storage is expensive, and without effective
compression techniques and appropriate storage solution, logs can rapidly consume
available disc space. In many cases, you'll be
monitoring many different logs, which could be located in
different files, systems, or even networks for that matter. Finding a way of bringing
logs to one central location is key to effectively managing
our scaling infrastructure. Secondly, manual searching through logs, especially at scale, quickly
becomes a daunting task that demands significant time
and computational resources. And lastly, the inherent lack
of standardization in logs, characterized by numerous
optional components and varying formatting types, further complicates log
management and analysis. This is why Grafana Labs developed Loki. - At its heart, Loki
is a database for logs, optimized to reduce storage costs, sift through a lot of logs very quickly, and easily handle whatever
weird format the logs come in. Usually databases parse a line like this by using something called an index. You can think of an index
as a way to categorize or split up this line of data so that later when you're
looking for something specific, you don't have to look through every single part of the
database in order to find it. Since logs don't often
come with a structure that facilitates indexing though, what tends to happen is that you have to decide
beforehand on a structure. That can be a problem because
it requires forethought and probably rewriting or at least reconfiguring
part of your component. Loki is a little different in this regard. You don't have to use a
premeditated structure to use Loki. Instead, you just send over
whatever you've got to Loki and it lets you define a few labels that it will use as indexes. Loki will index those labels,
not the rest of the log line, which makes it a lot more flexible. Now, you might think that
this could be a bad thing in terms of finding
that information later, but the magic of Loki is that instead of relying
on a very large index, which remember, requires something that's heavily structured, it instead requires a smaller index, but then parallelizes that
work so that it's still faster. When Loki receives a query, you can have it break
apart that bigger problem into smaller chunks, and then those chunks can be worked on separately and concurrently. This is what makes Loki faster and more cost-effective, too. Loki is also horizontally
scalable and multi-tenant. Loki is really more than
just a database, though. It's a whole log aggregation system. Jay. - Loki is fundamentally a
microservices-based architecture. So what does this mean? Essentially, Loki is built
from a series of components that all work together. For instance, when we
push our log data to Loki, they are picked up by distributors, who handle incoming push requests and validate our data stream. Data is then funny enough
distributed to ingesters, which are responsible for persisting data and shipping it to long-term storage, such as Amazon S3, Azure
Blob, Google Cloud Storage, or even on disk when running locally. Next, we have the query
frontend, scheduler, and queriers who work together to organize
and execute user queries against either persisted
long-term stored data or even log data found
within our ingesters. And there are many other services, such as the Compactor
that merges index files, as well as handing log
retention and deletion, as well as more advanced components such as the rulers and Bloom Compactors. Loki stores our data
in two main file types: index and chunk. Index is where we store our Loki labels, such as log level and source. This index provides us with significantly faster retrieval times when querying for specific groups of logs, whereas chunk is a container
for the log entries themselves, which match the labels
stored within our index. We will dive deeper into labels
and indexing in later videos when we discuss best
practices for ingesting, but for now, it's good
enough to know these basics. Now, have no fear. Although Loki runs best within its microservice architecture form, you can still run it in monolithic mode as a Docker container to start. Nicole, can you walk us through an example of deploying Loki? - Sure, but it's not quite that simple. Let me go through all of the
ways that you can deploy Loki and then I'll show you the
easiest way to get started. There are a few installation
options for Loki. You can use a Helm chart,
you can use Tanka, Docker, or Docker Compose. You can just download the binary or you can even build from source. There are also three
deployment modes for Loki depending on how you configure it. The first one is the monolithic mode, which runs everything as a
single binary or Docker image. The second mode is a simple scalable mode. In this one, you're
deploying via Helm chart, and there is some
separation of components. You get the read, write, and
backend components separately so that you can also
scale them separately. It's kind of like the middle ground between the other two modes. This mode is probably best for anything up to a few
terabytes of logs per day that you're ingesting. Beyond that, you should go
into the third deployment mode, which is the microservices mode. And this is designed for
Kubernetes deployments. You can run components as
entirely separate services. It is also the most scalable and the most flexible and
reliable for production, but it's also the most complex. In this demo, we're going to be going
over the monolithic mode, just as the best way to get started. We're gonna be using a simple demo app called the Carnivorous Greenhouse. If you'd like to follow along, then everything that I'm gonna show you is going to be in this repo right here. So go ahead and click that link. For simplicity, we're gonna
be using the monolithic and Docker Compose methods. And to deploy Loki, we're
gonna need three things. First, we will need to have
a Loki configuration file to specify the Loki settings. Second, we will need to
modify the Docker Compose YAML to include an image of Loki. And third, we need to use a collector to scrape the logs we
need from the application and then send them to Loki. So let's look at the
Loki configuration file. This is all going to be in the repo, so you can copy and paste this right in your configuration file. But essentially we are just defining how Loki is going to operate. There are some things
here that are optional. For example, this
allow_structured_metadata, and then this other flag
pattern_ingester enabled is true. These are going to be for
the Explore Logs feature, which I'll show later. There's a lot of options
here that you can change and modify to your heart's content, but if you're just starting out, then I recommend just
copying and pasting this, and then you can change
what you need to later. The second thing we need to
do is the Docker Compose YAML. Now we're going to be focusing specifically on the Loki part of it. Now you'll notice that the image that I'm using for Loki isn't latest. You could use the latest, but I am actually choosing
to use this version of Loki just because it is one where
I can use Explore Logs later. But you can use latest if you'd like to. And then I'm also specifying that Loki is going to be at the port 3100 on the local machine. We're all ready to deploy this, but let's head back over to Jay, who's gonna talk to us about
how to scrape those logs and get them to Loki, which
is what we call ingestion. - So we have Loki deployed. You might be asking, how
do I get my logs into Loki? We're going to cover this in
more detail in another video, but there are several ways
you can ingest logs into Loki. First of all is Grafana Alloy, which is our open source collector. This supports the
collection, transformation, and delivery of metrics,
logs, traces, and profiles. Alloy is our recommended path for new users ingesting
their logs into Loki. It inherently includes all
of Promtail's features, which we'll get to in a moment. As of Loki 3.0, we also now support native
ingestive OpenTelemetry logs, meaning you can just plug in your OpenTelemetry Collector
directly into Loki. Promtail is a Loki-specific agent designed to scrape local
files and system journals. And lastly, there are third party clients such as Docker driver,
Fluentbit, Fluentd, Logstash, and many, many more. - In this demo, we'll
be using Grafana Alloy as the recommended way
to ingest logs into Loki. So let's have a look at that
Docker Compose YAML again. Where we were looking
at the Loki part of it, I'm gonna scroll up here and you'll see that I also
have an Alloy section. Now this is specifying the
image of Alloy that we want, which is the latest one. It has the ports and a
bunch of other information that we're going to need to set Alloy up. Alloy will also require
its own configuration file. So I've got this here. I won't go too much more into
detail about configuring Alloy because that's a whole separate video, but we're using Alloy to
tail the application logs and the Docker container logs,
and then send them to Loki. So let's go ahead and actually run this. I'm gonna type docker-compose up -d and all of those containers
should be running. So as you can see, there are now four
containers that are started. One for Loki, which is running on 3001. Grafana for visualizing the logs on Loki will be on port 3000. Carnivorous Garden is our actual
application, the demo app, and that's going to be on 5005. And Alloy is going to be
what's ingesting the logs from the Greenhouse app into Loki. And that's going to be on port 12345 if you're using the same
configuration files that I did. This is what the app actually looks like. We are at 5005. I'm gonna go ahead and sign up, and I'm going to type in
a username and a password. Click sign up. And then I can log in. Now I can create a plant. So I'm going to create
a plant named Monster, and I'm gonna put a Venus
flytrap and you'll see it there. Now, just to create some
interest in the logs, I'm also going to toggle on error mode, and I'm going to create another plant, and it'll be a pitcher plant. And you'll see it didn't actually occur. I wonder what happened. Let's
go and look at the logs. Before we look at the logs, we're gonna have to talk a
bit about the query language. See, databases typically have this purpose-built query language for finding things in
that specific database. Well, for Loki, it's called
LogQL, query language. And remember those labels
that we talked about earlier? Well, LogQL uses those to find exactly what you're looking for. So now let's go over to
Grafana, which is at port 3000. Now, an easy way to start off with LogQL if you don't know the language and you don't particularly
want to learn it yet, and you just want to
immediately look at the data, is to toggle the sidebar
here, go to Explore, and then go to Logs. This is the Explore Logs feature, and this is what we enabled
in the configuration. So we're seeing some error messages here with a level of warning. And I want to drill down more into that. So I'm going to select
this unknown service, and then I can now see
all of these messages, the warning ones and the info ones. So I can see, you know, unauthorized or failed
attempt to add plant. And I can see when I've connected and disconnected as a user. So I'm gonna go over to Detected Fields. And a cool thing is without
even creating any queries, I can go to message and see all the different
types of messages that I saw over time. Now, I have just started this, so there isn't that much time yet, but I can already see that there were a few different types of error messages. Now what if you have a question
that you want to answer that you can't find here? Well, you can go ahead and
click on Open in Explore, and that opens up the
traditional query UI. Then you can go ahead and go to Builder. And this is kind of still a
bit more of a visual interface to explore your data. So I'm going to hit Operations here. Let's say I want to find
something in a line. So I'm going to go to Line
filters and I want Line contains, and here I'm going to type warning because that's what I'm interested in. So looking down here, okay, this is showing me all
the times that it had warning and all the instances where
those warnings occurred. So this was just without using
the query language at all. But if you'd like to see it, then you can go back to the code and this is what it looks like. And this way you can sort
of build your own query and then learn the query
language as you go. There's a lot more that you can do to query and visualize logs. There's a command line
interface called LogCLI if you just want to run
queries from your terminal. You can build your own dashboards to visualize your logs with
several types of panels. You can even transform the log data. Remember how we said that if you want to start with observability, you should start with logs? That's because you can
turn logs into anything. - That brings us to the
end of our intro to Loki. So what do we have in store for the rest of our Zero to Hero series? We are going to take each of these key topics
we discussed today and dive deeper into how
they work, best practices, and gotchas learned from our
community and developers. - So if you're interested
in more tutorials from us on how to deploy Loki,
ingest logs with it, and find what you're
looking for with LogQL, then click here to follow along with our Zero to Hero with Loki series. And if you'd like to learn more about visualizing those logs, then click on the link in the description for the Grafana for Beginners series by our colleague Lisa Jung.

