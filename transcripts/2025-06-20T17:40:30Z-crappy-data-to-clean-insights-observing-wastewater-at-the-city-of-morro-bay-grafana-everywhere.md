# Crappy Data to Clean Insights | Observing Wastewater at the City of Morro Bay | Grafana Everywhere

Published on 2025-06-20T17:40:30Z

## Description

From aging infrastructure to modern observability: learn how the city of Morro Bay uses Grafana to monitor every aspect of its ...

URL: https://www.youtube.com/watch?v=wucMZ9tb1I0

## Summary

In this video, Grant Chase, an operational technology specialist for the city of Morro Bay, California, discusses his innovative use of Grafana to enhance data visualization for water and wastewater treatment facilities. He explains his journey from managing outdated systems to implementing modern solutions that allow for efficient monitoring and problem-solving. Key points include the transition from basic metrics to comprehensive dashboards that visualize various data points, including sensor readings and laboratory findings. Chase emphasizes the collaborative impact of Grafana on his engineering team, facilitating quick access to vital information. He expresses pride in being recognized by the Grafana community and highlights the platform's flexibility in fostering creativity and innovation in addressing operational needs. Raj, the host, acknowledges Chase's achievements, including his recognition with a Golden Grot award.

That's really amazing stuff, Grant! It's not what we typically see in some of our IT dashboards. You give new meaning to concepts like flow, sinks, payloads, and maybe even logs. 

My name's Grant Chase, and I'm the operational technology specialist at the city of Morro Bay, California. In my role, I manage the control systems—from the hardware that supports the motors, sensors, and pumps to the software that the end user interacts with. We monitor the metrics of the water and wastewater treatment facilities for several reasons:

1. **Process Control**: To ensure that we're treating the water or wastewater appropriately.
2. **Efficiency Insight**: The data allows us to see how efficiently we are running the process itself and helps us catch potential problems with equipment early on. For instance, we can tell if a pump is not running as efficiently as it used to, which is much easier to identify with good visualization tools.

We started using Grafana in 2019. The old wastewater treatment plant, built in 1960, had two critical metrics that my lead worker at the time could pull into a browser. However, I soon realized that the equipment was over 20 years old, and the information was just a snapshot of a poorly designed graph. I told him, "Give me a couple of weeks, and I'll figure out how we can record this better."

I utilized Python and an industrial library for Modbus TCP to pull that data into InfluxDB. Then, I needed a place to visualize it, and Grafana turned out to be the perfect solution. We had our two metrics beautifully visualized in Grafana, which was our first exposure to the platform. It significantly changed our ability to create visualizations, and I began integrating it into our water system on the same instance.

When the old wastewater treatment plant was decommissioned, a new plant was built with modern software integrated into the project. Initially, it seemed that we wouldn't need Grafana since the new platform would provide us with new features. However, it quickly became apparent that the engineers were asking for datasets available in the database but not visualized anywhere. These requests were not part of the scope of work for the contractor building the system, so we had to pivot quickly.

I spun up Grafana for the new wastewater treatment plant and built out a dashboard for every single process area, including all data points. The engineering team was amazed by the accessibility and ease of use of the data that Grafana provided. 

There’s something incredibly gratifying about when an incident occurs and the team says, "Let's check Grafana to find out what happened." They view it as a true resource and a valuable tool for solving problems.

### Grafana Dashboard Overview

Our Grafana dashboard's keystone is the homepage, organized in columns that show the wastewater flow from left to right. Each column represents a specific process area, with navigational buttons allowing deeper entry into that area. Given the numerous metrics, it would be impractical to display them all on a single dashboard while ensuring efficient navigation for the operators. Therefore, the homepage serves as a collection of KPIs for the entire process and acts as a navigational springboard. 

All operators start there and can easily access any other process area. Many times, that’s all they need—just the quick metrics. If you delve deeper into a process, you’ll find graphs for every sensor, pump, or tank level. We even have laboratory data organized into its own dashboards and folders, including videos from our lab's microscope. These videos document microorganisms observed in the basin at specific times. 

The videos are timestamped, and the metadata is updated with tags for each type of microorganism, creating a more complete data model. We gain insight into the processes, sample details, and microorganisms observed at any given time.

That was an amazing overview of what you're doing at the municipal treatment plant. Thank you, and congratulations on your Golden Grot!

