# Why Building an Observability Center of Excellence (COE) is Essential for Observability Maturity

Published on 2025-10-22T16:59:36Z

## Description

Observability is everywhere—yet fragmented. In this ObservabilityCON talk, Brandy Smith and Jeff Freeman share Grafana's ...

URL: https://www.youtube.com/watch?v=6rY3Ch-AmRo

## Summary

In this video, Brandy Smith, a leader on the observability architecture team, and Jeff Freeman, VP of Customer Solutions, discuss the challenges of fragmented observability in organizations. They highlight a scenario where a customer's order fails due to unclear metrics and misaligned alerts, leading to lost sales and damage to the brand's reputation. The duo emphasizes the importance of creating a unified Center of Excellence (CoE) to streamline observability efforts, improve decision-making, and foster a culture of continuous improvement. They introduce the Golden Path framework, designed to guide organizations along their observability maturity journey by establishing best practices. Key functions of a CoE include standardization, education, tooling management, and community-building. The discussion also touches on how to measure business insights from observability efforts, underscoring the significance of tracking metrics that impact business outcomes. Brandy and Jeff conclude by announcing upcoming resources, including a Golden Path Hub and a tactical checklist for building a CoE.

## Chapters

00:00:00 Introductions of Brandy Smith and Jeff Freeman  
00:02:30 The impact of fragmented observability on customer experience  
00:05:00 The concept of a unified center of excellence in observability  
00:06:45 Introduction to the Golden Path framework for observability  
00:08:30 Customer case study on assessing observability maturity  
00:10:15 Explanation of what a Center of Excellence (COE) is  
00:12:30 Key functions and benefits of a Center of Excellence  
00:15:00 Importance of community and training in observability  
00:17:00 Discussion on the rollout of best practices for observability  
00:19:15 Introduction to business insights and their relevance in observability  
00:22:00 Upcoming resources and modules for the Golden Path initiative  

# Observability Architecture Discussion 

**Brandy Smith:** Hey everybody, I'm Brandy Smith, one of the leaders on our observability architecture team, and I'm joined by Jeff. 

**Jeff Freeman:** Hi, I'm Jeff Freeman, VP of Customer Solutions, which is a totally made-up name, but it encompasses our professional services team, SE team, tech support team, and observability architecture team. 

---

## Setting the Scene

Let’s set the scene here. Picture this: it’s lunchtime, and a customer is on your app trying to order food, but the order fails. Here’s the kicker: on the backend, one team’s metrics are green, another’s logs are delayed, and the alert that should have fired didn’t. Frustrated, the customer opens your competitor’s app and places an order there instead. To the customer, it just looks broken. 

Now, it might seem like one lost transaction, but in reality, it represents thousands of lost sales and a hit to your brand’s reputation, all because observability was fragmented. This is the reality for a lot of teams today. Observability is everywhere, but it’s fragmented. You have siloed data, unclear ownership, and context that lives in tribal knowledge. We’ve normalized this chaos, but the truth is, if your strategy is fragmented, your response will be too. 

Teams have different definitions of what "good" looks like. They might be asking questions like:

- What are we instrumenting?
- Are our dashboards any good?
- Are we doing too much or not enough?

While one team measures uptime, another logs everything, and another ignores alerts entirely. Alert fatigue is real. We’ve seen this with platform teams, SREs, product owners, and even executives. Everyone’s answer is different, and that’s a problem. The cost of this misalignment includes alert fatigue, bloated telemetry, and unclear return on investment.

---

## The Solution: A Unified Center of Excellence

The answer here is to create a **unified center of excellence** to continually drive maturity, and we'll discuss what that means. Organizations that have a mature observability strategy or centralized observability have seen that **79% have saved time or money** by doing so. You’ve probably heard a lot about our observability survey, and that’s where this insight comes from.

Now, let’s talk a bit about the **Golden Path framework**. This is at the center of today’s discussion. 

Last year, a customer from a large global company with a broad observability platform across 79 different countries came to us with a simple question: *How good are we at observability? Are we doing the right things?* We were a little stunned and didn’t know how to answer that, which encouraged us to create the observability maturity model. 

This model has been live on our website. It’s quite simple; you can link to it, answer a series of questions, and it will pinpoint you along this observability journey as either reactive, proactive, or systematic. 

That same customer came back four months later and asked, *Great, I’m in the red zone; apparently, we’re really reactive. How do we get to green?* This inspired us to build out what we call the **Golden Path**, which is a set of best practices that we’re harnessing together to give you insights into how to improve your observability platform.

