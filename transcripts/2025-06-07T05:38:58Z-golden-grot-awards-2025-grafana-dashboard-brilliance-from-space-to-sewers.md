# Golden Grot Awards 2025: Grafana Dashboard Brilliance from Space to Sewers

Published on 2025-06-07T05:38:58Z

## Description

Join us at GrafanaCON 2025 for the third annual Golden Grot Awards—Grafana's celebration of the most inspiring and innovative ...

URL: https://www.youtube.com/watch?v=CBct23Pf6r4

## Summary

In this video, the hosts celebrate the third annual Golden Grot Awards, recognizing outstanding dashboards created by community members. The event features winners Ruben Fernandez from Dell Technologies, who presented his innovative dashboard focused on tracking the International Space Station using Grafana, and Grant Chase, who showcased a municipal water filtration and restoration dashboard. Ruben's dashboard includes real-time tracking of the ISS and astronaut information, while Grant's project emphasizes the importance of SCADA systems in wastewater management. Both winners highlight the capabilities of Grafana for data visualization and its role in enhancing operational efficiency. The hosts, including Raj, express their appreciation for the creativity and technical achievements demonstrated by the winners.

# Golden Grot Awards - Transcript

Hello again, everyone! Are we having fun? Nice! I hope you’ve enjoyed the content so far. Now, we have a brief interlude for what is now the third annual Golden Grot Awards. 

We showed you some interesting dashboards that we found in the wild, and the Golden Grot Awards are a way for us to recognize special dashboards that were really well put together. Essentially, we give away a Golden Grot. I don't think it's actually made out of gold; otherwise, I would've heard from our CFO. But our Golden Grot winners receive a Golden Grot award, get flown out to GrafanaCON to share their inspiration and the dashboards they’ve built, and also receive a hearty handshake from me, along with an awkward photo, which I'm sure they are really looking forward to.

In all seriousness, these are the best of the best dashboards that truly make us go, "Wow!" They are voted on by an esteemed panel, and then we bring that vote out to the public for the entire community to vote for the final Golden Grot winners.

## First Winner: Personal Category

For the first winner under the personal category, I'd like to invite Ruben out to the stage. Ruben is a repeat winner of the Golden Grot Award; he won last year, right? Yes! In fact, as a result of this, we’re considering changing our rules to maybe no repeat winners. Just kidding! 

But it’s an unbelievable dashboard, and I’m really excited to hear you talk about it. So take it away, Ruben!

---

**Ruben Fernandez:**  
Hello, everybody! My name is Ruben Fernandez, and I am a Principal Engineer at Dell Technologies. It is an honor to be here today talking about my dashboard, and I would like to thank everybody who voted for it. 

Why did I decide to create a dashboard about the Station? Well, I’m passionate about space, so I thought it would be great to create a dashboard with something that I really love. The technology I used is Grafana Cloud, specifically a free account. I implemented multiple API calls using Python to gather my data sources, including the Infinity data source for API calls. 

I also used the Prometheus Python client for instrumentation to get the metrics from the data I was collecting. Additionally, I utilized Grafana Alloy to send these metrics to the cloud, and most of the panels are out-of-the-box panels—nothing too crazy. Some of them utilize the Business Variable plugin from Volkov Labs to enhance the appearance, and I also employed the video plugin from Innius to display videos from YouTube.

I divided my dashboard into two parts. The top section tracks the Station, where I have a geomap panel running an API call to get the longitude and latitude for the Station. This allows me to show its current location, refreshing every five seconds to create the illusion that the Station is moving around the globe. I also display the path that the Station is following with red dots.

Using the same metrics, I created another panel called the "passing by panel," where I can see where the Station is currently passing. For example, you can see on the right top that it says it is passing through Canada. Another basic panel indicates whether the Station is in a day or night area.

This is the cool part! I learned that NASA had streaming videos from the Station, so I decided to use one from a camera pointing directly down at Earth. The moment I saw the video playing alongside the panels providing synchronized information, I realized I was doing something special. I spent hours watching the video and examining the data from the other panels—all working in harmony.

I also added a widget from NASA called "Spot the Station," which allows users to enter their city and find out when the Station will next pass by their location. This is the top part of my dashboard.

