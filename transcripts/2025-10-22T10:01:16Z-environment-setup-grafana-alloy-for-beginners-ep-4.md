# Environment Setup | Grafana Alloy for Beginners Ep 4

Published on 2025-10-22T10:01:16Z

## Description

Ready to dive into Alloy and start building observability pipelines? Join Lisa Jung and Mischa Thompson from Grafana Labs as ...

URL: https://www.youtube.com/watch?v=fZRwVwCvLAg

## Summary

In this episode of the Grafana Alloy for Beginners series, hosted by Lisa Jung, the focus is on setting up a learning environment for hands-on practice with Alloy. The architecture of the learning environment includes a four-service application comprising a server, requester, recorder, and a Postgres database, all designed to generate telemetry data. Alloy collects and exports this data to databases like Loki, Tempo, Mimir, and Pyroscope, with visualization through Grafana dashboards. Lisa guides viewers through the installation of Docker Desktop and Docker Compose, cloning the series repository, and configuring the environment for application observability. She concludes by previewing upcoming episodes that will delve into building pipelines for infrastructure logs and metrics.

## Chapters

00:00:00 Introductions to the Grafana Alloy for Beginners series  
00:01:15 Overview of the learning environment architecture  
00:02:00 Explanation of the four services: server, requester, recorder, and Postgres database  
00:03:30 Introduction to telemetry data collection and processing with Alloy  
00:04:15 Instructions to access the series repo for the Learning Environment Setup  
00:05:00 Guide to installing Docker Desktop and Docker Compose  
00:06:00 Verifying Docker Desktop is running  
00:06:30 Cloning the learning environment repository  
00:07:15 Running the learning environment with the make run command  
00:08:00 Overview of the config.alloy file for building pipelines  

# Grafana Alloy for Beginners: Episode 2

Hey there! Welcome back to the Grafana Alloy for Beginners series. I'm Lisa Jung, a Staff Developer Advocate here at Grafana. 

In the last episode, we explored the key jargon and syntax for configuring Alloy. Today, we're diving into setting up our learning environment where all the hands-on practice will happen throughout the series. 

## Learning Environment Architecture

Here's a snapshot of our learning environment architecture. We have a four-service application, which consists of:

- **Server**
- **Requester**
- **Recorder**
- **Postgres Database**

The requester makes the HTTP requests to the server, which exposes the REST API and uses a database. The recorder service stores messages on an AMQP bus, while the Postgres database stores and retrieves data. 

Each service comes instrumented to generate metrics, logs, traces, and profiles. Alloy steps in to collect, process, and export telemetry data to relevant databases such as Loki, Tempo, Mimir, and Pyroscope. Finally, we'll use the Grafana dashboard to visualize and explore all that data.

## Getting Started

We'll be using this environment to learn how to use Alloy. To kick things off, open the series repository and scroll down to the **Learning Environment Setup** section. The link to the repo is included in the description of this video.

Next, we'll install Docker Desktop and Docker Compose using the links provided. Make sure that Docker Desktop is up and running by opening its app. After that, we'll clone the repository for the learning environment. 

To do so, copy this command, go to your terminal, paste, and run the command. Then, navigate into the project directory and use the `make run` command to start the learning environment. Afterward, open the project using a text editor of your choice. 

Once you get there, expand the **alloy** folder, then open the `config.alloy` file. This is where we'll be building our pipelines for both infrastructure and application observability, and we’re all set to go.

## Conclusion

Alright, we've just set up our environment. Over the next three episodes, we'll configure Alloy to build pipelines for infrastructure logs and metrics. 

Thanks for watching! See you in the next episode.

## Raw YouTube Transcript

Hey there. Welcome back to the Grafana 
Alloy for Beginners series. I'm Lisa Jung, a Staff Developer Advocate here at Grafana. In 
the last episode, we explored the key jargon and syntax for configuring Alloy. Today, 
we're diving into setting up our learning environment where all the hands-on practice 
will happen throughout the series. All right, so let's get started. So here's a snapshot 
of our learning environment architecture. We have a four service application, which consists 
of the server, requester, recorder, and a Postgres database. The requester makes the HTTP request 
to the server. The server exposes the rest API, and uses a database. The recorder service stores 
messages on an AMQP bus and the Postgres database stores and retrieves data. Now each service 
comes instrumented to generate metrics, logs, traces, and profiles. Alloy 
steps in to collect, process, and export telemetry data to relevant databases 
such as Loki, Tempo, Mimir and Pyroscope. Finally, we'll use the Grafana dashboard 
to visualize and explore all that data. We'll be using this environment to learn 
how to use Alloy. To kick things off, open the series repo and scroll down to the Learning 
Environment Setup section. The link to the repo is included in the description of this video. 
Next, we'll install Docker Desktop and Docker Compose using the links provided here. Now, make 
sure that the Docker Desktop is up and running by opening its app. Afterwards, we'll clone the 
repo for the learning environment. To do so, copy this command here, go to your terminal, 
paste and run the command. Then navigate into the project directory. Then use the make run command 
to start the learning environment. Afterwards, we'll open the project using a text editor of your 
choice. Now, once you get there, expand the alloy folder, then open the config.alloy file. So this 
is where we'll be building our pipelines for both infrastructure and application observability, and 
we're all set to go. Alright, we just set up our environment. Over the next three episodes, 
we'll configure Alloy to build pipelines for infrastructure logs and metrics. Thanks 
for watching. See you in the next episode.

