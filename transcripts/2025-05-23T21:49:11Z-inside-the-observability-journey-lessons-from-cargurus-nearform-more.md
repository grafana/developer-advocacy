# Inside the Observability Journey: Lessons from CarGurus, Nearform &amp; More

Published on 2025-05-23T21:49:11Z

## Description

Join us for a dynamic panel from Observability Sessions Boston where leaders from CarGurus, Nearform, and Grafana Labs share ...

URL: https://www.youtube.com/watch?v=mwKQmGIruhQ

## Summary

In this panel discussion, moderated by Ricardo Lupo, Solution Engineering Director, experts David Frankel from CarGurus and Joe Szodfridt from Nearform shared insights on the importance of observability in software development and operations. They discussed various aspects of observability, including its significance in enhancing business reliability, improving user experiences, and the challenges of managing complexities such as data cardinality and integration of third-party APIs. Key points included the need for effective stakeholder communication, establishing a standard observability framework, and the potential role of AI in predictive analytics and self-healing systems. The conversation emphasized a proactive approach to observability, focusing on actionable insights derived from observability data to drive business improvements and operational efficiency.

# YouTube Transcript Cleanup

We thought it'd be good to wrap up the afternoon discussions. We've talked about our observability strategy, our platform, and Brian shared his extensive career journey, outlining the six stages of observability that he has personally experienced. It was great to hear that. 

Listening to Laban was enlightening; thank you, Laban, for sharing your insights and perspectives. Having Matt discuss business values and facilitate our panel conversation was a nice way to end the day. Hearing from different perspectives and points of view is always valuable.

**Introduction of the Speakers**

You know me, I’m Ricardo Lupo, Solution Engineering Director. What I didn't mention earlier is that I spent the first half of my career on the customer side, working for large financial services organizations in New York—Merrill Lynch, CreditSuisse. The latter half has been with software companies. I’ve witnessed this journey evolve from data centers to the cloud and now to modern tooling.

Let’s get to know our panelists. 

**David Frankel's Introduction**

Dave, could you introduce yourself, your role, and share something we might not know about you? 

Sure! Hello everyone, I’m David Frankel, a principal software engineer at CarGurus. I’ve been with the company for a few years and have held various roles, including data engineering and traditional backend development. Currently, I'm part of the SRE team where we focus on reliability and observability. 

A random fact about me: I actually started my career in a genetics wet lab, working in biology before transitioning to software engineering. It was an interesting shift!

**Joe Szodfridt's Introduction**

Hi, I’m Joe Szodfridt, a Senior Solutions Principal at Nearform. My career spans over 25 years in IT, which is quite a long time! I began by writing software for industrial control systems, which was pretty cool. Over the years, I’ve built agile practices and helped companies develop software efficiently.

I was also a founding member of Pivotal, where we transformed large monoliths into microservices and moved them to the cloud. Observability has always been a critical part of that process. 

An interesting note about my name: it has nine letters, seven consonants, and two vowels, with a ‘Z’ thrown in there, which makes it quite unique! My name has Swedish origins, and according to my family tree, there are only three people with my name in the Americas, and everyone else is in Europe, all related to me.

**Discussion on Business Goals and Observability**

David, let’s talk about business goals. Why is observability so important to your business and users? 

Observability is critical for measuring MTTI (Mean Time To Identify) and MTTR (Mean Time To Recovery), which have clear benefits for the business. The less downtime our customers experience, the more reliable our systems are, leading to increased customer satisfaction. 

Moreover, from a development perspective, observability improves overall productivity, allowing engineers to focus on development rather than troubleshooting. At CarGurus, we’ve been using observability to support our transition from monorepo to multirepo, aiming for more microservices. We’re tracking deployment times and build times closely, which has driven significant value for the company.

**Challenges in Observability Adoption**

What challenges have you faced in this journey?

We’ve faced several challenges, particularly with adoption. Even with great tools and services, getting people to use them can be difficult. We’ve been encouraging training and learning about these tools. 

Configuration management has also posed challenges as we scale, especially with managing OTel SDK configurations across microservices. It’s a common hurdle for many companies as they grow.

**Joe's Perspective on Observability Importance**

Joe, from your perspective, why is observability important for your customers?

At a basic level, observability drives the end result of system reliability and performance. However, I also see it as essential for creating a common model of understanding within a business. Different stakeholders often have varying perspectives on the system, making it crucial to establish a shared view for informed decision-making.

**Organizational Structure Around Observability**

David, how is your organization structured around observability from the user's point of view?

Currently, our structure is centralized. We have an SRE team and an observability team that makes most architectural decisions, manages infrastructure, and acts consultatively for other engineers needing help with instrumentation and data analysis. 

We aim to shift some ownership to individual teams to scale better, encouraging them to take action and solve issues independently while maintaining standards and best practices.

**Looking Ahead in Observability**

What are the next developments in your vision for observability?

We want to enhance our frontend observability, which we’ve somewhat neglected in favor of backend observability. Tool consolidation is also a goal; while we’ve made some progress, we still have too many tools in play. We aim to create a more unified observability experience.

**Joe's Vision for the Future**

From your perspective, Joe, what do you see as the future direction for observability, especially concerning AI?

AI integration is crucial. While observability has primarily focused on infrastructure and backend operations, AI can help analyze customer interactions and system performance more proactively. This shift towards predictive observability will enable businesses to enhance their products and improve customer experiences.

