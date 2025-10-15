# How EA Monitors 200+ App Metrics at Scale with Grafana | Electronic Arts | EA App

Published on 2025-06-07T05:34:45Z

## Description

In this insightful talk from GrafanaCON 2025, Kenny Chen, Software Developer II at Electronic Arts, shares how EA uses Grafana ...

URL: https://www.youtube.com/watch?v=bGMcbIuasD4

## Summary

In this video, Kenny Chen from EA discusses the development of a monitoring system for the EA app using Grafana. He highlights the challenges of monitoring a monolithic application with over 500 events and more than 200 core metrics, emphasizing the difficulties in using traditional gauges for effective monitoring. Kenny introduces the concept of "status history" as a more informative visualization method, which allows easier identification of issues across multiple app versions. He also explains the importance of establishing meaningful thresholds using statistical methods, specifically the three-sigma rule, to enhance alert accuracy. Additionally, he presents the idea of "functional dashboarding," where dashboards are dynamically generated based on parameters rather than being static, which improves maintainability and adaptability. The presentation concludes with actionable takeaways for viewers interested in optimizing their own monitoring systems.

# Monitoring EA App with Grafana

Hi everyone! How are you doing? Thank you for joining. I know it's pretty late in the day.

My name is Kenny Chen from EA. Our team builds and supports the EA app, which is the launcher for EA games used by hundreds of millions of people worldwide. Today, I'm going to present how I use Grafana to build a system that effectively monitors the status of the app. 

I understand we have a lot of audience members rooted in backend development and SREs, and I hope to share a slightly different perspective with you, as we face different sets of challenges. If you have any questions, feel free to take a picture of this QR code, and we'll try to answer them by the end of the presentation.

## Scale of the Problem

First, let’s discuss the scale of our problem and the visualizations that have worked or didn’t work for us, as well as the math behind effective monitoring and large-scale root cause analysis.

Have you ever been asked to monitor 200 metrics at the same time? It can be overwhelming. If you were to visualize this with one gauge per metric, you would end up with a huge and complicated dashboard. 

Why do we do this? Because we are monitoring an app that runs on users' machines. Unlike the microservices everyone talks about, our app is a monolith by design. You can't split it further, and monoliths are just hard to monitor. 

Our app generates 500 different events, which can combine to yield more than 4,000 possible metrics. Even if we make a deal to cut that down to 95%, we still end up with more than 200 core metrics. 

### Key Metrics

Here are some examples of the metrics we monitor:
- Crash rates of our executables 
- Crash rates of our games 
- Login errors from our internal systems and external partners 
- Various kinds of updates, game installs, updates, and repair errors 

All of these are equally important to our user experience, and we need to monitor them closely. Whenever there's a problem, we want to know as soon as possible. 

### Challenges with Monitoring

Unlike a backend service where you typically monitor one version, we have multiple versions running simultaneously, and we need to monitor them all. This requires one gauge per version per metric to achieve full coverage. 

Moreover, our version list keeps growing due to weekly releases that introduce new builds. 

We initially tried using gauges, but we found that we can't really trust them. A gauge can represent various things, such as the last reading, the median, or the average. A dashboard full of gauges can easily mislead users, as different situations can appear identical on a gauge. For example, a spike in metrics can indicate either a new incident or a temporary issue, and gauges may not provide enough context to differentiate between them.

### The Visual Spectrum

We realized that visualizations exist on a spectrum. On one end, we have simple gauges that provide limited information, and on the other end, we have time series that contain every data point in history. Time series provide a lot of information but are not easy to scan when you have many metrics.

What we actually need is something that is both simple and informative: **Status History**. 

## Status History Visualization

If you're not familiar with it, you can think of a status history panel like a colored calendar, with rows representing different metrics and cells representing time blocks (e.g., an hour). We use colors to indicate good or bad status based on thresholds. 

The key features include:
- A time axis 
- Color coding 

This design allows us to quickly spot patterns, showing which metrics are improving or in trouble. It also enables us to display multiple app versions compactly. Instead of having a gauge for each version, we can use a single status history panel to show the most popular versions.

### Identifying Issues

