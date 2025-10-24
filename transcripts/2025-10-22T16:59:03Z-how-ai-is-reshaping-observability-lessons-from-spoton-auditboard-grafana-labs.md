# How AI is Reshaping Observability: Lessons from SpotOn &amp; AuditBoard | Grafana Labs

Published on 2025-10-22T16:59:03Z

## Description

Discover how AI is reshaping observability from the leaders driving innovation. In this ObservabilityCON 2025 panel, Dave ...

URL: https://www.youtube.com/watch?v=H_ThS3zdxl0

## Summary

In this YouTube video, Dave Russell, Director of Voice of Customer at Grafana Labs, engages in a discussion with Neil Laughlin, leading infrastructure engineering at AuditBoard, and Jeremy White, VP of Engineering at SpotOn, about the intersection of AI and observability. They explore the challenges and successes of integrating AI tools in their organizations, emphasizing the importance of proper data organization, quick wins in implementation, and the need for collaboration to foster adoption. Both Neil and Jeremy share insights on leveraging AI for documentation and triaging processes, while also cautioning against over-reliance on AI tools without maintaining fundamental troubleshooting skills. They highlight the rapid pace of AI development and the necessity for teams to adapt and experiment with new tools, ultimately advocating for a balanced approach between building custom solutions and utilizing existing technology to enhance operational efficiency.

## Chapters

Sure! Here are the key moments from the livestream along with their timestamps:

00:00:00 Introductions by Dave Russell  
00:02:30 Neil Laughlin's background and role at AuditBoard  
00:04:00 Jeremy White's background and role at SpotOn  
00:06:30 Overview of observability platforms at SpotOn  
00:09:15 Overview of observability platforms at AuditBoard  
00:12:00 Discussion on AI's impact on observability challenges  
00:15:30 Talking about the importance of user adoption of AI tools  
00:19:00 Navigating conversations about AI adoption with senior executives  
00:23:30 The significance of data organization for effective AI use  
00:27:00 Recommendations for experimenting with AI in observability  

Feel free to let me know if you need further assistance!

# Transcript Cleanup

So this is one of my favorite things to do, which is chat with our customers in front of lots of other customers and potential customers. My name's **Dave Russell**, and I am a Director of Voice of Customer at **Grafana Labs**. Amongst many other things, this means that if you've ever filed a feature request, it's come through one of my teams. We help the product and engineering teams understand the feedback and all that kind of good stuff.

With that, we are going to go through a couple of questions that we've already got prepared. As you can see, there's a QR code up here. If you would like to ask Neil and Jeremy any questions as we start to go through this—preferably around AI and observability—please hit the QR code and put those questions into Slido. 

But without further ado, Neil and Jeremy, tell us a little bit about yourselves. We'll start here. So, a little bit about you, your role at the organization, and what your organization does.

**Neil Laughlin:** My name is Neil Laughlin. I grew up in the technical operations discipline at a little company based in the Pacific Northwest called Microsoft. It was interesting to see them figure out how to run internet services. Very quickly, it became clear to me—with my science background—that monitoring was amazing. It gave you insight into what your customers are actually experiencing. 

With a first product that was shipping set-top boxes out to sit on top of people's televisions, understanding whether those set-top boxes were actually able to reach our services, ensuring they always were, ensuring they were updated, and recovering them when they went offline was just an amazing challenge to work through in the late nineties from a technical perspective. 

Since then, I have moved through a number of companies, some large, some more mid-sized. Currently, I lead the infrastructure engineering, resilience, release, and quality engineering function at **AuditBoard**. I'm not allowed to call it platform engineering; that's somebody else's job. But AuditBoard helps companies put their audits and governance risk and compliance capabilities onto boards so that they can be used for audit and other processes.

**Dave Russell:** Awesome, thank you, Neil. Jeremy, how about you?

**Jeremy White:** My name's Jeremy White. I'm a VP of Engineering at **SpotOn**. I kind of started as a developer and then really got into the operations area pretty soon. I started to get into networking, databases, DevOps, and security. My problem was I found everything fascinating, so I started to get into everything. I think that's one of the strengths you have when you get into platform engineering—having that bigger picture and seeing how software works at scale and how it interacts in all these different pieces.

I started observability very early on, building some of my own just to understand how things operated as they hit scale because that was the area that I enjoyed most. Specifically at SpotOn, I oversee our core services and our infrastructure teams. Our infrastructure teams are basically our platform engineering, focusing more on the code side behind the scenes to help our other engineering teams, as well as on the infrastructure side. 

We have a pretty complex environment in terms of having dozens of SaaS products with many different tech stacks and areas where those products work. We also have hundreds of thousands of Android devices out in the field that we have to monitor and networking devices. Trying to pull all those together and tell a more holistic story about how the whole platform is working is something that's been pretty fascinating and something that I think observability makes fun.

**Dave Russell:** Nice, nice. Okay, so maybe continuing with you, Jeremy, to give the audience some context: What does your observability platform look like?

**Jeremy White:** It was a little more segmented a little over a year ago. We purchased **Grafana Labs** around last June and got that implemented by the end of the year. That was a pretty big effort for us. I'm a big believer that if you're going to do something, just do it. We've had way too many projects that last two or three years, and when they drag out like that, it just saps everybody. 

We had really good success rolling that out. Now we've consolidated into one, but our bigger challenge was trying to collect information from so many different devices. OpenTelemetry helped with a lot of the cloud stuff in particular. We did have to do some of our own work on the Android side to get some of the metrics and hardware data because, again, our hardware, when it runs in kitchens, is not a hospitable environment. 

So we see a lot of problems for many different reasons, and we collect a lot of that hardware metric data to understand where our failure rates are, what hardware we should be using, what ones don’t work well, and when to waterproof things. We also found that many of our networking devices didn’t have the native capability to pull those metrics out, so we had to write some custom solutions there to get that into Grafana. Our big focus has really been about trying to pull all the data from these different actual applications and sources rather than relying on different observability technologies. 

**Dave Russell:** Nice, nice. Okay, so Neil, how about you? What does your observability platform look like at AuditBoard?

**Neil Laughlin:** AuditBoard moved to **Grafana Cloud** last year. Previously, we were using a very resource-intensive provider for our core observability capabilities. Right now, we're generally taking advantage of it for metrics, traces, and profiles. What I've really seen the power of over the last few months, particularly through this conference, is how bringing everything together and tying it to what we're calling artificial intelligence unlocks so much additional power. 

We are currently in the process of bringing over logs and generally tying together the insights we get from these different signals to produce better insights than when we were using separate, albeit best-in-area tools historically.

**Dave Russell:** Okay, nice. So maybe, Neil, we'll continue with you. When you look at the challenges you're trying to solve in the observability space, how does that change under the lens of AI?

**Neil Laughlin:** One of the challenges we have is adoption outside the centralized observability experts, largely within my organization. The previous product was a pretty good product, and some people figured out how to use it within the development organizations to solve problems. Jeremy and I were talking about this, and there was panic around switching and having to learn a new tool. 