**Conclusion and Audience Interaction**

Before we wrap up, I want to thank our panelists for their insights. Does anyone have questions for the panel? 

---

**Audience Questions**

1. **Cardinality Challenges**: David, could you elaborate on your struggles with cardinality?  
   Yes, we use Prometheus for time series data, which struggles with cardinality. For instance, we’ve had cases where a single pod had close to a million time series due to unique identifiers in service requests, making it difficult to manage and communicate the issue to developers.

2. **Governance**: How do you view the governance of proactive monitoring tools?  
   Governance involves ensuring the right access to data and determining what to measure and track. It's crucial to test your observability strategy and ensure it aligns with user needs and outcomes.

3. **Actionable Insights from Observability**: What’s the best way to turn observability data into actionable items?  
   Start by defining clear objectives. For instance, determine if the goal is to save money or improve performance. Once you have a focus, you can measure specific metrics that will inform actionable insights.

4. **Self-Healing Capabilities**: Are there plans or developments towards self-healing systems?  
   While self-healing is an area of interest, you can start with automating repetitive tasks and creating runbooks to handle common issues proactively.

5. **Enhancing Observability with Third-Party APIs**: How do you enhance observability for third-party systems?  
   We try to create boundaries around external APIs, instrumenting the code that interacts with them. This allows us to monitor metrics and set alerts for any failures.

---

Thank you all for your participation! Let's continue the conversation and explore these ideas further.

## Raw YouTube Transcript

