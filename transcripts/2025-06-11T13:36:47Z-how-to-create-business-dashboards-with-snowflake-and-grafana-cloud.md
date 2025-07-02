# How to Create Business Dashboards with Snowflake and Grafana Cloud

Published on 2025-06-11T13:36:47Z

## Description

Ready to bring your Snowflake data into Grafana dashboards? In this Grafana Quickstart, Shawn Pitts walks through how to ...

URL: https://www.youtube.com/watch?v=DA1zcCDY8k8

## Summary

In this Grafana Quickstart video, Shawn Pitts demonstrates how to connect Snowflake to Grafana Cloud to integrate business insights with application telemetry. He walks viewers through the installation of the Snowflake data source within Grafana Cloud, including essential configuration steps such as entering Snowflake account details, authentication options, and setting up environment parameters. Shawn also illustrates how to create queries to visualize data, build dashboards that display total sales and revenue per product, and customize visualizations with features like filtering options using RegEx. The video emphasizes the flexibility of Grafana in combining data from different sources for comprehensive business analysis and encourages viewers to refer to the documentation for further setup instructions.

# Grafana Quickstart: Connecting Snowflake to Grafana Cloud

Hello, my data-driven friends! Shawn Pitts is back again with another Grafana Quickstart. In this video, we'll be connecting **Snowflake** to **Grafana Cloud** to bring those business-level insights or ETL pipelines you've built out closer to your application and infrastructure-level telemetry.

Like the Snowflake data source, all of our enterprise data sources are available on every tier of Grafana Cloud, including the free plan, which I will be using today. It's also important to note that the documentation has all the setup instructions you need; however, this video will supplement that. So let's jump right in.

## Setting Up the Snowflake Data Source

First things first, let's jump into Grafana Cloud to install the Snowflake data source. 

1. Go to **Grafana Cloud**, look for the **Connections** tab, and click on **Add New Connection**.
2. You’ll see a variety of integrations and data sources. If we filter for "Data Source" and search for **Snowflake**, it will appear. Click on it to install it in the top right-hand corner. 
   
   *(Note: If you already have it installed, you can skip this step.)*

3. Once installed, go to **Data Sources** where you'll see all of your data sources listed. Click on **Add New Data Source** and select **Snowflake**.

Now, we are in our configuration window. We need to enter all the relevant Snowflake details to ensure that Grafana and Snowflake can connect so we can query and explore our data.

### Gathering Snowflake Credentials

To get our relevant details and credentials:

1. Go to the **Snowflake UI**. In the bottom left corner, click on your **profile** and look at your account. 
2. Click on **View Account Details**. A modal will appear with all the relevant information we need for the enterprise data source configuration.

The first thing we need is the **account name** and **region**. 

- The account name is the name assigned by Snowflake and the URL received after the account was provisioned. It is the entire string to the left of "Snowflake Computing."
- If your Snowflake instance is not on US West 2 (which ours is on US Central 1), then the region must be included in the account name. For example, `xyz123.us-east-1`.
- If the Snowflake instance is not on Amazon Web Services, then the platform must also be included in the account name, e.g., `xyz123-us-east-1.gcp`.

### Configuring the Connection

Back in our configuration:

- We see that our profile and account indicate we are running on **us-central-1** with **Google Cloud**. 
- We will plug that in as our account name: `us-central-1.gcp`. 

Next, we need to choose our **authentication type**. There are three options: password, key pair, or OAuth. For this demo, we'll use username and password. You will need to assign your user a role in Snowflake, but any role will suffice. 

Now, let’s enter my username and password.

### Environment Details

Next, we have our environment details. This is important for scoping. For example, if you want multiple data source plugins for Snowflake, you can scope it directly to a table or a schema. 

- In this case, our role is just **public**. We can see that in our account details.
- Next, we enter our **warehouse**. This can also be found in the account details under the config file. I will use the **compute warehouse** (COMPUTE_WH).
- The database we want to select is **COMPUTER_STORE**, and our schema is **ORDERS**.

Now we have all the details we need. We can also use additional parameters if we wish. This will be the default query that shows up whenever we use this data source, along with options for interval and row limits.

Finally, click **Save and Test**. If everything is configured correctly, you will see a green "go" signal, and we can start exploring our data.

## Querying Data

In the **Explore** view, you’ll see that our default query shows up. This isn’t quite what we want, so let’s modify it.

