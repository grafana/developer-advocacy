# Grafana for Business Intelligence: How Grafana Labs Runs on Grafana

Published on 2026-05-14T17:17:55Z

## Description

Grafana isn't just for SREs. At Grafana Labs, every department — product, sales, marketing, engineering — runs on Grafana as ...

URL: https://www.youtube.com/watch?v=_7Ld_xgmk64

## Summary

The show "Grafana for Business Intelligence: How Grafana Labs Runs on Grafana" was published on May 14, 2026. The speakers included Sam Jewell, a software engineer at Grafana Labs, and Chris, the leader of the central data and analytics team. They discussed how Grafana is utilized across various departments at Grafana Labs for business intelligence, product analytics, and sales analytics, showcasing features like the Grafana Assistant, Slack integration, and the semantic layer. Key takeaways included the versatility of Grafana for different business contexts, the importance of seamless collaboration, and the benefits of using a semantic layer to simplify data interaction and enhance the capabilities of AI agents. 

Topics: Grafana, business intelligence, product analytics, sales analytics, semantic layer, Grafana Assistant, Slack integration.

## Chapters

00:00:00 Building Grafana dashboards for business intelligence
00:05:23 Using Grafana for A/B testing and data analysis
00:10:52 Building powerful sales dashboards with Grafana
00:16:21 Using a semantic layer to generate SQL dynamically

Hey everyone. In this session, we're going to be talking a little bit about how we've been building Grafana dashboards for business intelligence (BI) internally at Grafana Labs and how it's become this visualization layer on top of our business data stack. But before we jump in, a little about ourselves.

Hello, I'm Sam Jewell. I'm a software engineer at Grafana Labs. I've been working on building support for a semantic layer into Grafana.

And I'm Chris. I was one of our first data hires here at Grafana, and I've led our central data and analytics team over the last two, two and a half years. 

So, our agenda for today: we're going to start off with a bit about our "why." Why do we build dashboards like this internally at Grafana, and why might you be interested in doing so as well? Then, we'll spend the majority of our time going through a couple of different demos, showing a couple of dashboards around product analytics, probably one around sales analytics, as well as some of the cool new features we're seeing around Grafana Assistant, our Slack integration, and the awesome work that Sammy's been doing around the semantic layer. At the end, we'll open it up for any Q&A from all of you.

You've adopted Grafana, and you use it with your SREs, with your engineers, with your technical staff. You use it to monitor, especially when things go wrong; it's there for you, and it's a flexible tool. So, perhaps you could apply it in more contexts. What about in your business? Grafana can do incredible things. At Grafana Labs, literally every one of our departments uses it—from product management to sales and marketing—and with a few other tools, we use it across the board. 

We use it for product analytics to answer questions like, "Is my feature being used?" We use it for project management to understand whether our engineers are becoming blocked. We use it for business intelligence (BI) to answer things like, "Which prospects should I be calling today?" And of course, it's our observability tool as well. With all of the rest of our products, we have so many questions, starting with the simplest: "Is my service up?"

So, why do we use Grafana for everything, and might you be able to do the same? There are a few reasons that are unique to us, but there are many reasons that may apply to you and be relevant to your context. 

The first reason that's unique to us is that we build Grafana, of course. To us, using Grafana in such a diverse range of contexts is dogfooding, and it helps us to make Grafana the versatile tool that it is today. Another reason is that we're heavily invested in open source, and our code, as well as our backlogs and issues, all live out in the open on GitHub. From there, it's a very simple step to connect that to Grafana and visualize it.

But the other reasons will be relevant to everybody. If you're able to use fewer tools, you can save a lot of complexity and a lot of money. We also find that it means more of our staff—almost all of our staff—are able to operate side by side in Grafana, in that same tool, allowing for seamless collaboration. This way, we can collaborate across roles and departments and see the results of one another's work super easily.