We thought it'd be good. We've been
talking at you for most of the afternoon. We talked about observability
strategy, we talked about our platform. Brian bared his heart and soul for
us in terms of his entire career. He basically laid out the six stages of
observability and that he's done all of them personally. So it was great to
hear that. And then listening to Laban, thank you Laban for sharing your
experiences and your perspective and then having Matt go through business
values, going through this, doing a panel and sort of talking through
and having a conversation I think is a nice way to end the day. And you hear from different perspectives
and points of views. So you know me, Ricardo Lupo, Solution Engineering
Director. What I didn't tell you before, and I should have told you, I spent most of my entire career doing
this first half of my career on the customer side working for large
financial services organizations. I'm from New York, you could tell from
the accent, Merrill Lynch, CreditSuisse, and then the other half
working for software companies. So I've sort of seen this journey
progress from the data center to cloud to modern tooling, but getting
some different perspectives. So getting both of you up here and
talking through your experience. So Dave, first maybe introduction,
name, role, company, what you do and one thing we don't know
about you that we could learn today. Yeah, sure. So hello everyone.
My name is David Frankel. I'm a principal software
engineer at CarGurus. Been at the company for a few years
now. Done many roles over the years, so did data engineering for a while, did
more traditional backend development, so been all over, but right now on the SRE team and we
work on reliability and observability. Awesome. And what's once one favorite
fact about yourself? Yeah, well not necessarily favorite fact, but kind of a random fact maybe
is a better way to put it. I actually used to work in a genetics
wet lab, so I started off in biology, not in side as you'd probably expect. So it was kind a interesting experience
going from that into the software engineering space. Awesome, thanks for sharing. Hi everybody, I'm Joe Szodfridt, I'm a
Senior Solutions Principal at Nearform. My career spans 25 plus years, way too long that I care
to admit sometimes in IT. I first started writing software for
industrial control systems making machines run, which still that was
a really long time ago, but today that's still one of the coolest
things in my career is making these mechanical things not slam into
each other. Did a long stint, building agile practices,
helping companies develop
software in very efficient, productive waves, mainly
on the software side. And then I was one of the founding
members at everyone knows a company called Pivotal. I was part of Pivotal, the application transformation
practice where we took giant monoliths, made them all microservices and
clouds and moved them to the cloud. So I've been around for a long
time seeing lots of things, many industry verticals, mainly
been on the software side, but as you're running software, the observability is always there
as well because it's all related. An interesting thing about me, I don't
know if my name's still up there, but my name has nine letters,
seven consonants and two vowels. It's pretty messed up
and there's a Z in there, which no one knows what to do with.
So see, everybody's laughing. Okay, so it is there. So the name
is, it has Swedish origins. My grandfather did our family tree back
actually like 400 years and when the Swedes came to Hungary they threw
in a bunch of extra letters. So it's pronounced phonetically
as it would be in Swedish. The interesting thing about
that is there's in North, South, and Central America, there's three people with that name and
anyone else who has that name in the world is in Europe and
they're all related to me. So I could never be a spy with that name. Very interesting. Also, probably a great final question on
Wheel of Fortune nobody would ever get. Yeah. Alright, awesome. So let's
get right into it. So David, I'll start with you talk
about business goals. We talk about business being really the
most important part of the observability journey, really getting aligned there. Why is observability so important to your
business and why is it so important to your users? Yeah, sure. So I mean we can talk
about more the MTTX type of metrics, so I won't go too deep into that, but
obviously MTTI is something we measure. MTTR very important. So that I think has kind of
clear benefits to the business. The less downtime our customers
experience and the product, the more reliable our systems are,
hopefully the more customers we get, things like that. I think there's some on more of the
development side for our internal users, there's a story of
improving productivity overall, letting people work more on the things
they want to do rather than focusing on troubleshooting for hours a day,
work on doing front development, backend development, what have you. So I think that's very
important too to the business. And I guess more specific
use case at CarGurus, which I think is a little bit
different and maybe not, I dunno, but we've been using observability
to try to help our move from monorepo to multirepo
so to more microservices and I think it hasn't really been
talked about today at all. So I think it's a little different, but it's something we've
been doing a lot of, how can we prove out the
faster deployment times, the faster build times, and just kind of tracking that progress
I guess is the best way I can put it. So that's something we've been
focusing on really the last year, I want to say maybe more and I think
that's driven a lot of value the company. Thanks for sharing. What are
some of the challenges you face? We talked again today about blockers
through adoption and why platforms don't. I'd love to hear what challenges
you face in that journey. Yeah, we definitely faced a
good amount of challenges. I think there's a few, right? So adoption is definitely one that's
something we, we've had difficulties with. You can provide all these
great tools and services, doesn't necessarily mean people
are going to want to use them. Even if you give them a really good pitch, it doesn't necessarily guarantee anything. So we've been trying to encourage more
trainings, people attending trainings, people learning more about these
tools, things of that nature. We've also run into issues with
configuration management I want to say. I mean, think that's a natural challenge
for a lot of companies as you scale, A lot of times companies do break up
into microservices and so how do you manage your OTel SDK configurations, how do you manage your various whatever configurations? I mean it's
not just unique to their ability. So that's something we've definitely
had a challenge with as we've scaled and grown and we've felt it in different ways, but I think it's an ongoing challenge. Thanks for sharing. Joe, I'll
ask you the same question, but I'll ask you from the perspective
of your business, what observability, why is observability
important to your customers? Well, at a real simple level, well maybe
not simple, Matt went into real detail, but that is the end result. So I don't
think that we need to rehash that, but that's the end result. So
that's what you're driving towards. But I think there's
another level here too, and from my experience in these
multiple scenarios doing software development and big system design, I like this word system and I like
to view everything as a system. So no matter what you're doing, whether it's a big enterprise
or a small application or a microservices architecture,
something like that, there's lots of things that are happening
and there's lots of people involved. There's manual processes,
there's automated processes, there's processes you probably
don't even know about. And there's a lot of people that need
to be involved to make this decision of what's going on. And I find this across the board and
almost every customer that we speak to is they're really lacking this kind of
common model of what is the quote unquote system. Everyone has a different
perspective of what's going on. We're sitting up here and we
see a lot of smiling faces. You're sitting back there, you see the backs of people's
heads and we all see the sidewall. So we're all looking at a system. If we consider this observability
event here as a system, we all have different perspectives, but if we all wanted to talk about
this and make informed decisions, we would need one solid model or
vision of what is this going on. I think that's critical to any business
because it gives you the ability to everybody come together and make
informed decisions on what you should be doing and what could be done. I love that analogy of looking at
it from a different point of view, like everyone in the rooms
is part of the system, but they see different things and
how do you bring that together. So speaking of that, how have you helped the customer on
that journey from your point of view in terms of the service that you provide? How have you helped the customer really
along that journey to help them be successful? Well, so at our company
we've developed a of, we have a lot of older
people that I worked with, the previous companies that we pulled
together from these different areas that we had. And we have processes where we
create this model of the system. So we've adapted value streaming,
we've modified event storming, we've created our own things like BORISes, BORIS modeling and thin slices where
we can very rapidly create a model of a system. And then once we create that model of
the system that we have a way to talk about it and then we pull in other people
to bring in all those perspectives. So what does a financial person want to
see? What does developer want to see? Everyone has data every everybody wants
to do. Where are all those use cases? We build a common model and then
kind of go around, what do you want? What do you want? How does that
relate to the rest of the model? So it's kind of unique to
our practice, but again, it's at that kind of high level of
that common canvas that people can talk about. Great, thank you for sharing that. So now we're talking a
little bit about models. We talked a little bit
about challenges. David, love to get your perspective here. How are you organized around observability
or the organization of it from the user's point of view? Yeah, sure. Real quick,
before we go to that, I want to go back to the previous
question about the troubles we've ran to. I was wondering some other stuff. So we also have had difficulties
with cardinality, right? I mean that's something you
guys touched on earlier. It's something we've constantly struggled
with and we haven't found a perfect solution to be honest. It's a problem and it definitely can
become more challenging as you try to shift ownership over more towards
teams. The whole shift left mentality, and that kind of ties into
just how we're structured. So to get back to your question
now we are pretty centralized. So that was a common theme talked about
today and we've always been that way at least since I've been at the
company. We have an SRE team, we have observability team that's
like a subset of that team and we really make the majority of
the architectural decisions
around observability, manage the infrastructure and are
kind of consultative in terms of other engineers coming to us, asking
for instrumentation help, helping them to really
dig deep into the data, some data and figure out what's
wrong with their services, how they can help themselves in the
future. That's kind of our current structure. And as I
touched on a minute ago, we're trying to move a bit more
of the ownership to the team. So rather than us having to go in
and really do a lot of this work, it just doesn't scale
super well in our case. At least that's what we're finding. And so how can we offload
some of this stuff, the teams to really encourage
them to take action themselves and feel empowered to solve
issues their own way, but at the same time maintaining standards
and maintaining best practices and those things. Curious since a lot of what he mentioned
was around getting to centralize and just getting a little bit
more federated to get scale, how have you seen an interaction with a
customer where they've evolved from your initial engagement
through their own journey? So going to go back to
some of the challenges that
people have and the way the reason the central model seems to work
is what we kind of see is that that centralized or a CEO perspective
seems to work the best. The challenges that people have
is there's tons of data silos. Everyone's got their own set of data.
The financial people have their data, the operations people have their data, the DevOps people have their data and
everybody wants to pull that together. And the easiest way or the one that we
find the most effective is to have this centralized COE. And what
we like to do with that, or what we've seen customers do with
that is similar to what you're talking about is you form a centralized team,
you bring in a multifaceted team, so you really need to bring in maybe
partial members or full-time members from finance, DevOps, everybody.
You need a multifaceted team. And then as that team starts
to get more proficient, you start doing mitosis, breaking
off little people into smaller cells. You can recreate this more
specifically in their area, say it's finance or DevOps or whatever. And that's helped customers along their
journey and kind of what we've seen to be the most common pattern you see doing
the same thing seems to work very well. Yeah, and to touch on that,
we exactly like you're saying, a lot of what we've been doing
recently is trying to bring people in temporarily, train them, really help them and hope that they bring
that back as tools to their teams when they go back to their
regular positions. And again, really encouraging the training aspect
of a lot of this to drive adoption of these tools as well as
just general education. And what you find is a lot of these
things that we're talking about, it's not unique to observability.
This is just the way you do software, IT projects, build
buildings, whatever it is. It is just a common pattern
that repeats throughout. Love that. Don't over
complicate a ham sandwich, just keep very simple and make it
repeatable. So there's a lot of talk, we talk about the organizational model, there's a lot on the LinkedIn sphere
about cloud being so expensive, go to on-prem, et cetera, et cetera. Very curious because a lot of this
has been driven around cloud native, microservices, this whole
transformation. David, first off for you, how do you view the journey to cloud
as it relates to observability? Yeah, it's actually an interesting story for
us because I think a lot of our efforts to move forward in the observability
space are tied to our cloud migration. So a couple of years ago, around the
time I started a little bit before, we'd really put a ton of effort
into instrumenting metrics, traces, stuff of that nature into all of
our services because we want to make sure that when we did a migration
over to the cloud from on-prem, that it would go as smoothly as possible
and we understand when things break because they always break. So that's a lot of how we started and how
we justified getting observability off the ground of the company.
That's one of the positive sides. I think the flip side on that is there
can be a lot of additional complexity when you move into the cloud. I think
most people realize that, right? It's not going to solve all your problems. One of the complexities obviously is
you have more distributed workloads when you have back in the day you have
one service running on the vm, right? It's a little bit easier in some ways to
look at logs, look at traces from that. When you have 20 microservices that are
all communicating with each other via queues, some via directly
via rest HTTP APIs, that's complicated. And you need different tools sometimes
to actually understand that fully. And I think that's sometimes a little
bit overlooked as well as how do you actually observe some of the
cloud services themselves? So you have options in AWS, you have
options in Google, but it can be tricky. What do you think was your
biggest challenge through
that whole journey that you had to overcome and how
did you overcome it? Yeah, that's a good question. I think one of the challenges I was
saying is trying to figure out how to tie all these different pieces of data
together and really select tools and trying to understand what
tool is best for each job. That took a while for us. How does
CloudWatch fit into these things? That can be super useful for a lot of
the native AWS services and in our case we're on AWS, but that may also not be the best choice
for having direct instrumentation and services that are not
necessarily an AWS service. So I think it just took a lot of research, a lot of time on our part and just talking
to our internal customers and seeing users, what they want and
what they're interested in. Thank you. Ask you from the same point
of view, from the customer perspective, I'd love to hear sort of
how the cloud fits into? So how the cloud fits in. It's an
interesting question because there's, people are different states in
their journeys to the cloud. People are moving to the cloud and
other people are born in the cloud. So I think probably the people who are
born in the cloud probably have it a little bit easier. Not as
much of a paradigm shift. You're just kind of immersed in it.
People are migrating to the cloud, are moving to the cloud. There's
a big mind shift difference. You used to control all your resources, now you're sharing the
controlled infrastructure
with providers and you on the other half your model, your pricing model used to be
you're just paying for hardware, now you're paying based on consumption. So you have to have that mind shift where
you have to know what you're looking for and make sure you're accurately
measuring it to. You can't just pick up something that you had running in a
data center and move it to the cloud and expect it to be efficient
or cost effective. And on the flip side is if you're in
the cloud and you're building a lot of microservices, if you're not paying attention to how
you're distributing those microservices, how they're running, you're also running up your bill
or you're not being efficient. So the challenge really is to take
a look at what you have and again, make sure that you're collecting the
right kind of data and try to analyze it. And it's not just
collecting a lot of data. Sometimes the way we help customers is
you can't measure everything because it's very difficult to do. So it goes back to business initiatives
or that big holistic view of your system. What's the most important
piece of your system, what is the guts, what makes the stuff happen? And make sure that that's instrumented
and you're paying attention to how that's operating and working. So you
could modify it and be aware. Thank you. So this leads us into the
next category, which is platform. David, I'll start with you again.
You mentioned your AWS user. So what were the most important criteria
and the choice of tools, platforms, and partners that you use? Sure. So I think there's
multiple answers to that. One of them, which I think is maybe overlooked
sometimes is business fit and business alignment. I can think of this more
in terms of not necessarily AWS, but in terms of other SaaS providers
for telemetry data and observability, we've done a lot of POCs
for different companies, we've talked a lot from
vendors and providers, and I think that comes up time
and time again. It's like, does what they're offering align with
what we want as a business, right? Because sometimes you get these
offerings that cover everything, but it may not necessarily fit with
what you're trying to actually do. So I think that's very
important. Obviously things
like costs, very important. Being competitive in the space with a
reasonable cost is definitely something that's critical for us, maybe less
critical for certain companies, but that's an important factor
for us. Think what else? There's relationships
with companies. I mean, it may be sounds I know not as exciting, but I think that's an
important factor as well, is establishing a good
relationship with a company, making sure you're on the same
page is very important for us. That's not always a given. Couldn't agree more with you on that
last part in relationship with the company's vitally important, you need to be able to trust
people and work with them. Absolutely. Joe, what about your point of view? My point of view is, let's see. So I think you have to make sure that
the tools that you use and the platforms that you're selecting do
what you want them to do. So take the analogy when you go to
hardware store, when you buy a drill, you don't want to half inch
drill, you want a half inch hole. What are you trying to do as you're
saying, well, how does that fit? What does that tool fit to the business
purpose that you're trying to do? Then once you get the right tool, then you can go into is it cost
effective and does it have a good support network is really good. Another thing I think that want to
bring up too is how fast is it evolving? So the tool is good today, that's a
good drill, it drills really good, but tomorrow there's going to be different
types of holes you need to make. So is that company building the right drills
that are going to go through whatever you need to drill a hole? And
I'm kind of making this up, but the analogy's probably
a little too long, but you need a company that's actually
moving forward and releasing software and developing features at a reasonable
pace that you can adopt and use. And then also does it have an ecosystem
where it integrates with a lot of things. So as we are a consulting company, we come into companies who've been
through their homegrown processes, six or seven other vendors
are in there making things. It's generally a mishmash of stuff. So if you want a tool and we
want to deliver Valley fast, what we're looking for is something
that we can pull in a lot of other integrations with very rapidly and
not have to learn a lot of things. So training and knowledge is very fast
too. Sometimes we recommend tools, but customers say, we want you to use
this one. If they make me use one, I would prefer to have one that
has a bunch of building blocks, things I could use out of the box and
get me ramped up very quickly as opposed to having to figure
everything out on my own. Integrations is a great call out. That's something we definitely
look forward to and I
think really minimizing the impact on other parts of the business. We don't want to have
to ask every developer, every engineer to put in a ton of effort
for something that we want to move to or migrate to or adopt. So yeah, integration's definitely key. Minimizing the amount of work for the
rest of the company and we do lean towards it for the most part. I think
more open source tooling as well. So OpenTelemetry very important
for us. We use it pretty heavily. Some FluentD FluentBit. Those types of tools as well
are I think pretty important. Thank you. So we talked a lot about your
experiences and what you've done to date, which I hope everyone finds super
helpful to just share your experience, share the tooling, how you're doing it. I want to focus a little
bit around what's next. So you got into a level of maturity.
David, again, I'll start with you. What are the next developments
in your vision of observability? What's around the corner for you that
you want to start thinking about and why? Yeah, so there's
definitely still gaps here. Things we want to improve on in our
observability story. One of them is, I'd say frontend observability
is something we've kind
of neglected honestly a little bit. What most of our focus has
been traditionally on the backend side of observability. So I think
trying to put in a good, some solid tooling there, a good story around the front end that
is equal to and on par with the back end that we have today, I think is pretty important and
definitely a direction we want to go in. There's also the tool consolidation. I mean we talked about that and you
guys talked about that in some of the earlier sessions, is that we've consolidated
it slightly over the years, but I think there's still too many tools. I think we need to get to a place where
there's maybe not a single pane of glass, but at least a few
pane of glass, a few windows. So that's something that we're still
striving towards and it's going to be, I think a long-term goal, but it's something we do want to keep
moving towards as much as possible. Joe, I'll ask you the same
question from your point of view. You deal with a lot of customers where
David deals with one concerned day to day. How about you? What do you see from your customers
in terms of what's around the corner? What's around the corner? I we not even mentioned AI
in this conversation we've
had in the last how many minutes, right? Only the second time we said it
all day. Right. That's pretty. Good. I think. I want to use your term. I like that it says I
want to rub some AI on it. Normally what we say our customers
want to buy AIs, and we say, well, how many AIs do you want?
Right? That's kind of the joke. The AI sku, right? The AI sku. Exactly. But there's a lot that it can't do
and there's a lot that it can do, and I think there's a huge
potential here because as you said, observability tends to lean more
towards infrastructure, backend stuff, not so much as to how the product
is, how the customer's using it. And I think AI could help a lot in
that way by being able to just look for patterns, look for patterns,
how things are used, how the backend is running
with the front end, and try to use that information to be,
as Matt was saying, way more proactive. So the thing is, most of the world in this space
here tends to be very reactive. Something happens, I don't
want it to happen again. But really going a little further, being proactive as to how
can I make my product better? How can I make this faster, quicker?
What features are customers using? That kind of stuff is all
possible. I think that's where, if I was to say where I want it to go, I'd want it to be pushed more down towards
customer interaction versus how the system's being used on
them on the backside. Yeah. Yeah, AI, it's a great
point. I'm shocked a few times. It's come up so far, honestly, I thought
it'd be talked about more, but yeah, I think in our case it'd
be a little bit different, but using some of the new AI tools to
really get to root cause faster for instance, is definitely
something we want to investigate. So less from the external
customer side maybe, but more from let's improve productivity
even more by just narrowing down on the abnormalities if you want to say in an
incident and really figuring out what's wrong and what's anomalous there. Or higher levels of automation
too. So AI is really good at, we like to say to remove human
drudgery, if you're doing it once, you should fix it. You could
write scripts and templates, but you could also build smart
things that know how to do certain configurations and if everything's as
code, it's viable to say, I want this, go do it for me, as opposed to having an engineer run
a bunch of scripts or do whatever. So there's a lot of
potential there as well. And there's been some asks definitely on
the development side to kind of enable tools that help them use AI and LLMs
to kind of pull from some of the different observability tools we use, which is kind of an interesting idea and
something we're trying to think of how we can work with them to incorporate that
into their developmental workflow and debugging practices. Thank you. How do you anticipate observability will
impact businesses as it continues to mature? How it impact businesses? I think
it's just going to help 'em, how's it going to impact?
It's going to make 'em better. It's going to help them make more money,
reduce costs, and be more efficient. Now as you move towards
being more proactive, which seems to be the trend that
is going to be a huge windfall for businesses. Right now, I think a lot of businesses are going
based on how the customers are using their applications, but maybe there's a more
impact there from being more predictive. So it's definitely something
you got to get on board with it. It's the ability not to react, but to predict and be proactive
into kinds of features, use cases, and all that stuff, I think supports
with just as much as data you can have. And again, making sure that
it's all consolidated data. The biggest thing I see again is that
there's all these silos of information and people don't pull that together. So as more of these progress applications
progress and you start pulling in all the different aspects of the finance,
DevOps, product, and everything together, that's just going to make
things move faster and quicker. Companies are going to run more
efficiently and make more money. Awesome. David, from your perspective, how do you see that impacting
businesses as it continues to mature for your business? Yeah, yeah, yeah. Actually it's something you just touch
on I think is going to be important to us too, is the FinOps side, right? It's something in the cost attribution
is something we're starting to look into more, not necessarily just on my
team, but other teams as well, right across the company. I think that's going to be a very
important part of observability. I mean, it's already kind of grown over the last
few years and I think that's going to continue to grow. Yeah,
similar like you're saying too, I think pulling these different
pieces of data together. I know that's been talked
about today a lot as well, and I think that's going to be more
of the future and really make a good business case for adopting more
modern observability tools as well. So I think that's the main selling
points services I can think of. Awesome. Alright, I got one more
question for each of the panelists, then we'll hand it over to the room.
Molly, what's our time check? Okay, wrap up. Okay, great. I think we'll do a little bit of
q and a with the room as well. Would you like that? Would you like to
ask some questions for the panel? Yes, absolutely. All right. There
you go. Somebody's excited. But that's a Grafana plant. I don think that count. I like that.
I like that. Matt, you can't ask, you have all the answers so
you can't answer questions. So I'm going to do one more for
each of you. David, I'll start you. If you have one recommendation for people
in the room embarking on observability strategy overhaul, what would it be? Yeah, I think talking to stakeholders
is critical building requirements as well, right? That's something we've
learned I think over the years, the hard way and trying to get that done
upfront saves you a lot of time down the road is just fully
understanding. What do you want? What do your stakeholders want, how can you find a way to get
there and meet in the middle? I think that's very important. I also think standardization as
early as possible is a big win. It's something that was hard for us. I
think it's hard for a lot of companies, especially if you've been around for a
long time and things organically grow every which way. But if you're
starting off from scratch, definitely as much as possible try to
come up with a same set of standards that people can use. Obviously they'll
change and shift over time, but at least you can start with hopefully
a solid base and grow from there. One recommendation, so this is a
multifaceted one recommendation, but it's kind of like treated. I come
from the software side, more of the world. That's where most of my career has been. So there's the way people run
projects there or that whole agile mentality, lean mentality of involving
the user like you were talking about, and really treating it not
like a technology driven thing, but as an outcome driven project
or engagement and having a prioritized list of things
you want to do first, identifying the business outcome
that you want, a real outcome, not a technology outcome. How
are you going to measure that? Who are the core users of the
system? What do they want? And run it like that to me is that's
the one recommendation I have. I see a lot of technology
being implemented for
technology's sake as opposed to running this kind of holistic view. If you're writing software and you're
good at writing software, you would say, well, who's using my software
and why would they buy it? You got to take the same
mentality on observability. Who's going to use my software and
who would pay money to give them the information that I'm doing? So I think
that's the thing I would suggest. Terrific. Alright. First off, big
round of applause to our panelists. You want to open it up? What's. That? If anyone has a question, I'll
run a mic to you. Anyone other than. Yeah. Dave, I was wondering if you
could tell us a little more about, you mentioned some
struggles with cardinality. If you could just say some
more words about that. Yeah, just in general. Sure. So we use Prometheus internally for
time series database and as I think most people have used Prometheus, no,
it struggles a lot with cardinality. It's kind of a known
issue with Prometheus. So we've had many, many
problems over the years. I can think of several examples, and
this is probably the most common one, where we will have a service
and they want some time series data and they want a dimension that's
on the URI. They want to see, oh, the unique paths for whoever's hitting
my man points. It's a reasonable request. The problem is, is that a lot of times you have unique
identifiers or almost unique identifiers basically buried in there
and that quickly explodes. So we've had cases where I'm
pretty sure I've seen one service, a single pod have close
to a million time series, which is insane.
So trying to communicate that to developers and engineers can be a little
bit challenging because a lot of times they don't understand the problem
and they also don't understand, oh, it's a reasonable ask,
why can't I do that? And it's hard to say technically it puts
a lot strain in the system and memory database, all that stuff. But that's something we've run into
a lot and that kind of comes up over and over again and we've
dealt with it in different waves. We have limits on the number
of samples and time series that will be pulled from services
and if they go over that, we trigger an alert and basically stop
pulling metrics from their service that has its own problems. But there
are different ways to deal with it. It's just none of them are ideal. Hi, So we were discussing
about the observability throughout the session, but what your opinion about the governance
of all these proactive monitoring tools? Because we are coming from
operations team and at one point we will be heavily depending on
these alerts coming from all these monitoring tools and one
day we find like, okay, there are alerts missing or there is
some proper performance issues with these monitoring tools. So it's high time. We need to think about the governance
around all these monitoring tools. So just want to know
the opinion around it. To say one is an approach of how
you implement governance. And again, I'm going to go back to my
software analogy, the one
I'm most comfortable with. When you build software,
you do a lot of testing, it's a lot of test driven development
or validating what's going on as you're implementing your
governance. Test it, right? There should be ways where you could
say that things aren't happening or they should be happening and your system is
capturing things that aren't missing. So that's the main points like
conceptually is do that right, but then figure out also out figure out
is what is it actually that you need to track or that you need to govern and make
sure how you're going to enforce that and then be able to test
that before it gets there. You want to again move towards being
proactive as opposed to being reactive. Yeah. Yeah, I mean just to build off that, we have tons and tons and
tons of dashboards and
different tools to monitor our observability stack. I mean that's something we constantly
have to look at in terms of, I don't know if you're touching on
this, but in terms of ownership, we're a centralized model, so it's really
owned by me and a few other teammates. So if something does break or we see, we get alerts on FluentD is having issues, it's on us to go in and
fix that and maintain that. And almost every time we'll catch
it before anyone else notices, which is the way it should be.
And we do have alerts and SLOs, SLIs that are more on the proactive
side to try to catch these things before anyone would run to problems. But
yeah, it's a challenge we have, but it's worked well enough for us over
the years. I'll say it's not ideal, but it works. I have a perspective on this. So you mentioned what alerts
do I react to? Why, how, governance has a few different angles. One is are the right people
accessing the right data? So there's a governance there. Then there's also like what
are you actually measuring
and tracking and reacting to? And that's where David, you were talking about the shift to
discrete from discrete individual alerts of components to things
like SLIs and SLOs, right? Things that actually measure
the experience that I can
actually get in front of and react before the customer cares
about. That's part of the evolution. And we talked a little bit earlier
about the observability strategy. That's where you need your stakeholders. That's where you need to
actually understand how
these systems are being used, how they're being measured and creating
those contracts in your observability system. It's a journey. It's not going to just be about alert
deduplication or event management. The one thing I always say is you have
to create better alerts and that starts by actually understanding the user
experience, understanding the contract. And that's something you can have very
different use cases for the same system. So to build off your
point, we've had this, it's been somewhat of an issue for us is
that in some cases developers are using their logs as just a debugging
tool. They just emit some stuff, they want to see it show up somewhere
and then like, oh, that's interesting, maybe something broke. I need to see
a line here that say why it broke. And then on the other side of that, we have teams that are using our log
pipelines as more of analytics pipelines. And so their use case is very different
and their tolerance for data loss is also very different. So to your point, it's very important to understand that
because what may not matter to one person may very much matter to another person, even though they're again technically
just logs or the same system. Hi, I'm Dave Lovelock. I work with a lot of performance
of large on-prem applications in hospitals around the world. And so what do you think is the best way to
take all of this information that we're gathering in an observability
platform and turn it into actionable items? Things that will actually
tell somebody take this action when the on-prem environment
often doesn't have a lot of skills in data analysis or such things. First you got to start by
asking what do you want to do? It goes back to the objective,
I'm calculating all this data. Do you want to save money? Do
you want to retire old hardware? Do you want to increase the
performance of something? So you've got to start with what is
the objective that you want first in your on-prem environment and then figure
out how you can measure it. Make sure. Think long term strategy, two o'clock
on Tuesday afternoon a moment, the form suddenly goes from
one second to five seconds. Okay, yeah, I can touch on that. I think at least in my opinion, the most useful of the three
pillars in that case is traces. I mean that's something we go to pretty
much immediately for any incident is we'll jump in and we'll
look at, in our case, we currently use Honeycomb for tracing
and we'll jump in and say, okay, and we have dashboards that visualize a
lot of this, but we'll see what broke, where it broke in the system. You can see if there's a call chain
that's across five or six different services, you can see all
of that visualized there. You can see a lot of
times where the error was. And also a lot of times the stack trace
depending on how it's instrumented, but we're fortunate enough that in our
case we're pretty Java heavy and Java, you get the OpenTelemetry tracing agent, which is auto instrumented for
a lot of different frameworks. So it's pretty easy to get
up and running there. Again, assuming you have some way
to do the analysis. And
that's kind of the key point. We have Honeycomb, which makes
it easy. We did also use Jaeger, which is open source, right? So if you want to deploy
that and manage it yourself, we did that for a while and it might be
good enough for your use case to find problems and got to fix
things as fast as possible. Actions where the people
on site look risky. I dunno. Hire more skilled people. [Cross talk]. Do you know if it's, have
you resolved these issues? Has it been similar things multiple times
over or is there always something new and random when you have these failures?
Code changes? Well, code changes. I mean, is somebody testing
it before it got in there? I mean that just go back to the software
development process as well, right? It's like you should do as much not to
put any failures into the system before you get to the system. And the runbook is a good call out if
it's a common issue, we do do that. We have runbooks all over the place, so if it's something that comes
up frequently and not full, just create a runbook for it and make it
pretty clear that this is what you do. If it solar fires, you'll literally put a link to the
documentation or even if there's some automation, have it trigger
automatically. So if it's common, you can do something like that. We have time for one more. I see. Oh,
all right. We'll do two more. Go fast. So I'm Satish. So in line with all these
questions that has been asked, so I know this is more of observability,
dashboard alerting and all that stuff. So are we looking at what's next? So can we get into self-healing? Is there any development or, I know it's all together a
different requirement as such, but are we thinking in that direction? So I know if we have to bind
too many tools right now for monitoring, we have plenty of tools and for
fixing them if we have to get into another set of tools.
So it's expensive. I mean, can we look at how we can, I know you already have huge
telemetry of the infrastructure data, so can we get into that? Is
there any plans for that? So what are we thinking
about that question? Yeah, is that a Grafana
roadmap question? I don't know. I can give you an operational piece of it. So we talked a little bit
earlier about the journey, right? And how do you implement a
successful observability strategy? And there was a key
part around the culture, which is automating the
things that are repetitive. And so I think of your question, it's
twofold, right? So self healing is like, okay, what are all the patterns? Tell me what the problem is
and go fix it for me. Great. The other piece of really driving
observability success is taking the low hanging fruit and automating that. And that's something we do today
in Grafana. It's not self-healing, but it's your ability to react to an
alert or an activity and go and say, go do something with this. The example
I always give because this is my brain, it works very simple. You have a Windows server that
Windows temp fills up the 99%. You don't need somebody to log into the
Windows server to go clear out temp. Write a playbook, write an
automation script, write something, allow the alert to go and
trigger that and go remediate it. So every time that alert triggers,
you now have an automated response, build a runbook around it. There's
a bit of secret sauce around it, but the real secret sauce is around
taking the things that are just common, documenting and making those
repeatable and automatable. So you take that toil completely
off of your book of work. That's a real part of making observability
successful is that you're able to show the value chain throughout
the entire thing that happens. And Grafana does give you the
tools to do that. But again, it becomes part of like, is this really
important? Should I invest the time? Because what you don't want to have happen
is you don't want to have Grafana or any other system to go and
say, oh, go auto heal it. And all of a sudden you take down an
entire Kubernetes cluster and then what? Either you calling the vendor and put a
support ticket in, but you're out. Matt, I know you have a view here. Testing, of course, End testing is so
important not just in Prepro but also in production where you learn those
lessons where you mentioned the example like this space filling up that happens
all the time or out memory conditions that arrives because your JVN
is start, maybe it's memory, but catching those proactively and then
coming up with these runbook to know your background and share
totally makes sense. We can then automate remediation of that. Something I've actually done in
other which is have the context maybe solve or maybe not, but you understand when
those issues arise, how do you deal with it?
So testing is critical. Both pre and prod and load
testing is where you see excuse, yes, you stress me enough, you find the
weaknesses and they'll tell you time. One more. Yeah, there's one back here. Thank you. So obviously it's easy air quotes to
implement observability within a system that you're writing yourself, specifically referencing the topic
that's come up several times today of observability as code. However, there are systems that are moderately
or heavily dependent upon third party systems, APIs that you have limited control over
how much insight you can glean from their systems. What are some tips, tricks, strategies you've adopted in those
cases to enhance your observability into those systems to the
best of your own ability? I can quickly talk on it. I mean, I
think that does come up sometimes for us, it's a challenge if you can't control
the third party and what the instrument, that's a problem. My general recommendation is typically
been to try to create a boundary or box around those separate APIs that you're
externally accessing for the third party and trying to make sure that boundary, that code boundary is very
well instrumented in terms
of metrics. So for us, that can be, we have the auto
instrumentation on the tracing side, but that might be more metrics around
the specific function calls that call those external APIs. Just trying to really make sure you
can see as much as possible in that one specific area of your code. That's
the best advice I can think of. At least you so much you can do if you
don't have a lot of insight into what the third party's doing. And we've done similar things, we
try to, if it's a third party API, you could try to probe it a bunch of
ways and write your own kind of little service that is actively monitoring it
in more ways than what you can get from a log or something like that. So
you don't have unlimited control, but you can write software yourself
and you can exercise stuff. So if you have an external system, you can kind of probe it and play with
it and just kind of write your own little agents. That's a bad word too, right?
Agents that we're talking about AI, it's little agents that are out there
trying to collect as much information as possible for you. Yeah, that is something we've done a
few times. I'm honestly proud to say it, but yeah, kind of just probes to
see if something's still alive. If they say they're alive. Yeah, that
is something you can do too. I mean, I think going back to
what I was saying before, I think in some cases we've just created
very sensitive alerts around those areas in the code and just really, if we know their uptime is 99.9%, right, if there's any failures immediately fire
an alert because we know it's going to lead to a cascade of failures
essentially in the system. Thank you.