Different types of issues can be identified using this method:
- If only the latest version is red, it indicates a regression, while previous versions are green.
- If all versions turn red simultaneously, it likely indicates an external outage.

### Setting Effective Thresholds

Now, where do those colors come from? If you randomly pick thresholds, the same metric can appear good or bad for no valid reason. 

**Here’s my tip:** Check the histogram of your metric. 

The histogram shows how often each value appears. It should ideally resemble a bell curve (normal distribution). According to the central limit theorem, if your metric comes from many independent random events, it should follow this distribution. 

With a normal distribution, values typically shouldn't go too high above the mean. You can draw a boundary line to separate what is likely to happen from what is unlikely. If you see a bunch of unlikely values, something fundamental has changed—perhaps a new bug or incident. 

In practice, you can calculate your threshold using the mean and standard deviation. For example, if your mean is 1.5% and the standard deviation is 0.2%, your threshold would be 2.1%.

## Recap

To summarize, we started with an overwhelming dashboard and realized that gauges weren't effective for indicating issues. We then adopted the status history approach, which necessitated good thresholds. By combining these techniques, we developed dashboards that allow us to easily identify different types of issues, such as external issues, regressions, and fixed bugs.

After proper training, our developers can review 200 metrics in about 10 minutes, which was previously a task that took hours or might not have happened at all. With solid thresholds set, we can also maintain 24/7 coverage, ensuring we don't miss critical issues.

## Root Cause Analysis

Once we detect a spike, we naturally want to know the root cause. For those familiar with backend workflows, Grafana has delivered many features to enhance this workflow. However, our setup is different. 

Our app does not send metrics or logs; we only collect a few anonymous JSON events. These events contain types and fields as context. When we see a spike, we receive a flood of JSON events, each with the same type but different context. 

### Analyzing JSON Events

For instance, if we have a spike in game launch errors, we can break it down by game ID to identify which games are causing the spike. This enables us to test those games locally and reproduce the issue or reach out to the game team for further investigation.

Breakdowns are useful, but they don’t scale. With 200 metrics and, say, 10 fields for breakdowns, we could end up needing 2,000 panels—impossible to manage.

## Functional Dashboarding

