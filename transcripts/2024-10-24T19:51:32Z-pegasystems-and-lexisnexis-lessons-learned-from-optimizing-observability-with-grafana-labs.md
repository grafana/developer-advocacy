# PegaSystems and LexisNexis: Lessons Learned From Optimizing Observability with Grafana Labs

This video features Grafana Labs customers — Frank Guerrera, Chief Cloud Officer at PegaSystems, and Neil Wilson, Director of ...

Published on 2024-10-24T19:51:32Z

URL: https://www.youtube.com/watch?v=3qlqgoqd88E

Transcript: Good morning everyone. Hope everyone's
doing well. So my name's Wayne. I lead our product marketing
team here at Grafana Labs. And one of the other privileges I have
is I get to chair our Customer Advisory Board. And so our Customer Advisory Board, these are customers that have
been with us for a while. They really help us with our
product vision, with our roadmap, and just give us a lot of insights on
how do we be better partners for our customers. And today I have the privilege of
having Frank and Neil join us from our Customer Advisory Board. They've graciously donated their time to
share a little bit of insights with you all just about their
journeys with observability. As we were preparing for this, I, I was trying to figure out
a fun way to introduce them. I'll let them talk a little bit more about
their business and their role and all that. But just, just to have a little
bit of fun. So I found out that Neil, in his free time, I don't know
if he does it as much anymore, but he was a passionate skydiver. Right. So Neil has done over
400 jumps in his life, and he's still here with us today,
so, nice, Neil. Great. Going. Okay. . When was your last jump? Oh, boy. 10 years ago, maybe. Okay. 10 Years ago. About the time my son was born.
Yeah. Okay. Yeah, that's something. There's correlation there. Yes. Yes. Yep. And you're in the
risk business? I am. Yeah. Yep. Okay. Good. So you made a good calculation.
Your insurance hasn't gone up. Okay, excellent. So, Neil is a skydiver,
a previous skydiver, and Frank, as I've gotten to know Frank a lot,
he's, he started off telling me okay, he was military. He's done a lot of really
interesting things with the military, but his first job he was trying to get
was actually just down the street here. He was going to Madison Square Garden, and there was a Barnum and
Bailey Circus performance there. And he was interested in
becoming a professional clown. And so, Frank, we, we don't
have anything to juggle here. Maybe you can juggle the water
bottles, but Frank is a pretty, pretty serious juggler. Mm-Hmm. And he actually this is also a
fun fact. I didn't know this, but there's actually a clown school.
And so where, where is it In Florida. Orlando. It's in it's, or in Orlando. So the
best, think of Harvard for clowns. So there's a college for clowns. Mm-Hmm. Frank applied, but
unfortunately got rejected. I did . And he had to go into it and observability
and all this other stuff, so. That's right. Maybe in a, in a, in another life you
would've been a, a professional clown. Absolutely, yes. So, excellent. Actually being in it has been a lot of
fun. A lot of laughs. So I, I think... Similar jobs actually. Yeah. Yeah. And congrats by the way, Frank, Frank just got promoted to
Chief Cloud officer at at Pega. And you could also say CCO
or Chief Clown Officer. Absolutely. . Okay. Well, excellent. So yeah, just
tell us a little bit about your, your role and your business for
folks that may not know as well. Sure. So like Wayne said,
my name's Neil Wilson. I'm a Director of Software Engineering
at LexisNexis Risk Solutions. My role really is, I have a, a couple of teams underneath me that
are really aligned to cloud engineering, site reliability,
engineering, observability, performance and automation and some
data, some like the DBA type of function. So really why some of that's important
is we are just have completed a transition into the
cloud from on-prem system. So a lot of my last couple of years has
been focused on getting all that stuff that was running on-Prem, some of the legacy observability
and transitioning it to the cloud, and also then making the shift over
to Grafana over the last 18 months. Great. So and Risk Solutions is a a collection of different business units
that ultimately we build products that help our customers identify fraud, make sure that they're in compliance
with regulations and laws ,verify that people are who they say they are
when they're trying to, like, let's say, get an insurance quote. You know, you don't want to be getting dinged
for somebody else's bad driving record. So things of that nature. So a lot of our products are aligned to
mitigating risk for our customers and making sure that that ultimately
kind of trickles down to, you know, everybody else that's
utilizing their services. Great. Frank? Yeah, sure. I'm Frank Guerrera. I'm the, I am the Chief Cloud
Officer at Pega for about, it's now almost two weeks now. I've
been in that role. That role really is, is allowing me to set up, to really take the company to the last
phase of what I want to do with Pega Systems. It's a 40 something year old
software company, works in the large, only the largest firms. We do workflow
automation for the biggest banks, insurance companies, airlines, telecoms.
So that's really what we are core to. I started out in the banking
industry a long time ago, all on-prem for many years. They
brought me on board seven years ago, and my title was the Chief
Technical System Officer. So I had to build out all the
architecture, the operations, the security compliance, every aspect of a company that really
ran on-prem software and transition, not only the technology, but also the
company to an as a service company. Over the last seven years that seven
years scale was the biggest thing for us. Knowing that we had basically a lot of
clients we had to move. We had 5 million, $5 million in, or $50 million in revenue when I
started with 5% of clients on the cloud. It really wasn't a cloud, by
the way. They called it a cloud, but it really wasn't. And
then seven years later, we're over $550 million in revenue. We have close to 50% of our clients on
a cloud. We had to be able to scale, and a big part of it, of course,
when we go and talk to clients, and I talk to clients in my new role is
really around two things they asked me right off the bat. One is around securing the data and
next thing is how do we observe it? So that's a big part of what we do. Excellent. Alright. Thanks guys. Okay. So this is going to be a
panel discussion, right? I've got a few questions prepared,
but definitely want the audience here. So we've got the QR code here
so if you have questions, please submit them. I'll start
looking through them and, and start getting to them
as as we go through. Okay. So please submit your questions. Alright. So the title of this talk is
You Implemented Observability at Scale. Now what? Okay. So I think maybe
similar to the folks in the audience, we've all been on different phases of
observability in our organizations, and I think for you guys
it's been probably a lot of
challenges, battle wounds, lessons learned along the way. I think you've all implemented
observability for your end users, your organization. Yep. And trying to think about now what,
right. So before we kind of get to the, the what's happening now and
what's happening in the future, maybe you could just start by a level
set of defining observability in your organization. So, you know, it means a little bit of different
things to different folks, but how do you guys think about that and, and how does that matter
to your stakeholders? Sure.
Frank, you wanna start? Yeah. Sure. Yeah, I mean, I mean, like I said, it's the number two thing we get asked
when we go meet with a client. So it's, it's definitely paramount to operating
any kind of cloud service, which we do. So from, from my organization, it's really
critical within what we consider the, the operations groups. The definitely the cloud engineering
groups that really build and also run all of the cloud services is to make
sure they understand how do we, how are we implementing the observability
around to the ability to be able to be not only reactive, but
move into proactive, which I'll talk about a
little more in a minute. But the other thing that we really
need to do in observability, which is, which is when you're dealing with
definitely engineering developers who are developing platform and product for the
software, you have to run on our cloud, we had to really make sure that they
understood what they need to do to basically contribute to observability.
And that really was the scale part, because we needed them to get in line
with making sure as they were building, we were implementing and understanding
how we constantly had to evolve observability to make sure it was, is really picking up the right things
we needed to pick up for how we were observing for our clients, how
we're running the platform, how we're running the
application. So it, it was, it's definitely something that was very
critical to the way we thought about from the beginning, how we're
gonna set up our cloud service, how we're gonna be able
to scale a cloud service. And observability was
a big part of it. We, we had a previous company before Grafana. We made a decision to
look at a new provider. Now it's been a little, little
while ago, but really, you know, when we looked at it, we did, we looked at every single provider out
there and Grafana was the one I really felt could help scale with us. And definitely from my perspective in
partnerships is making sure we had the ability, and the reason why I like being on the
CAB also is be able to influence the roadmaps and understand what's coming
out, which is a big part of scale too, from my perspective. And just having that ability to be able
to have that kind of influence. So, yeah. Yeah. Great. Yeah. So agree with everything Frank said
and kind of adding onto it. You know, know, we're kind of in
slightly different businesses, or we have different products
that we offer to our customers. The for us, we were in the middle of a cloud journey
when we made the shift over to Grafana. So we are going away, we're actually
exiting some of our on-prem data centers, you know, turning off the
lights, disconnecting the
cables, all those things. So we needed to be successful
in moving to the cloud, and we realized that we needed a better
observability platform in place than what we had at the time. That's
where Grafana came in and, you know, we made a pretty rapid shift. So for us, we went from having no Grafana
footprint of any, you know, discernible size to having a large
centralized Grafana Cloud hosted services for, for most of it in
about 18 months time. So January of last year is when we started
that journey. And now we're running, you know, we've had over a hundred
million orders placed in our cloud work or infrastructure
just in the last month. And all of that is observability
data is flowing through Grafana. So having good observability means
that we understand all this new infrastructure that we stood
up and that we're paying for, and that we are doing it in
a cost efficient way, that
we're doing a secure way, resilient way, slightly different but ultimately
that it is also performing it at the same or better levels than
what we had on-prem because our customers have very high expectations and
they're only getting higher. So really having observability
monitoring means that we have full like a full picture of what our
systems are doing at any moment. And we always know if there's a problem
when, you know, where the problem is, when it happened, how it happened, you
know, and what we're gonna do to, to, you know, remediate it or mitigate it
in the future, so doesn't happen again. Yep. Okay. Great. Thanks
guys. So we started talk, you started alluding to
this a little bit. How, how do you guys think about measuring
success? Like, what is the, we, we typically think of
MTTR incident resolution, but what are other metrics or other ways
you think about measuring success of observability? You want to start? Yeah, no, I, I think, you know well, I always believe that you measure success
when you're basically your clients realize that you're actually offering
a really great service. But no, internally we definitely make
sure that we understand you know, are we really getting the
ability to catch alerts, do something with them that's really
effective to be able to make sure we're operating our services that we have
make sure we are basically proactive. We talked about this, Neil and I. I
mean, one of the biggest things is, you know, I think we all know, especially when you're
offering services to clients, is that you never want them to tell you
that they actually have a problem before you know it. So for us, I mean, success
is, we don't hear that. I mean, we, we really have to think every day, what can we do more and more to make
sure if there's something that's gonna impact the service you offer, that the observability has given us
ability to catch it before our clients. So to me, that's like the
number one thing. After that, you can do a lot of data metrics
around capturing information, how many alerts you get, how many you really be able to
respond to how fast you respond. We, we track it all, we
measure it all. But my, my biggest thing is when I've had
conversations with clients and say, wow, you know, we, you've gone
from a place where, you know, we had to contact you all time to a place
now where we don't have to, you talk, contact us, you're proactively
communicating with us
about what's going on. You make us aware to maybe some impact
you're fixing the impact. That's, to me, the biggest measure that we have
to make sure we're successful. And on the scale side,
definitely you know, when we, when we had a move from the
old vendor, we had to Grafana. I mean, we only had six months,
tremendous amount of data. I mean, thou, I mean, thousands of clusters of data. We had so many things we had to move
so fast. During that transition, we had to make sure, again, that we were
measuring basically the project itself, which was a huge project. So for
us, really moving between the two, which some of you might do in your
careers if you're moving between two different providers, you know, having
that timeline, having that commitment, I could say that Grafana signed up with
us to have the commitment to make that scale, make the thing move. And
that was a big part of our success, was measuring basically that
transition, how well we did it. Mm-Hmm, Great. So yeah, I agree with all
that. The, if you look at the, you can look at from two
different perspectives, or
at least I do, but you know, quantitatively you have your mean time to resolution. You have your ability to measure your
SLOs and your burn your error budgets and how they're burning and all
that kind of stuff. And, and we utilize all that from
a different tact though, I look at measuring the success of our
observability also from the qualitative standpoint. We have seen a huge culture shift within
our company as we've transitioned from what was largely a log-based observability
platform to actually embracing OpenTelemetry, using metrics and traces. And what we've noticed is that
after some grumbling and, you know, some really tough conversations
and a lot of onboarding, a lot of, you know evangelizing, once
people finally started, it started to click for folks. It kind
of created this buzz within the company. And it was, it's neat to see when somebody comes
up with a new dashboard or a really slick way to do something that, you
know, even some of our, you know, observability experts on my
team haven't thought of yet, and they're then able to share that
back to the rest of the organization or come up with new ideas that we can
pitch to Grafana and working with them you know, from, you know, the CAB perspective.
Say, Hey, we've got this great idea. We think it's great. At least we,
we would like to see this you know, how can we make this a
feature within the platform? And we've had a couple of
those already come through. And I think there's one more
planned in the IRM space. So joining kind of the quantitative
and the qualitative together we're Frank mentioned, you never want
your customer to call and say, "Hey, do you know that you're having a problem? Do you know that this service is down?". Mm-Hmm, . "Did you know that you're
slow?" When I said, our customers have really
high expectations and they're
being higher every day, our customers are monitoring us. They
have observability about how we're doing, and it really is, you know, a, a
really tough phone call when they, they pick up the phone and say,
"Hey, you guys are slow right now, and you didn't know it." But it wouldn't
be uncommon for our customers to say, "Hey you're over 300 milliseconds on
your response time. You're slow." I mean, that's the type of responses that
our customers are expecting. So being able to, I guess, feel how the conversations have
shifted even with our customers as our observability has evolved, has been
a really big win for us. And that's, you know, a different way that we're looking at
how successful we're being with our observability. Yeah. Yeah. Great. Yeah,
it's never a great situation, right, where your customers know before you
do, right? Yeah. Yeah. Frank, can you, can you double click a little bit
into the proactive preventative side? I think you have a interesting mantra
you always say, right? When you, in your meetings with your team. Yeah. No, I mean, for me it's
when I joined the company, and, and this is just the way I've always
thought in my career is, you know, coming into a company like Pega who had
not really been a cloud service I knew how to go, I had to be
reactive right up front. So my whole thing about joining a scale
was how do I move from reactive to and responsive to basically
proactive and preemptive. And this was the shift
I had to go through. And it's a journey I had
to go on with the company, with my organization as I set up the
whole organization that did not exist. And making sure we understood
the shift to this right. And knowing it was gonna be a journey we
on and Observability was gonna be play a big part, even though it wasn't
the thing I initially focused on. It was definitely the part I knew
what would allow me to get to the, what I considered the real
proactive preemptive side
by really looking at how do we observe, how do we make sure we're
aware of the things that are really, have had trends and impacting us, and how we build any automation around
making sure we can either either order, recover, or to make sure we
have the ability to fail fast, whatever it was in the
proactive side. And, and everything we do internally
when we're dealing with clients is, I've had this thing that goes
on the bottom of every RCA, the every single email
when somebody tells me. So they're really great at telling
me how the problem, you know, what, what caused the problem. Everybody
can tell you what caused the problem. The answer has to be, how do we
make sure it never happens again? And when I get, when we, when I sit down with my observability
teams and they tell me, you know, we're getting everything we need.
We're seeing everything we need, all the indicators, all the
alerts. I keep on telling, saying, take a look at the data and tell
me how you're gonna reduce it all. How are you gonna make sure you
don't even need to get these alerts? How are you gonna, so I push to the end
to make sure we have the proactive and side of it. And then the preemptive side,
because, you know, for me and again, the companies we deal with, which are the largest firms that deal
with really critical information they're sharing and data that they use we have
to be in that proactive preemptive, they don't want to go down. I mean,
the, the, we, we get, you know, there's zero downtime,
absolutely no downtime. Everything we built in automation on
the way we not only update all of our software when we started, it was, I
mean, if I touched anything, a database, if I touched any part of
the infrastructure, we took
downtime on everything. Every client, when I sat with them,
I knew I had to present to 'em. I was gonna create no downtime and
be able to move, make that shift, and no downtime to be really proactive
was really what we had to do. And observability gave us the ability
to understand, you know, what, what is to happen? What
is the change we made? Why do we make that change
that had an impact, right? And how do we then observe how do we
make a change again, similar to that, that doesn't have an impact. So, you
know, it's really great to have a, a really talented, what I consider a real talented CloudOps
team that really looks at how we're operating our service. But I
challenge 'em every day to talk, think about how do we make sure the things
we do, the things that developers do, the things that we, we make changes from infrastructure
do not impact our clients. Yeah. No, that's great. Alright, Neil, so
maybe we start with you on this one. Okay. One, one thing we were chatting through
yesterday is the operational structure of your teams, the organization, right? So this whole shift from centralized
to decentralized, what happens when, you know, you acquire a
company and they come in? So walk us through a little
bit of that journey. What, what have you learned along the way
and how are you guys currently set up? Sure, Yeah. I mean, we were
talking a little bit yesterday. It's like this centralized, decentralized,
it's almost like a sine wave. You know, every five or 10 years we collapse in
everybody and then we pull 'em back out. What we have found, especially as we've made this
transition to the cloud and the observability platform with Grafana, is that we take kind of a hybrid approach
as far as how we structure our teams. So across Risk Solutions, we have a telemetry chapter
that is really tasked with defining the patterns and practices,
some of the architectural you know, guidelines that we need to enforce. And really just trying to make
a paved road for everybody. All the other sub companies or, you know, different areas within the larger
Risk Solutions to align to. So we have an overarching centralized
telemetry chapter - I'm a member of that - within each of our individual markets. 'Cause Really the way that we are set
up is we align our business units to like insurance, healthcare,
government, so on and so forth. Yeah. 'cause Our products we work with 98%
of the insurance companies in the US utilize our products, nine outta the
10 biggest banks in the world. I mean, a lot of overlap in that respect
with Frank and with Pega. So we, within our individual
markets, then we have a central team, the one that I manage within
insurance that is responsible for executing on those paved
roads that we have. And that means building
tooling. It means you know, doing a lot of training, upskilling, helping people with the
transition to a new platform. But that ultimately our individual
product teams, the one, you know, our app developers in many cases, our SREs are embedded within the
application teams themselves that are responsible for the infrastructure
for just this system. They're the ones that actually
have to then go and implement the you know, the Grafana Alloy is something that
we're moving to very soon updating which metrics we're gonna be
pushing across the board. I'm very excited about the
Alloy Fleet manager, by the way. I think it's gonna solve some major
hurdles that we've got right now. So in that way we're decentralized. When
we get down to the application level, those, our perspective
is those teams know best, what information's going to
be important to the health, observing the health of their systems. But it's done with the
kind of the guardrails that
we've put in place and some of the modules that we've written, the tooling that has been put in
place from a centralized perspective. Mm-Hmm. Great, what about you, Frank? Yeah. And so I would say, you know, ow, originally when I was dealing
with the reactive part, I had really the ops from an
infrastructure perspective
as one team trying to basically build what we need
to be able to scale there. And then I have another
team that deals the outside, since we're a platform and clients
build their own apps on a platform. I had another team that we use the tool
internally that we built to be able to basically manage the, the application
side of it, two separate organizations, engineering it, observing
it, and everything else. With me moving out of proactive, I put them under one group because I
need to be able to get the correlation between the two now so I can really think
about how I can become more proactive, preemptive. So from a company
perspective, there would, when I built out the groups,
it was definitely two separate, but I knew there's a point
I had to bring 'em together, but I had to let them mature to
be able to bring 'em together. And now they're together
and really mature, and they're really going
towards that, that approach. The only thing that we talked about
that's kind of decentralized is there were several acquisitions before I joined
the company that I want, we, basically, the decision we made is to get all of
this set up and then take those companies one at a time and figure out
how we roll 'em into our, our overall architecture strategy.
And that's really where we are now, is that we'll take those
kind of decentralized groups
out there and we have a playbook we'll run through on
the things we need to change, and eventually we'll bring 'em into our
overall observability model for Pega. And if we acquire a new company, we'll have the same kind of playbook
where we'll bring 'em in a lot sooner than kind of waiting until we get the structure
in place. But centralizing it for, for us, has been the right thing, because I wanna move to that proactive
and preemptive. And we do have, like I said the infrastructure side and
the app side really coming together to do that. So, so just to add on to that from
the the acquisition standpoint. 'cause made me think of something.
He's exactly right. You know, you bring in a new company, you,
you, you know, acquire somebody, they become part of your
group. We, you know, we try to kind of leave
'em alone initially because
you don't want upend their world. And there's gonna be, you know, some nervousness too if you're acquired
by a larger company and, you know, are they gonna, you know, all those questions I'm sure many of us
have had to deal with, myself included. I was originally part of ChoicePoint
which was then then bought by LexisNexis. But what we're finding
is that in many cases we have, you know, differentiation
in our tech stacks, which is usually not too bad, but the
observability with it comes... You know, they might have had a
contract with...Datadog has been the one that
we've seen most often. So one of the things that we are trying
to take a focus on is where we can, is now maybe being a little more
proactive in bringing that slice of the acquisitions, bringing them into
the Grafana contract. And, you know, that's where I think we're likely
gonna have some focus going forward, because you can, as long
as your systems are stable, it doesn't matter as much
initially to me at least, that you have differentiation
between the groups. And really you want people to have a
little bit of agency and how they build their system. Grafana is a pretty
good example of that. You know, Loki team is different than
Mimir, than Tempo and such. But I fundamentally believe that the
more aligned you can get with your observability, at least getting
everybody on OTel is going to be, it's going to make your life a lot easier, especially when you do that integration
work you know, with, you know, like an acquisition and such. Yeah. Sun Neil, we, you know,
we've both done this now, you know, where we tried to build
observability for scale. I mean, I'm sure we have both have experience
with the pitfalls and challenges and things we might have done a few things
a little bit differently. So what have, what have you, what, you know, what have you thought about maybe
in that context of, you know, what, what would you have done maybe a
little bit differently if you had the opportunity to start all over again? Oh boy. So we started, you know, the transition to Grafana
18 months ago. We, we got our production we had to
self host our logs, by the way, just so we we're hosting Grafana
Enterprise Logs within our own Kubernetes clusters. But then we use all the SaaS
services for Grafana, just for context. So we had a lot of learnings just
running Loki at the scale that we run it. And Grafana was a really good
partner in that. So like, we started using Redis Cache as our
backend because it was quick to stand up through through Azure. But do it again. We would've more quickly moved to
like memcache as our, you know, essentially our fast fast cache. But really some of the pitfalls that we
ran into would've gotten started sooner, which just helping people understand
as they transitioned from using just logs to what does
cardinality actually mean? It's some of the basics that even though
we thought we were doing a pretty good job still, we found that there was, there was some some issues with
really trying to quantify how much of, how many metrics are we going to need? Having our teams understand what
certain decisions like putting the pod name inside of a metric is actually
gonna do to you and the problems it's going to cause. But we one, one really good example I can
give you unrelated to that. We, as we start onboarding more and more
of our users with into the Grafana UI, we realized that we are using
the basic roles within Grafana: viewer editor you know,
very small number of admins. We had far too many people with either
the editor access or for what we were doing. The editor role was too permissive. So we ended up having a problem where
people's dashboards would go missing because somebody else deleted it, not thinking that they
were doing anything wrong. So we would've gotten ahead of
implementing custom roles for all of our teams. And and we've done that. We have...everything
that we do is as code. So we are able to build that into our
provisioning system that you know, our, our configuration of our users,
our as code, our dashboards are as code, our alerts or as code, everything is
provisioned through the Grafana APIs. And some of that stuff, I think we
would've gotten even further ahead of, had we known now what we, you
know, then what we know now. But beyond that, I think another big challenge we
had is dashboard sprawl, right? If hundreds of dashboards, thousands of
dashboards, version one, version two, version three, showing
up in the same folder, people forking each other's
dashboards, which isn't inherently bad, but there's no reason I needed to see
three copies of Grafana's own Kubernetes dashboard, you know, showing up. Trying to get a better handle on
that maybe would've been good. I think one really true, I'll, I'll pause here after this. Getting our labeling strategy
dialed in even better than we did for our logs and our metrics
as well as our attribute naming would've been a lot
would've been very helpful. We had set from the get go, these are the labels that you shall
apply to all of your logs. You know, we, there's certain number, there's a point of diminishing returns
with how many labels you put on some of this stuff. What we found
is that that went okay, but we weren't as we would've been a little bit more
strict about making sure that people were using the labels that we had set up, the values that we had defined for
things like level, you know, info warn, like I saw three or four different
ways of spelling the word error. Some, for some reason, , I, I mean, and hopefully like this
resonates with some of you guys. It's not that we didn't
know how to find it once, but we didn't even realize that
that was a blind spot for us, that this was gonna be a problem
that was gonna cause so much grief. And once you're deployed at
scale, making changes quickly, coming back to the fleet manager
thing, that's where it being, it's become a little bit of a, of a challenge for us as we're now
going back and taking kind of a round 2 approach of cleaning up our
labels, cleaning up our values. We have everything we need, but we've had to make some
really interesting links
within the data sources to correlate our logs to our metrics, to
our traces and back again. So, yeah. Great. Thanks for sharing. Yeah. Alright, so I'm gonna turn it over
to some audience questions. So thanks everyone for submitting
these. We, we talked a little bit about, now that you're implemented,
right? You've got all these tools, these services available for your
different teams in your organizations. There's a couple questions
around this theme of, well, how do you get people to A) learn
about it and start using it? So any, any guidance for the
group here around education, around training, around just getting people to start
using some of these tools and services? Well, yeah, from my perspective, of
course you know, from my, my ops teams, my observability teams internally
from an operation perspective, I mean, they all had to be enabled.
That was their job. I mean, really the biggest part was trying to get
the product engineering teams building the product side of it that they
knew they would have to use, basically the tool themselves
to understand how they
were building their code and how, how it's gonna affect the
overall operability of our
service was probably the biggest challenge. So getting
them the training we needed. Once we got them the training,
we, it was pretty much, we do a lot of mandatory training for
our engineers. But it, again, it was, it was for us, it was, and one of the
things we had to do was really, it's a, it was a real mind transformation
from how they thought about building code that was gonna
get deployed by a client, on-prem versus us building code that we
had to operate and really try and make sure that they were trained,
the ability to understand what, what did we need to observe
by bringing them on board. So we built it into our service lifecycle
early on for them to understand they had to be part of their process, how
to be able to understand observability, what they were doing, how to
build the code I was gonna change, and basically the things we
needed to alert on. So, you know, from our perspective, I mean, we really wanted to make
sure everybody got trained. Mandatory training was
really required. I, you know, and also I think because we
were an on-prem, the cloud, we really spent a lot more time with
our, with our product engineering groups, really making sure they understand
the value of, of observability. So and then i, I, the dashboard
crawl, because once they got it, they realized they had
to do this. I mean, i, I, it was literally at a point where I was
like, how many dashboards we have, we, that's a blind spot. How. Can you, how can you find anything? Yeah, we, we didn't even know it
was happening all outta nowhere. We had like hundreds and hundreds of
dashboards for like, common teams, and that's the one thing that we realized
we wish we would've done a little bit differently early on. So if that's
a lesson learned, I would say that. Yeah. so the, remind me of the question. Sorry, can you. Yeah. So, so how do you get people in
your organizations to adopt the tools, to educate them, to just
having them start using it? Yeah, so I've had a lot of conversations just
during this conference with a couple of the Grafana folks that have
been really encouraging. So Grafana has been
really good about when we, we tell them we have a need to
get some training, get, you know, a lunch and learn that kind of thing. Mm-Hmm. . Bringing somebody in and having that. And, but one of the conversations I've
been having around with, you know, some of your folks is how can we
formalize that a little bit more? And I've heard some really,
I don't want to, you know, share anything I'm not supposed
to, but I've very positive plans, it sounds like that you guys have in the
works for, you know, better training, more hands-on labs, that type type
of thing. Internally though, I, we had kind of an interesting situation
with everybody being so used to using logs, right? And, and so if anybody's used like an
ELK Stack type of thing as their backend, that was one of the things
we were moving from. And so if you're gonna try to query Loki
for 30 days of like doing a wildcard search, you're probably not going to
have a good time. But it's not meant, I mean, it's not meant to do that. So a lot of it was trying
to help bridge those gaps. It was a lot of our, our
team members, you know, becoming the experts first
and putting into place, here's the three things you need to
learn about. So we had we, we had a, a weekly meeting where we had
200 people on the phone call where we went over here's
what traces are, here's what, which are quite excellent.
And they're, I think, the biggest best tool in the
kit. Here's what a metric is and, and why you should care. And
there's different types of metrics. Here's why I do account over time on
logs. Yeah, it does give you a number, but there's a better way
to do that. So that's the, we spend a lot of time having these
types of formal, we're going to touch, we're gonna take one topic, we're
gonna put some process around it, and then we're gonna share
it back out to, you know, the rest of our organization,
the rest of our community. We also have pockets of user
groups kind of getting stood up to help each other learn. So we
had I think they called it like, like the Grafana Club, kind of like
the Breakfast Club a little bit. Yeah. Like one of my directs would and I didn't
know he was even doing it at the time, he had set up a small group where they
would meet once a week and just show each other what, you know,
what they were doing. So Ken's his name you know, Ken set this up proactively
and it was really successful. And that's something that we're now
gonna be formalizing because we're, we're in the cloud, we're
running at a very high scale now. But there's a lot of
things, you know, we're, we're in like the day two operations
mode and there's so many things now that we're gonna be working on. And I think formalizing some of
those continual education types of opportunities are
gonna be where we're at. Yeah, that's great. Yeah. Take advantage of some of the resources
we have for you as well, right? Yep. Yeah. Yeah. Alright, so another theme I'm
seeing in some of these questions is, is circling back to some of the
shift from the previous vendors. Mm-Hmm. That you have, whether it's through acquisition or
whether it's the whole journey you went on with us. Maybe I'll start with Frank. So one question here is around you know,
switching can be a pretty big effort, and how, how did you manage
that migration? What, what, what advice do you have for the group
here in, in terms of, you know, how, how to make that smoother? Yeah. Well, I mean, I've done quite
a bit of it in my career, but I, I have to say, when we, you know, decided on Grafana and met with the team
and we said we wanted to make sure we had a joint team, we had really
daily standups between the teams, we had a very short timeframe
to get onto Grafana. So we really had to make sure we
had the teams working together. Everybody raising the
blockers, you know, we have a, we have a concept of program management
within my organization where they basically, and, you know, really work after in the concept of
making sure a program gets completed. We treat this like a, a
program all executive level. That was it was raised to me. I had my weekly meetings to make
sure everything was going on track, but Grafana was there with us every
single day on this critical transformation we're going through because there was a
lot we were doing to not only make sure that we had parity with what we had, but also we had the ability
to make sure we could not, we could not miss on the day
we switched from observing our services. So it, for us in the, in the work we put into it and the effort
and Grafana stood at the table with us as a real partner to make
sure every single day if we
needed anything, you know, training, education, we needed some
way to configure something differently. They were, they were with us every single day along
the way over that six month journey to really deliver it. And it, and it really was an amazing thing to
see \my team and Grafana work so close. Today's relationships that we have
with the Grafana people we work with is exceptional. It's like, you wouldn't even know we're two
different companies at the end of the day, the way we work together,
which is fantastic, so. Wow. Great to hear. Yeah. Pretty similar
experience Grafana was in, they didn't pay us to say any of
this, by the way, . I mean, no, Grafana really was the a partner
with us as we moved from, so we've had migrations from Datadog. One of them is just wrapping up with
a company of ours called Cirium. So if anybody flew here, like they, they're a company that works
with flight data. We've moved from Elastic, you know, like an
ELK Stack type of stuff. And you know, I know, I don't remember if we end
up making transition from New Relic, but so somewhere in between
we've had, you know, experience with moving from
a lot of these vendors over. Grafana has been really the key to
helping show us the way to do it. 'cause you know, you guys have had a focus on that during
this conference even I've noticed. So really it's been a lot of
partnership with them. You know, one of the specific examples
I can give is we have coming from a very log centric type
of observability platform with ELK, which you can do metrics and
all those other things too, but we are usually
mostly using it for logs. We ended up having Grafana come and take
a look at some of these queries that our teams that were still getting used
to LogQL were just really nonperformant. And we were able to, you know, their Pro Services group was able to
take a look at these queries and then really come up with a guide
to say, you know what? I see what you're trying to do here, but if you do these three things
as a pattern across, you're going, it, it was able to increase, you know, or I guess reduce how long some of these
queries were run from like 30 seconds down to, you know,
subsecond in some cases. So we really relied heavily on Grafana
to help us make that transition and, and it went really well. Great. No, thanks for sharing. Alright. So I think that going back a
little bit to the kind of the alert fatigue and dashboard
sprawl and, you know, all the stuff that's out there, a any guidance or any advice
that you can share around just, just how to manage you know, like
how much is enough observability? Do you get some level of diminishing
return? How much is like too much? I mean, you should never have an
alert that's not actionable, right? So if you're getting an alert and people
say, oh, that happens all the time, you can ignore it, then you have to
ask yourself the question like, why, why do I have this in
place to begin with? Right. Early on we, so the, the way that we actually approached
this dashboard sprawl kind of problem at least for what we need at the time
we were making these big flips from on-prem to the cloud all at once. So
we're moving all of our services over. And we had, you know, 200 people on these phone calls
all trying to find information. We put together like a
dashboard of dashboards, kind of like a little bit of a meta
thing where we had all the most important dashboards from these various groups
that were involved in these big flips in one spot. And it seems kind of basic and
obvious, but that helped us quite a bit to keep ourselves organized
so people didn't have to ask, can you send me a link to this dashboard? They just went to this one central place.
What I'm really excited about though, is we've you know, kinda like BlackRock, we've been able to get a
preview with for Asserts. And I really fundamentally think that
that's going to change the way that we operate. And we're most of the way
onboarded in like a dev environment. It's gonna be really cool. So I'm
really looking at the problem of like, dashboard sprawl and such being solved
in a different way where we're gonna be writing less dashboards and
utilizing some of the out of the box. The app experiences you guys are putting
together have been really excellent. The Kubernetes one's really cool. I, I'm hoping that we utilize more
of that so that we're, we have, the only dashboards we're
gonna be creating are things
that we will be utilizing for specific customers,
specific types of orders, but not from the infrastructure
standpoint. Putting all that away. Yeah, no, I couldn't agree
more. I mean, alerts, you know, alert junkies and ticket junkies,
as I've said to my organization,  you know, it,
yeah, you want everything, but when you really have to
get down, and I guess for me, thinking about moving to correlation
and being able to be really proactive eliminates the noise, but you really have to know the content
that's really meaningful to be able to do the correlations that allow
you to drive towards proactive. So everybody wants them in the beginning.
You gotta then, you know, go through, which is what we did to definitely reduce
the noise and then really build on top of it to get the real
value on observability. Yep. Great. Alright, I think we are
just about out of time here. Any, any one word of advice or one thing you'd
like to leave the audience with here? Oh boy. I, I think the more that you can standardize, if you are in the point or
at the point where they, you're gonna start making a transition
to a new service in Grafana or, or away from a different vendor to them, getting your baseline
data as clean as you can early is gonna make such a huge
difference. If you can standardize, and I mentioned this earlier,
standardize on your label values, stuff that's maybe not out
of the box there for you, it's just gonna make life
a lot simpler for you. And really be be very particular
when people say, well, can I just send this thing
instead? Like, no, no, you can't, like put some guardrails in
place because it's, it, you know, it's kind of like garbage in, garbage
out, right? If you don't have clean data. Transforming it later is possible, but it's so much more
effort than it needs to be. Yeah. I think the biggest
thing when I, when, when I had the Grafana team
early on, I said, look, tell us what we shouldn't do. That was
the biggest thing. I said, you know, you have worked with all these clients,
please don't let me make those mistakes. Right? And that's really what I challenged
them to come to my meetings and say, don't do it this way, do it that way. And that's really what I
wanted out of real partnership. Because I look at them as an, I look as Grafana as an
extension of my organization. And having that ability to say you're
doing it the wrong way was really critical for me and my organization. Even though we had used
observability tools in the past, even though we had some really
talented people. Look you, you, you, you are somebody that I want you to have
that confidence that you could tell me and my organization. "Don't
do it that way." Yeah. That was the biggest thing for us. Great. Alright, well thanks you guys
for, for sharing your insights, audience. Thanks for the questions. Neil
and Frank, they'll be around, so grab them if we didn't get to some
of your questions. I'm sure if they, if you come up to them, they can, they
can talk to you about that. So again, thank you for your time. Really appreciate
it. Let's give them a round applause.

