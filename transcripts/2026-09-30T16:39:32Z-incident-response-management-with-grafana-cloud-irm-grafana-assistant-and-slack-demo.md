# Incident Response Management with Grafana Cloud IRM, Grafana Assistant, and Slack (Demo)

Published on 2026-09-30T16:39:32Z

## Description

Grafanistas Ashley and Edward provide a comprehensive walkthrough demonstrating chat ops integration with Grafana Cloud ...

URL: https://www.youtube.com/watch?v=Eb2XYqkgb44

## Summary

The show is titled "Incident Response Management with Grafana Cloud IRM, Grafana Assistant, and Slack (Demo)" and was published on September 30, 2026. The speakers, Ashley and Edward, provided a detailed demonstration of the Grafana Assistant's integration with Slack for incident response management. They discussed features such as automated incident declaration, real-time collaboration in Slack, and the use of an AI investigation agent to identify root causes of incidents. Key takeaways included the seamless integration of Grafana tools with existing workflows, the ability to manage incidents from mobile devices, and the automation of post-incident reporting.

Topics: Grafana Assistant, Slack integration, incident response management, AI investigation, mobile app features.

## Chapters

00:00:00 ChatOps integration with Grafana Assistant in Slack
00:04:53 Incident management and investigation in Grafana Cloud
00:09:29 Creating post-incident reports with Grafana mobile app

Okay, so today I want to show you one of the things that made me really excited about working on ChatOps integration with the assistant. My new favorite way is actually just going directly in Slack and pinging the Grafana Slack bot to ask it what is going on. This will kick off the assistant inside of Slack. Because the assistant has context to the alert and the entire Slack thread, I don't even need to provide it with any actual context. 

The assistant then looks at your telemetry, whether that's logs, metrics, trace profiles, or any sort of MCP you've set up. For example, if you set up a GitHub MCP, it is actually able to look at it, pull your code, and check for issues. One other nice thing about the Slack integration is that because the bot replies directly in that thread, if you're handling a support escalation or something, you don't need to update the support person because they will be able to see exactly what the bot is doing and the updates from the bot. 

The bot also runs in the backend. If you have spotty internet or disconnect, the bot will keep going. So the bot has some findings, and we can just pass it to Ashley. Thank you. 

Okay, so now we'll move from triaging this alert into finding the root cause. Here we can see the results from the Grafana assistant inquiry that Edward made. The assistant indicates that this alert is currently firing and is driven by cascading errors from two downstream dependencies, most notably the ad service. This seems to be part of the root cause. This is a critical service to our company, so I'm going to go ahead and declare an incident to bring the team together to collaborate and find out how to resolve this quickly. 

I'll go ahead and acknowledge the alert. This will break out of that escalation chain, so it will not continue to page my colleagues. Then I'll declare an incident. When I declare an incident, it will ask me what I want to title the incident. We'll name this "Front End Error Rate is Elevated." I can give an initial status, so I'll let everyone know that I'm looking at it. We can also give an initial severity, so I'll start out with pending and we'll go ahead and declare the incident. 

When I declare an incident, a number of automated actions will happen for us. First, we'll see that a Slack channel has been created for this particular incident. We can drill into that Slack channel, and this is where all the collaboration will happen from here on out about this particular problem. A number of other automated actions can occur, such as automatically creating a Zoom bridge, a Jira issue, or any other number of actions that you may want to take. 

Here in the channel, we can see my most recent status update. If we scroll up, we can start to take actions from Slack without ever leaving, in this case, our mobile device. So I'm going to go ahead and assume the role of commander and assign Edward as the investigator. Now we have our roles assigned, and stakeholders don't need to wonder who's actually working on this particular incident. 

I can also update the severity. For example, I may want to update this to critical now that I've had a chance to think about it. There are a number of other actions that we can take from Slack, such as escalating to page a team or an individual, adding more status updates, or creating tasks, which can then be moved into Jira or GitHub, wherever you manage your tasks, and will remain synced with those systems. 

