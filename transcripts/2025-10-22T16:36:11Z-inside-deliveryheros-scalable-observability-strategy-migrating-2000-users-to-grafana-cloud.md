# Inside DeliveryHero’s Scalable Observability Strategy: Migrating 2,000+ Users to Grafana Cloud

Published on 2025-10-22T16:36:11Z

## Description

Discover how Delivery Hero built a unified, cost-transparent observability strategy with Grafana Cloud. Andy Howden shares ...

URL: https://www.youtube.com/watch?v=LHc012seJlk

## Summary

In this presentation, the speaker, an engineering director at Delivery Hero, shares the complex journey of migrating over 3,100 engineers from various observability providers to Grafana Cloud. Delivery Hero, a large global company operating in over 70 countries, faced significant challenges due to its diverse tech stacks and independent company operations. The migration aimed to unify observability tools across its brands, improve financial predictability, and streamline communication. Key points discussed include the initial optimism of a fully automated migration, the unexpected challenges in data and dashboard conversions, and the importance of effective project management and user support. The speaker emphasizes the value of OpenTelemetry and the need for early engagement with its implementation to prevent complications. Ultimately, despite the difficulties encountered, the migration was deemed successful, leading to better collaboration and reduced observability costs. The talk concludes with reflections on lessons learned and gratitude towards colleagues and the Grafana team for their support throughout the process.

## Chapters

Here are 10 key moments from the livestream along with their timestamps:

00:00:00 Introductions and Overview of Migration Story  
00:02:30 Introduction to Delivery Hero and its Scale  
00:05:00 Challenges of Multiple Observability Providers  
00:08:15 Migration Goals: Financial Sustainability and Unified System  
00:12:00 Overview of the Migration Phases  
00:15:45 Issues with Data and Dashboard Conversion  
00:20:30 Importance of Project Management and Tracking Progress  
00:24:00 The Role of User Feedback and Support Challenges  
00:30:15 Formation of a Tiger Team for Successful Migration  
00:35:00 Lessons Learned and Future Recommendations  

These timestamps highlight significant points in the discussion, allowing viewers to easily navigate to areas of interest.

# Migration Story: From Multiple Observability Providers to Grafana Cloud

**Good morning, everyone!**  
Can you hear me? Yes, we can. The microphones work! This is going well so far. Hi, I'm here to tell you a bit of a story—one about how we migrated a whole bunch of people from various observability providers to Grafana Cloud. Initially, we aimed for 2000, but we ended up migrating around 3,100 people so far. I checked the dashboards this morning, and I'm here to share the good parts, the bad parts, and the tricky parts of how all of this worked in practice.

## About Me and Delivery Hero

Before diving into the details, there are two key things you need to know. First, **who I am**: I am the engineering director of an organization called Site Reliability Engineering (SRE). We focus on making things more reliable. I currently live in Berlin but was raised in Australia, so if my accent sounds a bit strange, that's why. If you don't understand something, just take a deep breath; this will be recorded.

Now, the second and more important thing is about **Delivery Hero**. How many of you have heard of Delivery Hero or its brands like Glovo, PedidosYa, or Food Panda? (Pause for hands). It seems like these brands aren't as popular here, but let me tell you, Delivery Hero is a large company. We operate in 70 different countries with 40,000 employees and 3 million riders—those who deliver food to your home. We partner with a million restaurants and 800 Dmarts, processing over 10 million orders each day. 

What’s crucial to understand is that we operate **11 different brands**, each with its own management and tech stack, languages, and working styles. This complexity makes it incredibly challenging for us to manage and integrate these companies.

## The Need for Migration

We had a significant reason for migrating to Grafana Cloud. The core challenge was that each of these companies operates independently, lacking a common way to observe their production systems. We had various observability tools—New Relic, Datadog, and Grafana—each with separate accounts that didn't communicate. Trying to take capabilities from one part of the organization to another felt like working with entirely separate companies, complicating our efforts.

