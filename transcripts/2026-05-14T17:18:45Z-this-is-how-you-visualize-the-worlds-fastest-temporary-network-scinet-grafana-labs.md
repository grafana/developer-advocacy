# This is How You Visualize the World&#39;s Fastest Temporary Network | SCinet | Grafana Labs

Published on 2026-05-14T17:18:45Z

## Description

Andy and Katrina from ESnet volunteer every year to build SCinet — the research network powering the SuperComputing ...

URL: https://www.youtube.com/watch?v=Y8zvrba5uRI

## Summary

The show titled "This is How You Visualize the World's Fastest Temporary Network | SCinet | Grafana Labs" was published on May 14, 2026. The speakers, Andy and Katrina from ESnet, discussed their volunteer work in building SCinet, a high-speed temporary network for the SuperComputing conference. They highlighted the network's impressive bandwidth of 13.72 terabits per second, the collaborative efforts of over 200 volunteers, and the use of Grafana for visualizing network data. Key takeaways included the importance of effective storytelling in network engineering, the challenges faced in data visualization during the conference, and plans for future improvements in their monitoring and visualization efforts. 

Topics: SCinet, Grafana, network visualization, collaboration, observability.

## Chapters

00:00:00 Overview of SCinet and its significance
00:06:07 Overview of SCinet and its networking challenges
00:12:18 Introduction to MetrANOVA and its purpose
00:17:39 Building dashboards for SCinet at SuperComputing

# This is How You Visualize the World's Fastest Temporary Network | SCinet | Grafana Labs

**Published:** 2026-05-14

---

Hello. Thank you. Yeah. So in case you're confused, I'm Andy, and this is Katrina. I also go by Andrew. We are both from an organization called ESnet, which connects the US National Labs together. A short way I explain it to my mom is that we're the internet service provider for science. However, that's a very permanent network. Luckily for our job security, what we're actually going to talk to you about today is something that Katrina and I volunteer for every year, which we like to call the world's fastest temporary network.

So what exactly do we mean by that? Every year, there's a conference called Super Computing. I might get crickets on this one, but has anybody heard of the Super Computing conference or been to it before? All right, I see a few in the crowd. It's a pretty big conference, with over 15,000 people attending last year. These days, especially with all the AI stuff going on and quantum advancements, it's a pretty cool place to be. The idea is that industry and academia come together to showcase the latest and greatest in high-performance computing, networking, and storage. It's set up kind of like a big trade show, with a giant exhibition hall—if the exhibition hall was like a football stadium in the attached conference center, which it was last year in St. Louis.

To support all that, you need a pretty good network, right? Just like here at GrafanaCON, you guys are probably on the conference network right now. If I drone on too long and get boring, you'll probably be paying more attention to that than to me. SCinet is no different, but there are actually two parts to that network. One is your traditional kind of wireless network for the attendees and booths. The more interesting aspect, and the one we're going to focus on today, is the second piece, which is a research network where people do all these really cool demos.

So what do we mean by that in terms of scale? The speed of this network last year was 13.72 terabits per second. It gets bigger every year, and it doesn't happen until November, so I don't know what the final number will be for this year, but it'll be greater than this. For context, the average connection speed for a home internet connection in the US is 300 megabits per second, which means SCinet is about 45,000 times faster than that. 

What’s cool about it is not just the speed, but how it all comes together. Over 200 volunteers make all of this happen. These volunteers come from different networking specialties, including systems folks, and they come from a bunch of different institutions all around the globe to put this all together. All the hardware is donated, totaling over $70 million, which is a pretty good amount. We have to fit it all on 31 pallets a year, which fills up like two big trucks that take it to the conference center. There’s a lot of fiber that needs to get laid and many things that need to come together.

Our mantra for all of this, which was already kind of alluded to, is: it takes one year to design, one month to build, one week to operate, and one day to tear down. There’s a lot of planning involved to acquire all the loaner equipment, figure out all the volunteers, and get everybody on the same page. About a month before the conference, we actually show up to the site and start building everything. 

Now, what's fun about this is that these are big conference centers, and they have other things going on in the preceding weeks until the conference. We can't just build the network in the middle of where we want to showcase it, so there's usually a staging area set up for us. We build everything there, take the $70 million of equipment, and then a few days before the conference, we get a forklift and nervously watch as they move all of this equipment into its final place. 

Once that's in place, the conference starts. In some ways, that's usually common because everybody's running around trying to get everything working before the conference starts. But once it settles in, usually most of the stuff works. You might have a few fires to put out here and there, but you're in a pretty good spot. After putting all this work in over the year, on the last day, you just kind of rip it apart, and you're all done. The one solace is that if you're going to participate the next year, you're right back into it with the planning.

