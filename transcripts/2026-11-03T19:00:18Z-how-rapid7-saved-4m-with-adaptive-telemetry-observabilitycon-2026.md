# How Rapid7 Saved $4M with Adaptive Telemetry | ObservabilityCON 2026

Published on 2026-11-03T19:00:18Z

## Description

Carl Eastman of Rapid7 explains how the company used Grafana Cloud Adaptive Telemetry to eliminate 1.4 billion time series ...

URL: https://www.youtube.com/watch?v=cfx38hEe2Ks

## Summary

The show is titled "How Rapid7 Saved $4M with Adaptive Telemetry" and was published on November 3, 2026. The speaker, Carl Eastman, is a principal software engineer for the Observability and Service Mesh team at Rapid7. He discusses Rapid7's transition to Grafana Cloud, specifically focusing on the use of Adaptive Telemetry to manage costs and improve observability by eliminating unnecessary data. Key takeaways include the significant savings achieved through Adaptive Telemetry, the importance of using open standards like OpenTelemetry, and the benefits of Grafana Assistant for enhancing user experience and onboarding. 

Topics: Grafana Cloud, Adaptive Telemetry, OpenTelemetry, Grafana Assistant, cost management.

## Chapters

00:00:00 Evaluating vendors and choosing Grafana Cloud
00:07:22 Cost management and adaptive telemetry savings
00:13:41 Using Grafana Assistant for enhanced observability

Hi, how's everybody doing? My name's **Carl Eastman**. I'm a principal software engineer for the Observability and Service Mesh team at **Rapid7**. Rapid7 is a human-led, AI-augmented cybersecurity company. Today, I'm going to be talking about our journey that kind of stalled a couple of years ago and how we ended up at **Grafana Cloud**.

A little bit about me: I love Jeep Wranglers. This is one of three. This one's themed after Netflix's *Stranger Things*, and my daughter usually drives this one to work.

### Agenda

The agenda today includes:

- The vendor evaluation we went through because our journey stopped.
- Why we chose Grafana Cloud and some of the reasons for that.
- The benefits we experienced after moving to Grafana Cloud.

### The Journey

In 2024, our journey stopped. We weren't on Grafana Cloud; we were on a different vendor. It was really expensive, and we could only look at metrics, which was costing a lot of money for our budget. We couldn't look at traces or logs, and we couldn't really do much of anything else. At that point, our contract was coming up, and we decided to look at the landscape: who else is out there?

We looked at some of the market leaders and also examined what Observability was going through at that time. We were really intrigued by **OpenTelemetry** and how it could help us correlate data. We weren't able to do that because we were on a proprietary vendor-locked library, so we had no correlation.

During the evaluation, we decided to stop using the vendor-specific agent and go with a more open-source approach. We used the OpenTelemetry collector as a level playing field for all the vendors to utilize. Basically, every vendor, all we did was change the endpoint. We kept all the metrics, traces, logs—everything that was generated stayed the same—and we just sent it to different vendors to see how they reacted and what they could do with it.

### Choosing Grafana Cloud

When we got to Grafana Cloud, one of the things that was really interesting was their adaptive... Actually, it wasn't called Adaptive Telemetry at that point; it was called Adaptive Metrics. Jumping ahead, we actually chose Grafana Cloud. When we started rolling out our collectors, we decided not to use the OpenTelemetry Collector; instead, we used **Grafana Alloy**. Grafana has a great Kubernetes monitoring Helm chart that helps you deploy and configure Alloy really nicely.

During the proof of concept (POC), which wasn't long—we only did a couple of weeks for each vendor—the Adaptive Metrics at that point showed a lot of promise. We were kind of skeptical, but we could see the potential. We didn't have a lot of users in the POC, so we didn't have many dashboards or alerts. There wasn't a lot for Adaptive Metrics to give us recommendations on, but we saw the potential there. 

So we made the jump. We decided, "Yep, we're going to go with Grafana Cloud." We saw the potential and all the cost management features we could use. That was two years ago, and now, fast-forward two years, we also liked it for the open standard support. We wanted to correlate our traces, metrics, and logs together to enable our engineers to troubleshoot much more effectively. Now, you're not trying to look at timestamps and go between different data sources and platforms.