The goal was to get everyone onto the same page. Let me give you the punchline of this talk upfront: we accomplished a lot with this migration. Everyone is now using the same system to observe their operations and communicate across organizational boundaries—from South America to Berlin to Korea. We also aimed for financial sustainability. Previous observability providers introduced unpredictability in costs, making it difficult to budget effectively.

We adopted **OpenTelemetry**, which facilitated a massive cleanup. Developers often create numerous dashboards and alerts that they stop using after a couple of weeks. We cleaned up most of that clutter. Most importantly, we're now looking at distributed tracing as our next key technology to integrate our systems.

Initially, our observability costs were around **15-25%** of our cloud spend, which is substantial. After migrating to Grafana Cloud, we're now down to about **6%**. While this number isn't directly comparable, it illustrates the significant reduction in costs and improved sustainability post-migration.

## The Migration Journey

This talk won’t be a fairy tale where everything went smoothly. Instead, I want to share the core challenges we faced. Surprisingly, most of the problems we encountered weren't technical; they were project and people-related. Unlike technical issues, project problems tend to recur and can compound quickly in large organizations.

We organized the migration into **three phases**. We started with a plan in February 2023 to automate the migration fully. Our intention was to lift everyone's data, dashboards, and alerts from the old system to the new one seamlessly. To achieve this, we had to address two main problems: the data problem and the dashboard/alert problem.

### Data and Dashboard Conversion

We found it was too expensive to do the instrumentation upfront. So, we took the vendor-specific SDKs and converted them to OpenTelemetry. We enriched the data and wrote it into Grafana Cloud, effectively migrating everyone’s observability.

However, converting dashboards and alerts was more complex. Dashboards include data, queries, and the way data is visualized, which makes the conversion challenging. Alerts were somewhat simpler, but still required a deep understanding of how the data was represented in the old system versus Grafana Cloud.

We managed to do most of this with the help of professional services at Grafana Cloud, which made our task much more achievable.

### The Reality of Migration

In practice, we had a Gantt chart with two workstreams running in parallel—data conversion and dashboard conversion—followed by an integration phase. Unfortunately, reality didn't align with our plans. Both workstreams encountered challenges. While the data conversion was mostly successful, we faced significant issues with the dashboard conversion.

As we began to integrate, we discovered problems with both data and dashboards, leading to delays. At this point, we realized the importance of understanding if a project is on track. 

To manage project tracking effectively, we introduced a simple system: each project representative would indicate if they were **red, amber, or green** regarding their project's status. This helped us identify issues early and intervene before they spiraled out of control.

### Lessons Learned

Two key patterns emerged from our experience:

1. **Always green projects are at risk**: A project that is perpetually green likely means you're unaware of existing issues. You need to dig deeper.
  
2. **Intervening early is critical**: When problems arise, you must be prepared to change deadlines or deliverables to keep the project on track.

We had to declare a bit of a "bankruptcy" regarding dashboards and alerts. While we successfully completed the data conversion, we couldn't migrate all dashboards, logs, or tracing successfully. Users encountered partially completed dashboards, leading to frustration.

### User Engagement and Support

To help users, we provided training and guidance, but it wasn’t entirely effective. The most successful approach was to integrate help directly into the dashboards, listing known issues and providing tickets for tracking.

Throughout this process, we discovered that developers rarely used most dashboards. We ended up cutting about **80%** of the dashboards from our migration scope, and the out-of-the-box capabilities from Grafana proved to be effective.

As we rolled out the new dashboards, we offered support, but the sheer volume of inquiries overwhelmed our support capabilities. This led to a loss of confidence in the migration. 

### Finding Solutions

During a particularly challenging phase, one organization suggested forming a **tiger team**—a specialized group of people who deeply understood our context. This team helped us alleviate user concerns and boiled down the feedback to manageable issues. Having a friendly ally within the organization transformed our approach, enabling us to address user objections more effectively.

## Conclusion: Migration Success

In the end, we successfully migrated **3,100 engineers** across a multi-billion-dollar business into Grafana Cloud, allowing us to continue delivering food efficiently. While it was a challenging journey, we learned valuable lessons that could help others facing similar migrations.