You'll see that Edward was automatically added to the Slack channel as soon as I assigned him a role. So we're now both part of the Slack channel and can start to collaborate. The first thing I'm going to do is let everyone know what my hypothesis is. I think it was this morning's deployment that caused this. As soon as someone says something super relevant to the investigation, we can react to it with a robot emoji. That will pull this message into the incident timeline and also pass that context into the AI investigation that we're going to look at later on. 

Now let's go ahead and take a look at the incident in the UI. Here we have our incident record, and we can see all the same details that we could see in Slack or on mobile. We can update the status from active to monitoring, mitigating, or resolved. You can see that we recently updated the severity. You can see me and Edward are represented as the two roles that are currently filled. Down on the left, we can see the timeline that's being built out as I make all of these updates. 

For example, first, you can see that I volunteered as commander, then volunteered Edward as investigator. I updated the status to critical, which triggered an automatic page to our IMOC, who is our incident manager on call. Finally, I sent that message in Slack that I thought it was this morning's deployment, and you can see that is also reflected in the timeline. 

If I wanted to add some tasks, I could certainly do that either from the UI or Slack. I'll go ahead and add a task that we really need to improve error logging on the front end service. While this is something that we need to do, it's not critical in the moment, but we don't want this to get lost. So we can convert this task to either a GitHub or Jira issue and make sure that the team that owns this has awareness of it. I'll go ahead and create this as a Jira issue, and these two will now remain bidirectionally synced. 

Over here on the right-hand side, you can see that the assistant investigation has been automatically triggered. As soon as I declared an incident, we triggered an investigation and sent out the investigations agent to find the root cause. We can wait for the investigations agent to report back on what the root cause was, which will update the incident as well as Slack and our stakeholders. 

But let's jump in and watch it live in Assistant Workspace. Assistant Workspace provides a collaborative interface where we can actually work with the agent to start to find the root cause and drill down into what might be going on. As soon as we trigger an investigation, all of the context that we pass when we trigger that investigation will be transparent to us. 

At the top, you can see that the context which triggered this investigation is that the front end error rate incident was declared. This includes all of the labels that are part of that incident, as well as all that information about the source alert that Edward worked on earlier in the demo. As soon as the investigations agent goes out to try to find the root cause, it builds multiple hypotheses and works to prove or disprove those hypotheses. 

Right away, we can see that it came up with a few different ideas and then worked to prove or disprove them, marking them as either symptom, root cause, or disproven. On the right-hand side, we have our canvas where the report will be built out. As soon as it's finished, we can see all of the sources that it's using to come to these conclusions and then see the actual hypotheses. 

Two of them are marked as suspected, and it has already disproven three of them. You'll notice that the last hypothesis is the one that I mentioned in Slack. So while our engineers are coming up with ideas in Slack, we are moving them into the incident, and automatically the AI agent is taking that and working to prove or disprove it. In this case, when we ran this check against the hypothesis about the deployment, it's actually using GitHub to investigate that particular hypothesis. It will use GitHub and the MCP server integration to figure out if that is the root cause. In this case, you can see that it didn't find any evidence of a deployment that could have...

Caused this problem. As it's continuing to prove and disprove the hypotheses, we can follow along. We can also add additional hypotheses; we could disprove them, we could reopen them, or however we want to interact with the investigations agent.

All right, so here we can see it finished working through all of the hypotheses. This one up top, where it says the root cause was probably the ad services get ads RPC calls failing end to end, does seem like it is actually the root cause. So I'm going to go ahead and confirm this. I mark that as the cause, and then we can go back to our incident and mark this as resolved. 

You'll see that when the report finished, as I mentioned, it does update the incident itself. So we have all of that detail in the incident report as well as updating the Slack channel. We can see that it updated the investigation with the findings from the report. This is part of the ultimate investigation report, and it also posted that update into the Slack channel so we can see the investigation findings are posted back here for anyone in our company to see and understand.

I'll jump back into our investigation, and at this point, what we would typically want to do is generate a post-incident report (PIR). PIRs are typically living in whatever platform you're using, potentially Confluence, Notion, Google Docs, or whatever it might be, and we need to get all of this information we just went through into that system. A lot of times, we're leaving our computers, and this might be a last thought that we need to come back to. The mobile app is a great way to support uploading these PIRs into those systems.

