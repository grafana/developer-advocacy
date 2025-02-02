# Grafana 11.5: Faster and Easier Migration to Grafana Cloud | Support for Plugins and Alerts

Updates to the Grafana Cloud Migration Assistant: Plugins and Alerts! ☁️   Thinking about moving to Grafana Cloud? Whether ...

Published on 2025-01-29T17:35:04Z

URL: https://www.youtube.com/watch?v=iBTmOhXbNoU

Transcript: Hi, I'm Daniel. I'm the product manager
for the Grafana Enterprise team, and I'm thrilled to share some exciting
updates about the Grafana Cloud migration assistant. Whether you're an OSS user exploring
Grafana Cloud or an enterprise customer transitioning large deployments, the migration assistant simplifies and
accelerates your migration journey. Let's dive into the latest features. Now, the migration assistant supports seamless
migration of all data sources and plugins, including credentials
and configuration settings, so you can hit the ground
running with your cloud instance. Let's perform a quick migration to
demonstrate plugins being migrated from a local enterprise instance to a
cloud instance in a few easy steps. This tab contains my
Grafana Enterprise instance, where I've already set up a number
of dashboards and installed a couple of popular plugins where we're
going to demonstrate the migration process. So there's a popular Zabbix plugin, which I've already installed
alongside the Enterprise Snowflake plugin. We're going to navigate now
to a Grafana Cloud instance, which I've recently set up. So in here we're going to take
a quick look at the currently existing dashboards. There's
a couple of demo dashboards, which are installed, and we're going to
quickly take a look at the plugins, which are installed
on the cloud instance. So in here you can see the Zabbix plugin doesn't currently exist as
installation within cloud, and the Snowflake plugin
is also not present. So the first step of the migration
process is we're going to navigate to the migrate to cloud page and
generate a migration token. We're going to copy this into
our local enterprise instance. Enter the details here. This is going to create a secure
connection between the local enterprise instance and the Grafana Cloud stack. And the next step is we're
going to build a snapshot. This is going to take a copy of
all of the supported resources by the migration assistant, and it's going to copy those into a
snapshot, which it stores locally. So we can see here the presence
of the Zabbix plugin alongside Snowflake. And we also earlier
prepared a Postgres data source that contains some
credentials to an active Postgres database within
an AWS environment. And you can see here we also have
a number of dashboards listed in the snapshot, along
with folders as well. The final step of the process
is to upload the snapshot. This is going to establish a secure
connection between our local enterprise instance and the Grafana Cloud instance, and securely copy the snapshot and resources to the Grafana Cloud instance. So we can see we've just
had a status update. All of the line items show that
we've successfully uploaded them to cloud, and we can go navigate back
to the cloud instance to review the results. Just navigating into the dashboard
page, I'm going to refresh this. Great. You can see that the
dashboards made their way into the instance, oh,
that's a Grafana Cloud. But we can see here
infrastructure monitoring, which was on the enterprise instance,
were successfully copied over. If we navigate over to the plugins, check for the installed plugins, now we can see we successfully
migrated the Zabbix plugin alongside the Enterprise Snowflake plugin as well. If we just quickly jump
over to data sources, the first entry, you can see that we also successfully
migrated the Postgres data source that we had set up on the enterprise instance. This contains the connection
details along with the database name. And you can see here we also
successfully migrated the username and password as well. So this particular data source is
up and running within the cloud instance, enabling end users to quickly
explore data or build a dashboard. Next up is streamlined alerting migration.
Migrating Grafana alerting resources is now easier than ever. With just a few clicks, you can
transfer all your alert rules, contact points and notification
settings securely to the cloud, saving you time and effort. Plus, with the new Alert Rules
State configuration option, you can migrate alert rules in a
pause state to prevent duplicate notifications. This allows you to review and test
your alerts in cloud before finalizing migration. We're excited to see how these updates
simplify your transition to Grafana Cloud. Try out the migration assistant
today and experience a faster, more secure migration. For more details, check out our documentation or
reach out to our team for support.

