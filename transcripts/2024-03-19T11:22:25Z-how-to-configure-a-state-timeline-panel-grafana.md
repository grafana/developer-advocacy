# How to Configure a State Timeline Panel | Grafana

Do you want to know how and when to use state timeline visualizations? Join Senior Developer Advocate Marie Cruz in this ...

Published on 2024-03-19T11:22:25Z

URL: https://www.youtube.com/watch?v=a9wZHM0mdxo

Transcript: Hi! My name is Marie Cruz, and I’m a Senior 
Developer Advocate at Grafana Labs. In this   beginner-friendly video tutorial, I’ll discuss 
state timeline visualizations in Grafana. By the end of this tutorial, you should know how   to configure a state timeline to 
visualize your data in Grafana. State timeline displays your data in a way 
that shows state changes over time. You   can use a state timeline to monitor the 
statuses of your servers, applications,   or services to know when they are experiencing 
any issues. You can also use a state timeline   to observe operational trends and spot any 
recurring health issues about your applications. To help you in this tutorial, I’ll be 
using the Grafana TestData data source,   which comes built-in with Grafana. The Grafana 
TestData data source has different scenarios,   so you can easily experiment 
with visualizing the data. With that explanation out of 
the way, let’s get started! First, I’ll add a new visualization to a dashboard 
and select the grafana-testdata-datasource. Then,   under the visualization drop-down, I can 
choose the state timeline visualization. A state timeline works best if you have 
data capturing the various entities'   states over time. So, to work with state 
timelines, your data must have timestamps,   the names of the entities, and their 
state changes. So, the state changes;   you can represent that as either a 
string, numerical, or boolean values. So, for example, I have a table 
right here that shows how your   data should look like to visualize 
it correctly as a state timeline. To use this data, I’m going to select the 
CSV content scenario and then I’m going   to convert the example table 
that you saw to a CSV format. When I hit refresh, you might see an error 
message saying that the data does not have   a time field. The timestamps I’ve added, they’ve 
probably been recognized as a string rather than   time. So what I’ll do is, I’m going to add a 
transformation rule to convert the Timestamps   column to be of type time. So I’m going to use the 
Convert field type transformation rule for this. Now, you should see data being 
displayed. If you don’t see any data,   make sure that you are in the 
correct date range. So you can   either search for a quick range or you 
can also apply the date range manually. Now, let’s improve how you can 
visualize this data even more. On the right side, there are different 
options specific to the state timeline   that you can configure depending 
on your use case. For example,   if you don’t want to merge the consecutive 
values, you can toggle this option right here   as well as different formatting options 
on how you would display the values. If you want to customize how null values, 
which are gaps that you see in this graph,   are visualized, you can choose to connect them   so you don’t see any gaps or not 
if you want to leave them as is. You can also assign colors to different 
states and make it easier to distinguish   any state changes. To do that, I’ll 
click the add value mappings button   and set different colors for the 
Up, Warning, and Down states. I also don’t need to set a threshold since I’m 
not using numerical states for this example,   so I’m going to remove the threshold and 
then we can go ahead and save the changes. And there you have it! In this 
beginner-friendly tutorial,   I’ve shown you how you can configure a state 
timeline to visualize your data in Grafana. Make sure to check out our Grafana documentation 
if you want to know more about state timelines,   which you can find in the video description below. I hope you found this video useful, and if you do,   let us know in the comments below 
and as always, happy visualizing!

