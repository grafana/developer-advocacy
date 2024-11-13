# The Evolution of Grafana Alerting | GrafanaCON 2024 | Grafana

From its humble origins as a dashboard feature to its growth into a full-fledged alerting system, Grafana Alerting is evolving still, ...

Published on 2024-04-25T23:27:25Z

URL: https://www.youtube.com/watch?v=7z5FwdfL7v4

Transcript: Hi everyone. My name's Jean-Philippe. I'm a software engineer here at
Grafana and on the alerting team. Hello, I'm Alex. I'm also an engineer
here working on alerting at Grafana Labs, and today we're going to talk about
the evolution of Grafana Alerting. I have a gift for you. Oh, thank you. Perfect. So I'm going to start
with a show of hands. We have more than one alerting
implementation at Grafana. So who here uses Grafana Alerting? Okay, that's like half the room - nice.
Who uses Mimir or Loki alerting? Okay, a few. Smaller number. Who doesn't
know the difference between the two?  A good number of people. That's a problem that I think we'd
like to solve during this talk, but let's talk about why
those are different first. So we need to start with the
timeline. So way back in 2016, which is Grafana 4.0, which is
a whole lot of versions ago, Panel Alerts was introduced into Grafana. And this is the inception of
alerting in the Grafana project. So the idea is pretty
simple: people watch panels, but you can't stare at it all the time. You have to get up from your
computer or go sleep, right? So you want Grafana to tell you when
something interesting happens on your panel. As far as I could tell, this was the first commit
of alerting in Grafana. It was by Carl Bergquist, who I'm sure you've seen walking
around this conference plenty of times. But it's very driven by dashboards. Alert rules are embedded in dashboards
and it's just kind of conceptually an add-on to dashboards, right?
It's not its own thing. So this feature really exploded
in popularity over time. I think much more than the
creators ever intended. The community really wanted
to push it to its limits. And in particular, in production, people want to run rules in this sort
of high-availability mode that Grafana has. So the idea is you just run more than
one Grafana and you load balance between them. So if one goes down, the others can pick up your work and
you can see your dashboards, right? But this is a really hard
problem for alerting because, well, notifications, right? So
the rules are straightforward, you can just replicate them
among all the instances, but you don't want to get three times
the Slack messages. That's kind of odd. So 4.2, really soon after, in 2017, there was a feature added to
de-duplicate notifications in HA mode. This is kind of the first
step to solving this problem. And it was fairly
straightforward implementation. It just uses transactions on the
SQL database that's part of Grafana. So they all attempt to basically
write a record that they're sending a notification to the database and the first
one that writes the record is the one to send it. So if you have three Grafanas,
you still only get one notification. If one drops out, you still get notifications from the
other two. They pick up the work, right? So this works really well, but kind of up to a point you can see
here are some issues from the time and we have hundreds of of
interactions there, right? So there are some really
highly requested feature gaps. So the big one is this problem that
we now call multidimensional alerting, which is kind of like, "I want to have a rule that works
across multiple different streams of data." So one rule for all of my
pods or something like that, right? But these were effectively
asking for that, but they used very dashboard-specific
language because at the time alerting was driven by dashboards, right? There were some other quality of life
features such as notification grouping and smarter multi-channel routing,
silencing of notifications. These kind of things were
really, really hard to implement, especially in that high-availability
model that I just showed you. But around the same time there's
kind of another player in this space, Prometheus. And Prometheus is developing its
own alerting model around same time. And as part of that it created a a
notification service basically called the Prometheus alert manager. And this seems to handle basically all
of the problems that we just talked about. It has this like label
semantic that it gets from Prometheus that handles the
dimensionality problem, right? And then all of this other stuff like
routing and silencing you get almost for free. So in Grafana
5.0, one release later, we added support for an external
Prometheus alert manager. You have to basically run it
yourself. It's a separate binary. But Grafana is now sent to alert managers
rather than sending the notification themself. And then the alert managers have this
gossip protocol that they use among each other and they kind of figure out
which one of them is going to send the notification. When they have consensus
it will send the one Slack message. The trade off is that you
have to run two binaries. So you have completely
different configuration
formats for these two different UIs. It's kind of a pain to run and
if you make a change to one, you have to make a change to the
other, deploy it at the same time. It's not ideal. Pretty quickly after we noticed that
alert manager adoption has been kind of insane, it's been on a really, really steady year-over-year growth
path ever since it was released. The community seems to demand it more
and more often. And around the same time, you see the same years like 2016 to 2020, there are other projects that
you've heard of like Mimir, Loki, there are some open source projects as
well like Thanos that were adopting the Prometheus model. And with
that came alert manager. So there's kind of this mass community
standardization that we're seeing for this project. And the natural step was to
make it the default in Grafana. So alert managers are pretty great,
but running your own is not fun. So the idea was, can
Grafana run it for you? And can we just kind of unify the
configuration experience between the two? Well, we decided to implement this we called
it Unified Alerting and it was first released as a beta mode in Grafana 8. So JP will tell you more
about unified alerting. With Grafana 8, that's roughly
the time we joined Grafana. We started to release a new alerting
system called Unified Alerting. And in 2021, it was in beta in October. And it was behind a feature flag.
So we had to opt in to use it. And it was not enabled by default. It was a complete rewrite of the existing
alerting system with the embedded alert manager for the first time. So the goal of this was to have
a unified alerting UI for all your alert managers that you might have. So you could configure the alert
managers in the same UI, the Grafana one, but also external ones. For
example, if you have Grafana Cloud, you have a cloud alert manager, you can also configure it through the
same UI that you would configure the embedded Grafana one. Or if you had
perhaps something external already, in Thanos or something like this, you could add it to Grafana
and then also edit it there. So looking at the timeline, we can
see that one year afterwards, in 2022, we released Grafana 9.0 and there,
unified alerting was enabled by default. So, all users using Grafana
9.0 starting from there, which ishad the unified
alerting experience. And we did a lot of work between
version 8 and 9 to align with the user expectations that we have
from legacy alerting. And now finally in Grafana
11, after roughly three years, we were able to completely remove
legacy alerting and Grafana now ships only with unified alerting experience. So, looking at the final timeline, we can see that it took roughly three
years to go from the first beta to completely removing it and bringing
this new solution as a default. So now let's walk a bit through a few
notable changes that we have in Grafana 11. I'm really excited about a few here. The first one is the
notification template previews. So perhaps you already have worked
with notification templates. It's basically how the message looks
in your receivers, which can be, for example, Slack or Microsoft Teams. And now you're able to basically preview
this message and not have to wait first for an alert to fire to
basically see how it looks. So on the left side you
now have the template, which is like a goal template where you
can define how the notification should look. And on the right side you can
basically select from past alert instances and template a preview that will be then templated
in the mail. Or you can even, if you don't want to select a past one, you see editor on the right side
and kind of create your own payload. And then this is the feature
I'm the most excited about, it's simplified routing of alerts. So
previously when you had an alert rule, you would first have to
create a notification policy
that kind of route your alerts through the alert manager and
then to a contact point and the legacy alerting system, you could directly
map an alert rule to contact point, what was pretty convenient if you were
just testing something or perhaps a smaller team that doesn't
need a huge routing tree. So what we did is we just removed it and
now you can directly map an alert rule to contact point if you like to and if
you don't need a notification policy. And the best thing about it, it has the
same semantics as a notification policy. So you have a one-to-one mapping between
your alert rule and a contact point. And you can still decide
how the grouping works, if you have mute timings or if you
need different intervals, for example, group rate, group interval,
or repeat interval. Another thing we did is redesign
completely the contact point overview. Before it was just a simple list. And now at the glance we can
directly see for example, for the email integration, which
emails are part of this contact point. We can see when it was delivered for
the last time and how long the delivery took from the Grafana system
to the third-party system. Another thing we did is the
redesign of the alert rule overview. So this looks really cool. You can now directly see that we have
on top a tap navigation where can either see the query that the alerting will
consist of or you can select to see the firing instances, look
into the alert history, or look for a detailed
view of the alert rule. So, here you can see you have directly
the query that runs the alert. And below it we, directly graph the
series that this query did return. We also directly show the
computational steps of the alert rule. So for example, there you can see the reduced step and
the reduced step for all the series that are assigned to this alert rule
by the query that's provided. So now let's talk a bit what's
next for alerting. So Alex, give us a sneak peek. With unified alerting, we have a similar-ish UI for the, the Mimir and Loki alerts
versus the Grafana alerts, but they're still like really
different systems on the backend. They both use alert manager, but
they use it in different ways. Like, the way that you configure
them is a bit different. Rule evaluation, however, is wildly
different between the two still. So it's still very much two separate
systems with a similar user interface. This means that if you're a user, you kind of still have to pick the
right one for your use case, right? There's a lot of
similarities between them, but you have to be an expert
in both to pick the right tool for the job and understand
enough about both tools. This is hopefully a choice that
we want to remove going forward. So the first one is that a big
drawback of Grafana Alerting is its scaling properties. So you can only run however many rules
actually fit in one Grafana instance. So you can only vertically scale
it. Even in high-availability mode, all of the rules run on all
of the instances. So, once
you run out of resources, you're kind of out of space for rules. The alerting implementations that
Mimir and Loki offer, however, totally solve this problem. We're going to solve it in
Grafana Alerting right now. We are bringing Mimir's, multi-tenancy and scalability
model to Grafana Alerting. So the result of this is that the scaling
properties of the tool shouldn't be a deciding factor as
to which tool you need. And you should be able to run any number
of alerts at any scale on any system with basically infinite scalability.
Here's how we're doing this. Starting with Grafana Cloud, we have built this system
that extracts Grafana Alerting out of Grafana. If you're familiar with the architecture
of the database projects like Mimir and Loki, it shouldn't come
as much of a surprise. We take all of the rules from multiple
different Grafana pods and we combine them into a big pool and then these
are distributed across a bunch of different rules engines that
can then be horizontally scaled. So if you need to fit more rules, you add another rules engine and they'll
automatically redistribute the rules amongst each other so that you can
horizontally scale alerting as far as you want to push it. We have already built this system, it is currently stabilizing and we are
testing it in Grafana Cloud right now. Production rollouts will be proceeding
to a hundred percent in the next few months. That is happening in 2024.
However, I mentioned Grafana Cloud a lot, so we want to gather some
community feedback on this project. It's a really exciting project, I think. And we want to understand
if the OSS community is
interested in this and if this is something that you think that
it's a problem that you would solve. We're actively wanting feedback on this. We will be at the Ask the Experts bar
immediately following this talk and we want to chat about this and hear your
use case and understand if there's enough community interest in this project
and potentially making it open source. Similarly, if you don't chat
with us at the conference, we have a Slack channel in the Grafana
community, Slack called Alerting. That QR code leads you
there. We have more to share. So I'm going to move on if
you haven't scanned this yet, it'll be back at the end
of the slides, don't worry. So the next one is that we want
to introduce a centralized API to cover all use cases and all clients
that is based on the Grafana App Platform. This is leveraging a lot of
the same tooling that you've
heard about in a lot of the previous talks, but this is largely in prototype phase. Here's an example of what it might
look like but we want to give everyone one single, one stabilized versioned
API that you can use to interact with your alert rules no matter
what system you're using and no matter what your client is. We want to remove the confusion over
which API you use for which use case, which model you use for file
provisioning versus API usage. We want to have a single ergonomic
pattern and an ergonomic model that's shared by everything, the UI
provisioning tools like Terraform, and then third-party clients
that you might want to write. Those are the big problems that we're
tackling in the next six months to a year. But I wan to hand it over back to JP
to talk about our two-year horizon. What's the vision for Grafana
Alerting going forward? Going forward, very interesting. The first thing we need to do is to
bridge the feature gaps between both alerting worlds that we have
at Grafana. So one side is the, what I call the database alerting, which is how Mimir alerting
and Loki alerting works. And the other side is the Grafana
Alerting, which as of today, are quite different in some ways. One of the differentiations
is that the integrations, which are basically the third-party
systems that the alert manager talks to, the configurations are quite different.
They do the same thing, for example, send a message to Slack. But how you configure it might be
different and the fields are called in different ways. So we want to align on a super set of
this to basically cater for both worlds. Another thing is evaluation. If
you use Loki or the Mimir ruler, you might know that there you have
sequential evaluation of rule groups. This is something we don't have
in Grafana Alerting right now, and we are working on introducing it soon. Another thing that's really exciting
is that we try to and want to implement Grafana managed recording rules. This will be the same as
Prometheus recording rules, but it will work with any data source.
And we'll write back to a time series. So if you have a data source that
is, for example, built by query, you could create a recording rule to
save some money and reuse the recording rule in your dashboards and your alerts. Another thing we need
to do is compatibility. So the rule configuration format of
Prometheus, which Loki and Mimir uses, and the Grafana managed
rules are quite different. What we want to create is a super
set of this so we can cater for both worlds. Another thing is we need the tooling
to migrate from the Prometheus and from the Loki systems to
the Grafana managed system. That's something we want
to do in the near future. If you look at the unification
of the alert managers, this is how it could look like. Today, if you run an LGTM stack
or you have Grafana Cloud, you may know that you
have two alert managers, you have the Grafana alert manager,
and you have the Mimir one. Both work in the same way, but the configuration of the
receivers is quite different. That's the first step we want to do is
to create a new binary that can run both configurations, the Grafana and the
Mimir one. Then in the next step, create the super set configuration
that's compatible with both and you only need one alert manager. This
would then look like this. So, in your alert manager selection, you
would only have one alert manager left. The external ones you could exclude
because you wouldn't need them. You could cater with one alert
manager for all your use cases. Let's take a bit of look at
the unification of the rulers. So if you have an LGTM stack, you have three components that you need
to run for alerting right now beside the alert manager, it's a Grafana ruler,
the Mimir ruler, and the Loki ruler. They all three basically
do the same thing. They run alert rules on a schedule
and then send the results somewhere if it's firing. The thing we want
to do there is a bit the same thing. It's unifying both in one binary, so that you have a binary
that works with Grafana, with Mimir and with Loki type of alert
rules. But then we want to do a big step, we want to create a new alert rule format
that's compatible with Prometheus and it's basically a super set. So we only have one rule
definition for all three systems. If we now take a look at how this
could look like on abstract timeline. On top, we have database alerting with Mimir
and Loki with the Mimir alert manager, the Mimir ruler and the Loki ruler. And on the bottom we have Grafana
alerting with the Grafana ruler and the Grafana alert manager. Our goal is to continue working on
unified alerting and unifying both worlds into one experience for
the users and the customers. So again, thanks for participating.

