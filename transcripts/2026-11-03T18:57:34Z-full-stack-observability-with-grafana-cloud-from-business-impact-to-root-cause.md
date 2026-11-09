# Full-Stack Observability with Grafana Cloud: From Business Impact to Root Cause

Published on 2026-11-03T18:57:34Z

## Description

How do you trace a dropped conversion or a checkout failure to its technical root cause? See how full-stack observability in ...

URL: https://www.youtube.com/watch?v=lPibSTdMfno

## Summary

The community call titled "Full-Stack Observability with Grafana Cloud: From Business Impact to Root Cause" was held on November 3, 2026, featuring Sarah, the product manager for Grafana Cloud's Knowledge Graph, and Jim, an engineer on the Knowledge Graph team. They discussed the importance of full-stack observability in tracing business impacts to root causes, emphasizing the role of Grafana Cloud's Knowledge Graph in managing and interpreting telemetry data. Key takeaways included the introduction of new monitoring capabilities for various cloud services, the ability to map custom business contexts onto the Knowledge Graph, and the enhanced efficiency of using the Knowledge Graph for root cause analysis, which significantly improved the success rate of identifying issues. 

Topics: Full-stack observability, Grafana Cloud, Knowledge Graph, telemetry, root cause analysis, monitoring capabilities.

## Chapters

00:00:00 Understanding full-stack observability with Grafana Cloud
00:05:40 Expanding observability coverage in Grafana Cloud
00:11:24 Exploring banking product entities and their performance
00:16:55 Using the Knowledge Graph for root cause analysis

Hello everyone. I'm Sarah, the product manager for Grafana Cloud's Knowledge Graph. 

Hi everyone, I'm Jim, an engineer on the Knowledge Graph team based here in Austin, Texas, in the US. We are super excited to be here today to show you how you can map from business impact to root cause with full-stack observability.

Before we dive in, let me share a bit about myself. I'm based in Lisbon, Portugal. You may have heard of Nazaré and Big Wave Surfing. I thought about it, but I've gone down a different path. I've decided to hone the expert skill of being a forever beginner surfer. So feel free to come chat with me about being a forever beginner at anything, or if you like surfing, that would be really cool.

Jim, how about you?

I'm a big motorsports fan, especially Formula One. Over the years, I've checked off a bucket list item by seeing the Belgian Grand Prix and enjoying the rain in the yard and forest there. I've also taken up the very affordable hobby of high-performance track days. And yes, I'm also going to be a forever beginner here.

Okay, so let's imagine Jim has just come out of a super-fast, shiny car, and I've just come out of an amazing forever beginner surf session. I didn't catch any waves, but I had a good time. Energized, we say, "Hey, why don't we launch that product we've been working on, the everyday checking product?" So we get the team together, push the big red launch button, and head out to celebrate. We high-five and throw some confetti because launching a product is something to celebrate. It takes work to get there.

However, many of you in this room know that at the time you launch a product, that's when some hard work really begins. Pretty soon, even during the celebration, there might be a killjoy in the corner—maybe it's a product manager who says, "Hey guys, does anybody know how the launch is going?" This can mean many things to many people. It could mean: Is anybody using the everyday checking product? Do they like it? Are they paying for it? It could also mean: Is the system we built holding up and supporting this product launch?

The funny thing is, those two things can be related. If a product is wildly successful, then maybe system performance is taking a hit. On the other hand, if system performance is struggling, then maybe the product isn't as wildly successful as it could be. So, it's important to be able to answer this question with these different perspectives in mind, but that can be difficult to do. When I look across my distributed system, how do I know which pods, which services, which databases? Is there an agent trampling around in my distributed system, right, across all these parts? How do I know which ones are rolling up to support the everyday checking product? And how do I know if they're doing a good job?

This problem isn't going away. In a survey this year, Flexera found that 94% of enterprises now use cloud services in some form. Gartner projects public cloud end-user spending to grow over 20% year-on-year. So, this kind of complexity problem isn't going away.

Now, you may notice over this image, there are some sparkly, colorful twinkles. I think they look a bit like some of the confetti from our celebration settling over our system, but actually, they're meant to illustrate all of the huge amounts of raw telemetry that a system is emitting. 

So, Jim, how about we just ask an agent to look through this raw telemetry and tell us how the product launch is going?

