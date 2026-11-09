# Enterprise AI Adoption at Scale: Costs, Security, and ROI | BlackRock, Rapid7, WEX | Grafana Labs

Published on 2026-11-03T18:56:54Z

## Description

What does enterprise AI adoption really cost, and how do organizations weigh the investment against the return? Leaders from ...

URL: https://www.youtube.com/watch?v=JcqV4fOQODw

## Summary

The panel discussion titled "Enterprise AI Adoption at Scale: Costs, Security, and ROI" took place on November 3, 2026, and was moderated by Andrew Zigler, host of Dev Interrupted. The panel featured Barry Driscoll (CIO at WEX), Elaine Hardwick (VP of Platform and Developer Experience AI at Rapid7), Olin (supporting Aladdin at BlackRock), and Joe McManus (CISO at Grafana). The conversation revolved around the complexities of AI adoption in enterprises, focusing on costs beyond just financial implications, including operational and cognitive costs, as well as security challenges. Key takeaways included the importance of collaboration across teams, the need for robust security measures, and the necessity of adapting organizational structures to accommodate rapid changes in technology and processes.

Topics: AI adoption, costs, security, operational challenges, organizational structure.

## Chapters

00:00:00 Discussion
00:06:21 Evaluating AI ROI and operational costs
00:11:53 The hidden costs of AI adoption in organizations
00:18:14 Managing security in AI development
00:23:38 Discussing the costs and challenges of enterprise AI adoption

Now we're going to move into a panel. There are obviously great capabilities that are emerging with the use of AI and these agentic technologies, but there are also a lot of practical questions being raised—things around security, cost and spend, and just generally around keeping our sanity. To dive into these topics, we've got some people who are dealing with these kinds of problems every day. 

So I'd like to invite up to the stage Joe, Elaine, Barry, and Olin, and moderating will be Andrew. Come on board!

**Andrew:** All right. Hello! How y'all doing today? I'll try that again. It's after lunch. It's all right. How are y'all doing today? 

**Audience:** Great! Amazing!

**Andrew:** I am so excited to be here hosting this panel for y'all today. We have some amazing experts on stage with me, so I'm not going to take a lot of time to set us up here. My name is Andrew Zigler, and I'm the host of *Dev Interrupted*. We're a podcast and newsletter for agentic engineering leaders. Today, we're having a conversation that I've been having all year, and that's about the real cost of AI. We're going to get down to the bottom of it from different perspectives because cost is more than just a dollar sign, but it is a dollar sign too. We're going to be getting that scoop as well.

Today, joining me on stage are some incredible guests. I'm going to give them each about a minute to introduce themselves. So Barry, how about we start with you?

**Barry:** Sure. Good afternoon, everyone. I'm Barry Driscoll. I'm the CIO at WEX, based in Portland, Maine. For those that don't know WEX, we're a two and a half billion dollar FinTech in the B2B payments industry. We process over a few hundred billion dollars in payments a year in three primary segments. The first is our mobility segment, which you can think of as fleet cards. Most of that spending is on fuel. The second is benefits payments. For those that have an HSA or an FSA, there's a good chance that WEX is the technology behind the payments for that. The third is our B2B payments, which we're mostly focused on in the online travel agency space, making payments on behalf of all those companies you use to book your trips. 

My role at WEX is CIO, which means I oversee all of our infrastructure technology, the majority of which is cloud-based, our employee technology services, our business systems, our platform engineering organization, and our site reliability team, which is responsible for our 24/7 support. That's where observability sits for us at WEX. Lovely. Thanks for having me.

**Andrew:** Amazing. Elaine?

**Elaine:** Sure. I'm Elaine Hardwick. I'm a VP of our platform and our developer experience AI, which is a mouthful to say. I work at Rapid7. For those of you who don't know Rapid7, it's a cybersecurity company. We focus on preemptive MDR. We are ingesting tons of different data sources at a very large scale, trying to enrich with all of our threat intel, all of our cloud, all of our on-premise, and making sure we're responding to things faster than those attackers. As you've probably seen in the news, there's more and more of this data coming through, so it's really important for us to get ahead of that. 

In my role, again, I'm focused on the platform, so I'm helping to ensure that all of our foundations are really secure, scalable, and operating at the scale that we need. On the developer AI side of the house, we've realized we need to go faster, so we have to invest in this AI SDLC initiative. This involves adopting, measuring, and ensuring that we're staying ahead of these attackers with our product delivery.

**Andrew:** Amazing. Olin?

**Olin:** Awesome. Hey everybody. Good to be back at ObsCON. I'm Olin. I work at BlackRock, specifically supporting our PaaS or SaaS business, Aladdin. I support two core platforms for that business. One is our service platform, which includes the CMDB, instant change management features, and other service management features. The second, and maybe more relevant here, is the observability platform. 

From a scale and scope perspective, I think of my first job as a platform engineer as stability first. The platform needs to be available and working for our clients. I think about two important sets of clients: the 5,500 engineers, data scientists, and data engineers working on financial models, and the business users who operate on the platform every day. So, I focus on scale for both engineering and business users, with an emphasis on stability in my space.

**Andrew:** Amazing. Joe?

**Joe:** I'm Joe McManus. I'm the CISO at Grafana. I think you might have heard of it. I'm in charge of the platform team, the foundations group, and security that makes all the products we've been talking about. We've moved into making these AI observability products. If you look at some of the demos, we were showing conversations being recorded, ensuring that we've shifted left in our development practices. We're building things that you'll trust us with your data, ensuring that we're reliable, resilient, and can meet the demands of a Black Friday. If there is an incident—and there always will be an incident—we ensure that the blast radius is contained, your data is secure, and there's no interruption to your services.

