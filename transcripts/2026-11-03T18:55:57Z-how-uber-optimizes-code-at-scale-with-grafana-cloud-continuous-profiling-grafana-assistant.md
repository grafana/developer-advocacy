# How Uber Optimizes Code at Scale with Grafana Cloud Continuous Profiling &amp; Grafana Assistant

Published on 2026-11-03T18:55:57Z

## Description

How does Uber use continuous profiling to improve performance and resource efficiency across several million CPU cores?

URL: https://www.youtube.com/watch?v=0VS80uDi_Z8

## Summary

The community call titled "How Uber Optimizes Code at Scale with Grafana Cloud Continuous Profiling & Grafana Assistant" took place on November 3, 2026, featuring Chris from Uber. The discussion focused on Uber's implementation of continuous profiling across over 6,000 services using Grafana Pyroscope, highlighting the importance of always-on profiling to improve performance and resource efficiency. Key takeaways included the significance of comprehensive profiling coverage, the need for careful optimization to avoid unintended consequences, and the role of automated agents in analyzing profiling data. Chris emphasized that while agents can assist in identifying issues, they can also misinterpret data if not properly guided.

Topics: Continuous profiling, Grafana Pyroscope, performance optimization, automated agents, profiling coverage.

## Chapters

00:00:00 Profiling services at Uber: challenges and strategies
00:06:09 Understanding Uber's microservices architecture and profiling challenges
00:11:34 Improving profiling efficiency with PyroScope Proxy
00:17:09 Optimizing CPU and Mutex profiling at Uber
00:22:45 Continuous profiling and optimization techniques at Uber

Hello everyone. My name is Chris. I'm from Uber, and today I will share our journey on how we profile over 6,000 services at Uber and how we leverage the agents on top of that. 

Yeah, I'm a big foodie, so if you want to talk about food, I'm happy to chat both within and beyond the Bay. But the easiest way to lose the entire afternoon is to ask me about the thing I will present to you because I spent two years building around it. I'm really proud of the work. 

Let's see if it works. Okay, still doesn't work. All right, it's fine. I don't have fancy animations, so that's okay. Here are my three promises for the next 20-ish minutes that I hope you can take away:

1. If you do random sampling on the profiles, you will probably not get what you want, as most people hope.
2. I will share how exactly we profile over 6,000 services at Uber with no one opted in really.
3. Particularly in this current era, it is more likely that the agent is reading your profiles, not your developers. So what does it mean to have valid data or good coverage data in this era?

Beyond that, I will also share two times we actually got it wrong, and I hope that will be even more helpful for many of the folks here.

Let me start with a quick question. Raise your hand if you've received pings in the past month or so saying your service is slow or anything, if any SREs are here. Okay, I see a few hands. By that moment, how many of you really know what exact line is wrong? Okay, you're experts, but I guess for most people, they really don't know. 

The slowness here is not abstract. Maybe you ordered dinner and it's running late. As a foodie, I would probably be a little concerned. Or if you ordered a ride and the driver is late, you'll probably also miss your schedule. So it's never just an abstract thing; you're just a spinner, and you really want to move on faster.

Your metrics will tell you something is slow, and then to move on, the next phase you can use tracing. Tracing will tell you, "Okay, this exact span, this service is slow." But quite often, what happens is you are on your own. You probably open your codebase and start guessing, "Okay, this might be wrong, or is this slow, or is that slow?" That's why we actually need profiling. Profiling is sort of like the last step; it will point you to exactly which line of the code is slow, and that's the difference between an investigation versus a pull request.

I'm trying to do a crash course here on what a profile is. In general, a profile is a survey. Within a certain frequency, we ask a simple question for each thread: "Which function are you in, and who is calling you?" By that survey, you will have a lot of columns stacked together. One simple sample won't really tell you much because it's just a random moment of the computer or the CPU. However, if we stack a lot of those profiles together—millions or billions of those moments—we'll see a clear picture. For example, in this case, we may say 62% of the CPU is spent on parts, so we probably have a line number to look at.

Two things to remember here: profiling is essentially sampling, so it's a little bit non-deterministic, which is why you really need good coverage. Secondly, profiling is relatively cheap, so you can keep it on. That's for CPU profiling. At the same time, if you want to ask about memory or mutex contention, you can do the same thing by looking at different types of profiling.

One interesting question I want to address is that the usual approach for profiling sometimes, or quite often, really doesn't work. Why is that? You might say, "Okay, I will profile when it's slow or when it's interesting." But the problem is that time has probably already passed—maybe an hour ago or so. 

At our scale, we can't really ask 6,000 service teams or owners to set it up individually—not because they are lazy, but because it's just under the roadmap right after updating the README. That's why we say it has to be always on, and it also has to be on infrastructure.