Then there's the strength of Grafana, the tool itself. It has that big tent of data sources. You can query data from two different places and see it side by side in the same dashboard, even blend it in the same panel. You can alert on absolutely anything, and it's fast; it's low latency. You can throw a fire hose of data at it, and it barely blinks, really.

So, we'd love to dive deeper into a couple of examples of our dashboards and pipelines we've built at Grafana Labs, and we really hope we can inspire you to consider whether you can apply Grafana in your business context when you get home.

Awesome! Now let's jump into our demos here. The first thing is that all these dashboards are going to be up on play.grafana.org or learn.grafana.net. We'll have a QR code at the end if you want to check that out.

The first example is a dashboard that we actually created for our product teams, namely our product design and engineering folks. The idea here was that we really wanted to help visualize and understand the Kubernetes monitoring adoption funnel. We've essentially established these dashboards for a number of different critical user journeys throughout our product. This one in particular is looking at four key stages: awareness, activation, engagement, and our "aha" moment.

What we were able to do with this is essentially put the power in the hands of our end users to inspect how our funnels are doing on a daily basis. They can look at the aggregate flows in the typical kind of funnel fashion, finding some of the drop-off rates and pull-through rates for each step, as well as our key KPIs around adoption percentage, time to set up, and time to value.

The cool thing that we can start doing is adding annotations on top. One of the things that we typically want to do is have this baseline understanding of our business, but then start to see how that changes as the overall user experience begins to change. As we launch different A/B tests, we can essentially have these annotations come up based on the underlying data. 

What's awesome here is that this is based on the BigQuery data. We actually don't have to have an analyst go in and annotate manually each of these different events. You can see that you probably could have figured out what was going on here without the annotation, but it's super helpful to see that we launched this A/B test to 30% of our population. 

Down here, you can also identify that as we launch this, there are now two different experiences out there in the wild, which is causing this distribution to increase. Then, as we end the tests and roll it out to 100% of our population, that goes back to kind of our longer-term average.

The other thing that we do quite often in most of our dashboards is start to build in interactivity. For this case, we're looking at different monthly cohorts, and we allow our users to essentially slice and dice this data, leveraging data links as well as the dashboard variables to get in, start inspecting, and get their hands on the underlying data.

The next set of panels that we're looking at is one around our A/B testing measurement. This is something that we've seen really be impactful for our growth in onboarding teams. You can imagine this is essentially something that we've built for all of our A/B tests going back for the last two, two and a half years, where we can combine the underlying data that we have in BigQuery with metadata about what we're testing and what we've seen be successful versus not.

That's been really helpful for us, not only as humans looking at this data and looking at that ledger of past history, but it's also been really helpful for us to bring this context to our agents and LLMs. What I was very curious to see was whether or not we would be able to have the assistant go in and essentially conduct an A/B testing measurement for our tests. 

This is typically something you'd have to go and, as a PM, kind of ask your analyst or maybe put into a specialized tool to run A/B testing. But what we're able to do here is, because we have all of the context in this dashboard, pass the dashboard to our assistant and ask generally, "Can you please go and test for statistical significance?" 

What's pretty sweet is that because we have the panels and because we can reference the dashboard, the assistant can more or less not have to start from scratch. It goes in and starts to read the underlying panels. You can parse through all the JSON here, and as it's working, it'll eventually, fingers crossed, come up with an understanding of the underlying test data that we have. This engagement test that launched...

from March 1st through March 31st, and then ultimately it decides the correct kind of two-proportion Z tests for us to go ahead and do that A/B testing and builds that into the BigQuery data. 

What's sweet here is that, more or less, it was able to do all the statistical calculations in BigQuery for us and ultimately come up with this pretty nice summary for our tests. It turns out this synthetic data that I created wasn't actually that fair of an A/B test. This was very, very significant in terms of the success of the test.