Cheers. Thank you, Raj. I am proud to be recognized by the community and by Grafanistas, and I’m excited to share the endless possibilities that Grafana offers. If you have a need and the right creative approach, you can solve it with Grafana because it’s an open platform. 

Again, the Big Tent—everything is under there. As a developer, I often feel limited by software, but with Grafana, I have the freedom to innovate and meet the needs of my team. That’s the biggest 'Aha' moment for me, for sure.

## Raw YouTube Transcript

That's really amazing stuff, Grant - not what we typically
see in some of our IT dashboards. You give new meaning to things
like flow and sinks and payloads, and maybe even logs. My name's Grant Chase and I'm
the operational technology
specialist at the city of Morro Bay, California.
At the city of Morro Bay, my role is to manage the
control systems - from the hardware that supports
the motors, sensors, and pumps all the way to the
software that the end user experiences that through. So we monitor the metrics of the water
and wastewater treatment facilities for a number of reasons. One is process control to make
sure that we're treating the water or wastewater
appropriately. Secondly, the data gives us insight
into how efficient we are at actually running the process itself. It allows us to see if there's a problem
with a piece of equipment and we can catch it early because we can tell that
the pump is not running as efficiently as it used to, for instance. And it's really easy to see that if you
have a nice product for visualization. We started using Grafana in 2019. The old wastewater treatment
plant, which was built in 1960, had two metrics that were most important, and my lead worker at
the time told me that he used to be able to pull it into a browser. It turned out that that piece of
equipment was 20 plus years old. So I quickly realized that it was
just a snapshot of a really bad graph, and I told him, 'Give me a couple of weeks and I'll
figure out how we can record this better.' And so I utilized Python and an industrial library for Modbus TCP,
pulled that data into Influx DB, and then I needed a place to see it. And Grafana turned out
to be the answer to that. We had our two metrics and they were
beautifully visualized in Grafana, and that was our first exposure to Grafana
and it really changed our ability to have visualizations. And I
started integrating it then
into our water system on that same instance. The old wastewater treatment plant was
decommissioned and a new plant was built. The new plant had all
of the modern software integrated as part of the build project, and it looked like we were not going to
need Grafana because this platform was going to provide new things for us. And it quickly became apparent
that the engineers were asking for data sets that were available in
the database but not visualized anywhere, and they weren't part of the scope of
work for that particular contractor building the system. So we
needed to quickly pivot, and I already had in my tool bag something
that I knew would work well and that was Grafana. I spun up Grafana for the new wastewater
treatment plant and built out a dashboard for every single
process area with every single piece of data.
The engineering team was floored that there was a platform that made
data that accessible and that easy for them. There's something so gratifying
about when an incident happens, the team goes, 'Let's go check Grafana and find out what
happened,' because they view that as a true resource, as a true tool
to help solve problems. Yeah, so our Grafana dashboard, the keystone of it is the homepage. The homepage is organized in columns
with the wastewater flowing from left to right. Each column
represents a process area, and below that are navigational
buttons that will let you enter deeper into that particular process area.
Because there's so many metrics, it would be impossible to display
them on a single dashboard and have the operators be able
to navigate it efficiently. So this home dashboard is a
collection of KPIs for the entire process as well as a
navigational springboard. So all operators start there and they can
get to any other process area from there. Many times that's all they need
is just to see those quick metrics. If you click deeper into a process, you'll see graphs on every single
sensor and every single pump or tank level. We even have the laboratory data broken out into their own dashboards
and their own folders, as well as videos from our lab's
microscope where we collect data for the treatment facility based on microorganisms that were
observed in the basin at any given time. Videos are taken and then
the metadata can be updated, tags will be updated for
each type of microorganism, and that gives us a timestamp of the
occurrence of that particular bug. And that really creates a complete
or more complete data model for us. We know what the process
is, what the samples were like, and what microorganisms were
observed at a given period of time. That was an amazing view of what you're
up to at the municipal treatment plant. Thanks so much and congratulations
on your Golden Grot. Cheers. Thank you, Raj. I am proud to
be recognized by the community, to be recognized by Grafanistas and to share the endless possibilities that Grafana has built in. If you have a need and you
have the right creative approach to it, you can solve it with Grafana because
it's an open enough platform. Again, the Big Tent - it's all under there. I am not limited by the
software when, as a developer, I am constantly limited by software. Having one that allows me to continue to innovate and to serve the
needs of my team is the biggest 'Aha' moment for sure.

