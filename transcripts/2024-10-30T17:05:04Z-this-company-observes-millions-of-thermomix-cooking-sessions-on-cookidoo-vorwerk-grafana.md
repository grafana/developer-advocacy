# This Company Observes Millions of Thermomix Cooking Sessions on Cookidoo | Vorwerk | Grafana

Principal Software Engineer Dennis and SRE Tim share their journey of integrating Grafana into Vorwerk's digital ecosystem, ...

Published on 2024-10-30T17:05:04Z

URL: https://www.youtube.com/watch?v=qt4E14pQJDo

Transcript: Hello. Recipe for observability. My name is Dennis. I am a principal software engineer
working for Vorwerk since now around five years. And this is... Tim. I'm a site reliability engineer at
Vorwerk since three and a half years now. And because Dennis is
long at Vorwerk than me, he's doing the introduction about
what we're actually doing at Vorwerk. Yeah. But he's lying. He was a contractor
before me, so but anyway, I lost. In a way. So Vorwerk you
may have heard of Vorwerk, it's, it's not a player
you often heard in IT. You usually know it from somewhere else. Your great great grandparents
may have bought a carpet from us. Your parents may know
Vorwerk for its vacuum cleaners. And you, you may want have
one of our products in your kitchen, which is the Thermomix. We have these two product lines basically, which is cleaning and what we call
culinary. So this is everything that is, comes to, comes to food
in the end. And Tim and I, we are working for the culinary area. So we are telling you how this is
working with with the Thermomix. So the Thermomix now exists
for a bit more than 50 years. In the very beginning, it was,
as we digital guys used to say, it was just hardware you
have in your kitchen. But over time the
customer demand arose and we included more and more
digitization options into our product line. First with the TM 5, which allows to attach
digital cookbooks to it. Later with a Wi-Fi assistant cookie. And later on the TM 6 has
everything in it tightly integrated. So what are these, these
products you, you have there, for those of you who don't
know the Thermomix has now
something which is called guided cooking. So these recipes we sold in the very
beginning just as books to give people an understanding how to cook
a meal with this device. And now digital recipes, which are basically a
program for the device, which tells you which
steps you need to take, which food you have to put
into it. It'll wait it for you, it will come up with the correct settings
so that in the end when you're good, done and ready with your recipe, you see you have a you have a meal
as it is intended by a professional chef. And what we have by now is also
a website to maintain all these recipes. And this is Cookidoo. So this is basically what Tim and I
are working on. This Cookido platform. You can imagine the Cookido
has something like a streaming service or on Netflix or Spotify. But for recipes in a way. And this is the service we are building. This is now running worldwide. And we have this from an infrastructure
perspective, now running in the US, in the European Union, in China. I'm so lucky I don't have
to deal with China from a regulation perspective. It's quite
difficult. And, and also in Australia. Back in the days it was just an SAP
hybrid instance, which was all doing this. But I'm very happy that this
is no longer running the show. What powers all this? So our developers
come up with around about 3000 commits, 1,600 pipelines and around 60 deployment
every working day to get all this running. This means an infrastructure,
something like 16 Kubernetes cluster, many data, many lambdas. You get the
idea. But for what are we doing this? So we have to give you an
impression of what this means for observability. We have more than 5 million paying
subscribers to our platform, which may do 5 million
cooking sessions each day. And in general, we have around 10 million
connected devices in the end. So this, from an IoT
perspective, this is quite a lot. But what did we invest in
Grafana? What is our journey? How did we come to Grafana? It was
actually always ever been there. So this is the earliest screenshot
somebody found from 2016, but sorry, went too far. No, it's working. But initially we started in 2015 to
just use the open source version of Grafana to monitor AWS Cloud. Later we moved to Instana
for everything more or less, but there was also the ways to integrate Instana data into
Grafana dashboards. 2021, we decided to replace
Instana - a transition, which started last year. And now we are one year in into having
Grafana running for everything on observability. So why did we ended up
initially with Instana? Usually this is something
which is tightly moving. So something you may have
seen today, but a lot bigger. This is quite nice, this is, this can make a super sales pitch if
you have something like this. And, and our CEO at that time really loved
that tool because it looked so complicated and fancy when everything was
moving around. But in the end, maybe not that super helpful. What we also wanted to have something
that allows more integration into our toolscape into into our landscape
that you can say alerts are displayed somewhere else. You want
tighter integration to select, want to get metrics from,
from GitLab, stuff like that. And this is where it gets
difficult also with Instana. What you get with this, with the tool in, in the past was you had fixed
dashboards and some people really love them because they gave them a real
impression of what is going on in terms of observability. But sometimes if you are
really in a crisis situation, it can get difficult especially if
this is everything you basically have. So this is a bit different for Grafana. So now there is a move to also come
up with automated dashboards, which, which is a good thing if you have nothing. But if there's only one way to
have this, it maybe can difficult. So one thing that always annoys
me when I think back of this an error, an error call.
What is an error call? An error call is everything
that is an HTTP 500 or higher. But sometimes you may think in the
semantics of HTTP and think, hey, if there isn't something and I
want to make this a valid outcome, then this is part of your business
logic that you say HTTP 400, this, this isn't there. And then you end
up with automated alarms saying, Hey, there are too many 400s something is
going on and all your dashboards look or your automated dashboards
now look difficult. For me the tipping point
was the 9th of August in 2021 that we had a P1 and this P1 took
quite a few hours to get it done. And the initial error message
we got was something like, cannot make something with the database.
No, no connections anymore. And this is something Cedric
said in the last last talk. The data was there, it was visible. What was the actual problem, what it was hidden somewhere below in
a perspective of a perspective of a perspective. And it took some time to get there
and actually inspect that to see the problems. Just something else. This is
my highest voted stack overflow answer. I'm still proud of this. I'm
not doing any much on this site, but still kind of proud. So anyhow, how did we move to to Grafana? This is
something we'll now hand over to Tim. So yeah, how did we actually migrate? More than a dozen teams get them
up to running in about six months, I guess should be roughly the timeline. So when we set out as the SRE
team in 2022 with the official approval to look for something to
replace in with we came around with OpenTelemetry and that looked
promising. 2022. 2 years ago, I think traces was just ga but
everything else was still alpha, beta something. But we said
maybe open source is a good way. And I think for until to
now that really stands true. On the one side that help really for
the documentation part because no vendor can produce that many information for
you and for your developers how to solve things. Then the open source community yeah, other providers were still
pushing their implementation 2022 more are using OpenTelemetry
now, but as we heard before, they're still putting something on
top of OpenTelemetry and Grafana didn't really do that. So that
was at least a part of our choice. The next probably obvious step was
to start with our platform teams and get first the Kubernetes
integrations all the default logging needs, get
everything up and running, learn how to use it, how
do we provision dashboards? Do we still want to do that as code as
before or do we just rely on Grafana Cloud managing this for us? That was also a good point for us to
learn how to handle that and give teams already advice. Maybe look here, look there could be problems. Maybe if you enable a whole product and
cluster with one click and now sending double the metrics or double the
logs. Grafana Cloud says, yeah, well maybe turn down we are
rate limiting you for a moment. Then the next part was early adopters
and Dennis was coming in again 'cause he was an early adopter on Grafana
even before we officially used it. And we started with some hands-on
workshops and really set together with the team how can we get the
best out of their metrics, how to implement, which
exporters are there for Java, for Python, whatever. And that also helped them again, to
create templates for the other teams, which were not so eager to migrate. But these teams were eager to migrate
because they already knew Grafana. They knew, "Ah, I know this
tool, I know how to write PromQL, give it to me right now, I need
it." And that really helped to, to get them into multipliers
into our, in our organization. And then you also have their
teams which don't want to go first and you always have to push them
a little bit. So we push them and yeah, help them on the implementation side
and they just wanted to finish that. We didn't use Beyla is
the name right for that. But we then just took over
the implementation effort
from the SE perspective. Why did we do Grafana Cloud? Well, we had Loki before and we already reached a limit where you have to
tweak, settings and say, ah, well we need some longer retention
here, some more time outs there. And we were getting experts
in maintaining a Loki Stack, but we shouldn't be experts
in maintaining a Loki Stack. We should be experts in
providing recipes to customers. And now our observability team
can help developer teams to get most out of Grafana Cloud instead
of maintaining the Loki Stack. Also less on call and maybe easier to, because there's always a question
who monitors the monitor. And now that's at least
not our problem anymore. Now one year in we have around 350
dashboards, hundreds of alarms, a lot of metrics and data. What
are we actually doing there? Yeah. but let's be honest, not all these 350 I visit daily. Sorry. So let's iterate a bit about
what recommendations we give to developers, how they could
make the most out of it. We said we came up with default
dashboards we gave to developers, which start basically with what you
usually have these RED metrics of rates of errors there's also distribution more below. What we also did is we
form of standardized to have a better understanding from
which region in the world this is coming from. But I have to be terribly sorry. At this size the EU flag
and the Australian flag are
basically just blue pixels. So we decided that it's now a
kangaroo if you're, if the traffic, if the log or the error log line
is coming from from Australia. We also encourage teams to come up with
logging markers to say something like, how many locks do you even have there? Also to give an impression
of what is the right amount of errors. Let's be fair, applications everywhere in the world
will have some kind of kind of errors you see there. But if you start with these dashboards
and with these panels there, they have no upper bound and something
which is maybe three errors might look like, like much. So you need to give
them a better scaling that you have, have a better understanding. What also was was working quite
well is having some clocks within, especially if you're in a, in a distributed scenario where you're
worldwide that you have a better understanding of, okay,
this is an incident now, but it's in Australia
three o'clock in the night, so don't super stress everything. I said this with Error Markers. What was also good is is a
pattern that you say when you're, when you're logging errors or or warnings,
that you give them a distinct number. This is something that is quite
common in in enterprise products. And what you can do then is you can write
a simple Loki rule together with this visualization that gives you an impression
maybe there are errors or are there all the same errors? Is there something
which is really related to COM 5 0 1 or is this general everything? This
gives you a better freedom of mind , if you look at this from
a daily perspective, you see in the logs here
there are some errors, but there will always be some
kind of errors. But you see, yeah, it's just some distributed over time and then
there is no clusters building in it. Something else we try to give in, and this is what no automatic
magical augmentation will give you, is the recommendation to also try to
include some kind of business metrics or business data into your metrics. We started to, so, so
where I'm exactly working, I'm working on on the component
which sells you subscriptions. So my business case is super distinct. So we are making a sale or
we are not making a sale. This is something that you can easily
count. In this case, you can, when you, when you start to instrument this and,
and you make your your your dashboards, you start to get a better
understanding over time of your domain. How much are we selling in what
countries? Something like this. You can further tweak
this over and over again. That when business discusses with you
what they want, you can tell yeah, maybe, but this what you think about is just
a minuscule case because this happens super rarely. And also it gives you the freedom
when you're in the position that you're making a deployment and
every other metric says, yeah, there's still traffic,
everything is going great, but suddenly you're not making that much
sales anymore or your usual business case isn't really running anymore. It tells you something is
really wrong also. And you, you, I think you have this
everywhere in every company, somewhere you have some managers
sitting in some country and it's not working for them and they make a call
to somebody and they call somebody and they call somebody. And in the end you're in an incident
call because everything is not working. This is all you get. And then
you can go and you refer to your, your business dashboards and tell
no, no, this, I, I get your point. Maybe there's something for you and
we'll find out, but don't stress out. This is just local for you. One  source of having this
is maybe you're sending out business events. So in this, in our case, we are sending Kinesis events to some
data aggregation system and these events have names and here it's super easy to
just count the names and how many of these events you're sending out. Or maybe another idea we're having
a voucher reimbursing dialogue. We started counting how often was it
successful or not successful and made these, these, these panels
out of this. And with this, you see and can have a better
discussion with UX experts and that something isn't really, really
working that well. In this case, some business dudes had more
freedom than they should and the, the voucher could be lower and upper case, which was super confusing for customers. Or maybe your domain has
what other domains crave. So in my domain we are also
asking customers if they
didn't buy a subscription or cancel their subscription,
what was the reason for it? And one of the things is I couldn't
find my recipes. Finding recipes. This is another domain, this
is the search domain so to say. And we introduced the search team to, to this metric and now in their dashboard
they have a panel which just shows are people quitting because
they couldn't find anything? Which is strong indicator for them how
good their job is doing or if the latest deployment brings something up to maybe
make people quit because they do not find anything. And then you have these
super special cases. You don't see this usually if
you're running on a web shop. Imagine the following scenario. One day a customer calls in and he
appears to be more technical adept than you usually have this. And he says, Thermomix isn't making
an internet connection. It says cannot connect
to to your platform. But I invested some time and I
see it's not working on my router, but on my mobile phone peering connection. And then you make this face because you have to go to that dashboard. What's the idea behind this? The Thermomix uses a custom certificate
to secure its communication. And sometimes your ISP decides that custom certificates are unsecure and you don't have this at super big Telcos, but this is usually something where you
have to go to some small Italian ISP and then have a conversation which basically
goes like, yeah, we are from Vorwerk, we discovered that you
are blocking our traffic. It's likely because you have this ISP
enterprise product and you have activated this rule. Can you please forward me
to your principal networking engineer? And then it goes like, have
you tried turning it off again? And then you have to find your way if
you think this is hard as a customer to get up the line, try to, if you have
something like this and what we have, therefore we have a dashboard which also
includes the metrics from which a ASN (autonomous system number), which is
basically your ISP is coming from that. You can differentiate if this is just
the customer and he just has a super weird setting on his router or if there
is an entire network segment missing. We also encouraging teams by
now to also include traces. We have seen this also on the Alloy
demo. We are also including this in, in the dashboards that we say
maybe just show some traces. We usually have a working mechanism
that one developer each week is some kind of sheriff for everything
that runs with with operations. So whatever comes in issues
or also having a look at the, at the dashboards if
everything is working okay-ish. And having these trace ideas invites
developers also to look into why is this call slow? And then you identify cases, which may be something I had this before
where we're sending Kinesis events for some reason. Sometimes Kinesis takes
two minute, two seconds to initialize, but this is nothing that a
customer needs to be waiting for. This can be an synchronous task. So
we made this an synchronous task, which was just an idea. We came up when
we started looking at these traces. Why something is slow. Working with traces came really handy
over time and we also learned that in the end it's just a string and, and
some kind of type you can, you know, put in there and if you have a scenario
where you have multiple teams working on this, they can come to the conclusion that they
want to add some information to their trace, the same semantic but maybe find
out a different name within tracing. There is also the thing, there are
different types that are important. True can be a string true or it
can be the type true or it, yeah, you get the idea. So we started also making a documentation
which can compile itself to a library, which you can then ingest that. You in the end have a Java 
that allows you to come up with standardized names also for tracing that
you can make a TraceQL query and let the auto completion do its thing. And, and everybody knows this is the key to
search for something super specific. How much time do I have? I give it to you. So now we have happy developers and
the manager who initially said, yeah, go for it. Now he's asking, okay,
how much does it cost actually? And you think, okay, we have a
lot of data and we pay per metric. Maybe we can reduce that a little
bit because budget is always a difficult thing. So this is a screenshot from our
ingest rate or active metric series from last year or up to
this year I would say. And you see in the beginning we enabled
more clusters and more integrations and we went around 2.4 million active series. And then quickly after Christmas, I just sat down for maybe an
hour or two and just click on Adaptive Metrics. Yeah,
enable, enable, enable. And I reduced our metrics without
anybody noticing by quite some amount because all these
standard exposures from frameworks amid really
a lot of data histograms about how many quantiles I don't remember. Yeah. And so we don't have to do that with
every team and to talk to every team say, yeah, do we really need that
detail level or is that okay? You don't use it in your dashboard. And now we could just take that off the
team's shoulders and do it on a central place. Beginning of this year there was
no Adaptive Logs unfortunately. So we had to build something ourselves.
So we started with a showback of course, and created just another Grafana
dashboard to see which service is sending how much logs. And then
you could go to the team and then ask, okay, you have that standard component, you have roughly the same amount
of codes than the other ones. Why do you have double the logs?
Ah, you haven't turned off debug, logging on production,
maybe you should do that. So, and that helped to at least
have a 40% reduction of log volume. And I'm just interested to see what we
can do with Adaptive Logs in the future. We haven't tried that yet. And please don't ask what that peak is
that I don't want to talk about that. . But what I want to talk about is Christmas and the right thing to do usually also
bring some wishes because Christmas is already soon and our, which are at least for my part is
features for the all the stack. All these fancy new Grafana features and
beta where they currently invite us to are usually bound to a single stack. But we initially decided for a
multi-stack set up and now that's hard to play around with all
the new beta features. Yeah. Building mature enough
dashboards also brings in some challenges. So to say what is
the timeframe we are looking at? What does this data actually
mean and or what's the, it would be nice to have
something to say like, everything is running on UTC because we
agreed that everything has to be UTC. And it's not something that
I need manually need to
configure in each dashboard manually. So that you're not talking
about "Yeah, it was at this time, oh no, no, sorry, it was in this time it's
UTC and then the other one it's CEST." So having something like, like
a linter or more config options, what could be there or at least
give, give, give some hints to, to the ones who are making really
the efforts to bring these customized dashboards would be something that
would be really helpful also in our case. So did we miss something? Yes, yes. We missed ai. We missed ai. Oh, oh ai. But. We asked AI to create a picture for that
talk and no, that's not the Thermomix, but yeah, that's it. Thank you. Okay.