Initially, it was just my dashboard, but then I realized the Station is not just a piece of metal; it has people inside—astronauts who share my passion for space. They are risking their lives and working on projects that will benefit us here on Earth. So, I created a panel featuring a basic data set of all the astronauts in space, adding videos and pictures from the internet, arranged nicely using the Business Variable plugin from Volkov Labs. 

I created similar panels for the spacecraft docked at the Station and the projects the astronauts are working on, linking to NASA's webpage for 15 ongoing projects. Lastly, I included a telemetry data panel with metrics like altitude and speed, which I already had from the API calls.

Now, I have an animation that hopefully works, showing everything in action. The Station is passing by Canada, and on the left, you can see it’s saying it’s passing through British Columbia while the video displays the mountains. 

In the lower part, you can select an astronaut to view their video and information. The video explains what they do in space. For the spacecraft, you can see them flying through space, and at the end, it shows the docking process. 

Here’s the URL for the live dashboard. You can check it out with the QR code provided. If you have any questions, please feel free to email me or ask me during the convention. Thank you!

---

**Host:**  
Amazing job, Ruben! Congratulations on winning the third annual Golden Grot Award! Thank you so much, and I hope to see you again next year.

---

## Next Winner: Professional Category

For our next winner, the final winner of the professional category of the annual Golden Grot Awards, I’d like to introduce and bring up to the stage Grant Chase, who has built an amazing municipal water filtration and restoration dashboard. Grant, thanks so much! Take it away!

---

**Grant Chase:**  
Thank you! I’m a musician, a father, a husband, and an organic homesteader with a passion for open-source IoT industrial automation technologies. Imagine an application where your user base is an entire city population, where your SLA is mandated by state and federal agencies, and any downtime could have critical public health or environmental impacts. This is wastewater.

The concept is simple: return a clean product to the water cycle, but it’s not easy processing a million gallons of wastewater every day. This requires extensive automated systems referred to in industrial automation as SCADA. SCADA stands for Supervisory Control and Data Acquisition. It’s a suite of hardware and software that gives operations teams remote control, data visualization, data collection, and alarming capabilities.

Now, you might be asking, if SCADA provides all of this, then why use Grafana? Well, besides the obvious, the rapid development allows me to quickly meet the needs of multiple teams. JSON helps me replicate styles to create a cohesive environment across the instance, and I can combine multiple data sources, preventing data siloing in our organization.

On the user side, intuitive navigation makes training very simple for the crew and adoption quick. It has become a staple in our organization—a single source of truth and more than just a single pane of glass. It is the central point of all data for our organization.

We also segment our data, separating historical from live processes, enhancing security and making it easier to share data with external organizations, such as contractors and engineers who need our data to review the process. 

Let’s get into a live demo, and I’ll show you what it’s all about.

---

This is the landing page for all operators. The flow is wastewater. From left to right, we see the influent pump stations that feed the wastewater treatment plant. This is a seven-day total of the influent. We process a little less than a million gallons each day; for perspective, the city of Seattle processes over a hundred million gallons daily. So, when you flush the toilet, you're contributing to this!

Over here, we have the heart of the facility—the treatment process. Our treatment process is biological, meaning we create an environment conducive to certain aerobic bacteria that break down organics in the wastewater. After this column, it moves to the effluent, which can either be recycled water or the ocean outfall.

This is the seven-day total output, along with chemical levels for all the chemicals we have on site. There’s also an embedded I-frame showing the last five videos recorded from the microscope. If the microscope is live, the stream will be live; otherwise, it fails over to pre-recorded videos after five seconds.

Underneath each process area is a breakdown of more in-depth information. For example, here are two of our main pump stations over the last six hours, with a shared tooltip connecting the times. We’re using mapping to make the pump states operator-friendly, showing them as "on" and "off." These little nuances help the end user understand what they’re looking at, and Grafana makes it easy to make it visually appealing.

We collect metrics in a very dense fashion—by the second. If an occurrence happens and I need to drill down, I can increase the resolution of that particular graph to pull in more detail.

Now, let’s go to where our bug friends live and look at the aeration level in the tank. We can see flow numbers from sensors contributing to that basin. In this area alone, we collect over 200 metrics from pumps, sensors, motor speeds, and airflow. We want to maintain a certain level of dissolved oxygen for the right bacteria, and this shows we’re on track. Below, you can see the valve position, which adjusts with demand while maintaining a constant dissolved oxygen level.

