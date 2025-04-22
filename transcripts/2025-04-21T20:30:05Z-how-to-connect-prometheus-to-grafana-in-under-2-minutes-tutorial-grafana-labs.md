# How to Connect Prometheus to Grafana in Under 2 Minutes | Tutorial | Grafana Labs

In this step-by-step tutorial, we'll walk you through how to get Prometheus and Node Exporter running locally on an ARM64 Mac ...

Published on 2025-04-21T20:30:05Z

URL: https://www.youtube.com/watch?v=8sqW-W1Rjyc

Transcript: First, let's open the browser. Go to
Prometheus io. Click on the downloads tab. We want to download the last stable build. We scroll down and pick the ARM64 install, since we're running a MacBook
Pro with an M3 chip. Scroll down, find the node exporter. Same deal.
Download the last stable build. We open our terminal of choice, change in to our downloads directory
and split the terminal vertically. We'll need one pane to run node
exporter and one to run Prometheus. To unpack these we'll use simple
tar commands. No surprises there. Let's first launch the node
exporter in the background. This should be easy and
will start exposing metrics
immediately on port 9100 for us, but anyway, we can get around this by just going
into the privacy and security tab in our system settings, and just clicking
the allow anyway button. Run again, open anyway. Enter password,
and you're all good. To scrape these node exporter
metrics, we need to use Prometheus. Let's change the config file.
Let's open this up in cursor and add a new job under our scrape
configs to capture the metrics coming from the node exporter. Now that
we have our job in place, we can go back and actually run
Prometheus. Now, the fun part, open up grafana.com. If you
don't already have an account, you can create one very easily for free. If you do sign in or access your account,
then launch your Grafana Cloud stack. Navigate to data sources. Click add,
new data source, choose Prometheus. We can see the data source has
been added. Let's name this. Since our Prometheus instance is
running locally and is insecure, we'll need to find a way to secure it. You can see that this won't work when
we enter in the HTTP localhost:9090. To get around this, we'll use
a free tool called the ngrok, which will provide us a secure
URL tunneling to localhost:9090, where our Prometheus instance
is running. From here, we'll just simply copy the ngrok URL,
paste it into our Prometheus survey, RL, scroll down, save, and test,
and we should be all set. We can successfully
query the Prometheus API. Now to verify these metrics are coming in. Simply go into dashboards and we
can look at our note exporter. We can see that all of our metrics are
coming in and that we're getting CPU network traffic, memory, and so forth.

