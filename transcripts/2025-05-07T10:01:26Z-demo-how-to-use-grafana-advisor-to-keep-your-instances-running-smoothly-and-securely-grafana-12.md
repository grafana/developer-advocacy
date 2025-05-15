# Demo: How to Use Grafana Advisor to Keep Your Instances Running Smoothly and Securely | Grafana 12

Grafana 12 introduces Grafana Advisor, a new tool to help admins detect misconfigurations, deprecated plugins, and unhealthy ...

Published on 2025-05-07T10:01:26Z

URL: https://www.youtube.com/watch?v=o84EfY-KP-c

Transcript: Hi, I am David, the group PM for plugins, and today I'd like to showcase a new
feature called the Grafana Advisor. So the advisor is designed to help Grafana
server administrators to keep their instances running smoothly, securely,
and in keeping with best practices. It gives you a centralized view of the
pressing issues that are requiring your attention and other more informational
checks for things which you should investigate. The advisor lives within the
administration section of the Grafana UI, and we provide links from both
the plugin catalog and the connections view. As
in our initial release, we've included checks for
both plugins and data sources, so when you navigate to the advisor, you get an overview of the
issues which have been detected. The checks do run periodically so you can
see when they were last checked and as necessary, you can refresh to get live data or you
can delete the currently stored results. The more info section at the bottom gives
you some insights into the available checks, so you can see
that for data sources, we're checking whether the unique
identifier for each data source is valid, whether the health check
is returning successfully, or if you have a data
source instance configured, but the actual data source plugin is not
installed and therefore it wouldn't be usable. Then for plugins, we check for any that are deprecated
so that they're no longer maintained, and maybe you need to
consider an alternative or
if you are running an out of date version of a given plugin and
you should consider an upgrade. Looking into the action needed section, you can see that we have a bunch of
unhealthy data sources and you get links into the given
configuration page so you can see if you hit save and test, you'll get the specific error that's
going wrong with this data source. You could fix it and resolve your issue
or you can delete it if this is just something that needs to get abandoned.
Similarly, for investigation needed, we can see we have a bunch
of out of date plugins, so we could quickly navigate to
a given plugin and hit upgrades. Get to the latest version. The advisor
will continue to evolve with new checks, and we would welcome any and all feedback
and suggestions to help make it easier for Grafana operators to keep
their instances healthy and secure. It's currently experimental. It
requires Grafana 12 as a minimum, and for the Grafana advisor
feature toggle to be enabled. It will be available across open
source enterprise and Grafana Cloud, and we're starting to roll this out
across Grafana Cloud users in late April, but if you would like to try it
out sooner, you're a customer, just contact support.
Thank you for watching.

