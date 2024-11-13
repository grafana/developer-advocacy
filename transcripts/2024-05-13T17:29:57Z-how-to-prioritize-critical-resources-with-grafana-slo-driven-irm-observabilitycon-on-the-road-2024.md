# How to Prioritize Critical Resources with Grafana SLO-driven IRM | ObservabilityCON on the Road 2024

New to Service Level Objectives (SLOs) and Service Level Indicators (SLIs)? Or curious how Grafana makes it easy to prioritize ...

Published on 2024-05-13T17:29:57Z

URL: https://www.youtube.com/watch?v=sD3Q9HRWwrw

Transcript: Alright, well thank you very much. The next presentation we have today is
really about SLO Driven Incident Response Management. Something I'm super passionate about and
hopefully you will be as well as we go through this. So, my name
is Marc Chipouras from Boulder, Colorado. I'm a senior director
of engineering here at Grafana Labs. I'm super passionate about observability
specifically 'cause we get to build tools to help engineers solve problems. And really what we need in the world
is actually that - solving problems. And I feel like I can be a part of
actually making it better for other teams that are out there, which is really good. I'm also a dad and I love
exploring the outdoors. Yeah. And hi, I'm Mimi Schatz. I'm
the engineering manager for IRM. Specifically focused on our incident
response management platform. When I'm not at work, you can find me taking advantage
of California's outdoor activities, much like Marc - biking, hiking,
skiing, surfing, you name it. She says surfing. She just started
surfing. She's just getting into it. Alright we're gonna take
a quick show of hands. Who is using SLOs in your
engineering culture today? Okay, maybe we're about a third. Alright, for the people who are using SLOs we're
gonna help give you some ideas on how you can make your SLOs better and help
them to drive your engineering culture. And for the rest of you, hopefully we can give you an introduction
on how they could be used and you get your teams moving in the
right direction here. Alright, we're gonna talk a little
bit about reliability, why reliability and
performance are important. We'll talk about how do you
choose great SLIs for your teams. We'll talk a little bit about how we
are building SLOs here at Grafana in our engineering culture. And then we're gonna step into a demo
on how you might be able to do some of these things in Grafana
Cloud today. Right? So let's talk about why we're here. Again, I talked about we love to build
engineering tools in order to support your teams. And what we like to do is actually bring
some of our high performing engineering culture from Grafana into the room to
share both into our products as well as with your teams today. We're helping want to build exceptional
production reliability for your teams. So what does that mean? What
does production reliability
actually mean? Well, first of all incidents
are going to happen. Like the goal here is not to eliminate
an incidents from your system. That's really an impossibility
to do. And, you know, maybe it's undesirable to eliminate
incidents entirely from your production system. It's a great opportunity for you to learn
how things are actually happening in production versus how you thought
they were going on in production. But it's really important and we wanna
work with you so that you can detect issues before your customers do. It's really important to identify and
resolve before somebody gets on the call with you. And that's really what we want to try
to do when we talk about incidents. And we're trying to help build
a culture so your engineers can, don't have to be reactive to everything
that's happening in production, but we can find the things that are
important that are happening in production and that's when they can be proactive
to respond to those issues, right? And this really helps us help build
healthier services running in production, but more importantly, a healthier culture for your engineers
and your product team as well as your customers moving forward. It's not just about
reliability and being up. Reliability is really about
performance as well. I mean, we see time and time again
that performance of your
system is as important as the availability of your system when
you're actually delivering your product, right? These are some stats here
from a recent e-commerce study. Basically two out of three
customers bounce if your
latency is over six seconds, half of your mobile users were bouncing.
If the latency is over three seconds, I guess our partner Embrace here, they could probably tell you all about
mobile monitoring and how true that is as well. But probably you've also
seen that 45% of you can see an improvement in the conversion of
your e-commerce payments with a higher performance or lower latency
as we're going through this. So service slowdown is really
important, as important as availability. So with this information, how
do we actually choose our SLIs? Plain and simple, the goal of an SLI is to measure the
service reliability and performance your customers are experiencing. So we're gonna step a little bit into
some vocabulary here for everybody. So the first one here is SLI,
I guess I keep using this word. We might as well bring it in.
It's a service level indicator. This is the measure of reliability
and performance for your site as, or your application,
whatever we're measuring. This is the actual measurement
usually expressed as a percentage of successful in performance
requests over the total. So it's a percentage and indicator
of how your service is performing. Service level objective is a
goal that we're going to apply to that service level indicator. So here is our performance of what we're
seeing of our measure of reliability and performance. And here's
what we're trying to hit, right? Incidents will always happen. You aren't always going to be a
hundred percent within your service. So you always wanna set your SLO in
something that's achievable for your team. So the SLO is the goal that
we're measuring up against. And the final thing
here is an error budget. An error budget is a way that we can
actually bring the service level indicator and the service level objective together
to understand how they're performing against each other over time. Our error budget looks to see how are
we meeting our service level objective over the last five minutes,
the last day, the last week. And we can make decisions about how we
might want to invest in the performance of our systems or maybe investing
more in our features based on how we're hitting on our, or we're burning down our or not
burning down our error budget. Alright, let's break this down. What
makes a great SLI? You may be, "We're gonna start with SLIs. I'm
gonna go ahead and ask my engineer. I need a service level indicator for my
service to make sure thatwe're meeting our customer needs and they're gonna come
back with maybe something like this." Well, we can measure to
see if the service is up. I'm gonna look up a Prometheus
up down number for that. And that that's something that's
actually going to indicate whether we're meeting our customer's needs or
maybe the service is accessible, we can actually reach it from
the outside through the gateway. Maybe their response is about the service
is responding in a performant manner. We're looking at the latency
of the service, right? And maybe the responses from
that services are valid. We're actually sending a valid
measurement back. It's actual JSON. It's actually the login. What we need. This is really looking at the indicators
of the health of your service from an internal view. It's not looking
at it from the external view, but it's looking at it from an
internal view. And you know what, it's okay to start with an SLI based on
this because this is the conversation you're having with your engineer. We can say this is something I can work
with here and let's see where we can move forward with that. 'cause SLIs are iterative and you'll
constantly involve them over time. So what we don't wanna do is have a
measurement for each single one of these things because the, it may be spurious and actually not
showing a real customer value for each one of the things. So the first thing we want to do is we
actually want to measure many things at once using one measurement. And
this is a key component of an SLI, it's actually going to measure
multiple things at once. So I put in an example of how we might
turn this into an SLI and let's see, request to the API provide a
valid response. That's great. If we can measure request to the
API, we have a valid response, well now we know the responses are valid
and we definitely know that the service is up, right? Because we are, we're
sending valid responses, right? We've kind of hit two of those things. If we start to say only the
responses that are happening within, in this case 250 milliseconds, we've added a latency and we can say
that we were responding in a performant manner and we're hitting
three of these measurements. And if I filter that down further to
only look at requests that are coming through the gateway, I've actually now created
a single measurement that
covers the four aspects of what we were putting into our
SLI. We can say the service is up, the service is accessible, it's responding in a performant
manner and the responses are valid. So we took it, measured many things at once and actually
brought it to a single measurement and that really empowers the measurement to
be more and more important for us as a user or for the engineer to respond to. But the problem we have here is it's
actually not representing customer value. The next step that we need to do to
convert an SLI into something that is representing business value is to tie
it to something that's happening for the customer. Something that's
really, really important. Now, if we are actually to look at that SLI
with those four measurements and filter that just to, is my login successful? All of a sudden I have a single
measurement measuring four things that's actually tied to a successful business
measure, which is can users log in? And that's something that your
engineering team will care about, your product team will care about and
the leaders across your company will care about. And this is part and
parcel to making a great SLI, we could do this for the
same thing for the payment. Is the payment going through successful
in a performant and valid way? Or is my shopping cart actually current?
So we can take these multiple measures, tie 'em into one as an SLI, and actually
tie them back to customer value. And that's really important
from an SLI standpoint. The next part about building great
SLIs happens to do with error budgets. So we now have an SLI, we're
measuring multiple things at once. We've tied it to customer
value. What do we do with that? The key point here is when we
are looking at an error budget, it can see how we're performing
against that SLO over time. And I as an engineer or
you as a product leader, can start to make decisions on how we
need to respond to that based on how we're meeting that objective. If I'm
burning through my error budget very, very quickly, I know as an
engineer this is important. We have a problem with a customer facing
measurement that is not functioning and I need to jump on this quickly.
It's not a, "Well the CPU is high, I don't need to know if I need to respond
or not." I know that this is a valid business measure and I need
to respond to it quickly. Or in this case you can see the error
budget is trending down slowly over time, over the course of a month. This is not something that needs
an urgent response to a page, but something that I can actually
schedule to happen during my normal engineering process and we
can solve during the day which is really the big, the big
change that SLOs really provide us. It gives us the ability to talk to
this as a measure between product and engineering and choose
the urgency to address it. Overall, SLOs are going to provide improved
reliability for our service because we're really measuring the SLI of what's
actually happening from a customer's perspective, which leads
to happier customers, which everybody in an
organization is gonna want. It provides better data-driven
decision making in order to prioritize engineering resources, whether those are on-call resources
or feature building resources, which leads to happier engineers
and maybe happier product team, but maybe they're less important, but more importantly for
your whole organization, it's gonna lead to fewer surprises. And
that's really what we're trying to do, trying to be consistent about
how we're delivering as a team. So with that, I'm gonna take a moment.
We're gonna introduce Grafana SLO. This is available in Grafana Cloud today. And it is the tooling that we're
providing to codify everything about SLIs, SLOs, and error budgets together to make it
super easy for you and your team to pick up this engineering practice. So it's available on all
tiers in Grafana Cloud. It's a step-by-step process where you
can provide a specific measure that you want it or multiple measures
that you want to be your SLI. It will automatically guide you through
the process of selecting the best SLO that you think we can
even meet for your SLI. And then it will automatically build the
fast and the slow burn down alerts and as well as the error budgets for your
team as we're moving through this. On top of that, we're gonna go ahead and
automatically build the visualizations, which actually provide the
piece of information you're
gonna use to collaborate and speak to for your team, right?
So we have visualization of your SLI, how it's performing over time,
how the, we can use these in operational excellence
reviews for your teams. And then we'll also have detailed
views into the error budgets as well. But that's all slideware. I wanna hand it over to Mimi here who's
actually going to step into a demo of how we can build an SLI inside of Grafana
Cloud today and how that fits into an incident response management
process. So thank you very much. Thanks. so as Jen said, nothing like doing a live demo and I am
also the thing standing between you and lunch. So try and keep this, keep this
moving. All right, so thank you Mark. The first thing we're gonna do is he
said is we're gonna create an SLO. We're gonna do that right
here within Grafana, as he's mentioned we have this really
nice workflow built in here for you. So it's five steps. We auto-populate
a lot of this information for you. And then I'm just gonna
walk us through, so yeah, defining our service level indicator.
It's how we're gonna measure our SLO. We have a time window of 28 days. And
then you can select from your data source. Both of these things are configurable, but I'm just gonna leave them as they
are. So for building our query we have two options here. One: advanced for those of you
who are significantly more
comfortable with PromQL - that is not me. So I am
gonna use our ratio query. We're gonna be looking at response
time for our mythical application. So I'm just gonna pull that up
in our request times bucket. Specifically curious about
our production name space. And you can see this just
auto-filling for you. Looking at responses that
are less than or equal to 200 milliseconds. And then filtering out for status 500, I guess filter out. So that's
gonna be our success metric. And now for our total metric,
looking at our, again, for the mythical times our
request times count and limiting that to our production namespace.
Now this is pretty good, but I'm actually a member
of our payments team. I don't really care about a lot of
the other endpoints this will pull in. So I'm actually gonna limit this
a little bit further and set it just for our payment and do that down here as well. And you can see in the auto fill like
the other endpoints that are available to you. Alright, so I'm feeling
pretty good about that. The last thing we can do
is we can do some grouping. I'm gonna group this by cluster. I know that the service is deployed
in a couple different places. And I'm simply just
gonna write cluster here. And now we have this dimensionalized, SLO. So with a click of run queries for
those of you who prefer your PromQL, the full query is visible. And then we have below the expectation
for how this SLI will perform. So as you move your cursor across the top, you can see for each one of our
clusters a value that's presented on a scale of zero to one, so
this one being 9.932. Okay. So with that set, the
next thing I'm gonna do, I'm gonna click through and we're
gonna set a target and an error budget. By default we say we provide 99.5, but you can adjust this as we also
give you a preview for how this will perform. As you can see,
this would not go very well. So I'm just gonna adjust this
down. I'm gonna be generous and set my error targeted
about 70%. The graph updates. I feel pretty confident that this is
something that our team can meet at this point. Our expectation with these are
you will update them as you improve your service. These
are not set to be stagnant, but rather things that you will
adapt over time. All right, so next step - gonna add a
name and description. You know, I don't want you to have
to see me type everything. So I'm just gonna grab a
predefined name for our payment service response time, SLO. And then a nice descriptor. For here, the expectation is this is
something that's going to
be visible to other people, something that can easily pick up
what this SLO is doing. So for here, use a request to the payment service
that are successful and under 200 milliseconds. Lastly, we suggest attaching
two labels to your SLOs. You can also customize this
and add additional ones. But we recommend team
name and service name. So I'm gonna go ahead and attach the core banking team to this.
And the service is payments. All right, so we're
three steps in two to go. The next is adding an SLO alert
rule. So we've defined this SLO, but we don't have any alert rules
set around it. So at this point, it's not the most actionable. We
make this really easy for you. You can just click the checkbox and we
are going to create two rules for you. You can dig into the details here, but out of the box we have a fast burn
alert rule and a slow burn - fast over a shorter period of time, something that we would expect
to page out to someone on call, declare an incident and slow burn
over a longer period of time. Probably something that can be handled
within work hours needs to be addressed, but not necessarily a fire. So with
that, I'm gonna review the SLO. All the information we've
just put in is now listed. You can kind of confirm and
go back and edit if you need. And then I'm gonna save. And so here we have our back to our
list of SLOs. For every SLO we create, as Mark pointed out, we also
create a dashboard by default. So here is the dashboard for our
payment service response time. SLO. You can see here at the top we've
got the time window that we defined. We have the SLO we defined and how
it's been performing over the last 28 days. You can adjust the time
period like on most of our dashboards. You can adjust the time period
up here in the upper right. And then you can see, well, we
already have two alerts going. In addition to creating a
dashboard for every SLO, we also append every SLO
to an overview dashboard. So this would be something, so across your department you can kind
of keep a bird's eye view on what's happening. You know, Dave Moore's test
here, it's really not going very well. Probably have something to address. Okay, so now we've kind of gotten the lay
of the land. We've created our SLO, we've defined an SLI for that and we've
associated some alert rules to it. When your alert fires, it's
gonna route through Oncall, our on-call product. And from there we're gonna send out
notifications to however you have that set up. That could be Slack, MS teams,
to your mobile, to the mobile app. And so for today we're
gonna pop over to Slack and we're gonna see here, here we have our payment service
response time SLO that's fired. It's been piped into our ops demo
alerts channel and with it comes a variety of information.
The team, the cluster, the service and also links out
for additional information. But because I know that this is the fast
burn I'm gonna go ahead and declare an incident because we've gotta get on this. And so with that, we're back into Grafana. And we've carried over with it for our
name. The name pulled from the alert. We can go ahead and set the severity. I'm actually gonna leave
it as undetermined 'cause
I don't really have much clarity yet. And I'm gonna go ahead and add
a label for the payments team to make sure that they're aware that
this gets associated to the team. Alright, so we've declared our incident. There's a bunch of things that we do
automatically for you to kind of help standardize your workflow. And
before I kind of get into that, I'm gonna go ahead and assign
a commander and an investigator so they can kind of take the reins
while I'm doing this. Oh boy, you're gonna be busy now. Yeah,
 oh, he's not available. Chris, are you here?
