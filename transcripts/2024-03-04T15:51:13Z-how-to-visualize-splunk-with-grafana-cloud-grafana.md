# How to Visualize Splunk with Grafana Cloud | Grafana

This video provides a step-by-step tutorial on how to visualize logs and metrics from Splunk using Grafana Cloud and the Splunk ...

Published on 2024-03-04T15:51:13Z

URL: https://www.youtube.com/watch?v=2yBuGkRDSMw

Transcript: In this video, I'll show you how you can visualize logs
and metrics from Splunk with Grafana Cloud. Using the Splunk
plugin in Grafana Cloud, you can visualize observability data
from all of your different tools in a single place. First,
navigate to Grafana Cloud. Click Connect Data and search for
Splunk amongst a library of hundreds of plugins. To connect to SignalFX, now called Splunk Infrastructure
Monitoring, select this data source. In this demo, we'll connect
to Splunk Enterprise, so we'll configure a Splunk
data source. Click Install, select your organization
and click Install Plugin. The Splunk plugin requires
access to port 80 89. If you're leveraging Splunk Cloud,
follow the documentation links, which will take you directly to the
Splunk docs showing you how to configure this. In this demo, we'll
leverage a Splunk server, which is running on a private
network. To connect securely, we'll leverage Private Datasource
Connect from Grafana Cloud. First, we'll deploy a PDC agent into our network, which will communicate with Grafana
Cloud, establishing an SSH tunnel. Then, Grafana queries will be forwarded
through that tunnel and secured via Socks over SSH as they traverse the public
internet. To configure our PDC, we'll navigate back to Grafana Cloud.
Go to Private Datasource Connect, where you'll find instructions on how
to deploy and configure the PDC agent. Choose your installation
method, create a token, and deploy the PDC agent. If
you're using Splunk Cloud, configuring a PDC is not required,
and you can skip this step. To visualize metrics and logs
from our Splunk instance, we'll configure a Splunk data source. There are a number of different
authentication methods outlined in the documentation. In this demo, we'll leverage Basic Auth with
credentials and skip TLS Verify. We'll navigate over to Splunk
to create a user. We'll create a user for Grafana
and go ahead and copy and paste in our username
and password. Next, input the URL of your Splunk instance. Here you can see we're
leveraging a private URL, so we'll be sure to select
the PDC we created earlier. If you're leveraging Splunk Cloud,
you can skip this step. In this demo, we're also leveraging an optional
configuration step outlined in the documentation, enabling data links between trace
IDs and Splunk logs and our tracing platform. This makes it really easy to correlate
observability signals to speed up troubleshooting. The Splunk plugin includes dashboards
for monitoring Kubernetes environments. If you're leveraging the
Splunk OTel collector, import these dashboards to get started. Here you can see a dashboard I created
for monitoring a web application. These metrics from Splunk can help me
isolate issues to particular web servers, or I can explore the logs to
find the root cause of issues. I can filter into logs with
errors, and sure enough, looks like that server
was running out of memory. And here we can see the data
links we configured earlier, allowing us to seamlessly navigate
between observability signals, visualizing logs, and traces side
by side as we investigate further. Finally, Grafana Cloud allows us to create
dashboards like this one where I can see observability signals across
my various tools in a single place. The Splunk plugin is available
with Grafana Cloud Free Accounts. Get started with Grafana Cloud
and the Splunk plugin today.