**Andrew:** Amazing. As y'all can tell, we have an incredible panel assembled here today. There's some really high-level expertise here at some of the largest companies working with data and AI, so the stakes are incredibly high. I want us to start with the topic of cost today—the dollar cost—and I'm going to start there with Barry. I want to understand from you, Barry, how do you evaluate the AI ROI of your investments and the tooling that you've been working on this year? 

**Barry:** Yeah, sure. The obvious metric people talk about is workforce productivity, and that's something we definitely look at. We are continuing to scale up our company and grow, trying to do that in a nonlinear fashion relative to labor and the people it takes to scale. Productivity is a real thing, but beyond that, we look at a lot of other metrics. We are a software company, so those platforms I mentioned are our software platforms that we sell to our customers. One of our biggest investment areas is around the agentic development life cycle. We're working to increase our product velocity, allowing us to release products more quickly while ensuring they are high quality and secure. We're seeing some really good results there.

Outside of that, we're also looking at ROI for revenue-generating projects. We are actively investing in projects to use agents to help our sales processes. I can talk about examples, but that revenue generation is one of our ROI areas. We're also very keen to improve our net promoter score and ultimately our customer experience. Where we can implement AI to help us deliver better services to our customers, let them self-service as much as possible, and hopefully walk away with a better experience is key. Another area very apropos for this conference is around reliability. We are investing in AI projects for reliability, incident reduction, MTTR, and MTT star improvements, and we're seeing really good results there. So it's definitely not all just about labor savings, which obviously gets the most news.

**Andrew:** Absolutely. I think that becomes a place to start. I'm curious, any of our other panelists, does any of that resonate with you or something that maybe you've seen stand out in your own company as well?

mean, every ObsCON needs MTTR in every session. I agree. Check that box for sure. We just hit our quota. I think the other thing though that we've been seeing is that in the observability space, the speed at which we can actually improve the maturity and the instrumentation of the application stack itself is also really important. I think that the tools can help teams that used to struggle to get the time to invest to improve the quality of their stack. Now we're seeing AI helping to accelerate that. When you can trade tokens for better telemetry in the stack, it can be a multiplier in that way. So definitely core MTTR, but then also how to improve the maturity as well.

Yeah. So starting with the dollar amount and then moving into how it actually gets operationalized, you talked a lot, Barry, about using it to measure cost savings, and that becomes a way of proving ROI. Then it moves further downstream into the organization, into the ops world. And Olin, I love that you spoke up because I want to lead with you on this next one about when you think about the operational costs of AI that maybe doesn't make it into a lot of business conversations, maybe the conversations that Barry's in, right? So how do you think about it as an ops leader and about making sure that those things get elevated and we have those real conversations about operational costs?

Sure. I think, and I'm sure everybody else is going to have thoughts on this one. My general feeling is that AI has a big second-order effect impact. So AI, I think we've talked about several times today already, some of the folks I met yesterday, everybody is seeing a multiplier in terms of PR and code change in their spaces. I think that's pretty much universally felt. So that's like a first-order effect, but there are several second-order effects that... Sorry, can you guys hear again? There we go. There are several second-order effects that also matter. 

I think one of them is as you accelerate the amount of code change, you build more products, you build more capabilities, telemetry becomes more prevalent, products become more prevalent, and the ability for operations to support that explosion and growth is something that we're tracking against. When we get those outcomes that we want for the business, we have to support the outcomes in the ops world. 

I think the second other effect that matters is agents themselves, and AI itself is able to search and query telemetry much faster and much broader. When you are capped by the number of people on call who can look at a dashboard, you search less. So I think both of those factors mean that the second-order effects of AI in operations especially are things we're still adjusting and figuring out. I think there are some huge hidden costs with AI. 

And so we've really, as you see, we're big AI users here at Grafana, but we've empowered people to code for themselves. Everybody's a citizen developer, but it's as if we've given everybody a hammer and told them that they're now carpenters. So they don't understand the fundamentals of computer science. They haven't read the Phoenix Project. And so there's this downstream effect where now we're standing up, okay, do we go with Vercel? How can people deploy this securely? Do they know how to monitor it? Do they have anybody standing up to support it when it breaks? How do you support the whole SDLC? 

So there's a hidden cost that we have to engage with security. When do we scan it? What tools can apply? Now we had to ramp up our DLP because it's not that AI is less secure, it's that it's exposed some of the failings. If you think of the fundamentals of the CIA triad—confidentiality, integrity, and availability—it's exposed some fundamentals there that maybe you didn't fix correctly when you had human actors, but now that we have non-human actors, it's really kind of highlighted some shortcomings that have had a multiplicative effect of cost for us.

Absolutely. I think the multiplicative effect of those costs becomes a lot more real when you move into the operational world, and then there's a lot of opportunities to leverage it to not only make your own feedback loops better, but those of your agents and the whole system you work in. It also invites us to reimagine and revisit the processes from before and be able to find new savings or new ways of doing stuff that are just completely re-imagined. Those become the new opportunities, I think, for teams as they move through that space.

And from there, I really want to move on to talk about, we've kind of covered a little bit about the dollar costs and then the ops cost. Someone has to work with it; someone has to implement it. But in reality, there's also a cognitive cost that builds up over time, and it isn't something that is immediately visible. It takes a different shape for the types of teams and ways that they're using it. 

