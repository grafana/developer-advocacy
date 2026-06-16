# GrafanaCON 2026 Keynote Livestream

Published on 2026-04-21T20:41:34Z

## Description

Join Grafana Labs CEO and co-founder Raj Dutt, Grafana creator Torkel Ödegaard, and leaders from across the Grafana Labs ...

URL: https://www.youtube.com/watch?v=UazoZQHW0kI

## Summary

In the opening keynote for GrafanaCON, Raj Dutt, CEO and co-founder of Grafana Labs, and Torkel Ödegaard, Grafana creator and co-founder, highlighted the growth and evolution of Grafana over the past decade, celebrating the event's 10th anniversary in Barcelona. They discussed the significance of community and open-source principles that underpin Grafana's mission. Key announcements included the introduction of Grafana 13, emphasizing new features for enhanced user experience, the expansion of AI capabilities with Grafana Assistant available for all users, and the introduction of the Grafana Cloud CLI (GCX) to streamline workflows. Additionally, they presented Loki's new architecture aimed at improving logging performance and the importance of OpenTelemetry in supporting observability. The keynote underscored Grafana's commitment to making observability accessible and useful, as well as its dedication to fostering a healthy community around open-source technology.

## Chapters

Here are 10 key moments from the GrafanaCON livestream along with their timestamps:

00:00:00 Introductions by Raj Dutt and Torkel Ödegaard  
00:02:15 GrafanaCON history and significance  
00:05:00 Torkel shares personal history with Grafana's development in Barcelona  
00:07:30 Overview of GrafanaCON's purpose and community engagement  
00:10:45 Raj discusses Grafana Labs' journey and open culture  
00:15:20 Key statistics about Grafana's growth and user base  
00:22:00 Introduction of Grafana 13 features by David Kalsmit  
00:35:10 Poyzan presents new Loki architecture and improvements  
00:49:00 Ted Young discusses OpenTelemetry updates and stabilization goals  
00:58:00 Mat Ryer highlights AI assistant features and future plans  

Feel free to let me know if you need more details or additional moments!

# Opening Keynote from GrafanaCON

Please welcome Grafana Labs CEO and co-founder, Raj Dutt, and Grafana creator, Torkel Ödegaard.

**Raj**: Hello! Wow, there's a lot of people here. Are we glad to be here to kick off GrafanaCON? Yeah, very cool. My name's Raj Dutt. I'm one of the co-founders and the CEO here at Grafana Labs.

**Torkel**: And my name is Torkel Ödegaard. I'm also a co-founder and CGO. It's great to be here. We're back in Europe for our annual GrafanaCON event. I just wanted to welcome everyone. Our last conference was in Seattle, and this is actually our 10th GrafanaCON, and it's our best and biggest yet by far.

I remember our first GrafanaCON; we had like 30 people in one of our early user Squarespace's office. We thought it was amazing, and our expectations just keep getting reset every year. It's bigger, better, and I think this is going to be the best one yet. 

Barcelona! I'm a huge fan of this city, but I think Torkel - Barcelona recently learned has a special place in Grafana history. Is that true?

**Torkel**: Yeah, that's definitely true. My sister used to live here for more than 10 years. Back in 2013, just a couple of days after I started working on what would become Grafana, I was traveling here for a Christmas holiday. I got a cold that whole day and spent most of the time in bed just working on Grafana nonstop. Even after I got better, I stayed locked in my room working on Grafana. I hardly spent any time with my family; I was already kind of obsessed with what I was building.

**Raj**: So what you're saying is Grafana is actually Spanish? We've been telling people that Grafana is Swedish, and you're from Sweden, but Grafana was actually made in Barcelona?

**Torkel**: Yeah, in a sense. The foundation and key features of the first version were mostly written here in Barcelona. We might have to tell our marketing team about this. Do we need to rename the project? Do you have any ideas?

**Raj**: Well, we could name it Grafaña (Grafanya) or this could become GrafañaCON (GrafanyaCON), but yeah, let's move on.

**Torkel**: All right. Well, like I said, welcome to GrafanaCON or GrafañaCON. I think we're going to go with GrafanaCON. This is our flagship open-source event. It's all about our technology, our community, our open source projects, new releases, and tech talks. It's really a big party to celebrate the wider ecosystem and community. 

It's one of two flagship events we have. The other is ObservabilityCON, which we also have every year. That's where it's more commercially focused, and we talk about our commercial flagship product, Grafana Cloud. But we put on a tremendous amount of events at Grafana Labs every year. It kind of blows my mind. 

We had over 7,000 workshop signups last year, and there were 80,000 people who attended a webinar. We've just got an incredible global marketing and events team that does a stellar job. It blows my mind that we are having multiple events, sometimes on the same day, in all corners of the world. I can't even attend them all if I wanted to. And believe me, I spend a lot of time on an airplane. 

So it takes a lot to put an event like this together. It's a lot of work, a lot of prep, and a lot of logistics. So before we get going, I just wanted to give a big thanks and shout out to our events and marketing team who've worked tirelessly to put this together. Please give them a warm round of applause.

We're here this week to celebrate the wider Grafana community, get an update on what's new from Grafana and our other open source projects, and to hear from speakers across this community about what they've been up to this past year and how they can use these open source tools to solve every new interesting challenge.

The Grafana community is growing, and it's growing fast. New meetups are happening, and we now just crossed over a hundred Grafana champions worldwide. A Grafana champion is someone who doesn't work for Grafana Labs but organizes meetups, events, and teaches others to be better at using Grafana and these open source tools. 

What's exciting is that new champions are emerging through mentorships from other community members and other champions. I think this is a sign of a really healthy community.

For Grafana Labs as a company, "open" has always been our strategy. And with "open," we don't just mean working on open source software. That is still kind of the foundation and core of what we do. The majority of the software we write is still open source, but it's more than that. It's about investing in open standards, standards like OpenTelemetry, and working with open ecosystems like the Prometheus ecosystem and ecosystems that belong to other communities and companies like Elastic or ClickHouse. 

What I think is kind of cool and fun is how Grafana then connects these different ecosystems together, both in the application and through events like GrafanaCON. Lastly, an open culture is also really key to Grafana Labs. It's not just how we do business and communicate internally but also how we share the good and the bad with the community through blog posts about security incidents or talks about outages, like you'll hear later today.

**Raj**: Can you tell us a little bit more about Grafana Labs and our journey?

**Torkel**: Yeah, absolutely, Raj. So like Raj mentioned, an open culture is a big part of who we are. We're always transparent, both internally and externally. Hopefully, you feel that in all your interactions with us as a company. 

I'd like to tell you a little bit about the journey that we've been on as a company for a few minutes and where we're going. This slide kind of represents where we've been and where we're going. My message is that this has been a shared journey that we've all been on. 

Because we're an open source company, we've been on this journey with all of you, and it's been an evolution. Step one and step two are kind of obvious. Who here is using Grafana? Maybe a silly question, right? That's not surprising. 

Step one was really becoming the default dashboard for everything. This was a really fun time in Grafana Lab's history. We had no customers, no revenue, no problems, and no stress. We were just building open source software, trying to make it popular. I miss those days. Life's a lot more complicated now. 

Where we are now is really step three and step four, which we're going to hear a lot about today. We're making observability easier for every software team. We've put a lot of work into that over the last few years, and it's a key theme for this week's conference. 

An exciting thing that's going on more recently is, of course, AI. Internally at Grafana Labs, we've been transformed over the last year, and we really believe that we're at this new paradigm in observability. Agents are going to become a primary consumer of observability tools and data. This will fundamentally change how we all interact and operate our software and interact with observability tools like Grafana.

We're really excited about this change. We don't only want to be the leading open observability cloud; we want to become the leading agentic observability cloud. There's a lot in this keynote and over the next two days that shares our vision on this topic. 

Lastly, we want to take everything that we're doing in IT observability and bring it to the rest of the business over time. This means looking at things not just like requests but maybe revenue, not just latency but maybe LTV. We see a convergence happening of business data and observability data, especially as companies become more software-led.

This is just a little taste of where we've been and where we're going. Obviously, we didn't write this plan in advance 10 years ago. It's a not-so-secret master plan that we wrote retroactively because we've zigged and zagged along the way. This company has always been agile, and it's kind of fun to think about where we're going and where we've been.

Again, I want to reinforce that this journey has been our shared journey. We've gotten so much great feedback, input, and pull requests from so many people in the community, including many people in this room. Thank you all for helping us go on this journey that we're accelerating on as we speak.

Speaking of accelerating on this journey, I wanted to share some key stats regarding Grafana Labs, the company, and the ecosystem. We have 35 million active Grafana users around the world, which blows my mind. There are over a million companies using Grafana.

I just wanted to stop here and go off-script for a second, which is going to alarm Torkel. I'm sure all of you feel the same way, but it's incredible that after 12 years of a project that my co-founder Torkel created, he's still involved in writing code for it almost every day. 

You're going to see features talked about today that Torkel had a hand in. I find that so cool, impressive, and amazing that my co-founder Torkel is still active in Grafana 12 years later on this open source project that he created here in Barcelona. So, please give a round of applause for Torkel!

**Torkel**: Didn't expect that, did you? 

**Raj**: No. So we've got about a million companies using Grafana, and we've got less than 10,000 customers. Now, in the early days, this used to alarm investors. They'd come up to us and say, "Wait a minute, how can you convert less than 1% of your users to customers? That isn't a business model. That's a disaster." These investors did not understand open source.

Generally, those investors that felt that way didn't end up becoming investors because they didn't understand open source. Our model has been very simple from day one. We want to grow an amazingly wide community by creating valuable open source software, and we want to capture a small piece of what is hopefully a very large pie. 

That strategy has really started to work and accelerate over the last few years. Grafana Labs as a company has hit over $400 million in annualized recurring revenue. We're the largest privately held observability company in the world at this point, and there are over 1,600 Grafanistas in 40 different countries that I have the pleasure of working with every day. 

It's just been amazing progress, and I'm super happy with the trajectory that we're on. Speaking of trajectory, there's one more thing I'd like to share with all of you. Who here has heard of the analyst firm Gartner? All right, a fair bit of people. 

Gartner has a quadrant, a magic quadrant, that they publish every year in observability. We made our debut on Gartner's Magic Quadrant about three years ago. In 2023, we made it furthest to the right in terms of completeness of vision, clustered around other top observability companies. 

We're pretty happy with this result, but the reason I'm sharing this is that I think so many of you, our community, deserve to share in this credit. The way we've built this and evolved our product over the last three years has really been with all your help and input. It's been a truly collaborative experience. So give yourselves a round of applause because you've helped us become a leading observability platform.

Okay. So let's move on to what we're really here for—an update of what we've been doing this past year. We've grouped things into three general themes: easy to get started, built for scale, and available everywhere. 

Let's start by diving into what's new in Grafana 13. To help me do that, I want to invite David Kalsmit up to the stage. David has been working on Grafana since 2018, first as a developer, then as a manager and director, and now he's VP of engineering. He's been running the Grafana engineering team for the past three years. So let's give it up for David and let's hear what's new in Grafana 13.

---

**David**: Thank you, Torkel. Thank you, Raj. Hola, Barcelona! Yes, all of Barcelona! I'm David, I run the Grafana team, and I'm here to talk to you about Grafana 13. So much has happened in a year, and I'm excited to show you some of the things we've managed to get into the product since Grafana 12. 

