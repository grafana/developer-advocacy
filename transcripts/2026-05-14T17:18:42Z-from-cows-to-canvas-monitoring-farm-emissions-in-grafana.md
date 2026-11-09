# From Cows to Canvas: Monitoring Farm Emissions in Grafana

Published on 2026-05-14T17:18:42Z

## Description

Sunil Gopalakrishna, a researcher at Germany's Thünen Institute of Agriculture Technology, uses Grafana to monitor real-time ...

URL: https://www.youtube.com/watch?v=UZJ2NqGBf5g

## Summary

The talk titled "From Cows to Canvas: Monitoring Farm Emissions in Grafana" was presented by Sunil Gopalakrishna, a researcher at Germany's Thünen Institute of Agriculture Technology, on May 14, 2026. Gopalakrishna discussed the use of Grafana in monitoring emissions from partially ventilated barns housing livestock, utilizing a sensor array to measure ammonia, carbon dioxide, and particulate matter. He highlighted the integration of InfluxDB for data storage and the creation of a Grafana dashboard that visualizes emissions data, enabling better analysis and understanding of environmental impacts. Key takeaways included the effectiveness of open-source tools like Grafana for real-time monitoring and the importance of community support in enhancing project outcomes.

Topics: Grafana, InfluxDB, emissions monitoring, open source, sensor technology

## Chapters

00:00:00 Using Grafana to monitor emissions from barns
00:02:22 Monitoring ammonia and carbon dioxide emissions in barns
00:03:55 Using Grafana Canvas for monitoring farm emissions

- Hi, good evening. My name is Sunil Gopalakrishna. I work as a researcher at the Thünen Institute of Agriculture Technology in Braunschweig, Germany. I'm going to talk about how I'm using Grafana for this particular use case where we have sensors built into barns, hence the title, **From Cows to Canvas Panels**.

We have traditionally closed barns. These barns house animals, which could be cows, pigs, or hens. Over the last decade, we have changed this build to a partially ventilated barn. This means we have bay areas where you can see pigs come out of these barns to get some fresh air, do their business, and get some sun before going back in. 

However, it becomes very difficult to measure emissions in barns with these bay areas. When trying to measure emissions in this region, factors such as wind and the presence or absence of animals make it quite challenging. I work on a project that aims to measure emissions from such barns, and we developed a Sensor Array Measuring Ball. It consists of four low-cost sensors that measure ammonia, carbon dioxide, particulate matter, and differential pressure.

When we collect data from these sensors, we wire each of these sensor balls together and send the data to telecommunication towers via LTE. We try to place them at the interface of these barns, and they are all interconnected. There is also the possibility to scale these balls up; for example, we could deploy 50 balls to measure emissions. 

Once we have these sensor values, we attempt to send them using Wi-Fi. However, this is not always feasible due to some locations lacking connectivity. Therefore, we use LTE. The data we collect looks like this: it is a hundred kilobyte file consisting of time-indexed data. From left to right, you can see time and values for particulate matter, carbon dioxide, and ammonia. This data is crucial for us as we are trying to quantify the emissions from these barns.

Currently, we are conducting campaign measurements, which means we have measurements happening between seasons. I decided to use an open-source solution, InfluxDB. In this scenario, I have a few buckets from which I can retrieve data from each of these spheres and plot them against time.

However, some engineers and technicians pointed out that this setup wasn't very helpful for them. After considering their feedback, I decided to use Grafana and created a dashboard. From top to bottom, I specified the type of barn, the number of spheres in these barns, and the concentration of emissions over time. I utilized the Canvas panel to create a layout of the barn and the spheres within it.

At the top of the dashboard, you can see data from each of these spheres in terms of emissions. Additionally, I can check and relate humidity or other factors from the spheres. I also included videos from different barns installed by our partners. If you look closely, you can see that our spheres are also being installed across these barns, which helps us correlate spikes in emissions.

We have annotations on each of these emission values to indicate the period of measurement, such as the growth or fattening period, or if there was an anomaly due to the addition of two or three pigs or cows to the barn. I also created a data completeness metric, which is particularly useful when it's live, as it allows us to see how much data was received in an hour. If the data flow decreases, we can quickly identify that there may be an issue with the sensors or the server.

