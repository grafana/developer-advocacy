# A Golf Launch Monitor That Actually Works | Open Source | OpenFlight | GrotShotPro

Published on 2026-05-14T17:17:48Z

## Description

Coleman, a staff engineer at Grafana, got tired of golf launch monitors that cost $30000, charge monthly subscriptions, or give ...

URL: https://www.youtube.com/watch?v=sgKlX8fn1NM

## Summary

In this video, Coleman, a staff engineer at Grafana, presents his innovative project GrotShotPro, which is an open-source launch monitor for golfers. Drawing from his lifelong passion for golf and personal experiences with expensive and inefficient launch monitors, Coleman decided to create a more accessible and effective alternative. He explores the two main types of launch monitors—radar-based and camera-based—focusing on the radar technology used in OpenFlight, which utilizes a Raspberry Pi and different radar types to accurately measure golf ball metrics. Throughout the presentation, Coleman discusses the technical aspects of radar operation, including Doppler and FMCW radars, and explains how the collected data is processed and visualized using Grafana. He highlights the project's growing community and encourages attendees to engage with his work, showcasing the potential of open-source technology in the golf world.

## Chapters

Certainly! Here are the key moments from the livestream, along with their timestamps:

00:00:00 Introductions and background on the speaker  
00:01:15 Overview of the speaker's passion for golf  
00:02:00 Introduction to launch monitors and their significance  
00:03:30 Discussion of the problems with existing launch monitors  
00:04:45 Birth of the OpenFlight project and its goals  
00:06:00 Explanation of the open-source nature of OpenFlight  
00:07:30 Primer on how different launch monitors work  
00:09:00 Introduction to radar-based and camera-based launch monitors  
00:11:00 Detailed explanation of Doppler radar technology  
00:14:30 Overview of frequency-modulated continuous wave radar  
00:16:00 How Grafana is integrated into the project and data processing  
00:17:30 Invitation for attendees to try the simulator and closing remarks  

# GrotShotPro Presentation Transcript

**Hey, everybody!** Thank you very much for sticking around for the last slot of the day. I promise it’s worth your time. 

I’m Coleman, a staff engineer at Grafana, and this is my Science Fair project, **GrotShotPro**. 

So, I know I met a few of you already today, but by show of hands, how many golfers are here? *I see a couple. Great!* 

I’ve been a golfer my whole life; it’s one of my oldest passions. I grew up working at a golf course, and in the past three or four years, I’ve gotten really serious about getting better. This journey comes with a lot of activities, like drawing lines on videos of my swing, FaceTiming my coach for emergency lessons, and using various gadgets in my practice to improve. 

One of those gadgets is called a **launch monitor**. These devices are essential for golfers to get fitted for the right clubs and to understand the metrics of their swing and ball flight. I found myself going through a cycle every few months, thinking, "Maybe I should get one of these. I think it’s time." 

However, there are significant problems with the launch monitor ecosystem. If you want a really good one, it’s going to cost around **$30,000**. I know there’s someone here who works for a company, and I apologize for calling you out on that. If you want a cheaper option, it might not work well; it could hallucinate or inaccurately estimate your numbers. And if you want something in the middle, they will charge you a subscription to use the device, which is crazy. Plus, all of them have subpar software. 

So, I thought, as an engineer with a Claude subscription, maybe I can try to build my own. That’s how my project, **OpenFlight**, was born. I started from scratch; I knew nothing about hardware or radars. I began posting my journey on social media, sharing my successes, failures, and everything I was learning. It turns out people were really interested in a project like this. I got invited on a podcast, did a Q&A for a golf news site, and TikTok started paying me some pretty big money. *Watch out, Grafana!* 

So, **OpenFlight** is this totally open-source launch monitor. The idea of open source is quite novel to the golf community, which is exciting. It has over 300 stars—almost 400 now—and I’ve got contributors from all over the world. I’m now at around **30,000 followers** across various platforms, which is something I would never have imagined saying. It’s been a really cool journey that just popped up for me.

### How Launch Monitors Work

Now, let me give you a primer on how launch monitors work. There are two kinds: **radar-based** and **camera-based**. 

- **Radar-based monitors** track the ball’s flight for a longer duration and rely on signal processing and something called beam-forming, which I don’t fully understand yet but know it’s powerful. 
- **Camera-based monitors** use a high-speed camera to capture a few frames while the club hits the ball, then estimate the rest of the flight after that initial impact.

OpenFlight uses **radar** and is powered by a **Raspberry Pi**. All the code running on it is written in Python, and it includes three radars in total—two different types that I’ll explain shortly. It also has a cool new 3D-printed enclosure contributed by someone in the repository.

#### Types of Radar

There are two different kinds of radar:

1. **Doppler Radar**: This is a large radar on the right. It relies on something called the **Doppler shift**. If you’ve ever stood on the side of the road and heard a police car pass by with a changing sound, that’s the Doppler shift. It uses continuous radio waves. When the radio waves bounce off an object and come back, the difference in frequency tells us how fast something is moving. Doppler doesn’t convey direction but does indicate speed, and it has one transmitter and one receiver. 

   A fascinating aspect I learned during this project is that you can also measure spin with Doppler. This is similar to how we observe planets spinning in space. When an object spins in the air, it wobbles or vibrates, and you can detect that with the radar.

2. **Frequency-Modulated Continuous Wave (FMCW)**: The other radar has one transmitter and two receivers. This physical difference in the receivers’ positioning provides enough data to create a vector to the golf ball. We transmit one radio wave, it comes back, and is received by the two different receivers, allowing us to understand the direction and trajectory of the ball.