Before I talk about what we built, I also want to shout out to Grafana and mention what we didn't build. Grafana Pyroscope handles all the storage, query, and many things for us. The version two is really great. I will stop here and leave the sales pitch to them because the Grafana folks are here, and they're doing a better job at that. 

Here's the hinge of this talk: essentially, one question Grafana Pyroscope can really answer for us is that they don't know our backend—the backend of how Uber services are running—and they can't really decide which one should be profiled. That's the question we are trying to answer here, one layer up, which no one really talks about.

You may think this is trivial, but the first question is: who gets profiled? I will tell you why it's actually not a trivial question to think about. One simple answer is that we all know we can't really profile everything; it's too expensive, and we probably have overhead. 

So one obvious answer is to start with random sampling. Let's just do some random sampling—1% of your containers, let's see. You can do that in all kinds of ways. The easiest way is to hash your instance ID or some other things. Basically, if you have 1,000 containers, each one of them flips a coin. If the coin is up, it's on; otherwise, it's off. On average, if you have 1% sampling and about 1,000 instances, you will always have 10 on. 

Notice here why this approach works: the reason is that 1,000 is really a big number. When people hear about Uber scale, this is sort of the normal picture they will come to mind. We are just one enormous system, like a monolithic size of a building. If that were true, this talk could literally end here, and we would just profile the entire building. But it's not the case.

This is what the real Uber backend looks like. If you tap on either Uber Ride or Uber Eats or some other apps, behind it are a lot of small microservices, each part answering each little piece of the question. But the person holding the phone never sees it; they only feel the slow part. 

We also have over 6,000 services across four languages and all types of different workloads. We did a survey on our side, both our skills actually in two dimensions: depth and breadth. The breadth covers a long tail of the small ones, and the depth handles a lot of big services. For the bigger boxes, you can assume they are bigger services; for the small boxes, think of them as really tiny services. 

An important thing here is that because it's two dimensions, depth is a part that a lot of people focus on, but breadth is actually the part that quietly breaks things. 

We just did a snapshot of a random 100 services in production, and it takes about—you can probably find over there—about 11,000 instances. The median service count of the container is actually only 17. So it's really a small number. 

I will also challenge you to think about what's the likelihood that if you have 17 containers, and you flip the coin 17 times at 1%, what's the likelihood that you will get a profile? 

I hope my agent is not hallucinating on the map here, but most likely, it's only the majority of the time, 84%.

the time you won't have any profiles. The issue here is it's not even a degradation; nothing is wrong. It's just a random sampling, by design. 

If we go back to the 100 random services we chose at that snapshot and run the projection, actually 71 of them will not have any CPU profiles—zero. This is an important point because nothing indicates that the dashboard you're looking at is probably looking fine; there are no red signals everywhere. However, as more and more profiles are either read by people or by the agents—more likely by the agents—71 of the empty services will definitely lead your agent to the wrong conclusions, which I can show you later.

Another common objection I've heard is, "Why not just focus on the big boxes, those big services with large instances, and ignore or accept the risk that the tail is dark?" There are three reasons why this is probably not a good idea:

1. **Small services can sit on the critical path.** If you have a really small service in front of a checkout, you really can't leave it dark.
2. **Service instance count doesn't necessarily mean importance.**
3. **This decision is to be blind.** It's about three-quarters of our services. At least at our scale, we can't really ignore them. It's not an unimportant part of the company; it's a majority of the company.

I want to spend a little more time here. Instead of random sampling, we stopped flipping and assigned positions. From a different level, all the way from the largest scope down to zone clusters, we assign a seat. You can think of it like a seating chart. Essentially, we're doing a seating chart instead of a raffle. Every instance will have its own topology, and it's pre-sorted. We compute all the assignments upfront.

For example, let's say we have 12 instances. If we can only sample one, any one is good. But for simplicity, because we already sorted them, let's say we sample the zero. If we can allow for another sample, I would argue that since region A is already covered, we should cover region B next. In this case, the next instance number one is in region B, and so on. If you can afford a third one, we'll go to region C. Essentially, every container is designed or computed upfront, and with the same decision, we will never skip a service. 

I will show you later why this is important. With the same 100 services and the same 1% sampling, we just changed the rules, and now zero services will get missed under the new schema instead of 71, which is like three-quarters. The zone coverage also tripled from roughly only 7% to 24%. 

This gives you a better and more obvious visualization of what we built before and after. Before, every container was flipping a coin and ingesting all the profiles to Pyroscope on its own. The credentials were copied all over the place among all containers. More importantly, if certain parts of our profiling were figured out as dangerous, you needed to fix it repo by repo. If you were on one repo, good luck if not.