The last thing I'll mention here is that we, at Grafana Labs, used the assistant quite often in our day-to-day work. The inflection point that happened for us was when we added the assistant into our Slack channels. I think we, like most remote companies, do a lot of our work in Slack. By having the ability to have the assistant come in—not only have access to the underlying data and the dashboards that we just saw, but also be able to look through the threads of conversations that we've been having—has just been a really great way to build in the assistant again into our daily flows.

So if you are interested in doing something like this for yourself, I'd highly recommend coming into the assistant settings and into the SQL table discovery tab and essentially turning this sink on for both your underlying kind of BigQuery or wherever you're storing your data, as well as into your semantic layer. Essentially, what that'll do is take all the metadata from your backend databases, put that into a vector database, and allow the assistant to do a much more efficient query over that metadata when looking for the right table or right column to end up using.

Great, so I'm going to show another example of how we're using Grafana as our BI tool. This, similar to the dashboards you've just seen, uses synthetic data. You can see customer names like Crest Commerce and Lunar Links. It's a smaller data set than we use internally—300 accounts—because this is on playgrafana.com; it's on the demo environment, so you can all explore this later. 

Apart from that, this dashboard is exactly as we use it internally. The schema is the same, and the panel is the same. You can see exactly how we're running our business. This dashboard is for our sellers, salespeople, and our SDRs in go-to-market. They do a fantastic job; we're very proud of them. They make sure we're getting paid, and we realized pretty early that we could keep them doing even better work by giving them the best tools and the best data. 

Our revenue operations team built this dashboard for them, and our internal version is loading hundreds of thousands of records from our Salesforce data. All of our prospects, all of our contacts, and each of those rows itself has over a hundred columns. So there's a lot of data being loaded in here, but it's all aggregated up to this high-level view of the entire sales pipeline for Grafana Labs. 

We get this top overview, and then we start to break it down by account size, how far through the sales funnel they are, how much activity they're showing on a couple of different axes, and even how close we are to hitting our targets for this quarter. More importantly, this has got over 15 different dimensions at the top here where this data can be sliced and diced, and different people can get in and slice it as they need. 

Our execs, who own large or smaller teams, can focus in on their region or sub-region, and then they can see if their teams and their region are on track and lean in and help where necessary. That's at the top of the organization. Then, at the cutting face, our sellers and SDRs are able to use the very same dashboard. They can slice and dice by some of these signals, and they can filter down to just the few accounts that are relevant to them and that they'll pursue that day or that week. 

This has been fantastic; it has been working, and it's been super powerful. We're proud of it. In the process of building this, we realized there were further opportunities to improve the UX even further. So I started to implement support for this semantic layer. 

So what is it? Well, it sits in front of the warehouse and connects to Grafana, and it allows for three really significant improvements with how we are able to interact with our data through Grafana. 

The first is that it allows you to click data within panels to filter and drill through dashboards. I'll show you that. The second is, once it's set up, you don't have to write SQL, you don't have to know SQL, and you don't have to know your data model either. I'll show you that in practice. The third way is it really elevates what AI agents and the Grafana Assistant can do with the data in your warehouse. 

So let's have a look at how that works in practice. This version is just built from a SQL data source directly. Our sellers wanted to be able to click this data and filter the dashboard directly. But if you try to inject something like "where behavior signal equals high" into a SQL query, that's this SQL query. They might have CTEs, they might have subqueries; you're inevitably going to hit a wall where you break the SQL query eventually. So we couldn't make these interactive. 

That was the first one about filtering from the panel. The second one, not needing to learn SQL. In the SQL world, this is built from a SQL query, which is almost 30 lines long. You have to know the table, you have to know what other tables to join and how to join them, and you also have to manually reference all of these filters as well. So this takes a bit of time to build a panel like this and also a bit of effort to maintain. 

Okay, so that was the status quo. Let's have a look at what it looks like when we rebuild this exact same dashboard, but we build it on top of a semantic layer. Specifically, this is a data source that wraps up a semantic layer. 

