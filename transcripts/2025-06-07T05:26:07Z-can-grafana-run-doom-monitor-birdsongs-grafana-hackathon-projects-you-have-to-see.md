# Can Grafana Run Doom? Monitor Birdsongs? | Grafana Hackathon Projects You Have to See

Published on 2025-06-07T05:26:07Z

## Description

What *can't* you do with Grafana? Several Grafanistas share how they've used Grafana to go beyond traditional observability ...

URL: https://www.youtube.com/watch?v=XZ3R2OEgBvc

## Summary

In this video, team members from Grafana Labs, including Gianni, Ivana, Sven, Domas, and Bogdan, share insights from their recent company hackathon, which empowers employees to innovate creatively. They discuss various projects developed during this event, such as a playful video game featuring Grafana's mascot, Grot, and a bird monitoring application called Birds Drilldown that allows users to explore bird songs and their environmental correlations without needing to write queries. Additionally, they present a humorous project that integrates the classic game Doom into Grafana as a data visualization tool. The hackathon fosters a culture of experimentation and skill development, with nearly half of the projects either shipped or in progress, showcasing the vibrant and collaborative spirit within Grafana Labs.

# Grafana Labs Hackathon Presentations

For those who don't know, Grafana Labs strategically empowers engineers by giving them a lot of agency to push and implement what they want to see. We use our own offerings, which is why I believe our software quality is so high. 

We also have a system of hackathons where, four times a year, every employee at Grafana—across Go-to-Market, Engineering, G&A—can take a whole week to work on whatever they like. At the end, they present a five-minute video, and we rank and vote on the projects. Almost 50% of the hackathon projects have already shipped or are in the process of being shipped. While not everything ships, a significant fraction does. Many features you see on stage today are based on hackathon ideas, although not all of them are production-grade; some are just fun.

For example, let me introduce **Super Grot**. Hi everyone, my name is Gianni, and I'm excited to share something we built during our most recent hackathon. If you've ever participated in a hackathon, you know the energy can be wild, with people prototyping new features and pushing boundaries. At the last hackathon, Domas and I decided to create something a little different—a tribute to our little yellow dinosaur mascot, Grot.

We built a video game featuring Grot using the Phaser JavaScript game engine. You can play it in your browser on almost any device, and we've instrumented it with the Grafana Faro web SDK to report level completion times, scores, player deaths, coins, and other data. There’s a public dashboard available at [play.grafana.org](https://play.grafana.org). If you achieve a high score, it will show up there for everyone to see. 

To try it out, you can scan the QR code or visit us at the science fair section on the second floor, where we have an arcade cabinet set up for the conference. We hope to see you there!

Now, let’s transition from dinosaurs to birds with our next project: **Birds Drilldown**. 

Hi, we are Ivana and Sven, and we want to talk about our fun hackathon project. As we just heard in the keynote, metrics, logs, traces, and profiles Drilldown are now GA, which is fantastic! You no longer need to know LogQL, PromQL, or TraceQL to write your queries. Drilldown Apps unlock a queryless, effortless solution to query your data and gain insights.

However, I think something is missing. What do you think, Ivana? 

You're right, Sven—there is something missing. Where is the **Birds Drilldown**? If you're confused, no worries! Let me provide some context. Sven and I have a side hustle: we’re on a mission to make Grafana recognized not just as a monitoring company, but specifically as a birdsong monitoring company. When someone mentions Grafana, we want them to think, "Oh yeah, dashboards and birds."

This started last year at GrafanaCON, where we shared how easy it is to create a bird monitoring solution. If you missed it, here’s a quick masterclass: all you need is a Raspberry Pi, a microphone, and one hour of spare time. We've written a detailed blog post to guide you through it. 

Inspired by Drilldown Apps and powered by open-source technology such as Grafana Scenes, Grafana App platform, and Grafana LLM, we developed a full-blown exploratory experience for birds. With **Birds Drilldown**, you don’t have to write queries or build dashboards anymore. Just open the app and start exploring! 

You’ll see the latest birdsong detection and be able to spot interesting patterns, such as how weather or air quality influences the quantity of birdsong. You can also learn which bird species sing the most or which songs vary the most by sorting the data and correlating it with environmental factors. 

