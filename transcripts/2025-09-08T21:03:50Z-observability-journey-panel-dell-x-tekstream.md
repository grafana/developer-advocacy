# Observability Journey Panel - Dell x TekStream

Published on 2025-09-08T21:03:50Z

## Description

Join Dell Technologies, TekStream Solutions, and Grafana Labs for a candid panel on scalining observability. Learn how ...

URL: https://www.youtube.com/watch?v=YTyKIbJHRSo

## Summary

In this video, Chris Longfield from Dell Technologies and Glenn McCoin from TekStream Solutions engage in a roundtable discussion about observability in IT. They explore the importance of observability for businesses, particularly in enabling developers and enhancing customer-facing services. Key points include the challenges of adopting observability tools, the need for collaboration among teams, and the evolving role of AI in streamlining processes and improving incident response. The conversation also touches on the necessity of flexibility in tool selection, the significance of building a community around observability practices, and the importance of taking small, actionable steps in implementation. Overall, Chris and Glenn emphasize the value of demonstrating the benefits of observability to drive adoption within organizations.

# Observability Round Table Discussion

**Participants:**
- Chris Longfield, DevOps Engineer at Dell Technologies
- Glenn McCoin, VP of Strategic Initiatives at TekStream Solutions

---

**Introduction:**

Chris: Hey, I'm Chris Longfield. I'm with Dell Technologies, working as a DevOps Engineer on a small observability team. Today, we'll discuss the centralized model and share some experiences.

Glenn: Hey everyone, I'm Glenn McCoin with TekStream Solutions. We focus on Digital Resilience solutions, including observability, SRE, cloud operations, infrastructure support, and security. I'm excited to weave these topics together today.

---

**Discussion Format:**

We're having a roundtable panel discussion, and I want to utilize Chris and Glenn's expertise in observability and the broader IT field. I have some questions to guide our conversation, but feel free to ask questions or share commentary as we go along. 

---

**Getting Personal:**

Before we dive into serious topics, let’s lighten the mood. Chris, what’s the most embarrassing app on your phone?

Chris: I have around a hundred apps, and I mostly use seven. The most embarrassing app for me is *Tiny Zoo*. It’s an old game where you do small tasks to speed up other tasks, kind of like observability!

Glenn: I scrolled through my apps too. I think the most embarrassing might be *GarageBand*. It might be there by default, and despite being a "has-been" musician, I’ve never opened it.

---

**Observability's Importance:**

**Question:** Chris, why is observability important to your business and your customers?

Chris: At Dell, we operate as Tech Ops, a layer of services for developers to write code. We manage tools like Git and Jira. Observability is crucial because if something goes wrong, it can halt the work of 10,000 developers. We need to see what’s happening in that "black box" to avoid issues.

**Question:** Glenn, how is observability important to TekStream and your customers?

Glenn: Observability is a significant area of movement for our customers. For example, one large enterprise we work with is geographically distributed and faces challenges with governance and innovation. Enabling agile deployment while maintaining oversight is critical, especially since many of their services are customer-facing.

---

**Customer-Facing vs. Internal Applications:**

**Question:** Is there a difference in how observability is approached for customer-facing services versus internal ones?

Glenn: Yes, the speed to market is a crucial factor. For customer-facing services, the clarity of application health is vital. The pace of innovation is much faster, and the goals differ. Our developers are our customers, and their priority is getting code out quickly, whereas operational teams focus on managing tools efficiently.

Chris: I agree. We see different objectives between developers and operational teams, which can lead to collecting and presenting different data.

---

**Challenges in Observability:**

**Question:** What challenges do you encounter from internal customers regarding observability maturity?

Chris: Our centralized model requires collaboration, which can be a challenge. We want tool owners to understand observability without needing them to become experts. Time zone differences and varying team priorities also complicate this.

Glenn: I echo that. Adoption struggles often stem from misalignment across business units. It’s essential to connect different parts of the organization for effective observability.

---

**Choosing Observability Tools:**

**Question:** What criteria did you consider when choosing your observability tools and platforms?