So let's try filtering. All of a sudden, you can click and click again, and not only do you filter this panel, but you filter the entire dashboard. We've now been able to drill down to the accounts that have this high behavior signal; they're the ones that are showing engagement, and we can drill even further. Now we want to drill again into the ones that have a high activity pulse, and suddenly we've drilled twice and filtered this dashboard down so quickly and intuitively. We've got those four accounts that we're going to engage with this week. 

So that's super powerful. That was the first benefit. The second benefit, not needing to learn SQL, let's have a look at how this panel was built when you use a semantic layer. I've only had to make 1, 2, 3, 4 selections, and I'm able to get the exact same data to render in the panel. 

How is that? How does that work? How is that possible? Well, the semantic layer is generating the SQL needed. So two things to learn to see here: first, only having to make four selections. It's much quicker to build that panel, and it's much, much easier to maintain as well. So we can go a lot faster when we're building these dashboards. 

Also, not having to write SQL anymore vastly lowers the barrier to entry, right? So people right across our business now are able to issue queries and get insights from the data in our warehouse. They don't need to learn SQL, and they don't need to learn the data model. This is huge. 

Let me just show you one more thing here with a semantic layer. If I come down here, I can also filter from tables. So here I'm choosing to filter to stage qualification. You see the filter lands up here: OPP stage equals qualification. If I edit this panel, you can see the SQL generated is from these selections made to define the panel, also from the filter up here: OPP stage equals qualification. So here it has injected a where clause, stage name equals...

That question mark will be populated as qualification. So how is this working? How does this overcome the problem I described earlier? This depends on having access to the table with the suffix OPP split. 

Well, in order to make sure that this SQL will run, an extra join has been made, and it's joined in the table we need, OPP split here. If you watch carefully, if I were to clear out this filter, not only will we lose the WHERE clause, but we'll lose the join as well, as the semantic layer is generating this SQL dynamically for us. 

So there you go. It's able to inject the joins it needs and traverse that graph of tables to apply any filters it needs to. That's the second of the two benefits. But you might be thinking, why do we need a technology to generate SQL for us today? We've got the generative AIs, right? The LLMs, they're going to generate all the SQL we need today. 

Well, unfortunately, they do hallucinate, and when they do, they're incredibly confident about it. They may forget to consider all of the wrinkles of our data model or the nuances of our data. Let me show you where this is defined. The semantic layer consists of this configuration in YAML files, which is metadata around your tables and your columns. 

It consists of things like descriptions and titles, and also how to make aggregations. For example, is a measure a count or a sum? Crucially, this forms the source of truth for your business metrics. Here we've got one named total ARR. Different companies define ARR in different ways, and what you don't want is your LLM, your agent, to be making an assumption about how you define ARR within your company. 

Some of these definitions are not straightforward either. This one you can see includes some logic as well. So we definitely want this single source of truth to be consumed across all of our panels and all of our dashboards. If it ever gets updated, we want all of those dashboards to still show the correct data. We also want our agents to consume from that single source of truth.

Now, let's go and have a look at what happens when we send a query to the Grafana Assistant. Here, I'm asking how many customers are there in Amir. You can see from this blue icon that it's querying the BigQuery SQL data source to get us an answer. It's made four queries here, and you can see the first one actually failed, but it still got us an answer. So that's pretty great.

Now, if I ask it to repeat using the Cube tool, which is the technology we're using wrapped up in that data source to power our semantic layer, you can see it's only made one or two queries. So it's getting us an answer faster, more cheaply, burning fewer tokens, and using that single source of truth. You can see that coming out here; it's giving us the same answer but with more granularity. 

So suddenly, we're leveling up our agents. This may not look super significant in this example, but it's the times when the agent might get something wrong with confidence that really bite, where this will really help you. 

We've done this by building a data source that wraps Cube. Cube is an open-source project, like Grafana. You can download it and self-host it today, and then you can install the data source as well, which is also free and open-source. The repos are on GitHub here, and we would love for you to give this a try in your own self-hosted Grafana or in your Grafana Cloud. I'd love to hear what you think.

