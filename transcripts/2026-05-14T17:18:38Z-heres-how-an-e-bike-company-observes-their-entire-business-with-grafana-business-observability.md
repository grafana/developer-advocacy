# Here&#39;s How an E-bike Company Observes Their Entire Business with Grafana | Business Observability

Published on 2026-05-14T17:18:38Z

## Description

Drive Terra built a Grafana platform that gives every role in their e-bike business — from on-call battery operators in Dubai's heat ...

URL: https://www.youtube.com/watch?v=MlESgnRzNvc

## Summary

The show titled "Here's How an E-bike Company Observes Their Entire Business with Grafana | Business Observability" was published on May 14, 2026. The speaker, who shared insights from Drive Terra, discussed how the company utilizes Grafana to monitor various aspects of their e-bike business, including battery health, fleet status, and operational KPIs. Key takeaways included the importance of observability for all roles within the company, not just technical teams, and the effectiveness of Grafana in providing real-time data visualization and alerts. The speaker emphasized starting with specific use cases and iterating based on team feedback to build effective dashboards for both technical and non-technical users.

Topics: Grafana, Business Observability, E-bike Monitoring, Data Visualization, Real-time Alerts

## Chapters

00:00:00 Overview of Drive Terra's operational structure and monitoring needs
00:03:08 Observability for the entire company with Grafana
00:05:32 Using Grafana for business observability in e-bike operations

I assume everyone here has experienced a moment when someone from the product team, the CEO, or the business came to them and said, "We need to monitor our processes. We need to monitor our data." If you work in a software company, you know that engineering consists of software engineers and SREs, but we all know what they are. 

At Drive Terra, we have five components: a battery station, bikes, batteries, the cloud, and a mobile app, along with a lot of operations happening on the ground. When a driver arrives at a station, they simply need to swap a battery instead of charging it. To ensure everything runs smoothly, we have several teams working together. 

The first team consists of our engineers, including software engineers, IoT engineers, and hardware engineers who work on firmware, connectivity, devices, and the entire IoT ecosystem. We also have electrical engineers focused on battery cells and charge cycles, as well as mechanical engineers who handle everything related to the bikes, such as faults, gears, and steering wheels.

The second team is operations, which includes fleet managers ensuring that the fleet is always running. We have a logistics coordinator managing all station activities, battery charging, and a maintenance team that tracks down bikes needing repairs. Additionally, we have a warehouse and inventory team working under operations.

Moving on to leadership, starting with the CEO, who constantly asks for visibility, we have the partners manager who needs to monitor bikes operating under specific partners, such as Amazon, Kareem, and Uber. The finance team also needs to understand their KPIs. Lastly, the partners themselves need to see the drivers operating on the ground.

The challenge lies between the non-technical and technical teams. Our non-technical team needs to see operational costs and KPIs without relying on WhatsApp or other informal systems. Leadership wants weekly reports, and previously, they used Excel. The new approach, which you'll see later, is much more efficient.

Whenever a partner calls us to inquire about the bikes or a specific driver, our software engineers can track the IoT data, servers, and electrical wiring within the bikes. From my experience, I can say that observability is not just for engineers; it's for the entire company. 

We utilized Grafana for this purpose. When we presented our dashboard to local communities in Dubai, Lebanon, and the Middle East, the initial reaction was, "You are crazy to do this." However, once I showed them the dashboard, they realized, "Wait, it's not crazy; it's doable." With the right infrastructure, database, and data pipeline, you can monitor the bikes live. The dashboard auto-refreshes every 30 seconds, every five seconds, or even every second, depending on your configuration. 

You can keep track of all faults, enabling everyone to understand how the hardware is performing. This is a full digital twin right there in Grafana. You can monitor battery levels; each bike has two batteries, and you can see them directly. At the bottom, you can observe the lifecycle of how a battery moves from a bike to a station and back again.

Speaking more technically, each bike has an IoT box that updates GPS every ten seconds. It includes voltage, short cycle data, fault codes, and motor data. Once we receive this data from the device, we need to process it. One of the cool features that Grafana offers out of the box is alerts. Imagine Grafana reading our data every five seconds; alerts can come directly from Grafana. 

Just as we have an on-call software engineer, we also have an on-call battery operator or station operator to monitor the lithium batteries in Dubai's heat. We take the data from the bike, live stream it to our servers using MQTT, and save it in the cloud with MongoDB for IoT. All metadata and inventory data come from PostgreSQL. All of this data converges in one place for visualization, which is Grafana.

We have numerous dashboards, each with different categories. Battery operators have their own dashboard, and station operators can even use Grafana's camera feature and button feature to control functionalities at the station. These buttons can call an API or endpoint, allowing station operators to manage issues without needing to access our main system. If they see something wrong, they can stop the station or initiate the fire process—all from one place.

What we learned from this journey is that Grafana is not just for engineers; it's for the whole company, from the CEO to every employee. Your team will ask questions, and ultimately, Grafana was the answer for us. We started with one use case—battery health—then moved to fleet status. You can pick any KPI, work on it, show it, gather feedback from the team, and build the right dashboard for the non-technical team. 

