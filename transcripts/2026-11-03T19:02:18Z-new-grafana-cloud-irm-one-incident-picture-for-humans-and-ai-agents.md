# New Grafana Cloud IRM: One Incident Picture for Humans and AI Agents

Published on 2026-11-03T19:02:18Z

## Description

When responders and their AI agents all investigate an incident at the same time, findings get stuck in separate chat windows.

URL: https://www.youtube.com/watch?v=ItF3wgpLDGo

## Summary

The show "New Grafana Cloud IRM: One Incident Picture for Humans and AI Agents" aired on November 3, 2026, featuring Mimi, a Senior Engineering Manager, and Michael Wettick, the Product Manager for IRM at Grafana. They discussed the challenges of incident management, particularly the need for better collaboration between human responders and AI agents during incidents. Key features introduced include Grafana Workflows, which automates incident processes, the new IRM response console for centralized incident information, and operational context using Grafana's knowledge graph to connect past incidents with current investigations. The overarching goal is to enhance teamwork and knowledge retention during incident responses.

Topics: Grafana Cloud, incident management, Grafana Workflows, IRM response console, operational context.

## Chapters

00:00:00 The challenges of incident response collaboration
00:06:21 Integrating incident response with Grafana tools
00:12:41 Incident investigation and collaboration using Grafana IRM
00:18:19 Incident response and post-incident review process

All right. Hi everyone. Thanks so much for being here. I'm Mimi. I'm a senior engineering manager with Grafana IRM. I've been a responder, a commander, and led incident management trainings at previous roles, and now I get to build the tools. Outside of work, I live here in San Francisco with my husband and our son. When I have free time, I'm often scrolling through Zillow, so please ask me about the homes I'm never going to buy.

Yeah. I'm Michael Wettick. I'm the product manager for IRM. I'm a very simple man. I like incidents, I like ice cream, and I like the greatest city in the world, Pittsburgh, Pennsylvania, where I live with my wife and son. My background is that I spent most of my career in engineering as an IC and an engineering manager, and then someone tricked me into a product role. So that's where I find myself now.

I always hate when I'm in the crowd and somebody does a raise-your-hand thing. So, who here is aware that Grafana has an incident management product? *Raise your hand.* Okay, this is pretty good. That's most of you. And for those of you that didn't, we do, and we've been incredibly busy the last couple of years building this end-to-end incident management platform. I'm really fortunate that every week I get to talk to companies that are migrating from a competitor, and it's sometimes a couple of teams up to thousands of on-call engineers. Especially if you're already using Grafana Cloud, it just makes so much sense. So stop by our booth. I think there's a promotion. Mimi is going to personally migrate anyone that shows up today and commits to make that switch. Just kidding! But yeah, see us at the booth.

Okay, one more question. Who here is using LLMs to help investigate during incidents? *All right.* And then leave your hand up if you're then finding yourself copying and pasting things out of Claude into the incident channel. *Yeah.* Yeah, that's what we thought. One slide too many.

So, a lot of you are already investigating incidents with agents, and you're often finding yourself manually sharing that information with your team. Incident response is changing as people and agents investigate together. I could be working with Claude, Michael with Cursor, somebody else with Grafana Assistant. We're all making progress and we're all moving a lot faster, but are we actually moving together? Keeping everyone up to speed has always been hard. The rest of the team doesn't necessarily know what you're doing. So we still have to stop and share: What have you checked? What have you ruled out? What are you planning to do next? If you've just joined the incident, you need the answers to a lot of those questions before you can even step in and help.

Sharing means recognizing what matters and remembering to tell each other. That takes judgment. Sometimes what I think is unimportant is exactly what you needed to know. Agents are helping us do a lot more, but we still have to bring that information back to the team. 

Let's take this incident, for example. A common question that comes up is, "Could it be the deploy?" I'm checking with Claude, Michael's working with Cursor, and somebody else is with Grafana Assistant. I've ruled it out, but that answer stays in my conversation. Michael and the assistant are still working on that. Then Alex joins, and he thinks he's seen something like this before, but he still needs to get caught up. We're actively making progress, but Alex can't see where the investigation stands.

Yeah, so this is a real pain point Mimi's describing, and I think it exposes a gap in the observability space overall. As an industry, we have an overly narrow view or definition of what the system is when we think about understanding our system. We have all these great tools to see what's happening in the technical part, but that isn't enough. 

This is the part of the system we spend a lot of time looking at. We have our services and our databases and the dependencies between them, and we have all this metrics, logs, traces, telemetry to understand what's happening, but these signals still need someone to interpret them. If there's a dashboard showing latency going up, someone has to figure out what that means, what to do next, and what to do about it. 

