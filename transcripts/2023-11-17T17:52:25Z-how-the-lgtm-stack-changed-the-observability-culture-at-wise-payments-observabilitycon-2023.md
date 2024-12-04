# How the LGTM Stack changed the observability culture at Wise Payments | ObservabilityCON 2023

The observability team at Wise Payments – Europe’s leader in cross-border money transfers – had long provided the company’s developers access to a multitude of tools. 

But as costs and complexity increased, Ibukun Itimi, Engineering Lead for Observability and Andrew Brown, Reliability Squad Lead, saw an opportunity to change not only the tools they were using, but also the observability culture. 

In this session, Ibukun and Andrew highlight how the Grafana LGTM Stack empowered their team to become more product-focused and shift from being external tool wranglers to providing in-house observability expertise.

Chapters:

0:00 Introductions
0:43 About Wise Payments
1:42 Wise Payments' architecture evolution
4:44 The challenges that needed to be addressed 
7:17 Wise Payments' thought process in selecting a new approach
10:53 Building a true platform for Wise Payments' engineers
14:37 Measuring value 
16:10 Creating a great user experience for engineers
17:50 What's next? Thinking about the future of observability at Wise Payments 
20:25 Excitement around future Grafana offerings 
23:21 Learn more about Wise Payments' engineering team

Published on 2023-11-17T17:52:25Z

URL: https://www.youtube.com/watch?v=RSTb8IW4v74

