# With OpenTelemetry, ComplyAdvantage overhauled its observability (twice) | Grafana Labs

ComplyAdvantage, which provides compliance and risk management tools, has overhauled its observability platform twice in two years, first moving from on-prem Grafana OSS to Datadog, and then migrating from Datadog to Grafana Cloud. Join Principal SRE Adam Wilson to hear how his team’s approach to observability evolved, and how their increased OTel usage made it possible to migrate twice — and to get the most out of Grafana Cloud for metrics, logs, traces, Kubernetes monitoring, and more.

Chapters
0:00 Introduction 
2:49 Why Migrate? (Inspired by Google SRE Book) 
3:45 ComplyAdvantage Infrastructure 
7:25 OpenTelemetry Has Entered the Chat 
10:31 Distributed Tracing 
11:35 Observability Infrastructure 
14:52 Sampling - do you really need all that data? 
16:44 Timeline of the first migration 
17:39 Why we decided to migrate a second time 
19:00 The second migration, this time with Grafana 
21:09 Telling stories with data 
26:00 Timeline of second migration 
26:18 Lessons learned and reflection

#observability 
#migration 
#grafana 
#infrastructure

Published on 2024-01-03T00:43:05Z

URL: https://www.youtube.com/watch?v=Wyvq7Mka3vI

