# Introducing Grafana Alloy, A Distribution of the OTel Collector | GrafanaCON 2024 | Grafana

Say hello to Grafana Alloy! Grafana Labs' distribution of the OpenTelemetry Collector brings together the very best of OTel and ...

Published on 2024-04-25T22:55:14Z

URL: https://www.youtube.com/watch?v=d9zLeFuIFIk

Transcript: And now that's a more
descriptive title, right? What? That's a more descriptive title. Oh, I don't know that "click wallpaper to
show desktop items." We'll pretend it's not there. All right. Hello everybody. We're here to talk about the newly
announced product we have, Alloy. We're gonna dig into it and we're
gonna talk about it a little bit. And at a high level Alloy is Grafana's
distribution of the OpenTelemetry Collector. And, uh, as we've discussed,
I am Matt with two T's, Durham. I'm Paschalis. And we're senior software
engineers here at Grafana. Okay. So we can start with
short history lessons. Not 2000 years like we try to
do, but with Grafana Agent, initially developed as a Prometheus
light alternative for the edge, like an easy way to get your
metrics in lightweight way. And, uh, eventually it evolved into adding
logs with support from Promtail, and then bolted on traces using like
some OpenTelemetry concepts. But, um, it was really successful for like both
hobby small users and huge corporations. But this didn't come without
challenges. At some times, Grafana Agent felt like three disparate
products instead of one with a single cohesive vision. The yaml configuration
was easy to mess up with and, uh, break things, especially when you're
copy pasting things from different teams. And the OpenTelemetry concepts that we
wanted to support weren't like really playing super nice with what
we had from Prometheus or Loki. So we thought that things could be better. We could standardize around a single
way of deploying the Agent closer infrastructure and make your lives
easier. So with this, Alloy was born. All right, so we sought out to take the best of OpenTelemetry and take what we had
Prometheus and blend it together to make what we're calling Alloy. Alloy is inspired by OpenTelemetry pipelines,
which you may be familiar with. So we came with this idea of
all these lessons learned, but to do that you need to talk with
protocols, you need to talk with backends. So we took all the traditional things
you loved from the agent, Prometheus, Loki, Tempo, Pyroscope, and we added OpenTelemetry and then a
little bit of Kubernetes for good measure. Now granted, this alone is not
enough. You need to actually get data, you need to get telemetry. So we included batteries, we included exporters from the community
to make it to where you could easily enable with one application, the ability to get data from Windows or
Linux or your favorite cloud provider. So what do you think are the defining
features of Alloy that set it apart from like Grafana Agent? I think our Alloy runtime configuration
is kind of one of the key features and differentiators that
makes it a step above. So today we're gonna go about these
Alloy basics and how Alloy actually works and is configured, look at what we mean by our
Kubernetes integration and talk about our relationship with OpenTelemetry.
As we mentioned in the keynote, we're continuously investing
towards that relationship. Uh, our App O11y product is
standardized along OpenTelemetry. All our databases can
ingest OTel natively and uh, really working with the upstream community
in our components to both package them in a nice way, but also
give back to the community. And finally we're gonna go over some
advanced concepts about new exciting stuff that Alloy can do for you. So with that, let's start with the Alloy
configuration syntax. There's just three primitive
things to keep in mind. There's attributes like key value pairs
that are backed by a type and a type set at runtime. There's expressions that really
make programmable pipelines. They're dynamically computed values that
propagate through all components that they touch and that are used to
compute values called functions from Alloy standard library, perform logical or mathematical
operations and wire components together. And finally we have blocks,
which are groups of, uh, either nested blocks or other expressions
and which are used to configure components. Now if you take these kind of low-level
concepts and wrap them together, you get components, which are
basic building blocks in Alloy. A component strives to do
one thing and do it well. It has a set of arguments
and a set of exports. So at the top here you can see we have a
local.file that's the type of component and every component within
Alloy needs to be unique. So that's where we add
a label -- credentials. You can see here we have
filename and is_secret, which are arguments you pass in.
And then at the OTel collector auth, you can see that we are passing the
output or the export from a component into this token argument. So this chaining together
of components can form what we like to call the pipeline. And uh, what Matt showed is a declarative
syntax for a living configuration. When talking to customers and users about
the use cases when moving like beyond the toy model approach, we found that often what they did
was extremely similar to an extract, transform and load NETL
pipeline. So they needed more, they needed like pipelines that could
branch out, that could be programmable, that would be highly
configurable and interconnected. So these components build this sort of
graph that propagates values dynamically. So for example, in the previous
example, the local file, component would push the new contents
to the better token authentication mechanism whenever the file, its
file contents changed. While here, the discovery HTTP and
discovery Kubernetes would
dynamically concatenate the targets to pass onto
the Prometheus scrape, which would again scrape those targets
and push these metrics out to a remote write endpoint. So maybe see this
in action. What do you think? Absolutely, yeah, let's go. So here you can see the UI of
a misbehaving Alloy instance. I can immediately see the list
of components that I have. I have some Prometheus components, some discovery components running and
some OpenTelemetry Collector components. I can see their health status and with
the view button I will be able to go to the details page. The graph view clearly shows two
pipelines running in parallel in a hybrid environment and OpenTelemetry Collector
pipeline with a receiver, a processor, an exporter, and the Prometheus
pipeline running side by side, which again dynamically
concatenates these targets for, uh, discovering services and pull from
Kubernetes, scrapes those metrics, and puts them out to Prometheus remote
write endpoint. It also uses, uh, a remote here. If I go to
discovery, I can see... You might have lost your mic. I can see the list of targets that are
actually being run at the very moment. So if I click on the
misbehaving component, I can see exactly why this is. So I can see that Grafana
Cloud credentials not found
and hear in the arguments, I can see the latest configuration. So I can see that I have already gone
on to fix the configuration error. So in the next pulling cycle, the component would pick up the correct
secret and continue sending metrics normally. So we talked a little bit about
Kubernetes because it's such an important aspect of developing the cloud and
kind of next generation development. And with the Agent or Prometheus you
might be familiar with the operator, and the operator is an orchestration
framework that configures the whatever service it's kind of handling, and sets it up based on
responses from Kubernetes. And we had that for the Agent and it
felt like an additional level of friction that we, you know, kind of was a pain point from
both development and deployment. Whenever we had to add
a setting to the Agent, we had to also kind of promote
it through the operator. So we looked at bringing in
what we call native Kubernetes, and we'll talk about those
components here in a bit. But we have built several Helm charts, some that are more vanilla and
some that are more opinionated. And I'd like to talk about the more
opinionated one that focuses on annotation-based discovery. This is very similar to how the Agent
Operator worked before the Prometheus Agent Operator, but allows you to automatically
start scraping things based upon annotations. So this really enables if you have like
an infrastructure team that's handling Alloy and you have a, you know, a
credit card processing something that, you know, wants to get it deployed. And that team can just deploy
that service and if they add the right labels, within minutes, you'll start receiving
telemetry data from those. And we think this really empowers
those teams to push things forward and stops your infrastructure team
from being a major blocker. So that really is one of the drives
you're gonna see consistently here is not only from a technological side, but also thinking how you live
and do maintenance while running Alloy.  And similarly, our years of experience
of running telemetry collectors at scale, for example, in a very
big Kubernetes cluster, we have some components to
deal with, stuff like that. So we saw that service discovery
can really impact the Kubernetes API. So we have a kubelet component that can
perform service discovery just from the local node to reduce the overall load
in the control plane. Uh, for one, for more security focused people who
don't want to run like as a daemonset, uh, with extra security
privileges just to get logs. We have a component that can get
Kubernetes logs over the network and avoid using daemonsets and deploy
simple stateful sets instead. Uh, we have also found
that people like CRDs, so we have like components
that can read from CRDs, either service monitors or pod monitors
or to sync recording rules to Mimir and Loki. And we found that this is
like enabling new use cases for people. Paschalis, you mentioned
getting away from daemonsets. What is like some reasons you would
want a stateful set over a daemonset? Well, the main, uh, benefit that you get is like more
fine-grained resource consumption. You don't need to worry about like
potential noisy neighbors problems and you have much finer grain control about what
resources you need to start your Alloy instances with.  So let's move into the
OpenTelemetry phase. So you can very broadly think of Alloy as the Agent plus OpenTelemetry
-- that gives you Alloy. Again, we're trying to take things that don't
normally work together -- Prometheus, OpenTelemetry, Alloy native components -- and combine them in a way in which they
can not only work together but create these programmable pipelines that
we think is incredibly powerful. So we are trying to make sure that
wherever you use the Grafana Agent or the OpenTelemetry Collector,
again, you'll feel right at home. This means that you can bring your
OpenTelemetry Collector configuration and convert it to an Alloy configuration
index file that you can just run. There are components that you can use
to convert signals from your Prometheus pipelines to OpenTelemetry pipelines and
have them flow downstream from there. We are keeping in sync with OpenTelemetry
collector releases and we're keeping the same defaults,
the same naming conventions, so that you can mentally transform
ideas from one place to another. But also what we found is that this allows
you to take advantage of the dynamic nature of Alloy's pipelines alongside
what you currently might be using with the OpenTelemetry Collector or
what you might intend to use. So I think that was a pretty broad
statement, maybe. Let's see a demo. Let's take a look. You can see here we've got
some components going on. We've got a receiver that's
gonna receive some OpenTelemetry. We got a batcher that's gonna batch it up, and then we have the exporter
that's gonna send it along. So this is pretty standard:
OpenTelemetry pipeline, nothing fancy, but there at the bottom you can
see we have this remote Vault, and that's an Alloy native
component. So here I am, I'm running this locally and I got an
environment variable that I'm pulling the token to authorize myself against
the Vault. And for demo purposes, I'm rereading it every 10 seconds. Then you can see where I'm using
those values, those exports, to get the username and password.
And what this allows me to do is, instead of hard coding this configuration
in the configuration file for these sensitive secrets, or putting
them in a file on disk, instead I can have one centralized
location. Now if you look here, we've refreshed the token and I
noticed there's a problem here. The auth isn't working. You can see
I'm getting this exporting failed, there's some problems. So I'm actually gonna log in
off-screen here to my Vault instance. I'm going to update the username. I ended up adding an extra
character where I shouldn't have. And then I'm gonna come back
here and we see refreshing token, we see it evaluated, and
no error is recorded. Great. It seems like everything's working and
I didn't have to go in and change that configuration, but just to check, I'm
gonna log into our App O11y dashboard. It's a very simple app I'm running
here that just rolls dice on command. I'm gonna check my traces, make sure I'm
getting some traces. Yep, looks good. And then I'll get a little
dashboard, check it out. That's automatically generated,
that's handy to have. So this combination of marrying Alloy with OTel or
Prometheus into one kind of overarching ecosystem that can
communicate with each other is one of the driving goals behind Alloy. It's this blending of things that
not only gives Alloy its name, but also its purpose. I think what's really interesting here
that you can use components to actually combine them in ways that we didn't
expect for you to build novel use cases without having to have a dedicated feature
developed for you in the Alloy or the OpenTelemetry Collector repo. Okay, so we can also discuss some things
that we are passionate about some more advanced Alloy topics. And the three things that we have
for you today is clustering, modules, and a sneak peek of an upcoming
fleet management solution. So should we get started? Let's rock. Yeah, let's go. So we hinted at this in the keynote
about how Alloy supports clustering, and this means that Alloy
instances can discover one another, perform graceful workload distribution, and also high availability at
the same time, using clustering. This enables you to have dynamic
scaling, say through the pods, behind the horizontal pod autoscaler. And they can scale up and down
to meet demands at all times. All instances must use the
same configuration file, and this means that it's much easier
to deploy than say a hashmod sharding solution where you have to manually go
change the configuration of each specific Prometheus Agent instance every
time you wanna scale up or down. On a technical level under the hood, this works using streaming HTTP/2
connections and works on a Gossip-based eventual consistency model. We
found that clusters of up to 100, 150 Alloy instances can
converge within like a second. And it also use a consistent hashing
algorithm so that Alloy instances can calculate ownership. Which
things am I responsible for scraping, which things am I responsible
for getting logs out of? And this ownership is
dynamically recalculated every
time the cluster changes or the list of targets changes. And this is how it ties
into Alloy's dynamic nature. So every time a node is declared dead
or announces its intent to leave due to being descheduled, let's say for
example, or a new node joins, all instances will recalculate ownership
individually and arrive at the same result. This means that internally it has been
roughly 50% cheaper to run than hashmod sharding with high availability
pairs like multiple replicas and is currently available for all
pull-based workload components. So you can scrape Prometheus
metrics and Pyroscope profiles, you can use to scrape with Operator
components to scrape metrics based on CRDs or get logs over the network. But we're also looking to make it as a
de facto way of scaling Grafana agents. So you won't have multiple options. You can have one option that works
reliably and works all the time. For push-based models, you can use the same scaling mechanisms
that exist in the OpenTelemetry Collector, of course, like
the load balancing exporter, we have components that
enable this as well. So in the future we're looking to like
converge these two situations into one solution that's great for everyone. Paschalis, the previous Agent,
its scraping service mode, required console or etcd to handle
configuration and membership list. Does the Alloy have that dependency? No. And this has been like an explicit
design goal for us that you don't have to deploy any extra moving pieces, but Alloy instances can take advantage
of the dynamic nature to do it all on their own. So let's talk about a topic near
and dear to me, which is modules. So I talked a little bit earlier how
components are the basic building blocks. Modules are blueprints. Modules allow you to create
custom components that
consist of other components. And just like regular components,
they have inputs and outputs, and they allow... They allow the chaining
of things together and the encapsulation of complex
functionality in just a few lines.  So if you have, let's say, a thousand lines of log rules
that you need to handle, you can instead encapsulate those
into one module that then you import into your project,
and you're only in... From a configuration standpoint, you're
looking at only a handful of lines. Now, modules, they allow you to... They can pull from any sort
of string -- files, Git, S3, HTTP -- and that is very powerful because you could
even pull them from Vault if you wanted to. Now we are taking a community... We're taking the best modules that
we've developed through Agent, which had a similar feature, and we're putting them in a
community repo that we invite you to take a look at, use and add your own. We really want this to be driven
by the community, by your needs. You all deal with the
telemetry data more than we do. So definitely take a look at that
URL and get back to us. And again, the updates are applied automatically, which will come here in a bit and
see how that actually functions. All right, so this is a
configuration file. At the top, we have the import.git that tells
me I want to import a module from a git re... Oh my gosh. All right, gimme one second here. Thought I turned no notifications.
Apparently I did not. Well I got rid of everything but that
thing at the top. So we'll go with it. I dunno where I'm at in this demo,
but we'll pick it back up here. Uh, you can see on the logs.filter agent, that's where I'm instantiating the custom
component and I'm writing to the Loki default receiver. We can
skip that Loki.write default. And then I'm using at the
very bottom at the logging, this is what a module looks like. So at the top you have a declare and that
is how you declare a custom component. You have an argument at the
top, write_to. At the bottom, you can see what we're exporting. And then in the middle is kind
of the meat of the module, where you're handling what
you actually need to happen. So here I'm adding a static label
,and I'm dropping some labels, depending on what is matched. Now let's pretend I realize I'm gonna
go here, I'm gonna look at some logs, and I pull up a log and I
look at it and I realize I did not add the host name. And that's really important when you're
trying to figure out a problem is where this is actually happening.
So since I'm using modules, I can go off screen here, I can update the git repository
and the git file that is... That I just pulled from. And I'm gonna add the host name using
one of our constants, host name. I'm going to commit, add, check in. And you can again have all of these
actions be gated by your normal git behavior. So you can have a process
there that's built into git. And then if I go and refresh the
file and see if the changes occurred, you'll see I've added
host name. All right, so we'll give it, there's
could be some cache in here. So we'll give it just a few seconds
here to make it automatically pull. And then if I go to refresh my logs, we should see host name, Aspen. Now what this unlocks is the
ability to do gitops development. And we have found that that is
transformative because it's easy to update the config on a device
if you only have 10 of them. But we have instances where people
are running hundreds of thousands of Agent and Alloy instances and going
to each one of those and adding some configuration is incredible overhead.
And in some cases it can take months. And oftentimes you're not even on boxes
that you own as an infrastructure team. So that's even more red tape
that you have to get through. So let's say for instance, you needed to add something
to redact credit cards. We just recently added a Loon processor, which will automatically find
credit cards and add redacted to it. And the ability to go in there and
to add that and within minutes, all of those hundreds of
thousand instances are now
redacting without you having downtime, having to go to configuration, or having to update anything is one
of the key features that we're really focusing on beyond just
the technical part. We also want to unlock and enable
the teams to have agency and empowerment over their changes. A big shout out to the community who
have already contributed a lot of cool modules.  So do feel free to check out and also
feel free to contribute your modules for things that you think are
worth spreading around. Cool. The clicker stopped. So finally, as a natural
evolution of that idea, we're gonna tease an upcoming fleet
management solution that we are working on Grafana Alloy. It'll allow you to assign
remote pipelines remotely, dynamically to your running
Alloy instances based on
a set of metadata so that you can tag individual Alloy instances
like running on, OS= windows. And the specific set of
pipelines would be applied to it. It'll also help to get a
centralized debug UI for people. All this is gonna be based on an open
source protocol that is gonna be available alongside the Alloy repo, and
it's probably coming soon. So with that, that was all from us
for today. If you have more questions, feel free to meet us in the hallway.
Come chat about Grafana Agent, Grafana Agent Flow, or Grafana Alloy.
We'd love to hear your history, your experience, and how you
think about this new announcement, how you plan to migrate. You can join us at our community forums
or the Grafana public Slack in the Alloy channel.  And with this,
let's enjoy the break. Thank you all.