Finally, I’ll pull up our microscope videos. This interface is custom-built to allow our operators to quantify microorganisms observed over time. Below, we have a thumbnail time series representation of each video. I can click to view a video live, and if I want to expand my time range, I can see videos over the past six months.

This particular microorganism, a rotifer, is trying to suck in food. These microorganisms are responsible for returning clean water to us, which is amazing. We create an environment for them to thrive.

This interface isn’t just for fun; it also allows us to tag microorganisms retroactively. After a video is taken, we can update metadata. For example, if I no longer want this video to be a favorite, I can change that status and push it to our backend program through an API.

In closing, what you’re seeing here are the possibilities of that big tent concept—if you can think it, you can probably build it with Grafana. A big shoutout to Volkov Labs for these plugins, as they make this possible.

Thank you very much!

---

**Host:**  
That’s really amazing stuff, Grant! Not what we typically see in IT dashboards. You give new meaning to terms like flow, sinks, and payloads! Just kidding. But in all seriousness, that was an incredible view of what you’re doing at the municipal treatment plant. Thanks so much, and congratulations on your Golden Grot!

Thank you, Raj.

## Raw YouTube Transcript

Hello again everyone. We having fun? Nice. Hope we've enjoyed the content so far. So now is a brief interlude
for what is now the third annual Golden Grot Awards. And so we showed you guys some of the
interesting dashboards that we found in the wild and the Golden Grot
Awards are a way for us to recognize special dashboards that
were really well put together and essentially give away a Golden Grot. I don't think it's actually made out of
gold otherwise I would've heard from our CFO, but our Golden Grot winners
get a Golden Grot award. They get flown out to GrafanaCON to
be able to share their inspiration and their actual dashboards
that they've built. And they also get a hearty handshake
from me and an awkward photo, which I'm sure they're really looking
forward to. But no, in all seriousness, these are the best of the best in terms
of dashboards that really make us go, wow. They are voted on by an
esteemed panel and then we kind of bring that vote out to the public
and have the entire community vote for the final Golden Grot winners. So for the first winner
under the personal category, I'd like to invite Ruben out to
the stage and Ruben is a repeat winner of the Golden Grot Award. Ruben actually won last year. That's
right, isn't it Ruben? Yes. And in fact, as a result of this, we're considering changing our rules
for maybe no repeat winners. No, just kidding. But unbelievable dashboard and really
excited to hear you talk about it. So take it away. Yep. All right, thanks. Okay. Hello everybody. My
name is Ruben Fernandez. I am a Principal Engineer
at Dell Technologies. This is an honor to be here
today talking about my dashboard and I would like to thank
everybody who vote for it. Why I decide to create a
dashboard about the Station? Well I'm passionate about the space. So I thought it was going to be
great to create a dashboard with something that I really love. So the technology that
I use is Grafana Cloud. I use a free account. I use multiple API calls using Python to get my data, my data sources, Infiniti data source also to do API calls. I also use the Prometheus Python
client for instrumentation to get the metrics from the data that
I was getting from the API calls. Grafana Alloy to send
these metrics to the cloud. And then the panels that I use, most
of them are out of the box panels, nothing crazy and some of them I am using the Business Variable plugin
from Volkov Labs to make those panel looks nicer. And also the video
plugin from Innius to display the videos from YouTube. I could divide my dashboard in two parts. The top one is about the tracking
to the Station where I have a geomap panel and I'm running
an API call to get the longitudinal and latitude for the station
so I can display where it is at any moment, the station, and I'm
refreshing that every five seconds. So that gives you the illusion
that the station is moving around the globe. I'm also displaying the path that the
station is following those red dots. Using the same metrics.
I create another panel, the passing by panel I call it, and using the Infinity data
source plugin I'm able to get with the location where the station is
passing right now at that moment, like in the sample you can see on the
right top it says it's passing through by Canada and also using the same metrics I'm creating, this is a basic one, just a panel to tell me
the station is passing by a day area or a night area. This is the cool part. Also, I knew that NASA had
streaming videos from the station. So I decide to use one from a
camera that was pointing down directly to Earth. And the moment that I saw the
video plaing and the panels giving me the same information, all those four panels
giving the same information, that was the moment that I realized that
I was doing something cool because I spent hours just watching the video
and reading the information that I was getting from the other panels and
everything working synchronized and receiving the same information.
That was pretty cool for me. Then I decide to add this widget
from NASA that is called the Spot the Station that allows everybody
to just introduce in where you are, your city, in your country,
and some places your state, and you get when it's going to be the
next time that the station is going to pass by your location. And this is what the top
part of the dashboard. And for a while it was my dashboard, but then I realized that
the station is not just a piece of metal, it's not
just a satellite moving around. It has people inside all
these astronauts that they have my same passion about the Space. They are risking their lives and they
are working in projects that we're going to use later and here down on earth. So I decide that they
deserve a space on my panel, on my dashboard. So I create this panel with
another API call that I'm getting a basic data from all
the astronauts in the Space. And I also add a video
for each one of them, a picture from internet and using
the business variable plugin from Volkov Labs. I put
all together in a nice way. And also I use the video plugin from
Innius to display the video using variables. That way I can show
different videos depending of the astronaut. So I did the
same for the spacecraft, docked at the station, similar panel, same different information, similar panel. And I created another panel for the
projects that they are working on. The astronauts at the station, these are links going to
NASA webpage where they talk about 15 of the projects
that they are working right now. And last ones, I call it
telemetry data. These metrics, I already have them from
the other API calls, so I decide that it was
nice to have the attitude, the speed of this basic data. And this is how the lower
part of my dashboard look. And now I have an animation that hopefully
works where you can see everything working on the top part. The station is passing by Canada on the
left you see it saying is passing by Canada, Columbia, British Columbia, and the video is passing through the
mountains and also on the spot the station trying to search when going
to be the next time that I can see the station spot, the station in Madrid, Spain. And now in the lower
part you see I can move around searching for the astronaut that I want
to see the video and the information. So it's changing depending on
the astronaut that you select. And the video is from YouTube's
telling you what they do and why they do whatever
they do in the Space. And this one for the
spacecraft, this is cool too. Those are all the spacecraft that
the astronauts use to go to the station back and forth. And here
is the launch of one of them. You can see it's flying through the
space going to the station and at the end you can see is docking into the
station, which is pretty good to see. And those are the links
that I told you before. And you see is giving
information from the page on NASA. And that's it. That's my dashboard. Here you have the dashboard is
still live. Here is the URL. And you can check on the QR code that you
want to see and the user and password. And if you have any question,
please send me an email or ask me. I'm going to be around during
the convention. Thank you. So amazing job Ruben, and congratulations for winning
the third annual Golden Grot award. Thank you so much. And hope to see you again next year. I'll be here. Maybe. Yep. Alright, thank you.
No worries. Thank you. Great. Okay, great. So for our next winner, our final winner for the professional
category of the annual Golden Grot Awards, I'd like to introduce and
bring up to stage Grant Chase, who's built an amazing municipal water
filtration and restoration dashboard. Grant, thanks so much. Take it away, sir. Sir, I'm a musician, a father and husband and a
organic homesteader with a passion for open source, IoT industrial
automation technologies. So imagine a application where
your user base is an entire city population where your
SLA is mandated by state and federal agencies
and any downtime could have critical public health
or environmental impacts. Well this is wastewater. The concept is simple return a
clean product to the water cycle, but it's not easy processing a
million gallons of wastewater every day. This takes extensive automated
systems referred to in industrial automation as SCADA. S SCADA is an industrial acronym
for supervisory control and data acquisition. It's a suite of hardware and software
that combined give operations teams remote control, data visualization, data collection, as well
as alarming capabilities. Now you might be asking at this
point, if SCADA provides all of this, then why Grafana? Well,
besides the obvious, the rapid development allows me to
quickly meet the needs of multiple teams. And JSON quickly helps me
with reduplicating any styles create a cohesive environment
across the instance, and I can combine multiple data
sources, of course the Big Tent, so it prevents data siloing in our
organization. On the user side, intuitive navigation makes training
very simple for the crew and adoption quick. And it became and is a
staple in our organization. It's the single source of truth
and it's more than just the single pane of glass. It is the central point
of all data for the organization. And then there's segmentation. So by separating the historical
from the actual live process, we free up critical resources
for the control side. And we also separate the data
historically on another layer, enhancing security and making it
easy to make this data available to organizations outside. Contractors and engineers often
need our data to review the process. So let's get into a live demo and
I'll show you what it's all about. All right, so this is the landing page
for all of the operators. The flow is wastewater. Left to right here we see the influent pump stations
that feed the wastewater treatment plant. This is a seven day total of the influent. Now we do a little less than a million
gallons every day for some perspective, the city of Seattle does over a
hundred million gallons every day. So when you flush the toilet,
you're contributing to this. Over here we have the heart of the
facility, which is the treatment process. Our treatment process is biological, meaning that we create a environment
that is conducive to certain aerobic bacteria that break down organics in
the wastewater. After this column, it moves to the out - the
effluent as it's referred. It can either be the tertiary process, which is recycled water
or the ocean outfall, and then it goes out to the fishes. This is the seven day total of the out. And we have chemical levels
for all of the chemicals we have on site, as well as an embedded Iframe of the last five videos that were taken from the
microscope. If the microscope is live, then the stream will be live. It fails over after five seconds
to the prerecorded videos. Underneath each process area is a breakdown of more intense and in depth
information for each process. So if I scroll down here, I'm
going to enter, not that one, but that one's cool. Okay, so here is two of our main pump
stations over the last six hours, a shared tool tip kind of
bonds the times together. Here we're using mapping to
take the pump states of one and zero to a more operator
friendly on and off. These little nuances really help your
end user know what they're looking at. And of course, Grafana makes it
pretty easy to make it look pretty. We collect metrics in a very
dense fashion. So by the second, and if a occurrence happens and
I really need to drill down, I can increase the resolution
of that particular graph and it's going to pull
in a little more detail. So I'm going to head back
to the home screen. Now. We're going to go where
our bug friends live and we're going to look at the
aeration level in the tank currently. So here we can see from the
flow top down numbers of sensors and flows that contribute to that basin.
Now this area alone, we collect over
200 metrics from pumps, sensors, motor speeds, airflow. This using thresholds
we want to be in that green zone maintaining a certain parts per million
of oxygen in the basin for the right bacteria. And this shows
that we're on track below, you can see the valve position. So the
valves are swinging wider with demand, but maintaining a
constant dissolved oxygen. And so we use this a lot if we
have problems with our aeration. So the final thing here, I'm going
to go back to the home screen. We're going to pull up
our microscope videos. So this interface is custom
built to allow our operators to quantify what microorganisms are
observed at different periods of time. So below we have a thumbnail time series representation of each of these videos. I can go one click in and now I
have that video live if I want to expand my time range and
look at videos over the past six months.
Then now my thumbnail is a lot longer here. We can see this one's been tagged
as a favorite, hence the little star. This is a great one. Actually, this one's even better
because he actually eats it. This is a rotifer trying to suck in
this piece of food. There it goes. So he's hungry. Alright, so these are the guys who are responsible
for returning clean water to us, which is pretty amazing. And all we do is create an
environment for them to live. Now this interface isn't just for fun. It also allows us to tag the
microorganisms retroactively. After the video is taken,
we can update the metadata. Let's say that I didn't really
want this video to be a favorite. I can make it false. Push that to our backend program
through an API. Update successful; star is gone from the favorites. I can also search by favorites using
dashboard variables. I can just bring in the favorites from the last six months, maybe drill down to a certain
microorganism, a water mite, also known as hydrocarnia.
Here's our friend right there. Pretty icky looking dude. Now these microorganisms
are indicative to the age of the wastewater in that particular basin. So this is not one we normally
want to see. We've only it once, but it helps us quantify with the
timestamp when that was observed. So in closing, what you're seeing here is the
possibilities of that big tent concept where if you can think it, you could
probably build it with Grafana. A big shout out to Volkov Labs because
these plugins and what you're seeing here is what makes that possible. So remember that if you can think it, you can probably do it with
Grafana. So thank you very much. Cool. That's really amazing stuff, Grant. Not what we typically see in
some of our IT dashboards. You give new meaning to things
like flow and syncs and payloads and maybe even logs. No, just
kidding. But in all seriousness, that was an amazing view of what you're
up to at the municipal treatment plant. Thanks so much and
congratulations, your Golden Grot. Thank you, Raj.

