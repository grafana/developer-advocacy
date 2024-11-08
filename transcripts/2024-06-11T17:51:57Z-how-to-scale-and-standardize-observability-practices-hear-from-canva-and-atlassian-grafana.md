# How to Scale and Standardize Observability Practices: Hear from Canva and Atlassian | Grafana

This panel discussion, featuring Jenna, Director of Engineering, Reliability Platforms at Canva and Andrew, Head of Engineering ...

Published on 2024-06-11T17:51:57Z

URL: https://www.youtube.com/watch?v=kKCP7dxkxBk

Transcript: For everybody else to, to have some
success and get straight to that value. So next up we're gonna
have a, a panel discussion. So we're gonna talk about
scaling observability. And so what better way to, to talk about scaling than to invite
you know two people from you know, two of Australia's you
know arguably, you know, most successful technology
companies we have, so from being Canva and
Atlassian.With that, I'd like to invite up onto the stage
Jenna Nelson from Canva and Andrew Brainwood from Atlassian to come and
talk to us about a scaling observability. Welcome, guys. So we'll just wait for some chairs
to come down so we can can sit down. But I guess while we're waiting for that
how about we just start with I guess some introductions. Tell us a little
bit about yourselves and your roles. Why don't I kick off?
Hi, I am Jenna Nelson. I'm currently the director of
Reliability Platforms at Canva. And before that I was at, I've been in that role for about a year
now although I started as a principal engineer. And before that I was
at Google for about 14 years, where I started as an
individual contributor and
then worked my way out through the tech lead TLM manager, manager,
manager, manager, manager managers. And what was the part second
part of that question that was. I guess, you know not only your, I
guess your role, but also, you know, what's your, I guess,
your team's mission that. You have? Oh, that's right, that's right. And the mission we have is
to not only build reliability tools to drive the product, but also drive cultural change
throughout the organization. So like, I think it's the two big aspects
of reliability is, you know, part of it's about building the
hygiene factors that you need, the, the tooling and rolling
the tooling out, but, but actually driving cultural
change as well. Andrew? Hi, I'm Andrew Brainwood. I've been with Atlassian for
a little over 10 years now. But I've only been in the
observability leadership position since October. I was working with half the
team for about a year before that, but reorgs being what they are, we move around and shuffle often due
to the scaling nature of our business. And so yeah, working with
these guys since October, they've come and paid to watch
me speak. Hi guys. . So yeah, if you, if you're looking
for any info from the Atlassians, they're all here. Really
proud of these guys. It's been wonderful working with them and, and getting to know the
observability space from the side of leading observability versus
causing them trouble which was where I was before that, you know, the past nine years is basically dumping
a whole heap of logs and metrics on them and wondering why they
can't deal with it. And so, yeah, our mission is sort of shifting at
the moment. It's been through a few, few different hands over
the last few years. And I, I guess the whole of Atlassian is, is sort of shifting from
Scott used to say we, we are after the Fortune 500,000
and now we're after the Fortune 500, so we're, we're
going enterprise grade. And that it's really a big shift in
how we approach reliability in general. So we run the, the observability platforms
for Atlassian Cloud, but that also involves how teams use it how they achieve enterprise
grade reliability. That's great. So I guess you know, the
first question I'll start off with, well, I guess second question now you know,
it's really, you know, how you know, do you define observability,
right? So, you know, how's it perceived within your
organization? You know, both by, you know, your engineering teams as
well as by your leadership? Yeah, great question. I, I think you know, we've got a lot of different personas
that that use are involved with the observability space. So everything from the on-call
engineer to support engineers up to exec level leadership, incident commanders the finance team there's, there's
lots of different perceptions at play, so it's kind of hard to just say like
one thing, but I, I think in general, you know, everyone knows it's vital. It's, it's a vital part of the business, but it's also very difficult part of the business to, to run and I guess provide the right features
at the right cost at the right scale when you're a fast scaling business. Yeah, I think Anthony's probably
covered most of it. Oh, and I, I, I think of it in the same way.
Basically, there's two big roles to play. Part of it is around successfully
knowing you've rolled out a service and debugging features. It's
like actually, you know, the technical bit of you've rolled
a service out, making sure it works. But then the second part of it is
more around product management, senior leadership. So product management actually
wanna know the features being used, how it's being used and the sec and
the senior leadership wanna understand, I use the term right sizing a lot, which is basically how do you
rightsize your reliability efforts? How do you make sure you're actually
applying your effort in the right way? And the only way you can look at that
is to understand where the errors are coming from, how the
features are being used, it's all that sort of loading around cost. And I'll probably talk about that
in one of the other questions. Yeah, that's great. I think this is a, a
common common trend with observability. I think, you know, everyone understands
the value, right? It's how about, you know, how do we, you know, drive that, I guess that change in the organization?
And so with that, you know, in speaking about change
and, you know, and what the, I guess the outcomes and the, the
objectives of observability, you know, above just, you know, the traditional,
you know, mean time to resolution, you know, what other kind of
key metrics, you know, are you, are you looking at to, I guess,
measure and, and focus you know, your teams towards? Yeah, so the, I guess there's two ones that I'm very
interested in at the moment. I, I, I think our organization, look, organizations sit at different
points in their maturity curve, and some organizations are still gonna
be very focused on the, the, you know, the meat and potatoes of making sure
you've got over the latencies measured of key user flows and, you know, error
rates and all that sort of stuff. We're a long way down the journey now. And a big part of what we're trying
to do is get really reliable top level metrics that we can drive SLOs with, and particularly things
like enterprise SLAs. So we have a bunch of metrics that
we are driving through tracing data, and it's to do with the success and
failures of user flows. And the, that's the first part is, you know, having that really top level metric
that is genuinely about the customer experience. We really wanna understand whether the
customer is actually being affected or not at scale. That's a really big problem. We have a 200 million MAU and at scale, that's, that's an interesting challenge because
there's so many different experiences that users can have. So what does it
even mean to have a top line metric? But the other part I'm really excited
about is we've been driving a project called the Cost of Unreliability, where we wanna actually
put a cost against outages. And we're about six
months away of having a, like a consistent data pipeline
that gives us an actual, like first order cost of, of an outage.
And that's based on survivor analysis. So basically when there's an outage, we look at the differential between
a between the group of people who are affected and a control group who
have similar sets of properties. And then we look at the survivor
analysis over a period of about 30 days. And the drop off tells us how many people
were affected by the outage and left the product, and it's not zero. And so we know when outages
are causing problems, and then I twisted finances
arms to give me a number. And so we multiply by a magic number,
and that gives us a cost. So to, with the the outage, which I'm
really excited about. Even at Google, we never had a figure that was
like so directly tied to an outage, and it's only first order. It doesn't take in reputational damage
and a whole bunch of other things. But that's a pretty good first cut. And the nice thing about that is that it
begins to be a number that we can talk to product management and
senior leadership about, and it's very easily translatable
into their prioritization. And this is where I get back
to, you know, right sizing, how do we talk about feature
versus reliability work? It's a, it's a great a use case, you know, when it comes to talking leadership
money talks, right? So . I mean, at some point, all metrics you need to be able to
be talking apples with apples, right? And dollars is just where you
always end up gravitating towards. It's an easy number to talk about. Yes, I, I, I guess you know, MTTR obviously super important, but when we've focused
on that specifically, we've found it's very hard for
us to move the needle on that if, if teams aren't engaged.
So another one that we've, we've had direct focus on, and then just like in the background
and I think we're coming back to a point where it's probably gonna
be a closer focus again, is customer detected
incidents. So how often do, do people run into stuff when we
find out from them it's really bad. The answer is all the time. We
find out regularly, and it's, it's really not okay. So, you know,
from the platform's point of view, what can we do to make it easier
to instrument the right things to, to get telemetry on the right things,
to highlight the right things. Things like the asserts
piece we're showing you
correlating alerts is something that we've been looking into as well.
And then I guess the other metric, you know, cost, cost as a proportion of our cloud
spend our observability costs are really quite high at the moment. We find most teams that we serve
don't really understand the, the implications of the changes they make. So they'll roll out changes to logging and and, and DPM and metrics time series that
just blow us away either push us over the edge in terms of what we can
scale to or completely destroy our license. And, you know, that's, that's a thing that we
keep a pretty tight eye on. I mean, team breakdown of cost
is really important. Like, you wanna be able to drive all your
costs back to a team level. Yeah. Because it turns out that basically
there's some big teams that cost money and everyone else you don't care about. Yeah. So we've got some, some cost attribution, but getting a little more granular on
how much we're, we're attributing back. And then there's like always the threat
of like, how, how can we, you know, with some of these teams that just
don't wanna play ball, should, should we go to chargeback? Should
we find some other way to help them? I, I will say it's
interesting, one of the, one of the drivers I have is to stop
people from worrying about cost, because it's very easy for small teams
to get obsessed about like, oh my God, I need to optimize this. I've got five
servers, and what if we had to add a six? I'm like, add the six. That's
not worth your time. Yeah. And driving that is also a really
important little cultural idea. Yeah. And so, so our,
our next three years, we really want to get away from being
the cost control team and back to being the reliability team, but that's,
that's a journey. And to get there, we're gonna have to lean into cost
first. But yeah, getting the, the, the top line items and not
worrying too much about the bottom, I think you've always gotta
prioritize your efforts. Yeah. I think that's really important. And I think it's something we see kind
of consistently kind of working with, with customers, you know,
and certainly like, you know, we talk about observability being
a journey, right? Like, you know, you start off small, obviously, you
know, people say, what's the, you know, the first, you know, kind of a telemetry
signal. I'm like, well, that's, you know, customer support, ,
that's the first signal you start with. But I think, you know, we see
this journey, we see you know, we went through it ourselves, right?
Where you start with, you know, you've got small teams they start
with, you know a lot of autonomy. They just go and do
their own thing. They're, they're responsible for their
own costs. And then as you scale, you move to centralized observability, and then suddenly you now lose that
kind of control and visibility. So individual teams don't know how much
they're spending sometimes. And so, you know, as we kind of
talk about, you know, I guess observability being a journey,
you know, on the journey, I guess, that you know yourselves have been on,
you know, what are some of the kind, I guess, significant challenges you know, that you've encountered and and how
are some of the ways that that you've approached them and tried to tackle them? I mean, I, I think by far, one of the biggest problems you run into
is always around adoption and cultural change, right? It's all very
well to have an application. You can do a lot of stuff with
an observability team. And look, this is a problem related
to scale. Canva is at about, I think four and a half
thousand employees. So
there's about 1500 engineers, and we have, I call it, call
it in the order, 300 services. But that means there's a
lot of teams and, you know, the teams are not all the same. And I
talk about marketing a lot these days, which is a bit of a shift from where
I used to be talking. But, you know, I talk about marketing reliability,
because at the end of the day, one of the big things you do in
marketing is marketing segmentation. And it turns out we have a bunch
of big services. There's, you know, about a dozen really big services that
I care deeply about when they go down, it's a big deal. And then there's a really long tail of
services that if the avatar icon doesn't show up, I'm sad, but I'm not super sad.
Like, you know, we can live with that. And so that segmentation's really
important and you end up with very, very different, you know, behaviors. And
so getting adoption in the big teams, actually usually not too bad.
They're often very sophisticated, they're very mature, they have people
who know what the heck they're doing, and they really care. They're
actually driving the technology. They want more from us. Getting adoption in the long
tail is a very different game. 'cause In the long tail, you've got
people who are still very focused on, we're just trying to deliver a
product. I need to develop the code. And getting that balance of how much are
we driving the smaller teams to adopt our services, and how
much are we, you know, letting them just adopt in their
own time. There's a, there's, there's nuance there. 'cause
At the end of the day look, reliability without question is the
most important feature of a service. If your car doesn't
turn on in the morning, you hate that car and you're never
gonna buy that brand again. Like, you need that car to be reliable.
And services that don't work look, they're shit, you're never gonna use
them again. So reliability super matters. But it turns out, if you
don't have any features, then it doesn't matter
if it's reliable or not. Super easy to make reliable services
that don't do anything. So look, there's a trade and you know, right
sizing, reliability, I talk a lot about, and I'll keep on saying that
again, it's a bit of a mantra. You need to find that balance. So look,
cultural adoption, I will come back to, is a really big deal. And, and associated with that is also
around how do we find metrics that are really actually useful to senior
leadership. Like we're just saying, money's a great metric
and it's pretty good. But the first product manager I talked
to about giving them outages was like, we don't use money. Like, but, but, but
we went to all this effort. He's like, yeah, that's not like, it's a small
factor. And how we prioritize our work. We do a lot more around impact. We do a
lot more about this and this. I'm like, okay, tell me more. Like, you know,
let's, let's talk that through. So, you know, meeting your
audience and actually trying
to find ways that drive it. And that's all about having that
close connection, getting in you know, working very closely with the
teams to understand them. Sorry, I'm gonna go on a little bit of a
round, but I promise I'll be short. Like I worked at Google, and Google has one particular
extreme of reliability engineering, which is the site reliability
engineering approach. And it's all about, you know, embed engineers in the teams,
and you have people who work on photos, and you have people who work on blogger
and networking and ads and whatever else. And Canva is at the other extreme,
which is basically teach a man to fish. So we have a centralized team, and
we're all about providing services, and both of them have goods,
you know, pros and cons. The trouble with the embedding everyone
in a team is that you end up with a constant tension where the
developers' are like, oh, thank gosh, I can give you my pager. And like, I'm
not, like, we are just not pager monkeys. We actually do more than that. And the trouble with this approach is
that you don't necessarily end up with the sympathy that you need
to really understand the
problems that you're trying to address. And the truth is, I'm trying to drive for an
answer somewhere in between
where we do secondments and embeddings so that my
team is constantly, you know, like understanding the problems that
the developers are trying to face and making sure that our tools
are fit for purpose. So yeah, culture embedding sympathy with the
customer. Turns out we're a, you know, a service provider as well. Yeah, I think at Atlassian, like
I, when I started there was, what, 700 people and
now we're 15,000. And so similarly like the, I guess,
you know, the, the numbers are somewhat irrelevant. We're all
at a a point on that journey. But facing exactly the
same problems still. As when we had 300 services, we've
now got about 1500 services that, that we care about. The
rest are like, there's, there's a ton more of it
they can burn, and it's okay. We do 500 million active metrics, time series 200 million DPM and that whole way
through that journey from, from 700 to 15,000, it's always been a little
too much the whole time. And, and that story really hasn't changed.
You know, the, the scale of Atlassian, how fast it's growing has always been
the thing to keep up with, the thing to, to solve. And because we've had to react to a
lot of those things, you see that in, in our architecture, in some
of our decisions to like, fix things mid incident
as they're burning, and then they stay fixed like that for a
really long time until we can carve out some space to actually do
something about it and fix it up. And the team's continuously
improving those things. But they do lead to
serious challenges because the company wants to do
more, they wanna scale more, they wanna throw more metrics at us.
And as I said before, just a year ago, I was on the other side of the
fence a few years before I was running a project called Service Proxy, which is an Envoy proxy that we stuck
in front of all of our services. I think there was about 3000 at the
time that we stuck it in front front of. And we rolled that out very carefully.
We thought, isn't this great? We're gonna be able to provide
standardized metrics to everybody. Let's just turn it on
and see what people use. And Colby the head of observability
at the time, I was like, no, what are you doing? It's like, it'll
be fine. It's like, we'll just, we'll just turn it off later.
And so we switched it on, and then I got reorged out and
forgot all about it, . And a couple of months ago I found out
they just were doing a project to turn all those off. It's
fantastic. So, you know, the the scale side of things I think
leads to a lot of, of other problems. And depending what your model looks
like ours is very similar to that. The, the Canva model that you described
along with standardization issues and a whole bunch of
other things like that, it just results in us constantly
sort of in this reactive space. So I guess, you know, getting in front of that anticipating
that you're always gonna have scale problems, these aren't
going to go away and, and making decisions with the long
term in mind is really important. But of course, as you go through
that journey, you change leadership, you change decision makers.
And so the marketing aspect, not just out, but up as well, it becomes really important to
try and get people aligned. Hey, this is what we're trying to do. This is how we're gonna dig ourselves
outta the hole, so to speak. But yeah, for what it's worth, I still drive a car
that breaks down regularly, you know? And do you hate it? Many Fords
later? I'm still in a Ford . There you go. Yeah. Okay, let's move
on for that. So you mentioned you know, the, the importance of I guess
that internal alignment, right? And and getting people on board and, you
know, that I guess relates to you know, culture and, and driving, you know, that,
that organizational change, you know, so what are, I guess, you know, some of
the ways you know, that you can drive, you know, those changes, especially when
you're introducing new tools you know, people you know, it's, it's natural,
right? Humans are averse to to change, right? So how do you, how
do you go about, you know, driving that change you know,
getting people to adopt new tools, new technologies you know, and
have that be successful, right? There's obviously this, this traditional,
you know, carrot versus stick, right? So you know, what, what are your, your thoughts there and and how does
that work in, in your organizations? Yeah, that's an interesting
one. When I started Atlassian, the most common thing to hear
was, don't tell me what to do. Over the course of, of, of
the last 10 years though, the the realization of platform
tax when you're running non-standardized and all the things you
have to do because the platform's not looking after you, I think sort of started
to change things a little bit. And, and teams are realizing like,
we've got this insurmountable set of requests of all the things that
we have to do just to be compliant and, and secure and reliable. Like,
can't the platform do it? Yeah. If you did these things, we
could. And I was like, oh, great, please tell me what to do. And, and
so it's, you know, it's a spectrum. We're not all the way of everybody wanting
to be told what to do all the time, but there, there's a
lot more openness to it. But if I was to go back right
to the start where we had leadership talking on stage
about radical autonomy, and everybody should just do whatever
they want and be the change of seek looks like just doing whatever you like I'd
probably try and roll out a metric around like the cost to retrofit
a standard, you know, as, as we talk about what we could
be doing together, what's, what's the cost to retrofit that today?
It's zero. Let's keep track of that. And as it goes up, we'll, we'll get an idea of the trajectory of
how hard this is gonna be to fix in the future. We didn't do that. And so now there's some things that
we're able to standardize as a platform. We've, we've rolled outside cars
on many of our services, which is arguably costly, but also puts
us in control of a lot of things. We've had James Moses here, he's instrumented our Java tech
stack, for example, with O TLPs. So people get that outta the box now. We don't have to worry about
them introducing their own
weird and wonderful ways of doing things. And so
I, I think as a platform, trying to do things for the rest of the
company rather than do things to them it, it tends to help both in terms
of gaining reputation and in, in standardizing without sort
of clamping down on innovation. We want teams to be able to do new things. We don't want to get in their way
but we don't want too much internal competition such that,
like, we can't get a, a standardized view of across
services, what's going on when, when incidents are affecting, you
know, a massive service stack. Yeah. Look, I I, all of that.
Well, everything you just said, I totally agree with. And I and
particular love the idea of a metric of, of like retrofitting to standardization.
I think it'd be really hard to do, but it'd be amazing if you had it, because you can just see
that going up and up and up. I think it's really hard to understand
that when you start developing. I think a lot of people come to
development, they're like, oh, how hard can this be? I
just put a lamp stack in, I'll have the code written by this
afternoon. I'll roll it out. It's like, that's, that's cute.
That's really, really cute. Now let's actually talk about real
services, because as you grow, when you become more complex, and particularly as you move into
the enterprise space, you know, you start doing things
like, well, we need to, to have be able to be able to actually
demonstrate that we've deleted data and we need to have accounting standards
that we meet. And it becomes hard. It's just genuinely complex.
The code is not simple anymore. I slightly off track, but I, it uses me, there's a great story about how
I was listening to apparently the accounting protocols and at, if you're trying to sell product in
the US it's so complex that there are billion dollar organizations, like billions of dollars that their
approach to doing this is basically just sell the product everywhere. And then
when someone come and finds them, like, work out, whether you wanna retrofit
your accounting system, you know, your sales system to work with it, it's not actually worth trying to
like get it right the first time. And this is the nature of enterprise.
Enterprise works in a very, very, very complex space. And so it's a really easy to
naively walk in and think it's easy, and then later on you're
like, no, this isn't easy. And this is where the platform has
platforms, standards, frameworks, this is all the stuff that matters. Look,
at the end of the day, I think I've, I've kind of my key points still come
back to, we need to make sure that we're, we're going to the customer, our internal customers we're
making their life easy, and we need to make it so that there's
well paved paths to make stuff work. And look, I've seen this at scale at Google and
at Google there's an amazing amount of standardization. Like everyone
does stuff very, very consistently. And our constant complaint was people
were doing consistent like that last 1%. There's always the last 1% where
you are fighting to get, like, could everyone just do
it this way? Please. 'cause you're always
pushing the next frontier. So despite the fact that people were
using consistent frameworks and consistent deployment standards, and consistent
CICD pipelines, we were still being like, but could you please do it
this way? So it never stops. You're always pushing the next level of
consistency. But at the end of the day, you've just gotta make sure that you're
genuinely adding value and you're selling that value and making
it clear how you're selling it, why that's valuable. So, bit
of a ramble, sorry, but look, there's no straightforward answers. That is true. Yeah, I think it's
a, it's really interesting. I mean, it's something we've,
we've kind of you know, discovered ourselves as
we've evolved, right? This this need to move to
more standardization. I
mean, we're really excited, obviously the, the, the work that we've
been doing to, you know, take, you know, what we're doing. You know, we have a very good culture
internally around like dog feeding, so we get people to, to
use our software first, which helps but definitely
resonates with me of like, it's very difficult to tell engineers
what to do. You know, the, we, we have a great conversation with our,
with our sales team so our CRO Dave, who would always be
like, I don't understand, why can't you just give them money?
It's like, that's not how they work. They're not motivated like
salespeople, Dave, they, they wanna do interesting work.
They wanna be exciting work. And so it's always a, a great revelation
of it's not just that simple, you know, you have to kind of, you
know, make them, you know, want to Right want to change, right?
Which is always the big challenge. Yeah. I think like, like you said, like the marketing piece is really
important with engineers. They, what we find is engineers, they
wanna solve problems. And if, if we take the time to go and talk to
them about the problems we are facing, sometimes we'll find that they'll want
to come on board and solve it with us. Not always we, we have some
that are like, too bad. I'm, I'm solving it this way. And, you
know, you, you pick your battles, but there's certainly like that
aspect of engineers really wanting to jump on and, and solve things together.
And I think when they can see the, the benefit to the company that
makes a huge difference. But. Yeah, totally agree. Actually,
one point I didn't make, but did come to me is like there's a, there's a cultural change I want to
engineer at to Canva, which is to, to reflect something
that was true at Google, which is a level of comfort with
change. A lot of developers are like, they get a little bit set in their ways
and they're like, I know how to do this, and I totally get that. Like, they're
very efficient, they're very fast. They can make happen when you move
their cheese. They're a little bit like, come on, man, you've just broken my
path. The, the process. I was very, very fast. And they, you've broken it. One of the things I found at Google is
Google is Google Engineers are insanely comfortable with change. You
know, we made a change of our core back at Google. We
changed from GFS to CFS, so from the Google file system to the
closest file system, which is our, you know, data center wide storage
layer. We did it in 12 months, and that was an indisposable number of
exabytes of data and an undisclosable number of tens to hundreds of thousands
of projects across a hundred thousand engineers at the time. I think,
like, these are insane numbers, and we did it in 12 months. And look,
there were some complaints about it, but less than you'd expect. Like
largely people are like, it's Tuesday, it's what you do. And that's, I think, one of the key features you do
need to build into your culture. You need to get people to
the point where it's like, I am not defined by the fact that
I'm a Java engineer or a front engine engineer. I'm defined by the fact
that I'm an engineer and you
can move my cheese and I'll just be like, Hey, that is a better
space for that cheese. Good point. And that's a really big cultural
change I need to drive at Canva. That's great. So I think that's all the
the structured connections we have now. So now we'd like to to
open it up to the audience. So if there's anybody that that
has a question raise your hand, we'll bring a mic over to you
and and you can ask the panel. Thank you for asking questions. It's
always awkward to sit here in silence. I guess I should stand as well. The question I have is for yourself from
Atlassian standpoint you talked about scaling collection of metrics, is
it's just been a never ending journey. There's never been a point you felt
like you could handle the load. If you were to look back, what changes would you do to try and
get yourself in a theoretically better position? Yeah, okay. So I, I think some of what I talked
about around the standards is, is probably a part of that, right? So we, I, I guess we, if you
look back across the journey, you see waves of us observability, getting connected with the
rest of the organization, the organization understanding what
we're trying to achieve and trying to get there. And then we acquire some massive company
and they come in with a whole new set of vendors, and that's the big focus. And then we decided we wanted to change
the way our, our cloud system works. So we, that's the big focus. And so there's these like pockets
in between where we're not doing transformative change,
we're just, you know, standard evolution that I think if we
could have utilized those better to take Atlassian on the journey and, and really connect with I guess
leaders around each of the, the pockets, each of the departments around Atlassian
and get them on board with, Hey, this is where we need to go and this
is what the standard looks like, this is what we want to achieve,
this is the value for you. All of that good stuff. We've probably
been in a slightly different place now, but I think that also has to be codified
in the tooling, codified in our paths. And that's part of the journey right
now is like trying to get those things into standards that are I guess agreed for want of a
better word, aligned, topped down. When you've got our previous leadership
that wanted that radical autonomy, that was very hard. You can't drive this sort of cultural
change bottom up without some sort of alignment. And so now we're, we're in a place where we have the
opportunity to do that. So I, I, I'm not sure how well that
answers your question, but, but look for the opportunities
to be able to drive mind, share and alignment and, and
take them as often as you can. All right, any other questions?
There was a few hands popping up. I feel like I've heard a lot
today about thank you both. The, the issues that come at scale and the feeling I'm getting is
that observability is not
just something to help us, you know, debug and code better becomes
about integrity and accountability. And that can even lead
up to the, you know, the, the teams that we don't work
with, like product for example. Whereas if you build it in at
the start, like a nervous system, it gives you a tactile sense of what's
working and not working in your business and then allows you to hold the
people accountable and see, you know, which teams you wanna scale up or even
scale down in that matter. Do you, how do you guys feel about
that? Or can you comment in. Go for it. So as I just mentioned, we, we acquire businesses pretty regularly
and they come in with their own stack. It's really interesting to see what, what companies have done when they've
started later in the journey with, you know, better technology available to them
through vendors and things like that. And I think one of our recent ones is
using a vendor that we used to use, but the way they're using it is, it's
awesome for their size and scale. Fantastic. We can't roll that out to the rest
of Atlassian because it would be cost prohibitive. But I think when you're
at a smaller point in your scale, you, you have the ability to sort of set
up for a longer term future with a, a different, I guess, foundation, right? You don't have the same legacy that a
company that's been building products for, for 25 years does. And so again, looking for the opportunities that are
unique to your situation in your company and understanding your
own scale trajectory you have to make the decisions that are
best for you in at your particular time. I don't think copying Atlassian or copying
canvas ever gonna be the right thing to do because we're so far
down that, that journey, unless you are having exactly the same
set of problems, in which case, cool, let's work together, let's talk about
it and, and solve those things together. Yeah, I think it's one of the interesting
things about the enterprise space, which is that a lot of what we're talking
about is like an external cost to the product. So minimizing that cost
is how we do well. If, you know, if we could make observability $0,
that'd be great. Thank you very much. We're not really a profit center,
although having said that, I've had plenty of reliability engineers
save the company millions of dollars because they've basically gone,
did, you know, this costs money? And people have been like,
does it? And you're like, yeah, we should save a million dollars a
month by achieving that. And they did. So we could be a profit center. I think
actually we did make money last year. Usually we put those problems
there to begin with though, right? Well, my team didn't but I totally agree. Look, the,
the, the, the journey's really, really different depending on where you
are and exact details of your company. It's really hard to come up with
generalized lessons. You know, I think probably the biggest generalized
lesson I have is get people comfortable with change. 'cause Change is gonna
be necessary. But you know what? Like if you are a company, if
you're a bank, then you are not, scaling isn't your issue.
You are not scaling quickly. Your problem is basically what is
the right level of instrumentation. And if you're a company that has to run
a whole bunch of third party software, well that's a different set of
challenges. Yet again, you know, like one of the places I think that
enterprise has not done a great job yet is sharing things like, and I've
mentioned this to to Grafana, which is like SaaS dashboards. Now this is a super common problem
that everyone comes across. At some point you're like, Hey,
we'll get saas, that'll be great. We'll externalize all our, all
our problems. They'll to solve it. At some point you're like, we
still need to monitor them. They actually still need to understand
if they're delivering the service, and we still need to do all these
sorts of things. So, you know, I want a SaaS dashboard, I don't
need to solve that, right? Like, this can be solved by the community
and I'm very keen to, you know, potentially a bunch back. We've got a big Grafana rollout that
we're in the middle of and you know, there's a bunch of stuff
where I'm like, let's, let's ship that out to the rest of the
community because we'll get refinements and improvements back. And
this is the right thing to do. It's just the right thing to do.
It lowers everyone's costs. It's a, it's a net win for everyone. So. Yeah. And, and at a time when it's crucial
when you're scaling you know, there's this obsession with building out
new features and it can also help with making decisions around which one of
those you want to chase and not chase. Yeah, that's a, that's a great point. And Tom it's gonna be back here later
today talking about kind of SLOs and, and, and why those are so important, right?
To help you balance that you know, where, where is it important for
you to invest your time? Is it building new features or is it
focusing on reliability? And, and, you know, some of the, the
approaches that we have for, for how you just better make that
decision. Yeah. So stay tuned for later. Alright. Yep. It's very
similar question actually, but could you characterize
for us particularly Andrew, with you know, radical autonomy. You, you are bringing large number of
teams on or wanting to bring them on. Where's the biggest momentum or resistance
and where are the things that you've found that just dreadfully easy?
Like, there's obviously two camps. There's probably more than two,
but yeah, there's certainly a, an easy way to get things done, and
there's a hard thing, a hard way. So we've got about 600
engineering teams at the moment. And the, the problem with that is if, if we do anything that's
asking them to do something, we've worked out that's about a
million dollars a day for one engineer to do something in every team
plus or minus a bit, but, you know, a million dollars a day for, for any sort of request we make
where they have to do things. So that's generally the hard way. 'cause Not only is it that
million dollars a day, it's also trying to convince 'em that
that's the most important thing to do. We were just talking about
features versus reliability. We, we had Mike Canon Brooks tell us many
years ago that we're an and company, we do that and that it's not this
or that. And so, you know, that, that bubbles down to, like, we do the feature and we do the
reliability and we do the security and the compliance and the cost. And we
might do some dev prod as well. And so every team is sort
of under this radical autonomy is dealing with
this prioritization problem
where everything's urgent, everything's priority zero, and then
I come along and say, Hey, could, could I have some more? It doesn't, it
just doesn't work. So wherever we can, we push things into the platform,
we push things into the sidecar. Recently we've partnered with support
to help them reduce their work hours logged talking about another metric of
interest that we hadn't sort of played in that game before that we found really
interesting to solve their problem. We rolled out traces which we've
tried to many times in the past and, and failed to get sort of standardized standardization of
tracing instrumentation. But what we did different this time
is we went and instrumented a ton of services on behalf of the
products in the key SLA experience journeys that the, the customer
support teams were complaining about. And tried to sort of kill two
birds with one stone on on 1 cent. We were looking after
reliability for the, the most key key experiences. And on the other we're helping support
with the things that kill them the most in terms of their investigation time. Sometimes they'll spending a whole
week just trying to dig in to find a, an issue. We find, you know, JIRA's got something like 2000
spans in one issue, view trace. And so you can imagine jumping through
logs manually trying to find that that's just soul destroying.
And so we've got these, these opportunities that come up where
we can hit multiple aspects with one go without the teams having to do a
lot of work and they're stoked. At the end of the day, we're stoked. And we haven't told anyone what to
do. On the other end of the spectrum, we've got a standards and practices
program that's rolling out now that is sort of top-down sponsored, and I guess that would be the other side
of it is if you need to make a change that's painful, it's gonna be unpopular. Make sure you've got top-down
sponsorship and it's, it's known, it sits in the priority stack somewhere
and it's not just another priority zero, but it's something that
everybody understands and
they've got enough runway to, to roll it out. Alright I think we're outta time there, so I'd like to thank both Jenna
and Andrew coming up and and sharing your thoughts and
insights with us. It's been great. So we can just get a quick
round of applause for them. And, and thank you guys very much. Thanks for having us. Alright, so we're gonna take
a quick 30 minute break now. So we've got some snacks and
beverages outside behind the doors. And we'll be back at restart
sessions at 1215. So half an hour. So make sure you know, grab a drink,
grab a snack. We also have the, the demo booth and expert
boots that are outside. So I think there's one over in
that corner. There's some down the, down the end here. So come in and talk to us if you've
got any more questions about the, the, you know, certainly what
we've been doing at Grafana. We'd love to hear hear what you
what you've been thinking and, and also love to show you what
what we've been working on. So we'll see you back here at at 1215. Thanks. For having us.

