# How to use data source variables in Grafana dashboards

Data source variables let you change where Grafana looks for data without having to create duplicate dashboards. So for example ...

Published on 2025-03-27T16:06:16Z

URL: https://www.youtube.com/watch?v=jCTRy6NX1wo

Transcript: Hi! I'm Ronald McCollam, part of the 
Developer Advocacy team at Grafana Labs and if you're like me, you need to visualize data 
that's stored in a lot of different locations. Maybe it's production versus 
development or testing, maybe it's different regions, maybe just different teams 
set up their infrastructure   at different times and in different locations. Whatever the reason, Grafana has a 
feature that makes it easy to switch   between data sources on a dashboard 
without having to rewrite queries. They're called data source variables and 
today I'm going to show you how they work. I'll start with a blank dashboard. I'll open the dashboard settings, choose 
the variables tab, and add a new variable. I want to let viewers choose what data source to 
use so I'll pick the data source variable type. Give it a descriptive name 
like "Prometheus Source", a friendly label for it on 
the dashboard, and optionally   some descriptive text about 
what this variable does. I also need to tell Grafana what type of 
data source I want to let people pick. Let's use Prometheus. You can see I've got three Prometheus 
instances connected to Grafana,   but maybe I don't want to show all of them. I might want to filter which ones 
people are allowed to pick from. I can use a regular expression for this,   like selecting any Prometheus instance 
that ends with the word "prom". You'll notice that I'm now down to two. Let's see how this works with a visualization. I'll add a time series panel and 
for my data source I'm going to   pick the Prometheus variable that I just defined. This means that when a data source is selected it 
will be passed as the source for the panel here. Let's look at a metric. I'll 
look at CPU utilization. This makes a boring graph, so let's take the range 
function to look at this data's rate over time. Now when I run the query I see a 
nice graph of utilization rates. If I switch this to a different 
source, I'll get different data. The query that is run is the same 
-- only the data source has changed. Note that when I select different 
data sources the labels on the   data will change because these 
are different environments. Now you can make dashboards that 
let viewers choose where their   data comes from without having to 
rewrite queries or edit anything!

