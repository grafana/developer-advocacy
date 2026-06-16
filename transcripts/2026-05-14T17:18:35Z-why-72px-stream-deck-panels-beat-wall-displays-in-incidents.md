# Why 72px Stream Deck Panels Beat Wall Displays in Incidents

Published on 2026-05-14T17:18:35Z

## Description

Wall displays in operations centers don't help engineers solve incidents — and the reason is neuroscience. In this talk, a ...

URL: https://www.youtube.com/watch?v=WgSw-bwJ_h8

## Summary

In this video, the speaker discusses the limitations of traditional large wall screen displays in monitoring system metrics during engineering work, arguing that they often serve more to comfort management than to aid engineers. The speaker, who has experience in productivity hacks, critiques the use of such displays, especially after adapting to remote work during the pandemic. They highlight the importance of human peripheral vision in detecting changes and propose a solution using a Stream Deck, a programmable macro pad, to keep important metrics visible in the periphery instead of relying on wall displays. This approach enhances productivity by reducing stress and improving response times to alerts. Key points include the mechanics of human vision, the psychological effects of alerts on productivity, and practical setup instructions for integrating Grafana with the Stream Deck. The video concludes with a call to action for viewers to explore the project on GitHub.

## Chapters

00:00:00 Introduction and personal beliefs about screen displays  
00:02:30 Discussion on wall screen displays and their actual utility  
00:04:15 The concept of visual perception and saccades  
00:06:00 Explanation of the human eye's detail perception  
00:08:00 Impact of alerts on productivity and flow state  
00:10:15 Introduction of the Stream Deck as a productivity tool  
00:12:00 Overview of setting up Grafana on the Stream Deck  
00:14:30 Discussion on alternative setups (Raspberry Pi, Arduino)  
00:16:00 Importance of monitoring signals and Miller's Law  
00:18:15 Conclusion and invitation to explore GitHub resources  

**Transcript Cleanup**

Cheers! 

I used to believe what many others do: that more screens equal more observability. I thought if I could just see enough metrics in enough places, I wouldn't get pulled out of a flow state while working, or get stuck, or surprised. But that's not always true. I've become suspicious of the idea that large wall screen displays truly help engineers solve incidents. During the pandemic, many of us learned to work from home without these displays, making them somewhat of a moot point. In many cases, they just make management feel comfortable or impress visitors. No engineer wants to be interrupted by a manager asking, "Why is this red?" 

So we have this unspoken agreement: we’ll keep the pretty dashboards up on the walls, while we reserve the good, albeit ugly, dashboards for ourselves. As for the operation centers, no one is actually looking at the wall displays anymore. They’ve turned into more of a project or system status art piece for me. 

Additionally, wall displays work against how the human eye has evolved. Your awareness and perception are fundamentally linked to how our eyes function, particularly through quick little rapid eye movements called saccades. These movements, among the fastest at 700 degrees per second, are utilized when trying to find food or escape a predator. Saccades comprise only 2% of your entire field of view and are focused on a small spot at the back of the retina known as the fovea, which is densely packed with cone cells. This small spot represents only 0.16% of your retina—approximately the size of your thumbnail or the moon in the night sky. 

As your eyes make these small saccades every few milliseconds, your brain uses 50% of your visual cortex to process just 2 degrees of your field of view. To visualize this, imagine your awareness as a frame buffer that only refreshes with two degrees of what you can see during each clock cycle. Not everyone has a role that requires constant monitoring of changing dashboards. We’re expected to work on evolving systems and building new features, and then we get slammed with alerts, feeling a rush of adrenaline that pulls us out of our flow state, replacing productivity with cortisol. Sometimes, we’re stuck in a freeze or fight-or-flight response.

In these moments, you might open a browser, and if you’ve bookmarked the dashboard, that could be helpful. Otherwise, you might give up and SSH into the server to tail the logs. This is where I want to hack the model. Your foveal vision gives you only two degrees, while your central vision spans 60 degrees, and your peripheral vision is more effective looking down than up. This is why you’re more likely to notice something on your desk than on a wall display. 

So, how can we hack this model? Your peripheral vision is broad but low in detail. Detection occurs before awareness, and it’s wired to respond to motion, sudden changes, and contrasts. That’s why your phone, resting on your desk or your lap, can easily grab your attention. I want to put this to better use by reducing your mean time to detection and minimizing interruptions and stress.

To achieve this, I’ve borrowed an idea from Twitch streamers. A stream deck is a programmable macro pad that can control various apps and programs. My interest in it stems from productivity hacking, and it has matured into a reliable platform over the years. Elgato manufactures these devices, and while I don’t work for them or receive any compensation, I appreciate their developer program and want to shout out to Stephanie and Zach from the Elgato marketplace.