Grafana, as always, is your trusted and reliable source of a single pane of glass. With that comes a huge range of data sources. I’m just dazzled by that number. We stand for open observability, and we don't really mandate where you store your data. We're quite unique in that regard.

Over the last year, we also added a few more data sources, and these are maintained by us now: Jenkins and SolarWinds. So as always, it's a mix of telemetry and productivity signals. We now have 170 data sources in the catalog and with 120 ways to visualize it. If that map checks out, it's really a ton of flexibility.

Let me tell you about one more way to visualize data. Let me introduce you to the Graphviz panel. I know it's only in private preview right now, but it's really cool. Who here has heard of Graphviz? There are a few people. Awesome! 

We have wrapped it in a panel, so now you can define flow charts. Essentially, whatever you can envision in the dot language, which is part of Graphviz, you can visualize in Grafana. You can map metrics onto labels and define how the edges and nodes look based on thresholds in your data. This is extremely powerful.

In this example, we're using Graphviz to render its own rendering pipeline, and that's pretty cool. Obviously, you can showcase your own business processes with this as well.

We're also working on a visual refresh of our main panel components, starting with the gauge panel. I think these are looking pretty slick, and there’s more to come later this year.

Next up is annotations. They’ve been a bit of a pain point for a while, which is a shame because modeling events as annotations can be really powerful when troubleshooting an issue. However, if you have a lot of them, they can overlap, making it difficult to read. 

But we shipped a few improvements! Look at this detail right there. These are our multi-row annotations. You can have a row for deployments, one for incidents, and another for alerts, for example. If you have a lot of them, they can also get clustered.

Next step is dynamic dashboards. This is something we introduced last year. It’s an easy way to make your dashboards more interactive, with a conditional rendering engine that makes them generally more responsive. With tab layouts, you can make them better organized. We’re excited to announce that they are now generally available, so thank you, dashboarding team! 

Personally, I think tabs are cool. Internally, we have a lot of them in our dashboards, especially as Grafana is getting adopted by bigger organizations. We worked hard over the last year to make it easier to onboard whole teams. 

I always wanted a feature where I don't have to start from scratch when working with slides or something like that. I like templates. So right now, we’re shipping Grafana with a few templates based on common methodologies—including DORA metrics, USE method, RED method, and golden signals. 

We're still working on a way to define your own org templates, which will ensure consistency across teams. Templates work as you think they do. Here's an example of the USE method dashboard. You start off with example data and then replace queries or remove panels. The layout is there. You can write the queries yourself or use the assistant.

Next is saved queries. If your organization is anything like mine, there are usually a few people who know how to write queries better than others. These people can now set up the rest of your team for success. 

Saved queries allow teams to agree on what certain queries mean, like "active users." The query can be defined and then shared with your team, bringing consistency. This, combined with dashboard templates, can really help someone who just started out in your team become productive in building powerful dashboards.

My favorite feature is interactive learning paths. We now built something inside the product near the help menu to help users make sense of some of the new stuff. It can show you what you're looking at right now and give you instant help, or it can guide you through a workflow in the product.

The best thing is you can modify these guides to suit your organization and onboard new people. You don’t have to start from scratch; there's a whole catalog of pre-made learning paths in the docs. You can also check them out on play.grafana.com or at the self-demo booths.

All right, let's talk about operations. Who here is running Grafana for other people? Any operations people? More than Graphviz, awesome! This next feature is really going to up your game: GitSync. 

We teased GitSync last GrafanaCON, and we’ve made significant progress. GitSync allows you to manage your dashboards as code with a proper two-way integration. Imagine modifying your dashboards in the UI, creating a pull request that gets reviewed by your team. If it gets merged, it’s saved. 

You can then use other tools to modify the code when it gets merged into the repo, and Grafana picks it up and shows you the changes. We had to rework the data model and architecture to make this work, but now we think it’s rock solid. It’s also a great disaster recovery mechanism. 

GitSync also allows for a proper publishing workflow. You can try new dashboards in Dev, promote them to staging, and then eventually to prod. We’re also bringing you more connectors, not just GitHub, but also GitLab, Bitbucket, and PureGit. This is a great way to manage dashboards at scale.

Speaking of scale, there’s startup scale, enterprise scale, and then there's Google scale. Google's SRE culture has always played a big role in Grafana's engineering. We even make newly hired engineers read the Google SRE book. 

About a year ago, Google approached us to see if it’s possible to run Grafana visualization inside Google for their internal monitoring. I'm super proud to say that this partnership is in full swing. It’s a bit crazy; the company that popularized SRE wants to use our software for exactly that purpose. 

This also brought some interesting enhancements back into Grafana as a product. Google is very disciplined in their approach to monitoring, which is necessary when working with layers of services handled by various teams. They’re big on reusability in dashboards, leading to many new features we’ll showcase in later sessions.

Grafana is your trusted single pane of glass, bringing all your data together, and we’re trying to be more open and composable. One more thing I have for you: you’ve seen the number 170 data sources in our catalog, but we believe there’s room for more. 

We started with a select group of partners who have built the first few apps, and they’re already in the catalog. You can try them out. It’s early days, so we’re looking for feedback on what other apps you would like to see in this marketplace or if you want to partner with us to start publishing your own plugins.

That was Grafana 13, your trusted single pane of glass, giving you new tools to bring teams into your organization. GitSync is finally ready for production, and we have a marketplace pilot that allows you to participate more in the Grafana ecosystem.

Next up, to talk about my favorite logs database, Loki, is Poyzan. Thank you, David!

---

**Poyzan**: Thank you! Hello, everyone. My name is Poyzan. I'm running the EMEA Group in Loki, and I'm very excited today to be here with you to tell you all about Loki's new architecture. 

Loki is designed to be lightweight and operates on the core principle that you don't need to index every bit of every log line. It makes logs available immediately and relies heavily on object storage. It has been excellent at what it does, enabling petabytes of logs data on affordable infrastructure. 

However, we know that the world of logging is shifting, and we are evolving Loki with it. Structured logging is now the default, and OpenTelemetry adoption is accelerating it. Log volumes are increasing along with the number of fields in every log line. 

What used to be a simple error message now carries key-value pairs, including service name, trace IDs, status codes, order IDs, and transaction IDs that contain business logic. The way you query this data is changing too. You're not just grepping over error messages anymore; you're running targeted analytic queries over massive volumes, drilling down by service, aggregating over the status quo, or wanting to gain business insights from those custom fields.

When those queries take minutes or never return results at all, that's where the frustration starts. To meet these new requirements, we are rebuilding the foundations of Loki with three major changes: 

1. An ingestion pipeline that separates reads and writes without compromising on high availability.
2. A brand new query engine that filters data closer to the source and distributes work better.
3. A columnar storage format that natively supports selective reading to enable smart filtering.

Let’s do a mini deep dive. On the left, classic Loki distributes span out writes to three ingestor zones that replicate data, which is then flushed to object storage. The same ingestors are serving recent read queries. 

A heavy query that may need multiple stream selectors can stall your writes, creating operational headaches. Replication comes with costs too. Loki is designed to flush the same data only once to object storage. However, when ingestors go out of sync, it can cause duplicates on the persistence layer.

On the right, we are adding Kafka to our write pipeline. Distributors write to Kafka partitions, and each partition is consumed by a single ingestor. Now, writes are durable before the ingestors, allowing us to completely separate reads and writes. This is a massive win that we wanted for years.

We’re also addressing the duplicates I mentioned earlier. Data shows that Loki can end up storing up to 2.3 times the same log data on object storage, which is considerable when operating at petabyte scale. With Kafka, we guarantee that every log line is written once. When an ingestor dies, a new one will just pick up and replace it, ensuring durability in the process.

Operational complexity in running Kafka is a trade-off, but the read and write isolation with a more robust write path is justified. Let’s move on to the read side. The biggest lever we have for a more performant query path is reading less data in the first place. 

The new query engine filters data closer to the storage layer. What does this mean? The data that doesn’t match your query never enters the pipeline to be parsed, and it’s backed by a scheduler that distributes work over a pool of workers. 

As a result, results are dramatically faster on large range aggregation queries and drill downs. To make this possible, we rely on a format that supports selective reading natively. That’s where columnar storage comes in. 

Loki's original storage chunks made sense for fast flushing and scanning at query time. However, across millions of log lines, filtering a subset of selective fields becomes a bottleneck. The columnar format flips this logic; each field can live in its own column.

For example, if you want to get all the services running at a given time, classic Loki will have to parse every log line and every metadata to filter the service name. Columnar just returns it—and this is still schemaless, so you don’t have to define columns upfront. You can continue to send your logs, and Loki stores and organizes them for you.

Now, let’s talk about results. We are running one of the largest cloud logs instances to monitor Grafana Cloud itself. These numbers are coming from our internal cluster and can handle gigabytes per second throughput, which turns into a couple of petabytes a month. We’re seeing 20 times less data scanned, returning results 10 times faster. 

This is a massive win for the scale at which we operate. These are preliminary results, and we are actively working on different new avenues, so stay tuned for even better performance.

Did we solve it all? Not really. If you ask Loki to get a specific string without using stream selectors, it will still be slow. We call those needle-in-the-haystack queries. Columnar storage does not unlock this out of the box. 

We attempted to solve this problem a couple of years ago, but our solution did not scale. However, we hear you, and we know this is a real need. Grafana Labs made an acquisition to bring Jason Nochlin and his technology to Loki. Jason implemented targeted secondary indexes, which can result in up to a 99% drop in byte scan. This is currently in private preview on cloud first and will be made available on open source data this year.

I hear you asking, how are we going to try this? The new architecture format with all its components will be available on all modes of Loki. We are committed to a great monotonic experience known as a single binary. If you're running Loki locally or on a single node today, we will not force the Kafka overhead on your workloads. 

However, if you need larger scale, Loki distributed is the future. The diagram here represents how we are testing our internal migration strategy. We’re writing both new and old formats and running them against the engine today and the new engine we are developing.

We have an open-source component called Querity that allows you to choose your preferred engine for comparison. This enables us to continue iterating safely and comparing results side by side at any time.

As we move forward to Loki 4.0, we will iterate over a simplified migration path for you and help you there. If you're running Loki via Helm, Tanka, or your own setup, we will meet you where you are. 

Everything we build, we build for scale on open standards, and that’s the Grafana way that we are very proud of. Now, to tell you all about OpenTelemetry, I want to hand it over to Ted Young.

---

**Ted**: Thank you, Poyzan! Hi, everyone. I'm Ted Young, a Grafanista and OpenTelemetry co-founder, back with your friendly neighborhood OpenTelemetry updates. You could definitely say that structured logs were indeed a big event last year in OpenTelemetry. So what's coming up this year? 

OpenTelemetry, as I like to think of it, is a high throughput, high latency organization. We all win when we bet on open standards. I firmly believe that. Grafana Labs has been betting big on OpenTelemetry, and you can see that reflected in all the initiatives and components we've been working on and sponsoring. 

But what’s the project's top goal for this coming year? I'm excited to announce that it's to be as boring as possible. Yes, that's right. You heard me right: boring. Now, that might sound crazy, but it’s actually important to remember that with telemetry, the opposite of boring isn’t interesting; it’s frustrating. 

When you think about it, boring is amazing and it's harder to be boring than one might imagine. This year, we’re trying to get back to our standardsy roots and be as boring as possible. That’s why our top priority is to stabilize all the things. What could be more boring than this? Not changing things.

