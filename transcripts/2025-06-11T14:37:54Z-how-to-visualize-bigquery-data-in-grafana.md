# How To Visualize BigQuery Data in Grafana

Published on 2025-06-11T14:37:54Z

## Description

Ready to bring your BigQuery data into focus? In this Grafana Quickstart, Shawn Pitts walks through how to connect Google ...

URL: https://www.youtube.com/watch?v=osY3J1U2n-M

## Summary

In this Grafana Quickstart video, Sean Pitts demonstrates how to connect Google BigQuery to Grafana Cloud for enhanced data visualization and insights, particularly focusing on sales data. He explains the installation of the BigQuery data source in Grafana Cloud, emphasizing that it is available on all tiers, including the free version. Sean walks viewers through the configuration process, including enabling the BigQuery API in the Google Cloud Console and creating a service account for secure connections. He showcases how to query and visualize data using Grafana's intuitive UI and SQL code editor, providing practical examples from a fictional computer store to illustrate how to create time series and statistical visualizations. The video concludes with an invitation for viewers to share their questions and ideas in the comments.

# Grafana Quickstart: Connecting Google BigQuery to Grafana Cloud

Hey everyone, Sean Pitts back again with another Grafana Quickstart. In this video, we'll be connecting Google BigQuery to Grafana Cloud to help bring business insights, such as sales data, closer to your application and infrastructure-level telemetry. 

Just like all of our data sources, the BigQuery plugin is available on every tier of Grafana Cloud, including the free tier, which is what we'll be using today. The Grafana Docs cover all the step-by-step details here, but this video serves as a supplemental resource. So if video is your preference over reading, this will be for you. Let’s jump right in.

## Installing the BigQuery Data Source

First things first, let's get this installed in Grafana. We’ll jump into Grafana Cloud under **Connections**, then add a new connection and toggle on **Data Source**. You can see that I have Google BigQuery listed, but you can also search for it in the box above. 

Click on **Google BigQuery**. In this case, you’ll see two options in the top right corner: **Uninstall** (because I already have it installed) or **Add as a new data source**. You'll most likely just see **Install**. Click on that, and it will only take a few seconds to add it as a new data source. 

Once added, we can move on to the fun part: configuring the data source to ensure a secure connection from Grafana Cloud to BigQuery. 

## Configuring the Data Source

We need to perform a few steps in the Google Cloud Console to establish this connection. First, the BigQuery API must be enabled on GCP for the data source to work. There are two authentication options: 

1. **Google JWT file**
2. **GCE default service account**

If you are running a virtual machine or GCE instance, Grafana can automatically retrieve the project ID and authentication token from the metadata store. However, you still need to grant read access to the BigQuery API.

In this tutorial, we’ll use the **Google JWT file upload** method. Let’s jump to the Google Cloud Console to set this up.

### Enabling APIs

In the Google Cloud Console, select your project (in this case, "computer store"). Next, enable the necessary APIs. In the left-hand menu, click on **APIs & Services**, then go to **Library**. 

First, ensure that the **BigQuery API** is enabled. Scroll down to find it and click on it. It may already be enabled for you; if not, enable it. 

Next, we need to enable the **Cloud Resource Manager API**. Go back to the API services library and search for **Cloud Resource Manager**. Click on it and enable it. This step is crucial because we won’t be able to read or get metadata from Google Cloud without it.

### Creating a Service Account

Now that we have both APIs enabled, we can focus on creating a service account. In the left-hand navigation menu, go to **IAM & Admin** and click on **Service Accounts**. 

Create a service account and name it something like "gana". After creating it, we need to generate the JWT file. Go to **Actions**, then **Manage Keys**. Here, we can add a key to obtain our JWT file. Choose the key type as **JSON**, and a file will be downloaded onto your computer. This file is essential for us.

### Uploading the JWT File to Grafana

Now, let’s jump back into Grafana. In the BigQuery data source, scroll down to the JWT key details and drop the file directly in. Grafana will automatically fill in specific details we need, such as the project ID, client email, and token URI. 

When we go to **Save & Test**, you’ll see the data source is working, allowing us to explore and build dashboards based on this data. 

## Exploring BigQuery Data

Now that everything is configured and our data source is up and running, we can explore and query the BigQuery data. Grafana Cloud offers two options for visualizing data:

1. **Builder** - A user-friendly UI dropdown for selecting items such as project, dataset, table, column aggregation, filtering, grouping, and ordering.
   
2. **SQL Code Editor** - For those who prefer writing SQL queries. The editor provides autocomplete features and displays how much data will be processed when the query is run.

Let’s look at a real use case. I have a project called "computer store," which sells products like GPUs, CPUs, cooling units, and fans. In the dataset "stored details," we have customer details and customer orders.

### Running a Query