This is what we built after: we created a service named the Pyroscope Proxy. It's a small service in the middle, literally a proxy. Now, all the containers just ask a question every 10 minutes: "Should I be profiled or not?" The proxy looks up the table and answers whether you should be profiled or not. The upload goes through the proxy as well, so it's validated, and everything is routed to Grafana with central credentials. Because it's in one place, you can also turn it off. Keep that in mind; I will show you why it's important.

Another important principle here is that profiling must never become an availability risk for the thing it is watching itself. Everything needs to fail open. If the containers cannot reach the proxy, profiling should just stop. If the proxy cannot upload in time, it should just drop the profile. It never blocks the application. That's the bottom line.

Now, I want to mention why all the rules I was discussing are not theoretical. It's the first time we actually got it wrong. We turned on the Mutax lock contention profiling for our Cadence deployment. Cadence started at Uber, but it's a workflow engine, an open-source repo. Some of you in this room might be using it. 

When we deployed the Mutax profiling, every instance kept crashing with segmentation faults. The bug was not in Cadence or in our profiler; it was an outdated third-party dependency request deep in the tree. There was some kind of weird handwritten assembly code that left certain garbage on the frame pointer. Essentially, whenever we collected the profile, we just walked through that stack and fell over. 

Normally, being first is a good thing, but not in our case. However, because we had Pyroscope as a switch, we quickly turned off all the Mutax profiling in minutes. We updated only after we fixed those issues in the dependencies, and then we switched it back. So, "always on" means it only works if you can turn it off.

Here are some big numbers from last week: there were hundreds of millions of checks reaching out to the proxy, and about 50 million requests were actually uploaded to Grafana. For the majority of cases, the requests returned within 10 milliseconds. The reason is that everything is pre-computed, and the proxy is just doing a table lookup. 

Again, this is by default; it's not a pilot program and applies to every service. Now, I will talk about what we can achieve once we build this entire framework. We have coverage, and it's actually way more than just savings. We did an internal survey, and 70% of the developers said that the profiles are more useful than either logging or metrics alone to help them answer or debug issues faster. 

It's not only the people who are seeing it; more on that in Act Three. Today, I will just show you two quick examples that you can follow in seconds. These two fixes were actually generated by agents. 

The first fix we have is from a service named Flow Eval, which is one of our largest workflow evaluation platforms. There was just one line for change. This object UUID was already computed; however, for some reason in the old code, it kept re-decoding every time within this flow loop. It's very slow. It's probably the kind of code you would stamp "looks good to me" before you finish your coffee or lunch. 

However, it's a tiny change, but it has a relatively big impact in terms of savings. If we benchmark it, reading from the cached result is almost 150 times faster than decoding the field again and again. The issue is you won't have any alerts because nothing is broken. You won't see this from the tracing because it's within the same function, and nobody is actually complaining, so there's even no incident. 

But the point is, the entire service spent 1.6 of all the CPU time within that one line. If we change that one line, it saves more than 500 cores. So, "too small to alert on" doesn't mean it's "too small to matter." 

How do we find it? We didn't even start with the investigation; the profile was already running and collecting. The answer was already there. This is the entire argument we are making about why the...

**Profiling Needs to be Always On**

In one example, we discussed CPU profiling optimization. Now, I will show you another example focused on Mutex profiling optimization. We asked the Grafana Assistant to rank all services based on their Mutex profiling, and we identified one significant outlier. This particular service contributed more than half of the entire fleet's Mutex contentions. The only reason we could obtain this ranking is that we profile every service, as mentioned in Act One.

**Understanding Mutex Issues**

Let's have a crash course on what's going wrong with Mutexes. A Mutex, or lock, is like a gate; it only allows one request to enter and access shared data at a time. The problem here is that the service only had one gate. You can imagine it as having only one bathroom key for an entire building with several floors. Request B must wait for Request A to finish and return the key before it can enter the gate. This is why we observed a 55% contention rate.

If you understand this, the fix is straightforward. Instead of having one key for the entire building, we give every floor its own bathroom key. Now, requests only wait when they are trying to access the exact same data. This change requires about ten lines of code. Micro-benchmarks show great results, and we project to save over 1,000 cores. We didn't measure it because the profiling continues, and the Mutex contention is resolved.

However, I want to point out that this is actually the second time we encountered this issue. It wasn't that the optimization was incorrect; it worked, and throughput increased. The problem arose because there was a capacity threshold set for the lock case before, where the lock acted like a read limiter, slowing the entire system down. Once the lock was removed, the traffic surged unexpectedly. It’s like knocking down a wall during renovation, only to discover that it was holding up the second floor. In this case, the lock itself was the wall. 

We needed to revert the change, determine the correct capacity threshold, and then roll out the change again. These two cases are not unique; they represent significant wins that customers report back to us. There are also many smaller wins that either go unmeasured or unreported. As you can see, these issues span different domains, including error rates, throughput, latency, and involve various teams and signals, yet nobody was monitoring them. The profiles were already available.

