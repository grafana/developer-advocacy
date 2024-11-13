# Grafana 11 deep dive | GrafanaCON 2024 | Grafana

You've seen the highlights; now let's get into the details of what makes Grafana 11 a better way for you to connect to your data, ...

Published on 2024-04-25T22:58:56Z

URL: https://www.youtube.com/watch?v=8pPJ_X1xPfA

Transcript: Hello everybody. So
welcome back from lunch. Like Matt just mentioned Mihaela and I
are going to go a little bit deeper into some of the new features in Grafana 11. So we're going to spend a little bit
less time talking about some of the headline stuff that already came up in
previous talks, like Explore Metrics, Explore Logs, Alerting AI and App Platform improvements
and get right into the heart of some of the more detailed features. So
I'm Mitch Seaman, like Matt mentioned, and I'm the product director for Grafana. And that means that if you have a feature
request that you've been waiting on for years and it's not yet in Grafana,
you finally have somebody to blame. And I'm joined by Mihaela, who's an
engineering director for dashboards, data visualizations and Explore, which means that if your
feature did get into Grafana, it's probably her team
that put it together. So this one's going to be
pretty action-packed and
we're really excited to show you probably more demos per minute
than any other talk in the day. So very high level, just before we get into the demos what
we've been up to this year can kind of be divided into three categories for
three different types of people who participate in the Grafana community.
The first one is the biggest group, and this is monitoring. So we've remained just as focused
as ever on Grafana's main focus, which is to help you
to explore, visualize, and alert on data no matter
where that data lives. So it's just as important
today as it was 11 years ago. And as I'm learning today, it's just as important for space agencies
around the world or around the solar system as it is for the companies who
operate the software that's running in your pocket right now. So, second
and a smaller but much more say, high leverage group is the people who
manage Grafana instances that tens or hundreds or thousands of other teams use. And I think that's a lot of people
here in this room. So, you know, the scale that we're talking about
is potentially massive and platform observability teams or people that run
Grafana for other users are really our partners in offering great observability
services for the people who are doing that sort of first use
case. And then third, we're focused on helping developers,
members of the community, to extend Grafana. And here we're going to be talking
not just about data sources and visualizations, but also about applications as a new
way that you can extend Grafana to do things that you could never do before. So let's get started with monitoring
and troubleshooting. Mihaela, you ready? Yes. So, Mitch challenged me to make this very
interesting for you and go straight into demo time because I wasn't stressed
enough presenting to such a large room. It's very interesting to see
everyone's migrated upwards, , and hoped us to see us better, not
to hear less from us. But, you know, so let's go straight into it. So earlier in the keynote Torkel
and Cyril introduced us to Explore Metrics and Explore Logs, which is our way to enhance
your troubleshooting
experience on Prometheus and Loki. We're very excited for
those experiences to evolve, but we're equally curious to keep
investing in Explore as our advanced troubleshooting tool for the big tent. So you'll usually use Explore when
you're trying to troubleshoot. Let's say you have an incident and you're
trying to pick at every thread that your data tells you about, so you can
try and find out what's going wrong. So let's try and mimic
that. I'm going to pretend, obviously I've preloaded some
information here just to make it easier, lower the risk of it. So here I'm using the Explore page with
mixed data sources to load a bunch of different types of telemetry signals. So I'm loading some metrics
from my Prometheus data source. And while we're at it, you can actually use the Query
Advisor to help you on your way. So if you have an idea of what you're
looking for, you can actually use it, but it can also help you start with the query if you're like,
I don't even know where to go first, you know, so it's there to help you and this is
one of the AI features you might hear about. But let's move on. Let's say I also want to look through my
logs and I'll talk to you about that in a bit. I want to look through
some traces as well. And here, hopefully you can see that
we're now using the Tempo search powered by TraceQL. So we've now improved the experience so
much that we've removed the old search tab and we now default to this one, which is a very simple point and click
way to search through what you need. And let's say I also want to look through
some profiles via Pyroscope, but now, I've got so much on my screen, how am I
going to jump from one thing to another? Well, the feature that I wanted to show you
today is Content Outline and it's meant to help you with exactly that. So I've
loaded a ton of data, I'm like, how do I look through it? Well, now you can jump to the relevant
parts to help you hopefully troubleshoot more easily in Explore. Now I said I'll talk to you about logs. So we actually have a new table
view for logs that you can see here. So you can control what
fields you see in the view, you can sort as you'd expect, and you can equally filter for
value by pressing this icon here. So what this actually does is it goes
and it changes the query for you. You don't have to manually
go and do anything. Now let's move on to
another area of Explore. So last year we introduced you
the concept of correlations. This was our way to help you link
your different telemetry signals, maybe representing the
same system. So again, it can help you in troubleshooting. Well, we weren't quite proud of the
experience at the time. I mean, yes, it's a very difficult
thing to set up, but we, we set a challenge to
make it better for you. So I'm going to show that to
you right now. So over here, I just loaded up the commits from
the open source Grafana repo. And what I'd like to do is I'd like to
more easily go from these commits and see some information related to
the bill data for that commit. And I'm going to correlate a
correlation to help you with that. So I'm going to go to add correlation. I know I want to link on the ID because
that's probably how I refer to it in my other data source. I'm going to copy this ID field
because I know that's what I need. I'm going to find the right data source. So I know I have some build
information in this one. I'm going to use the TraceQL search
because it really does make things easier. Filter by the right field. There you go. Save it. Ta-Da. So I now have links and clicking
on them I get trace information related to the build for the
commit. Isn't that awesome? Wasn't that much easier
than it used to be? . So with this basically, you know, earlier when I was showing you
multiple queries in explore, if you set up your correlations, you
don't need to do any of that, right? So you can open up your logs and if you want to go to
other related telemetry signals, you'll just point and click and go
through to the right information. So correlations should help you do
all of that much easier. But yes, there's a secret to it. So yes, of
course you need to know your system, know a bit about your data sources and
equally you need to have admin rights on your environment. What that means though is once the person
with admin rights that also knows the system sets them up, they are there and available for
everyone else of every role to use them. And that's the beauty of it. Like you
shouldn't have to set them up that often. Once they're there though,
it's awesome magic. Now moving on from Explore. So I've
talked to you about troubleshooting, but I also wanted to talk to you about
some visualizations and dashboarding improvements as well. So
going to the dashboard view, I'll first say you might notice some
slight changes and we've also made some considerable performance improvements
for those of you that have loads of dashboards. There isn't
that much on this instance, but we have some really crazy
instances internally and it gets very hard to go through them equally. So this view now will maintain state. So if you expand certain folders and
you go out and then you come back in, it'll maintain the state without any
negative performance implications. And I wanted to specifically mention
to you that this part of the demo, so it is all in play.grafana.org. The intention of this is to invite
you all to go ahead and try it out. So in here I also want to mention to
you that sub folders is now officially GA. So whether you use your sub
folders to organize your loads of dashboards or you want to
set up granular permissions, they are there now for you to use. Let's go to our Grafana 11 dashboard. There's a lot to talk through here. I'm not going to talk to you
about absolutely everything. I want you to pique your interest so
then you can look into them as well. The first visualization that I want
you to mention is the XY chart. So hopefully you all know that the
XY chart helps you plot data on two dimensions, X and Y, and it helps you identify
relationships between numerical values. And if you were using the
XY chart before in Grafana, can you prove it because it wasn't
officially supported, but it is now. So we obviously support multiple modes
and you can go and have a look more into it in the documentation as well. There's more in here that
you can look through as well. But I want to jump to tooltips. So we've been doing a lot of work
in standardizing our tooltips and that results in benefits
for the users as well. So over here you'll see that I have a lot. So now what we have in
tooltips is color indicators. The content is scrollable. If you're crazy like me and you
want to look at them all at once, you can click and copy the information
from a tooltip and you can also add annotations straight from here.
You don't have to go anywhere else. Additionally, I also wanted to mention
to you that we have a new Y zoom. So on most of our visualizations
you can do an X zoom, but now we have a new Y zoom.
So if you shift and select down, it'll zoom on the Y axis as well.
This is done in the front end, double click and you come back. Now let's talk about the Canvas panel.
Mitch was telling me some of you love it, some of you don't, but you
know, you have choices there, so use whatever you like. So Canvas was officially GA in
Grafana 10, so almost a year ago. But we, we've kept our investment in this because
there were so many more use cases that we wanted to cover. So now we officially support universal
data links in most of the Canvas components, which is what you can
see here. And more excitedly, now we support bidirectional data
flow between the Canvas panel. So what I can actually do now is with
the use of the button component that you can see here on the right. So I'm monitoring this server is currently
on standby and let's hope this works because it is a live demo. But
by clicking the start button, I've actually started the
server. This is not fake, I promise you there is a server running
somewhere. I pressed the button, it actually started it.
I did not fake this. So what you can do now is - you're
not just monitoring your system, mapping it out to see
how the data is flowing, but you can instigate
actions from Grafana itself. You don't have to change tabs, you
don't have to change systems, anything. You can actually do it from
here. Isn't that awesome? And then we've also invested a lot
in our flow charting capabilities. So now hopefully you can see everything
you'd expect in a flow chart tool, you know, different types of
components, snap and align, and a lot of control over how
you edit these components. And before I move on
from the Canvas panel, I wanted to talk to you about
one more interesting thing. So I've got this panel here and I want
to change the title and the description of it. I'm not great at naming
things, naming is just hard. But thanks to our AI co-pilot,
Grafana can do it for you. Isn't that helpful? Imagine you're setting
up a dashboard with loads of panels, just set it up, AI sorts out the
title and description for it. Awesome. And like I said, for me,
it's actually better than me. And now last but not
least, transformations. So again, I expect many of you
already use transformations. So they help you manipulate the
data that your query returns. You can use them to rename fields
or just run mathematical, you know, calculations on the data itself.
But things can get very complicated, right? Like, so with that in mind,
we've actually made some changes. We have some brand new illustrations
for transformations with the purpose of hopefully explaining better what that
transformation is meant to do without you having to read a lot of
documentation. On top of this, you will notice that some transformations
are deemphasized and that is to highlight that the transformation
isn't applicable to the data that I have available in the panel right now. And this little information
box also tells you why. So in case you expect it
to use this transformation, but for some reason you can't, you know
how to change your data to make it work. While I'm here, let me also tell you that we have
additional transformations help within the tool itself. So you can what
I did here, if you missed it, I just pressed on this icon here and
it opens up some documentation about that specific transformation
right in Grafana. Again, you don't have to swap and
go to our documentation to
see some information about it. So I hope this encourages more
people to use transformations. And we're really looking
forward to your feedback really. And on top of all this, we've actually
added some new transformations as well. So we added a way for you
to format date and time. If you like the US format, I
don't understand it really. You can filter by value, so you can create some template variables
to then filter in the front end. Your data is really dynamic and cool. We have a new tabular join, which basically works like
your SQL outer join and much, much more that you can discover yourself. And before I move on from here, I actually wanted to briefly talk
to you about alerting as well. Let's find a good alert
to look at. There you go. So hopefully for those of you
that are using alerting already, you'll notice that this view
has changed considerably. So we've done a complete redesign. We now have at the top
some valuable metadata. You can also have links
to useful dashboards or a
link to your runbook maybe. And the rest of the content is actually
split into multiple tabs. Again, to hopefully make the experience easier, you no longer have to scroll through a
very long page to get to the part you're interested in. Everything is
hopefully better organized for you. So you can see the query that's being
used for the alert and also some related visualizations to
help you understand it. And you get some history and details
to help you with debugging as well. And you can always jump into
Explore if you want to as well. And a similar thing you'll
see in other pages as well. So like here the contact points again, the information is split into multiple
tabs and you can see some very useful information about the integrations
you've set up as well. Now I'm going to go back to the slides. So with the improvements in
alerting in this last year, we're now confident to say that
new Grafana Alerting is superior. So legacy alerting is officially end of
life. We've announced this in advance. So again, I hope it doesn't
take anyone by surprise. The new Grafana Alerting system is
much more powerful and flexible. You can create alerts
based on complex queries, configure multiple integrations for your
notifications and set up sophisticated alerting rules and much, much more. But you'll hear more about this
in the alerting talk tomorrow, so please go and watch it. Now, I've shown you improvements
in Explore and visualizations, but you might be like, Hey, the thing
that I use Grafana most is for monitoring. So what about dashboards? Well, we've
been working a lot in that area as well. So last year in the keynote actually, we announced Scenes as our
new dashboards architecture. And at the time it was powering our
latest dashboarding app plugins. And it's done awesome. Like we, we've had some great feedback and it
helped us spin up new plugins much faster. We've since been investing in rewriting
our core dashboards experience with the Scenes framework and we're almost
ready to make the switch in Grafana 11 users with viewer role will now
be using dashboards via the Scenes library. As a user, you shouldn't see
any major differences, and if you do, we might be in trouble.
So please raise an issue. The Scenes library will enable a much
more dynamic dashboarding experience, and this migration is the first step
in harnessing those new capabilities. So speaking of new capabilities, as for
editing your dashboards with Grafana 11, you'll be able to preview a
new edit mode for dashboards. So this helps you compartmentalize
between editing and viewing a dashboard. So in order to edit, you will enter
the edit mode, which you can see here, and you have various menu options.
And once you're done, you save it, you're back into view mode. You'll see much more improvements
in this space very, very soon. And another feature that I pretty much
wanted to leak to all of you is our Slack integration. So it's not quite ready yet, but almost there because obviously
I have a screenshot of it. This will enable you to
visualize a snapshot of your
panel or dashboard in Slack when you share a Grafana link. So now I'm going to pass over to
Mitch to talk to us about managing and extending Grafana. All right, let's get into it. So I love all the new dashboard and
data visualization improvements, but I have to admit with my past
as the product manager for auth, I really have a soft spot
for the operators who manage
Grafana for other people. So I really nerd out about
RBAC and auth features, and I actually have a whole bunch of
exciting ones to talk to you about. So like I said, if you're here, probably
you're not just a user of Grafana, you probably manage Grafana for other
people and that makes you basically a partner to the Grafana team and people
who contribute to Grafana because you are operating the system
that other people use. So here's what we've
done to help. All right, so first up, we've added a brand new
UI for single sign-on configuration. One of the first things that you do when
you set up Grafana is to configure SSO so that other users can log in. This used to only be possible in
Grafana's INI configuration files, which is okay, it works if you're
provisioning a lot of instances, but it's a little bit tedious to
set up if you're self-managing Grafana. And it's impossible
to set up in Grafana Cloud, you had to open up a support ticket
so you have access to all the same information including team sync
in SSO and access right now to SAML and OAuth providers and LDAP is
going to be supported pretty soon. So this doesn't replace the
INI configuration option. It just augments it with something that's
a little simpler and you get a nice feedback loop with error handling
descriptions of the fields and things like that. Also in permissions we continue
to work down our big list of Grafana resources that support
role-based access control. So we've added RBAC support for
library panels and for a lot of new alerting resources, a lot of people have been requesting
RBAC for alert silences contact points, notification policies. So we've gone a long way to making
alerting fully RBAC compatible. All right next up is finer-grained
auth for data sources. So still in authorization, but when a really interesting use case
that I think is going to be valuable for a lot of Loki users specifically. So Grafana allows users to access some
very sensitive data. In this case, logs. Logs can contain personally
identifiable information. They can contain customer names or
other sensitive data that you don't want everybody to see. But our traditional way of managing
access to that data is the data source. So you'd configure one data source
with one set of credentials, and then anybody including these teams
I've configured who can query that data source, can query anything
with that set of credentials. And this leaves you
with a bit of conundrum. If you have a lot of different
access policies for your logs, you can either set up a whole bunch
of data sources and configure your dashboards in a special way so that people
select the data source and then that filters what they're looking at. Or you can allow everyone access
to some somewhat sensitive data. So you have to make this difficult
choice between security and convenience. So with Loki, now you get to have
both. So I have these three teams, the checkout platform and security
teams who can all query this Loki data source. But I've qualified the
permissions for a couple of those teams. So the checkout team can only access
logs with a checkout namespace or the payment namespace, and the platform team can access any
logs except for those from the security namespace or with a high security
level. If I want to add a new team, it's the same as what I did before. So I can add an alerting team and then
I can qualify their permissions with an arbitrary set of labels. In this case, I'm limiting them to the
alerting CD namespace. So hopefully this makes it much easier
to decide who can access what logs and still have that very convenient
experience in exploring dashboards. In Azure Monitor, we've we've
gone even a step further. If you use Azure Monitor or
Azure services in general, you've probably already set up all
of your users' permissions there. So rather than recreating
those permissions in Grafana
either using data sources or even more granular permissions, we've just made it possible to use the
current user's credentials when running queries. So you remember back here
we had configured the Azure AD OAuth provider and now in Azure Monitor, I can just forward that user's
credentials along with all their queries. So two users could look at the same
dashboard with the same data source and they'd see just the the logs
that they're supposed to see. Just in case you're wondering how we
still evaluate alerts or perform other background actions for this data source, there's a set of fallback
credentials as well, which we call fallback
service credentials. The last thing I wanted to show you
is something we've been working on. I'm really excited to
give you a sneak peek. It's probably going to drop
somewhere in like Grafana 11.1. But this is a tooling to migrate from an
open source or enterprise instance to a Grafana cloud stack. So a lot of,
you're probably managing hybrid setups, or you might have considered that it
could be more convenient to move over to Grafana Cloud as opposed to managing
a Grafana instance on your own. But you might've thought, well, that's impossible because I'm querying
a bunch of network secured data sources or things that are not accessible
from the public internet. Or you might've thought that it's just a
pain because you have a bunch of users, dashboards and data sources that are
sitting in your on-prem instance, and it's just not worth
the bother to migrate. So we've been working on both of those. So what I've got here is a local Grafana. It's running in a Docker
container alongside a
Prometheus and a node exporter. And those are monitoring my Mac itself. So making it really obvious that I bought
way too much computer for a product manager. But I've got a
bunch of dashboards in here.
I got my Mac OS overview, a weather monitor and
all kinds of nice stuff. But I can't share this
dashboard with any of you. I couldn't share it with anybody to
access over the internet because it's running on local host. And also this
is only as reliable as my MacBook. Obviously I need to put it somewhere. Grafana Cloud seems like it would
be a convenient place to put it. So I set up a Grafana Cloud stack, and one of the first things I notice
is a new option to migrate to Grafana Cloud. Grafana Cloud said this
gives me some simple instructions. I can generate a migration token, see a mirrored setup here
in my open source instance, try out that that token, and what's happened in the background
is my open source instance is now connected to my Grafana cloud stack. I have one deceptively simple looking
button when I click upload everything, all of my data sources and dashboards. And that is data sources along with their
encrypted credentials just migrated to cloud. This was one of the annoying
things about cloud migrations before, is that you have to migrate data
sources one by one and go and find their credentials again, like, look up that
password or regenerate an API key. So this is quite a lot more
convenient. So in Grafana Cloud, I head to my dashboards page and
I can see all of my information. So I can see my weather
overview and then I click into my Mac OS overview.
But this one is broken. This is broken because like I mentioned, this Prometheus is also
running on local host. So how can I access that
network secured data source? And now obviously I could start sending
my metrics to Grafana Cloud metrics, but if I don't wanna do that, that's where a private data
source connect comes in. Private data source connect lets me
establish an SSH connection between an agent that I deploy on my local network
and my Grafana Cloud stack so that that Grafana Cloud stack and nobody else on
the internet can access my private data sources. So in this case, you know, I'm doing it on my local computer and I
could just as easily do this on my local network running on a Raspberry Pi. But this also works for huge deployments. We have customers you know in some
of the biggest banks in the world, for example, who are using private
data source connect as well. So the instructions work
for Kubernetes Docker, or I can deploy using the binary.
In this case just for expediency, I've deployed the agent here
alongside my other infra. I can test the agent connection, see
it's connected. Then on my data source, I see the option for this
Prometheus data source to connect using that Mitch's laptop connection. And when I test it now from Grafana Cloud, I can access all that that local data. Let's get back to some other details. So when it comes to upgrading for
everybody who is still managing Grafana themselves, what we really want for every user is
to get vetted reliable features to you as fast as possible, and to make upgrades
themselves smooth and and simple. So the 11.0 preview release goes out
today, but if you use Grafana Cloud, probably you've already
seen some of these features, and that's because for the
better part of a year now, we've been releasing every feature
in waves and we start in Grafana Cloud in the fast channel and then sort
of move on eventually getting to an open source release. The benefit of that is that we gain
more confidence in the security, reliability and performance of every
new feature as it goes out and everybody gets better reliability and quicker
access to features as a result. So this has also led to
some nice side innovations, like this is the What's
New in Grafana Cloud page. You can visit this to see all the new
features we're releasing as they go out instead of waiting for an
on-prem release. Next up, I have to inform you that
we're saying happy trails to AngularJS. So we've been doing this for a long time
and preparing for AngularJS removal for a while. What's happening in Grafana 11 is
that Angular is turned off by default. In Grafana 12, we're going to
completely remove the code. What you should do in this release is
basically upgrade your plugins and migrate off of plugins that are
still using AngularJS. There's some really good instructions
on grafana.com and our docs. I also wanna thank all the plugin
developers who have upgraded their plugins from Angular to React. Angular is an
old library. It's no longer supported, and therefore it's a security risk.
Great. Okay, so last but not least, and I'll breeze through this section
is GrafanaCON is for a community of contributors as well as users. So there are just a couple more highlights
into how we're turning this from a dashboard tool. Grafana is no
longer just a dashboard tool, it's a platform for observability
applications. So App Platform, it's the next stage of
Grafana's, big tent, and that's the idea that Grafana should
be interoperable with other tools and extensible. The big tent is growing. We have a bunch of new data sources
this year, like PagerDuty, Sumo Logic, DynamoDB, SurrealDB, MonetDB. There are a lot of DBs but there's
a third way to extend Grafana, which is apps. It's been possible to create app
plugins in Grafana for a long time, but they've been relatively
isolated from the rest of Grafana. It's sort of like a standalone web app
that you can open from Grafana's nav. So we have a lot of developers including
employees maybe some who participated in hackathons, like Jonathan, who are interested in extending Grafana
itself to do things that are a bit more immersive. So we've been improving
the tools you can use to create apps. So first, apps are better
integrated into Grafana. You've got access to services
like navigations, search and RBAC, so you can help users discover and
sort of use those apps as features in Grafana. Second, you can mix and match prebuilt components
from our design system or from Scenes, which Mihaela was just
talking about. And then last, we've invested in a much
better dev experience as
well. So better documentation, you can check out a lot of the demos
and learn how to scaffold a plugin with just one command at
grafana.com/developers. And thanks to everybody who's
been building apps as well, my friends at Volkov Labs, who are in the front row and the Logs
app that we just demoed is also an app running on Grafana. There's a lot of detail here
that we don't have time for. So I'd refer you to Ryan and
Stephanie's talk tomorrow as well. Back to Mihaela to close this out. Thank you. So we've shown you a bunch of examples
of improvements that we've made in monitoring with Grafana, managing
Grafana, and also extending it. And I wanted to mention now, although we've used a bunch of cloud
environments in the demos today, everything that we showed you works
in both open source and cloud, and that includes the AI
features that I teased. There is a talk focused on AI tomorrow
as well. So if you're curious about that, please attend. I know
Nathan's been prepping for it. But we also want you to get
involved in all of this. So we want to invite you to go and
download the Grafana 11 preview release and try it out or go to
cloud and try it out if you want. We also want you to go and read the
What's New docs that are available on our website and come talk to us
at the Ask the Experts booth. We're obviously out of time, so
we're not going to get any Q&A, but we're heading straight over there. So we'll be available if you want to
chat. Thank you everyone. This is it. Thanks everybody.

