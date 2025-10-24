# Alloy Configuration Language 101 | Grafana Alloy for Beginners Ep 3

Published on 2025-10-15T10:33:46Z

## Description

Configuring Grafana Alloy doesn't have to feel like cracking a secret code! Join Lisa Jung and Mischa Thompson from Grafana ...

URL: https://www.youtube.com/watch?v=fN0uwuwm1Fo

## Summary

In this episode of the "Grafana Alloy for Beginners" series, host Lisa Jung, a Staff Developer Advocate at Grafana, introduces viewers to the configuration language used in Alloy to build data pipelines. She explains the concept of components, which are the individual tasks Alloy performs, and how they are organized by ecosystem to manage different functions such as data discovery, processing, and export. Lisa uses the Prometheus components as an example to illustrate how to specify and customize tasks, including scraping and relabeling data. She emphasizes the importance of the documentation sections—usage, arguments, and blocks—for effectively setting up components. The episode concludes with a preview of the next session, which will focus on setting up the learning environment to see the Alloy configuration in action.

## Chapters

Sure! Here are the key moments from the livestream with their corresponding timestamps:

00:00:00 Introductions to Grafana Alloy for Beginners  
00:01:30 Overview of what Alloy is and its purpose  
00:02:15 Explanation of components in Alloy  
00:03:00 Description of different functions performed by components  
00:04:00 Introduction to Prometheus components and their uses  
00:05:15 Breakdown of the prometheus.relabel component  
00:06:30 Detailed explanation of how to customize components  
00:07:45 Navigating the Alloy documentation for components  
00:09:00 Key sections to focus on in the docs: usage, arguments, and blocks  
00:10:30 Preview of the next episode on setting up the learning environment

# Grafana Alloy for Beginners: Episode Overview

Hi, welcome back to the Grafana Alloy for Beginners series. I'm Lisa Jung, a Staff Developer Advocate here at Grafana. 

In the last episode, we discussed what Alloy is and when it makes sense to use it. In this series, we'll learn how to configure Alloy to build data pipelines. Just like learning a new language, we'll start by getting familiar with key jargon and syntax used in Alloy configurations, and that's exactly what we'll cover today. 

Think of Alloy as our trusty pal who can collect, process, and export our telemetry data. To tell Alloy how we want that done, we write instructions using a language—the syntax that Alloy understands. Imagine we're writing a set of instructions for Alloy to follow; each individual task in those instructions is called a **component**. 

The components are grouped by **ecosystem** to keep things organized. You can find a link to this page in the resources section of the repo. Under each ecosystem, we find components that handle different functions. Generally, components perform one of the following functions:

- Discover targets or expose data from a known target.
- Scrape or receive data.
- Process data.
- Export data to its destination.
- Handle miscellaneous tasks, such as reading a file and exposing its contents to other components or fetching more Alloy configuration from a remote source.

Essentially, our pipelines will be built by combining components that manage these tasks. To understand what a component does, just look at what comes after the ecosystem name. 

### Example: Prometheus Components

Let's take the Prometheus components as an example. When we want to get metrics ready and share them with other Alloy components, we use the **exporter**. To scrape data, we turn to the **scrape** component. If we need to relabel data, the **relabel** component is the one for the job. And when it's time to export the data, we use components like **remote_write** or **write.queue**, and so on. 

The components tell Alloy exactly how to collect, process, and export telemetry data. Like LEGO blocks, we can mix and match these components in any way to build a pipeline in Alloy that fits our needs. Each task or component can be further broken down into a detailed set of instructions. 

### Focus on the prometheus.relabel Component

Let's take a closer look at the **prometheus.relabel** component. This component is designed to process metrics. Like all components, it receives data from somewhere, does something to that data, and then sends it off to the next destination. Here, we specify exactly how we want to process that data, and with the **forward_to** field, we define where the data should be sent next. 

Breaking down the same component even further:

1. **Component Name**: Identifies the component.
2. **Label**: Helps distinguish it from others.
3. **Instruction**: We use either an argument (a key-value pair) or a block to instruct Alloy on what to do with the data. 

We can customize a block even more by sending attributes to expressions. If needed, we can create nested blocks within blocks to get really specific. 

