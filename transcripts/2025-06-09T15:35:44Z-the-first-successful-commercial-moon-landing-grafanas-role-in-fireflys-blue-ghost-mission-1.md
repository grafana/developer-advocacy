# The First Successful Commercial Moon Landing | Grafana&#39;s Role in Firefly&#39;s Blue Ghost Mission 1

Published on 2025-06-09T15:35:44Z

## Description

Go behind the scenes of Firefly Aerospace's historic lunar landing. Jesus Charles, descent flight director for Blue Ghost Mission 1, ...

URL: https://www.youtube.com/watch?v=bbt2lO9VN9M

## Summary

In this YouTube video, Jesus Charles, the descent flight director for Blue Ghost Mission 1 at Firefly Aerospace, shares the story of the mission that successfully landed a lunar lander on the moon on March 2nd. He discusses Firefly Aerospace's role as a space services provider and outlines the team's rigorous preparation process, including extensive training and the implementation of Grafana dashboards for mission operations. Charles reflects on his personal journey from growing up in Mexico to pursuing aerospace engineering and ultimately contributing to a historic lunar landing. He emphasizes the importance of teamwork, the intense moments of decision-making during the descent, and the scientific payloads operated during the mission, including a unique solar eclipse captured from the lunar surface. The video serves as both a technical overview of the mission and an inspirational story encouraging perseverance and dreams in space exploration.

# Blue Ghost Mission 1: A Journey to the Moon

Hello everyone! I'm happy to be here and share the story of our project. My name is **Jesus Charles**, and I had the immense privilege of being the descent flight director for **Blue Ghost Mission 1**. Today, I want to share that story with you. Please don’t forget to send in your questions for the Q&A at the end.

### What is Firefly Aerospace?

First of all, what is **Firefly Aerospace**? We are a space services provider focused on providing safe, reliable, and economical access to space. We achieve this through our three core products: 

