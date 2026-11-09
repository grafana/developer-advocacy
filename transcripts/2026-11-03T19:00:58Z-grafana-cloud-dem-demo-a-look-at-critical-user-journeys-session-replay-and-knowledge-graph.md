# Grafana Cloud DEM Demo: A Look at Critical User Journeys, Session Replay, and Knowledge Graph

Published on 2026-11-03T19:00:58Z

## Description

Your dashboards can be green while users can't finish the thing they came to do. In this session, Grafana Labs' Priscilla Lam and ...

URL: https://www.youtube.com/watch?v=yHYlbHmXiro

## Summary

The show is titled "Grafana Cloud DEM Demo: A Look at Critical User Journeys, Session Replay, and Knowledge Graph," published on November 3, 2026. The speakers are Priscilla Lam, Senior Product Manager at Grafana Cloud, and Lucasz, Principal Engineer at Grafana Labs. They discussed Grafana's digital experience monitoring (DEM) features, including critical user journeys, session replay, and the knowledge graph, emphasizing the importance of understanding user experience alongside system health. Key takeaways include the necessity of connecting user data with system telemetry to identify issues proactively, the introduction of synthetic monitoring for critical user journeys, and the integration of session replay to enhance debugging processes. 

Topics: Digital Experience Monitoring, Critical User Journeys, Session Replay, Knowledge Graph, Synthetic Monitoring.

## Chapters

00:00:00 Understanding user experience in digital monitoring
00:06:24 Understanding user journeys and incident impact
00:12:51 Analyzing critical user journeys and session replay
00:18:32 Understanding digital experience monitoring in Grafana Cloud

Hello. Hey everyone. Hope you all are having a great ObsCON right now. Happy Wednesday. I'm Priscilla Lam, senior product manager at Grafana Cloud. 

And I'm Lucasz, a principal engineer working on digital experience monitoring here at Grafana Labs. Yes, we’re pretty excited about the topic we have at hand today about users. But before that, a bit about ourselves and what we do outside of Observability. 

If you find me out in the conference hall, feel free to talk to me about anything related to Observability, but also spicy foods—specifically the hot ones gauntlet. It's very painful, but also tasty. I enjoy urban sketching, and of course, One Piece theories. I actually didn't know about One Piece before we started putting this talk together, so we have to catch up on that.

On my side, I enjoy a lot of sports. I'm a big tricking guy. I used to do breakdance for about ten years before I went to university. So if you want to learn a backflip, I can definitely help you learn that in just a couple of minutes backstage. I also have a corgi named Marian; he's one year old. I became a big stack enjoyer around two years ago. 

Before we show off all the new cool features that we've built, I want to start with a little story. A couple of months ago here at Grafana Labs, we were migrating one of our internal feature flag services to a new system. It wasn't my team's project, but it was just something happening in the background. 

One morning, I woke up, brewed my coffee, and sat by my desk, ready to start my day. To my surprise, the feature we had been working on for months at that point—and the one we were about to demo later that day—was gone from production. At that moment, I learned that cortisol kicks in even faster than caffeine. It was a really high cortisol situation. 

I thought to myself, okay, it's time to pause and think about what's going on. Back then, the feature was still in private preview, so I checked the feature flag. Customers were using it, but we still had it hidden behind it. I queried my flag provider, and it turned out that the flag was basically missing. Like, what the hell happened? Why is it missing? 

I went to debug, checked the code where we manage those flags as code, and it was there. It should be true, but it was just not. So now it was time to pull up the big guns. I opened all my dashboards. Every single backend signal looked healthy. Data was still being ingested. Services looked green. No alerts were firing. By every single metric we had, that feature was working; it just wasn't there in production for anyone actually trying to use it. 

So we opened an incident and kept digging as a team. Within a couple of minutes, we found the issue. It turned out that there was an earlier change rolled out that made it so that in production, if a flag was missing a certain very specific metadata field, it would stop evaluating. This change passed every single environment we tested in. It was working in dev, it was working in staging, in canary, in our ops environment—pretty much everywhere—but it did break the environment our customers were using. 

The fix itself was tiny; we just added a single line of code to our repository. We shipped it, and within a few minutes, everything was back to normal. The demo was saved, and so were the customers. 

