# Grafana &amp; Prometheus Use Cases: Bringing Situational Awareness to Observability

Published on 2025-06-07T05:34:24Z

## Description

Learn how Chris from Orange Barrel Media uses Grafana tracks light levels, touchscreen bugs, and even cracked screens across ...

URL: https://www.youtube.com/watch?v=_mSXnYEewU0

## Summary

In this video, Chris from Orange Barrel Media discusses the complexities of managing production systems for a nationwide network of information kiosks that provide services like free Wi-Fi and wayfinding to residents in various U.S. cities. He emphasizes the importance of situational awareness and measuring operational data to make informed decisions. Chris explains how they monitor around 3,000 devices, including touchscreens and cellular routers, using Grafana to visualize metrics and identify issues. He shares examples of measuring performance, such as monitoring ambient light levels during an eclipse and analyzing touchscreen activity to detect malfunctions. The video highlights the integration of technical data with field technician reports to create a comprehensive understanding of kiosk functionality and user experience. Chris concludes with advice on engaging stakeholders and being innovative in measurement strategies.

# Transcript Cleanup

**Hi, I'm Chris.** I work at a company called Orange Barrel Media, where I manage production systems. Today, I would like to discuss the concept of situational awareness.

It's good to measure things, and I think we can all agree on that. However, what's even better is actually knowing what's going on; this way, we can make better operational decisions. It turns out that achieving this is quite challenging, especially where I work, as we have a nationwide network of information kiosks.

These kiosks are located in about 20 cities across the U.S. They are approximately six feet tall and feature touch screens, provide free Wi-Fi, emergency call buttons, wayfinding, and other information for residents. We install these kiosks in cities for free because we can run advertisements on them and share the revenue with the municipalities. While these kiosks are incredibly useful, they are also quite complex, and it is crucial to keep them running smoothly.

By the numbers, we currently have **680 units**—and it's actually now up to **700**. This means we have nearly **1,400 touch screens** running various apps that need to be operational. In total, we monitor about **3,000 devices**, which includes not just the touch screens but also cellular routers, security cameras, computers within the kiosks, and other electronics. This results in approximately **3 million time series** in our Grafana Mimir cluster. We truly enjoy measuring things, especially when you have a platform across cities nationwide.

Here’s an example of what we can measure: *Raise your hand if you think you know what's happening here.* (No hands raised) I'll give you a hint; this graph shows ambient light levels in various U.S. cities. The cities are marked in red, and the peaks follow the yellow arrows. If you haven't guessed by now, this is from **April 8th, 2024**, when our ambient light sensors detected an eclipse as it marched across the country. We were able to observe this event with a single line of PromQL, which was really fun. However, that's not the primary thing we need to measure.

### Measuring from Machine to Experience

We aim to measure everything from machine performance to user experience, which can get tricky. In the middle, you have your operating system and applications, and there are plenty of resources available for that. Generally, you can find plugins to help with profiling, such as node exporters and other tools. 

As you move down towards the machine level, it becomes harder due to a lack of plugins and the presence of obscure APIs. For example, how do you instrument a cellular router made by a third party? Moving in the other direction towards user experience can be challenging as well, since content and usability are often not well-defined and sometimes not even measurable.

Today, I'll go through a couple of examples of how we approach this problem in our kiosks and how we measure from machine to experience to better understand what's going on and what actions we should take in the field.

### Dashboard Evolution

We started with basic dashboards for each computer that typically display CPU metrics and time series data. Engineers would look at these dashboards and conclude whether they need to replace a component or if a system has crashed. While Grafana can provide actionable insights, such as system CPU IRQ times, it doesn't indicate whether ads are playing or if a user is struggling to access the transit app.

Today, our dashboards look much more comprehensive. Every little indicator on the dashboard has earned its place; each feature was added in response to specific issues someone encountered. This dashboard is used not only by engineers and SREs like myself but also by field technicians who open the kiosks, replace parts, or take pictures for promotional purposes. 

A dashboard like this spans the entire spectrum from machine performance to usability, allowing Grafana to simply indicate, “The kiosk is doing its job”—no interpretation required.

### Content Monitoring

For example, we monitor content on nearly **1,400 screens**. This allows us to identify whether a screen is stuck or blank. If a problematic software update leads to a loading spinner being displayed on multiple kiosks, we know immediately. We achieve this by taking constant screenshots of our display hosts, running them through ImageMagick to extract metrics like the root mean square (RMS) change in pixels over time and the density of edges in the image. These metrics feed into our node exporter and are displayed on our dashboards. If the display isn’t functioning correctly, a notification appears in Slack, alerting us to a stuck screen.

### Touchscreen Monitoring

