# Visualize any CSV File with Grafana

Getting started with Grafana requires a basic understanding of how dashboards, datasources, and queries work.  In
this post, we'll go through a complete worked example of using Grafana to visualize any CSV file anywhere on the web.

We will:

1. Create a datasource that connects to the data
2. Create a dashboard that visualizes a query
3. (Optional) create a transform to change the CSV before visualizing it
4. Visualize the resulting data

This will give you all the concepts you need to build any kind of dashboard with Grafana.

![Dashboard Component Architecture](https://grafana.com/media/docs/grafana/dashboards-overview/dashboard-component-architecture.png)

## Create a Datasource

In the left hand navigation of Grafana, select "Connections > Data Sources".  Click the "Add a new Data source" button
in the top right corner.  Then, enter "Infinity" as the data source type.

**Note**: do not select the CSV plugin; while there is a plugin under that name, Infinity is much more flexible, actively maintained, and will give you super powers you'll learn about later in this post.

![Add Infinity Connection](img/1-add-datasource.png)

After you click the Infinity tile, you will arrive at this screen, which will prompt you to name the data source.

![Name your Datasource](img/2-name-datasource.png)

The default name is `yesoreyeram-infinity-datasource`, which we will keep for this example, but you can name it whatever you like.  This screen has the option to configure a lot of access parameters for any endpoints online; for example, if
you needed to provide a bearer token to access CSV at some endpoint, you could configure that in the Authentication section.

Click "Save and Test"

![alt text](image.png)

We'll be using a public dataset, so we can simply continue without customizing anything further.  

In Grafana, every data source comes with a _Query Editor_ that lets you specify what data you want. The data source is
a plugin that controls how the data is fetched.  The Infinity datasource lets you flexibly fetch any resource, from any
endpoint online that uses HTTP/HTTPS.

## Create a Dashboard

Using the lefthand nav, click "Dashboards".  In the resulting list, look for the "New" button in the upper right, and click "New Dashboard".

![Create Dashboard](img/4-create-dashboard.png)

You'll land on an empty dashboard, which will prompt you to add a new visualization.  Let's start with a simple 
table, showing CSV data.  Click the "Add Visualization" button.

![Pick datasource](img/5-pick-datasource.png)

To create a visual in Grafana, we need to know where the data is coming from and what data it is.  So select the 
`yesoreyeram-infinity-datasource` datasource we created previously.