There we go. All right. So Mark's the commander. I've
assigned Chris as my investigator. And Chris, you gotta get
on this. Yeah, . I'm actually gonna page out as well. So we have an integration
right here for Oncall. I'm actually gonna page out
to the infrastructure team. I am pretty sure I'm gonna
need their help with this one. So with that, I've invited them. So while they're assembling
and starting to investigate, I'll go through a little bit of
what we do automatically for you. So our incident has been created. With that we've also created
a post-incident report. It's just a skeleton
template at this point. It will get auto-populated with some
information from the incident as it gets filled out. And you can configure those templates
to kind of fit your business' needs. We also link a Google meet or
potentially Zoom depending on what you're using in order to
create a virtual room. And lastly, we create a channel within Slack or
MS teams if you're using one of those services. As we scroll down you'll
see that the alert that I use to declare this incident has been
brought into the incident and attached to the timeline. So at the bottom here, this is a timeline that will get populated
as we move through the investigation. As we can see Ryan's in here
starting to triage the issue. Looks like we have some crash loops.
And this will get filled out as we go. And this really allows for a
much easier post-incident report. This is all built for you. You don't
have to go ahead and do this yourself. So from here there's also a few pieces
of automation that happen within Slack and we're just gonna pop over there. So we have a general incidents channel, and in the channel it posts for
every time an incident gets declared. This really makes for easy
stakeholder communications. Anyone can be a part
of it can be watching. You can see that we've also populated
with the commander and the investigator, so we know who's responsible as well as
a link to the specific incident channel. So now we've clicked into
the incident channel, and as I I scroll down here
Ryan and Chris are  are doing a great job responding. You'll notice that there's this little
robot emoji that they've attached to a few of their messages. That's what helps push information
from Slack into Grafana incident. Slack, MS teams, they're
kind of ephemeral in a lot of ways. It's really hard to come back and
look through this information. You kind of forget about the channel.
So using this, pushing it into incident, it will live there associated to
the specific incident indefinitely. All right, really they're doing a
great job. What have we found here? Crash loops come to
potential culprit. Alright, so we've also attached a panel. Sorry, we've attached a query. You
can also attach a panel. You can post the alerts to it. I was expecting, see this is
what you get for live demos. I was expecting our Grafana machine
learning Sift investigation to work out, but it seems it didn't. So one of
the other features we have here, Sift, I think it was mentioned in some of
the previous talks is this automated investigation phase. So with
a namespace and a cluster we're able to look across your
logs, metrics, and traces. So all of your observability signals
and bubble up for you potential issues. So that could be recent deployments,
it could be error log patterns, hoping to see that sadly not. So it looks like it looks like
they figured out what's going on. Do you guys think you're
close to a resolution? Yeah. Okay. , I'm gonna say they're
close to a resolution. So with that one, it's time to resolve your incident.
There's a couple of things we wanna check. One, I just wanna look over the task list. So tasks can get created on the fly
during the incident and potentially you need to convert those into
GitHub issues to track them for afterwards. So I see update runbook for alert has
been added and I'm actually just gonna make sure that that's converted
to a GitHub issue before closing out. All right, nice. So now we've
got an issue created in GitHub. We'll be able to track
after action items easily. And with that I'm gonna
go ahead and resolve. So one other feature we have in
here is an integration with OpenAI. And it'll let us do auto
summarization of the incident. So for all of the information
you've pushed into the timeline, it's gonna read through
that, create a summary, and then I can append that to the incident before closing it out. I feel pretty good about what
ChatGPT has told me today. So I'm going to append it
and I'm going to resolve. And with that, our incident is solved. So the last thing I'm gonna show you.
So we've gone from creating our SLO, associating it to alerts,
firing those alerts, declaring an incident
and for closing it out. That's really within the
context of an incident. And what does that look like
across your whole organization? How do we start to keep a
pulse on how your org is doing? So with that, we have an
incident insights dashboard. And for here we aggregate information
from across your incidents. This is the default, but we have
a Grafana incident data source. So you can build out your own dashboards
as you see fit. At a high level, we have, you know, the amount of incidents meantime
to resolve and then slicing it by total incidents, by severity, potentially by labels and as well
as incidents over the monthly. So with that, I'm gonna turn it back over to Marc
and hopefully you can see how you can detect, respond, and learn
from incidents. Nice. Thank you very much Mimi.
You did a great job. I'm really impressed as we 
demoing live here folks, so it's good. Yeah, so overall what's really interesting here
is we've taken kind of the entire life cycle of kind of detecting anomalies when
your data responding to them healthy, and then being able to learn from
the end all within inside of Grafana. We're trying really to target
to bring your engineers, keep them in one location, and use the observability data underneath
in order to solve that incident response process, that lifecycle for them.
So we do area error budgets, routing, escalation management. Clearly the collaboration and workflow
automation is a core piece of what we're delivering here at Grafana Labs in
order to be able to help your team stay within on tool and get more value
out of your observability data. With that, I encourage you all to go into
Grafana Cloud, whether it's your free, your paid version, go ahead
and try creating an SLO today. We wanna get some feedback and work more
closely with you as we go through this. Thank you very much. Really
appreciate everybody's time today. And thank you very much to Mimi
with an excellent demo. Cheers.