So this is the whole system: the rest of the system. You all, the people in the room, you engineers and your expertise, bring that every day to keep the system running. You're diagnosing, troubleshooting, inferring, and anticipating other problems, and you're learning how the system actually behaves versus how you think it behaves. All of this is super valuable knowledge to the next person, the next incident, your colleagues, and the other people in the incident, but most of it isn't captured and just vanishes when the incident is over. 

We obviously can't look directly inside your head and pull this out, but there are signals that are left behind. We can see the things you do and say as you work. These are the signals of response itself: the conversations you're having with each other, the conversations you're having with your agents, the queries you're running, how you're using Grafana Cloud, who you're asking for help, which teams and which people you're pulling in, and the mitigations you apply to the system. 

With the new IRM, we're bringing together all of this data from both people and agents and Slack to have this shared picture as a response unfolds. The goal is just to surface this, making it visible like all other observability data.

So we have three announcements today. One is Grafana Workflows, which is a new product going public preview. That's in your stack today, and we'll talk about it in a second, as well as the new IRM response console and operational context on the knowledge graph, which is in private preview. We'll have a sign-up QR code at the end.

So, Workflows: any kind of process you have, and today we're talking about incidents. Think about specifically around an incident. Any kind of process you have, you can turn into automation and take that toil off the responders during an incident at the beginning of the incident. These can react to events, which we'll see. They can be run manually in the web UI or via API. We have a series of built-in actions, and you can run code and call third-party systems. You can build these with agents, you can build them in the web, and we have a bunch of prebuilt blueprints as well. The goal is just to handle that toil so you can focus on the investigation during the incident.

Yeah, so if Workflows is helping get your response organized, the response console is bringing your investigation together. Let's go back to Alex. He was joining while we were all working with different agents, and he needed to get caught up. Oftentimes today, that really means scrolling through Slack or DMing one of your colleagues, and that ultimately pulls them out of the investigation. You might also find yourself just starting from scratch and duplicating the work of your teammates. 

These are the questions that we're trying to answer for Alex. Here's an example from the incident we're going to show shortly. I can see that customers are reporting duplicate payments. I can see that we've confirmed that the duplicate payments are true. I can see that someone's actively investigating the front-end payment flow, and ultimately, there's this open question: why is the second payment being created in the first place? 

So for Alex joining, he can see what we know, what's underway, and has a thread to pick up on where to help. Ultimately, that information's constantly changing, and responders need to stay current without really having to interrupt their teammates. With the response console, people are able to share directly with IRM, and IRM can pick up relevant findings from Slack. Then, through GCx, agents can read that.

context, build on what's known, and then contribute back their findings. So I can keep working with my agent and share what I find with my teammates. For Alex, who joins later, he can either catch up in the UI or through his own agent. We may all be working in different places, but now we're working from the same picture.

There was also a question at the beginning where Alex joined and said, "I think I've seen something like this before." That's where operational context can help us. We can follow that lead. It uses Grafana's knowledge graph and helps connect your current investigation to your entire incident history. An agent can look across your incidents, find something that was similar, see what was tried, how it was resolved, and potentially suggest something to test out now.

We recognize that every organization is different—your services, your people, how you respond—and we want each of those responses to add to what your team knows. Responders no longer need to get pulled away; people and agents can build on what's already been done. Hopefully, that means less time repeating work, less time hunting down information, and more time fixing the problems at hand.

Now we want to jump in and show you how that works. 

**Demo**

So we are Grafana Bank. I'm an on-call engineer, backend engineer on the payments team, and no alerts have fired. I haven't been paged, but support dropped into our team channel saying, "Hey, a bunch of customers are making transfers and payments out of their bank accounts, and they're seeing they're being charged twice." So I'm going to start investigating that.

Grafana Assistant's great, and Assistant Investigations is great. Internally, I always try to sneak around and look at how we're handling incidents at Grafana. Often, an alert comes into Slack from IRM, and then people are just having this conversation with Grafana in Slack to figure out what the problem is. But we also know everybody has their own way of working. You have harnesses you really like; you might have custom harnesses internally that you want to use. Our approach is just agentic big tent. If you're running incidents, we want you to be able to use whatever tool you're using, but just consolidating that information and bringing it together.

So I'm in Claude Code. We're going to run it this way to start. I'm just going to say, "All right, support says customers are reporting being charged twice. Let's declare an incident." Claude, now using the Grafana CLI (gcx), can declare this incident, which you can see it running now. It's going to be really fast; we won't have any problems with any of the LLMs. 

