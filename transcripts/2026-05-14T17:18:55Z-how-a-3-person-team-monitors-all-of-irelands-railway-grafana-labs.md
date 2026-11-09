# How a 3-Person Team Monitors All of Ireland&#39;s Railway | Grafana Labs

Published on 2026-05-14T17:18:55Z

## Description

Irish Rail built IRIS — a real-time railway monitoring platform powered by Grafana — with a team of just three, turning fragmented ...

URL: https://www.youtube.com/watch?v=Cr7yGJdMTI8

## Summary

The show titled "How a 3-Person Team Monitors All of Ireland's Railway" was published on May 14, 2026. The speakers included Richard Donovan, a technology consultant, and Seosaimh O Fatharta, the IRIS Project Manager at Iarnród Éireann. They discussed the development of IRIS, a real-time railway monitoring platform powered by Grafana, which integrates various IoT devices to provide actionable insights and alerts for Irish Rail. Key takeaways included the importance of user engagement in dashboard design, the flexibility of Grafana in handling different data sources, and the transition from reactive to predictive maintenance through real-time data monitoring. 

Topics: Grafana, IRIS, IoT, real-time monitoring, predictive maintenance, user engagement, data integration.

## Chapters

00:00:00 Introduction to Irish Rail's remote monitoring project
00:06:07 Building a real-time railway monitoring platform with Grafana
00:12:15 Building a real-time railway monitoring platform with Grafana
00:17:42 Real-time monitoring and alerting for railway operations
00:23:52 Building a real-time railway monitoring platform with Grafana

How many all just came for the AI like I did? Nobody? They're very polite. How many are using AI in actual production in their environments? Good, so that's quite a few. 

We are going to talk about something a lot older: rail systems, which are quite old. But I think you'll also see it's kind of the future of maybe where a lot of people are going with AI, doing the development of the websites and the apps. Our technology is spreading out into the real world, and this has been a challenge for Irish Rail, which we'll talk about. It's probably where a lot of us will end up working.

So I'm Richard Donovan. I'm a technology consultant that's been working with Irish Rail for four years now. 

- **Seosaimh:** And I'm Seosaimh O Fatharta. I'm the IRIS Project Manager with Iarnród Éireann, and I've been in Irish Rail for a bit longer than Richard, about 20 years.

I'm going to give you a glance at who we are. We are obviously the Irish National Railway company. Like all other railway companies, we were founded 180 years ago and we have almost two and a half thousand kilometers of track. 

This whole thing started off about a year and a half ago when I met Richard, and I was given a task for a remote monitoring project. I thought I knew what remote monitoring was at the time, but it turns out what we've been doing for the last 20 years was very remote. We had loads of instrumentation and devices out in the field, but none of them were integrated. They were effectively just very remote, out there, not talking to anything except for themselves. We would physically go out with a smart card or something, download it, and bring it back to the office.

Then about five years ago, IoT came along, and it was a game changer for us. We were working with a lot of surveying companies like Trimble and Hexagon, and a lot of smaller, tiny companies. But they all had the same thing in common: they all had their own dashboards, their own systems, and their own UIs. It was great; we were finally getting visibility on information in real time, analyzing patterns. I was in heaven. I was like, I don't need to go to site anymore. There's a battery powering the unit, it's sending the information up, and I've got instant visibility on it. 

And that's when the problem started. Basically, we were getting more and more devices. All of the devices were sending information up. There were a few slight technical problems, like the lads on the ground couldn't remember their passwords, they'd lose their passwords, they'd go on holidays, or the wrong mobile number would be input in the system. I had no control over how to manage the system. As you can see, it was getting very, very frustrating to manage that kind of base that was growing out of control, because we were going from having four or five devices to...

- **Richard:** Yeah, so we had over 50 plus vendors, everybody saying that they had the dashboard, their platform that we should all integrate onto. They had no desire to actually engage with users across the board. This is safety critical, so our time to understand what the problem is is key, as you'll see as the businesses move out into the real world. We're dealing with real data and real-world scenarios.

This was very frustrating for Seosaimh, and we didn't really have a solution. So, as any big state-owned organization that Irish Rail is, they went through a procurement process. Lots of documents were written, lots of requirements were gathered, and lots of people engaged with huge lists of IoT devices that we should all work through. And this went on for months...

- **Seosaimh:** Months and months and months. I remember it well. We were sitting down with all the procurement executives, and they were going through the process of what kind of instrumentation we had, what it could do, and so on. From my experience of 20 years, I knew what the machines could do. I could repair them, I could fix them, I could move them around. But what I couldn't get was the finished product. 

So, unlike a lot of solutions, I jumped right to the end. I said, "This is what we want, Richard. How the hell do we get here?" We just bypassed everybody in the middle.

- **Richard:** Don't tell 'em that. Don't tell 'em that. We followed the process.

So I suppose this is where the round of applause happens. Richard showed me Grafana for the first time, and I was like, "What is that?" It was all black, and I couldn't really understand it. He said, "This is what we want."

- **Richard:** He still has a problem with the black, actually.

- **Seosaimh:** Yeah, yeah. So you know the black theme in the background in Grafana? You'll see later on in my slides, I use white, but I've got a confession to make: after this event, I'm going back to the office tomorrow, and I'm going to change them all to black because all the guys up in the science fair... 

- **Richard:** A conversion.

- **Seosaimh:** Their slides are brilliant. Their dashboards are class; they jump out at me. I really feel it. So yeah, I'm a convert. Thanks.

This is part of this whole process. Again, this is probably not the most technical presentation, but this is an opportunity for you working with Grafana. It is so flexible working with end users, especially if the end users are not also DevOps or SREs. You're working with real people, real engineers who are used to doing physical things, and you turn up with what you think is a super sexy Grafana dashboard. Often, these guys don't like it or the look of it. 

I've worked on projects where we built beautiful dashboards and showed them to the customer, and they said, "We hate it." We asked, "What do you want?" They said, "I want a big green dot over there in the corner, 'cause we never look at this, and if anything goes wrong, it turns red. If anything happens, then we'll call you." This is the early stages of engaging with a customer and actually finding out what they want. Sometimes, less is more.

