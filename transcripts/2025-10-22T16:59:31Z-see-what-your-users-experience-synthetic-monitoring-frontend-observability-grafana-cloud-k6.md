# See What Your Users Experience: Synthetic Monitoring, Frontend Observability, Grafana Cloud k6

Published on 2025-10-22T16:59:31Z

## Description

Uptime isn't the whole story — user experience is. In this ObservabilityCON session, Mark Meier and Chris Bedwell show how to ...

URL: https://www.youtube.com/watch?v=aEnP7tZFH2Y

## Summary

In this video, Mark Meier and Chris Bedwell from Grafana Labs present a discussion on reliability from the user's perspective, emphasizing the importance of understanding user experience in monitoring applications. They describe a common scenario where system dashboards show normal performance, yet users experience slowdowns. The speakers introduce several key concepts, including user experience thresholds (100 milliseconds for interactivity, 1 second for responsiveness, and 10 seconds for attention retention) and Google’s Core Web Vitals, which measure loading performance, interactivity, and visual stability. They highlight the significance of combining various monitoring tools—such as Synthetic Monitoring, Frontend Observability, and Grafana Cloud k6—to provide a comprehensive view of performance issues. The duo demonstrates using a fictional application, QuickPizza, to showcase how these tools work together to identify and resolve performance degradations. They conclude by announcing new features in their products aimed at improving user experience monitoring and management.

## Chapters

Here are 10 key moments from the livestream transcript along with their timestamps:

00:00:00 Introductions by Mark Meier and Chris Bedwell  
00:02:15 Importance of user experience in system reliability  
00:04:30 Explanation of the three main thresholds for user interaction  
00:06:00 Introduction to Core Web Vitals metrics  
00:08:45 Discussion on the variability in user experiences across different environments  
00:10:30 Explanation of the Swiss Cheese model for risk assessment  
00:12:15 Introduction to the tools in Grafana for monitoring user experience  
00:14:50 Live demonstration using the QuickPizza application  
00:18:00 Recording a user journey with k6 Studio  
00:25:30 Analyzing Synthetic Monitoring data after a service degradation alert  
00:30:45 Conclusion on the collaboration of tools for maintaining reliability and user experience

# Enhancing Reliability with Grafana: A Talk by Mark Meier and Chris Bedwell

**Mark Meier:** Hi everyone! My name is Mark Meier, and I live about 4,000 miles that way. 

**Chris Bedwell:** Hi, my name is Chris Bedwell, and I live about 25 miles that way. 

We both work on the Synthetic Monitoring squad here at Grafana Labs, and we're here to talk about reliability from the outside in—how Grafana can help you see what your users experience. 

## The On-Call Dilemma

Let's get started with a situation you may have lived through before. You're on call. Dashboards look good. There's no alerts firing, and there's nothing interesting in the logs. There's plenty of time for us to look at Hacker News. Then, you get pinged. You get pinged 11 more times. Apparently, things are slow for some users, but you can't figure out why. You recheck your dashboards and see that the system isn't down; it works fine for you, yet some users are still having a bad experience. 

Reliability isn't just about system uptime; it's about what your users feel. That's what this talk is about—how we bring user experience into the picture of reliability. 

## Understanding User Perception

Humans have limits in how they perceive interactivity and reliability. Let's represent 10 seconds with a line. Some of you may have heard of this. Jacob Nielsen famously studied this, and there are three main thresholds we need to consider when optimizing performance of web or any application:

1. **First Threshold:** The point at which systems feel interactive—this is 100 milliseconds.
2. **Second Threshold:** The time before it feels like you're telling the system to do something—this is 1 second.
3. **Final Threshold:** The limit in holding a user's attention—10 seconds, which is really a long time.

Luckily, we can measure user experience on the web. 

### Core Web Vitals

I want to see a show of hands: Who here has heard of Core Web Vitals? Great! These are Google-defined metrics that are essential for a good user experience on the web. We'll focus on three core metrics today:

- **Largest Contentful Paint:** How long it takes for the main content to load.
- **Interaction to Next Paint:** How responsive buttons are or how sticky they are.
- **Cumulative Layout Shift:** How much the content moves. You've all been on a news site before, reading an article, when suddenly an ad loads, and you've lost your place—super frustrating.

The good news is that all of these things are measurable, but the bad news is that they are only part of the story.

## The Chaos Outside Your System

Inside your system, you likely have structured things and visibility into how the system performs and how it starts to misbehave. Is the CPU saturated? Are you running out of memory? Are garbage collectors doing their collecting? 

Outside your system, however, there's chaos. Different networks and browsers render JavaScript, CSS, and other elements differently. Throw in various mobile devices, and there's a huge amount of variability. The catch is that users don't care about this variability; they only care if the system works. They want to log into your site, have the buttons work correctly, and do the job they need to do. 

This is why outside-in matters. We want to see things early, understand the impact, and validate fixes if we have them. 

## The Swiss Cheese Model

Let's talk about the Swiss cheese model, a risk assessment model for managing risk in systems. Each slice represents a type of check to avoid failure. No single slice is perfect; it won't catch everything, but stacking them provides value. Fewer complete failures occur if you have multiple checks.

We see this in real life: when driving a car, you wear a seatbelt, adhere to speed limits, check your speedometer, and use mirrors. When the worst happens, we have airbags. Reliability works the same way. Different tools give us different perspectives to create a complete picture.

## Tools for User Experience

I can apply this model to the entire Grafana Stack, but I want to focus on three tools today that emphasize user experience:

1. **Synthetic Monitoring:** To detect regressions in critical workflows.
2. **Frontend O11y:** To help us see what real users are experiencing and validate the blast radius of issues we know are happening.
3. **Grafana Cloud k6:** To gain confidence before we release or before an important event.

Now, I'll invite Chris on stage to show us a site called QuickPizza, which delivers the world's fastest pizza recommendations. We'll look at web vitals across all three solutions.

---

**Chris Bedwell:** Thank you very much, Mark. Here we can see our QuickPizza application. It is completely over-engineered to do one thing really well: we click "Pizza Please," and it gives us a recommendation. Let's be honest; it's pizza—so we're always going to click "Love It."

As you can see in our flow here, we have to log in first. We know that a common user flow is people coming to the website and logging in. We want to record that user journey in the form of a k6 script using our browser module.

### Using k6 Studio

To help me do this, let me introduce our k6 Studio, a dedicated desktop app that's open-source software. There's a great team working on it, and they're always eager for feedback. Today, we'll look at the recorder. 

I'll click on "Record Flow," ensure that "Capture Browser Events" is clicked, and then start recording. This will open up a Chrome instance. I’ll just drag the k6 Studio widget over and click through the site like any user would. 

I log in using our highly secure credentials, click "Sign In," and then see all our pizza ratings. I can click "Go Back to Main Page," go to "Pizza Please," and again, great recommendation—we're going to click "Love It." Before we finish up, I'll use one of the widgets to assert that "Rated" has appeared on the page.

Now that we've recorded the session, it captures every single event, including all the different requests, whether it was our static CSS, images, JavaScript, or third-party dependencies. One of the benefits of an end-to-end user test like this is that it captures all our API endpoints as well.

### Creating the Test

Next, we'll create a test and export the script. Before we take this script over to Synthetic Monitoring, we'll go to our IDE of choice and import the check module. This allows me to put an assertion on this whole user experience, requiring it to take less than six seconds in total.

Now, no human will run through this faster than six seconds, but because we have a deterministic bot, as long as our APIs behave correctly, it'll do it in a very similar amount of time every single time. 

To test this, I’ll use the k6 CLI with an environment flag for k6 browser equals false. This means it will load a visible Chrome browser for us to watch. I’ll run the test, and it finishes quickly. We can review the CLI output, showing that our assertion was successful and the iteration duration took less than four seconds.

