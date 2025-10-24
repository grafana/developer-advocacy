# How Fivetran migrated enterprise observability from New Relic to Grafana Cloud in 60 days

Published on 2025-10-15T14:28:23Z

## Description

In this Observability Sessions Bay Area talk, Mike Gordon, VP of Platform Engineering at Fivetran, shares how his team migrated ...

URL: https://www.youtube.com/watch?v=uj92QG2OngI

## Summary

In this YouTube video, Mike Gordon, VP of Platform at Fivetran, discusses the company's successful migration of its enterprise observability from New Relic to Grafana, which was completed in 60 days. He outlines the migration's goals, including cost efficiency, improved query performance, and the need for a reliable observability solution to support Fivetran's operations, which handle around 6 million data syncs daily. Key points include the involvement of Fivetran's SRE teams, the strategic planning that enabled a smooth transition, and the importance of training and support for engineering and support staff during the process. Gordon emphasizes that the migration was not just a technical challenge but a people problem, requiring buy-in and adaptation from various teams. The lessons learned from this migration will inform future projects, such as transitioning to Jira.

## Chapters

Here are the key moments from the livestream along with their timestamps:

00:00:00 Introductions and overview of the talk  
00:02:00 Introduction to Fivetran and its services  
00:05:30 Overview of Fivetran's infrastructure footprint  
00:08:00 Discussion on observability requirements for data syncs  
00:10:30 Introduction of the team involved in the migration  
00:12:00 Goals for migrating from New Relic to Grafana  
00:15:30 Strategy for evaluating solutions and planning the migration  
00:18:00 Execution plan and timeline for the migration  
00:20:30 Training and support strategies during the migration  
00:24:00 Lessons learned from the migration process  

Feel free to ask for any more details!

# Migration of Enterprise Observability in 60 Days

Hi everyone, my name is Mike Gordon, VP of Platform at Fivetran. Today, I'm going to talk about how we migrated our enterprise observability in just 60 days.

## Agenda

1. Introduction to Fivetran and myself
2. Overview of our infrastructure footprint
3. Observability requirements
4. Key personnel involved
5. Strategy and execution
6. Lessons learned from the migration

## About Fivetran

Fivetran was founded in 2012 and has grown to serve over 10,000 customers with a team of more than 1,200 employees located across various offices around the world. Our platform engineering organization includes four Site Reliability Engineering (SRE) teams that played a significant role in this migration.

### What We Do

We synchronize data from about 600 different sources to a few dozen destinations. With just one click, we can sync data to data warehouses, data lakes, and other platforms. Our motto is to make data as simple and reliable as electricity—just plug Fivetran in, and your data syncs from point A to point B.

Customers choose our product because we are reliable, fast, and more cost-effective than having a data engineering team build custom pipelines. We run approximately 6 million syncs a day, which leads us to our observability requirements for managing such a large infrastructure.

## My Background

At our all-hands meetings, we have a segment called "Meet a Fivetraner." Here’s my 30-second version:

- I learned to program on an Apple IIe.
- I attended West Point and majored in computer science.
- I served in the Army for five years, focusing on networking and communications.
- I worked for Northrop Grumman and Cedars-Sinai in Los Angeles.
- I spent about eight and a half years at Google, where I also earned an MBA from Colorado State.
- I then joined Hippo, an InsureTech company where we used Grafana open-source software and were also a customer of Fivetran.
- I have been at Fivetran for three years, leading the platform engineering team.

## Our Infrastructure Footprint

To give you an idea of what we needed to monitor, we operate in about **39 regions**, each with multiple Kubernetes clusters. In each region, we have a connector cluster for data syncs and a supporting services cluster. Currently, we manage thousands of servers and tens of thousands of pods, making it essential to have a robust observability framework.

### Observability Footprint

We handle over **170 terabytes of logs**, using logs and metrics as our primary observability tools, along with synthetics and traces. Each of our approximately 50 engineering teams is empowered to configure their own alerts and dashboards. Our centralized SRE team also provides on-call support as a backstop.

## Personnel Involved

In terms of personnel, we have:

