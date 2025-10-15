# This Student Monitors Laundry and Browser Tabs with Grafana — Observability in Real Life

Published on 2025-06-07T05:35:29Z

## Description

Why monitor just servers when you can graph your laundry usage and open Chrome tabs? Dakota, a high schooler from Oregon, ...

URL: https://www.youtube.com/watch?v=_bMU_jRlFzU

## Summary

In this engaging talk, Dakota, a high school student from Oregon, humorously explores the concept of graphing unusual data, specifically focusing on laundry machine usage and browser tab management. He shares a story about a college friend's internet-connected washing machines and how they discovered an API to gather and graph data, revealing insights about optimal laundry times and user behavior. Dakota discusses his projects involving graphing browser tabs and introduces the G.O.P.T. stack (Grafana, Go, Prometheus, and Timescale) used for data visualization. He emphasizes the importance of finding joy in graphing unconventional metrics and concludes with takeaways about laundry timings and the value of creativity in data analysis.

# A Talk on Graphing Laundry and More

Hi, we're here to air out some dirty laundry today and talk about laundry. So, who am I? I'm Dakota. I'm still in high school, and I think I'm the youngest person in this room. If I'm not, I'd like to find out. I'm from Oregon, and I'm currently missing eighth period—though that’s not a real company; I just made that up. 

I have a cool graph for you guys, actually. This is why I skip school: to graph things. Boom! Before I get too far into this, is there a point to anything I'm about to tell you? And like most of the lightning talks, the answer is no. Well, kind of. If you want to learn, I think that messing around with Grafana and graphing weird things is the best possible way to do it. 

So, I'm assuming all of you know what you should be graphing, right? Latency, traffic, error saturation—Google SRE talks discuss all sorts of stuff about this. The four golden signals are common topics, but "should" is very different from "could." The "could" could be anything, right? We can graph anything that has a number that changes over time. I think Abraham Lincoln said that? But anyways, we can graph things like how many unopened emails, how many tabs we have open, and what our washing machine's doing. 

## A Story About Laundry

So what does this really look like in practice? Well, I have a story to share. Once upon a time, in a college dorm, a friend of mine who does computer science on the side for fun reached out to me. He said, "My dorm washing machines are internet-connected." He then shared a website where you could see how many minutes remained on your dryers—like, "Go get your laundry, please. We don't want it here!" 

I thought, "You can check out your laundry? That's awesome! Do you think there's an API?" And thus began the shenanigans. We found an API and realized we could get the state of it minutely. Initially, we considered making a game—buying or selling stocks based on what washing machines were doing. But then we thought, "Oh, what if we just graph it?" 

Bam! We can graph laundry. Here's the best time to run it: between 2:00 AM and 6:00 AM, if you can't tell. We analyzed 32 machines—16 washers and 16 dryers—all in the freshmen dorms. We could see people switching between loads; for example, someone starts a washer, then moves it to the dryer. While exploring the API, which was unfortunately unsecured, we discovered other interesting data fields, like whether a machine was open or closed and the soil level. Unfortunately, we couldn't graph how long stuff sat in the machine in limbo between changes because I live out of the dryer. I don't know about you guys! 

Since October of last year, we have about 9 million rows worth of data on washers and dryers in our Timescale database. Here’s a bigger graph—a whole dashboard! We can see how many loads we've run and the total usage if the washer was running nonstop 24/7. There are all sorts of fun little metrics we have.

## Graphing Tabs and More

Now, let's pivot a bit. How many tabs do you think you guys have open? Do you think you have more than a hundred? Raise your hand if you think I have more than a hundred tabs open right now. (Heckler: "You can't see!") Well, I can see a little. How about more than 500 tabs? A thousand? You see where this is going? *Boop!* I graphed it. 

You can see when I program and then stop programming. I close out my tabs because I have problems if I don't. We can graph tabs using a Chrome extension. You can also see outages in my home lab—I don't have very good power. While making my Chrome extension, I thought, "What other metrics can I grab?" A lot, apparently: bookmarks, how much RAM is available, muted tabs, and total windows. So, you see where this is going, right? *BAM!* Dashboard! 