What I've seen with the AI Assistant, even just this week, is that it's very straightforward to use it to bridge the gap of remembering the syntax and how to interact with the Grafana-specific tooling. It solves many problems, shows you what it does, and then gives you the ability to look at its solution and say, “Okay, I see what is happening here. Next time, I can get to this more quickly, or I can work with an AI agent to ensure that the implementation is done quickly.” 

**Dave Russell:** Yeah, adoption—any kind of change is always scary for people. Change management, while it sounds dull, is so critical to things like migrations. Jeremy, what about you? How do the challenges you're facing shift or change under the lens of AI?

**Jeremy White:** It's funny because Neil and I have been talking about this. The same applies: it's adoption, even outside of engineering. One of the challenges is that observability is currently seen as an engineering tool for identifying problems, which makes it hard to sell if that's all it's doing. We’re trying to find ways for other teams to leverage that because there is a lot of good information there. 

I like to think that we’re data-rich but story-poor. We have so much telemetry and data to tell really good stories, but it’s overwhelming when you try to look through the data. We want to get subject matter experts to sift through that data for what's relevant for them, whether that be in product, support, or any other area. We’re trying to get to a point where observability tells a larger story of how our product is working, rather than just looking for problems and sending alerts to be on call.

**Dave Russell:** Okay, that makes sense. So maybe continuing on the adoption vein a little bit, Jeremy, what are the things preventing you from adopting some of the AI solutions out there or even things you might be looking to build yourself faster?

**Jeremy White:** AI is tricky because it’s moving so fast; it’s hard to tell what to do. Six months ago, it was different than a year ago. I also feel like the hype has added a little too much resistance. You have some people going all in and willing to get into AI, while others think the hype is too big and that it won’t work. 

So there’s a lot of focus on wanting to use AI, and it's a great tool. I think treating it as a tool instead of calling it AI is one of the biggest things we’re really trying to push. It’s like back in the day when people would get upset about Googling how to code. Now, everyone does that regularly. Change is hard for most of us as humans, and the transition with something that’s moving so fast and is sold as so impactful is just hard for people to cope with. Finding practical use cases is where we see more success.

**Dave Russell:** Yeah, makes sense. Neil, what would help speed things up for AI adoption for you?

**Neil Laughlin:** There's an impedance mismatch we're seeing right now where the new tools are emerging so quickly. The engineers working on AI adoption for the other parts of the development organization look at what exists today and think, “This is good. We'll probably want to switch to something new in three months when something disruptive appears.” 

Then, when we take it through the procurement process, legal asks, “So these are the only tools you’re going to be using for fiscal year 2026, right?” and we say, “No, we can’t promise that.” So the process of educating finance and legal partners on how this ecosystem works has been critical to our success. We haven't solved all the problems, but creating that dialogue has been valuable for speeding things up and creating a plan to explore something that may not exist today but might be useful in a few months.

**Dave Russell:** Yeah, I can see that being beneficial to have some sort of top-down mandate saying, “Hey, we want to explore this world as much as we can because we know that if we don’t, we run the risk of falling behind.” With that comes challenges in figuring out how to financially plan for it. 

Right now, we do have a mandate from above to adopt AI tools. There is a belief, often from non-technical sources, that we just need to do this and the magic will occur from there. I’m curious how many organizations represented here face a similar “go use AI” challenge but with the expectation of being more productive by drawing on these tools? 

*[Show of hands]*

**Dave Russell:** We're in it too. The challenge is that if you look at how AI was used before, it was more about conversations. Now, you’re seeing more spec-driven development. The biggest challenge is that the patterns haven’t truly evolved yet. It’s moving so fast that it makes it hard. I think we’re still in that experimentation phase to figure out how best to use AI in different areas. 

There are areas where AI does phenomenally well, and others where its non-deterministic nature makes it less effective. I believe AI will change the way we work moving forward, but how is unclear. The more we get familiar with where it works well and where it doesn’t—as a tool like any other—the better we’ll be set up for success.

**Neil Laughlin:** This is a nice segue because there is so much hype, and it’s unavoidable. Senior execs hear the hype all the time and wonder, “Why isn’t this already here? Why haven’t we done all the things in AI?” How do you navigate those conversations and temper some of the enthusiasm with a dose of reality?

**Jeremy White:** It comes down to testing it. They’re not wrong that this is a powerful tool that can accelerate what we do. Where they go wrong is going too far too fast regarding potential versus reality. What I found helpful is to say, "Directionally, we should learn more to adopt it and figure out how to leverage this tool set in our normal day-to-day." 

As you start to work out examples of where it worked and where it didn’t, you can assess whether it didn’t work because of the tooling or our process for using it. A lot of this is an age of experimentation. Once people figure out what that workflow looks like with AI as a part of it, instead of thinking, “AI will replace workflows,” we can leverage it inside workflows to become more efficient. 

Once we find where it works and where it doesn’t, we can show that it does work here and not there, as we gave it a real try. The demand for doing this comes from resistance to the hype being too big, which is right, but it doesn’t mean we shouldn’t look at it because it has progressed impressively over the last few years.

**Neil Laughlin:** As I mentioned, we are receiving top-down direction to explore AI and hit quantitative goals around being more productive. Anyone who has worked in an engineering function for any amount of time knows that measuring engineering productivity strategically is really difficult and often an outcome of events outside the engineering team’s control. 

Also, I’ve never worked on a job that has been good and interesting where I’ve had as many people to solve problems as I wish, and that’s very much the case at AuditBoard today. If we can leverage AI in the observability space to get to some of that work we've always wanted to do, such as correlation or the investigation capabilities, I’m really excited about how it can make it easier to do projects we’ve always wanted to do. 

I encourage my team to try the tools and let us know if they’re working and solving problems. We don’t want to use every possible tool in an industry where more show up literally every day, but let’s find a few that solve problems important to us. When the “Are you more productive because you’re using AI?” conversation is directed at us, we can say, “Yes, here’s what we did, here’s the problems the AI tooling we focused on solved for us, and we’re happy about it.” 

Being happy about things is very important.

**Dave Russell:** Yes, it’s a nice segue again. We’ve been talking a lot about the executive perspective and top-down views, but of course, there’s a lot of fear, uncertainty, and doubt surrounding how to encourage adoption when there’s so much scare-mongering about AI taking our jobs. 

**Neil Laughlin:** I wish I had a perfect answer for that. Within my organization, understanding that the incentives for my group and the success of our customers tie to doing the work we always wanted to do—that AI tools will let us do the work we’ve always wanted to do faster—has great appeal. 

We can get past the fear of whether we’ll hit productivity numbers by saying, “No, go try it. I’m going to support the members of the organization in trying it out. I’m going to be right there learning the tools with them. Some will be good, some won’t meet expectations, but we will chart a path together.” We will be able to demonstrate how we met our goals using AI—not just use AI as the goal.

**Jeremy White:** A lot of it is socializing where it’s worked and where it hasn’t. People’s eyes really opened up when they saw someone else go through the whole process because it’s scary. You’re getting into a new field that most of us are unfamiliar with, and there are very few experts. 

It’s daunting to be told, “Alright, you’re expected to deliver 10x because we gave you this tool on day one,” and I think that’s unrealistic. Somewhere along the way, I think we forgot that we have to relearn technology. I’ve been in this business for a while, and this is the third or fourth generation where everything just upended, and you had to adapt. 

