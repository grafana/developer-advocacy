# Grafana Learning Journeys: Send metrics to Grafana Cloud using Prometheus remote write

Published on 2025-07-09T17:11:26Z

## Description

This video is part of the Grafana Learning Journeys, and it walks you through how to send metrics to Grafana Cloud using ...

URL: https://www.youtube.com/watch?v=BDJO-vC-gEw

## Summary

In this video, Antonio provides a tutorial on how to send metrics from Prometheus to Grafana Cloud using the Prometheus remote write feature. He explains that Prometheus is an open-source monitoring system that collects time series metrics from various targets. Antonio discusses the benefits of using remote write, such as simplicity and flexibility, and emphasizes that it doesn't require significant changes to existing configurations. He walks viewers through verifying that Prometheus is running, configuring it to send metrics to Grafana Cloud, and checking the setup for successful data transmission. The video aims to help viewers visualize their system metrics effectively using Grafana Cloud.

# Monitoring Your System with Grafana Cloud and Prometheus

Do you want to know how your machine, web app, or entire fleet of servers is doing? Do you want more than just phone numbers? What if I told you that you could monitor your system metrics with dashboards, graphs, and maybe even alerts? If that sounds like you, then stick around!

Hey there, I'm Antonio, and in this video, I will show you how to send your metrics to Grafana Cloud using Prometheus remote write. 

## What is Prometheus?

First, let's talk about what Prometheus is. Prometheus is an open-source monitoring system that collects and stores time series metrics by scraping targets like applications, services, and infrastructure. 

Just so you know, this isn't the only way to bring Prometheus data into Grafana Cloud. In another Learning Journey, we show you how to connect to a Prometheus data source directly without sending or storing the data in Grafana Cloud. Both Learning Journeys are linked below, so if you're watching this on YouTube, check the video description for more details.

You can send Prometheus metrics to Grafana Cloud without making significant changes to your existing configuration. 

## Why Use Prometheus Remote Write?

Now, let’s take a quick look at why you might want to use Prometheus remote write in the first place. There are a few different ways to send Prometheus metrics to Grafana Cloud, but using remote write has some clear benefits, especially if you want to keep things simple and flexible.

- **No New Installations**: If you already have Prometheus running, remote write means you don't have to install anything new like Grafana agents. 
- **Testing the Waters**: If you're just testing the waters with Grafana Cloud, remote write is perfect. You can start sending data without making big changes to your current configuration. 
- **Selective Data Management**: If you're trying to be selective about what data goes where, remote write lets you filter and send only the metrics you care about while keeping everything else stored locally in your Prometheus instance. This is especially useful for managing cost or data privacy.

## Verifying Prometheus Installation

The next thing we want to do is verify that Prometheus is installed and running as a service. This ensures Prometheus starts automatically when your machine reboots, so you don't have to manually start it each time. 

We also want to confirm that it's capturing metrics. When you installed Prometheus, you likely also set up Node Exporter. This exporter allows Prometheus to collect system-level metrics such as CPU usage, memory consumption, and disk space by exposing them in a format that Prometheus can scrape.

To check if both Prometheus and the service are running, open a terminal and type:

```bash
systemctl status prometheus
```

This command will inform you whether the process is running and if the service is active. If you are on Windows, a similar command is:

```bash
sc query prometheus
```

Finally, to ensure that Prometheus is capturing metrics, we can send a request to the metrics endpoint. It should return a number of metrics and metadata about the metrics being exposed.

## Configuring Prometheus for Remote Write

Now that we have verified that Prometheus is up and running, let's walk through how to actually configure it. This is the main part of the setup, and don’t worry, we will take it step by step.

To enable remote write, you will need to add a small code snippet to the Prometheus YAML config file. This snippet comes directly from your Grafana Cloud account and tells Prometheus where to send metrics and how to authenticate securely.

1. **Log into your Grafana Cloud portal** and select your stack.
2. On the left-hand navigation panel under Grafana Cloud, click the name of your stack. 
3. In the Prometheus tile, click "Send Metrics." 
4. Scroll down to the section labeled "Sending Metrics with Prometheus." You will see a code snippet here. This is what you will paste into your Prometheus config file. 
5. Just below that snippet, click "Generate Now" to create a new API token. This token is what Prometheus will use to securely connect to Grafana Cloud. 
6. On the "Create an API Token" screen, enter a name for your token and click "Create Token." The code snippet will now auto-populate with your new API token. 
7. Click "Close" and then click "Copy to Clipboard" just below the snippet.

Now it's time to add that snippet to your Prometheus configuration. 

1. **Log into the machine where Prometheus is installed.**
2. Open a terminal and, if necessary, switch to a user with write access. 
3. Locate and open the Prometheus file, usually found at `/etc/prometheus`.
4. Use your preferred text editor, like Vim, Nano, or Notepad if you're on Windows. In my case, I'm on Ubuntu and I'm using Nano.

Scroll down to the bottom of the file and copy in the code snippet. Mind the indentation when pasting code; YAML is sensitive, and bad spacing can break the file. Finally, save and exit your editor. If you're using Nano, press `Ctrl + X`, then type `Y` and hit `Enter` to write and quit.

Lastly, restart Prometheus to apply the changes. On Linux, type:

```bash
systemctl restart prometheus
```

Once restarted, Prometheus will begin forwarding metrics to Grafana Cloud using the configuration you just added. 

## Confirming Metrics are Streaming