Transcript: Hi, everyone. So yes, today our talk is going to be about how
the LGTM stack changed the observability culture at Wise. So my name is Andy. I, so the, the question was,
where are you from? So, England, it's not very exciting. So
things, things that I like to do. So about once a year, I really like to enjoy going to watch
a day of test cricket at Lords which is a cricket ground. I'm
the squad lead at Wise, and I've worked there for just
over four and a half years. And on stage with me is. Hi, I'm Ibukun. I'm from Nigeria, and during the weekends I'm typically
working on building my community or finding the next adventure. Cool. Thank you. So yeah, we're both from Wise. At Wise we have a very clear mission.
This is Money Without Borders, instant, convenient,
transparent, and eventually free. So Wise was found in 2011, and we specialize in
cross-border payment transfers. So we currently have approximately
16 million customers. We move over 9 billion GBP in
cross border volume per month. We allow our customers to move
their money in over 50 currencies, and we've grown to over 5,000
employees. And within that 5,000, we have a engineering
function of about 800 people. So the talk today, we're going to go through the
origins of observability at Wise, the journey that we've been on, and then
talk a little bit about what's next. So first, some, some context. So the Wise technology journey will
have a very familiar feel to it. It started out as a monolith
hosted in a data center, and as new services were added
when the company began to grow. And monitoring was originally provided
by leveraging tools such as Zabbix, Graphite, and a vendor. Over
time, additional tools were added, and these were to cover things like
measuring our uptime availability, some synthetic testing, managing on-call. And these additional tools were there
to make sure that as we were growing, we made sure that we
could identify our issues, that we could be notified of them
and ultimately go and fix them. And this was working
pretty well for a while, but Wise kept growing and growing and
that speed of growth meant that the company had to rethink their architecture
and how it was hosted and the outcome included as expected, a move to the cloud. We also did a bit of a fast forward and
decided to change and go all in on the microservice architecture,
leveraging Kubernetes and containers. So what did that mean for
our monitoring stack? Well, the change of technology required a
different approach and gave us a chance to review our tooling and our
approach to monitoring and logging. This is what I like to think of as the
beginning of the observability journey at Wise. So we began by creating a team, and we called that team Observability
and it had a very clear mission to make wise observable. So first we changed our tooling to
reflect the new and growing requirements. We phased out some of the original tools
and replaced them with Prometheus and Thanos for metrics. We added
in Alert Manager for alerting. We increased our footprint
on Elasticsearch for logs. We productionized our Grafana
offering for dashboards. We added in Jaeger for tracing
all of these new offerings, gave our engineers greater visibility
into their into their services. Secondly, we decided
to instrument the code. So we created a library and we unified
the data that was being emitted from these various services, and we tried to ensure that
we had a standardized format
as all this data flowed into our new observability
stack. And thirdly, we pushed for adoption and we did
this via Tech Talks, documentation, day-to-day support, and also starting
to provide some dashboards for free. And over a couple of years, we had our product teams using the new
suite of tools and Wise was becoming observable. But our story doesn't finish there
because Wise continued to scale fast. And as Wise grew, the Observability
team were faced with three challenges. These were: the volume of
data, the maintenance burden, and the deteriorating customer experience. So let's quickly go through each of these. That's a very bright slide. As Wise grew, so do the demands of the observability
stack, and it meant more data, more queries, increasing diversity
in data sets. This meant more alerts, more metrics, more logs, more new use
cases from new parts of the business. This graph here is of our service
growth over the past few years. And as you know, each new microservice
has a data footprint and additional cost. The challenge the team was facing
as we're starting to hit limits, we needed to regularly
scale our resources, or we needed to begin sharding the
different data sets. In addition, the latency of getting all of that
data from ingest into storage, sending back to our
customers was increasing. And we had to do things like starting
to reduce the number of open indices, reducing retention and
increasing aggregation. Second challenge that we were facing was
new accounts and new environments were being added often, which meant more deployments to
maintain and a longer and increasingly upgrade cycles. We had to replicate our infrastructure
and right size each resource. And for the team, oncall was
becoming a full-time role. And thirdly, whilst we continued to meet our original
objectives of making wise observable, the actual experience of our engineers
when using the stack wasn't ideal. This slide from earlier was highlighting
the key tools that we transition the company to, but we also had additional
tools for on-call, for error tracking, synthetic testing, profiling, uptime
monitoring, database, querying, frontend tracking. Ultimately, all of these distinct tools will start
to increase the time it was taking to restore during an incident. An example here is an alert
from your oncall system, or maybe you got your alert via Slack
and then you went to your dashboard, or maybe you went to your error
tracking and then you went to your logs. We actually ended up with 15
distinct UIs for our engineers. And this led to context switching time, wasted hopping from metric driven
alert to a log to get trace ID. So efforts in the team began to focus on
joining the dots together and creating a more seamless experience. But rather than try and solve each of
these three challenges individually, we decided to pause and we asked ourselves
was it time for a different approach? And with that, I'll hand over to Ibukun. Alright. All right. Thanks Andy for walking us through
the team's journey until now. Obviously a lot of work has
gone into observability at Wise, but we really needed to think about
what was next. And so at this point, we took a step back to evaluate
what was important to the team. And it came down to a few things. We
wanted observability that was open source, cost efficient, scalable, but most
importantly properly supported. And we wanted to create a unified
experience for our engineers. We wanted to give them things
like observability out of the box, alerting dashboards that make
their experience a lot easier. And so Grafana was easily our tool
of choice. Through our journey, we've worked with the Grafana engineers
to make sure that we're making the right decisions in our implementation. We've really seen them as a partner
that have supported our growth. We obviously have a large volume of data, and so we looked at the fact that one, we're using S3 as our backends, meaning
that as we continue to grow our data, our cost doesn't scale exponentially. And then because Grafana is so
dedicated to evolving the product, we knew that as we continue to grow and
as the industry continued to change, we would have a partner that will
support us through that journey. And so given our decision to go open
source with Grafana as a partner, we dubbed our mission building becoming Wise's observability vendor.
And it's not a term that we take lightly, but we use it to gauge our performance
and make and make decisions on what the team is going to be working on and how
we implement what we're going to work on. And so given the vendor model, you sort of think about a few things
that a vendor promises you when you're onboarded to them, they promise you that they're
going to scale as your data grows. They promise you that they're going to
give you a set of service offerings that, that have very specific values and usually
would have an SLA attached to them. And they also promise you some
level of user experience, right? And so these were things that we decided
to focus on on the team to sort of, you know, dictate how we continue
to evolve observability at Wise. And so throughout the rest of this talk, I'm going to talk through
these three things, what we're doing and what team plans
to achieve given these three pillars. So for scale, the question we've
always asked us, asked ourselves is, can we handle 10x? And that thinking obviously has paid
off because a lot of the decisions that the team made years ago is what
supports the data that we have today. But in truth, you can never really
support your future scale 100%. The most you can do is sort of make
decisions that make it easier to adjust as your data grows. And so even though yes,
we support the data that we have today, we're thinking what's next? How can we continue to evolve
and support Wise's scale? Our data continues to grow exponentially, and the data that you see is
what we process on a daily basis. And so this is just 2x
what we had last year. It's obvious that at every point when
we ask ourselves can we handle 10x, we are obviously not
very far away from that. So it's a question that we have to
keep asking ourselves because we know in a few years we're
going to get to that point. And so the team continues to
think about skill on a team level, but we are part of a larger
tribe platform tribe at Wise. And generally as a tribe, we're starting to think of how can we
provide a true platform to our engineers, a platform that comes out the box
with everything that they need. So we're working with teams like
our compute team, our connect team, CICD, cloud foundations to make sure that the
platform that we give to our engineers is well supported and is scalable and
supports what they need to do their day-to-day jobs. And so we're currently working on a
re-architecture of our observability infrastructure, and we're moving again towards this
vendor model that we've, you know, discussed. And usually, like there are few things that a vendor
would give you when it comes to how they collect your data and how
they present your data. They would give you a set of endpoints,
you would run a few commands, and you're able to get your
observability up and running. And so we wanted to adopt that model of
having endpoints that we use to receive data from wherever, you
know, whatever cluster, whatever piece of infrastructure in
such a way that our engineers don't care about what we do with this. We give them a set of commands or they
deploy their stuff to Kubernetes and out the box they're able to get
observability. And so we, and so given this endpoint model, the other thing that we wanted to
do was also to adopt Mimir, Tempo, and Loki. So we have a
migration from Thanos to Mimir, one because it also helps us to scale
how we manage our infrastructure since they're deployed, you
know, in similar ways. And so the maintenance problem that
Andy talked about earlier starts to get resolved because we're reducing
our infrastructure footprint, but scaling how we're able to handle data. And given the fact that you can scale
the different components independently, it means that our costs, you know, can also stay doesn't have to grow
exponentially because we're only scaling what we need part time and we're making
very efficient use of our resources. The other thing that goes with this is
that we're able to reduce our lead time from when someone says they
need observability to when
they become observable. Why? Because we give
you a set of endpoints, you send your data to us and
you have it up and running. The other thing we also have have put
into consideration is that usually when you send your data, you're sending
this data from different environments, and we want them, we want our engineers to be able to
interact with those with the data in intuitive ways. And so taking advantage of things
like multi-tenancy on Grafana side, we're able to present your data regardless
of where is coming from production, staging, sandbox in a way that makes
sense to the engineers to interact with. And I think one of the most
important pieces is the, is actually the migration from
Thanos to Mimir because again, we have huge volume of metrics and
have had issues with scale in the past. So making that migration, you know, is actually quite key for us to
continue to scale as our data grows. The second thing that we talked about
our service offerings and our SLOs. Usually when you're
implementing something, you don't want to just like implement
it because it's the newest technology on the market. You want to think about the value behind
why you're implementing it and what that means for your engineers. We want to make sure that not
only are we providing value, but we're also benchmarking our
performance by actually saying like, okay, we've provided this thing, does it
work for our, our engineers use case? And is it to the level of performance
that we want to be able to give? And so with everything that we adopt,
with the changes that we're making, we're thinking of how can we actually
measure value? So for metrics, how do we know that our users, you know, are able to query their data in good time? How do we know that we're
providing the right data as well? So we sort of did some work internally
to just go through the metrics that we have and see which of these metrics
actually depicts our user experience. And if we're able to measure that, it means that we can make
decisions based on we want to work on this this quarter because
we know that the user experience is terrible or this is the work that we've
done this quarter and we have improved our user experience by X percent. So being able to measure this value is
quite critical to how we scale as a team, because again, we don't want to be doing just like a
bunch of work and not having any impact on the business or not having
any impact on the engineers. And so measuring our SLOs is a practice
that we're adopting on the team to actually use that to prioritize the
work that we do. And where we, you know, place our focus as a team as well
is very critical for our engineers to be able to get visibility
into their system. So our reliability is really a huge part
of Wise's business and it's something that we take very seriously. And so
by being able to measure this, we, we know whether or not we're giving
adequate support to our engineers. The last thing that we have is
user experience. And of course, if we get the first two things right,
if we're scaling and we're, you know, providing value, we would have a
high user experience and high NPS, which we measure during
our engineering survey. But we didn't want to stop there.
We wanted to take our UX, you know, just a few steps further, the first
thing, which I think we heard a lot about, you know, in this conference is just
providing that one pane of glass. We wanted to, we want to, to reduce the complexity for
how our engineers find data and interact with their data.
But more importantly, we really want to chart a golden path. It goes beyond just having
all of your data in Grafana. It's like how do they connect? How do
you go from a metric to a log to a trace? How do you make sense of everything to
be able to really troubleshoot or really understand your system
performance? And so having, and so taking advantage of some of the
things that Grafana provides by linking, you know, the data between these three sources and
also exploring things like correlations since Grafana 10 are
things that, you know, we've been prioritizing to sort
of create this unified user experience for our engineers. The other thing is that this also
impacts adoption because the more engineers can use their data
together, the more they are, you know, incentivized to actually adopt new things
that we introduce to them as a team. And again, that sort of brings a sense of value
to the team who is doing the work, that we're not just
implementing new things, but we're bringing this new things as
a part of a lifecycle that enriches our engineers observability experience. Well, in a perfect world, if we had all of
this, our story wouldn't still be done. We still have more work to do. And so we think about the future and we
believe that even though we're making the right choices today, there's still a
few things that we need to think about, you know, in the future.
The first thing is culture. Wise's observability culture has
obviously evolved over the years as the team continues to evolve
our stack, our processes. But then there are a few things that
we factor into what we term culture. The first thing you have, your people,
your processes, and your products. Your people aspect sort of relies heavily
on your engineers' ability to use your tools and actually have best practices
that you as a team want to push. And so being able to like
work with engineers to really
solve their problems and to also work as partners
to be able to say, this is the observative best practice
and this is how we're going to enable you to follow it is quite important. I think it's very important to note at
this point that your people goes beyond just your engineering team. There
are other people in the organization, product managers, customer success,
that we, that can, you know, take advantage of the data
that you're collecting. Like we're collecting such
a huge amount of data, it makes sense to be able to use that to
impact the business across the company. The next thing that we
think about is also process. So how do we provide
support to our engineers? How do we ease the
onboarding process for people to be able to quickly and easily adopt
observability because that impacts how widespread we can go
across the organization and
it impacts the completeness of our observability as well. And
the final thing is the product. So for the product, you're thinking about how do we provide
a top-notch product to our engineers? Because ultimately if the product doesn't
work or doesn't fit their use case, then they're not going to
adopt it plain and simple. And so we want to ensure
that we're working, we're concentrating on our people process
and product to be able to provide and to be able to increase the adoption
of the observability culture at Wise. The next thing is the
evolution of our stack. Observability is a fast evolving industry. It's a fast moving world, and we know that with the adoption of
new trends or with the emergence of new trends, it improves how much visibility and how
much understanding that you're able to get into your system.
And so we think about, and so we have our eyes on a few
things that Grafana is releasing, and it's so exciting to be here and
sort of hear the future of the product because we know that even though
we're being cautious in our approach of introducing new things, because again, we're a financial company
and we're responsible for
people's money and it's not a responsibility that we take
lightly, but we know that, you know, if we don't sort of in a sense keep up
with what is available in the industry, we sort of start to fall back behind. And it means that we might
not be providing the best
product to our engineers. So we keep our eyes on these things
and as new things come up, we, we start to think of again, what is the value that this is going
to provide into our provide to our engineers, and how can we
bring this into our ecosystem? The final thing that we're thinking
about is balance. It takes a lot of work, you know, to maintain and build your own
infrastructure and your own observability, especially at Wise's scale. And so it's not lost on us that
there would come a time where our engineering our maintenance
costs, you know, starts outweigh what it
would cost to pay a vendor. And so we're keeping an eye on this
balance such that we know that the responsibility of being a
Wise's observability vendor
could potentially evolve to a place where we're doing
this in partnership with
a company that aligns with our value, our mission,
and supports, you know, what we want to do at Wise and how we
want to continue to grow our observability team, our observability tools
and our observability culture. And so some of our, you know, infrastructure decisions
today are actually preparing
us for a future where we partner with Grafana to
create this ecosystem of providing an observability
platform that's top-notch. While we sort of focus on like the best
practices and making sure that our team continues to evolve as our
observability is evolving. We're looking at things like
Adaptive Metrics, you know, that can reduce our cost. We're looking at things like anomaly
detection that helps us to really understand our data because our, our mission at Wise is really to provide
money without borders that's eventually free. And being eventually free, you know, the infrastructure costs
actually play into that mission. So at the point where we're, you know, thinking about these things or where we
sort of are faced with this question of, you know, build versus buy, the thing that we're going to be asking
ourselves really is that how does this support Wise's mission? And I think the, the direction in which Grafana
Cloud is going and you know, in what we've heard today, sort of helps us to maybe make that
decision a bit easier in the future. And so we think that this is a
future that's really possible. That brings me to the end of my talk. If you're curious about what we're
doing observability wise and engineering wise, you can definitely check
out our blog Engineering at Wise. So that's medium.com/wise-engineering. And if you find anything
really interesting, we also have a couple of roles. We have a number of roles engineering
and platform that you can check out as well on Wise.Jobs. And thank you so much for
listening to us today.