In conclusion, it is indeed possible to use an open-source tool like Grafana for this use case. We pull data from the spheres, calculate the velocity using partial differences, and send it to InfluxDB. Ultimately, this results in a dashboard. I used the Canvas panel, and I would appreciate a few more additional features in it. I had great discussions with some experts here, and I am very thankful to the community for their support on the forums.

I would also like to thank my partners and team members at my institute. With that, thank you so much. (audience applauding)

## Raw YouTube Transcript

- Hi, good evening. My name
is Sunil Golpalakrishna. I work as a researcher at Thünen Institute of Agriculture Technology
in Braunschweig, Germany. I'm gonna talk about how I'm using Grafana for this particular use case where we have sensors built into barns and hence the title, From
Cows to Canvas Panels. We have traditionally closed barns. So barns, housing animals, could be cows, could be pigs, could be hen. And we have changed this build
for the last decade or so. We have now a partially ventilated barn. That means we have bay areas
where you can see pigs, they come out of these
barns, get some fresh air, do their business, get
some sun, go back in. Now it becomes very difficult to measure emissions
when you have such barns which are, or which have these bay areas. What happens here is you try to measure emissions in this region and due to winds, due
to different scenarios of animals being there and not being there, it
becomes pretty difficult. So I work with, in a
project that we are trying to measure such barns or
emissions from such barns and we developed a Sensor
Array Measuring Ball. It consists of four
sensors, low cost sensors, measure ammonia, carbon
dioxide, particulate matter, and partial, sorry, differential pressure. And when we're doing this, we get this data from these sensors and we wire each of these sensor balls with each other and send them to telecommunication towers or LTE. And if you look, we try to
place them at the interface of these barns and they're
all wired to each other. And it's also a possibility that we can scale these balls up. So let's say we can do 50 balls and try and measure the emissions. And once we have these sensor values, we try to send them using wifi. We have tried it, but
it's not easily possible because we are in some locations where there's basically no connection. So we use LTE and some of
this data looks like this. And this data in turn, as I would say, a hundred kilobyte file
because of this packages, we have time-indexed data. So basically, from the left
to the right, you see time and particulate matter, carbon
dioxide, ammonia values. And this is important for us
because we are trying to see how much of ammonia emissions, how much of carbon dioxide is emitted from these such barns, right? And once we have this
data, it could gather up and basically create gigabytes of data, which doesn't happen at this point in time because we are doing
campaign measurements, we have measurements
happening between seasons. So I decided to go ahead and use an open source
solution that was InfluxDB. And in this scenario, you
could see I have a few buckets, and from these buckets I
could get the data from each of these spheres and also
plot them against time. So this is what it looks like. But there were some engineers between us. There were some technicians
who realized this doesn't help them so much. So then I thought about it and I decided I would go
ahead and use Grafana. And I created a dashboard. And you can see, from top to
bottom, I specified what kind of barn it was and how many
spheres are we having on these barns and the concentration
with respect to time. And I used the Canvas
panel to actually try and create the layout of the barn and the spheres in the barn. And if you look on the
top, you can see from each of these spheres we have data
in terms of the emissions. And also, I can check
and relate the humidity or other factors from the sphere. And I also have other
inputs like this video or two videos from different
barns from our partners. So they have been installed. And if you look carefully, I don't think it's
installed here, our spheres are also being installed
across these barns. And that also helps us to correlate the spikes
in these emissions. And we also have annotations on each of these emission values so
that we could actually say what period of time we measured,
basically talking about the growth period or the fattening period, or if there was an anomaly
because we have two or three pigs added or
cows added to this barn. And I also created something like the data completeness here. It makes sense if it's live because then you can
actually see in an hour how much data was received. And if it goes down, then we
already know that the sensors or the server itself has an issue. So what I would like to conclude
here is that it is possible to use an open source tool like Grafana for this such a use case. And you can basically see
what's happening here. We pull the data from the spheres, we calculate the velocity
separately using the partial differences, and then
send it to the Influx. And basically, then you have a dashboard. I use the Canvas panel. I'm a bit, I would say I
would like few more additional features in the Canvas panel. I had a great talk with a
few of the experts here. And also, I'm very thankful
to the community here because I was able to go on
the forums and ask questions. I thank you all. Finally, I would like
to thank the partners and the team members in my institute. And with that, thank you so much. (audience applauding)