Chris: We focused on flexibility, standards, and the idea of a single pane of glass. Flexibility allows immediate adoption without needing a complete overhaul. Using tools like Grafana with open telemetry standards helps maintain independence and adaptability.

Glenn: I agree with Chris. Every customer I talk to has too many tools and data stored in various places. I prioritize platforms that demonstrate a rapid pace of innovation, like Grafana, which has quickly advanced in the market.

---

**Looking to the Future with AI:**

**Question:** How do you see AI shaping the future of observability?

Chris: We’re implementing an open-source MCP server for Grafana to interact with our data. The vision is for systems to autonomously identify anomalies, perform root cause analysis, and potentially even fix issues autonomously with human oversight.

Glenn: With AI, we will manage volumes of data and discern actionable insights. There’s potential for automation in areas with high context fidelity and lower consequence actions. Ultimately, everything will move faster.

---

**Evolving Organizational Structure:**

**Question:** How do you plan to evolve your observability team organization in the future?

Chris: We are looking into tools like Fleet Management to standardize processes and improve collaboration among teams without losing their specialized knowledge.

Glenn: One customer effectively combines centralized and decentralized models, allowing teams to make their own choices while also collaborating on best practices. This balance fosters innovation and efficiency.

---

**Final Thoughts:**

**Question:** Any recommendations for those starting their observability journey?

Glenn: Assess your maturity model for observability and identify the next small steps you can take. Small, automated steps lead to better outcomes than trying to implement everything at once.

Chris: I’d suggest moving quickly. Start with visualization for your first meeting to engage people and generate excitement. The faster you innovate, the better.

---

**Audience Interaction:**

Does anyone from the audience have questions or experiences to share? 

Audience Member: I manage the observability team at Cisco Collaboration, and we onboarded teams with existing stacks to show value quickly. Now, teams come to us instead of managing their stacks.

Chris: That resonates! Showing value is key to adoption.

Audience Member: We’ve also engaged product owners to understand their needs, which has led to quick adoption of our dashboards.

---

**Conclusion:**

Thank you, Chris and Glenn, for your insights today. It's been a valuable discussion on observability and its evolving landscape.

## Raw YouTube Transcript