---

## What is a Center of Excellence?

So, what exactly is a center of excellence? A center of excellence essentially centralizes observability efforts and helps you achieve real-time end-to-end visibility into your systems. 

It can be a dedicated team, a federated team, or a hybrid team—whatever works best for your business. It serves as a strategic function that enables better decision-making, faster incident response, and continuous improvement. 

It's not just about improving operations either; it's about driving the right culture. You’ll hear me mention culture a few times today. It’s super important to get people, processes, and technology right.

### Functions of a Center of Excellence

In practice, some functions of a center of excellence include:

- **Standards and Best Practices**: Establishing guidelines for observability.
- **Education and Training**: Helping teams better utilize tools.
- **Consulting and Supporting Teams**: Providing assistance to various teams.

Other, less obvious but equally important functions include:

- **Tooling, Templates, and Guides**: Building and maintaining tools used by teams, such as dashboard templates.
- **Admin and Vendor Management**: Centralizing administrative functions, including licenses and identity management.
- **Community Building**: Creating a space for exchanging ideas, sharing information, and celebrating success stories.

Many customers I’ve worked with have a centralized team that runs training for broader audiences, even if they’re not on the same team. In larger organizations, there may be a rollout plan to replace existing tooling with Grafana, and the center of excellence plays a crucial role in planning and tracking this.

---

## Bringing It All Together

Bringing it all together, here’s a high-level view of who does what. As I mentioned, the structure can be centralized, federated, or hybrid, depending on what works best for your organization. Different personas can share roles in smaller teams, while larger organizations may require dedicated roles such as project managers.

By a show of hands, how many of you consider your organization to have an observability center of excellence? 

Brandy has done a lot of work in establishing what a strong center of excellence is at Grafana. If you have the opportunity to talk to her later in the conference, definitely stop by; she has a lot of valuable information on how to do it.

---

## The Golden Path Rollout

The Golden Path is about best practices and how we bring them all together. To do this effectively, we want it to be outcome-driven. We don’t want to just talk about the talk; we want to present concrete outcomes and instrument this effectively in our companies.

We want the best practices to be real, authored by our professional services team, observability architects, solutions engineers, tech support teams, and our partners and customers who have harnessed great practices. This information will be available on our website in a modular format, allowing you to focus on areas that are most relevant to you.

Earlier in the year, I asked my team a simple question: *Where do our customers get stuck in adopting Grafana Cloud?* The responses fell into three categories:

1. **Technology**: For example, we’re developing a best practice white paper on optimizing data telemetry pipelines.
2. **Operational Excellence**: This encompasses organizational strategies, such as building power users and interfacing with InfoSec for log management.
3. **Business Insights**: Many customers struggle to translate metrics into business value, which can be challenging depending on the organization's size.

We are working to provide customers with dashboards that address questions like:

- How available is our observability platform?
- What cost savings are we yielding from adaptive telemetry?
- How effective are our teams?

These insights are crucial, especially when changes occur, such as leadership transitions or acquisitions. It’s essential to have metrics of success readily available.

---

## Getting Started

So, how do we get started? We are launching a **Golden Path Hub** soon, where you’ll find all these resources as we release the various modules. In the meantime, feel free to engage with an observability architect if you have questions. Many of you may already be working with our observability architecture teams, so reach out to them if you're collaborating with a Grafana account team.

The first module we’re releasing will focus on the center of excellence, complete with resources like a tactical checklist for building a center of excellence and our maturity model, which you can start utilizing today.

## Raw YouTube Transcript