### Results and Savings

The estimates during the POC were not wrong; they were actually a little lower than what we're seeing right now. It also changed from Adaptive Metrics to Adaptive Telemetry. Every time Steve and his team turned something new on, I was in there turning it on too. I was like, "Yes, adaptive logs, sounds good. Adaptive profiles, sounds good. Keep turning it on."

As Steve mentioned, there's so much data out there now, and a lot of it doesn't matter. For example, if you're new to coding and your boss says, "Make me a microservice," you might tell your coding agent, "Hey, I need telemetry." The agent may or may not ask you, but then it just turns on auto instrumentation. Now you have metrics for things that don't matter, like a whole bunch of 200 status code log lines or traces from your Kubernetes readiness probes.

But with Adaptive Telemetry, you can turn off those things that don't matter. A couple of months ago, my account executive came to me and said, "Do you realize how much money you're saving from Adaptive Telemetry?" I said, "No," because I've been busy looking at other dashboards and projects. When I checked the cost management billing tab, I was shocked to see we saved almost $5 million in the last year. 

How many people think saving $5 million a year is pretty good? *Show of hands.* Yeah, I think a lot of people would like to save that much. 

### Conclusion

Adaptive Telemetry shows you what doesn't matter. We're generating $5 million worth of stuff that doesn't matter, but it's really easy to manage with Adaptive Telemetry. The hard part is stopping all those signals from coming in. That takes time; you have to work with your development team and analyze the data. Adaptive Telemetry tells you what's not useful, and then you can take that information back to your development team and say, "Stop logging all this stuff. Stop tracing this stuff." 

This way, you can keep shrinking that bill back down. I'd love to have that at zero, but that's not realistic. Customers of ours don't care if our Adaptive Telemetry bill is zero, so it's hard to justify that much development effort to shrink it down.

Currently, this is what our Adaptive Telemetry looks like. A couple of months ago, I was in the private preview for the auto apply feature, and I was one of those scared customers because the auto apply would increase my series by 480,000. That wasn't too bad; a couple of weeks before this, the screenshot showed 2.5 million, which is quite a bit if I just turned on auto apply. 

I'm really excited about the cost management feature they just talked about. I'm looking forward to getting back to work and turning on auto apply and that cost management feature so that someone can't just write a query and suddenly my bill goes up by $10,000 overnight because they wrote a query looking at pod-level metrics.

The toil of trying to keep this up to date and maintained is significant. I remember one Saturday morning, I was having some coffee and doing what you normally do: logging into Grafana. I looked at some of the legacy dashboards, including a cost management dashboard that shows how many series are coming in. I knew on Friday it was about 30 million, but Saturday morning it was 40 million. 

Somewhere along the line, Friday afternoon, someone decided to auto-instrument, deploy, and leave for the day. I was able to quickly go into Adaptive Metrics, find the metric that showed up, those 10 million series, and click "drop rule." I haven't heard from that person, and it's been a year. So whoever enabled it didn't need it.

cost us a lot of money. However, because Grafana gives you a nice little window of opportunity every month to fix mistakes like that, I was actually able to save that 10 million series for that month.

Here's an example of a rule. This is one of the Adaptive Telemetry recommendations. You can see the analysis that it goes through. It shows you that there are no alerts, one dashboard, and three queries. Based on that analysis, it recommends the type of aggregation you should do and the labels you can aggregate away without impacting anything because nobody's queried them, and the dashboard isn't referencing them. Enabling that just saves you money.

With the adaptive metrics saving us a lot of money, we also turned on the adaptive logs and adaptive traces. That was saving us a lot of money too. But we didn't just take that money and put it in the bank, saying, "Okay, we're good. We're just going to look at metrics and that's it." That's not Observability; looking at just one pillar of metrics is not enough. Instead of going all the way back and saying, "Yep, our budgets dropped a lot," we did reduce our budget, but we kept some of that money and started looking into other things. We began sending more logs and more traces.