Hey, I'm Chris Longfield. I'm with Dell
Technologies, a DevOps Engineer there, and a small observability team
that I've learned today is the centralized model, so we'll be talking about that a little
bit and I'll be sharing some of those experiences with you. Excellent. Glenn, would you like
to introduce yourself a little bit? Hey everyone, I'm Glenn McCoin.
I'm with TekStream Solutions. I'm our VP of Strategic Initiatives
and we are a Digital Resilience solutions company, focusing on
obviously observability, SRE, cloud ops, infrastructure,
hardening support, and a big area for us is security, so I'm excited to weave some of
this together for us here today. Excellent. So folks, what we're going to do here is sort
of a round table panel discussion. I wanted to take advantage of the fact
that we have Chris and Glenn over here and they both between them, have a great deal of expertise around
observability and the broader IT area as well. So I have some questions
that I'm going to put to them. They go back and forth. We'll talk a little bit about
their contrasting experiences, but if you folks have questions,
commentary along the way, I think that would be really
great to hear as well. I'm happy to repeat your questions, but this really is an opportunity
for you to converse practitioner to practitioner person living the dream, two person living the dream.
Alright, before we get started, you explained your
background a little bit, but I thought it'd be fun to
talk about a little bit more. Maybe, we can start. Chris, what is the
most embarrassing app on your phone? So this was the "heads up" of potential
questions. I did have to look this up. I've got a hundred apps on my
phone and I use seven of them. So I reviewed it before this and I
believe the most embarrassing for me personally is Tiny Zoo.
Tiny Zoo. Tiny Zoo. What is Tiny Zoo?
It's a really old one. It's one of those things where you have to
do a little piece of work and it enables you to do another little piece of work
faster and then you do another piece of work faster. So really just like
Observability. Oh, there you go. Yeah. There you go. It all comes full
circle. Glenn, how about you? Well, I had to scroll
through a bit as well. Probably the most embarrassing thing is
just the volume of apps that are on the phone that I feel like customers with
data and they just have data everywhere and they don't know what or why.
So that's my apps, but Garage Band. Maybe it's there by default,
I don't even remember, but I'm not sure I've ever opened it
and I'm even a "has been" musician and I still just nothing with it. Well, at least you
tried step one. Alright, I told you guys it's going to be a
serious detailed intellectual discussion. Alright, so we talked a little bit about
your backgrounds, both of you, right? The big question that's top
of mind for me and Chris, I'd love to start with you over here, is why is observability
important to your business or to the business of your customers as
well? Both parts of it are important. I'd love to just get your take on it
from a business perspective considering. So the organization that I work for
is kind of called Tech Ops within Dell, and we're like a layer of services
that developers use to write their code. So we own the
get parts, we own Jira, we own the whole process for
which people are doing their development and for us it's
really important to know
how well that's going for them. We're the middle of
all of these processes, so if something is not working or
something is slow or God forbid something completely breaks, then
10,000 developers are stuck. So it's really important for us to be
able to see what's going on in that black box and expose that data. Okay, and is that actually
10,000 developers? Yeah, there's 10,000 developers that
rely on our services. It's true. Wow. And growing I imagine, too? Yeah. Let's say it's growing. Glenn, how about you? How would you say observability is
important to TekStreams business and your customers? Yeah, I'm going to answer on
behalf of customers if I could. And I failed to mention in my intro
that I work with some selected customers on strategic
initiatives that they have, and observability is really an area where
we're seeing a lot of movement right now. There's just a lot
of acceleration there. So one customer that comes
to mind in particular is a large enterprise. They're very
distributed geographically. They have venture arms, they have
small operations, large operations, a lot of innovation happening. And so just the sheer volume of
what's happening and their need to understand that. But they also, we talked earlier about this struggle
with governance and innovation and whatnot. So enabling people
to go build and deploy without getting into trouble or over
their heads is really important. And in a lot of cases these are
customer facing services that they have to know are going to deliver,
so it's a critical function. So that brings up a really
interesting point, and I think Chris, I'd love your take on this as well. You mentioned customer
facing services there. Have you seen any difference really
in how observability is approach for customer facing services versus not
customer facing? Purely internal ones? Yeah, I'll start. One is
just pure speed to market. We have one particular
scope where the ask was, "Hey, customers are using this already, and our clarity of the health of the application is marginal, so anything
you do is better than what we had today. How fast can you go or
better than we had yesterday? How fast can you go?" And so it's just
an example of the pace of innovation that's happening. And we're going to talk about this
a little more in the context of AI, but speed to market really critical there. So I mean you have really different
objectives there. So for us, I mean we consider the
developers to be our customers. So for that customer facing thing, we want the business value for
them is getting that code out fast, getting the PR through, et cetera.
On the other side are our ops teams, so our operational teams for every tool. And typically people are
segmented across different tools. So they have expertise in
that particular system. They want to get to the MTTX quickly
when there is a problem or there's an SLO violation. So it's slightly different goal in terms
of what you're trying to support there. And sometimes that can be different data.
So we're collecting different things, present it in different ways. Gotcha, gotcha. Now this is going
to be a difficult question for you, just considering the volume of engagements
you see and the size of Dell itself, but what challenges do you often
hear from your internal customers, whether they happen to be focused more
on internal applications or on external ones, and what challenges have you
faced in your journey of maturity within observability as well? Yeah, when I think about this, I mean I think a lot more about
our particular challenges, which I think people have talked
about a little bit here today as well. But as I mentioned before, we're
kind of doing the centralized model. We call ourselves an enablement
team because we're trying to get everybody that owns these different tools, getting that data in so that they
can do their operations well. And our problem is just that takes a lot of collaboration. So you've got people
that are experts in their domain, but not necessarily observability experts, and you don't necessarily want
a hundred deeply connected observability experts. You don't need every tool owner to
know everything there is about Grafana, but people need to have enough skill to
be able to use that effectively and use the tools that we're showing to them, and they also don't have time to do the
research on some of the cool features that are in the cloud. We are here
to learn that, expose that to people, get them using it effectively.
So I think especially, Dell, is like a global organization, so there's time zone challenges
and different priorities
among different teams. And so I was actually really interested
in some of the stuff that you were talking about earlier with culture and
some of the other people had mentioned, like Kyle was talking about how we might
help overcome some of those challenges because that for us, I think has been
kind of one of the main sticking points. Yeah, I would just add, I really enjoyed the comments earlier
about understanding the behavioral change that has to happen and
creating a culture for that. I see challenges around adoption
almost inevitably there is some sponsor somewhere in the organization
that says, "Hey, I see a path forward. Here's a platform, here's a capability." But
without alignment from say, line of business or other areas that
are going to provide the funding and alignment for that, then adoption struggles in
the developer community. It also struggles on the line of business. It struggles out in the
venture arms and innovation. So connecting those worlds together. And that's a lot of the work that I've
personally done and some of our teams have done is we'll work with one part
of the organization that's finding some traction in one area, and we'll go grab another part of the
organization and bring them together and say, "Hey, let's share
what we're learning. Let's share these opportunities
for better adoption and funding."
Another area that we're really seeing some recent traction in is for these
customer facing mission critical type of application areas, looking at the customer experience and
then working backwards from there into the incident response and even
support metrics and saying, well: "How can we define a
better customer experience? How can we enable that through better
support?" And then we're asking for adoption and observability to enable
that customer experience in the lower support costs that go along with that. So those are challenges that
we're seeing where frankly, there's some exciting changes happening. So the cultural barriers,
the cultural differences, and then the different focuses needed
for customer facing applications. Okay. When you talk about your platform today, we talked before about how
most organizations have a
large number of tools that they would consider to be part of
their observability stack in somewhere. When you chose yours, Glenn, at Dell,
what were the important criteria? Any your choice of tools,
platforms as well as partners? Sorry. Was that for me or for Chris? Sorry. Or for me? Go ahead. Either a few. Pick one. We can both. Yeah, both of you please. Sure. So I mean, I think the three main things
that we were kind of looking at when we were trying to
bring this all together is flexibility and standards and
that single pane of glass idea. So flexibility, the Big Tent philosophy is super helpful
in getting some immediate adoption because you're not having to roll
out the collection to everything all at once. People are already
doing some kind of observability, so we can bring that data
in and that leads to that single pane of glass, but it's accentuated when we have
something like Grafana Alloy, which is open telemetry standards, right? It's a wraparound open
telemetry collector. So that
gives us some independence. In the future, of course, we'll
always be staying with Grafana, but if there were other tool choices
that had to change that gives us that anchor in standards that is useful.
And then once we're doing that, we're getting the metrics, the logs,
the traces, hopefully profile soon, and then able to see that in the single
pane of glass connect things together as other people mentioned. And that gives us a better sense
of what's going on with those particular tools. So those three things were kind of the
big drivers that we didn't see all of that in other tools that we evaluated. I would just echo the data that
we've seen up here. I mean, every customer I've talked
to has said lots of tools, probably too many tools, lots
of data, probably too much data, probably stored in too
many places. So for me, when I think about the future and
the pace of innovation that we're all experiencing, I want to see a
pace of innovation of a platform. So when I look at Grafana, I'll
make a plug for Gartner here, but if you look at their Magic
Quadrant for observability, I think the right year is 2022.
Grafana wasn't on the map, and today they're arguably
in the leading position, and that's just in a few years. To me,
that just screams pace of innovation. And so if you add to that, the unknowns that we all wrestle with
every day about what will things look like even six months
out, we just don't know. And so I look for a company that is very
open minded in their thinking so that they can adopt to whatever our
future becomes. Then I look for a large base of talent. We all have to learn things quickly, but is it 25 million Grafana
users, 25 million about? That's just one metric. But it tells me that there are a lot of
people that already know something that are interested in this.
And so if I'm a business, I have to build things quickly, change
quickly, then I need talent to engage, whether that's people to hire,
consultants to bring in or whatever. And then I also want flexibility. I want to be able to try things to build, to experiment without having to make a
big long-term commitment to a platform. And so I think the OSS capability plays
nicely with their word "dabble in it" or frankly on a cloud subscription. But I just see that as being a
really critical step is just do something experiment quickly. I wanted to tie in there was mentioned
earlier of the one-way and two-way doors. I'm a former AWS-er as well,
and I really buy into that. Most decisions are two-way
decisions. If it doesn't pan out, you can turn around and come
back without tremendous costs. So acknowledge when you're
facing a decision, which is it. If it's a one-way door, then do all your planning and analytics
and be very careful and intentional. Otherwise, speed is more
valuable. Just do it, try it, see what you learn from it, adjust and go. And so having the different
options of how to use a platform enables that in a great way. That's a really good piece of advice, and I see common themes between your
answer and then yours, Glen, as well, because when you talk about flexibility
and you reiterated flexibility, which you also talked about
looking into the future, I'm curious how far into the
future you look when you say, is this platform going to be flexible?
Are you thinking for the next six months, for the next year, for the next two years, what is a typical period that gives
you confidence in your experience? I mean, I agree with the
previous presenter that
anything past a year is like, if you don't like what you're
doing now, wait a year, it's going to be different. I would give a counterpoint
to that. It's hard to retool. I was just talking to a person
yesterday that said, "Hey, we're somewhat migrating from
one hyperscaler to another". And I said, "man, that's a big
lift". And he said, "Yes, it's hard". Platform changes. I mean,
they're necessary to some degree, but it's also a lift. And so I try and at least
think about 3 to 5 years out because think about adoption and
how quickly people change their behaviors. So I try and
look further out, and again, I tie it back into my prior comments
about flexibility of options, architectures, licensing
models, resourcing, all that stuff gives you
a longer runway, I think. So is AI going to blow all
that up though? I mean, right. We're just all experimenting with this
new technology and it's just changing the way that we're thinking about stuff. It seems so hard to make that
roadmap that goes longer. Which actually brings me to the next
question I was going to ask you is: How do you see AI shaping the future of
observability? In terms of automation, in terms of generating new
insights, things are moving so fast, and the crown seems to change on a weekly
basis between the leading players at the market. Yeah, I mean right now we're implementing
the, I think it's open source. Yeah, the open source MCP server for Grafana, and we're looking forward to talking
to our data, right? That's the idea. You connect this to an LLM, it's
got your data in the system. You ask questions, you
learn stuff. So I mean, I think that's a really exciting
thing that we can do right now. I think the overall vision, and Dell
is really big on agentic AI as well, is systems that are watching this
data, they're finding those anomalies. It passes it off to an RCA
agent. The agent does the RCA, then that passes it off to something that
could write some code or configuration that would go into get fix that problem. You get a human in the pull review, you get some review capability. But a lot of this work that people are
doing now that is represented in these MTTXs is just super shortened, or at least that's the dream.
So if we can get to that, I think we're all going to
have really different jobs. Agreed. Lots of thoughts there
from the audience, I'm. Sure. What's that? No, I was saying it sounds like the
audience had a lot of thoughts over there. What did you want to add? Yeah, I was just going to
add with the on invent of AI, certainly there's going to be more
volume, more volume of every layer, every angle, everything, and so the ability to sort through the velocity and the volume, weed out the noise and discern action
is going to become more and more critical. We all know that each of us are
going to have to manage more information personally, and we're
going to need help with that. So I think about when
you go to see a doctor, a specialist, how much time do you spend in the office
and how much of that time is actually with the doctor? I think for
our support agents, our SRE, et cetera, we're going to move more and more to that
where things are teed up and we enable people with great context, great history, great suggestions, but we still leverage the discernment
of humans to do at least the critical things. And I think we're also
going to see automation when there's high fidelity of context and
data and history and there's lower consequence of action. I think we're going to see
a lot of automation there, but certainly faster.
Everything's going to be faster. I mean, it really is a
pivotal point in time, and that's why we are investing in
this practice and growing it right now. Because to your point,
if we don't do this well, then all this hype and all these, look at all of the spending that's
going into infrastructure right now, whether it's energy or data
centers or that's all to build more stuff that we're going to be managing. So it's a critical point in time. That's a really interesting topic overall, because one of the backbones of the
series of talks we've had today has been around how do you organize the people
and the processes to be able to deal with the technical challenges
we have in observability? And we talked about if the volume
of innovation is going to increase, the complexity is going to increase,
data volumes are going to explode. One might argue that the centralized
model that has been the go-to model for more mature organizations, I
wouldn't say it'll go away, but you might say that it would have to
evolve and perhaps put more capabilities in the hands of developers or other
parts of the organization as well. So today, if you look at how
your teams are organized, keeping in mind that you are at
the center of the AI revolution, Chris, right? How are you planning to evolve your observability team organization tomorrow? And if you could contrast
that with today as well. Yeah, I mean, just to call
back to the, so for us, that challenge before of the collaboration
with teams where we've got the subject matter experts for various
tools that we need their help to do things. I think Fleet Management is kind of
opening us up a little bit to be able to get in there and standardize
things a little better. So for us, that's a new thing that
looks very exciting in terms
of making that centralized organization work better. So I don't know that it actually
changes the way that we organize it, but it gives us a tool that
lets us get to all those things, have recipes
for the various tools, add a security layer that's consistent
across all those different tools. That's the hope that I have
going in the short to medium term that will help us accelerate
our observability journey. That's a good point. And especially
as you value flexibility, no matter how the organization
evolves, if you feel confident, the fleet management can keep up and
adapt to whatever you need to do, that bodes well for its future
within your stack. Thoughts, Glenn, anything you want to add? Yeah, I just wanted to share a
customer that has a little bit of both. They have a little bit of centralized, a little bit of decentralized
large enterprise, tens of billions in revenue. And the centralized team does manage
multiple platforms. They have roadmap, a vision. They have
programs to drive adoption, technical and business side, but they've also allowed for
other parts of the organization to make their own choices.
And was mentioned earlier, if you choose to deploy and you're not
following our standards or our platforms, then good luck, happy to help later, but let us know what you learn otherwise. And they've really embraced both
models and they've done a good job of collaborating back and forth. And so yes, there's a little bit of
downside to probably any model, but they're also getting the upsides
of both because they collaborate. I've also seen other enterprises that
have both without the collaboration and that doesn't lead to fruit. And this particular customer
has also allowed for multiple deployment models of Grafana
in the environment. And again, they learn from each
other in both scenarios, and they could argue pros and
cons of both, but overall, the organization is flourishing and
at times they work together to drive business values. So I've seen, I
just wanted to put that out there. I think it's been pretty cool to see. Yeah, for sure. So as we get
to the close of this one, I have one final question for both of you. And I also wanted to throw a
question open to the audience. You've heard the themes of
adoption, governance, people, relationships and business value
echo throughout the day over here. So does anybody have any creative ways
in which you have been able to grow the adoption of your observability
platform, whatever it is? This is a great venue to just
share nuggets. Yeah, please. So I run the observability
team for Cisco Collaboration, and we had a couple of
different things that we did. One is when we built out, we started in one part of collab, and we would find other teams
that had little Prometheus or Grafana stacks running, and
we kind of just onboard them. We wouldn't do a big planning
session and a quarterly review. We kind of just grabbed the
data and then show the value, sort of the old adage, beg for
forgiveness instead of asking permission. And it worked. And we're about, I
looked while I was sitting here. We're at 500 million active
series now across a dozen Mimirs. And we're at the point now where
teams come to us, we are the default, and they don't want to be in the
business of running their own stack. So I guess that's our story. I'm
wondering, Glenn or Christopher, if that resonates with either of you, that strategy of grab the data
and once you got to critical mass, did the teams just come
to you as the default? Yeah, absolutely. That's kind of
a variation on show the value. So I think a lot of our better
successes have come when we're showing people, look what's going on. And I think you were calling it
application observability earlier. I know it as Asserts, but look what's
going on here in your Kubernetes cluster. And people are like, "Oh, wow, my
Kubernetes cluster has a Grafana built in, but it can't do this" because
it's some bundled thing. It's not the cloud features. So that thing of when
people get to see it, once the data's in there and they
can see it and they start to use it, then it becomes a must
have and not a like, "oO, that's a cool little thing
that you built there". So that's key to getting adoption
across the organization for sure. Anyone else from the audience want to
volunteer a spicy take on adoption here? Just want to comment on, I've done a very similar approach where
I'm working as a quick serve restaurant in Atlanta, and while I've heard mostly
here talked about approaches for technology groups, organizations, the same approach can be used
for product development as well. And what I've had a lot of success with
is reaching out to product owners and people that are working directly
with customers and saying, "Hey, what do you need to know?
We have all this data here, hear what questions do you have for
us? What can we possibly tell you? What questions are you getting that
you wish you could get answers to more quickly?" And just build
dashboards for those topics, and they end up getting used very
quickly and with a lot of energy. And so had a lot of
success with that approach. It's great to hear. I think
that combination of, I guess, curiosity about their world as well as
the ability to help them can be very powerful. Is there another one? Okay, one final one, folks. So if you have one recommendation for the
folks in the room who are embarking on an observability journey or a strategy
overhaul project, what would that be? So I think people referred
earlier to the different to maturity models for observability. And I've seen one a couple of times
that kind of followed what people were talking about earlier, where you've got the reactive phase where
you're going on a machine and you've got logs on the machine, not very good. You've got a second level
of siloed monitoring, but the data's not very
consistent. At the third level, you're collecting data in a centralized
place, you're getting telemetry logs, et cetera. If you go a level above that, you're automating more stuff. You're using predictive analysis to
see what's going on in your systems. And then finally, the glory of the AI world aligned
with your business objectives. So you look at, I mean, I think it's very helpful to look at
that maturity model or any maturity model have been presented earlier
today and say, well, where am I? Can I get to the next step?
What is the next small step? And this was also mentioned earlier
as well. I think it's super useful. Take a small step. I would throw
in there, automate that small step, because if you want to
do it with another team, now you've got a little piece of
something that makes it go fast. But just like small steps, right? We did try to boil the
ocean our first year. It was not particularly
successful, right? Yeah. Okay. Great tip. I would just say run. Seriously, away or towards? I mean, start with the visualization
for your first meeting. Give people things to react to.
And we have a window to get ahead. And so many are the
initiatives that succeeded by moving quickly. And many are those that have failed
because they analyze too much upfront. We all know it. So this is a platform and an
ecosystem that enables you to experiment, try things,
unwind it if it doesn't work, but build and innovate fast.
Go, go, go, would be my, and we're doing this in
strategy kickoffs right now, where we're starting. It feels so crazy, but we're starting by building and then
we're talking about it and planning kind of around that. But it's just easy to
unwind it if it wasn't a good idea, but then you have that behind you. I
know it's crazy, but that's where I'm at. Well, how do you talk people out of the
Big Bang theory if they want to go big? Yeah, difficult one. I'm going to let that one go. Alright folks, so questions
from the audience, right? Anything that's top of mind,
what would you like to learn? What would you like to
ask our panelists today? I don't have a question, but I do want to piggyback on the last
question and something that what I've noticed too, to help kind of enhance the observability
team itself for one of my customer, and it's Dell actually,
is creating a community, and we have community
events biweekly where we do crowd driven enablement. So when your stakeholders have questions, have them dictate and build that community
of the users and create that user group mentality, it really kind of
helps expand what you're trying to do. So kind of a callback to the center of
excellence from the previous one Yeah, for sure. Exactly. Exactly. You're trying
to build a community, right? You're building your own internal
Grafana community within your business, and you want those champions. You want the people that are excited
about this stuff and see the value because that will spread to the folks that might
not be on the same page as that and might have a different opinion.
And then they say, "Oh, wow, well, DevOps engineer number two
just solved this problem, lowered our MTTX by doing this,
this, and this. Let me try that. Let me start to see the value
there". So community is important. If there are no questions from the
audience, then well, I guess we will wrap. Thank you very much, Glenn and
Chris for all of your insights. Really appreciate the time we took today.