### Integrating with Grafana

So, how do we utilize this with Grafana? After you hit a shot, we crunch all the numbers and go through all the radar data. Each shot becomes a JSON log containing all the metrics we collect, which we then ship off to **Loki**. All of this runs on the Raspberry Pi. 

The logs transform into ball flight data, and I have an app plugin running in Grafana that pulls data from Loki every few seconds. We used a Claude special physics engine, resulting in a nice simulator right in your backyard. 

I know some people tried it out today, and that was super fun to watch. I wanted to do a live demo on stage, but unfortunately, no one would let me. So, I think there’s a video here. 

*Come see me tomorrow! If you didn’t get to try it out, it’s pretty cool.* 

**Thanks, everybody!**

## Raw YouTube Transcript

- Hey, everybody. Thank you very much for sticking around for the last slot of the day. I promise it's worth your time. Yeah. So I'm Coleman. I'm a staff engineer at Grafana, and this is my Science
Fair project GrotShotPro. So I know I met a few already today, but show of hands, any golfers here? I see a couple. Great. So I've been a golfer my whole life. It's one of my oldest passions. I grew up working at a golf course, and in the past three or four years I've gotten really serious about getting better. And that comes with a lot of stuff like drawing lines
on the videos of your swing, FaceTiming my coach for
an emergency lesson, and also involving a lot of gadgets in your practice to get better. And one of those gadgets
is called a launch monitor. And, you know, these are
really important things as a golfer and as a player to
get fit for the right clubs, to understand the metrics of your swing and your ball flight. And I found myself every
few months kind of going through this cycle of, "Maybe
I should get one of these. I think it's time." But there's problems with the launch monitor ecosystem. If you want a really good
one, it's gonna cost $30,000. And I know there's someone
here who works for a company, and I'm sorry to call you out on that, if you want a cheap one, it's
not gonna work that well. It sometimes might hallucinate, it might kind of estimate your numbers. That's no good. Do you want one right in the middle? Well, they're gonna
charge you a subscription to actually use the
device, which is crazy. And all of them have subpar software. So I thought, I'm an engineer,
I have a Claude subscription, maybe I can try to build my own. And so that's how my
project OpenFlight was born. So I started from scratch. I knew nothing about hardware,
I knew nothing about radars, but I started posting my
journey on social media, all the successes that
I had, all the failures, everything that I was learning. And it turns out that people were really
into a project like this. I got invited on a podcast, I did a Q&A for a golf news site, and TikTok started paying
me some pretty big money. Watch out, Grafana. And so yeah, OpenFlight was born, and it's this totally open
source launch monitor, and the idea of open
source is totally novel to the golf community,
which is really cool. It's got over 300 stars, almost 400 now, and I've got some contributors
from all over the world, which is pretty cool. I'm at, like, 30,000 followers now over a couple different platforms, which is something I would
never hear myself say. So it's been a really cool journey that kind of just popped up for me. So real quick, I'm gonna give you a primer
on how launch monitors work. So there's two kinds. Radar-based and camera-based. Radar-based watches the
ball fly for a longer time, and it relies on signal processing and something called beam-forming, which I don't fully understand yet, but it's really powerful. Then there's camera-based, which relies on a high speed camera to capture just a few
frames while the club is hitting the ball, and it estimates the rest of the flight after that initial impact. So open flight uses radar, and it's powered by a Raspberry Pi. All the code running on it is Python, and it's got three radars
total, two different ones. And I'll explain the
difference in a minute here. And it's got a new cool
3D-printed enclosure that was contributed by
someone in the repository. So there's two different kinds of radar: one large Doppler radar on the right, and two radars on the
left that are called FMCW, which I'll get to in one second. And I tried using a camera
but it didn't work that well because you need a lot of computing power, and, you know, from the
position of the radars, you can't see the ball that well. It didn't work. So the Doppler radar relies on something
called the Doppler shift. If you've ever been standing on the side of the road and a police car goes by you and the sound changes,
this is the Doppler shift. It uses continuous radio waves. And when the radio way is
bounce off of something and come back, that
difference in frequency tells us how fast something's moving. Doppler does not have
a concept of direction, but it does know speed, and it has one transmitter and one receiver, which is
important information for later. Something really cool that I
learned during this project is that you can also
measure spin with Doppler. And this is also how we observe
planets spinning in space, which is pretty cool. When when an object is spinning in the air, it kind of wobbles
or it kind of vibrates, and you can pick that up with the radar. Okay, bear with me on this one. Trust me, it's not that complicated. The other radar is called frequency-modulated continuous wave. And the main difference is
that it has one transmitter and two receivers. That physical difference in the receivers, how they're positioned
physically on the board, will give us enough
data to create a vector to where the golf ball is. So we transmit one radio wave up, it comes back, is received by two different receivers, now we have a vector to the golf ball. This is how we understand direction and the trajectory of the ball. So how do we do this with Grafana? So, after you hit a shot,
we crunch all the numbers, we go through all the radio waves, we go through all the radar data, and a shot becomes a JSON log. These are all the metrics we collect, and then we ship it off to Loki. Alloys running on the Raspberry Pi, and then the logs become ball flight. I have an app plugin running in Grafana that pulls Loki every few seconds. We used a Claude special physics engine, and you get a nice simulator
right in your backyard. I know some people tried it out today and that was super fun to watch. I really wanted to do a live demo on stage, but no one would let me, so I think there's a video here. (putter puts) Come see me tomorrow. If you didn't get to try
it out, it's pretty cool. Thanks, everybody.

