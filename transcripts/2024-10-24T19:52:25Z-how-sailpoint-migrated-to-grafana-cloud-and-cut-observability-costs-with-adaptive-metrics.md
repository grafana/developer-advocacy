# How SailPoint Migrated to Grafana Cloud and Cut Observability Costs with Adaptive Metrics

Omar Lopez, Head of Observability at SailPoint, discusses SailPoint's journey scaling observability with Grafana Cloud.

Published on 2024-10-24T19:52:25Z

URL: https://www.youtube.com/watch?v=VkrQQFPQu2g

Transcript: Thanks everybody. I'm Omar Lopez, and I am the head of observability
at SailPoint, and it's, it's actually really great to be
here today. Thanks for having me. That's a bit of a mouthful, that title, but here to just really
talk about our journey. Know we worked with Grafana a lot to
solve a lot of our scaling issues. And so that's what the talk
is about. You know, our, our journey and how it
went. A little about me. I've been with SailPoint for about four
and a half years now with 20 years of industry experience. I was a Unix
admin, moved into DevOps, you know, very common role. Live in Austin, Texas with my amazing wife and two
beautiful children. Austin's great; food, weather, maybe ObsCON will,
will make a stop there at one point. Soccer like I said I mean, if we were
in London, I'd be calling it football, but we're in US. And
yeah, I love watching it, playing it when my knees allow
it. And coaching my son's team. We are big fans of the, of the US
National team. Maybe one day they'll, they'll win us a World Cup.
Yeah. Yes. . I mean, the women have four. I mean,
we can't get one. Come on guys. And this is the team the
observability team at SailPoint. I just wanted to give
'em a, a shout out. Gosh, I wouldn't be up here without
them, without their hard work and, and dedication they bring in every day. We really want to give the, our engineering teams the best
experience that they can to do their, to do their jobs well, and while keeping the lights on on the
infrastructure side. So my agenda is, you know, who is SailPoint if
you're not familiar with it. I'll give a quick rundown. Our
first challenge, rising metrics. We're a hypergrowth
company, and, you know, where we getting a flood of metrics
and, you know, what did we do? I'll talk about our DACI, which is our decision making
framework that helps us make complex decisions. And then our second challenge was
reducing the volume because it's just too much, right? And then I'll talk
about where we are today and, and where we're gonna
go in the future. So, if you're not familiar with SailPoint... SailPoint is the category leader in
identity security and provides a leading identity security platform that manages
and secures access to applications and data, enabling the world's most complex and
sophisticated enterprises to protect against identity centric cyber
threats while enhancing efficiency and supporting business transformation.
I memorized all that by the way. Since I've been there, we've, we've
gone undergone so much growth, and with that growth comes challenges.
So what's driving this growth? We're signing up new customers, we're
writing new features, new microservices. We're opening up new
regions, having acquisitions, and all of this is just really
adding to our telemetry, our, our observability platform.
But before I get to the answer, I wanted to start off with a little
analogy where my Skip-Bo players at? Anyone out there play Skip-Bo
one, really two . I know I, I didn't play as a kid myself, but
I've been playing with my kids lately. And as we were playing it, it
just kind of reminded me of, of how we were scaling Prometheus. So just real quick the rules of Skip-Bo, the goal is to let's see.
Did that work? Okay, cool. You want to get your build pile you want to get rid of that first. So the way you do that is to throw
it on the stack pile here, or, yeah, this is a stock stack
pile, sorry, stockpile, and you want to put it on your build pile. And the way to do that is through
sequential orders. So that six, that the, the player on the right will be
playing the six top of the five. Then they'll play the seven,
then they'll play the eight, and so on and so forth until
you hit 12. And once you hit 12, that's kind of your limit that, that's
where the cards end and that pile is, is gone. It's removed. And that could
happen to your Prometheus server. When you scale up and up and
up and up, you hit the limits. And that's what was happening to us. We
were hitting the limits of Prometheus. We couldn't scale any higher.
And so here's the journey, and I want to go back
to where it all started. How Prometheus and Grafana
got started at SailPoint. It actually was an intern project.
We were on another vendor, you know, prices changed, some other factors happen,
and we gave it to an intern and say, "Hey, stand this up. See how the engineers
like it." Well, they loved it. We, there was so much adoption by the
time I showed up a year later, we were running it in production and
we were off that previous vendor, and that was going well, going great. And we started to hit the growth,
the hypergrowth stage, and we were, like I said, going higher and
higher in AWS instance types. And we couldn't scale any higher.
And so we moved to Cortex. Cortex solved a couple of things
for us. The first thing, obviously, we're able to scale horizontally. The second thing we solved our single
it, it gave us a single pane of glass. Previously we had Grafanas
in all of our regions. Now we could have one Grafana
to pretty much rule them all, which was huge for us at
the time. And that was, and that worked well for a
while until issues happened. Performance issues, you know,
we're, we're still scaling, right? Long range queries started to error out. And what do you do with performance
issues? You throw money at it. And so we we're throwing money
at the problem and, you know, increase those ingestors. And
at the same time, we just, we started to spend a lot of
engineering time on maintaining it and supporting Cortex. You know, we couldn't get to those
higher priority initiatives. And it was about this time that Mimir
came out. Grafana released Mimir. And so we really were at a
crossroads. Do we move to Mimir? Do we try to figure out
Cortex and stay with it? Was Cloud an option or perhaps another
vendor? Were they even an option? And so we really were at a decision point. Enter the DACI. So the DACI is
something we use at SailPoint. It's not a new concept, but it's a decision making framework
that SailPoint engineering uses to make large, complex decisions
involving multiple stakeholders. So just going over the framework real
quick. The driver, the D is for driver, they're, they're really
pushing the DACI forward. You really don't want it to stagnate.
You want that driver filling it out, getting corralling stakeholders,
setting up meetings, really driving to the due date. The approver obviously making
the decision. Ideally, you, you want one approver you can
have a, a group approving it, but you really want that, that single
person making the decision. And they, they're the ones to listen to the
pros and cons of, of everybody. And, and they make that final decision.
And once that decision has been made, it's very important to,
to, you may disagree, but everybody commits to that decision. Contributors, you know, they, they
could be subject matter experts. They help the driver with information
that they, that they may have. It could be another engineering team
that's, that's saying, "Hey, you know, don't, don't forget about me. Don't
forget about my use case. You know, I want to have my, my say in there
as well." And then the informed. Teams that may be
affected by the decision. We want to be very transparent with
everybody so that there are no surprises. So what does it look like? It's it,
it could be a Confluence doc or a, a Google Doc, whatever. You use
it in your office. And let's see. So it's pretty much, you know, all the personas are listed up here
with a due date. Very important. And what happened, pretty much all the information
they need to know about list, list out all the options,
the pros and cons, you know, just an essential place to
everyone can, can contribute and, and see what's going on. Another great thing about
the DACI is that posterity. New people join SailPoint all
the time. And when they join, maybe they have a question of
why are we using such software? Or why was a certain decision made? We can always point them
to the DACI and say, look, this is the decision we made at the
time with the information we had, and this is, this is why
we're using what we're using. And it's it's extremely
helpful in that case. Another important thing is, is to
not stay stagnated in that decision. There could be several reasons why
it makes sense to open up a new DACI. Vendor stops innovating, or they're
not listening to your feedback. Maybe there's a new player in the market.
Costs have changed. You know, don't, don't, don't just think that decision is
what you have to stick with. You know, stay stay opening up new DACIs. So back to our Cortex DACI, what
were we looking at? What were, what were our prerequisites. Cost I mean, it's obvious. Costs have, have
been important in the past, will always be important in the
future capabilities. You know, what did Mimir offer? What
did cloud had to offer us? Was there another vendor that had
some features that nobody else had support? Very important to us. We, we've
always had great support from Grafana, even while we were on
open source. Maintenance. This was a big one. Was Mimir easier to maintain than
Cortex or something like Cloud, where there really wasn't much
maintenance was a very important. Then a customer reference once
it got down to the final two, we wanted to hear from their customer,
from a customer, you know, what, what did they have to say about their
experience? So where did we end up? , Grafana Cloud,
obviously. Cost they, or on all these things,
they, they really hit cost. It was actually cheaper to run in Grafana
Cloud than we could do in open source. We weren't expecting that. Capabilities, Cardinality management
dashboards, Adaptive Metrics, and a lot of performance
gains were huge for us. I'll get to that in in a moment
here. Support., You know, when we were in open source, we met
with Grafana all the time, and, and, you know, they were just
passionate. They, they just, they really wanted us to be
successful. And, you know, I, I look fondly at those moments where it
was just open source and it was just, you know, it was good times. And I,
I thank Grafana for all the support. Maintenance. There was very little
to no maintenance. You know, we let Grafana handle all that
complexity that we were handling. We could spend that time on
higher priority initiatives. And we did speak with a customer
and they gave a rave review. So this was our Cortex architecture.
It's, it's actually the, the reference architecture. But we ran
it pretty much exactly like you see. And it's it's a little complex.
So that was before going to cloud, and now it's much simpler
architecture again. It, it is a reference architecture
from Grafana. But again throw, throw a couple more
exporters in there. And, and that's pretty much
how we run it internally. We let Grafana handle all
that complexity in the cloud. So that brings us to our next
challenge. Now that we're in cloud, could we now leverage the tools that
Grafana Cloud offers to reduce the cardinality and the metrics? And the answer is absolutely
we could. The built-in, out-of-the-box cardinality
management dashboards, we were able to take those and work with
our engineering teams on reducing their cardinality, pinpoint where they could
reduce. And, and they helped us a lot. Adaptive metrics is not going to lie,
is is really the star of the show. You know, being able to drop metrics
that aren't being used by anybody, and we're paying only for the
metrics we value brought us, allowed us to drop from 75 million active
series to 50 million active series, a 33% reduction. We were early adopters. And we actually have a success
story with Grafana and a blog post, if you wanna check that out. It goes into much more detail
about how it all came about. And that was last year. Last
year was a 33% reduction. We continue to run Adaptive Metrics, and today we're down 50%. It it just, it's amazing. It is truly amazing. So what did we learn about
through all that process? SaaS can be more cost
efficient than open source. This this totally went against
everything we had assumed before. We could spend more time on
higher priority initiatives. The project where we were able to work
with engineering on their cardinality, that, that, that wouldn't have happened if we were
just maintaining our infrastructure constantly. It was a projects like that
where we could stop cardinality at the source instead of dealing
with the outcomes. And finally, we could reduce metrics while we
continue to grow. You know, we, we we're still starting up new customers,
we're still writing new features, new microservices. We're
still opening up new regions. All that growth is still
happening, but at the same time, we're reducing our metric count,
which it blows my mind how, how, how it happens. So what's next? You know, we've been busy since then.
We've run a ton of DACIs, now in Grafana Cloud, where we have access to all these tools
that so we're checking 'em all out. One interesting to note on here is, is k6. k6 was a completely
different team from ours. That was the performance engineering team. They ran a DACI and they came to the
conclusion that k6 was the best tool that they evaluated. And that came in handy when we
ran our Grafana Synthetics DACI because it, it's worked so well together. Our use case was really relatively simple there. There was some low traffic in some
areas that wouldn't trigger alarms, would have a low quality SLOs. So we
just needed some, some synthetic traffic, keeping those alarms up. That, that was
our, that's our base case right now. We know it works really well with k6 and
we are going to do a lot more advanced testing in, in the weeks
and months to come. Grafana Asserts, this is a DACI that's actually in progress
right now where we're taking a look at it. We've met with Manoj. We, we do have some internal
tooling monitoring our, our in our services internally. But it, there's much to be desired.
It can be improved a lot. And when we saw Asserts come out
last year it was very intriguing. And so we're kicking the tires
on that. Last thing for me, I want to invite I take it you all like
conferences and so I want to invite everybody to our conference, which
is next month, Navigate in Orlando. We will be releasing our, our
latest and greatest stuff. We'll have hands-on workshops as well, and you'll get to network with
identity experts. But that's my time. If you have any questions, I'll be around. But thank you very much for your time.