This has been going on for 35 years. The first one was in 1991, and these days, we're a little bit faster. We're now 56,000 times faster than we were in 1991. I've been doing this for a while.

So, I talked about all of this stuff that comes together and all these people volunteering their time, but why do they do all of this? To describe that, I need to zoom out a bit and talk about what the day-to-day life for Katrina and me is like. If you're not familiar with big scientific research, there's a pretty similar setup. There are a lot of different disciplines, but many big scientific instruments are all around the world.

One picture shows the Vera C. Rubin Observatory in Chile, which takes highly detailed images of the night sky and produces terabytes of information with each image that scientists want to access. On the other side is the Large Hadron Collider (LHC), which is on the border of CERN in Switzerland. That's a big particle accelerator that smashes atoms together, generating petabytes of information that needs to be shipped all around the world. Scientists who want to access this data and actually use it to make discoveries aren't where the instruments are. Furthermore, to analyze the data and sort out the interesting stuff, they usually need to ship those datasets over to supercomputers, which are yet a third location.

To make all this happen, you need really good networking. One such network is ESnet, which connects the US National Labs funded by the US Department of Energy. You can see where we have routers and equipment on this map. This is our first Grafana panel we're showing, and networking folks love maps. Our running joke is that if you have any type of demo or anything, you're basically guaranteed to have a map in the networking world. This is actually a plugin that Katrina wrote, one of many, and you'll see some more that you can get from the official Grafana plugin list. If you search for it in the plugin panel or on the website, it's there. You can build all sorts of maps.

**Map, a geographic map**—keep that in mind because you'll see this again later, but it'll look very different when we're talking about the conference itself.

Okay, so there's a network like ESnet, right? We serve science, and we've got to serve these use cases that generate tons of data. Well, we're not the only ones, right? When a packet or data is traveling around the world, it's going to hit a lot of these different networks as it goes. For example, we're in Barcelona today. I mentioned the LHC; there's a tier one site called PIC, which means they host a lot of the data. If you want to send some of that data over to the US, you're basically going to hit PIC's network. 

There's a Spanish network that serves the Spain research and education community called RedIRIS. It'll hit that. Then there's a European national backbone called GEANT, and it will hit that as well. After that, it will go on an undersea cable over to the US and hop onto ESnet, and then off to wherever it's going to go. 

So that's a long way of saying that there are a lot of things that can go wrong from end to end as that data travels from one place to another. We have a good picture here. I mentioned the undersea cable; those are actually pretty important pieces of global transfers like this. We saw that a shark thought it looked pretty tasty, but he actually didn't get through it, and it didn't cause any problems. Much more likely in that case, you have to worry about anchors getting dragged on things, intentionally or unintentionally. 

If you want to fund an online dumpster dive tonight, the geopolitics of undersea cables is actually kind of an interesting topic. But there are also some of the more usual problems, like hitting a bunch of different organizations as you go. There are different hardware platforms, different policies, and different firewalls. For ESnet, we kind of sit in the middle, so we can see stuff on our network, but we can't necessarily see stuff on other people's networks. All our customers know is their data's not getting there as fast as they want or things like that.

So that's all kind of leading into the networking world, where collaboration is super important. We have to have good relationships with these other networks. What we're normally working on too are open-source projects to share data between networks. For example, perfSONAR is one, and MetrANOVA is another that we'll kind of drop. Grafana fits into there really well because of its open-source nature. We actually use that for all the visualization of this data. 

Again, I'm showing another panel that Katrina created. That's one of the official ones that basically is a grid structure. A lot of what we deal with is source and destination performance. So you've got rows as the source and columns as the destination, allowing you to get a quick summary of how things look.

Now, let's bring this all back to SCinet, the conference. Why do people go to this conference? I've talked about the worldview of things. Well, it's a really great chance for all these people to come together. As I mentioned, collaboration is really important. That's why people are sending their folks here, and our folks are helping build that. It's a great chance to get hands-on networking, learn from others, and try new things, which is kind of what we were doing in the network measurement space. 

There are all these cool demos that happen once you've built this network. If any of you have huge data that you want to send around, you can apply for one of these. There are things like AI-driven networks, new data transfer services, and all this programmable hardware that people are trying. They actually use almost all of that bandwidth I mentioned. There's this data tsunami on the last day, where they basically fill that pipe, which is really hard to generate that much data on the compute side. So it's pretty cool to see all that.