1. Select everything from the **ORDER_ITEMS** table.
2. Since we scoped it to the ORDERS schema, we can reference the table directly without needing a longhand notation.

When we run the query, we will see all of our fields. We can format this as a table, logs, or traces. In this case, let’s format it as a table since that’s how data is stored in Snowflake.

Now, let’s create a dashboard or visualization based on this data.

### Creating a Dashboard

1. Click **Add** and then **Add a Dashboard**. This will open a new tab to create a new dashboard with this query.
2. Now, we want to visualize some sort of business outcome, such as total sales or total revenue from sales. 

In the edit panel, we can use the **subtotal** field. We will select the **SUM** of the subtotal field from the **ORDER_ITEMS**. 

If we play this, we will get a time series, but we want a different visualization type. So we’ll select **Stat**, and now we see the total sales price.

We can clean this up by changing the units to currency and adjusting the threshold. 

### Visualizing Revenue Per Product

Let’s go a step further and see the revenue per product. We can add another visualization using a **pie chart**.

1. Select the **Grafana Snowflake data source** and start a query.
2. We will select the **product name** and calculate the **SUM** of subtotal, naming it `dollars_sold`.

To group the results, we will use `GROUP BY PRODUCT_NAME`. If we run this, we will see our pie chart showing revenue per product.

### Adding Variables

We can also scope this further by adding a variable. 

1. In the dashboard settings, add a variable called **product**. 
2. The query for this variable will be `SELECT DISTINCT PRODUCT_NAME FROM ORDER_ITEMS`.

This will allow us to filter by product. However, we need to modify our queries to reflect this filtering. 

For example, in the total revenue panel, we will add a **WHERE** clause using `RLIKE` to filter by the selected product.

Now, when we select a product, our revenue will be reflected based on that choice. 

Grafana allows us to integrate visualizations from other data sources, such as Prometheus or Loki, enabling us to see both business and observability data side by side.

## Conclusion

And that’s a wrap on this video! If you have any questions, please leave them in the comments. I’ll drop the docs and everything you need to get started. 

Thank you for tuning in, and I will catch you in the next video!

## Raw YouTube Transcript