- **30 SREs** in our organization
- **300 software engineers** spread across about 50 teams
- **150 support engineers** who assist our customers daily

As we migrated, it was crucial that we maintained support and operations without interruption.

## Migration Goals

We transitioned from New Relic to Grafana due to several reasons:

- **Cost Efficiency**: Annual contracts with New Relic were unpredictable, prompting us to seek a more stable solution.
- **Performance**: Our log queries in New Relic were becoming increasingly slow. After migrating to Grafana, we noticed a significant improvement in query speed.
- **Open Source Compatibility**: We wanted to utilize OpenTelemetry while still using Fluentbit and Micrometer.

### Goals of the Migration

- Maintain reasonable cost and value.
- Avoid managing our observability infrastructure ourselves.
- Ensure there were no surprises during the transition.
- Keep our 6 million syncs running reliably.
- Provide a single solution for logs and metrics.

## Strategy and Execution

We evaluated three solutions, one of which was Grafana. During planning, we estimated each task for every solution, which helped us understand the scope of the migration.

We made a strategic decision to run Grafana and New Relic in parallel for 30 days. Additionally, we developed training focused on logs adoption since we anticipated it could be a sticking point during the transition.

### Planning Example

Here’s a brief overview of how we planned the migration. We detailed tasks in spreadsheets, estimating time for each task across the three solutions.

### Execution Steps

1. **Lead Team Assignment**: We designated one SRE team as the lead for the migration.
2. **Task Ordering**: We carefully sequenced tasks, starting with migrating alerts after metrics.
3. **Parallelization**: We broke down estimates into smaller tasks to allow parallel work across SRE teams.
4. **Expectation Setting**: We prepared for the possibility of running both systems in parallel for up to 30 additional days and communicated this to all involved.

### Training and Support

- A multi-level training strategy was implemented for Grafana.
- Shared Slack channels were established for real-time support and training.
- Our Grafana account team provided continuous assistance, answering a multitude of questions throughout the migration.

## Timeline

We set a clear timeline for the migration: starting on August 5th and completing by October 5th. This was an ambitious goal, but we committed to it.

- **August**: Begin migration.
- **September**: Push telemetry logs, metrics, and migrate alerts and dashboards to Grafana.
- **October**: Shut down New Relic and remove user access.

## Lessons Learned

1. **Using Standards**: Streamlining logs and metrics into multiple systems made the transition smoother.
2. **Fix Existing Logic**: This migration gave us an opportunity to clean up metrics, labels, dashboards, and alerts.
3. **People Problem**: The biggest challenge was ensuring all teams adopted the new system without interrupting operations.
4. **PromQL Learning**: We should have invested more time in learning PromQL upfront to facilitate smoother query creation.

## Conclusion

In summary, we successfully completed the migration in about 60 days. Although some tasks took longer than expected, we focused on the migration without getting distracted by cost management during that period. Today, we have a predictable solution with Grafana and a satisfied support team that benefits from improved log query performance.

We're applying the lessons learned from this migration as we tackle other projects, including a recent transition to Jira for project management.

Thank you for your time! If you have any questions, feel free to ask.

## Raw YouTube Transcript