You can download hundreds, possibly thousands, of apps for these devices. When I first got one, I searched for a Grafana app but found none. So, I created a small solution to display stats and gauge controls on the stream deck, making them always visible in your peripheral vision. I’ve used the soon-to-be-deprecated v1 HTTP API of Grafana for this. While Elgato manages their apps well, I’ve taken extra steps to scrub any tokens and added some encryption. You can check out the details on GitHub, and there’ll be a QR code at the end of this talk.

To set this up, all you need is to create a read-only service account and input it into the Elgato software for your stream deck. From there, you can pull existing dashboards and controls, specifically your gauge and stack controls. You can choose the panels you want to monitor, and it’s up and running in just a few minutes. 

While all of this could be done with a Raspberry Pi and a touchscreen in kiosk mode, or even with an Arduino if you’re a maker, I prefer a more professional-looking solution that fits well on my desk. An added feature is that if a metric isn’t behaving as expected, you can tap on it to open the specific Grafana dashboard for a closer look. 

However, it’s important to follow Miller's Law, which suggests having five to seven controls to avoid overwhelming yourself. You want to monitor signals that indicate something might be wrong, prompting you to investigate further. If it’s crucial to notice when something is starting to fail, this approach works well.

I aim to shift everyone away from the experience of receiving an alert, experiencing an adrenaline spike, and scrambling to respond. Instead, I want you to be able to pick up trends out of the corner of your eye, sparking curiosity to explore further. 

Another aspect I enjoy is being able to quote real-time changes in stats during late-night calls when something goes wrong, all while maintaining eye contact with the camera. There have been other attempts to bring information into people’s peripheral vision, such as the MacBook Touch Bar, though it didn't quite succeed.

When experiencing major outages, it’s common to experience perceptual narrowing or tunnel vision, becoming fixated on a specific task or thought. Interestingly, police officers are trained to handle high-stress situations by forcing saccades and moving their heads around to maintain awareness. 

While many of us may not have the same training, I would argue that we have all been preparing for this throughout our lives. Many began early, and if you're picking up trends, you’re accustomed to focusing on one thing while still tracking the environment, knowing when to pivot or grab additional resources.

If you see this pattern, I’d argue you’re ready.

Thank you very much! Everything is available on GitHub if you’d like to experiment, and now I’ll hand it back to Matt. 

*(audience applauds)* 

*(upbeat music)*

## Raw YouTube Transcript