So we went through this whole procurement process that was going absolutely nowhere. We had all these vendors trying to sell us super expensive systems all the way up to SAP that were very bespoke. They would take six months to produce anything sort of demo, and if we wanted to make a change, that would be another six months. Obviously, that's not the world I came from, and I didn't think this was good for the solution.

So I started introducing this more adaptability. Basically, from my laptop, I started showing Seosaimh a Grafana dashboard with mock data from a laptop, saying, "What do you think of this? Does this start looking like what you might want?" He said, "I like this bit, I don't like these bits." We started iterating very quickly with our chief subject matter expert and then started expanding it out to other engineers and other stakeholders across the organization. 

We had no data, but we had...

- **Seosaimh:** We had plenty of data. It just wasn't integrated.

- **Richard:** We had no access to any data.

- **Seosaimh:** Had no access. 

But we had a concept now that the engineers were buying into. They liked the look of it; they could understand it easily. If we could get them more of this, they would actually buy into it. So how do we get them more of this? From a laptop, we started off with an MQTT broker and began searching for existing data providers across the organization.

- **Seosaimh:** So I'll jump in there 'cause I remember the day. Like I said, we're working with multimillion dollar companies and small, tiny companies with one person in his bedroom delivering a sensor device. It was a lot easier to work with one individual. I remember him well. He was a small operator with a little weather station, and he was just providing us with temperatures and moisture content. And he went on board straight...

way. He goes, "Look, all you need is an API." I came back to tell Richard, and he goes, "I didn't know you knew what an API was." I still don't, but I got it. And Richard is like, "Perfect. We have our data." 

We took that, we ran with it, and within what, two days? We had it up. The managers just couldn't believe what we had done. Not only did we put it up, but we used the alerting system on it. It was in the middle of the summer, and with rail and temperature, we can't run trains when the temperature gets too hot in a CWR (continuously welded rail) because you have a chance of buckling. So, you get a hot summer or a hot day, and sometime in the mid-afternoon, which it—ironically, it does happen in Ireland. 

Oh yeah. It happened in, I think it was June or July. But anyways, we had built a system not knowing that this weather was coming in, and we had an alert system built in. Richard asked me, "Give me some phone numbers just to trial this on." So, I fired out a few phone numbers to some of our managers, and all of a sudden, their phones were ticking, getting alarms. "What's this? It's like 44 degrees somewhere in Cork." And they're calling me, "Seosaimh, what are you sending us?" I'm sending, "That's the data." 

Unknown to us, my original supplier, Declan, his system wasn't working properly, and he wasn't sending any text messages even though we were paying for it. His system was like, what, 10 years old? And it was our take. Or we would say it was elegant and simple. It was one little box and a SIM card and some sensors wired up to it. 

Once Richard bought it into the IoT world, it was going down that way as opposed to poor Richard not paying his call card for the— 

That was the key thing. So we started sending out alerts to the end users saying, "Your tracks are getting hot." And they're going, "How come the system of record is not sending us any messages?" We found out the guy was running a prepaid SIM card, and he had forgotten to top it up. 

So it went from, "Why are you guys spamming us with bogus data?" to, "Hey, you guys are now the belt and braces because we're safety critical." We're not frontline safety yet, but you guys are now the belt and braces that we can see what's going on. You can gather the data and you can start sending out alarms and alerts that really provide actionable intelligence to the people. 

Right? And that was one sensor. They're used to dealing with one sensor. But now we were starting to get that traction where more people were coming to us saying, "Can you work with this sensor?" And again, with the platform being so flexible, we could start adding more and more sensors onto the platform. 

So we had now some user engagement being, again, a sort of risk-averse organization, big organizations. Only when they start to see a real platform turn up, which was at zero cost at this stage, would managers start to get involved because, you know, it's good for their reputation to have something, and if there's something concrete there, it makes a big difference. 

And Seosaimh came up with a genius idea to brand it. 

Yeah, like people have ideas all the time, but trying to get it out there and trying to get them to believe in it, you only get one chance at it. So we had a demo day, or a continuous improvement day in somewhere like this. Not as big as this, obviously. This is massive. And I told Richard, "We just need to get it out there. It needs to be flashy, it needs to be cool, it needs to have a bloody name as opposed to Grafana." 

So we're calling Grafana, we can't call it Grafana. We have to have our own name for it. So we came up with IRIS. 

You came up with IRIS. 

I came up with IRIS. So originally, it was the Infrastructure Remote Monitoring and Inside Systems, which was very, very engineering, very civil engineer. We said, "You know what? It's bigger than us. Let's call it something else." So we called it Irish Rail's Intelligence Sensing. 

And since then, from being an infrastructure project, it's grown to the whole company, whereas we've got like BNF building and maintenance looking at it for elevators. 

We've got— 

Yep, cameras. 

We've got cameras. Do you want to tell them about that? 

No. Everybody, actually what— 

What you can do with a camera is amazing. 

The cameras in the lifts they have turned off because things that happen in the elevators that nobody wants to see, but that's another story. 

So— 

Counting people in stations and clusters. You can do anything. We're looking at cameras. So I've been using lenses for years. Some of the engineering companies and serving companies, really good top-of-the-range lenses. And they can monitor movement for me. 

So picture, you've got like a bridge, and you've got a target on a bridge, and you've got, let's say, some sort of a total station measuring the distance. If any movement, vibration, anything, it'll pick it up. Lo and behold, that lens, the Leica lens, is also able to catch it now without any targets. It'll just catch the corner of a limestone keystone on the bridge, and it will know if it's moved. 

It'll catch the length of an embankment if it's going straight, and if you have a slide or deviation, it will tell me, "Oh, it's gone five mls, it's gone 10 mls." Something, what, 10 years ago was— 

Not possible. And it's now possible in very cheap hardware. So the ubiquity of cheap, affordable, high-quality hardware is a game changer. The ability to gather the data is the bit that's probably the bit that's missing that Grafana is filling the gap in. 

And this is where it starts to become a game changer for, say, not so technical, not so software-oriented companies to start going, "This is doable for us." This is also doable for us to do mostly in-house. 

And we haven't talked about the stack very much, but obviously, Grafana is a key part of it. We wouldn't have, we don't have a big—I have one graduate, I have no software developers to work with me on this. 

