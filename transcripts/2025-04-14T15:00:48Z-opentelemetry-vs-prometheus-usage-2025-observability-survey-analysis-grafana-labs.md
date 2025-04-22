# OpenTelemetry vs. Prometheus Usage: 2025 Observability Survey Analysis | Grafana Labs

Myrle Krantz, Director of Engineering at Grafana Labs, talks about vendor lock-in, OpenTelemetry vs. Prometheus, open source ...

Published on 2025-04-14T15:00:48Z

URL: https://www.youtube.com/watch?v=XeU7onUlUK4

Transcript: Hi, my name is Myrle Krantz. I really love talking about open
source and this is my opportunity to explore the observability
survey. This is a free report. It's based on 1,255
responses that Grafana Labs collected by outreach to our community.
This is the third one that we've done. We're going to keep doing them and you'll
get a snapshot of how organizations approach observability today, where
they think the industry is going, and maybe you'll learn something from
this and contribute to it the next time round. As you look at this in
the context of open source, you're probably going to start
by looking at the top concerns. You're going to see that there's a wide
variety of concerns that we asked people about. More noise to signal ratio. The challenge between
the noise and the signal, like finding the most important pieces. The complexity when you're
trying to set these things up, the costs the vendor lock-in
convincing management of value. I was looking at this
trying to understand, now
open source isn't mentioned as one of the top concerns here.
It wasn't offered to people, but you'll notice that a couple of
these things do play in to open source concerns, and one of them is costs. A lot of people think of open source
as free. It's free as in puppies, you still have to feed it.
There's also vendor lock in here. This is really relevant for open source. A lot of people end up
choosing open source, not because they're religious zealots
about open source because they want to be free of being forced to
decide for a specific vendor. They want to be able to
switch between vendors. They want to be able to use that to price
pressure the vendors who are offering their products. There's also convincing management of
value and predictability of costs and getting adoption within my organization.
This last one also is relevant for open source - getting adoption within your
organization because oftentimes open source projects, especially foundation open source projects
are things that people have used at other companies when they
change between companies. And getting people to use something that
they've already used is always easier than getting people to use
something completely new, even if the new is better in some way, if it's something they're familiar with
and they know the ins and outs of it, they're more likely to want to use that. So decision makers are starting with
these top concerns and then they're going and they're breaking them
down into selection criteria. And so we also ask people what are
their selection criteria when they're choosing an observability
product. Again, we see cost, we see ease of use, we
see interoperability, we
see based on open source. And here what I found
interesting is that based, based on open source was
fairly far back in the list of selection criteria, but that doesn't mean that people don't
care about open source. And what that means is that they, or at least what I think that means is
that they understand that open source isn't a concern by itself. Open source is a way of achieving
certain kinds of concerns. Open source is a way of
achieving a lower cost. It's a way of making it easier for your
users to learn the technology sometimes. It's definitely a way to improve
interoperability with other technologies because open source often
pairs with open standards. We're going to dig down into
that a little bit more later. And open source historically has not
had enough designers engaged with those projects because open source
projects are often pieces of a larger product. And also because the
engineering systems around open source are not necessarily well
designed for creating engagement among designers, this can make open
source projects harder to use, and it's actually one of the things
that tends to work against open source product adoption.
Also, one of the things we see, there's a lovely paper from Baldwin and
Clark about how architecture drives the economics of open source. We see that these economics of open
source often drive a certain amount of fragmentation of the solutions. Like people take a product and they
break it out into individual projects and they compose those projects into something
they sell, but that's the product. The projects themselves
are not necessarily very usable all by themselves. They have to
be composed with other things. Again, that pushes against ease of use, but it pushes towards more flexibility
and more interoperability with other tools. Interesting sidebar too is
we noticed in this survey that a lot of people are using a lot of
different observability technologies in their companies. The sort of medium mean
was around four different observability technologies, but we had people using as many as a
hundred observability technologies and similar the data sources, these are often also open
source technologies people
were using a lot. This is being driven by some
of the same economics. People are using solutions
that are open source. People are creating solutions that
are open source for a wide variety of different problems. These companies are then
taking these data sources and putting them together and creating
their dashboard boards to look at them. So one of the great things about Grafana
is it makes it possible to manage this very fragmented technology landscape, and this is part of the reason why
I think that Grafana is so powerful. And in this case, you've got open source sort of easing
adoption by making it easier to view other open source projects. We've got
this virtual cycle going on. Another thing that open
source does to ease adoption, I actually saw this at an insurance
company in Cologne a couple of years ago. Sometimes there's budgets, right? People have a budget for their
observability tool, whatever it is, and then their developers start to run
up against those budgets and they want to solve that problem. And the easiest
thing for them to do is to take something that's free. So they install Prometheus
and use Prometheus and start creating solutions around that, and they don't have to go
through a decision maker for
that because there are no costs involved. For more
sophisticated decision makers, though, this is strategic, right? They're picking open source software
because of the avoidance of the problem of vendor lock-in. What
does vendor lock-in mean? And this is something that I
keep hearing people saying, we don't want vendor lock-in. We don't
want to use project or product X, Y, Z, because there's some sort of vendor
lock-in associated with that. Different people mean different things
when they're saying this, right? Let's take a couple of projects
as examples. Prometheus. Prometheus is a foundation
open source project. When people use Prometheus, they can assume that even if one of the
companies that's working on Prometheus goes under or changes
focus or otherwise stops contributing to Prometheus, that Prometheus will continue to be
a viable project. So when people say, I don't want vendor lock-in in the
context of something like Prometheus, they're saying, I want to be able to continue to use this
project regardless of what happens to my vendor of today, but it can
also mean other things, right? So OpenTelemetry for example, includes a strong component
of open standards. Transport
protocols are defined. Semantic conventions are
defined. When people say, I don't want vendor lock-in in this case, they could be saying that I want to be
able to combine multiple solutions from different vendors because these standards, the transport protocols
and the command semantic conventions, these make it possible to make
these pieces interoperate. The foundation provides continuity, but the foundation also provides a place
where all of these different vendors can collaborate and make a higher quality solution potentially, but potentially
also a slower moving one, right? So there's also these risks around this. If you're insisting on a
vendor neutral solution, that could mean that you're
going to wait a long time for the vendors to agree on something.
For all of these things, you're going to end up paying for
support because while the code is non-rivalrous, you can copy
code as many times as you want. I create the code once and then you can
use it and you can use it and you can use it, and none of that
impinges on each other. People's time is a rivalrous resource,
so people are going to run out of time. That's why you need to pay for it so that
you can show that your support request is more important than that person's
support request because you're willing to pay for it and the other person
isn't. So vendor lock-in, avoiding vendor lock-in doesn't solve
all of your problems. You still going to have to ask for help. Alright, so let's drill down into some of
our specific open source projects. We've got OpenTelemetry adoption, and
we also asked about Prometheus adoption. I found it really interesting here
that people who are using OpenTelemetry exclusively are also using
Prometheus exclusively. That tells me that people are not
seeing OpenTelemetry and Prometheus as mutually exclusive technologies. So you can use nothing but OpenTelemetry
and still also use nothing but Prometheus. I think that's a good thing
because they aren't mutually exclusive. One thing we also noticed here in
this survey for both OpenTelemetry and Prometheus, roughly 50% of the respondents claim that
they're using these technologies more than last year. Again, these gross trends
are reinforcing each other, I think. They're not excluding each other. People aren't treating Prometheus
and OpenTelemetry as competitors, and that makes a lot of sense too
if we look at what the Prometheus and OpenTelemetry communities are doing. The Prometheus community in 2024 at their PromCon came to the
conclusion that they wanted to make Prometheus the default choice
to store OpenTelemetry metrics. There's a nice little blog post on
that too that Goutham and Carrie put together. OTel support was also one of the core
features for the Prometheus version 3.0 that was released in November 2024. There's still a lot of specific problems
that the Prometheus and OpenTelemetry communities need to resolve in order
to make that compatibility better, but they're working on it and
they're making a lot of progress. And so this increase in
usage that we're seeing here, an increase in interest that we're
seeing here between both Prometheus and OpenTelemetry makes a lot of sense and
all of the signals also go towards people continuing to increase that. So if we
look for example at the Google trends on searches for OpenTelemetry, we
just see that increasing over time. Now if we look at the survey results here, we're also going to see that
it's not as mature as Prometheus. So we've got, if you look at
people just using it in general, the trends are roughly the same
for Prometheus and OpenTelemetry, but there's a lot more Prometheus
users using it in production and more OpenTelemetry users using it, investigating it, or they're using it in a
sort of a proof of concept. Let's end this conversation on one last
mystery that I would like to see as exploring more in the next survey. If we look at the use of open
source and the use of SaaS, I was very interested to see that we've
got self-managed only and open source only here being kind of the largest
bucket of our survey respondents. This tells me that for some reason, and I have a couple of theories what
the reason might be. For some reason, open source only and SaaS only are
not being seen as mutually exclusive. What this tells me is that are
seeing these things as somehow, at least some of these people are seeing
these things as somehow complimentary. They are possibly, one possibility, is that they are treating SaaS that deploys open source technologies
as open source only, or another possibility. They care about what they're deploying
on their own infrastructure and they want to pair that with SaaS
and maybe they care, maybe they don't about whether
or not the SaaS is open source. So what I'd like to see in the next
survey is for us to drill down in that and figure out, do people care
that their SaaS is open source? It's possible they do. Maybe this is
providing a migration path for them. If they're looking for vendor neutrality, then they're achieving
it maybe by saying, okay, well we're using this vendor
now, but if we have to, then we can deploy the
technology ourselves and migrate. Or maybe they're saying, okay, well as
long as we are deploying open technology, open source technology on our
infrastructure with open standards, then we can take those
ingestion pipelines. I'm taking
in my observability data, and we can take those ingestion pipelines
and we can point them to another vendor. I would love to
know the answer to that. Maybe we'll find out in it's
time out, but enough from me. Why don't y'all go and check out that
report and also the interactive dashboards and drill down on it and maybe you'll
discover some interesting things and share them with each other as well.

