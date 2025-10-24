# Just Eat Takeaway.com Ensures Millions of People Get Their Orders Reliably — Here&#39;s How

Published on 2025-10-22T16:59:27Z

## Description

Discover how Just Eat Takeaway load tests at global scale using Grafana Cloud k6. Senior Support Reliability Engineer, ...

URL: https://www.youtube.com/watch?v=qG5tCR4OS9g

## Summary

In this presentation at ObservabilityCON, Christopher, a Senior Site Reliability Engineer at JustEatTakeaway.com (JET), discusses the company's approach to load testing using Grafana Cloud k6. He begins by explaining the critical importance of reliability and performance testing for JET, which operates in 17 countries and processes over half a billion orders annually. Christopher outlines the evolution of JET's load testing practices, particularly after a significant incident caused by inadequate load testing on a Tier 3 application, which impacted their core services. He details the transition from an in-house tool named Rambo to adopting k6, emphasizing a user-centric approach that encouraged engineers to embrace the new tool. The presentation covers various types of load tests conducted at JET, including pipeline testing and scheduled stress tests in production environments, highlighting the importance of real-time testing to ensure system reliability. Key takeaways include the interconnectedness of services, the importance of selecting tools that meet engineers' needs, and the necessity of testing in production to build confidence in system performance.

## Chapters

Sure! Here are the key moments from the livestream along with their timestamps:

00:00:00 Introductions and speaker background  
00:02:30 Overview of JustEatTakeaway.com (JET) and its operations  
00:04:15 Importance of load testing and risks of not performing it  
00:06:00 Explanation of Application Tiering at JET  
00:09:30 Introduction to the analytics service and its migration  
00:14:00 Description of the incident during the migration on a busy Friday night  
00:18:45 Lessons learned from the incident and the importance of load testing  
00:22:00 Introduction to Rambo, the in-house load testing tool  
00:26:30 Transition to Grafana Cloud k6 and its adoption  
00:30:15 Overview of load testing processes and pipelines at JET  
00:34:00 Key takeaways on load testing and its importance in production environments  

Feel free to ask if you need any more information!

# Load Testing at JustEatTakeaway.com with Grafana Cloud k6

Hello, ObservabilityCON! It is an absolute pleasure to be here with you today. I'm Christopher (he/him pronouns), and I will be talking about how JustEatTakeaway.com (JET) load tests using Grafana Cloud k6. 

## About Me

First, a little bit about myself: I'm a Senior Site Reliability Engineer at JustEatTakeaway.com, and I've been here for around 6.5 years. I originally started on one of our Product Engineering teams but gradually shifted to find my home in Platform Engineering. Now, I am based in the Platform Assurance team, where we provide reliability tooling to over 2,000 colleagues in our product and tech department. 

As you can tell by my presence here today, I am very passionate about performance testing and ensuring overall system reliability. Outside of work, I enjoy photography and video games, and yes, I do have a maxed Ironman account on RuneScape.

## Agenda

Now, let's take a look at the agenda for today:

1. Introduction to JustEatTakeaway.com (JET): Who we are, where we operate, and why reliability is critical for our business.
2. The importance of load testing and the risks associated with the absence of load tests.
3. How our platform has evolved over time and how we have adopted Grafana Cloud k6, along with the benefits it has brought us.
4. How we load test at JET and what we encourage our engineers to do.
5. Key takeaways.

## Introduction to JustEatTakeaway.com

JustEatTakeaway.com is a leading global on-demand delivery company with over 350,000 partners located across 17 different countries. These partners serve over 60 million active customers, and in 2024 alone, we processed over half a billion orders. 

With operations in 17 countries and spanning across 15 different time zones, we process thousands of orders throughout the day. Uptime is critical for us, especially ensuring we can handle peak load during busy times, which will be a key focus of my talk today.

## Importance of Load Testing

Load testing involves putting your applications and services under varying levels of load and monitoring their performance. Why is this important? By the end of this session, I hope to convey a strong understanding of why load testing is crucial and inspire you to implement it within your organization.

### Application Tiering at JET

At JET, all components deployed into a production environment are assigned a tier, ranging from Tier 1 to Tier 3. Tier 1 components are critical for processing orders and avoiding legal or compliance risks. In contrast, Tier 3 components provide additional features and improve user experience, but without them, order processing can still occur, albeit with some reduced functionality.

### Case Study: Analytics Service

