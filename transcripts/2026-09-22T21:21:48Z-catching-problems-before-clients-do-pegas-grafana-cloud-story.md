# Catching problems before clients do: Pega&#39;s Grafana Cloud story

Published on 2026-09-22T21:21:48Z

## Description

Pega runs mission-critical case-management applications for telecom, healthcare, insurance, and government clients at ...

URL: https://www.youtube.com/watch?v=JamMORINPP8

## Summary

The community call titled "Catching problems before clients do: Pega's Grafana Cloud story" took place on September 22, 2026, featuring Satya Mishra, a product manager responsible for cloud infrastructure at Pega. The discussion centered around Pega's mission-critical case management applications and their integration with Grafana for monitoring and observability. Key topics included the use of Grafana dashboards to track application performance, the importance of observability in managing complex systems, and the lessons learned from their partnership with Grafana, such as the need for effective data management and access control. The call emphasized Pega's commitment to proactively resolving issues before clients are affected, leveraging advanced monitoring techniques and AI.

Topics: Pega, Grafana, observability, application performance, monitoring, AI integration.

## Chapters

00:00:00 Introduction to Pega and application building
00:07:07 Building a customer service application with Pega
00:18:11 Importance of monitoring and observability
00:20:41 Monitoring application performance and data management at Pega

Hello everyone. My name is **Satya Mishra**. I'm responsible for cloud infrastructure at **Pega**. So basically, I'm a product manager, which means my three favorite words are *what*, *why*, and *when*. My favorite phrase is, "it's on the roadmap." 

Today, I'm going to talk about what Pega is all about and how we have partnered with **Grafana**. We'll hopefully see some cool demos as well. I think the first question to answer is, *who is Pega?* At Pega, we strongly believe that the best way to answer this question is to look at our products and experience them. So how about we just look at it right away and understand what we are all about, right?