### Configuring Our Pipeline

To configure our pipeline, we will use the components pages in the documentation. To access this, go to the Alloy docs, click on **Reference**, then **Components**, and finally choose the ecosystem we are working with. 

To set up our components properly, keep an eye on three key sections in the docs:

- **Usage**: Shows how the component is structured and provides a solid starting point for our setup.
- **Arguments**: Details how we can further customize our actions with the data.
- **Blocks**: Another method to configure Alloy to meet our needs.

As we write our configurations, pay close attention to the type, description, defaults, and required categories so that Alloy understands what we're asking it to do. 

In this episode, we covered the basics of the Alloy configuration language. Next up, we'll set up our learning environment so we can see firsthand how Alloy configuration works in action. 

Thanks so much for watching, and I'll see you in the next episode!

## Raw YouTube Transcript

Hi, welcome back to the Grafana Alloy for Beginners
series. I'm Lisa Jung, a Staff Developer Advocate here at Grafana. In the last episode, we talked 
about what Alloy is and when it makes sense to use it. In this series, we'll learn how to 
configure Alloy to build data pipelines. And just like learning a new language, we'll start 
by getting familiar with a key jargon and syntax used in Alloy configurations, and that's exactly 
what we'll be covering today. So think of Alloy as our trusty pal who can collect process and 
export our telemetry data. To tell Alloy how we want that done, you write instructions using 
a language, the syntax that Alloy understands. So imagine we're writing a set of instructions 
for Alloy to follow. Each individual task in those instructions is called the component. 
The components are grouped by ecosystem to keep things organized. You can find a link to 
this page in the resources section of the repo. Now, under each ecosystem, we'll find components 
that handle different functions. Generally, components perform one of these functions shown 
here. Depending on what we're working with, we'll use components that discover targets or 
expose data from a known target. Some components scrape or receive data, others process it, and 
some export it to where it needs to go. There are also miscellaneous components that do all sorts 
of things like reading a file and exposing the contents to other components or fetching more 
Alloy config from a remote source. Basically, our pipelines will be built by putting together 
components that handle these different tasks. To understand what a component does, just 
look at what comes after the ecosystem name. Let's take the Prometheus components as an 
example. When we want to get metrics ready and share them with other Alloy components, we 
use the exporter. To scrape data, we turn to the scrape component. If we need to relabel data, 
the relabel component is one for the job. And when it's time to export the data, we use components 
like remote_write or write.queue, and so on. The components tell Alloy exactly how to collect, 
process, and export telemetry data. Like LEGO blocks, we can mix and match these components 
in any way to build a pipeline in Alloy that fits our needs. Each task or component could 
be further broken down into a detailed set of instructions. So let's take a closer look at 
the prometheus.relabel component. This one is designed to process metrics. Like all 
components, it receives data from somewhere, do something to that data, and then sends it 
off to the next destination. Here, we specify exactly view how we want to process that data. 
And with the forward_to, we define where the data should be sent next. Let's break down the same 
component even further. First, there's a component name. Then we add a label to help distinguish 
it from others. Next, we use either an argument, which is a key value pair or a block to instruct 
Alloy exactly what we wanted to do with the data. We can customize a block even more by sending 
attributes to expressions, and if needed, we can create nested blocks within blocks to get 
really specific. So we'll use the components pages in the docs to figure out how to configure our 
pipeline. To get there, we go to the Alloy docs, click on reference, then components, and finally 
choose the ecosystem that we're working with. To set up our components properly, keep an eye on 
three key sections in the docs: usage, arguments and blocks. The Usage section shows us how the 
component is structured and gives us a solid starting point for our own setup. The Argument 
section shows how we can further customize what we want to do with the data. As we write our 
configurations, pay close attention to the type, description, defaults, and required categories 
so Alloy understands what we're asking it to do. The same goes for blocks. They are another way 
we can configure Alloy to do what we need. So focusing on these three things will point us in 
the right direction as we configure our pipeline. In this episode, we cover the basics of 
the Alloy configuration language. Next up, we'll set up our learning environment so we 
can see firsthand how Alloy configuration works in action. Thanks so much for watching, 
and I'll see you in the next episode.