But it’s actually amazing because it means that we’ve reached the end of the road for the original goals of the project—tracing, metrics, and logs, stable, unified, everywhere. These are the final pieces that OpenTelemetry needs to finally graduate from the CNCF.

So what does stabilization mean exactly? Is it really that OpenTelemetry is so unstable? No, of course not. OpenTelemetry has been in production for years, and we’ve made quite a bit of defacto stable software along the way, but we do have some cleaning up to do to make our software reflect that reality.

Some organizations have security rules that ban the installation of software marked as beta. We want OpenTelemetry to be available to everyone everywhere, which means we need a simple and reliable way to ensure that OpenTelemetry only contains stable packages. That means everything important in OpenTelemetry needs to become 1.0.

The final boss of this stabilization effort isn’t the collector, SDKs, or any other core component; it’s the instrumentation. That’s where the surface area gets enormous. We’ve been stabilizing the core semantic conventions, the data definitions for things like HTTP, SQL, and message queues. 

This is boring but important work, but the real heavy lifting comes in rolling out all of those stable semantic conventions to all the actual instrumentation packages in every single language. 

Going forward, we’ll be engineering a two-stage rollout. Most instrumentation packages are in a state of defacto stable. This means they work fine, they’re safe, they’re reliable, but the data could be better. Identifying these packages and marking them as 1.0 brings our concept of stability better into alignment with user expectations.

Stage two will involve lifting that data to the latest version of the semantic conventions once they become available via another major version bump. This is harder than it sounds, and it’s the last remaining piece. We’ll need to invent new tools and potentially apply new coding techniques to handle the scale of instrumenting all the software on the planet. 

Boring is harder than it looks. But why stop there? What could be even more boring than stabilizing the definition for database queries? How about installing all of these bits? 

In order to make OpenTelemetry work, the correct instrumentation needs to be installed into every application, creating a little matching game. The way this matching game works is that OpenTelemetry first identifies all the libraries and frameworks that your application uses. Then it needs to identify the matching pieces of instrumentation and combine those two things together.

Of course, we have automation that plays this matching game for you, but the only issue is that the way you configure and use those automated tools works differently in every language. Learning how those tools work can make OpenTelemetry difficult to install the first time you try it.

It’s not just confusing; the current automation requires developers to touch every single application one by one. What we want is a single-click way to install OpenTelemetry system-wide. This brings us to the people we like to call operators: SREs, infrastructure teams, sysadmins, and people like that. 

Today, operators can install and manage some parts of OpenTelemetry, basically the collector and OB, plus a couple of languages. However, there are still many cases where it isn’t possible to apply the language-specific automation comprehensively. 

That's a problem—not just because we like the operators, but because at many organizations, it's the operators who are charged with installing and managing observability. Often, operators are the only way to get a quick, consistent rollout across an entire organization.

While it’s fabulous if application teams can manage their own observability, most organizations are designed to give their teams independence. This means trying to do a coordinated rollout where every single team has to do a bit of work will be really difficult. 

But don’t worry, we have a solution. What I would like to call integrated OpenTelemetry: a set of initiatives that, when combined, create a new way to instantly and consistently install OpenTelemetry everywhere. 

Let’s get into how it works, starting with Linux. How should you install OpenTelemetry on Linux? I believe it should be the same way you install anything else: via package management. That’s right! `apt-get install OpenTelemetry` is coming to a Linux box near you. 

Under the hood, OB, the injector, and language automation are doing a lot of heavy lifting to make it work, but you don’t have to worry about any of that. Just install the package, add a few lines to a config file, and by default, everything that can be instrumented will be.

From one machine, it’s easy to scale up everywhere because this is the part of the system that operators control. If you’re using Kubernetes, it will be just as easy. We’ve had an OpenTelemetry operator for a while, and it’s a popular solution. 

With these additions, all its current limitations will be removed. Of course, if you’re familiar with the Instrumentation Hub from Grafana Cloud, it will use the same mechanisms under the hood to manage these bits for you. 

Right now, we’re only focused on Linux, but once we stabilize things here, we plan to look at Windows and Macs next, as well as potentially looking at development environments, not just production. This is integrated OpenTelemetry: easy for everyone to install, easy to scale, amazing, simple, boring. Just the way we want OpenTelemetry to be.

All right, so enough with all the boring stuff. Let’s have some actual fun and excitement. For that, I believe you need a British accent. So I’d like to welcome Mat Ryer up onto the stage to talk about artificial intelligence and all the amazing things going on in that department.

---

**Mat**: Thanks, Ted! Amazing. Hello, everybody. I'm very excited to tell you about the continued investment we’re going to make into AI here at Grafana Labs. We want to be a first AI-native platform, and that means dealing with non-deterministic inputs that we see now.

It means dealing with scale. Now, anybody can write complex queries by prompting in natural language through the assistance or through agents. It also means making sure that the APIs are giving data back in a way that the agents can deal with without blowing out the context window.

Now, more than ever, we’re dedicated to building safe, secure, and actually useful AI. We take this quite seriously. We don’t want to ship slop. We don’t want to be a slop shop. Everything we deliver, everything we’re doing here is about guaranteeing that when we ship something to you, it will actually make a big difference in your day-to-day work.

So, actually useful—like the Grafana Assistant. This is our flagship app, integrated deeply into Grafana to help more and more people every day. We’re thrilled by the success of this, and it’s great to see the stories people tell us about how it helps them. 

If you haven’t tried Assistant yet, let me tell you a few reasons why you might like it. It’s an LLM integrated into the very fabric of Grafana. You can ask it questions; it knows how to write complex queries, digging into telemetry and giving you the insights you need. 

Since it’s in a loop, it can gather relevant context to make informed assessments. That means it can investigate issues, mixing signals like only pros know how to do. Many people know about metrics and logs, but fewer have experience with tracing and profiling. The assistant knows it all. 

It can also build deep links, taking you where you need to go in Grafana—not just to the right page, but to the actual view filtered for you. It’s smart about building those URL parameters. Of course, since it's Grafana, it can build dashboards too—beautiful dashboards! 

We have a fantastic user base already, and some of the feedback we hear from them is great. For some people, it’s supercharged their teams. They’re able to automate things, get things done more quickly, and deliver more reliable systems than ever before. 

I’m not surprised they love it. The team is fantastic, and they’re moving quickly. If you use Assistant, you’ll notice new features dropping in every week. 

Now, how do we keep the quality high? I'll tell you about that in a minute. But first, I want to tell you about a couple of my favorite features. 

The first one is assistant investigations. We knew that one assistant was good, and we thought, what if we had lots of these? It works! You can prompt the investigator, giving it as much context as you know, and it will swarm multiple agents around the problem. They cooperate together to get a good analysis going before you’ve even reached your computer.

This is driven by cutting-edge research we’re doing at Grafana Labs, and it’s exciting to see. We’re going to keep developing this. All our agents ship with good quality knowledge and expertise prompted by the world-class engineers and operators we have at Grafana Cloud and Grafana Labs. 

But they don’t know your systems quite like you do. This suite of tools allows you to control how your agents behave, how they answer questions, and what actions they take. You’ve spent years developing high standards for your systems; those agents should have the same high standards.

If you can mix this with trusted MCP servers, you really start to level up what you can do. New are automations. Automations let you schedule regular work, so you can get a morning report with your coffee. You might say every week, "Have a look at the past week’s incidents and tell me if there are any common themes or root causes." Just prompt it in natural language—in any language. 

It does support Spanish! (Pause for applause.) Yeah, why not? You can build these amazing workflows, and that’s Grafana Assistant. We love it. Our users love it. It answers questions, digs into telemetry, and takes action.

Of course, this is the first question we always get: Is this available on-prem? Is this available in open source? So far, the answer has been no, but I’m going to introduce somebody now who you know what he’s going to say probably. Please welcome Sven Grossman.

---

**Sven**: Exactly! So as Mat mentioned, user feedback for Grafana Assistant has been great over the last year, and it's helping more and more people with their workflows every day. However, so far, Grafana Assistant has only been available in Grafana Cloud. 

Well, now Grafana Assistant is available everywhere—not just for cloud customers but also for Grafana OSS and Grafana Enterprise. As we make Grafana more and more innovative, we think this should not be limited to just Grafana Cloud. We believe that you and all our on-prem users should benefit from this awesome tool as well. 

Let me show you how you can use Grafana Assistant. The Grafana Assistant plugin will live alongside your Grafana installation, and for the assistant to work properly, you will need to connect it to your Grafana Cloud account, which will handle all the LLM communication for you. 

This works with our Grafana Cloud free forever plan. Your data does not have to live in the cloud, and only relevant pieces will be sent as part of your conversation with Grafana Assistant. This allows us to manage multiple frontier models for all kinds of use cases: some will be better at certain tasks, some are faster, and some are better than others. All of that is managed and maintained by us for you and Grafana.

But enough slides, let’s see it in action. (Demo begins.) 

After you install Grafana Assistant in your local Grafana, as I did here, you’ll need to connect it to your Grafana Cloud account. All this requires is basically two clicks and sunglasses because this portal is very bright!

You select your account here and authorize the connection, and that’s basically it. After you go back to your Grafana plugin, the connection between your on-prem install and Grafana Cloud has now been made. 

Now Grafana Assistant is ready for you in Grafana, wherever you are, as this little sidebar chat app. However, if you prefer a more full-page view of the assistant and more agentic workflows, you can use Grafana Assistant’s new workspace feature, as I did here. I asked Assistant to investigate an issue in the product catalog service.

Assistant did all the querying for me and created a nice panel, but now I want to persist this investigation as a dashboard. In the workspace, it’s as simple as one click on this button, and it will continue the same conversation within the assistant, prompting it to create a dashboard based on this past conversation.

So now Grafana Assistant is thinking and reasoning about this problem and laying out a plan to create this dashboard for you. In a minute, some panels should appear. 

One of the best things is that Assistant knows about these new features. As David mentioned earlier, tabs are now GA, and Assistant knows about tabs. You might not need to learn how to create tabs best; just use Assistant, and in 20 seconds, you’ll have a dashboard with a nice incident summary and an overview tab, plus detailed tabs that help you organize your dashboards.

That was my little demo. Back to the slides—a very brief look at just one part of what the assistant is capable of. If you are looking to use and try out Grafana Assistant, we offer a very general three-tier plan that is actually useful. It includes three users and does not require any contract or credit card, which is way easier than checking into my hotel this week.

So now everybody can use Grafana Assistant, whether you’re in Grafana Cloud, Grafana OSS, or Grafana Enterprise. But we want to show you even more places how you can integrate it into your day-to-day workflow. For that, please welcome Ward Becker.

---

**Ward**: Thanks so much, Sven! Hello, everybody! As Sven showed, Grafana Assistant really changed the game. We moved from writing PromQL and LogQL by hand to chatting with your telemetry. We also moved from automated root cause analysis, so that’s really cool.

Now, we’re taking this to yet another place. Introducing the Grafana Cloud CLI called GCX. GCX brings the full power of Grafana Cloud and the assistant to your command line—and more importantly, to your agentic coding environments. 

With GCX, your terminal truly becomes a window into your production stack. This window is becoming more important than ever because the way we write code nowadays has changed dramatically. In the last few months, the adoption of agentic coding tools like Cloud Code or Cursor has dramatically increased. 

You are writing code faster than ever before, but there is a dangerous gap. The agent can see your code, but it doesn’t know your production reality. It doesn’t see the latency spikes or whether you’re hitting your SLOs, or whether there’s a huge amount of CPU burn. 