- Cheers. So I used to believe the same
thing everyone else does, that more screen equals
more observability. And if I could just see enough
metrics in enough places, I wouldn't get pulled out
of a flow state when I work, or get stuck, or get surprised,
but that's not always true. And I've become suspicious of something, being that large wall screen
displays are not there to help engineers solve incidents. And of course, during the
pandemic, many of us learned to work from home without
any of these things, and they've become a bit of a moot point. And in many cases, they're just there to make management feel
comfortable, or to impress visitors. And no engineer wants to be bothered by a manager coming over and
asking, "Why is this red?" So we have this unspoken agreement where we're gonna keep
all the pretty dashboards up on the walls, and we're going
to keep the good dashboards for ourselves even if they're ugly. So why wouldn't you look at
any of these operation centers? No one is looking up at the wall displays. They've become more like project or system status art at this point for me. And besides, wall displays work against how the human eye has evolved to work. Your awareness or perception
these days isn't different to how it came and evolved when we still looked out
over the plains or jungles. And this comes from the way your eye works with these very quick little rapid eye
movements called saccades. It's amongst the fastest
movements your eye can make, at 700 degrees per second. And you use them when you try
to do something like trying to find food or trying
to escape a predator. And it makes up only 2% of
your entire field of view. And that's because your
retina has a small little spot on the back or the fovea,
which is very densely packed with the special cone cells, so densely that there's
a non-linear drop off in the ability for you
to perceive any detail beyond that space, because
of this tiny little spot that makes up only 0.16%
of your entire retina. So that's about the size of
your thumb if you hold that up, just the size of your thumbnail or the moon in the night sky. So what happens is, as you're perceiving these small little saccades
every couple of milliseconds, your brain is using 50% of your visual cortex to process only 2%, or rather, two degrees
of your field of view. So if you wanted to create
a loosely coupled model of how the brain works inside
as a computational model, you could think of your awareness as a frame buffer that only
gets updated with two degrees of what you can see every clock cycle. And not everyone has a
job where they're going to watch dashboards change all the time. We're expected to work on the
systems that we are evolving and setting up and building
new features, et cetera. And then we get slammed with an alert, and we get this rush of adrenaline. We're pulled out of a flow state, and we replace productivity with cortisol. And you're sometimes stuck in this freeze, fight or flight response. So then you open up a browser and if you did put the
dashboard into a bookmark, then that worked out pretty well. But then you still need
to go search for it. Or you give up and you
just SSH into the server, and you tail out the logs. So this is where I want to hack the model. If your foveal vision
only gives you two degrees and your central vision is 60, your peripheral vision gives
you more looking down than up. And that explains why you're more likely to notice something in
your desk than you are to notice something up on a wall display. And that's exactly
where we hack the model. So your peripheral vision
is wide, but low detail. Detection happens before awareness, and your peripheral vision is
wired to only work on motion, sudden changes, and contrast differences. That's why your phone,
sitting on your desk, on your lap right now
can grab your attention. And that's what I want
to put to better use. I want to reduce your
mean time to detection if that's something important to you, and reduce the number of interruptions and stress that you experience. And I've done so by stealing something from Twitch streamers. Now a stream deck is just
a programmable macro pad that you can use to control
all kinds of things, launch apps, programs, et cetera. And my interest in it came
from productivity hacking, and it's become quite a
mature platform at this point. They've been around for many years. They even have a foot pedal, and there's no coincidence that the size of those little 72-pixel by 72-pixel screens on those buttons are the size of your thumbnail. So to that end, just a disclosure, they are manufactured by Elgato. I do not work for Elgato. They didn't pay me, they
didn't give me any hardware. I wish they did, but they do have a really nice-to-work-with
developer program. And I want to give a big
shout out to Stephanie and Zach from the Elgato marketplace who set all these things up. You can download hundreds, maybe even thousands by this point, of different apps to use
on this kind of device. But when I first got one,
I looked for a Grafana app that I could use, and there wasn't one. So what I've done is hacked
together a small little way of putting at least stats and gauge controls onto the stream deck. So they're always in
your peripheral vision, and you notice them. Now I've done this with
what I've now learned is the soon-to-be-deprecated v1, HTTP API of Grafana's. And I've worked, now, while all these
apps are DRM-protected and managed well by Elgato themselves, I've taken an extra
step to scrub any tokens that you might use, and I've added some additional encryption. You can go check out some of those things on the GitHub repository. There'll be a QR code
at the end of this talk. And the way you set this
up, one pro is nothing that Elgato writes comes in light mode. I see that's important to this audience. But anyway, all you need to do
is set up a service account, preferably a read-only one, always, and then you pop that
into the Elgato software that controls your stream deck, and then from there, you can select it. It uses the API to pull
out the existing dashboards and different controls. It'll only pick up your
gauge and stack controls. And from that point on, you can just choose
whichever panel you want, and then it's up and running. There's also the ability
to, from manual controls, be able to shorten some of the names just for the version you've
put on your stream deck. And then in a few minutes, you
can have something like this. Now in all fairness,
all of this can be done with a raspberry pie and a
nice touchscreen in kiosk mode, or on a phone with some free software. You could, if you're a maker, you can make something with an Arduino. And I love the raspberry pie, but if one's sitting on my desk, I'm going to plug it into something else and use it as a server
or something like that. So I prefer using something
that is more professional, sits on my desk, and makes me look cool. One other feature that you
just saw happening there is whenever you have a metric that's not behaving the way
you want, you can tap on it, and it opens up that
specific Grafana dashboard where you can see
exactly what's happening, although it's not practical to maybe have so many controls over a big stream deck. What you typically want to follow is something called Miller's Law, which is the idea you want
maybe five to seven controls. You're not overwhelmed
by everything on there, and you only want to be
able to monitor signals to let you know that
something's not right. Something needs to be addressed, and you want to go look into
that with some more detail. And of course, if it's going
to be very costly for you to not notice that something
is starting to go wrong, this is a good approach to follow as well. So I want to take everyone
out of this experience where you suffer this alert and you get this adrenaline
spike, and then you have to run and scramble more to a place where you can pick up a trend
out of the corner of your eye, and you get curious about something, and you can begin investigating. Another cool thing I really enjoy is all of you have been on
these calls late at night where something's gone wrong,
and everyone's unhappy. There's nothing like being able to quote real-time changes in stats without breaking eye
contact from the camera. And there have been other attempts at putting things in
people's peripheral vision. Now, the MacBook Touch
Bar didn't work out, and I know it wasn't
exactly designed for this, but it's not a perfect model. And certainly when we experience
any of these big outages, you can get this perceptual narrowing or tunnel vision where
you get stuck in your idea of what you want to do
or what you need to do, and are you following the correct path. Interestingly, police are trained to deal with high-stress situations
by forcing saccades and moving their heads around. They practice this and practice this. Did you notice that the
assailant in this case has already dropped their gun? Now, some of you may also argue that I've not been trained
like a police officer or someone to do this kind of thing. Most of you probably drive, but not everyone's used
to checking their speed. Few of us are flying planes
or even fighter pilots with cool heads-up displays
or anything else like that. But I'd like to argue that all of you, in one way or another, have been training to do
this your entire lives. Many of you started early, and if you're picking up the trend, you're used to focusing on something where you're in a fight, but
you're still tracking things and you know when to
break off, go grab ammo or health points or
whatever else you need. So if you saw the pattern,
I'd argue that you're ready. Thank you very much. Everything is up on GitHub
if you wanna play with that, and I'm gonna hand it back to Matt. (audience applauds) (upbeat music)