Here are some examples of our savings on logs. For an hour, we generated 1.1 terabytes of data, but we dropped 1.02 terabytes of noise that just didn't matter. For tracing reduction, we achieved the same thing with a 90% reduction. We enabled many of the features discussed, such as volumetric policies and diversity policies. As soon as they turned things on, I went in and enabled them because there's no sense in not doing so; it just saves you money, which you can then invest into other things.

Adaptive log patterns analyze the incoming data. For instance, if there's a log pattern that has never been queried, we can drop 99% of it. You don't want to drop 100% because then your developers might wonder, "Is my application working because nothing's coming in?" So, you still need a little bit coming in to give them that warm, fuzzy feeling that the application is still working and logging. We can save a good amount of money by dropping 99% or even 99.9%.

This is a drop rule. You don't have to wait for adaptive logs to analyze your usage. I enabled some debug logs for an application, knowing it would generate a lot. There’s a log line that says "framed," which I didn't need from the debug logs. So, I created a drop rule for this particular service: for the log level debug, if it contains that line, just drop 99% of it. This saved me 14 terabytes because I preemptively knew I didn't need that data.

All the savings we achieved allowed us to invest in more Observability. Now, we're expanding into our testing and doing some front-end Observability stuff. We're using Grafana Assistant, which has provided us with more value out of our Observability dollar.

This is from the Grafana playground, showcasing synthetic testing. You can write a little test and say, "Send this out to three different countries and let me know how things look from those locations." If your service is not publicly exposed, you can deploy a private probe into your environment and run the test from there, feeding the data back up to Grafana Cloud.

For front-end Observability, for a small price, just adding an SDK into Node.js gives you real user monitoring. Now, you can start seeing what the user experiences. Recently, they enabled replay sessions, allowing you to see what a customer is experiencing. I was talking with our support manager and showing him the front-end Observability and Grafana Assistant. I said, "Check this out. This is cool. You can analyze the website." 

He, being part of the support team, often gets calls from customers saying, "I'm on your website, and I'm going down a certain path, and it's not working." Previously, he would ask customers to send a hard file. How many people know what a hard file is? Now, he has to explain how to generate and submit it. But with this new setup, we instrumented the front page. We hit Grafana Assistant and analyzed the website. He asked, "Can we go back three days? We had a problem then." I said, "Sure. Grafana Assistant, three days ago, was anything happening?" 

He turned away, and I said, "Yeah, two different paths from your main website were having issues." He was blown away. He didn't ask for a hard file, nor did he have to wait for multiple customers to report issues on that particular path.

Grafana Assistant has become our best buddy. Many people at Rapid7 are using it. I've had people reach out to me directly or in our public instant messengers, sharing how they're using it and how happy they are. Teams are creating dashboards without knowing a query language; they just use natural language to create dashboards or analyze alerts.

I wrote a skill for cluster upgrades. How many times do you upgrade something, and someone says, "Well, it's broken, or you broke my application," and you're like, "I'm pretty sure I didn't." With this skill, you can run a two-part analysis. First, it looks at your cluster and environment, checking all logs, metrics, and traces. Then, after the upgrade, it compares the data to see if anything new started crashing or if there are any performance differences. This provides a nice validation to go back to the team you upgraded and say, "It looks good before and after." 

If they say, "This is crashing now," you can respond, "Well, it was crashing before. I can't fix 'image not found.' Upgrading the cluster isn't going to fix that." Teams are even creating their own skills and sending them to us for integration, leading to a lot of good usage.

This is Grafana Assistant analyzing an alert. When an alert pops up, it analyzes what happened. This is great for those late-night situations where someone is troubleshooting. It can quickly analyze and say, "Oh, your thing's getting OOM killed." That's an easy fix. Before Assistant, you would have to...

To start going, finding the pod, which cluster is it on? It just makes it so much easier because there's so much data to access. Here's a dashboard I built. One tip though: hit save. When you're having an assistant make changes to your dashboard, hit save fairly often. Ninety-nine percent of the time, it does a great job, but I've run into a few instances where it's like, "Oops," and then your dashboard is gone. You have to go into version history, go back one, ask it the same prompt, and then it does it correctly. So, save often.