Let me introduce you to our analytics service, a Tier 3 application at JustEatTakeaway.com. This service receives over 750,000 requests per minute, especially during peak times. In 2024, this service migrated from legacy EC2 infrastructure to EKS. However, this migration was conducted without load tests in place.

To illustrate, both our EKS and EC2 deployments direct traffic through the same API gateway. In EC2, traffic is managed by a dedicated application load balancer, while in EKS, it goes through an Istio gateway responsible for multiple applications within the cluster.

The migration was gradual, but during a Friday night when order traffic surged, we encountered issues. Our analytics service initially functioned well, but as traffic increased, one of the underlying nodes struggled with high CPU usage. This led to a significant drop in incoming orders, affecting our Tier 1 components and ultimately resulting in one of our largest incidents.

### Lessons Learned

To summarize, we load test not to celebrate successes but to uncover failures. The incident I shared could have been prevented with prior load testing. At JustEatTakeaway.com, we maintain a blame-free culture, acknowledging that Tier 3 services often go untested, and we've learned that they can significantly impact critical components.

This incident led to changes in our platform architecture and our approach to performance testing, which eventually resulted in our migration to Grafana Cloud k6.

## Load Testing at JET

At JET, we have been load testing for many years, using an in-house tool named Rambo since 2016. Rambo consisted of a test orchestrator, a cache, and a cluster. However, it became increasingly bloated over time due to feature additions and incident responses.

To address this, we adopted a user-centric approach in evaluating replacements. We conducted user research to understand the challenges with our existing tooling and built internal proof of concepts. After selecting k6 as our global load testing tool, we received overwhelmingly positive feedback from our engineers, who were excited to use it.

### Utilization of k6

Here's how we utilize k6:

- **Pipeline Testing:** We integrated a k6 step into our standard CI/CD pipeline that runs a selection of tests defined by our engineers. If tests pass, the deployment to production proceeds; if there are errors, deployment is halted to prevent negative user impact.

- **Weekly Stress Tests:** We run an analytics stress test, making over 45 million requests in one hour to ensure our platform can handle peak loads. Additionally, teams can manually trigger tests as needed.

- **Order Flow Stress Tests:** These tests validate critical Tier 1 applications by simulating real user behavior across all countries we operate in, helping us confirm that we can handle peak order traffic.

### Testing in Production

We run all load tests in production environments, which may seem intimidating, but it builds confidence in our platform's performance under real user load. We encourage our teams to embrace this practice to ensure their components can handle actual traffic.

## Key Features of Grafana Cloud k6

Using Grafana Cloud k6 provides us with several valuable features:

- Curated dashboards with extensive test run information.
- Thresholds to automatically stop tests experiencing problems, minimizing user impact.
- Unique load zones for testing relative to our real users, including internal services.
- Quick integration with GitHub Actions for seamless test execution.

## Key Takeaways

1. **No Service Runs in Isolation:** Load testing helps uncover ripple effects across various services. It is crucial to test both upstream and downstream.
  
2. **User-Centric Tools:** Involve engineers in the selection of load testing tools to encourage adoption and enthusiasm.

3. **Confidence in Production:** Testing in production is vital. It validates how your environment handles real traffic and ensures confidence in your releases.

I hope this has been useful to all of you today. If you have any questions, I believe we have time. Thank you!

## Raw YouTube Transcript

