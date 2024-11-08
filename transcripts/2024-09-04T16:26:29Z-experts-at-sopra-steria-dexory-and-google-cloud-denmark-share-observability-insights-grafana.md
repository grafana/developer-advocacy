# Experts at Sopra Steria, Dexory, and Google Cloud Denmark Share Observability Insights | Grafana

This session delves into the multifaceted views on observability, exploring both internal and customer-centric perspectives.

Published on 2024-09-04T16:26:29Z

URL: https://www.youtube.com/watch?v=bSDcd5OL35M

Transcript: Have a couple of people here that we
wanted to invite to ask a couple of questions too just to bring us home. They'll do a quick introduction of
themselves in a, in a second as well. But we wanted to get several different
perspectives as to like what they look at towards observability for themselves or
for the customers that they work with. And we'll spend about 30 minutes on that. And as they rightfully said themselves, they are the final session
between us and beer. So we're gonna do great to
meet that bar and exceed it. So what I wanna ask first is each of the
panelists to just introduce themselves, name, role, and just a little bit about
your company. So we'll start with you. Yes, thank you. My name is Gaute Holmin. I am a product offering
manager in Sopra Steria, a large consultancy company. I used to be an observability
consultant for many years, long before it was called observability. But the recent year I've been the
product manager for monitoring and observability in our MSP space. Awesome. Yeah. Thank you. Thank you. My name is Matt MacLeod. I'm the VP of software at
a company called Dexory. We're a UK-based startup that build an
autonomous system that does inventory and warehouses, so it's sort of like a robot. We come and install it in your warehouse, and then it takes a photograph of
everything in the warehouse every day and sends it back to our system. And we have those deployed
across Europe and the US market. Nice. Last but not least, my name is Mark Lang. I'm part of the Google
Cloud team in Denmark. I'm a customer engineer
focused on infrastructure. I have a couple of decades doing what
they is now called observability, so I'm trying to put
some insights into that. Awesome. Thank you. So maybe to start with the first
question why is observability important to your business or why is it
important to your customers? If I'm going to look at it
from an MSP perspective, most of our customers are quite basic. They want to know if their
applications are up and available, which they surprisingly often don't know. Besides that I think it's
important to look at, at the business side and see what, what is important for
themanagement to see if what value does our applications give
us when they're up. Mm-Hmm. Yeah. so I think observability is, is important
to more than just the tech guys. It's important to the business side
as well. They don't know it yet, but they should. Exactly. Good. For us, the tech guys, we are dependent on actually
observing what happens out there. So we have a very, very complex platform
that's rolled out internationally. So what we rely on is just understanding
what's going on under the hood on that. And that's both stuff that's
happening out there with our, our platform in real time. But also understanding where
changes are happening to that, that allow us to perform
preventative maintenance. So it's a bit different from what
we're maybe looking at with monitoring, say web services or something like that, but we're monitoring changes in hardware
changes in the environment as well. And so key for that is to allow us to
scale rapidly by just understanding when changes are happening and being able to
get out there to customer sites before we see something like a downtime or
some kind hardware damage that is gonna impact on our ability to
deliver service to customers. So it's important both for us
from a business perspective, but also for customers as well, just being able to actually provide
that service to them on a regular basis. Yeah. And well, Google Cloud is
primarily the customers, right? So they wanna know how much time
they're down, same as Scott mentioned. So it's the same putting stuff available
,talking about what makes sense from a observability perspective, if it's built in tool sets or Grafana
other aspects that can be used. Third party tools talking a lot about
multi-cloud platforms, hybrid subs, so capturing your application the
right way. I think we've had a good, good part of piece of sessions
here and actually focus on, on getting it right and
it's very difficult. So we try to assist from an easy
and simple point as possible and putting that towards the customer. Awesome. Okay. Good. Matt, maybe just start with you
then for the second question. What challenges do you often hear from
customers or internal or external? Like what type of challenges
do you typically hear? I mean, for us, the biggest challenge for me is that
our service drive themselves around and most other peoples don't. So what we
find is we have connectivity challenges. We have lots of different
hardware versions out there
in the field as well. So, you know, we may find
that we have, you know, every single robot that gets deployed
is custom in some way for that environment. So for us, we are making sure that we can gather
a consistent set of data from all these things that we can't necessarily upgrade
by just pushing out a software release to them making sure that we can connect
with these devices that are deployed in the field and get regular
updates from them. And also just generally the volume of
data that we need to gather as well. We need quite high resolution metrics
to monitor things like power consumption or, you know, like performance of
motors and actuators. So for us, the challenge is how do we take those
models that are quite well-studied and maybe web services or other
applications and apply them to the, the sort of like detailed data
that we need to get from the fleet. Yeah. And from our perspective is just making
sure that customers actually can get the most out of the cloud without actually
putting too much effort in there from our operational perspective,
so ease of use and, and integrations and collecting as much
usable data as possible. Internally, we have even more metrics
than we actually use for good and bad. Dissecting what's relevant is one of
the principles we use in in the SRE practice internally as well. So the
SLO and SLIs that you talk about here, they need to be pretty aligned with
what is the user journeys and the experiences on the outside, and that's also echoed down
into the customer aspect. Yeah. many of our MSP customers
have big challenges in, in having, they don't have the new cool
container based applications. They have old silo based C++
Oracle applications that they, they really don't know how to
monitor them. They don't know how, how to make sure it's how, how
do we monitor if it's up or down. So that's most, many of our
customers' biggest chances. Okay. Cool. And maybe one question
for you specifically. How do you, how do you help customers? We spoke
a bit, quite a bit about it today, but how do you help them on their journey? Yeah, we we do something when, when we take on new MSP customers
we do something we call a service decomposition. Mm-Hmm. Where we, we interview them and find out where
are the end points in all these old applications that we can monitor to make
sure that we know the application is up. So we create instance when, when this thing is happening. Everything else is just trends
and stuff we can use to, to kind of troubleshoot. But, but we do a service day composition
where we mainly draw a drawing of the application and find out just where do
we put the, put the needle. Yeah. Okay. Okay. Nice. And then maybe for
Mark, let's start with you. How are you, or the question
is double. So on the one hand, how are you organized around observability
or how the organization of your customers? Right. So our concepts are based on, on SLO,
so service level objectives. Mm-Hmm. And then we drill down from there
based on the SLA principles, that's, that's kind of the, the narrative
we wanna put out. So it's made, it made easy to actually utilize the
metrics we have available and put it towards error budgets and
be getting like a visible, visible aspect all the way to business
that, okay, this has an impact X, Y, Z. Now we can do certain updates depending
on, on the applications and so on. So we really try to highlight that. Well, our own practices we use internally
is the same tool sets we, we add outside and OpenTelemetry
is a big part of that. Yeah. So Novo people nodding. Yeah. So we're trying to do all the practices
and all the stuff we're advocating and that echoes all the way out
into, into the frontline. Yeah. Let's do this. I think for us we are obviously
much earlier stage than Google. So our challenges around organization
are much more about how do we get access to that platform as quickly as possible
to an organization that's scaling rapidly. You know, so thinking about
what Pierre was talking about earlier, we're quite federal already in the sense
that we do have a central platform. You know, we use Grafana Cloud and
everyone is on board with that, but individual teams are still really
responsible for their journey into that system, like how they're building their individual
contributions into the platform, how they're building their dashboards. So there's not really sort of like
a central operation for us yet. So we do enforce a culture of
metrics from the get go and we encourage and empower people to add
metrics into that platform as much as they can. So for us, it's really about just making sure that
we can open that pathway into getting metrics until we get to
a level where, you know, maybe we can centralize that
strategy a little bit more. But really just now it's
focused around scalability. Yeah. I think I'll use an example where I was
hired as a observability consultant. Mm-Hmm. Where we were developing this
sauce solution for tens of thousands of users where we
appointed an observability champion per development team. And we put them in an observability
squad that after every, every sprint, we looked at the observability dashboards
and looked at all the traces looked for exceptions long response
times and, and focused on them and prioritized what to, what to fix. And then we deployed this application
to what we called Wave Zero was, which was a small group of users. And
then we did the whole thing again, where we looked at all the
traces and all the metrics. And then we did this every week during
the sprints where the observability champions got together, looked at this prioritized and
moved it to the developers. Okay. And then maybe
just say with you, like, how does your view on the journey
to cloud relate to observability? Well, the journey to cloud makes
things even more complicated, I think. So observability is very
important. It's important to, to ensure that we have the metrics in
place before we move so we know what to measure when we move. Okay. Yeah. I mean, definitely from
our side, you know, we have a huge number
of  devices, which is quite a different
proposition from, from some of the cloud implementations
that we might otherwise see. So for us, it's about how do we start treating
like a fleet of distributed devices as something like a
distributed cloud, you know, kind of taking a lot of those lessons
from cloud observability and then applying them across a fleet of devices
that are distributed. So, you know, it's trying to make sure that we have
things like a similar posture for collecting metrics and logs from both
the relatively small number of cloud services that we do have and taking those
lessons and applying them to a fleet of hardware devices as
well. So kind of trying to, trying to have a nice uniform
platform between them. Awesome. Mark, if you can also include
a little bit about how then GCP would, would help on this journey, that
would be interesting to also hear. So from the cloud journey aspect, I discussed multi and
hybrid cloud solutions, so looking at broader aspects
of vendors rather than just one. So we have a subset that makes it readily
available to get metrics and create your own customized ones, depending on the user journeys
and the aspects you have in that. And if you have metrics readily
available, you need to use them. But we also work a lot with third party
vendors to, to do something on that. And we actually have a majority, specifically in Denmark using
Azure DevOps as their base. So we try to integrate as much as possible
and assist on how can we make this readily available. So yeah, there, there are a lot of tie-ins all the way
around, but generally I would say we, we try to understand the, the scope and assist as much as possible
to give this give it relevance rather than yeah. Being stuck in Well,
you're not using GCP then. Well, you are on your own, right?
Yeah. So we tried to do the multi as, multi-cloud aspect on, on that part. Awesome. Okay. Really cool. Maybe moving a little bit more
to the organizational side. I think that was also a topic
quite often discussed today. So when you look at your
customers that you work with, how are they typically
organized around observability? I think most of them typically
aren't   so we try to help them. We are, we have organized ourselves in, in
in different product organizations. So, so my group is called
the right control. So, so we basically try to help the customers
by offering them different levels of, of security where we can help them
with, with the tools and the processes. Okay. For you. I mean, our whole job is
ultimately observability, but in the physical space instead of
the, the digital space. So like we, we call that internally the
observability gap, you know, that, that customers have between data
that comes in and data that, that, that goes out the other
side. So, you know, we're, we're pretty familiar with that from,
from the logistics industry perspective. And a lot of the stuff that was, was
being mentioned earlier by DFDS, you know, is, is a challenge for, for customers just in the practical
space as well as the observability OO of the data systems. So, you know, we not
only try to, to solve that for them, but to provide exposure about what
we are doing to help them with that. So a lot of the product
that we offer is both this, this kind of like version of physical
observability and then the sort of information that goes along with it. How often are we running through their
warehouses? How are we collecting data, how are their systems working and
how, you know, ultimately the, the goal for us is to provide insight
into how accurate their systems are representing the state of the
environments that they have. And so what we want to do is expose as
much data as we can to them to make what we are doing observable as well. Yeah, and I think I, I go caught on on,
there's one that maturity is sparse on, on a lot of these topics. So a lot of very few have a lot of
experience and a lot of focus on that and and whole other aspect is that
they wanna be educated on, okay, what's the best practice?
What do we do here? Actually learn from how we've done
things and put that into the aspect of, of their organization. And I think Pierre
alluded a bit to the, to this as well, like, people and culture
is a big part of this, and I have in common understanding or
at at least accept or disagree on some aspects and create the observability
platform that you need. So you'll start at some point and then
you'll mature and depending on where your your organization are, then kind of
embrace it and then move on with it. Cool. Matt, maybe one
specific question for you what were important criteria that you
looked at or look at when you look at in terms of choosing tools,
platforms and partners? Definitely openness for us and
flexibility in terms of what we can, can do with it, you know, so, so
just being, I, I'd say both that, both the openness, the stuff like open telemetry is really
helpful for us because it lets a team that isn't gonna have a
lot of coordination at our
stage of a scale up know how they're gonna send metrics
into a platform. It, it reduces the overhead and burden for
us but also just giving us flexibility in terms of being able to switch to other
platforms for telemetry if we need to do that, or if we need to work
with other partners as well. And secondly on, on that, just being able to deploy to
lots of different cloud systems. So we will have a variety
of customers that, you know, Google is not going to allow us
to host data in AWS for them, and they're not going to allow
telemetry to be in there. So we need to make sure that whatever
solution that we have is gonna work across multi-cloud environments as well. Awesome. Okay. Final question
for the three of you. So if you have one recommendation for
people in the room embarking on their observability journey what would it be? Organize. As simple as that. Whatever. I, I will echo
what, what we just had. However much data you think you've got, you've probably got roughly four
to 10 times as much as that. And yet probably 50% of it
is never gonna be touched. Don't just buy a big full
stack observability suite. Start small with some metrics
that total interest of, of everybody from development
to management and, and build small MVP
dashboards that triggers their interest. Okay. In that case, I might
have one more question. I think we went through
this one relatively quick
compared to the other ones. There's more few future
looking then, right? If we, if we look at the next developments in
terms of like, vision for observability, this can be for your customers,
you or, or generically. What do you see there and how do you
think that will impact the business? Yeah, I think I think we, we need
to build more observability that, that gives value to the business
side so that they get interest in investing in observability. I've had quite big success at a couple
of projects where we built dashboards for the CIO based on, on monitoring data. So I think that's important. Okay, nice. Yeah, we actually see a really similar
challenge for that. So, you know, we go through quite a lot of
maybe due diligence processes, questions from investors and
questions from customers. And what the business wants is a strategic
answer to things like operational lifetimes for devices. How
often are they out there? What is the return on investment
in the customers we've seen? So giving them the ability to, you know, kinda create their own
observability dashboards for
that sort of information is, is kinda like one of
our key things as well. Yeah, I think I'll echo some of this. And, and also I see that the future of this
open telemetry EBPF looks amazing, really looking forward to see what's
gonna come out of that. So yeah, I think that's, that's the focus that trying to be as
transparent as possible and use the tool sets that's that's relevant,
but anchor it in business. Exactly. Awesome. Are there any questions from
the audience for the panel? And I can start running the mic
around her. There must be quite, we have three people here,
there we go. Oh, that's nice. I got a runner for myself now doing
the whole session. Sorry. Sorry. You . Could you maybe talk a little
bit about manual instrumentation instrumentation of code
versus order instrumentation? Where do you see benefits
what do you see being used? I see that, I'm seeing that for, I'm
still talking about the business side, but I, I see that manual instrumentation of code
can be very useful to build stuff for the business. You can't get that
automatically. You, you need to, to make the developers put in, in,
in the right metrics in the code. I would also say that probably 90% of
the junk metrics that I have are the automatically generated ones. So while
they may seem useful on the surface, and I'm absolutely certain that for
some applications they are where you're looking to shave off very small
amounts and you're very concentrated on performance. For us, they
end up being noise almost, and we end up spending money
to process and look at them. Well, internally, we, we use a
lot of manual instrumentation, so like automated metrics doesn't
really cut for us on a lot of aspects from a customer perspective. It seems to be the same thing that they
need to generate some kind of metric out of a lock aspect. Y alluded to this 70% CPU
usage and so on in locks, simplifying some of that aspect
so you don't have to like, save a lot of locks and pay
for that amount of data. Simplifying a lot of the structure and
then what actually you need to save. So yeah, manual instrumentation in code really
makes sense because you can simplify the general infrastructure and,
and optimize your cost. Thanks. Any other questions? I have a question. Yeah. Cool. You mentioned Gautethat you formed a, a squad of observability
into , right? So I'm thinking, I'm curious about how who has been driving the, probably the proposal
and the, you know, the, for me, the culture around this? Is that something from the management
or do you have any sort of cultural embedded in the, in the company? I'm
just curious sometimes like you feel, you feel there is business assistance
or some, some sort of this kind of, you know, in injustice, you know? Yeah. Yeah. I, I had this idea of the observability
squad and I think I spent almost a year convincing management that
this was something they
needed to, to invest in and, and let the observability enthusiasts
or champions as we call them let them spend time on this. So, so yeah, I needed to go through management
and force it through. Yeah. Okay. Any other questions for our panel going once, twice. Big thank you to you all panel. Thank you.

