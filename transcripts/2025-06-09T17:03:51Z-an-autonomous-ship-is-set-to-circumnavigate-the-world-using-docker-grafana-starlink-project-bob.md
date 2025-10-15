# An Autonomous Ship is Set to Circumnavigate the World Using Docker, Grafana, &amp; Starlink: Project Bob

Published on 2025-06-09T17:03:51Z

## Description

Join Andrew McCalip of Varda Space Industries as he builds Project Bob—a DIY, solar-powered, autonomous ship aiming to ...

URL: https://www.youtube.com/watch?v=uUmXbG3Y4iU

## Summary

In this video, Andrew McCalip from Varda Space Industries presents Project Bob, an initiative to create an unmanned solar-powered boat aimed at circumnavigating the globe using open-source tools. The project began with a Twitter post and quickly gained momentum, leading to a successful Kickstarter campaign. Andrew, who typically works on satellites, discusses the similarities between building spacecraft and autonomous boats, mentioning the technical challenges involved. He explains the boat's design, hardware, and software stack, including the use of Docker containers, Raspberry Pi, and various sensors for operation and monitoring. Testing of the boat has commenced, with initial successes and some challenges, and the team aims to launch in June. Andrew encourages viewers to follow the journey online and expresses gratitude for the open-source tools that made the project possible.

# Project Bob Presentation by Andrew McCalip

**Introduction**

Hello, I'm Andrew McCalip from Varda Space Industries, and I'm here to talk about **Project Bob**. This project is an unmanned, solar-powered craft — essentially a small boat — that we're aiming to take around the world. It's all about circumnavigation or bust, using open-source tools. We have a limited time of 15 minutes for this presentation, so please hold your questions until the podcast that follows.

**Origins of Project Bob**

This journey began with a Twitter post. I enjoy building hardware and software projects in public, which has been a lot of fun! Seven months ago, this project kicked off and quickly gained momentum. We launched a Kickstarter campaign that got fully funded in just one day, leading us to where we are now.

**Choosing an Autonomous Boat**

You might wonder how I ended up choosing an autonomous boat for this project. As background, my day job involves building satellites and spacecraft, which are essentially expensive autonomous boats. The systems are quite similar, including propulsion, batteries, solar power, RF communications, and compute. I build the hardware and software that test these systems, so it seemed like a natural fit.

In the past, I gained some notoriety on the internet for attempting to replicate room temperature superconductors, which was another Twitter project. It was a fun adventure that included trying to import materials and build quartz reaction vessels. Although the science didn't pan out as we hoped, we made some contributions and friendships along the way. At one point, we had 15,000 people watching a live stream of a webcam focused on a furnace door, which inspired me to think about creating more engaging live streams.

**The Concept of Project Bob**

So, why hasn't anyone done this before? Well, they have, but my approach is different. I'm sending a craft around the world rather than going myself. This idea dates back 500 years to Magellan's journey. To circumnavigate the globe, we need to cover about 25,000 miles, cross the equator twice, hit the antipode, and avoid using canals. My route will take us from Los Angeles, under South America, Africa, Australia, and back to Los Angeles. While this is ambitious, I don't expect to succeed on the first attempt, but we will keep trying until we do. If we pull this off, it would be a world record!

**Hardware Development**

Before diving into the software stack, let's briefly discuss the hardware. This project started as an after-hours hackathon with engineers coming together to design the boat from the ground up. We discussed factors like the size of the boat, the solar panels, and battery capacity. As we built the spacecraft, we carried around a collection of tools and components that we wished we could use in space, but may not be space-rated. This project has been a creative outlet for us to explore those ideas.

We currently have two hull designs: a sleek, fiberglass version for efficiency, and a more rugged kayak filled with batteries and foam. The latter is slower, but both designs are in the race, with the second hull launching first.

**Progress and Testing**

We've been testing the boat, which is about 14 feet long and weighs around 300 pounds. I’ll show some videos of it operating later. However, let’s now shift to the software stack. As a mechanical engineer, I had to learn software development from scratch after a 10-year hiatus. Fortunately, a plethora of helpful tools emerged during that time.