If we return to the slides, Chris and I will be at Ask the Experts tomorrow at 3:15. Please do come and find us. The demos that we showed today are all available at the demo booths and at play.Grafana.com, which is at the first QR code. We'd love to field any questions you have. Thank you. (audience applauding)

## Raw YouTube Transcript

- Hey everyone. So yeah, in this session we're
gonna be talking a little bit about how we've been
building Grafana dashboards for BI internally at Grafana Labs and how it's become this
visualization layer on top of our business data stack. But before we jump in a
little bit about ourselves. - Hello, I'm Sam Jewell. I'm a software engineer at Grafana Labs. I've been working on building support for a semantic layer into Grafana. - And I'm Chris. I was one of our first
data hires here at Grafana, and I've led our central data and analytics team over the
last two, two and a half years. So our agenda for today,
we're gonna start off with a bit about our why. So why do we build dashboards
like this internally at Grafana and why might you be
interested in doing so as well? And then we'll spend the
majority of our time going through a couple different demos, showing a couple dashboards
around product analytics, probably one around sales
analytics, as well as some of the cool new features we're seeing around Grafana Assistant,
our Slack integration and the awesome work
that Sammy's been doing around the semantic layer. And then at the end, we'll open it up for any Q&A from all you. - So you've adopted Grafana and you use it with your
SREs, with your engineers, with your technical staff, and you use it to monitor, you use it, especially when things go
wrong, it's there for you and it's a flexible tool. So perhaps you could
apply it in more context. What about in your business? Grafana can do incredible things. At Grafana Labs, literally
every one of our departments use it from product management
to sales and marketing and with a few other tools,
we use it across the board. So we use it for product analytics
to answer questions like, is my feature being used? We use it for project management to understand whether our
engineers are becoming blocked. We use it for business
intelligence that's BI to answer things like which prospects should I be calling today? And of course it's our
observability tool as well. With the all of the rest of our products, we are so many questions, starting with the simplest is my service up? So why do we use Grafana for everything and might you be able to do the same? There are a few reasons
that are unique to us, but there are many reasons
that may apply to you and be relevant to your context. So the first reason that's unique to us, well we build Grafana of course. And so to us using Grafana
in such a diverse range of contexts is dog fooding and it helps us to make Grafana that versatile tool that it is today. Another is we're heavily
invested in OpenSource and our code, but also our backlogs, our issues all live out
in the open on GitHub. And so from there it's a
very simple step to connect that to Grafana and visualize it. But the other reasons will
be relevant to everybody. If you're able to use fewer
tools, you can save a lot of complexity, save a lot of money. We also find that it means
more of our staff, almost all of our staff are able to
operate side by side in Grafana in that same tool, allowing
for seamless collaboration so we can collaborate across
roles, across departments and see the results of one
another's work super easily. And then there's the strength
of Grafana, the tool itself, it has that big tent of data sources. You can query data from
two different places and see it side by side
in the same dashboard, even blend it in the same panel. You can alert on absolutely anything and it's fast, it's low latency,
you can throw a fire hose of data at it and it barely blinks really. So we'd love to dive deeper
into a couple of examples of our dashboards and pipelines
we've built at Grafana Labs and we really hope we can inspire you to consider whether you can
apply Grafana in your business context when you get home, so. - Awesome, yeah. So now let's jump into our demos here. The first thing is all these
dashboards are gonna be up on play.grafana.org or learn.grafana.net. We'll have a QR code at the end
if you wanna check that out. The first example is a dashboard
that we actually created for our product teams, namely our product design
and engineering folks. And the idea here was
that we really wanted to help visualize and understand the Kubernetes
monitoring adoption funnel. And we've essentially
established these dashboards for a number of different critical user journeys throughout our product. This one in particular is
looking at four key stages across awareness, activation,
engagement in our aha moment. And so what we, what we were able to do with this is essentially
put the power in the hands of our end users to, you know, inspect how our funnels are
doing on a daily basis. Look at the aggregate
flows in the typical kind of funnel fashion, finding
some of the drop off rates, pull through rates for each step, as well as our key KPIs
around adoption percentage, time to set up as well as time to value. And the cool thing that we
can start doing is adding on annotations on top, because one of the things that
we typically wanna do is have this baseline understanding
of our business, but then start to see how that changes as the overall user
experience begins to change. So as we launch different AB tests, we can essentially have
these annotations come up and be based on the underlying data. So what's awesome here is that this is based on the BigQuery data. We actually don't have
to have an analyst go in and annotates manually each
of these different events. And so you can see, you
probably could have figured out what was going on here
without the annotation, but it's super helpful to see
that we launched this AB test to 30% of our population. Down here and then you can
also identify that, you know, as we launch this, there are
now two different experiences out there in the wild,
which is causing this distribution to increase. And then as we end the tests and roll it out to a hundred
percent of our population, that goes back to kind of
our longer term average. The other thing that we
do quite often in most of our dashboards is start
to build in interactivity. So for this case, we're looking
at different monthly cohorts and we allow our users
to essentially slice and dice this data,
leveraging data links as well as the dashboard variables
to, yeah, get it in, start inspecting and get their hands on the underlying data. So the last or the next set of panels that we're looking at here is one around our AB testing measurement. And this is something that
we've seen really be impactful for our growth in onboarding teams. And you can imagine this
is essentially something that we've built for all
of our AB tests going back for the last two, two and a half years, where we can combine the underlying data that we have in BigQuery
with metadata about what we're testing, what we've seen be successful versus not. And that's been really helpful for us, not only as humans looking at this data and looking at that
ledger of past history, but it's also been really helpful for us bringing this context
to our agents and LLMs. And so what I was very
curious to see was whether or not we would be able to
have the assistant go in and essentially conduct
an AB testing measurement for our tests. This is typically
something you'd have to go and as a PM kind of ask your analyst or maybe put into a specialized
tool to run AB testing. But what we're able to do here is because we have all of the
context in this dashboard, past the dashboard to our assistant and ask generally, can you please go and test for statistical significance? And what's pretty sweet is that because we have the the panels and because we can
reference the dashboard, the assistant more or
less can not have to start from scratch. It goes in and starts to
read the underlying panels. You can parse through all the JSON here and as it's working, it'll
eventually, fingers crossed, come up with an understanding of the underlying test data that we have. This engagement tests that
launched from March 1st through March 31st, and
then ultimately it decides the correct kind of two
proportion Z tests for us to go ahead and do that AB testing and builds that into the BigQuery data. And so what's sweet here is that more or less it was able to do all the statistical
calculations in BigQuery for us and ultimately come up with
this pretty nice summary for our tests. It turns out this synthetic data that I created wasn't actually
that fair of an AB test. This was very, very significant in terms of the success of the test. The last thing I'll
mention here is that we, at Grafana Labs used the
assistant quite often in our day-to-day work. And the inflection point that happened for us was when we added the assistant into our Slack channels. I think we like most, you know, remote companies do a
lot of our work in Slack. And so by having the ability
to have the assistant come in, not only have access to the
underlying data, the dashboards that we just saw, but also be able to look through the threads of conversations
that we've been having, has just been a really great way to build in the assistant
again into our daily flows. So if you are interested in
doing something like this for yourself, I'd highly
recommend coming in the assistant settings and into the
SQL table discovery tab and essentially turning this sink on for both your underlying kind of BigQuery or wherever you're storing your data, as well as into your semantic layer. Essentially what that'll
do is take all the metadata from your backend databases, put that into a vector database and allow the assistant to do a much more efficient query over that metadata when looking
for the right table or right column to end up using. - Great, so I'm gonna show another example of how we're using
Grafana as our BI tool. This similar to the dashboards you've just
seen uses synthetic data. So you can see customer
names like Crest Commerce, Lunar Links, so, and it's a smaller data
set than we use internally, 300 accounts because this
is on playgrafana.com, it's on the demo environment, so you can all explore this later. But apart from that,
this dashboard is exactly as we use it internally. The schema is the same,
the panel is the same. So you can see exactly how
we're running our business. This dashboard is for
our sellers, salespeople and our SDRs in go to market. They do a fantastic job,
we're very proud of them, they make sure we're getting paid and we realized pretty early that we could keep them
doing even better work by giving them the best
tools and the best data. And so our revenue operations
team built this dashboard for them and our internal
version is loading hundreds of thousands of records from our Salesforce data. All of our prospects, all of our contacts, and each of those rows itself
has over a hundred columns. So there's a lot of data
being loaded in here, but it's all aggregated up
to this like high level view of the entire sales
pipeline for Grafana Labs. So we get this top overview and then we start to break
it down by the account size, how far through the sales funnel they are, how much activity they're
showing on a couple of different axes and even how close to hitting our targets
we are for this quarter. And more importantly, this has got over 15 different
dimensions at the top here where that this data
can be sliced and diced and different people can get
in and slice it as they need. So our execs who own large or smaller teams can
focus in on their region or their sub region and then
they can see if their teams and their region is on track and lean in and help where necessary. That's at the top of the organization. And then at the people
at the cutting face, our sellers, our SDRs are able to use the very same dashboard. They can slice and dice
by some of these signals and they can filter down to just the, you know, the few accounts
that are relevant to them and that they'll pursue
that day or that week. And this has been fantastic,
this has been working, it's been super powerful
and we're proud of it. In the process of building this, we realized there were
further opportunities to improve the UX even further. So I started to implement
support for this semantic layer. So what is it? Well it sits in front of the warehouse and connects to Grafana and it allows for three really
significant improvements actually with how we are able to interact with our data through Grafana. So the first is that it allows you to click data within panels to filter and drill through dashboards. I'll show you that. The second is, once it's set up, you don't have to write SQL,
you don't have to know SQL and you don't have to know
your data model either. And so I'll show you that in practice. And the third way is it
really elevates what AI agents and the Grafana Assistant can do with the data in your warehouse. So let's have a look at
how that works in practice. So this version is just built from a SQL data source directly. So our sellers wanted to
be able to click these data and filter the dashboard directly. But if you try to inject something like where behavior signal
equals high into like a SQL query, that's this SQL
query, this SQL query, they might have CTEs, they
might have subqueries, you're inevitably gonna hit a wall where you break the SQL query eventually. So we couldn't make these interactive. And so that was the first one. That was the first one about
filtering from the panel. The second one, not needing to learn SQL. In the SQL world, this is
built from a SQL query, which is almost 30 lines long. You have to know the
table, you have to know what other tables to join
and how to join them. And you also have to
manually reference all of these filters as well. So this takes a bit of time
to build a panel like this and also a bit of effort to maintain. Okay, so that was the status quo. Let's have a look at what it looks like when we rebuild this exact same dashboard, but we build it on top
of a semantic layer. Specifically this is a data source which wraps up a semantic layer. So let's try filtering. All of a sudden you can
click and click again and not only do you filter this panel, but you filter the entire dashboard. And so we've now been able
to drill down to the accounts that have this high behavior
signal, they're the ones that are showing engagement
and we can drill even further. Now we want to drill again into the ones that have a high activity pulse and suddenly we've drilled twice and we filtered this
dashboard down so quickly and intuitively and we've got those four accounts that we're gonna engage with this week. So that's super powerful. That was the first benefit. So the second benefit,
not needing to learn SQL, let's have a look at
how this panel was built when you use a semantic layer. I've only had to make
1, 2, 3, 4 selections and I'm able to get the exact same data to render in the panel. How is that? How does that work? How is that possible? Well the semantic layer is
generating the sequel needed. So two things to learn to see here. First, only having to
make four selections. It's much quicker to build that panel and it's much, much easier
to maintain as well. So we can go a lot faster when we're building these
dashboards, but also not having to write SQL anymore
vastly lowers the barrier to entry, right? So people right across our
business now are able to issue queries and get insights from the
data in our warehouse. They don't need to learn SQL and they don't need to
learn the data model. This is huge. Let me just show you one more thing here with a semantic layer. If I come down here, I can
also filter from tables. So here I'm choosing to
filter to stage qualification. And you see the filter lands up here. OPP stage equals qualification. And if I edit this panel, you can see the SQL generated is generated
from these selections made to define the panel
also from the filter up here, OPP stage equals qualification. So here it has injected where clause, stage name equals question mark. That question mark will be
populated as qualification. So how is this working? How does this overcome the
problem I described earlier? This depends on having access to the table with this suffix OPP split. Well, in order to make sure
that this sequel will run, it's made an extra join and it's joined in the table
we need, OPP split here. So if you watch carefully, if I was to clear out this filter, not only will we lose the where clause, but we'll lose the join as
well as the semantic layer is generating this sequel dynamically for us. So there you go. It's able to inject the joints it needs and traverse that graph of tables to apply any filters it needs to. So that's the second of the two benefits. But you might be thinking
why do we need a technology to generate SQL for us today? We've got the generative AIs, right? The LLMs, they're gonna generate
all the SQL we need today. Well, unfortunately they do hallucinate and when they do, they're
incredibly confident about it and they may forget to, you
know, they may not know all of the wrinkles of our data model or the wrinkles of our data. Let me show you where this is defined. The semantic layer kind of consists of this configuration in
YAML files, which is metadata around your tables and your columns. So it consists of things
like descriptions and titles and also how to make aggregations. So is a measure account or
is it a sum for example. But crucially this is
forms the source of truth for your business metrics. So here we've got one named total ARR. Different companies define
ARR in different ways and what you don't want
is your LLM, your agent to be making an assumption about how you define ARR within your company. And some of these are not
straightforward either. This one you can see in
lines some logic as well. So we definitely want this
single source of truth to be consumed across all of our panels, all of our dashboards. And if it ever gets updated
for all of those dashboards to still show the correct data. And we definitely want
our agents to consume from that single source of truth as well. So let's go and have
a look at what happens when we send a query to
the Grafana Assistant. So here I'm asking how many
customers are there in Amir. And so you can see from this blue icon, it's querying the BigQuery SQL data source to get us an answer. It's made four queries here and you can see the first
one's actually failed. It has got us an answer.
So that's pretty great. Now if I ask it to repeat
using the Cube tool, Cube is the technology
we're using wrapped up in that data source to power our semantic layer. And you can see it's only
made one two queries. So it's getting us an answer faster, more cheaply. It's burning less tokens and it's using that
single source of trees. And you can see that coming out here, it's giving us the same answer
but with more granularity. So suddenly we're leveling up our agents. And this doesn't look
super, super significant, this example, but it's
the times when the agent might get something wrong with confidence that
really bite, you know, where this will really help you. So we've done this by building a data source that wraps Cube. Cube is an open source, free and open source project. Like Grafana, you can download
it and self-host it today and then you can install the data. The data source as well
is free and open source. The repos on GitHub here,
we would love for you to give this a try in your
own self-hosted Grafana or in your cloud Grafana. I'd love to hear what you think. So if we return to the slides. So Chris and I will be at Ask the Experts tomorrow at 3:15. Please do come and find us. And the demos that we showed today are all
available on the demo booths. They're available at Grafana, sorry play.Grafana.com, which is at the first QR code. And we'd love to field
any questions you have. Thank you. (audience applauding)