That sounds like a great idea. We have all the telemetry streaming off of our applications, and we have this business telemetry we've added. So, let's just ask the Assistant, "How is everyday checking going across the stack?" However, we don't have our business telemetry mapped into the Knowledge Graph yet, so it's going to try and just go through all the raw telemetry and see what it can find. It takes quite a while, but eventually, it comes up and says, "I couldn't find anything."

Now, we can have the agent keep digging, keep going through all the raw telemetry because that's what they're good at, but that's going to cost a lot of time and money in the form of tokens, and we can do better. 

In summary, re-deriving context from scratch burns tokens, it burns calories because you have to go back and forth with an agent, and it also introduces the chance of error. So, what if instead, when we ask a question like that, we could start from a shared context layer? That is the goal of full-stack observability, which is powered by Grafana Cloud's Knowledge Graph.

When you send your raw telemetry to Grafana Cloud, our observability solutions detect the part of your system for which they are specialists. They write those onto the Knowledge Graph as entities and also write relationships to other parts of the system that they detect. These solutions continuously monitor those parts for health, which could include changes to a dynamic baseline projected by machine learning algorithms or changing configurations. The solutions write their findings onto the graph as insights. 

The cool thing is this gets stored over time. You can say, "Hey, what was on my system yesterday? What was looking healthy or unhealthy? And how about today? What's changed versus yesterday?"

So, what's new? We've been extending the coverage of what's automatically monitored for our existing observability solutions. With database observability, Microsoft SQL servers are now automatically monitored. For infra and cloud observability, we've extended coverage of what's automatically monitored, whether you're using AWS, GCP, or Azure environments. To name a few of our popular entities in this space, we now have AWS RDS, Lambdas, and Azure Virtual Machines.

Beyond extending the solutions that already exist, we have also introduced brand new solutions mapping new kinds of things onto the graph. Thanks to agent observability, we now have agents being mapped onto the graph. This means that you can look at a rogue agent and have the context of all the parts of the system that it's interacting with. Thanks to frontend observability, we now have frontends being mapped onto the graph. With this, we're super excited about how it means you can traverse from a problem all the way to impacted end users. If you want to hear more about that, come along to our talk tomorrow focused on digital experience monitoring.

Thanks to synthetic monitoring, we now have synthetic checks also being written onto the graph. With this one, we're super excited about how you can have the context of a failing check when you're trying to investigate an issue with a backend service. Equally, if a check fails, you can more easily traverse to try and understand what's causing the problem.

Going beyond expanding our full-stack coverage, we have been focusing on how you can curate your context that's important to your business and write that onto the graph so that you can share it with your teams and agents. 

Firstly, you can now add your entities onto the graph. You can say, "This group of parts of my system rolls up to power the everyday checking product." You can do that by writing rules based on your raw telemetry that then map custom entities onto the graph, and that's supported to configure with Grafana Assistant.

Next up, you can add your service catalog onto the graph. You can do that using Grafana Service Center, which is a place where you can add your catalog and then link services that you define with things in Grafana like owning teams, run books, or on-call schedules.

Finally, you can add your lessons onto the Knowledge Graph. We've been testing this on our own production stack where we investigate an issue using...

**Grafana IRM and Knowledge Graph Overview**

We extract lessons from investigations that happen, focusing on aspects like hypotheses—whether they were true or false—and the actions we tried, noting whether they fixed the issue or not. This information is documented as operational context onto the Knowledge Graph. We're super excited about this, and if you want to hear more about it, please join us for tomorrow's talk on the new Grafana Cloud IRM.

We have been working to make the Knowledge Graph available as runtime context for agents. It's not trivial because there's a lot of information for an agent to understand and to get to the relevant context they're looking for. However, we've set up skills and tools that are yielding pretty good results, which I can discuss later.

To facilitate this, we've launched a new Cypher query tool that agents can use, wrapped in a specialized set of skills. Does anybody know what Cypher is? Cool! Cypher is the query language for graph databases, and it's really powerful because it allows agents to find exactly the context they're looking for in the Knowledge Graph. This is available with Grafana Assistant and also with your agents via gcx. It's also available with Grafana Assistant Investigations and in Private Preview.

**Product Launch Inquiry**

So, Jim, I think I stalled enough. Did you manage to figure out how the product launch went yet? Earlier, we asked that question, and it didn't find it right away. As Sarah mentioned, we can map our custom metrics to custom entities on the entity graph of the Knowledge Graph. Let's ask Assistant to map our products from the telemetry as a banking product. We want it identified by product code and let it do its work.