I kind of remember this incident. Do we remember who was impacted, or can you tell us how this manifested? 

Yeah, this is actually the crazy part. We didn't know. And what's worse, we only found this regression by accident. If it wasn't for the demo later that day, I might not have even opened a Grafana Cloud instance like a production one. We would probably only learn that the feature was not working once our customer reported it or opened a support ticket. 

This was obviously really bad. And this is the thing about software: sometimes it doesn't throw exceptions. Our full stack observability was telling us that everything looked healthy, but in reality, user experience was impacted. The irony? The feature that went missing is one you're about to see in just a couple of minutes, and it's part of our digital experience monitoring product suite. Its sole job is to show you exactly what your users experience. That morning, we couldn't tell. 

But hold onto that question because we are not the only ones asking it. In fact, digital experience monitoring emerged from questions that we heard from customers running into limitations with their observability today. We said, "If my full stack looks healthy, why are we still seeing issues?" 

Teams were doing everything right. They had backends, infrastructure, even front-end apps instrumented, but problems still emerged unexpectedly, and it was because there was a gap. They could understand system health, but they were missing another essential layer: the user experience. Without that connection between system telemetry and users, there were a set of problems that kept coming up. 

There was disjointed context, unclear impact, and issues were found a bit too late. Does that sound familiar? 

Let's start with a quote. An infrastructure engineer at a large UK bank said, "We own tools that see part of, but not the entire end-to-end view. We burn a lot of time piecing information together." That's the first problem: that disjointed context. 

Your digital experience might look something like this: it's a web of services and infrastructure with interconnected goals. Most of it relates to keeping the lights on in your companies today. Some of it powers part of your user experiences, and some are more critical than others. 

When a component starts to degrade, like these in yellow or red, there's no easy way to really separate those two modalities in your system. Especially during an incident, when you have to comb through all of this information and understand the health and impact of that incident, it's hard. You have to hand-match logs and traces at every layer. This is time-consuming, stressful, and just slows everything down when you need those minutes. 

Instead, you should consider tracing from a user. Think about how certain users are able to complete their journeys and perhaps look at users who didn't complete their journeys at all or are frustrated. By orienting around the user, you can connect what happened in their session to the services involved. 

Imagine during an incident or just trying to answer a question; this gives us a smaller scope to investigate. Connecting users to your systems doesn't always prove cause, but it does tell you where to start looking and where to look next. 

But that's only half of it. What else can users do for you? They tell you who's affected. 

Take this example on the left. Without users, you can see that there are about 500 errors in the last 30 minutes, but it's really hard to tell whether all 500 really matter. Let's take the right, add in user context, and we just get so much more interesting information. You can see how many people are impacted. Is it a majority of my users or not? Who are they, and how do they feel about these errors and issues in your system today? 

In this example, I can already see these are new users trying to get through a critical new user workflow, like creating an account. That gives me so much information to take a decision and know whether to escalate the scenario or wait for tomorrow. 

And finally, what about detection? An engineering leader at a B2B manufacturer said, "In the worst scenario, we get a call from our client that something is wrong before we know." 

Okay. Oops. So even if we can see exactly what is happening to a user, that person has already experienced and felt that failure. For a critical journey, that first failure has a cost. In the example Lucasz shared earlier, that cost could have been the demo. The customer could have not signed the deal because they couldn't see the...

**Grafana Cloud DEM Demo: A Look at Critical User Journeys, Session Replay, and Knowledge Graph**

You don't want to wait for a real user signal to experience issues at times. Even worse, you don't want to wait for the hundredth or the thousandth user to report a problem. Instead, synthetic users can walk through these same journeys for you instead of your customers, allowing you to catch failures before they impact the business. Users are a core part of digital experience monitoring. A synthetic user tells you that a known path works, while a real user can tell you which paths were taken, what mattered, and who was affected. Occasionally, you have a user that has a bad experience, and you go in, trace it through, and fix it. Both are part of your stack. 

So let's close that gap in Grafana Cloud. Our philosophy is really grounded in one principle: if your goal is happier users, why aren't we just observing those users alongside your systems today? 

