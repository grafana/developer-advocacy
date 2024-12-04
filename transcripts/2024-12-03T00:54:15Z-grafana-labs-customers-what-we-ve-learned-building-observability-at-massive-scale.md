# Grafana Labs Customers: What We've Learned Building Observability at Massive Scale

An in-depth conversation with a panel of observability leaders from Sky, Just Eat Takeaway.com, and BlackRock. The panelists share stories about their organizations’ observability journeys, their perspectives on scaling observability across an enterprise, and their opinions on the current trends in the space.

Published on 2024-12-03T00:54:15Z

URL: https://www.youtube.com/watch?v=WUyzZ-qCNyA

Transcript: Alright, so good morning
everyone. My name's Wayne Gin. I, I'm here at Grafana Labs. I
run our product marketing team. And so what we do is we do a lot of
the content here that you see for the sessions a lot of our things on our
website and just help our product teams bring the, these new
launches to the market. The other thing I get to do is I get
to chair our customer advisory board. So what that means is that we have a, a
really privileged group of folks, or we, we are privileged to have a group of folks
that advise us on a product strategy, advise us on, you know, things that
we're trying to bring to market, and really just, just be there as a sounding board
for us to just make sure that we're, we're hitting the mark and serving
our customers in the right way. And so these guys have been
on our customer advisory
board for a little bit now, and it's been awesome to, to get to know you guys and just
understand like where you've been in your journey with observability and just to
help you guys along that way. Right? So they, they've graciously donated
their time here to provide some insights. I'm sure that they have many battle
wounds and scars to, to share as well, but I think that based on the title here, they've all been doing observability
for several years now and have reached a point of scale in their organizations to
share some, hopefully lessons learned. So we wanna make this interactive.
There is a QR code here, so please, just like yesterday you can write
some questions in the Slido. We also will have some
mics running around. I've got a couple questions prepared, we'll just get the conversation going
and then we'll turn it around to to q and a. Okay. Alright. So real quick,
just do a quick little intro. Tell us about yourself, your
company. Not everyone knows, like, what each of your businesses does. ING Director for observability
and automation at Sky. So, sky probably two people here who
don't know what the company does, but we're providing entertainment
and communications solution to millions of customers in
uk, Ireland, Italy, Germany, and for some JVs also in,
in many more countries. Been with a company
for about 27 years now, almost recently, looking after a function
that is doing alerting, monitoring, observability, operational data,
and, and a bit of enterprise as well. Great. Okay, Alex? Yeah, so I'm Alex senior technology manager
for Reliability Engineering at Just Eat Takeaway. Been at Just Eat for
eight, just over eight years now. So just Eat Takeaway is a food
delivery and grocery marketplace. So you can get all of your Friday
night takeaways and other things, iPhone cables and the
like. Yeah. we look after, or my teams look after all of the
observability and reliability. So Cal engineering load testing
and all of the telemetry data. Awesome. So Hi everybody. I'm Olin. I've
been at BlackRock about 12 years. I had a couple of, couple of roles, but most recently took over
observability for our Aladdin platform product. So Aladdin is kind of our investment
management platform for institutional clients. You know, everything
in the money management process, trading compliance portfolio management. But my team is focused
on kind of similar to, to Robert and Alex focused on the
observability of that SaaS business and making sure that we are kind of
building to the, to the title of the, the presentation, right.
Building for scale in our, in our monitoring and
observability tools. So excited to, to chat with folks today and just wanna
shout out amazing keynote yesterday, hopefully people this morning really
excited about the stuff that we saw, but. Happy to kick us off this morning.
Yeah, great. Thanks den. Okay. Why don't we start with a question here
just to, just to get things going. So, observability, it's a pretty big word, means a lot of things to different
people, I think where I sit in marketing, it's been used in maybe the
not purest definition ways, but when you think about observability
in your organ organization, how do you define it? How do you
think about it? And ultimately, how does your stakeholders
or leadership think about it? Maybe we start with you, Robert. Yeah. Observability for me is bringing
together in one place the visibility of all the, the operational state of
all of the, the various services. We are very distributed organizations. We have literally more than a
hundred technical teams who support some part of the component.
It's SE teams, DevOp teams, application support
teams, and historically, therefore had their own responsibilities, often coming with their own
instances of some, some tools. So these hundred plus, if I interpret it as instances
of tools that could be us. And but doesn't help when you have
more complex issues that spread, different technology domains, different teams where we
then have of calls with 20, 30, 40 people sharing
screenshots of graphs. And that's just a very inefficient
way of working. And so for us, the, the main objective here was to
address that and really bring in one place everything that any, any tech
team, any support team needs to know, needs to see down from the, the very, very low level details up
to some  and
asset laws for the services. Great. Yeah, I think it, for us, it's really
around understanding the behavior of the, the platform, both when it's running well and
when it's not running quite as well. Being able to see what the platform's
doing gives us the the chance to help the business to make product
decisions on what we're doing how we can add new features,
how those features are behaving. So it's really allowing us to make
or get business value by using, using the tooling to understand
the behavior and how, how the platform's being used. Yeah, I would echo that. I think
the other thing that for us, like there's a very practical element
to observability, which is, it is the, the tool set kind of in
a crisis, right? So the, the things that operator, operator
teams, operational teams you know, we have a group of folks called
the command center, right? This is their lifeblood, right? You
talk about the screenshots or the, the views that are getting
shared around, like, that is a very practical element of
just being able to enable folks with the right information to, to be able to respond when we're
seeing un un unexpected conditions. But I think aspirationally
where we want it to be is around being ultimately an enabler
for the development teams
themselves. Like I think, I think observability needs to be
embedded all the way left in the process, right? As soon as you are
developing the, that next feature, that next capability. So I, I wouldn't
say we've, we've completed that journey, but I think being a core tool that
developers are thinking about as early as possible is where you're gonna
get more of that business value. You're gonna be able to, to change the
conditions that the tools are running, improve the performance, or
even just understand you know, things like AB testing and, and,
you know, K six for example. Those kinds of tools are
really valuable early. And so I think when we think about
observability we wanna be as early as possible Yeah. In the developer
process. So that's a big aspect. Great. Yeah, I think it's that big thing
about being as preventative as you can, right? So let, let's understand using load
testing that you can link that in with your observability platform to
see as part of your pipelines are, are you gonna have a problem? 'cause You, you don't wanna find out in production
that something's gonna break . So yeah, let's find that out
early. So, yeah, definitely. Great, thank you. Yeah. So Alex, maybe
we start with you here. You know, we have a lot of questions that we
tend to get is how do we measure observability? And we all know sort of the classic
definitions of MTTR and when you're in an incident, how to improve
that whole process. But based on some of where
you're going with observability, what are some other interesting ways
that you are measuring right now or considering measuring? So I think stock, so yeah, reducing MTTR for our business
is absolutely massive. I think anybody that's ordered a
takeaway at home when you are opening up and out and you see a little
spinning wheel of death and you are not getting your takeaway and you
are desperately hungry, you are, you are not gonna hang around and
wait for it to come back again. You are gonna open up one of the other
I'm not even gonna say the names, but one of the other available
food delivery platforms. Very strong signal, right?
Hungry. Yeah. Boom, . Yeah. You, you are hungry, you are just, if
I'm not getting my food, that's it, I'm going somewhere else. So, yeah. So for us being able to
reduce that time that if you are having an outage, the minutes cost a lot of money. So our, our business is really, really down to being able
to get people access to their, their food order
quickly. So if we are down customers aren't hugely
sticky Mm-Hmm, , they will go and use one of the
other suppliers. So yeah, for us, reducing MTTR is just
massive. And having a, having good strong observability
that allows you to get to that answer of where the problem is
quickly hugely important. So being able to have good
observability with the really exciting onset of the generative AI
and all of the AIOps that being announced and with the
the acquisition that was, or merger, however it is that was
announced yesterday, absolutely amazing. It is just how can you get to that
answer quickly? Yeah. How can you go, this is the thing out of all of the
alert noise that you're getting. Yeah. This is the thing that you need
to look at. Yeah, great. So yeah, that's hugely important. I think. I think also like we, you know,
we talk about scale and observability, and I think the natural focus is
outcome based, which it should be, and the business will be
focused on an outcome like MTTR, but we've been thinking a lot about the observability at scale is also about
understanding the entire breadth of the platform. And I'm sure many
folks in the audience can, can kind of understand the challenge as
the complexity of the software systems that we're running are just
ex exploding, right? I mean, sure there's models and
other pieces as well, but even thinking about cloud
providers and, you know, multi-cloud setups and you know, where you're hosting data versus
where you're hosting instances, that kind of thing requires you to
have eyes everywhere. And so it may be, it may be obvious in some sense, but making sure that every
aspect of the stack you know, thinking about all the way from, you know, client network connectivity all the way
up to an application SLO and whether we're breaching an error budget, like that entire set of
services needs to have eyes on it from an
observability perspective. So do we have all that data that we need? That's a pretty core question that
we need to make sure we measure. And the business is
evolving rapidly, right? We are always trying to catch up with
folks that are building the next great feature or the next great
capability on Aladdin. We have to be ready to monitor that and
to partner with them to understand it, right? So I think there's a, there's a breadth of stack component
in addition to an outcome measurement, you know, both matter, but if there are areas of the stack that
you don't have eyes that can be a real challenge when, when things you
know, make it to production, make it, to make it to scale. Yeah.
And then the infrastructure. It's, it's getting more and more
dynamic and quicker, faster change and Ephemeral resources that we
need to understand to set. It's a lot more complicated as well, for
sure. I would throw a few more metrics. So one is effort, so to
investigate an incident. So also adoptions. We have some internal maturity
assessment where we see the we have individual teams, individual services stand with
a goal that if I have the, the gold standard then we will achieve
the eventual outcomes of mt art reductions and, and so on. Yeah. So a lot of, lot of
different ways to measure, right? So it depends on where you are
along that curve. So let, let's, let's start with you Olin here. As you've thought about your
journey so far of scaling, and we talked a little
bit about this yesterday, is how do you think about those, the
biggest challenges along the way? Because I think your, your
organization's a little interesting and, and where you've gotten it to, right?
So maybe share with the group here, what are some of the, the
challenges you've seen? Yeah, I think you know, this
is a story like you know, I heard from several
folks at the conference. So I know that I'm not alone
in this, but I think where, where I came into observability,
it started to answer this question, but I think for the organization,
we began with a, you know, a focus on open source
Grafana and Prometheus, right? And I think a lot of folks
started there. But it was really, it became a success and that
success became a problem in terms of the scalability of the solution
that we could, we could run with, with the teams that we had.
When I came into the role, we had started the process of leveraging
Grafana Labs Cloud to help us with that scale. And that started to
pivot us. I guess you could, you could steal a little bit from,
from Raj yesterday in terms of the, the three acts, right? So one act is you need to be able
to scale the observability itself. If you're worried about the
reliability of the data, or you're worried about trimming
the data because you, you, you're, you're unable to retain it and use
it. You've lost the value already. So then that second stage was leveraging
the value from something like ref funnel labs cloud in terms of the
feature sets, in terms of you know, distributing it to thousands of users
to internally and then kind of building the capabilities on top of that. You
mentioned the maturity model, right? Like, you know, that that kind of
approach of your bronze, silver, gold is really essential to make sure
that once you have those thousands of users actually using the platform. And then I think we're heading
into this third stage where the, the simplest form being
the MTTR, but like, how do you measure that value that
that's coming out of that platform? That is where you know, almost intro inspecting or meta
inspecting the observability stack. Here's where it's, here's
where it's providing value. Here's the teams that
are doing a great job, and they are reducing their
you know, incident time. Those things are the third stage
of scaling challenge. Great, we've solved the data problem,
great. We've solved the, the tooling and platform
capabilities problem. Now how are we measuring and
showing value back to the business? And I think we're, we're always gonna
focus on that. That's, that's a, that's, that's, you never, it's, it's one of those problems
you're never done with. But I think that's where we've, we've
had those first, you know, challenges, hiccups, whatever. And now
we are, we're focused on new, new areas. And I, I think you guys have
had some of those similar experiences, right? So it's very much similar. So one, one thing perhaps I I wasn't so clear
at the beginning of the journey is that there are different reasons
why people use the platforms, why people come on it
and onboard. They have, they can have their own intrinsic
reasons that are valid for that team to achieve something that they want to do, but to do it in a standardized way that gives wider benefit is quite different. So I think we've been through
this phase of kind of friend success driven adoption, but now going through making it at
most standard is making sure that we, we really get the original outcomes
that we wanted to achieve from that, and not just people onboarded
and use it. And yeah, I mean, there were some great
users. Yeah, I mean, some, sometimes it's completely surprising. So one team used it to measures as some S3 storage bucket usage
for the store films and achieved very significant
savings through that. So that wasn't planned originally.
It's a great use, right? But still, we shouldn't lose sight of, of what
we originally intended this for. And, and that's a bit harder to achieve. Do. You think there's a tension between
the standardization and customization? 'cause I feel like the history
of Grafana has been like a, the platform is immensely
customizable, right? The whole dashboarding workflow and all
that. Yes. But it sounds like you're, you've, you've kind of pivoted a little bit and
thinking about those standard flows and those more opinionated flows, right? So
there's a little bit of tension there. Yes. I, I think so. And I think
to have more availability of, of opinionated views is, is
the right direction to go. Not necessarily mandating it, but going towards having that
available in, in the toolkit and, and driving it. Where, where are you on that journey? So I think one of the, one of the problems that we had was
which actually I think is probably something that would be
true for a lot of people, is when you start off on
your observability journey
you don't really have many standards in place. And you
are just, here's a bucket, throw everything which is absolutely fine
until you hit the sort of hypergrowth hyperscale bit, especially through startups that
you just end up spending your, or your on-call people spend up every
evening trying to stop your observability platform from falling over. Yep. Tough weekends. Yes. Yeah. That is what we went through. We had this self-hosted Prometheus
and Grafana stat, sorry, graphite stack C stacks, and you are, you are just trying to hold absolutely
everything that's being thrown at you. So yeah, being able to, when we moved to Grafana Cloud and
being able to send all of our metrics, that stopped us having to look after
these massive great big clusters of basically just looking
after storage. So yeah, being able to move to Grafana cloud
really, really supported us in that. So yeah, I think the being able to set standards
hugely important so that you can whether or not you are looking at
opting into what you want to send versus just sending us everything. And what does that
engagement model look like? Like is that meeting with
individual teams? Is, do you guys have a method of like
publishing out something? Yeah. It, it is really about
understanding what your, what your teams need
from their observability. Our dev DevOps teams are really good, and they understand their observability
platform right from the, the, the get go. So they, they know
what they need, but there is a, there is a huge education
piece so that some engineers, you need to tell them that they cannot
just send absolutely everything . The adaptive metrics
really huge. If you're, if you're not alerting against something
and you're not graphing it do you really need to send it in some cases, yes. Mentioning that is really
good to have a almost a, a data lake of observability
telemetry data, because sometimes you don't quite know
that you've got a use case for it yet. But there are certainly
some things that you just, some metrics you don't need to
send, so don't send them. Yeah. It. Was like these, the hello world example
yesterday, half, half a terabyte. Yeah. You don't, yeah. Probably
don't need those. Yeah. Don't. Need that . Yeah. And you get lot, you get lots of interesting
development techniques where you might block sending debug
logs so people change their debug logs to be info and send
them anyway, . So it is being able to catch some
of those nefarious challenges. All right. So let's go to a
question from the audience here, which was one that's similar
to what we, we had planned for. What are some of the most impactful
mistakes you've made during your journey with observability? So lessons learned,
mistakes along the way. What, what, what can you share with the
group here? Maybe Robert. Or. With one false start with
labeling. So it took one, one particular initial approach
of, of our labeling standard, and then revamped it so that, I
wish we hadn't done that. . . Okay. Needed a take two. Yeah. I think maybe not a, maybe not
a mistake. Like pivoting the, the, the question slightly. I think one
of the really interesting things is, is finding the right initial audience. You mentioned that initial kind of
startup, almost startup like stage, right? Where adoption is your key
measure, your key metric. And I think what we found is early
on we attempted to go very broad with those set of you know, folks
that we, we brought into the platform. And what we ended up seeing is
much more of a power user curve where a small set of people internally,
you know, and, and you know, I would shout out you know,
like kind of that SRE function, especially that partners with us, those power users have an
outsize impact internally. And I'm talking about, you know, single digit percentage points
of the overall user base, but they are driving the
outcomes for many of the teams. They are watching the presentations
and panels at conferences. They are contributing back to the
open source. Like those, it's, it's, I think enabling those power
users early on is something we, we ended up having to hustle to
do because they are doing quite a bit of education and honestly
you know, Wayne's job that, that marketing piece internally,
right? And, and making sure that, that folks are excited
about the stack that, that the platform team
is putting together. So I would say really
focusing in on a core internal audience that helps you evangelize really
makes a difference when you're then going and expecting other teams
that have less experience, you know, you could bring those power users
to those engagements and it really, it really helps get a footing in
places where folks aren't, aren't. I couldn't agree more for with that
one. It was our approach as well. So that's an initial team that was
already familiar with the technology, but very open, very collaborative
in, in attitude as well. And and then we were able to
show some initial results based on those PTR metrics, for example. So we had something really valuable
to show. And then they are, they're, they're great champions. So if you're
watching this, James, hi, . . Oh. It's, it, it has been fantastic. And, and that's really driven adoption
and also convinced some of the, the teams that were really
skeptical initially. Yeah. I, I think engineering
engagement is really important as well. So not just going after the, you know, not trying to do everything in Mongo
and trying to boil the ocean that making sure that you are creating something
that your engineers want and need. There's a few times where
we might have gone down the, the route of if we build it, they
will come mm-Hmm, , and then you build it, you offer it, and they go we don't really
need that . So yeah, engineering engagement
make sure that you are, you are creating something that your
engineers want to adopt and want to use. Got it. Yeah. Just double clicking
on that a little bit. How, how have you done that internally,
the, the marketing within? So how do you get more engineers
aware, adopting, trying things out? I think it's case of finding
those power users. So you, you start off with a,
a small group and they, they evangelize themselves as
part of the development community. So they'll, they'll show off
something that they've done. We have a a monthly what we
call operational excellence meeting where all of the engineers that
come together we go through lessons learned for any instance
that we might have had. And also we have teams that, that show
you something that they've done. So you are, you are able to have your power users
talking to the rest of your engineering community and really showing,
look at this really cool thing, and it's helped me get to a root
cause of a problem quicker than Yeah, it used to. And then people
start contacting, you go, oh, I saw this really cool
thing. How can I get. Involved? That's interesting. We have like an office hours concept
that's very similar, right? And the goal, we've actually brought Grafana
to a couple of those as well, but the goal is to kind of you
know, show not tell, right? Yeah. And the more that you can the more that
you can engage people kind of where they are and bring it to a use
case that's, you know, say, important in the trading space or
in the compliance space, right? And, and demonstrate that then people can
start making connections to their other business lines or their product lines,
right? Yeah. So I think bringing, I, I also think generally we've taken a, a pretty strong view lately that there's
a community element. And, and again, I'm not trying to sell
everybody con per se. I'm just saying that I think collectively,
like in this room, for example, the amount of expertise is something that
I think we all should be interested in tapping into more, more collectively. And I think there's real
value in figuring out not necessarily the right way, but strong effective techniques to
monitor certain kinds of systems, right? I think pave paths are really,
really important in this space. So I think we're seeing that that's
another way to engage those teams is to say, listen, we think you should
have A, B and C from, you know, an SLO perspective and give
people data on, you know, who, who is far along in that journey
and who is less far along. It's that maturity model kind of concept. I think that's really important to help
teams know where they stand and then have the power users or the, the examples or the paved paths that
they can go on. Yeah. Where this doesn't, you know, it, we, the last thing you
wanna do, I think, and we've talked about, we talked about this last
night, like, you do not wanna you do not wanna have this be yet
another task on the task list. You want to turn this into
an enabler for those folks. So as much as possible bring
it to their use case means, oh, this actually helped me, this
actually help our, our product line. So trying to get out of that zone of this
being yet another thing on the list is pretty Important. Yeah. We've also set up a structured
internal community within sky of a nominated observability
champion, because I mean,
it's a complex organization. Yeah. So we, we couldn't bring all
engineers together, for example, something like that.
It's, it's impossible. So we had nominated and then regular
sessions where we demonstrate show and tell of what people have achieved and
that those sessions really have sparked and, and great interest. Yep. Yeah. I think having we have guilds all over
the place and jet for all different manner of things, and yeah,
we have a observability guild. People come together 'cause
lots of engineers have got a, a real love for observability. I mean,
it helps their day job. So yeah. They, they want to get involved and
they want to support the journey. Yeah. I love that. I'm gonna
take a note here. Guild, we, we don't usually say that as often in
the states. It sounds very, very fancy. So we're gonna start
using that. That's Yeah.  to get more people to join. Okay. So there's a lot of questions coming
in for the audience. This is great. I'm gonna try to theme some
of these a little bit there. There's a few questions around org
structure and org dynamics. So Robert, this is, this is one for
you. As a telco provider, how much overlap is there between
the NOC and observability functions? So my, the telco functions mean they all
have their own character. So I, I, I wouldn't say that we, we see them in, in the same way among responsible
for both sides of things here. And yes, there are specialist solutions
that look at the telco world equally, it's getting more
and more into a, an, an Kubernetes app deployment world
where telco solutions are really deployed like enterprise services.
And for those solutions, we, we apply the same approaches of, of
monitoring, of, of observability, of dashboarding that, that we do in,
in the rest of the enterprise world. So it's almost like we splitting our, our telco state into the kind of
modern application side of it, and the more classical telco
device side of things that, that are just dealt with through
their own device managers or, or specialized telco folder and
performance management tool. Okay. Got it. Yeah, it's pretty
industry specific there. Right. What about you guys? Like, is there interesting ways that you've
organized observability teams or have it, has it shifted over time?
And how do you think about that? I think it, for us,
it's definitely shifted. Originally we had a platform
engineering team that kind of did absolutely everything that, which meant that a lot of things would
not get as much love as they needed to because you can't do everything. And when you're looking
at prioritizing stuff, something's gonna have
to fall by the wayside. So we made an organizational
change where we split out platform engineering into its
own sort of components. So we have a reliability team that is
split out into platform assurance and observability. Then we
have A-C-I-C-D team. We have sort of a platform
infrastructure type team. So you are then able to focus on a specific area of your, of your
platform, and that allowed us to move, move a lot faster. Yeah, I think one of the
interesting things I, the, the, the team structure I think has,
has been around for, you know, quite a bit of time. I think one of the interesting things
we're seeing is we've invested a lot in observing lower and lower
down into the stack. So I think a lot of folks think of
observability and they think of, you know, a top level SLO for, for an application. But the more and more we can collect
from the lowest components in the stack, the less people have to
instrument themselves. And I don't wanna step on the presentation
coming up next, but I know there's, there's more great work on the Grafana
side in terms of thinking about how to go, how to, how to monitor at, at
deeper levels. But organizationally, one of the things we're seeing is if you
have a lot of these signals and you've done a lot of the, the, the groundwork and you've brought that
into an ecosystem like frontal labs it almost starts to become
more of an SRE or an engagement challenge than it does an
operational platform challenge there. There's always the platform to
maintain, of course. But I think what, what I'm seeing with my team is we are
starting to think about going out into the business more and more and,
and bringing best practice, bringing the right you
know, approaches or, or, or standards and, and sitting kind of within the business
and trying to partner very closely, because that's a way the business will
get the outcomes they want. You know, the, the MTTR reductions, the
other things we talked about. But they will also you know, we will, we will have the partnerships and we
will then have more of those established paths as we wanna say, roll out
a new feature set, you know, oh, we want to introduce, you know,
profiling or something like that. We have the partners that we can
work with. So I think from a, from an org perspective, starting
to see us move from that, that platform ownership more
exclusively to being now more of a, a team that's willing to be you know,
embedded in the org is really, I think, gonna be an enabler for the
next, like, stage of our, of our. Growth. Yeah, I think that's something that we're
looking at doing is once you are no longer worrying about having to look after your
own platform and you're able to send, you know, you are using Grafana Cloud a little
bit more and sending everything over to that stack, it allows you
to go out and, you know, be an enabler for teams, move that dial on
reliability embed in teams, almost observability consultancy.
Yeah, exactly. And yeah, going out and really helping
people to move that dial. Yeah. Excellent. Okay, so we do have mics. So if anyone wants to ask a live question, just raise your hand and we'll have a
mic runner come around. While we prepare, prepare for that, I'll have one question
here. There's another theme around, we talked about observing further
and further down into the stack, into the components. What about going
up? So questions around how do you, how do you connect to the business? How
do you think about business process, observability, things like that.  maybe a little more challenging
thing going down to see the. Infrastructure. It's kind of the
key question in some ways, right? Because I think I mentioned
earlier, right? The, the transition is third stage in
terms of how you focus more on value. Ultimately, and we talked about
this yesterday, right? Context, right context of the data that you're
collecting is ultimately how you're gonna draw that line. And it's very
easy to look at, you know, millions and millions of time series
ingesting all of these logs, right? As value in and of itself. The
business doesn't see it that way, right? Not until that
data is translated into a, a narrative or a process or a story, do you actually get to get
to leverage that value? So I think it goes back a little bit you
know, I'm, I'm stealing my own answer. I think it goes back a little bit
to that consultancy element because, you know you know, I'll, I'll
give a tangible example, right? So when we wanna engage with some of the
folks that own the messaging platform internally we need their
expert views on that system. But then you need to
combine that with a very, very opinionated view of the right way
to observe said system. And so it's, it's bringing together both that
view of that internal system and kind of expertise of it with the expertise
of the right way to monitor. I, I don't know if you can just
organically achieve that, right? I don't know if you can turn a dial
yourself and get that without partnership within the business. So ultimately it comes down to
more and more engagement there. Obviously there will be
always be a set of teams, and we probably all have a couple in
mind where they just raised their hand and figured it out themselves.
They read all the docs they wrote, they wrote all the configs themselves,
and we're like, we know what we need. You know those teams are
awesome , we love them. But but I think yeah, my, my view is that ultimately you have
to really sit with the business. And I, if anyone has shortcuts to
that, I would, I would love to hear it. Let's chat after. But
I think I think that's, that's been what we've seen so far. Yeah, I think you've mentioned
that slows quite a few times, and I think that's a hugely
important thing that, that we're, we're looking at doing, which is
moving away from, you know, the, the standard waking everybody up
because you've had a CPU spike. The reactivity. Yeah. And it's more about having SLAs
based on your business outcomes and alerting on SLOs, not just
alerting on absolutely everything. 'cause That's the important
thing. Yes, you want, you know, you want five nines on everything, but if your customer's not
going to notice anything that, that's the important bit is when is my
customer feeling the effect of something that's happening? And tell me
before that happens, right? So yeah, SLOs and how you set SLOs, you
need to talk to the business. The business are the ones that
need to set that. So yeah, engagement with business, huge. Great. Okay. Let's go
to audience right here. Hi, my name is Jas sja and
I work at Goldman Sachs. My question is primarily directed at Olin. Do you feel that your work has
added a lot of value for the unique regulatory requirements your teams
face being in the financial services industry? That's a good question. From a, from a regulatory perspective it's
certainly not my expertise first of all. But what I would say is that concept of of breadth in, in the stack and observing
kind of bottom to top every, every component that makes up the
platform in a lot of ways what we're, what what I think is going on in the
regulation space is needing to be very clear about how that works and need
to be very transparent about it. And so my view, my general view would be
that observability can
contribute more and more into like, kind of telling
that story. In some ways, I think that's the
maturation of the tool set, whereas maybe before it was
seen as purely an application kind of tool, right? For the
individual product lines. But if you can build a breadth wise view, it can be an input to, to those
kind of processes. You know, that yeah, that's, that's basically
how I, I see it. Great. Thanks. Okay. Let's do one more here. Hi Robert. This is a question
for Robert. I'm , I'm from computer center. You touched upon noc the ways of
working with NOC a little bit. So the question is do you now
see the IT side of your telco which is producing the services,
running the services and noc, which is network working closely together
because because we have come to a place where it's more observability
rather than monitoring. I mean, in all, in all parts
of the organization, like it, it is a lot more about
doing more automated and, and putting less eyes on screens and, and triggering run books, et cetera. So When the, there is a still a kind
of enterprise IT side, which is, in our world at least quite separate
from what is really supporting the telecommunication services directly.
So the, the mobile services, the broadband and every, every component
of that, which is what that our, we all we call SRC, is responsible for. That's still actually quite separate
from, from other classical IT services, but there are more and more observability approaches and
techniques, as I said before, where, where they're using applications
that are just really, really complex and distributed. It's,
in particular in the mobile world, it's, it's just just really, really complex. And probably people who don't know that
 don't have that kind of insight, just how many different components