This is a team of three. 

Yeah. 

That developed this. 

And so it started with something like Postgres, and then went up to TimescaleDB because that's a familiar technology. And this is, whilst Grafana has a great stack, we were able—it's so pluggable and adaptable, we were able to plug in initially the technology that really works with what you've got on the ground. 

It's not prescribing a very complicated stack. If I had gone in with the full stack of Loki and Mimir and everything else, I would've just lost most of the audience. And I've lost my own graduate working on it. 

But it can do plain SQL on TimescaleDB. It can plug into APIs and the simple devices we had, and suddenly, we were up and running with a robust industrial stack, but super simple. 

Okay, so IRIS itself, so turning data into vision was our kind of catchphrase at the beginning. And I can honestly say that we did it. 

So its foundations are four key pillars of collecting data, monitoring alerts, insights, and decisions. So like I said earlier on, collecting the data was quite easy. We used multiple IoT devices in the field, all remotely connected with SIM cards, and onto the cloud computing. 

What it allows us to do is to collect real-time information, trigger alarms and predefined thresholds that are already set, and send SMS messages to the users, or whoever the maintenance lads are on the ground. 

Of course, our field, being a big huge organization, customization was a massive part of this because there's no point sending a text message alert to somebody in one part of the country when it should be going to somebody in the other part. 

Also, in Ireland, there are 28 days of holidays a year. So it's kind of managing the guys who are on call, or who have moved from one job to the next was a major thing. Getting their phone numbers, their email addresses in. The alerting system on IRIS allowed us to do that. The data that we were getting was brilliant.

insights. Insights we never had before. We can understand the behavior and the relationships between our assets, between our bridges, and between our track. Even for the weather, like when we had flood events. Where am I going with this? So, yeah, we had customized dashboards for each area. All that decision allowed us to be really, really reactive when those threshold levels were triggered, and it allowed people to be better decision makers. 

One of the things that everybody kept telling me was, "Oh, we're all engineers. You know, we want to have engineering judgment." My answer to them was always, "But I'm giving you more time to do that. So let the data guide you and free you up, and you won't be trapped looking at Excel charts all day." And that was probably great feedback.

So this is what it looks like. Again, sorry, it's white for now, and it'll be black tomorrow. But this is just a dashboard from one of our operators, and his area has, I think, five different ones there. But straight away, it's all green. And green is gold. Green is good. Green is "don't worry about it." But you can see the number four at the bottom, not really jumping out at you, but it's there. And the red warnings, and then there's one amber. And that's what I wanted to hit on. I want them to trigger onto that message going, "Where's that four, and what do I do about it?" 

So let's go to the next slide. 

This is a very basic presentation, a very basic stack. We've got, again, one graduate working on this. We haven't really done much with the alerting components. We are using Windows to make sure that the end users are not getting spammed with SMSes, which is also very important. We've got a long roadmap to go, 'cause we're getting now, of course, buy-in and more resources. But we are able to start super simple and get real value out to the people out and around the world.

Here are two different pages, planes that we have. GIS, that's another in engineering. We love our GIS, we love our coordinates, and we love to know where we are. As engineers, we always go to the map. We just go to a map, a chart, whatever you want to call it. So we've got three red alerts here, and straight away I can tell that there are actually four on the map. So they're scattered around Ireland. Now, there are four different individual areas. 

There might have been some work happening that night. The manager comes in the morning, he gets a handover, and he goes, "Well, why have I got red dots on my dashboard?" And straight away, he's able to call his local representative in that area and go, "We were out there last night, and the door wouldn't close on whatever unit it was, and it was giving us an error feed." All those triggers were coming back into Grafana. 

We were able to report on it. Obviously, the reds will have to be fixed straight away, and there's a time limit on them. The amber is also handy because some things are out of our control. Like it might be batteries getting low. You know you've got 20 hours to get out there to repair the battery before it goes red. And that's really handy. It's almost better the amber stuff than the red stuff because I don't want anything going red. But when it goes amber, I can go and solve the problem before it becomes a problem.

And that's the snowball that we're getting on. So the first challenge we get is the GIS. Can we work with GIS? And it does. Again, we're not buying a super expensive system. The second thing is, can we bring in asset data? Everything's driven by numbers and driven by SAP. What can we pull in asset data and display it so it's relevant to people? We can, again, for a very low cost, start with an open-source system, which is a game changer for them. 

As soon as you see this, and as soon as we get the engagement with the users, it's like, "Okay, we can give them the status hot or cold, or what the temperature is." But we can also start saying, "Well, what's the battery like? When has it been patched? What's the firmware?" It opens up all those conversations in a nice way. We're not just traditional procurement; we're not generating a massive bunch of requirements to hit people with a stick and giving no solution. 

With the stack, with Grafana, we're giving them a solution saying, "We can gather the data, we can display the data, and now we can start enhancing it and enriching it without starting another massive project that builds another separate system that silos all the data into somewhere else."

The real-time aspect of it is perfect. This happens in Ireland all the time: rain, flooding. You'd be surprised at how they elevate. You could wake up in the morning, and it's lashing rain. What you don't know is it's been lashing the previous two days, and that's building up saturation levels. All of a sudden, if it gets higher than the top of the rail, I've got to go and put a mitigation in place for that. 

Before, that involved somebody going out or being retrospectively informed by the train drivers, "Hey, you've got flooding on both sides of the track." Now, we can go and use remote monitoring, put out temporary devices anywhere we want in a matter of hours, and have instant feedback coming back to the office. This is saving travel time for the operators, getting out in the vans, walking down the tracks, and setting up a secure method to get to the site because we work in a red zone. The railways are a no-go area. 

If you want to get out there, I won't tell you how much paperwork you have to do just to get out there, but it's near to impossible. So having something remote takes the boots off the ground, and our safety department will love us first. 

Taking possession of a track or going out onto a track can be a dangerous thing. Depending on where it is, there could be high-speed trains running around. So it's a non-trivial activity to send somebody out to a location to do an inspection. Again, all of this helps in a very nice, elegant, clean way.

