# Grafana Learning Journeys: Connect to a Prometheus data source in Grafana Cloud

This video is part of the Grafana Learning Journeys, and it walks you through how to connect to a Prometheus data source in ...

Published on 2025-04-23T14:28:02Z

URL: https://www.youtube.com/watch?v=_ojYThjkpN0

Transcript: Welcome to the Prometheus 
data source Learning Journey. My name is Antonio, a developer 
advocate here at Grafana,   and I'm here to walk you through 
connecting Prometheus as a data source. Prometheus is an open- source 
metric-based monitoring system   that collects and stores time series data. With Grafana Cloud data source connections you can 
visualize data directly from where it is stored,   meaning that the data itself is not 
sent to nor stored in Grafana Cloud. On the other hand, if you already have 
a Prometheus setup, and you actually   want to send metrics to Grafana Cloud, 
where they will be stored and managed,   check out the Prometheus remote 
write learning journey instead. Before we dive in though, take a look 
at the "Before you begin" section,   and make sure that you have 
set up a private connection   to your Prometheus data source, 
and have the PDC agent running. We recommend this approach so your data 
and queries aren't exposed to the internet.  This is covered in a separate Learning 
Journey which you can find in that section.  Once you're set up, I'll see 
you in the next milestone. Before we get started, why 
would you want to connect   to a self-managed data source in Grafana Cloud? Here are a few reasons. The first reason is cost. If you are sending large amounts of metric 
data to Grafana Cloud and cost is a concern,   a self-managed option might be better. Compliance: if regulations 
require you to keep data on-prem. Custom configurations: If you want to 
configure things exactly how you need. Retention needs: Grafana Cloud retains metrics 
for 13 months. If you need longer retention,   a self-managed solution might be ideal. Internal management: if your team prefers 
full control over your metrics environment,   a self-managed setup gives you that flexibility. if your metrics are stored and 
managed in another platform,   connecting directly to your 
data source keeps things simple. Lastly if you're using a different metrics backend 
and don't want to switch to Prometheus or Mimir,   a self-managed approach lets 
you keep your current setup. Ultimately, it comes down to your 
cost, compliance and retention needs. If any of these apply to you, a self-managed 
data source connection might be the best fit. And now that you know when opting for 
a self-managed data source make sense,   let's kick this off by making sure 
that your environment is ready. The first thing we want to do is verify that 
Prometheus is installed and running as a service. This ensures Prometheus starts 
automatically when your machine reboots,   so you don't have to manually start it each time. We also want to confirm 
that it's capturing metrics. By the way, when you installed Prometheus, 
you likely also set up Node exporter. This exporter allows Prometheus to collect 
system level metrics such as CPU usage,   memory consumption, and disk space, by exposing 
them in a format that Prometheus can scrape. To check if both Prometheus 
and the service are running,   open a terminal and type systemctl 
status prometheus.service. It should inform us whether the process 
is running and if the service is active If you are on Windows, a similar 
command is sc query prometheus. Finally, to ensure that 
Prometheus is capturing metrics,   we can send a request to the metrics endpoint. It should return a number of metrics and 
metadata about the metrics being exposed. All right, now that we have verified 
that Prometheus is up and running,   let's add it as a data source in Grafana. First, login to your Grafana Cloud account. Now, look at the top left corner 
and click on the Grafana logo.  This will open the main menu. From here click on connections to 
go to the data sources section. Next click add new connection. In the search bar type: Prometheus. Then select Prometheus data 
source from the results. Once you have done that, click add new 
data source in the top right corner. Finally give your data source a name. Keep in mind that this name will 
appear in your visualization,   so choose something meaningful that 
helps you easily identify it later. Next, we will enter the Prometheus server URL.  This URL points to the machine where 
Prometheus is running and collecting data. The exact URL depends on your setup. If Prometheus is running locally, 
you will use a local host address. If it's hosted on a server within your network, 
you will use that server's internal address. If it's running as a container alongside Grafana,   you might need to use the appropriate 
container network address. Or, if you are not connected via a 
Private Data source Connection (PDC),   Prometheus must be accessible via a public 
IP or a fully qualified domain name. In this Learning Journey, I 
have access to the Prometheus   data source because I have already set 
up a private data source connection. If you need guidance setting up a PDC, 
check out the dedicated Learning Journey. That said, since I have my PDC set up, I should 
be able to reach Prometheus on port 9090. Then, if you scroll down a little bit, 
you will reach the authentication section. If you have configured Prometheus 
to require authentication,   enter your Basic Auth credentials here. Otherwise, you can skip this step. Next, we select an active PDC and 
test the connection to Grafana Cloud. Think of PDC like an encrypted SSH 
tunnel that allows Grafana to query   your Prometheus server securely without 
exposing it to the public internet. if successful, you should 
see a message saying that   you have successfully queried the Prometheus API. Now that our connection is working, 
let's check out some real data. To do that, open the main menu, 
and then go to Drilldown > Metrics. Here, you should see a list of 
available Prometheus metrics. If everything is setup correctly, your 
screen should look like something like this. And that's it! Thanks for watching, 
and see you in the next one.