**The Agentic Error**

Now, let's quickly move to the last part: the agentic error. We have three layers: ask, analyze, and act. First, we ask the Grafana Assistant. It's a bit embarrassing because someone from another team pinged me on Slack, saying, "Hey, we have a memory issue. Can you take a look?" I can, but the issue is that I don't read or write Java, and I don't understand anything about it. However, working on profiling doesn't require me to understand every runtime. I can simply read the question out loud to the Grafana Assistant without spending the entire afternoon studying Java's memory documentation.

I also want to give you a taste of what a real flame graph looks like at Uber scale. Five years ago, I would have recommended studying it, but nowadays, like most of you, I just nod my head, think it looks good, and keep scrolling while the agent does its job. In fact, the agent did do its job. I was multitasking, and just 30 minutes later, the agent had already figured out the root cause. I informed the developers that it seemed reasonable to me and suggested they take a look. The next day, they reached out to me, saying that normally this would take at least a couple of days to do manually, but the agent pointed it out in only 30 minutes. I didn't even mention that I couldn't understand anything about Java.

Performance work used to be an expert domain requiring knowledge of your runtime, but now you just need to ask a good question. 

**Analyzing Internal API Calls**

The second part of the layer is quieter. I dug into the data to find out who is actually calling our internal profile API. When we analyzed the data, we found that we built this for developers. However, the largest callers are now the MCP agent and some other automated pipelines. Don't get me wrong; developers are still doing their jobs, but we built this API for engineers, and now agents are the biggest callers.

Lastly, I want to briefly mention why you can sometimes blindly point the LMs to a profile in certain cases. One case involves Mutex profiling. If you're familiar with Go's Mutex profiling, the cost always lands on the Go routine that unlocks the lock. The hottest frame is always in the standard library. However, if you point this to the models, the model will start fixing the Go standard library. I believe the Go team is doing okay, and you should focus on your own functions that you can fix and optimize.

We coined a term called "neurosymbolic." Essentially, it has two parts. The symbolic part involves program analysis that reads a profile and identifies hard functions and good candidates for optimization. We then pass these functions to the neural part, which is a model or agent. They excel at optimizing code, writing synthetic benchmarks, and iterating until the process is refined. 

At a high level, we conduct program analysis to determine which functions to examine, and the agent or model decides how to write and optimize the code. This is the overall loop: we start from the continuous profiling we have collected, rank and localize the functions, and the agent continues optimizing until it reaches a good PR review for humans. No one is really triggering it, and the profiles are already there, with pipelines running.

**A Quick Trick for Performance Optimization**

I want to share a quick trick that we tried, which is worth mentioning. Here’s a rule we hold ourselves to: when discussing performance optimization, if the original function and the new function yield different results on the same input, it’s likely not an optimization; it’s just an outage with good numbers on paper. We have a special pipeline to measure all branches of a function, ensuring that the input and output are exactly the same. If they are not the same, we will not approve the PR. 

However, I want to clarify that this is only a filter, not proof. In the Mutex optimization case I showed you earlier, all the paths were exactly the same, but the problem was in the downstream.

In conclusion, I want to emphasize that agents can only fix the things they can see. Compared to developers, if developers lack data, they will stop. However, agents may confidently hallucinate and pick the wrong functions to optimize. This is why, like flipping a coin, three-quarters of our services may not have any profiles, which is not ideal. 

**Key Takeaways**

Two things to take home: 

1. AI can only fix the things it can see in this era. 
2. Before trusting your agent's ranking, check your data or profiles to ensure you have a comprehensive view.

Good coverage is important, and it's not just about the dashboard; it implies a service level as well. Additionally, be careful about your fix or optimization. A fix can work, but it can still break things. When something gets faster, make sure to check downstream to ensure your system is ready for the optimization.

Before I finish, I want to say thank you. This is not a solo project. I have probably about 25 or even more collaborators from both Uber and Grafana, and I think some of them are actually in this building. So, my thanks to every one of them; without you, this project is not possible. 

For most engineers, it's just a flint graph that is already there, and they take it for granted. However, for the infrastructure team, that's actually one of the best compliments you can get. 

So, that's what we contribute. We are also working on open sourcing the PowerSchool proxy. If you want to know when it lands, argue about sampling, or just chat about favorite restaurants in general, my email is there. It has been a privilege, and thank you.

## Raw YouTube Transcript

