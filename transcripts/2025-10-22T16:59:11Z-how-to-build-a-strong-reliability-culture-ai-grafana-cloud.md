# How to Build a Strong Reliability Culture | AI + Grafana Cloud

Published on 2025-10-22T16:59:11Z

## Description

Reliability isn't just about uptime — it's about culture. In this ObservabilityCON session, Devin Cheevers and Sonia Aguilar show ...

URL: https://www.youtube.com/watch?v=bzQzYuc_jDg

## Summary

In this session led by Devin, a product director, and Sonia, a software engineer at Grafana, the focus was on enhancing reliability culture within organizations, particularly through improvements in their Incident Response Management (IRM) product. They discussed the critical importance of reliability, emphasizing how outages can lead to substantial financial losses. The speakers outlined the interconnectedness of people, processes, and tools in fostering a robust reliability culture. Sonia demonstrated new features in the Grafana IRM, including enriched alerts, automated incident management, and the integration of AI to facilitate investigations and reduce alert fatigue. They highlighted the need for effective coordination during incidents and the importance of learning from past incidents through post-incident reviews. The session concluded with a roadmap for future developments in IRM and alerting features, encouraging attendees to assess their observability maturity and adopt best practices with Grafana's tools.

## Chapters

Here are the key moments from the livestream, along with their timestamps:

00:00:00 Introductions by Devin and Sonia  
00:02:15 Importance of reliability and potential financial impact of outages  
00:05:30 Discussion on the challenges of incident response and alert noise  
00:10:00 Audience interaction on current alert and incident processes  
00:15:45 Introduction to Grafana's integrated incident response management (IRM)  
00:20:30 Demo begins: handling an incident as an on-call engineer  
00:25:00 New features: enriching alerts with logs and investigation links  
00:30:00 Coordination tools: creating Slack channels and Google Meet rooms  
00:35:15 Overview of the post-incident review (PIR) document creation  
00:40:00 Introduction of AI features for incident management and alert fatigue reduction  
00:45:00 Recap of demo and future roadmap for Grafana IRM enhancements  
00:50:30 Call to action: using the observability maturity framework and available tools  

Feel free to use this summary to navigate the key points discussed in the livestream!

# Improving Reliability Culture at Grafana

**Devin:** Hi everyone, I'm Devin, one of the product directors here at Grafana.  
**Sonia:** I'm Sonia, one of the software engineers here at Grafana.  

I know it's the last session, so hopefully, we're going to bring it home strong. Today, we’re focused on culture, specifically how to improve your reliability culture. We’ll discuss some of the improvements we've made to our Incident Response Management (IRM) product, SLO and alerting product, and showcase some AI features in the context of alerts.

You’ve likely heard this a lot this week, and it’s a common theme in the industry: reliability is paramount for many people in this room. You use Grafana to build reliable systems, and when an outage happens, it can have major financial consequences. Some estimates calculate the cost of an outage at up to $10,000 per minute. A 30-minute outage can lead to a significant amount of money lost. 

We’re all dealing with competing forces when trying to build more reliability. For example, improving communication during an incident is crucial, both externally and internally. You want to manage performance issues while minimizing downtime and keeping your team productive, shipping more often, and avoiding data loss. 

Another consideration is the rise of AI code generation tools. While they can help us move faster, they also increase risk since code may be written by AI instead of humans. This raises questions about the ease of debugging when an outage occurs. We believe this shift towards AI code generation highlights the increased importance of observability and improved incident response. 

However, enhancing reliability is not solely a financial issue. While money helps, the real focus should be on culture. We break down culture into three components: **people**, **processes**, and **tools**. These elements intermix, and we believe that effective tools can help you hire and retain great people. The right processes influence tools, and vice versa. As a tool builder, we aim to create great tools to enhance your culture.

### Audience Engagement

Now, I’d like to ask a few questions to see how everyone is handling challenges related to incident response. 

1. **Alerts:** Who here feels that alert gaps and alert noise are a non-issue?  
   * (No hands raised)