Hey everybody, I'm Brandy Smith. I'm one of the leaders on our
observability architecture team, and I'm joined by Jeff. Hi, I'm Jeff Freeman, VP
of Customer Solutions, which is a totally made up name, but it's basically our professional
services team, our SE team, our tech support team, and our
observability architecture team. Awesome. So let's set the
scene here. Picture this, it's lunchtime and a customer is
on your app trying to order food, but the order fails. Here's the kicker. On the backside one team's metrics
are green, another's logs are delayed, and the alert that should
have fired didn't. Frustrated, The customer opens your competitor's
app and they place an order there instead to the customer,
it just looks broken. Now it might seem like
one loss transaction, but in reality it is thousands of
lost sales and a hit to your brand's reputation, all because
observability was fragmented. And that's the reality for a lot of
teams today. Observability is everywhere, but it's fragmented. You've got
siloed data, the ownership is unclear, and the context lives in tribal
knowledge. We've normalized this chaos, but the truth is, if your strategy is
fragmented, your response will be too. And teams have different definitions
of what good looks like. They might be asking, what are we instrumenting?
Are our dashboards any good? Are we doing too much or not enough? Now while one team measures
uptime, another logs everything, and another ignores alerts
entirely alert fatigue is real. We've seen this with platform teams,
SREs, product owners, and even executives. Everyone's answer is different,
and that's a problem. And the cost is around misalignment,
alert, fatigue, bloated telemetry, and unclear return on
investment. Excuse me. The answer here is to create a unified
center of excellence to continually drive maturity, and we'll talk
about what that means. So in organizations that have a
mature observability strategy or the centralized observability, 79% have
saved time or money by doing so. You've probably heard a ton about our
observability survey and that's where this comes from. Alright, all right, so let's talk
a bit about Golden Path framework. So this is kind of the center of
today's discussion. Last year, just a little bit of history, we had a customer that came up to
us and they had this large global company, this really broad observability
platform, 79 different countries, and came to us with a
really simple question, which was how good are we
at observability? Are we
doing the right things? And we were a little bit stunned by that. We didn't really know how to answer it. So that really encouraged us to create
this whole thing around the observability maturity model, which is now
has been live on our website. It's really actually quite
simple. You can go in there, you link in it would basically ask you
a bunch of questions and then it would pinpoint you along this observability
journey as either you're reactive, proactive, or you're systematic, right? So that was a really interesting
step. We can plot you along the journey. And then that same person came back
four months later and goes like, great, I'm in the red zone, apparently we're
really reactive. How do we get to green? I was like, well, that's also a really good question we
should probably have the answer to. And that's inspired us to build out
what we're calling the golden path, which is real simple. Contextually all that is a set of best
practices that we're going to harness together to give you insights as to how
to improve your observability platform. So that's currently our work in progress, and we're starting with this one key
area around center of excellence. And this was an easy way for us to
start because a lot of questions came out more on the operational
layer versus the technical layer. And this one customer, I'll
let you speed read this quote, but came to us and said basically
they're having really big problems in organizational structure,
productivity velocity, and by going through and taking time with
them to build a center of excellence, they had marked improvements
in all areas. So Brandy, what is exactly a center of excellence? So a center of excellence
is essentially it centralizes observability efforts and
it helps you get real time end-to-end visibility into their systems. It can be, we'll talk a little bit about what
different center of excellence looks like, but it doesn't have to
be one dedicated team. It could be a federated
team or a hybrid team. It really depends on what
works best for your business. It serves as a strategic function. It
helps enable better decision making, gives faster incident response
and continuous improvement. It's not just about
improving operations either. It's about driving the right culture. So you'll hear me mention
culture a few times today. It's super important to get people,
process and technology right in this. And so what does it actually
look like in practice? Some of the functions of a center of
excellence are obvious things like standards and best practices,
education and training, looking at how to make the most of your
tools and consulting and supporting teams. But there are other
functions that are not so obvious, but they are equally if
not more important. So this
will be things like tooling, templates and guides, building and maintaining some of
the tooling used by the teams. Maybe you're making dashboard
templates or library panels, admin and vendor management. This is huge
to have a centralized team to do this. It's not just admining the system itself,
but looking at things like licenses, renewals, identity and
access management as well. And then community, again, I told you
this is going to come up a lot today. It's important to build
a Grafana community, allowing to exchange ideas and share
information as well as success stories. Many of the customers that I've worked
with in the past have a centralized team that then runs trainings for the
broader folks using the platform, whether or not they're on the
same team. And then lastly, in large organizations, there may be a large rollout plan to
replace existing tooling with Grafana and someone needs to plan and track this, and that's also another place where
the center of excellence comes in. And so bringing it all together, this
is a high level view into who does what. Like I said before, they can be
centralized or federated or hybrid team. It really is about what works
best for your organization. Different personas can be
shared in a smaller team, so maybe wearing different
hats as you see here. And the size truly depends
on the organization. Sometimes the project manager or PM role
may only be applicable in larger orgs. Smaller orgs just don't
have those resources. And you could also have
multiple SMEs in a large group. And so by show of hands, how many of you would consider yourselves
to have an observability center of excellence. Brandy? Brandy did a lot of work in actually
establishing what a strong COE is at Grafana. So if you have an opportunity
to talk to her later in the conference, definitely stop her. She's got a lot
of great information on how to do it. So the golden path, needless to say, our marketing team is having a lot of
fun designing our T-shirts around this. But from a rollout perspective, it is really about best practices
and how we bring 'em all together. And so in order for us
to do this effectively, certainly we want it to be outcome driven. We don't want to have the talk about the
talk. What are you actually providing? What are you presenting? And how can we
actually instrument this in our company? And we want them to be real. So the authors of all these
different best practices, which will be shown out through
white papers, how-to videos, demos, all different kind of vehicles, but they're authored by our professional
services team. They're authored by our observability architects,
like folks on Brandy's team. They're authored by our solutions
engineers and our tech support teams, but also authored by our
partners and customers who in effect actually have harnessed some
really great best practices and will participate with this in
collecting all this information. It's going to be available on our
website. And the nice thing about it too, it's not going to be this long boring
novel that you have to read page to page. It's going to be very modular. So for the areas that have
specific interest or relevance, if you want to really focus in on tracing
or if you really want to focus on COE, you'll be able to do so. You'll be able to pinpoint the areas
that are most efficient for you and relevant. So earlier in the year, I asked my team a simple question.
And again, this is professional services, our tech support teams, our
observability architects. I said, where do our customers get
stuck in adopting Grafana Cloud? Where do they fall down? Where do things
stall out? It was really interesting. They sent in just all the different
topics and areas that they felt like their customers were experiencing. And it was interesting also that we could
actually fit them all in these three nice little boxes, like
one, certainly technology. So an example of technology best
practice that we're working on is optimizing data telemetry pipelines. So from various different endpoints
and applications from instrumentation into cloud, egress, ingress,
add a cloud across VPCs. There's a lot there to know how to
optimize things like fleet management with Alloy. That's a great example of a technological
best practice white paper that we're building and we're going
to be releasing soon. But operational excellence was another
big topic. So the things that Brandy was talking about for center of excellence,
nothing to do with product at all, but really about how do we
organize effectively internally. So center of Excellence is
a great example of that. Building power users is a great example. Interfacing with InfoSec
was a really popular one, especially for things like log
management and security access. These are things nothing
to do with product, but we have to actually bring these
things forth because you're going to run into these pitfalls invariably
in your observability journey. It's our job to help you through it. And then this is one of the
ones I found most interesting, which ties into our strategy in terms
of how we're moving toward business observability was business insights. So you saw from Ocado, they were
talking about in the end here, kind of the core benefits of moving to
Grafana. But where a lot of customers stall out or struggle is like how do
you actually materialize the metrics of that? So what does that
actually mean for your company? What does it mean for your business? And it turns out it's actually
pretty hard to do, right? Depending on how larger company is, how you've already
reestablished these metrics. So some of the efforts that we're
working on from a business insights perspective is to arm our
customers with dashboards like tactically, we can
address things like, okay, how available as our
observability platform. What are some of the cost savings we're
yielding from things like adaptive telemetry year upon year? How are we enabling our
teams and our users, how effective we are that what
are some of our MTTX timeframes across these applications? Those
actually are fairly simple. But then if you take even a
greater leap and then say, okay, well what does this actually
mean to the business? So that's even a higher
level of abstraction we can
work with you on and saying, okay, we are shipping orders faster
because of our observability platform. We're able to mitigate churn because
of our observability platform and the insights that we're getting, and we're able to actually
increase our customer velocity. So those are examples that will
have very industry specific focus areas that we can start to
bring to light. And again, as we talk about it, a certain customer we just consulted
with from a co OE perspective, just by having this
more advanced structure, this more kind of standardized
approach, they had a real impact. They were able to obviously improve
their MTTR as demonstrated here, but actually a true financial impact
that they also received. And in fact, they built a dashboard that they
show back to the business. So again, the business insights
are really important, especially when you think about things
that happen that are beyond your control. When you have leadership changes, when you have things like
acquisitions that occur, it's always going to be important to
have these metrics of success at your fingertips. So how do
we get started, Brandy? Yeah, so we are going to
have a Golden Path Hub. It's coming soon where you'll be able to
see all of these resources as we launch the different modules of the
Golden Path. In the meantime, you can find an observability architect
here today. If you have questions, find one of us. And some of you may already be working
with our observability architecture teams, so definitely engage them if you've got
an OA that you're working with or your Grafana account team. And so the first module
of this, as I mentioned, we're going to be releasing
a center of excellence. We've got a few resources
for you already available. That's going to be things like a
tactical center of excellence checklist. How do I go and build this thing?
We've also got our maturity model, which you can take today. Some of you did and had a session with
our OAs and some other resources here.