Transcript: Hello. Yeah, as Matt just said, my name's Adam Wilson. I'm the
Principal SRE at ComplyAdvantage. I'm not here announcing any cool products
of any kind but I'm just telling you how we've ended up using quite a cool
product and how we went from on-prem Grafana to Cloud Grafana with
a little bump in the middle. Just for a bit of background on myself
I'm actually from Medway in Kent. It's a lovely picture of
someone from Medway in?  Lovely picture of Rochester, which is the only place in the UK I think
that has actually managed to lose its city status. There's quite an interesting
Tom Scott video on that if you, if you want to know the
details behind that. And purely based on that I
ended up moving to Brighton, and that's a lovely picture
of Concorde 2 in Brighton, which is where I spend as much
my free time as I possibly can. I play drums and go to as many
gigs as I can. But anyway, when I'm not at gigs and playing
drums I work for a company called ComplyAdvantage. We're all about trying to find
bad guys in the financial system. So we kind of work with a lot of
with different FinTechs across the globe, really to try and find
anti-money laundering and or help provide anti anti-money
laundering. And yeah, like I said, try and root out anybody in the financial
system that we'd rather wasn't there. So after all of that spiel, I'm going to talk about what we've
ended up doing with Observability. And yeah, I gave it away in
the title of the talk, really, which is that I did a gigantic
observability migration
with the entire company, got everybody onto one vendor,
which I'm not going name. But there's some clues hidden throughout
the slideshow and 10 points to anyone that can work out which observability
vendor we were using in the middle of this process. And just as we'd finished that project I
got the enviable task of turning around to the entire company and saying, well,
guess what? We're about to do it again. , and we've ended up now migrating onto
Grafana Cloud which is why I'm here. So in order to talk about all of that, I'm going to break down a
million different ways of
breaking down the parts of an observability system. But the three
things that I'm interested in today are: how we export data from our
systems, our applications, and you know, the various different things that we
want to collect information about; how we collect that information; and then how we ship that into our storage
which has a big impact on how we end up querying the data. So why did we end up migrating
twice and, and, you know, why migrate or think about changing
your observability stack at all? This is one of my favorite
diagrams ever. I bring it up very, very regularly simply because, so if
anybody doesn't recognize this, sorry, this comes from the Google SRE book, and this is kind of like their
summary of all the different, like the Maslow's Hierarchy of Needs. This is like the Maslow's
hierarchy of SRE. And the bottom three parts
of this pyramid are all directly related to, or kind of directly tied into
your observability stack. So for me, it's all about making sure that you
absolutely nail the bottom parts of this stack before you start trying to do too
much at the top and start trying to be too clever. You've, I'm a really big believer in absolutely
nailing those basics before you go too crazy. So to give you an idea of
like our infrastructure and, and what we're dealing with at
the moment we deal with about that many spans per day. That doesn't include the spans that are
flowing through Istio because we've had to sample them all away because
there's just so many of them, and they weren't giving us the information
that we actually cared about at the time. So that's taken directly
from our span metrics, and I'll talk a little bit more
about our span metrics later. We've got about 41 Kubernetes clusters, that many nodes about 20% we
reckon of our metric series are in OpenTelemetry. The rest
of them are in Prometheus. And to give you an idea of the size of
some of our on-prem Prometheus servers that are still hanging around this
is a screenshot from our ArgoCD. So you can see there's two replicas
in the stateful set 110 GBs of memory. And we're requesting
four CPUs. So that if, in terms of like the number
of Prometheus servers, I'm not sure if they're still in
every single cluster, but yeah, we're talking about 82.
That'll become relevant later. So where, like our starting
point, where do we start off? We started with an on-prem Grafana,
and this is a basic overview, very high level diagram of
what our observability stack
looked like when I first joined the company. It was
set up like this for a reason. And it's got a little 41x over
there on the right hand side because basically there was no federation. Everything here was deployed
into every single cluster. So if you wanted to know about something
that was going on across two different clusters, you were logging
into let's have a look there. So you're logging into Kibana Grafana, you're probably running some kubectl
commands directly against the Kubernetes API as well, to understand what was going on in
bits that hadn't made it through, because there was an error in the
Fluent stack somewhere. So yeah, in, in terms of like how everything worked, we had what I felt was like all of
the constituent parts of a great open source observability stack but
just not really serving us. During an incident, yeah, you had to hold
all of that information in your head, go into one tab, then the next tab,
then the next tab. And, you know, that was all going on
with people trying to put screenshots from k9s, which is something people use for kubectl
commands on the command line. So yeah, k9 screenshots were flying
across Slack all over the place, which is not great because you can't click
on them and get anything out of them, really. You just have to take their word for
it that they haven't engineered that or they've run the right
k9s commands. And yeah, at basically at the end of the day, we had too many people with too much
access to our production clusters. And in a FinTech that's focused
on compliance and security and data security that wasn't gonna hold up. And also just basically because of the
culture around observability at the time, everybody wanted their logs forever. They
wanted more and more and more metrics. So the Prometheus servers, the reason why there's two replicas
is 'cause they'd fall over constantly. So when I first joined, I haven't got the exact data because we
were very bad at collecting data back then. But basically every single day I had
an SRE who was off because they'd been up all night trying to keep the
Prometheus servers up because they'd just constantly fall over. Anyway,
so that's where we were, and this is what it looked like
during an incident. There you go. So you've got tabs opening, and you had to try and
collect this context and go
from one tab to the next and look at all the different things and try
and work out what was going on. Right? There we go. So started looking into
this thing called OpenTelemetry. I'm going to very briefly, I'm sure most
of you here know what OpenTelemetry is, but for anybody who doesn't it covers,
now it covers traces, metrics, and logs. It didn't when we first started using
it. But logs has come in more recently. It really is geared, everything around Traces is like a first
class citizen within Observability. It allows you to do
drop-in instrumentation. So you can start off with just
a few lines of code get maximum benefit from it. And then when you've kind of sold the
idea of using OpenTelemetry to your organization, people then, and I
can tell you this from experience, people start to use it
more and more and more, and they want more out of it because they
start to realize the power of it. But, you know, often trying to get over that first
hurdle the drop-in instrumentation is absolutely key. And another thing that was
really important to us is
that it was open source and vendor neutral. And we'll be talking a bit more about
the vendor neutrality as this talk goes on. But that fact that it was open
source was really important to us. We're a company with a big history of
using as much open source technology as we possibly can. We contribute
regularly back to open source. Our engineers like to jump into the
GitHub and find out if something isn't working and we're sure it's a bug in,
you know, the systems that we're using. We want to go and find the bug,
raise an issue, raise a PR, see what we can do to help. So yeah, this was really key for us.
In terms, oh, sorry. Yeah, OpenTelemetry came about as a fusion
of OpenTracing and OpenCensus. I'm doing a massive whistle stop
tour through this, by the way, if you want to know any
more of the details, I, I can bang on about this forever
and ever and ever. Anyway, so yeah, this is what's ended up
running for us. So a big, a big piece of the
OpenTelemetry ecosystem, again, for anybody who's not already using
it, is the OpenTelemetry collector. And this is a visualization that I've
pulled from a tool called OTell Bin, which if you're using the Collector,
is a really cool tool interesting one. So you can, so the Collector is a GO binary that
basically absorbs a hell of a different a hell of a lot of different
observability data types. So it can absorb for us, for our case, we've got OpenCensus and
pure OpenTelemetry coming in. You can then run a lot of
different processes on it within your, within the Collector itself. And then you can export to all
sorts of different places. For us, I think we've got, what have I got one there doing to the
load balancing exporter, which again, talk a bit more about later.
And one going out to OTel HTTP. So the OpenTelemetry protocol
works over HTTP or GRPC. This one is exporting via HTTP. And at the top there is a
pipeline that's running traces. And I think the second one
is doing metrics from, I
can't quite read the slide, but it's probably metrics. So yeah, that is all I want to say on that. So in terms of like what this
looks like in the backend, this is a quick screenshot
from Grafana Cloud, just in case anybody isn't already using
distributed tracing in their Grafana Cloud instances. This is actually
just touching one application, but applications don't run on their
own. In our Kubernetes clusters, they've got Istio gateways that the
requests touch before they come into the application pod. Then
when it hits the app, so this top one right at the
top here is the Istio Gateway. Then underneath that in a different
color, we've got the Istio Proxy, which is a sidecar that runs inside
the same pod as our application. And then all of these other little
bits and bobs underneath are the application operations that
are happening within the app. So the whole thing to keep
us all on the same page, that whole thing is called a trace. And each of the different bits
underneath it are called spans. So they're all tied together with IDs
and all of this is just driven through request headers set out by
the OpenTelemetry schema. So yeah, I'd mentioned there was gonna be a few
clues and if anyone can guess who we ended up migrating to, but
I don't wanna get sued, so I haven't got anyone's
actual logo on there. So anyway, so in terms of how this works
for our purposes internally we have our app pods. So in this case we've got a Kotlin
app and it's got the OpenTelemetry SDK running inside the app pod that's
over there on the left hand side. And this developer has actually
read my documentation and added the annotations that I asked them
to, to their application pods. So well done them 10 out of 10.
And what that happens over here, we've got the OpenTelemetry
Operator, which has a number of CRDs. So in Comply Advantage, we've got
a dedicated observability team, and they are able to control
the deployment of the Operator, and they deploy the configuration
that's in these sidecars. And what the sidecar what the
Operator will do is actually inject the OpenTelemetry Collector binary
into the application pod sitting alongside the application
itself. So there's, it's the exact same binary every time
you see the OpenTelemetry logo on this slide, it's the same go binary with
slightly different configuration. So that's what's really cool
about 'em. You can sync, you can sort of point one
to the next, to the next, and you can build pipelines that feed
into pipelines that feed into pipelines. Anyway, what happened for our purposes was we
tried to keep it as simple as possible app exports to local host, hopefully 4317 on the GRPC
OpenTelemetry protocol endpoint. There's a sidecar
sitting, listening there. It's gonna chat to the OpenTelemetry, what we call OTel gateway via Istio. That's what the little sailing boat is,
if anyone's not familiar with that logo. So anyway, everything goes out. So what this means is that the
observability team are able to control the sidecar config to make sure that
no one does anything silly there. But you know, if we trust
an application developer, they might be able to add that
config themselves to the helm chart. The thing that we really care about
though, is the OpenTelemetry gateway, and that's where we have our
sort of final controls in place. We make sure that we're tagging
it with the right environment. When I first started migrating, we ended up with like a dropdown list
in our UI of like 10,000 different environments 'cause Everybody across
the company was deciding, no, hang on, that's not a name. So that's QA 01, and
that's not playground. That's, you know, QA, whatever I've decided it
is today. So we tell them, we don't care about that anymore. We're gonna tell you what
the environment's called. So we have three environments
in our dropdowns, which makes things 10 times easier when
we're communicating across the company. Makes things easier for our support teams, and more importantly for
my boss and his boss to you know, the people that
pay our money anyway. So then how do we handle everything else?
So I mentioned at the time early on, we didn't trust OpenTelemetry with logs, and I don't think OpenTelemetry
trusted itself with logs. So we did logs via the unknown
vendor's proprietary agents. So we did, we tried to keep things
as open source as we possibly could, but we did have, you know, some necessary
evils and we used that to ship logs. What else did you want to say there?
Yeah, I think that's it for that. So very soon after we started
implementing all of that, I started having lots and lots of
conversations with people about sampling. And this is one of the, the more interesting things that has changed
most recently has been that people have started to get on board with the fact
that sampling is going to happen, whether you like it or not. No application developer seems to want
any of their application operations to be sampled. But if anybody
here is running, you know, a non-trivial observability infrastructure
you are probably gonna be sampling or you've got way more money than I have
to play with. So yeah. But anyway, in, in most cases, you do not need
every single one of your traces. You need an example of what works,
and then during an incident, you need an example of something that
went wrong and you can compare the two and go, 'ah, that's probably
the issue.' So, yeah. Very quick on sampling. I don't
have the time to go into detail, but I can talk about this all day. Early on that first diagram
that you were just looking at, we were using what's called
probabilistic sampling. So effectively, every time a trace hits our gateway, we roll a dice and if the numbers come
up the way we want we sample it away. And if they don't we
send it onto our backend. We've actually moved to oh. So probabilistic is really good
because it's very easy to do. So we had so many different things going
on. We were doing the first migration. So as the observability team, we didn't
have time to get really complicated, and we were actually able to use some of
the tools that were in the vendor that we were using at the time to get away
with just using as much probabilistic sampling as possible because the vendor
that we were using would sample our data for us, which meant that we could keep our
infrastructure internally quite simple. But yeah, as time went on, we
ended up moving to Grafana Cloud. Anyway, timeline migration on the first, the first migration took us ages as, I
don't wanna go into the details of it, it doesn't really matter to any of you. I don't think you're going to get much
out of how long it took us to migrate to a vendor that we're not here to talk
about today. But just to talk really, really quickly, some of the things
that took the most time I always say, you know, I can reprogram computers
tomorrow. They do what I tell them to. It takes you about 18 months to two
years to reprogram the people and in any proper observability
infrastructure, the people are, you know, a massive key aspect of
getting this stuff to work properly. So yeah, it's, it was a long, what I'm trying to say with
this slide is it took us many, many months to migrate. There you
go. That's all we need to know there. So anyway, we're on Grafana Cloud now,
so yeah, after that first migration I'll give you, so some of the reasons that we
ended up moving was were more around like our feeling around the culture of
this other vendor and the culture that we had internally. And it was
very much like we were, we were talking different
languages and as a result, the relationship with this
vendor didn't go very well. And started to kind of looking around at
different people that we could use for our observability backend now that we
were in OpenTelemetry and we're vendor neutral, you know, we could, we could
migrate on a whim, like for, you know, zero cost. Yeah yeah. So yeah, we started
looking around at different, different companies and it as, as
soon as I started talking to, again, it made absolute sense to migrate
to, to work with those guys. They came from an open source background
a similar size in terms in terms or more similar than with
our previous vendor to us. And as soon as us kind of got a lot of
our technical teams talking with some of their technical teams, spoke to Tom as part of the
onboarding process and it just, everything gelled much,
much, much better. So anyway, moving swiftly on in terms of what we
needed to do though to migrate to Grafana with our vendor neutral OpenTelemetry,
that wasn't that vendor neutral at all. We had to solve for our
sampling issues that we would, that we didn't need to
solve to begin with. So we actually had to implement a much
more complex setup of our OpenTelemetry gateways. So we, this is where the
load balancing exporter came in. And yeah, so what we do now
is we similar kind of thing. We get the, the stuff out of the
apps, they dump all sorts of rubbish, it goes into our gateways. And the gateways now use
something called span metrics. So every single trace that flows through
that first layer of OpenTelemetry gateways, we extract all of the metadata and
the numbers and the metrics about it. We ship them straight to Grafana Cloud. Then the first layer of
OpenTelemetry gateways then uses the load balancing exporter to send
all of the spans from the same trace into the second layer of OpenTelemetry
gateways where we make our sampling decisions. And this is important because both of
these are run as Kubernetes deployments and we need some kind of way of, basically we're hacking state into our
observability infrastructure at the moment using request headers. We're
constantly debating this though, so if anybody wants to
come up and talk with me, I've got a couple of guys
from my team here as well, Edwin's in the audience who
put a lot of this together. So we're always happy to
have a conversation about
anybody else's experience with running this kind of
stuff. And it'd be cool to, to bounce some ideas
back and forth. But we, we use all of this and we've swapped in
the Grafana Agent where we were using a proprietary agent previously.
And it dropped in quite neatly. It does the same thing that we did
with the proprietary agent stuff. It handles the logs for us. And actually what we've done is we've
added Prometheus running in agent mode back into our clusters to handle
our metrics specifically for the Prometheus endpoints. So I've got a little picture of RabbitMQ
there that runs in some of our runs on some of our nodes, and we can scrape the the RabbitMQ
metrics and ship them up to Grafana Cloud along with everything else. So that's what our infrastructure
looks like at the moment. So all of those changes that I
was talking about there, like why, what changed across the organization,
like as we did these migrations and I think the big thing
for us was the change in the way that people started
to tell stories with data. So these screenshots are from an
earlier talk that I used to give. And it's basically, so we've got the trace on the left hand
side there and we extract the metrics from the trace and we're
able to build pie charts. What I found was that these
pie charts actually opened up a conversation across the organization
that had never happened before. Because previously when people used
to talk about, like for example, when our CEO wanted to talk
to us and say you know, how many searches were run across the
systems they'd get some kind of complex answer, well, we've got, you know, 300 HTTP responses from this
system and actually know only 30% of our requests go via that service. So we have to add that to that and
extract with this. And I don't know, really start talking about traces because
the traces don't matter about which kind of route the operation took
through your infrastructure. So you're able to answer very simple
questions, how many searches were run? This many. And this is the breakdown by customer
that's actually fake customer IDs up there. So hopefully I've not revealed
anything too proprietary. But anyway, the cool thing about this
was the CEO could go from our engineering infrastructure data and go and have
conversations with our customers and our partners and going, 'hang
on a minute. You know, that discount that I gave you last year, this is quite an interesting pie chart
considering how many searches you're running on my infrastructure.
You know, is this, is this really the best relationship for us to take into
the next year?' And just being able to have that impact on product, on,
you know, sales, on, you know, all of that kind of side of the business
just from getting some request headers into our applications was,
was revolutionary really. This is just gonna be a quick slide. It's basically in terms of like
pulling off the migrations and then migrating again it's a standard
IT change management project. Yeah, so identify your allies. Every time people come up with
problems 'cause they will, you need a team that they know they
can go to solve the problems quickly. We actually ended up building an
observability team as I mentioned earlier, purely to do, I mean, they're not just there to do migrations
'cause we're not doing anymore. Like I'm done now.  I think
we've all aged about 10 years. But yeah, so we, we need, you just need the team there so that
you can solve the problems quickly. Help people with any of the
questions that they have. We actually got two Slack channels, one of them for like tech supporty
type questions and one for just general observability discussions
so that people can go, has anybody solved this problem
before? Or across the org, Like, how do people think we should get this
into the Python data science teams? You know, how do we do tracing there?
How does it work? And you know, people that aren't anything to do with
the observability team can just chat about observability and I
can keep an eye and go, oh, that's an interesting
conversation. And yeah, we try to dogfood as much of
our stuff as we possibly can. Like we should be the experts at using
whatever we're trying to get everybody else to use. What else
have I got coming up? Yes. So yeah, so apparently I've completely
got the slides in the wrong order. So this is a bit meandering
and disorganized, much
like the migrations were, but you know, we pulled it off. So
just work with me here. So these were, these were the concerns I was talking
about before we started to use more and more of the previous vendors
proprietary technology. And this is the thing that you do need
to bear in mind when you're starting to use things like OpenTelemetry and it
starts talking about vendor neutrality is, it's like the technology might
work with multiple vendors, but can you? And do you end up
in a place where you're like, actually I quite like this particular
vendor's magic. Like some of the, the features that Grafana were
announcing earlier. You know, as you start to bake more and more and
you start to rely more and more on those features, you just, you don't
need to be like, oh my God, like we're not vendor
neutral at all. Like, you can migrate you just
have to bear that in mind. Yeah, and we didn't, we, we actually got quite a lot out
of implementing span metrics. We didn't have to do span metrics
before. But yeah, it's, it's just, it's one of those things to bear in mind. I'm just providing food for thought here. Yeah, that's an AI diagram that , I'm not quite as good at generating
AI slides as the Grafana team are. So this is as good as I could get. I think most of the words are
actually real words in that as well. So yeah, that was the timeline of
our migration onto Grafana Cloud. It was much shorter 'cause
we were using OpenTelemetry, so we didn't need to
re-implement the SDKs again. So yeah, we've reached the end  and I'm going to reflect a
little bit on some of the things that happened throughout
the migration. So yeah, we've ended up needing to build more
and more tooling as we went from the previous vendor into Grafana Cloud.
So, you know, bear that in mind. We originally did a lot
of metric under budgeting. As we sort of started
to move into Grafana, we ended up with way too
many infrastructure metrics. This is one of the reasons
why we started turning off. We've turned off the Prometheus metrics
that come out of our OpenTelemetry sidecars. We've turned off the span metrics that
are generated from our SGO proxies because that's not, they, they weren't giving us the story that
we wanted to generate with our data, that that was just not interesting
enough for us at the time. Or currently it's not. But we're going to continuously
review this side of things. The other problem with like moving from
on-prem to cloud, especially in the, the setup that we had was we had
41 different clusters and yeah, within each cluster we had the replicas, but almost every single one of those
Prometheus deployments was a little bit snowflaky. So something
that can happen over time. And so trying to really understand
how many, how or, you know, our total metrics volume, it wasn't
going to be a one-to-one. We never, we didn't need to migrate everything
from on-Prem Prometheus because it was a total dumping ground, which is
what I fell over all the time. So going across to Grafana Cloud, I basically had to just generate a
spreadsheet of all of the metrics that we were using across the company. And I
went through it by hand and just went, Nope, no. Yes. Okay. Maybe,
nope, nope, nope, nope, nope. Which isn't super scientific but
it got us through for a little while. Yeah, in terms of
like what we want to do in the future as well, the thing that we are kind of
looking at the moment we have, we are using the Grafana SLO
product and it's been quite cool as part of our relationship with
Grafana is that we're actually able to, that they're willing to work with us and
we're able to provide feedback on new product projects and products
that they're developing. So yeah, we were sort of heavily into
SLO before it was released. And we're now looking at can
we sync between the SLOs? So if a team sets up an SLO that says
actually 400 milliseconds is a slow operation for us can we sync that into
tail sampling so that we make sure that anything that's over 400 milliseconds
is sent to Grafana Cloud for review? Because the concept of a bad trace that
needs a review is different and can be completely service specific.
I'm rushing through the, the last couple of slides here. And yeah, I think in terms of like where we've
ended up now, we've ended up with a, an observability vendor and it that has
a really great culture match with us internally, very important because it's a, it's our second biggest contract
after our cloud contracts. To give you an idea of the
importance of this relationship, and this was why it was so disappointing
to see it sour before when we were with the previous vendor. But also really nice to see that it's
that we are now with somewhere that we're really happy and we're able to kind
of work together into a much more of a partnership. And I think, there you go. That's my final slide. That was a fairly
okay one from the AI tools I think. But like I said, so this has been a
really, really swift whistle stop tour. Slightly meandering, a bit
disorganized. But yeah, I'm, I'm really happy to talk about any
aspect of this much more in depth. If you want to grab me, I'll be floating
around for the next couple of days. But apart from that I think I'll
end it there. And yeah, thank you.

