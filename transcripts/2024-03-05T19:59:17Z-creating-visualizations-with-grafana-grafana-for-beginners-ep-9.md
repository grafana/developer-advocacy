# Creating visualizations with Grafana | Grafana for Beginners Ep. 9

Creating visualizations is one of the most effective ways to understand your data. Join Senior Developer Advocate, Lisa Jung to ...

Published on 2024-03-05T19:59:17Z

URL: https://www.youtube.com/watch?v=yNRnLyVntUw

Transcript: Hey! Welcome to Grafana for Beginners. I'm Lisa 
Jung and I'm a developer advocate at Grafana.   In the last episode, we learned about the most 
commonly used visualizations in Grafana. In this   episode, we'll create five of these commonly used 
visualizations and become familiar with creating   visualization panels. This is the dashboard we'll 
be creating today. The dashboard consists of   visualizations of logs, metrics, and traces from 
an e-commerce app. This app has a microservices   architecture and it's running on Kubernetes. In 
episode 7, we covered a brief background about   this app and we explored the data collected from 
this app as well. If you need a refresher, click   on the info card up top to watch this episode. 
When building a dashboard, having a clear idea of   who the audience is helps us determine what data 
we choose to show and how we visualize that data.   In our case, we're building a dashboard for SREs 
who are observing our system. This dashboard will   help them understand the infrastructure the app 
is running in. We'll create visualizations that   keep track of the number of running Kubernetes 
nodes, the amount of CPU activity per node,   the number of containers, the rate, errors, 
and duration metrics for apps on our cluster,   and logs with errors. This is not by any means a 
comprehensive dashboard with all the info that an   SRE might need. The core point of this episode 
is to become familiar with dashboard tools and   create your first visualization panels. So 
we'll be creating the simplest visualizations   that don't involve complex queries or knowledge 
of advanced concepts. Let's start with creating   a dashboard. From the homepage of Grafana 
Cloud or Grafana in your local environment,   expand the menu and click on the "Dashboards" 
option. Click on the "New" button and select   the "New dashboard" option from the drop-down 
menu. Then click on the "Add visualization"   option. It will prompt you to select the source 
of data you want to visualize. The first three   panels show the visualization of metric data 
that helps us understand the infrastructure   the app is running in. These provide information 
regarding nodes and containers. Our metrics data   is stored in a Mimir data source connection 
named grafanacloud-microbslisajung-prom. So   we'll select that. Mimir is like an Enterprise 
grade of Prometheus so it's shown as Prometheus   in Grafana. When you select your data source, 
it'll immediately take you to the panel editor.   This is where you can create and customize 
a visualization panel in a dashboard. Think   of each box here as panels. Each panel contains a 
visualization of factors that you want to observe.   The query section is where you write queries 
to retrieve the data you want to visualize.   The options section is where you can customize how 
you want to visualize that data. The visualization   section displays a visualization you're creating 
in real-time. The first visualization we'll create   is a gauge visualization type. We'll use this to 
show the number of running Kubernetes nodes. The   gauge visualization shows you the numeric value 
of whatever you are observing and where it lies   within the range you specify. These are especially 
useful when you're monitoring something that you   want to stay within a certain range. In this case, 
we're showing how many nodes we have in total and   how many are actually running. Let's go back to 
the panel editor and look at the query section in   order to create a visualization. We first need 
to write a query to retrieve the data we want   to visualize. Before writing a query, make sure 
the correct data source is selected. Earlier,   we selected the Mimir data connection that 
contains metrics data about the nodes. Next,   we'll use the code view to write a query. So 
click on that option this is where we'll enter   a PromQL query that will retrieve the number 
of running Kubernetes nodes. In this series,   we're assuming that you're familiar with the 
query language of your data source and how your   data is structured. So, we'll go over the queries 
at a high level. This is a PromQL query here that   counts the number of nodes in a cluster. It's 
doing that by getting the sum of the nodes in   a cluster. So let's see if this query works by 
running the query here. Now, if you look at the   visualization section, it'll visualize the data 
as a time series line graph by default. it looks   like there are three nodes running in the cluster 
over time but this isn't the visualization type we   want. We want to visualize this as a gauge. 
To customize a visualization, we'll use the   options section here. Up top is a drop-down menu 
with all the visualization types that could be   created within Grafana. From here, we'll select 
the gauge visualization. The visualization type   should update to a gauge with the number 3 in the 
center. This means that there are three nodes that   are currently running in a cluster. Now, if you 
look at the options section on the right, it lists   all the ways in which a gauge visualization could 
be customized. All visualization types in Grafana   could be customized using the options section. 
For time's sake, we won't go over every option   available but I do want you to bookmark this 
documentation here. The link is also included   in the info card up top as well as in the 
description. This documentation lists all the   visualization types you can create with Grafana. 
When you click on the desired visualization, it'll   take you to a page that explains all the options 
you can use to customize that visualization.   So when you're doing this on your own and come 
across an option that's not covered in the series,   you can always use this doc to learn more about 
it. So let's get back to the options section of   the gauge visualization. Before we customize 
anything, it's important to give your panel   a title so the viewers know exactly what they're 
looking at. Under the Title section, we'll give it   the title of "# of running Kubernetes nodes". When 
you click anywhere on the dashboard, you'll see   that the panel title is automatically updated in 
the visualization section. Another thing you may   want to fill out is the description. The chances 
are you're working with multiple team members who   will be observing the system. Not everyone will be 
familiar with all the factors you're observing and   may need more context. This is where you can 
add the context for your teammates. The gauge   visualization type shows you the numeric value 
of whatever you're observing and where it lies   within the range you specify. These are especially 
useful when you're monitoring something that you   want to stay within a certain range. Right now, 
we have the number of nodes running but we have   not specified a range. We're going to do that 
by going to the options section and scrolling   down to the Standard options section. Let's 
say we have four nodes in our cluster. So the   minimum number of nodes we could have is 0 and 
the max is 4. So we'll specify that under the   "Min" and "Max" here. When you do so, you'll see 
the gauge reflect that there are three nodes that   are currently running and that's not the maximum 
number of nodes we have. Let's add more context   here to make this visualization even more helpful. 
We have a side-by-side view of the visualization   we just created and the final visualization we're 
working towards. Our final visualization has a   number of nodes shown whereas the current does 
not. We also see this outer band on the current   visualization but the final one doesn't have 
this. To make these changes, we're going to   scroll up to the Gauge section. We're going to 
toggle on the "Show threshold labels". This will   show the thresholds we set. So far, we have the 
minimum and the maximum value set as thresholds,   so our visualization will reflect that. Next, 
we'll toggle off the "Show threshold markers".   This will get rid of this outer band here which we 
don't need. Let's take a look at the current and   the final panels again. The current one is green 
whereas the final one is yellow. The colors are a   powerful way to alert the viewer whether something 
needs our attention or not. With Grafana,   you can configure thresholds for your panels so if 
whatever you're observing hits a certain threshold   the info is displayed in certain colors. Let's 
apply that to the gauge visualization. Earlier,   we mentioned that we have 4 nodes in 
our cluster. In a hypothetical scenario,   let's say we want all four nodes running for 
optimal performance. If we have 3 running, it's   less than ideal but things still function. But it 
warns us to look at what's going on and decide on   the next steps. If we have 2 or fewer running, 
then things start falling apart. We need someone   on this now and address this right away. To help 
our team members understand this at a glance,   we're going to color-code the thresholds. To make 
that happen, scroll down to the Standard options   section. From there, make sure the color scheme 
is selected for the "From thresholds (by value)"   option. Then scroll down to the Thresholds 
section. You'll see the green dot here with   the word "Base" next to it. This makes the color 
of the gauge green by default. When you click on   the green dot, it'll show you the color menu. 
When you select the "Text color" option here,   it will turn the base color to gray. I like 
using the colors of the traffic lights to signify   whether something needs our attention or not. I 
will use the color green to signify something is   in the optimal range. Yellow when things are not 
at an optimal level and someone should take a look   at what's going on. Red when we're in trouble 
and something must be addressed right away. I'm   going to use the Thresholds section to accomplish 
this. I want the gauge to turn green if we have 4   running nodes. I'm going to change this threshold 
to 4 and change the color to green. In order to do   so, click on the number. You can type any number 
you want. Replace the number 80 with 4, then click   on the red dot to get the popup menu. Then select 
the green color. This tells Grafana to change the   color of the gauge to green if there are 4 nodes 
running. Next, we want to add another threshold.   When the number of running node is three, I want 
the gauge to turn yellow to let someone know to   look into this. So we're going to select the "Add 
threshold" option. Just like we did last time,   we'll type in the number 3 and select the yellow 
color. You'll see that the color of the gauge   immediately turns to yellow as the number of 
running nodes is 3. You'll also see the number   3 reflected on the gauge here. Following the same 
steps, we're going to add the thresholds of 0, 1,   and 2 nodes. If the number of nodes is anywhere 
between 0 to 2, the gauge is going to turn red,   signifying that this must be addressed 
right away. Now that our current and final   panels are identical, we'll save this dashboard. 
You could do that by clicking on the "Save" button   up top. Give the dashboard a descriptive name. 
Under the description, provide some context to   what the dashboard is visualizing. Select the 
folder you wish to save this dashboard in.   Then click on the "Save" button. Then you should 
see the saved dashboard with the panel you just   created. You can adjust the size of the panel by 
holding and dragging the lower right corner of the   panel. You can also move the panel by holding 
and dragging the panel title. All right. Next,   we'll create a time series line graph. The graph 
type was chosen because we want to look at how the   CPU activity of each node changes over time. 
It's great for detecting trends at a glance.   To add another visualization. click on the "Add" 
button and select the "Visualization" option. The   first thing we're going to do is to make sure 
we have the right data source selected. We're   using the same metrics data source we're using for 
the previous panel so we're good to go. To create   this, we'll write a PromQL query to retrieve the 
data we want to visualize. This query calculates   the amount of CPU activity per Kubernetes node 
over time. In other words, how much workload   each node is handling over time. This info is 
obtained by calculating the rate of this metric   here measuring CPU activity from each node. With 
the rate function, you must specify an interval   in which that rate is calculated. We're using the 
"[$_rate_interval]" variable here to tell Grafana,   "Hey I don't want to figure out this interval. 
Will you pick the appropriate interval for me?".   Next, we'll run the query by clicking on the "Run 
queries" button. By default, it'll create a time   series line graph, which is actually what we want 
to create. At the bottom, you'll see the legend   which shows each node in its respective colors. On 
the x-axis, it shows you the time. On the y-axis,   it shows you the measurements of CPU activity. 
The panel should always always have a descriptive   title. We'll change the title to the "Amount of 
CPU activity per Kubernetes node". You can also   include the description here to provide more 
context. The options section will allow you to   customize the graph in many ways. Again, we'll 
go over a few to create the final visualization   we want. For an explanation of options we don't go 
over, check out the documentation that I shared at   the beginning of the episode. Let's say you wanted 
to customize how the legend is shown on the panel.   If you toggle off the "Visibility" option, you'll 
see that the legend is gone. I want the legend   shown so let's toggle it back on. You could also 
change the placement of the legend. Right now,   it's at the bottom but by clicking on the 
"Right" option here, you could move the   legend to the right. I'm going to put the legend 
back to where it was by clicking on the "Bottom"   option as I like the way that looks. Let's move 
on to the axis. Scroll down to the Axis section.   When it comes to the time series visualization, 
the time will be on the x-axis and it'll be in   your local time zone by default. You could change 
the time zone by selecting an option from a drop-   down menu. You could also change the placement of 
the y-axis either on the left or the right side   of the graph. You can even hide it by selecting 
one of the placement options here. For example,   by selecting the "Right" placement option, the 
y-axis values were moved to the right side of   the graph. But I like the y-axis values on the 
left, so I'm going to return to the original   placement. Next, let's scroll down to the "Graph 
styles" section. You could change the style of   the time series visualization to lines, bars, or 
points by clicking on each option. Here is the   same data shown in a time series bar chart, the 
same is shown in the points time series graph. The   time series line graph helps me see the trend best 
so I'm going to revert back to the original line   graph. In the same section, you could change the 
"Line width". You could change the "Fill opacity"   to add color to the space under each line. You 
can also change the line style from "solid" to   "dash". But I actually like the graph created by 
default so I returned everything to the original   setting. Last thing I'm going to show you is how 
to change the color of the graph. So scroll down   to the Standard option section, then down to the 
Color scheme. Right now, it's set on the "Classic   palette" by default but you could choose from any 
of these options to get the color you'd like. This   is what it looks like when the color scheme is set 
to "Red-Yellow-Green (By value)". "Blue-Purple (By   value). Again, I like the default color scheme 
of the classic palette that shows each node in a   different color so I returned it to the original 
setting. Once you finalize your panel, click on   the "Apply" button. This will add the panel to 
the dashboard. By holding and dragging the panel   title, I'm going to move the panel. I'm also going 
to adjust the size by holding and dragging the   lower right corner to arrange the dashboard like 
this. Next, we will create a Stats visualization   panel. We're interested in the realtime stats 
about the number of running Kubernetes containers.   From the dashboard, click on the "Add" button, 
then select the "Visualization" option. We're   going to visualize the number of running 
containers. The data is contained in the   same metrics data source we have been using. In 
the code view, we'll enter the PromQL query that   counts the number of containers. It's doing 
that by getting the sum of the containers in   the Kubernetes cluster. Let's see if this query 
works by running the query here. It'll show you   a time series line graph by default. Let's change 
that by clicking on the "Visualization" option,   then selecting the "Stat" option. You'll see this 
on the screen. By default, it shows you the most   recent value of whatever data you have queried. It 
shows that there are 91 Kubernetes containers that   are running right now, along with the spark 
line which shows the trend of this data over   time. What we're creating is a simple stats 
visualization that only shows the number of   running Kubernetes containers. We'll start by 
changing the panel title to the "# of running   Kubernetes containers". The spark line, the graph 
in the background is used to show the trend of the   data. For this dashboard though I just want the 
number so we'll remove the spark line. Scroll   down to the Stat styles section. Under the Graph 
mode, select the "None" option to get rid of the   graph. This panel by default is showing the number 
in red. I want this number displayed for context   only so I'm going to keep this in a neutral color. 
Scroll down to the Standard options section and   click on the "Color scheme". Choose the "Single 
color" option from the drop-down menu. It'll   turn the color to gray. Let's save this panel by 
clicking on the "Apply" button. Next, we'll create   a Logs visualization to display logs with errors. 
This will help us to take a quick look at the log   lines. We'll be able to see if this is an event 
we need to look further into. From the dashboard,   click on the "Add" option, then click on the 
"Visualization" option. Since we're viewing logs,   we need to select our logs data source. In my 
setup, the logs are stored in a Loki connection   called "grafanacloud-microbslisajung-logs", so 
we'll select that. To write the query, click   on the "Code" view, then enter the LogQL query 
which retrieves logs with errors. This query is   saying to retrieve all logs from a Kubernetes app 
called "e-commerce" from the "microbs" cluster.   These logs must contain one of the variations 
of these keywords such as "critical", "error",   "exception", "fail" or "fatal". Then click on 
the "Visualization" menu, then select the "Logs"   option, then click on the "Run query" button. 
You'll see log lines that contain a variation   of the keywords we've specified. These are 
highlighted in orange. Let's zoom in on the log   lines here. If you want more metadata about the 
log line you're interested in, you can click on   the arrow to get more metadata here. The default 
visualization is exactly what we want so we won't   customize it any further. If you want to explore 
how else you can customize a logs visualization,   you can check out the doc I shared earlier. For 
our panel, we'll just add the panel title "Logs   with errors" and click on "Apply" to add the logs 
panel to the dashboard. We'll resize and move the   panel just as we've done before to arrange the 
panels as shown here. Last but not least, we'll   create a node graph. This will help us visualize 
the state of all parts of our system and how   these parts are connected to one another. We'll 
specifically display rate, errors, and duration   metrics for apps on our Kubernetes cluster. 
From the dashboard, click on the "Add" button   and select the "Visualization" option. In Grafana, 
node graphs are most commonly used to visualize   trace data and this is no exception. We'll start 
by selecting our trace data source. In my setup,   traces are stored in a Tempo data connection 
called grafanacloud-microbslisajung-traces.   For node graphs, we don't need to write a query. 
Grafana automatically generates everything for   you. From the query section, select the "Service 
graph" option, then click on the "Visualization"   drop-down menu and select the "Node graph" 
visualization. What I've been encountering is   that Grafana doesn't load the node graph until I 
change the time range. So I clicked on the "time   picker" and selected for the "last 24 hours". Then 
it generated the node graph. At first, I just saw   a partial node graph, so I grabbed and dragged 
the visualization panel down. This node graph   shows the state of all parts of our system and 
how these parts are connected. You could see the   services of our app represented as a circle. We 
see checkout, content, API Gateway, etc along with   calculation of the rate, errors, and duration(RED) 
metrics. All of this is done automatically without   configuring anything as it's already in 
the trace data set we have. The node graph   is attuned to that data source. Let's zoom in on 
the visualization by clicking on the "plus sign".   Each circle or service displays two numbers. 
The bottom number is the number of requests   the service receives per second. This is also 
known as rate. The top number shows the amount   of time those requests take. This is also known as 
duration. Together, these two numbers reflect the   total traffic the service particularly deals with. 
Should the requests fail, the circle will turn   red. This is known as errors. You could also see 
the same metrics between two specific services.   This is why the final node graph visualization is 
titled as "Rate, errors, and duration(RED) metrics   for apps on our Kubernetes cluster. Using the 
panel editor, we'll change the title as such. Then   click on the "Apply" button. All right. We just 
created the gauge, time series line graph, stats,   logs, and node graph visualizations to observe 
our system. While we're observing our system,   we'll come across some interesting events or 
patterns that we want to mark and discuss with our   teammates. This is known as annotating events. In 
the next episode, we'll learn how to do that with   Grafana. If you want to access more episodes 
of Grafana for Beginners series, go to the   Grafana community web page. This is where all the 
community resources are shared. You can access the   series by clicking on the Grafana for Beginners 
card. Last but not least, if you want to delve   deeper into any of these topics covered in the 
series, documentation is a great place to start.   To access the documentation, scroll down on the 
page and click on the docs card. On the docs page,   you can either search for the topic you want 
or look at the table of contents to see what is   there to explore in Grafana. You can also click 
on the product name to delve further into that   product. All right, that's a wrap. Thank you for 
watching and I'll see you in the next episode.

