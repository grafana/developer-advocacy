# Grafana 11.3 Now GA! Here&#39;s the TL;DR | Grafana

Welcome to Grafana 11.3! Scenes-powered dashboards are now generally available and the Explore Logs plugin is now installed ...

Published on 2024-10-22T20:19:00Z

URL: https://www.youtube.com/watch?v=a0rdRbYPCls

Transcript: Grafana 11.3 is out, and
here's what you need to know. We've got a new Explorer Logs app that
lets you visualize your logs with Loki, but without using LogQL. Scenes-power dashboards to give you an
easier and more flexible way to create dashboards, experimental actions to fire off
these HTTP requests from dashboard elements. And we made some
nice improvements to alerting,
the plugin ecosystem, and the overall administration of your
Grafana instances. Let's dive right in. Explore Logs is a new app for Grafana
that addresses one of the most difficult things about browsing and analyzing logs
from Loki - having to learn the query language. With Explore Logs, we automatically spot patterns in your
log data and just show you prebuilt dashboards of log information so that
you don't have to build them yourself. You can drill down by service
and spot problems faster. Explore Logs is generally available
for Grafana Cloud Enterprise and OSS. It's enabled in Grafana 11.3 by default, and you'll also need to use Loki version
3.2 to be able to use it for more information on that as well. As a
run through on what it looks like, I did a community call here
with my colleagues, Jay
Clifford and Trevor Whitney, all about Explore Logs. Jumping on over to dashboard
and visualization improvements. We've got Scenes-powered dashboards. Now. Scenes is a framework that we initially
introduced to make the building of plugins a little bit easier, but we've taken that framework and we've
brought it over to dashboards so that you can do things like flip
between view mode and edit mode. So you can go into edit mode when
you're creating or building a dashboard, and then go to the view mode so that
you can see your dashboard in a less cluttered way. You also have now template variables and
the time range picker sticking to the top as you scroll down
through a dashboard. We've got a time zone
parameter in the Grafana URL. So now when you share a dashboard, you can already have a time zone
selected and now a kiosk mode displays dashboard controls while you're playing
a playlist or while you're viewing a dashboard in full screen.
Next up is Actions. Now this is really cool because what this
means is that when you're interacting with elements on a dashboard, you can
now have that correspond to an action. This action could be, for example, an HTTP request that opens up a
GitHub issue based on a problem that you've spotted or you can
use it to call any API. So there's lots of possibilities
for things that you can do here. It is available for these
visualizations, but it is experimental, so you will need to enable the vizActions
feature toggle to be able to use it. Let us know what you think. Some other dashboard improvements in this
release are auto formatted table cell values and cell inspect, plain text and code editor tabs when
inspecting table visualizations. There are now legends in bar gauge
visualizations and the ability to apply binary transformations to all
numbers in a table at once. We've also been working on
alerting in this release. We've simplified the query
section for creating new alerts, but you can still switch back to advanced
options for creating more complex rules. This is generally available, it will roll out to Grafana
Cloud over the next few weeks. And if you're using enterprise
and OSS versions of Grafana, you'll need to enable the alerting
query and expression step mode feature toggle. Now in the future, we're
trying to improve this even more. We wanna make it so that alerting is so
easy to set up that you don't have to be an expert in Prometheus to either
make or respond to an alert. So we're looking at
things like consolidating
Grafana-managed alerts and data source alerts to a single alert
type. Just to avoid confusion, we wanna automate evaluation
groups. So in the future, all you need to do is to set a
polling period for the Alert Rule, and we really want stronger integration
with other Grafana Labs projects. So stay tuned on more features
on alerting in the future. We've got a couple changes
in the plugin ecosystem. The GitHub data source now allows you
to authenticate via a GitHub app rather than just a personal access token. This gives you better security
and allows you finer grain control over permissions. And this is available
already for all versions of Grafana. We've also begun the redesign of the
plugin details page within Grafana. We've added when plugins
were last updated, but there's so much more that
we wanna do here. In general, we wanna make it easier for
you to manage your plugins, so we want you in the future to be able
to do things like raise feature requests or bug reports, or have lots of options for supporting
your favorite plugin developers. So more to come on this, but for now
it's in public preview. To see us off, here's some new features for
administration and security. You can now display these customizable
banners that are perfect for announcements, like important
updates or maintenance schedules, and you can control who gets to show
these banners using role-based access control. This is in public preview for
Grafana Enterprise and Grafana Cloud, and you'll need to enable the
feature toggle notification banner. Also in public preview is a
new UI for configuring LDAP, but you'll need to enable the
feature toggle, SSO settings LDAP, and that's a wrap for 11.3. For more
details on anything I mentioned, check out the links in
the description below. I'll also add a link to the What's New
page for this release so you can go over all of the information there in text. And if you just can't get enough of
Grafana news and who can blame you, then go ahead and check out this
keynote from our recent conference, ObservabilityCON, where a bunch of us go over all of
the things we're working on across the Grafana stack. Thanks for watching.

