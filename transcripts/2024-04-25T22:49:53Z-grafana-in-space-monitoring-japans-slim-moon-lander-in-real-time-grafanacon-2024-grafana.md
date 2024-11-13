# Grafana in Space: Monitoring Japan&#39;s SLIM Moon Lander in Real Time | GrafanaCON 2024 | Grafana

On January 19, 2024, Japan became the fifth country to land on the moon – and Grafana was there! In this session, JAXA ...

Published on 2024-04-25T22:49:53Z

URL: https://www.youtube.com/watch?v=CpHQfwFPvw8

Transcript: Hi, I'm Satoshi Nakahira from
JAXA. I'm glad to be here.Thank you very much for inviting me. So I'm gonna talk about Grafana's
use case in space in Japanese moonlander, SLIM, on behalf of these guys. So this is the agenda of
the talk and I'm gonna talk about me, about my institution, and the overview of the mission. And then we'll talk on the implementation of SLIM and
our requirement for the "Quick-Look (QL) System" and system overview and examples of
dashboards we have created. So first about me, I'm working on science satellite
operation unit and data archive unit of ISAS/JAXA. And I was originally majoring in
astrophysics for 10 years, but then my focus moved
to engineering science. I'm involved in open data
archive of space science, observational data.
This is my site, DARTS. And I'm also involved in
operational systems of space science probes or satellites. So then to my institution - JAXA is the space agency of Japan
and ISAS is the division of JAXA on space science. And
as you can see in this photo, we have been operating many various
types of satellites or probes. So let's take a look. This is a solar image by
HINODE, the solar telescope. This is Akatsuki's orbital
image and then this movie is from Kaguya: moon orbiter and this is an asteroid
named [inaudible] by Hayabusa2 probe. And smaller images, microscopic image of samples
that Hayabusa2 brought back to us. And this X-ray
Spectrum is taken by XRISM with the same vehicle with SLIM. So you can see the mission lift room here. And then I introduce the mission of SLIM. SLIM is dedicated to demonstrate
high-precision lunar landing technology and its goal is to achieve a pinpoint landing
with 100 meters accuracy and it'll be achieved through image matching
navigation and autonomous navigation guidelines control. And
this figure shows three smooth craters and matches it to with preloaded image. And this process is repeated
and then leads to the landing point. The landing point
is named Crater Shioli and another picture of
SLIM. It's light weight. So weight of the SLIM
body is only 200 kilograms and 500 kilograms of propellant. So let's move to the actual data of SLIM. And in this figure, the center is Earth and the
white circle is the moon orbit and yellow line is actual
trajectory of SLIM. So SLIM launched on
September 7th and this is the movie of the launch. So SLIM stayed around us for a while and then left us and
set off to the moon on October 1st. So then SLIM executed moon swing-by on October 4th and then reached to its farthest point of three
times as far as the moon and then go back to moon
on Christmas of last year. And this movie is taken at that
time, so the crater is very clear so because it is approached. And then SLIM remained
in orbit for one month then attempted its moon landing. So as you may know, SLIM's moon landing was successful. So I'll
share highlights of SLIM. So just before landing, SLIM released two robots
named Lev-one and Lev-two. And soft landing was successful. It's the first in Japan and then pinpoint landing within 100 meter
accuracy was also successful. It was first in the world. And then as seen in this photo, a
selfie is taken by robot Lev-two and unexpectedly survived two
extreme temperature shifts from night to day. Among
these temperatures, Slim woke up two times at this date. So let's move to how Grafana
is used in SLIM operations. So we are still using these
quick look systems and there are some problems.
So as seen in the photo, there are many characters. So it is not easy to find
certain parameters from here and this software is viewed
as a monolithic software. So it is not easy to
maintain or add in new features. So then how is the telemetry of space scientific probes? So we have two types of data.
One is housekeeping data, the other is scientific data. So, scientific data includes image, event by event data, spectra, but usually analyze in a longer timescale. So not time critical. So we do not include this in
realtime monitoring purposes. On the other hand, housekeeping data is used to monitor the health and functionality
status. So it includes voltage, current, temperature,
attitude, position, velocity, acceleration, status flags, and counts. So it's basic metrics so
similar to what you find in IoT devices. So any other difference
between IoT and the probe data? SoIoT data - we collect a
small amount of telemetry from many devices. In probes, we collect large number
telemetry from one big device. So general, but content of data is still similar. So as a result, inspired by IoTs we have
integrated Grafana to space probe's operations for enhanced
observability. This is System Configuration that we have integrated
Grafana and our control center receives SLIM data through
ground antenna station. And so we adopt InfluxDB as
a data source for Grafana and we also use API to get a calculation for our image generation. And in front of InfluxDB we
built a data receive/register module. It is written in
Python. For data register, we of course, use the InfluxDB client. And for data received, we use the C libs for communication protocol
handling or binary decoder. It is wrapped with Python.
So in this project, "red text" is newly written and "other"
is open source or reused software. So we have successfully built
this system with very low effort. And we also configured in loosely coupled architecture based on REST API. And this will be inside of the Control Room,
just a moment before the moon landing. So there are many people, many displays Grafana based system is used here and here. And this screen is streamed
in real-time on YouTube. So in this critical phase, the Control Room and the
YouTube audience were all looking at the same Grafana
dashboard at the same time. So then I show you the
example SLIM dashboards. We have built over 10 dashboards and constructed for each subsystem - like some are power navigation and for each phase, launch, running or cruise. And as you see in the previous movie Classic Quick-Look was still dominant but Grafana-based
system has played an important role in our operation. So this is the dashboard for the
navigation system during the cruise phase. We can easily build this system by connecting
InfluxDB with Grafana, and in this area we monitor system status and in this area we
monitor error or warning status. And in this area, we monitor log messages that are
generated by ground processing. We use the stats or logs
panel here and  right area we monitor using
x-y plot or time series graph, we monitor attitude or
atmospheric change or solar angle. And next dashboard is for heater status. Heater is important because
instruments can be damaged by extremely low temperature in space. So this dashboard is 
and several pages of information below. In this area, we monitor
power-related metrics. For example, power
generation, power usage. And this second graph provides a
clear view for total power consumption for each component is stacked graph. So SLIM has 50 heaters. And so it is
controlled autonomously, but it is important to
monitor its duty cycle. It it was easy with this
state timeline panel so we can compare it with temperature shown from the left side. So this dashboard is for thrusters
and the maneuvers monitor and used in attitude
change or orbital change. So SLIM has two main big
thrusters and 12 smaller thrusters. So it is arranged to
reflect its physical layout. So with this layout we can
easily check the status and with this gauge we saw the remaining fuel of SLIM's thrusters and we also check the remaining battery here. And this 3D is used to monitor
its attitude in relation of Sun and Earth and it is implemented by Python API and images are generated by offline
rendering by using trimesh or pyrender  and generated images passed to Grafana . So the dashboard that uses the variable feature of
Grafana is very efficient for us. This movie shows a demo. So we set string to current CUR
current and check parameter. Parameter is shown. So change parameter and query variables. So how it is set up, we used the two variables.
One is text box, the other is query. So we used textbox as a filtering strings
and the second query is variable. We wrote this command of InfluxDB and as a result we obtained this
list of filters same three names. So this is the rest of list of
will change three name and if we check here we can
show the multiple graphs with the repeat option of Grafana. So then finally, I show you recorded movie
drawing the moon landing. This dashboard is almost the
same as the previous one but this figure is new. So horizontal axis is distance and but vertical axis is
attitude and flight line is actual planned trajectory of SLIM. And red line is actual trajectory
of the last five minutes. So then start. Now it's reached full phase and then thrusters are
firing in full power. You can see fuel is decreasing rapidly and then current velocity
is almost neutralized. And start vertical descending. So this is our final phase
seeing it seems to be just above running point at attitude
of six kilometer, then it starts going down three kilometers, and one kilometer bearing at 500 meters. And then  again. So arrive to Moon and this number shows the time stamp of SLIM. So this is moving. So where we see this is changing, we believed that SLIM has arrived and
the moon soft landing was successful. So let me conclude with our impression to Grafana. So we are able to build our
entire system quite easily and the visualization capability
was broad from simple to detailed graphs. We are also able to create dashboard
that were well-received and visually impressive. And for me, editing was straightforward
and could be done even during operations. The variable future was game
changer for us and extremely convenient. And being able to call
Python from the API means we could do everything. So to summarize, we are glad to use Grafana. Yeah, once more. Thank you very
much for the Grafana community. Let's go to the next planet
with JAXA! Thank you.

