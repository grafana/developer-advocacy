# How to use the Alloy UI to debug pipelines | Grafana Alloy for Beginners Ep 8

Published on 2025-10-22T10:00:19Z

## Description

As our pipelines grow, so does the complexity—and debugging gets trickier. That's where Alloy UI comes in! In this episode ...

URL: https://www.youtube.com/watch?v=B-5bcVlVuMY

## Summary

In this episode of the "Grafana Alloy for Beginners" series, hosted by Lisa Jung, a Staff Developer Advocate at Grafana, the focus is on utilizing the Alloy UI to visualize and debug complex pipelines created for collecting infrastructure logs and metrics. Lisa guides viewers through accessing the Alloy UI, reviewing component health statuses, and exploring component details, including arguments and exports. The episode highlights features such as Live Debugging for real-time data inspection, a Graph page for visualizing component connections and data transfer rates, and a Clustering page for monitoring the status of cluster nodes. The episode concludes with a preview of the next installment, where Mischa will demonstrate building pipelines for application metrics, traces, and logs.

## Chapters

00:00:00 Introductions to the Grafana Alloy for Beginners series  
00:01:20 Overview of the Alloy UI and its purpose  
00:02:00 Accessing the Alloy UI in the browser  
00:02:30 Exploring the Component Detail page  
00:03:10 Reviewing component arguments and rule blocks  
00:03:50 Accessing documentation and Live Debugging features  
00:04:30 Introduction to the Graph page for visualizing components  
00:05:15 Understanding data transfer rates in the Graph  
00:06:00 Rearranging components in the Graph for better organization  
00:06:40 Overview of the Clustering page for monitoring node status  
00:07:30 Tips for debugging with the Alloy UI  

# Grafana Alloy for Beginners: Episode Overview

Hi, and welcome back to the **Grafana Alloy for Beginners** series. I'm Lisa Jung, a Staff Developer Advocate at Grafana. 

In the last few episodes, we built pipelines to collect infrastructure logs and metrics. As we add more pipelines, our configuration grows more complex, and debugging gets trickier. That's where the **Alloy UI** comes in. It helps us visualize what's happening in our pipelines so we can quickly spot issues and debug more efficiently. 

In this episode, we'll use the Alloy UI to explore and understand the pipelines we've built so far. 

## Getting Started 

Before we get started, make sure your learning environment is up and running. Go to your browser and open the Alloy UI at `localhost://12347`. 

You'll see a list of all the components that we've defined in our `config.alloy`, along with their health status. When we click on the **View** button, it will take us to the **Component Detail** page. 

This page shows the health of the component, the arguments it's using, as well as its exports. 

### Exploring Component Details

Now, when you scroll up, you'll see that this component is called `prometheus.relabel.postgres`, which is the component we defined in the previous episode. 

Let's take a look at its arguments. You'll see the three rule blocks that we defined in the last episode for the labels: **group**, **service**, and **instance**. 

You can also access the component's documentation by clicking on the button here, as well as a **Live Debugging** view. When you click on that, we see a real-time stream of telemetry flowing through a component. 

From here, we can:
- Pause and clear the data stream
- Sample data
- Disable auto-scrolling to handle heavy loads
- Search through the data using keywords
- Copy the entire data stream to the clipboard

It's a great way to inspect what's happening under the hood.

### Graph Page

Next up is the **Graph** page, which is a really helpful tool. Click on **Graph** at the top to open it. This page gives us a visual map of all our components and how they're connected. 

Right now, we see the three pipelines we built so far for collecting, processing, and exporting infrastructure logs and metrics. 

Let's zoom in on the logs pipeline. The dotted lines between components are color-coded by data type, and we can match them using the legend at the top. The number on each line shows a data transfer rate. That rate is calculated based on the window setting above. For example, a window of **10** means Alloy calculates a per-second rate over the last **10 seconds**. 

You can even drag components around to rearrange them, making it easy to organize and understand your pipeline.

### Clustering Page

Next, we have the **Clustering** page, which we can access by clicking on the option up top. A cluster node is an instance of Alloy that participates in workload distribution and ensures high availability. 

This page shows the status and role of each node, allowing us to easily see which nodes are active, their addresses, and their current state. 

### Debugging with Alloy UI

To debug using the Alloy UI, make sure all components are showing as healthy. Check that the arguments and exports for any misbehaving components are correctly configured. Use **Live Debugging** to confirm that the data flow through each component matches your expectations. 

In this episode, we used the Alloy UI to explore and better understand the state of the pipelines we've built so far. 

Up next, Mischa will show you how to take things further by building pipelines for application metrics, traces, and logs using Alloy. Stay tuned!

## Raw YouTube Transcript

Hi, and welcome back to the Grafana Alloy 
for Beginners series. I'm Lisa Jung, a Staff Developer Advocate at Grafana. In the 
last few episodes, we built pipelines to collect infrastructure logs and metrics. As we add more 
pipelines, our configuration grow more complex and debugging gets trickier. That's where the Alloy UI 
comes in. It helps us visualize what's happening in our pipelines so we can quickly spot issues 
and debug more efficiently. In this episode, we'll use the Alloy UI to explore and understand 
the pipelines we built so far. Before getting started, make sure your learning environment 
is up and running. Go to your browser and open the Alloy UI at localhost://12347. We'll see a 
list of all the components that we've defined in our config.alloy, along with its health 
status. When we click on the View button. it'll take us to the Component Detail page.
This page shows the health of the component, the arguments it's using, as well as its exports. 
Now, when you scroll up, you'll see that this component is called prometheus.relabel.postgres, 
which is the component we defined in the previous episode. So let's take a look at its arguments. 
Now, you'll see the three rule blocks that we defined in the last episode for the labels: group, 
service, and instance. And when you scroll up, you can also access the component's documentation 
by clicking on this button here, as well as a Live Debugging view. Now, when you click on that, 
we see a real-time stream of telemetry flowing through a component. From here, we can pause and 
clear the data stream, sample data, and disable auto scrolling to handle heavy loads, search 
through the data using keywords, and copy the entire data stream to the clipboard. It's a great 
way to inspect what's happening under the hood. Next up is the Graph page, which is a really 
helpful tool. Click on Graph at the top to open it. This page gives us a visual map of all of our 
components and how they're connected. Right now, we see the three pipelines we built 
so far for collecting, processing, and exporting infrastructure logs and metrics. 
So let's zoom in on the logs pipeline. The dotted lines between components are color coded by data 
type, and we can match them using the legend at the top. The number on each line shows a data 
transfer rate. That rate is calculated based on the window setting above. For example, a window 
of 10 means Alloy calculates a per second rate over the last 10 seconds. Now you can even 
drag components around to rearrange them, so it's super easy to organize and understand 
your pipeline. Next, we have the Clustering page. We can access this page by clicking on the option 
up top. A cluster node is an instance of Alloy that participates in workload distribution and 
ensures high availability. This page shows the status and role of each node, so we can easily 
see which nodes are active, their addresses, and its current state. To debug using the Alloy 
UI, make sure all components are showing as healthy. Check that the arguments and exports 
for any misbehaving components are correctly configured. Use Live Debugging to confirm that 
the data flow through each component matches your expectations. In this episode, we used the Alloy 
UI to explore and better understand the state of the pipelines rebuilt so far. Up next, Mischa 
will show you how to take things further by building pipelines for application metrics, 
traces, and logs using Alloy. Stay tuned.