To address this, we apply the **DRY principle** (Don't Repeat Yourself). Instead of creating redundant panels with different parameters, we treat dashboards as functions. 

The idea is simple: dashboards can be called with different URL parameters, generating the necessary configuration without hard-coding each panel. 

### Demonstration

Let me show you how this works in action. 

[**Switch to the Laptop View**]

Here’s a simple dashboard with six metrics, featuring status history for daily monitoring. Each panel has a link pre-populated with the correct parameters. 

As I open two links, you can see how the content differs, while the underlying dashboard remains the same. 

On the left, there's a sample JSON event from our app with clickable fields. As I click on a field like user language, the panel on the right updates to show the breakdown of error rates by that language. We can also break it down by operating system, revealing a spectrum of Windows versions in use. 

The key takeaway is that we don't need 2,000 panels; just one functional and configurable dashboard will suffice.

## Conclusion

Behind the scenes, our breakdown panel reads the dashboard variable to adjust itself. The query uses variables instead of hard-coded terms, enabling dynamic updates based on user interactions. 

The benefits are significant. Instead of managing thousands of static panels, we maintain just one configurable dashboard. This allows for free exploration and maximizes the use of our JSON event data.

Lastly, the maintainability is crucial. We generate everything from templates, ensuring easy extensions and keeping our dashboards and alerts up to date with weekly recalibrations.

### Actionable Takeaways
- Try using status history instead of gauges for better insights.
- Implement the three-sigma rule for high-quality threshold settings.
- Treat dashboards as functions to reduce redundancy.

Thank you for your attention! If you have any questions, I’d be happy to answer them now. 

[**Applause**]

## Raw YouTube Transcript

Hi everyone. Okay, cool. Hi everyone. How are you doing? Yeah, thank
you. Thank you for joining. I know it's pretty late in the day.
So my name is Kenny Kenny Chen from, I'm from EA. So our team basically builds and supports EA app, which is the launcher of EA games used
by hundreds of millions of people around the world. Today I'm going to present
how I use Grafana to build a system that can effectively
monitor the status of the app. So I know we have a lot of
audience that are rooted in backend development and SREs, and I hope this is a slightly different
story for you because we have different sets of challenges. So as usual,
if you have any questions, take a picture of this QR code and we'll
try to answer that by the end of the presentation. So cool. So I'm going to discuss first of
all the scale of our problem and the visualizations that I used that
worked or didn't work for us, and the math behind effective
monitoring and large scale root cause analysis.
So let me start with a question. Have you been asked to monitor
200 metrics at the same time? Okay, cool. I mean, for real, you
might picture something like this, but that's not the entire picture. That should be if you only
use one gauge for metric, that should be the 200 metrics,
the dashboard, something
huge and overwhelming. So why do we do this? That's because we're monitoring an app. An app that's running on user's machine.
Unlike unlike the microservices, everyone talks about an app
is a monolith by design. You can't split it further and
monoliths are just hard to monitor. Our app throws off 500
different events and by combining them you can get more
than 4,000 possible metrics. So even let's make a deal,
let's say it give you 95% off, that still gives you more
than 200 core metrics. This is the list of the metrics
that we're looking at. Like for example, crash rates
of our own executables, crash rates of our games, log in from our error from
ourself, from external partners, various kinds of update, game
install updates, repair error. Either way, they are equally important
to our user experience and we need to closely monitoring them all. And whenever there's a problem, we wanted to know as soon
as possible and we have a different challenge. Unlike a backend service where you
probably just monitor one version, we have multiple versions running at the
same time. We need to monitor them all. This is the real picture. You need one gauge per version per
metric to achieve full coverage for metrics. So not to mention that our version list
keeps growing because we have weekly release that release
new builds every week. And that's not the end of bad
news because we've actually tried, we've actually tried something like that, like this and we found that
we can't really trust gauges because a gauge can, for example,
gauge can mean a lot of things. It could show the last reading,
it could show the median, it could show the average. If you
have a dashboard full of gauges, it's really easy to make things up. Plus gauges are kind of vague by design. Totally different situations can
look exactly the same on a gauge, maybe you have a POD spike, maybe you have an ongoing incident. If the average is the same,
they show up as the same gauge, but you need to take
completely different actions. So gauges can sometimes
be misleading and they are not best for spotting issues. Then we realized that visualizations exist on the spectrum. On one end you have gauges
that're super simple but not much information. And on the other hand you have time
series that contain every data point in a history. It's super that contain
a lot of information, but they're not very easy to
scan when you have tons of them. So none of these works well
when you have a ton of metrics. So what we actually need is something
that's both simple and informative. Our answer is status history. If you are not familiar with that,
lemme describe it a little bit. So a status history, you can
think of a status history panel, like a colored calendar. You can stack rows with different
meanings of the row and each cell, it's like a time block
for example, an hour. And we use colors to show good or bad based on thresholds. The key is it's got a time
axis and it's color coded. That makes it super
useful first. For example, you can quickly spot patterns
like it's easy to see which metric is improving or
which one is in trouble. It also lets us show lots of
app versions in a compact way. Instead of having a
gauge for each version, we can just have one set of history
panel that can automatically display the most popular versions in just one panel. And it helps us spot
different types of issues. Like if only the latest version is red, it indicates a regression
like the previous version
are all green and the latest version is red, a bug. But if all versions suddenly
go red at the same time, it's probably just an external outage. But here's a question, where
do those colors come from? We already enjoy the
effectiveness of the color coding, but where those color come from, if
you just randomly pick a threshold, the same metric can look good
or bad for no real reason. So how to find good metrics, sorry, how to find good
thresholds, that's very important. And here's my tip. So first thing to do, I think you need to check
the histogram of your metric. So on the left you see the
typical normal time series everyone knows. And on the right
that's a histogram of the same metric. The histogram shows how
often each value comes up. In case you are not very
familiar with histogram, here's how to read a histogram. So this basically tells you
that in the past seven days the metric was at 1.5% for 22 hours and it was at 2.1% for just one hour. This just showed the frequency
of each possible value and usually it should
look like a bell curve, also known as a normal distribution.
And this is not a coincidence. The central limit theorem actually
says that if your metric comes from many independent random events, it should follow a normal distribution. And this often works for error rates. I wouldn't go deep into
the math detail here. The important thing is
with a normal distribution, values shouldn't go too
high above the mean. You can actually draw a
boundary, draw a line, that's the boundary between what's
likely happen and what's unlikely happen. So if you see a bunch of unlikely values, somethings' fundamentally
changed, maybe that's a new bug, maybe that's a new incident. So the boundary is a really good place
to put your threshold for good or bad. In practice, it's really easy for any time
series just calculate the mean, the standard deviation, your threshold, it's just a mean plus three
times the standard deviation. So in this case, the mean is 1.5% and the
standard deviation 0.2%. So that gives you a threshold, that 2.1% you can see how
good it fits into our chart. Okay, so here's a quick recap
of why we are doing this. So we started with this overwhelming dashboard and we realized that
gauges are not really good for indicating issues. So we realized we had to
use status history instead. And that gives you the
need for good thresholds. And by combining the techniques
together, we get dashboards that work. Through this dashboard you can easily
tell different types of issues like external issues, regressions, bugs fixed, and external issue that's resolved. So our devs after proper training
can review 200 metrics in about 10 minutes and that makes it
possible to always keep an eye on everything that's
important. So before this, this will had taken hours or maybe never, sorry, I'll be honest. Anyway, with the solid thresholds, we actually
set up alerts for every metric. So we have 24/7 coverage, not
just when someone's locked, not just when someone's looking. So
I'll be super honest here, before this, we sometimes missed critical issues
simply because there are so many things to look at and things were not very
obvious. Since we've set up this system, we haven't missed any critical bugs
caused by our own code changes. Thank you. [applause] But we didn't stop there. So once you detect the spike, okay,
you see an error that's error rates up, you naturally want to know
what's the root cause. So for those familiar with
the backend workflows, I know Grafana has been delivering a
lot of super cool features that can help enhance this workflow, but for
us that's a different challenge. That's because this is
a typical backend setup. You have metrics, you have
logs, you have traces, they're separate. And when
you see a metric spike, you go to check the logs
and to find the root cause. But our setup is different because
our app doesn't send metrics or logs. You can't seriously send all the logs
from user's machine to our server. So we only collect a few
anonymous JSON events. That's a standard approach.
And those JSON events, they have the type and they have fields as a context. So whenever
you see things like this, whether you like the status history
version or the time series version, it's a spike. And what's actually happening behind the
scenes is that we get a flood of JSONn events like this. So each of them has the same type but
with different contacts and those contacts and help us figure out the
root cause. For example, if we have a spike in game launch error, we can try to break it down by game id. So right away we see which
games are causing the spike, that's a green one and the yellow one, and then we can test those games locally
and try to reproduce issue or even reach out to the game team. Either
way, those are actionable insights. Or we might want to break
down by app version. So that would tells us if maybe
there's a regression in our new release and at least we'll know
which versions are being impacted. So breakdowns are not magic, like you've seen similar
things through Loki Drilldown, but you can achieve similar
stuff just by using the group by transformation. It's not
transformation anyway, it's a query. So I think this is available in most
data sources. You can build your own. So breakdowns are super useful
except that they don't scale. Let's do a simple math. We have 200 metrics and for each metric, let's say we have 10 fields
that's worth breaking down. That would give you another 2000 panels. So that's just impossible to build or
use. Let's say even if we build it, where are we going to put them all? Are we going to put 'em in the same
dashboard that already crammed with 200 metrics, 200 panels? We are
Devs, we're not search engines. So it's just not possible. What do we do? I always think about the dry
principle that don't repeat yourself. When you're
faced with repetitive task, you should really think about
turning it into a function. So that's the same here. All those panels are basically the
same, just with different parameters. They have different queries, they
have different breakdown fields, but they're essentially the same. So what we actually need is a function, give it the query and the breakdown field
and it gives you the right dashboard to use. And you can think about that. You can see how a dashboard URL, it's similar to a function call
starting by the function name. And then here's how you populate. Okay, here's how you populate the,
okay, typical, yay. Anyway, then you here's how you
populate the variables. And by visiting this URL, you get the
dashboard you need. That's simple. So don't actually hard code 2000, dashboard 2000 panels like this. What you should do is you should use
different URL parameters to represent them all. So this is the concept of what
I call functional dashboarding. The core idea is that
dashboards are not static pages, they're functions, you can call them by visiting the URL
with different parameters and you get the dashboard you need. I want to demonstrate how I use
it and how this works in action. Cool. Can we switch to my laptop
please? Okay, there we go. Thank you. Thank you very much. So this is part of the
dashboard that I show here. It is a simple dashboard
with just six metrics. It's not the 200 metric
one that keep mentioning. So each role it's a status history. These are metrics that we watch day to day and we have errors like a game crash, three games crash,
one of our binaries. Okay. You can see how easily you can see issues from our
dashboard. This is completely green, sorry, completely red. Anyway, so what I'm going to do is that, so for each panel here, I provide a link that's attached
that's already pre-populated with the correct parameters. I'm
going to open two of them. So as you can see here, they show complete different
content. Like the title is different, the metric is the show is different. You can tell it's completely
different, but one thing is the same, they're the same dashboard underneath. So they're essentially the same
dashboard just with different parameters. So scrolling down a little bit on the
left here we provide a sample JSON event that's sent from our app and there's a list of fields here
that all of them are clickable. And I want you to pay attention to the
panel on the right here. So this panel, I want you to see that as I click
on the link language, user language, it's been updated to show the
breakdown of this error rate by user language. And we can also break it
down by a different field
like operating system. Okay, you see our users use a spectrum of Windows operating system. The key thing here is that
there are so many fields here, they're just the fields that are all
fields that are available in our user events that sent to our server.
And for some of the fields, I don't even know what they mean. Be really honest. Like the end
reason. What's the end reason? I don't know. Content Id offer id. There's a lot of IDs here, I don't
really even know what that means, but you know what I mean. Whenever
there's a bug or there's a spike, I can click on basically any of them. I can just freely click on any of them. And if I see some very dramatic
change in distribution, I know there's a direction to investigate. So let's do a quick recap. Remember at the very beginning we're
thinking about building 2000 panels like this, and now we
see the answer. Okay, so there's no need for 2000 panels, just one dashboard that's really
configurable, that's really functional. So I think we can switch
back to the presentation. Nice. So here's how it
works behind the scene. The breakdown panel always
reads the dashboard variable to adjust itself. This is the query. You can see it's a variable.
It's not any hard-coded term. And when you click on the
field like operating system, it'll update the breakdown term
variable of that dashboard. And it doesn't need any
external plugin or something. This is just a simple URL trick. So there's no development work. And essentially this is just the
data link off the table and the link is configured like this. It start with the link to its
own dashboard and then you need to prepare the cell value as
the new breakdown term variable and forget to append other variables
so that you keep this state and remember, don't tick this so that it's a direct
refresh of the current tab instead of opening a new one. And that's it. So the benefits are really huge. Instead of having 2000 panels
or even is a growing number, we have just one, it's
configurable for anything we need. And people can explore freely,
not just predefined routines. Like as I said, you don't even
need to know what those fields are. If you see any distribution change, you can know that's maybe
the root cause and we can use our events to the fullest. Anything that's available in the
JSON fields are available to us. Last important thing, maintainability. For a system that's big like this one, it has a big alert dashboard and more
than 200 alerts and you can't build it by hand. Ours is all generated from
templates. So once you define a query, everything else is automatically
generated by scripts. It can be really easy to extend. And we have pipelines that calculate
the three sigma thresholds from history and rebuild everything every
week. So it's always up to date. For the deep dive dashboard,
that one is generic, so it basically need no maintenance. So this is the overview
of how the system works. We have a pipeline that refreshes the
thresholds and rebuild the dashboard, rebuild the alerts, and all of them have customized links
that's pointing to the sheer deep dive dashboard. So it's a large system, but there are some really
actionable takeaways for everyone. So if you're using gauges a
lot, I think you should try, you can give status history
a try is really good. I think you should really try the
3-sigma rules if you have staggered thresholds, if you want high
quality staggered thresholds. And last thing, I think you can treat dashboards as
functions to reduce redundancy in your system. And that's the end of my
presentation. Thank you everyone.