Let’s say we want to look at customer orders. If we retrieve all columns, we’ll see that it processes approximately 6.55 KiB of data. Running the query gives us all the relevant columns, including the computer part, price, quantity, and total order amount.

To visualize this data more effectively, we can switch to a time series view to see sales or purchases over time. Since we have a purchase date in ISO format, we can select that column for our X-axis and the total order amount for our Y-axis. 

When we run our query, we must ensure that the format is set to **Time Series** so we can visualize purchases over time along with the total order amount.

## Adding to a Dashboard

To add this visualization to a dashboard, click **Add Dashboard**, and it will open in a new tab. From there, you can save it or add more panels as needed. Let’s say we want to display the total sales. 

We’ll configure it to aggregate the total order amount from customer orders. When running this query, it shows 800 bytes of data. However, we need to select a different visualization type, like **Stat**. 

To make it more readable, we can change the unit to currency (dollars), which shows that we have generated $1.28 million worth of sales in the last 30 days. 

### Customizing the Dashboard

Returning to the dashboard, we can customize the layout. In Grafana 12, there’s an auto-grid feature that allows us to choose narrow or tall views for better organization. 

Additionally, Grafana lets us pull telemetry from different data sources. For instance, we could combine business data from BigQuery with logging data from Loki or metrics from Prometheus, enabling side-by-side visualizations for deeper insights.

## Conclusion

That’s a quick start on how to get up and running with the BigQuery data source for Grafana. If you have any questions, please drop them in the comments below. I’ll make sure to post all the relevant documentation and information. I can't wait to see what you all are building!

Talk to you in the next video!

## Raw YouTube Transcript