Let's get into the demo. I'm going to go ahead and put on my VP of Product hat and we'll get into a scenario here. I've noticed that our production adoption dashboards are kind of off today. I see that money transfers are dropping, and I decided to go into Slack and message the engineering team because I haven't seen any support tickets or escalations. "What's going on, Lucasz?" 

All right. So I'm going to wear my regular hat, which is the engineer's hat. I must say I love those messages when they come from the VP of Product that something's up. I'm going to start my investigation as I would normally do these days since we live in an agentic world. I'm going to start one just in my Codex CLI. What I have here is I literally copy-pasted what Priscilla had realized into my Codex CLI. It's also configured with Grafana GCX, which is a brand new CLI that gives agents the same access to your Grafana Cloud as you have as a human. 

I'm going to kick this investigation off, and while it's running, I'm going to do what I would normally do. My very first instinct when something's down is to check if my website is even working. To figure this out, I'm going to go ahead and check my synthetics. I can see that we do have one synthetic check configured for our banking application. Unfortunately, it's just an HTTP check, and we're going to get back to this in just a moment to see how we can improve this. This basic check just assesses whether my website is working, and it feels like it's been relatively stable over the last 12 hours. 

Let me go ahead and navigate down. This is the knowledge graph integration, and we are actually shipping it today. The knowledge graph is the shared context layer across Grafana. Since our synthetic monitoring check is monitoring from an application, it just shows up here. We can click to open it in the knowledge graph, and it helps us navigate to where we want to be. 

Let's go ahead and check our KPI dashboard. We know the site is up, but what is the performance and what is the error rate of the website? It looks like it's pretty stable. "Priscilla, do you know when the regression happened?" 

"I feel like it's been going on for the last day." 

"Okay, so let's maybe expand this a little bit to the last 24 hours." I can see that perhaps some pages could use some love in terms of performance, but in terms of the error rate, it looks relatively flat. We know the website is up, we know the performance metrics look okay, and so do the error rates. 

So what can we do next? We can actually ask the question: what are the users actually experiencing? To do that, we are going to navigate to critical user journeys, which is yet another brand new feature we are premiering today. Critical user journeys are a sequence of actions that you wish to monitor. In our case, we have five configured: we are monitoring whether we are able to add a new payee, whether people can apply for a loan, check recent activity, and in our case, we are interested in the money movements. 

Let's go ahead and navigate to that. I can already see there is a little dip here. I think Priscilla was actually right that it did start yesterday. Let's try and zero in on that. Since we are monitoring our critical user journey, which consists of four steps—choosing transfer type, starting transfer, reviewing transfer, and submitting a transfer—if there is a drop in conversion rate, we can now see this. 

Let me zoom in on that and let's try to figure out why this is the case, why those people are failing to convert. To do this, I'm going to click on this step of the user journey and... Actually, no. Let me navigate to the drop-off analysis step. Here, I can see which attributes are not finishing those journeys. In this case, there is something strange going on with mobile. People on mobile Safari are struggling, both on iOS and Android. 

Let's go ahead and maybe group by this attribute. Now I think we've revealed at least part of the answer to the question we are asking. We can see that people on Windows devices are completing their journeys exactly as they were. However, the mobile cohort of users is actually affected. Let's try to figure out why that's the case. I'm going to filter by my iOS device, and now I'm going to simply go into my session list. I only care about these sessions that didn't make it all the way through. 

I can expand it, and this is session replay—yet another feature we are shipping today to help you understand what your users are actually doing. In this case, we are watching a user navigate through the Grafana Bank application. If I want, I can toggle this to full screen. We can see them entering the amount of money, and we can see the masking and everything. At the end of their journey, they seem to be stuck for some reason, but it's not immediately clear why that might be the case. 

Let's see if we can maybe take a look at another session replay. Let's try to find a session that actually did complete the entire user journey because it's not like all of the users are struggling; it's just some cohort of them. In this case, I can open this in a dedicated session player. Here we can see a whole user journey alongside the replay, and let's try to find some user action. 

So, submit transfer. It feels like this user actually did manage to submit a transfer, and let's see how they did that. They are again reviewing the payment and scrolling down. I think we now zeroed in on the issue. You can see that there is an "Ask Grafana Bank" button that's overlaying the actual button used to send the payment. 