On the right-hand side of the screen is a screenshot of my phone with the very first alert. Since then, I've discovered that I'm bombarding everybody with alerts, and like anybody, once you start sending them too much, they're like, "Oh, it's another alert from Seosaimh. Another alert, another alert." I quickly found out to grab their attention, and this is to the developers in the room, that I've got three requests from the alert system. 

The first alert is the initial result, flashing in red. Then there are repeat alerts every hour or every two hours, or whenever I want to, maybe in orange. And then the best alert is when the problem is solved, and that goes in, I don't know, a line. I won't use green again. 

But are you with me? It's all about just wanting to flash on their phone, have a look at it, and see something quickly. They don't want to go looking at the dashboards. The dashboards are great for my meetings, but the lads who are under pressure tell me the information. I want to go and react straight away. That's their job. They're like firefighters. Without them, our trains wouldn't move. 

The level above them, again, in senior management, they love dashboards. They can instantly say, "Huh? So you're going to work on that?" This is what happens after the shift. We've got to stop that. Dashboards are for everybody. Dashboards are for the maintenance guy who's in the van who's got his mobile phone. It's for his manager who can go and push notifications towards him. It's for us in the back office to be able to use the information and push notifications to create work orders. 

And then, something happened last week, and I got a phone call from one of our engineers, and he asked me, "Seosaimh, could you..."

"Tell me the temperature of the track on the 15th of August last year?" And I'm like, "Eh, unusual request, but yeah, give me two seconds." I went back into the history, and there was another event that day. He just wanted to know if the spike in temperature caused it. Before, I would've had to go back to the vendor, ask him for a check—probably would've asked for money. But yeah, I would've asked him for the trace because I wouldn't have had it. Having the history on our own server allowed me to go back in Grafana, and with the time map, I think I had it in less than 30 seconds. 

So that's another part of it. Again, we don't sort of pitch it, but you start to get sovereignty of your own data, which is very good for these organizations. We're starting from the super simple stack, which is a great way to get going. You know, from the sensors, we're moving towards MQTT. MQTT allows us to start setting a standard across the whole organization, an ontology of all the data, if you will, that actually maps back to SAP, which they absolutely love. That's a big game changer; we have this correlation of all the data. 

We're using Timescale for now because it's super simple and robust, and it's working really well for us. We're diving deeper into Grafana for alerting the anomalies. The AI we're very excited about because it provides real operational insight, not just some noise. The thing we're just tiptoeing into is what we'll talk about, but we don't have time for it, which is sensor fusion. So when there is rain, and we can see the weather forecast, and we know the status of the tracks, suddenly that becomes a much richer picture for people who are now making decisions about what's really going to happen.

So where do we go? We went from one sensor on a laptop, some demos, then to small operators that would actually talk to us. We were working with them to get access to some data, and now it's built into the procurement contracts that we're going forward with. They must share the data. We prefer to have it in MQTT, but we'll work with almost anything. It's rolled out across regions and hubs across the whole country. It's a simple, robust architecture that scales well with us, especially within MQTT. We basically have national coverage in a fraction of the time, at a fraction of the cost, with very happy customers, which is probably the most important thing.

We're then working on more integrations now to the service management systems and the asset management systems. Nearly everything has a service life and a history built into it. We can start working with that data, pulling it from a different direction to give people insights on when they should do their maintenance and preventative maintenance. For the actual passengers and the customers we're working with, we feel that we're making a real difference in that they should not see the problems. We should know about the problems long before any interruptions of service for customers or threat warnings. Our time to notification, our time to fix, our time to be aware of it has gone from potentially hours and days—some random person ringing up, a driver calling in saying, "Hey, the track is getting flooded," or "There's a disruption," to devices going off, real-time sensors.

Time is definitely the biggest factor in what the outcome was. I can't emphasize it enough. From getting that phone call to knowing that phone call never has to happen is magic for us. You know? You get on the train in the morning, and you sit down, and you don't know there's a fault, like, I dunno, 50 miles up the road. By the time you get there, I've already known the fault, there's an engineer gone out, solved it, and the train keeps going at line speed. But that train might have been slowed down to travel at a safer, reduced speed. Or it might just be a technical glitch that can be resolved remotely. But if you don't know about it, you can't fix it.

So that makes us go from being very reactive to now getting into almost predictive, where we can solve things before they actually happen, or nobody's really aware of it. For us now, Grafana as a core has become much more than just a dashboard of data that sits on a wall somewhere. It is really an operational hub for information that takes a very old company to a real-time data-driven company without having to have massive consultants and a whole transformation, cultural change. It's that ease of use of working with Grafana and its flexibility to deal with feedback that has made it so special to us. Not to mention it's open source, which we all love here. It's not taken us down strange routes with strange companies and strange technologies. It's been able to scale with us to now hundreds and thousands of sensors in the roadmap with no problem.

We're running it on Azure for now. It's been super simple to run; it's been robust. We've had zero issues with it, which has been a kind of revelation for them. Our roadmap, you can kind of guess, is going to include AI, anomaly detection, and insights. We have a backlog of many thousands of different types of sensors that people are interested in and fusing them. So when we get an alert, a camera can look at that device and see if somebody is tampering with it, if anything has changed, or if there’s a truck hanging off a bridge somewhere because somebody's driven into it. That gets us to a much better place, quicker, faster, better, and easier for the people working with it. They're not out in the field in all weathers trying to find out what the hell happened in a location.

The kind of takeaways from all of this, with this stack being so flexible, is that you can start simple. You can start doing showcases; you can start from your laptops. You can be super iterative with your potential customers, clients, and people out there to workshop it in real time. We drag and drop dashboards in real time with them, which is a game changer for them. It allows you to scale into various technologies that will give you an architecture that will scale out to the real world and take sense of devices from anywhere we've seen.

But once we build it, we can just duplicate it. That's the biggest learning I have: duplication. That loop that goes around, the more sensors I get. Like, I'm telling Richard, "We're gonna run out of space," and he's like, "Ah, don't worry about it. There's plenty of space out there." 

But yeah, look, it's been great. I can't applaud the guy beside me enough for introducing me to Grafana on the very first day. We hope to keep on going because it becomes our sovereign platform for our data, which we can do what we need to and get that insight. We're very interested in the Grafana insights as well. 

