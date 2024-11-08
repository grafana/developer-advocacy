# Demo: Incident Response Management (IRM) Solution in Grafana Cloud | ObservabilityCON 2024

This video explores Grafana Cloud's Incident Response Management (IRM) solution. Learn how to streamline your incident ...

Published on 2024-10-24T19:51:55Z

URL: https://www.youtube.com/watch?v=yyNV4WFsgY8

Transcript: Welcome everyone to a User's
Guide to Grafana Cloud's... Oh, right. I need this. Grafana
Cloud's end-to-end IRM solution. Sarah Kaplan. I am the
manager for the SLO team. Hey, I'm Devin, one of the
product directors here at Grafana. And Devin is actually gonna walk
us through the IRM solution. But first we're gonna take a little time
and talk about what end-to-end means. Logistics. You guys know
the drill? Snap a pic. Put in your questions. We'll get
to some of them at the end. Okay. Can I get a thumbs up
if your engineers, you, your engineers are comfortable
opening a pull request? Yeah. I should see almost every thumb up.
I, I really hope. Yeah, right. Okay. Keep it up. If they're just as
comfortable declaring an incident. Yeah, that, that one's a little harder.
I've grappled with that. Is this, is this really an instant? Do I wanna do this whole
process for this little thing? Maybe I just push a fix and no one
will know. That leads to bad things, bad things. So at Grafana
we want to enable, this is our view of end-to-end is we
want to enable your engineers to be as comfortable declaring an incident
as they are opening a PR. We believe this is essential so that
you continue to learn and improve your incident management processes.
So how do you do this? How do you make it a routine practice? Something that everyone is
comfortable doing? It's kind of hard, but very possible. It is a culture change because
it goes across tooling, process, and people, you need to be intentional in the
tooling you choose because you want this tooling to enable the
frictionless, easy, blameless, anxiety-free processes that you have
for pull requests because then the people get bought in. So we believe this is best
done with observability-native IRM. So for us, that means putting your incident
management processes right with your telemetry data, right next to it. You don't want your engineers to be looking at telemetry to determine if
there's an incident and then having to go somewhere else to declare it and then
come back here to investigate and then go back here to take notes. If it's all together, it enables
this lifecycle of an incident. This is the sweet spot where
you detect things early, you can respond quickly,
all the data's there. And then with the process embedded in it, you capture all of it to
then learn, prove detection, improve your response,
and the cycle continues. You heard a bit of that actually from
TeleTracking in the earlier call, right? PR's much easier. It enables you to learn more from 'em
and get that whole response better. However, if any part of
this cycle is broken, perhaps your customers are telling you
when there's a problem or it's hard to get the right people involved,
hard to find the data. Maybe you're doing your post incident
reports and making action items, but not actually doing those action
items. If any of these happen, you're in a reactive state.
This is where ACME finds itself every incident, they're diligent,
they create an alert for it, they create additional metrics and
logging, but that led to alert fatigue, huge number of alerts, what's
actually relevant. Too much data, hard to find what they need.
Same problems keep happening. So now Devin's gonna walk us through
how Grafana's IRM solution helps them with all of this. Thank you Sarah. Okay, so I'm gonna
walk you through about a 15 minute demo. It's gonna be based on a scenario where
a team is owning the payment service. They're gonna set up an
SLO on the payment service. They're actually going to then respond
to an issue with that and learn from it. Okay, so we're starting off
with the actual SLO builder, and this is in Grafana
Cloud. It's our SLO product. And one of the things we've done outta
the box is make it really easy to actually create the SLO with a guided UI. You can see five simple steps to
create the SLO and we start with defining our SLI. So
service level indicator. In this example, you can see
I've created the success metric, which is essentially a Prometheus
query that checks to see the number of requests that return successfully
in less than 200 milliseconds over total number of requests in
this case to the payment service. I'm gonna group that by cluster that will
probably give us relevant information maybe in the context of an outage
on what cluster is affected. Just a quick shout out to and reference
back to Asserts yesterday and today. Asserts also provides the ability to
create SLOs. And this is a separate UI, but it's built on top of the SLO platform. This is just another example of how we're
trying to bring more opinionation into Grafana Cloud. And you can see here you're guided on
both availability and latency SLOs from the Asserts side, but for now,
we're gonna stick with our, our general SLO builder and build
the SLI off of the Prometheus query. Next up, I am gonna set up the actual SLO
and corresponding error budget. I'm gonna go with about a 70%
target. That's pretty generous, but this SLI isn't performing that
well based on historical data. So I want to give the team some room
to improve that before they set a more aggressive SLO. We're also gonna name and describe the
SLO and add labels and labels are gonna be key. As many, many of you're familiar labels are
key across the Prometheus and Grafana ecosystem. They're actually gonna
be critical for this demo as well. We're gonna use that payment
label, that service name, which is payment to flow information,
both from SLOs to Grafana OnCall, and even into the dashboards that we
review to learn more from incidents. Finally, I'm gonna create an a rule, a set of alert rules off off this SLO. It's one click and you get a fast
burn and slow burn alert condition created for you. Again, another example of how we're making it
easy to get up and running with your SLO. Okay? So that essentially is
gonna have your SLO built for you. Let me show you what you get.
Once you've created that, you also get a dashboard and this prebuilt
dashboard is gonna help you obviously understand the performance of
the SLO over time, but it's, it should work right outta the
box after the creation point. So that's gonna give your team the
ability to see what's been happening, change the time window and maybe
even adjust that SLO at that moment, but they can go back and
revisit it over time. All right, one other example that I wanted to give
you you're of course gonna likely be creating static alert thresholds as well. And we're investing in Grafana
alerting ease of use in many places. And one recent release was
around improving the ability, leverage our notification policy
without having to do some complex label matching. And the way we've achieved that is through
the ability to just select a contact point in your alert rule creation. And that is actually gonna build the
notification policy in the background. In this case, I've selected an oncall
contact point essentially saying, for this alert rule, I wanna send
the alert to Grafana Oncall. Okay, that is a quick example of how we're
helping you on that detect part of the incident lifecycle. I'm
gonna move over to respond. One of the key parts of respond is getting
the right alert to the right person at the right time. And part of
that is your on-call schedule. We offer a product call Grafana
OnCall, which is part of Grafana IRM, and that allows you to
manage your schedules. Here is an example of a
schedule you can see up here. We actually show where your team is based
on their time zone at a glance you can tell their time zone and obviously that
can help in terms of making sure the on-call schedule is adhering to the
fact that they might be asleep or awake. We have some other
features as part of this, which is a quality score and
warnings around gaps in the schedule. And another example I wanted to highlight
is our request shift swap feature. So this is essentially making it really
easy for someone to sh swap a shift with someone on their team. Maybe they
have a dentist appointment coming up. You can come in here and hover over
your name, request a shift swap, and that's gonna invite someone on
the team to actually take their shift. But it's essentially an open invite that's
periodically pinging the team saying, Hey, Devin needs someone to take his
shift. Could you please take that shift? All right. I am gonna switch over to context
where we're actually responding to an alert group. I'm gonna
demo the mobile app. So we actually have a mobile
app if you didn't know. And this mobile app is gonna allow you
to understand various things including your recent alerts that have been
sent to you active incidents. You can actually also come
in and see your schedule. So this was that example
schedule I just showed. So really nice you can at a glance
understand if you're on call, see who else is on call. But
I am gonna jump back into the alert groups And show you an example of triggering
an incident directly from your phone. I created an issue but it
looked like it didn't fire, but we'll use this one
from a few hours ago. So this is an alert group that was sent
to me on actually the payment service SLO. I can look at the glance and see,
okay, well this is payment service. I know that this is a
key service for my users. I think I wanna declare an incident
proactively to get some help from my team and coordinate and see what's happening. So quickly say it looks
like there is an issue here with payment. I'm gonna say I think it's actually a
major issue right now because it affects customers. I'm add a couple labels to help coordinate
and we say customers are affected and now we're pretty good. Okay, so I've created the
incident really easily and I'm gonna switch over, oops, to desktop to finish the triage process. Ah. Live demo. No, I guess
I broke the internet. Or it's hardwired
actually. Yeah, maybe go. Back to wifi. I dunno. It's the mobile phone demo. Probably
broke it. All right, we're back. Maybe. I don't know any jokes. Do you? ?
There we go. I got a little laugh. Matt would be proud.
All right, here we go. Okay, so this was the issue I
just declared from my phone. So kind of key highlights
here. The incident product. I know TeleTracking did a great job
of explaining some of the value there, but we automatically run a number
of routine a number of actions to help your, your team and yourself if
you're, if you're running an incident, a PIR doc is created
automatically a bridge is created. We create a Slack room or an MS
teams room for the demo environment, we're using Slack. That's really helpful. That's gonna be part of helping getting
the incident declaration to be more routine, having some of this automation happen
and have your team not have to think about, well what doc do I create?
What room do I do I create? It's all done for you automatically. Another thing which you didn't get to see
the loading bar here, but that's fine, is Sift. So Sift is one of the key ways we're demonstrating
that observability native IRM message. What does that really mean? Well, Sift is an example of how we're using
your telemetry data in combination with the fact that you're running an
incident workflow in Grafana Cloud. To combine telemetry data with
the context of an incident. Better put probably is we run a series
of checks against your data in the context of this incident.
So it inherits the labels and we'll find interesting information
that may be relevant contributing causes. So this example we actually
find anomalies in your logs. So this is super useful. Customers find the log anomaly pattern
one exp extremely useful for the context of an incident. So you can see here we've found
four new patterns in the logs. Obviously get information on the
changes that's happening across the, the log patterns. We actually can help
explain the log itself and potentially give a user
remediation steps as well. If I, if I glance at this, I can tell
there's some issues with Postgres. It's gonna gimme some more explanation
here, so I think that's pretty relevant. So that's sift I'm probably over time. So I'm gonna also assign some roles and role as assignment is critical
part of incident response. It helps with coordination, it obviously helps with setting up
playbooks and guidance to your team on what to do if they
have a specific role. You can customize the roles in
Grafana incident. In this case, we're just gonna have a
commander and investigator. We also sync directly
with your chat platform. So we have a Slack integration
and an MS teams integration. We do things like if you write a note
here in the incident timeline that's directly translated into Slack
and or if you're using Slack, you can put that back into the timeline
as TeleTracking showed you just now. Okay that's a little bit around
the incident response aspect. I can also page and pull users
in directly through OnCall. So Ryan actually is someone that is really
familiar with the payment service and the underlying infrastructure. So I'm
gonna page him, I can also pull in teams. So let's pull in the app
environment team as well. So Ryan and the team will get paged and
the team will be the whoever is on call via the escalation chain that is
associated with the app environment team. Okay, I'm gonna go ahead
and resolve this issue. I think we've solved it
and move on to the learn aspect of the incident
lifecycle that Sarah mentioned. So as part of resolution
process and workflow, we actually provide the ability to auto
summarize what happened inside of the incident itself. So this is powered by OpenAI and
here you can see it's generated a quick summary of what it's seen
in the timeline. It's pretty good. There's not a lot of data actually
in the timeline right now, but I think it's done a decent job. Obviously you could edit this as you see
fit but that's just another example of how we're making it a little bit easier
for your team to start following a specific process around incidents. So
there we go. We've resolved the issue. And I'm gonna show you a couple other
examples of how we're helping you with the learn phase. So I didn't get
to highlight in the demo, but incident also provides
a task capability. It can create tasks with an incident. You can actually convert those
into GitHub issues automatically. And then we show you
here a central task list. So this is gonna help you track and
follow up on any tasks that you think are identified to prevent
the incident reoccurring. We're obviously syncing with GitHub
through that auto assignment piece. And then here you can also see tasks
if you want to centralize in Grafana incident, you have multiple options. Finally we have a number of dashboards
that I've shown you that we build out of the box to help you understand trends. One of these is the SLO
performance dashboard. This is showing your performance
across all your SLOs here. I've actually scoped it
to the payment service. We have lots of payment service SLOs
because it's the demo environment, but this is gonna give you a bird's
eye view across all your s SLOs. You can scope that to team
to service. And then finally both our oncall product and our incident
product come with a trends dashboard. This will show you trends across, in this case the number of people that
have been paged incident dashboard will show you trends across
incidents in this case. I can see that the payment service over
the last seven days has at about 14 alerts. It's been about
20 minutes for MTTR. And I can even go into the
squad and users that have been paged around this service. So that's gonna be a great starting point
to start to have conversations about where your alert and
on-call load is at all. It was a lot, it was quick, but that's,
it was a lot. That's the demo thanks to. Sarah. It was a true demo 'cause you
had a problem. . Okay, so yes, Devin went through a lot of stuff with us. And what I wanna just highlight a few
things is in our view of this end-to-end IRM process, we're embedding as many
best practices as we can to help you. You noticed he started with SLOs. Awesome. We make that easy in the cloud
and easy to alert on the SLOs. This is important because it allows
you to start your alerting journey, where if you have a lot of noisy alerts, hard to understand what is truly critical, you can start whiting those down and
have your alerts just based on your SLOs because those are keyed
off of customer impacting SLIs things, you know, affect customers. So it'll reduce the noise once
you're there. Oh, celebrate woo. And then you can start branching out
and you can add in predictive alerts. It'll get a little more noisy,
so be careful, but that, that'll give you even more
lead time to, to track issues. We saw respond best practices.
Super easy to declare an incident, almost like creating a pr. You can
get the right on-call people engaged. You have all the data you need right
there. Observability, native, IRM, you can have runbooks,
all the best practices. We try and embed it right
in there for you and learn. Teletracking talked about this
a lot with their PIR process. We try and help you gather as much
of the data as you need as easily as possible. In the keynote
yesterday, you saw incident rooms, automatic note taker,
awesome. All of this is coming and this helps you then
learn and get that, get that virtuous cycle going
and the insights help you look across all your incidents,
across the on-call schedules. Where are there problems? Are there
trends that you need to be aware of? Do you happen to have problems? Every
time there's a configuration change, you can start to, to find
some of these bigger things. So we help you at every stage. And our goal in this end-to-end
process is to get this flywheel going, this virtuous cycle. Here's an example. In addition to tele tracking of Clearco, a FinTech company company out
of Canada having a few problems, one alert fatigue common. They
also had hard to read alerts. It was a string of text and
they had a manual IRM process. So they moved off PagerDuty, oncall is now super happy and their
incident processes have greatly improved. You can read more about it on
our website. So where does, where does that leave us? It's
gonna be a culture change. It'll be well worth it to get this going. We believe your tooling should be as
close to your data as possible. Right now, Grafana is the only observability
native IRM solution out there. And that it is a continuous practice. If you wanna get started,
talk to your engineers, especially in the context
of detect, respond, learn. They know where the problems are. This
will give you an idea of where to start. And then find one team, team
willing to work with you, willing to iterate with
you, give you feedback, and get that success story going. So you've seen yesterday with
certs incredible tool to, to RCA to respond to an issue. We
saw incident rooms yesterday as well. A really exciting capability that's gonna
reduce toil and capture more context from the incident. Today, I know we had TeleTracking talk
about how they're using incident. We talked about the service
level explanation feature, and then you saw today in the brief
demo everything from SLO creation to incident response to on-call management
to even understanding your trends with multiple dashboards. So we're really
excited what we've done so far, helping you respond and
learn from incidents. And we think we're just getting started. So we're excited to partner with you
and look forward to building more great products and features with you. Woo. Okay.