Hello ObservabilityCON. It is an absolute
pleasure to be here with you today. I'm Christopher, he/him pronouns, and today I'm going to be talking to
you about how JustEatTakeaway.com load tests using Grafana Cloud k6. But first, a little bit about myself. I'm a Senior Site Reliability
Engineer at JustEatTakeaway.com, and I've been here around 6 1/2 years now. I originally started out on one
of our Product Engineering teams, but in this time I've gradually
shifted and found my home in Platform Engineering. I'm now based in the Platform Assurance
team and in this team we provide reliability tooling to
over 2000 colleagues in our
product and tech department. As you can tell by me being here today, I'm very passionate about performance
testing and ensuring overall system reliability. Outside of work though, I do enjoy photography
and video games, and yes, I do have a maxed Ironman
account on Runescape, but if we have a bit of a
look at the agenda for today, I'm going to give you an introduction to
JustEatTakeaway.com (JET), who we are, where we operate, and why reliability
is critical for our business. I'll talk to you about the importance
of load testing and what can happen with the absence of low tests, what
the risk to your platform is. This will lead us into how our platform
has evolved over time and how we have adopted Grafana Cloud k6, and the benefits it has
bought us. And then finally, I'll discuss how we load tests at JET, what we encourage our
engineers to be doing. And then I'll finish off with a
couple of key takeaways for you. JustEatTakeaway.com is a leading
global on demand delivery company. We have over 350,000 partners, which are located across
17 different countries. These partners are then used by
over 60 million active customers. And in 2024 alone, we took
over half a billion orders. As I mentioned, we are in 17 countries, but within the countries we are then
split across another 15 different time zones. So throughout the day we are processing
thousands and thousands of orders. Uptime for us is key and
ensuring we can handle peak level load throughout the day, that is critical and that is going
to be a key focus of the talk today. So load testing involves putting
your applications and your services under different levels of load
and monitoring their performance as you do. So why is this important? That is one of the key questions I would
like to try to answer for you today, and that I hope by the end
of this session, if you're
not already load testing, you have a strong desire and
understanding of why it's important and a need to implement it
within your organization. But first I want to talk to you
about Application Tiering at JET. All of our components that get deployed
into a production environment are given a tier. This ranges from a Tier 1
component to a Tier 3 component. Those that are tier one are those
that are critical to our platform. These are required in order to
process an order or without these components, we would hold
a legal or compliance risk. But on the other end of this scale,
we have our Tier 3 components. These give our users additional features, they improve our user
experience, but without them, there are simply reduced
user functionality, but we
can still process orders. Our core business operations still work. We may see a minor conversion
impact or a revenue impact, but the business functions. But what this really means is
a Tier 3 component should never in any way be able to impact
the flows of a Tier 1 or Tier 2 component. So now let me introduce you
to our analytics service. This is a Tier 3 application,
JustEatTakeaway.com. And by definition, this means it is non-critical
and should not affect our Tier 1 or our Tier 2 components. This service receives a
lot of data per minute, is getting over 750,000 requests, and at peak, even more so. But in 2024, this service went through a migration. It moved from legacy EC2
infrastructure over to EKS. And this is a migration we
actively encourage teams to do. We have seen a lot of
benefits containerizing,
our applications addressed, but in this situation, it was done
without any load tests being in place. To give you an understanding
of the changes here, you can see our EKS and EC2 deployments. And in this you can see
how traffic is directed. For both of these, the traffic enters the platform the
same way through the same API gateway. But on our EC2 deployment, this traffic goes to a dedicated
application load balancer, which does what you expect. It distributes the traffic
between the various EC2 instances. Our EKS deployment, however, is
a bit different. This deployment, the traffic again goes
into our API gateway, but it now goes to a secondary gateway: our Istio gateway inside
of our EKS cluster. This gateway is not just responsible for our analytics service, it is
responsible for application A, application B, all of
those in this cluster. So for our analytics service,
the traffic hits this gateway, it goes through the virtual
service to the service, and eventually to the pod.
But that same flow happens for application
A, B, and C. Everything in that cluster. This migration, the analytic service
did, it was not a big bang migration. It was done gradually over the
course of a week. Each day, the rollout percentage was increased
and the platform and the service itself were monitored. So why am I
talking to you about this? And like all good reliability stories,
it happened to be a Friday night for us. In the UK. People had finished work,
they were ordering their takeaways, they were ordering their groceries
so they could make dinner, and that's exactly what we saw happen.
We saw our orders starting to come in. We saw traffic hitting our platform. The EO gateway, I just mentioned, started our evening running at three pods. This gateway had a horizontal pod
autoscaler configured so it could scale out to a maximum of five pods. We started our evening at 60%
capacity, therefore not great, but it wasn't the end of the world. And then as orders came in,
so did analytics traffic. Users were interacting with our platform, they were going through our
help pages, going through menus, and all of this generated more
and more traffic. So to handle it, a fourth pod scaled in
everything working as expected, we were at 80% of our HPA capacity. The evening continued. We got more
orders and we got more traffic, and we were now at 100%
capacity. Unfortunately, at this time, one of the underlying
nodes that these pods were scheduled on, it started struggling. It
hit very high CPU usage. And that is when our entire
evening completely changed. We saw a sudden drop in
incoming orders to our platform, one of the five pods for RSDO gateway. It got taken out of service. This gateway, as I mentioned, did not just
power or serve analytics traffic, it served traffic to other
components in the cluster. And these components were our
Tier 1 and Tier 2 components critical to placing an order. I'd love to say things
got better after this, but the evening continued and we saw
an even further decline in incoming orders. A second EKS node hit 100% CPU. These pods in the SDO gateway, they were split across two nodes, both of which were now struggling with
very high CPU and very high memory utilization.
We had three pods serving what, at least five, honestly, ideally a lot more than
five were needed to serve. And it is very safe to say our
platform was struggling at this point. So we engaged our on call teams, we
got our Platform Engineers involved, and we were able to scale out of this, and we were able to recover our
platform for the evening. However, this incident had a drastic
hit on our users and our business. Our users were hungry.
They wanted to order their takeaways, their groceries, and
every item they needed, and they were having issues doing so. But for our business to this day, this is still one of our largest
incidents we have ever encountered. So to summarize this for you, we are not load testing to
celebrate every success. We're not testing to celebrate every
green light we get from a test. No, we load tests to uncover failures. And in this incident I just shared, it would've been prevented if it
had been load tested before reaching 100% rollout. I want to
make it very clear here, though I'm not blaming the owning
team for this. At JustEatTakeaway.com, we have a blame-free culture.
And when this incident happened, Tier 3 services, they weren't often
considered for load testing. It wasn't considered that a non-critical
platform feature could have such wide impact on the rest of our platform, that it could affect upstream
and downstream services. So from this incident, we
had a lot of learnings, a lot of changes to how we architect
our platform to prevent this happening, but also a lot of changes to how we
performance test at JustEatTakeaway.com, which did lead to our eventual
migration to Grafana Cloud k6. And I know you want to hear
more about k6 and how we use it, but first I want to talk about how we
load tests and how we have been at JET. So let me introduce you to Rambo. At JET, we have been load testing for
many, many years, since 2016. We developed an in-house tool named Rambo, which consisted of a test
orchestrator, a cache, and a cluster. This orchestrator bought up
short-lived ECS tasks in our cluster. If these needed to communicate
between one another, they had a Redis cache to do so. These tasks were then run a
dedicated test engine, JMeter, Taurus or Artillery. When Rambo was first created,
it supported only JMeter. These other two engines, they got added to improve our user
experience and to further improve the experience. We added additional features
sometimes in response to platform incidents had to add
safeguards into Rambo. But because of all of this, Rambo became more and
more bloated over time. So we wanted to have a
look at replacements on the market. To do this, we wanted to take a user-centric approach. We did not just want to throw
a tool out there to them. So our team provides load
testing-as-a-service to engineers. They write their own tests
and we maintain the service. So we did some user research. We wanted to understand everyone's needs
and their current challenges with our tooling. Once we had all this information, we were able to build out some
internal proof of concepts. We selected two services off the shelf.
We set these up internally, which gave our team the
understanding of how they work, what the maintenance was to maintain them. But then more importantly, we could put
these tools in the hands of our users. And that's exactly what we did. We gave our users some test scenarios
and asked them why to load tests in service A and service
B. And as they did this, we gathered feedback, we learned
what they liked, disliked, and honestly what they
hated. But based on that, we can make an informed decision and
decide on the service we want to use globally at JET for load testing. Once we'd selected the tool,
we wanted to deliver it. We don't just want to
give them the service. We wanted to integrate it in our systems, so it feels seamless
to our users using it. And then onto the adoption phase, we
wanted our users to get off of Rambo. We wanted them to adopt this new tooling. So after all of this, and as I'm
sure you can tell by our talk title, we adopted k6 as our
global load testing tool. In this process, we got a huge amount of positive
feedback about the service. Our engineers absolutely loved it. But one very big thing about this, k6 was the tool picked by our engineers. It was not picked for them, and
therefore they wanted to use it. They were excited to use it. So how do we actually
utilize this tooling? I know that's what you're
all here for today. It's our global tooling used across all
of our companies with countries with engineering for performance testing. And let's start off with pipeline testing. What you see here is a standard CICD
pipeline. It's nothing new to you. The application gets built and during
those additional steps, one unit tests, security scans the standard, and
it then gets deployed through QA, through staging, everything you'd expect. But we have
added a new step for our engineers, a one k6 step. This does
exactly what it says on the tin. It will run a selection of tests for
our engineers, whatever they define. And based on this step, engineers
will get immediate output. They will be told if their response
times were within thresholds, were there any errors, and if
any custom checks they defined, have they passed? If all
of this comes back green, like in this example, the pipeline allows them to deploy
to production and they can do so knowing their performance
has not been degraded. The customers are getting
the best experience possible. But if this step had to
come back with any errors, the pipeline could make a decision
to prevent a production deployment preventing any negative
impact to our will users. This for us is critical. We want
to shift left as much as possible, catch issues as early as possible. Alongside pipeline testing, we run
a weekly analytics stress test. If you look back at that
incident I just shared with you, this test covers that exact situation. And if you can see the metrics on
there, it makes a lot of requests. In that one hour period, it made over 45 million
requests to our analytics service. Upwards of 17,500 requests per second. This one's on a schedule so we can
ensure the same issue we saw before, does not happen again, and that any other changes teams have
made have not affected our wider platform. But if the team that owns the
analytics service needs to test it, they've made a change.
They can do exactly that. They have the ability to
manually trigger a test. We also run order flow stress tests, and these tests are Tier 1 applications. So those I mentioned earlier that
are critical to our business function and these tests, one concurrently through all of the
countries we operate in at once, and they cover that core
flow. They go to our homepage, the search page menu, they build a basket and they eventually
place a test order on our platform. We do this to help validate changes
that teams have made per week on the JustEat platform. We make over 1,100 changes, and these have all been deployed
through staging into production. We make a lot of change. So these tests help us. They confirm we can
handle peak order traffic. However, all of these tests
I've just shared with you, there is one additional thing about them. We do not only run these in staging. At JustEatTakeaway.com, we run all of our load tests
in production environments. This is something we
encourage our teams to do. We want production to be a part of
their software development lifecycle. We want them to have faith in the
components they are releasing, the components they are being on
call for and testing in production is how we achieve that. And I'll
be honest, to a lot of people, this seems absolutely terrifying. Putting your production environment
under peak level load when you also have real users using it at that time is scary. But that fear is what
then gives you confidence. You know that going into your
weekend, "Yeah, you can handle it. The platform is good". So to summarize how we load test
address JustEatTakeaway.com, we offer pipeline testing for teams. They can embed this in their standard
CICD pipelines and throughout their development process. This gives them confidence and they
can run these tests in staging, but also in production. Teams can run schedule tests to get
continuous feedback on how their applications are performing with
change and with wider platform change. And then finally, teams
can run on demand tests. If they've made a change and
need to validate performance, they can do exactly that. And they are empowered to run the
test whenever they think best in whatever environment is
best for their situation. All of this we achieve
using Grafana Cloud k6. And out of the box, we get a
lot of very useful features. We get given curated dashboards
with extensive test run information. All of the screenshots you've just
seen. Yep, got them out the box. But if you need to dig deeper into
exactly how an individual request or endpoint is performed,
you can do exactly that. We have thresholds. And when
running a test in production, these are our number one feature.
These are critical to us. If a test is experiencing any problems, thresholds can detect these and they
can stop the test automatically. So if we see an elevated number
of 503s from a production Test 1 cool, they can be stopped automatically
without any or with minimal user impact. Grafana Cloud k6 gives
us 21 unique load zones. This means we can test in a
location relative to our real users. And if we need to test an
internal service, cool, we can do exactly that. We can set up an internal load
zone and we can hit the endpoints. And then finally, out of the box, we get given a GitHub actions
integration within minutes of importing this to a
GitHub actions workflow, you can have tests running locally
on the GitHub actions runner. You can have them in your private load
zone or running through Grafana k6 Cloud. And these are just some of
the key features that we
are utilizing every single day when we run load tests. So a couple of key takeaways for you today. No service runs in isolation. Load testing helps you uncover ripple
effects across a variety of different services. As an engineer, you may believe your service
will not impact any others, but just believing that is not
enough to gain that confidence. You need to have a test in place. You need to run a performance test
and look both upstream and look downstream. Your tools should be there
to serve your engineers. We had a user-centric
approach in adopting k6. However, doing this resulted
in a really fast rate. With Rambo, we had teams honestly not wanting to
ride tests because it was a very tedious process. With k6, we had teams coming to us while we were
still developing it and embedding it, asking us, "can we be an early
adopter? We want to write load tests". In platforms, this isn't
something we see very often. So when you are selecting a tool, have your engineers select it and
they will want to use it. And finally, confidence lives in production. We all love our staging environments. They give us a lot of
assurances pre-production, but the real test is how your production
environment handles that traffic, how it handles intensive load. If there is one minor difference
between staging and production, you could invalidate your whole test. Have confidence to run in production, and you'll have confidence
in your production platform. I do hope this has been really
useful to all of you today. If you do have any questions, I
believe we have time. Thank you.