We have the Knowledge Graph mode here for the Assistant that helps you configure the Knowledge Graph. It will chug through and find a number of things, presenting you with some rules. You can refine them, and when you're okay with them, you can allow and apply them. After some time—I'm showing you this on screens because it takes a little while—it works well. It takes a few minutes, but we've discovered everyday checking, personal loan, and rainy day savings banking products within the system.

**Live Site Demonstration**

Now, let's take a look at that on a live site. Recall the earlier question we asked: how's everyday checking doing? Initially, it couldn't find it. Let's ask that again, but I also want to see business and system performance. 

As we start here, let's run that again. Perfect! While that's running, let's take a look at those entities we just mapped. Here are our banking product entities: personal loan, rainy day savings, and everyday checking. For each of these, we can check and see their connected entities and if they have any issues directly related to their connected services.

Sarah mentioned that agents are using Cypher to walk the graph. To assist the agents, we've exposed a schema that gives them the topology of the graph. Here are our new banking products, along with a visualization of the entities related to this specific graph. This provides the narrow focus that the agent needs for this data set. 

We have synthetic checks in there, the frontend, our products, the services they interact with, all the infrastructure, and even agents—all working for us here. In addition to this graph view, we have a new data source. Every stack has a Knowledge Graph data source that you can use, which will utilize Cypher queries. You can use the builder to start building your queries, and if you're a Cypher guru, you can directly write the Cypher.

**Querying Connected Entities**

Let's see here. I would like the Assistant to show me all the connected entities to my banking products, their connected services, and ignore the infrastructure and agents. The Cypher query gets generated for me. 

Here we have our banking products and all their connected services, and we can see everything else that's connected to them. From here, you can see the rings and insights on these different services. If you click on them, you can choose to go directly to the entity graph to continue investigating any possible issues. 

The nice thing about this being a data source is that you can also include it in any dashboard. I had an earlier query where I asked the Assistant to create a banking product overview dashboard with a mixture of business and system metrics. 

Here we see the topology again: our banking products, the services they call, and their backend databases. We can see the transaction history from a system level, and it looks like we've got a big bump here. We'll take a look at that in a bit, but we also see the business side of it—accounts opened, approval ratings, and all the business metrics from the custom metrics we reviewed. We also have these next to the system metrics, and we can see some latency increasing here.

**Investigating Everyday Checking**

In the meantime, let's see what the Assistant found when we asked about everyday checking. Recall that earlier it didn't find it, but now it says it's healthy. We see the business metrics around it, approval ratings, and system performance information. 

Because of the additional context we have, I want to follow up on those slower connections or transactions. I want to ask which database is servicing my everyday checking transactions. Since we've added that context to the graph, it knows which service to talk to and which databases are used by that service. 

Here we quickly see that the transactions are serviced by the MySQL database. Let's take a look at this new database fleet view that we'll be releasing soon. Here we have our MySQL database, and if we hover over it, we can see insights firing on it, including a missing index and some anomalies. Let's have the Assistant analyze that for us.

While that's running, we can see this fleet view gives you a nice overview of all the databases in your system that are having issues. You can see the ones with the highest errors, slowest instances, and even a bubble up of the queries causing the biggest issues. 

The Assistant has come back with a breakdown of this database. You have your timeline of system events happening here and a recommended next step. It looks like we had that missing index, so we need to create an index.

**Conclusion**

To summarize, we added context to the graph so the product was connected to the services. We asked the same question where earlier the Assistant didn't find anything, but this time it found it. Same telemetry, more context, better results. 

With that, back to you, Sarah. 

Thanks, Jim. Hopefully, this has shown you how you can spend less time rebuilding context and more time celebrating product launches, as well as asking important questions and figuring out the answers more quickly. I wanted to now run through a couple of proof points of where...

We've already seen the Knowledge Graph helping. Firstly, we talked to Neil from LexisNexis, who told us about a specific incident where the Knowledge Graph really came into its own and showed its value. He described when a latency alert fired, and the issue was actually caused a few hops down by an external vendor that was causing issues with their database. He said that without the Knowledge Graph, different people in the team would have had to kick off multiple investigations of different potential root causes. However, Grafana Assistant walked down entities and insights on the Knowledge Graph and figured out the root cause. He really called out that for him, this highlighted that when you add more kinds of context onto the Knowledge Graph, the value scales non-linearly.