They write code based on what could happen, not what is actually happening. We designed GCX to bridge that gap. Let me show you. 

I have a web shop where I’m selling rods that yellow for the creature you saw in the beginning, and my web shop is not very happy. In fact, the order process is down. If I look at my synthetic monitoring checks, I can see that all my probes are failing to reach my website or a specific part of the process.

We can also see that there’s an investigation ready for me because the alert that triggered kicked out automatic root cause analysis for me. I have an assistant investigation report available.

Well, I’m using Cloud Code a lot, so I want to fix the issue from Cloud Code, right from my code for my web shop. GCX allows me to bring all that context from Grafana Cloud into my terminal, where I want to improve my code.

Here, you can see GCX executing commands against the Grafana Cloud stack. It gets metrics, it gets logs, and if it needs to, it fetches synthetic monitoring checks. In this case, it’s fetching the assistant investigation context and allows me to combine that full context.

No manual copy-pasting from Grafana Cloud—just the full context, allowing me to fix the issue in the right place. This looks good; this is indeed the recommended fix I want to execute. 

Next up is to ask Cloud Code to do it for me because that’s the benefit of using agentic coding tools. Please do that for me! Based on the investigation findings, it’s redeveloping the source code and identifying the root cause. 

We want to double verify because we always want to make sure that the agent is doing the heavy lifting and avoiding mistakes. It found three issues in the current version of my code, so that’s great. It’s now modifying the code for me. 

In this case, just before this short demo, typically you would have a proper CI/CD lifecycle with a controlled flow and reviews before going to production. Today, this is running on my own Kubernetes cluster using Docker, so I’m going to have a very lightweight shipping to production. 

Cloud Code is already doing that for me. As you can see, it is building the new images with the new code. It actually patched the Postgres database, so it has an index right now, and the deploy is successful. 

Let’s see if it actually fixed the issue. It’s now checking whether the synthetic monitoring check is back to healthy. Is it able to reach that critical endpoint of the order process? Is latency correct? 

It’s checking these metrics, and the cool thing is you don’t need to tell Cloud Code how to use GCX; it’s able to figure it out itself. We put a lot of effort into making it great for agentic use cases. 

It sees that indeed, yes, the synthetic monitoring check is green, so we fixed the issue. Well done! I couldn’t have done it without you. If we look in Grafana Cloud, we can see that the alerts have been resolved, and now we’re in the green. 

The latency is great, and the check is no longer failing. So that’s great! We fixed it with GCX. Well done, team! GCX is designed to do a lot of that heavy lifting for you. It allows you to move from a greenfield project to full observability in minutes, not days. 

It’s about reducing alert noise, optimizing resource costs, and fixing critical issues before they lead to outages, as we just saw in my web shop. I invite you to install it, point it at your stack, and fix or improve that struggling service in minutes, not days. That’s GCX, and it’s in public preview today.

Thank you very much! Please welcome back Mat and Sven to the stage.

---

**Mat**: Thank you, Ward! Wow, it’s exciting to see the power of Grafana brought into your terminal and coding agent. It works with Assistant and also works without Assistant. We want that to be beneficial even if you're not using Grafana Assistant. 

We’re announcing an open observability benchmark to set the standard for the models, LLMs, and how they deal with common observability tasks. We’re helping to establish industry standards for agentic performance, which means we can build dependable, safe, and secure AI software.

If you’ve been building with agents yourself, you’ll know that working with these non-deterministic inputs and results brings brand new challenges. How do we know we’re making things better when we do work? How do we know when we fix something over here, we aren’t breaking something over there?

We rely on our test suite normally for that, but we don’t have the same thing here since the agents behave differently every time. To address this, we’d like to introduce a brand new AI observability solution with this short video that came from a recent hackathon.

---

**Video Plays**

---

**Mat**: The world is different, but it doesn’t look different. Trees, traffic... where’s that? Washing machines? Life goes on. 

Increasingly, we’re building agents—agents are building agents. Metrics, logs, traces, and profiles are helping us see how those agents are performing, but not how they are behaving. Are they answering properly? Are they doing the right work? How much are they hallucinating? Are they actually useful? 

How much does each one cost? This modern problem requires a new modern signal. Yes, we are thrilled to announce AI observability, brand new in Grafana Cloud. 

This new app gives you a complete end-to-end solution for building modern, professional agentic applications. You get the 10,000-foot view to see where time and tokens are going and therefore dollars. You can drill down and get forensic detail into the agents—what they're doing and what they're thinking while interacting with users. 

So you can iterate at AI speed. This came from the same team that built the Assistant, stemming from hard lessons learned running this at scale. 

**Sven**: Let me talk you through four of my favorite features, at least from the AI observability app. After you instrument your agents with our SDKs, metrics will provide insights that make it easy to spot slow tool calls, the most used models, or the most expensive agents. 

It also lets you drill into conversations straight from that. We treat conversations as a new primitive in the AI age. Seeing how users interact with agents in that detail unlocks new potential for debugging and improving your agentic applications.

The AI observability app offers concrete ways to improve your agents. It analyzes the system prompts and tool definitions based on real conversations users have with the agents. This unlocks the new potential for debugging and improving these applications.

We also have online evaluations, allowing you to implement real-time continuous evaluations of your agents in production. This enables you to monitor if your system prompt changes really improve the agent's quality or not. 

Combining this with Grafana alerting unlocks new potential and provides a complete feedback loop. 

**Mat**: We think most software is going to become agentic in some way or interact with agentic software in some way. We want to be right there with you as you enter this AI age.

Don’t create more AI slop, please! That was our Grafana AI update. Easier to get started with Assistant, now available for everyone. You can just self-serve it. 

You can ask it questions. You won’t feel embarrassed asking the obvious question that everyone else knows and you don’t. It’s going to turn your whole team into observability superheroes. If you’re building agents, try our new AI observability. 

This unlocks the next generation of insights into the AI’s performance and behavior. Take advantage of all the customization tools we offer so you can really make Assistant your own and scale it across your organization. 

If you use the desktop coding agents, you’re going to love the new CLI GCX, which plugs right into your terminal and your coding apps. 

Now, we’re going to hand it back to Raj and Torkel to take us home.

---

**Raj**: Thanks, Mat! Thanks, Sven! Lots of amazing AI stuff going on, in case you can’t tell. Also, thanks, Mat, for your amazing British accent. We all love it! 

Speaking of AI, one of the themes I really wanted to get across is the hype—there’s a lot of hype, a lot of "marketecture," and a lot of slop and false promises with AI. Pardon my Spanish, but there’s a lot of bullshit. I think this hype is really annoying people. 

I don't know if people here are kind of annoyed at how much false promises, marketing-driven solutions, and BS is in the AI world right now. Do other people feel it? Yeah, that’s what I thought. 

Our strategy at Grafana Labs is to use the term "actually useful AI." Last year, there weren't a lot of AI topics at GrafanaCON. There were some, but not a lot. This year, we're all in and full on. 

The reason why that is is that we really believe this stuff is actually useful. That’s a key requirement for us. We’re an engineering-driven company and kind of allergic to marketing hype. Our engineers are very skeptical people, like many engineers. 

We really need to make sure that this stuff is actually useful and provides real value, and we’re confident that it does. Our AI strategy isn’t just about a particular product but is really interwoven in our overall roadmap. 

There are a couple of examples here. The new Loki engine that we talked about is going to have massively improved performance. Yes, that’s going to be really important even for non-AI use cases, but for the agentic world, these things are running in an interactive debugging loop. Speed is paramount in this new agentic world, and we’re thinking ahead on that.

Similarly, with the new Grafana schema, yes, that locks down the definition for a Grafana dashboard. Is that a good thing? Absolutely! But in the agentic world, it’s particularly important because that means that agents are going to be able to build Grafana dashboards more easily and then test and validate them using the schema.

We’re really excited about all this stuff. One of the things we talked about in the keynote that I’m honestly really excited about, but also quite afraid of, is that we’re offering Grafana Assistant to the 99%. It’s not going to be limited to the 1% of Grafana users. 

As we mentioned, we’re going wide and making Grafana Assistant available for free to the 35 million Grafana users around the world. I was talking to our Chief Financial Officer about this, and he was kind of worried. So I’m excited—please use it, but maybe not too much because we’re going to have to figure it out as we go.

In all seriousness, we’re really excited about getting Grafana Assistant in the hands of everybody, and we really look forward to your feedback. 

The really cool thing about our AI story is how it comes back to our original roots and some of our original goals.

**Torkel**: Yeah! One thing that strikes me after seeing everything presented today is how well it ties back to one of our early posters—in fact, the first poster: democratize metrics. This was unveiled more than 10 years ago at the very first GrafanaCON in 2015. 

Back in those days, it was a simpler time. Grafana just did metrics. With it, we wanted to rally around making monitoring and data visualization tools easy to use and more powerful. I think a lot of what we’ve been doing this past decade has been working towards this mission. 

With the recent features in Grafana 13, especially the new AI features, I think they fulfill this mission in ways I could never have envisioned over a decade ago. 

So really, really exciting times! With that, I want to thank everyone who’s been part of the keynote, and I want to thank all of you for being here. I hope you have a great conference. Grab me in the hallway if you have a feature request or pet peeve about Grafana—I’m sure you do! I want to hear them. 

With that, I hope you enjoy GrafanaCON. See you, everyone!

## Raw YouTube Transcript