I'm going to send it off to investigate now and figure out what's happening. While it's doing that, let's jump back into Slack. We can see IRM here posted that a new incident was declared in our announcement channel, and I can see an incident channel specifically for this incident was created. There's some automation that happened here as well. We have an incident commander assigned to every incident, and I can see Marisol was assigned automatically. We also have a helpful little message reminding people of the process that was sent into the channel, along with some bookmarks. I bookmarked our major incident runbook, so all of this was running as a Grafana workflow.

Stepping out of the incident for a second, we can take a look at that. If I come to Grafana workflows, I can just describe to Assistant what I want. For example, if I wanted to say, "Hey, when an incident becomes critical, page in the support team," it will go and build that. We also have a set of prebuilt blueprints. The one we're using in this example is the major incident kickoff workflow, but we have others, like when an on-call schedule changes, prompting Assistant to create a handoff report and then start a conversation in Slack with those engineers to do the handoff. You could also do some basic alert triage, looking to see if this is worth declaring an incident, as well as some basic reporting. For instance, every morning, give me a briefing of what's happening on my services, or maybe give me that weekly.

The major incident workflow we ran here can be clicked into. This was triggered when the incident was created, and we have a variety of triggers. It can be manual or scheduled. Right now, we have events for IRM, such as alert groups, schedules, and incidents. Over time, we'll be taking events from all other Grafana products, like dashboards updated. I can run a workflow, for example. 

I have my steps in here. I created my incident channel, found my on-call commander, assigned them to the incident, and then there are the actions I took in Slack. Just a quick overview: we have some flow control, you can make API calls, safely store your secrets and pass those in, run Python, Prompt Assistant, and we have lots of actions for IRM Teams and Slack to Microsoft Teams.

Okay, I mean that genuinely. Stepping back into the incident, Claude's probably still churning away in that investigation. I'm going to do some old-school manual investigation here. I know that we depend on a service called FedNow to do the transfers, so I'm going to take a look at that dashboard. I can see we had a spike in latency with a lot of really slow requests. I can see that here in these traces as well. It looks like the front end was failing after two and a half seconds, but the actual transfer of the funds continued on and completed successfully. 

I'm going to drop that in the Slack channel. I do not want you to watch me type. 

Okay, let's see what Claude found. It started its investigation and, while installing gcx, it came with some skills on how to use IRM. One of them is to query the knowledge graph. We have an impact: there are duplicate payments. It queries the knowledge graph to see what past incidents exist that have that similar type of impact where there were duplicate payments. For that incident, what was the accepted hypothesis? What did we think was happening? What ended up being the cause or one of the contributing factors? It pulled that from a past incident and tested it in this scenario. In this case, that wasn't what was happening, but we've now effectively ruled that out from the past data.

So, not reading through it, it found there were duplicate payments. Fine. Let's share this to the incident. This is going to do a couple of things. One is it's going to take our investigation to this point—the queries it ran, the evidence it found, the hypotheses it had—and bundle it up into a structure that IRM expects, then send that up to IRM via gcx. It's also going to draft me a status update, like a high-level status update that leadership can get notifications on.

All right, there's my status update. I could send it or correct it if I wanted to. In this case, I'm just going to send it. If I pop back over to the Slack channel, I see now that the status update shows up in Slack, and I should also see it in the thread on my announcement message. If people are subscribed to this, it's now sent out.

At this point, there's some mention of timeouts on the front end. I think I need to page in the front end team. There are a couple of ways I can do that. One, within Grafana...

I can go to our service catalog service center and look directly for the front end. In this case, I'll just go to our service transfer, and I can see that the front end is dependent on our service. So I'll just click to get to them from there. I can see the digital experience team owns this service, and I can see that Mimi is on call. So that's one way. 

Or, directly from my Claude session, I can just ask Claude, "Okay, who owns the banking front end? Who's on call for them right now?" Again, through GCX, it can query the service center, find that data, and return it into the session. Okay, so the front end is owned by digital experience, and Mimi's on call for them. I can page them into the incident, again using GCX to page Mimi in. 

All right, so I've been paged in. Right now, I would drop into our incident view. This is what it looks like today. It kind of looks like some other incident management platforms. You've got some high-level information: the title of the incident, its current status, and severity. There are also a bunch of other links in here, whether it's to Slack or to our PIR. But let's actually open this up in the new response console. 

So, yeah, now when I come to the incident, I can immediately get caught up. What's currently broken? What are our current hypotheses about what's going on? Some information about what's changed recently and potential next steps. All of this is based on your team's work, whether that's in Slack or with a coding agent. 

Michael, let's dig into Slack a little bit. 

Yeah, so in this case, we're using agents and sharing those findings, but we're also pulling in Slack data. If you're just running incidents in Slack, talking to each other, all of that is going to be ingested. I have a little recording here I made earlier. There's an incident channel on the right-hand side, and there's a new response console on the left-hand side. I'm just speed running an incident, playing through the scenario at like ten times speed. 