Now, I'll hand it over to Katrina to talk a little bit more about how that actually goes.

---

**Katrina:** Right, so this sounds like a super cool project, right? But why have none of you ever heard of this before? Why don't more people know about this? The answer's pretty straightforward: we need better storytelling. Network engineers are super smart, but they're not really concerned with whether people know what they're doing or not. They just want to make sure their network works, right? 

So they called me and Andy, and they were like, "Yo, we need some vis." And we're like, "All right, cool, here you go." No, but really, I wish it were that simple. So how did we go from this diagram to this super cool vis down here, which is actually the same panel, the same type of panel plugin as the network map that Andy was showing earlier? 

We didn't come empty-handed. This is our day job, like we said, so we had a bunch of stuff to rely on. We had this MetrANOVA Pipeline that we wanted to test out. We had this thing called Terranova. We had some super sick Grafana skills, which were really helpful. That all lent itself to what we actually had to do when we got there. 

Imagine with us: we get there on day one, and we're like, "All right, let's go." Then on day seven is actually the opening of the conference, so that's showtime. I know you're thinking, "You had a year to design this." We sure did. We started on day one. It was really fun.

So you're probably wondering at this point, what is MetrANOVA? You've said this like five times. MetrANOVA is a consortium. It's the name of the consortium as well as the product, but it's basically dedicated to network monitoring and observability. We work at ESnet, doing all of this observability. There are a bunch of other R&E networks that also do observability, and then there are a bunch of smaller networks that would like to do observability but maybe don't have the same resources that we do. We think everyone should have great observability on their networks. 

The consortium is dedicated to coming up with a nice open-source stack that anyone can deploy on their networks and get a good view of what's going on. It's pretty new. Andy just wrote a brand spanking new pipeline for it, and we wanted a place to test it. So why not a 13.72 gigabit per second temporary network? Sounds great. But that's still a lot of work to do in a week, right? That's why there are two of us. 

Luckily, Andy is really cool and can do all the backend stuff. He was in charge of getting all of the data, getting it through the pipeline, gathering up the metadata, and getting that into the pipeline—kind of worrying about that stuff. I was like, "I'll go make some pretty pictures; see you in a few days." So we kind of split the work streams up like that. 

It sounds pretty straightforward. Again, we do this in our day-to-day lives. We're like, "All right, let's go." But it's SCinet, and with SCinet come struggles, as always. The first few days, like we said, it's our first time on the project. We were like, "All right, who do we get the data from? Who can turn this on for us? What do we do?" Andy was running around trying to figure out who to talk to. 

We had metadata coming in from a couple of different sources because they switched out their inventory system this year. So that was fun. We had to figure that out and determine what was even available, all of that stuff. On my side, I was also figuring out what metadata we had and how to turn that into an...

**Interesting story?** That's what they brought us in for, right? To get people excited about SCinet and to tell this story. So how can we do this? And one step further, how can we do this on these essentially just TV displays that will be cycling through in kiosk mode around the conference center? So, not your normal dashboard case, right? 

I'll say Andy worked super hard, but since this is a GrafanaCON conference, I'm going to just talk about the Grafana stuff on the front side. What we landed on for our solution to kiosk mode was that we would do the standard one question per dashboard. This was really helpful for a couple of reasons. One, again, we were trying to draw people in and get them interested. Hopefully, these questions would perk their interest and bring them over to look at it. 

We put it nice and big at the top of each dashboard and themed each of those dashboards around it. Instead of one large dashboard with a couple of tabs that you can click through, we chunked it into these very small kiosk-mode pieces. We had a question at the top to draw the person in and also to give them some context around what the dashboard is—like, what am I even looking at, right? Because again, they're not used to looking at this type of stuff. 

We started with some basics, you know, standard stuff. How much traffic is there moving across the network? So we used the time series graph. Who's using the most bandwidth? We used this bump chart. The little QR codes are for the plugins because some of them are custom that we've written or other people have written. What are the usage patterns? Like, when is SCinet the busiest? That was a fun hourly heat map plugin that I was like, "Guys, just wait, the last day it's going to look super cool," and then it did. 

We were working through all of these and had a good set of dashboards we were pretty happy with. But I was like, we need something else. We need some eye candy. You know what people like? Maps. So I was like, "All right, how are we going to get a map?" Then we came across the conference website and were like, "Okay, well, there's this map of the showroom floor, so we should be able to grab those coordinates." 

We'll plug it into Terranova, which is one of our projects that basically just outputs a map topology that you plug straight into our network map plugin in Grafana, and you just get a map in Grafana. It's super great, really easy to use, and then you can attach your data to it. We thought, "Yeah, this would be really cool. We can show where the network traffic is going on the showroom floor." 