If you notice the prompt there, you can see it on the screen. It's basically, "Bring me a dashboard for this microservice in this namespace." There's no query language in there. This is a usage graph. I was curious, so I looked through Grafana Cloud and saw there's a usage section underneath the Assistant. I've been using the Assistant every day, a lot. I was expecting to be first or second, but I was actually fifth, and the top two people were using it three times as much as the third person. I was like, "Wow, they're really using the heck out of this thing." 

I looked at it and didn't recognize either of their names, so I looked them up. I was surprised to find out that they were two interns we hired. I reached out to them and asked, "Hey, how are you finding Grafana Assistant?" They replied, "It's fantastic! We just got out of university. We don't know anything about Grafana, dashboards, or alerts. We know nothing, but in the first week that we're here, we've been creating dashboards and helping our team investigate alerts." 

So, there's an immediate onboarding benefit for people. I thought, "Great, keep going," because in my mind, it's more the mid-level senior people who would be using the Assistant. I didn't even think that this would be a great use case because you don't need to know a query language. I mean, how many universities teach query languages? It's not usually on the syllabus.

So, three things: Observe what matters. Adaptive Telemetry shows the opposite; it shows you what doesn't matter, so leverage that. And Grafana Assistant— you'll see their little double star on every page. Click it, ask it questions. It knows the page you're on, and it just keeps getting better and better. 

Thank you very much. Carl Eastman from Rapid7.

## Raw YouTube Transcript