Hello everyone. My name is Chris. I'm from Uber and today I will
share our journey on how we profile 6,000 plus services at Uber and how
we leverage the agents on top of that. Yeah, I'm a big foodie. So yeah, if
you want to talk about food, yeah, I'm happy to chat both
within and beyond the bay. But sort of easiest way to
lose the entire afternoon is ask me about the thing I will present to
you because I spent two years building around it. I'm really proud of the
work. Yeah, let's see if it works. Okay, still doesn't work. All
right, it's fine. All right, because I don't have fancy
animations, it's fine. All right, so here are sort of my three promises.
All right, thank you. All right, here are my promises in the next 20-ish
minutes that I hope you can take away with basically three things.
First is a buck. If you do random sampling on the profiles, you will probably not get what
you want as most people hope. And the second part is I will share how
exactly we profile 6,000 plus services at Uber with no one opted in really. And third is particularly under this
current era, more and more important, more likely the agent is reading
your profiles, not your developers. So what does it mean to sort of
have a valid data or a good coverage data under this era? And beyond that, I will also share two times actually we
got it wrong and I hope that probably is even more helpful for many
of the folks here. All right, so let me start with a quick question. Raise off your hand if you've got some
pings in the past month or so saying your service is slow or anything,
if any SRE is here. Okay, I saw a few hands. By that moment, how many of you really know
what exact line is wrong? Okay, you're expert, but I guess for most
of the people, they really don't know. So essentially also the slowness here is not abstract. So maybe you order a dinner and
it's running late. As a foodie, I would probably be a little bit
concerned or if you order a ride and if the driver is late, you'll
probably also miss your schedule. So it's never sort of the abstract thing. It's you just a sort of spinner and you
are really wanted to move on faster. All right. So your metrics will tell you
something is slow and then to move on, next phase you can use tracing. So trace
will tell you, okay, this exact span, this service is slow. But quite often, normally what happens
is you are on your own. You probably open your code base
and you start to guessing, okay, this might be wrong or is this slow or
is that slow? So that's why we sort of actually need the profiling. The
profile is sort of like the last step. It will point to you exactly which line
of the code is slow and that's sort of a difference between an investigation
versus a pull request. All right. Also, I'm trying to do a
crash course here on what is a profile. So in general, a profile is a survey. So let's say within the certain
frequency under basically we ask a simple question for each thread. Which function
are you in and who is calling you? So by that survey, you will have a lot of the
columns stacked together. One simple sample won't really tell you
much because it's just a random moment of the computer or the CPU. However, if we sort of stack a lot
of those profiles together, a lot of those moments, millions or
billions of those moments together, we'll see a clear picture on the right.
So for example, in this case, we may say 62% of the CPU is
spending on parts. So we probably, even with a line number, that's
sort of where you should look at. And two things to remember here,
profiling is essentially a sampling, so it's a little bit non-deterministic. So that's why you really need a good
coverage. Second part is in general, profiling is really relatively
cheap, so you can kind of keep it on. And that's for CPU
profiling. At the same time, if you want to ask about a
memory or mutex contention, you can do the same thing, you look at
different types of profilings. All right. So one interesting question I want
to see here is the usual approach for profiling sometimes or quite often
it really doesn't work. And why is it? You can say, okay, I will profile when it's slow or when
it's interesting. But the problem is that time is probably most likely already
passed, I don't know, one hour ago or so. And the other issue is at our scale, we can't really ask 6,000 service
teams or owners really set it up individually, not because they
are lazy, because it's just under the roadmap right
after update ReadMe. That's why we are saying it has to
be always on and it also has to be on infrastructure. All right. Before
I talk about what we build, I also want to shout out to Grafana
and mention what we didn't build. So Grafana Pyroscope, they basically
handle all the storage, query, many things for us. And the
version two is really great. I will stop here and leave the sales
pitch to them because Grafana folks are here and they're doing better job at that. But here's a hinge of this talk.
Essentially, one question Grafana Pyrascope can really
answer for us is they don't know our backend, the backend of how Uber service is
running and they can't really decide which one should be profiled. And that's the question we are trying
to answer here is one layer up like no one really talks about. All right,
you may think this is trivial. The first question is who get profiled? I will tell you why it's actually not
a trivial question to think about. One simple answer is, because we all
know we can't really profile everything, it's too expensive and we
probably have overhead. So one obvious answer
is everyone start with, let's just do some random sampling.
Let's just random sample 1% of your containers, let's see. You
can do that by all kinds of ways. Easiest way is hash your instance, your ID or instance ID or some other
things. Basically you have a lot of, let's say you have 1,000 containers,
each one of them flip a coin. And if the coin is up, it's on,
otherwise it's off. And on average, if you have 1% sampling and
you have about 1,000 instance, you always have 10 on. But notice
here why this approach works. The reason is 1,000 is really
a big number. All right. And when people hear about Uber scale, this is sort of like a normal
picture they will come into mind. We are just one enormous system,
like a molodistic size of a building. If that were true, this talk can literally end here and
we just profile the entire building, but it's not the case. So this is sort of what the
real Uber backend looks like. If you have a one tap on either Uber
ride or Uber Eats or some other apps, behind it a lot of small microservice, each part answers each little piece of
the question. But the person's holding the phone, they never see it. They
only feel the slow part. And we also, we have 6,000 plus services and four
languages and across all the type of different workloads. And we
did a survey like on our side, both our skills actually
in two dimensions. One is
depth, the other is breadth. And the breadth covers a lot of a long
tail of the small ones and the depth handles definitely a lot of big
services. For the bigger box here, you can assume it's a
bigger service. Small box, you can think it's sort of like a
really tiny bit of a small service. And I think important thing here
is because it's two dimensions, depth is a part that a lot
of people are focusing on, but the breadth is actually the part
that quietly breaks things. All right. So we just did a snapshot of a random
100 service at a production and it takes about, you probably
can find over there, it's about 11,000 instances. So the
median service count of the container is actually only 17, one seven.
So it's really a small number. So I also will challenge you to think
about what's the likelihood if you have 17 containers, 1%, you
flip the coin 17 times, what's the likelihood that
you will get a profile? Yep. Okay. I hope my agent is not
hallucinating on the map here, but most likely it's only
majority of the time, 84% of the time you won't
have any profiles. And the issue here is it's not even
a degradation. Nothing is wrong. It's just a random sampling.
It's just by design. All right. So same thing if we go back to the
100 random service we chose at that snapshot, if we run the projection, actually 71 of them will
not have any CPU profiles, zero. And that's a part I think really
important because nothing told us the dashboard you're looking is probably
looking fine. There's no red signals everywhere. But today as more and more profiles
is either read by the people or by the agents more likely, 71 of the empty service will definitely
leads your agent to the wrong conclusions that I can
show you later. All right. And the other quite of common
objections I've heard is why not we just focus on the big boxes, those big service with a big
instance and we can just ignore or just accept the risk
that the tail is dark. Three reasons it's probably not a
good idea. First is small service, they can sit on the critical path. So if you have a really small
service in front of a checkout, you really can't leave it dark. And also the service instant count
doesn't necessarily mean the importance. And also the last one is
this decision is to be blind. It's about three quarters of our services.
At least at our scale, we can't really... It's important. It's
not an important part of a company. It's a majority of the part
of a company. All right. I want to spend a little bit more time
here. So instead of a random sampling, what we did, we stopped quiet flipping and what
we do is we assign the positions. So from a different level all the way to basically from the most larger scope
from the area with down to zone cluster, basically we assign a seat. You
are see like a seating chart over here. So basically we're doing a
seating chart instead of a raffle. So every instance will have sort of
its own topology and it's pre-sorted and we compute all the
sort of assignment upfront. I will give you a quick example. Let's
say we have 12 balls here or 12 instance. If we can only sample one, any
one is good. But for simplicity, because we already sort it, let's
say we will sample the zero. If you can allow to sample another one, I will argue probably because
region A is already covered, we probably should just cover
region B. Let's see. In this case, that's why the next ball number one
is in region B, so on and so forth. If you can afford a third
one, we'll go to the region C. So essentially it's sort of every
container is designed or sort of computed upfront and with
the same decision and that will never skip the service
I will show you later why. So with the same 100 service, same 1% sampling more or less, we just changed the rules and zero
service now under the new schema will get missed instead of a
71, like a three quarter. And the zone coverage also tripled
from roughly only 7% to 24%. And sort of also give you a better
or more obvious visualizations on what we built before and after. This
is what before we have the service. So every container of its own flipping
the coin and ingesting all the profiles to PyroScope on its own. So the credentials copy all over
the place among all containers. And more importantly, if certain part of our profilings
are sort of figured out as dangerous, you need to fix it repo by repo, if you
are on one repo, if not, then good luck. And this is what we build after. So essentially we build a service
named the PyroScope Proxy. It's one small service in the
middle, literally a proxy. So now all the containers just ask a
question like every 10 minutes it asks the proxy, should I be profiled or not? Then the proxy just look up the
table and answer back whether you should be profiled or not.
And upload go through the proxy as well. So it's validated and everything
is routed to Grafana with a central credentials. And because of one
place, you can also turn it off. Keep that in mind. I will show you why
it's important. And the other thing, I think one of the important
principle here is the design profiling must never become
availability risk of the thing it is watching itself. So
everything needs to fail open. If the containers cannot reach
the proxy, just to stop profiling. And if the proxy cannot upload
in time, just drop the profile. It never blocks the application.
That's the bottom line. All right, this is sort of a part. The first thing I want to mention why
all the rules I was mentioning is not theoretical and it's the first
time we actually got it wrong. So we turn on the Mutax like a lock
contention profilings for our cadence deployment.
So Cadence is start from Uber, but it's a workflow engine
open source or repo. Probably some of you in
this room are using it. So we deploy the Mutax profiling,
every instance keeps crashing, segmentation fault. So the bug is not
in Cadence. It's not in our profiler. It's an outdated third party dependency
request that deep in the tree, there's some kind of a weird handwritten
assembly code that left some certain kind of garbage on the frame pointer. So essentially whenever
we collect the profile, unfortunately we just walked
through that stack and fell over. So normally be first is a good
thing, but not for our case. However, what happened is because of we
have a pyroscope as a switch, we quickly turn off all the mutax
profilings in minutes and we update only after we update the dependencies
of fix those issues, we just switch it back. So always
on means only works if you can turn it off. All right. And there are some big numbers from, I think this is the data I put
from last week. As you can see, there's hundreds of millions of the
checks reaching out to the proxy. Also, there's a half, like a 50 million requests we actually
uploaded to Grafana for the past week. And for the majority of the case, the request returns
within 10 milliseconds. The reason is everything is pre-computed
and its proxy is just literally doing a table lookup. And again, also
this is sort of by default, it's not a pilot program and
for every service. All right. Now I will talk about once we
build this entire fancy framework, what can we have? So we have coverage and it's
actually way much more than savings. We did an internal survey, 70% of the developers that the
profiles are more useful than either logging or metrics alone to
help them answer or debug the issue faster. And it's not only
the people who are seeing it, more on that in actor three. So today I will just show you two quick
examples that you can basically follow in seconds. And also those two fix
are actually generated by agents. All right, this is the first fix we have. So essentially it's from a
service named the flow eval. If one of our largest workflow
evaluation platform on the sort of, it's a big service. So literally
there's just one line for change. This object UUID was
already computed. However, for some reason in the old code, it keeps re-decode every time
sort of within this flow loop. It's very slow. It's probably kind of a code you are
just a stamp looks good to me before you finish your coffee or
finish your lunch. However, it's tiny bit of a change, but it's actually a relatively big
change in terms of a savings. So actually if we do a benchmark, reading from the cache result
is almost like 150 times faster than decoding the field again and again. So the issue is you won't have any
alerts because nothing is broken. You won't see this from the tracing
because it's within the same function and nobody is actually complaining
so there's also even no incident. But the point is the
entire service spent 1.6 of all the CPU times within that one
line. And if we change that one line, it saves more than 500 cores. So too small to alert on doesn't
mean it's too small to matter. All right. And how do we find it? Not
even start with the investigation. The profile was already
running and collecting. So the answer already sits there. And this is the entire argument we are
saying why the profiling needs to be always on in one example. All right. Next I will show you another example. The previous one is a CPU
profiling optimization. This is more on the Mutex
profiling optimization side. So essentially we asked the Grafana
assistant to sort of rank all which service are bad in terms
of Mutex profiling. And we found definitely one outlier. I'll show you it's actually
the exact same service. That service itself contribute more
than half of the entire fleet Mutex contentions. And the only reasons we can get this rank
is because we profile every service as we mentioned in act one. All right. So a crash course on what's
going wrong between a Mutex. So what is a Mutex or lock in
general? So the lock is like a gate. It only left one request to enter and
touch the shared data on the right. And the problem here is the
service only had one gate. So you can imagine we only have one
bathroom key for the entire building with several floors. So request B of the key B
needs to wait until the key A finish and return the key so it can
enter the gate. That's why it was 55%. So if you sort of understand this, then the fix is actually very
straightforward. Instead, we just give every key its own gate. So every floor now gets its own bathroom
key instead of the entire hundred floors shares the same key. So now the request only wait when
they really touch the exact same data, and that's the actual real meaning
of the locks using for. It's about 10 lines of a code of change. So micro benchmark shows great results
and we project to save 1,000 plus cores and we didn't measure it because
the profiling keeps coming and the mutex connection is gone.
However, I want to tell you, this is actually the second
time we got it wrong. And it's wrong not
because the optimization is incorrect, it works. The fix
works and throughput went up, that's a problem because in the
downstream there was a capacity threshold. It was set for the lock case before
where the lock pretty much acts like a read limiter slow the entire system down.
Once the lock is removed, the traffic basically entire run through the
street into the ceiling and nobody was expecting that value. So it's sort
of like you are doing a renovation, you knock out a wall and the wall is
actually you then figure out it's holding the second floor.
But here the lock itself is the wall. So actually what we do is we
need to revert the change, figure out the right capacity threshold,
then roll out the change again. And those two cases are not special. Those are also only like a big
document wins that the customers get back to us. There's also
a lot of small wins. It's either not measured or not
get back to us. But as you can see, it's across different domains
like from error, throughput, latency and from different teams and
different signals and nobody was looking. The profile's already there. All right. Now quickly go to the last part. Basically when nobody's reading the
profile now is the agentic error. So we have three layers,
the ask, analyze and act. First is ask from Grafana assistant. It's also a little bit embarrassing one
because someone from other team just pinged me on Slack like, "Hey, we have a memory issue.
Can you take a look?" Yeah, I can. Only issue is I don't read
Java. I don't write Java. I don't understand anything about Java, but I work on profiling doesn't mean
I need to understand every runtime. So what I can do is I just read
basically the question out loud to Grafana assistant and without
spending the entire afternoon study what is Java's memory
doc. All right. Also, I want to give you a taste of what is
a real flame graph looks like at Uber scale. If it's five years ago, I would
recommend go study it. But nowadays, I'm like most of you, I just nod
my head, okay, it looks good. Then just keep scrolling and
the agent do it job. Yeah. So actually the agent
did do the job. I mean, also I was multitasking do something
else and I was just only 30 minutes after the agent already figured out the root
cause. So I just tell the developers with, seems like this is looking
reasonable to me, take a look. And on the next day he
reached back to me like, okay, normally this probably at least take
a couple days to do it manually, but nowadays you point it
out within only 30 minutes. And I don't even mention I can't
understand anything about Java. So performance work used to be an
expert domain if you are in your runtime, but now you just
need a good question. And this is a second part of the
layer two, which is a quiet one. So essentially I just dig this data to
figure out who is actually calling our internal profile API. So
when we call the data, but you can see we build
this for developers. However, the largest coder now is MCP agent
and some other of the automatic pipelines. Don't get me wrong, the
developers are still doing the job, but we build this API for engineers,
but agents now are the biggest callers. All right. And last part, I also want to mention briefly why
sometimes you can blindly point the LMs to a profile in some cases. So one of the case is
about Mutax profiling. If you're familiar with GO
in GO's MUTAX profiling, the cost always lands on the GO
routine that unlock the lock. So the hottest frame is always
on the standard library. However, if you point this to the models, the model will start to fixing
the GO standard library. I guess the GO team is probably doing
okay and what you should focus on is your own functions that you can fix and decide. So what we do is we coin a term
named sort of a neurosymbolic. So essentially it's two parts. The symbolic part is we do some kind of
a program analysis, it reads a profile, it finds out what are hard functions and
what are good candidates to basically run over for the optimize. And then we
pass this function down to the neural part, which is a model or agent. So they
are really good at optimize the code, write synthetic benchmark, keeps going until the
game is sort of stopped. At a very high level, we just
sort of doing kind of analysis, program analysis to decide where to or
what functions we should look at and the agent will decide or the model will decide
how they really actually to write and optimize the code. And this is sort of
like a whole loop going to look like. We start from the continuous
profilings we already collected. We rank and localize the functions
and agent keeps optimizing it until it reaches to a good PR
review for the humans and no one's really triggering it and the profiles
is already there and pipelines running. Also, I want to share sort of
a quick trick that we tried, I think probably good to mention. Here's
a rule that we hold to ourself because when we're talking about
performance optimization, if the original function and the new
function gives different results on the same input, very likely
it's not optimization. It's just the outage with
a good number on paper. So what we do is we have a special pipeline to measure
basically all the branches of a function that the input and output needs to be
exactly the same. If it's not the same, we will not resolve the PR. However, I also want to mention
this is only a filter. It's not a proof because the mutex
optimization case I showed you earlier, all the paths
is exactly the same. The problems on the downstream
agent won't know it. All right. Yeah. Okay. So this is a sort of a thread that
basically through the whole talk. I want to mention is agent can
only fix the things it can see. And compared with developers, if
developers doesn't know any data, they will stop, but agent will confidently hallucinate
and pick up the wrong functions to optimize. That's why like
whiz of coin flipping, three quarters of our service will not
have any profiles and it's not ideal. And two things to take home. First, again, AI can only fix the things
it can see under this era. So before you trust your agent's ranking, check your data or profile or other
datas in general to make sure you have a good coverage and what it's not like
only at the dashboard implies at a service level. And second is also be careful about
your fix or your optimization. A fix can work, but it still can break
things. When something gets faster, go and look the downstream to make
sure your system is ready for the optimization. All right. Before I finish, I want to say thank you.
This is not a solo project. I have probably about 25 or even more
collaborators from both Uber and Grafana, and I think some of them are
actually in this building. Yeah. So my thanks to every one
of them and without you, this project is not possible. And also
I want to say for most of the engineers, it's just a flint graph already
there. They take it for granted, but for infrastructure team, that's actually one of the best
compliment you can get. All right, so that's what we contribute. And we are also working on open
sourcing the PowerSchool proxy. And if you want to know when it's land
or argue about sampling or just chatting about favorite restaurant in general, my email is there and it has
been a privilege and thank you.