2. **Incident Process:** When you think about your incident process, who feels that creating an incident is as routine as creating a pull request?  
   * (Only about four hands raised)

3. **Learning:** If I asked a random engineer on your team whether they feel they are learning from incidents and have a post-incident review process, who would say yes?  
   * (About ten hands raised)

4. **AI:** Who here is currently using AI for any sort of remediation or automation?  
   * (About two or three hands raised)

These responses align with our annual observability survey, which found that around one-third of respondents identified alert fatigue as the number one obstacle to incident response. Other challenges included the lack of an incident response process, coordination issues, and difficulties in learning from incidents. 

We believe that fragmentation—particularly tool fragmentation—can amplify these problems. When engineers use multiple tools, context switching can lead to pain points. Post-incident reviews can become challenging if data must be moved between different tools, and sometimes you may be paying for users who barely use certain products. 

We think our observability native IRM is uniquely positioned to tackle these issues. We offer an end-to-end platform that includes alerts, SLOs, and features that help detect issues on the response side. With Grafana IRM, you can route alerts to the correct team and have strong scheduling and escalation tools. We’re also excited to show you some enrichment features we’re delivering this week.

### Demo by Sonia

**Sonia:** Now, let’s imagine a scenario where I’m the on-call engineer, and I’ve just received a notification about an outage at 4:00 AM.  

Here in the IRM app, we can see the alert that just came in. We’re holding off on declaring the incident until we investigate the severity of the problem. Let's check the labels—it's related to the payment service, which is concerning. 

Now, we've added a new feature to enrich notifications with logs. This means that when the alert fires, it can include additional context, such as logs, before the notification is sent out. 

As I check the logs, I see that the payment service is experiencing several failures with Stripe, impacting multiple regions. This critical information informs my decision to declare an incident. 

Additionally, we have a link to an investigation that started in the background as soon as the alert fired. By the time I officially declare the incident, I already have a head start on the investigation, which saves us critical time. 

Let me go ahead and declare the incident, adding relevant labels about the customers affected. Now, I’ll switch to my web browser to view the incident we just declared. 

When we declare an incident, several things happen automatically to support workflows:
- A post-incident review document is created, which will be filled out as we resolve the incident.
- A Google Meet room is set up for virtual collaboration.
- A Slack channel is created for responders to share findings.

Defining roles during an incident is crucial for clarifying responsibilities. I’ll assign myself as the commander and assign Brandon, who is familiar with the service. I can also page Dimitry and the relevant team members to start investigating the problem. 

The **timeline** feature is very useful for new joiners to track the incident's progress. It's connected to the Slack channel, so any messages in the timeline are pulled into Slack and vice versa. 

We also have a feature for status updates, which keeps stakeholders informed about important milestones and decisions during the incident. 

Now, regarding the investigation link I mentioned earlier, let’s check it out. The investigation is complete, providing us with root causes and recommendations, such as implementing a circuit breaker. 

Once we fix the issue and understand the root cause, it’s essential to create tasks from the incident to make it actionable. We can even convert these tasks into GitHub issues for future tracking. 

As we resolve the incident, we have an OpenAI integration that generates a summary based on the timeline, which helps streamline the process. 

### Service Center and Operational Reviews

Now, let’s fast forward to a week later during the operational review for the payment service. In the **Service Center**, we can see how this service is performing, including the number of incidents over the last seven days and SLO performance. 

We also have the ability to create SLO reports, which are great for operational excellence reviews. 

Addressing alert fatigue is critical since it can lead to missed incidents and delayed responses. We recommend moving most alerts to SLOs to reduce this fatigue and focus on what truly matters. 

Flapping alerts can also contribute to alert fatigue. Our alert state history allows us to track alert activity, and we’ve added an AI button that analyzes patterns in alert behavior and provides actionable insights.

Finally, creating notification templates can be challenging due to the complexity of go templating. We’ve added an AI button that simplifies this process, allowing users to generate templates more easily.

### Closing Remarks

**Devin:** Nice job, Sonia! To recap, we’ve covered the alert lifecycle through Grafana Cloud, including how alerts are enriched with log lines and how the Assistant Investigation feature works. 