We also spoke to more customers who had a lot of data on their Grafana Cloud stacks. They talked about this kind of problem a lot, where you have a signal, an issue firing here, but actually the cause is multiple hops away. They're complicated problems that sometimes take quite a lot of time to figure out what's going on. Our customers described how this often wouldn't be solved by one person; it would be solved by multiple people from multiple areas of expertise. You wouldn't expect one agent or a swarm of agents to be able to pinpoint the root cause in one shot.

So, we looked at our production stack and found an issue that looked like that. I would caveat that we picked this issue because we thought the Knowledge Graph would help. We set it up as an experiment. We basically had an agent running with [inaudible 00:20:13], and we gave access to Grafana via gcx. Then, we gave it the alert that initially fired and asked it to try and find the root cause. The results were really exciting. Without the Knowledge Graph, the agent found the root cause 1 out of 16 times, and with the Knowledge Graph, the agent found the root cause 15 out of 16 times. So, it's a really exciting sort of positive signal that we wanted to share.

Equally, we looked at Grafana Assistant Investigations and found that sometimes runs go in parallel, but they get to the same hypothesis root cause. However, sometimes the run uses the Knowledge Graph, and sometimes it doesn't. When we analyzed those pairs of runs that got to the same answer, we found that when the agent was using the Knowledge Graph, it was more efficient. It used fewer tokens and made fewer queries to raw telemetry. So, another really exciting positive signal that we wanted to share.

In summary, we're bringing more context onto the Knowledge Graph. Firstly, we're extending coverage across the full stack. Then, we're letting you add your business context onto the graph. Finally, we're making this available to agents, whether it's via Grafana Assistant or via your agents with gcx. We are really working to evolve the Knowledge Graph into a platform capability for Grafana. Every Grafana Cloud stack has a Knowledge Graph, and you can add your context there by sending your raw telemetry, adding your catalog, or sharing your lessons with Grafana Incident Response Management (IRM).

To get started, head over to Grafana Assistant and ask, "How can I get more from my Knowledge Graph?" Let us know how it goes. Thank you very much for listening.

## Raw YouTube Transcript