Hello, my data-driven friends, Shawn Pitts back again with another
Grafana Quickstart. In this video, we'll be connecting Snowflake to Grafana
Cloud to bring those business level insights or ETL pipelines you've built
out and bring that closer to your application and infrastructure
level telemetry. Now, like the Snowflake data source, all of our enterprise data sources are
available on every tier of Grafana Cloud, including the free plan, which
I will be using today. Now, it's also important to note that
the documentation has all the setup instructions you need, however,
this video will supplement that. So let's jump right in.
Cool. So first things first, let's jump into Grafana Cloud to
install the Snowflake data source. We'll do this by jumping to Grafana Cloud, looking for the connections tab
and clicking on Add New Connection. Now you'll see there's a bunch of various
integrations and data sources we have at Grafana, but if we filter for Data
Source and just search for Snowflake, you'll see that this appears
when we click on this, we can install it in the top
right hand corner. In my case, I already have it installed, so then we'll
just have to add it as a data source. When you do install this plugin,
it will take a few moments, so just get up, stretch
or go grab a coffee, but it should only take a few
seconds. And then once that's done, we'll go into data sources and you'll
see that all of our data sources are listed here. To add our
new Snowflake data source, we'll click add New Data
Source and click on Snowflake. You'll see this has been added and now
we are in our configuration window here. We'll have to enter in all the relevant
Snowflake details to be able to make sure that Grafana and Snowflake can
make that connection so we can query and explore our data. So to get our
relevant details and our credentials, what we'll do is we'll go into the
Snowflake ui and in the bottom left hand corner you'll have your profile. If you
click on that and then you look at the account, you'll see that
there is view account details. A modal will appear after you click
this and it'll have all the relevant information we need for the
enterprise data source configuration. So let's jump back in and we'll see that
there is an account and region that is the first thing we need.
Now, if we go into the docs, there's some important information that
we should note. First things first, the account name is the name
of the Snowflake account
assigned by Snowflake and the URL received from Snowflake
after the account was provisioned. The account name is the entire string
to the left of Snowflake Computing. If Snowflake instance
is not on US West two, which ours on US Central one, then the region must be included in
the account name. That's good to know. Example, xyz123.us-east-1.
Okay, so if the Snowflake instance
is not on Amazon Web Services, then the platform must also be
included in the account name example, xyz123-us-east-1.gcp. So if we go back into our configuration, you'll see that the profile and the
account says we're running us-central-1 and we have the Google Cloud sign,
which means we're running GCP, so we're going to need to actually
plug that in. So by doing that, we'll go and plug the account
name in directly. We'll do us-central-1, and then we'll enter in GCP. Now this actually omits
the need for the region, so you can see that below in the docs
where it says this is deprecated in favor of account, so we don't
have to worry about that. Next we have our authentication type. We have three different types for this
password key pair or OAuth. If you want to go OAuth and use something
like Azure AD for access, this is also broken down in our
documentation here with the OAuth authentication. If you want to use
key pair authentication, same deal. But in this demo we're just going
to use username and password. You'll have to assign your
user a role in Snowflake, but that is also documented as well.
We don't take any specific user role, just any. So in this case, let's enter in my
username and password here and we should be all good for that part.
Now we have our environment details, and this is important
because this scopes it. So let's say that we want to have
a multiple data source plugins for Snowflake, and maybe we want to scope it directly
to a table or a schema per se. So we have, let's say our
COMPUTER_STORE database, and under that we have our orders schema,
but you might have another schema, and let's say you only want certain
people querying that data source and then you want another team only accessing
some data. You can actually scope it that way. So in this case,
our role is just public, which we saw in our account details. So if we go back into
view account details, we can see our role is
public in this case. And then what we'll have to
do is enter in our warehouse. Now our warehouse is also
found in these account details, and you'll see here that
the warehouse is under config file and you'll see that we
can actually select the warehouse specifically. So I'm using
the compute warehouse, which is just a very basic one.
So we'll enter that in COMPUTE_WH and then the database we want to select. So the database in this case is
going to be my COMPUTER_STORE. And then that actually gives us our
database here. So COMPUTER_STORE, and then we choose our schema.
Our schema in this case is ORDERS, right?
Because if we look back here, we have our ORDERS schema right above. So now that we have all that details, we can then use additional
parameters if we so wish. Now this will be the default query
that shows up whenever we use this data source. And then you also have
your interval, your row limits. So if you only want to return a specific
amount of data so you're not abusing or you're watching out for performance,
that is also at your disposal. Now all we really have left to do here
is just click save and test and green is go. So we can start to explore this data.
So by clicking into the explore view, you'll see that our default
query shows up here, and this kind of isn't really
what we want to go with. So let's actually strip this down and
elect to select everything and we'll say from our ORDER items table.
And the reason we can do this, and we don't have to define a
longhand notation for our schema is because we already scoped it. We scoped it to the ORDER schema
in our configuration. Now, if we got rid of that, then what we'd have to do is do
COMPUTER_STORE.ORDERS.{table}, but we can just reference
the table directly, which is ORDER_ITEMS since we configured
that. So when we run the query, you're going to see that we get all of
our fields and we can format this as a time series, A table, logs
or traces. In this case, let's just do a table because it's very
simple and that's how data is stored in Snowflake. So we can see that we
get all of our relevant fields here. But let's say now we want to take this
one step further and actually create some sort of dashboard or visualization based
on this. We're going to go into add, we'll just click add a dashboard, and then we'll do open a new tab to create
a new dashboard with this query. Now, this gives us all the
relevant data we have, but maybe we want to actually see
some sort of business outcome. So let's keep this and let's
actually add a new visualization. We'll choose our data source, which is the Grafana Snowflake
data source that we can configured. And then let's start working
on a query for this. Now, if we go back into our dashboard, you're going to see that we get
this price and subtotal field. Now, let's say we want to visualize
some sort of business outcome, which is the total number of sales or
maybe the total revenue from sales. We can go into the edit panel and we know
that subtotal is going to be the field we use because let's say we
purchase two items at $130, we're going to have 260 as a subtotal, and that's what we really want to get
the total value. So we'll click on edit here, and then we'll say select. And then we're going to use
the sum of our subtotal field. And then we're going to say from ORDER_ITEMS. So now if we just play
this, we're going to get a time series, and we don't necessarily want to
use this as a visualization type. So we'll go stat and you'll see
now we have a total sales price of 54,617. Now I can clean
this up a little bit, so maybe I want to change
the standard options, which is the units to let's say a
currency like dollars in this case, which we're calculating. So now we've
kind of made this look a little prettier. Our threshold is set to 80, so
anything over 80 is going to be red, but let's just change that to green
because money's green and we like that. So the next thing we maybe want to do
is change the gradient of background. So we can go up or scroll up, and then when we see color mode,
we can see background gradient. And now this is looking a lot prettier. We name this and we'll say total revenue, we're not factoring anything else in.
And now we have all of our orders, but we also have the total revenue here.
But then we can go one step further. So let's say we want to see
the revenue per product. What we can do is we can
add a visualization here, and we're going to actually use a pie
chart because this is the best way to sort of visually represent all of our
products. So we'll go into pie chart, and then we'll go into our
Grafana Snowflake data source, and then we'll start working on our query. So we're going to actually move
this and we're going to do select, and then we'll do a product name, which is one of our columns
in our Snowflake database.
And then we'll also want to calculate the sum of subtotal
like we were doing originally, right? And we'll name this as
dollars_sold. So from here, what we'll want to do is we'll want to
add a comma because that's important for syntactical reasons. And then we'll say, give us it from the order
items table in our database, and then we'll group by the PRODUCT_NAME. And then if we run this, you're going
to see that we get just dollar sold, and that's because our pie
chart is set to calculate. We'll want to see all the
values. So now we see it here, but it might not necessarily be ordered. So we might want to even add an order
by. So we'll say ORDER BY dollars_sold and do it by DESC order. So then you'll see that we kind of
get this sort of beautiful pie chart, and then we can scroll down and we can
change the standard units again like we did in the last visualization as dollars.
So when we scroll over it, we get 8.5, 9.35K, and
now we have our pie chart. So we can say revenue per product back out of this. And then
let's just clean it up, make it a little prettier here,
and then we will expand this, and then we can save our dashboard
and we'll just save this as a sales and then we'll save it. Now what's awesome about this is we could
actually scope this a little further. So if we wanted to edit this, and then let's say we want to add or
go into settings and add a variable, what we can do is we can make a dropdown.
So when we select a specific product, it gives us all the relevant details.
And this is going to be using RegX, which we're going to show
here. So we'll do add variable, we're going to use it as a query.
We're going to name the query, it's going to be called product, and the label is going to
be product with capital P, just so it looks a little cleaner.
We're going to hide nothing. So this is actually seen in our dashboard. And then we're going to
select our data source, and we're going to say select
the distinct PRODUCT_NAME from ORDER_ITEMS. And then you'll see that
this actually runs the query in below. We get all of our values
that are returned. So we're getting all of
our distinct product names. So now what we can do is we can actually
include an all option or a multi value. And this is important because maybe
we want to see the revenue of specific products, and maybe some of 'em
are categorized the same way. So when we go back, you're going to see all of this up
here and we're going to be filtering by product. But you'll notice that
when we select the value, let's say, let's say we choose the ryzen9 5900, you're going to see that
nothing actually changes here. The reason being is because
when we filter for a product, our queries are not
actually reflecting this. So we have to change this and we have
to modify it in our panels directly. So let's go into the total revenue panel
and see what this looks like. Well, you'll see that we're just selecting the
subtotal and we're calculating the sum from the order items, but now we'll have to add a WHERE clause
to be able to filter for that RegX. So what we're going to do is we're
going to say from product name, which is what we're doing the RegX on, we're going to say RLIKE which
allows us to do a Reg X in SQL. And then we'll add our variable in
here, which will be product, which is what we named it. And then
we're going to use say, : regex if I can type. And then we'll
close that out and we'll play that. You'll see that I get a reflected
revenue based on the product I chose. So if we go back and then let's
say instead of this we choose the N-X-T-H-S 500, you'll see that
our number is now reflected. We could do this for the
other panels as well, just using that wear and that
RLIKE value on the product name. So now we see a very custom
dashboard based on our business data. And what's great about Grafana is we can
loop in other visualizations from other data sources. So let's say maybe we had Prometheus
data coming in or Loki data for logs, we can tie this directly to our business
dashboard and maybe even create tabular views in our dashboard to be able to
see both business and observability side by side. So it's pretty
amazing. And that's a video. So if you have any questions,
please leave it in the comments. I'll drop the docs and everything
you need to be able to get started. But thank you for tuning in, and I
will catch you in the next video.