While we were looking at that, our agent was working in the background. Let's see if it found anything useful. It says that the evidence points to a mobile payment flow regression triggered by a mobile payment footer experiment. Users reach transfer review but often never submit, and this seems to check out. If you look at this session, you can see that it did actually query all the live data from my Grafana Cloud instance and was able to figure it out all on its own in just around three minutes. 

So that's it for the demo. Let's go back to slides. As you saw in the demo, Grafana Cloud digital experience monitoring is really all about extending your full stack observability all the way to the user. However, the real software development lifecycle doesn't end with an investigation. We have to apply the fix and, more importantly, make sure it never happens again. This is where digital experience monitoring becomes a loop. 

In our scenario, we lacked robust synthetic monitoring checks. We only had a very basic HTTP check configured, and it's not enough if you want to proactively test your user journeys. But it doesn't have to be that way. With browser checks in synthetic monitoring, you get full scripting capabilities and...

You can make it easy to exercise your critical user journeys however you like. And as a bonus, your VP of Product can get some well-deserved peace of mind. So Priscilla, your payments are flowing again, and this time we are going to hear about it first if they stop. Take it away.

Oren Lion, Director of Software Engineering at TeleTracking, puts it well: "Synthetic monitoring tells you something's up. With user actions, it tells you how a customer feels, and session replay helps you debug it." So it's three parts working together to proactively monitor the end user experience.

**DEM is a loop.** Synthetic monitoring protects those key journeys with synthetic user checks so that you know the moment something breaks, even as early as a deployment. Meanwhile, front end observability shows what your real users actually experience and why across the stack, so that you can learn and improve the product.

Here's how you can think about applying this and all of the new features in Grafana Cloud. Let's start with what we saw earlier in the demo. The site was up, but nothing was paging, and critical user journeys showed the completion rate falling. With critical user journeys, you can create a handful of journeys for your teams and get one view end to end, from that user KPI down to the trace, to debug what is going on with your user experience today. You can, of course, create synthetic checks on these journeys. With a new easy button in synthetic monitoring, you can create SLOs on these checks and align them against your own team's reliability goals, so you know what to optimize for. Together, they help you protect a core user experience across your teams.

**Next, detect and see who's affected.** When something breaks, usually you get that number, an error rate, or a failed check, but you don't actually have enough to see what a user went through to reproduce the issue. That's easier now with session replay and front end observability, currently in public preview. It shows what the user actually did and what they saw with a video-like fidelity, so that you can explore what they did and saw in the browser. These are connected to traces and logs across the stack, so that you can find the root cause easily if issues are occurring.

**Second, real user context is now closer to your browser checks today in synthetic monitoring.** When a check fails, you now have front end observability data alongside it, so that you can see how a failure felt to a user and decide what to do next.

**Finally, understanding the complete story.** During an incident, we talked about how all that context is scattered everywhere. Full stack visibility powered by knowledge graph now includes front end and synthetic checks on those graphs, so that you can follow an issue from a user running into an issue, a failed synthetic check, down to the backend services, and down to the underlying database. Meanwhile, mobile observability also brings more native mobile users into your stack as well. We showed some examples where the issue was impacting mobile Safari users. If you were to create an app today, you could get that visibility and start seeing the mobile experience with mobile observability. 

With mobile observability, you see that end-to-end view similar to front end observability and understand the health of your apps. Finally, Lucasz showed this earlier: that data's noisy and hard to navigate at times. You can connect all of this data for your users to GCX and Grafana or Grafana Assistant. We've added more context to these tools so that whether you want to use your custom tools to connect to your code bases or context, or use the UI in Grafana Assistant, you can better understand what is going on and how to navigate all the insights that you'll be seeing across your users today. Both have better context for better token efficiency.

Again, just use all of that you've learned to improve your product or your observability. Each time you learn something new, those new unknowns can become and inform new protected knowns. So many of these features are available to try on Grafana Cloud, and some of these are coming soon. 

If you do one thing this week, pick a journey that's important to your business today. Consider creating a synthetic check on that journey or use session replay to see what users actually did in that journey. Grafana Cloud is growing beyond observability into digital experience monitoring. Our philosophy hasn't changed. We do believe in full stack observability, but we really want to change how you understand your systems. 