Hey everyone, Sean Pitts back again
with another Grafana Quickstart. In this video, we'll be connecting Google BigQuery
to Grafana Cloud to help bring those business insights such as sales
data closer to your application and infrastructure level telemetry. Now,
just like all of our data sources, the BigQuery plugin or data sources
available on every tier of Grafana Cloud. Yes, even the free one, and that's exactly
what we're going to be using today. Now, the Grafana Docs always covers all
the step-by-step stuff we'll do here, but this is just a supplemental video. So if video is your thing and reading's
not, then this will be for you. So let's jump right in.
Okay, so first things first, let's get this installed in Grafana. So what we're going to do is jump
into Grafana Cloud under connections, we'll add a new connection and toggle
on data source. You can see that I have Google BigQuery right here, but you can
search it up above and it'll appear. So let's click on Google
BigQuery and in this case, you see I have two options in right
hand corner, it's to uninstall, meaning I already have this installed.
Or to add it as a new data source, you'll most likely just see installed
in the top right hand corner. You'll have to do that and it'll
just take a few seconds or moments, but then you should be able to
add it as a new data source. We'll click on this and you can
see the data source has been added. Now comes the fun part of
actually configuring the
data source to make sure that we can make a secure connection
from Grafana Cloud to BigQuery. Now we'll have to do some steps in the
Google Cloud console to be able to make sure that it makes a connection. One of
them is being that the BigQuery API has to be enabled on GCP for
the data source to work. There's also two authentication versions
here. So we have the Google GWT file, and then we have the GCE
default service account. There's a few specific details about the
GCE default service account option that you have. So if you are running a
virtual machine or GCE instance, it's possible for Grafana to automatically
retrieve the project ID and the authentication token
from the metadata store. So you don't actually have to do that
manually if you are running an instance through Google Cloud, but you'll still need to give it
read access to the BigQuery API. So it's important regardless that we
configure that on. Now in this tutorial, in this demo, we're going to be
using the Google JWT file upload, and we're going to jump into Google
Cloud Now to do that. So now we're in the Google Cloud console and we'll want to
select our project in this case minus computer store. And then we'll want to enable the proper
APIs that are needed to be able to get set up with the data source. In
the left hand hamburger menu, you'll see that there's APIs and
services and then we're going to click on library here. The first thing we need to make sure
is that the BigQuery API is enabled. You'll see that there's 17 results. You're going to scroll down and look
for the BigQuery API and then click on that. You'll see that in this case,
the API is already enabled for me. You might have to enable
it, but once you do so, we're going to have to enable one more,
which is the cloud resource manager, API. So we'll go back into the API
services library and we'll look for cloud resource and then you'll
see the Cloud Resource manager. API is the first result here. We'll
click on this and we will enable it. This is super important because we won't
be able to actually read or get the metadata from Google Cloud. Now that we have that and we
have both of those installed, we can start to worry
about the service account. We'll go into the left hand navigation
menu again and go to I am an admin and click on I am in here. You'll see that there's service accounts
and we'll need to create a service account for this enterprise data source. So we'll create a service account
real quick. We'll just call this gana and then you'll see that this has been
created. However, we need that JWT file, right? So what we're going to do is we're
going to go into actions, manage keys, and in here we'll be able to actually add
a key. This will give us our JWT file. So we can upload this to Grafana
to make that secure connection. We'll create a new key. We'll
choose the key type to be JSON, and then you'll see that a file
actually downloads onto my computer. So this is important that we have this.
So now let's jump back into Grafana. And you can see in the BigQuery
data source as we scroll down, we can drop that file directly
into the JWT key details. You're going to see that it automatically
fills in specific details that we need, such as the project id, the
client email, and the token URI. So now when we go to
actually save and test this, you're going to see the data sources
working, which means we can explore, we can build dashboards based on this
data. So let's go ahead and do that now. Alright, so now that we're all configured
in our data sources up and running, we can now explore and
query the BigQuery data. So what's awesome about Grafana Cloud
and the enterprise data source for BigQuery is that we have two options
of really visualizing data here. We can do this with a builder, which you can see is just a very intuitive
UI dropdown. So we can select the items that we want such as the project
dataset, table, column aggregation, as well as filtering group
by ordering and so forth. But if you want to write
SQL and you're an SQL pro, then we have the code editor as
well. So you can see here what's, say I'm running a from statement, we're going to notice that
all of this auto completes, and then in the bottom of this panel, we're going to see this query will
process X amount of data when run. This is nice because instead of just
running a big giant query and not understanding what the consequences
of running such a big query is, you can look at it and say, oh wow,
this is gigabytes or terabytes of data. I don't want to query all that. That's going to cost me a lot of money
on the BigQuery or Google Cloud side. So that's important to note. Let's jump back into the builder and
actually look at a real use case. So I have a computer store, and this is where people can
just purchase simple products. So this could be GPUs, CPUs,
cooling units, fans and so forth. But I have a project computer store,
which is my Google Cloud project, which we saw. And then dataset,
which is stored details. And this stores all my tables. We have customer details
and customer orders here. So let's say we look at customer orders,
and if we get all the columns here, you're going to see that this actually
processes 6.55 KIB worth of data. We'll run this and you'll see that we
get all of my columns back along with the computer part, the price, the quantity,
total order amount, and so forth. But let's say I want it to actually
visualize this to be something more useful instead of just my orders. Let's say
I want to see what the sales or the purchases over time look like. So what we can do is we can
flip this onto time series. Let's say we just tried to run this. You're going to see that it's unable to
process data because it's not sorted by any time. Now, when we
walk back in that data, when we walk at the table, you'll
notice that there is a purchase date. This is an ISO formatted purchase date. So what we can do here is we can get
the column, which is the purchase date, and you'll see that there is the clock
indicating that this will be our time on our act axis. Now we want our Y axis, so we'll choose the total order amount.
Now we'll select total order amount, and then when we run our query, you're going to see that we still get
in a table view. We have to toggle this format to be time series, and then we can see our purchases over
time and how much the total order amount is. You can see since we're looking
at this from a purchase date, we can see that on the X axis. And then we can see the column on the
Y axis such as the total order amount. And now we can add this into a
dashboard pretty straightforward. We just click add dashboard, and
then we'll open this up in a new tab. You'll see that this
automatically drops it in for us, and then we can just save this as a
dashboard or we can start to add more. Let's say we want to add one
more panel. We'll configure this, maybe we go back into our BigQuery
data source. And then we want to say, you know what? Give us the total sales.
So we'll going to store details, customer orders, give me the total order amount
and aggregate this by the sub. So now when we run this query,
which you'll see it's 800 bytes, which is really nothing, we can run this query and you're going
to see that we don't get any data. That's because we don't
want to use a time series. We'll want to use something like a stat. And you can see here that we have
quite a bit of purchase sales, but this isn't really in
a human readable format. This is going to be hard to interpret
every time you come to look at it. So we'll go into the standard
options on the right hand side here, and you'll see under unit, we
can choose currency and dollars. So in this case, we've done $1.28 million
worth of sales in the last 30 days. It's pretty good.
So we can go back to the dashboard, we can actually add this in and we can
toggle this if we want to change the layout. Now in Grafana 12, we
have an awesome way to do this. We have the auto grid so we can start
to change this based on if we want 'em wide, if we want 'em custom, if we want to choose these
specific amount of columns. So maybe we want to do a narrow view,
and then we want the row to, let's say, be tall. So now everything's a lot higher
and we can put these side by side. And then what's also about Grafana
is we can have telemetry coming from different data sources. Right now we
have business data coming from BigQuery, but what if we have some sort
of logging database like Loki, or if we have metrics in Prometheus, we can actually bring that in to be
able to view it side by side and make correlations to be able
to visualize this further. So that's a quick start on how to get
up and running with the BigQuery data source for Grafana. If
you have any equipments, please drop 'em in the comments below
and I'll make sure to post all the docs and relevant information in the details
and can't wait to see what you guys are building. Alright, talk with
you guys in the next video.