Each bird has its own page in the app featuring a picture, descriptions, and the ability to listen to their songs—so you don’t have to go outside anymore! Additionally, we have integrated a 24/7 AI bird expert into the app using the Grafana LLM plugin to answer questions like the pronunciation of a penguin or its pooping schedule.

At our science fair booth, we showcase three main parts of our app: the bird monitoring setup (Raspberry Pi, microphone, etc.), some plush birds that make real bird sounds (since our idea of bringing actual birds flew out the window), and a demo of our app with Drilldown. Everything is hands-on, so we hope to see you at the science fair!

If birds aren't your thing but you’re more into games, let’s return to Domas and Bogdan.

Hello, everybody! I'm Bogdan, and I'm here with my colleague Domas. We're both software engineers, and we want to share our first hackathon project: **Faro**. After some time, we had our second hackathon. On the last day of registrations, we wondered what to create. It should be meaningful, fun, useful—a classic hackathon project. But we had no idea.

So we decided to answer the question: **Does Grafana run Doom?** 

Running Doom on various devices has always been a thing—MacBook Touchbars, ATMs, and even pregnancy tests. But what about Grafana? We created a data source plugin for Doom! It runs WebSockets and is a fork of Chocolate Doom compiled to WebAssembly by CloudFlare. 

We render the video into a WebGL buffer in memory, which we then translate to Grafana data frames, with 256 fields—one for each color. We stream it to a regular time series panel with 256 overrides. For every frame of Doom, it renders 64,000 data points. On my machine, I got it to run at 15 frames per second. 

We learned valuable lessons on maximizing performance for live streaming time series panels, such as avoiding expensive on-the-fly calculations by setting minimum and maximum values, keeping the list of fields constant, and pushing new data frames during the request animation frame tick. Also, if you’re using Chrome, enabling the Canvas out-of-process restoration flag helps significantly.