How do we start getting more insights out of the data we're collecting? And we go from alerts to much more information across the system. 

[Seosaimh] And the business intelligence part of it. 

Yeah. So cool. 

Okay, thanks very much. (audience clapping)

## Raw YouTube Transcript

How many all just came
for the AI like I did? Nobody, they're very polite. How many are using AI in actual production in their environments? Good, so that's quite a few. So we are gonna talk about
something a lot older. Rail systems, which are quite old. But I think you'll also
see it's kind of the future of maybe where a lot of
people are going with AI, doing the development of
the websites and the apps. Then our technology is spreading
out into the real world. And this has been a
challenge for Irish Rail, which we'll talk about, and it's probably where a lot
of us will end up working. So I'm Richard Donovan. I'm a technology consultant
that's been working with Irish Rail for four years now. And Seosaimh. - And I'm Seosaimh O Fatharta. I'm the IRIS Project Manager with Iarnród Éireann, and I've been in Irish Rail for a bit longer than Richard, about 20 years. And so I'm gonna talk about,
at a glance, of who we are. So we're obviously the Irish
National Railway company. Like all other railway companies, we were founded 180 years ago and we have almost two and a half thousand kilometers of track. This whole thing started off about a year and a half ago when I met Richard, and I was given a task for a remote monitoring project. I thought I knew what
what remote monitoring was at the time, but it turns out what we've been doing for the last 20 years was very remote. We had loads of instrumentation and devices out in the field, but none of them were integrated. They were effectively just
very remote, out there, not talking to anything
except for themselves. And we would physically go
out with us with a smart card or something and download it and bring it back to the office. And then about five years ago, I suppose, IoT came along. And it was a game changer for us. We were working with a lot of surveying companies like
Trimble and Hexagon, and a lot of smaller, tiny companies. But they all had the same thing in common. They all had their own dashboards. They all had their own systems. They all had they're own UIs. And it was great. We were finally getting visibility on information in real time, analyzing patterns. Like, I was in heaven. I was like, I don't need
to go to site anymore. There's a battery powering the unit. It's sending the information up, and I've got instant visibility on it. And that's when the problem started. Basically, we were getting
more and more devices. All of the devices were
sending information up. There was a few slight technical problems. Like, the lads on the ground couldn't remember their passwords, they'd lose their passwords,
they'd go on holidays. The wrong mobile number would be input in the system. And I had no control how
to manage the system. As you can see, it was getting very, very frustrated on how to manage that kind of base that was growing out of control, because we were going from like having four or five devices to. - Yeah, so we had over like, 50 plus vendors, everybody saying that they had the
dashboard, their platform that we should all integrate onto. They had no desire to actually engage with users across the board. And this is safety critical. So our time to under
understand what the problem is, is key as you, again, as you'll see, as the businesses move
out into the real world. And we're dealing with real data and real world scenarios. So this was very frustrating for Seosaimh, and we didn't really have a solution. So as any big state owned organization that Irish rail is, they went through a procurement process. Lots of documents were written, lots of requirements were gathered, lots of people engaged with huge lists of IoT
devices were gathered and that we should all work through. And this went on for months, - Months and months and months. And I remember it well. We were sitting down with all the procurement executives, and they're going through like, the process of, you know, what kind of instrumentation have we got, kind of do this, kind of do that. And from my experience of 20 years, I knew what the machines could do. Like, I knew the machines inside out. I could repair them, I could fix them, I could move them around. But what I couldn't get
is the finished product. So unlike a lot of solutions, so maybe some of them, I jumped right till the end. I said, this is what we want, Richard. How the hell do we get here? And we just bypassed
everybody in the middle. So we kinda reversed-
- Don't tell 'em that. Don't tell 'em that. We followed the process. - So I suppose this is where the round applause happens. Whereas Richard just showed me Grafana for the first time and I'm like, what is that? And it was all black, and I was like, couldn't
really understand it. And he was, this is what we want. - [Richard] He still has a problem with the black, actually. - Yeah, yeah. So you know, the black theme in the background in Grafana? You'll see later on in
my slides, I use white, but I've got a confession
to make after this event. I'm going back to the office tomorrow. I'm gonna change 'em all to black because all the guys
up in the science fair. They- - A conversion. - Their slides are brilliant. Their dashboards are class,
they jump out oat me. I really feel it. So yeah, I'm a convert. Thanks. - And so this is part
of this whole process. Again, this is probably not the
most technical presentation, but this is an opportunity
for you working with Grafana. It is so flexible working with end users, especially if the end users
are not also DevOps or SREs. You're working with real
people, real engineers who are used to doing physical things, and you turn up with what you think is a super sexy Grafana dashboard. And often these guys don't like it, don't like the look of it. I've worked on projects where
we built beautiful dashboards and we showed it to the customer, and they said "We hate it." And we said, "Well, what do you want?" He says, "I want a big green
dot over there in the corner, 'cause we never look at this, and if anything goes wrong, it turns red. And if anything happens,
then we'll call you." Like, this is the early stages
of engaging with a customer and actually finding out what they want. And sometimes less is more. So we went through this
whole procurement process that was going absolutely nowhere. We had all these vendors trying to sell us super expensive systems
all the way up to SAP that were very bespoke. That would take six months to
produce anything sort of demo. And if we wanted to make a change, that would be another six months. And obviously, that's not
the world I came from, and I didn't think this
was good for the solution. So I started introducing
this more adaptability, basically from my laptop, I started showing Seosaimh
a Grafana dashboard with mock data from a laptop saying, what do you think of this? Did this start looking
like what you might want? And he said, "I like this
bit, I don't like these bits." And we started iterating very quickly with our chief subject matter expert, and then started expanding
it out to other engineers and other stakeholders
across the organizations. We had no data, but we had... - We had plenty of data. It just wasn't integrated. - We had no access to any data, - Had no access. - But we had a concept now that the engineers were buying into. They liked the look of it, they
could understand it easily. And if we could get them more of this, they would actually buy into it. So how do we get them more of this? So from a laptop, we start off with an MQTT broker, and start searching for
existing data providers across the organization. - So I'll jump in there 'cause I remember the day. Like I said, we're working with
multimillion dollar companies and small, tiny companies with one person in his bedroom delivering a sensor device. It was a lot easier to
work with one individual. He was, I remember him well. He was a small operator with a little weather station, and he was just providing
us with temperatures and moisture content. And he went on board straight way. He goes, look, all you need is an API. I came back to tell Richard, and he goes, I didn't know you knew what an API was. I still don't, but I got it. And Richard is like, perfect. We have our data. - Yep.
- We took that, we ran with it, and with what, two days? - Yep.
- We had it up. - Yep.
- And the managers just couldn't believe what we had done. Not only did we put it up, but we used the alerting system on it. - Yep. - And it was in the middle of the summer, and it was a really, with rail and with temperature, we can't run, nobody can run trains when the temperature
gets too hot in a CWR, continues welded rail, because you have a chance of buckling. So you get a hot summer or a hot day, and sometime in the mid-afternoon, which it-
- Ironically, it does happen in Ireland.
- Oh yeah. And it happened in, I think it was June or July. But anyways, we had built
a system not knowing that this weather was coming in, and we had an alert system built in, and Richard asked me, give me some phone numbers
just to trial this on. - Yep.
- So I fired out a few phone numbers to some of our managers, and all of a sudden, there's phones ticking, getting alarms. What's this? It's like 44 degrees somewhere in Cork. And they're calling me. "Seosaimh, what are you sending us?" And I'm sending, that's the data. Unknown to us, my original supplier, Declan, his system wasn't working properly, and he wasn't sending any text messages even though we were paying for it. His system was like, what? 10 years old. And it was, it was our take. - Or we would say it
was elegant and simple. It was one little box and a SIM card and some sensors wired up to it. - Yeah. Once Richard bought it into the IoT world, it was going down that way as opposed to poor Richard not paying his call card for the-
- That was the key thing. So we started sending out alerts to the end users saying your tracks are getting hot. And they're going, how
come the system of record is not sending us any messages? And we found out the guy was
running a prepaid SIM card, and he had forgotten to top it up. So it went from why are you guys spamming
us with bogus data with, hey, you guys are
now the belt and braces because we're safety critical. We're not frontline safety yet, but you guys are now the belt and braces that we can see what's going on. You can gather the data and you can start sending
out alarms and alerts that really provide actionable
intelligence to the people. Right? And that was one sensor. And they're used to
dealing with one sensor. But now we were starting
to get that traction where more people are coming to us saying can you work with this sensor? And again, with the
platform being so flexible, we could start adding more and more sensors onto the platform. So we had now some user engagement being, again, a sort of risk
averse organizations, big organizations. Only when they start to see
a real platform turn up, which was at zero cost at this stage, would managers start to get involved, because, you know, it's
good for their reputation to have something, and if there's something concrete there, it makes a big difference. And Seosaimh came up with
a genius idea to brand it. - Yeah, like people
have ideas all the time, but trying to get it out there and trying to get 'em to believe in it, you only get one chance at it. So we had a demo day, or a continuous improvement day in somewhere like this. Not as big as this, obviously. This is massive. And I told Richard, we just
need to get it out there. It needs to be flashy,
it needs to be cool, it needs to have a bloody
name as opposed to Grafana. So we're calling Grafana, we can't call it Grafana. We have to have our own name for it. So we came up with IRIS. - You came up with IRIS.
- I came up with IRIS. So originally, it was the infrastructure, remote monitoring and inside systems that was very, very engineering,
very civil engineer. We said, you know what? It's bigger than us. Let's call it something else. So we called it Irish
Rails Intelligence Sensing. And since then, from being
aN infrastructure project, it's grown to the whole company, whereas we've got like BNF building and maintenance
looking at it for elevators. We've got-
- Yep, cameras. - We've got cameras. Do you wanna tell them about that? - No. Everybody, actually what- - What you can do with
a camera is amazing. - The cameras in the lifts
they have turned off, because things that
happen in the elevators that nobody wants to see,
but that's another story. So-
- Counting people in stations and clusters. You can do anything. We're looking at cameras. So I've been using lenses for years. So some of the engineering companies and serving companies, really good top of the range lenses. And they can monitor movement for me. So picture, you've got like a bridge, and you've got a target on a bridge, and you've got, let's say some sort of a total station measuring the distance. And if any movement, vibration, anything, it'll pick it up. Lo and behold, that lens, the Leica lens, is also able to catch it
now without any targets. It'll just catch the corner
of a limestone keystone on the bridge, and it
will know if it's moved. It'll catch the length of an embankment if it's going straight, and if you have a slide or
deviation, it will tell me, oh, it's gone five mls, it's gone 10 mls. Something, what, 10 years ago was... - Not possible. And it's now possible
in very cheap hardware. So the ubiquity of cheap, affordable, high quality hardware is a game changer. The ability to gather the data is the bit, that's probably the bit
that's missing that Grafana is filling the gap in. And this is where it starts
to become a game changer for say, not so technical, not so software oriented companies to start going, this is doable for us. This is also doable for
us to do mostly in-house. And we haven't talked
about the stack very much, but obviously, Grafana
is a key part of it. We wouldn't have, we don't have a big, I have one graduate, I
have no software developers to work with me on this.
- This is a team of three. - Yeah.
- That developed this. - And so started with
something like Postgres, and then went up to TimescaleDB because that's a familiar technology. And this is, whilst Grafana has a great stack, we were able, it's so pluggable and adaptable, we're able to plug in
initially, the technology that really works with what
you've got on the ground. It's not prescribing a
very complicated stack. If I had gone in with the full stack of Loki and Mimir and everything else, I would've just lost most of the audience. And I've lost my own
graduate working on it. But it can do plain SQL on TimescaleDB. Can plug it into APIs and
the simple devices we had, and suddenly, we were up and running with a robust industrial stack, but super simple. - Okay, so IRIS itself, so turning data into vision was our kind of catchphrase
at the beginning. And I can ally say that we did it. So its foundations are four key pillars of collecting data, monitoring alerts, insights, and decisions. So like I said earlier on, collecting the data was quite easy. We used multiple IoT devices in the field, all remotely connected with SIM cards, and onto the cloud computing. What it allows us to do is to collect real time information, trigger alarms and predefined thresholds that are already set, and send SMS messages to the users, or whoever the maintenance
lads are on the ground. Of course, our field, being a big huge organization, customization was a massive part of this, because there's no point
sending a text message alert to somebody in one part of the country when it should be going to
somebody in the other part. Also, in Ireland there's 28 days, holidays a year. So it's kind of a managing
the guys who are on call, or who have moved from one job to the next was a major thing. Getting their phone numbers,
their email addresses in. The alerting system on
IRIS allowed us to do that. The data that we were getting,
giving us brilliant insights. Insights we never had before. We can understand the behavior and the relationships between our assets, between our bridges, between our track. Even for the weather, like, when we had flood events. Where am I going with this? So the, yeah, so we had customized
dashboards for each area. All that decision allowed us to be really, really reactive when those threshold
levels were triggered, and it allowed people to
be better decision makers. Like one of the things that
everybody kept telling me was, oh, we're all engineers. You know, we want to have
engineering judgment. And my answer to them was always, but I'm giving you more time to do that. So let the data guide you and free you up and you won't be trapped
looking at Excel charts all day. And that was probably great feedback. So this is what it looks like. Again, sorry, it's white. For now. And it'll be black tomorrow. But this is just a dashboard from one of our operators, and his area has, I think it's five different ones there, but straight away, it's all green. And green is gold. Green is good. Green is don't worry about it. But you can see the
number four at the bottom, not really jumping out at you, but it's there. And the red warnings, and
then there's one amber. And that's what I wanted to hit on. I want 'em to trigger
onto that message going, where's that for, and what do I do about it? So let's go to the next slide.
- Yeah. But this, and this, so this is a very basic presentation, very basic stack. We've got, again, one
graduate working on this. We haven't really done much
with the alerting components. We are using Windows to make sure that the end users are not getting spammed with SMSes, which is also very important. We've got a long roadmap to go, 'cause we're getting now, of course, buy-in and more resources. But we are able to start super simple, and get real value out to the people out and around the world. What's happened to that one? - I hit it again. So here are two different pages, planes that we have. So GIS, that's another in engineering, we love our GIS we love our coordinates, and we love to know where we are. As engineers, we always go to the map. We just go to a map, a chart, whatever you wanna call it. So we've got three red alerts here, and straight away I can tell that there's actually four on the map. So they're scattered around Ireland. Now, there are four
different individual areas. So there might have been some
work happening that night. The manager comes in the morning, he gets a handover, and he goes, well, why, why have I got red dots on my dashboard? And straight away, he's able to call his local representative in that area and go, we were out there last night and the door wouldn't close on whatever unit it was, and it was giving us an error feed. All those triggers were
coming back into Grafana. - Yep.
- And we were able to and go and report on it. Obviously, the reds will have
to be fixed straight away, and there's a time limit on them. And the amber is also handy because some things
are out of our control. Like it might be, it might be batteries getting low. You know you've got 20, you know, I dunno, 20 hours to get out there to repair the battery before it goes red. And that's really handy. It's almost better the amber stuff than the red stuff because I don't want anything going red. But when it goes amber, I
can go and solve the problem before it gets a problem. - Yep. And that's the snowball
that we're getting on. So first challenge we get is the GIS, can we work with GIS and it does, again, we're not buying a super expensive system. Second thing, can we bring in asset data? So everything's driven by
numbers and driven by SAP. And what can we pull in asset data and display it so it's relevant to people, and we can, again, for a very low cost, starting with open source system, which is a game changer for them. And as soon as you see this, and as soon as we get the
engagement with the users, it's like, okay, we can give 'em the status hot or cold, or what the temperature is. But we can, as you said,
we can also start saying, well what's the battery like? When has it being patched? What's the firmware? And it opens up all those
conversations in a nice way. We're not just traditional procurement, we're not generating a
massive bunch of requirements to hit people with a stick and giving no solution. With the stack, with Grafana, we're giving them a solution saying, we can gather the data,
we can display the data, and now we can start
enhancing it and enriching it without starting another massive project that builds another separate system that silos all the data into somewhere else. - Yeah. Like, the real time
aspect of it is perfect. Like, this one happens
in Ireland all the time. Rain. Flooding And you'd be surprised
at how they elevate. So you could like, wake up in the morning, and it's lashing rain. What you don't know it's been lashing the previous two days, and that's building up saturation level, and all of a sudden, if it gets higher than the rail, the top of the rail, I've got to go and put a mitigation in place for that. Before, that involves somebody going out, or be retrospectively
informed by the train drivers. Hey, you've got flooding
on both sides of the track. Now, we can go and use remote monitoring, put out temporary devices anywhere we want in a matter of hours, and have instant feedback on
it coming back to the office. Like, talking about saving time. This is saving travel time
for for the operators, getting out in the vans,
walking down the tracks, setting up a secure method to get to site, 'cause we're work in red zone. Like, the railways a no-go area. If you wanna get out there, like, I won't tell you how much paperwork you have to do just to get out there, but it's near to impossible. So having something remote
takes the boots off the ground and our safety department
will love us first. - It's 'cause taking possession of a track or going out onto a track
can be a dangerous thing. Depending where it is, there could be high speed
trains running around. So it's a non-trivial
activity to send somebody out to a location to do an inspection. So again, all of this
helps that in a very nice, elegant, clean way. - On the right hand side of the screen is a screenshot of my phone with the very first alert. Since then, I've discovered that I'm bombing everybody with alerts, and like anybody, once you
start sending them too much, they're like, oh, it's
another alert from Seosaimh. Another alert, another alert. I quickly found out to
grab their attention, and this is to the developers in the room, that I've got three requests
from the alert system. The first alert is the initial result. Flashing in red. Then there's repeat alerts
every hour or every two hours, or whenever I want to, maybe in orange. And then the best alert is
when the problem is solved, and that goes in, I dunno, a line. I won't use green again.
- Yeah. - But are you with me? It's all, just wanna flash on their phone, have a look at it, and
see something quickly. They don't wanna go
looking at the dashboards. The dashboards are great for my meetings, but the lads who are under pressure tell me the information, I wanna go and react straight away. That's their job. They're like firefighters. And without them, our trains wouldn't move. The level above them,
again, in senior management, they love dashboards. They can instantly say, huh? So you gonna work on that? This is this is what happens, you know, after the shift. We gotta stop that. You know, so dashboards are for everybody. Dashboards are for the maintenance guy who's in the van who's
got his mobile phone. It's for his manager who can go and push notifications towards him. It's for us in the back office to be able to use the information
and push notifications. - Yeah.
- To create work orders. And then, something happened last week, and I got a phone call
from one of our engineers and he asked me, "Seosaimh, could you
tell me the temperature of the track on the 15th
of August last year?" And I'm like, eh, unusual request, but yeah, give me two seconds. And I went back into the history, and there was another event that day, and he just wanted to know, did the spike in temperature cause it? Before, I would've had to go back to the vendor, asked him for a check. - Give him an envelope.
- Probably would've asked for money. But yeah, I would've asked him for the the trace, because
I wouldn't have had it. Having the history on our own
server allowed me to go back, and in Grafana, and with the time map, I think I had it in like, I
dunno, less than 30 seconds. - Yeah. - And it was great.
- So that's another part of it. Again, we don't sort of pitch it but you start to get
sovereignty of your own data, which is very good for
these organizations. We're starting to, from
the super simple stack, which is a great way
to get going, you know, from the sensors, we've
moving towards MQTT. So MQTT allows us to start setting a standard
across the whole organization, an ontology of all the data, if you will, that actually maps back to SAP, which they absolutely love. That's a big game changer, that we have this
correlation of all the data. We're using Timescale for now, because it's, you know,
super simple and robust, and is working really well for us. And then we're, you know, diving now deeper into Grafana for the alerting the anomalies. The AI we're very excited about because it provides real
operational insight, not just some noise. And the thing we're just tiptoeing into is what we'll talk about is, we don't have time, is sensor fusion. So when there is rain, and we can see the weather forecast, and we know the status of the tracks, suddenly that becomes a much richer picture for people who are now making decisions about what's really gonna happen. So where do we go? We went from one sensor on a laptop, some demos, then to small operators that would actually talk to us that we were working with
that would give us access to some data to basically now built into the procurement contracts that we're going forward
with with everybody that they must share the data. We prefer to have an MQTT, but we'll work with almost anything. It's rolled out across regions and hubs across the whole country. It's a simple, robust architecture that scales well with us, especially within MQTT. And we basically have national coverage in a fraction of the time, at fraction of the cost with very happy customers,
which is probably- - Yeah, really happy.
- Most important thing with it. We're then working on
more integrations now to the service management systems, to the asset management systems. Nearly everything has a service life and a history built into it. We can start working with that data, pulling it from a different direction to give people insights of when they should do their maintenance and their preventative
maintenance going on. And for the actual passengers and the customers we're working with, we feel that we're
making a real difference in that they should not see the problems. We should know about
the problems long before any interruptions of service for customers or threat warnings, and our time to notification, our a time to fix, our
a time to be aware of it has gone from potentially
literally hours and days. Some random person ringing up,
a driver calling in saying, hey, the track is getting flooded, or there's a disruption, to devices going off, real time sensors. - Yeah, time. Time is definitely the biggest factor of what the outcome was. Like, I can't emphasize it enough, from getting that phone call to knowing that phone call never has to happen is magic for us. You know? You get on the train in the morning, and you sit down, and you don't know there's
a fault, like, I dunno, 50 miles up the road. By the time you get there,
I've already known the fault, there's an engineer gone out, solved it, and the train keeps going at line speed. But that train might have been slowed down to travel at a safer, reduced speed. Or it might just be a technical glitch that can be resolved remotely. But if you don't know
about it, you can't fix it. - So that makes us go
obviously from very reactive to ours now getting into almost predictive where we can solve things
before they actually happen, or nobody's really aware of it. And so for us now, Grafana as a core has become much more than
just a dashboard of data that sits on a wall somewhere. It is really an operational
hub for information that takes a very old company to a real time data-driven company without having to have
massive consultants, and a whole transformation,
cultural change. It's that ease of use
of work with Grafana. It's a flexibility to deal with feedback that has made it like,
kind of so special to us. Not to mention it's open source, which we all love here. It's not taken us down strange roots with strange companies
with strange technologies. It's being able to scale
with us to now hundreds and thousands of sensors in the roadmap with no problem. We're running it on Azure for now. It's been super simple
to run, it's been robust. We've had zero issues with it, which is, again, been a kind
of a revelation for them. Our roadmap, you can kind of guess, it's gonna be AI in there, it's gonna be anomaly detection, it's gonna be insights. We have a backlog of many, many thousands of different types of sensors that people are interested
in and fusing them. So what we get an alert, a camera can look at that device, and see is somebody
tampering it with a it, has anything changed? Is there a truck hanging
off a bridge somewhere 'cause somebody's driven into it? That gets us to a much better place, quicker, faster, better, and easier for the people working with it. They're not out in the
field in all weathers trying to find out what the hell happened in a location. So the kind of takeaways from all of this, with this stack being so
flexible, you can start simple. You can start doing showcases, you can start from your laptops. You can be sort of super iterative with your potential customers, clients. and people out there to
workshop it in real time. And we drag and drop dashboards
in real time with them, which is a game changer for them. It allows you to scale
into various technologies that will give you an
architecture that will scale out to the real world and take sense of devices from anywhere we've seen,
- But once we build it, we can just duplicate it. That's the biggest learning I have. Duplication, that loop that goes around, the more sensors I get. Like, I'm telling Richard, we're gonna run out of space, and he's like, ah, don't worry about it. There's plenty of space out there. - Yes. - But yeah, look, it's been great. I can't applaud the guy beside me enough for introducing me to Grafana
at the very first day. And we hope to- - Keep on going, 'because it becomes our sovereign platform for our data, which we
can do what we need to and get that insight, and then we're very interested in the Grafana insights as well. - Yeah.
- How do we start getting more insights out of the data we're collecting? And we go from alerts to much more information
across the system. - [Seosaimh] And the business
intelligence part of it. - Yeah. So cool.
- Okay, thanks very much. (audience clapping)