To verify that everything's working, you can check the service status again:

```bash
systemctl status prometheus
```

Your Prometheus instance is now set up to send metrics to Grafana Cloud. 

So, how do you know it's actually working as the final step in this journey? Let's confirm that the metrics are coming through. 

1. In Grafana Cloud, navigate to the left-hand menu and click "Drill Down."
2. Then, select "Metrics." You should see something similar to this:

If everything's connected correctly, you should see live Prometheus metrics right here in the Drill Down Metrics app, just like what's shown on the screen.

And that's it! Your Prometheus metrics are now streaming to Grafana Cloud and ready for visualization, alerts, and more. 

Thanks for watching!

## Raw YouTube Transcript

Do you want to know how your machine, web 
app, or entire fleet or servers is doing? Do you want more than just phone numbers? What if I told you that you could monitor your system metrics with dashboards, 
graphs, and maybe even alerts? If that sounds like you, then stick around. Hey there, I'm Antonio and in this 
video I will show you how to send your metrics to Grafana Cloud 
using Prometheus remote. write. But first, what's Prometheus? Prometheus is an open-source monitoring system. It collects and stores time series metrics 
by scraping targets like application, services, and infrastructure. Now, just so you know, this isn't the only way to bring 
Prometheus data into Grafana Cloud. In another Learning Journey, we show 
you how to connect to a Prometheus data source directly without sending 
or storing the data in Grafana Cloud. Both Learning Journeys are linked below. 
So if you're watching this on YouTube, check the video description for more details. You can send Prometheus metrics to Grafana Cloud without making significant changes 
to your existing configuration. Now let's take a quick look at why you might want 
to use Prometheus remote write in the first place. There are a few different ways to send Prometheus 
metrics to Grafana Cloud, but using remote write has some clear benefits, especially if you 
want to keep things simple and flexible. For starters, if you already have 
Prometheus running, remote means you don't have to install anything new 
like Grafana alloy or other agents. Maybe you're just testing the waters with 
Grafana Cloud. In that case, remote is perfect. You can start sending data without making 
big changes to your current config. And if you're trying to be selective 
about what data goes where, remote guide lets you filter and 
send only the metrics you care about while keeping everything else stored 
locally in your Prometheus instance. That's especially useful for 
managing cost or data privacy. The next thing we want to do is verify that 
Prometheus is installed and running as a service. This ensures Prometheus starts 
automatically when your machine reboots, so you don't have to manually start it each time. We also want to confirm 
that it's capturing metrics. By the way, when you installed Prometheus, 
you likely also set up node exporter. This exporter allows Prometheus to collect 
system level metrics such as CPU usage, memory consumption, and disk space by exposing 
them in a format that Prometheus can scrape. To check if both Prometheus 
and the service are running, open a terminal and type 
systemctl status prometheus. It should inform us whether the process 
is running and if the service is active. If you are on Windows, a similar 
command is sc query prometheus. Finally, to ensure that 
Prometheus is capturing metrics, we can send a request to the metrics endpoint. It should return a number of metrics and 
metadata about the metrics being exposed. All right, now that we have verified 
that Prometheus is up and running, let's walk through how to actually configure it. This is the main part of the setup and 
don't worry, we will take it step by step. To enable remote write, you will need to add a 
small code snippet to Prometheus YAML config file. This snippet comes directly from 
your Grafana Cloud account and tells Prometheus where to send metrics 
and how to authenticate securely. Log into your Grafana Cloud 
portal and select your stack. On the left hand navigation panel under 
Grafana Cloud, click the name of your stack. In the Prometheus tile, click send metrics. Scroll down to the section labeled 
sending metrics with Prometheus. You will see a code snippet here. This is what 
you will paste into your Prometheus config file. Just below that snippet, click 
generate now to create a new API token. This token is what Prometheus will 
use to securely connect to Grafana Cloud. On the create an API token screen, enter a 
name for your token and click create token. The code snippet will now 
auto-populate with your new API token. Click close and then click copy to 
clipboard just below the snippet. Now it's time to add that snippet 
to your Prometheus configuration. Log in the machine where Prometheus is installed. Open a terminal and if necessary 
switch to a user with right access. Locate and open the Prometheus file 
usually found at /etc/prometheus. Use your preferred text editor like Vim, 
Nano, or Notepad if you're on Windows. In my case, I'm on Ubuntu and I'm using Nano. Scroll down to the bottom of the 
file and copy in the code snippet. Mind indentation when pasting code.
YAML is sensitive. Bad spacing can break the file. And finally, save and exit your editor. If you're using nano, press Ctrl X, then 
type Y and hit enter to write and quit. Lastly, restart Prometheus to apply changes. On Linux, type systemctl restart prometheus. Once restarted, Prometheus will begin forwarding metrics to Grafana Cloud using 
the configuration you just added. To verify that everything's working, 
you can check the service status. On Linux, type systemctl status prometheus. All right, your Prometheus instance is now 
set up to send metrics to Grafana Cloud. So, how do you know it's actually working 
as the final step in this journey? Let's confirm that the metrics are coming through. In Grafana Cloud, navigate to the 
left hand menu and click drill down. Then select metrics. You should see something similar to this. If everything's connected correctly, you 
should see live Prometheus metrics right here in the drill down metrics app 
just like what's shown on the screen. And that's it. Your Prometheus metrics are now 
streaming to Grafana Cloud and ready for visualization, alerts, and more. Thanks for watching!

