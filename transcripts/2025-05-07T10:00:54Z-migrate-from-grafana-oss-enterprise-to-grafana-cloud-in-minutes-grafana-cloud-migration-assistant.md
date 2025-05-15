# Migrate From Grafana OSS/Enterprise to Grafana Cloud in Minutes | Grafana Cloud Migration Assistant

Generally available in Grafana 12, the Grafana Cloud Migration Assistant is a powerful yet intuitive tool designed to streamline ...

Published on 2025-05-07T10:00:54Z

URL: https://www.youtube.com/watch?v=SeNIN0rd6cg

Transcript: Hi, my name's Daniel. I'm the product
manager for the Grafana Enterprise team, and today we're excited to announce
the general availability of the Grafana Cloud Migration Assistant. A powerful yet intuitive tool designed
to streamline your migration journey, moving your existing Grafana instance
to Grafana Cloud just got dramatically simpler. I have a local Grafana Enterprise instance
set up where we're going to attempt to migrate the contents to a
target Grafana Cloud instance. The first step is to locate the
migration assistant found under the administration section of your instance. We now need to enter a migration token, which we'll retrieve from the
cloud stack. In the next tab here, I've spun up a Grafana Cloud stack
on which I have in the light theme. If we take a look at the dashboards, we can see it's shipped with the
standard set of Grafana Cloud dashboards. And if we go over to the
data sources section, we already have the standard set of
Grafana Cloud data sources that have been pre-installed. The migrate to cloud
page contains the ability to generate a migration token. We can do
that right here. Take a copy, and we're going to copy this back
into our local Grafana Enterprise instance. This establishes a secure connection
between the local enterprise instance so that we're able to upload
resources to the cloud instance. We've added a new resource
selector on this snapshot page, so previously it included all
resources within the instance. Now you'd have the ability to pick
specific resources to upload to Grafana Cloud. Since this is the first time
we're going to be running the migration, we're going to include
all and build snapshot. This is going to take a copy of all the
resources that we have on this local instance. You can see
that we have 72 in total, and this consists of a number of plugins. I've set up a very simple
alerting rule along with folders and dashboards as well. Next step is to upload the snapshot. You can see that the resources
are updating the status in real time. So, so far we've got 44 resources that
have been successfully migrated. Great. Now we've reached
the end of the process. The migration has successfully completed, and you can see we have 72 out of
72 resources successfully migrated. In Grafana 12, we've also added the capability to
sort through the resources table so you can sort by type, name and status. And we've also added a new filter
in the top that allows you to view only errors. In this particular
case, everything uploaded successfully, so we don't see any errors
when applying this filter. Going back to the cloud instance, we can check whether we successfully
migrated the resources over. If I refresh the dashboard page, great. You can see that we have
a number of folders, including dashboards which
have successfully migrated. Let's take a look at the alert rule. We can see this has been
successfully migrated too. Notice that the state is
in paused. So by default, the alerting rules will be migrated to
the cloud instance in a pause state. This is to allow users to pick and choose
which alerting rules that they wish to test within the cloud instance,. Primarily is to avoid double
notifications from both your self-managed instance and the Grafana
Cloud instance. This is configurable, so when it comes to the time when
you are cutting over and naturally transitioning from your
self-managed instance to cloud, you can migrate all of your alert
rules in the original alert state. Let's check out the data sources next. So you can see that we've successfully
migrated the Postgres data source, which was on our local
instance. Critically, this all includes the
username and password, so all the credentials are taken care
of by the migration assistant. Let's go down here and just quickly
test the connection, and we've got confirmation that
the database connection is okay, and you can continue to build out your
dashboard and explore your data within your cloud instance. Earlier I mentioned I set up an alert
rule that was actually for monitoring Grafana, where I'm pulling out Grafana metrics
into a local Prometheus instance. This was actually migrated to the
cloud instance as well. My colleague, Mitch Seaman does a demo around
Private Data Source Connect, which explains how you can connect
your local databases to cloud instances. So do check that out in
an earlier public preview video. And then finally, let's look into
the plugins that were installed. Great. We can see that the Zabbix plugin was
installed on the cloud instance along with the Snowflake Enterprise plugin. So I've just taken you through the process
of copying over resources from your local enterprise instance and
successfully migrating those to cloud. Do check out documentation
that we have around this. And if you've already made the
decision to transition to cloud, go ahead and try out the
migration assistant today. We'd love to hear your feedback.

