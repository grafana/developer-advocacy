# Grafana Alerting Overview Plus New Features Coming to Grafana 12 | Grafana Labs

In this walkthrough, Grafana Labs' Ryan Kehoe dives into the biggest improvements designed to help teams create, manage, and ...

Published on 2025-05-02T01:01:17Z

URL: https://www.youtube.com/watch?v=NsFVxXTMbUc

Transcript: Hi, I'm Ryan Kehoe and I'm excited to talk
to you today about all the great changes we've made in Grafana Alerting
leading up to Grafana 12. Grafana alerting is a powerful
and flexible engine that
allows users the ability to customize their experience and ensure
all their resources and services are actively monitored. Throughout
Grafana 11 versions, the Grafana alerting team is at a heavy
focus in simplifying the alert creation process while automating
unnecessary actions. We want to ensure both new and
existing users of Grafana have a great experience. On top of making
alerting easier to use, we've invested heavily in ensuring our
platform has a reliability in features that enterprises need to
run Grafana at scale. Today, I'll walk through some highlights as
we tour Grafana. So let's jump in. Grafana Alerting provides users with
the tools and expressions needed to make extremely complex multi-data
source queries. For new users, these options can be daunting. They're simply coming in and looking
to make a basic CPU or storage alert. We've moved a lot of these options that
are not commonly used under the advanced options slider. Users have the ability
to select multiple data sources, as well as multiple expression steps
and recovery thresholds for their alert rule. Another area that users struggle with
is routing alert notifications to the correct contact point. Grafana
Alerting uses label matching, which takes the labels on an alert
rule, as well as the alert instance, combines them, and then traverses a notification policy
tree to find the correct contact point to notify. In many cases, users simply want to send alerts
to a single contact point. Under the basic options, users can select the contact
point directly in the alert rule, and Grafana alerting will automatically
manage the notification policy for them. For users that still want
to use label matching, they can simply select advanced options
to set the alert rules to route via label matching instead of selecting a
direct contact point. On top of making it easier for users to create alert rules, we've made it easier for users
to view their alert rules. We've revamped the alert details view to
pull up critical information that users need to the top level so they no longer
have to dig through the alert rule to find that information. Information
such as the query in their threshold, the alert instances in their status, the history of their alerts firing, detailed information about the alert
and the new feature that was added in Grafana 11.6: The version
history of the alert. Version history of the alert allows users
to view all the different versions of an alert rule, who made
those updates and when, as well as compare versions
with each other. And finally, restore previous versions of the alert.
Whether you're a data source alert user looking to move to Grafana managed
alert rules for the enterprise features, or you're a Grafana managed alert
user looking to copy out-of-the-box integration data source
rules, starting in Grafana 12, users can import Data Source alert
rules into Grafana managed rules. First, click the import to Grafana managed
rules button in the data source managed area. Collect the data source that has the
data source rules you would like to copy over. Collect your target folder for the
new Grafana managed alert rules to be created into, select the data source rule, namespace, and group. You also have the option
to pause the alert rules on copy to ensure they don't start
firing and give you time to adjust and massage the data. You can also pause recording
rules that get copied over, as well as select the data source that
you would like your Grafana managed recording rules to be created into.
When you're all done, click import. Review the new alert rules and recording
rules that would be created and confirm your import. You'll notice
that the new folder has been created. New alert rules as well as recording
rules will be created as well, and they will be paused.