We can see all the messages coming in, and automatically, IRMs are pulling that in and generating these summaries. So anybody that's paged into the incident, any stakeholder that comes to this page, can immediately know, "Okay, here's what's broken, here's what we're doing, here's what we ruled out, here's what we think is happening." 

Nice. So now we're back in the response console. I've been paged in. This is one way for me to get caught up. As we were saying, all of this information here is based on what your team is providing. This is sort of the high-level summary, but if we want to, we can dig in a little bit further. 

Any of those links off to the side take you a step further, and you can see where that information came from. In this case, this is a couple of pieces of information that were pushed up from a Claude session. There's also a source located linked at the bottom, so this one, like a Tempo trace, or both of these are from traces. 

So this is one way I can get caught up, but I actually don't even need to come in here. I can do this directly from a conversation with my agent. 

Yeah, so here we are. I just got paged. Let me know where I'm needed. Using GCX again, it's going to query up for that incident context. It's going to search through what's been shared and hopefully give me some information about what's going on and where I can help out. 

Yeah, so it says there's an open hypothesis. Oops. Oh, sorry. Yeah, no, it's okay. So it says, "Why is the front end..." It shows me that the front end is timing out after two and a half seconds. I can then follow up and ask, "Well, why is that happening?" Then it comes back and lets me know that there's this feature flag. 

I'm actually going to let the team know right from here. I'm going to say, "Hey, I found this. Here's the current update." Again, it's going to post back to me, asking if I want to edit or if I'm just good to push it along. Now I've let my team know not only what I've found but the mitigation step that I'm taking. 

While that's happening, I remember that when we've done this before, we had to credit customers. I'm actually just going to go ahead and ask that question so GCX can query across the knowledge graph and see how we handled this in a previous incident. 

I'll send you a status update for you first. Perfect. Thank you so much. I went a little faster than our buddies could move. We've got a lot of incidents to crawl through. I could probably interrupt it as well, but I think it's probably... There we go. 

Normally, you have this moment in an incident, and you might go back to the Slack channel. You might find yourself digging through some docs trying to figure out sort of what's your process for this. But instead, I'm kind of able to make this quick query and figure out that, in fact, we did credit customers the last time. 

So we're going to go ahead. We're going to magically fast-forward and call this incident resolved. At this point, I figured out what's going on. I've let my team know that I'm taking action, and I've got an idea of what to do next. 

Yeah, so I just resolved the incident. Now we go into our next step. For all of our incidents, we generate a post-incident review. I just moved it to resolve, and in the background, a workflow kicked off. So we could take a quick look at that. 

Here I have my draft post-incident review workflow. It's running when the incident is resolved and it's prompting the assistant. It's just saying, "Okay, here's the incident. Use a Grafana notebook and create us a post-incident review draft following this format and then send it to Slack." 

We can look to see that's running and should finish in a second. There we go. If I pop back to Slack, here's our executive summary for the post-incident review, and I can open that right up into a Grafana notebook. 

Grafana Notebooks, again, is in public preview as of this week and allows us to take all of this extra context for the incident—the hypotheses, the impacts, the data from Slack, the agent sessions—and combine that with the telemetry of what happened in the incident to come up with this nice first draft. 

This is editable as well. We can get this cleaned up and bring it to our review meeting. So we can pop back to the slides. 

Hey, we'll take it. We'll take it. Yeah, so we started this by asking a question. We're moving faster, but are we moving together? Individual speed is only going to take us so far. The real value comes when what one person finds helps someone else act. 

That's really what we're building towards: people and agents working together, making that work visible, and creating something where you can build off each other's expertise. We ultimately want you to spend less time catching up and more time solving the problems at hand. 

When that incident ends, we don't want your learning to. So that knowledge will stay with your team and hopefully make your next response better. 

Just a quick recap of all the things we showed you: I know we clicked around through a bunch of different products, but here's everything that's generally available. Grafana workflows and notebooks have moved into public preview, and the response console and operational context are currently in private preview. 

Michael can tell you how to get involved. 

Yeah, so come see us at the booth. We're over by the lightning talk stage, and this QR code will take you to a signup. You can just send me an email address. I'll be in touch, and we can get these things enabled for you and kind of talk through it. 

We're happy to have you use IRM with whatever agents you're using and bring it all together. So thanks. Thank you.

## Raw YouTube Transcript