Hi everyone. My name is Mike
Gordon, VP of platform at Fivetran, and I'm going to talk
about how we migrated our
enterprise observability in 60 days. Has anyone heard
of FiveTran before? Oh, so we have a few of you
who've heard of us, of course, those of you at Grafana who we
work with. So a quick agenda, I'll tell you a little bit about Fivetran
and myself and then we'll talk about our infrastructure footprint,
like what did we actually migrate, what our requirements for observability
were, who the people involved are, what our strategy and execution was, and then lessons we
learned from the migration. So Fivetran founded in 2012.
We've been around for a while. We have 10,000 customers and a
little over 1200 employees and then offices around the world and our platform
engineering organization that includes four SRE teams that are located around
the world who are very involved in this migration. And so what do we do? So we sync data from about 600 different
sources to a few dozen destinations. So if you have any one of these sources
or a number of others with one click, we'll sync data over to data warehouses,
data lakes, and anything in between. Our motto is that we want to make
data as simple and reliable as electricity. You just plug Fivetran in and your
data sinks from point A to point B. So why do customers use our
product? We're reliable, we're fast. It's cheaper than paying
your data engineering team
to build custom pipelines so that they can spend their time
doing analysis or data science. We run about 6 million syncs
a day, which is in here. And so I'll talk about the observability
requirements on 6 million syncs because we do run a pretty big infrastructure
and we're scalable and secure, and so we sync data quickly
or we sync it fast or both. So before I move on, I'll
talk a little bit about me. So at our all hands we have a
segment called "Meet a Fivetraner". And so I'll give you the 30
second version. I learned
a program on an Apple IIe. I went to West Point,
majored in computer science, was in the Army for five years doing
mostly networking and communications, then worked for Northrop
Grumman for a little while, and then Cedar-Sinai in
Los Angeles. After that, I was at Google for about
eight and a half years, and along the way picked up
an MBA from Colorado State. I had a son who was born while I
was at Google and then was at Hippo, which is an InsureTech where
we used Grafana open source, and we were also a customer of Fivetran. So I kind of have experience with both
as a customer and then have been at Fivetran for three years
leading platform engineering. And so our platform engineering group, this is just a quick view of
our engineering organization. We have a few peer organizations
that build other parts of Fivetran. And then in platform engineering
we build the core and the base of Fivetran, so infrastructure,
core software, quality engineering, and we have
a performance engineering team, and then our SRE and operations
team. So that's how we're organized. And this project to migrate
was mostly run by our SRE team. So our infrastructure, what did we
actually need to monitor and observe? We run about 39 regions. Each region has a couple
of Kubernetes clusters. You can see the zoom on the left side
of our regional setup where we have a connector cluster where
we do the data syncs, and then a supporting services cluster. And then we also provide
buckets and tunnels in each region. And so with the 39
or so regions, this says 38, but we have one more now.
We probably run thousands of servers at any one time and tens
of thousands of pods. So it's a pretty big infrastructure to
observe and we had to switch it over. Our footprint on observability. Here's just a quick summary
of the kind of volumes. So things to note is
170 terabytes or more of logs. Logs and metrics are our primary
way that we run observability, but we also use synthetics/traces. And then we have a lot
of alerts and dashboards. We allow individual engineering teams
of which we have about 50 to configure their own alerts and dashboards. And so teams will run
their own operations as a franchise where they're responsible
for their components in production. And we do run a centralized SRE
on call as well as a backstop. And then we're working on profiles right
now so that we can profile our software in production.
So pretty big footprint. The people involved in
moving this footprint. We have about 30 SRE in our organization, 300 software engineers that are
scattered across about 50 teams and then 150 support engineers who
support our customers every day. And when we moved, couldn't miss a beat. And so these are the different things
these groups do. So our SRE team, they do pretty deep dives in
investigations as well as dashboarding and alerting. They also do capacity
monitoring and capacity planning. Our software engineers, they need to look into both logs and
metrics to fix complicated problems, and they do their own
dashboarding and alerting as well. And then our support engineering
group, they're pretty heavy logs users. They work with customers
to solve problems, and so they want to go through logs of
every single sync that's involved and understand what happened
and why did it happen, so we couldn't let them down as we moved. So the goals of our migration, we
moved from New Relic to Grafana. Our annual contracts for New
Relic were a surprise every year, both in the cost and then the pricing. And after I was at Fivetran for
two years in a row and after two difficult negotiations, we said, well,
okay, we need to move to something else. Cost efficiency is important to us, and we didn't know it at the time,
but we wanted faster queries. Our logs queries in New Relic
were slow and getting slower, and we realized this after we moved to
Grafana that our log queries were much faster after we moved and then
open source compatibility using OpenTelemetry. We still do use
Fluentbit and Micrometer as well. And so we wanted compatibility
as we moved to a solution. And so what were the goals of this move? We wanted some reasonable cost and value.
We did not want to run our observability infrastructure ourselves. We said someone else can
do it better than us. We don't want the headache of doing it. We did do a cost analysis and it is a
little bit cheaper to run it ourselves, but it comes with a whole
lot more headache, and that's
not something we wanted. That's not our core competency. We wanted a stable vendor and
long-term partner. No more surprises. It couldn't affect reliability. Those 6 million syncs needed to continue
to run and our support team needed to be able to support the 6 million syncs. And then we still wanted best in
class logs and metrics and a single solution for all of this. We didn't want to have to go from
system to system to system to look at what's going on with all
of our syncs. And by the way, if you have any questions as I'm going on, I'm happy to answer as we go so
that we don't run out of time. So our strategy, we
evaluated three solutions. Grafana was one of those three solutions. What we did as part of the planning is
that we estimated each task with every possible solution. So we did both
planning and evaluation at the same time. That led us have a pretty good idea when
it was time to migrate of what we were dealing with. We also decided when we chose Grafana
that we needed to run Grafana and New Relic in parallel for 30 days, and we needed to develop training to
hit the hotspots, especially logs. We knew. We knew that logs adoption
would be something that
could burn us if our support couldn't pick up the new log solution. And so this is an example
of how we planned. This is just an excerpt from
one of our spreadsheets. We had our different tasks
during our evaluation. We had all three solutions and we looked
at each task and estimated how long it would take. This is a
very generalized version, but we went more specific than this. So the execution, the one thing
we did is we assigned a lead team. We have four SRE teams, and we
said, one team is the lead team. This team is going to spend
most of their time on this, and this team's going to be responsible
for this move. We ordered the work well. For example, we knew we needed
to migrate alerts after metrics. And so we carefully ordered all of the
tasks to move to make sure that we could do this move, and we broke down the estimates
into really small tasks so that we could parallelize this across
not only the same SRE team, but have other SRE teams help, especially
during the night for our teams. We set expectations. We knew that we may need another 30 days
of running each system in parallel and we might incur more cost, and that was okay by us. And then we
also knew that querying our logs and metrics might be slower. We knew that our support team might need
more help and that we might need more of our SREs to be available. And then we needed to have a
multi-level training strategy. We needed to train on Grafana. We needed to provide ways to understand
what the difference between a New Relic query and a Grafana log query was.
Office hours and help channels. And the Grafana account team also
had a shared Slack channel with us, and so they answered question after
question. I think we peppered them with, I don't know, a few hundred
questions as we moved on. So they also helped us
finish this migration. Here's a timeline. This is basically verbatim of what
we told our engineering teams. We said on August 5th, we're going to start migration and we're
going to finish around October 5th. We kind of took the line in the sand
strategy with this and said, well, if we say it's going to be 60
days, we'll finish in 60 days. If we say it's going to
be 90, we'll finish in 90. So we set 60 days as the goal.
It was an ambitious goal, but we thought we could
do it. And so in August, we would start migration. In September, we would have all of our
telemetry logs, metrics, and everything else also
pushed to Grafana. In parallel, we moved all of our Terraformed alerts
and dashboards to Grafana during that. And so over time, we switched to Grafana as the primary
alerting solution by the end of September. And so we still had New Relic running
for reference, but we told our teams, you should really be using Grafana,
and our alerts are running on Grafana. And then we set a cutoff date for New
Relic. We pulled everyone's access the beginning of October and said,
well, now you have to use Grafana. All of our alerts are on Grafana. We still had New Relic
running for a little while, and it took us a little longer, but by October we were removing
users and shutting down our old solution. So roughly 60 days. This was the migration plan that
was communicated by our SREs. So the first thing they said
is we're pushing telemetry, then we're migrating Terraformed
alerts and dashboards. Teams that didn't Terraform their alerts
and dashboards would have to migrate them themselves. And we
told those teams that. We thought it would also give
them a chance to learn Grafana. And so they took that opportunity
to recreate some of their alerts and dashboards and leave some
behind. Then we'd shut off New Relic. And then we also have runbooks
and a Zendesk integration. So runbooks for our engineering
teams and then our support. What we did is we just have a for them
to click when there's an incident and it goes right into our observability tool. So we kind of did instant migration with
that by just switching the link over when it was time. And so that kind of put them into
Grafana instead of New Relic anyway. And so we set expectations with their
engineering teams. We told them, use Grafana asap. Don't wait because
you're going to have to use it eventually. We're going to shut off New
Relic and you won't have access. We told them to migrate your manually, migrate your dashboards and alerts and
to update your own service docs and runbooks. And so our engineering teams did this
as well as our centralized SRE team. And then we had a support plan for this. The support plan for making sure that
we could support this 60 day migration, which was ambitious, was
shared Slack channels. So our SREs had a Slack channel
with all of our engineers. They answered any question that came. And then we also had a shared Slack
channel with the account team. The account team provided live training. So we had a number of
live training sessions. PromQL is in some ways a black art.
And so we had to train both SREs and engineers how to use
it and how to do log queries. I told you about our Zendesk integrations.
So we just pointed those over. We maintained these internal
channels and we staffed them 24/7. So we had extra SREs on call. And
because we run four different regions, there was always someone up during
the day. We had office hours. So our SRE ran, I believe
it was multiple time a week, office hours that people
could sign up for. And at first they use them pretty
often, and then after a while, they stopped being attended.
And then the other thing we did, which was kind of a support plan, was we added some of our
senior support engineers into our evaluation, and we asked them to
evaluate the solutions before we started. And so we kind of got support buy-in for
what we were going to choose and how we were going to use it before we
actually started the migration, which helped get adoption in our support
team because that was the biggest thing we were worried about was logs. And then we provided a
number of training resources. These are all links that
go into our internal wiki. We have something called Fivetran Academy
where people have self-paced learning. We added courses in there and we required
everyone to take at least something. And then we had different articles, one
for just an overview of Grafana Cloud, how support uses Grafana,
how to use Grafana for logs. So a little deeper dive because
logs were new for us compared to New Relic. Query mapping between the two. So we actually had some side-by-side
queries to provide people, you used to do this, now you do this. And then how to use filters correctly, which was something
that teams got used to, but also helped us do really quick log
queries because once we learned how to filter, the queries went a lot quicker. So some lessons we learned from this. Using standards helped us because
we were able to just switch. It actually made the switch really
quickly because we could just stream our logs and metrics
into multiple systems at once. And so we kind of got a jump on migrating. We fixed existing logic,
so fixing labeling, we got rid of metrics, we changed labels, even dashboards and alerts we got rid
of. So it was a good time for cleanup. And so we reduced our
logs, metrics, dashboards, and alerts while we moved and it
let us clean house a little bit. And then the thing about
this observability migration
is it really is just a people problem. Our SRE team probably
could have switched in two weeks. The problem is getting everyone using
the system and our support not missing a beat and our engineers used to creating
dashboards and us not sacrificing Fivetran's reliability. And so that's really what took
the 60 days or a little longer. Then the last thing, which is a lesson learned that we
would go back and do is spend more time learning PromQL upfront.
PromQL is difficult. Hopefully with AI that becomes easier
because the AI can create your PromQL for you. But that was probably one of our
more complex parts of the migration, especially for our SRE team because we
have a few complex alerts in our system for making sure that we
can observe our syncs. So to sum up, we were successful.
We did make it in around 60 days. We had some things that took
longer. Doc cleanup took longer. We intentionally chose
not to manage our costs in that 60 days. We just
knew it would cost more, and then we reduced our costs
in Grafana as we went on. And so that's one of the
things we just chose not to do, which didn't distract us from
the main task of migrating. We solved our problems, our
cost problems were solved, our pricing and unpredictability
were also solved. And now we have a predictable solution
and a partner that works well with us and we're happy with where we are with
Grafana. Our support team is happier too. They really like the
logs query performance, and as they got used to the filters, they can do a query now that used to take
them 30 seconds and it takes a second and a half. And so our support team feels like
they can solve problems more quickly. And we applied these lessons
because we like punishment so much. This year we did a migration from our
old project management solution to Jira, and so we did learn some lessons
in another difficult migration.