Would I do it again? Absolutely, yes. Despite the difficulties, we are in a better position now than we were at the start. We achieved our project goals—different brands can now communicate about their production systems, and we’re generating shared value through new dashboards and alerts.

We used OpenTelemetry to handle millions of time series, and Grafana Cloud has evolved rapidly over the past year. As a result, we can manage costs more effectively.

Two main factors drove the complexity of our migration: 

1. The deep embedding of SDKs from previous observability providers in our production systems.
2. The waterfall-like nature of our project management, which didn’t account for the evolving needs of developers.

If we had conducted a smaller pilot first, we could have learned these lessons more efficiently.

I want to extend my gratitude to everyone at Grafana who made this possible: Linda, Stefan, Dee, and the whole team. If you have any questions for me, feel free to find me afterward. Thank you very much!

## Raw YouTube Transcript

Oh, good morning everyone. Can we hear
me? Yes, we can. The microphones work. This is going well so far. Hi. Hi. I'm here to tell you a bit of a story. It's a story about how we migrated a whole
bunch of people from a range of these different observability
providers to Grafana Cloud. It says 2000. We ended up
going a little bit further. This was around 3,100 people so far. This is what I was checking in
the dashboards this morning, and I'm here to tell you the story of
the good parts and the bad parts and the tricky parts, how all of this
stuff worked in practice. Clicker works we're good. There's two things that you need to know
in order to make sense of this talk. The first is who I am. I am the engineering director of an
organization called Site Reliability Engineering.
There's a lot of that going around today. Basically we take care of things that
make us more reliable. I live in Berlin. I was raised in Australia, so I have
a very strange accent. That's okay. If you don't understand me,
just sort of take a deep breath. It will be recorded. The second and far more important
thing is about Delivery Hero. Now everyone's heard of
delivery, actually hands up. Who's heard of Delivery
Hero or Glovo? PedidosYa, Food Panda, any of these
other brands? Fine. Okay. It seems like it's not that popular in
this country or with these lovely people, but Delivery Hero is a very large
company. It operates across the world. It has 70 different countries,
40,000 employees, 3 million riders. The people who actually deliver the food
to your house, a million restaurants, 800 Dmarts, and we do north of 10 million orders
per day. But the most important part of this slide is that little section
there that says 11 brands. We operate 11 of these different
kind of companies across the world. Each of these companies has their own
management stack, their own tech stack, their own language, either language actually speaking in
that country or computing language, their own way of working, their own
style of doing that kind of work. And what we have to do from a central
perspective is deal with each one of these companies. That makes this incredibly
complicated. As a migration, we had a problem. There is a reason
that we moved to Grafana Cloud. We didn't just kind of spontaneously
wake up one day and decide it was a good idea. The core challenge that we have is that
each of these companies that operate across the world, some of these companies
are building these truly world-class, these really exciting capabilities, and we want to take these capabilities
from one of these company and we want to provide it to the rest of the companies
that exist around the world. So if somebody does something amazing in
South America with the Pedidos team, then we can provide that to the Glovo
team or we can provide that to the Talabat team. Or if we're able to build some
central capability like Grafana, we're able to expose that
to the rest of the world. But we had a fundamental challenge because
each of these are separate companies and because each of these kind
of operate very independently, they didn't have a common way of
looking at their production system. So a kind of common diagnostic language. We have New Relic and Datadog and Grafana. Each of those are separate Datadog
accounts that never talk to each other. So if you're thinking about trying to
take a capability from one part of the organization and expose it to the other, it's essentially like working with a
separate company and it just makes these things much harder than they need to be.
So we wanted to get everybody onto the same page. Now I'm going
to cheat a little bit. I'm going to give you the punchline
of this whole talk up front. I know there are many
management people in here, so I'm going to make this
sort of fairly numeric. We did accomplish a lot
with this migration. We were able to get everybody
into that single pane of glass. Everybody now uses the same system to
observe their stuff and they're able to talk to each other across these
organizational boundaries, the South Americans to talk
to the people in Berlin, people in Berlin can talk to the
people in Korea, so on and so forth. The other thing that we aim for as
part of this project was financial sustainability. There have been many hints to some of the
challenges that we have had with other observability providers In
making these things sustainable, we would suddenly find that people had
turned on a capability that they found very exciting and they'd
left that capability running
for a couple of months and they'd suddenly get this bill and it
would be problematic or they'd be sort of surprising ways in which the pricing
worked or other bits and pieces. It became very hard to make the financial
aspect of observability predictable, which is the most important
part, how much it costs. You can budget for that predictability
so that you can fit within the 12 month budgets that companies work
for is an absolute must. We were able to give it everything on
OpenTelemetry. OpenTelemetry is good. That's part of what I will talk about. We were able to do an
enormous amount of cleanup. Turns out that developers
create an enormous number
of dashboards and alerts and things like that, and they look at them for a good two
weeks and then never look at them again. So we just clean most of that stuff
up. And lastly, most critically, because this is a large
integrated company, we're looking at distributed tracing as
our next key technology to integrating against these things to make working with
this software so much easier. The core punchline at the start of this project, we were looking at around 15 to 25% of
our observability cost relative to cloud cost spend, which is quite a large amount if you
think about the amount you're spending on AWS and Google Cloud and whatever,
and we're now looking at around 6%. Now to be clear, this
number cheats a little bit. They're not directly comparable,
but it gives you an idea. We're able now we're in a position where
things are much cheaper and much more sustainable, much more predictable after this migration
to Grafana Cloud and after the move from these proprietary
SDKs towards OpenTelemetry. But while that's the punchline, I'm
here to tell you about the journey. I'm doing this storytelling
thing all backwards. That's fine. The thing about this is it's not going to be a talk where I
stand up here and I tell you all of the beautiful ways in which this went
absolutely flawlessly and things worked wonderfully from the start
and we had no problems. That's not what happened, and I would feel disingenuous standing
up here telling you it's going to be very easy. It's not. I'm going to talk about some of the core
challenges that we had along the way. The thing that I need to convey to you
is because Delivery Hero is such a large and complex organization, most
of the problems that we had, they weren't technical problems.
From a management perspective, and I'm going to annoy all of my
engineering colleagues by saying this, but a technical problem can be
solved from a management perspective, by applying talent and time, and they're usually fairly predictable.
Either things work or they don't. Project problems cannot
be solved in the same way. They tend to reoccur over and over
again and people problems can compound enormously quickly as you're
working with large organizations. So I'm going to tell you mostly about the
project and the people lessons and the technical lessons we can absolutely
chat about. I'm a huge nerd. I would really enjoy that.
But in another conversation, we ran this project in
three phases. I would say. We had this project organized from
the start. We were sitting there in, I don't know, it was February, 2023
or something, February, 2024. God, it was only last year and we had a plan. We were going to fully automate this
migration. It was going to be perfect. We were going to take everyone's data
and their dashboards and their alerts and we're going to lift them from one system.
We're going to improve them to the new system. It's all going to work
wonderfully. Developers will love us. It's going to be great.
In order to do this, we had to solve two problems. We
had to solve the data problem. We had to solve the dashboard and
the alert problem, the data problem. It was too expensive for us to do
the instrumentation upfront. Instead, what we did is we took the instrumentation
that was provided by these vendor specific SDKs and we converted it from
that vendor's proprietary format into open telemetry. We then sort of further convert it from
a Delta series to a cumulative series, enrich it a little bit in the same way
that the previous providers did in their backend, and then we write that into
Grafana Cloud, thereby sort of seamlessly, seamlessly migrating everybody from their
previous observability provider into Grafana Cloud.
This is complex, but definitely doable. What is surprisingly more complex is
the conversion of dashboards and alerts into something that is
usable in Grafana Cloud. And the reason this is more complex is
not only do you have to think about the construction of the data itself,
which is fairly predictable, but the dashboards include the data. They include the queries to the way
the data is represented in the previous system. They include the widgets that visualize
that data in a specific way and that is composited into a dashboard that renders
these things in a fairly constructive way. Alerts are less complex, I would say, but you still need to understand how
the data was represented in its previous system and then how it can be represented
in the same way in Grafana Cloud. So the absolute complexity
of this was quite difficult. We managed to do most of it, and I have to say a thank
you to professional services
at Grafana Cloud. This was a team we worked with at Grafana
in order to make this whole thing a lot more achievable than it
would've otherwise been. Here's what this looked like in
practice. We had this beautiful timeline. It's a Gantt chart. Yes,
I know I'm management. We had the data conversion work stream
and the dashboard conversion work stream running in parallel, and then we'd have this integration
period where we'd start using the data conversion and the dashboard conversion
to check themselves against each other and then we'd pass
these things onto users, whereas users would then check these
dashboards and we'd be sort of away and free things are successfully migrated. That is not what happened. What happened instead is
what you see on your screen. We had these two work streams running. We had the data conversion work stream
running and the dashboard conversion work stream running, and they
started to run into challenges. We did actually manage
to make this all work. Part of the technology that we use
to make this all work as part of the OpenTelemetry project actually built by
some people at Grafana, among others, it is the Datadog to
OpenTelemetry conversion pipeline. So if you're looking at this yourself
and you're like, ah, how do I do this? Then don't worry, a whole bunch of
the lessons are already open source. But the core challenge we had is as
we were talking to the teams doing the migration, as we were actually
having the discussions, look, are we on track and are you delivering
things correctly and sort of is this all going to work? The teams
would get back to us and say, of course things are going to
be fine. Don't worry about it. We are working and things
are happening as they should. We're making progress
with the data conversion. Some of the dashboards look really
good, everything's going to be fine. And we believed this right up until
it was time to start integrating these things against each other where we checked and we started to find
that there were problems, there were problems in the data conversion
and there were many more problems in the dashboard conversion itself, and it was only at the moment where we
started to try and compare these things against each other where we were
starting to be in a position where, look, this project is starting to run late and
then this project is getting very off track, and then we're in a position where
this is getting very uncomfortable and here's where the first lessons
start to apply. If you are running any large technical project. To be clear, this has nothing to do with
migration itself as a project. Every large and complex technical
project will run into risks, and the most important thing you can do
from a project management perspective is to understand if that project
is on track. Sounds easy, practically a little bit more complicated. The way in which we do
this now is very simple. Essentially we assign someone to figure
this out. If the project is on track, they represent the success of the
project and we ask them, are you in red, amber, or green? If they are
in green, the project is good. We're going to be delivered on time.
Everything is okay. If they are in amber, there are some problems with
the project. That's also okay, you believe that you can start
to fix this. If you are in red, the project's not going to work.
That's also okay. It is just the case that we need to change
something about this project in order to be successful. Now, there's two patterns of
projects that are going to fail. A project that is always green is the
project that is least likely to be successful. The reason for this is because every
technical project runs in a problem and if a project is always green, what happens is you haven't figured
out what the problems are yet, so you need to go digging. The second and much easier case is a
project that goes from green to amber to red, fine. Some things turn out to
be more complicated than we expected. You can start to intervene and start to
address things where a project is off track. You have to change what you expected to
deliver within the project and you have to be far more aggressive than might
be comfortable. The thing about running these large projects is as
you're moving through the project, something will start to go wrong and
the developers will think to themselves, okay, great, this went wrong, but don't
worry if everything else goes right, we'll be on time, and then the next thing goes wrong and
then they think to themselves, oh God, okay, it's fine. If everything else goes right and
then we get a miracle over here, then we'll all be fine. And then the next thing goes wrong and
you end up in this position where in order to complete the project,
you need a stack of miracles, which is just probabilistically
unlikely to happen. So you need to jump in there.
You need to change deadlines, you need to change what
you're going to deliver. You need to change something in order
to make this successful. And we did. We changed what we would deliver.
Essentially, we had to declare a bit of bankruptcy on
the dashboards and alerts. Sounds bad, not so bad in the end,
I will tell you why, but we delivered as much as we could. We were able to absolutely
complete the data conversion stuff. The OpenTelemetry to Datadog to
OpenTelemetry conversion works fine. It's running in production for many of
these companies around the world today. The dashboard conversion,
we got pretty well. We got most of the time series
converted. We didn't get the dashboards, the logs or the tracing
converted successfully, and we ended up at this point where we
started handing these things to users and a user would get this dashboard that we
would complete it and they would open this dashboard and they would see
some things that were mostly correct. They would start to see their panels.
Some of the panels would have information, some of that information would be missing.
There's a range of reasons for these things to be missing. Things like submitted directly to
the API or not integrated against the SDK or things derived server side in the
previous vendor or things deployed in some sort of strange place
that we hadn't discovered yet. This is an amazing project to discover
your shadow IT organization by the way, or there'd just be query
differences between the tooling, minor bugs and the conversion.
But users don't care. A user will open the dashboards,
they'll see the dashboard, they'll look at it and they'll say,
it's broke. And you'll say, yes, but you have to fix it. And
they'll say, and here's a ticket. And it's very frustrating. We really tried to coach users
on how to make this migration successful. We did these trainings,
we did these, ask us anything. We worked with Grafana to get people
around the world to sit in a room with 'em and actually coach them through this
stuff. None of it was super effective. The only thing that was meaningfully
effective was in the converted artifacts themselves. In these dashboards,
in these alerts and things, we provide the help directly in the
dashboard. A user opens their dashboard, they see their half completed dashboard
and they see instead of nothing, look, we know this dashboard has problems. Here
is a list of the problems that it has. If you have this problem, don't worry,
we're going to fix it. Here's the ticket. You can track it over here. If you have this problem and
you're under this condition, then you need to check X, Y, and Z. You need to integrate your data source
so it's successful and then the dashboard will work correctly. One of the things I was thinking about
as I was sitting over there watching the early morning talk, this would've been much more effective
if we were able to deploy some sort of magical AI tool in which we could
enrich the context to say, look, here's a bunch of things that may be
missing. Here are the things that you need to check. Please go and do a bunch
of stuff. But we didn't. Instead, we just kind of handcrafted this help. One of the lessons out of this migration,
developers don't use most dashboards. We cut about 80% of the dashboards out
of our migration scope, and it was fine. There was a series of core dashboards
that everybody checks on a regular basis, but that's about it. And one of the surprising things is the
out-of-the box capabilities from Grafana are really very good. They're able to replace an enormous chunk
of what people were doing manually in their previous observability tools. So
thank you very much to the AppOlly team. That tool has evolved enormously over
the last 12 months. Through that, it was much easier for us to
make this migration successful. The second thing that happened is we
rolled these dashboards, the alert, everything else out to
the users and we said, here is the help. Here is the
training, here is the guidance, but don't worry if you get
stuck, you can reach out to us. You can lodge a ticket.
We'll make this work. Now, if you offer this to
developers, they will, we're talking about thousands of people, not just developers but the rest
of the engineering community. And they opened these dashboards and
they looked at them and they said, great, we have questions. And
we said, no worries, but we were immediately overwhelmed with
the sheer amount of support that we had to deal with, and this support
varied quite a lot on its quality. Some of it was deeply technical. We had some very smart
people who understood the
details of the migration and the inners of Mimir and how this
transforms, and it was amazing. It was able to point out bugs that we
had, but we had a lot more feedback, which essentially said, my migration
doesn't work. Please fix it for me. The problem is the amount of tickets
that we have just overloaded, the support capability that we have. As users started to get no
answer for their project, they started to get even less
confidence in this migration, and we were in this position where we'd
lost the confidence of community to make this all work. Obviously, this turns out
okay, don't worry, I'm getting there. Thank you very much. By the way, we have people at Grafana that we
rely on in order to make this work. There's one of them called Seamus, and he does an amazing job of making sense
of our entire complexity and bringing us to the support that
we need. So here we are. We're in the darkest hour of our migration
and we're trying to make this whole thing work, and one of the organizations that we
were working with turned around to us and said, look, you need this migration
to work. We said Yes, and they said, we need this migration to work.
And we said yes. And he said, what we can do is we can supply some
people from our organization so people who deeply understand the context of our
organization and we'll tie them together with you and then together you can see
what you can do in order to make this migration work. Essentially, we built a kind of tiger
team or specialist team for
this organization and this migration. This was fundamentally
transformative for us. What it was able to do, it was able
to take the enormity of feedback, all of this user context
and these user problems, and it was able to boil it down to a
much smaller set of issues. Additionally, they were able to take the kind of
context of that organization and they were able to start to address just themselves
some of the problems of the migration so that users would start to see things
work and start this to become more successful where we were
having conversations with
users instead of us being a central team, being please for God's
sake, adopt our tooling. We had a friend, we had an ally within that organization
who would be part of that conversation. Who was staked on the success of this
migration and who was able to overcome some of those less technically
deep user transitions or user objections? Special thanks.
By the way, this is an internal team. There's a guy called Sebastian,
another guy called Gabe. They were the people who
put together this team, and this was the redemption arc for us. This was a way in which this
migration transformed successfully, and at this point we were
pretty much complete. We get to the end. We've converted
all the dashboards and alerts, we've converted all the data. We
have to actually hand this to users, and then users need to review these
artifacts and accept them so that we can sort of switch off their
old observability providers, make this whole thing work.
This one is pretty funny. Grafana is an amazing tool for bringing
all of the data together in one view. So immediately developers took advantage
of this and they took their old observability provider and they took
their new observability provider, which is Grafana Cloud, and they put them together in the same
graph and they overlaid that data and it looked mostly correct. It looked just slightly different, and the reasons for these slightly
different are very legitimate things like just the way in which rate is
calculated is slightly different. There's a small delay in the way in
which we convert all of the data. There are very minor differences
in these tools, but again, we ended up in this conversation with
developers about whether or not this was working and whether or not this
would be successful. We had to again, shift the conversation. We did go really deep on understanding
the internals of how Mimir works in order to understand whether or not the problem
actually existed or whether or not this was just a, tools are different
because tools are different, and I want to say very much thanks.
The Mimir engineering team, some of whom we spoke to at length
about a bunch of these topics, but we were asking users
the wrong question. The question that we'd asked users when
we started this migration is, look, let's take your dashboards, your alerts to everything else that
you were using in your previous tool, and let's put them in a new tool and can
you compare them and see if they look the same? Obviously they don't.
They are in fact different tools, but the core question you want to ask
if you're doing these migrations is not, do these tools look exactly
the same, but instead, can you debug your
production applications? Can you reason through the failure
states of what you're talking about? Can you identify a bad release? Can you
understand when there's a memory leak? Can you understand when
your error rate spikes? Those are the questions that actually
matter in order for you to be able to reason through your diagnostic tooling.
Migrating the dashboards, migrating the alerts is interesting, but not the success of whether or
not these migrations actually work. Only once we'd anchored
in this conversation, we'll be able to make
progress and say, look, as long as you can debug your
production systems, you're good. Things are working enough as
they should, and that was it. We're done. As I mentioned, we have
successfully migrated these people, these 3,100 engineers, this multi-billion dollar business that
delivers a bunch of food around the world into Grafana Cloud well enough
that we still deliver a whole bunch of food, but it was a journey. It was a very painful journey in which
we had to learn some of these core lessons the hard way, and I think the obvious question that
you should be asking yourself at the moment is if you are doing the same thing, if you're looking at this journey
or if we were to do the same thing, would we do it again? I mean, it would be weird if I said no. It would be odd if I stood
up here at ObservabilityCon, I was about to say GrafanaCon and said,
no, it was not worth it. Of course, it was worth it. It was absolutely
worth it. It was difficult. There were some challenges along the way, but we are overwhelmingly in a better
position than we were at the start of this project. What I'm trying to do is convey to you
the core challenges that we had along the way so that if you're looking at the
same project from your own perspective, you can make this a lot less
painful than we had ourselves. We were able to deliver
on the project goals. We got all of these
entities in the one place. All of these different brands can now
talk to each other about their production systems, and we're actually
having people learn and develop. These new dashboards and shared alerts
and automations that we're sharing across the company we're compounding value in
a way that was just not possible before we were able to get all
3,100 people. So far, there's about 5,000 total into Grafana
Cloud. We have Open Telemetry everywhere. If anybody has any doubts about the
fidelity of the OpenTelemetry project, we are using it to ship millions
or hundreds of millions of time. Series 20 petabytes of logs,
20 petabytes of traces, another two petabytes of logs. It works
fine. It's just technology. It's good, and obviously we were able to
very meaningfully reduce our cost, which makes the financial
people very happy. We also found a bunch of things that
we just frankly hadn't expected. Grafana Cloud is evolving
just extremely quickly. The last 12 months have
been transformative for
what the company is doing, and I'm really looking forward to
seeing what they do over the next 12. We saw AppOlly, which has become kind of the central
thing that developers will use to understand most of their
production systems drill
down for the things that they don't have dashboards for or for the
metrics that they've kind of produced but forgotten about or things that are
just outside the standard flow cost attribution makes my life so much easier
from a central perspective to be able to say, dear team, you have
spent a lot of money on logs, please pay for it or stop doing it. I
don't mind which, but I'm able to now say, engineering manager, you
need to address this. And Adaptive Telemetry is
really useful for especially intervening where a developer
makes it very well-intentioned, but very expensive decision to suddenly
publish all of their debug logs in a production system or suddenly multiply
their time series by a thousand or something equal. That makes it very difficult to
control costs on the other providers. Grafana themselves have been
really, really very collaborative. We do a lot of work on
product development. Obviously I'm standing
here in front of you, which is an expression
of that collaboration and
their support team is just excellent, especially given the amount
of stress and complexity in this project. So would I do it again?
Absolutely, yes. However, there are two things that drove the
fundamental complexity of this migration. The first is the deep embedding of
SDKs of the previous observability provider in our production systems. This is absolutely what required those
initial translation work streams, what introduced the risk to the project, and I can't stress enough if you're
looking at the move to OpenTelemetry, start looking at it now.
Start looking at it directly. The technology's fine. It works with
all your observability providers. We deployed it with Datadog and New
Relic and Prometheus and everything else. It's good. You can
start using it directly, and regardless of if you're thinking
about doing this migration or not, it will save you enormous
pain in the future. The second thing is an absolute nod to
my software engineering forebearers. If you're looking at this project and
you're a software engineer of some years, the first thing that should have stood
out is we had a large requirements period, and then we had a fixed
deadline after 12 or 18 months, and then we had these work streams
and a Gantt chart and everything else, and if this looks exactly like a waterfall
project because it's exactly like a waterfall project, our initial assumptions
about the migration were not correct. Developers didn't actually need most of
their dashboards. A lot of the data that they fundamentally required, either they didn't or needed to
be transformed in a different way. If we'd done this migration with just
a small section of the business end to end, we would've been able to learn a
whole bunch of these lessons a whole bunch cheaply than we needed to migrate
in the whole organization at once, and this would've made the
whole experience far less
painful, and that's it. Migration success eventually. I want to thank a few people at Grafana
who help make all of this possible. We have Linda, we have Stefan, we have Dee and the team here
have been just transformative, just amazing in their ability to help us
overcome some of these core challenges. If you have any questions for me, I
encourage you to come find me afterwards. Unfortunately, I don't
have time to do it now, but I will hand across to our lovely mc
and leave you all to engage in the next talk. Hopefully this was useful for
some of you. Thank you very much.

