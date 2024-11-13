# Exploring logs, metrics, and traces with Grafana | Grafana for Beginners Ep. 7

Exploring logs, metrics, and traces for the first time could be an overwhelming experience if you don't know where to start.

Published on 2024-02-07T18:00:01Z

URL: https://www.youtube.com/watch?v=1q3YzX2DDM4

Transcript: Hey! Welcome to Grafana for Beginners. I'm Lisa 
Jung and I'm a Developer Advocate at Grafana. In   this series, we're using Grafana to visualize logs, 
metrics, and traces from an e-commerce app. This   app has a microservices architecture and it's 
running on Kubernetes. For more context about   this app, go to the microbs repo and click 
on the e-commerce app. It's part of an open   source framework created by Dave Moore, who is a 
Customer Solutions Engineer at Grafana. This is   a fantastic resource for you if you want to demo, 
test, or learn about microservices observability.   The link to the repo is in the info card up top.
So logs, metrics, and traces are being collected   from this e-commerce app. The logs are stored in 
Loki, traces are stored in Tempo, and metrics are   stored in Mimir. In the last episode, we learned 
how to add data sources to Grafana. Today, we'll   learn how to use Grafana Explore to see what's 
in our data. To get started, go to the homepage   of Grafana Cloud, or Grafana in your local 
environment. Click on the "menu" icon, then click   on the "Explore" option. This is the Explore view. 
It helps you to explore the data without creating   a dashboard. It also helps you to write queries 
that retrieve the data you want. In this episode,   we'll be using Explore to verify that the data is 
flowing in. We'll also poke around to see what's   in our data. The first step is to choose a data 
source you want to explore. You could do that by   clicking on the data source option up top. You'll 
see a list of all the data sources you have added   to Grafana. We'll start with logs. In my setup, 
my logs are stored in a Loki connection named   "grafanacloud-microbslisajung-logs". So I'm going 
to select that. Next, we'll choose the time range   for the data we want to see. I want to look at 
more recent data to make sure that there's data   flowing in. So click on the time range to display 
the drop down menu and select the time range of   last 15 minutes. The section highlighted here is 
a query builder. This is where you could write   queries to retrieve the data you want. It comes 
with tools that guide you to build the queries,   so you don't have to think about the syntax as 
much. One way to explore what's in your data is   by looking at the labels in the data. So, think of 
labels as fields. It consists of a key-value pair   that shows what information could be found in your 
data. When you click on the "Select label" option,   it gives you a drop-down menu of labels in 
the logs. It looks like the logs contain info   regarding the cluster, the app, the container, 
and so on. So let's say you want to learn more   about the cluster associated with the app, so you 
select the "cluster" option. When you click on the   "Select value" option, it'll show you all values 
associated with the cluster. It looks like the   logs are associated with a cluster named microbs. 
When you select that, you'll see that Explore has   automatically built a query for you. What this 
is saying is, to fetch me all the logs from the   microbs cluster. Now, if at any point you want 
an explanation about the generated query, go to   the "explain query" option, and click on the toggle 
switch, and it'll provide you with an explanation.   So this is another tool at your disposal when 
you're getting started. Now, this in fact,   is the query that we want to run, so we'll click 
on the "Run query" button. When you scroll down,   Explore displays a graph of Logs volume from 
the past 15 minutes. Scroll down a bit more,   and you'll see the actual logs displayed here 
from the same time range. This is good news   because it means that the logs are coming 
in as expected. When you click on the arrow,   it'll show you the metadata associated with the 
log like the cluster name, the application name,   etc. You can also see that this log is coming 
from the web gateway container. If that is what   I'm particularly interested in, I can tell Grafana 
to further filter by that. All you have to do is   to click on the "plus" icon here. When you scroll up 
to the query section, you'll see that my query has   been updated. It's saying fetch me the logs from 
the microbs cluster. From those logs, only show   me the logs from the web gateway container. By 
seeing what's in your data, you can narrow down   your queries to understand the data even more. 
Next, let's take a look at the metric data. To   do so, we'll select the correct data source up 
top. Click to expand the drop down menu. Our   metrics data is stored in Mimir, in a connection 
named "grafanacloud-microbslisajung-prom",   so we'll select that. Mimir is like an enterprise 
grade of Prometheus, so it shows up as Prometheus   in Grafana. Now, you'll notice that the labels we 
selected earlier, were automatically applied here.   Because Grafana knows how to do that within 
its own data sources. I want to start fresh.   So highlight the query and use a backspace key 
to delete it. It'll return to the default page.   You'll see that this page has a query builder as 
well. Each data source has its own query language,   so the query builder is customized to that 
specific language. To check that the data is   flowing in, we'll explore the metrics collected 
from the last 15 minutes. So double check that   the time range is set to that. Then click on the 
"Select metric" option here. The drop-down will list   all the metrics that are coming in. By reading 
the names of the metrics, I sort of have a clue   about what these are, but I want to know more. 
So I'm going to click on the "Metrics explorer".   It'll list the name, type, and description of 
metrics that exist in our data. With more context,   we could further narrow down which metrics we want 
to explore. If you have a rough idea of the name   or the type of metric you want to explore, you 
can also search or filter up here, instead of   scrolling through every metric. All right. Let's 
close this window. Once you choose the name of the   metric, you can select the label and the value you 
want to filter by, and run the query to get more   info. Now, I want to show you another helpful tip, 
while you're exploring your data. I find scrolling   through metrics, labels, and values, to be a bit 
tedious. And I prefer see more info at a glance,   so I could quickly figure out what I want to see 
more of. There are two views you could use with   Explore. One is the builder view, which is the 
view you're looking at right now. Then there's the   code view. So click on that. With the code view, 
you're able to write your query from scratch. It   also offers the "Metrics browser". When you click 
on it, in one page, it displays the names of the   metrics that exist in your data, plus the labels, 
and the values associated with that metric. So   it allows you to sift through the metrics a 
lot quicker. So let's say you come across a   metric called "traces_spanmetrics_latency_bucket". 
You're like 'hmm, what's that all about?' When you   click on that metric, it'll automatically update 
the labels associated with it. Let's just click   around to see what's in there and we'll click 
on the label "cluster". Now it'll show you that   the metrics are associated with a cluster named 
"microbs". So let's select that value and let's   narrow this down even more. So we'll look at the 
list of labels again, and we're looking at the   metrics data from a microservices app, and I want 
to see what services we're working with. So let's   select the label, "service_name". Now it's showing 
seven services named "cart", "web gateway", "payment",   "product", and "checkout", which are crucial aspects 
of our e-commerce app. Let's say we want to look   more into the payment service, so we click on 
that. From here, you don't even have to write   a query. You've selected what you wanted to view, 
and it automatically generated a query for you. So   this query is saying fetch me the metrics with the 
name "traces_spanmetrics_latency_bucket". These   must be from the payment service associated with 
the microbs cluster. Then you're going to click on   the "Use query" button and Grafana will display 
the results. Up top, it displays a query that   was ran. It shows you a line graph, with a legend 
that shows you what each line represents. You can   visualize the same data in different formats, by 
selecting the format highlighted here. For example   you can select the bars option to see a bar 
graph, points, stacked lines, and stacked bars.   So you can visualize the data in the format you 
need to understand what's going on within your   system. And, when you scroll down, you'll also 
see the raw data from the last 15 minutes here,   which tells us yes, we have data flowing in, and 
we could also see what's in the data that might   be of interest to us. We could also convert this 
into a table view, by clicking on that option,   if you find that view to be more helpful. So 
let's switch gears and take a quick look at   traces. Click on the data source selector up top. 
The traces are stored in a Tempo connection named   "grafanacloud-microbslisajung-traces", so we'll 
click on that. We'll first verify that we have   new traces coming in. To do so, set the time range 
to the last 15 minutes and run the query. When you   look at the table below, you'll see a bunch of 
traces that came in within the last 15 minutes.   So we got data flowing in as expected. We see the 
trace ID, start time, service, name, and duration,   and when you click on the trace ID, you could 
see the full traces here, which you could further   delve into. Similar to the Builder and Code view 
of Loki and Mimir, there are Search and TraceQL   views in Tempo. Search view, is like the Builder 
view, and TraceQL is similar to the Code view,   where you could write a query from scratch. Now, 
we'll focus on the search view as this is more   beginner friendly. The Search view allows you to 
filter the data by the service name, span name,   status, duration, and tags. So let's say you 
wanted to filter for traces with a duration   that was greater than 1,000 ms. You would go to 
the duration section, from the drop down, choose   a trace option, and enter the value of greater 
than 1,000 ms, then run the query. Now, this   will pull up all traces with a duration greater 
than 1,000ms. When you click on the trace ID,   it'll display more details to help you understand 
what might be going on with your system. Alright,   so we just went over how you would explore logs, 
metrics, and traces with Grafana. Next we'll learn   how to create a dashboard with Grafana, and get an 
overview of different types of visualizations you   can build with Grafana. If you want to access 
more episodes of Grafana for Beginners series,   go to the Grafana Community webpage. This is 
where all the community resources are shared.   You can access the series, by clicking on the 
Grafana for Beginners card. Last but not least,   if you crave in-person learning and interaction 
with community members, you can attend a local   Meetup. To join a Meetup group, scroll down on 
the page and click on the Meetups card. We have   Meetup groups in 22 countries around the world. 
Search for the one closest to you, to join the   next Meetup. And that's a wrap! Thank you for 
watching and I'll see you in the next episode.