We discussed the importance of coordination and how our tools can facilitate that during incident resolution. We highlighted features like status updates, AI debugging, and the automatic creation of PIR documents.

Looking ahead, we are focused on enhancing workflows in Grafana IRM and integrating third-party tools. We continue to invest in Grafana alerting, improving triage capabilities, and providing support for operational reviews.

In conclusion, building a great engineering culture involves recognizing that effective IRM is fundamentally a cultural problem. Your tools should be closely aligned with your observability data to facilitate this. We maintain a philosophy of keeping humans in the loop as we develop AI features.

What’s next? We encourage you to explore our observability maturity framework on our website to assess your current stage. If you’re in the early stages, try out our SLOs product included in Grafana Cloud. If you’re a bit more advanced, consider operational reviews and the PIR process.

Thank you for your attention! We’ll now open the floor for Q&A.

## Raw YouTube Transcript

Hi everyone, I'm Devin, one of the
product directors here at Grafana. I'm Sonia, one of the software
engineers here at Grafana. I know it's the last session, so hopefully
we're going to bring it home strong. We're focused today in this session on
talking about culture and specifically how to improve your reliability culture. We're going to focus on some
of the improvements we've
made to our IRM product, SLO and alerting product and also show
some of the AI features in a different light in the context of an alert. I know you've heard this a lot this
week, you hear it a lot in the industry, but reliability is of course paramount
for many people in this room. I know you use Grafana in part
to build reliable systems and when an outage happens it can
have major financial consequences. I was doing some prep for this talk
and obviously there's a wide range of estimates, but some estimates calculated
at up to $10,000 a minute for an outage.
So a 30 minute outage, that's a significant amount of money
and I know we're all dealing with a lot of competing forces in terms of
trying to build more reliability. On the right side there, you've got things like how to improve
your communication during an incident. How do you do that externally? Internally you're obviously trying to
manage performance issues just generally and you want to minimize
downtime at the same time. Obviously you want to keep your
team productive, ship more often, avoid data loss. And a new wrinkle, I know you've heard a
lot about it this week, but we are all experimenting I think, or many of us are experimenting
with Code Gen tools and that in some cases is helping us move faster, but it's also potentially increasing the
risk there's code that's being written not by humans. Does that increase the risk of not
having it easily debugged when an outage happens? And so we definitely
think this move to AI Code Gen is increasing the importance of
observability and then better and improved incident response. And it's not just
something that you can solve with money. Money helps, don't get me
wrong, but it's more than that. So it's really about culture and one of
the ways that we think about culture, I know it can mean many different things, but in this context we're
breaking it into three components. People, processes and tools and all of
these three things obviously play together. They intermix and we really
believe that tools can help you hire great people. Obviously they
can help you keep great people. You want to have the right processes
and processes influence tools and tools influence processes obviously. And ultimately we are a tool builder as
a company and we want to build obviously great tools for you to help improve your
culture. So I'm going to do a quick, I think four questions for
the room. So hang with me. See how everyone's dealing with some
of these challenges that come around incident response. So
starting with alerts. So who here would raise their hand
and say, really we have no alert gaps, alert noise is a non-issue,
complete non-issue. Okay, zero. Incident process.
Maybe this one's a little easier. So when you're thinking
about incident process, and let's say I went to
someone on your team, a random engineer on
your team and ask them is creating an incident, I mean it's not going to be completely
as easy as creating a PR or emotionally, but it's pretty close in terms
of a pull request versus an incident creation. Who feels like their organization is at
a place where creating an incident is pretty routine, mundane, in
terms of just getting it started? Who here would raise your hand and say
yes? Alright, I got 1, 2, 3, 4. Okay, four people. What about learning? If I again went to an engineer
on your team and asked them, they we're doing pretty
good. Most incidents, we do some follow-up items. We have a PIR post-incident review type
process and we feel like we're actually learning from most of our incidents.
Who here feels like that's happening? Alright, that's probably the best in
terms of count response, maybe 10. And then AI of course. Who here is using AI to do any sort
of remediation automation currently? Okay, about two or three. So this matches pretty
close to what we saw in an observability survey that we do an
observability survey every year, and it's a fairly large survey. It's about a third of folks
said the number one obstacle
to incident response is alert fatigue. So that
matched, I think everyone, no one raised their hand in terms
of that being a solved problem. And then pretty close
follow up in the next three. So about 17% just not having
an incident response process. 16% was really focused on the coordination
being the number one obstacle, pain across coordination
and then about 15% on the process or culture on learning and
improving from incidents. So we think, and a lens that we bring
to this is that fragmentation, in particular tool fragmentation,
can amplify these problems. So during incidents, if your
engineers are using multiple tools, they are switching context,
they are using different UI, different ergonomics that can
amplify some of this pain. The post-incident review
actually doing it. Sometimes that can be harder if you're
jumping between different tools, trying to move data
between different tools. And then sometimes if you're using
certain point solutions in this space, you may be paying for users that
don't even use the product and maybe ultimately funding features
that your teams barely touch. So we believe that observability native
IRM is uniquely positioned to help tackle some of these problems and we're
one of the few vendors that actually offer this today in the market.
We have an end-to-end platform, so we have alerts, SLOs, some features that Sonia is going to
show in a minute that help you better detect issues on the response
side with the Grafana IRM, you can route to the correct team, you can schedule to have a strong
scheduling and escalation tooling. And then we're going to show off some
enrichment features that we're delivering this week. On the more learned side and
sort of actual response side, we have Assistant Investigations,
which we've seen a lot of. We have some workflow tools
and then we have obviously help around post-incident review
processes and then using data to improve your culture with things
like Service Center. So with that, I'm going to hand it over to Sonia
that's going to show you a demo of these features and some of the highlights from
the last six months of work we've done. Okay, so let's imagine on a scenario, I'm the oncall engineer today and of
course right when I least expected, we've got an outage. So, it's 4:00 AM and I just received
a notification on my phone. Now I can show you here
we have the IRM app and here we have the
alert that just came in. We are holding off on declaring the
incident because we want to investigate a bit how serious a problem is.
Let's take a look to the labels. Okay, is the payment
service, that's not good. Wait, here we have something
new. We have some logs. This is a new feature. Now we have the ability
to enrich notifications. We can enrich notifications
by adding new labels, new annotations, or by querying
metrics, logs, or external services. For this demo, I created an
enrichment for this particular rule, adding these logs. This means
that once the alert starts firing, before the notification is sent, we enrich this notification
with this additional context, these logs.
So let's take a look to these logs. Okay. As you can see here, these logs are telling me that the
payment service is experiencing several failures with Stripe. And this is impacting multiple regions. This information is critical for me
to determine that I want to declare an incident. But before that, let
me show you something else. If we scroll down here,
here we have a link. This is an enrichment and this links to an investigation that
already started in the background once the alert started fighting. What's really powerful here is that by
the time I'm officially declaring the incident, I already have a head start
on the investigation and this can save us critical minutes
when customers are impacted. So I'm going to go ahead
and declare the incident. Let me copy from notes, description, okay? And we are going to add a
customer's affected label and it's critical and let's incident created. Okay, I'm going to grab a
coffee and open my laptop. So let's switch to the web browser. Okay, here we have the
incident that we just declared. There's a bunch of things
that we automatically create
for you in order to help out with your workflows. For example, we create a post-incident review document that at this point it's
just on a skeleton, but it's going to be felt out as
we progress through the resolution. We also create a Google Meet room
in order to have a virtual room. And lastly, we create a Slack channel
for responders to share their findings. One important thing when running
incidents is defining the roles. Because roles help
clarify responsibilities. The whole team knows who
is responsible of what. So I'm going to assign myself as a commander and I'm going to assign
Brandon that I know that is very familiar with this service. And you can page people directly.
I'm going to page Dimitry and you can also page teams. I'm going to page this team.
When you are paging a team, you're actually paging the person who
is on call in this team and these paged people are going to start
investigating the problem. Let's go to the timeline. Timeline is super useful for you new
joiners to have a picture of what's going on in the incident, but we also have, and this timeline is connected with
the Slack channel that we already created. So all the messages that you put
in here in the timeline are pulled them into the Slack channel and at the
same time the message that you put in the slack channel when someone
reacts with the robot emoji, this message is pulled into the timeline. We also have the ability to track updates. Status updates are designed
for stakeholders to be informed about the important milestones,
important decisions, and important changes during the incident. So let's make sure we
add our findings so far, our important findings so far and copy from the notes. Okay, I'm not going to change
the status nor the severity. Nice. Now do you remember that I mentioned
a link to investigation that the started once, the alert started firing?. Let's go to the links and context tab. Here we have the link
to the investigation. Let's take a look to this investigation. Nice. As you can see here, the
investigation is completed. This is good because we are very nervous
and we don't have to wait for it. And this investigation is going to
help us to understand the root causes and it's giving us some recommendations
in this case. As you can see, confirm it, Stripe payment
provider, timeout, cascade, and it's giving us some
recommendations like implementing a circuit breaker. You can also click here to the assistant
button if you want to follow up with more questions regarding this
investigation and you can take a look to the details of the investigation. Okay, so let's imagine that
we have fixed the issue, we understand the root cause,
we have some recommendations, but before coming back to our incident,
let me show you a new feature. Now if you press command plus I, you can see my cursor now is a cross. We can do a screenshot of
this because we think it's important and now we select our incident. This one and this screenshot
is going to be attached to our timeline. This is a new feature. Nice. Let's come back to our incident. And here you can see the
screenshot that we just took. Nice. So time to resolve
the incident, right? But we believe that it's not just about
solving the incident but also making sure that things improve. We can create tasks. Tasks, allow us to convert this
incident to something actionable. So let's create a task and you can convert this task to a
Github issue if you want to track it afterwards. Alright, time
to resolve the incident. Okay, so here we have a cool feature
is an open AI integration that is going to take the timeline as a context
and is going to generate a summary for us. As I mentioned before,
it's 4:00 AM I'm tired, so I'm going to use this feature. Life demo, we have errors
sometimes, but it's going to work nice. Let's append.
You can edit of course, but it looks pretty good,
so I'm going to resolve it. Incident resolved. Nice. Now let's change. Let's imagine another scenario. It's a week later and we are in the
team that owns this payment service and we are in the operational review. Let me show you. Service center, as I mentioned before, we believe that it's not just about
solving incidents but also learning from them, understanding trends
and iterating every week. In here you can see all the list of
services that we have in this system. Let's take a look to the payment service. In this page you can see at the
glance how this service is performing. You can see also who is on call, how many incidents happened
within the last seven days. You can see also how are
the SLOs performing If something is deteriorating, we have some links to some useful
dashboards regarding the SLOs. You can also see here the alerting activity
for the alerts that are related to the service and also
the activity of the alert groups related to the service. Speaking of SLOs, let me show you a new feature because now we have the
ability to create SLO reports. You can select the SLOs, then the time window. I'm
going to select weekly, and here we have the SLO report. So we believe that
service center SLO reports are great tools for operational
excellent reviews with your team. Now let's talk about alert fatigue
because we know that alert fatigue is one of the main reasons for missing
incidents and delayed responses. We highly recommend moving most
of your alerts to SLOs in order to reduce this alert fatigue and
also focus on what really matters. But we also know that one of the
reasons for having alert fatigue is having flapping alerts. This is the central alert state history
and here you can see at the glance the activity of your alerts. For this
demo, I created this flapping alert, as you can see is changing the
status constantly and we added this AI button with this AI button. This AI button
is an integration with assistant. It's going to take this list of events. We are doing some promt engineering and
we are injecting this to the assistant and assistant is going to analyze and
detect patterns and is going to give us some recommendations. Let's see what happens. As you can see here, assistant has
detected this flapping alert behavior and it's giving us some investigation
priorities, some insights, and some next steps. So in a few seconds we can detect
these kind of patterns and we can get also an actionable guidance to
reduce this all fatigue and focus on what really matters. Speaking of AI
buttons, let me show you the last feature. We know that one of the things
our users struggle with the most is creating notification
templates because it requires go templating knowledge
and sometimes this can be very hard. So then we decided to add this AI
button that when you click on it, you can create a notification
template being declarative instead of imperative. So you can ask,
I want a message like this. You can type in here or you can
pick one of the provided examples. I'm going to pick this one template that produce a message
like this and you click generate template. And here we have the
definition and the preview. We believe that this AI button is
going to help our users to reduce time and complexity when creating
notification templates. That's the demo. Back to you, Devin. Nice job, Sonia. Alright, so I'm just going to do a
quick recap of what we saw. It's the alert lifecycle through
Grafana Cloud. So the alert fired, you saw it get enriched with
log lines and also the Assistant Investigation. We think that's an obvious way that
observability native IRM is helping you. The alert was routed to the
right person in this case, Sonia, showed up on her phone. IRM,
our offering has really rich, powerful routing logic, and then the AI investigation
was triggered automatically. Again, an example of something that's
better with observability native, then we debugged it or Sonia debugged it
from her phone, declared the incident, and then did a bunch of coordination.
As we talked about earlier, coordination is a real
pain point for many teams. It's really beneficial if that tool or
the coordination is happening in the tool where your engineers are
already debugging. So we
showed you the status update feature. We showed you debugging with AI, and we showed you also using roles
to help coordinate. Then resolve, we created that, that PIR doc
was created automatically, and then we showed you using tasks to do
follow-up tasks that you can link with GitHub. Then switching from firefighting to
operational reviews or improving from what you've seen. We showed off
Service Center. That's a GA feature, showed you how you can use
Service Center to review trends. We also used some of Grafana Assistant
to run an analysis of your alerts to tune them, improve them both. Those things we feel do really well
when you're doing that on top of your observability platform.
So that was a demo. That was a bit of the setup and framing. I'm going to move a little bit into
roadmap and some action items for everyone in the room. So just some highlights,
not everything that's coming. But on the IRM side, we're really
focused in the near term on workflows. So today you can use
webhooks within Grafana IRM, we're ready to integrate
it with third party tools. We want to make a far richer offering
around workflows that's more flexible. Obviously that could benefit
also any agentic workflows. The Grafana AI investigations feature, we're moving rapidly hoping to GA it
soon and continue to invest there and integrate it into Grafana IRM.
And then on alerting. So alerting, we know many of you use Grafana
alerting. Maybe you're not using IRM yet. Maybe you're not using AI. We continue
to invest in Grafana alerting, including coming soon improvements
to how we're helping you triage your alerts. So yeah, sort of three takeaways. We really do believe that building a
great engineering culture includes, I'm sorry, building effective IRM
is a cultural problem. Your tooling, we believe if it's as close to your
observability data as possible, it can really help. And a design philosophy around
AI is obviously. Not obviously, it's keeping humans in the loop. That's a fundamental principle that
we're using within Grafana development. What to do next? So we do have a observability maturity
framework that you can see on our website. And take a questionnaire
and understand where you're at. If you're a little bit more on the earlier
stage of your observability journey, what we would call the reactive stage. Highly encourage you to
check out our SLOs product. It's included in Grafana Cloud. Potentially get a beachhead
team to try that out. Grafana Assistant is fantastic in terms
of helping teams adopt observability best practices and use Grafana. If you're a little bit more
towards the proactive stage, maybe you've got SLOs set up, maybe you're doing some of
the early stages of incident processes. Consider operational
reviews, consider using Service Center. And then yeah, the PIR process. We've found a lot of value internally
at Grafana and with our customers on improving that. Finally,
on the systematic stage, we do have an MCP server out. We do have Grafana Assistant and
we have Assistant Investigations. So we'd love to work with you on using
that as you move to more of agentic workflows. And I don't know if we
have time, but with that, with Q+A, thanks so much.