All right, cool, where are the coordinates? There were no coordinates. So we thought it was a really good idea, and I didn't want to give it up. I'm pretty stubborn. So we just threw a grid on top of the screenshot, and then I hand-typed in hundreds of coordinates for each of the booths across the showroom floor because what else am I going to do? I'm stuck there waiting for data. 

But I did get pretty tired of it and called in some reinforcements. Shout out to my intern Ethan. He is literally down for anything, really great. He had a few hours before his class started, so we sat there and plugged in a bunch of coordinates. When we were done, we put it through Terranova. It was great; we had a map. 

There was still no data going into that map, and about now we are on day four. So if you're keeping track, day seven is when the conference opens. On days four and five, we had a bit more struggles. Andy had found the people that we needed to talk to, which was great, but they were a little busy. There were some fires they were putting out, getting the network up—important things like that. They weren't super concerned with monitoring because, again, they were more focused on getting the network up for the conference, which you can't blame them. 

So we were just trying to figure stuff out with them, see if there was anything we could do. Usually, it's pretty straightforward to turn monitoring on your routers, but for some reason, it wasn't this time because SCinet. We were just working through that and getting it all figured out. At this point, I had pretty much all of the dashboards built. Luckily, we had some test data that we could use, so we were pretty confident it would all work—99% confident. 

We had put it in public dashboard mode, which worked great, by the way. We had it displaying on the TVs around the conference. We were pretty confident that stuff would work if we could just get some data. Finally, on day six, things happened. Stuff worked out. Andy got the data connected. He said, "It's in, it's going into ClickHouse." 

And literally, I kid you not, it was like a movie. He was like, (imitates drumming) "Enter, it's in ClickHouse." I was like, "Cool, let me hit refresh," and then ta-da! We had lights light up, and we were super stoked. We were sitting in the corner like, "Yeah, super excited. Good job." Everyone was still running around putting out fires, like, "What are they doing? Nerds, why?" 

So we spent the next few hours—well, I say a few hours; it was probably less, probably like one hour—just making sure, double-checking all the rest of our dashboards. They did indeed work. Miracles! Then we thought, "Well, we've got a couple more hours; what else can we do?" So we made another dashboard with another map because we like maps. 

This one you probably recognized from earlier, but this time it was specific to SCinet data that was coming over ESnet. We thought that would be cool and would make our bosses happy, so we threw that one in there too. Then we got to day seven, and it was showtime. 

As Andy said, we kind of just were like, "Woo-hoo, it's done! Let's just walk around, see if it's working." We got to show our bosses; they were pretty happy. They got to show their bosses, which was pretty cool. We took a bunch of pictures, walked around, and saw what was up. Just to put it out there, the light mode one with the pie chart—that's not ours. So, no responsibility for that one. But the nice purple and blue ones, those were what came out of what you did. 

It was really cool. We caught some people talking about our stuff, pointing, having conversations about it, which was really the point, right? If we go back to the beginning, we wanted to tell a story. We wanted to get people engaged and have them talking about this network that all these people put all of this time and effort into. 

Was everything perfect? No. Is there a lot of stuff we want to do next year? Yeah, for sure. But did we have more engagement than before? I think so. So we call that a success. Of course, we are looking forward to this year already. As Andy said, basically as soon as you're done, you're planning for the next year. 

We've got big plans; we want to grab some more metadata, tag the flows with some more stuff, maybe hone in on specific use cases. We've got all these plans for cool dashboards, maybe do some stuff for the network engineers in the back—all of this fun stuff. We'll see how much we get to. (chuckling) 

We had some plugin improvements we wanted to do. Like we said, a lot of the plugins that we use, we developed in-house. So if we want new features, we have to then do them. I've started on that, so that's coming along. And then maybe start sooner than a week before—that's kind of our main goal this year. 

We did attend our first meeting last night? Two? Last night. So, yeah, we're getting there. Thanks for listening to our talk. Feel free to put questions in there, and if you wanted more of those QR codes, we threw them up here for you.

(applauding)

## Raw YouTube Transcript

