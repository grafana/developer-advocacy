# Unity&#39;s Observability Stack and Migration From Thanos to Grafana Mimir | ObservabilityCON 2024

Lucas Monkevicius and Greg Chambers, Senior SREs at Unity, discuss and share examples of their multiyear project where they ...

Published on 2024-10-24T19:52:12Z

URL: https://www.youtube.com/watch?v=v3pR8NBMg1o

Transcript: Hey everyone. Really nice to be here.
I'm Lucas Monkevicius. I'm a Senior SRE here at Unity. Yeah, so a bit about me. I'm originally from Lithuania.
I've been at Unity since 2020. I moved to the US and Seattle last
year, as you can see from my accent. In my free time, I love cycling and
exploring beautiful Pacific Northwest. If you guys haven't been there,
definitely recommend to do that. Hi, I'm Greg. Moved to
Seattle back in 2015. And been at Unity since 2016. I've
worn many hats there from SDE, SDET, and now more recently SRE. I really like working there 'cause I
get to work on something related to the best hobby I have, which is video games. And just as a fun fact about myself
my first job ever was actually as a blacksmith over at (inaudible)
Museum in Connecticut. So today we're going to
talk about what is Unity. Some of the problems that we faced in
the beginning when we didn't have a centralized place for observability. Our journey with adopting
Prometheus-based tooling. Why in the end, we ended up migrating to Mimir. Greg was going to talk about some of the
lessons that we learned and lastly he will give, give you guys
some of our future plans. Okay yeah. So Unity it's fairly,
fairly new company, fairly new company. We were founded in 2004 in Copenhagen.
We are a leader in real time, 3D content. At the moment, there's around 3.6 billion
made with Unity applications. downloaded per month based on the
publicly available data on our website. We do have a variety
of different offerings. Most of you might be mostly familiar
with Unity Engine and Editor, 'cause that is a backbone of some of
the most popular games in the world. However, we also offer monetization
services, multiplayer services. Our runtime is accessible
in more than 20 platforms. And there's many, many more things that we offer that we
definitely don't have enough time to touch upon. So in the beginning we didn't have a
centralized place for observability. It was up to the teams to decide how, or even if they want to
monitor their services. And this has created a very
fragmented landscape. 'cause at one point we had upward of
10 different SaaS providers. Some teams were running Prometheus and
Influx and deploying their own Grafana. At one point, we also had like
five or six Grafana running there. And it was it was a mess. A lot
of operational overhead for us. And since we had to train engineers
and make sure that we are implementing things correctly because yeah, custom metrics aren't aren't cheap. So now I'm going to give a, give
an introduction about our journey with, with the Prometheus based tooling.
And our use case is a bit different. 'cause If we run everything ourselves
we run the open source LGTM stack ourselves. Any of you in the audience
do that as well. Okay. Also, quite, quite, quite a lot of you.
So hopefully you know, you, you'll relate to our experiences. So we started using Prometheus in 2017 when Unity adopted
Kubernetes. At first, it was like a single
EC2 VM running Kubeadm. However, we really doubled down on
Prometheus tooling in 2018 when we migrated to Google Cloud. This allowed
us to adopt a multi cluster model. And to be able to observe, to be able to bring those
clusters into a single space. We adopted Thanos project.
Then as Unity grew, we, in 2020, we started a, we started
a project that we called Kronus, which is our way of providing network agnostic observability to
teams because a lot of our services are run in untrusted environments.
And then it worked fine, but around two years later for and for ease of use for our users, we moved to Cortex and
we actually did that around the week before
Mimir was announced. So we've been closely following all
of the developments. And then 2023, we finally pulled the
plug and moved to Mimir. So it all started in 2018 when
we ran Thanos and Prometheus in our internal VPC network. It was very simple at scale that we
had at the moment. At, at that moment, we just ran Prometheus, Alert
Manager, Thanos sidecar, reading metrics from Prometheus and
sending the memory to ours. Also, Thanos Query that would that would be
used to query metrics that didn't meet that to our benchmark.
And on the other end, we had a user making queries in Grafana
that would then hit our central clusters Thanos Query and Thanos store, if
that's needed. And that's about it. It was good for our use case. It provided us with a global
view of our infrastructure. We also built at that time, we also built a service that we called
inventory that allowed us to propagate alerting rules and recording rules as
well as alert manager configuration to our Prometheus instances by using
by updating their config maps and just performing reloads
with some sidecars. And it worked fine. But then
yeah, as Unity grew, we needed, we needed something that would scale more
that we could run in any environment, not only in our VPC. So we started
so we started the Kronus project, which was our next
iteration of observability. And we made, we made
the, we made it public, like we made the access to the
public and we secured it with MTLS. So how it worked, the teams ran their
own Thanos stack in their cluster. And the central cluster would only
host the Thanos query net that user would query. And the central query would hit
every single cluster to get the data. So from that you can probably
understand that running a whole Thanos stack is quite difficult, especially for a team that develops
services and doesn't do observability and didn't, didn't do observability before. And also it was a single
point of failure because like whenever you would try to, you would
try to hit a high cardinality query. If we weren't careful enough, we
could accidentally get the whole entire read query path down. And also at that point Thanos rulers
were not really stable enough, so we had to rely on alerting
inside of the cluster. So we weren't able to do
Z-score calculations or SLOs
or things of that nature that require us to use weeks or more than weeks worth of data. In 2022, we moved to Cortex mainly
because it offered remote write. Teams no longer had to run the
whole Thanos thing on their own. They just had to have from
Prometheus running. And since we continued to use MTLS, yeah, CERT manager to perform that. And this was all really
simple for teams to onboard. It also provided us with
the centralized alerting. So managing alerting
rules, recording rules, alert management configuration was
super simple. It also had multi-tenancy, so we were able to isolate tenants that
were really noisy or they were like accidentally doing
something weird. However, it had a decentralized querying.
So in order to make a query, you had to make sure that the
query has a header in it, X OrgID, tenant name. So we built a service that
we called Kronus Cross-tenant Proxy, that whenever the user would make a query
in Grafana, it would call the service. It would assemble all of the tenant
IDs and make a query to Cortex. It was cool at first, since we
only had one tenant that we, that we could query all of our, we only had one tenant that had all
of our tenants in it. As we grew, it really became super
slow. So we, we had to, we had to find something
that is better than that. And that brings to our migration to Mimir that we did in 2023.
And why did we do that? Well, first of all, it offered better scalability and
performance based on our testing at lower resource cost, which is,
yeah, also really was really, really good thing to have. The migration was straightforward
because it was based on Cortex and we had some minor issues that we were
able to resolve within a couple of hours. The new features, like Out of order sample ingestion
has been tremendously helpful In those cases where we have network issues. OpenTelemetry support and native
histograms for Prometheus also have been really, really helpful to
manage the scale that we have. And our current architecture
looks like this. We have replaced the MTLS in favor of
an auth-token service that we built. It allows us to onboard teams in any
environment that could be a Kubernetes cluster data center,
your laptop, et cetera. We also introduced Loki and Tempo for
logs and traces to help us to better correlate those signals. And we decided to create every, create a, create a separate data source for each
tenant just because it's so much quicker than to have all of them in
a single, in a single tenant, like in a single data source. So we built a service that we call
Grafana Data Source Controller, which is able to discover
tenants in Mimir, Loki, and Tempo and basically create
create those data sources in Grafana, like Unity tenant name slash
metrics slash log source slash traces. So that has been really, really great. And our current scale is around 200
million time series since we initially submitted the talk. We grew by by
a bit because we're doing some, some onboardings with some of the teams. We are currently ingesting 6 million
samples per second and our production environment has around 80 tenants at
the moment. So quite, quite a big scale. And now I'm going to give it to Greg
to tell you guys more about some of the lessons that we learned. Thanks, Lukas. So these are gonna be the general
lessons I'll be going over in detail real quick here. We found that there were some general
themes as we went through this whole journey. So we really want to share
this knowledge with you guys here. Some of these were kind of obvious, such
as predicting future growth is hard. If that wasn't hard, we'd be
probably all down on Wall Street, making millions being traders right now. Also cost management in
the cloud can be difficult. This isn't specific to observability. You'll find plenty of articles
across the internet talking about how cloud costs get easily run
away from many companies. Also want to touch on how
signal correlation is awesome
between different parts of the LGTM stack. And last but not least, user interviews are important.
You can't forget what the, you can't forget who
these systems were for. So on predicting future growth. A tenant that scale horizontally will
inherently increase their cardinality as the number of nodes or pods scales out. Any sort of metric that includes those
as labels will inherently increase the cardinality of what they're sending you, which means you have to be able
to scale with your own tenants. They might not actually know that they're
about to get the scale up themselves. They might get a bunch
of unexpected traffic. We also have problems where sometimes
we're onboarding a tenant from another SaaS vendor that they're moving off of. Sometimes that SaaS vendor will claim
that they have so many metrics series and once we onboard them, we find that
wasn't really the case. Sometimes more, sometimes less. So we have to be able to roll with the
punches on some of these unknown factors. I also want to call out the fact that
it was really great to experience the differences in metric series
cardinality with native histograms. We have a very large tenant we moved on
recently that we actually converted to native histograms on the way over. We originally didn't and found that the
cardinality of this tenant was around 1.4 million on their own
and got 'em down to about 400,000 with native histograms. So to the Grafana devs that work on that,
that's awesome. Thank you very much. It saves us a lot of workload. On cloud cost management, it's
difficult. This, like I said, this isn't unique to observability, but there are some unique aspects in
terms of the specific context of running this stack. We have limits
and quotas for our tenants. That way if they accidentally send
us a cardinality bomb by accident, we don't have to automatically
autoscale to acquire to deal with that. We can start to throttle them and we
can alert that and ask them, "Hey, what's going on over here?" But
sometimes they're launching a new product and so we do need to scale with them. So keeping that balance between having
those limits there to prevent from the runaway auto scaling
and cost versus no, we need to legitimately scale up for this. We also have issues with some users.
We let them define recording rules, alert rules that are being evaluated
once per evaluation period for 30 seconds or a minute. And
since users can make those, users can make them very expensive.
So we have to add protections to that. But we also still wanna
enable folks to make, enable folks to make these type of at
least fairly complex queries that are reasonable for their given context. We did find that actually downscaling
after say an upscale for an incident is a bit tricky with this stack, especially with the staple set
ingesters since in order to actually scale them back down, you have to simulate
a one, a complete one zone outage, basically downscale them there
and do this zone by zone. And you have to wait for the actual
retention period you have your ingesters configured for. So you can actually
see, like this is an actual, I excluded the numbers here, but this is an actual graph of our
costs month to month from this year. You can see how we had
that spike in April. And while we did reduce
it backed down over time, the amount of effort to downsize
it again afterwards is an ongoing effort that takes a lot longer
than being able to scale up. Also we found some other miscellaneous
challenges specifically related to the fact that we have
very asymmetric tenants. While we have about 80 tenants, probably around five of 'em make
up about 50% or more of our usage. So having to deal with
that such as on the rulers, the way that those work, you know, getting the the rulers get a
unique rule group per ruler at least. And if our largest tenant, if they have a very
high cardinality query, we have to have a ruler that is
big enough to, to handle that. But that means we're now over provisioned
for the much smaller lower cardinality rules for all of our other tenants. So that's an area where we need to look
into seeing if we can get cost savings there. Signal correlation is awesome. There's the trinity of observability
though as stated in the last talk. There's definitely other places, well we should stop talking
about thes as pillars. But in this particular example, I'll call out specifically how you can
go around to the fact that I actually had a recent faulty alert that I was
able to actually go through and fix very quickly when it would've been a
rabbit hole that was probably closer to an hour rather than the 10 minutes it
took otherwise because I was able to follow up. It was a latency metric that was going
off and I was able to look at an exemplar from the metrics, follow that to a trace that then
had the link straight to the logs for that trace and
find out pretty quickly, oh, the selector includes a
regex that was incorrect. So this is including a debug path that
was being included in the latency alert and we shouldn't be including that.
Very quick thing to fix with this flow. Would've been a harder rabbit
hole to fix without this. And last but not least, user
interviews are important. Like I said, you can make this the most scalable system
ever, the most reliable system ever. If it's a pain in the butt to use,
your users aren't gonna come running, you're not gonna get the adoption.
And then who's this system for? You gotta listen to them and
what they want. Actually, I just sneak a screenshot here of Lukas
actually doing just that in the in our Slack channels here. 'cause We got
asked like, what do they actually want? Lately we've been hearing that the
big thing that they want is easier onboarding. How do I, they are already pretty satisfied
with the reliability of our system, how can they get on easier? And that was something
that you saw through our
iterations that Lukas went over that we really tried to improve
as each iteration went on. We do have some future plans that we're
hoping to do to make things even even better with our system. We, while we did deploy Loki and Tempo
in our system for logs and traces, they are relatively newer compared to
how long we've been running metrics for. And so we're still looking to get
further adoption from all of our tenants. We are documenting ourselves for our meta
monitoring and we hope to show them as an example to our other tenants. "Hey, you can get some really cool benefits
through that trinity I mentioned before if you use all three." And
so we're getting more and
more traction as time goes on, but we really want
to get that further. We also want to make Alloy the primary
telemetry agent for our collection of telemetry. Right now, our tenants and their clusters
are having to use a combination of Prometheus agent, PromTail, and the OTel collector
to send us everything. We would like to simplify that, get that down to a single thing that
we have to deploy and Alloy would be a great way to do that. So we're really look looking forward
to actually switching everyone over to that. We also want start utilizing a couple
of other options that we haven't really gotten into setting up for our system yet. We currently do not do shuffle sharding
and we want to use that and we wanna do remote rule evaluation, which may help actually with the issue
of the very large rulers we have to run right now. As I said before, native histograms turned out to actually
be a really big win for the last big tenant we moved over. So we really want to try to adopt
that for more and more of our tenants. It's technically still
a experimental feature, but we've had really good results with
it and I do highly recommend to people give it a try. It is really cool. And last but least, we want to start
adopting the eBPF-based tooling. It would be really great if out the door
we can get our instrumentation for new tenants to just automatically, before they even even have
to instrument their code, just immediately get that feedback
and instantly see metrics and see how their systems are running. And so getting Beyla into our system
would be a really good opportunity to get those wins in there. I also want to give a quick shout to
the folks that are responsible for this current iteration of Kronus that we're
running besides ourselves. So Andrea, Archit, Jhin, Steven, and
Taylor. You guys are awesome. Thank you.