This one is moving so fast that it’s a little scarier. The more you start to see collaboration and people helping one another out, the better it becomes because we’re learning new patterns. You can’t even go and see what the best practices are for using AI right now. 

Even if you did, they’d probably be different tomorrow. We’ve started different sessions where one person runs a “prompt club,” and the whole group tries to solve a problem collectively. It’s really about getting familiar with the tooling again to figure out where it works and where it doesn’t.

**Neil Laughlin:** I really like that. Unlike cloud or Kubernetes, where we had to choose to invest in that area, AI is coming to us and we’re being told from the top to be prepared for it. 

**Dave Russell:** That’s a great point. It is an awkward situation. I can’t remember the last time we encountered something like this in our industry because usually, it takes a while for things to ramp up and gain popularity, allowing time to establish patterns. This is moving so fast that it feels different.

**Jeremy White:** Alright, so we’ve got a few other questions, but we have some good questions coming in from the audience. Maybe we’ll continue with you, Jeremy. How do you see AI, particularly agentic LLMs, being economically viable in the long term? How will this be sustainable regarding large amounts of context and tokens being necessary?

**Jeremy White:** That’s going to be the next big challenge. Most engineers are going to have to manage context. In the beginning, we used to handle requirements gathering, testing, design, and infrastructure. We worked our way into specialists in different areas, whether it was front end, mobile, backend, or databases. 

I think this will help sustain us because we can take a step back and look at the bigger picture, relying on specialists. An LLM can recall things far better than I can. While I may deduce patterns and see the bigger picture, the recall and creative capabilities are hard to compete with. 

I do see it being sustainable, but it’s a tool like any other. People go wrong when they look at AI as a person. I don’t think it will replace people for some time—maybe someday—but right now, it’s more like any other tool. If you look across programming languages, we’ve consistently created higher levels of abstraction in programming languages. The next one may be context. 

Context and specifications are going to be the new programming language because we’re translating what we’re handed into solutions. At the end of the day, as engineers, we’re here to solve problems. Sometimes we get excited about the code we write, but ultimately it’s the solutions that matter.

**Dave Russell:** Neil, do you ever consider the environmental impact when planning for or implementing AI at scale?

**Neil Laughlin:** Yes, and it’s an interesting situation to gather information about the impact of using these new capabilities and data centers. Having had a seat at Microsoft a decade ago, I know that’s one area where large companies still running bare metal data centers are investing. 

As a consumer of those services, the flow of information is harder to find and understand regarding the impact of the services being used. I think the model we’re in right now is a trial model for pricing these capabilities. We don’t know the end-to-end cost of using these products built on token consumption down to the AI data center today. 

My team is planning for a complete shift in how these capabilities are priced in 12 to 18 months while evaluating what we want to buy into and become dependent upon. Again, it’s a hard sell to finance and legal teams to expect that everything we’re doing now will need to be thrown out in 15 months. But this experimental phase will teach us the actual economics of these token-based products in a relatively short time.

**Dave Russell:** It feels like we’ll be in that experimental phase for a while now. It’s not as if we’ll figure this out in the next 10 or 15 months and have everything sorted. There will probably be continuous evaluation for a while until it settles in some way. 

**Neil Laughlin:** Once it settles, I think you’ll see a shift toward efficiency—whether that’s cost, pricing, or just overall effectiveness. When you’re in an experimentation phase, right or wrong, you’re less interested in efficiency and more focused on how to get to a solution faster.

**Dave Russell:** Exactly. When migrating, the first step is to make it work. Make sure you can leap from what you were doing to what you want to be doing going forward. Then, invest in making sure the model is sustainable over time.

**Neil Laughlin:** I think something else worth mentioning is that it can be difficult to find really good information on this. There are some solid research papers out there if you dig deep into these ecosystems to find meaningful research material. But, it’s changing quickly, and there’s a lot of digging needed to extract something useful.

**Dave Russell:** I go back to my first experience with Usenet, where there was a warning when you posted that your message would be distributed to thousands of computers and that this would cost money. 

**Neil Laughlin:** Are you really sure you want to talk about your latest book review? Those barriers obviously didn’t last, but it’s a good reminder that there is a cost to the infrastructure we’re leveraging.

**Dave Russell:** Definitely. Alright, so next question: what’s been the biggest barrier to entry for internal users adopting AI into their triaging process? Maybe triaging or code review—what’s that side of things like? Jeremy?

**Jeremy White:** There hasn’t been a lot yet. It’s more about figuring out when and where to use it. I actually think triage is one of the most valuable places and one of the easiest to sell for AI right now. Especially when you start getting a lot of logs and metrics—when you can point them to RAGs with all our support documentation, that’s arguably one of the easier positions to take from an AI perspective. 

The trick is how to make it easy for everyone to do. Right now, if you don’t have that productization, it’s hard to implement. This is one reason I was excited about the Assistant because it makes that much easier. 

We end up with a lot of engineers pulled from proactive work to do reactive work. The more you can trim that down—the number of times I’ve seen a ticket wait for days because no one looked at it, only to discover it took an hour to find and fix the problem. Those are the instances where I think LLMs and AI can help direct you faster.

I don’t see a lot of resistance there other than we don’t have good processes baked in yet for, “Hey, here’s what you do.” This is why we’re excited about Assistant—if you’ve already got an alert, you can already get that information. It lowers the barrier to entry, making it easier for people to use.

**Dave Russell:** Neil, anything you’d add?

**Neil Laughlin:** I think the biggest barrier right now in how we typically triage is twofold: one, we don’t have all the data in the same place, so the human has to do the integration across different signals; and two, we need to go to the engineers who are very busy and say, “Okay, if you take five minutes to practice pushing the little sparkle button when you’re in Grafana and then tell it what you want it to do for you, you’re going to like the results here. Let me show you.” 

If we can just get that bit of time with the users of the observability product to show them how it can help them, they will realize there’s a lot in it for them to adopt it. This isn’t even specific to AI; it’s generally true for any place that pulls developers out of their often very product feature-focused commitments to teach them something new.

**Dave Russell:** No, makes sense. Alright, what are some of the case studies or success stories you’ve had when using AI? Are there any particular things where you’ve been satisfied? Neil, let’s start with you.

**Neil Laughlin:** Developer experience is one of my organization’s responsibilities, and the company I’m at right now is one where the leaders are not engineers. Explaining the importance of developer efficiency was an early challenge for me in this job. We survey our engineers and gather information on their priorities. Documentation consistently comes up as a struggle for new engineers. 

Smart search, which essentially uses a model to index our various collaboration tools and provide AI-curated responses back to developers trying to solve problems, has been phenomenal. Building a knowledge graph of all our distributed documentation has been a great solution. I’m now finding customer success people, salespeople, product people—everyone else in the organization—is coming in to use what I’m going to call an AI tool to solve their problems. It’s been incredibly powerful to see that come together.

**Dave Russell:** That’s amazing! How about you, Jeremy? What successes have you seen?