I'll give you a really firm example. AI acceleration and adoption this year has not been equally graceful to everybody in the engineering world, and we know this. If you're a front-end developer, you're probably having a lot more luck a lot sooner working with LLMs to generate React than an embedded systems developer working in their own language. Those barriers kind of create an unequal kind of velocity between teams that show up as pain points and frictions. 

And so I want to focus a bit on that element of adoption and culture within organizations. I want to give this one to Elaine about how you think about, as an ops leader, creating the right environment for your engineers to be successful with each other and their agents without clobbering each other.

Yeah, it makes sense. It's kind of an interesting thing. I read Molly Graham's article recently about the Lego piece, and one of the things that's fun with that one is basically as you're building, you build something, you tear it down, you shift it, and you give it to someone else. With AI, you don't have that ability. So one of the things that a lot of my engineers are struggling with is they're constantly building all these things, but they don't really have anyone to hand it fully over. You give part of it to AI, but you still have the accountability that you have to maintain and control and govern and make sure it's in a good spot. 

And so with our groups, the things that we've really focused on were first managers. As humans, we have managers, and we want to make sure that they understand the workload that we're having and all the burdens that we're having. So we created a lot of programming around management training, making sure they understand how to go end to end through our AI SDLC, making sure that they've actually pushed PRs and had that experience and understand some of the pain points. 

At the same time, we have AI champions. Those are those people that are really hungry for AI and love it and want to evangelize it and want to make it a passion project for their team and share as much knowledge as possible. And so we've made a ton of investments around that—lots of training, lots of time where we can just sit and listen. I think that's probably one of the biggest things is learning from each other and figuring that out. 

And then obviously we have our vaults and a lot of our tools in order to make sure that we're establishing processes and patterns and things so that people don't have to relearn everything on their own. I'm so glad you brought that up too, because that's what I think of as it becomes a hidden cost, absolutely, where you get these different agentic centers or agentically enabled groups of folks, and they all invent an agentic way of working with maybe your whole stack, and they did it three times over. That's a three times over investment that you didn't need to make. 

And so if you had created the environment for them to surface and collaborate together, then you'd have one more cohesive system. Those become the challenges, I think, as we move.

into more operationalizing with AI and our AI SDLC from end to end is revisiting that stuff and making sure we have those kinds of conversations. Since it's unequal and different people move at different speeds, I think it's great that we have conversations as well, like the one we're having today. 

In the movement of all of that, I think something that can be a stickler in the AI adoption journey at any organization could be security and the security team. There's no bigger nightmare for the super agentically 1000 X engineer than to get a DM from the CISO or someone in the security organization asking, "What are you doing?" Those costs are just as real, and they manifest in much uglier and even more invisible ways that are further removed from the agentic loops that are causing the problem. 

So, I want to move into talking about guardrails and security and maybe hand this over to Joe. From your perspective as a CISO, what are the trade-offs in an agentic world that keep you up at night, and how do you make do with them?

**Joe:** Well, I feel seen. Initially, when AI started blowing up, it just changed. It got real so fast. We focused on what the developers were doing and how they were going to change with this. Honestly, the developers have not been a problem; they have been fantastic. At Grafana, we partnered early and often. Almost every new AI product that was shown this morning, we partnered early, shifted left, and made reusable code that we checked multiple times for security. We ensured that the sandboxes were secure. 

That's great. We have a fantastic relationship. In fact, we were just asked, "Hey, can we get somebody to be fully embedded with the AI team?" I don't have the headcount, but I would love to. What keeps me up at night is actually the newly empowered citizen developers. Once again, AI has not made me less secure; it has exposed failings in our platform. You would go into a tool and say, "Can you get me this information?" and it will try every way it can to get you that information. 

What we've had to do is ensure that we have the right identities tied to the right people, that they're short-lived, and that they can access the right data. Some of the things we've had to do include increasing our use of DLP (data loss prevention) software to ensure that if you follow along, we had an incident back in May. We were part of a supply chain incident that many people were hit by. Honestly, our biggest impact from that was some of the data that people had put into GitHub from using AI tools or writing their own tools, which then falls into what you talked about earlier—multiple people inventing the same product. 

At Grafana, we've really tried to say, "Here's our catalog of products." One of the founders of Grafana helped make a staff apps product that can let people deploy their software securely. The Orbit app that many of you were using was written with a lot of AI assistance and deployed quickly. We had to adjust to say, "Hey, how do we do this the right way?" It changed our whole paradigm for how we deployed software. 

So, when you're in that environment and moving so quickly, how do you think about creating the right kind of guardrails for people to develop safely? 

**Joe:** What we've had to do is put in static analysis tools into GitHub. We require PRs. We are using Truffle Hog and everything we can to look for secrets and check for SQL injection and cross-site scripting. We've had these tools and plans to deploy them at certain times, but we've accelerated all of that. Now we're doing it much faster. We're building our own harnesses for penetration testing and vulnerability analysis for our home-written software. It's just been constantly deploying because every week there's a new thing. I mean, two weeks ago, had anybody heard of Jiv? For one week nonstop, that's all we talked about. The world was going to change because of that. 

So, it's really about reacting quicker and sort of throwing out your roadmap. Even though you're holding to the fundamentals, you're reacting much quicker. You're no longer planning a year out; you're planning weeks out.

**Speaker:** Just following up on that a little bit, it's definitely beyond the developers for sure and the AI tool sprawl. We are facing that for sure. We're a public company, very highly regulated. We've got PCI, SOCs, HIPAA, HITRUST, and on and on. We take security very seriously, certainly all the automation around secure software and secure release management. But beyond that, there's a new tool every week. 