You can find our project live at [play.grafana.org](https://play.grafana.org), or you can scan the QR code. We’d love for you to visit us at the science fair and discuss our project further. Thank you!

## Raw YouTube Transcript

For those who don't know,
Grafana Labs really deliberately, strategically empowers engineers. Engineers get a lot of agency to push
and implement stuff which they actually want to see. And we dog
food all our offerings. And this is why personally I believe
we have so good offerings and the quality of our software is so good. We really do use the
stuff which we produce. We also have a system of hackathons
where four times a year every employee at Grafana - Go-to-Market, Engineering, G&A - everything can take a whole
week and work on whatever they like. The only thing which they have to do
at the end is to present a five minute video and then we rank and we vote
and we have winners and everything. Almost 50% of the hackathon
projects have already shipped or are in the process of being shipped.
And not everything ships, but a huge fraction does. And also a
lot of the features, which you see, a lot of what you saw on stage, a lot of what you're going to see on
stage is actually based initially on hackathons, but not all of
this is production grade. Some of this is just fun,
like for example, Super Grot. Hey everyone, my name is Gianni and
I'm excited to be here to share something that we
built during our most recent hackathon. So if you've
ever been in a hackathon, the energy can be wild with
people prototyping new features and pushing the boundaries of what
is possible to do with our products. However, at the last hackathon, Domas and I decided to do
something a little different, a little fun, a little tribute to a
little yellow dinosaur, our mascot, Grot. So we built something that was fun for us, something a little bit weird. So instead of explaining it, I will actually show it to you. Yes. All right, thank you. So it's an awesome platform or video
game starring Grafana's most adorable mascot. We built it using Phaser JavaScript video
game engine and the [inaudible] in the browser, you can play
it on almost any device. And of course we instrumented
it with Grafana Faro web SDK, so it's reporting level completion times scores, player devs,
coins, and other data. There's a public dashboard, you
can find it on play.grafana.org. And if you post a good
time or a high score, it'll show up there for everyone to see. If you want to try it out,
and you definitely should, you can scan the QR code
and play it on your device, or you can come and find us at
the science fair section on the second floor where you can actually
play it in a little arcade cabinet that we have built for the conference.
So please come check it out. We'll see you there. And now we continue talking about birds, about dinosaurs, from dinosaurs to birds with the next
project. Birds Drilldown. Thank you. Yeah. Hi. So we are Ivana and Sven and we want
to talk about our little fun hackathon project, but for now, let's
talk about Drilldown apps. As we've just heard in the
keynote: Metrics, Logs, Traces, and Profiles Drilldown are now
GA, which is really amazing. You don't need to know
LogQL, PromQL. TraceQL anymore to write your queries, Drilldown Apps really
unlock a queryless and effortless, easy, opinionated solution to query your
data and get insights into the data that you are looking for.
And they're really awesome. I can just encourage everyone
to go and try them out. However, I think there's something missing in
this list. What do you think, Ivana? I think you're very right, Sven.
There is something missing. Where is the Birds Drilldown?
And if you're all sitting here, very confused right now. No worries. Let
me provide a little bit more context. Me and Sven, we have a little
side hustle, side quest going on. We are on a mission to
make Grafana recognized, not just as a monitoring
company, but very specifically, a birdsong monitoring company.
So when someone says Grafana, we want people to
immediately think, "Oh yeah, dashboards and birds."
It started all right here at the last year's GrafanaCON where we
shared how easy it is to create a bird monitoring solution. If you weren't
here or if you've missed it, here is a super quick masterclass. All you need is Raspberry
Pi. Then you need microphone, one hour of the spare time. And we have written a very detailed
blog post that you can just follow. Of course, you'll need some
birds that you will monitor. Inspired by Drilldown Apps
and powered by awesome open source technology
such as Grafana Scenes, Grafana App platform and Grafana LLM. We've built a full-blown
exploratory experience for birds. With Birds Drilldown, you don't need to write queries
anymore or build dashboards anymore. All you need is to open the
app and start exploring. You will immediately see the
latest bird song detection. You will be able to spot interesting
patterns and learn how things such as weather or air quality influences
the quantity of the bird songs. Moreover, if you are interested to learn more
about which bird species sing the most or which bird species songs vary the most, you can simply sort by that and
then align this with environmental data to learn some interesting patterns. So every bird has its own page in the app
where you can see a picture of a bird. You can post some descriptions
or you can read about it. You can even listen to birds so you don't
have to go outside anymore, I guess. And nowadays, no great
project comes without AI. So we have a 24/7 AI bird expert
directly built into the app using the Grafana LLM plugin. And it's always there to answer your
questions like pronunciation of a penguin or it's pooping schedule, for
example. So at our science fair, we showcase three main parts
of our app. First of all, the bird monitoring setup,
so the hardware, Raspberry
Pi, microphone, and so on. We wanted to bring real birds, but that
idea flew out of out of the windows. So we brought bird plushies
that make real bird sounds, and obviously we demoed
our app with Drilldown. So everything is hands-on.
See you at the science fair. And if you're not that much
into birds, but more into games, back to Domas and Bogdan. So hello everybody. I'm Bogdan and I'm here
with my colleague Domas. We are both software engineers and we are going to start by mentioning
our first hackathon project. That would be Faro. Some time passed, and then we had our second hackathon.
And during the last day of registrations, we are there asking, what should
we do? It should be meaningful, it should be fun, it should be useful, it should be a normal hackathon project. But we had literally no idea. So we wanted to answer a question. Does Grafana run Doom?
So without any further... Running Doom in virtually every
device that can display pixels has always been a thing.
MacBook Touchbars, ATMs or even pregnancy tests. But what about Grafana? Can Grafana run Doom? So we created a data source plugin for Doom. Thank you. It runs Websocket's doom, which is a fork of Chocolate Doom
compiled to Web Assembly by CloudFlare. It's a rendering video into
WebGL Buffer in memory, which we then translate to Grafana
data frames with 256 fields, one per color. And then we stream it to a regular
time series panel with 256 overrides. So for every frame of Doom, it's
rendering 64,000 data points. And on my machine, I got it to
run at 15 frames per second. No, that was my machine. Your machine
did not run it to 15. Come on. All right. We learned a few things along the way
on how to max out performance for live streaming time series panels. It's important to avoid
expensive on-the-fly calculations
by explicitly setting minimum and maximum values for
your data on the data frames. Also, to keep the list of fields constant, even if they don't always have
any values for every frame. And push new data frames on window
request animation frame tick. Also, if running Chrome, it really helps to enable Canvas
out of process restorization flag, if it's not on already. So it is live on play.grafana.org, you can find it there or just scan the
QR code or please come and see it in the science fair and talk to us. Thank you. Thank you.