**Jeremy White:** I definitely share the same sentiment regarding documentation. We’ve always struggled with finding the right documentation, and when someone doesn’t find it, they create additional ones. That’s never not been a problem for our industry. AI has helped identify and coalesce that information, and now AI agents even show their work by indicating where they got the information. 

Another success is how quickly we can move from idea to prototype. That’s been pretty amazing for our design and product teams, and even for engineering to help contribute more. Being able to vet ideas quickly and see what works and what doesn’t—there’s still a lot of work in that last mile, and people often underestimate that part—but how quickly we can ideate and see if it’s going to work has helped us toss around different ideas faster before we commit.

**Dave Russell:** Makes sense. Alright, let’s see if we can squeeze in two more questions. What do you think we need to be cautious or aware of as AI becomes more integrated into observability? Maybe Neil, we’ll start with you.

**Neil Laughlin:** Specifically within observability? That’s interesting. I do think back to what Jeremy touched on: you still have to look at the code it generates. I worry about the limits of the tools, but if we forget the essentials of troubleshooting as a skill set and rely totally on the agent, we’ll lose the creativity that humans who understand complex systems—often not documented in a way AI can discover—bring to triage today.

**Jeremy White:** I think the overdependence is a worry across the board for AI. I do worry that if you don’t have some expertise in an area, you might be overly trusting. AI can be dangerous, but it’s not any different from humans. Not every human will give you the right answer. 

I think we often forget that. With alerting and things like that, my first thought is false positives. I think back to how many thresholds were set too low or too high by humans. It doesn’t really change: we still can’t be overly trusting. This isn’t always going to give you the right answer, just as a human won’t either. So if you treat it as such, I think you’ll be well prepared for any concerns that come up.

**Dave Russell:** I couldn’t agree more. The big thing for me whenever I look at something like this is “trust but verify.” Just make sure that it hasn’t hallucinated something weird or done something crazy. As you would test code someone gave you, you’ve still got to run it through your CI/CD pipeline or whatever else it might be. 

**Neil Laughlin:** Exactly. 

**Dave Russell:** Alright, so we’ve got a little over five minutes left, and there’s one big question I’d like to hear from both of you: if you had one recommendation for the audience here based on your experiences for people embarking on the journey of AI in observability, what would that recommendation be? Let’s start with you, Neil.

**Neil Laughlin:** Start in an area where you can relatively quickly determine if you’re having a positive impact as you experiment. What you don’t want is to be tied up in a six-month tools evaluation for two or three different tools, only to reach the end and have finance or legal say, “We can’t afford this one.” 

Every time we’ve tried to do a big, complex migration, it has taken significantly longer than expected. Nothing will be different with AI tool adoption. However, places where you can quickly get value—like the AI Assistant or my own use of it to quickly solve problems with broken dashboards—are fantastic. 

It took me 15 minutes to evaluate and solve a problem. Documentation smart search was also easy to bring in, and we started to see value quickly. In contrast, if we try to rewrite the entire code base using Cursor or another tool in an agentic fashion, I don’t think we’ll evaluate its feasibility in a reasonable time.

**Jeremy White:** I would say organize your data. Context in data is going to become way more important as you can run analysis over it with AI. If your data is disorganized, your results are likely not going to be well organized. Good taxonomy is essential. We’ve tried to ensure our data in observability is segmented properly—where everything's together, what runtime it’s running in, or what team it’s associated with. 

Narrowing context helps get better results and scans fewer tokens during processing. Those are things you can train the AI on better, helping it understand how the data is structured and organized, making it far more efficient than wasting time trying to deduce through the data.

**Dave Russell:** I think we saw both yesterday in the keynote and in some other sessions that the more context you can provide—the more structured context—the better the AI performs. More context leads to higher likelihood of achieving your goals. 

I couldn’t agree more. From my perspective, there’s an Australian woodworker I follow on YouTube named **Dainer Made** who says, "Just get started." Pick something you think you can turn around quickly or realize you’re having success or making progress. Build muscle memory, awareness, and familiarity with the tooling. Gain experience, share it across teams, and build upon that to make it less scary for everyone.

Alright, we’ve got time for one more question. What’s the balance between building versus buying AI tooling? When should you DIY versus see if something off the shelf will work? Jeremy?

**Jeremy White:** Anyone looking to jump into that arena? It’s a lot. It seems like there are many people trying to compete in that space, and it’s really saturated. The good news is that the progress being made is impressive. It’s hard to believe that one more could add much value. 

I think it’s best to wait it out and buy because, at this rate, I don’t know how anyone could start and try to keep up by building as everything moves so quickly now.

**Neil Laughlin:** Core versus context is always so important for a company. Do the things that are core to your business and really differentiating for its success. If there are other people solving problems that are context for your business in a way that meets your needs, leverage what they’re doing. 

It will be their focus. Just consider how many engineers work at Grafana on observability versus how many engineers work at your company on observability. Draw on the expertise of those solving larger problems, then figure out how to adapt it for your own needs. 

**Dave Russell:** Awesome. Alright, that’s all the time we have, but please give a massive round of applause to Neil and Jeremy here!

## Raw YouTube Transcript

