# How To Visualize Your Sales Data: Salesforce Enterprise Data Source for Grafana

Published on 2025-08-21T13:10:36Z

## Description

Learn how to monitor your organizations sales performance by connecting Salesforce with Grafana! In this quick-start tutorial, ...

URL: https://www.youtube.com/watch?v=9GdSAKuyti4

## Summary

In this Grafana Quick Start video, the presenter provides a detailed tutorial on connecting Salesforce to Grafana to enhance sales performance analysis. The video covers the step-by-step process of setting up a connected app in Salesforce, including enabling OAuth settings and configuring necessary credentials such as the consumer key and secret. The presenter emphasizes that the Salesforce data source is accessible to all tiers of Grafana Cloud and offers guidance on how to pull Salesforce data into Grafana using SOQL queries and the query builder. Throughout the video, practical examples are demonstrated, such as querying opportunity data and visualizing sales metrics on dashboards. Viewers are encouraged to comment with questions for further clarification.

# Grafana Quick Start: Connecting Salesforce with Grafana

Hey everyone! Welcome back to another Grafana Quick Start. Today, we're diving into one of the most powerful ways your team can understand sales performance: by connecting Salesforce with Grafana. I'll be taking you step by step through the entire process, from setup to pulling your Salesforce data into Grafana, so your organization is no longer flying blind. Let's get started!

## Prerequisites

Before we jump in, I want to mention that the Salesforce data source is available to all tiers of Grafana Cloud, which means that any free or paid Grafana Cloud plans have access to this, as well as any activated on-prem Grafana Enterprise licenses.

## Creating a Connected App in Salesforce

First, we need to create a connected app in Salesforce. Here’s how to do this:

1. In Salesforce, click on the gear icon in the top right-hand corner and select **Setup**. This will open a new tab in your browser.
2. On the left-hand side, look for **Platform Tools**. Under this, you'll see a dropdown for **Apps**. Here, you'll find options like App Manager, Marketplace, Connected Apps, and External Client Apps.
3. Navigate to **External Client Apps**. Under **Settings**, ensure you toggle on **Allow Creation of Connected Apps** (you need admin access for this).
4. Click on **New Connected App**. This will bring you to the configuration menu for your new connected app.

In the configuration menu:

- **Name your connected app** (e.g., "Demo for Grafana"). The API name will auto-fill once you click out of it.
- Provide a **Contact Email** (this field is mandatory).
- Enable **OAuth Settings** (this is crucial because the Grafana data source supports two forms of authentication: credentials or JWT flow). For this tutorial, we’ll use the basic credentials flow.
- Note that the Salesforce data source uses the OAuth 2.0 username-password flow. 

Next, you’ll need to fill out a **Callback URL**. This can be any valid URL (e.g., `https://localhost`). Just make sure to enter something, as it is a mandatory field.

You do not need to toggle on **Use Digital Signatures** or any of the other optional settings. 

For **OAuth Scopes**:

- Look for **Manage User Data via APIs** and add it to your selected OAuth scopes. 
- You don’t need to enable any of the client credential flows or the refresh token flow.

Once everything looks good, click **Save**. Keep in mind that changes can take up to 10 minutes to take effect.

## Configuring Grafana

While the changes are taking effect, let’s start setting up the configuration in Grafana:

1. In Grafana, go to **Data Sources** and click on **Add New Data Source**.
2. Search for **Salesforce**. If it's not already installed, you’ll need to install it.
3. Once installed, click **Add New Data Source**. Name it "Salesforce" and enter your credentials.

### Finding Your Credentials

To find your Salesforce credentials:

- Click on your profile picture in the top right-hand corner of Salesforce and select **Settings**. Your username will be there.
- You’ll also need your password. If you don’t have a **Security Token**, you can reset it by going to **Settings** > **Personal Information** and clicking **Reset My Security Token**. This will send you an email with a new token.

Next, you’ll need the **Consumer Key** and **Consumer Secret**:

1. Go back to the App Manager in Salesforce.
2. Click **View** next to your connected app.
3. In the managed consumer details, you’ll find the **Consumer Key** and **Consumer Secret**.

Paste these credentials into Grafana, select your environment (e.g., Sandbox), and check that the data source is connected.

## Exploring Your Data

Now, let’s jump back into Grafana to explore your data. In the left-hand navigation menu, click on **Explore**. You’ll see all your data sources at the top; select your Salesforce data source.

In the query editor, you’ll find:

