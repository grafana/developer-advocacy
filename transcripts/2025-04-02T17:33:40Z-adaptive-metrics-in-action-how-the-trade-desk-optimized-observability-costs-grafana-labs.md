# Adaptive Metrics in Action: How The Trade Desk Optimized Observability Costs | Grafana Labs

Managing observability costs at scale is no easy task — especially when metrics volume grows fast. In this talk, Paul Givens, Head ...

Published on 2025-04-02T17:33:40Z

URL: https://www.youtube.com/watch?v=XgeaJmah31k

Transcript: My presentation is on Adaptive
Metrics or how I learned to stop worrying and love the button, the
button that I'm talking about here. I don't know if anyone's seen
the Adaptive Metrics feature, but there's basically a big button that
says "Save Money". And we like that. Alright, so we use Adaptive Metrics. It was easy and it saved us
a ton of money. Questions? So seriously, when the organizers saw
that three slide slideshow, they told me I needed to fill
it out a little bit more. So we'll add some context here. So what
is the Trade Desk? What do we do here? We're an advertising technology company. We help agencies and
brands target customers. Every time you load a webpage, there's a huge series of
auctions for your eyeballs, and we are the company or one of the
companies that bid on these auctions on behalf of our customers. To oversimplify things a bunch,
this makes us similar to a high frequency trading platform with massive scale. So a lot of people talk
about massive scale, but The Trade Desk more or less see
a vast majority of the traffic on the internet and we interact
with a large amount of it. So when I wrote this slide that was
around 18.7 million queries per second. But what does this mean
practically for observability? This means that we stretch every single
third party solution to the absolute limit. And just to give you context
there, we found bugs in AWS. That's the kind of scale that we got. So our team, the team that I'm on, the observability team is
called Service Excellence. We're not just responsible
for monitoring observability. We do incident management
and response as well. And we also manage a lot of our third
party contracts and integrations. Some of those include Grafana, we
have Honeycomb, we have Sumo Logic, and a whole bunch of suite of
other tools that we manage. This is another thing that
gives you context to the
amount of metrics that we're seeing in our system. I had to count out the commas there to
figure out how many series that we have, but that's like no joke, a whole
bunch of data that's 210 million. So what does our system look like? So as
far as observability goes with metrics, we have metal data centers,
we have Kubernetes centers, we have some cloud data centers, and each of those are running two
Prometheus nodes that ensures that we have very high uptime and all those
Prometheus nodes are working with an Alert Manager cluster that
we have running and that sends alerts to our internal alerting stack. We have something called Alert Gateway, which takes those alerts and enriches
them because we want to do more than just what Alert Manager does. We also have something called Monitoring
Adapter that takes our third party alerting systems and transforms them
into our own bespoke internal system. And we've just recently
moved to Grafana IRM, we moved off OpsGenie, and that is what we use to both send
alert notifications to our users and allow our users to view
those alerts as well. We also have our system
over here to view Prometheus metrics. That's in Grafana LTS. And you can see all of our
Prometheus nodes are writing to Grafana LTS. We also provide a monitoring platform. I know Grafana would love us to
have our alerts in their system, but we have so many bespoke custom
things that we've written a long time ago that our devs really love. So we have our own monitoring platform
that pushes rules into Prometheus to evaluate. We also wrote this nifty
thing called Metric Exporter, which takes database queries
and converts them into time series. And that's a very
useful tool that we built. So what do people use metrics for? A
lot of people kind of wonder like, Hey, what does your team do?
So we provide metrics. Every dev everywhere uses metrics, but it's especially useful when
we're testing new features. It's critical for our
alerting in our systems. But I would say if you had to
distill down to a single use case, one of our biggest use
cases is comparing our releases. So we release on a weekly
cadence for our main systems, and that means that we have
a test and we have a control. And then I wish I could say we
did something smarter than this, but we have a dev go through and look
at the test and the control data and say thumbs up or thumbs down
as far as the release goes. So on SC, what do we spend
most of our time doing? A huge amount of it is just
maintaining that massive scale, which is upgrading servers,
migrating to new infrastructure, and importantly protecting
our systems from Oopses, which is when you have, I think we're somewhere near
500 devs in our company now, at least once a week some dev will
write a query that just blows up our cardinality. And we have to stay on top of that with
all sorts of alerting to make sure that we're like, "Hey, did you really
mean to double the cardinality?" In our system, we also address costs, which is different than
those one-off. Oops. It's making sure that we are being as
efficient as possible with our money and building observability and response
tools to make our developers more efficient. Something we just
recently added was tracing. So we're always kind of building those
new tools as well. And as always, pushing for best practices
like we would love to sit, believe it or not, our team
is almost entirely introverts, but sitting out there and attempting
to train our devs on how to best use observability is a good use of our time. So what do we do here?
Some example projects. One thing that we've recently done
is we've pushed Gateway to OTel. If you don't know what Push Gateway is,
it's a way for transient jobs to send telemetry to Prometheus. And this was something
that was really cool. I don't know when we
built it five years ago, but this is starting to cause
a lot of problems. For example, there's delays between metrics being
pushed and the information getting populated. You can't use counters. There's no easy way to clean up outdated
metrics because they never expire and we're shifting to Otel anyway.
So what we decided to do was take our Push Gateway metrics and push
them towards the OpenTelemetry collector. And this was migrating a whole
bunch of old crufty batch jobs. And I'm sure everyone out here
knows that the most tech debt is always in those batch
jobs for some reason. So there's a lot of touching some of the
oldest things in our system and there's always, communication is key just talking to teams
and helping them understand why we're doing this. And this is the solution
that we came up with. So over here we have our
different instrumenting applications. We have to do both K8s and physicals
since we're in a transition period. And the way this works is we push
it to the OTel agent collector, we hydrate the metrics, we push
that to a gateway collector, and then Prometheus scrapes that we have
this thing right here called the skip agent that we built to a global collector
because the way that Push Gateway works is you had no sense of
the instance things were running off. So a lot of our backend dashboarding was
based on the assumption that we didn't care what service our job was running on. So we had to create a way to make it
look like our things are global. Oh, my laser pointer's gone. No laser pointer. Templated alerting is
another project that we did. So our company we're moving to
Kubernetes. It's been a very good move. The company
has saved a lot of money. It's made our devs more efficient. But one thing that we noticed when
we were doing that migration is that different teams were all building
their own system level alerts and queries into our system, which was making it very difficult
because there was no canonical way to find those system level metrics. So we needed
to figure out a way to be like, Hey, how can we make it as easy as possible
for teams to alert around their system level metrics and Kubernetes? So what we did is we added
a custom resource. (Oh, it does work now) a custom resource
so that they could get high quality system level alerts. And when you let devs
build their own stuff, when they have a ton of product pressure, you tend to end up with
terrible best practices. So this is one way that
we could be like, Hey, it's even easier to just add this custom resource. You'll get high quality alerts
and you don't have to write your own, you'll save time. And of course, we had to provide a mechanism
to override those defaults. So this is the way the system
looks over here to the right. You can see this is how an engineer
would override some of those alerts. They can set their own
thresholds for the alerting. They can set their own severity as well. And the way that it works is you
have those custom things over here, like the kube state metrics, which is a way that things metrics in Kubernetes get
populated to Prometheus. And then you have the custom
resource that we wrote down here, which has a k8s API, where you can have our rules over
here that we talked about earlier. They get populated into
those kube state metrics. So best practices, how
does our team operate? We run an operational health meeting. If
anyone has an observability team here, I have found this to be extremely useful. It's a great way for a team that has a
lot of moving parts to keep eyes on all those moving parts. It's also a forcing function to ensure
that we're keeping an eye on all the things that we need to keep an eye on. If it's something that happens once
a month, everyone's like, all right, I need to look at versioning. I
need to look at resource management. I need to look at the amount of
alert noise that we're generating. So what does that look like? We
can identify some anonymous usage. That's kind of the spikes that
we're talking about before We can take a look at
our alerts over time. This is our own custom dashboards that
we've written in Grafana. So I can see, hey, we're making less noise here, but why the heck is this
alert going off again? We also have our own SLOs. This is another thing that we built
before Grafana had their SLO product, and we like our internal thing a ton, but you can see in the operational
health meeting, we can review like, 'Hey, what are our systems that aren't doing
so well' and 'how much work do we need to put in to make them better?' So now
kind of onto the meat of the talk, we had a problem, and I realize
now my boss is in the audience. This presentation is about bad decisions
that I made, but it's after review, so I think I'm good. So up into the right is good, right? Nope, not when it comes to costs. This
is what our costs look like, which is bad. Those are big numbers.
It's going up into the right. So how did we go about fixing
that? Well, Grafana tried to help. They suggested that we use
Adaptive Metrics, but as
you'll see in a few slides, we didn't do that right away.
There's a myriad of reasons we run both self-hosted and Grafana Cloud. We were an early adopter of Grafana
Cloud, and for a lot of reasons, we wanted to use our own custom
backend solution that we were using along with Grafana Cloud, which meant that using Adaptive Metrics
wasn't as simple as just hitting the button. And here Grafana also offered
Professional Services to help migrate our system to Adaptive
Metrics. But we refused, and I'll kind of get into the
reasons that we did that later. But a main reason, and I'm sure all of you suffer from this
engineering time at The Trade Desk is super tight and we need to be
extremely intentional around how we spend engineering time. Grafana told us that we could save
an average of up to 40% with Adaptive Metrics, but I came in hot
with the smug and was like, you know other companies probably could
save that much, but we're on top of it. We run meetings where we
look into our metrics. I have devs go out and
investigate how much we're using various metrics. Maybe they
could get us 5%, that'd be great. And we really couldn't prioritize it because we had no clear
understanding of the return on investment, which is hard to do because you don't
know how much adaptive metrics is going to save you until you can hit the button
with our system. But a lot of people out there can probably, if you
just use Grafana Cloud, you can see how much
you can save right now. I joke that I went through a
series of phases of acceptance. If you know anything about psychology,
there's a bunch of different phases. So my first was denial. I kind
of talked about that already, but we have a good process to
detect high cardinality metrics. It couldn't save us that
much. And then there's anger, and I'm sure you've never gotten angry
at your devs. It's those damn engineers. If only we could get them to consider
their telemetry costs when they add metrics to our systems, then
there came into depression. I don't think we could
change the culture here. Devs have too much on their plate.
There's nothing that we can do. And then there's bargaining, which is maybe if I loan
out some of my team's time, we can drive down costs and
then acceptance, maybe I
should just hit the button. So eventually we found the time to do
that. Turns out problems you ignore, don't go away. And cost kept exploding. I transitioned from thinking that, 'hey, this increase in cardinality is a one-off. Team X is doing this team Y is doing this. Eventually we'll just level out.' And
then I came to the acceptance that, 'Hey, I think this is going to
continue going up into the right, so we need to address it.'
And our organization is also
migrating to Kubernetes, which I mentioned, which
saves us a ton of money, but it also exposed the cardinality
because of those system level metrics. So what did we do? We invested a little time to see
what Adaptive Metrics could give us. It required us to migrate all
of our internal dashboards
to the cloud version of Grafana. We had to migrate all of our globally
configured alerts into Grafana Cloud. Like I said, we have that custom alerting
monitoring platform. But all in all, this was a relatively short investment.
I think it took about two weeks, and I was like, all right, let's
see what it gets us. And holy shit! I didn't expect that big number. So communication strategy, after we
saw the number, we were really excited, but it's not something that I can go
do. I mean, I could go hit the button, but I want devs to understand
what's going on with their metrics. We explained why it's pretty easy to make
an argument when you see a number like that. But telling them
what exactly is happening, letting them know that we're not
permanently taking their metrics. They have the power to undo
any changes that we're making. And something that I've learned a while
ago is visibility is one of the most important things here.
Making sure that you send an email, making sure that you post on Slack, making sure you do this four or five
times because even if you do that, 10% of devs are going to be
like, what? I didn't know. So making sure that you're visible.
And I tell everyone, including my boss, very excited. But we ran into a problem. I thought I was being smart. I was like, I want to make this as
easy as possible for teams. I had a list of suggested
adaptive metrics to drop. We have a janky backend way to join
those metrics to teams so we can tell which teams are spending most of our
money. So I go to dev and I'm like, Hey, buddy, do you mind joining the
metrics to the teams so that I can just send a subset to teams? Can anyone see a problem with that?
I just touched all of our metrics. So we went from saving
a huge amount to it being like, Nope, every single metric in
your system is used do perfect, which is not great. I took
careful aim at my foot. The cool thing about this is we
absolutely know the feature works. We touched all the
metrics, it all went away. But Grafana came to the rescue
again with a top secret feature. You can see that they're like, oh
yeah, we only use this internally, but we'll turn it on for
you, which was super helpful. And we went back to cutting a
large amount of metrics again. So future work. I want to talk a little bit about
what we're thinking when it comes to telemetry. There seems to be a tension
in the observability world. Developers still care a ton about
these instance level metrics, even though we're migrating to
Kubernetes. People talk about cattle, not sheep all the time, but people still want to go in and see
what their individual boxes are doing. But that costs a ton of money. If you know anything about
cardinality that explodes cardinality, but they only care about
it for a very short time. So what options can we provide? We thought about three of them in our
system because we still need to save money here. The first one is federation. Our Prometheus servers provide
a variable three day lookback. This is constrained by
disc, so it can go up, it can go down depending on the load in
our system. And the thought was we could provide a light front end that provides
devs a centralized area to query any Prometheus server. The pros
of this solution is it'd
be super easy to stand up. The cons of this solution is it's terrible
user experience and devs are kind of okay with that. But the more important thing there
is we want more than three days, or the devs want more than a
three day look back window. All these options are bad, by the way.
Option two is streaming aggregation. So one neat thing that we thought about
is putting an agent between our nodes producing metrics and Prometheus that
aggregate on a specific label before sending it to Prometheus. And the cool thing about this is that
this saves us load on our Prometheus servers, which like I said before, is something that we're always looking
to do is relieve pressure off of our systems. But the cons is we lose
those instance level metrics all together, forcing devs to
opt out if they want those gains. So yeah, we might save on, let's say 50% of the
metrics in our system, but if devs are opting out
of a large amount of them, we're not going to see
what we really want to see. And our third option, and this is the
one we're probably going to go with, is medium-term storage. And this is where we're adding
another midterm storage. We're thinking Thanos right now that
Prometheus can do remote rights too in addition to our long-term storage. And then we can use recording rules
to compress those metrics that we're putting into long-term storage. So the developer can go to the smaller
midterm storage if they want to get instance level metrics, and they can shift to the LTS if
they want longer term storage. And the cool thing about this is that
customers get exactly what they want. But on the flip side, we found
Thanos to be flaky in the past. We're concerned about uptime, and this is a solution we don't think
we can continue to scale as we move into the future. So this
solution buys us time. It doesn't really solve
the problem permanently. So then we start thinking
about ultra high cardinality, and now we're kind of in la la land. These are ideas that devs spit out
without really thinking about them, myself included. So how do we handle the future
when devs want these super high cardinality information? But that's something that's
just not financially feasible. One option we've thought
about is down sampling. So how can we provide extremely high
cardinality for short periods of time and then down sample and aggregate as time
goes on so devs can get that short look back window that they're really looking
for. But when it goes to that longer term storage, it's more compressed. And maybe that would be a series
of really short term metric storage, medium term, medium
long term, and then long term. Another one is stochastic methods. Could we find some sort of
way to determine significance? So we could automatically drop
time series and the developers could still conduct the experiments that
they wanted to see without having all the data in our system. Another thing we've thought
about is tunable granularity. Can we provide tools that allow devs to
increase cardinality and sampling rate for short periods of time? This is another
thing where let's say there's an im, they could go out there,
they could say, alright, let's crank up the
cardinality on this feature to get more information. And the last thing that we've
thought about is verbose servers. Can we have 99% of our fleet running on reduced cardinality while a
much smaller set produce a much more verbose set of
logs, metrics, traces, so that if there is a problem,
hopefully it's caught by that system. Other stuff, I'm running out of time,
so I'm going to race through this. We're also the largest
user of Grafana IRM, which means we're beta testers. Grafana has been super responsive in
our asks and working with us here, but there's still plenty
of features that we want. We also migrated off of Grafana
IRM, not off of Grafana, from OpsGenie to Grafana IRM. And this is way too long to
squeeze into this presentation, but the story is just as exciting, so
you can come and talk to me afterwards. I also want to say thank you to the team. I really do mean this when I think we're
the best monitoring observability team out there. So if you're interested
in working with us, let us know.

