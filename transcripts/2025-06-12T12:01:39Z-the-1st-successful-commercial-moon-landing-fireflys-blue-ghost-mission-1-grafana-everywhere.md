# The 1st Successful Commercial Moon Landing | Firefly&#39;s Blue Ghost Mission 1 | Grafana Everywhere

Published on 2025-06-12T12:01:39Z

## Description

Firefly's Blue Ghost Mission One successfully landed on the moon with the help of Grafana. In this behind-the-scenes talk, learn ...

URL: https://www.youtube.com/watch?v=seaOb7ub19E

## Summary

In this video, Jesus Charles, who has been with Firefly Aerospace for over five years, discusses the successful Blue Ghost Mission One, which marked the company's first fully commercial lunar landing on March 2nd. He describes his role in leading the architecture for the ground system that tracked and communicated mission data during the autonomous descent. The video highlights the critical dashboards created using Grafana, which provided real-time data visualization, allowing operators to monitor the landing process and ensure mission success. Charles emphasizes the importance of having clear metrics and data accessibility for decision-making and expresses excitement about future missions and the integration of Git for dashboard management. He encourages viewers to continue innovating with Grafana tools, as they contribute to advancements in space exploration.

# Transcript Cleanup

Hello, my name is **Jesus Charles**, and I have been at **Firefly Aerospace** for a little bit more than five years. Firefly Aerospace is an end-to-end space transportation provider, meaning that we make access to space reliable and economical. 

On **March 2nd** of this year, we achieved the first fully commercial lunar landing. My work on **Blue Ghost Mission One** involved leading the architecture for the ground system we needed to execute the mission. This included everything from how we ingested data, visualized it, and communicated all that information to our operators and customers.

During our final moments as we descended onto the lunar surface, everyone was laser-focused. You could hear a pin drop in the control room; we were all glued to our screens because the descent was fully automatic. The lander was doing its job, and all we could do was track the data. 

As we touched down, our chief engineer gave the green light that we had successfully landed on the moon. I couldn't believe it! I kept looking at the screen, celebrating and hugging people while still glued to the display. It was an unreal experience.

We chose **Grafana** because it provided us with speed, flexibility, and clarity. It allowed us to build dashboards quickly, getting the necessary data in front of us. Additionally, it enabled us to evolve those dashboards as our mission progressed and share data between all the different consoles. We could borrow panels from another system to create a better dashboard.

### Descent Dashboard

First on the screen is one of our descent dashboards. We needed to track numerous metrics as we approached the lunar surface. In the panel, you can see how we monitored altitude versus the distance to our landing site. The two panels on the right gave us confidence that we had landed and were stable. 

This dashboard maps the acceleration of the lander in terms of lunar gravity on the vertical axis. As we descended, we experienced gravity variations. When we touched down, we knew the gravity reading needed to match lunar surface gravity, which is one.

We also had our landing sensor panel, connected to four sensors on the footpads of the lander. When the lander touched down, those footpads would align, move, and rotate, triggering the sensors. This provided a clear indication that we were on the lunar surface.

### Surface Dashboards

I have a couple of surface dashboards that we used on our video wall to keep all operators informed. On the left, you can see we tracked the state of each of the payloads. We had **10 payloads** on this mission, each with multiple components, so we needed a clear way to confirm if they were powered on or off. 

We also monitored our fly jet sequence tracker, which indicated the sequences we used onboard the lander to know what operations were ongoing. Here, we can see a few of the sequences running at that moment, along with other information like states for the vision navigation system and floodlights.

Here's another surface dashboard showing our mission phase, which was descent, and the specific mode as **descent critical**. This mode has specific implications for our mission, indicating that the lander is focused on executing its descent sequence. We also tracked the time, communication mode for our antennas, and the solar array states.

Now, on the screen is a dashboard for the flight directors. This dashboard contains a lot of information at a high level, allowing us to gauge how the system was performing without drilling down into specifics. We can see our mission phase, mission mode, and the **ADCS mode**, which indicates how the lander was behaving as it descended.

### Future Missions

Having used Grafana for **Mission One** gives us confidence for **Blue Ghost Mission Two**, **Blue Ghost Mission Three**, and other **Elytra missions** coming up. It provides us with a baseline we can pull from, rather than starting from scratch like during our first mission.

I'm excited about learning more about the integration with **Git**. One of the main topics we discussed during our mission was controlling the dashboards. We want to avoid having dashboards that constantly change, missing critical information. I believe that integrating with Git will be ideal for configuration management.

Grafana contributed to the success of **Blue Ghost Mission One** by making data available, allowing us to make quick decisions. It provided all the information in a single, clear, and concise manner.