Hello everyone. I'm Sarah. I'm the product 
manager for Grafana Cloud's Knowledge Graph. Hi everyone. I'm Jim. I'm an engineer on the 
knowledge Graph team based here in Austin, Texas in the US. Not here, but in the US. We are super excited to get to be here today to show you how you can map from business impact 
to root cause with full-stack observability. So before we do that, some quick introductions. 
I'm based in Lisbon, in Portugal. You may have heard of Nazaré and Big Wave Surfing. I thought 
about it, but I've gone down a different path. I actually have decided to hone the expert 
skill of being a forever beginner surfer. So feel free to come chat to me about being a 
forever beginner anything, or if you like surfing, that would be really cool.
Jim? I'm a big motor sports fan, Formula One over the 
years, and this is me checking a bucket list item, seeing the Belgian Grand Prix and enjoying 
the rain in the yard and forest there. And I've also taken up the very affordable 
hobby of high-performance track days. And I'm also going to be a forever beginner here.
Okay. So let's imagine Jim has just come out of a super-fast, shiny car, and I've just come 
out of an amazing forever beginner surf session. Didn't catch any waves, but had a good time. 
And so we are so energized, we say, "Hey, why don't we launch that product we've been 
working on, the everyday checking product?" So we get the team together, we push the big 
red launch button and we head out to celebrate, right? We high five, we throw some confetti 
because it's true when you launch a product, it's something to celebrate. It takes work to get 
there. But likely, many of you in this room know that actually at the time that you launch a 
product, that's when some hard work really begins. Because pretty soon, even during the celebration, 
there might be some killjoy in the corner. Maybe it's a product manager who says, "Hey guys, 
does anybody know how the launch is going?" And this can mean many things to many people.
You could mean, is anybody using the everyday checking product? Do they like 
it? Are they paying for it? And you could also mean is the system we built 
holding up and supporting this product launch? And the funny thing is those two things can be 
related because if a product is wildly successful, then maybe system performance is taking a hit. 
And on the other side, if system performance is struggling, then maybe the product isn't 
as wildly successful as it could be. So it's important or it would be useful 
to be able to answer this question with these different perspectives in mind, 
but that can be difficult to do because when I look across my distributed system, how do I 
know which pods, which services, which databases? Is that an agent trampling around in my 
distributed system, right, across all these parts of my system? How do I know which ones are rolling 
up to support the everyday checking product? And how do I know if they're doing a good 
job? And this problem isn't going away. In a survey this year, Flexera found that 94% of 
enterprises now use cloud services in some form. And Gartner projects public cloud end user 
spending to grow over 20% year-on-year. So this kind of complexity problem isn't going away. Now 
you may notice over this image, there's some kind of sparkly, colorful twinkles. I think they look a 
bit like some of the confetti from our celebration settling over our system, but actually they're 
meant to illustrate all of the huge amounts of raw telemetry that a system is emitting.
So Jim, how about we just ask an agent to look through this raw telemetry and tell 
us how the product launch is going? That sounds like a great idea. So we have all 
the telemetry streaming off of our applications and we have this business telemetry we've 
added. So let's just ask the Assistant, how is everyday checking going across the stack? 
And we don't have our business telemetry mapped into the Knowledge Graph yet, so it's going to 
try and just go through all the raw telemetry and see what it can find. And it takes 
quite a while, but eventually, it comes up and says, "I couldn't find anything."
Now we can have the agent keep digging, keep going through all the raw telemetry 
because that's what they're good at, but that's going to cost a lot of time and money 
in the form of tokens and we can do better. Thanks. So in summary, re-deriving context from 
scratch burns tokens, it burns calories because you have to go back and forth with an agent, and 
it also introduces the chance of error. So what if instead when we ask a question like that, we 
could start from a shared context layer. And that is the goal of full-stack observability, which 
is powered by Grafana Cloud's Knowledge Graph. When you send your raw telemetry to Grafana Cloud, 
our observability solutions detects the part of your system for which they are a specialist 
and they write those onto the Knowledge Graph as entities and they also write relationships 
to other parts of the system that they detect. And then these solutions continuously monitor 
those parts for health. So that could be things like changes to a dynamic baseline, which are 
projected by machine learning algorithms to things like changing configuration. And the solutions 
write their findings onto the graph as insights. And the cool thing is this gets stored 
over time. So you can say, "Hey, what was on my system yesterday? What was looking 
healthy or unhealthy? And how about today? What's changed versus yesterday?" So what's new?
Well, we've been extending the coverage of what's automatically monitored for our 
existing observability solutions. So with database observability, Microsoft SQL 
servers are now automatically monitored. And for infra and cloud observability, we've 
extended coverage of what's automatically monitored, whether you're using AWS, GCP, 
or Azure environments. To name a few of our popular entities in this space, we now have 
AWS RDS, Lambdas, and Azure Virtual Machines. Now beyond extending the solutions that already 
exist, we have also got brand new solutions mapping brand new kinds of things onto the 
graph. So thanks to agent observability, we now have agents being mapped onto the graph. 
So this means that you can look at a rogue agent and have the context of all the parts of 
the system that it's interacting with. Thanks to frontend observability, we now 
have frontends being mapped onto the graph. And with this, we're super excited about 
how it means you can traverse from a problem all the way to impacted end users. And 
if you want to hear more about that, come along to our talk tomorrow focused 
on digital experience monitoring. And thanks to synthetic monitoring, we now have 
synthetic checks also being written onto the graph. With this one, we're super excited about 
how you can have the context of a failing check when you're trying to investigate an issue with 
a backend service. And equally, if a check fails, you can more easily traverse to try and 
understand what's causing the problem. Okay. So going beyond expanding 
our full stack coverage, we have been focusing on how you can curate 
your context that's important to your business and write that onto the graph so that you 
can share it with your teams and agents. Firstly, you can now add your entities 
onto the graph. So you can say, "This group of parts of my system, they roll 
up to power the everyday checking product." And you can do that by writing rules 
based on your raw telemetry that then map custom entities onto the graph and that's 
supported to configure with Grafana Assistant. Next up, you can add your service catalog onto 
the graph. You can do that using Grafana Service Center, which is a place that you can add your 
catalog and then you can link services that you define with things in Grafana like owning 
teams, run books or on-call schedules. And finally, you can add your lessons onto the 
Knowledge Graph. We've been testing this on our own production stack where we investigate an issue 
using Grafana IRM and then we extract lessons from that investigation that happened. So things 
like hypothesis, whether they were true or false, and also things that we tried and whether 
they fixed the issue or they didn't. And we take that and we write that as 
operational context onto the Knowledge Graph. We're super excited about this and 
if you want to hear more about it, then please come along to tomorrow's 
talk on the new Grafana Cloud IRM. We have been working to make the Knowledge 
Graph available as runtime context for agents. It's not trivial because it's quite 
a lot of information for an agent to understand and get to the relevant context 
that they're looking for, but we've got to kind of set up with skills and tools where we're 
getting pretty good results I can speak to later. So to get there, we've launched a new 
Cypher query tool, which agents can use, wrapped in a specialized set of skills. 
Does anybody know what Cypher is? Cool. Okay. Cypher is the query language for graph 
databases, and it's really cool because it gives agents the power to find exactly the context 
they're looking for in the Knowledge Graph. This is available with Grafana Assistant 
and also with your agents via gcx. It's also available with Grafana Assistant 
Investigations and Private Preview. Okay. So Jim, I think I stalled enough. Did you manage to figure out how 
the product launch went yet? So we saw earlier, we asked that question and it 
didn't find it right away. So as Sarah mentioned, we can map our custom metrics to custom entities 
on the entity graph, on the Knowledge Graph. So let's just go ask Assistant, have it map 
our products from the telemetry as a banking product. We want to have it identified by 
product code and let it go do its work. We have the Knowledge Graph mode here for the 
Assistant that helps you configure the Knowledge Graph and it will chug through and it finds 
a number of things and it'll present you with some rules. You can refine them and when you're 
okay with them, you can allow and apply them. And after some time, I'm showing you this is 
screens because this takes a little while. It's not really a good demo, but it works well. 
It takes a few minutes. But we've discovered everyday checking, personal loan and rainy day 
savings banking products within the system. So now let's take a look at 
that on a live site. All right. So you recall the earlier question we asked 
was how's everyday checking doing? And we got the fact that it couldn't find it. So let's ask 
that again, but I want to also see business and system performance.
Okay. So as we start here. All right, let's run that again. All right, perfect. So while that's running, let's 
go take a look at those entities we just mapped. So here's our banking product entities we 
see now, and we see we've got personal loan, we've got rainy day savings, 
we've got everyday checking. And for every one of these, we can 
check and see their connected entities. And we can see if they have some issues directly 
on the products to their connected services. Now Sarah mentioned that agents are using Cypher 
to walk the graph. So in order to help the agents, we've exposed a schema that gives them the 
topology of the graph. So you'll see here, here's our new banking products. And she also 
mentioned there's a lot of AWS entities and such, and this is a visualization of the entities 
related to this specific graph. So it gives you the narrow focus that the agent needs for this 
data set. So we've got synthetic checks in there, we've got the frontend, we've got our products, 
we've got the services it talks to, we've got all the infrastructure and we've even 
got agents all working for us here. So in addition to this graph view, we have a new data source. So here's something 
you're probably familiar with. So every stack has a Knowledge Graph data source 
that you can use and it will use Cypher queries. So you can use the builder. I'm sure you're 
familiar with the builders here and you can see you can start building your queries 
and there's our banking product, but you can also, if you're a Cypher guru, 
come in here and directly write the Cypher. But let's see here.
I would like to have the Assistant do it for me. So I'm going to 
ask the Assistant to show me all the connected entities to my banking products, their connected 
services and ignore the infrastructure and agents. So the Cypher query gets generated 
for me. Let's take a quick look here. So here we have our banking products and all their 
connected services and we can see down the line everything else that's connected 
to them. And from directly in here, you can see the rings, the insights on these 
different services. And if you click on them, you can choose to go directly to the entity graph 
to continue to investigate any possible issues. The nice thing about this being a data source 
is you can also include it in any dashboard. So I had an earlier query that I asked the Assistant 
to create me a banking product overview dashboard with a mixture of the business and the 
system. So here we see the topology again, there's our banking products, the services 
they call and their backend databases. And we can see the transaction history from 
a system level and it looks like we've got a big bump here. We'll take a look at that in a 
bit, but we also see the business side of it. We see the accounts opened, approval 
ratings, all the business metrics from all those custom metrics we looked. And we 
also have that next to these system metrics. And we can see we've got some latency increasing 
here. We'll look into that in a moment. But in the meantime, let's go see what the Assistant 
found when we asked about everyday checking. So you recall earlier it didn't find it, but now 
it's found everyday checking. It says it's healthy and we see we've got the business 
metrics around it, approval ratings, and we've got system performance information. 
And because of the additional context we have, I want to follow up on those slower connections 
or those slower transactions and take a look and see. I want to ask which database is 
servicing my everyday checking transactions. And because we've added that context to 
the graph, it knows that for that product, which service to talk to and see which 
databases are used by that service. And here we quickly see the transactions 
are serviced by the MySQL database. So let's go take a look over here at this new 
database fleet view that we'll be releasing soon. And here we have our MySQL database and if 
we hover over it, we can see we've got some insights firing on it. We've got a missing 
index. We've got some anomalies. Let's have the Assistant analyze that for us. All right. 
And while that's running, we can look and see this fleet view gives you a nice bubble 
up of all the databases in your system that are having some issues. You can see 
the ones with the highest errors, slowest instances. You can even see a bubble up of the 
queries that are causing you the biggest issue. So we can keep drilling in and take a look 
here. We've also got connection saturation. We've got weight events. And let's see. 
Here we go. And the Assistant has come back with a breakdown in this database here. So you 
have your timeline of system events happening here and you have a recommended next 
step. So it looks like we had that missing index, so it looks like 
we need to create an index. So to summarize, we added that context to 
the graph so the product was connected to the services. We asked that same question where 
earlier Assistant didn't find anything. This time it found it, same telemetry, more context, better 
results. And with that, back to you, Sarah. Right. Thanks Jim.
Hopefully that has shown you. I think the applause shows that this has shown you 
how you can spend less time rebuilding context and more time celebrating product launches 
and also asking the important questions and figuring out the answers more quickly.
I wanted to now run through a couple of proof points of where we've already seen the Knowledge 
Graph helping. Firstly, we talked to Neil from LexisNexis who told us about a specific 
incident where the Knowledge Graph really came into its own and showed its value. 
He described when a latency alert fired and the issue was actually caused a few hops 
down by an external vendor that was causing issues with their database. He said that without 
the Knowledge Graph, different people in the team would have had to kick off multiple investigations 
of different potential root causes, but Grafana Assistant walked down entities and insights on the 
Knowledge Graph and figured out the root cause. He really called out that 
for him, this highlighted when you add more kinds of context onto the 
Knowledge Graph, the value scales non-linearly. We also spoke to more customers that had a 
lot of data on their Grafana Cloud stacks and they talked about this kind of problem a lot 
where you have a signal, an issue firing here, but actually the cause is multiple hops away. 
They're complicated problems that sometimes take quite a lot of time to figure out what's going on. 
And we had our customers describing how this often wouldn't be solved by one person, it would be 
solved by multiple people from multiple expertise and you wouldn't expect one agent or a swarm of 
agents to be able to one shot to the root cause. So we looked on our production stack and 
we found an issue that looked like that. And I would caveat that we picked this issue 
because we thought the Knowledge Graph would help. So we set it up as an experiment. We basically had an agent running with [inaudible 
00:20:13] and we gave access to Grafana via gcx. And then we gave it the alert that initially fired 
and we asked it to try and find the root cause. And the results were really exciting. Without the 
Knowledge Graph, the agent found the root cause 1 out of 16 times and with the Knowledge 
Graph, the agent found the root cause 15 out of 16 times. So it's a really exciting sort 
of positive signal that we wanted to share. Equally, we looked at Grafana Assistant 
Investigations and we found sometimes runs go in parallel, but they get to the same 
hypothesis root cause. But sometimes the run uses the Knowledge Graph and sometimes it doesn't. 
And when we analyzed across those kind of pairs of runs that got to the same answer, we found that 
when the agent was using the Knowledge Graph, it was more efficient. It used less tokens 
and it made less queries to raw telemetry. So another really exciting positive 
signal that we wanted to share. Okay. So in summary, we're bringing more 
context onto the Knowledge Graph. Firstly, we're extending coverage across the full stack. Then we're letting you add your business 
context onto the graph. And finally, we're making this available to agents, whether it's via 
Grafana Assistant or via your agents with gcx. We are really working to evolve the Knowledge 
Graph into a platform capability for Grafana. So every Grafana Cloud stack has a Knowledge 
Graph and you can add your context there by sending your raw telemetry, adding your catalog, 
or sharing your lessons with Grafana IRM. To get started, head over to Grafana Assistant and 
ask, "How can I get more from my Knowledge Graph?" And let us know how it goes. Thank 
you very much for listening.