We also monitor touch screen functionality. The idea is that the kiosk is idle, playing ads, until someone interacts with it. If the touchscreen is malfunctioning, it can remain stuck on the app screen, which doesn’t present a good user experience.

We monitor touch activity at the hardware interface level by capturing a raw stream of touch events. If you're a Linux user, this can be accessed via a specific path that provides a continuous flow of touchscreen data. We analyze this data to compute metrics such as touch frequency, gesture duration, and touch location density.

For instance, in a healthy kiosk, you might see occasional touches with gesture durations of less than one second. In contrast, another kiosk showing **32 touches per minute** for several hours, with all touches concentrated on one line, indicates a malfunction—likely a broken touch layer. This alerts us that the touchscreen is overactive, and we can dispatch a technician with a new touchscreen controller.

### On-Site Inspections

Some issues cannot be measured remotely, but we still do our best. For example, a kiosk might show a green status in Grafana, but upon arrival, it could have a bullet hole or heat damage. Another kiosk may show that the router is offline, but upon inspection, we find that a car hit it, necessitating more than just a router replacement.

When all our metrics and data analysis fail, we rely on our field technician team. We have about **30 technicians** across the country who check on kiosks daily. They clean the kiosks, interact with them as users would, and report any problems using a mobile app. This low-tech approach connects to a PostgreSQL database, allowing us to create a map displaying which kiosks were checked and which ones were flagged with issues.

When a kiosk is flagged, it goes into a channel visible to the tech supervisor, who can then dispatch help as needed. Grafana helps us integrate human observations with technical data, providing a comprehensive view. This way, we can identify content problems, buggy touchscreens, and on-site damage.

### Takeaways

In conclusion, my key takeaways are to **communicate effectively with stakeholders**, work backwards from their needs, and be creative in how we measure things. Thank you!

## Raw YouTube Transcript