To everyone using the great tools that Grafana offers, keep on building, keep on dreaming, and maybe someday this might help you land on the moon. Thank you very much!

## Raw YouTube Transcript

Hello, my name is Jesus Charles and I have been
at Firefly Aerospace for a little bit more than five years. Firefly Aerospace is an end-to-end
space transportation provider, meaning that we make access to
space reliable and economical. In March 2nd of this year, we were the
first fully commercial lunar landing. Yeah, my work on Blue Ghost Mission
One really consisted of leading the architecture for the ground system
that we needed to execute the mission - everything for how we
were going to ingest data, for how we were going to visualize it, and how we were going to communicate
all that to our operators and to our customers. During our final moments, as we were descending
onto the lunar surface, I think everyone was laser focused. You could hear a pin
drop in the control room, so we were all glued to our screens
because the descent was fully automatic, so the lander was doing its job, and all we could do was track the data.
So as we landed and we touched down, our chief engineer basically gave the
green light that we were successfully on the moon. I couldn't believe it. I just kept looking at the screen
and celebrating and hugging people, but I kept looking at the screen.
It was an unreal experience. We selected Grafana because it
provided us with speed, flexibility, and clarity. It allowed us to build dashboards fast
so we could get the data in front of us. It allowed us to evolve those dashboards
as our mission was progressing, and it also allowed us to share data
between all the different consoles. We could borrow panels from another
system and make a better dashboard. So first on the screen, this is
one of our descent dashboards. Basically, we needed to keep track of
a lot of metrics as we were
coming down to the lunar surface. Here in this panel, you can see how we're
tracking the altitude versus
the distance to our landing site, and then we have another panel. These
two panels on the right really allowed us to have confidence that we had landed
and touched down on the surface and that we were stable. This dashboard
maps, in terms of lunar gravity, the acceleration on the
vertical axis of the lander. So as we descended, we have these gravity variations, right? And then as we touch down on the
surface, we knew it needed to go to one, so the gravity that would be matching
the lunar surface gravity. Also, we have our landing sensor panel. This was hooked up to four sensors
on the footpads of the lander, and they were hooked up so that when
the lander touched down on the lunar surface, those foot pads will
align and move and rotate, and then they would trigger the sensors. So we had a clear indication that
we were touched down on the surface. I have a couple of surface dashboards.
These are most of the dashboards that we use on our video wall to give
all the operators awareness. Here, you can see on the left, we are tracking
the state of each of the payloads. We had 10 payloads on this mission, and
each of them had multiple components, so we needed a clear way to see if
they were powered on or powered off. We also have our fly jet sequence tracker. This is the sequences that we used
onboard the lander to know what operations were ongoing at the time. Here we can see a few of the sequences
that we're running at that moment, and then along other information we
have like states for vision navigation system and floodlights and
some of the other components. Here's another one of the
surface dashboards. It's showing, in the timeframe that I have selected,
it's showing our mission phase, which is descent, and then the
specific mode is descent critical, which has very specific
meanings for our mission, but basically it's - the lander is
focused on doing its descent sequence. And then we have other data here such as
the time that the lander is tracking, the communication mode that
we have for our antennas, and along with the solar array states. Here now on the screen is
one of the dashboards for the flight directors. So this
has a lot of information, but at a high level so that we could
get a sense of how the system is doing without having to drill down
into any specific area. Again, we can see our mission
phase, our mission mode, and then this ADCS mode is
basically what the lander, how it's behaving, while it's going down
to the surface. We had different modes, for example, when it was moving into the vector
to do a maneuver into the orientation or into pointing to the earth for
our S-Band communication system. So really the goal of this dashboard
is to show us and give us a quick overlook into key things that we
needed during the mission. Having used Grafana for our mission one makes us
feel really comfortable about our Blue Ghost Mission Two, Blue
Ghost Mission Three, and the other Elytra missions
that we have coming up. Now, it gives us a baseline that we can pull
from versus having to start from scratch like during our first mission. I'm really excited about learning more
about the integration with Git because one of the main topics that we discussed
during our mission was the control of the dashboards. You don't want to have dashboards that
could be constantly changing and then not have the critical
information that you need. So I think having that integration with
Git will be perfect for configuration management. Grafana contributed to
the success of Blue Ghost Mission One, by making the data available, it allowed us to make quick decisions
and basically gave us all the information in a single, clear, concise manner. And I just want to say to all the people
here using the great tools that Grafana makes available, keep on
building, keep on dreaming, and then some time maybe this
might help you land on the moon. Thank you very much.