So this is one of my
favorite things to do, which is chat with our customers in
front of lots of other customers and potential customers. So
my name's Dave Russell. I'm a Director of a Voice
of Customer at Grafana Labs. So amongst many other things that means
if you've ever filed a feature request, it's come through one of
my teams and we help the product and engineering teams understand
the feedback and all that kind of good stuff. So with that, we are going to kind of go through a
couple of questions that we've already got prepared, but as you can see,
there's a QR code up here. So if you don't like to ask Neil and
Jeremy any questions as we start to go through this, preferably
around AI and observability, then please hit the QR code and
put those questions into Slido. But without further ado, Neil and Jeremy tell us a little
bit about you. So we'll start here. So a little bit about you, your role at the organization
and what your organization does. My name is Neil Laughlin. I grew up in the technical
operations discipline at a little company based in the Pacific
Northwest called Microsoft. It was interesting to see them figure
out how to run internet services. Very quickly, it became clear to me with
my science background that monitoring was amazing. It gave you insight into what
your customers are actually experiencing and with a first
product that was shipping set top boxes out to sit on top
of people's televisions, understanding whether those set top
boxes were actually able to reach our services, ensure that they always were, ensure they were updated and they
recover them when they went offline. It's just an amazing challenge to work
through in the late nineties from a technical perspective. Since then I have
moved through a number of companies, some large, some more mid-sized. Currently I lead the infrastructure
engineering, resilience, release, quality engineering
function at AuditBoard. I'm not allowed to call it platform
engineering, that's somebody else's job. But AuditBoard helps
companies put their audits and governance risk and compliance
capabilities onto boards so that they can be used for
audit and other processes. Awesome, thank you Neil.
Jeremy, how about you? So my name's Jeremy White. I'm
a VP of Engineering at SpotOn. I kind of started as a developer and
then really got into the operations area pretty soon, started to get into
networking, started to get into databases, started to do DevOps, security. My problem was I found everything
fascinating and so I started to get into everything. I think that's one of the strengths
I think when you get into platform engineering is kind of having that bigger
picture and seeing how software works at scale and how it interacts
in all these different pieces. And so I started observability very early
on building some of my own early on, just trying to understand how things
operated as things hit scale because that was the area that I enjoyed
most. So specifically at SpotOn, I oversee our core services
and our infrastructure teams. Our infrastructure teams. These are basically our
platform engineering. So
more on the code side behind the scenes of what we do to try to help
our other engineering teams as well as on the infrastructure side. We've got a pretty complex environment
in terms of we've got a SaaS, dozens of SaaS products, many
different tech stacks, many different, even just areas of where
those products work. But then we also have hundreds
of thousands of Android
devices out in the field that we have to monitor
and networking devices. So trying to pull all those together
and tell a more holistic story about how the whole platform is working is something
that's been pretty fascinating and something that I think observability
makes kind of fun to be able to see. Nice, nice. Okay, so maybe
continuing with you then to give maybe the audience some context. What does your observability
platform look like? So it was a little bit more
segmented a little over a year ago. So we purchased Grafana Labs about last June and then got that
implemented by the end of the year. So that was a pretty big effort for us. I'm a big believer that if you're
going to do something, just do it. We've had way too many projects that
last two and three years long that just when they drag out like
that, it just saps everybody. So we had really good
success rolling that out. So now we've consolidated into one, but our bigger challenge was trying
to collect information from so many different devices. OpenTelemetry
helped with a lot of the cloud stuff in particular, we did have to do some of our own on
the Android side in order to get some of the metrics and the
hardware data because again, our hardware, when it
runs in the kitchens, it's not a hospitable
environment for that hardware. So we see a lot of problems
for a lot of different reasons, and so we collect a lot of that hardware
metrics to understand where our failure rates are, what hardware we should be
using, what ones don't work so well, when to waterproof things,
a lot of things there. We also found that a lot of our networking
devices didn't have the native being able to pull those metrics out. So we
had to write some custom stuff there, pull that out, get it into Grafana. So our big thing has
really been about trying to pull all the data from all these different
actual applications and sources as opposed to different
observability technologies. We've been able to consolidate
on the observability technology, which has been pretty good for us. Nice, nice. Okay. So Neil, how about you? What does your observability platform
look like at AuditBoard board? AuditBoard moved to
Grafana Cloud last year. Previously we were using a very
hungry dog as our provider for the core observability capabilities, and right now we're generally taking
advantage of it for metrics, traces, profiles. What I've really seen the
power of over the last few months, and particularly
through this conference, is how bringing everything together
and tying it to artificial and what we're calling artificial intelligence
unlocks so much additional power. So we're in the process of bringing
over logs right now and just generally tying together the insights we
get from these different signals to be able to produce better insights than
we could when we were using separate, albeit best in area tools historically. Yeah, okay. Okay, nice. So maybe
Neil, we'll continue with you. When you are looking at the challenges
that you're trying to solve in the observability space, how does that change under the
lens or with the lens of AI? One of the challenges
that we have is adoption outside the centralized
observability experts. Largely within my organization. The previous product was a pretty
good product and had some people that had figured out how to use it within the
development organizations to solve the problems. So there was - Jeremy
and I were talking about this, there was panic around switching
and having to learn a new tool. What I've seen with the AI Assistant
even just this week is that it's very straightforward to use it
to bridge the gap of remembering the syntax, remembering how to interact
with the Grafana specific tooling. It solves so many problems,
shows you what it does, and then gives you the ability to
look at its solution and say, okay, I see what is happening here next time
I can get to this more quickly or I can work with a AI agent to make
sure that the implementation is done quickly and I'm not spending
all my time doing research on how to put the query together. Yeah, yeah, adoption, I mean any kind of change is always
scary for people and change management, while it's such a dull sounding topic, is so critical to things like migrations
and stuff like that as well. Yeah, makes sense. So yeah.
Jeremy, what about you? The challenges that you're
facing under the lens of ai, how does that shift or change things? It is funny because Neil and I have been
talking about this because the same, it's adoption and it's adoption for
me, even outside of engineering. I think one of the challenges is that
observability right now is seen kind of as an engineering tool and
just identifying problems and that makes it a hard tool to
sell if that's all it's doing. So really trying to find ways for other
teams to start leveraging that because a lot of good information there. I
like to think that we're data rich, story poor, where I think we have so much telemetry
and so much data to tell really good stories, but it's just overwhelming when you're
just trying to look through the data. So trying to get subject
matter experts to more easily sift through that data
for what's relevant for them, whether that be in product,
whether that be in support, whether that be in any other area. I think that's where we're trying to get
to where observability tells a larger story of how our product is working as
opposed to just looking for when there's problems and sending alerts to be on call. Okay, that makes sense. So maybe continuing on that
adoption vein a little bit and with you Jeremy, what are the things that are preventing
you from adopting some of the AI solutions that are out there or even
things that you might be looking to build yourself faster? So AI is a tricky one because,
well for one, it's moving so fast, it's hard to tell what to do. I mean, six months ago it was
different than a year ago. It was different than even more than that.
I also feel like kind of the hype has made added a little too much resistance. You see some people that go all in and
are willing to get into the AI and use that and then others that the
hype's too big, it won't work. So really I think I know there's
a lot of focus of wanting to use AI and it's a great tool. I think just using it as a tool and
just treating it as a tool instead of calling it AI is one of the biggest
things that we're really trying to push. It's kind of like back in the day I
remember people getting upset when people would Google how to do
code and things like that, and it became this big thing like, oh,
you can't just copy pasta it your code, and now people are doing that
regularly. You're almost, it's so I think change is hard
for most of us as humans and I think that transition with something
that's moving so fast and that's been sold as being so impactful is just
hard for a lot of people to cope with. So honestly, I think it's finding
where it's practically usable Is where I think the sweet spot is. I think all the over hype of what it
could do, it does it a disservice. I think if we can focus more on here's
the practical use cases and where it can help, that's where we've seen
a little bit more success with. Yeah, makes sense. Neil, how about you? What would help speed things
up for AI adoption for you? There's an impedance mismatch
we're seeing right now where the new tools are emerging so quickly that the engineers working in my team on
AI adoption and AI enablement for the other parts of the development
organizations are looking at what exists today and saying, I think this is good. We'll probably want to switch to
something new in three months time when something new and disruptive appears. And then when we try to take it through
the procurement process and are having the conversations with financial
planning and legal, they're saying, okay, so these are the only tools you're
going to be using for FY 26, right? And we're saying, no,
no, we can't promise that. So the process of educating
the finance and the legal partners on how this
ecosystem we're in right now works has been critical to our success. And I wouldn't say we've solved
all of the problems here, but creating that dialogue between
our partners on the business side and the engineers that are working
on adoption has been valuable for speeding it up and creating
essentially a plan to be able to explore something
that may not exist today, but we might want to bring in
three, four or five months from now. Yeah, yeah, I can see that. I can see being beneficial to
have some sort of top-down sort of mandate saying like, Hey, we want to explore as much of this world
as we can because we know that if we don't, the chances are we run
the risk of falling behind. But with that comes the challenges of
figuring out how do you financially plan for any of that? And what I'll say is that right now
we do have a mandate from above to adopt AI tools. There is the belief often
from non-technical sources
that we just got to go do this and the magic
will occur from there. I'm actually curious how many
organizations represented
here face that same sort of go use AI challenge but be more
productive by drawing on these tools? Yeah, I mean show of hands,
who's in that state right now. And we're in it too. And I think the challenge is even if
you look at how AI is used before it was more you're just having
conversations, constant conversations. Now you're seeing more
spec driven development. The biggest challenge is I don't think
the patterns have truly evolved yet and it's moving so fast that that's
what makes it hard. So we're still, I think in that experimentation phase
to figure out exactly how best to use AI in different areas. There are
areas that does phenomenal at, there's other areas that
it's non-deterministic
nature makes it a little less great.
So I think the important part is really understanding this. I do believe that AI is going to change
the way much of us do our work moving forward, but how is unclear? So I think the more we get familiar with
where it works well, where it doesn't, it's a tool like any other tool and I
think the better we get at equipping that tool, the better we'll be set up
for success as we move forward. Yeah. I think this is kind of a nice
segue onto because there is so much hype and it is unavoidable and
obviously senior execs are hearing the hype all the time and
are wondering why isn't this already here? Why haven't we done
all of the things in AI? How do you help navigate those kind
of conversations and maybe temper some of the enthusiasm and excitement
that folks have with maybe a dose of reality? Jeremy will continue with you. It comes down to everything. You
kind of have to test it. I mean, they're not wrong in that this
is a very powerful tool that can accelerate what we do. I think where they did go wrong
was going too far too fast about what the potential is
versus what the reality is. And so what I found helpful is
yeah, directionally it's right, we should be learning more to adopt it
and figuring out how to leverage this tool set in our normal day to day. But I think as you start to work
out examples of where it worked, where it didn't work, did it not work because of the tooling
or did it not work because of our process for using the tooling? A lot of it is, this is again an age of experimentation
and I think the moment people start to figure out what that workflow looks like
with AI as a part of it instead of the, I'm not a big fan of the AI is
going to replace the workflows, that part gets I think a little too
far down the road maybe someday, but right now leveraging it inside of
the workflows and figuring out how you become more efficient and that
10x multiplier kind of thing, I think that's once we hit that spot
and find out where it works and where it doesn't and just showing it does
work here, it doesn't work here, but we gave it a real try because I
think the reason you're starting to see a lot of the demand for doing it is because
there is a lot of resistance to the hype being too big, which is right, but it shouldn't mean don't even look
at it because it really has progressed impressively these last few years. It genuinely impressive
how far AI has come along. Just because the hype is so big doesn't
mean we shouldn't look at it at all though. Yeah, yeah. Makes sense.
Neil, how about you? How are you helping to give a
healthy dose of reality to some folks in the story? Well, as I alluded to, we are receiving top-down
direction to explore and hit quantitative goals
around being more productive. But anybody who has worked
in an engineering function
for any amount of time knows that at a strategic level, measuring engineering productivity
is really difficult and is often an outcome of events outside an
engineering teams control. Also, I've never worked on a job that
has been good and interesting where I have had as many
people to solve problems as I wish, and that's very much
the case in AuditBoard today. I'm sure it's very much the case for
people here working on instrumenting the systems that they manage, build own using observability
tools. So for me, if we can leverage AI in
the observability space, get to some of that work that we've always
wanted to do with correlation or the investigation capabilities that were
demoed this week or fantastic to see, I'm really excited about the fact
that this will make it easier to do some of the projects we've always
wanted to do and I've encouraged my team go try the tools, let us
know, let me know if they're working, if they're solving the problems or not. We don't want to try to use
every possible tool in an industry where more are
showing up literally every day, but let's find a few that solve
problems that are important to us. And then when the "are you more
productive because you are using AI", conversation is directed us say, yes, here's what we did, Here's the problems
that the AI tooling we are choosing to focus our time in solved for
us and we're happy about it. Being happy about things
is very important, I think. Yes. Actually it's a nice segue again onto, we've been talking a lot about the exact
perspective and top down and things like that, but of course there is a lot of FUD and
there is a lot of scare mongering and that side of things around how do you encourage adoption when there's
so much scare mongering around AI is going to take our jobs
and that side of things? Yeah, I wish I had a perfect answer to that. Within my own organization, understanding that the incentives for my group and for the success of
the customers ties to doing the work we always wanted to do, that the AI tools will let us do
the work we always wanted to do faster will let us engage on some of the
code migrations where we're eliminating technical debt will let us retire some
old code that we would like to delete out of the code base that has a lot
of appeal and where we can get past the, but will we really hit the
percent productivity number too, no, go try it. I'm going to support the members of
the organization in trying it out. I'm going to be right there with them
learning the tools alongside them. Some will be good, some of them
will fail to meet our expectations, but we will chart a path together. We will be able to demonstrate
how we met our goals using AI, not just use AI as the goal. Yeah. Yeah. Jeremy, how about you?
How are you helping to counter some of this that's coming in the news? A lot of it is, I think socializing
where it's worked and where it hasn't, it was interesting seeing
how many people at first their eyes really opened up when they
saw someone else actually go through and actually do it end to end
because kind of scary, right? You're getting into a whole new field
that most of us are just unfamiliar, there's no experts,
there's very few at least. And so it is kind of daunting
to go in and be told, alright, now you're expected to deliver 10x
because we gave you this tool on day one and I think that's unrealistic.
And so I think right now, somewhere along the way, I think many of us kind of forgot
that we have to relearn technology. I've been in this business
for a little while. Yea. So this is the third or fourth generation
where just everything just upended and you had to. So I think a lot of people are
new to that where everything you used to and got comfortable with
is going away. It's not away yet, but you see that. And what's weird about this one is usually
you get a couple of years where this is, it's a slow moving thing. This is
moving so fast that it's a little scarier. So I think the more you start to see
collaboration where people are working together and then helping one
another out, because again, we're learning new patterns, you can't even go and see what the best
practices are for using AI right now. And even if you did tomorrow they'd
be different. So I found that we've started different sessions where
we've got one person that's running prompt club and they'll go
through and they literally just, they'll come up with a thing and the
whole group will just collectively try and go through prompts and try
to solve the problem with it. And it's really trying to get familiar
with the tooling again to figure out where it works and where it doesn't. So
I think the more you start to see it, the more you start to see the examples, you get a better feel for how
and where to apply this tool. I really like that. Unlike, I don't know, cloud or Kubernetes where we had to
go choose to invest in that area. Yea. AI is coming to us and
saying, and we're being. Told they're coming to us the top now
and then they don't even have the, here's how you do it, it's just the it's
coming. Be prepared. That's a great, so it is, it's an awkward situation. I can't remember in our industry when
we last ran into that because usually it takes a while for these things to really
ramp up and get enough popularity where you've got some time to kind of get some
patterns established and figure out, okay, we could do this or we could
do that. It doesn't exist right now. I think it's consumer web. That was the time everything
was so disrupted as it is now. Yeah, no, that absolutely makes sense and it
is very much whether you think about cloud or Kubernetes or virtualization, you can go back any number of revolutions, evolutions that we've been
through in the tech industry, this is one that feels very different
for the speed and for the rate of innovation has definitely
ramped up here, I think. Makes sense. Alright, so we've
got a few other questions, but we've got some good questions
coming in from the audience, so maybe Jeremy we'll continue with you. How do you see AI in
particular agentic LLMs being economically viable the longer term? How will this be sustainable when it
comes to large amounts of context and tokens being necessary? I think that's going to
be the next big challenge. I think most engineers are going
to become really how do you manage context? And if you think about it, we used to do this when I started. I did the requirements gathering, I
did the testing, I did the design, I did the infrastructure. I think in the beginning it was a
lot of generalists and then you, we worked our well, worked our way into specialists into
different areas, whether it was front end, mobile backend databases. I think this will help sustain because
now we can take a step back and be looking at the bigger picture and
relying on specialists that honestly, I guarantee you that an LLM will
recall things far better than I can. I may be able to deduce patterns and
I may be able to see bigger picture, but when it comes to just recall and some
of the creative things that it's able to do, it's hard to compete with. So I
do see it being sustainable, but again, it's a tool like any other, where I think people go wrong is when
they look at AI as a person, again, I don't like the, it will replace a person because I
don't believe that at least not for some time, maybe someday, but at this point it's more
as this tool like any other, if you look across programming languages, we've consistently created higher level
of abstractions of programming languages that we've programmed in and I think
the next one is going to be context. I think context is going to be, and specifications are going to be the
new programming language farther on down the road because really that's what we
are being handed and we're translating that and putting that into solutions.
At the end of the day, us as engineers, we're here to solve problems. Sometimes we get excited about the
code we write and things like that, but at the end of the day, it's the
solutions that ultimately matter. And so I think this tool is just going
to be one that's going to become a major part of how we deliver those solutions. So maybe Neil asking you
a different question. Do you ever consider the environmental
impact when planning for or implementing AI at scale? Yes, and it's an interesting
situation to be in right now to gather information around
the impact of using these new capabilities, the new data centers. Having had a seat at
Microsoft a decade or so ago, I know that that's one of the areas where the large companies are still running
bare metal data centers are investing in, but as now a consumer of those services, the flow of information,
it's harder to find, harder to understand the impact of the
services that are being used. Also, this is jumping a bit back to the
question that you asked Jeremy, but I also think that the
model that we're in right now, it's the trial model for
pricing these capabilities. We don't know what the
end to end cost of using these products built on token
consumption down to the AI data center is today. My team is planning for
12 to 18 months or so out a complete shift in how
these capabilities are priced in evaluating what we want to buy
into and become dependent upon now. Again, it's a hard sell to the finance and
legal teams expect that everything we're doing now you'll have to
throw out and forget in 15 months time. But I do think this is the
experimental phase and we're going to learn what the actual
economics are of these token based products
In a relatively short amount of time. It also feels like we are going to be
in that experimental phase for a little while now Because It's going
to carry on changing as well. So it's not even as if
like, oh, excuse me, but we'll figure this out in the next 10
or 15 months or whatever and then we'll have everything sorted. There's probably going to be quite a bit
of continuous evaluation of this for a little while until if even
it kind of settles in some way. And I think once it's
settles to a certain point, you'll start to see a shift
more towards efficiency, whether that's the cost and
pricing, whether that's just the, I think right now when you're
in an experimentation phase, right or wrong, you're less
interested in efficiency, you more interested in how do I get to
the solution faster And I think that's the phase we're in now. Which is any migration first make it work, make sure that you can make the leap
from what you were doing to what you want to be doing going forward. Exactly. And then invest in making sure that the
model is sustainable over time in all the terms. Yeah, I think something else I
think you mentioned as well
is it's quite difficult to get really good information on this. There are some really good research
papers out there if you go really digging and you really dive deep into
those kind of ecosystems to find the research material
that is out there. But A, it's changing so quickly and
B, it's research material. There's a lot of digging in you
need to do to extract something a little bit more meaningful to what
it is that you are trying to do. I go back to my first experience with
Usenet where there was a warning when you post to Usenet your story or message, I don't even remember what
they're called anymore, your post will be distributed to
thousands of computers and this will cost money. Are you really sure you want to
talk about your latest book review? Well those barriers obviously didn't last, but it is a good reminder that there is
a cost to this infrastructure that we're leveraging. Definitely, definitely. Alright, so next question is, and we'll
go to you for this one Jeremy, what's been the biggest barrier to entry
for internal users adopting AI into their triaging process? So maybe triaging or code
review that side of things. So there hasn't been a lot yet. It's more about figuring
out when and where to use. I actually think in triage is one of
the most valuable places and one of the easiest to sell for AI right now Because
especially when you start getting a lot of logs and metrics, a lot of data, when you can point them
to RAGs where you've got, here's all our support
documentation and things like that, I think that's arguably one of the
easier positions to take from an AI perspective. The trick is how to make it easy for
everyone to do because right now, again, if you don't have that productized, and this is one of the reasons I was
excited about Assistant because it really does make that a lot easier.
We end up with a lot. It is always hard pulling engineers
out of the proactive work they're doing to do the reactive work. And so the more you can
really kind of trim that down, the number of times I've seen a ticket
wait for days because no one looked at it and then it only took an hour not
only to discover what was wrong but also fix it Or it takes 10 hours to figure
out what's wrong and it's the one line of code that all it did to fix it. Those are the kind of things I
think that LLMs and AI in general will be able to help direct
you faster and better. I don't see a lot of resistance there
other than we don't have good processes baked in yet for hey, here's what you do. Which again is why we were kind of
excited about assistant because now you're already in this tool. If
you've already got an alert, you can already get this information. I think that kind of lowers
that barrier of entry, making it easier for people to use. Yeah, yeah. Makes sense. Neil,
anything you'd add there? I honestly think the biggest barrier
right now in how we typically triage two barriers, actually one, we don't
have all the data in the same place, so the human has to do the integration
across the different signals and two, we need to go to the engineers
who are very busy and say, okay, if you take the five minutes to practice
pushing the little s sparkle button when you're in Grafana and then tell
it what you want it to do for you. You're going to like the results here,
let me show you. You try it, you got it. Okay, good. YeaAI. Then if we just can get
that bit of time with the users of the observability
product to show them how it can help them, they will realize that there's a
lot in it for them to adopt it. And this isn't even specific to AI, this is generally any place where
you pull the developers out of their often very product feature focused
commitments to teach them a new thing. Yeah, no, makes sense.
Makes sense. Alright, so what are some of the, and
again we'll sit with you Neil, what are some of the case studies or
examples of success stories you've had when using AI as opposed to
just some of the generic things? Are there any particular things
where you've been happy with. Developer experience is one of the
responsibilities of my organization and the company I'm at right
now is one of the first ones where the leaders were not engineers. So explaining the importance
of developer efficiency, developer experience was an early
challenge for me in this job. We survey our engineers and gather information on what they
see as a priorities for that. Documentation consistently came up as
one of the places that they struggle with as new engineers come in. Smart search, which is essentially just
using a model to index all of the different collaboration
tools we have amazing number and provide AI curated responses back to developers
who are trying to solve a problem has been phenomenal. And I think that building the knowledge
graph of all of our distributed documentation has been such a
good solution that I'm now finding customer success people,
sales people, product people, all the other parts of the
organization are coming in to use what I am going to call an AI
tool to solve their problems. It's been incredibly powerful
to see that come together. That's amazing about you. What's
some of the successes you've seen? I definitely share the same
one there on documentation. I've found that we've always struggled
with where the right documentation is and someone doesn't find that they create
additional ones and things like that. I don't think that's ever not
been a problem for our industry. And so I think AI has
really helped identify, coalesce that and even sometimes, and I love now how a lot of the AI agents
will even show their work like, hey, I got the document from over here, so
here's their standard operating procedure. So that's been a pretty big win. The other one that I really
like is getting from idea to prototype has never been faster before. That's been pretty amazing for our
design and product teams and even for engineering to be able to help
contribute a little bit more. That I think being able to vet that
out and see what works and what, I mean there's still a lot
of work in that last mile. I think people often kind
of underestimate that part, but how quickly you can really ideate
and then see if that's going to work has helped us really toss around a lot of
different ideas and see what works and what doesn't a little faster before
we go all in and commit on it. Makes sense. Alright, see if we can squeeze in two
more questions. The next one is, what do you think we need to be
cautious or aware of as AI becomes more integrated into observability?
Maybe Neil, we'll start with you. Specifically within
observability. Okay, interesting. I do think back to what Jeremy touched on, you still have to look at the code that
it's generating and I shared the same fears, the Replit story around, "I deleted your code base and I lied
to you about it", but I worry about. Within observability. I don't know, I haven't really discovered
the limits of the tools yet, but I think if we forget the essentials of troubleshooting as a skillset, totally relying on the agent, we'll lose that element of creativity
that humans who understand complex systems that are not necessarily documented
in a way AI can discover bring to triage today. Yeah, anything on your side?
Yeah, I think the overdependence there, I think that's a worry just
across the board for ai. I do worry that if you don't
have some expertise in an area and that you might be overtly
trusting, AI can be a little dangerous, but it's also, it's not
any different than humans. We have human error as well. Not every
human that says something is right. I think we often forget that. So even
with alerting and things like that, my first thing that comes
to mind is false positives. But then I think back to how many
thresholds were set too low or too high by humans as well that I think
it doesn't really change. I think it comes down to we still
can't be overly trusting. This isn't, isn't always going to
give you the right answer. Just like a human is not always
going to give you the right answer. So if you treat it as such, then I think you'll be well prepared for
any of the concerns that come up Yeah, yeah. No, I couldn't agree more. Big thing for me whenever I'm looking
at something like this is trust but verify. Just make sure that it hasn't
hallucinated something weird or done something crazy and just as you
would test code that someone gave you and had completed that's still got
to run through your CI/CD pipeline or whatever else it might be, make
sure that it is running as expected. Yeah, makes sense. Alright, so we've got a little over about
five minutes left and there's one big question I'd like
to hear from you both on, which is if you had one recommendation for the audience here, the folks here, based on your experiences
for people embarking on the journey of AI in observability, what would be that recommendation?
Maybe Neil, we'll start with you. Start in an area where you can relatively quickly determine if
you are having a positive impact as you experiment. What you don't want to do is end up
tied in a tied up in a six month tools evaluation for two or three different
tools where you get to the end and legal or finance says, we can't afford this one or you
can't buy this one because reasons. Every place we've tried
to do a very big complex migration over the course of my career, it has taken significantly
longer than expected. Nothing will be different with AI tool
adoption. But places where you can go in, get value quickly - I go back
to both the AI Assistant and my own use of it to quickly solve
problems with broken dashboards and surface information. That was fantastic and it took me 15
minutes or less to evaluate and solve a problem there. And then the
documentation smart search as well, that was pretty easy to bring in and
we started to see that value quickly in contrast, proving that we can
rewrite the entire code base using Cursor or one of the
other tools in an agentic fashion. I just don't think we're going to be able
to evaluate the feasibility of that in a reasonable amount of time. Yeah, I did see something highly amusing as
someone had actually gone through and asked a code tool to rewrite the entire
code base and they said, oh, this code, it's so beautiful. It's amazingly
commented, none of it works, but it looks so nice. It looks so
pretty. Yeah, that's a real challenge. How about you Jeremy? What's the one
bit of advice for the folks here? I would say organize your data. I think context is in data
now is going to become way, way more important when you can run
analysis over it the way you can with AI, but at the end of the day
it does well with patterns. So if your data is disorganized, your results are likely not
going to be as well organized. So I think good taxonomy in terms of, one of the things we've tried to do with
our data, at least in observability, is make sure that we've segmented
products properly where everything's all together or what runtime it's running
in or what team it's associated with so that you can narrow the context,
which helps get you better results, scanning less tokens when
you're processing it. But then also those are things you can
train the AI a little bit better on. Here's how the data already
is structured and organized, so it's far more efficient than wasting
the first portion of its time trying to figure out and deduce through the data. Yeah, yeah, I mean I think we saw both yesterday
and the keynote and in some of the other sessions, the more context you can give. More structured context. Yes, but the AI is like a human in a
lot of cases in that if you don't give a human any context,
it's like go do task X. Will it do what you wanted? Maybe,
maybe not flip a coin, I don't know. But the more context that you give it, the more likelihood it's going to achieve
the kind of goals that you are looking for. I couldn't agree more. We're still very much in this
world of garbage in, garbage out. We haven't fundamentally changed
that From my perspective, just for what it's worth, there's an Australian woodworker who
I follow Dainer Made made on YouTube who just says, just get started. Just need to pick
something, pick something. I like the way you said something that
you think you can turn around relatively quickly or you can realize whether you
are having success or making progress really quickly. But pick something
relatively easy to start with. Build the muscle memory,
build the awareness and the sort of familiarity with the
tooling. Gain the experience, share the experience
across teams and build upon that, make it less scary
for everybody. Alright, so I think we've got one, we've got
time for maybe one more question and let's see. Okay, so maybe I'll just
try and simplify this a little bit. AI tooling build versus buy. When's the balance there
between DIYing this stuff versus seeing if just taking something
off the shelf? Maybe Jeremy. Like building AI tools. Anyone right
now that wants to jump into that arena? Seems a bit. It's a lot. Yeah. I mean you'd have to be, it seems like there's a lot of people
right now trying to fight in that space. Fight's not necessarily
the greatest term there, but compete in that space
And it is really saturated. The good news is the progress
that's being made is impressive. So it's hard to believe
that one more could add that much better. I'm here to wait it
out and buy because at this rate, I don't know how anyone else could start
and try to keep up and build as quickly as everything's moving right now. Yeah, makes sense. Makes sense.
Anything to add on your side? Core versus context is always
so important for a company. Do the things that are core
to your business and really
differentiating for its success. If there are other people that are
solving problems that are context for your business in a way that meets your
needs, leverage what they're doing. It will be their focus. Just the general
conversation around observability, how many engineers work at
Grafana on observability, how many engineers work at
your company on observability? Draw on the expertise of the
people who are solving a larger problem and then figure out how
to adapt it for your own needs. Awesome. Alright, well that's all
the time we have unfortunately, but please give a massive round of
applause to Neil and Jeremy here.

