# Sneak Peek: Private Data Source Connect + Tailscale | Private Preview | Grafana Labs

Published on 2025-07-24T14:01:34Z

## Description

With a new integration between Private Data Source Connect in Grafana Cloud and Tailscale, you can now securely query private ...

URL: https://www.youtube.com/watch?v=Gqs3whtiZWQ

## Summary

In this video, David introduces the private preview of Grafana Private Data Source Connect (PDC) over Tailscale, a feature that enables secure querying of data sources on private networks without exposing them to inbound traffic. He explains that PDC is currently utilized by many Grafana Cloud customers and is accessible to all tiers of Grafana Cloud, serving a wide range of users from hobbyists to enterprises. David details how the new PDC over Tailscale simplifies connections by allowing users to query data sources directly from their Grafana Cloud instance without needing additional software. He demonstrates the process of querying a MySQL database on a Tailscale network, including generating an auth key and configuring the data source settings in Grafana. David concludes by encouraging viewers interested in accessing this feature to fill out a form linked in a blog post for further information.

# Grafana Private Data Source Connect over Tailscale Preview

Hi, my name is David, and welcome to the private preview of **Grafana Private Data Source Connect (PDC)** over Tailscale. 

PDC allows you to securely query data sources on your private network without the need to open your network to inbound traffic. Today, PDC is used by thousands of Grafana Cloud customers who query a wide variety of data sources. It is available to all tiers of Grafana Cloud, benefiting users from hobby projects and home labs to large enterprises.

Currently, the only way to use PDC is by running PDC agents in your network. These agents establish a secure connection to your Grafana Cloud stack, enabling you to query your private data sources. While the PDC agent is simple to run, any additional software creates an extra operational burden for users.

Today, Grafana Labs and Tailscale are previewing a simpler and more powerful alternative to PDC agents for those who use Tailscale to configure their private networks. **PDC over Tailscale** allows you to connect to any data source supported by a PDC running on your tailnet directly from your Grafana Cloud stack, without the need to run additional software on your infrastructure.

### Demo: Querying a MySQL Database

Let me show you what it looks like. This is my Grafana Cloud instance, and from here, I want to query a MySQL database that I have running on my tailnet. Here are the machines on my tailnet; I've got "my computer," which is where the MySQL database is running.

To query this database from my Grafana Cloud instance, I'll first need to create an auth key. I'll go to **Settings**, then **Keys**, and generate an auth key. I'll name it after my stack, make it reasonable, ensure it's set to create new in-process Tailscale servers, make it ephemeral, and add a tag for identification. After copying the key, I'll go back to my Grafana Cloud instance.

From here, I'll create a new data source, specifically a MySQL one. I'll use the machine name on my tailnet as the host name with a port. I have a sample employee database running on that instance, and I've created some authentication. 

Under the **Private Data Source Connect** section, I can click on the new Tailscale tab. I will add my stack name as a machine label, which becomes part of the machine name that Grafana Cloud adds to the machines on my tailnet. I'll paste my auth key here.

For this private preview, we need to paste the auth keys for each individual data source. You can use the same key across multiple data sources, and in future releases, we hope to have a single place to manage those keys.

After clicking **Save and Test**, this stands up an ephemeral machine on your tailnet and sends a query to it. We can then see some of the data. If we go back to the Tailscale admin console, we will notice that at least one new machine has been added by Grafana Cloud. It includes your stack identifier in the machine label, the tag from our auth key, and an ephemeral label indicating that these machines can appear or disappear at relatively short notice.

### Conclusion

This is a preview of how you can query private data sources with PDC over Tailscale. This feature will be available to all tiers of Grafana Cloud and Tailscale. 

If you're interested in getting access to this feature, please fill out the form linked in this blog post, and the team will be in touch with you as soon as possible. 

Thank you!

## Raw YouTube Transcript

Hi, my name is David, and welcome to the private preview of
Grafana Private Data Source Connect over Tailscale. Grafana Private Data Source Connect or
PDC allows you to securely query data sources on your private network without
you having to open your private network to inbound traffic. Today, PDC is used by thousands of Grafana Cloud
customers who use it to query a wide variety of data sources. PDC is
available to all tiers of Grafana Cloud, so it benefits all users from people
running hobby projects or home labs to large enterprises. Currently, the only way to use PDC is to
run PDC agents in your network. PDC agents establish a secure
connection to your Grafana Cloud stack, allowing you to query your private data
sources. The PDC agent is simple to run, but any additional software creates
an extra operational burden for users. Today, Grafana Labs and Tailscale are
previewing a simpler and more powerful alternative to PDC agents for those whose
Tailscale to configure their private networks. PDC over Tailscale allows you
to connect to any data source supported by a PDC running on your tailnet directly
from your Grafana Cloud stack without having to run any additional
software on your infrastructure. Let me show you what it looks like. So this is my Grafana Cloud instance
and from here I want to query mySQL database that I have running
on my tailnet. Here are
the machines on my tailnet. I've got this my computer machine, and that's where the
mySQL database is running. To query this database from
my Grafana Cloud instance, I'll first need to create an auth
key. So I'll go to settings, keys, and generate an auth key here.
I'll give it the name of my stack. I'll make it reasonable, which we need to be able to create
new in-process Tailscale servers. Make it ephemeral and I'll add a tag that
I created to be able to identify these machines. I'll copy that key and
I'll go to my Grafana Cloud instance. From here, I'll create a new
data source and mySQL one, I'll use the machine name on
my tailnet as the host name with a port. I have a sample employee's database
running on that database instance, and I created some authentication. And then under the private data
source connect section here, I can click on this new Tailscale
tab. I can add a machine label. I'm going to add my stack name here, and that will become part of the machine
name that Grafana Cloud adds to the machines on your tailnet, I'll paste
my auth key here. For private preview, we need to paste the auth keys in
for each individual data source. You can use the same key in multiple
data sources and in the future releases, we hope to have a single place to manage
those. So we click save and test on this, that stands up an ephemeral machine on
your tailnet and sends a query on it. And then we can see some of the data, like so. If we go back to the
Tailscale admin console now, we'll be able to see that there's at
least one new machine being added by Grafana Cloud. So it's got your stack identifier in
the machine label that we added there. It's also got the tag that
we added to our auth key, and we've got this ephemeral label
that shows you that these can appear or disappear at relatively short notice. So there's a preview of how you can
query private data sources with PDC over Tailscale. This feature will be available to all
tiers with Grafana Cloud and Tailscale. If you're interested in
getting access to this feature, please fill out the form
linked in this blog post, and the team will be in touch with
you as soon as we can. Thank you.

