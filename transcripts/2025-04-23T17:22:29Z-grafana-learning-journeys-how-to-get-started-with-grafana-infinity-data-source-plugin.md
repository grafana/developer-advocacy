# Grafana Learning Journeys: How to Get Started with Grafana Infinity Data Source Plugin

In this Grafana Learning Journey supplementary video, Developer Advocate Marie Cruz shows how to start with the Grafana ...

Published on 2025-04-23T17:22:29Z

URL: https://www.youtube.com/watch?v=BxWw4BWY5ns

Transcript: The Infinity data source is an 
open-source plugin that lets you   query and visualize data from various 
external sources, like REST APIs, CSV,   JSON, and/or GraphQL, directly 
into your Grafana dashboards. In this video, I’ll be guiding you on how to get 
started with the Infinity Data Source plugin.   By the end of this, you’ll know to install 
the Infinity data source and add it to your   Grafana environment. You'll also learn how 
to configure basic authentication and have   the knowledge to select a private data 
connection, especially when working with   internal datasets. Finally, you'll build 
a dashboard using CSV and/or JSON data. Before jumping into this video tutorial, there 
are a few prerequisites that you need to know. First, you need to have a Grafana Cloud account 
in which you are an administrator. You’ll   also need to have a CSV or a JSON file that's 
populated with data and accessible via a URL. In this demo, I’ll be using a public dataset, but 
if you’re working with internal data, make sure   you have the knowledge of the authentication used 
to secure the endpoint. With internal datasets,   it’s also highly recommended that you set up a 
private data source connection and that the PDC   agent is up and running so that the connection 
is secure. If you haven’t done this part yet,   make sure you check out our learning journey 
for creating a private data source connection. Feel free to pause the video here, but 
when you’re ready, let’s get right into it. The first step is to install the Infinity data 
source plugin because it’s not installed by   default. In your Grafana environment, 
open the navigation menu on the left.   Click connections, enter `Infinity` 
in the search bar and press Enter. You should see the Infinity tile. Then, in the upper-right corner, click Install. You should see the message `Install 
requested, this might take a few minutes.` After the data source is installed, we 
need to add it to our Grafana environment. To add, navigate back to Connections 
but this time, click Data sources. Click add new data source and search for Infinity. Go ahead and click the tile and add a name. 
You can give this a more meaningful name,   but I’ll just stick with the default. If you’re using internal data 
and require authentication,   you need to provide an authentication 
method and add the respective credentials. To do that, click Setup Authentication or you   can also click Authentication 
on the left navigation menu. Select the authentication method for your 
data set. If it’s basic authentication,   you can add the username and password here. Since I am working on a public data set, I don’t 
have to provide any authentication details. Next, let’s test the connection 
to the data endpoint. To do that, click Health check on the   left navigation menu and enable 
the custom health check toggle. For this demo, I’m going to use two endpoints—one 
that returns CSV data and another that returns   JSON data. In your case, you should use 
a URL that returns the data you want. When you’re ready, click save and test. You should see the following 
health check success message. To establish a secure connection between 
Grafana Cloud and your data endpoint,   you need to select an active PDC agent 
and test the connection to Grafana Cloud. This is optional but highly recommended. 
Without a PDC, your queries and data   are transmitted over the public Internet, 
exposing them to potential security risks. I have a PDC agent running already, so 
in the private data source connect field,   I can select the name of my PDC agent. To test the secure connection,   click save and test and you should see the 
following health check success message. We’ve done the installation 
and configuration. Now,   the final piece of the puzzle 
is to build our dashboard. To build a dashboard with the Infinity data 
source, you can click Dashboards in the Grafana   main menu. Afterwards, click New and select new 
dashboard. You should see the following screen. On the empty dashboard, just 
click add visualization. Search for your Infinity data source 
and select it. Now, in the URL field,   enter the endpoint of the data 
that you want to visualize. I'm going to start first with the CSV endpoint. 
Now, in the advanced options section, you should   see a delimiter field. Most commonly for CSV 
data structure, this is a comma but again,   make sure to check your own CSV data structure 
in case you are using a different delimiter. Ok,   now we're going to visualize this as a time 
series data so go ahead and click add column. Again, depending on the structure of your 
CSV, time series should have at least one   timestamp entry. I have a column named 
created_at, which corresponds to when   the entry has been created. But, since this 
is a CSV, everything is set as a string. So,   I need to format this as a time and also 
set a title. So for example, "Created at." I'm going to continue adding columns for my 
field1 and field2 column. So, for field1,   I'm going to give it a title of "Density of 
Westbound Cars" and then I'm going to format it   as a Number instead. I'm going to do the same for 
field2, but instead of Westbound Cars, we're going   to give it a title of "Density of Eastbound 
Cars" and also set the format as a Number. Now, if you hit refresh, you should now see 
a preview of your dashboard. At this point,   feel free to manipulate the time range.   Once you're happy, click Save dashboard, 
enter a title, and click Save. Now, you've just created your first 
dashboard using the Infinity data source. Now, let's visualize a JSON data. So, going back 
to my dashboard, let's click Add visualization and   select the Infinity data source. Next, I'm 
going to provide the URL for my JSON data,   and then I'm going to expand the Parsing 
options and results field section. In the rows/root field, I'm going to enter a   row name. So, let's go back and look at my 
JSON structure. In this particular example,   I only want to look at fields. Now, the Infinity 
data source can give you the ability to specify   the section of data that's relevant for your 
visualization. This is useful because many   APIs will return more data than what you want 
to show to Grafana, such as different metadata. Next, we're going to add columns the 
same way as we've done for the CSV   example. We're going to add a column for 
the created_at, set a title and format   it as time and then we're going to do the 
same for field1 and field2, setting both   titles as Density for Westbound and Eastbound 
Cars, and then the format as both Numbers. Now, if I hit refresh and just 
zoom to the correct data range,   I should now see a dashboard preview. At this 
point, you can add a title for this panel. So,   in this example, I'm going to name it 
as JSON example. Click save, and now you   should have two panels. One for visualizing 
JSON data, and one for visualizing CSV data. And there you have it. In this video, 
you learned how to install the Infinity   data source plugin and add it to your 
Grafana environment. You also learned   how to set up basic authentication and add 
a private data source connection. Finally,   you learned how to build a 
dashboard using CSV and JSON data. I hope you found this video useful and I'll 
see you on the next one. Happy visualizing!