Now that we're done, we found the suspected root cause. We can come in and confirm, yes, that was the cause, and we have our final report. What's next? We need to build a PIR. A lot of times, we might forget to do this, and we might go home or close our laptops. Before, we would have to reopen our laptops, sign in, and create that PIR manually. Today, with the Grafana mobile app, we can take AI investigations on the go, as well as take actions such as creating PIRs.

For example, we come into the mobile app, we open up the Grafana mobile app. We can certainly manage all of our IRM schedules, interact with our alert groups, make shift swaps, and manage our incidents from the mobile app. But we can also interact with Grafana Assistant and Grafana Investigations. 

So I'm going to come down and find my recent investigation. We can come in here, and we can either see all of our conversations or all of the investigations which have recently kicked off. So we can come right here and find all of our recent assistant chats, which includes both investigations and regular chats. Here's the one that we were just working on from our incident for the ad service error rate. 

So I'll click in here, and we can continue the conversation. You can see the latest thing that happened was that it disproved that hypothesis about the recent deployment, and I can come in and interact with the investigations agent. So what I'll say is create a PIR and upload it to Confluence. Confluence is the tool that we use internally, so we want to upload our PIR there. 

What the investigations agent will now do is review the report that it generated, and it's also going to use a skill that I have set up, which outlines how to format the PIR correctly to put into Confluence. It's going to use the Atlassian MCP server integration in order to upload that PIR. We'll just let this go for a sec. 

Okay, so here we can see that the agent has responded that it created the PIR and uploaded it into my Confluence workspace. We can click the direct link into the PIR if we want to review it. Here's what that looks like. We can see the PIR is formatted exactly how it outlined, and it includes a summary, impact, and full timeline based off of both the investigation and the incident. 

So no matter where people were collaborating—in Slack, on mobile, or in the UI—all of that context now exists in the system that we need that information to be in. For our demo, we got to see Edward showing us in Slack where you're working already, how we can interact with the assistant, which has access to our actual data as well as our on-call information, our alert information, and can help us very quickly understand the blast radius of any alerts that we're getting. 

We also saw the new mobile app, which contains capabilities expanding across IRM and assistant. And we saw how when we declare an incident, we have an AI investigation agent, which is automatically triggering, working to find that root cause for us, and then posting the updates so that everyone can see them. Finally, we saw how we can integrate with other tools to expand the workflow into our existing workflows to make sure that we're meeting you where you are using MCP server integrations.

## Raw YouTube Transcript