Onboard the boat, we use a Raspberry Pi 4 running 14 Docker containers that manage propulsion systems, motors, GPS, accelerometers, magnetometers, and more. We utilize Redis for communication among these containers. We also have Influx and Starlink onboard to facilitate live streaming and data collection. The idea is to broadcast as much as possible while pulling metrics and video from the boat.

On the GCP side, we backfill our Influx database and push it to Grafana Cloud dashboards, where we also reassemble video chunks. This process has been a convoluted but effective pipeline that continues to improve.

**Testing Environment and Challenges**

Our development environment is set up as a FlatSat, where we lay out all the components and write drivers for them. After establishing stable communication with the various devices, I installed solar panels, batteries, and Starlink on the roof of the office to run tests continuously. This setup allowed us to identify and fix long-term bugs.

During testing, I often took the opportunity to check GPS accuracy while on the road. We have successfully tested the boat in the marina, and our primary goal was to avoid sinking — which we achieved! There were minor mishaps, like hitting a few boats due to lag in WiFi connection, but we learned a lot from these iterations.

**Next Steps**

Looking ahead, we aim to launch in June while taking advantage of the optimal sun position dictated by physics. From now until mid-June, we will be conducting test runs and debugging as much as possible. This is critical because we need to leave for the southern hemisphere during their summer. 

**Conclusion**

That wraps up the presentation on Project Bob. If you have any questions, please feel free to ask during the podcast. You can also follow along on Twitter and our website for updates. We plan to live stream every day during the journey, so it should be an exciting adventure. 

A huge thanks to all the sponsors and the open-source tools that have made this project possible. Thank you very much!

## Raw YouTube Transcript