For the technical team, you can always find templates to start with, but for the non-technical team, that was the challenging part. Throughout this journey, the non-technical team became our champions. When the CEO or anyone else asks a question, you know the answer. 

Thank you, everyone. Stay fully charged! (audience clapping)

## Raw YouTube Transcript

- I assume everyone of you, there was one time
someone from the product, the CEO, or from the
business, they came to him and they said, "We need
to monitor our processes. We need to monitor our data." So if you work in a
software company, you know, engineering are the software
engineers we have or the SREs, but we all know what they are. But at Drive Terra, so this is not working. Okay, so what we do at Drive Terra is we have five components. We have a battery of stations,
so a station of batteries. We have a bike and we have the
batteries, we have the cloud, we have the mobile app, and we have a lot of
operation going on the ground. So when a driver come to a station, you just need to swap a
battery and not charge it. So when speaking about this, we have several team
working together to ensure that things are working in a good way. The first are the engineers, and of course they are
our software engineers. We have our IoT and the hardware engineers working on the firmware,
on the connectivity, on the device, on the hardware
and all the IoT ecosystem. You have the electrical engineers working on the cell of the batteries, working on the charge cycle and working. And we have the mechanical engineers working on everything
related to the bike, faults, working on the gears, working on the steering wheel, everything we know about bikes. The second team is operation, which is related to the fleet managers, ensuring that the fleet
is running all the time. We have our logistic coordinator coordinating all the stations
stuff, battery charging, and we have the maintenance team going for chasing every bike if it
goes down for maintenance. And we have have our
warehouse and inventory team working under the operation. And then you move on to the leadership, starting with the CEO, that is always asking for some visibility, moving to the partners
manager where they need to see all the bikes working
under specific partners. Let's say the bikes working for Amazon, the bikes working for Kareem, for Uber, and we have the finance team. They need to understand their KPIs. And last you have the partners
themselves where they need to see the drivers running on the ground. So the problem here is
between the non-technical team and between the technical team. Our non-technical team, they need to see all the operation cost or the operation KPIs. They don't go and wanted
to do the WhatsApp stuff without any system. The leadership want to
see weekly reporting. The old way was they use Excel and the new way is, you'll see later on. So, and every time a partner
call us to ask what's happening with the bikes, what's
happening with a certain driver and why his bike is going down. On the other way, the way we know, are the software engineers, the engineers, they can track the IoT,
they can track the servers, and they can track from
an electrical perspective all the electrical wiring
inside the bike itself. So here I can say that
after my experience, observability is not
just for the engineers, it's for the whole company. So what we did is we used
the Grafana for this. The local communities in Dubai and Lebanon and the Middle East, the first word outta their mouths was, "You are crazy to do this." And then when I show them this dashboard, it's like "Wait, it's
not crazy, it's doable." If you have the right infrastructure, if you have the right database, and the right data pipeline, you can monitor the bike live the dashboard auto
refresh every 30 second, every five second, every one second. You can configure it the way you want. You can keep track of all the faults. I can use the laser here, fault
by fault by fault by fault, enabling everyone to understand how the hardware is performing. This is a full digital twin
right there in Grafana. You can monitor the battery levels. We have two battery in each bike, so you can see them directly. And here at in the bottom
you can see the lifecycle on how the battery goes
in a bike to a station, to another bike, to another station, to another bike, to another station. So speaking a little bit more technical, I'll take the bike as example. We have an IoT box in every bike, GPS update every ten second. It includes the voltage, just
short cycle, the fault codes, and the motor data. Once you receive this
data from the device, you need to process it. One of the cool things that
the Grafana has out of the box are the alerts. So just imagine that if
Grafana is reading our data every five second, the alerts can come directly from Grafana. The same way we have an
on-call software engineer, we have an on-call battery operator or station operator just
to be able to monitor the lithium batteries in Dubai heat. So we take the data from the bike, we move down to, we live
stream it to our servers, using MQTT and then it's
getting saved in the cloud using MongoDB for IoT. And we have all the
metadata, the inventory data, coming from PostgreSQL itself. All of those end up together
PostgreSQL, MongoDB, RabbitMEQ in one place to
visualize it, which is Grafana. So we have a lot of dashboards. Every five to six dashboards, they have a different category. The battery operators
have their own dashboard. The station, they can even
use, we use the Grafana. There is a camera feature, button feature, to control some
functionality on the station. So those buttons that they
can call an API or endpoint and the station operator,
they don't need even to go to our main system from Grafana. If they see something wrong,
they can stop the station or they can start the fire process. They can do everything from one place. What we learned from this
journey is that Grafana is not just for engineers,
it's for the whole company, from the CEO to every and
each one of our employees. Your team will ask questions and eventually Grafana
was the answer for us. The way we started, we
started with one use case, the battery health, then we
move to the fleet status. Then you can pick up any single KPI, work on it, show it, gather
the feedback from the team, and then build the right dashboard for the non-technical team. I mean, for the technical
team, you can always go and find some templates,
start with them and kick off, but for the non-technical,
this was the hard part of it. So, in this journey, the non-technical team is your champion. When the CEO or anyone ask
question, you know the answer. Thank you, everyone, stay fully charged. (audience clapping)