Okay, so today I want to show you one of
the things that made me really excited working on ChatOps integration
with the assistant. My new favorite way is actually
just going directly in Slack and ping the Grafana Slack bot and just ask it what is going on. So this will kick off the
assistant inside of Slack. And because the assistant actually
has context to the alert and the entire Slack thread, I don't even
need to provide it any actual context. So the assistant then goes
on to look at your telemetry, whether that's logs,
metric, trace profiles, or any sort of MCP you've
set up. So for example, if you set up GitHub MCP is
actually able to look at it, pull your code and check code for issues. One other nice thing about the Slack
integration is because the bot replies directly in that thread, if you're handling a support
escalation or something, you don't need to update the support
person because they will be able to see exactly what the bot is doing
and the updates from the bot. The bot also runs in the backend. If you have spotty
internet and whatnot, even if you disconnect,
the bot will keep going. So the bot has some findings
and we can just pass to Ashley. Thank you. Okay. So now we'll move from triaging this
alert into finding the root cause. So here we can see the results from the
Grafana assistant inquiry that Edward made. And we can see that the assistant is
saying that this alert is currently firing and it's driven by cascading errors
from two downstream dependencies, most notably the ad service. So that
seems to be part of the root cause. This is a critical service to our company, so I'm going to go ahead and declare an
incident so that we can bring the team together to collaborate and find
out how to resolve this quickly. I'll go ahead and acknowledge the alert. This will break out of that escalation
chain so it will not continue to page my colleagues. Then I'll go
ahead and declare an incident. When I declare an incident, it will ask me what I want to title
incident. We'll name this front end error rate is elevated. I
can give an initial status, so I'll let everyone know
that I'm looking at it. And we can also give an initial severity. So I'll start out with pending and
we'll go ahead and declare the incident. When I declare an incident, a number of
automated actions will happen for us. First, we'll see that a Slack channel has been
created for this particular incident. We can drill into that Slack channel
and then this is where all the collaboration is going to happen from
here on out about this particular problem. A number of other automated actions can
occur such as automatically creating a Zoom bridge, a Jira issue or any other number of
actions that you may want to take. Here in the channel, we can see
my most recent status update. And if we scroll up, we can start to take actions from Slack
without even ever leaving, in this case, our mobile device. So I'm going
to go ahead and assume role. I'll assign myself to commander and I'm going to also assign
Edward into investigator. Okay. So now we have our roles assigned and
stakeholders don't need to wonder who's actually working on this particular
incident. I can also update the severity. For example, I may want to update this to critical
now that I've had a chance to think about it. And there's a number of other
actions that we can take from Slack, such as escalating to page
a team or an individual, adding more status
updates or creating tasks, which can then be moved
into Jira or GitHub, wherever you manage your tasks and
will remain synced with those systems. You'll see also Edward was automatically
added to the Slack channel as soon as I assigned him a role. So we're now both part of the Slack
channel and we can start to collaborate. The first thing I'm going to do is let
everyone know what my hypothesis is. So I think it was this
morning's deployment that caused this. As soon as someone says something
super relevant to the investigation, we can come in and react
to it with a robot emoji. That will pull this message into the
incident timeline and also pass that context into the AI investigation
that we're going to look at later on. So now let's go ahead and take a
look at the incident in the UI. Here we have our incident record and
we can see all the same details that we could see in Slack or
we could see in mobile. We can update the status from active
to monitoring, mitigating or resolved. You can see that we recently
updated the severity. You can see me and Edward are represented
as the two roles that are currently filled. And here down on the left, we can see the timeline that's being
built out as I make all of these updates. So for example, first you can see
that I volunteered as commander, then volunteered Edward as investigator.
I update the status to critical, which then triggered an
automatic page to our IMOC, who is our incident
manager on call. Finally, I sent that message in Slack that I
though it was this morning's deployment, and you can see that is also reflected
in the timeline. If I wanted to add some tasks, I could certainly come in and
do that either from the UI or Slack. I'll go ahead and add a task that we
really need to improve error logging on the front end service. While this
is something that we need to do, it's not critical in the moment,
but we don't want this to get lost. So we can convert this task to either a
GitHub or Jira issue and make sure that the team that owns this
has awareness of it. So I'll go ahead and create this as a
Jira issue and these two will now remain bidirectionally synced. Over
here on the right hand side, you can see that the assistant
investigation has been
automatically triggered. As soon as I declared an incident, we triggered an investigation and we sent
out the investigations agent to go and find the root cause. We can wait for the investigations agent
to report back on what the root cause was, which will update the incident
as well as Slack and our stakeholders. But let's jump in and watch it
live in Assistant Workspace. Assistant Workspace provides
a collaborative interface
where we can actually work with the agent in order to start to
find the root cause and drill down into what might be going on. As soon
as we trigger an investigation, all of the context that we pass when
we trigger that investigation will be transparent to us. So here at the top, you can see that the context which
triggered this investigation is that the front end error rate incident
was declared. This includes
all of the labels that are a part of that incident, as well as all that information about
the source alert that Edward worked on earlier in the demo. As soon as the investigations agent
goes out to try to find the root cause, what it does is it builds multiple
hypotheses and it will work to prove or disprove those hypotheses. So right away we can see that it came up
with a few different ideas and then it worked in order to prove or disprove
them and mark them as either symptom or root cause or disproven. Over
here on the right hand side, we have our canvas where the report will
be built out. As soon as it's finished, we can see all of the sources that
it's using in order to come to these conclusions and then we can
see the actual hypotheses. So two of them are marked as suspected
and then it's already disproven three of them. And you'll notice that the last
hypothesis that it has is that one that I said in Slack. So while our engineers
are coming up with ideas in Slack, we are moving them into the incident
and automatically the AI agent is taking that and working to prove or
disprove it. In this case, when we ran this check against the
hypothesis about the deployment, it's actually using GitHub to
investigate that particular hypothesis. It will use GitHub and use the MCP server
integration in order to figure out if that actually is the root
cause. And in this case, you can see that it didn't find any
evidence of a deployment that could have caused this problem. As it's continuing to prove and disprove
the hypotheses, we can follow along. We can also add additional,
we could disprove them, we could reopen them or however we want
to interact with the investigations agent. All right, so here we can see it finished
working through all of the hypotheses. This one up top where it says the root
cause was probably the ad services get ads RPC calls failing end to end, that does seem like it is
actually the root cause. So I'm going to go ahead and confirm this. I mark that as the cause and then we
can go back to our incident and mark this as resolved. You'll see that when the report
finished, as I mentioned, it does update the incident itself. So we have all of that detail in the
incident report as well as updating the Slack channel. So we can see that it updated the
investigation with the findings from the report. So this is part of the
ultimate investigation report
and then it also posted that update into the Slack channel so we
can see the investigation findings are posted back here for anyone in our company
to see and understand. I'll jump back into our investigation and at this point, what we would typically want to do
is generate a post-incident report. PIRs are typically living in
whatever platform you're using, potentially Confluence, Notion,
Google Docs, whatever it might be, and we need to get all of this
information we just went through into that system. A lot of times we're leaving our computers
and this might be a last thought that we need to come back to, and the mobile app is a great way
to support uploading these PIRs into those systems. Now that we're done,
we found the suspected root cause. We can come in and confirm, yes, that was the cause and we have
our final report. What's next? We need to build a PIR. So a lot of times we might
forget to do this maybe, and we might go home or close our laptops.
Before, we would have to reopen our laptops,
sign in and create that PIR manually. Today with the Grafana mobile app, we can take AI investigations on the
go as well as taking actions such as creating PIRs. So for example,
we come into the mobile app, we open up the Grafana mobile app. We can certainly manage
all of our IRM schedules, interact with our alert groups, make shift swaps and manage our
incidents from the mobile app, but we can also interact with Grafana
Assistant and Grafana Investigations. So I'm going to come down and
find my recent investigation. We can come in here and we can either see
all of our conversations or all of the investigations which
have recently kicked off. So we can come right here and find
all of our recent assistant chats, which includes both
investigations and regular chats. And here's the one that we were just
working on from our incident for the ad service error rate. So I'll click in here
and we can continue the conversation. You can see the latest thing that happened
was that it disproved that hypothesis about the recent deployment and I
can come in and interact with the investigations agent. So what I'll
say is create a PIR and upload it, upload it to Confluence. Confluence
is the tool that we use internally, so we want to upload our PIR there. What the investigations agent will now
do is it will review the report that it generated and it's also going to
use a skill that I have set up, which outlines how to format the PIR
correctly to put into Confluence. It's going to use the Atlassian MCP server
integration in order to upload that PIR. We'll just let this go for a sec. Okay, so here we can see that the agent has
responded that it created the PIR and it uploaded it into my Confluence workspace, and we can click the direct link
into the PIR if we want to review it. Here's what that looks like. We can see the PIR is formatted exactly
how it outlined and it includes a summary impact and full timeline based
off of both the investigation and the incident. So no matter where
people were collaborating in Slack, on mobile or in the UI, all of that context now exists in the
system that we need that information to be in. For our demo, we got to see Edward showing us in
Slack where you're working already, how we can interact with the assistant, which has access to our actual data
as well as our on-call information, our alert information, and can help us very quickly understand
the blast radius of any alerts that we're getting.
We also saw the new mobile app, which contains capabilities
expanding across IRM and assistant. And we saw how when we
declare an incident, we have
an AI investigation agent, which is automatically triggering, working to find that root cause for us
and then posting the updates so that everyone can see them. Finally, we saw how we can integrate in with
other tools to expand the workflow into our existing workflows to make sure that
we're meeting you where you are using MCP server integrations.