- **Alpha and MLV launch vehicles**
- **Blue Ghost lander** (the focus of today's talk)
- **Orbital vehicle, Elytra**

We successfully landed on the moon on **March 2nd** of this year, but behind that achievement lies a story of the people, processes, and efforts it took to get there. 

### The Control Room Moments

Picture this: you’re in the control room, in front of your monitors. The clock is ticking, and the lander is hurling down towards the moon. We have less than **30 minutes** to decide whether to continue or abort our descent sequence. There’s no time for second-guessing; we must make the right call. Our only window into this complex machine is a set of dashboards. 

Here’s a glimpse into the moment our team decided to go for landing:

- **Thermal state:** 11
- **Power descent initiation (PDI):** 97% state of charge

We conducted a go/no-go poll with the following results:

- Payload? **Go.**
- Comp? **Go.**
- Ground software? **Go.**
- Flight software? **Go.**
- ABI? **Go.**
- VNS? **Go.**
- GNC? **Go.**
- Fido? **Go.**
- Prop? **Go.**
- TCS? **Go.**
- Systems? **Go.**
- C? **Go.**
- FC? **Go.**

The **Blue Ghost Lander** was a **go** for power descent initiation. 

As you can see, this was an intense moment. It was fast-paced and crucial that we made the right decision. Being at the flight director console is akin to being the orchestra director for the mission operations team; I was responsible for ensuring that the procedures and processes were followed to meet our mission goals.

### My Journey to Flight Director

Being in the flight director seat is a long way from where I started. Like many of you, I didn’t grow up in the U.S. I grew up in **Mexico**, and it wasn’t until I was 16 that I came to the U.S. for high school. Growing up exposed to both Mexican and American cultures taught me to be adaptable and leverage the power of diversity. 

I always worked hard and set goals for myself. Growing up, I liked math, science, and working with my hands, so I pursued a career in engineering. I earned a degree in **aerospace engineering** from the University of Texas at Austin. My first chance to work with spacecraft came as a student when I worked on **CubeSats**.

Afterward, I began my career as a **payload integration engineer** at the Johnson Space Center in Houston, where I worked on several projects. One significant milestone was when I saw my name fly to space, which felt like a major achievement. However, I always felt the need to keep pushing myself and make even bigger dreams. I wondered, “What if I could fly payloads to the moon instead of just the ISS?” 

### Joining Firefly Aerospace

In 2017, **Firefly Aerospace** was founded, and I began tracking them closely. As I was studying in Austin, I wanted to work there, but there were no space companies. When Firefly emerged, I knew they were one of the NASA providers competing for lunar missions, making it a perfect match. I joined in early **2020** and began working on the first set of payloads we flew on our alpha rocket, as well as proposals to make those missions a reality with NASA.

Here’s an early concept of our lunar lander. After a year of hard work, we were selected by NASA, and Blue Ghost lander became a reality. In the early days, our team consisted of only five people, but we were all driven to make history.

### Challenges and Growth

As I sought to grow as an engineer, I took a leap and joined the **mission operations team**. I left my comfort zone of payload management to help establish a new capability for the company in mission operations. Initially, I didn't have all the answers, but I had the determination, drive, and process experience, along with a team eager to learn and build.

We had the chance to visit other organizations, including the **ISS** and **ISA operation center** in Germany. We learned how they structured their operation centers and approached similar missions, which helped us validate our approach.

As we began working on this project and setting up our systems, we started using **Grafana** to build the dashboards for our video wall. The video wall is a grid of TVs at the front of the operation center, providing situational awareness to all operators. It displays critical information to help us make decisions during the mission.

### Training and Preparation

Once the systems and processes were in place, we focused on the people. We conducted an extensive preparation campaign for our operators, which included:

- **16 mission simulations**
- **More than 500 hours of training**
- **A full week of 24-hour support**

We wanted to ensure our team knew the mission and the necessary decisions inside and out. Initially, we were like the blind men and the elephant—each of us an expert in our own system but not seeing the full picture. After intense training and hard work, we came together as a unified team.

We were honored to hear from **Gerry Griffin**, an Apollo flight director, who emphasized that teamwork was key to making this mission a reality.

### Mission Readiness

With our Grafana deployments, we organized the development and production of our dashboards, ensuring redundancy in our systems. There were numerous dashboards created to help operators understand their systems better. We even deployed an instance of Grafana in **AWS** to make it easier for our customers to access their data.

By this time, we were mission-ready. Our mission operations team was in the control room, eagerly awaiting the moment our spacecraft would separate from the rocket. The anticipation was palpable as we watched the live stream during the launch from **SpaceX’s Falcon 9**.

### The Moon Mission

Our mission to the moon had a **45-day transit**, with 25 days in Earth orbit, four days to reach the moon, and 16 days in lunar orbit. Throughout this time, we executed multiple maneuvers, using our dashboards to inform our decisions. We collected stunning images and videos from our onboard cameras, providing a remarkable visual journey.

On descent day, we finally had to land in the **Sea of Crisis**—though spoiler alert: there were no crises! We had a full house in the control room, with about **40 engineers** present, many of whom were double-staffed at their consoles. The mix of emotions was intense, with years of work culminating in this critical event.

During breaks, while our spacecraft was behind the moon and we were cut off from communication, we reassured ourselves that this was just another mission simulation. We had our dashboards and processes in place to execute successfully.

### Landing on the Moon

Finally, on **March 2nd**, around 2:00 AM, we landed on the lunar surface. Here’s a compilation of various camera angles recorded during our descent. Remember, during the landing, we could only see our dashboards and data—not the visuals!

I was on the night shift, starting my official shift at **7:00 PM** and ending at **7:00 AM**. As we watched the touchdown clock tick down, I felt a mixture of nerves and excitement. My role as flight director was to keep the team calm and focused.

After landing, I prepared a speech to celebrate that historic moment:

**"Blue Ghost riders, the path to the stars is no longer limited to nations alone. Firefly is building the road to the next frontier, one mission and one dream at a time. Tonight, we didn't just reach another mission milestone; together, we created a moment in history."**

### Achievements and Science Goals

This moment was significant, marking the first fully successful lunar landing by a commercial company. We aimed to share this experience with the world, not just confining it to those in the control room. Our marketing team produced a "Meet the Team" video series, along with launch and landing live streams to inspire others.

During the mission, we flew **10 NASA payloads** from various universities and NASA centers, relevant to our landing site. Some of our notable experiments included:

- **LISTER**: A lunar drill that penetrated up to three meters into the lunar surface.
- **SCALPS**: A set of cameras recording the descent, focusing on the interaction between engine plumes and lunar regolith.
- **EDS Experiment**: A technology designed to clear dust from surfaces on the lander.
- **LMS**: An experiment that deployed probes on the lunar surface to measure magnetic fields.

We even captured a **solar eclipse** on the lunar surface, a first in history, as the Earth moved in front of the sun, creating a red tint on the moon's surface.

### Conclusion

Our mission on the lunar surface lasted just over **14 days**, during which we achieved **100% of our science goals** and gathered valuable lessons learned. For example, we discovered that current thermal models for the lunar surface do not account for landings near craters.

As we look forward, we plan to implement these lessons in our upcoming missions, **Blue Ghost Mission 2** and **Blue Ghost Mission 3**. 

Being the flight director for this mission was an opportunity of a lifetime. Blue Ghost Mission 1 exemplifies how you can chase your dreams, work hard, and persevere to achieve great things. 

To everyone here, using the fantastic tools that Grafana provides: keep building, keep dreaming, and maybe it will help you land on the moon one day. 

**Thank you very much!**

## Raw YouTube Transcript

Hello everyone. I just want to say I'm happy to be here
and happy to share the story of our project. My name is Jesus Charles and I had the
immense privilege of being the descent flight director for Blue Ghost Mission 1, and today here I want to share that story. So please don't forget to send your
questions for the Q&A at the end. Alright, so first of all,
what is Firefly Aerospace? Firefly Aerospace is a
space services provider. We focus on providing safe, reliable, and economical access to space. We
do that via our three core products, which are our Alpha and MLV launch
vehicles. We have our Blue Ghost lander, which I'm here to talk about today, and
we have our orbital vehicle, Elytra. So we landed on the moon. That
was on March 2nd of this year. But behind that achievement, there's
a story of the people, the processes, and the effort it took to
get there. So let's dig in. So picture this: you're in the control
room, you're in front of your monitors. The clock is ticking and the lander
is hurling down towards the moon. We only have less than 30 minutes to
make the call to continue or abort our descend sequence. There's
no time for second guessing. You've got to make the right call. Your only window into this complex
machine is a set of dashboards. There's no time to make the wrong call, so we have to make informed
decisions via our data. This video is the moment where our
team decided to go for landing. Thermal state is 11. We will be starting PDI
at 97% state of charge. All councils, flight and ops -- PDI cannot be aborted if the lander has
transitioned to descent critical. Also, at this point, we're going to proceed
with our power descent initiation. Go/no go poll. Starting
with payload? Go. Comp? Go. Ground software? Go. Flight
software? Flight software is go. ABI? ABI is go. VNS? VNS is go. GNC? Go. Fido? Go. Prop? Go. TCS? Go. Systems? Go. C? Go. FC? Go. Blue Ghost Lander
is a go for power descent initiation. ...three minutes remaining
until power descent initiation. We are Go for the power
descent initiation. So as you can see, this
was -- thank you -- an intense moment. It was fast and it was very critical
that we made the right decision. Being there in that console,
that's a flight director console, you're basically the orchestra director
for the mission operations team. You're in charge of making sure that the
procedure and the process is followed so that we can meet our mission goals.
But being in the flight director seat, that's a long way from where
I started. Like many of you, I didn't grow up in the
U.S. I grew up in Mexico. It wasn't until I was 16 years old when
I came over to go to high school and start a new chapter of my life. So
being exposed, while growing up, to the Mexican and American
cultures taught me really to be adaptable and to leverage
the power of diversity. I really wanted to show that I
could work hard and I could make an effort. And really, growing up, because I was removed
from access to space, it wasn't really a dream that
I had since I was little. It was something that I developed. I
always heard that I needed to work hard, so I set goals for myself and I started
just moving forward to meet them. So then growing up I liked math,
science, and working with my hands. So I decided to go for
a career in engineering. I went for a degree in aerospace
engineering at the University of Texas at Austin. My first chance of getting to work with
spacecraft was while I was a student. I used to work on CubeSats. Those are those small satellites that
you can see up on the big screen. And then after that, I got to start my career as a payload
integration engineer at the Johnson Space Center in Houston where I worked
on a few different projects. Here in the second picture on
the bottom, you can see STP-H5. That's a complement of experiments that
is still flying on the ISS up to this day. So there was a moment in my career
when I saw my name fly to space, and that was a big milestone.
That was something that felt like, okay, I think I made it. But I always had that feeling that
I need to keep moving forward. I need to keep pushing and
make even bigger dreams. So one time I said, what
if I could fly payloads, but instead of the ISS to the moon? And then that's where Firefly
Aerospace is going to enter the story. So Firefly Aerospace is a new space
company that was founded in 2017 and, in the beginning, I had my
eye on them. I was tracking them. As I went to the university in Austin, I
wanted to come back and work in Austin, but there were no space companies.
So once Firefly was there, I was tracking them. I knew that they were one of the NASA
providers able to compete for lunar missions and the goal for those lunar
missions is to fly payloads to space. So it was a perfect match. So I joined in early 2020
and I started working on the first set of payloads that
we flew on our alpha rocket, and then we also worked on the
proposals for making those missions a reality with NASA. Here you can see a very early concept
of a lunar lander that we had back then and, basically, we worked the proposals and after a
year we were selected by NASA and we received a call from them making
Blue Ghost lander a reality. And also here you can see
a picture of our team. This is one of our early
program reviews where we had the whole team present to NASA our design
and show that we knew how to get the project going. You can see
there's a few people here, but basically when I joined in early 2020, the team was about only five people,
but we were all driven to make history. So looking again at the
challenges and driving forward, I wanted to keep growing as an engineer. So after a while I took a leap and I
joined the mission operations team. I left my comfort zone of knowing
payload management to help stand up a new capability for the
company in mission operations. So the job was to make sure that we
prepare the people, the processes, and the systems to make sure that
we could execute our lunar mission. And in the beginning, I
didn't have all the answers, but I had the determination,
I had the drive, and I had the process experience along
with a team that was eager to learn and build. We even had the chance
to visit other organizations. We visited the ISS and the ISA
operation center in Germany, and we got to see how they've structured
their operation centers and how they approach these types of missions so that
we could learn from them and validate our approach. As we started
working on this project, and as we started setting up the systems, we started taking our first
steps into using Grafana. We basically started using Grafana
to build the dashboards that we have for our video wall. And
what is the video wall? So the video wall is basically a TV
grid that is in the front of the room and in the operation center. It is meant to give situational awareness
to all the operators sitting there. It is intended to show the critical
and clear information so that we can make all the decisions
during the mission, right? It is meant to collaborate
and help us achieve all of our goals. So this is when we started
choosing what system we wanted to use and we chose Grafana
as our data display system. It was already used to track
other metrics in the company. So we were able to leverage that
experience and start applying it towards mission operations. So once the system and
the process was created, we had to focus on the people. So we had a pretty extensive preparation
campaign for all of our operators. We had 16 mission simulations, we had more than 500 hours of training, and we had even a full
week of 24 hour support. We really wanted to make sure that
our team knew the mission and all the decisions that needed to be made like
the back of their hand. In the beginning, when we came together, it
was a room full of experts. There's a console for every part of the
lander or every system and each of the persons sitting there is an expert. But we were somewhat like the blind and
the elephant. We were all at our system, but we weren't seeing the full picture. So after this intense training
campaign and a lot of hard work, we were able to come together
as a team and work as one. We had the privilege and the honor
of hearing from one of the Apollo flight directors, Gerry Griffin. So he came over and provided us
with a chat on how he experienced Apollo, and what he thinks we need to do. And he really emphasized that teamwork
was the key element that we needed to rely on to make this mission a reality. So as we are starting to prepare,
as we're starting to get ready, we have our Grafana different deployments. So we had deployments that
helped us organize the
development and the production of our dashboards, deployments that gave us critical
redundancy in the systems so that we could make all the decisions that we needed
and we could face any of the anomalies. Imagine if we had this infrastructure
that is just maybe single threaded and one of the elements fails. We would not be able to have the data
that we needed and if that compounds with an anomaly, that would
be a recipe for disaster. So there was a lot of detail that
was put into our architecture. We also had a lot of dashboards
that were created by the team. So you can imagine there are 20
consoles in the room and a lot of these systems are very complex. So you can
imagine there's a lot of dashboards that got created so people could
know more about their system. We even had an instance of Grafana
deployed in AWS so that we can make it easier for our customer to get access to
their data without having to go through a lot of complicated setups.
By this time in the story, we are mission-ready; our systems and people and
processes are all in place. The picture you see on the left is our
mission operations team in the mission control room and we're all
sitting there. We're waiting. You can kind of see the TVs. We're
watching the livestream for the launch. Our mission launched in
a Falcon 9 from SpaceX. So we're all sitting there in anticipation
of the moment when our spacecraft is going to separate from the rocket and
all of our dashboards are going to get data. You can see that it says no
data. We're waiting for that moment. And then on the second picture, you can
see a very busy operations control room. This is the picture during our first
shift handover where we had the night shift come in -- or sorry, the night shift go out and the
green shift come back in -- to keep the operations going. You can
see the operators are really busy. They're exchanging notes. They're talking about the data
that they were able to visualize. And you can see now our dashboards are
all beautifully lit up with data and we can get a sense of what's
happening with our spacecraft. So our mission to the
moon had a 45-day transit. 25 of those days were in earth orbit, and then the four days that
it took us to get to the moon, and then we had 16 days
around in lunar orbit. All through the transit, we executed multiple maneuvers and we
used our dashboards to inform us of everything that was happening and
allowed us to make critical decisions. As you can see, we also had the chance to collect a lot
of images and beautiful video from our onboard cameras. It's really a night and day difference
being able to watch these images in the quality that we
were able to collect. So it's funny that every time I will
go into the control room for my shift, I will look through the last shift's
images that they downlink and I'll pick a favorite and it's like, this is amazing.
This is mind blowing. And then I came up the next day and it's
a whole new set of pictures and another favorite. So these are
a few of my favorites. I think my top favorite is this:
as we're going around the moon, you can really see and
start getting a feel for the excitement and everything that's
going to happen on descend day. So you can see here that we're about a
hundred kilometers over the surface of the moon. While our systems
are doing a lot of checks, we're doing a lot of preparation
to get ready for the landing. So then finally the day came -- the day where we had to do our
descent into the sea of crisis. But spoiler alert, there were no crisises. That's just the name of her
landing site: Mare Crisium. So on descent day we had a full
house. We had our main control room, which had about 40 engineers.
Like I told you, there were 20 consoles and almost
all of them were double staffed. We had about 40 engineers
just in that single room. And then we had a lot of other
engineers in supporting control rooms, along with our NASA customer also on site. During the night, because this
happened in the night shift, our team was feeling a mix of
emotions. As you can imagine, these are years and years of work that
are basically funneling into this single critical event. So we wanted to
make sure that we were ready. So during a few of the breaks -- as
you can see in the picture on the left, we had a few breaks while our
spacecraft was going behind the moon -- we were blocked from communications. So that gave us a little bit of a
chance to stand up, stretch our legs, and we just kept
reassuring ourselves, 'Hey, this is just like another mission
simulation.' We have our eyes on the data, we have our dashboards, and we have the
process and we are prepared to execute. And then the picture on the right is
after the 'Go/No Go' video that you saw earlier. We're all locked in. Everyone
knows that for the next 30 to 40 minutes, we're going to have to be laser-focused
and we're going to have to pay attention to our dashboards. The whole descent for the lander to go
into the lunar surface is automated. So the only way that we can experience
this descent is through our dashboards and seeing the data on the screen. And then we get to the
descent. So on March 2nd, it was about 2:00 AM when we
landed on the surface of the moon. Here's a compilation of a lot of the
cameras and camera angles that were recording as we made our descent. But please remember that these
videos we got after the fact; during our landing, again, all that we could see were our
dashboards and the data in front of us. So these are a few of the different
camera angles as we're coming down that day. I was on the night
shift, so I started... my official shift was at 7:00
PM and it wouldn't end until 7:00 AM. So while we were
looking at the touchdown clock, just come down and tick down and get
closer to zero, it was very exciting. I remember feeling nervous.
I remember feeling excited, but I knew I needed to just stay calm
and make sure that the room was calm and collected.
Like I mentioned, the job of the flight director is
kind of to be like the orchestrator, and I needed to make sure that the
team will play this music to get us to the surface basically.
And then afterwards, I prepare a speech and I wanted
to make sure that I celebrated the moment when we touched down because I
had full confidence that we were going to be able to execute that.
So here in the next chart, this is my speech that I shared
after the touchdown footage. Blue Ghost riders, the path to the stars
is no longer limited to nations alone. Firefly is building the
road to the next frontier, one mission and one
dream at a time. Tonight, we didn't just reach another
mission milestone. Together, we created a moment in history. It still gives me chills just to watch
that footage and thinking again of that moment. So this was a
very critical moment. It was important because it marks the
first time that we had a fully successful lunar landing by a commercial
company. Also during our mission, we had the goal of sharing
this experience with the world. We didn't just want that to be limited
to the people that were in the control room. So our marketing team put
together a meet the team video series, and they put together our launch
and then landing live streams. So they're made public so that we have
a chance to reach out to public and make sure that we get an opportunity
to inspire and to show the people that if you work hard and
if you follow your dreams, you can also be part of something great. Again, during our preparation, we were looking at making sure
that we were ready for any anomaly. Like I mentioned before, we had created a lot of dashboards
and we had done a lot of training. So I wanted to show you, next, what it would look like to
be in that control room. What was the data available for us to
know that everything was going nominally. This is just one of the
many, many dashboards that
we used during that descent. As part of the process, we knew we needed to track information
that you can see on the left pane, such as the altitude and range
distance to our landing site. So as we're coming down, we would
be able to see that narrowed down. But also, after seeing a lot of the
other attempts at lunar landings, we wanted to make sure that we had very
clear proof and clear data showing that we had landed successfully on the lunar
surface. So the panel in the middle is showing the actual acceleration
along the vertical axis of our lander. So this is a device that
measures the acceleration, right? So after we made a
successful lunar landing, it would need to match the acceleration
of the lunar gravity exactly in that axis showing that we were
upright and we were not in a different orientation. And then the panel right next to it
tracks the sensors that we had on our footpaths. We had four footpaths on our
lander and each of them had a sensor. So we had this panel that would trigger
whenever those footpaths will align with a lunar surface. So that's when you saw our chief engineer
in the video say that we were on the surface of the moon. Those
were part of the verifications. We had a lot of engineers
check their data, and then relay to the chief engineer and
he was the technical authority able to say, 'Hey, we have confidently landed
on the moon upright and we're stable. So this is just one of the
dashboards that were used for that.' So, after landing on the moon,
that was not the end of the trip. We went to the moon because
we needed to get science done. So we had a full plate of payload
operations we needed to execute. So you saw the celebration from the team, you saw the other little
video of the flight director, flight controller and mission
director celebrating as well. But that only lasted a few minutes. We
knew we needed to keep our mission going. So after that, we all sat back down and
started hitting our payload operations. During this mission, we
flew 10 NASA payloads. These came from different universities, NASA centers and companies that were
selected for this particular landing site and the relevance it
had for their science. So up on the screen I can show you a few
of the videos of the payloads that were operated during this mission.
First, this is lister, which is the lunar drill. So this drill went down up
to three feet into the lunar surface, or I think it's
three meters, sorry. The next one is scalps, which is a set of cameras that
were recording our entire descent. The goal here was for their system
to see the interaction between the plumes generated by the
engines and the lunar regulate. And then the third image is
showing a before and after of the EDS experiment. This is a technology that would help
clear dust from surfaces on the lander. And then we have our LPV
and our LMS experiments. LMS is an experiment that deployed
probes on the surface of the moon. So we can basically say we shot the moon. And then we also had a mass that
deployed and these instruments were going to measure magnetic fields on
the surface. And then we had our lunar planted valve, which is self-explanatory. But then it's weird to think how
is it vacuuming in the moon, right? So it's not doing that. So if you want to have a conversation
about a lot of the details for the payloads, you can find me at the ask the
experts booth after the presentation. So also during this mission, we got the unique chance
to capture a solar eclipse on the lunar surface. That is something
that has never been done before. So we had the opportunity because we
were operating on the lunar surface, and we had a lot of cameras. So we had the benefit of
being there at the right time. You can see in the video as the earth
is moving in front of the sun and it's blocking it. Just as you can see
this type of event from earth, you kind of see it starts turning
like a little bit red. So we actually see that that is true. We see a red tint on the surface of
the moon as well as the sun is being blocked. Our mission on the surface
of the moon was 14 days long, a little bit more than 14
days. And during that time, we were able to hit a hundred percent
of our science goals plus some bonus operations. We were also able to learn
and gather a lot of lessons learned. One example is that the current
thermo models for the lunar surface do not cover you whenever
you land next to a crater. We found that and we also found some
lessons learned on the ground that we needed to have different and detailed
approaches for looking at data real time versus doing a data analysis long-term
for all the data we collected on the surface. And we plan to implement these lessons
learned on our upcoming missions. We have Blue Ghost Mission
2 and Blue Ghost Mission 3. And then I just wanted to say that having
the chance to be the flight director, specifically also the
descent flight director, was an opportunity of a lifetime. I think Blue Ghost Mission 1 is a true
example of how you can chase your dreams, you can keep working hard,
and if you persevere, then you can achieve great things. And I just want to say
to all the people here, using the great tools that Grafana
makes available, keep on building, keep on dreaming, and then maybe
this might help you land on the moon. Thank you very much.