What we're going to do is build an application. You might be thinking, "We have 30 minutes and we want to build an application," but let's give it a try. You can do this yourself as well; you can head to [pega.com/blueprint](https://www.pega.com/blueprint) and start building your application too. You can build an application for a vertical of your choice—be it healthcare, telecommunications, pharmacy, insurance, you name the industry. But today, let's try and build an application for the communications industry. Let's select consumer B2C. I'm going to build an application for their customer service department.

At this point, if you have supporting assets for your app, you can just upload them. It could be your policies, an old application that you're trying to modernize, videos, training manuals—anything that you can find, just upload them. So I'm going to build a customer service application for communications. We are going to select a company called U+ Communication. Let me say US.

Pega has years and years of research and experience in building applications. So it's going through that research to understand what the best practices are for building an application for the customer service industry. Then we are reaching out to the internet to understand what other best practices are there. If you uploaded your proprietary documents in this process, we'll go through that as well. 

We came back with recommendations for the necessary processes that these applications should have. If you were to log into a telecommunications company, be it a brick-and-mortar store or online, you would see that they would have workflows like, "I want to upgrade my device," "I want to move the service," "I want to add mobile plans to retain my customer," or "I want to report something stolen." I could generate more workflows and I could also add my own workflows at this point. 

So let's see what it does and what it comes back with. It's going through and figuring out what the other best possible processes might be needed for an application like this. Okay, I'm just going to wait for something. 

It came back and said, "Yep, the customers might want to report network outages, upgrade a service, or apply for international roaming." So I hit next. Now it's detailing out who is going to act upon these workflows, how these workflows might be connected to each other, what different departments might be engaging with this workflow in this company, and what kind of roles might be needed to interact with the workflows. 

You can think of a process as a case in Pega, which arranges work in different stages and steps. For example, if you apply for a credit card, it goes through a set of stages and steps inside that company and might interact with other vendors and services. It might go through credit checks and look at what kind of discounts can be given to you. 

That's what it's trying to do—build out that process flow behind the scenes. It's almost there, and we are now going to shortly look at what those workflows look like. And by the way, this is all live. This is not a recorded session; this is actually happening from our production systems. 

So look at the upgrade device workflow. This is what the system recommended: you would go through various steps and stages, whether it's a trade-in or not, different recommendations, and whether you want to upsell. As you go through this process, this is what the contact center agent might be walking you through when you apply for this process at this company. 

Like this, you can add mobile devices. So there's a flow for that. You can change your plan; there's a flow for that. This looks good to me, and of course, I can add all my different steps or stages that I require right now. 

Now, the beauty of this workflow is that for every part of the process, I can connect with an API if I have to. I can assign this to a person, a bot, or a person in a different department. Everything is configurable here. So I'm just going to hit next. 

Now, each process requires not only to store the data about the process itself but also to act upon certain work objects. For example, you might have your data about your customers in a separate system. In this application, you can decide to store the data in our database, or you can say, "Okay, let me interact and connect the data to my own system." You can choose where the data resides. You can save your customer data or your account data in some other system, and we can understand that data model and interact with it.

Now, one last step. We need to figure out the personas that would be interacting with the application. If you have ever called into a telecommunications company, you know that there is a CSR, back office users, and billing specialists. Different personas work with this application. 

Then, this application needs to know what kind of channels to interact with. Do you want my customer to send emails? Yes. Do you want them to call? Yes. So I'm going to tick all those things that my application would need. Of course, I would need AI to understand what those messages are and what the voice interaction is. So I'm going to enable a bunch of products that our company offers.

And we are at the final step. Now we have generated what we call a blueprint of this application. I think you would like to see this application for real, right? It would be nice to see how it looks after going through this process. 

So this is how the application looks. This is what we built in the last five minutes. This is an application that is deployed for the U+ company, and it has all these different workflows that you can start. It has some test data in it. For example, if I want to move my service, I can just interact, feed the data, and then I want to transfer these services. This is a typical customer service application. 

I can move this process from one department to another, interacting with different people. This is what we do at Pega. We are in charge of mission-critical workloads, helping work get done faster and ensuring that the right people are connected to the right work. 

This application also comes with a lot of inbuilt dashboards. If you're a line manager in the contact center department, you can see what kind of cases are coming in the queue and what kind of work is happening. We can also extend this application to **Salesforce**. If you're using Salesforce in your company, then we can extend it there. 

If I deploy this application in a contact center agent, this is how the view would be. They would receive incoming calls, and it would understand the profile of the customer calling in and what they have. It's equipping the contact center agent with all the necessary details to act upon the customer's request. 

Now, any modern portal will have some sort of self-service. So this comes with the self-service as well where...

you would log into their portal as a customer and ask for changes. For example, in this case, I would upgrade my device. As a customer, I might log in and say, "Yeah, upgrade these devices that I have, select one of these options and start raising the case." So this is the self-service flow that is interacting with the application. And you don't have to build this separately; it all comes with what we just did. 

Yeah, like trade-in options. Now, the other thing that people might want to do with this kind of application is that they might want to connect with it using APIs. So it comes with interfaces that you can call directly from any third party or your own app as well. It also comes with guidance on how to connect to Cloud or ChatGPT. Additionally, it comes with an MCP server, so you can just start plugging in and connect with this now if you want. 

The other thing that it comes with is a conversational agent as well. So now you can have a chatbot that comes with it. You can start asking questions. For example, "What was my last transaction?" I was going to ask because I'm worried about my international trip and how much charge it costs. So maybe we come back with the answer, right? 

Okay, so I'm trying to add a line now. Let's say five lines. I think this is too much typing, so how about I just call them right away? 

Yeah, so I'm just going to make a call. 41997342. Please enter your voice preview code. 458414. Connecting to your blueprint voice preview. 

Hello. Thank you for calling U+ Comms. How may I assist you today? 

Yeah, I was hoping to add a line to my account. Can you do that for me? 

I'd be happy to help you add a line to your account. Could you please tell me the type of device you'd like to add, or are you interested in seeing available options? 

Absolutely. I can help you add a line to your account. May I know which device you'd like? 

Yeah, just add the Freedom 250 unlimited internet plan on my device. 

Thank you for choosing the Freedom 250 unlimited internet plan. Could you confirm how many lines you'd like to add with this plan? 

Five lines, please. 

Thank you for confirming you'd like to add five lines for the Freedom 250 unlimited internet plan. Can you confirm the device you'd like to select for these new lines? 

iPhone 17 Pro. 

I've added five lines with the Freedom 250 internet plan. And can you also update my address to 123 Mystic Street, Boston? 

You're welcome. To update your address, could you please provide the state and postal code for 123 Mystic Street, Boston? 

Yep. Massachusetts 02474. 

Thank you for confirming your new address as 123 Mystic Street, Boston. 

Thank you. Can you summarize what all you did for me in French? 

The answer: I don't know French, but can you summarize this in Spanish? 

Freedom 250 Internet Limitado and un iPhone. 

I'm going to... well, so that's who we are. That's what we do. I'm going to switch back to my slides, and this is real. This is not a recorded call. This is not a recorded demo. So I'm happy that it went well. 

So that's what we do. If you look at organizations today, what they do is they build software for different channels or different personas. They might have software for their web channel, for their Apple users, or for their web front end, and then they figure out how to connect all those software solutions, and usually, they struggle with it. 

But at Pega, what we do is the diamond at the center is the brain. So no matter the channel you come from, you're always getting the same connected experience. Whether it's mobile, coming from an iPad or tablet, using a phone, speaking to them, or going to the store, it's all going to the same workflow, which is the brain of a Pega app. 

So potentially, you could begin your journey through a phone call, follow it up on an email, or later ask your agents to follow through on what happened to your case. And that's the brain at the center, which is kind of mapping all the stages and steps. You don't have to bring in all your data to Pega; it can connect with wherever the data resides. It can understand the flow, model the connections, and work with that without any issues. 

Most likely, if you applied for a credit card, filed for a claim, or the doctor's office ordered a prescription, it went through a Pega application behind the scenes. So that's all our customers are there and their logos. A lot of analysts also recommend us as well over the years. 

Some statistics: being a product manager, I love numbers all the time. On average, we are processing billions of executions, creating billions of cases in Pega applications deployed worldwide. We have over three million users. Now we are deployed in both the AWS cloud and the GCP cloud. We operate in 45 regions worldwide and have over 24 compliance certifications like ISO and similar. 

Our infrastructure is massive: 10,000 plus instances, 150,000 plus pods. Behind the scenes, we build the whole cloud infrastructure. It runs in Kubernetes and has a lot of other technologies. We have our own control plane, security plane, and management plane, parameter security operations, antivirus, anti-malware—you name it, it's all part of the underlying infrastructure. 

What is important in this slide is that our customers who are Pega clients, the vision we have for all our customers is to focus on solving your business problems through building the apps, and the rest is managed by Pega. So you don't have to worry about it at all. 

From an architecture perspective, for folks who want to have a deeper dive into the technology of what we do, a very simplistic version looks something like this for one customer. We provision one dedicated VPC for a client. We have web nodes, batch nodes, decisioning, and the backing service kind of connect to various large language models for case attachments like invoices. We store them in file storage. We use Postgres as a database for storing all the transactional data. We use Elasticsearch and OpenSearch. We use Kafka and Cassandra for various streaming and summarizing tasks. 

Now, as simple as it looks like, this is not the real picture. It actually looks like this behind the scenes. Don't worry, I'm not going to go through all that, but I do want to point out that there's one key thing missing here. Guess what it is? 

It's right there. Yep. It's a trick question. It's monitoring and observability; that's why we are here. So we're going to talk about that next. 

How about we just quickly look at what Pega has done and what kind of dashboard we have implemented, right? I think that would be cool. 

So this is the last six hours of one of those systems that can power an application that you just saw, right? So I'm looking at this Apdex index. It's at 84%, and if I look at the last 30 minutes, the number's gone down. And it's a real system, so something's wrong with this system. 

By Apdex, I mean the application performance index; the true experience of the end user who is connected to this system is not having a good experience because most likely, I can see that a lot of their requests are 500s. So definitely, something's wrong. 

So how about we can just trigger an investigation real quick? For example, I... So let it run because it's going to take a while to understand what's happening. And by the way, this is one of the coolest features that our engineers use, site reliability or operations; that's the first thing they would do. 

So anyway, we can always, I'm sure, let this run in the background, but this is how a real dashboard for one of these environments looks like. What we have done is we have kind of taken all the data from the stack and sent this to Grafana so you can see the HTTP request response times. We also look at the failed ones.

Particular API or URL is the problem or is causing the problem. So I can do that too, like which URL paths or which API requests are failing, how much time they're taking. We also measure the Tomcat behind the scenes and how the Tomcat traffic is looking at, busy threads, errors, everything's out here. 

Then we also kind of pull in the data of the health of those tiers that I saw on the web tiers or the batch processing tiers, so it has all that data as well. We also pull in the data for the background processing. How are the background processing nodes working? Are they able to meet the SLA of our customers or not? And all the processes, the work they have scheduled, right? So we monitor that as well. 

Then we also look at the database because the application is interacting with the database. We check how the queries are doing, how the database CPU is performing, the throughput, and digitalization. We do all that. We also put all the log data in place to understand if there's a problem and how we can troubleshoot that. 

So yeah, that is just one of the dashboards, and hopefully by now the Assistant would have come back with an answer on what is happening. This analysis would look like, which is kind of pretty cool and helps pinpoint where the problem is. For Pega, I think it's very important that we are able to resolve these problems in very quick succession. Most likely, a team would be working at it right now, looking at what's happening.

Okay, coming back to the slides again. Here are some numbers on how Pega has used Grafana. We have over 1,600 users in various roles: SRE, operations, client-facing field teams. As I just said, we monitor over 10,000 clusters. They have probably 150,000 parts. We ingest 120 terabytes of data every month and over 130 million active metric series.

Now, some learnings that we have had in the last five or six years of this partnership with Grafana: when we started this journey, we only had metrics, but now we are seeing the power of having logs and traces in there. That's one. The second is having data for the entire stack. We have our networking data, ALB data, ALB traffic data, HTTP monitoring data, database, Kafka, and Cassandra data feeding into it. We also have the Kubernetes health data coming in. 

Having all this in one place helps. Essentially, if you look at it in a way, you're solving a cardinal problem. You have various signals coming from the stack, and if lower levels of the stack are a problem, it will start reflecting on the upper layers of the stack. You don't want those signals getting assigned to different people trying to solve the same problem. You'd rather want to assign all that to one person and let that person solve the problem. If that problem is repeating across thousands of clusters, you don't want a thousand people engaged to solve the same problem. 

So I think that's what we are trying to figure out as well: what's the best way to manage the cardinality and keep the cost down. We are huge fans of the Adaptive Metrics and Logs; that has really worked out well for us to reduce costs. 

Another thing that happened at Pega was that the moment this was accessible to people, guess what happened? I was sitting with 2,000+ dashboards. We don't want that. We want the ones that our team produces with the right correlation and the right meaning. Of course, we allow people to create their own dashboards, but we also publish the ones that we use for RCAs or SLAs. Those are the ones that we don't allow people to touch or mess with. 

We have strict guardrails around who can change from an administrative perspective, like what gets ingested. When it was open, we suddenly found that people changed what gets ingested, and suddenly tomorrow the cost is very high. So yeah, we operate responsibly. 

Another thing is that the logs might contain PII data. Having some sort of access control really works because, as per our compliance regulations, not everybody should have access to the logs and data. It's highly regulated because we have, as I just mentioned, so many different types of regulations, including deploying applications within the government cloud, the FedRAMP space. So it's very tightly regulated in terms of access control.

Now, some of the projects that we are working on right now: just like any other company, there's an uptick of all the AI agents. We are trying to figure out how we can monitor them efficiently and make sure that the agents are performant, that they are not being misused, and what kind of tokens they're consuming. This is all in progress right now. 

We also want to improve upon our signal-to-noise ratio. There's so much data that we are collecting. We want to reach a state where, for 100% of the time that we can, we can detect a problem before a client does. Right now, I would say that we have reached at least 40-50% of that state, and we are constantly improving on that front. 

It's on my roadmap to produce the SLA reports for our clients in an automated fashion. For any other company, SLA reports are usually used for issuing credits back if you have not met the SLA. We want to be as transparent as possible to our customers and give out these SLA reports. Obviously, it has to be backed by a lot of credible information about why a problem happened and who is responsible for initiating those credits. This is our project for this year as well.

## Raw YouTube Transcript

Hello everyone. My name is Satya Mishra. I'm responsible for cloud
infrastructure at Pega. So basically I'm a product manager, which means my three favorite
words are what, why, and when. And my favorite phrase
is, it's on the roadmap. So today I'm going to talk
about what Pega is all about and how we have partnered with Grafana. We'll hopefully see
some cool demos as well. I think the first question to
answer is who is Pega? And at Pega, we strongly believe that the
best way to answer this question is to look at our products
and experience them. So how about we just look at it
right away and understand what we are all about, right? So what we're going to do is we're going
to build an application and you might be thinking we have 30 minutes and
we want to build an application, but let's give it a try. You
can do this yourself as well. You can head to pega.com/blueprint and start
building your application as well. So you can build an application for a
vertical of your choice, be it healthcare, be it telecommunications, be it pharmacy,
insurance, you name the industry. But today let's try and
build an application for
the communications industry. Let's select consumer B2C. I'm going to build an application for
their customer service department. At this point, if you have
supporting assets for your app, you can just upload them.
It could be your policies. It could be an old application
that you're trying to modernize. It could be videos, training
manuals, anything that you can find, just upload them. So I'm going to build a customer
service for communications. We are going to select a company
that's a U+ communication. Let me say US. So at this point, Pega has years and years of research
and experience in building applications. So it's going through that research to
understand what are the best practices to build an application for the
customer service industry. Then we are reaching out to the internet
to understanding what other best practices are there. If you uploaded your
proprietary documents in this process, we'll go through that as well. And we came back with recommending these
are the necessary processes that these applications should have. If you would have logged into
telecommunications company, be it a brick and mortar store or online, you will see that they would
have these workflows of, I want to upgrade my device,
I want to move the service, I want to add mobile plans
to retain my customer, I want to report something stolen.
I could generate more workflows and I could also add my own
workflows at this point. So let's see what it does
and it comes back with. So it's kind of going through and
figuring out that what are the other best possible processes that might be
needed for an application like this. Okay. I'm just going to wait
for something. Okay. So it
came back and said, yep, the customers might want
to report network outages. They might want to upgrade a service. They might want to apply for
international roaming. So hit next. Now it's kind of detailing out who
is going to act upon these workflows, how these workflows might
be connected to each other, what are the different departments might
be engaging with this workflow in this company and what kind of roles
I might be needed to interact with the workflows. So you
can think of a process as a case in Pega, which kind of arranges work
in different stages and steps. So if you apply for,
let's say a credit card, it goes through set of stages and
steps inside that company and it might interact with other vendors,
other services. It might
go through credit checks. It might go for looking at what kind of
discounts it can be given to you. So that's what it's trying to do. It's trying to build out that process
flow behind the scenes and it's almost there and we are now going to shortly
look at what those workflows looks like. And between, this is all live.
This is not a recorded one. This is actually happening
from our production systems. So look at the upgrade device workflow. This is what the system recommended that
you would go through various steps and stages to whether it's a trade in
or not, different recommendations, do you want to upsell? So as
you go through this process, this is what the contact center agent
might be walking you through when you go and apply for this
process at this company. And like this, you can add mobile
devices. So there's a flow for that. You can change your plan. So
there's a flow for that. So yeah, this looks good to me. And of course I can add all my
different steps or stages that I require right now. Now the beauty of this workflow is
that for every part of the process, I can connect with an API if I have to.
I can assign this to a person. I can assign to this to a bot. I can assign this to a person
in a different department. So everything is configurable here.
So I'm just going to hit next. Now, each process requires that not only
stores the data about the process itself, but also it needs to act upon
certain work objects. So for example, you might have your data about your
customers in a separate system. So in this application, you can decide to store
the data in our database or you can say, okay, let me interact and connect the data to my own system. So you can
choose where the data resides. So you can save your customer data or
your account data in some other system and we can understand that data
model and interact with it. Now, one last step. Now we need to figure out the personas
that would be interacting with the application. So if you have ever called
into a telecommunications company, you know that it has a CSR,
there might be back office users, there might be billing specialists. So different personas work
with this application. And then this application, what kind of channels to
interact with my application? Do you want my customer to send emails?
Yes. Do you want them to call? Yes. So I'm going to tick on all those
things that my application would need. And of course, I would need AI to
understand what those messages are, what is the voice interaction happening. So I'm going to just enable a bunch
of products that our company offers. And we are the final step. So now we have generated what we call
as a blueprint of this application. I think you would like to see
this application for real, right? It would be otherwise we
went through this process. So it's nice to see this
application, how it looks like. So this is how the application looks like. This is what we built in
the last five minutes. This is an application that is deployed
for the Uplus company and it has all this different workflows
that you can start. It has some test data into it. So for
example, I want to move my service. I can just interact and then I can
feed the data and then I want to transfer these services. Typical customer service application. And I can move this process
from one department or interacting with different people in this. And this is what we do at Pega. We are
in charge of mission critical workloads and help work done faster, make sure that the right people
are connected to the right work. And this is all about it. I can add mobile devices. Now, this application also comes with
a lot of inbuilt dashboards. So you can see that if you're a line
manager in the contact center department, you can see what kind of cases
are coming in in the queue, what kind of work is happening. Now, if we can extend this
application to Salesforce as well. So if you're using Salesforce in your
company, then we can extend it there. If I deploy this application
in a contact center agent, this is how the view would be. They've
been coming call and you saw that, right? And it would understand what is the
profile of the customer calling in, what they have. And it's kind of equipping the contact
center agent with all the necessary details to action upon the
customer's request. Now, any modern portal will have
some sort of a cell service. So this comes with the self-service
as well where you would log into their portal as a customer and ask for changes.
For example, in this case, I would upgrade my device. As a
customer, I might log in and say, "Yeah, upgrade these devices that
I have, select one of these options and start raising the case."
So this is the self-service flow that is interacting with the application. And you don't have to build
this separately. It all
comes with what we just did. Yeah, like trade in options. Now, the other thing that people might want
to do with this kind of application is that they might want to
connect with it using APIs. So it comes with interfaces that you
can call directly from any third party or your own app as well. And then it also comes with on how
to connect to Cloud or ChatGPT. So it also comes with an MCP server. So you can just start plugging in and you
can connect with this now if you want. The other thing that it comes with
is a conversational agent as well. So now you can have a chat bot comes
with it. You can start asking questions. So for example, what was my last. I was going to ask because I'm worried
about my international trip and how much charge it costs. So maybe we
come back with the answer, right? Okay. So I'm trying to add a line
now. So let's say five lines. I think this is too much typing. So
how about I just call them right away? Yeah. So I'm just going to make a call. 41997342. Please enter your voice preview code. 458414. Connecting to your blueprint
voice preview. Hello. Thank you for calling U+ Comms.
How may I assist you today? Yeah, I was hoping to add a line to
my account. Can you do that for me? I'd be happy to help you
add a line to your account. Could you please tell me the type of
device you'd like to add or are you interested in seeing
available options? Absolutely. I can help you add a line to your
account. May I know which device you'd. Like? Yeah, just add the Freedom 250
unlimited internet plan on my device. Thank you for choosing the Freedom
250 unlimited internet plan. Could you confirm how many lines
you'd like to add with this plan? Five lines, please. Thank you for confirming you'd like
to add five lines for the Freedom 250 unlimited internet plan. Can you confirm the device you'd
like to select for these new lines? IPhone 17 Pro. I've added five lines with the
Freedom 250 internet plan. And. Can you also update my address
to 123 Mystic Street, Boston? You're welcome. To update your address, could you please provide the state
and postal code for 123 Mystic Street, Boston? Yep. Massachusetts 02474. Thank you for confirming your new
address as 123 Mystic Street Boston. Thank you. Can you. Summarize what all you
did for me in French? The answer. I. Don't know French, but. Can you. Summarize this in Spanish. Freedom 250 Internet
Limitado and un iPhone. I'm going to. Well, so that's
who we are. That's what we do. I'm going to switch back to
my slides and this is real. This is not a recorded call.
This is not a recorded demo. So I'm happy that it went well. So that's what we do. If you look at organizations
today, what they do is they build a software for different
channels or different personas. They might have a software
for their web channel. They might have a software
for their Apple users. They might have a software for their web
front end and then they figure out how to connect all those softwares and usually
they struggle with it. But at Pega, what we do is the diamond
at the center is the brain. So no matter the channel you come from, you're always getting the same connected
experience. No matter it's mobile, it's coming from an iPad or tablet or
using a phone or you're speaking to them or you're going to the store.
It's all going to the same workflow, which is the brain of a Pega app. So potentially you could begin
your journey through a phone call, follow it up on an email or later ask
your agents to follow through on what happened to your case. And
that's the brain at the center, which is kind of mapping
all the stages and steps. And you don't have to bring
in all your data to a Pega. It can connect with wherever the data
resides. It can understand the flow. It can understand and it can model the
connections and it can work with that without any issues. So most likely if you applied for
a credit card or filed for a claim or the doctor's office
ordered a prescription, most likely it went through a Pega's
application behind the scenes. So that's all our customers
are there and their logos. A lot of analysts also recommend
us as well over the years. Some statistics, being a product
manager, I love numbers all the time. So on average, we are processing billions of executions, creating billions of cases in Pega
applications deployed worldwide. We have over three million users. Now we are deployed in both the
AWS cloud and the GCP cloud. So we operate on 45 regions worldwide, have over 24 compliance certifications
like the ISO and similar. Our infrastructure is massive,
10,000 plus instances, 150,000 plus pods. Behind the scenes, we build
the whole cloud infrastructure. It runs in Kubernetes and it
has a lot of other technologies. We have our own control plane,
security plane and management plane, parameter security operations, antivirus,
anti-malware, you name the thing, it's all part of the
underlying infrastructure. What is important in this slide is that
our customers who are Pega clients, the vision that we have for all our
customers is that focus on solving your business problems through building
the apps and rest everything is managed by Pega. So you don't have
to worry about it at all. So that's what this slide
is telling essentially. From an architecture perspective, for folks who want to have more deeper
dive into the technology of what we do, a very simplistic version looks
something like this for one customer. So we provision one
dedicated VPC for a client. We have web nodes, batch nodes, decisioning and the backing service kind
of connect to various large language models for case attachments like invoices. We store them in file storage. We use Postgres as database for
storing all the transactional data. We use Elasticsearch and OpenSearch. We use Kafka and Cassandra for various
streaming and summarizing things. Now, as simple as it looks like,
this is not the real picture. It actually looks like this
behind the scenes. Don't worry, I'm not going to go through all that, but I do want to point out that there's
one key thing missing here. Guess what it is? It's right there. Yep. It's a trick question. It's
monitoring and observability, that's why we are here. So we're
going to talk about that next. How about we just quickly look at what
Pega has done and what kind of dashboard we have implemented, right?
I think that would be cool. So this is the last six
hours of one of those systems that can power an application
that you just saw, right? So I'm looking at this
Apdex index. It's at 84% and if I look at the last 30
minutes, the number's gone down. And it's a real system. So something's
wrong with this system. By Apdex, I mean the application performance index, the true experience of the end user
who is connected to this system is not having a good experience
because most likely I can see that a lot of their requests are 500s. So definitely something's wrong. So how about we can just trigger a
investigation real quick? So for example, I. So let it run because it's going to take
a while to understand what's happening. And by the way, this is one of the most
coolest features that our engineers use, site reliability or operations, that's
the first thing that they would do. So anyway, we can always, I'm sure,
let this run in the background, but this is how a real dashboard for
one of these environment looks like. What we have done is we have kind of
taken all the data from the stack and kind of sending this to Grafana
so you can see that the HTTP request response times. We also
kind of look at the failed ones. I actually can know which
particular API or URL is the problem or is causing the
problem. So I can do that too, like which UL paths or which
API requests are failing, how much time they're taking. We also
measure the Tomcat behind the scenes and how is the Tomcat traffic
looking at, busy threads, errors, everything's out here. Then
we also kind of pull in the data of the. So if you look at the health of those
tiers that I saw on the web tiers or the batch processing tiers, so
it has all that data as well. Then we also kind of pull in the data for the background processing. So how is
the background processing nodes working? Are they able to meet the SLA of our
customers or not? And all the processes, the work they have scheduled,
right? So we monitor that as well. Then we also look at the database because
the application is interacting with the database and how the query is
doing, how is the database CPU, the throughput, digitalization.
So we do all that. And then we also put all the log data
as well to understand if there's a problem, how we can
troubleshoot that. So yeah, that is just one of the dashboards
and hopefully by now the Assistant would have come back with an
answer on what is happening. And maybe I can. So basically this
analysis would look like, which is kind of pretty cool and kind
of helps pinpoint where the problem is. For Pega, I think it's very important that we are
able to resolve these problems in very quick succession. So most likely a team would be working
at it right now looking at what's happening. Okay. Coming
back to the slides again. So some numbers of how
Pega has used Grafana. We have over 1600 users in
various roles, SRE operations, client facing field teams. As I just said, we monitor over 10,000 clusters. They have probably 150,000 parts. We kind of ingest 120
terabytes of data every month and over 130 million active
metric cities for the. Now, some learnings that we have in
the last five or six years of this partnership with Grafana, I would
say that when we started this journey, we only had metrics, but now we are seeing the power by
having logs and traces in there. So that's one. And the second is have the data for the entire stack.
We have our networking data, ALB data, ALB traffic data. We have our HTTP
monitoring data. We have our database, Kafka, Cassandra data feeding into it. We have the Kubernetes health
data coming in from as well. So having all this at one place
kind of helps. Essentially, if you look at it in a way, you're
solving a cardinal problem, right? You have various signals
coming from the stack, and if lower levels of
the stack is a problem, it will start reflecting on
the upper layers of the stack. And you don't want those signals
getting assigned to different people trying to solve the same problem. You'd rather want to assign
all that to one person and let that person solve all that problem. And then if that problem is repeating
across thousands of clusters, you don't want a thousand people
engaged to solve the same problem. So I think that's what we are
trying to figure out as well, that what's the best way to manage the
cardinality and keep the cost down as well through that. And I think we are
a huge fan of the Adaptive Metrics and Logs. That has really worked out
well for us to reduce the costs. The other thing that happened at Pega was
that the moment this was accessible to people, guess what happened? I was
sitting with 2000 plus dashboards. So we don't want that. So we would want the ones that
our team produces with the right correlation, the right meaning. So of course we allow people
to create their own dashboards, but then we also publish the ones that we use for RCAs or SLAs. So those are the ones that we don't
allow people to touch with or mess with. But yeah, we have strict guardrails around
who can change from an administrative perspective, like what gets ingested because when it
was open and then you suddenly find that people change what gets ingested and
suddenly tomorrow the cost is very high. So yeah, we operate responsibly. And another thing is the
logs might contain PII data. So having some sort of an access
control really works because as per our compliance regulations, not everybody
should have access to the logs and data. So it's highly regulated because
we have, as I just mentioned, so many different types of regulations
and including we also deploy applications within the government
cloud, the FedRAMP space. So it's very tightly regulated
in terms of access control. And then some of the projects that we
are working at right now, so we are, as you can see that just
like any other company, there's an uptick of all the AI agents. So now we are trying to figure out how
we can monitor them efficiently and make sure that the agents are performant,
they are not being misused, what kind of tokens they're consuming. So this is all in progress right now.
We also want to improve upon our signal to noise ratio. There's so much
data that we are collecting. We want to really reach a state where
for 100% of the time that we can, can we detect a problem
before a client do. So right now I would say that
we have reached at least 40, 50% of that state and we are improving
constantly on that front. And it's on my roadmap to produce
the SLA reports for our clients in an automated fashion.
For any other company, SLA reports is usually used for
issuing credits back if you have not met the SLA. So we want to be as
transparent as possible to our customers, give out these SLA reports. And obviously it has to be backed by
a lot of credible information that why a problem happened and then who's
responsible for initiating those credits. So this is our project
for this year as well.