Hi. So I'm Chris. I work at a
company called Orange Barrel Media, more about that in a minute,
and I manage production systems. So let's talk about that. So it says
situational awareness. So real quick, what do I mean? So it's
good to measure things. I think we all agree what's better
is actually knowing what's going on because that way we can make
better operational decisions. And it turns out that this is pretty hard. And where I work, because we have this nationwide
network of information kiosks. So these are in about 20
cities throughout the US. They're about this tall.
They have touch screens, they provide free Wi-Fi,
emergency call buttons, way finding things like that,
information for residents. We put them in the cities for free because
we can run ads on them and share the revenue with the cities.
So these are really useful, but they're also very complicated and
it's also very important that we keep them running.
So just by the numbers, we have 680 units, it's
actually now up to 700. And that means we have nearly
1400 touchscreens running apps that need to be running. And those make - and in total, we have about 3000 devices that we
monitor because it's not just the touchscreens, it's also
the cellular routers, the security cameras,
the computers themselves, and other electronics within the
kiosk that we need to keep an eye on. And that means we have about
3 million time series in our Grafana Mimir cluster, and we
just love measuring things. It's super fun when you have this
platform on cities across the country. So here's an example
of what we can measure. I can't see very well, but raise
your hand if you think you know what, this is what's happening here. Okay,
good. No hands. I'll give you a hint. This is ambient light
levels in various US cities. And the cities are marked in red, and the peaks kind of
follow those yellow arrows. And if you haven't guessed by
now, this is April 8th, 2024, and that's the ambient light sensors
on our LCDs that normally balance the backlight. Then they're seeing
an eclipse. So we got to, with one line of PromQL, watch an eclipse march across the
country. So that was really fun, but that's not what we need to
measure. So what do we need to measure? We need to measure all the way
from machine to experience. And that gets kind of
tricky. I'll kind of explain. So in the middle you'll have your
operating system and your apps, and we all know there's
plenty of help for that. I've actually learned a lot
about that today and yesterday. And so you generally can find plugins
that help you with that profiling, node exporter, all that kind of stuff.
When you go down towards the machine, it gets harder because there
might not be the plugins. You get some weird APIs. How do you instrument a cellular
router that someone made? If you go in the other direction, it just gets weird because we're
talking about content and usability. These things aren't even well-defined and
they're sometimes not even measurable. So I'm just going to go through
a couple examples today on how we approach this problem in our kiosks
and how we measure all the way from machine to experience
to kind of get a better idea of what's going on and what we
should do about it in the field. So how do we do it? So we started
out with something like this. So every computer had
a dashboard like this. This is the kind of dashboard
you usually have for a computer. It tells you something about
the CPU some time series. And usually an engineer looks
at this and they say, look, you need to go out and replace
something, or this thing's crashed, get a new one. And Grafana can tell us really
actionable things like the system CPU IRQ. time is 1:27, but it won't tell us whether ads are
playing or whether a user's having a hard time pulling up the transit app.
Today, it looks more like this. So we have this nice dashboard
and everything on this, every little indicator earned its place. Every time, everything you see here. At some point someone
had a problem and said, I wish I could see when the touchscreen
is overactive or how many times the thing had to reboot itself. So everything here kind of earned its
place and is looked at by not just engineers or SREs like myself, but folks who are in the field opening
these things up, replacing parts, or even folks who have the job of taking
pictures of the kiosks to show them off. And so a dashboard like
this kind of spans that entire spectrum all the way from
machine to usability. And it's the thing where
Grafana can say, "Hey, the kiosk is doing its job." Plain and
simple, no interpretation necessary. Some examples about this, for example, we check content on nearly 1400 screens. So this means we know whether
it's stuck, whether it's blank. So if a bad software update rolls out and
everyone sees a loading spinner on the sidewalk, we see it here. And this is, we're actually just looking
at the pixels like this. So we have our display hosts and
we take screenshots constantly, and then we run them through image
magic and we extract things like the RMS change in pixels over time and the density of edges in the image. And then that goes into node exporter
and shows up on these dashboards. And if it doesn't look good, a little
shows up in Slack and we know that, "Hey, this kiosk has a stuck screen,
or a lot of kiosks have a stuck screen, you probably deployed something
bad." Another example here. Oh, forgot that queue. Yeah, Grafana can now tell us you have
content problems and it can tell us that it's scale, which is neat, right? You have content problems on
20% of your fleet. For example, we also, not just the displayed
content, but also the touch screen. So we have touch screens. And so the idea is the kiosk
is sitting there doing nothing. It's playing some ads and then you walk
up and you touch it and the apps come up. And so we need that to work well. And if the touchscreen is broken, it can be overactive and the thing is
just stuck on the apps and it just doesn't look good. It looks
kind of broken that way. It should go back to sleep
when no one's using it. So we actually monitor touch activity
at the kind of hardware interface level.
So we pull the raw stream of events. So if you're a Linux user,
this you can cat out. There's a certain path that will give
you this fire hose of touchscreen data. So we take that fire hose and we compute
things like how often is it being touched, how long are the gestures, where are they and how densely populated
are they? How clustered are they? And then we can get metrics from
that. So this is a normal kiosk. You see occasionally someone walks
up and touches it. There's locations, we've plot them XY here, and the gesture durations are less
than one second that looks healthy. I think that kiosk is okay.
This one, however not so good. So this one's 32 touches per
minute for several hours, and all the touches are on one line. So we pretty much know that one
of the lines in the touch layer is broken or something like that.
And so that one will alert and it will look like
this. On our little dashboard, it'll say touchscreen is overactive. The content is not rotating because
the apps are up all the time. And Grafana can now tell us, "You have content problems because your
touchscreen is buggy." And so now we have a better clue we can go out there
with a new touchscreen controller. Finally, there's some things
you just can't measure remotely, but we do that anyway.
So I'll give examples. So we have this kiosk. Grafana says,
it's all good, everything's good, everything's green. Then you
show up and it looks like this. So this one literally has a bullet hole
in it, and this one's heat damaged, so that's not good. We don't want
that. And then the other kiosk, come on, click. Oh, there
we go. Grafana says, "Hey, the router is offline."
And we say, "Okay, that happens." We'll get out
there later with our new router, maybe ethernet cable or something
like that. But no worries, it happens. We'll fix it. And we show up and
it looks like that a car hit it. A router is offline.
You're right about that. But we kind of had to show up
with something than a router. And so our last defense, when all the cool metrics and all the
analyzing of data fails is our field technician team. We have about 30 people throughout the
country and they drive around and walk around all day and they walk up to
the kiosk, they clean off any dirt. They operate the kiosk like
we would expect a user to, and they make reports via a
mobile app. Those reports, I mean, this is a really low tech, but we
just have a Postgres data source, hooks right into the application database.
And it lets us make a nice map. And so right here we can see
which kiosks were checked, which ones are flagged with problems. And when a kiosk is
flagged with a problem, it goes into a channel that the tech
supervisor sees and they can dispatch some help to take care of it. And what Grafana does here is it puts
the human observation on the same pane of glass as the technical observation. So you can go all the way from
some low level CPU thing up to the actual user experience. And that way
Grafana can tell us something like, "Hey, you have content problems.
Your touchscreen is buggy also, Matt showed up and it was cracked
and he couldn't fix it." And that's pretty much it. So my takeaways
are for this kind of thing, really talk to your stakeholders, work
backwards from what they need to know, and be really creative with how
you measure things. Thank you.

