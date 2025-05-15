# How to Visualize and Explore Your Datalake: Databricks Enterprise Data Source for Grafana

Ready to bring your Databricks data lakehouse to life? In this Grafana quick start, Shawn Pitts walks through how to connect ...

Published on 2025-05-13T18:38:40Z

URL: https://www.youtube.com/watch?v=Qc83dSVe0vQ

Transcript: Hello, my big data friends, Shawn Pitts back again with another
Grafana Quickstart. In this video, we're going to be showcasing how to
get up and running very easily with the Databricks plugin for Grafana Cloud. Now, it's important to note if we look
here that the Databricks plugin, along with all the other enterprise data
source plugins are available across all tiers of Grafana Cloud,
including the cloud free plan, which we'll be using today. So whether you are just getting started
or you're already running production workloads, it's really super easy to
get started. So let's jump in. Cool. So first things first, we're going to have to jump into
Grafana and install the plugin. First thing we'll do here is we'll go
into the left-hand navigation menu and then go down to connections
and add a new connection. In here you'll see that there's
all the plugins integrations, and we are just going to search
for Databricks. When you see this, you're going to click it, and if you have an enterprise license
or the enterprise plugins enabled, you can see that there'll be an install
option. In the top right hand corner, you can see that I already have
this installed on my account, so no worries there. We're just
going to add a new data source. So now we have a new data source created, but we've got to fill in all
the relevant information. So you'll see that there's host HTTP
path and then the authentication type, which is a personal access token. So the real question is how do
we get this inside of Databricks? So let's jump into Databricks. And you can see here that I'm rocking
with a light theme on both Grafana and Databricks. Does that make
me a psycho? I don't know. But ultimately what we'll do here
is you can see we have a table with expected stats. I have some CSVs
as well as Databricks giving us some system metrics such as the
billing and compute information. So maybe we want to visualize that
and bring it closer to our telemetry. So how do we do that? Well,
we go into the compute, and this is where we're going to get
our connection details for the Grafana Databricks plugin. So we'll go into just our starter
warehouse that we're running, our SQL warehouse, and we'll
go into connection details. You'll see that there's a server host
name here. So we're going to copy that, we'll pop that into the host,
and then we'll get our HTTP path, which is right here, and then we'll need
to generate a personal access token. It's actually pretty convenient because
in Databricks you can just create a personal access token directly from here. We'll open that up in a new tab
and we'll generate a new token. So we'll just say for visualization,
and we can set a lifetime of this. Let's just say I want to do 30
days. So we'll generate this token. It'll give you at one time, make sure to copy it and put it
somewhere safe because if not, you'll lose it and you
won't have it anymore. So then we just jump back in and we're
going to use this personal access token. There are also alternative options
such as the OAuth pass through OAuth M two M and the Azure on behalf of. So you can select those if you
want. We'll click save and test, and you'll see that this
might just take a few minutes, but it should just take a few seconds
and it'll say the data source is working. So now we can actually jump into the
explore view and start to look at our Databricks data. So in here you'll
notice that we have a very easy plug and play option for creating
queries. We see our scheme is here. So if we go back into Databricks
this lines with what's in our org. So if we look at the default
information schema and MLB, the default and information schema
are going to be there out of the box. But the MLB is a custom schema that
I created. If we go into explore, we click on MLB. You can see that we
have a table called Expected Stats. In here I really have all the players
from the 2024 MLB season and all their statistics. If I pull this, you'll see that it actually
creates an SQL query for me, so I don't have to do this. You can
write your own custom code here, so it'll automatically convert
it over into the code section, but we'll show you how to do this when
it comes to the compute and billing information that you want to see inside
Databricks. So let's jump into the builder. We'll run this query and you can see that
we get the name of all of our columns or the column full name from our
expected stats table and Databricks. So now what if we want to create
a dashboard for this? Cool. So taking this Databricks data that we
just queried for and putting it into a Grafana dashboard is
actually quite simple. All we have to do is click add in the
top right hand corner and click add to a dashboard. We're going to open this
up in a new tab in a new dashboard, although we could inject it into an
existing dashboard. So let's do that. Now you can see that we get our existing
explore query into a panel here. Let's stretch this out and then
let's go into the edit tab. Okay, we'll move myself over a little bit
so we can actually see this. And you can see now that we are
looking at this data, however, we want to look at everything
that comes along with it. Right now we're only looking at the full
name, but what else do we get with it? So when we run this query, our table's going to change
and give us all the columns. So now we can see batting
average lugging percentage, and maybe that's what I want to visualize. Maybe I just want to see the full name
of the player and the batting average. I want to filter out the rest of this
crap. So we can actually do a select, we'll do a full name for the column, and then we'll also add another
one and add the batting average. We'll run this query again, and now you
can see that we only have two columns. Maybe we want to visualize
this in something else than
a table. Tables are cool, but maybe we want to make it a little
prettier so we can do a bar chart. You can see that a bar chart is a pretty
good way of representing the data here. We can see that Aaron judges query
heating the wig right now with the biggest bar. However, this may not be the best way because
you can see our x axis is a little messy and all these are very squished together. So what if we choose a horizontal
orientation for our X axis? You're going to see that Now
this shifts over a little bit, so now everything's on the X axis. So if we go back to the dashboard
and stretch this out a little bit, you can see now that all of our
players really fit here, which is nice. If we want to go back into the
edit and maybe make this prettier, we can scroll down and choose the gradient
mode to be hue. And now we have quite a pretty visualization of all the batting
averages from 2025 of the players. So now we can save this real quick and
we can just make this a new dashboard. We'll call this MLB stats
and we'll save this. So now we have our dashboard and we can
continue to add visualizations here. But one thing I wanted to show you was
how do you get something like billing data from Databricks? So what
if you want to see, okay, how much is my SQL warehouse costing me? How much are my compute
resources costing me? Well, it's actually quite simple as well.
We just have to write custom queries. And since the plugin
accepts the SQL editor, we can write custom SQL queries
for this. So let's click edit. We'll click add, and we'll
add another visualization. Let's make this a table just for the time
being. And then we're going to have to choose our data source again. So let's
look up the Databricks data source. And you can see again that we're probably
going to not want the MLB scheme in this case. So what do we
actually want to get? Well, if we look back into the Databricks ui, you can see that there is the
information or the system catalog. And then under here we get a bunch
of stuff like the compute resources, like the warehouses. Maybe we want to see billing information
such as the usage and so forth. So how do we actually get that data and
how do we write the SQL query for it? Well, what we're going to do is we're going
to jump back into the edit panel. We're going to grab a query that
allows us to do so. And in this case, I'm going to be honest, I use
Claude to generate this for me, but you can see that we're selecting the
usage date and we're representing it as a time field. We're taking the billing
origin product and making it a product field. And the same thing, we're
calculating usage quantity, which is just another column that's
giving us the actual usage quantity. And then we're naming this total usage, and we're getting this from
the system billing usage. So if you go back into here, we can see
that we'll look at system billing usage. That's what we're getting, right? And
then we're grouping it by the usage date, the billing origin product, and
we're ordering it by the usage date. So whenever I change this, essentially what's going to happen is
we're going to get the correct data for it. So let's run this. We'll
run it for the last hour. This might just take a moment. And you can see now that we get
the per product, the total usage. Now these are in different units, so we might actually want to
eventually get the units along with it. So if we go back into the catalog explorer
and maybe we're looking at the usage and we look at all of the
data that comes along with it, it gives us the comment
of what each field means. So maybe we want to get
the usage unit as well. So let's grab that and let's
throw it into our panel. We'll just say usage unit as unit. Awesome. And then we'll add this group
as well. So now when we run this query, you'll see that now we get our unit. So we have DBUs here for the SQL
and interactive. And in this case, the SQL is our SQL warehouse. And if you are curious about how
the Databricks billing works, you can look at the product
SKUs for Databricks, and there's actually a
pretty good representation
of all the SKU groups so you can see how everything reflects. And this is a great way to bring
cross telemetry into Grafana. So if you want to view the
billing and usage of Databricks, if you want to view MLB player
stats all in one dashboard, or maybe you want to bring in the
logs from another data source, you have it all unified in one
view. So thank you for tuning in. I hope you got a lot out of this video,
and I'll catch you in the next one. Take it easy.