A very kind introduction. So I'm Andrew
McCalip from Varda Space Industries, and I'm here to talk about Project Bob. So Project Bob is one
of my hobby projects. It is a unmanned solar-powered craft, small boat that we're trying
to take around the world. So it's circumnavigation or
bust with open source tools. So we've only got 15 minutes for this, so hold your questions to the
podcast that comes right after this. We're going to go through
this pretty quick. So this all started with a Twitter post, and I do a lot of things in public. I love building these hardware
software projects in public, live, and it's been a ton of fun. And so this one kicked off seven months
ago and it got a little bit out of hand. We did a Kickstarter project
and it got funded in a day. And so this is the result of that.
So to give a little background, how did you end up choosing an
autonomous boat? So as background, my day job, as you can see, is
building satellites and spacecraft. So these are really just essentially
really expensive autonomous boats. It's all the same systems. You've got
propulsion, you've got batteries, solar, RF comms, compute, all the same
things. And so I do this as my day job. I build infrastructure. I build the hardware and software
to test the hardware and software. So it looks like a very similar set
of problems. You've got a bunch of io, a bunch of pressure
transducers, temperatures, lots of things to monitor
- bi-directional comms. And so my day job is to assemble
hardware and software to test this vehicle. So this is a satellite bus we launch
into space and you saw it come back from space there, sort of like the Apollo capsules of old.
And so that's what I do for my day job. And then so the work knows me as
the guy with the weird hobbies. The internet knows me as the
guy from the LK-99 debacle. And so this is where I got
slightly infamous for doing
another Twitter project, trying to replicate the room temperature. Superconductors also did it on
Twitter, and this was a fun one, trying to buy red phosphorus and trying
to import stuff from Poland and building quartz reaction vessels
after hours at work. And it didn't end up working.
The science wasn't great. We ended up making some contributions. We donated our samples to a lab
and got some papers out of it. But it was fun. We made
some friends along the way. The key part about this though
is that during the adventures, we had, it was like 15,000 people watching a live
stream at one point where it was just a webcam looking at a furnace door
with a Grafana temperature plot, and the whole entire internet was riveted.
And so they gave me the idea like, "Hey, can we do more really
boring live streams?" And so that was kind of the
genesis of this idea is, "Can we do an orbit? Can we do
a really boring live stream? And we engage the public as we build
with these cool tools?" So the most boring live stream in
history is Project Bob. So why has nobody done this before? Well, they have, and actually I heard last night there's
somebody at Grafana that has sailed around the world. And so find
that person and congratulate them. We're doing this the easy way. I'm
sending a pie around the world. I'm not going myself. And so
we did this 500 years ago. Magellan did this. And so what does it
take to circumnavigate? I use that word. It's like we got to go 25,000 miles,
we have to cross the equator twice, we have to hit the antipode, which is the opposite side of
the earth from where you started, and we cannot use the canals.
And so my route looks a little bit different than Magellan. We're
going to go from Los Angeles, our launching point, and we're going to
go under South America, under Africa, under Australia, and
then back to Los Angeles. This is all very optimistic. I don't think that we're going
to make it the first time, but we're going to keep
trying until we get it. This would be a world record
if we can pull it off. So before I talk about the software
stack I'll touch real briefly on the hardware. So this started as an after
hours sort of hackathon activity where we had some engineers come together
and build it up from first principles of how big does a boat need
to be, how much solar panel, how big do the batteries need to be,
how can we assemble this stack of parts? And so as we build the spacecraft, there's always a collection of tools and
components that you would love to use in space, but they may be not space graded. And
so you're always carrying around in your back pocket this cool collection of, "Hey, wouldn't it be nice to use..." these
panels or these really great motors? So this has been a creative outlet for
some of the engineers to get some of those ideas out of their system. So here's the progress of
where we're at right now. So we've got two different hull designs. We've got sort of the more efficient one
where we fiberglassed a hull and it's sort of the sleek aerodynamic version
- should be way more efficient. And then we have the rough and ready, off the shelf where we've taken a kayak
and filled it full of batteries and foam. And so this is
the more rugged version, but it's going to be a lot slower. So it's a little bit of a
race between the two designs. We're launching number two first
and then one we'll catch up later. So this is the point where
this is the Iron Man montage of it's where the hero spends 20 seconds
and there's fast-paced music and it all just comes together really
quickly. In reality, it's been like six to seven months of
nights and weekends and come into work an hour early and do a little bit of wiring. And you can see us doing PCB work, riveting on panels, building wire
harnesses, welding up the keel. It's truly like a full stack effort. And so jump ahead to, we're on the water. So we've been out testing. So this is the culmination
of six months of work. And so this is the boat.
It's about 14 feet long. It's about 300 pounds. And so I'll
show some videos of it operating later. But yeah, let's talk a little
bit about the software stack. So I'm a mechanical engineer. I am not a software engineer. And so
I had to learn all this from scratch. I haven't really done
software in 10 years. So I come back and after 10 years there's
whole sprawling ecosystem of wonderful tools that wasn't there the first time. And so I'm super grateful for all
of these tools that have sprung up. And so this is just some of
the things that we use on the boat. And so real quick touch on, and we can go into more detail later, but this is the pipeline of
the boat side and the land side. Onboard the boat,
we have a Raspberry Pi 4, and this is running a whole
bunch of Docker containers. We've got I think 14 Docker
containers now and they do everything on the boat. They control
the propulsion system, the motors, the stepper motors on the actuators, GPS and accelerometers, magnetometers, IP cameras. So we have this huge collection of all
these assorted protocols. And this is a common theme in all my projects is it
has to interface with real life. To me, it has to go out and touch something in
the real world to really be interesting for me. And so Docker was a
good way to isolate all these different protocols. And then what we do is we use Redis to
communicate to all the Docker containers. So that's sort of our back plane of
sensing and command. And then from Redis, we take it over to Telegraph. And so we run Influx on the boat
and we also have a Starlink. And so part of the idea remember was
that this should be a live stream. We should broadcast as much as possible. And so we turn on the Starlink six hours
a day and we pull all the metrics off the boat, we pull, we replicate the onboard
Influx database over to GCP, and we also transfer over all the videos
that we've stored throughout the day. And then on the GCP side, what we do is we backfill our
Influx database and then push that to the Grafana Cloud dashboards. We also reassemble all the
video chunks because we chunk everything over
Tailscale and Starlink, and then we reassemble all those chunks
and do something kind of fun where we composite the Grafana
dashboards in OBS over the video that we've collected
from the onboard cameras
and eventually push that out to YouTube. And so it's just
like convoluted pipeline, but took a little while to write,
but it's working pretty well. So testing, embracing the SRE culture
of test everything, record
everything all the time. And so this is us in our dev environment. So dev environment for us is like
FlatSat. We take all the parts, lay 'em out on a table, start
writing drivers against those. So this is how the project started like
a month after the original post. And so this is us talking to
motors, talking to GPS. I would wheel this outside and
start writing all the drivers and all those Docker containers to talk
to each one of these different devices. So then as we got the drivers
working and it's sort of stable, I climbed up on the roof of work
and installed some solar panels, installed Starlink, batteries,
and actually started
getting some solar cycles. So we're actually
powering the whole system, powering that HitL bench
and running it 24/7 and running Starlink all the time, and just collecting metrics
and finding those long-term bugs that inevitably do pop up. So this one's kind of a fun one. You can see me Grafana-ing from the front
of the truck on the way to the marina. And so there's things like GPS
where you can't really exercise it sitting in the back lot. And so took some of these rare
opportunities to check my GPS heading accuracy and a couple other
things as we're on the road. So I am sitting in the truck,
we've got Grafana open, we're streaming video through Starlink, through Tailscale back down to the
laptop as we drive down the 405 in Los Angeles. So that was kind of fun.
We got a couple strange looks. And so here we are
actually out on the water. So this has turned into one
of my favorite dashboards. This is the FPV mode, how we
drive the boat from the marina. So a couple things here.
We are embedding video. So we've got live video from the
Ford facing cameras on the boat, which is what you see there in the center. And then the standard button plugins
for Grafana weren't quite enough. I needed to do a couple custom things. And so this is a fun hack that
I've used now for all of my work projects and personal projects
starting to embed HTML elements in the dashboards to give them
controls. So now with these controls, we can reach out, turn on
the rudder, hard starboard, we can go control the speed
of the boat, power channels, and so that's with a nice GUI and fast API. And that's been absolutely
fantastic. And then of course, all the standard metrics, tracking power and rudder
angle and all that. But this one has been great
for driving it around. We were pretty successful in the marina
testing. So we've been out three or four times now. And number
one goal was don't sink. And we did not sink.
We did hit a few boats. There was some lag, and once we
got out of range of the WiFi, we lost WiFi connection to the
boat and it ran away from us. But other than that, it's been
good. Little iterations you find, like the rudder's too small and
other little mechanical improvements. And so this has been
a great test campaign. You got to get all the bugs out
because once we send this thing off, there's no way to ever get to
it again. We've got one chance. Just like the satellite when you
launch, everything's got to be perfect. It's got to be able to boot itself up
and come up to a clean state every single time. And so you can see us out on
the water chasing kayaks and paddle boarders around, and it's been a lot of fun. There's a
lot of questions from people on the water of how it gets controlled. And I have to
tell the story of me and my laptop of, "Oh, I'm driving it through a
dashboard," and they're very confused. And so the next steps for us. So ideally we're launching in June, so we have to launch with the
sun in the right spot in the sky, sort of dictated by physics. So every
weekend from now until the middle of June, I need to be out there and getting
test runs in and doing some debugging. We need to leave here in the summertime
to get to the southern hemisphere by their summertime. And so simple physics dictates
and gives me a hard deadline. So we're launching in June. So that is Project Bob. And so
if you've got any questions, feel free to ask 'em in the podcast. Also follow along on
Twitter and the website. Twitter's the best place and you'll see
me tagging the Grafana and Influx and tail scale accounts as
we push out some content. And then we should be livestreaming every
day of the journey during the daylight hours. So it should be a lot of fun. So huge thanks to all of the sponsors
and all the tools that we've utilized along the way. We really couldn't have done it without
the wonderful open source tools that we're here to celebrate.
So thank you very much.