One of the friction points for WEX is the general audience idea of, "Hey, all these great tools, let's start using them," and the risk to the company of doing that. We certainly have a governance process, but one of the key things is vendor risk management. We see that as one of the highest enterprise risks in the company. We do a very rigorous review of those things before we allow any production data or usage. 

People feel like, "Okay, well, you're slowing us down." One of the things we're doing in parallel with that is trying to be really clear in our communication. It's like, "Well, this is what we're trying to protect the company from. Here are examples. This is why we use that process." We also have our architecture review board to ensure we're looking at things carefully. We want to move fast; we've introduced a lot of tools, but it's never fast enough. We feel like we're trying to balance pragmatic implementation with security. 

Also, there's a balance in what you both said. You started with a list of technical solutions to solve all of the problems, and you began by talking about it in a communication way because we have to attack it from both sides. Ultimately, it's about creating the enablement. Just as quickly as we can turn code into any kind of product we're trying to deliver, writing code is no longer the obstacle or bottleneck; it's obviously moved into other places. 

Being able to quickly take that capability and turn it inward on your own company, let's get enabled across the board, let's have that ecosystem, let's have that catalog, and just take the time upfront to invest in the roots. Those become, I think, the fundamental ways of controlling and understanding and communicating about cost. 

I'm curious to know if any of our panelists have more color to add from the worlds they come from. Are there other costs that you think we haven't talked about today that are definitely lurking and part of everyone's day-to-day? 

**Panelist:** I would say the way data moves around now has changed. Before, you had it in a MySQL database or your G drive, but now these tools pull everything together and aggregate it. The end user just wants to see a quick summary of it, not realizing it's stored somewhere. Some of the costs are now that we've had to accelerate how we're doing EDR. I wouldn't want to do this, but I could see something like WEX, highly regulated, where maybe now you have to have an allow list of software that could actually be installed. We're not there, but I see why people do it because the sprawl of tools and data is something entirely new and has created a new challenge. 

**Another Panelist:** I think one other thing we didn't touch on is that the core of the team structures we've built has all been designed around the way we used to build software. So it's not just the security constructs, but the...

Actual organizations themselves. Would we design the organizations the same way now if we were launching at this moment? Do we have very large platform organizations with teams running a lot of microservices, or are microservices actually part of the problem because now you can more vertically integrate? Some of those things I think are costs that we're going to see because we're going to want to adapt to the way we build.

And the planning process, right? We've talked about that a lot, but our customers are expecting us to deliver X feature at this point in time on this roadmap, and things are changing so quickly that you can't really commit a year out, like you've mentioned. So that planning process is really kind of tilted on its head right now, I think.

A couple of maybe not as obvious costs to AI or the ripple effect of the AI industry that I see. One is for your software suppliers. For those looking at all kinds of contract renewals, the request for increased pricing is something I've never seen anything like. Now, some of this I'm sure is real, but there's also the tendency of the software vendors to say, "Well, yeah, your prices are going to have to go up because we're spending all this money on AI." And it's like, "Well, if you're not getting an ROI on that investment, then that's your problem. That's not my problem." So we are seeing that, and there's spending a lot more time on negotiation and contract renewals.

The second one is for those that need to buy thousands of laptops for their companies. The price of laptops has increased 50 to 70% in the last 12 months as a result of the RAM shortage and just chip shortage in general, which was not something I certainly was thinking about a year ago. So there are other ripple effects way beyond token costs.

Cost is very complex, y'all, as we've very much learned here today. What we've learned about costs too is that there are the obvious costs, like the dollar costs, there are the hidden costs, and there are the costs that you have to really root out. But there's also the responsibility to reimagine the way we work and to rebuild the systems in a way that lets us have that trust again and to let us have the most synergistic system.

Something that's really happened in the last year is we've had to throw away a lot of our assumptions about how we work. It's like we talk about cost and how cost changes. I mean, think about just how building has changed in general. Everyone's obsessed with consumption pricing right now. The fundamentals are completely changing. Because of that, there's so much opportunity to learn and build something new.

I'm curious, just any closing thoughts about what would be your advice to the builders and leaders in the room about how they can take advantage of the opportunities in the industry right now and get ahead? 

I mean, mine's basic. Everything's changing. So take all of your previous assumptions, throw them out, and be willing to learn, be curious, and ask all those questions. I think that's the only way we're going to survive—thinking six months down the line and continuing to push ourselves to see where this industry is going. Being stagnant is not an option anymore, basically.

Yeah. And shorter iterations too on top of that, right? If you can't look that far out anyway because of that unknown and change, you might as well iterate very quickly. I'd push the partnership again. It's multiple teams working on things; before, it would be one team solving it. So making sure you can get in early and sort of get that economy by all solving the same problems and not rebuilding things. Also, sometimes ask yourself, should I buy it? I don't have to build it.

Yeah. I guess the other thing I'd add is taking a lead from Joe's comment around system development. It's really easy to create a prototype or a demo or an individual productivity tool, but scaling that to an enterprise that needs to run seven by 24 at millions of operations securely—with customers impacted directly if something breaks—is a different challenge. A lot is changing, but there are still some things that aren't changing. The processes around this stuff, whether it's IT service management or our general controls or legal compliance, all the other things, if you want to be able to implement something and run it at scale reliably, you still have to do the basics, and that's way harder than that demo. 

So that's the easy part. We've had some incredible experts up here today. Can you please put your hands together for them? This has been a super fun conversation to host. We're going to be walking off stage. If you have any follow-up questions, come find us, come chat with us. We had an amazing time up here—at least I did. I can't speak for everybody, but I had a ball. Thanks, y'all, for hosting us here today or for coming here today, and we'll see you soon.