All right. Hi everyone. 
Thanks so much for being here. I'm Mimi. I'm a senior engineering manager 
with Grafana IRM. I've been a responder, a commander and led incident management trainings at 
previous roles, and now I get to build the tools. Outside of work, I live here in San Francisco with 
my husband and our son. And when I have free time, I'm often scrolling through Zillow. So please 
ask me about the homes I'm never going to buy. Yeah. I'm Michael Wettick. I'm the product 
manager for IRM. I'm a very simple man. I like incidents. I like ice cream and 
I like the greatest city in the world, Pittsburgh, Pennsylvania, where 
I live with my wife and son. My background, I spent most of my career in 
engineering as an IC and an engineering manager, and then someone tricked me into a product 
role. So that's where I find myself now. I always hate when I'm in the crowd and 
somebody does a raise your hand thing. So who here is aware that Grafana has an incident 
management product? Raise your hand. Okay, this is pretty good. That's most of you.
And for those of you that didn't, we do, and we've been incredibly busy the last 
couple of years building this end-to-end incident management platform. And I'm really fortunate 
every week I get to talk to companies that are migrating from a competitor and it's sometimes 
a couple teams up to thousands of on-call engineers. And so especially if you're already 
using Grafana Cloud, it just makes so much sense. So stop by our booth. I think there's a promotion. 
Mimi is going to personally migrate anyone that shows up today and commits to make that switch. 
Just kidding. But so, yeah, see us at the booth. Okay. One more question. Who here is using 
LLMs to help investigate during incidents? All right. And then leave your hand up if you're 
then finding yourself copying and pasting things out of Claude into the incident channel. Yeah.
Yeah. That's what we thought. One slide too many. So, yeah, a lot of you are already investigating 
incidents with agents and you're often finding yourself manually sharing that information with 
your team. Incident response is changing as people and agents investigate together. I could be 
working with Claude, Michael with Cursor, somebody else with Grafana Assistant. And we're all making 
progress and we're all moving a lot faster, but are we actually moving together? Keeping 
everyone up to speed has always been hard. The rest of the team doesn't necessarily know what 
you're doing. So we still have to stop and share. What have you checked? What have you ruled 
out? What are you planning to do next? And if you've just joined the incident, you need the answers to a lot of those questions 
before you can even step in and help. Sharing means recognizing what matters 
and remembering to tell each other. That takes judgment. And sometimes what I think 
is unimportant is exactly what you needed to know. Agents are helping us do a lot more, but we still 
have to bring that information back to the team. Let's take this incident, for example, 
like a common question that comes up. Could it be the deploy? I'm checking with Claude. 
Michael's working with Cursor. Somebody else is with Grafana Assistant. I've ruled it out, 
but that answer stays in my conversation. Michael and the assistant are still 
working on that. And then Alex joins and he thinks he's seen something like this 
before, but he still needs to get caught up. We're actively making progress, but Alex 
can't see where the investigation stands. Yeah. So this is a real pain point Mimi's 
describing, and I think it exposes a gap in the observability space overall. I think 
as an industry, we have an overly narrow view or definition of what the system is when we 
think about understanding our system. We have all these great tools to see what's happening 
in the technical part, but that isn't enough. So this is the part of the system 
we spend a lot of time looking at. We have our services and our databases 
and the dependencies between them and we have all this metrics, logs, traces, 
telemetry to understand what's happening, but these signals still need someone to interpret 
them. If there's a dashboard showing latency going up, someone has to figure out what that 
means, what to do next, what to do about it. And so this is the whole system, the rest of 
the system. You all, the people in the room, you engineers and your expertise, and you're 
bringing that every day to keep the system running and you're diagnosing and troubleshooting 
and inferring and anticipating other problems and you're learning how the system actually 
behaves versus how you think it behaves. And all of this is super valuable 
knowledge to the next person, the next incident, your colleagues, 
the other people in the incident, but most of it isn't captured and just 
vanishes when the incident is over. And we obviously can't look directly inside 
your head and pull this out and pull out what you're thinking, but there are signals 
that are left behind and we can see the things you do and say as you work. So these 
are the signals of response itself. There's the conversations you're having with each other, 
the conversations you're having with your agents, the queries you're running, how you're using 
Grafana Cloud, who you're asking for help, which teams and which people you're pulling 
in, the mitigations you apply to the system. And so with the new IRM, we're 
bringing together all of this data from both people and agents and Slack to have 
this shared picture as a response unfolds. And the goal is just being surfacing this, making 
it visible like all other observability data. So we have three announcements today. One 
is Grafana Workflows is a new product going public preview. So that's in your stack 
today and we'll talk about it in a second, as well as the new IRM response console and 
operational context on the knowledge graph, which is private preview. And we'll 
have a sign-up QR code at the end. So workflows, any kind of process you have, and 
today we're talking about incidents. So think about specifically around an incident. Any kind of 
process you have, you can turn into automation and kind of take that toil off the responders during 
an incident at the beginning of the incident. These can react to events, which we'll see. They 
can be run manually in the web UI or via API. And we have a series of built in actions and you 
can run code and you can call third party systems. You can build these with agents, you can 
build them in the web. And we have a bunch of prebuilt blueprints as well. The goal just 
being handling that toil so you can focus on that investigation during the incident.
Yeah. So if Workflows is helping get your response organized, the response console 
is bringing your investigation together. Let's go back to Alex. He was joining while 
we were all working with different agents and he needed to get caught up. Oftentimes 
today, that really means scrolling through Slack or DMing one of your colleagues and that 
ultimately pulls them out of the investigation. You might also find yourself just starting from 
scratch and duplicating work of your teammates. And these are the questions that we're trying to 
answer for Alex. So here's an example from the incident we're going to show shortly. I can see 
that customers are reporting duplicate payments. I can see that we've confirmed that the duplicate 
payments are true. I can see that someone's actively investigating the front end payment flow 
and ultimately that there's this open question, why is the second payment being created 
in the first place? So for Alex joining, he can see what we know, what's underway and 
has a thread to pick up on where to help. And ultimately, that information's constantly 
changing and responders need to stay current without really having to interrupt their 
teammates. With the response console, people are able to share directly with IRM and 
IRM can pick up relevant findings from Slack. And then through GCx, agents 
can then read that context, build on what's known, and then 
contribute back their findings. So I can keep working with my agent and 
share what I find with my teammates. And for Alex who joins later, he can either 
catch up in the UI or through his own agent. So we may all be working in different places, 
but now we're working from the same picture. And then there was sort of the other question 
at the beginning where Alex joined and he said, "I think I've seen something like this before." That's where operational context can 
help us. We can follow that lead. It uses Grafana's knowledge graph and it helps 
connect your current investigation to your entire incident history. So an agent can look across 
your incidents, find something that was similar, what was tried, how did you resolve it and 
potentially suggest something to test it out now. And we recognize that every organization is 
different, your services, your people, how you respond, and we want each of those responses 
to add to what your team knows. So responders no longer need to get pulled away and people and 
agents can build on what's already been done. So hopefully that means less time repeating work, 
less time hunting down information and more time fixing the problems at hand. And now we want 
to jump in and show you kind of how that works. Did you-
Yeah, demo. All right. So we are Grafana Bank. I'm an on-call 
engineer, backend engineer on the payments team and no alerts fired. I haven't been paged, but 
support dropped into our team channel like, "Hey, a bunch of customers, they're making transfers, 
they're making payments out of their bank account and they're seeing they're being charged twice." 
So I'm going to start investigating that. And Grafana Assistant's great and Assistant 
Investigations is great. Internally, I always try to sneak around and look at how 
we're doing incidents internally at Grafana. And it's often an alert comes into Slack from IRM 
and then people are just having this conversation with Grafana and Slack to figure out what 
the problem is. But we also know everybody has their own way of working. You have harnesses 
you really like, you might have custom harnesses you have internally that you want to use. And so 
our approach is just agentic big tent. If you're running incidents, we want you to be able to use 
whatever tool you're using, but just consolidating that information, bringing it together. Yeah.
So I'm in Claude Code. We're going to run it this way to start. So I'm just going to start 
by saying, all right, support says customers are reporting being charged twice. Let's declare 
an incident. So Claude now using the Grafana CLI gcx can declare this incident, 
which you can see it running now. And it's going to be really fast. We're going 
to have no problems with any of the LLMs. Okay. And so I'm going to send it off to investigate 
now and just figure out what's happening. Okay. So while it's doing that, 
let's jump back into Slack. So we can see IRM here posted. There was a new 
incident declared in our announcement channel and I can see an incident channel specifically 
for this incident was created and there's some automation that happened here as well.
So we have an incident commander assigned to every incident and I can see 
Marisol was assigned automatically. We have just a helpful little message reminding 
people of process that was sent into the channel. And we have some bookmarks here as well. 
So I bookmarked our major incident runbook. So all of this was running as a Grafana 
workflow. So stepping out of the incident for a second, we can take a look at that.
If I come to Grafana workflows, I can just describe to Assistant what I want. So if I wanted 
to say, "Hey, when an incident becomes critical, page in the support team," and it'll go and build 
that. We also have, if you go to create, a set of prebuilt blueprints. So the one we're using 
in this example is this major incident kickoff workflow, but we have things like when an on-call 
schedule changes, prompt assistant to create a handoff report and then start a conversation in 
Slack with those engineers to do the handoff. You could do some basic alert triage. So 
when they come in, look and see if this is worth declaring an incident, as well as 
some basic reporting. So every morning, give me a briefing of what's happening on 
my services, maybe give me that weekly. So the major incident one we ran here, 
I can click into. Let me close that. So this was triggered on the incident being 
created and we have a variety of triggers. So it can be manual, it can be schedule. And right 
now we have events for IRM. So alert groups, schedules and incidents. And then over time 
we'll be taking events from all other Grafana products. So dashboards updated. I 
can run a workflow, for example. And I have my steps in here. So there I created 
my incident channel. I found my on-call commander. I assigned them to the incident and then 
there are the actions I took in Slack. So just like a quick little overview, we have 
some flow control, you can make API calls, you can safely store your secrets and 
pass those in. You can run Python, Prompt Assistant, and then we have lots of 
actions for IRM Teams and Slack to the Teams. Microsoft Teams. Yeah. Okay. I mean that 
genuinely. Okay. And then within this, you can reference data. So I can write expressions 
to pull data from other steps so I can start piping and chaining data between steps. I have 
access to all the information of the incident. So all the details of the incident I could 
then pass out to another system, so forth. Okay. So stepping back into the incident, 
Claude's probably still churning away in that investigation. I'm going to do some old school 
manual investigation here. I know that we depend on this service called FedNow to do the transfers. 
So I'm going to take a look at that dashboard and I can see, okay, we had this spike in 
latency, a lot of these really slow requests. And I can see that here in these traces as well.
So it looks like the front end was failing after two and a half seconds, but then the actual 
transfer of the funds continued on and completed successfully. So I'm going 
to go drop that in the Slack channel. And I do not want you to watch me 
have to type. We're doing that. Okay. And then let's see what Claude found. 
All right. So it started its investigation and installing gcx, it came with some 
skills on how to use IRM. And one of them is query the knowledge graph. So we have an impact, 
there's duplicate payments. It queries the knowledge graph to see what past incidents exist 
that have that similar type of impact where there are duplicate payments. For that incident, 
what was the accepted hypothesis? What did we think was happening? What ended up being 
the cause or one of the contributing factors? And so it pulled that from a past incident and 
tested it in this scenario. And in this case, that wasn't what was happening, but we've now 
effectively ruled that out from the past data. So not reading through it found there was duplicate 
payments. Fine. Let's share this to the incident. So this is going to do a couple things. One 
is it's going to take our investigation to this point, the queries it ran, the evidence it 
found, the hypotheses it had, and bundle it up into a structure that IRM expects and then send 
that up to IRM via gcx. And it's also going to draft me a status update, like a high level status 
update that leadership can get notifications on. All right, so there's my status 
update. I could not send it. I could correct it if I wanted to. In 
this case, I'm just going to send it. And if I pop back over to the Slack channel, so 
I see now that status update show up in Slack and I should also see it in the thread on 
my announcement message. So if people are subscribed to this, so that's now sent out.
Okay. So I think at this point there's some mention of timeouts on the front end. I think I 
need to page in the front end team. So there's a couple ways I can do that. One, within Grafana, 
I can go to our service catalog service center and I could look directly for the front end or in 
this case, I'll just go to our service transfer and I can see that the front end is dependent on 
our service. So I'll just click to get to them from there. I can see the digital experience 
team owns this service and I can see that Mimi is on call. So that's one way.
Or directly from my Claude session, I can just ask Claude, "Okay, who owns the banking 
front end? Who's on call for them right now?" And again, through gcx, it can query service center, 
find that data and return it into the session. Okay. So front end's owned by digital 
experience. Mimi's on call for them, page them into the incident. Again, 
using gcx to page Mimi in. All right. So I've been paged in. Right 
now, I would drop into our incident view. This is what it looks like today. Kind of looks 
like some other incident management platforms. You've got some high level information. I've got 
the title of the incident. It's currently open, the status and the severity. There's also a 
bunch of other links in here, whether it's to Slack or to our PIR, but let's actually 
open this up in the new response console. So, yeah, so now when I come to the incident, I 
can immediately get caught up. What's currently broken, what are our current hypotheses about 
what's going on, some information about what's changed recently and potential next steps. 
All of this is based on your team's work, whether that's in Slack or with a coding agent. 
Michael, let's dig into Slack a little bit. Yeah. So in this case, we're using agents and 
we're sharing those findings, but we're also pulling in Slack data. So if you're just running 
incidents in Slack, talking to each other, all of that's going to be ingested. So I have a 
little recording here I made earlier. There's an incident channel on the right-hand side. There's 
a new response console on the left-hand side, and I'm just speed running an incident playing 
through the scenario like 10 times speed. And so we can see all the messages coming 
in and automatically IRMs pulling that in and generating these summaries. So 
anybody that's paged into the incident, any stakeholder that comes to this page can 
immediately know, "Okay, here's what's broken, here's what we're doing, here's what we ruled 
out, here's what we think is happening." Nice. So now we're back in the response console. 
So I've been paged in. This is one way for me to get caught up. As we were saying, all of this 
information here is based on what your team is providing. This is sort of the high level 
summary, but if we want to, we can dig in a little bit further. So any of those links 
off ... Oh, you've already clicked it. Any of those links off to the side take you a step 
further and you can see where that information came from. So in this case, this is a couple 
pieces of information that were pushed up from a clod session. There's also a source located linked 
at the bottom, so this one like a tempo trace or both of these are from traces.
So this is one way I can get caught up, but I actually don't even need to come in here. I can do 
this directly from a conversation with my agent. Yeah. So here we are. I just got paged. Let me 
know where I'm needed. And so now using gcx again, it's going to query up for that incident context. 
It's going to search through what's been shared and hopefully give me some information about 
what's going on and where I can help out. Yeah. So it says there's an 
open hypothesis. Oops. Oh, sorry.
Yeah, no, it's okay. Yeah. So it says, why is the front end ... It shows me that 
the front end is timing out after two and a half seconds. And so I can then follow up and 
ask, "Well, why is that happening?" And then it comes back and lets me know that there's this 
feature flag. And so I'm actually going to let the team know right from here. I'm going to say, 
"Hey, I found this. Here's the current update." Again, it's going to post back to me, ask me if I 
want to edit or if I'm just good to push it along. And now I've let my team know not only what I've 
found, but the mitigation step that I'm taking. And so while that's happening, I remember that 
when we've done through this before that we had to credit customers. And so I'm actually 
just going to go ahead and ask that question so Gcx can query across the knowledge graph and 
see how we handled this in a previous incident. I'll send you a status update for you first.
Perfect. Thank you so much. I went a little faster than 
our buddies could move. We've got a lot of incidents. 
It's got to crawl through. I could probably interrupt it as well, but 
I think it's probably ... There we go. All right. So normally, you have this moment in 
an incident and you might go back to the Slack channel. You might find yourself digging through 
some docs trying to figure out sort of what's your process for this, but instead, I'm kind of able 
to make this quick query and figure out that, in fact, we did credit customers the last time. So 
we're going to go ahead. We're going to magically fast-forward and call this incident resolved. 
At this point, I figured out what's going on. I've let my team know that I'm taking action 
and I've got an idea of what to do next. Yeah. So I just resolved the incident. Now we go 
into our next step. So for all of our incidents, we generate a post-incident review. I just 
moved it to resolve and in the background a workflow kicked off. So we could 
take a quick look at that. Here I have my draft post-incident review 
workflow. It's running when the incident is resolved and it's prompting assistant. And so 
it's just saying, "Okay, here's the incident. Use a Grafana notebook and create us a post-incident 
review draft following this format and then send it to Slack." So we can look to see that's running 
and should finish in a second. There we go. So if I pop back to Slack, here's our executive 
summary for the post-incident review and I can open that right up into a Grafana notebook. So 
Grafana Notebooks, again, is public preview as of this week and allows us to take all of this extra 
context for the incident, the hypotheses, the impacts, the data from Slack, the agent sessions, 
and combine that with the telemetry of what happened in the incident to come up with this nice 
first draft. And then this is editable as well. We can get this cleaned up and bring it to our review 
meeting. So we can pop back to the slides. Hey, we'll take it. We'll take it. Yeah. 
So we started this by asking a question. We're moving faster, but are we moving together? 
Individual speed is only going to take us so far. The real value comes when what one 
person finds helps someone else act. And that's really what we're building 
towards, people and agents working together, making that work visible and making something 
where you can build off each other's expertise. We ultimately want you to spend less time catching 
up and more time solving the problems at hand. And when that incident ends, 
we don't want your learning to. So that knowledge will stay with your team 
and hopefully make your next response better. And so just a quick recap of all the things we 
showed you. I know we clicked around through a bunch of different products, but here's everything 
that's generally available. Grafana workflows and notebooks have moved into public preview 
and the response console and operational context are currently in private preview. 
Michael can tell you how to get involved. Yeah. So come see us at the booth. 
We're over by the lightning talk stage and this QR code will take you to a signup. 
You can just send me an email address. I'll be in touch and we can get these things enabled 
for you and kind of talk through it. And, yeah, we're happy to have you use IRM with whatever 
agents you're using and bring it all together. So thanks.
Thank you.