You can download this extension and contribute to my dashboard if you'd like to. You can join the public tab graph or run your own private one. I set that all up and wrote documentation on it, so if you feel like graphing tabs, you totally should.

## Why Graph the Mundane?

Now, let’s pivot again because why not? Here’s a graph of all the graphs I don’t regret making. I think everyone should graph something dumb. We spend all day at work graphing computers and how many seconds it takes to respond to an error. I believe the most exciting things to graph are the things that are real. 

I spent maybe five minutes one day thinking, "Can we graph how many coffees people are getting?" Unfortunately, no. But we were close! My process is simply to find fun things to graph. I do it outside, at the gym, anywhere I go—listening to friends' bad app ideas generates lots of graphs.

You might be asking, "What's your stack, bro?" Well, I'm proud to introduce the G.O.P.T. stack. It makes use of Grafana, Go, Prometheus, and Timescale. It looks something like this when you use it. I write a lot of my scraping scripts in Go, scraping from unauthenticated APIs. Depending on my mood and energy levels, the data either gets pushed into a Timescale database for advanced queries or into Prometheus when I'm tired and lazy. But it’s still amazing to work with, and from that, we graph it all in Grafana. 

The push gateway is pretty awesome—it's a big player when you want to push from thin clients, like a browser extension for how many tabs you have open.

## What's Next?

So, what comes next? I'm hoping we can find patterns in this arbitrary data, like correlating rainfall with dryer usage. I think there’s a connection between all the data we have—points upon points. Also, I'm looking for an internship for this summer. I’ll be at the experts' booth after this if anyone’s interested. I’m for hire—I’ll fly anywhere!

As my language arts teacher always told me, “So what?” So, key takeaways: 

- You should run laundry between 2:00 AM and 6:00 AM if you're in college. I promise you it’s the best time—statistically, I have months of data to prove it.
- Sometimes we’re so preoccupied with whether or not we could do something that we should just stop and ask ourselves if we should do it.

If you know where that quote's from, you’re good. 

Anyways, that’s all I have for today. If you liked how I talked and found it funny, I try to write my blog (codaea.com) in a similar way. Hopefully, you learned something and had a good laugh. So, I accomplished rule number one. Thank you!

## Raw YouTube Transcript