Hi, how's everybody doing? My name's Carl 
Eastman. I'm a principal software engineer for the Observability and Service Mesh team at Rapid7. 
Rapid7 is a human-led, I guess, AI augmented cybersecurity company. So today I'm going to be 
talking about our journey that kind of stalled a couple years ago and how we ended up at Grafana 
Cloud. So a little bit about me. I love Jeep Wranglers. This is one of three. This one's themed 
after Netflix's Stranger Things, and my daughter usually drives this one to work. So the agenda 
today I want to talk about is the vendor valuation we went to because our journey stopped. We needed 
to move on from the vendor we were on. Then we're going to talk about why we chose Grafana Cloud 
and some of the reasons for that, and then some of the benefits after we got onto Grafana 
Cloud of everything else that we're using. So 2024, our journey stopped. We weren't 
on Grafana Cloud, we were on a different vendor. It was really expensive. And it was really 
expensive so that we can only look at metrics and that was costing a lot of money for our budget. We 
couldn't look at traces, we couldn't look at logs, couldn't really do much of anything else. So at 
that point, our contract was coming up and we decided to look on the landscape. Who else is out 
there? So we looked at some of the market leaders and we also looked at what is Observability going 
through right now? We were really intrigued by OpenTelemetry and looking at how you could 
correlate stuff together. We weren't doing that now because we were on a proprietary vendor 
locked in library, so we had no correlation. So during the evaluation, we decided to stop using 
the vendor specific agent and go with a more open source. So we used the OpenTelemetry collector 
as a level playing field for all the vendors to utilize. And basically every vendor, all we did 
was just change the endpoint. So we kept all the metrics, traces, logs, everything that was getting 
generated stayed the same and we just sent it to different people and just saw how those different 
people reacted and what they could do with it. So when we got to Grafana Cloud, one of the things 
that was really interesting was their adaptive... Actually it wasn't called Adaptive Telemetry 
at that point. It was called Adaptive Metrics. Also, jump a little bit ahead, we actually 
chose Grafana Cloud. So when we did start rolling out our collectors and everything, 
we decided not to use the OpenTelemetry Collector. We decided to use Grafana 
Alloy instead. Grafana's got a great Kubernetes monitoring helm chart that helps 
you deploy and configure Alloy really nicely. So during the POC, it wasn't a long POC, we 
only did a couple weeks for each vendor, but the Adaptive Telemetry, well, adaptive metrics at 
that point really showed a lot of promise. We were kind of skeptical, but we could see the potential 
for it. We didn't have a lot of users in the POC, so we didn't have a lot of dashboards, not 
a lot of alerts. There wasn't a lot for Adaptive Metrics to give us recommendations 
back on, but we saw the potential there. So we made the jump. We decided, yep, we're going 
to go product cloud. We saw the potential. We saw all the cost management features that we 
could use. So that was two years ago and we jump ahead two years now. We also liked it for 
the open standard support because we want to get to where we can start correlating our traces, our 
metrics, our logs together to enable our engineers to actually troubleshoot much more effectively 
because now you're not trying to look at timestamps and go between different data sources, 
different platforms. So fast-forward two years, the estimates during the POC were not wrong. 
They were actually a little lower than what we're actually seeing right now. It also changed 
from adaptive metrics to Adaptive Telemetry. So every time Steve and his team turned something 
new on, I'm in there turning it on also. I'm like, "Yes, adaptive logs, sounds good. Adaptive 
profiles, sounds good. Keep turning on, keep turning on." Because as he was saying, there's 
so much data out there now. There's so much that doesn't matter because you can vibe code something 
and let's say you're really new into coding and your boss says, "Make me a microservice." So you 
go to your coding agent, make up a microservice, and he tells you, "Oh, we need telemetry." So 
you tell your agent, "Hey, I need telemetry." And your agent may or may not ask you, but then 
it just turns on auto instrumentation. So now you have everything in the world is turned on. 
So now you have metrics for things that don't matter. You have a whole bunch of 200 status code 
log lines coming out for things that don't matter. You have a bunch of traces from your Kubernetes 
readiness probes. Those don't matter either. But with Adaptive Telemetry, you can turn all 
those things off because those don't matter. So two years from now, or 2026 now, a couple months 
ago, my account executive came to me, he goes, "Do you realize how much money you're saving from 
Adaptive Telemetry?" I'm like, "No," because I've been busy looking at other dashboards and 
everything and other projects. So I came and looked at the cost management billing tab and I 
was like, "Wow, almost five million we've saved in the last year." How many people think saving 
five million a year is pretty good? Show of hands. All right. Yeah, I think a lot of people would 
like to save five million. I would actually like to save a lot less, but if you think about it, 
what Adaptive Telemetry shows you is what doesn't matter. So we're generating $5 million worth of 
stuff that doesn't matter, but it's really easy. Adaptive Telemetry, little check boxes, you 
can make it really easy to start saving a lot of money. The hard part is stopping all those 
signals from coming in. That takes time. You got to work with your development team. You have to 
analyze, but Adaptive Telemetry tells you what's not useful, what doesn't matter. And then you can 
take that information, go back to your development team saying, "Stop logging all this stuff. 
Stop tracing this stuff." And then you can keep shrinking that bill back down. I mean, I'd love 
to have that at zero, but it's not realistic. That would take forever. And customers of ours don't 
care that our Adaptive Telemetry bill is zero. So it's really hard to justify that much 
development effort to shrink that down. So here's what our Adaptive Telemetry looks like. 
Currently, this is a couple months ago. I was in the private preview for the auto apply and I 
was one of those scared customers because if you'll see here, the auto apply will increase 
my series by 480,000. That wasn't too bad. I think a couple weeks before this, the screenshot 
was like 2.5 million, which that's quite a bit if I just turned on auto apply. So I'm really 
excited about the cost management feature they just talked about. So I'm looking forward to 
getting back to work and turning on auto apply, turning on that cost management feature so that 
somebody can't just write a query and all of a sudden my bill goes up like $10,000 overnight 
because somebody wrote a query looking at pod level metrics. The other thing too is the toil of 
trying to keep this up to date and maintained. I remember one Saturday morning I was having some 
coffee and do what you normally do. You log into Grafana when you're having your coffee and you 
look at some of the legacy dashboards they have, it's a cost management dashboard, kind of shows 
you how many series are coming and everything. And I know on Friday it was about 30 million, 
but Saturday morning it was 40 million. So somewhere along the line, Friday afternoon, 
somebody decided to, yep, auto instrument, deploy and leave for the day. So I was able to 
actually really quickly go into adaptive metrics, find the metric that showed up, those 10 million 
series, click drop rule. I haven't heard from that person and it's been a year. So I mean whoever 
enabled it didn't need it. It would have cost us a lot of money, but because Grafana gives you 
a nice little window of opportunity every month to fix mistakes like that, I was actually able 
to save that 10 million series for that month. Here's an example of a rule. So this is one 
of the Adaptive Telemetry recommendations. You can see the analysis that it goes through. 
So it shows you, well, there's no alerts, there's one dashboard and three queries. But based 
on that analysis, you can see it recommends here's the type of aggregation you should do. Here's 
the labels you can just aggregate away and they shouldn't impact anything because nobody's queried 
on them. The dashboard's not referencing them. So enabling that just saves you money. So with the 
adaptive metrics saving us a lot of money, we also turned on the adaptive logs, adaptive traces. 
That was saving us a lot of money too, but we didn't just take that money and just put it in the 
bank and go, "Okay, we're good. We're just going to look at metrics and that's it. That's what we 
had two years ago." But that's not Observability looking at just one pillar of metrics and not 
metrics, but one pillar of Observability. So instead of going all the way back and 
saying, "Yep, our budgets dropped a lot," we did reduce our budget, but we kept some 
of that money and started looking into other things. So we started sending more logs 
in, we started sending more traces in. So here's some examples of our savings on logs. 
So that's not bad for an hour, we generated one terabyte of data, 1.1 terabyte, but we dropped 
1.02 of that. More noise that just doesn't matter. Tracing reduction, same thing, 90%. We enabled 
a lot of the features that they talked about. So the volumetric policies, the diversity policies, 
all that stuff. So as soon as they turn things on, I go in, turn them on because there's no sense 
of not turning them on because it's just going to save you money, which then you can invest 
into other things. Adaptive log patterns. So it goes through and analyzes. Here's all the data 
that's coming in. So here's a pattern of data that's a log that's coming in and query frequency 
never, which means not a single person has looked for this sequence of data. Drop 99% of it.
You don't want to drop 100% because then your developer's like, "Is my application working 
because nothing's coming in." So you still need a little bit coming in just to give them that 
nice warm, fuzzy feeling that application's still working and it's still logging. So 99, 99.9%, 
but you can still save a good amount of money. This is a drop rule. So this was something, 
so you don't got to wait for adaptive logs to go through and analyze your usage. So I was 
enabling some debug logs for an application and I knew it was going to generate a lot for 
this. I don't know if you guys can see it, but there's a log line in there that says 
framed. I didn't need that from the debug logs, but I knew it was going to generate a lot of 
logs. So I was able to go in and didn't have to wait for the adaptive log analysis.
I just created a drop rule going for this particular service, for the log level debug, 
if it has that line in it, just drop 99% of it. So that was 14 terabytes that I saved because 
preemptively I knew I didn't need that data. So all the savings we put into more Observability. 
So now we're expanding into our testing. We're doing some front end Observability stuff. We're 
using Grafana Assistant. So we're just getting more and more involved and more value out of 
our Observability dollar. This is from the Grafana playground. So this is synthetic 
testing. We don't know what it looks like. Hopefully you do, but it's pretty cool. You just 
write a little test and you say, "Send this out to three different countries and just run this 
and let me know how things look from those three different countries." And that's assuming 
yourself is publicly exposed. If it's not, sometimes you have stuff that's private and it's 
not exposed to the internet. They have private probes, so you can deploy a private probe into 
your environment and then you can run the test from there and inside your firewall, inside your 
platform, which is really nice. And then it just feeds the data back up to Grafana Cloud.
Front end Observability, for small price, just adding an SDK into Node.js, you get 
real user monitoring. So now you can start seeing what the user sees. So this is all just 
the statistics and metrics, but they've just recently enabled replay sessions. So now you can 
actually see what a customer is experiencing. So I was talking with our support manager and I was 
showing him the front end Observability and the Grafana Assistant. I'm like, "Hey, check this out. 
This is kind of cool. You can go in here because he's the support team." So they get calls from 
customers saying, "Hey, I'm on your website and I'm going down this certain path and it's not 
working." So before this, what he would do is, or their support engineers would, "Oh, can you 
send me a hard file?" How many people know what a hard file is? Now you got to explain, here's how 
you generate a hard file and submit this to us." But with this, now we've instrumented the front 
page. So now we hit a Grafana Assistant. I'm like, "Hey, let's analyze the website." He's like, 
"Wait, can we go back three days? Because three days ago we actually had a problem." So I'm 
like, "Sure. Grafana Assistant. Three days ago, was anything happening?" Turns away, turns away. 
"Yeah. Two different paths from your main website. We're having issues." He was like, "That's 
right." So he was just blown away. He didn't ask for a hard file. He didn't have to wait for 
five, 10, 15 customers to call in saying, "Hey, this particular path on our website is failing." 
So it was really great validation for that. It's onto Grafana Assistant. This is our best 
buddy now. I mean, there's so many people at Grafana at Rapid7 that are using this. I've had 
people reach out to me directly or in our public instant messengers just saying all the different 
ways they're using it and how happy they are using it. I have teams that are creating dashboards that 
don't know a query language, but they can go in, you just use natural language, create me a 
dashboard for X, Y, Z, or I see this alert. Can you analyze this alert and let me know what's 
happening? And you can see on the side of it's going through doing all this analysis that 
would take an engineer a lot longer to do. So this is a skill that I wrote. This is a 
cluster upgrade. So how many times when you go through and you upgrade something and somebody 
goes after the upgrade, "Well, it's broken or you broke my application," and you're like, "I'm 
pretty sure I didn't." Well, with the skill, what you can do is have a two part skill. So you 
run it before. So it takes a look at your cluster, your environment, goes through and looks at 
all the logs, all the metrics, all the trades, every data, all the data that's available, how 
many things are crashing, how many things are running? And then you perform your upgrade and 
then you run it again. And then it goes through and compares. Did anything new start crashing? 
Any performance differences? Anything like that? So now you have a really nice validation 
to go back to the team that you upgraded their cluster on and say, "It looks good 
before and after." And they're like, "Well, this is crashing now." And you're like, "Well, it 
was crashing before. I can't fix image not found. Upgrading the cluster is not going to fix that."
We've got teams that are actually creating their own skills. They send them to us and then we 
just add them in. So this has been really a lot of good usage out of it. This is Grafana Assistant 
analyzing alert. Alert pops up. What happened? So this is great for that one o'clock in the morning 
where the guy's having my ties and goes through and analyze it, looks at it. It's like, "Oh, your 
thing's getting oom killed." Oh, okay, that's an easy fix. But before that, without Assistant, 
you have to start going, finding the pod. Which cluster is it on? It just makes it so much easier 
because there's so much data there's access to. Here's a dashboard it built. One tip though, hit 
save. So when you're having an assistant making changes to your dashboard, hit save fairly 
often. 99% of the time it does a great job, but I've always run into very few little instances 
where it's like, oops, and then you have your dashboard's gone. So you have to go into version 
history, go back one, ask it the same prompt and then it does it correctly. So save often.
And if you notice the prompt there, you can see it on there. It's basically bring me a dashboard 
for this microservice in this namespace. There's no query language in there. This is a usage graph. 
So I was curious, I was looking through Grafana Cloud and I saw there's a usage underneath the 
Assistant. I've been using Assistant every day, using it a lot. I was expecting to be first 
person, second person. I was actually fifth and the top two people were three times as 
many as the third person. And I was like, "Wow, they're really using the heck out of 
this thing." And I looked at it, I didn't recognize either of their names.
So I looked them up and I'm like, "Wow, it's really interesting." It was two 
interns that we hired. So I reached out to them over instead. I'm like, "Hey, how are you 
finding Grafana Assistant?" And they're like, "It's fantastic. We just got out of university. 
We don't know anything about Grafana. We don't know anything about dashboards, alerts. We know 
nothing, but the first week that we're here, we've been creating dashboards. We've been helping 
our team investigate alerts and everything." So immediate onboarding benefit for people. So I was 
like, "Great, keep going." Because in my mind, it's more the middle senior people would 
be using Assistant. So I didn't even think that that is a great use case because you 
don't need to know a query language. I mean, how many universities teach query languages? 
It's not usually on the syllabus. So three things. Observe what matters. 
Adaptive Telemetry shows the opposite, shows you what doesn't matter. So leverage that. 
And Grafana Assistant, you'll see their little double star on every page. Click it, ask it 
questions. It knows the page you're on and it just keeps getting better and better and better. 
Thank you very much. Carl Eastman from Rapid7.

