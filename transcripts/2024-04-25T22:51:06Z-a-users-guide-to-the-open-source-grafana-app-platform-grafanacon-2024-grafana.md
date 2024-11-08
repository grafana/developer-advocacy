# A User&#39;s Guide to the Open Source Grafana App Platform | GrafanaCON 2024 | Grafana

Based on the lessons learned from building and running the SLO app, Grafana Labs launched the open source Grafana App ...

Published on 2024-04-25T22:51:06Z

URL: https://www.youtube.com/watch?v=4slp7WFlIC8

Transcript: Hi I'm Ryan. I'm Stephanie. Today, we're going to talk about the
Grafana App Platform. Yesterday, a lot of what we talked about were
real concrete things that you can use and features we're having
you look at. But today, this talk is going to
be a little different. We're talking more about where we're
going with Grafana as a platform and what you all can look forward to. Today this is really not an announcement
about new features. This is really a discussion
of where we're going. In the next half hour, we're going to
talk about why we're building this, what we're thinking about as we build it, and then concretely what
kinds of features to expect, what kinds of building blocks that
we'll be working with. And finally, what does it look like for you as you're
trying to run the application, use it, or build new features. Why? Right now we have a very
powerful plugins platform, but if you've used it, you know, you hit some key issues
with it, limitations, and what we're going to talk about
here aims to address many of those limitations. Currently, we have a powerful plugin ecosystem, but it mainly focuses on key
tools for data sources and panels. For apps, you can build stuff, but you're pretty much on
your own for most of them. There's an endpoint that lets you have
an http endpoint to do whatever you want, but you don't get access to
storage or access control, or access what teams exist,
which users exist. So, moving forward, we're trying to build a platform
that enables you to build all of the normal things that
we build in Grafana core. This should enable building more
dynamic and powerful applications. Plugins have always been at
the heart of our big tent philosophy. They truly embody
what we mean by big tent. Though we say that, our core plugins are actually built so
differently than everything else in the ecosystem. So internally, we really adhere to very different rules
than what we make everyone else deal with. So with this shift, we're actually changing it so that there
is no difference between our external plugins and our internal. We're
going to build them all the same way. So we have to use the same building
blocks that you all have access to. Next, we're going to walk through what some of
these key building blocks actually are. We're going to use the
cliche "software as Lego" analogy, and look at what you'll
be able to build with these. We'll dive into these. The most basic building block is resources and storage. In this model, we take our resources and
stick them in a storage engine. Here we have storage. So, out
of the box, you get storage, define a resource, stick
it in your storage engine. Concretely in Grafana
resources are things like your dashboards or a playlist or an alert. These are typically the things
that you interact with in the UI. So the core objects. Currently,
when we define these, we write special SQL commands
to create tables and then manage those over time. But as a plugin
developer, you don't have access to that. You're on your own. No luck there. What we're adding to this is
the ability for plugins to define resources in the same
way we do our internal plugins. So the SLO app, for example, can define a resource and manage it
the same way we manage dashboards. Functionally, it works the
same as creating a table. You see the same behavior, but we're not
actually creating a new table for it. A resource kind of more concretely
is a text definition of an object. So the key parts to it that you'll start
to get used to seeing is a kind at the top. For example, a dashboard,
or a team, or a user. Everything in this world
has an API version. And that really lets us say that a
dashboard at V1 means something specific moving forward, if we want to change it, we now have a consistent
way of identifying that. So the next part is the metadata section, and this is a mix of user-defined values, like what's its name,
what folder it lives in, and a bunch of machine-generated
stuff like who created it when, and tracking its behavior over time. And the final part that
is this spec definition. And the spec, the meaning of that spec is controlled
by what the kind and API version are. And with the spec in the dashboard case, that's where we define
what the panels are, where we define other
properties of the dashboard. So this model is what we talk about
when we're talking about a resource. So I'm back to you here. Awesome. So, we're back in Legoland
and we have our garden now, and we have our garden bed as our
storage. And then in our storage, we've defined our resources as
these plants, and that's great. We wanna keep our garden
happy and healthy, and so we decide to add
a watchtower to it. Now, this watchtower is going to consistently
look over the state of the world and let us know if anything changes. So, one day we all go to Amsterdam and
forego our garden and forget to water it. So, we get a notification
from the watchtower that, "hey, your plants are starting to wilt
and die," and it lets us know that. So back in Grafana land, what that looks like is your application
will be able to watch over any resources within the Grafana ecosystem. This can be resources that are
core to Grafana, like dashboards, playlists, teams, users, you name it. Or, it could also be resources that
were defined by your application. So in the Legoland example, that
could have been the flowers. But for a more real-life
example, the incident app, you could have incidents
as something you watch. And so then when those changes do occur, your application will be automatically
notified by the platform that something within a dashboard has
changed. And then from there, you'll be able to act on that. This is a major shift
from where we are today, where usually if you want
to look for any changes, you need to consistently pull
the database and see, hey, have any dashboards changed
or anything like that. Now it will be automatically
notified by the system, an- that'll be a lot more performant
and event driven. So let's take a look, an example of this for how it would work. So let's say that your application
really cares about dashboards. Your application would
subscribe to dashboard events. And if your Grafana instance had a whole
bunch of dashboards, so team insights, API, insights, et cetera, and a user comes in and updates one
of your dashboards, API insights, that would generate an event. Now, this event can be different types of
events. So it could be a create, update, or delete. Here we're
notified that it was updated, and then it would tell you what type
of resource was updated. So dashboard. And then also specifically
what dashboard was updated. Since your application has
subscribed to dashboards, your application automatically
will get that event sent to it. So let's hop back to Legoland
to see how we could use that. So back in Legoland, we got the notification that our plants
are wilting and dying, and that's great, I guess. But if we're in Amsterdam,
we can't do anything about that. So what we need is an operator, and this operator will be able to
take action on our behalf to drive the current state of the world towards
the desired state of the world. So, the operator will be able to go
down and water our plants and then bring the desired state
of the world to life, and our flowers will be happy and
healthy again. Back in Grafana land, what does that look like? So it'll be the same thing where you can
create an operator to drive the current state of the world towards the
desired state of the world. And you'll do that through what's
called a reconciliation loop. So your application will subscribe
just like in the watch to what it's interested in. And then when it gets an
event that something has been changed, the operator will look at, what's
the current state of the world? What's the desired state? And what action can I take
to reconcile the difference? So it's consistently trying to drive
the current state towards the desired state, but let's look at an
application to make this more real. Let's say you have a
giant office building, and in there you have hundreds of
teams and each team has a TV around their workstations, and you want to be able to loop through
relevant dashboards using a playlist for that team. So you have a
few different teams and in those teams, you want to use the dashboards that have
the tags that relate to that team name, and then put those in the various
playlists that have been created for that team. So, how could you
do that with an operator? So first, your operator will subscribe on any
of the resources that it cares about. So for here it would be the team,
the dashboards, and the playlists, and then it will start to get events
from any changes that occur within the system. So the first event that you get is
that a team one has been created and it will say, "Hey, this event has
been created, the type is a team, and that's the name of the team."
Then your operator will look at the current state of the world where
there's a team without a playlist and try to reconcile the difference to
create a playlist for that team. I'll see if this one works. Okay, cool. Then your operator will go ahead
and take action to move the current state of the world
towards the desired state. Then the next day you get a notification
that your dashboard has been updated, and now it has the tag of team one on it. So you wanna go ahead and put that
playlist within the dashboard. So your operator will take action to
add the dashboard to that playlist to drive the current state of the
world towards the desired state. Then one day you get a notification
that a team has been deleted, and since you created that
playlist for the team, you want to clean things up
so things aren't left around. So you go ahead and delete that playlist
to bring the current state of the world towards the desired state. So, this is
what is called the operator pattern, and it's taking action on anything within
the Grafana ecosystem that you care about. So this is super powerful and can allow
your applications to interact with the entire Grafana ecosystem.
These changes though, will be asynchronous, and so eventually the operator will get
to it and will update the current state towards the desired state. But
if you want a synchronous change, then that's where you'll want to
use admission or mutation webhooks. So back in Legoland, let's
look at what that looks like. So your operator's doing great. It is making the garden super successful, and people start to notice that you
have this automated watering system. So people start to come in and plant a
whole bunch of plants in your garden, and that's not great. So you add this gate and that can prevent
different plants that you don't want from getting admitted into your garden. But you can also let in plants if
you're like, "Hey, that's pretty cool, and I want that one." So this is
what is called an admission hook, but there's also mutation hooks. So let's
look at Grafana land for what this is. For admission hooks, this is a synchronous way to validate
any resources that are being created. So if you create a new resource and you
wanna make sure that certain things are not allowed in your system, you
can do that. So for example, let's say that you wanna make sure
your dashboards do not have any secrets or things that look
like secrets included in them. You could create an admission hook
that when a user tries to create this dashboard, it will scan the dashboard
contents and then reject it if you think that it has some
secrets. Then for mutation hooks, you could also decide to
modify things if you want. So if we go back to that example
where we're trying to add a team tag to every dashboard you could have
when the user creates a dashboard, you look at the first team
that it's been added to, and you add that tag to the
dashboard and then send it back. So this is how you can
do synchronous changes. And now we'll head back to Legoland and
back to Ryan to see how we can wrap that all together. So next up. You know, we've made a
flower garden, but you know, in a real world we have many types
of objects. There's many things, in this case we've got coconuts and
pumpkins and they're all out there, but how do we link them all together? So in this world, we
build roads between them. So we're essentially connecting the city
to all of our different resources and their individually
managed set of resources. In this world, we're gonna
call this aggregation. So this allows us to treat these
many types of resources as one kind of coherent single
surface. So in APIs, what these really are is these are the
labeled routes that get you to each of these resources. So I've got my
flowers API, I've got my coconuts API, and pumpkins. So in Grafana land, what we're really talking about in this
shift is moving from a world where we have a monolithic, bespoke kind of API route that
encompasses everything that we're kind of changing at any point towards one
where we are aggregating multiple APIs under a single surface. So currently our plugins,
if you've built an app, there's a structure to see these. So
we have API plugins, your plugin ID, and then a resource. And the resource could be anything but
very little control over what exists there. Moving forward, we are going to have essentially
registering sets of APIs. So, we have our dashboard APIs,
we have our playlist APIs. These are each kind of
individually managed services and routes that then get
exposed in a much like with much more capabilities and much more
precision about what the payloads mean and what to expect in the bodies. So externally, this still looks
like a single API surface, but under the hood it's pulling together APIs that are managed individually, the
individually managed walled gardens. So as a review here, we're gonna step
through what this world looks like. We're starting off with our storage. So the base layer of where
everything actually gets saved and persisted. Within that, there
are definitions of resources. So what does my individual objects
I care about? What do they mean? And they get stored into our
persistent storage layer. We have a watch capability that
the storage engine will notify an operator so that it can act
on whatever it sees when changes exist to drive the state
towards our desired state. Hooks allow us to put in
synchronous changes when those are necessary, they're not
always necessary. And in fact, for the more scalable systems, the
less we do synchronous, the better. And then aggregation is our system to
pull this all together into a single world and be able to construct the dynamic
applications we're looking for. So, for anyone kind of in the
audience familiar with this, you're probably shouting, isn't
this just Kubernetes? And you know, the answer is yes, of course it is, but it's actually a pretty different
pattern that we're talking about. Where Kubernetes is really an application
to manage your infrastructure, we're using the base, the building blocks of Kubernetes
to build user-facing applications. So many of the rules that we think of
like what's control plane versus data plan are gonna be pretty different.
If you're not into Kubernetes, you can kind of ignore all this
and your behavior won't change. But know that we're using the standard building blocks used to
build Kubernetes to build this application platform. So what does
the future look like? We are actively rebuilding most of Grafana core to depend on these
models. So what can we expect? One of the great benefits of this
approach is that by using these patterns, we can exist and cooperate much
more with an open ecosystem that many of you are already
working with. You know, can we use Valero as our backup
tools? That would be great. You know, Argo is a amazing CI/CD
system with this model, we can use that to drive your
applications to drive ours. And the other part is
Kube control becomes our standard command line tool to
manage the resources that we define. So the next key piece of this is, yes, you can build all these things
directly on Kubernetes concepts, but it's pretty overwhelming
compared to what our existing plugin platform looks like, where you implement a few Go functions
and you have something working. So, we're actively working on making these
tools much more approachable. So, all the concepts we've discussed will be
exposed and you can use them directly, but we also have helpers and wrappers
around these that make them more approachable. And literally the same APIs
you're working with today can be exposed as API servers. So what changes for you specifically?
There's really a few things here. So an operator, if you're running Grafana we have many options for it, but
if you don't care about Kubernetes, don't worry about it. It
starts up, it's running. You don't have to run Kubernetes. It's just part of the
Grafana binary starts up. There's no special container
requirements. It's really no change. So you can almost ignore the fact that
we waited until the end of this talk to say Kubernetes was on purpose.
It shouldn't really matter. It opens up tools if you want them, but it doesn't require them
if you don't need them. The routes on the API will look different. So rather than our bespoke kind of
whatever we threw in at the time, we will now have much more structured
API surface where each feature owns its own API server space and
is able to add explicit versioned APIs. And then the other huge benefit of an
operator is that we now have a much more consistent as Code story. So every
resource that we talk about writing, dashboards now have a consistent way
to read and write them across all the various ways you may access them. So as a data source developer, really also no big changes expected, like the exact same API
you write today, which is, essentially fronted by a gRPC endpoint. We wrap that and expose
it as an API server, but we'll now give you new ways to specify changes to the config model
and expected changes to the response. So ways of actually versioning the APIs
versus just whatever you happen to write in the past is now what you need
to support forever into the future. And then finally, as an
application developer, currently you can do whatever
you want and with this model, you can continue to do whatever you want, but you will have out-of-the-box access
to all these features that we talked about. So you don't need to manage your
own storage, we can do that for you. You get the ability to watch changes on
those and add these operator patterns that we've seen be really
successful at scale. So we've talked through why we did this and what you have access to. We're gonna be in the Ask
the Experts booth after this. Joe is gonna talk about actually writing
an application on top of this. So our SLO app is already
using this pattern.