Now that we have our script verified, we can navigate to our Grafana Cloud instance and go to Synthetic Monitoring and checks. I’ll add a new check, focusing on the browser type. I’ll paste my check in, add a job name, and select three probe locations that would be interested in pizza. I’ll leave the frequency at five minutes and set up alerting.

Before finishing up, I’ll click "Test" to run a test for all selected probe locations. It’s worth noting that this view is a preview build, so it might differ from what you’ll see in production soon. All three checks were successful, with durations well under six seconds.

## Analyzing Synthetic Monitoring Data

Now, I’ll fast forward a little to show you what I’ve prepared earlier. I received an alert over the weekend about a degradation in this service. I’ll apply the time range on our new dedicated time point explorer for Synthetic Monitoring.

Before we dive deeper, notice the metrics above—uptime and reachability. Uptime asks whether we had any successes during a given time period, while reachability tracks what percentage of executions passed. A discrepancy here suggests a regional issue. 

Looking at our reachability view, we can see the alert started firing just after five o'clock. As we analyze further, we see that our London probe started failing, taking almost 22 seconds to complete the user journey—much longer than the six seconds we allowed for.

Examining other metrics, we notice that while the web vitals look okay overall, applying filters to the London probe reveals significant degradation.

### Frontend Observability

Synthetic Monitoring is great; it controls and understands every variable going in. However, it doesn’t tell us the full picture of what's happening with real users. This is where Frontend Observability comes in—our Real User Monitoring (RUM) solution. 

I’ll apply the same time range we just saw in Synthetic Monitoring. As we look at the web vitals, we see degradation. Selecting everything outside the UK shows healthy metrics, but focusing on the UK reveals a drastic decline. 

The homepage and login web vitals show that while errors remain flat, the service has degraded in latency. As dinnertime approaches, more users are coming to the application, causing slower experiences.

## Reproducing Issues with k6

Now, I’ll take this information back to our devs, who can try to reproduce the issue in a lab-like environment. I’ll use the k6 script we previously created to replicate the issue. The script is written in JavaScript, but we’re also using TypeScript, which is now supported natively.

I’ve defined three scenarios in the hybrid test: the default one is the same as our Synthetic Monitoring check, with added stages to replicate the loads seen in production. 

I’ve set success criteria, including HTTP errors below 2%, 95% of requests below 2 seconds, and 99% of checks successful. I’ve also added load zones to see if we can replicate results in different areas.

Now, moving to Grafana Cloud k6, we can check the results of our tests. The first test was run before the devs deployed a fix, and it replicated the production issue. As requests increased, so did response times. 

### Validating Fixes

After the devs fixed the issue, we can rerun the same test with zero modifications. We see a significant performance increase, with response times remaining flat even under load. Checking browser web vitals shows healthy metrics, and we can use the comparison feature in Grafana Cloud to see the exact differences.

## Conclusion

As Chris just showed us, reliability isn't just about uptime. In our case, the site was never down; it was just slow. This was tricky to detect. Some pizza lovers experienced degradation, but not all. No single tool told the entire story; they all worked together to signal the problem, validate its existence, and verify a fix.

Together, these tools help us maintain fast, reliable, and predictable experiences. 

## Upcoming Features

Before we get to Q&A, we want to share some features we’ve been working on:

1. **Integration with Grafana Secrets Management:** You can now store tokens, certificates, and other sensitive data in Secrets Management, injecting them into Synthetic Monitoring tests automatically.
   
2. **Time Point Explorer:** This feature will soon be available in Synthetic Monitoring to help you understand failures better.

3. **User Actions in Frontend O11y:** This allows you to link key steps in user flows to telemetry, helping to spot reliability issues in critical workflows and focus on resolving those business-impacting issues.

Thank you for your attention!

## Raw YouTube Transcript