Please welcome Grafana Labs CEO and
co-founder, Raj Dutt and Grafana creator, Torkel Ödegaard. Hello. Wow, there's a lot of people here. Are we glad to be here to
kick off GrafanaCON? Yeah. Very cool. Well, my name's Raj Dutt. I'm one of the co-founders and
the CEO here at Grafana Labs. And my name is Torkel Ödegaard.
I'm also a co-founder and CGO. So it's great to be here. We're back in
Europe for our annual GrafanaCON event. Just wanted to welcome everyone.
Our last conference was in Seattle, and this is actually our 10th GrafanaCON
and it's our best and biggest yet by far. I remember our first GrafanaCON, we had like 30 people in one of our
early user Squarespace's office. We thought it was amazing and our
expectations just keep getting reset every year and it's bigger, better, and I think
this is going to be the best one yet. So Barcelona, I'm a huge fan of,
but I think Torkel - Barcelona, I recently learned, has a special place
in the Grafana history. Is that true? Yeah, that's definitely true. So my sister used to live
here for more than 10 years. So back in 2013, just a couple of days after I started
working on what would become Grafana, I was traveling here for a
Christmas holiday and I got a cold that whole day and I spent most of the
time in bed just working on Grafana nonstop. And even after got better, I stayed kind of locked in
my room, working on Grafana. I didn't spend hardly
any time with the family. I was already kind of obsessed
with what I was building. So what you're saying is
Grafana is actually Spanish. We've been telling people that Grafana
is Swedish and you're from Sweden, but Grafana was actually
made in Barcelona. Yeah, in a sense. The first foundation, the key features of the first version
was actually written mostly here in Barcelona. We might have to tell our
marketing team about this. Do we need to rename the
project? Do you have any ideas? Yeah. Well, we could name it Grafaña
(Grafanya) or this could become GrafañaCON (GrafanyaCON), but yeah, we'll
see. But yeah, let's move on. All right. Well, like I said,
welcome to GrafanaCON or GrafañaCON. I think we're going to go with GrafanaCON. This is our flagship open source
event. It's all about our technology, all about the community, our open source
projects, new releases, tech talks. It's really a big party to celebrate
the wider ecosystem and community. It's one of two flagship events we
have. The other is ObservabilityCON, which we also have every year. That's where it's more commercially
focused and we talk about our commercial flagship product, Grafana Cloud. But we put on a tremendous amount of
events at Grafana Labs every year. It kind of blows my mind. We did over
7,000 workshop signups last year. There were 80,000 people
that attended a webinar, and we've just got an incredible global
marketing and events team that does a stellar, stellar job. It blows my mind
that we are having multiple events, sometimes on the same day in all corners
of the world. I can't even attend them all if I wanted to. And believe me,
I spend a lot of time on an airplane. So it takes a lot to put an event like
this together. It's a lot of work. It's a lot of prep. It's a lot of
logistics. So before we get going, I just wanted to give a big thanks and
shout out to our events and marketing team who've worked tirelessly
to put this together. Please give them a warm round of applause. So we're here this week to celebrate
the wider Grafana community, get an update on what's new from Grafana
and our other open source projects, and to hear from speakers across this
community of what they've been up to this past year and how they can use these
open source tools to solve every new interesting challenges. So the Grafana community is
growing and it's growing fast. New meetups are happening, and we now just crossed over a
hundred Grafana champions worldwide. So a Grafana champion is someone
who doesn't work for Grafana Labs, but kind of organizes
meetups, organizes events, and teaches others to be
better at using Grafana and these open source tools. So
what's exciting, I think, is that new champions are emerging
through mentorships from other community members and other champions. I think a sign of a really healthy
community. So for Grafana Labs, as a company, "open" has always
been our strategy. And with open, we don't just mean working
on open source software. That is still kind of the
foundation and core of what we do. Majority of software we write is still
open source, but it's more than that. It's about investing in open standards. Standards like OpenTelemetry and
working with open ecosystems like the Pometheus ecosystem and ecosystems that
belong to other communities and other companies like Elastic or ClickHouse. And what I think is kind of cool and
fun is how Grafana then connects these different ecosystems together,
both in the application, but also through events
like GrafanaCON. And lastly, an open culture is also
really key to Grafana Labs. And it's not just how we do business
and how we communicate internally, but also how we share the good and the
bad with the community through a blog post about a security incident
or through, for example, a talk about an outage like
you'll hear later today. So Raj, can you tell us a little bit more
about Grafana Labs and our journey? Yeah, absolutely, Torkel.
So like Torkel mentioned, an open culture is a big part of who
we are. We're always transparent, both internally and externally. Hopefully you feel that in all your
interactions with us as a company. So I'd like to tell you a little bit
about the journey that we've been on as a company for a few minutes
and where we're going. So this slide kind of represents
where we've been, where we're going. And I guess my message is, this has been a shared journey
that we've all been on. Because we're an open source
company and we do stuff in the open, we've been on this journey with all
of you and it's been an evolution. So step one and step two are kind of
obvious. Who here is using Grafana? Maybe a silly question.
Right. That's not surprising. But step one was really becoming the
default dashboard for everything. This was a really fun time in Grafana Lab's
history. We had no customers, we had no revenue, we had no
problems, we had no stress. We were just building open source
software, trying to make it popular. And it was, I miss those days.
Life's a lot more complicated now. Where we are now is really
step three and step four, which we're going to
hear a lot about today. We're making observability
easier for every software team. We've put a lot of work into that over
the last few years, and it's a key theme for this week's conference. And an exciting thing that's going
on more recently is, of course, AI. And internally at Grafana Labs, we've been sort of transformed over the
last year and we really believe that we're at this new paradigm in observability and that
agents are going to become a primary consumer of observability tools
and data. And this is going to change fundamentally the way that we all
interact and the way that we operate our software and interact with
observability tools like Grafana. So we're really excited about this change. We don't only want to be the
leading open observability cloud, we want to become the leading
agentic observability cloud. So there's a lot in this keynote and over
the next two days that kind of shares our vision on this
topic. And then finally, we want to take everything that we're
doing in IT observability and bring it to the rest of the business over time. So that means looking at things not
just like requests, but maybe revenue, not just latency, but maybe LTV. And we see a convergence happening of
business data and observability data, especially as companies become
more and more software led. So this is just a little
taste of where we've been, where we're going. Obviously we didn't
write this plan in advance 10 years ago. It's a not-so-secret master plan that
we wrote retroactively because we've zigged and zagged along the way. This company's always been agile and it's
kind of fun to think about where we're going and where we've been. And again, I just want to reinforce that this journey
has been our shared journey because we've gotten so much great
feedback, input, pull requests, all of the above from so
many people in the community, including many people in this room. So I really wanted to thank everyone here
for helping us go on this journey that we're accelerating on as we speak. So
speaking of accelerating on this journey, wanted to share some key stats
in terms of Grafana Labs, the company and the ecosystem. So we're at 35 million Grafana
users active around the world, which just blows my mind. There's over
a million companies using Grafana. And I just wanted to stop here
and go off script for a second, which is going to alarm Torkel. And I'm
sure all of you here feel the same way, but I think it's just incredible that
after 12 years of a project that my co-founder Torkel created, he's still involved in writing
code for it almost every day. You're going to see features talked
about today that Torkel had a hand in. And I just find that so cool and
impressive and honestly just amazing that my co-founder Torkel is
still active in Grafana 12 years later on this open source project
that he created here in Barcelona, we just discovered. So just give
a round of applause for Torkel. Didn't expect that, didn't you? No. So we've got about, like I said, a million companies using Grafana and
we've got less than 10,000 customers. Now in the early days, this
used to alarm investors. They'd come up to us
and say, wait a minute, how can you convert less than
1% of your users to customers? That isn't a business
model. That's a disaster. And these investors did not understand
open source, right? Generally, those investors that felt that way didn't
end up becoming investors because they didn't understand open source. Our
model has been very simple from day one. We want to grow an amazingly wide
community by creating valuable open source software, and we want to capture a small piece
of what is hopefully a very large pie. And that strategy has really started to
work and accelerate over the last few years. Grafana Labs as a company has hit over
$400 million in annualized recurring revenue. We're the largest privately held
observability company in the world at this point, and there's over 1,600 Grafanistas
in 40 different countries that I have the pleasure of
working with every day. So it's just been amazing
progress and super, super happy with the trajectory that
we're on. And speaking of trajectory, there's one more thing I'd
like to share with all of you. Who here has heard of the
analyst firm, Gartner? All right, a fair bit of people. So Gartner
has a quadrant, a magic quadrant, they call it, that they publish
every year in observability. Now, we made our debut on Gartner's Magic
Quadrant about three years ago in 2023. And on this quadrant, we're a
whole bunch of observability companies, and this was kind of cool when we made
our debut because we felt like we'd finally been seen by Gartner. We were finally beginning to be taken
seriously as an observability platform. Now, we weren't in the
upper right quadrant. We were technically in the lower right
quadrant as a visionary rather than a leader, but it was a good debut.
The next year we made some progress. We went to the upper right, and this was cool because we started to
become part of the same conversations and RFPs with customers who were looking
for the best observability platform. There were companies in this quadrant
that we had admired and continue to admire. When we started the company, we
really looked up to, and to be clear, we continued to look up to in some ways
companies like Datadog and Dynatrace. And it was really cool that the
cloud platform that we built, built on Open was now being taken
seriously and being mentioned in the same breadth of these other leading
observability platforms. Well, what happened last year
was really spectacular, and we were really happy about this.
So last year, just several months ago, Gartner published their new
Magic Quadrant for observability, and Grafana Labs made it furthest to
the right in terms of completeness of vision, clustered around other
top observability companies. And obviously we're pretty
happy with this result, but the reason I'm sharing this
is because I think so many of you, our community deserves to share in this
credit because the way we've built this and the way we've evolved our product
over the last three years has really been with all your help and your input. It's
been a truly collaborative experience. So give yourself a round of applause
because you've helped us become a leading observability platform. Okay. So let's move on to
what we're really here for, an update of what we've
been doing this past year. So we've grouped things into three
general themes, easy to get started, built for scale, and available everywhere. And let's start by diving into what's new
in Grafana 13. And to help me do that, I want to invite David
Kalsmit up to the stage. David has been working on Grafana
since 2018, first as a developer, the manager and director, and
he's now VP of engineering. And he's been running the Grafana
engineering team for the past three years. So let's give it up for David and
let's hear what's new in Grafana 13. Thank you, Torkel. Thank
you, Raj. Hola, Barcelona. Yes. All of Barcelona. Yeah. I'm David. I run the Grafana team and I'm here
to talk to you about Grafana 13. So much has happened in a year, and so I'm here to also show you a bit
the things that I'm excited about that we managed to get in to the product since
Grafana 12. So Grafana, as always, is your trusted and reliable source of single pane of glass. Yes, sorry. And with that comes a huge
range of data sources. Yeah, I'm just dazzled by that number there. And so we stand for open observability
and we don't really mandate where you store your data. And I think
we're quite unique in that regard. And so over the last year,
we also had a few more, and these are maintained by us now,
Jenkins, SolarWinds. So as always, it's a mix of telemetry
and productivity signals. So now we have 170 data sources in
the catalog and with 120 ways to visualize it. And if that
map there checks out, it's really a ton of flexibility. But let me tell you about one
more way to visualize data. Let me introduce you
to the Graphviz panel. And I know it's only in
private preview right now, but it's really too cool not to show
you. Who here has heard of Graphviz. All right. Yeah. There's
a few people. Awesome. So we have wrapped it in a panel, and
so now you can define flow charts. And essentially whatever you can
envision in the dot language, which is part of Graphviz, you
can visualize then in Grafana. And so you can map metrics onto
labels and you can define sort of how the edges and nodes look based
on thresholds in your data. And so this is extremely powerful.
And in this example here also, we're using Graphviz itself to
render its own rendering pipeline, and that's pretty cool. Obviously, you can showcase your own business
processes with this as well. So we're also working on a visual
refresh of our main panel components, and we started off with the gauge panel, and I think these are
looking pretty slick, and there's more to come
here later this year. Next step is annotations. So they've
been a bit of a pain point for a while, and I think it's a bit of a shame
because I think events like modeled as annotations, it can be a really powerful source
when you're starting to troubleshoot an issue. But if you really have a lot of
them, there's sort of too much overlap. It's difficult to tell the various
sources apart and it makes it impossible to read, but we
shipped a few improvements. And so look at this detail right there.
So these are our multi-row annotations. So you can have a row for
deployments, one for incidents, and another one for alerts, for example.
And if you have a lot of them, also then they can get clustered. And next step is dynamic dashboards. So this is something we
introduced last year, and so it's an easy way to make your
dashboards a lot more interactive, and it has a conditional rendering engine, and it's generally more responsive. And with tab layouts, also you can
make them a lot better organized. And so we're excited to announce
that they're now generally available, so thank you dashboarding
team. And personally, also, I think tabs are really cool. And
so internally, we have a lot of, really just a lot of them
in our own dashboards, except Grafana is getting adopted
by bigger and bigger organizations. And over the last year, we worked really hard on making it
easier to also onboard whole teams. And so I'm going to show you three features that really
also help you establish Grafana in your organization.
This is a feature I always wanted, right? So when I work with
slides or something like this, I really don't want to start from
scratch. I really like templates. And so I don't know about you, but I always found it easier to just
edit something that's already there or remove some panels that I don't like. And so this is how dashboard
templates was born. And so right now we're shipping Grafana
with a few templates based on common methodologies. So think DORA
metrics, use method, red method, or golden signals. And so we're still working on a way
also to define your own org templates, right? Because then you really
have a way also to ensure how templates kind of work across Teams and
make it really easy for you to kind of feel at home. And templates really just
work how you think they do. And here's an example of
the use method dashboard. And you start off with example data and
then you start replacing queries or just remove some panels. And
so the layout is there. You can write the queries
yourself or use the assistant, or you can use this next
feature, saved queries. And I don't know if your
organization's anything like mine, but there's usually a few people who know
how to write queries a bit better than others. And so these people can now set
up the rest of your team up for success. And it's not just writing the queries, it's also just agreeing on
what certain queries mean. So something like active
users or something, right? So that query can be defined and then
shared with your team and really sort of bring some consistency. And if you combine this with the other, with the dashboard
templates I showed earlier, so you can really see how someone who
just started out in your team can really be really productive in
building powerful dashboards. So this last one here is my
favorite, interactive learning paths. So sometimes I'm dazzled how
many features we're shipping, and we now build something inside
the product in near the help menu to really make sense of
some of the new stuff. And it's really good at two things. It can show you what you're looking at
right now and give you sort of instant help there. So if it's, I don't know,
like editing a panel or something, or it can guide you through a whole
workflow flow in the user interface and really show you where to
click all inside the product. And the best thing is you can modify
these guides and really sort of suit your organization and onboard new people,
and so you can really customize it. You don't have to start from scratch. There's a whole catalog of pre-made
learning paths in the docs. Just go check them out. You can also chime on play.grafana.com
right now or here outside in the self demo booths, which
is pretty cool. All right, let's talk about operations. So who here
is running a Grafana for other people? Any operations people? All right.
Yeah. More than Graphviz. Awesome. So this next feature is really going
to up your game there. GitSync, right? So it's something we teased last GrafanaCON and we
really got far there now. So GitSync allows you to manage your
dashboards properly as code with a proper two-way integration. So imagine sort of modifying your
dashboards here in the user interface, then you create a pull request
that gets reviewed by your team. And if it gets merged to the repo,
then it's sort of saved there. And then you can also use other
tooling to modify the code when that gets merged into the repo, then Grafana
picks it up and shows you the changes, like a proper two-way integration. And
we really had to do a major rework of the data model and the
architecture to make this work. So a lot of work went into this, but now we think it's rock solid
because it's also just a great disaster recovery mechanism. And I'm really proud to say that
it's now ready for production. So one more thing about GitSync, this also makes it possible to
have a proper publishing workflow. So really think like you can
try new dashboards in Dev, promote them to staging, and then eventually the prod. And so we're also bringing you more
connectors now, not just GitHub, but also GitLab, Bitbucket, and PureGit. So this is really a great way
to manage dashboards at scale. Speaking of scale, there's sort of startup
scale and there's enterprise scale, but then there's Google scale. So Google's SRE culture always played
a big role in GoFundMe's engineering. We even make newly hired engineers
read the Google SRE book. And so about a year ago, Google approached us to see if it's
possible to run Grafana visualization inside of Google for their
own internal monitoring. And I'm super proud to say that that
partnership is in full swing and also it's a bit crazy to me, right? So the company that popularized
SRE not wants to use our software for exactly that purpose, I'm just blown away. So yeah, we can now count Google among
our customers. Super proud of this. And this also brought some interesting
enhancements back into Grafana as product. So Google is very disciplined in sort
of the way they approach monitoring. And so this is something you need when
you have really layers and layers of services that's sort of being
worked on by various teams. And so they're very big on this
concept of reusability in dashboards. And so there's a ton of features that
went into the product now and we're going to show you in a later
session. All right. Grafana. to trusted single pane of glass,
brings all your data together, really trying to be more
open and composable. And one more thing I have for this.
So you've seen this number earlier, 170 data sources we have in a catalog, but we believe there's room for more.
Room for more data sources, more apps. So also you can
think normal telemetry, but also it goes a bit
beyond, like hardware, industrial or IoT. And so we started with a select group
of partners now and they have built the first few apps and they're
already in the catalog. And you can also try them
out. And it's early days. So we're doing things a bit differently. So we're still looking a bit of feedback
on what are other apps that you would like to see in this marketplace. Or if you want to partner with us
and start publishing your own plugins on this marketplace, just
come and have a chat. All right. That was Grafana 13,
your trusted single pane of glass, gave you a set of new tools to
bring teams into your organizations. Git Sync is finally ready for production, and we have a marketplace pilot that
allows you also to participate more in the Grafana ecosystem.
All right. Next up, to talk about my favorite
Logs database, Poyzan. Thank you, David. Hello, everyone. My name is Poyzan.
I'm running the EMEA Group in Loki, and I'm very excited today to be here
with you to tell you all about Loki's new architecture. So Loki is designed to be lightweight. It operates with the core principle of
you don't need to index every bit of every log line. It makes logs available immediately
and heavily leans on object storage, and it has been excellent at what it does. It made it possible to have
petabytes of logs data, all an affordable infrastructure, but we know that the world of logging
is shifting and we are evolving Loki with it. So structure logging is now the
default and OpenTelemetry adoption is accelerating it. Log volumes are increasing along with
number of fields in every log line. So what used to be a simple
error message now has key value pairs that carries things
like service name, trace IDs, status codes, or like order IDs, transaction IDs that
has business logic in it. And the way you query
this data is changing too. So you're not gripping over
the error messages anymore. You're running targeted analytic
queries over massive volumes, drilling down by service,
aggregating over the status quo, or wanting to get like business
insights from those custom fields. And when those queries takes minutes
or never return result at all, that's where the frustration starts. So to meet these new requirements, we are rebuilding the foundations
of Loki with three major changes. First is a ingestion pipeline that separates reason rights without
compromising on high availability, a brand new query engine that filters
data closer to the source and distributes work better and a columnar storage
that natively supports reading selectively to make that all
smart filtering possible. So let's do a mini deep
dive. On the left today, classic Loki distributes span
out right to three ingestor zones and these replicate data and
then flashed object storage. The same ingestors are
serving recent read queries. So a heavy query hit that may
need a multiple stream selectors, it can stall your rights and this is
an incredible operational headache to manage and replication
comes with it costs too. So Loki is designed to flush the same
data only once to object storage, but when ingestors go out of sync, it can actually cause duplicates on
the persistence layer. So on the right today, we are adding Kafka
in our right pipeline. Distributors are right to
the Kafka partitions and each partition is consumed by a single ingestion. Now rights
are durable before the ingestors. We can completely separate reads
and rights. This is a massive win. We wanted for years and there's more. Remember the duplicates I
mentioned on the storage layer. So data shows that Loki can
end up storing up to 2.3 times the same log data on object storage. This is a lot when you operate at
the petabyte scale that Loki can do. So with Kafka, we can guarantee that every
log line is written once. And when an ingestor dies, the new
one just picks up and replace it. So we are not compromising
from durability while doing so. Operational complexity of running
Kafka is a very difficult trade-off, but the read and write isolation
with a more robust write path is more than justified as complexity. So let's move on to the read side. The biggest lever we have for a
more performance query path is reading less data in the first place. The new query engine filters
data closer to the storage layer. So what does this mean? So the data that doesn't match your
query never enters the pipeline to be parsed, and it is backed by a
scheduler that distributes work over a pool of workers. So results are dramatically faster on large
range aggregation queries and drill downs. To make it all possible, we rely on a format that supports
selective reading natively. That's where column R comes in now. Loki's original storage chunks made a lot
of sense for what it was designed for, flush fast and scan at
query time. However, across millions of log lines, trying to filter a subset of selective
fields becomes the bottleneck. On the scanning level. So the column R format
flips this logic. Now, each field can live on its own
column. Looking at the example here, so get me all the services
running at a given time. Classic Loki will have
to parse every log line, every metadata to be able to filter the
service name. Column R just returns it. And this is still schemaless. So you
don't have to define columns upfront. You continue to send your logs and Loki
source them, organize them for you. The best bit, let's talk about results. We are running one of the largest cloud
logs instances to monitor Grafana Cloud itself. And these numbers are coming from our
internal cluster that can do gigabytes per second throughput, which will turn
into couple petabytes a month. And 20 times less data scanned, returned 10 times faster. This is a massive win on
the scale that we operate. And these are still preliminary results. We are actively working
on different new revenues. So stay tuned for better performance. Did we solve it all then? Not really. So if you ask Loki to get a specific
string without in-stream selectors, look at all my log lines and return
results. It will still be slow. We call them needle in
the haystack queries. And Column R does not really
unlock this out of the box. We attempted to solve this
problem a couple of years ago, but our solution did not scale. But we
hear you, we know this is a real need. So Grafana Labs made an acquisition
to bring Jason Nochlin and his technology to Loki. Jason implemented targeted secondary
indexes that can result up to 99% drop in ByteScan. This is currently being developed on
cloud first and it's already in private preview. We are working on making it
available on open source data this year. I hear you asking. Well, how
are we going to try this? So the new architecture format with all
its components will be available on all modes of Loki. And we
are committed to a great monotic experience known as single binary. So if you're running Loki on your
local or on a single node today, we will not be forcing the Kafka
overhead on your workloads. However, if you need a larger scale,
Loki distributed is the future. And the diagram here today is representing
how we are testing our internal migration strategy. So you can see that we are
writing both new and the old formats and running them against the engine today and
the new engine that we are developing. And we have an open source
component called Querity that can allow you to choose the preferred
engine you want or race results. This allows us to
continue to iterate safely and compare results side by
side at any time. As we are moving forward to Loki 4.0, we will be iterating over a simplified
migration path for you and we'll help you there. If you're running Loki by
a helm, Tanka of your own setup, we'll meet you where you
are. So everything we build, we build for scale on open standards, and that's the Grafana way
that we are very proud of. Now to tell you all about OpenTelemetry,
I want to hand it over to Ted Young. Thank you. Thank you. Thank
you. Thanks, Poyzan. Hi, everyone. I'm Ted Young, Grafanista,
an OpenTelemetry co-founder, back with your friendly
neighborhood OpenTelemetry updates. You could definitely say that structured
logs were indeed a big event last year in OpenTelemetry. So what's coming
up this year? OpenTelemetry, as I like to think of it, is a high
throughput, high latency organization. We all win when we bet on open
standards. I really firmly believe that. And Grafana Labs has been
betting big on OpenTelemetry, and you can see that reflected in all
the initiatives and components that we've been working on and sponsoring. But what's the project's top
goal for this coming year? I'm excited to announce that
it's to be as boring as possible. Yes, that's right. You heard me right.
Boring. Now that might sound crazy, but it is crazy. And it's important
to remember though with telemetry, the opposite of boring isn't interesting.
It's frustrating. So actually, when you think about it, boring is amazing and it's harder
to be boring than one might imagine. So this year, we're trying to get back to our standardsy
routes and trying to be as boring as possible. And that's why our top priority
is actually to stabilize all the things. What could be more
boring than this? Not changing things. But it's actually amazing because it
means that we've reached the end of the road for the original goals of the
project, tracing metrics and logs, stable, unified, everywhere. These are the final pieces that OpenTelemetry needs to
finally graduate from the CNCF. So what does
stabilization mean exactly? Is it really that OpenTelemetry
is so unstable? No, of course not. OpenTelemetry has been in production
for years and we've made quite a bit of defacto stable software along the way, but we do have some cleaning up
to do in order to make reality ... Sorry. In order to make our software
actually reflect that reality. Some organizations have security rules
that ban the installation of software marked as beta. We want OpenTelemetry
to be available to everyone everywhere, which means we need a simple and reliable
way to ensure that OpenTelemetry only contains stable packages. That means everything important in
OpenTelemetry needs to become 1.0. So the final boss of this stabilization
effort actually isn't the collector or the SDKs or OB or any
other core component. It's the instrumentation. That's
where the surface area gets enormous. We've been stabilizing the
core semantic conventions, the data definitions for things like
HTTP and SQL and message queues, that kind of a thing. It's
boring but important work, but the real heavy lifting comes in
rolling out all of those stable semantic conventions to all of the actual
instrumentation packages in every single language.
So going forwards, we'll be engineering a two-stage rollout. Most instrumentation packages
are in a state of defacto stable. That means they work fine,
they're safe, they're reliable, but the data could be better. Identifying these packages and marking
them as 1.0 brings our concept of stability better into alignment
with user expectations. Stage two will be lifting that data up
everywhere to the latest version of the semantic conventions once they become
available via another major version bump. This is harder than it sounds,
and it's the last remaining piece. We're going to need to invent new
tools and potentially apply new coding techniques in order to handle the scale
of instrumenting all the software on the planet. Boring is harder than it looks. But why stop there? What could be even more boring than
stabilizing the definition for database queries? How about
installing all of these bits? I'm talking about package management, the amazing place where software
and the mail finally meet. Some background. In order
to make OpenTelemetry work, the correct instrumentation needs to
be installed into every application, and that creates this little
matching game that we have to play. The way this matching game works, OpenTelemetry first has to identify all
of the libraries and frameworks that your application uses. Then it needs to identify the
matching pieces of instrumentation. Then it needs to combine those
two things together. Of course, we have automation that plays
this matching game for you, but the only issue is right now, the way you configure and use those
automated tools works differently in every language. And learning how those tools work can
make OpenTelemetry difficult to install the first time that you try it.
It's not just confusing though. The current automation requires developers
to touch every single application one by one. What we want is a
single click way to install OpenTelemetry system wide, and that brings us to the people
we like to call operators, SREs, infrastructure teams, sysadmins,
people like that. Today, operators can install and manage
some parts of OpenTelemetry, basically the collector and
OB plus a couple of languages, but there are still many cases where
it isn't possible to apply the language specific automation in a
comprehensive way. That's a problem. Not just because we like the operators,
but because at many organizations, it's the operators who are charged with
installing and managing observability. Often operators are the only
way to get a sort of quick, consistent rollout across
an entire organization. While it's fabulous if application teams
can manage their own observability, most organizations are designed
to give their teams independence, which means trying to do a coordinated
rollout where every single team has to do a bit of work is going
to be really difficult. But don't worry, we have a solution. What I would like to call
integrated OpenTelemetry. A set of initiatives that when combined
create a new way to instantly and consistently install OpenTelemetry
everywhere. Let's get into how it works. Starting with Linux. How should
you install OpenTelemetry on Linux? I believe it should be the same way that
you install anything else via package management.
That's right. apt-get install OpenTelemetry is
coming to a Linux box near you. Under the hood, OB, the
injector, language automation, all of these things are doing a lot
of heavy lifting to make it work, but you don't have to worry about any
of that. Just install the package, add a few lines to a comp
file, and by default, everything that can be
instrumented will be. From one machine, it's easy to scale up everywhere because
this is the part of the system that operators control. And if you're using
Kubernetes, it will be just as easy. We've had an OpenTelemetry operator for
a while, and it's a popular solution. With these additions, all of its
current limitations will be removed. And of course, if you're familiar with
Instrumentation Hub from Grafana Cloud, it will use the same mechanisms under
the hood to manage these bits for you. Of course, right now, we're
only focused on Linux, but once we've stabilized things here,
we plan to look at Windows and Macs next, as well as potentially looking
at development environments, not just production. So that's integrated OpenTelemetry, easy
for everyone to install, easy to scale, amazing, simple, boring. Just the
way we want OpenTelemetry to be. All right. So enough with
all the boring stuff, right? Let's have some actual fun
and excitement. For that, I believe you need a British accent. So I'd like to welcome Mat Ryer up
onto stage to talk about artificial intelligence and all the amazing
things going on in that department. Thanks, Ted. Amazing. Hello everybody. I'm very excited to tell you about the
continued investment that we're going to make into AI here at Grafana Labs. We want to be a first AI native platform, and that means dealing with
non-deterministic inputs that we see now. It means dealing with scale. Now, anybody can write complex queries just
by prompting in natural language through the assistance or through agents. And it means making sure that the APIs
are giving data back in a way that the agents can deal with. It's not going
to blow out the context window. So more than ever, we're dedicated
to building safe, secure, actually useful AI. And we
take this quite seriously. We don't want to ship slop. We
don't want to be a slop shop. So everything we deliver, everything we're doing here is about guaranteeing when
we ship something to you, it is going to actually make a big
difference in your day-to-day work. So actually useful, like the Grafana
Assistant. This is our flagship app. This is a sidebar chat app that's
integrated deeply into Grafana, and it helps more and
more people every day. We're thrilled by the success of this, and it's great to see all the stories
that people tell us about how this helps them. If you haven't tried Assistant, let me tell you a few reasons
why you might like to. So it's an LLM integrated
into the very fabric of Grafana. It helps you do everything you
need. You can just ask it questions. It knows how to write complex queries
so it can go and dig into the telemetry and give you the insights that
you need and it's in a loop. So it can go around and gather relevant
context so it can make informed assessments. That means it can investigate issues
and it mixes signals like only pros know how to do. A lot of
people know about metrics and logs. Fewer people have experience with tracing
and profiling while the assistant, these agents, they know it all. They can also build deep links so they
can take you where you need to go in Grafana, not just to the right page, but to the actual view filtered for you, because all the filters are just in the
URL parameters and we taught it how to build those URL parameters.
Of course, it's Grafana, so it can build dashboards as well,
beautiful dashboards, in fact. We have fantastic user base already, and some of the things we hear from
them is just great for us. We love this. And for some people, it's
really supercharged their teams. They're able to automate things, they're
able to get things done more quickly, and this means that it frees them up
so they can do more important things, and they're delivering systems more
reliable than ever before because of it. And I'm not surprised they love it. The team is fantastic and they're
moving so quickly. Genuinely, if you use Assistant, you will notice new
features every week dropping in there. Now, how do we keep the quality high?
I'll tell you about that in a minute. But first, I want to tell you about a
couple of my favorite features here. So the first one, assistant
investigations. We knew that one assistant was good, and we thought, what if we had
lots of these? And so it works. So what you can do is
prompt the investigator, you give it as much context as you know, and it will swarm multiple
agents around the problem. They'll follow and chase down different
leads and they cooperate together so you can really get a good analysis going
before you've even reached your computer. So this is all driven by cutting edge
research that we're doing at Grafana Labs, and it's very exciting to see, and we're
going to keep developing this as well. All our agents ship with
good quality, good knowledge, expertise that's been prompted by the
world-class engineer operators that we have at Grafana Cloud and Grafana Labs, but they don't know your
systems quite how you do. So this suite of tools allows you
to control how your agents behave, how they answer questions,
and what actions they take. You spend years developing high
standards for your systems. Those agents should have
those same high standards. And if you can mix this
with trusted MCP servers, you really start to level up what
you can do. New is automations. Automations let you schedule regular work, so you can get a morning report with
your coffee. Maybe you say every week, have a look at the past week's incidents
and tell me if there's any common themes or common root causes. And you just prompt it in natural
language, in any language. It does support Spanish.
Pause for applause. Yeah. Okay. Yeah. Why not? So you can plug this now and build
these kind of amazing workflows, and that's Grafana Assistant.
We love it. Our users love it. It answers questions. It can dig
into telemetry. It can take action. And of course, this is the
first question we always get. Is this available on- prem? Is
this available in open source? So far that answer has been no, but I'm
going to introduce somebody now who ... You know what he's going to say
probably. Please welcome Sven Grossman. Thank you. Exactly. So as Mat mentioned, user feedback for Grafana's assistant
has been great over the last year, and it's helping more and more people
with their workflows every day. However, so far, Grafana System has only been
available in Grafana Cloud. Well, now Grafana Assistant
is available everywhere, not just exactly. Not just for cloud customers, but also
for Grafana OSS and Grafana enterprise. As we are making Grafana
more and more innovative, we think this should not be
limited to just Grafana Cloud, and we believe that you and all of our
on- prem users should benefit from this awesome tool as well. So let me show
you how you can use Grafana assistant. The Grafana system plugin will live
alongside your Grafana installation, and for the assistant to work properly, you will need to connect it
to Grafana Cloud account, which will handle all the LLM
communication for you. But obviously, this also works with our
Grafana Cloud free forever plan. Your data does not have to live in cloud, and only relevant pieces will be sent as
part of your conversation with Grafana Assistant. This allows us to manage multiple frontier
models for all kinds of use cases. Some will be better at certain
tasks, some are faster, and some are better than others, and all of that is managed and
maintained by us for you and Grafana. But enough slides, let's see it in action. In a minute. There we are. So after you install Grafana
assistant in your local Grafana, as I did here now, you will need to connect it
to your Gavana cloud account. All this requires is basically two clicks
and sunglasses because this portal is very bright. So you
select your account here, authorize the connection,
and that's basically it. So after you go back
to your Grafana plugin, this connection between your on- prem
install and Grafana cloud has now been made. So now Grafana
assistant, after this is done, the loading should be here
ready for you in Grafana, wherever you are as this little
site buyer chat up. However, if you prefer a more full page view of
the assistant and more agentic workflows, you can use Grafana Assistant's new
workspace feature as I did here, and I asked Assistant to investigate an
issue in the product catalog service. So Assistant did all the querying
for me and did this investigation, also created some nice panels, but now I want to persist this investigation as a
dashboard. In Workspace, it's as simple as one
click on this button, and this will basically continue the
same conversation within the assistant, and it prompted the assistant to
create a dashboard based on this past conversation. So now Grafana
assistant is, like kicking off, is thinking and reasoning
about this problem, and is basically laying out a plan how
to best create this dashboard for you. And in a minute, some
panels should appear. And then one of the goodest things I
believe is that Assistant basically always knows about these new features.
As Dave mentioned earlier, tabs are now GA and also
assistant knows about tabs. So you might not need to
learn how to create tabs best. Just use Assistant and you will see
in 20 seconds in just one prompt, you will get a dashboard like this with
a nice incident summary and an overview tab and then detailed tabs that
help you organize your dashboards. So that was my little
demo. Back to the slides, very brief look and just some part of what
a system is capable of. And if you are looking to use
and to try out Grafana system, we offer a very general three tier
that is actually useful and it includes three users and does not
require any contract or any credit card, which is way easier than
checking into my hotel this week. So now everybody can use Grafana
Assistant, whether you're in Gavana Cloud, Grafana OSS, or Grafana Enterprise, but
we want to show you even more places, how you can integrate it into your
day-to-day workflow. And for that, please welcome Ward Becker. Thanks so much, Sven.
Hello, everybody. All right. So as Sven showed, Grafana Assistant really changed
the game and we moved from writing PromQL, LogQL by hand to
actually chatting with your telemetry. We moved from also to
automated root cause analysis, so that's really cool. And from cloud, we moved now beyond cloud to
yourself hosting the environments, so that's awesome. But today, we're actually taking
this to yet another place. Introducing the Grafana
Cloud CLI called GCX. GCX beings the full power of
Grafana Cloud and the assistant to your command line, and more importantly, to your agentic coding
environments. With GCX, your terminal truly becomes a
window into your production stack. It bridges the gap between your local
dev environment and key observability insights from Grafana Cloud. And that window is becoming more important
than ever because the way that we write codes nowadays has
changed dramatically. In the last few months, the adoption of agentic coding
tools like cloud code or cursor have dramatically changed. You are
writing code faster than ever before, but there is a dangerous gap.
The agent can see your code, but it doesn't know
your production reality. They don't see the latency
spikes or whether you're actually hitting your SLOs or whether there's a huge amount of CPU burn. They write codes based on what could
happen, not what is actually happening. And we designed GCX to bridge
that gap. Let me show you. So I have a web shop. I'm selling rods that yellow for
creature you saw in the beginning, and my web shop is not very
happy. Actually, the order process is down. So if I look in my synthetic
monitoring checks here, as you can see, there is ... And I might need to click another button.
I think it's now going to run then. So there we go. Somebody's
helping me. Great. So the growth shop is not very happy. We can actually see in my center
monitoring checks that all my probes are failing to reach my website or that's
a specific part of the process. And we can also see that
there's an investigation ready for me because the alert that triggered kicked out automatic
root cause analysis for me. So I have an assistant investigation
report for me available. Well, I'm using cloud code a lot. So
what I want is from cloud code, from my actual code of my
webshop, want to fix the issue. So what GCX allows me to do is
actually bringing all that context from Grafana Cloud into my terminal right
where I want to improve my code. So here you can see actually GCX executing
all kinds of commands against the Grafana cloud stack. So it gets
metrics, it gets logs, if it needs to, and of course synthetic
monitoring checks. In this case, it actually fetches the assistant
investigation context and it allows, of course, to combine that full context. So no manual copy and pasting from
Grafana Cloud, just the full context, and it allows me to indeed fix
the issue in the right place. So this looks good. This is indeed the
recommended fix that I want to execute. So next up would be to ask Claude Code
to do it for me because that is of course the benefit of using agentic coding
tools. So please do that for me. So based on the investigation
findings, redevelopment source codes, identified root cause, that we want to double verify because
we always want to make sure that the agent is doing all the heavy lifting
and making sure there's no mistakes. So it actually found those three issues
in the current version of my code, so that's great. And it's now actually
modifying the code for me. Great. Awesome. So in this case,
just before this short demo, typically you would have a proper
CI/CD life cycle where you have a very controlled flow with reviews
going to production. Today, this is running on my own Kubernetes
cluster running on Docker. So I'm going to have a very
lightweight shipping to production. So actually a cloud code is already
doing that for me, as you can see here. So it is building the new
images with the new code. It actually patched the Postgres database, so it has an index right now and
the deploy is successful. Great. Okay. Let's see if it
actually fixed the issue. So it's now checking
whether the actual code, the synthetic monitoring
check is going to be healthy. So is it actually able to reach that
critical endpoint of the order process? Is literacy correct? So it's
checking here the metrics. And the cool thing is you don't need
to tell cloud code how to use GCX. It's able to figure it out themselves. So we put a lot of effort in making
it great for Agentic use cases. So it's able to see that
indeed, yes. Okay, great folks. The synthetic monitoring check is
green, so we fixed the issue. Well done. I couldn't have done it without
you. So that is great. So actually, if we look in Grafana cloud, we can actually see that the alerts
have been resolved and now we're in the green. So the latacy is great and
the check is no longer failing. So that's great. We fixed
it with GCX, well done team. So GTX is really designed to do a
lot of that heavy lifting for you. It allows you to move from a greenfield
project to full observability in minutes, not days. It's about reducing the alert noise
or to optimize resource costs, and of course, fixing those critical issues before they
become like outages as we just saw in my web shop. So I would like to invite you to
install it, point it at your stack, fix or improve that struggling
service in minutes, not days. That's GCX. It's in public preview
today. Thank you very much. Please welcome back Mat and Sven to stage. Thank you, Ward. Wow. That is so exciting to see now the power
of Grafana bought into your terminal and into your coding agent.
It works with Assistant. It also works without Assistant. And I think we want that to also be good
if you're not using Grafana Assistant where you get all the bells and whistles. And so we are announcing a
open observability benchmark, and this is to set the standard
for the models, the LLMs, and how they deal with
common observability tasks. We're helping to establish these industry
standards for agentic performance, and that means we can
build dependable, safe, secure AI software. And if you've been building
with agents yourself, you'll know that working with these
non-deterministic inputs and these non-deterministic results
brings brand new challenges. So how do we know that we're making
things better when we do work? How do we know when we fix
something over here Here, we aren't breaking something over there.
We rely on our test suite normally for that. We don't quite have the same thing here
since the agents behave differently every time. And so to address this, we'd like to introduce a brand new AI
observability solution with this short video that came from a recent hackathon. You can't tell from here,
but the world is different. It doesn't look different.
Trees, traffic. Where's that? Washing machines? Oh, I see, because
life goes on. Yeah, no. Well, I was expecting another... like
trees, traffic. Yeah. Increasingly, we're building agents.
Agents are building agents. Metrics, logs, traces, and profiles are helping us to see
how those agents are performing, but not how they are behaving.
Are they answering properly? Are they doing the right work?
How much are they hallucinating? Are they actually useful?
How much does each one cost? This modern problem requires
a new modern signal. Yes, we are thrilled to
announce AI observability, brand new in Grafana Cloud. This new app gives you a complete
end-to-end solution for building modern, professional agentic applications. You get the 10,000 foot view so you
can see where time and tokens are going and therefore dollars. You can drill down and get
forensic detail into the agents, what they're doing and what they're
thinking while they're interacting with users. And so you can iterate
at AI speed. This came out of, from the same team that
built the assistant, came from a lot of hard lessons that
we learned running this at scale. And Sven, please, please Sven, tell
us what does this unlock for people? Yeah. Let me talk you through
four of my favorite features, at least from the AI observability app. So after you instrument
your agents with our SDKs, Metrics will provide all
kinds of insights for you. And that makes it very easy to spot
slow tool calls, the most used models, or the most expensive agents. And it lets also drill into
conversations straight from that. And we treat conversations as a
new primitive freely in AI age. It lets you deback right down to every
sub-agent, every tool call, every word, every token, even. And seeing how your users use agents
in that detail really unlocks the new potential of debugging and
improving your agentic applications. The AI observability app offers
concrete improvements for your agents, and it analyzes the system prompts
and the tool definitions based on real conversations that your
users have with the agents. That unlocks the new potential of debugging and
improving these applications. And we use this also quite often
in legal funnel system experience. And this is one of my favorite - online
evaluations. So online evaluations, you can implement real time continuous
evaluations of your agents in production. And this will ,more than ever, allow you to monitor if your system
prompt changes really improve the agent's quality or not. And combining this with Grafana alerting
really unlocks the new potential and gives this complete feedback loop. Yeah. We think that most software now is
going to become agentic in some way or interacting with agentic
software in some way. And we want to be there right with
you as you enter into this AI age. And we do this together and
don't create more AI slop, please. So that's AI
observability in Grafana Cloud. Everything you need to build AI agents, AI technology at scale. And that was our Grafana AI update.
Easier to get started now with Assistant. You can just self-serve it.
You can ask it questions. You don't feel embarrassed asking the
obvious question that everyone else knows and you don't. It's going to turn your whole team
into observability superheroes. If you're building agents,
try our new AI observability. This unlocks the next generation of
insights into the AI's performance and behavior. And take advantage of all the customization tools
that we offer so you can really make assistant your own and
scale it across your org. If you use the desktop coding agents, then you're
going to love the new CLI GCX, plugs right into your terminal and into
your coding apps. And thanks to Sven, Grafana Assistant is now
available everywhere. So now we're going to hand back to Raj
and Torkel to take us home. Thank you. Thanks, Mat. Thanks, Sven. Lots of amazing AI stuff going on in case
you can't tell. And also thanks, Mat, for your amazing British accent.
We all love it. So speaking of AI, one of the themes I really wanted to
get across is there's a lot of hype, there's a lot of "marketecture,"
there's a lot of slop, there's a lot of false promises
with AI. Pardon my Spanish. There's a lot of bullshit. And I think
this hype is really annoying people. I don't know if people here are kind
of annoyed at how much false promises, marketing driven solutions and
kind of BS there is in the AI world right now. Do other people
feel it? Yeah, that's what I thought. And so our strategy at Grafana Labs,
we've used the word actually useful AI. So last year there wasn't a
lot of AI topics at GrafanaCON. There were some, but not a lot. This
year we're kind of all in and full on. And the reason why that is, is because we really believe
this stuff is actually useful. That's a key requirement for us.
We're an engineering driven company. We're kind of allergic to marketing
hype. We're allergic to false claims. Our engineers are very skeptical
people, like many engineers. And so we really need to make sure
that this stuff is actually useful and provides real value, and
we're confident that it does. So our AI strategy isn't just
about a particular product, but it's really interwoven
in our overall roadmap. So there's a couple of examples here.
The new Loki engine that we talked about, massively improved performance. Yes, that's going to be really important
even for non-AI use cases, but for the agentic world, these things are running in an interactive
debugging loop. Speed is highly important, right? Agents are very
iterative, they run hypotheses. And so the query performance of Loki
becomes paramount in this new agentic world, and we're thinking ahead on that.
Similar with the new Grafana schema, yes, that locks down the
definition for a Grafana dashboard. Is that a good thing? Absolutely.
But in the agentic world, it's particularly important because that
means that agents are going to be able to more easily build Grafana dashboards
and then test and validate them using the schema. So we're really
excited about all this stuff. And one of the things that we talked
about in the keynote that I'm honestly really excited about, but also quite afraid of is the fact
that we're offering Grafana Assistant to the 99%. It's not just going to be
limited to the 1% of Grafana users. As we mentioned, we're going wide and we're making Grafana
Assistant available for free to the 35 million Grafana users around the world.
Now, I was talking to our Chief Financial
Officer about this and he was kind of worried. So I'm excited. Please use it, but maybe not too much because we're
going to have to figure it out as we go. But in all seriousness, we're really excited about getting Grafana
Assistant in the hands of everybody, and we really look
forward to your feedback. But the really cool thing about our AI
story is it's a way that it comes back to our original roots and some
of our original goals. Torkel? Yeah. So one thing that strikes me
after seeing everything presented today is how well it ties back to one of our
early posters, in fact, the first poster, democratize metrics. This was unveiled more than 10 years
ago at the very first GrafanaCON in 2015. And back in those days, it was a simpler time.
Grafana just did metrics. And with it, we wanted to really rally around making
monitoring and data visualization tools easy to use and more powerful. And I think a lot of what we've been
doing this past decade has been working towards this mission. And with this kind of recent features
in Grafana 13 and especially the new AI features, I think they fulfill this mission in
ways that I could never have envisioned over a decade ago. So really,
really exciting times. And with that, I want to thank everyone
who's been part of the keynote, and I want to thank all of you for
being here. I hope you have a great conference. Grab me in the hallway if
you have a feature request or pet peeve about Grafana. I'm sure you do. I want to
hear them. And with that, I hope you have a great conference
and welcome to GrafanaCON. See you, everyone.

