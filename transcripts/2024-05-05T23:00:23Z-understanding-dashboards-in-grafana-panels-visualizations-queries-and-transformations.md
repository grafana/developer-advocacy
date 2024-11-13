# Understanding Dashboards in Grafana | Panels, Visualizations, Queries, and Transformations

Gain a fundamental understanding of what Dashboards are in Grafana and how they can be used to visualise your data to ensure ...

Published on 2024-05-05T23:00:23Z

URL: https://www.youtube.com/watch?v=vTiIkdDwT-0

Transcript: Hi I'm Tom one of the developer Advocates here 
at Grafana labs and in today's video we'll be   taking a look at dashboards in grafana we'll 
dive into what they are how they can be used   to visualize and monitor your data as well as 
discuss the individual components that they're   made of so what is a dashboard well a dashboard 
is a set of panels that allows you to visualize   the various pieces of information about your 
system giving you the ability to monitor   whatever metrics necessary to determine whether 
or not your systems are healthy and Performing   as expected and perhaps more importantly to 
alert you when there are issues you can think   of a grafana dashboard like the dashboard in a 
car there are a number of panels and gauges that   each show you a visual representation of the 
various pieces of information being gathered   by the car sensors these include the current fuel 
level the speed of the vehicle the internal cabin   temperature and more it's also where you'll 
be warned of any issues the vehicle might   have via warning lights which indicate that 
there's something that needs your attention   all of this information is gathered by the various 
sensors inside the vehicle and then visualized on   the dashboard to give you an at-a-glance glance 
picture of the current status of your car just   like with dashboards in a car grafana dashboards 
allow you to take the metrics logs and traces from   your various systems and visualize them using 
panels to give you an overall picture of the   system's current health and Status unlike the 
dashboard in a car however grafana dashboards   typically make use of Time series data to allow 
you to visualize information about your systems   over time this helps you identify changes such 
as whether or not there may be a spike in CPU   usage in the last hour or if there's a rise 
in error messages being generated within your   application we said that a grafana dashboard is 
made up of a set of panels so let's take a look   at the individual components that make up a panel 
first of all is the visualization itself grafana   offers a wide variety of ways to visualize your 
data including things like time series graphs   heat Maps histograms gauges data grids and more 
you can think of this like the speedometer in the   car it's the visual component that portrays 
a particular piece of information next is   the data source that will be used to power the 
visualization grafana currently supports around   150 different data sources as part of our big 
tent philosophy which includes everything from   simple csvs to time series databases such as 
Prometheus once the data source has been chosen   the next component is the query this is where you 
decide what data you'd like to visualize from your   data source for example you may want to grab 
the average response time of HTTP requests for   your web application from Prometheus or perhaps 
retrieve a list of all error logs for your backend   API from Loki each panel can have multiple queries 
which allows you to represent different pieces of   information within the same visualization such as 
the response times for different endpoints in your   web application finally there are transformations 
this is where you can take the data retrieved by   your queries and transform it into in some way for 
example You may wish to filter particular values   or properties from the results or you might want 
to aggregate the data in some way grafana offers   a large number of built-in transformations to 
suit a wide variety of use cases allowing you   to represent your data in a way that works for you 
let's imagine that you have a server and you want   to monitor the current CPU load to ensure it's 
not running into any issues in this instance you   may choose to create a panel with a Time series 
visualization that uses a Time series database   as a data source such as Prometheus you can 
then write a query that will be used to extract   information about the cpu's load over time so 
that it can be visualized as a graph within your   dashboard you can give the panel a title specify 
that the units are percentages set the minimum   and maximum values of 0 and 100 respectively so 
that you'll always see the values relative to 100%   usage on the graph this panel can then further be 
enhanced by adding a threshold that will visually   indicate when the CPU load is running a little too 
hot for example when it's above 80% this threshold   can be visualized on the graph in a number of ways 
for example there's a red area with a dash line so   that it's clear when the CPU breaches this value 
though not strictly part of the dashboard itself   you can also configure grafana to send you an 
alert when the CPU usage has crossed your defined   threshold for a sustained period of time allowing 
you to be alerted when there's something that may   need your attention just like the warning 
lights on our car's dashboard you can also   add annotations to panels to indicate events that 
may have occurred these annotations can come from   a variety of sources dynamically or can be added 
manually by clicking on the graph for example You   may wish to indicate that at a certain time the 
server was restarted once you've created a panel   to monitor your CPU load you'll likely want to 
add ones for visualizing other pieces of data   about your system such as memory and dis space 
utilization server up time application logs and   more the sky really is the limit dashboards 
are at the heart of grafana and while there   are many more powerful features that I haven't 
covered here hopefully this video helps you to   understand the fundamentals and how dashboards 
within grafana can be used to monitor your systems   to ensure they remain healthy and operational if 
you're looking for some inspiration and want to   see what other members of the community are doing 
with grafana dashboards I encourage you to check   out the golden grot awards where each year members 
of the grafana community submit their amazing   dashboard creations and a panel of Judges selects 
the very best ones to be showcased at GrafanaCON   if you found this video useful remember to give 
it a like and if you have any questions please   let us know down in the comments below don't 
forget to subscribe stay up to date with all   things grafana and with that said I hope you have 
an awesome day and I'll see you in the next one [Music]