Can someone accomplish what they set out to do? If not, why? Who? After all, if the goal is happier users and better experiences, it's time to close that gap and make the user experience a part of your full stack. 

Thank you. Thank you.

## Raw YouTube Transcript

Hello. Hey everyone. Hope you all are 
having a great ObsCON right now. Happy Wednesday. I'm Priscilla Lam, senior 
product manager at Grafana Cloud. And I'm Lucasz. I'm a principal 
engineer working on digital experience monitoring here at Grafana Labs.
Yes. So we're pretty excited about the topic that we have at hand today about users. But before 
that, a bit about ourselves and what we do outside of Observability. So if you find me out in the 
sort of conference hall, feel free to talk to me about anything related to Observability, but also 
spicy foods, specifically the hot ones gauntlet, very painful, but also tasty. Urban sketching, 
and of course, One Piece Theories. I actually didn't know about the One Piece before 
we started putting the stock together, so we have to catch up on that. On my side, I enjoy a lot 
of sports. So I'm a big tricking guy. I used to do breakdance for like 10 years before I went to 
university. So if you want to learn a back flip, I can definitely help you learn that in just 
a couple of minutes backstage.I also have a corgi. So this is Marian, he's one year 
old. And I actually became a big stack enjoyer around two years ago. So this is me.
And before we show off all the new cool features that we've built, actually I want to start 
with a little story. So a couple of months ago here at Grafana Labs, we were migrating 
one of our internal feature flag services to a new system. It wasn't my team's 
project, but it was just something happening in the background. So one morning I 
wake up, I brew my coffee, I sit by my desk, ready to start my day. And to my surprise, the 
feature we've been working on for months at that point and the one we are about to demo later that 
day is gone from production. That moment I learned that cortisol kicks in even faster than caffeine. 
So yeah, it was really high cortisol situation. Anyhow, I think to myself, okay, it's 
time to pause and think what's going on? So back then the feature was still in private 
preview. So I go ahead and I check the feature flag. Customers were using it, but we still had 
it hidden behind it. I query my flag provider and it turns out that the flag is basically missing. 
Like, what the hell happened? Why is it missing? I go, I debug, I check the code where we 
manage those flags as code and it's there. It should be true, but it's just not.
So now it was time to pull up the big guns. I open all my dashboards. Every single 
backend signal looks healthy. Data is still being ingested. Services look green. No alerts 
are firing. So by every single metric we had, that feature was working. It just wasn't there in 
production for anyone actually trying to use it. So we open an incident and we keep digging as 
a team. Within a couple of minutes, we found the issue. So it turned out that there was an 
earlier change rolled out and it actually made it so that in production, if a flag was missing 
a certain very specific metadata field, it would stop evaluating. So this changed past every single 
environment we tested in. It was working in dev, it was working in staging, in canery, in our ops 
environment, pretty much everywhere, but it did break the environment our customers were using.
So the fix itself was tiny, right? We just added a single line of code to our repository. We 
shipped it and a few minutes everything was back to normal. Demo was saved 
and so were the customers. I kind of remember this incident. 
Do we remember who was impacted or can you tell us how this manifested?
Yeah, this is actually the crazy part. We didn't know. And what's worse, we only found this 
regression by accident. If it wasn't for the demo later that day, I might have not even opened a 
Grafana Cloud instance like a production one. And we'd probably only learn that the feature is not 
working once our customer reported it or opened a support ticket. So this was obviously really bad.
And this is the thing about software, sometimes it doesn't throw exceptions. Our 
full stack observability was telling us that everything looks healthy, but in reality, user 
experience was impacted. And the irony, well, the feature that went missing is one you're 
about to see in just a couple of minutes and it's part of our digital experience monitoring 
product suite. And its sole job is showing you exactly what your users experience. That morning, 
we couldn't tell. But hold onto that question because we are not the only ones asking it.
Yeah. In fact, digital experience monitoring emerged from questions that we heard from 
customers running into limitations with their observability today. We said, "If my full stack 
looks healthy, why are we still seeing issues?" So we had teams doing everything right. They had 
backends, infrastructure, even front end apps instrumented, but problems still emerged 
unexpectedly, and it was because there was a gap. They could understand system health, but 
they were missing another essential layer, the user experience. Without that connection between 
system telemetry and users, there were a set of problems that kept coming up. There's disjointed 
context. Impact was unclear and issues were found a bit too late. Does that sound familiar? Let's 
start with a quote. An infrastructure engineer at a large UK bank said, "We own tools that see part 
of, but not the entire end-to-end view. We burn a lot of time piecing information together. That's 
the first problem, that disjointed context." So your digital experience might look 
something like this. It's a web of services, infrastructure with interconnected goals. 
Most of it relates to keeping the lights on in your companies today. Some of it powers 
part of your user experiences and some are more critical than others. When a component 
starts to degrade like these in yellow or red, there's no easy way to really separate those two 
modalities in your system. And especially during an incident when you have to comb through all 
of this information and understand the health and impact of that incident, it's hard. You have 
to hand match logs and traces at every layer. And this is time-consuming, stressful, and just slows 
everything down when you need those minutes. Instead, you should consider tracing from a user. 
Think about how certain users are able to complete their journeys and perhaps look at users who 
didn't complete their journeys at all or are frustrated. By orienting around the user, you 
can connect what happened in their session to the services involved. And you can imagine during 
an incident or just trying to answer a question, this gives us a smaller scope to investigate. 
Connecting users to your systems doesn't always prove cause, but it does tell you where to 
start looking and where to look next. But that's only half of it. What else can users 
do for you? They tell you who's affected. So take this example on the left. Without 
users, you can see that there are about 500 errors in the last 30 minutes, but it's really 
hard to tell whether all 500 really matter. Let's take the right, add in user context and we 
just get so much more interesting information. You can see how many people are impacted. Is it a 
majority of my users or not? Who are they and how do they feel these errors and issues in your 
system today? In this example, I can already see these are new users trying to get through 
a critical new user workflow, like creating an account. That gives so much information for 
me to take a decision and know whether to escalate the scenario or wait for tomorrow.
And finally, what about detection? So an engineering leader at a B2B manufacturer said, 
"In the worst scenario, we get a call from our client that something is wrong before we know." 
Okay. Oops. So even if we can see exactly what is happening to a user, that person has already 
experienced and felt that failure. For a critical journey, that first failure has a cost. In the 
example Lucasz shared earlier, that cost could have been the demo. The customer could have 
not signed the deal because they couldn't see the feature we were trying to show them. You don't 
want to wait for a real user signal to experience this at times. And even worse, you don't want to 
wait for the hundredth or the thousandth user to report this. Instead, synthetic users can walk 
through these same journeys for you instead of your customers so that you can catch the 
failure before it impacts the business. So users are a core part of digital experience 
monitoring. Synthetic user tells you that a known path works. A real user can tell you which 
paths were taken and what mattered and who was affected. Occasionally you have a user that 
has a bad time and you go in, trace it through and fix it. Both are part of your stack.
So let's close that gap in Grafana Cloud. Our philosophy is really grounded in one 
principle. If your goal is happier users, why aren't we just observing those 
users alongside your systems today? So let's get into the demo. I'm going to go 
ahead and put on my VP of product hat and we'll get into a scenario here. So I've noticed 
that our production adoption dashboards are kind of off today. I see that money transfers are 
dropping and I decided to go into Slack and message the engineering team because I haven't 
seen any support tickets. I haven't seen any escalations. What's going on?
Lucasz, what's up? All right. So I'm going to wear my regular 
hat, which is the engineer's hat. And I must say I love those messages when they come from 
VP of product that something's up. So I'm going to start my investigation as I would normally do 
these days since we live in an agentic world. So I'm going to start one just in my Codex CLI.
What I have here is I literally copy pasted what Priscilla had realized into my Codex 
CLI. It's also configured with Grafana gcx, which is a brand new CLI that gives agents the 
very same access to your Grafana cloud as you have as a human. So I'm going to kick this 
investigation off. And while it's running, I'm going to do what I would normally do. So 
I'm going to go and take a look in Grafana. My very first instinct when something's down is, 
is my website even working? So to figure this out, I'm going to go ahead and check my synthetics. 
And I can see that we do have one synthetic check configured for our banking application. 
Unfortunately, it's just an HTTP check and we're going to get back to this in just a moment to see 
how we can improve this. So this basic check just assesses whether my website is working. So it 
feels like it's been relatively stable over the last 12 hours. So let me go ahead and navigate 
down. This is the knowledge graph integration and we are shipping it actually today. So what 
knowledge graph is, is the shared context layer across Grafana. And since our synthetic monitoring 
check is monitoring from an application, it just shows up here. So we can click open it in the 
knowledge graph and it helps us navigate to where we want to be. So let's go ahead and check our KPI 
dashboard. So we know the site is up, but what is the performance and what is the error rate of the 
website? And it looks like it's pretty stable. Priscilla, do you know when 
the regression happened? I feel like it's been going on for last day.
For the last day. Okay. So let's maybe expand this a little bit to last 24 hours. And I can see that 
perhaps some pages could use some love in terms of performance, but in terms of the error rate, 
it looks relatively flat. So we know the website is up. We know the performance metrics look okay, 
and so do the error rates. So what can we do next? We can actually ask a question, what are the 
users actually experiencing? And to do that, we are going to go ahead and navigate to 
critical user journeys, which is yet another brand new feature we are premiering today.
So critical user journeys is a sequence of actions that you wish to monitor. In our case, we 
have five configured. We are monitoring whether we are able to add a new payee, whether people 
can apply for a loan, check recent activity. And in our case, we are interested in the money 
movements. So let's go ahead and navigate to that.And I can already see there is a little 
deep in here. So I think Priscilla was actually right that it did start yesterday. So let's try 
and zero in on that. And since we are monitoring our critical user journey, which consists of four 
steps, choosing transfer type, starting transfer, reviewing transfer and submitting a transfer, 
if there is a drop in conversion rate, we can now see this. So let me zoom in on that 
and let's try to figure out why this is the case, why those people are failing to convert.
So to do this, I'm going to just click on this step of the user journey and... Actually, 
no. Let me actually go and navigate to the drop-off analysis step. So in here I can see which 
attributes are not finishing those journeys. And in this case, there is something strange going on 
with mobile, right? People on the mobile safari are struggling, on iOS and Android. So let's 
go ahead and maybe group by this attribute. And now I think we've revealed at least part of the 
answer to the question we are asking. So we can see that people on Windows devices are completing 
their journeys exactly as they were. However, the mobile cohort of users is actually affected.
So let's try to figure why that's the case. I'm going to filter by my iOS device and now 
I'm going to simply go into my session list. And I only care about these sessions that didn't 
make it all the way through. So I can expand it, and this is session replay. So yet another feature 
we are shipping today to help you understand what your users are actually doing. In this case, we 
are watching user navigating through the Grafana Bank application. If I want, I can toggle this 
full screen. And we can see them entering the amount of money. We can see the masking and 
everything. And at the end of their journey, they seem to be stuck for some reason, but it's 
not immediately clear why that might be the case. So let's see if we can maybe take a look at 
another session replay. So let's try to find a session that actually did complete the entire user 
journey because it's not like all of the users are struggling. It's just some cohort of them.
So in this case, I can maybe open this actually in a dedicated session player. And here we can 
see a whole user journey alongside the replay and let's maybe try and find some user action. 
So submit transfer. So it feels like this user actually did manage to submit a transfer, and 
let's see how they did that. So they are again, reviewing the payment and they're scrolling 
down. I think we now zeroed in on the issue. So you can see that there is an Ask Grafana 
Bank button that's overlaying the actual button that is used to send the payment.
So while we were looking at that, our agent was working in the background. Let's 
see if it did find anything useful. So it says that the evidence points to a mobile payment flow 
regression triggered by a mobile payment footer experiment. Users reach transfer review, but often 
never submit, and this seems to check out. And if you look at this session, you can see that it did 
actually query all the live data from my Grafana Cloud instance and it was able to figure it out 
all on its own in just around three minutes. So that's it for the demo. 
Let's go back to slides. And yeah, so as you saw in the demo, Grafana Cloud 
digital experience monitoring is really all about extending your full stack observability all the 
way to the user, but real software development lifecycle doesn't end with an investigation. 
We have to apply the fix, and more importantly, make sure it never happens again. This is where 
digital experience monitoring becomes a loop. In our scenario, we lacked robust synthetic 
monitoring checks. We only had a very basic HTTP check configured and it's not enough 
if you want to proactively test your user journeys. But it doesn't have to be that way. 
With browser checks in synthetic monitoring, you get full scripting capabilities 
and you can make it easy to basically exercise your critical user journeys however 
you like. And as a bonus, your VP of product can get some well-deserved peace of mind.
So Priscilla, your payments are flowing again, and this time we are going to hear about 
it first if they stop. Take it away. So Oren Lion, director of software 
engineering at TeleTracking puts it well, "Synthetic monitoring tells you something's up. 
With user actions, it tells you how a customer feels and session replay helps you debug 
it. So it's three parts working together to proactively monitor the end user experience."
So DEM is a loop. Synthetic monitoring protects those key journeys with synthetic user checks 
so that you know the moment something breaks, even as early as a deployment. Meanwhile, front 
end observability shows what your real users actually experience and why across the stack 
so that you can learn and improve the product. So here's how you can kind of think about applying 
this and all of the new features in Grafana Cloud. Let's start with what we saw earlier in the 
demo. The site was up, but nothing was paging, but critical user journeys showed the completion 
rate falling. With critical user journeys, you can create a handful of journeys for your 
teams and get one view end to end from that user KPI down to the trace, to debug what is going on 
with your user experience today. You can of course create synthetic checks on these journeys. And 
with a new easy button in synthetic monitoring, you can create SLOs on these checks and align them 
against your own team's reliability goals so you know what to optimize for. Together, they help you 
protect a core user experience across your teams. Next, detect and see who's affected. So when 
something breaks, usually you get that number, an error rate, a failed check, but you don't 
actually have enough to see what a user went through to reproduce the issue. That's 
easier now with session replay and front end observability currently in public preview. 
It shows what the user actually did and what they saw with a video like Fidelity so that 
you can explore what they did and saw in the browser. These are connected to traces and 
logs across the stack so that you can find the root cause easily if issues are occurring.
Second, real user context now is closer to your browser checks today in synthetic 
monitoring. When a check fails, you now have front end observability data 
alongside it so that you can see how a failure felt to a user and decide what to do next.
Finally, understanding the complete story. So during an incident, we talked about how all 
that context is scattered everywhere. Full stack visibility powered by knowledge graph now includes 
front end and synthetic checks on those graphs so that you can follow an issue from user running 
into an issue, a failed synthetic check, down to the backend services, down to the underlying 
database. Meanwhile, mobile observability also brings more native mobile users into your stack 
as well. We showed some examples where the issue was impacting mobile Safari users. If you were to 
create an app today, you could get that visibility and start seeing the mobile experience with mobile 
observability. Mobile observability, you see that end-to-end view similar to front end observability 
and understand the health of your apps. And then finally, Lucasz showed this earlier, 
that data's noisy and hard to navigate at times. You can connect all of this data for 
your users to gcx and Grafana or Grafana Assistant. We've added more context to these 
tools so that whether you want to use your custom tools to connect to your code bases or 
context or use the UI and Grafana Assistant, you can better understand what is going on and 
how to navigate all the insights that you'll be seeing across your users today. Both have better 
context for better token efficiency. And again, just use all of that that you've learned to 
improve your product or your observability. Each time you learn something new, those new unknowns 
can become and inform new protected knowns. So many of these features are available to try on 
Grafana Cloud, and some of these are coming soon. If you do one thing this week, pick a journey 
that's important to your business today. Consider creating a synthetic check on that journey or 
use session replay to see what users actually did in that journey. Grafana Cloud is growing 
beyond observability into digital experience monitoring. Our philosophy hasn't changed. 
We do believe in full stack observability, but we really want to change how you understand 
your systems. Can someone accomplish what they set out to do? If not, why? Who? After all, if 
the goal is happier users and better experiences, it's time to close that gap and make the 
user experience a part of your full stack. Thank you.
Thank you.