## Raw YouTube Transcript

Now we're going to move into a panel. So there's obviously great capabilities
that are coming about with the use of AI and thisogentic technologies, but there's also a lot of practical
questions that are being raised, things around security,
around cost and spend, and just generally around keeping our
sanity. So to dive into these things, we've got some people who are dealing
with these kind of problems every day. So I'd like to invite up to the
stage, we've got Joe, Elaine, Barry, and Olin, and moderating will
have Andrew. So come on board. All right. Hello. How y'all doing today?
I'll try that again. It's after lunch. It's all right. How are y'all
doing today? Great. Amazing. I am so excited to be here hosting
this panel for y'all today. We have some amazing
experts on stage with me, so I'm not going to take a
lot of time to set us up here. But my name is Andrew Zigler and
I'm the host of Dev Interrupted. We're a podcast and newsletter
for Agentic Engineering Leaders. And today we're having a conversation
that I've been having all year, and that's about the real cost of AI. We're going to get down to the bottom of
it from different perspectives because cost is more than just a dollar
sign, but it is a dollar sign too. We're going to be getting
that scoop as well. And today there's on stage joining me
some incredible guests. I'm going to give them each about a minute to
intro themselves. And so Barry, how about we start with you? Sure. Good afternoon,
everyone. I'm Barry Driscoll. I'm the CIO at WEX based
in Portland, Maine. For those that don't know WEX, we're a two and a half billion
dollar FinTech in the B2B payments industry. We process over a few hundred
billion dollars in payments a year in three primary segments. The first is our mobility segment,
which you can think of as fleet cards. Most of that spending is on fuel. Second is benefits payments. And for those that have an HSA or an FSA, there's a good chance that WEX is the
technology behind the payments for that. And then third is our B2B payments, which we're mostly focused in
the online travel agency space, making payments on behalf of all those
companies you use to book your trips. My role at WEX is a CIO, and what that means for us is all
of our infrastructure technology, which majority is cloud-based,
our employee technology services, our business systems, our
platform engineering organization, and our site reliability team, which is responsible for our seven by 24
support. And that's where observability sits for us at WEX. Lovely. So thanks for having me. Amazing. Elaine? Sure. I'm Elaine Hardwick. I'm a VP of our platform and
our developer experience AI, which is mouthful to
say. I work at Rapid7. So for those that you don't know
Rapid7, it's a cybersecurity company. We focus on preemptive MDR. So we are ingesting tons of different
data sources at a very large scale, trying to enrich with all of our
threat intel, all of our cloud, all of our on-premise, and making sure we're responding to
things faster than those attackers. And as y'all have
probably seen in the news, there's more and more of
this data coming through. And so it's really important for us to
get ahead of that. With my role, again, I'm platform, so I'm helping to ensure that all of
our foundations are really secure and scalable and working and operating
at the scale that we need. And then on the developer
AI side of the house, we've kind of realized we
need to go faster. And so
we have to invest in this AI SDLC initiative. And so
it's adopting, measuring, making sure that we're staying ahead
of these attackers with our product delivery. Amazing. Olin? Awesome. Hey everybody.
Good to be back at ObsCON. So I'm Olin. I work at BlackRock and
specifically I support our pass or SaaS business Aladdin, and I support two core
platforms for that business. One is our service
platform, so think the CMDB, the instant change management features
and other service management features. And then the second, maybe more relevant
here, is the observability platform. And really, I think from a
scale and scope perspective, I think of our first
job as another platform engineer is stability first. The platform needs to be available
and working for our clients, but I think it's two
important sets of clients. The first is the 5,500 engineers, data scientists, data engineers, folks that are working on
financial models, et cetera. Aladdin is where they build and develop, and then all of the
business users that use the platform and operate on
the platform every day, that's the second level. And so thinking
about scale both for engineering and then scale for business
users and most importantly, stability in my space. Amazing. Joe? I'm Joe McManus. I'm the CISO at Grafana.
I think you might have heard of it. And so I'm in charge of the platform team, the foundations group and security
that makes all the products we've been talking about. And particularly, we've moved into making these
AI observability products. If you look at some of the demo, I think once before this where we were
showing the conversations being recorded, making sure that we've shifted left
in our development practices and we're building things that you'll
trust us with your data, that we can make sure that
we're reliant, we're resilient, and we can not only meet the
demands of a Black Friday, but we can also ensure that
if there is an incident, because there always will be an incident, that the blast radius is contained
and your data is secure and there's no interruption to your services. Amazing. Well, as y'all can tell, we have
an amazing panel assembled here today. There's some really high level expertise
here at some of the largest companies that are working with data and AI.
So the stakes are incredibly high. And I want us to start with, we are
talking about cost today, the dollar cost, and I'm going to start there with Barry.
And I want to understand from you, Barry, so in your role, how do you evaluate the AI ROI of
your investments and the tooling that you've been working
on with this year? Yeah, sure. I mean, the obvious one that people talk
about is workforce productivity, and that's something that
we definitely look at. And we are continuing to scale up
our company and grow our company, and we're trying to do that in a nonlinear
fashion relative to labor and the people that it takes to scale.
So productivity is a real thing, but beyond that, we look at a lot of
other metrics. We are a software company, so those platforms I mentioned are our
software platforms that we sell to our customers. And one of our biggest investment
areas is around the Agentic development life cycle. And what we're doing there is to
increase our product velocity. So we want to be able to
release products more quickly, make sure that they're high quality, make sure they're secure
and all the other things. And we're seeing some really good
results there. But outside of that, we're also looking at ROI for
revenue generating projects. So we are actively
investing in projects to use agents to help our sales processes
and can talk about examples, but that revenue generation
is one of our ROI areas. We're also very keen to
improve our net promoter score, and so ultimately our customer experience. So where we can implement AI to help
us deliver better services to our customers, let them self-service as much as possible
and have them hopefully walk away with a better experience. And
then another area very apropos for this conference
is around reliability. So we are investing in AI projects
for reliability, incident reduction, MTTR, MTT star improvements, and we're seeing really
good results there. So it's definitely not all
just about labor savings, which obviously gets the most of the news. Absolutely. And I think that becomes
a place to start. I'm curious, any of our other panelists, does any of that resonate with you or
something that maybe you've seen stand out in your own company as well? Well, I mean, every ObsCON
needs MTTR in every session. I. Agree. Check that box for sure. We just hit our quota. I think the other thing though that
we've been seeing is that in the observability space, the speed at which we can actually improve
the maturity and the instrumentation of the application stack itself
is also really important. I think that the tools can help
teams that used to struggle to get the time to invest to improve
the quality of their stack. Now we're seeing the AI
helping to accelerate that. When you can trade tokens
for better telemetry in the stack, it can be a multiplier in
that way. So definitely core MTTR, but then also how to improve
the maturity as well. Yeah. So starting with the dollar amount and
then moving into how it actually gets operationalized, you talked a lot, Barry, about using it to measure cost savings
and that becomes a way of proving ROI and then it moves further downstream into
the organization, into the ops world. And Olin, I love that you spoke up because I want
to lead with you on this next one about when you think about the operational costs
of AI that maybe doesn't make it into a lot of business conversations, maybe
the conversations that Barry's in, right? So how do you think about it as an ops
leader and about making sure that those things get elevated and we have those
real conversations about operational costs? Sure. I think, and I'm sure everybody
else is going to have thought on this one. My general feeling is that AI has a big second order effect impact. So AI, I think we've talked about
several times today already, some of the folks I met yesterday, everybody is seeing a multiplier in
terms of PR and code change in their spaces. I think that's
pretty much universally felt. So that's like a first order effect, but there's several second
order effects that... Sorry, can you guys hear again? There we go. There's several second order
effects that also matter. I think one of them is as you
accelerate the amount of code change, you build more products,
you build more capabilities, telemetry becomes more prevalent,
products become more prevalent, and the ability for operations to support
that explosion and growth is something that we're tracking against. When we get those outcomes
that we want for the business, we have to support the outcomes in
the ops world. I think the second other effect that matters is
agents themselves and AI itself is able to search and query telemetry
much faster and much broader. When you are capped by the
number of people on call
who can look at a dashboard, you search less. So I think both of those factors mean
that the second order effects of AI in operations especially are things we're
still adjusting and figuring out. I think there are some huge hidden
costs with AI. And so we've really, as you see, we're big AI
users here at Grafana, but we've empowered people
to code for themselves. Everybody's a citizen developer, but it's as if we've given everybody a
hammer and told them that they're now carpenters. So they don't understand
the fundamentals of computer science. They haven't read the Phoenix project. And so there's this downstream effect
where now we're standing up, okay, do we go with Vercel? How can
people deploy this securely? Do they know how to monitor it? Do they have anybody standing
up to support it when it breaks? How do you support the whole SDLC? So there's a hidden cost that
we have to engage with security. When do we scan it? What tools can apply? Now we had to ramp up our DLP because
it's not that AI is less secure, it's that it's exposed some of the
failings. If you think the fundamentals of the CIA triad, confidentiality,
integrity and availability, it's exposed some fundamentals there
that maybe you didn't fix correctly when you had human actors, but
now that we have non-human actors, it's really kind of highlighted
some shortcomings that
have had a multiplicative effect of cost for us. Absolutely. I think the multiplicative effect
of those costs becomes a lot more real when you move into the operational
world and then there's a lot of opportunities to leverage it to not only
make your own feedback loops better, but those of your agents and
the whole system you work in. And it also invites to
reimagine and revisit the processes from before and be able
to find new savings or new ways of doing stuff that are just
completely re-imagined. And those become the new opportunities, I think for teams as they move
through that space. And from there, I really want to move on to talk about, we've kind of covered a little bit about
the dollar costs and then the ops cost. Someone has to work with it, someone has
to implement with it. But in reality, there's also a cognitive cost
that builds up over time and it isn't something that is immediately
visible and it takes a different shape for the types of teams and ways that
they're using it. I'll give you a really firm example. AI acceleration and adoption this
year has not been equally graceful to everybody in the engineering
world, and we know this. If you're a front end developer, you're probably having a lot more
luck a lot sooner working with LLMs to generate React than an embedded systems
developer word in their own language. And those barriers kind of create an
unequal kind of velocity between teams that show up as pain points and frictions. And so I want to focus a bit on that
element of adoption and culture within organizations. And I want to give this one to Elaine
about how you think about as an ops leader, creating the right environment for your
engineers to be successful with each other and their agents
without clobbering each other. Yeah, it makes sense. It's
kind of an interesting thing. I read Molly Graham's article
recently about the Lego piece, and one of the things that's fun with
that one is basically as you're building, you build something, you tear it down, you shift it and you give
it to someone else. With AI, you don't have that ability. So one of the things that a lot of my
engineers are struggling with is they're constantly building all these things, but they don't really have
anyone to hand it fully over. You give part of it to AI, but you still have the accountability
that you have to maintain and control and govern and make sure it's in a
good spot. And so with our groups, the things that we've really focused
on was first managers. As humans, we have managers and we want to make sure
that they understand the workload that we're having and all the burdens that
we're having. And so we created a lot of programming around management training, making sure they understand how to
go end to end through our AI SDLC, making sure that they've actually
pushed PRs and had that experience and understand some of the pain points. At
the same time, we have AI champions. Those are those people that are really
hungry for AI and love it and want to evangelize it and want to make it a
passion project for their team and share as much knowledge as possible. And so we've made a ton of investments
around that, lots of training, lots of time where we
can just sit and listen. I think that's probably one of the
biggest things is learning from each other and figuring that out. And then obviously we have our vaults
and a lot of our tools in order to make sure that we're establishing processes
and patterns and things so that people don't have to relearn
everything on their own. I'm so glad you brought that up too, because that's what I think of as it
becomes a hidden cost, absolutely, where you get these different agentic
centers or agentically enabled groups of folks and they all invent an agentic way
of working with maybe your whole stack and they did it three times over and
that's a three times over investment that you didn't need to make. And so if you had created the environment
for them to surface and collaborate together, then you'd have
one more cohesive system. And those become the challenges
I think as we move into more operationalizing with AI and
our AI SDLC from end to end is revisiting that stuff and making sure
we have those kinds of conversations. And since it's unequal and different
people move at different speeds, I think it's great that we
have conversations as well, like the one we're having today.
And in the movement of all of that, I think it's something that
can maybe be a stickler in the AI adoption journey at any organization
could be security and the security team, right? It's like there's no bigger nightmare
for the super agentically 1000 X engineer to get the DM from the CISO or someone
in the security organization about what are you doing? Because those costs are just as real and
they manifest in much uglier and even more invisible ways that are further
removed from the agentic loops that are causing the problem. So I want to move into talking about
guardrails and security and maybe hand this over to Joe here to think
from your perspective, as a CISO, what are the trade-offs in an agentic
world that keep you up at night and how do you make do with them? Well, I feel seen. We initially, when AI started
blowing up, I mean it just changed. It got real so fast. We focused
on what are the developers doing? How are the developers going to
change with this? And honestly, the developers have not been a problem.
The developers have been fantastic. At Grafana, we partnered
early and we partnered often. So almost every new AI product that was
shown this morning, we partner early, we shifted left, we made reusable code that we
checked multiple times for security. We made sure that the sandboxes
were secure. That's great. We have a fantastic relationship. In
fact, we were just asked like, "Hey, can we get somebody to be fully embedded
with the AI team?" I don't have to head count, but I would love to. But what keeps me up is actually
the newly empowered citizen developers, because once again, AI has not made me less secure. It's
exposed failings in our platform where you would go into a tool and say, "Can you get me this information?"
And we'll try every way it can to get you that information. And so what we've had to do is make sure
that we have the right identities tied to the right people, that
they're short-lived, they
can access the right data. Some of the things we've had to
do is increase our use of DLP, data loss prevention software, so we
can ensure that if you follow along, we had an incident back in May. We were part of supply chain incident,
many people were hit by it. Honestly, our biggest impact from that was some
of the data that people had put into GitHub from using AI tools
or writing their own tools, which then falls into what
you talked about earlier, multiple people inventing the
same product. So at Grafana, we've really tried to say,
"Here's our catalog of products." One of the founders of Grafanda
helped make a staff apps product that can let people deploy
their software securely. The orbit app that many of you were using, that was written with a lot of AI
assistance and deployed quickly. And we had to adjust to say, "Hey, how do we do this the right way?" It
changed our whole paradigm for how we deployed software. So when you're in that environment
and you're moving so quickly as well, how do you think about creating the
right kind of guardrails for people to develop safely? Well, so what we've had to do is say we
put in static analysis tools into GitHub. We require PRs.
We are using truffle hog. We are using everything we can to
look for, are there secrets in here? Are we checking for SQL
injection, cross-site scripting? So we've had these tools and we've had
the plan to deploy them at these times, but accelerated all that. Now
we're doing it much faster. We're building our own harnesses
for doing penetration testing and vulnerability analysis for
our home written software. So it's just been constantly deploying
because every week there's a new thing. I mean, two weeks ago, had anybody
heard of Jiv, but for one week nonstop, that's all we talked about. The world
was going to change because of that. So it's really reacting quicker and sort
of throwing out your roadmap because even though you're holding
to the fundamentals, you're reacting much quicker and no
longer you're planning a year out, you're planning weeks out. Yeah. So just following
up on that a little bit, it's definitely beyond the
developers for sure and the AI tool sprawl. And so we
are facing that for sure. We're a public company.
We're very highly regulated. We've got PCI and SOCs and HIPAA
and HITRUST and on and on and on. And so we take security very seriously
and certainly all the automation around the secure software and secure
release management, all of that. But beyond that, there's
a new tool every week. And so one of the
friction points for WEX is the general audience idea of
like, "Hey, all these great tools, let's start using them and the risk to
the company of doing that." And so one of the things, we certainly
have a governance process, but one of the key things
is vendor risk management. We see that as one of the
highest enterprise risks in
the company. And so we do a very rigorous review of those
things before we allow any production data or any production
usage. And so one of the things, then people feel like, "Okay, well, you're slowing us down." And so one of
the things we're doing in parallel with that is trying to be really clear on
the communication. It's like, "Well, this is what we're trying to protect
the company from. Here's examples. This is why we use that process." And we
also have our architecture review board that we're using to try to make sure
we're looking at things carefully. So we do want to move fast.
We've introduced a lot of tools, but it's never fast enough, but we feel like we're
trying to balance pragmatic implementation with security. Also too, there's a balance
in what you all both said. You started with a list of technical
solutions to solve all of the problems, and you started by talking about it in
a communication way because we have to attack it from both of those
sides. And ultimately too, it's about creating the enablement
because just as quickly as we can turn code into any kind of product
that we're trying to deliver, writing code now is no longer
the obstacle or the bottleneck. It's obviously moved into other places. And so being able to quickly
take that capability and turn it inward on your own company, let's
get enabled across the board, let's have that ecosystem, let's have that catalog and just take
the time upfront to invest in the roots. Those become, I think, the fundamental ways of controlling and
understanding and communicating about cost. And that's some of the things that have
stood out to me just while we've been here. And I'm curious to know maybe if
any of our panelists have more color to add just from the worlds
that they come in, are there other costs that you think
we haven't talked about today that are definitely lurking and part
of everyone's day to day? I would say it's really the way data moves around
now has changed, right? It's before you had it in MySQL
database, you had it in your G drive, but now these tools will pull
everything together and aggregate it. And the end user just wants
to see a quick summary of it, but not realizing it's stored
somewhere. So some of the costs are now, we've had to accelerate how we're
doing EDR. I wouldn't want to do this, but I could see something like WEX highly
regulated where maybe now you have to have an allow list of software
that could actually be installed. And we're not there, but I see why people do it because
it's really this sprawl of tools, the sprawl of data is something entirely
new and that's created a new challenge. Yeah. I think one other thing we didn't touch
on is the core of the team structures that we've built have all been designed
around the way that we used to build software. So it's not just
the security constructs, but the actual orgs themselves. Would we design the orgs the same
way now if we were launching at this moment? Do we have very large platform
organizations with teams running a lot of microservices or microservices
actually part of the problem because now you can more vertically integrate. Some of those things I think are costs
that we're going to see because we're going to want to adapt
to the way we build. And the planning process, right?
We've talked about that a lot, but our customers are expecting us to
deliver X feature at this point in time on this roadmap and things are changing so
quickly that you can't really commit a year out like you've mentioned. So that planning process is really
kind of tilted on its head right now, I think. Yeah. A couple of maybe
not as obvious costs to AI or the ripple effect of
the AI industry that I see. One is for your software suppliers. So I don't know those that
are looking at all kinds of contract renewals. The request for increased pricing
is, I've never seen anything like it. And now some of this I'm sure is real, but there's also the tendency of the
software vendors now to say, "Well, yeah, your prices are going to have to go up
because we're spending all this money on AI." And it's like, "Well, if you're
not getting an ROI on that investment, then that's your problem. That's not my problem." So we are
seeing that and there's spending a lot more time on negotiation
and contract renewals. And then the second one is for
those that need to buy thousands of laptops for their companies, the price of laptops have increased
50 to 70% in the last 12 months as a result of the RAM shortage
and just chip shortage in general, which was not something I certainly was
thinking about a year ago. So there's other ripple effects
way beyond token costs. Yeah. Cost is very complex, y'all, as
we've very much learned here today. And I think what we've learned
about costs too is that there are the obvious costs, like the
dollar costs, there's the hidden costs, there's the cost that you
have to really root out, but there's also to the
responsibility to reimagine the way we work and to rebuild the systems in
a way that let us have that trust again and to let us have
the most synergistic system. And so something that's really happened
the last year is we've had to throw away a lot of our assumptions
about how we work. It's like we talk about cost
and how cost changes. I mean, think about just how building
has changed in general. Everyone's obsessed with
consumption pricing right now. The fundamentals are completely
changing. And so because of that, there's so much opportunity to learn and
build something new. And I'm curious, just any closing thoughts about what
would be your advice, the builders, leaders in the room about folks about
how they can take advantage of the opportunities in the industry
right now and get ahead? I mean, mine's basic.
Everything's changing. So take all of your previous assumptions, throw them out and be willing to
learn and be curious and ask all those questions. I think that's the only way we're going
to survive is thinking six months down the line and continuing to kind of push
ourselves to see where this industry is going. Being stagnant is not
an option anymore, basically. Yeah. And shorter iterations
too on top of that, right? If you can't look that far out anyway
because of that unknown and change, you might as well iterate very quickly. I'd push the partnership again. It's multiple teams working on things
before it'd be one team solving it. So making sure you can get in early
and sort of get that economies by all solving the same problems
and not rebuilding things. And also sometimes asking yourself,
should I buy it? I don't have to build it. Yeah. Yeah. I guess the other thing I'd add is
taking a lead from Joe's comment around system development. I'd say it's really easy
to create a prototype or a demo or an individual productivity tool, but scaling that to an enterprise
that needs to run seven by 24 at millions of operations
securely with customers impacted directly if something
breaks. So a lot is changing, but there's still some
things that aren't changing. And so the processes around this stuff, so whether it's IT service
management or our general controls or legal compliance, all the other things, if you want to be able to implement
something and run it at scale reliably, you still got to do the
basics and that's way harder than that demo. So that's the easy part. We've had some incredible
experts up here today. Can you please put your
hands together for them? This has been a super
fun conversation to host. We're going to be walking off stage.
If you have any follow-up questions, come find us, come chat with us. We had
an amazing time up here. At least I did. I can't speak for
everybody, but I had a ball. And so thanks y'all for hosting us here
today or for coming here today and we'll see you soon.