- **SOQL Editor:** A standardized way of writing SQL queries in Salesforce.
- **Query Builder:** A user-friendly point-and-click option for creating queries.
- **Reporting Tab:** Pull in existing Salesforce reports directly into Grafana.

### Running a Query

As an example, let’s look at the Opportunity entity:

1. Select all fields without any filters.
2. Limit this to 100 results and run the query.

If you want to drill down further, you can add a filter (e.g., closed opportunities) to see specific data. 

### Visualizing Data

To visualize the data:

1. Add the results to a dashboard.
2. Change the visualization type (e.g., from table to graph).
3. Aggregate the data (e.g., sum of amounts) and set the unit to currency (e.g., dollars).

You can see how much revenue has been generated over a specific period, allowing you to visualize your sales data effectively.

## Conclusion

That’s it for this video! Thank you for tuning in. I hope you now understand how to get up and running with the Salesforce Enterprise data source in Grafana. If you have any questions, please feel free to comment below. 

I’ll catch you all in the next video. Take it easy!

## Raw YouTube Transcript

Hey everyone. Welcome back to
another Grafana Quick start. Today we're diving into one of the most
powerful ways your team can understand sales performance, which is by
connecting Salesforce with Grafana. I'll be taking you step by step through
the entire process from setup to pulling your Salesforce data into Grafana,
so your orgs no longer flying blind. Let's get started. Okay, so
before we get right into it, I just want to add that the Salesforce
data source is available to all tiers of Grafana Cloud, which means any free or paid Grafana
cloud plans have access to this as well as any activated on-Prem Grafana
Enterprise licenses. Alright, so now we need to create a connected
app in Salesforce. How do you do this? Well in Salesforce, you go into the gear icon in the top
right hand corner and click on setup. This will open up a new
tab in your browser, and then on the left hand side you'll
see a bunch of different options. Yet again, when you see platform tools under
there, you'll see a dropdown for apps, and here you'll see app manager,
the marketplace connected apps, external client apps, lightning bolts, etc. And this can kind of be overwhelming, but essentially all we need to know
here is the external client apps and the connected apps. What you do is you go into external
client apps and under settings, if you're an admin, which
you'll need to be, in this case, you'll see that there's the
allow creation of connected apps, and this might be toggled off. You'll want to toggle this on and then
you'll want to click on new connected app Here, you'll be brought
to the configuration menu
for your new connected app right here. We will
name our connected app, and I'm just going to call
this demo for Grafana, and this will automatically fill in
the API name. Once I click out of it, you'll want to give your contact
email because that's mandatory, and then all the rest of the
options are actually optional, so you don't have to do anything there.
Next, you'll see that there's the API, which is to enable OAuth settings. This is super important because the
Grafana data source actually provides or offers two forms of authentication. That
is through the credentials or JWT Flow. In this case, we're just going to
use the basic credentials flow, but the documentation also supports JWT. So go take a look at that if that's
how you want to configure it. It's also important to note that the
Salesforce data source uses the OAuth 2.0 username-password flow. So you'll see that there's also a
callback URL in the configuration menu for your connected app, and
that's actually not utilized, so you can set it to any valid URL.
For example, you could literally set it
to HTTPS, a localhost, right? It really doesn't matter, so
fill that out, whatever you want, but you do have to put some sort of
callback URL because that's a mandatory field. Next, you'll see that
there's used digital signatures. You don't need to toggle that on. Then you'll want to select your
OAuth scopes. Now, this has changed. In the old version of Salesforce, you would've seen something like access
and manage your data in parentheses API. They actually switch that permission. So now what you'll want to do
is you'll want to go down to manage user data via APIs, and
then it'll be in parentheses APIs. You'll want to click on that and you'll
want to add it to your selected OAuth scopes. It's actually all you need. Next, you'll see that there's a bunch of
different options like enable client credential flows, require secret for
refresh, token flow, web server flow, PKCE. You actually don't
need any of these toggled on. You can enable the web server
flow or the refresh token flow, but you don't have to.
That's completely optional. The rest of what you're
looking for is really all defaulted, right? So you don't
need to add any more configuration. We can just click save in this case and
you'll see that it says changes can take up to 10 minutes to take effect. Deleting a parent org also de
deletes all connected apps, all auth settings enabled.
We'll quick continue, and then this will take
just a few minutes. So like it says almost 10
minutes to really take effect, but what we can do is we can start to
set up the configuration for this in Grafana. Now, to find the data source
in Grafana to start configuring this, we'll go into Grafana and
under the data sources, we'll click on add new data source
and we'll look for Salesforce. Now, if Salesforce
isn't already installed, what you'll do is you'll
go into the connections, you'll do a search for Salesforce, and then you'll need to install that.
Now, I already have this installed, so I'm just going to quick
add new data source From here, it would've been the same flow if I went
into data sources and added one there. We're just going to call this Salesforce, and then we're going to start getting
up and running with our credentials. So we'll need to enter in our credentials, and if you're wondering
where you can find this, you can find this by going into Salesforce
in the top right hand corner and clicking on your profile picture and then
clicking on settings under your name. Now in here you'll see that there's
personal information and your email and username will
actually be there as well. So your username is what you're going
to need for Grafana. We'll go into username, pop that in there, and then you'll need your password for
how you actually log into Salesforce. So go my password, and then
we'll need our security token. Consumer key and consumer secret. This is where things get a little bit
interesting. So the security token, you might have one, you might not, and
if you do need one, what you can do, this is pretty easy. You just go into your view profile and
Salesforce in the top right end corner, you click on settings. This will bring you to your
personal information dropdown, and you'll see that there's a
reset, my security token option. You'll reset your security token. This will actually send you an email
with the new security token you need. I'm going to click to
reset my security token, and then this will send me a new token
in my email. I'm going to go into Grafana and I'm going to paste that
into the security token field. And then I need to get my consumer key,
which is my connected app, consumer key, and then my connected app Consumer
Secret. How do I do this? Well, we'll jump back into Salesforce and
where we were in the setup with all the apps, and we'll go under App Manager.
We'll go in here and we will click on view. In view. You'll see that there is
a consumer key in secret. We'll click on the
managed consumer details, and then this will actually send you
another email to verify your identity. This will then bring you to all the
managed connected app details you need, so the consumer key and
the consumer secret. We'll grab both of those credentials
and we'll actually pop those into Grafana, and then we will
choose our environment, which in this case is a sandbox for me, and you'll see that the data source
is working and connected. Okay, so now let's jump right back into
Grafana and start to explore this data. If you go into the left-hand
navigation menu and click on explore, you'll see that there are all
of our data sources at the top, and we can select from this, we'll look
for our Salesforce one specifically, and then you'll see that we have a bunch
of different query types and sort of this rich editor for the
Salesforce data source. You'll see that there's SOQL editor, which is sort of the standardized way
in Salesforce to writing SQL queries. So if you want to pull something
very custom, you can do so. We also have the easy to use query
builder, which is more point and click, and you can just choose from
a bunch of dropdown items. And then we also have the reporting tab. So if you've already created some reports
in Salesforce and you want to pull those directly into Grafana, you can. So let's just jump back into
the query editor and we'll do something simple, right? We'll
look at the opportunity entity and we'll just select all the
fields. We want to get everything back. We'll add no filters, we won't order by
anything. We'll limit this to a hundred, and then we can run this query. If we maybe wanted to then drill
down further, we can add a filter, and then we can look at something
like closed, or actually, let's look at if one is true, and then
this will show us all of our one deals. So maybe we want to track how much
money we've brought in or revenue we've brought in the last quarter per se. So we'll want to look at that data and
then we can start to visualize that. So maybe we want to add,
then add this to a dashboard. We'll just click open in a dashboard, and then maybe what we'll want
to do here is change this. So we'll go into the edit tab. We'll
make this, let's say a stab, right? And you'll see that there's a bunch of
different data points that we get now, and let's say we maybe want
to aggregate this, right? So let's do the sum and then
we'll get the sum of amount, and we will just mark this as total
count. So we'll still filter by one, but you can see now that this is
the amount of data or the amount of money that we've essentially
brought in throughout the quarter. Now what we can do is
we can change the unit. So if we wanted to do something like
a standard unit and click on currency, we can do dollars, and you can see
that we brought in $54.6 billion, which is a crazy amount of money.
This is all fake dummy data, but essentially this is how you can
start to visualize your sales data, and if you want to pull in data about
your sales team, you can do that as well, because there's going to be entities for
that in Salesforce. So that's a video. I want to thank everyone for tuning in. I hope you understood and got how to
get up and running with the Salesforce Enterprise data source.
If you have any questions, please feel free to comment below and
I'll catch you all in the next video. Alright, take it easy.