there are that that interact. And we, we use the, in that, that space as well to really get a very
simple and, and, and easy overview from, from all the many different
places. Fragmented. War rooms, basically. Yeah. Yes. Yeah. Alright. Thank you then. Thank. You. Okay. All right. We've just
got a couple minutes left here, so probably get to maybe two
more questions real quick. This one's a a little bit spicy, I
think, not, not too crazy, but we, we talked about adaptive metrics here,
right? We all know the cost pressures, what's happening in the economy
with budgets and everything. Is there a concern that this feature makes
users not worry as much about whether metrics they publish are actually useful?
So I think the spirit of it, right, is if you just have people send whatever
and think the system will take care of it, are they accountable for that? Right? I think that one thing that was
certainly missing for us was teams understanding the
TCO of their application. So yes, they when you're looking at cost
management or cost ownership, guess they may well understand their
infrastructure cost if you are in, in cloud. But observability
for a long time was just a, was just a black box. So they
might not understand that their, their little feature that, that know doesn't do a, do a huge
amount for them, but, you know, a small little feature could
be sending way more metrics, may way more logs that they, they shouldn't be sending and
could be a massively costly costly impact. So being able to raise those the total cost of ownership of a feature
is something that I think teams need to understand. I remember we had we had
one team that was sending debug logs for a feature that
was using 25% of the login cluster that we had at the time, and for,
we would call it a tier four feature. So it wasn't part of the, the
core order flow. But yeah, it was just sucking up money
and the team had no idea. So being able to make sure that they
understand the total cost of their, their futures huge. Yep. Yeah. And I think adaptive I
think adaptive is a win. Like my, my view is it, is it nothing else observability
on the observability, right? In terms of what, what you are collecting and the relative
sizes to those things that has value, whether or not, you know, to what level you focus on fitness or TCO
or those concepts, you need that data. And we were, we were about a quarter of the way down
the road of trying to build that feature internally when  Grafana
made it part of the platform. So I think that's the indication that
like, it's important enough, yeah, that you need it. How you manage kind of
your applications you know, footprints and the teams and the politics
and the budgets and everything else is one thing, but that feature is a, is
a net advantage to have regardless. So. Yep. Great. All right. I think
we're just coming up on time here. So maybe just real quick,
one word or couple words, what are you most excited about for
the future of observability? Anything, any particular capabilities, particular
areas that you're looking at. Looking at the future together with. Aiops AI ops. Okay. Yep. Alex, you. Stole mine. Yeah. AI ops and
generative ops. Yep. Yep. I'm in, you guys saw certs, right?
You guys saw that that was yesterday. I wear it as a certs. Yeah. Alright. Yep. Awesome. Cool. Okay, so this is
funny, we're gonna take this full circle. Alex, this question came in given Alex's
aptitude with spinning chair, did you have any previous designings
apple's click wheel ? I don't know who wrote that,
but  what? Alright, we're gonna end on that one.
Okay. Amazing. Amazing. Okay. So let's give a round of
applause for our panelists here.