- Hello. Thank you. Yeah. So in case you're confused, I'm Andy, and this is Katrina. So, and I also go by Andrew. So, yeah, as he already told you. So we're both from an
organization called ESnet. So that's what we do
for our day jobs, right? So that's basically, I'm guessing a lot of you
haven't heard of that. So that's a network that connects the US
National Labs together. We kind of, a short way I,
when I explain it to my mom is like we're the internet
service provider for science. But that's a very permanent network. Luckily for our job security, what we're actually gonna
talk to you about today is something that Katrina and
I volunteer for every year, which we like to call the world's
fastest temporary network. So what exactly do we mean that by that? So every year there's a
conference called Super Computing. I might get crickets on this one, but has anybody heard of the
Super Computing conference or been to it before? All right, I see a few in the crowd. It's a pretty big conference. There's over 15,000 people
that attended last year. These days especially, it's
a pretty cool place to be with all the AI stuff going on and quantum and things like that. So basically the idea is industry and academia kind of come together to kind of showcase
the latest and greatest in high performance computing and network and networking and storage. It's set up kinda like a big trade show. So a giant exhibition hall, if the exhibition hall was
like a football stadium in the attached conference center, which it was last year,
(chuckling) in St. Louis. And so to support all that stuff, you need a pretty good network, right? So just like here at GrafanaCON, you guys are probably on the
conference network right now. If I drone on too long and get boring, you'll probably be paying more
attention to that than to me. And so SCiNet's no different, but there's actually two
parts to that network. One is your traditional
kind of wireless network for the attendees and the
booths and things like that. But the more interesting aspect, and the one we're gonna
be focusing on today is kind of the second piece,
which is a research network where people do all
these really cool demos and things like that. So what exactly do we mean
by that in terms of scale? So it was already mentioned, so the speed of this network last year, it gets bigger every year. So it doesn't happen until November. I don't know what the final
number will be for November, but it'll be greater than this, right? So 13.72 terabits per second
was the total bandwidth. Probably most of you
are, you know, technical, so have an idea that that's pretty big. But I looked it up in the US,
the average connection speed for like a home internet connection is 300 megabits per second. So this is like 45,000
times faster than that. And you're also already told how fast you can get Grafana on that. So it's pretty fast. What else is cool about,
it's not just like the speed, but how it all comes together. So over 200 volunteers. So all volunteers kind of make
all of this happen, right? And so you have people from
different networking specialties and there's like systems folks and things like that that, that they get from a bunch
of different institutions all around the globe to
put this all together. And then all the hardware is all donated. So it's over $70 million in hardware, which is pretty good amount. We have to fit it all
on 31 pallets a year, which fills up like two big trucks that they take to the conference center. And there's a bunch of
fiber that needs to get laid and all of that. So a lot of things that
need to come together. So kind of our mantra for all of this, which was already kind of alluded to, was it takes one year to design, one month to build, one week to operate, and one day to tear down. So basically there's a bunch of planning to acquire all the, you know,
all the loaner equipment, you know, figure out all the volunteers, get everybody kind of on the same page. And then about a month
before the conference is when we actually show up to the site and start building all of this. Now what's fun about this is, you know, these are big conference centers. They have other things going
on in the preceding weeks until the conference, right? So we can't just like build the network in the middle of where
we wanna showcase it. So there's usually a staging
area that they set up for us. We build all that, we take
the $70 million of equipment and then, a few days
before the conference, we get a forklift and all very nervously watch as they move all of this
equipment into its final place. So then once that's in place, you know, eventually the conference starts. In some ways that's usually common 'cause everybody's like running around trying to get everything working before the conference starts. But once it kind of settles in, usually most of the stuff works. So you maybe have a few fires
to put out here and there, but you're in a pretty good spot. And then you've put all
this work in over the year and it kind of, as life goes
sometimes, on the last day, it's just you kind of rip it
apart and you're all done. So I guess the one solace is though, if you're gonna participate the next year, basically you're right back
into it with the planning. So this has been going on for 35 years. So the first one was in 1991, you can see the diagram
there, that's a little fuzzy. And these days, you know, we're a little bit faster
as these things go. So 56,000 times faster
than they were in 1991. So, I've been doing this for a while. So, okay, I talked about all of this stuff that comes together, all these people volunteering their time, but like why do they do all of this? And so to kind of describe that, I need to zoom out just a little bit and talk about kind of a little bit more what's like the day-to-day
life for Katrina and I. So basically, if you're not familiar with kind of big scientific research, there's a pretty similar setup. You know, there's a lot
of different disciplines, but there's a lot of these
like big scientific instruments all around the world, right? So I've got a couple pictures up there. One's the Vera C. Rubin
Repository in Chile. It takes like these highly
detailed images of the night sky and produces like
terabytes of information, like each image that scientists
want to get access to. On the other side is the
Large Hadron Collider or the LHC, which is on the
border of CERN and Switzerland. So that's a big particle accelerator. They're smashing atoms together, have these sensors that detect them and generate like
petabytes of information. And again, needs to be
shipped all around the world. So the scientists that
wanna access this data and are actually use this
data to make discoveries aren't where the instruments are. And furthermore, to actually
like analyze the data and sort out the interesting stuff, they usually need to ship those datasets over to supercomputers, which then are yet a third location. So I've got a middle one
there, that's in California, got actually a floor
before below the home base of our organization. And, and so basically
to make all this happen, you need really good networking is kind of the the point, right? And so one such network is ESnet, who Katrina and I work for. And as I mentioned, we
connect the US National Labs funded by the US Department of Energy. And so you can kind of see
where we have like routers and equipment on this map, which I'll say, this is our first Grafana
panel we're showing, and networking folks love maps. Pretty much our running joke is if you have any type
of demo or anything, you basically guaranteed you're gonna have a map
in networking world. And so this is actually a
plugin that Katrina wrote, one of many, and you'll see some more that you can get from the official Grafana
kind of plugin list. Like if you search for
it in the plugin panel or search on the website, it's there. You can build all sorts of maps. So this one is obviously
a kind of a world map, a geographic map, you
know, keep that in mind 'cause you'll see this again later, but it'll look very different when we're talking about
the conference itself. Okay, so there's a
network like ESnet, right? We serve science, we've
gotta serve these use cases that generate tons of data. Well, we're not the only ones, right? And so like when a packet essentially, or data is traveling around the world, it's gonna hit a lot of
these different networks as it goes, right? So like we're in Barcelona
today, I mentioned the LHC, there's a tier one site called PIC, which means they host a lot of the data. If a, you know, if you
wanna send some of that data over to the US, you're basically gonna hit PIC's network. There's a Spanish network that serves kind of the Spain research and education community called RedIRIS. It'll hit that. There's a European national
backbone called GEANT, it'll then hit that. It'll go on an undersea
cable over to the US and hop onto ESnet and then, you know, off to wherever it's gonna go, right? So that's a long way of saying that there's a lot of
things that can go wrong from end to end as that data travels from one place to another, right? So we've got a good picture here, right? I mentioned the undersea cable, those are actually pretty important pieces of kind of global transfers like this. We saw that that shark there
thought it looked pretty tasty. He actually didn't get through it. It didn't cause cause any problems. Much more likely in that case, you have to worry about anchors
getting dragged on things, intentionally or unintentionally. If you wanna fund like
online dumpster dive tonight, the geopolitics of undersea cables is actually kind of an interesting one. But there's also, you know, maybe some of more of the usual problems of you're basically hitting a bunch of different organizations
as you go, right? So there's different hardware platforms, different policies, different firewalls. And like, you know, for ESnet, we kind of sit in the middle, so we can see stuff on our network, but we can't necessarily see stuff on other people's networks. And all our customers know is
their data's not getting there as fast as they want or
things like that, right? So that's all kind of leading into like, in the networking world, like collaboration is super important. Like we have to have good relationships with these other networks. And what we're normally working on too is like open source projects to like share data between networks. So like perfSONAR is one, MetrANOVA is another
that we'll kind of drop. And so Grafana fits into there really well because it's open source nature. We actually use that for all
the visualization of this data. And again, I'm showing another
panel that Katrina created. That's one of the official ones that basically is a grid structure. So a lot of what we
deal with is, you know, source destination, how
are things performing? So you've got rows that's a
source, columns the destination, and you can get a quick summary
of how things look right? All right, so let's bring this all back to SCinet, the conference, right? So why do people go to
this conference, right? So I've kind of talked about
the worldview of things. Well it's a really great chance for all these people to
come together, right? And as I mentioned, collaboration
is really important. So like that's why people
are sending their folks here, our folks to kind of help build that, is it's a great chance to
get hands on networking, learn from others, try new things, which is kind of what we were doing in the network measurement space. And so it's really appealing
for all of those reasons. And so there's all these, once
you've built this network, there's all these cool demos that happen. I guess if any of you have any like, you know, huge data that
you wanna send around, you can apply for one of these. But there's stuff like, you
know, AI-driven networks. There's like new data transfer services, all this like programmable hardware that people are trying
and stuff like that. And they actually use
almost all of that bandwidth that I mentioned. Like there's this data
tsunami on the last day, where they basically fill that pipe, which is, it's actually really hard to generate that much
data on the compute side. So it's pretty cool to see all that. And so then I'll hand it over to Katrina to talk a little bit more
about how that actually goes. - Right, so this sounds like
a super cool project, right? But like why have never, none of you ever heard of this before? Why don't more people know about this? And the answer's pretty straightforward. We need better storytelling. Network engineers are super smart but they're not really
concerned with like, do people know what I'm doing or not? They just wanna make sure
their network works, right? So they called me and Andy, and they were like, yo, we need some vis. And we're like, all
right, cool, here you go. No, but really I wish it were that simple. So how did we go from this diagram to this super cool vis down here, which is actually the same panel, the same type of panel plugin as the network map that
Andy was showing earlier. So we didn't come empty handed. We had, you know, this is
our day job like we said. So we had a bunch of stuff to rely on. We had this MetrANOVA Pipeline that we wanted to kind of test out. We had this thing called Terranova. We had some super sick Grafana skills, which was really helpful. And that kind of all lent itself to what we actually had
to do when we got there. So I would like you to imagine with us, we get there on day one, we're
like, all right, let's go. And then on day seven is actually the opening of the conference. So that's showtime. And I know you're thinking, you had a year to design this. We sure did. We started on day one. It was really fun. So you're probably
wondering at this point, what is MetrANOVA? You've said this like five times. So MetrANOVA is a consortium. It's the name of the consortium
as well as the product. But it's basically dedicated
to network monitoring and observability. So like we said, we work at ESnet, we do all of this observability. There's a bunch of other R&E networks that also do observability and then there's a bunch
of smaller networks that would like to do observability but maybe don't have the
same resources that we do. But we think everyone should
have great observability on their networks. So the consortium is kind of dedicated to coming up with a nice open source stack that anyone can deploy on their networks and get a good view of what's going on. It's pretty new. Andy just wrote like a brand
spanking new pipeline for it. It's pretty great. And we wanted a place to test it. So why not a 13.72 gigabit
per second temporary network? Sounds great. But that's still like a lot of
work to do in a week, right? So that's why there's two of us. Luckily Andy is really cool and can do all the backend stuff. So he was like in charge
of getting all of the data, getting it through the pipeline,
gathering up the metadata, getting that into the pipeline, kind of worrying about that stuff. And I was like, I'll go
make some pretty pictures, see you in a few days. So we kind of split the
work streams up like that. So it sounds pretty straightforward. Again, we do this in our day-to-day lives. We're like, all right, let's go. But it's SCinet, and with SCinet
come struggles, as always. So the first few days, like we said, it's our first time on the project. So we were like, all right,
who do we get the data from? Who can turn this on
for us? What do we do? So Andy was running around trying to figure out who to talk to. We had metadata coming in from
a couple different sources 'cause they switched out their
inventory system this year. So that was fun. So we had to figure that out, figure out what was even
available, all of that stuff. And then on my side, you know, also figuring out what made
it metadata do we have, how do we turn that into
an interesting story? 'Cause that's what they
brought us in for, right? Is to get people excited about SCinet and to tell this story. So how can we do this,
and one step further, how can we do this on these
essentially just TV displays that will be cycling through in kiosk mode around the conference center? So not your normal dashboard case, right? And I'll say Andy worked super hard, but since this is a GrafanaCON conference, I'm gonna just talk
about the Grafana stuff on the front side. So kind of what we landed on for our solution to kiosk mode was that we would do the
standard one question per dashboard. And this was really helpful
for a couple of reasons. One, again, we were
trying to draw people in and get them interested. So hopefully these questions
would perk their interest, bring them over, get them looking at it. So we put it nice and big
at the top of each dashboard and we kind of themed each of
those dashboards around it. So instead of one like large dashboard with a couple of tabs that
you can kind of click through, we were chunking it into these very small sort
of like kiosk-mode pieces. So we had a question at the top, hopefully to draw the the person in, and then also to give them some context around what the dashboard is, like, what am I even looking at, right? 'Cause again, they're not used to looking at this type of stuff. So we started with some basics,
you know, standard stuff. How much traffic is there
moving across the network? So we used the time series graph. Who's using the most bandwidth? We used this bump chart. The little QR codes are for the plugins 'cause some of them are custom that we've written or
other people have written. What are the usage patterns? Like when is SCinet the busiest? That was a fun hourly heat map plugin that I was like, guys just wait, so the last day it's
gonna look super cool, and then it did. And we kind of were working
through all of these. We had a good set of dashboards
we were pretty happy with. But I was like, we need something else. We need some eye candy. You know what people like maps. So I was like, all right, well
how are we gonna get a map? And then we came across, you
know, the conference website and we're like, okay well there's this map of the showroom floor, so we should be able to
grab those coordinates, we'll plug it into Terranova,
which is one of our projects which basically just
outputs a map topology that you plug straight
into our network map plugin in Grafana and you just
like get a map in Grafana. It's super great, it's really easy to use, and then you can attach your data to it. And we're like, yeah,
this would be really cool. We can show where the
network traffic is going, you know, on the showroom floor. All right cool, where's the coordinates? There were no coordinates. So we thought it was a really good idea and I didn't wanna give it
up and I'm pretty stubborn. So we just threw a grid
on top of the screenshot and then I hand typed in
hundreds of coordinates for each of the booths
across the showroom floor, 'cause what else am I gonna do? I'm stuck there. We're waiting for data. But I did get pretty tired of it and I called in some reinforcements. Shout out to my intern Ethan. He is literally down for
anything, really great. So he had a few hours
before his class started. So we sat there and we plugged
in a bunch of coordinates. And then so when we were done
we put it through Terranova. It was great. We had a map. There was still no data
going into that map and about now we are on day four. So if you're keeping track, day seven is when the conference opens. So day four and five we
had a bit more struggles. Andy had found the people
that we needed to talk to, which was great, but they
were a little bit busy. There were some fires
they were putting out, getting the network up,
important things like that. They weren't super
concerned with monitoring because again, they were more concerned with getting the network
up for the conference, which you can't blame them. So we were kind of just trying to figure stuff out with them, see if there was stuff that we could do. Usually it's pretty straightforward to turn monitoring on on your routers, but for some reason it wasn't
this time, because SCinet. And so just kind of working through that and getting that all figured out. At this point I had pretty much
all of the dashboards built. Luckily we had some test
data that we could use. So we were pretty confident
it would all work. 99% confident. And we had, you know, we'd put
it in public dashboard mode, which worked great by the way. You know, we had it,
the pies displaying it on the TVs around the conference. We were pretty confident
that stuff would work if we could just get some data. So finally, on day six, things happened. Stuff worked out. Andy got the data connected. He's like, it's in, it's
going into ClickHouse. And literally I kid you
not, it was like a movie. He was like, (imitates drumming)
enter, it's in ClickHouse. And I was like cool, let me hit refresh, and then ta-da. And we did, we had lights light
up and we were super stoked. Okay, we're sitting in the
corner like, yeah, super excited. Like good job. And like everyone is still running around putting out fires, like what are they doing, nerds, why? All right, cool. So we spent the next, you
know, remaining of the day, I say a few hours, it was probably less, it was probably like one
hour, just making sure, double checking all the
rest of our dashboards. They did indeed work. Miracles. And then we're like, well, we've got like a couple more hours, like what else can we do? So we made another
dashboard with another map 'cause we like maps. So this one you probably
recognized from earlier, but this time it was
specific to SCinet data that was coming over ESnet. So we thought that'd be cool and it would like make our bosses happy. So we threw that one in there too. And then we got to day
seven and it was showtime. So like Andy said, we kind of just were
like woo-hoo, it's done. Let's just walk around,
see if it's working. So we got to show our bosses,
they were pretty happy. They got to show their
bosses, which was pretty cool. We took a bunch of pictures,
walked around, saw what was up. Just like to put it out there, the light mode one with the
pie chart, that's not ours. So like no responsibility for that one. But the nice purple and blue ones, those were what came out of what you did. So it was really cool. We caught some people talking
about our stuff, pointing, having conversations about it, which was really the point, right? If we go back to the beginning,
we wanted to tell a story. We wanted to get people engaged and have them talking about this network that all these people put all
of this time and effort into. And so was everything perfect? No. Is there a lot of stuff
we wanna do next year? Yeah, for sure. But did we have more engagement
than before? I think so. And so we call that a success. But of course we are looking
forward to this year already. Like Andy said, basically
as soon as you're done, you're planning for the next year. So we've got big plans, we
wanna grab some more metadata, tag the flows with some more stuff, maybe hone in on specific use cases. We've got all these plans
for cool dashboards, maybe do some stuff for the
network engineers in the back, all of this fun stuff. We'll see how much we get to. (chuckling) We had some plugin
improvements we wanted to do. Like we said, a lot of
the plugins that we use, we developed in-house. So if we want new features
we have to then do them. So I've started on that. So that's coming along. And then maybe start like
sooner than a week before. That's kind of our main goal this year. So we did attend our
first meeting last night? Two? Last night. So-
- Yeah. - We're we're getting there. And so thanks for listening to our talk. Feel free to put questions in there and if you wanted more of those QR codes, we threw them up here for you. (audience applauding)