Hi everyone. My name is Mark Meier.
I live about 4,000 miles that way. Hi, my name is Chris Bedwell and
I live about 25 miles that way. We both work on the Synthetic Monitoring
squad here at Grafana Labs and we're here to talk about reliability from the
outside in and how Grafana can help you see what your users experience. So let's get started with a situation
you may have lived through before. You're on call. Dashboards look good. There's no alerts firing, there's nothing interesting in logs. There's plenty of time for
us to look at Hacker News. Then you get pinged. You get pinged 11 more times. Apparently things are slow for some
users, but you can't figure out why. You recheck your dashboards.
You see the system isn't down. It works fine for you, yet some users
are still having a bad experience. Reliability isn't just
about system uptime, it's about what your users feel and
that's what this talk is about - how we bring user experience into
this picture of reliability. So humans have limits in how they
perceive interactivity and thus reliability. Let's represent
10 seconds with a line. Some of you may have heard of this. Jacob Nielsen famously studied
this along with some others, but there's three main thresholds
we need to consider when optimizing performance of web or any application,
any system that users interact with. The first threshold, the point at
which systems feel interactive, like you're actively making
the system do something. It's a hundred milliseconds. The next threshold - the time before it
feels like you're telling the system to do something. You're giving
an instruction, waiting
for it to do something. One second. And finally, the limit
in holding a user's attention. 10 seconds - really long time. Luckily we can measure
user experience on the web. So to get your attention, again,
since I gave you 10 seconds to think, I just want to see a show of hands. Who here has heard of core
web vitals before? Very good. So these are Google-defined metrics and
they're signals deemed essential for a good user experience on the web. These
are just the core ones. Other ones exist. We'll just talk about these today.
There's three that we'll talk about and they focus on loading,
interactivity, and visual stability. We have Largest Contentful Paint; How
long for our main content to load. Interaction to next paint; how responsive buttons are
or how sticky they are. Cumulative layout shift; How
much is the content moving? Sure, you've all been on a news site before
reading an article an ad loads, all of a sudden you've lost your place.
Super frustrating. So again, good news here. All of these
things are measurable. Bad news, the only part of the story.
So inside your system, I'm sure many of you
have structured things, you have visibility into
how the system performs, how it starts to misbehave. Is CPU
saturated? Are you running out of memory? Are garbage collectors doing their
collecting? Outside your system, there's chaos. We have different networks. We have different browsers on
different networks. JavaScript, CSS, rendering differently on different
browsers, on different networks. Throw in a bunch of different mobile
devices and there's a huge amount of variability. The catch here, users
don't care about this variability. They only care if the system works,
if they can log into your site, if the button is working correctly, if
they can do the job that they need to do. And this is why outside-in matters.
We want to see things early, understand impact, and validate fixes if we have them.
And to be very clear, this isn't about a perfect
tool nor a perfect metric, but layering data that we do collect.
Let's talk about Swiss cheese. The Swiss cheese model is a risk
assessment model for managing risk on systems. The general concept is each slice
represents some type of check to make sure that, "Hey, we will avoid failure."
The core component of it is that no one single slice is perfect.
It's not going to catch everything, but you get value from stacking them. There's fewer complete failures
if you have multiple checks. And we see this in real life. You're
driving in your car, you wear a seatbelt, roads have speed limits that say
how safe it is to go on a road. You have speedometers to know your
speed relative to the speed limit. You have mirrors. Your
car may have lane assist. There's people out there that
may choose to use their blinker. When the worst happens, we have airbags.
Reliability works in the same way. Different tools give us different
perspectives to make this picture whole. I can apply this model to
the entire Grafana Stack, but I want to focus on three tools
today that focus on the user experience. We have Synthetic Monitoring to detect
regressions of critical workflows. Frontend O11y that can help us see
what real users are experiencing, or help us validate a blast radius of
issues we know are happening. Finally, Grafana Cloud k6, which we can use to gain confidence
before we release or before an important event. I want to invite Chris on stage. He's going to be showing
a site called QuickPizza. Does one thing - delivers you the
world's fastest pizza recommendation. We'll take a look at web vitals
across all three solutions. We're going to see that browser checks
catch a blip that may be a canary of a larger issue. Frontend O11y
will confirm our blast radius, and finally a k6 test to gain
confidence before we deploy our fix. Great, thank you very much, Mark. So here we can see our
QuickPizza application. It is completely over-engineered
to do one thing really well. We click "Pizza Please" and it
just gives us a recommendation. And let's be honest, it's pizza. We're always going to click "Love It."
But as you can see in our flow here, we have to log in first. So we know that a common user flow is
going to be people coming to the website and logging in. And this is where we want to record that
user journey in the form of a k6 script using our browser module.
And to help me do this, I'm going to introduce our k6 Studio,
which is a dedicated desktop app. It's open source software. There's a great team working on it
and they're always eager for feedback. And today we're going to be looking at
the recorder. So here I'm going to click on Record Flow. I'm going to
click on our pizza instance. I'm going to ensure that "Capture Browser
Events" is clicked and then do start recording. And this is going to open up a Chrome
instance and you can see our k6 Studio widget over the top here. And I'm
just going to drag that over to here. And I'm just going to click through
the site like any user would. So I'm going to go to log in. I'm going to type in our highly
secure credentials here and then I'm going to click "Sign In."
I'm going to get rid of that one. We can see all our pizza ratings. We can click "Go Back to Main Page."
We can go to "Pizza Please." Again, great recommendation, we're going to
click "Love It." And before we finish up, we're going to use one of the widgets
up here to have a text assertion that "Rated" has appeared on the page. Great. I can use one of the last widgets up
here to toggle the event list and we can say, "Yeah, they look okay." So
I'm going to stop the recording. So now we go back to k6 Studio and you
can see that during that whole session, it's recorded every single event
with all the different requests, whether it was our static CSS,
our images, our JavaScript, even our third party dependencies. But one of the things that I really
like about an end-to-end user test like this is it captures all
our API endpoints as well. So you can see that there's 11 of them, which we can assume were all
essential for that user experience. And attesting from this
perspective of a user is completely implementation-agnostic. So if these endpoints are ever to change
to a version two or we are to ever update the routing for them, it wouldn't
matter. This test would still endure. So now that we have those, we're going to click "Create Test,"
we're going to export the script. We can see it here. And then just before we take this
script over to Synthetic Monitoring, we're going to go to our ID of choice. And oh, I can see that Cursor is trying
to tell me what I want to do here. So I'm going to import
the check module here and this is going to allow me to put an
assertion on this whole user experience that I want it to take less than
six seconds on a whole. Now, no human is ever going to run through
this quicker than six seconds, but what's nice about having
a deterministic bot is that
as long as our APIs are behaving correctly, it'll do it
in a very similar amount of time, every single time. So, to test that I'm going to use the k6
CLI and I'm going to have an environment flag here for k6 browser equals false. So this means that it's actually going
to load up a visible Chrome browser for us to watch and then I'm
going to run the test. So it's very much: blink and you miss
it. It goes through and it's finished. And we can review the CLI output here. We can see that the assertion that we
added is successful and we can actually see that iteration duration
took less than four seconds. So that's six seconds we had as
plenty of wiggle room for it. So now that we have our script
and we verified that it works, we can go over to our Grafana Cloud
instance and we're going to navigate to Synthetic Monitoring and to checks. So I'm going to add a new check.
We've got several different check types. Obviously we're focusing on browser
today. I'm going to paste my check in. I'm going to add a job name in instance
so that our telemetry is uniquely identifiable. In our wizard form
here, I'm going to go to execution. I'm going to pick three probe locations
that I think would be interested in pizza. I'll leave the frequency at five
minutes and then I'm going to go over to alerting and I'm going to say
alerts...if at least three.. of nine probe executions
fail in the last 15 minutes, I could add a runbook URL for anybody
that was on call or on duty and there was an instant, but I'm a lazy front
end dev so I'm not going to bother. So just before we finish up here, I'm going to click "Test," and it's going
to run a test for all of those probe locations we've selected. It's worth noting that this view is
something that we're working on Synthetic Monitoring. This is a preview build so it's not
quite what you'll see in production right now, but it will be coming
very soon. And great. We can see here that all three of them
were successful and we can see that the duration again is well under the
six seconds and they all passed. So now we can save that. And if you thought that 10 seconds earlier
for Mark's part of the demonstration was long, wait until I make you wait 10 minutes
of Synthetic Monitoring data to come in. Don't worry, I've blue petered this
and here's what I made earlier. But before we look at that dashboard, I actually received an alert
over the weekend telling me that there was a degradation in this service. So now I'm going to go to their dashboard
and I'm going to apply that time range and we'll go back so you're here. And
this is our new dedicated time point: explore visualization
for Synthetic Monitoring. And just before we look at
this in a bit more detail, I just want to draw your attention
to metrics up here in particular, which is uptime and reachability.
So uptime is asking the question: for any given period
of time or time points, did we just get one success or
not? And if so, mark it successful? Where reachability is maybe our more
traditional idea of light uptime monitoring, which is asking of all
the executions for that time period, what percentage of them passed? And
when you see a discrepancy like this, it paints a picture very quickly that
there's probably a regional issue. So we can confirm that going down to our
time point explorer and we can see that the alert started firing
just after five o'clock. And we can start to hover
to get some tooltips here. And instead of hovering over all of them, I'm going to move to our reachability
view and I'm just going to disable our alert annotation here so we can see, and here we can start to
see the picture unfolding. We can start to see that our
London probe started failing. We can either go over to the mini map
here and if we ignore some of the outliers and have a look at the apex, we can
have a look at the logs of that probe, and we can see that the user journey is
taking almost 22 seconds at this point, much more than the six seconds that we
had allowed for. We can continue to have a look down in the dashboard here, to
have a look at some of the other metrics. And right now as I have no filters
applied, our web vitals look okay, but if I was just to go up and I
was applied to our London probe, we can start to see how
they start to degrade. But Synthetic Monitoring - there's
a double-edged sword to it. It's great because we control and we
understand every single variable that is going in and we know the result
that we want to come out, but it's not really telling us the full
picture of what's going on with our real users. And for this is where we
go to our second product, which is Frontend Observability. So Frontend
Observability is our RUM solution, which stands for real user monitoring. And this is where we'll be instrumenting
our web applications and they'll be sending telemetry back to our real users. So I'm going to apply the same time
range that we just saw in Synthetic Monitoring and again, we can start to see that our
web vitals are degrading here. And just to try and confirm
what the blast radius is, I'm very deliberately going to select
everything that is not the United Kingdom and I can see these all
look really healthy. So now I'm going to remove
all those filters and just
put the United Kingdom on. And then here the pictures really told
to us and we can see that our web vitals have really degraded hugely. We can see that it's instrumented our
homepage and our login for the web vitals here and how they're responding. We can see how many page loads and how
many errors we have and we can see the error rate is staying fairly flat. It's
not a case that our service is erroring, it's a case that our service has
degraded and its latency is huge. The times here I think paint quite a
compelling story that as dinnertime is approaching and people are coming
to our application for their pizza recommendations to know
what to have that night. The more people that
are coming on the site, the slower the experience is becoming. And now I'll enter this information
before we hand it over to our devs. We can also just go to the HTTP tab here, and we can have a look and see whether
any of our API endpoints are affected as well. And we can see that our
pizza recommendation route
had an average of almost a second and three quarters there, much, much higher than any of
the other APIs endpoints. So to recap where we are at this point, we've used Synthetic Monitoring that's
given us an early warning sign of only minutes that an incident has started. We've gone to Frontend Observability
to confirm the blast radius. And now on that information, we can give it to our devs who can now
try and reproduce this in a lab-like environment. So just before we
navigate it to Grafana Cloud, I just want to use the k6 script that
we're going to be using here to reproduce it. So k6 script is written in
JavaScript. In this case, is actually written in TypeScript
which has supported natively now. And I'm going to be using what
we consider as a hybrid test. So I have three scenarios. The default scenario that I've dictated
here is exactly the same script as that we use for our Synthetic Monitoring check
that we recorded in k6 Studio. And all I've added is three different stages
to start to try and replicate the loads that we saw in production. So it's
going to last for three hours. And we also saw two
problematic endpoints as well. So one was the login HTML route, where it's also going to run
for the same amount of time. And also the pizza API route that
we saw was problematic as well. No test is going to be any good unless
we define what its success criteria are here. So I've put in three thresholds where
I've said that HTTP areas have to be less than 2%, that 95% of the requests
should be below two seconds, and 99% of the checks
should be successful. I've also added three different load
zones as well to see whether I can replicate these results in different areas
despite we only saw it in London with our London and our UK users.
So now going over to Grafana Cloud k6, we're going to go to our
QuickPizza projects and we
can see the two tests that I ran here. So the first test is before our devs had
deployed a fix and we can have a look at the results and here we can see that
they've replicated with lab-like data, exactly what we saw in production. That as our request went up
significantly, so did our response time. You can see that we made almost 110,000
requests over the three hours there. And we can also see because
it was a hybrid test, what the web vitals returned as well
for all that important user journey. And we can see that these are
quite highly degraded too. One last thing that I didn't show you in
that script is that we also introduced the screenshot API. So I can go and spot-check any of these
iterations and get some idea of what's going on at the time. So we can see here this is what our
homepage looked like after a second of loading or so. We have the thresholds down here so we can
see exactly by what margin that they were failing by. And now that our devs went off and we've
given them this information and they've reproduced it, they've gone
away, they've done a fix, we can go back to our project in this
test run and we can rerun exactly the same test with zero modifications. And we can see a huge performance
increase where it's finished, absolutely fine. Where even despite when the load and
the requests went up significantly, the response time still stayed flat.
And we can have a look as well, at the browser web vitals, and we can see that these are all
very healthy in the green as well. We can even use the comparison feature
here in Grafana Cloud so we can see the exact differences. And go over to the thresholds and see
that we actually had a perfect check rate versus 56% previously.
And then there we have it. There it is - our three cloud products
working together. So Mark, back to you. So as Chris just showed us, reliability
isn't just about uptime, pure uptime. In our case, the site was
never down, it was just slow. And this was kind of tricky to detect.
Some of our pizza lovers saw degradation, but not all pizza lovers. No tool told
the entire story of what happened; they actually worked together to signal
the problem, validated that it's real, and verified a fix. So together these
tools can help us maintain fast, reliable, and predictable experiences. So we showed you a lot of things
today. And before we get to Q&A, we do want to tell you about some
things we've been working on in these products. Let's start with one of our
most requested features this year. We've integrated Synthetic Monitoring
with the Grafana Secrets management service. You can store
tokens, certificates, other sensitive data in Secrets
Management - inject them into a Synthetic Monitoring test in your requests, automatically redact those so they're
not invisible in metrics or logs. This is in public preview, so you can go
use it today. It's widely available. Next in the demo, Chris showed
the time point explorer, so we eventualized executions
in Synthetic Monitoring. We want to make it easier to understand
failure. This is coming very soon. Over the next few weeks, it'll ship to all Grafana Cloud
accounts so you can make use of it. Our friends in Frontend O11y have been
working on a feature called User Actions. I think Manoj may have shown it to
you yesterday. This allows you to link key steps in user flows to telemetry so
you can spot reliability issues in these important workflows and focus on
resolving those business-impacting issues.