Hi, we're here to air out some dirty
laundry today and talk about laundry. So who am I? I'm Dakota.
I'm still in high school. I think I'm the youngest person in this
room. If I'm not, I'd like to find out. I'm from Oregon. I'm currently
missing eighth period, and that's not a real
company. I just made that up. And I have a cool graph
for you guys, actually. This is why I skip
school - to graph things. Boom. Before I get too far into this, is there a point to anything
I'm about to tell you? And like most of the lightning
talks, the answer is no. Well, kind of, if you want to learn, I think that messing around with Grafana
and graphing weird things is the best possible way to do it. So I'm assuming all of you know what
you should be graphing, right? Latency, traffic, error saturation - google SRE
talks, all sorts of stuff about this. The four golden signals, but should
is very different than could, and "could" could be anything right? We can graph anything that has
a number that changes over time. I think Abraham Lincoln said that? But anyways, we can graph things
like how many unopened emails, how many tabs we have open, what
our washing machine's doing. So what does this really look like
in practice? Well, in practice, I got a story for us to get here.
So once upon a time, a college dorm, a college friend of mine who does
computer science on the side for fun, reached out to me and he was like, "My dorm washing machines are
internet connected." And he was like, "Check out this website." And I checked
out the website and you could click on it and you could see how many minutes
are remaining on your dryers. Like, "Go get your laundry please.
We don't want it here." And I'm like, "You can check out
your laundry? That's awesome. Do you think there's an API?"
And this only goes downhill. Commence shenanigans. Like
usual. We found an API. We realized that we could
get the state of it minutely. So we were initially going to make
some sort of game actually. And like, do we buy or sell stocks based off of
what washing machines are doing what? But we realized - I realized that wasn't a
very good idea. And then we're like, "Oh, what if we just graph it?"
And bam, we can graph laundry. Here's the best time to run. It's between two and 6:00 AM if
you can't tell. And these are 32 machines - 16 washers, 16 dryers, and they're all in the resident
hall of the freshmen dorms. We can also see people switch
between the loads. You can see up, somebody starts to washer right here, then you can see them
move it to the dryer. And then when we were doing this
and we were exploring their API, which was unsecured unfortunately, we realized there was
other sick data fields we could get, whether the was open or
closed or the soil level. Unfortunately we couldn't graph
how long stuff's sat in the machine in the limbo between somebody changing
it because I live out of the dryer. I don't know about you guys. So since October of last year, we have about 9 million rows worth of
data of just washers and dryers in our Timescale database. So
here's a bigger graph. Whole dashboard, right?
Like wow, lots of things. So we can see how many loads we've run. We can see the total usage of if
the washer was running nonstop 24/7. We can get current state. There's
all sorts of fun little metrics we have. And here's more graphs
too, right? I love graphs. We can go back and forth between
what's up and what's down in a sense. And if you want a more technical
writeup, this is my buddy's writeup. He also needs a job just like me. You should totally check this out. His blog is so much cooler than mine
or more technical and maybe less funny. Anyways, we're going to pivot a
little and segue over to how many, I can't see anything, but how many
tabs do you think you guys have open? Do you think you have
more than a hundred? Open? Raise your hand if you think I have
more than a hundred tabs open right now. (Heckler: You can't
see!) I can see a little. Do you think you have more than 500
tabs open right now? A thousand? Well, you see where this is
going? Boop, graphed it. So you can see when I program and
then I stop programming, right? I close out my tabs because
I have problems if I don't.
And we can graph tabs. This was just a Chrome extension actually. And you can also see the outages in my
home lab. I don't have very good power. And when I was in there making my
Chrome extension because I was like, "This is fun. What other metrics
can I grab?" A lot apparently: Bookmarks, how much RAM is available.
I didn't know they could even get that. Muted tabs, total windows. So you
see where this is going, right? BAM! Dashboard. You can
download this extension. Actually you can contribute to
my dashboard if you'd like to. And you can join the public tab graph
or you can run your own private one. I set that all up too and
wrote documentation on it. So if you feel like graphing
tabs, you totally should. So we're going to pivot
again because why not? And here's a graph of all the
graphs I don't regret making, right? I think everyone should
graph something dumb. We spend all day at work graphing
computers and how many seconds it takes to respond to an error. I think the most exciting things you
can graph are the things that are real. I spent maybe five minutes the first
day, someone can tell you about it, of can we graph how many coffees
people are getting? Unfortunately, no. But we were close. Really my process is, I just like to find fun things to graph. I do it outside at the gym anywhere I
go, listening to friends' bad app ideas, lots of graphs come from that. And you might be asking, well,
what's your stack, bro? Well, I'm proud to introduce the G.O.P.T. stack. It makes use of Grafana, Go,
Prometheus and timescale. And it looks something
like this when you use it. I write a lot of my scraping scripts
that scrape from unauthenticated APIs in Go. And depending on my mood
and/or energy levels, it either gets pushed into a timescale
database for really weird advanced queries and then Prometheus
when I'm tired and lazy. But it's still amazing to work
with. And from that, well, we graph it all in Grafana, right?
Push gateway is pretty awesome. It was a big player.
When you have something, when you want to push from thin clients
outwards like a browser extension for how many tabs you have
open, I have plenty of time. Let's see what else we
got. So what comes next? I'm hoping we can find patterns in this
arbitrary data between things like how much rainfall is there to
how much drier usage we have? I think that there's a connection between
all the data that we ever have, right? Points upon points. And also I
find an internship for this summer. I'll be at the experts booth after this
if anyone's interested. I am for hire. I'll fly anywhere. Anywhere. So from that, I was always told to do a
"So what?" by my language arts teacher. So with that being - key takeaways. You should run laundry between two
and 6:00 AM If you're in college, I promise you it's the
best time. Statistically, I have months of data to prove it. And just we're so preoccupied with
whether or not we could do something we sometimes should stop.
Whether or not should we. If you know where that quote's
from, you're good. Umm, man, I'm under like usual.
Anyways. That's all I have today. If you like how I talk
and you think it's funny, I kind of write my blog
the same way (codaea.com), or at least I try to the most part. And hopefully you learn
something and you all laughed. So I accomplished rule
number one. Thank you.

