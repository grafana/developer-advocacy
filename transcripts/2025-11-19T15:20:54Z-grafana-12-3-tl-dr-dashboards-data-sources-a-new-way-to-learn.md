# Grafana 12.3 TL;DR - Dashboards, Data Sources &amp; A New Way to Learn?

Published on 2025-11-19T15:20:54Z

## Description

Grafana 12.3 is here and it's a big one! In this TL;DR, we break down everything new in Grafana 12.3 from slick new dashboards ...

URL: https://www.youtube.com/watch?v=VidGeu4PRZw

## Summary

In the video, the presenter discusses the release of Grafana 12.3, highlighting major improvements in three main areas: dashboard upgrades, data source enhancements, and quality of life improvements, with an additional focus on interactive learning. Key features include a revamped logs panel with better performance and usability, new panel time settings for comparative analysis, and support for various data sources like Databricks and Honeycomb. The release also introduces machine learning capabilities for AWS CloudWatch logs, along with PPL support for OpenSearch, and several quality of life improvements such as image export for dashboards and a new switch template variable. The presenter encourages users to upgrade and explore the new features.

## Chapters

00:00:00 Introduction to Grafana 12.3 release  
00:01:15 Overview of release features: dashboards, data sources, quality of life improvements  
00:02:00 New logs panel and its features  
00:03:30 Improved log experience with syntax highlighting and client-side filtering  
00:04:45 Panel time settings for better time control in dashboards  
00:05:50 Databricks Unity Catalog support for data governance  
00:06:30 Raw Query support for Honeycomb users  
00:07:10 Introduction of SolarWinds data source plugin  
00:08:00 AWS CloudWatch logs anomaly detection feature  
00:09:00 Quality of life improvements: switch template variable and exporting dashboards as images  
00:10:15 Grafana's new interactive learning experience for tutorials and help

# Grafana 12.3 Release Overview

Grafana 12.3 has officially been released, and you know what that means? Another TL;DR to give you the quick recap of what's new. This release can be broken down into three main areas: **dashboard upgrades**, **data source enhancements**, and **quality of life improvements**. Additionally, there's a new interactive way to learn about Grafana right inside the platform, which you definitely don’t want to miss. 

## Dashboard Upgrades

Let’s kick off this release with what we all love Grafana for: *dashboards*. In version 12.3, Grafana’s log experience has been significantly improved. The new logs panel is now generally available across Grafana OSS, Enterprise, and Cloud. It has been rebuilt from the ground up with better performance and visually appealing upgrades. 

### Key Features:
- **Syntax Highlighting**: Easier reading of logs.
- **Client-side Filtering**: Enhanced usability for filtering logs.
- **Redesigned Log Details**: Log details can now open inline or in a resizable sidebar.
- **Embedded Traces**: You can embed traces directly inside log details when trace IDs are available.
- **Logs Context**: Easier visibility of lines before and after search results, similar to using `grep`.

A new **field selector component** for logs is also available, allowing you to toggle which log fields are displayed and reorder them to your preference. This creates a much cleaner, faster, and more flexible debugging flow.

If you’ve ever struggled with time settings in panels, there's a fix for that too! Grafana 12.3 introduces **panel time settings** and **time comparison** (currently in public preview for OSS, Enterprise, and Cloud). This feature lets you control time ranges, shifts, and comparisons per panel without needing to edit the entire dashboard. You can easily do side-by-side comparisons, like this month versus last month, right in the same panel. No more cloning dashboards just to compare trends!

## Data Source Enhancements

Grafana 12.3 also brings significant upgrades to your data sources, expanding from enterprise data governance to raw API querying and even some machine learning features.

### Notable Additions:
- **Databricks Unity Catalog Support**: Now generally available for Grafana Enterprise and Cloud. This allows you to manage data access permissions and auditing across all Databricks workspaces securely.
  
- **Raw Query Support for Honeycomb**: This feature is now available for Enterprise and Cloud users, allowing you to utilize the full power of the Honeycomb API right inside Grafana, complete with variable substitution and complex filters.

- **New SolarWinds Data Source Plugin**: Available for Enterprise and Cloud in public preview. This provides visibility into network and infrastructure health, allowing you to visualize CPU load, memory usage, and active alerts alongside your application metrics.

- **AWS CloudWatch Logs Anomaly Detection**: Now in public preview for OSS, Enterprise, and Cloud, this feature adds machine learning-powered anomaly detection to your CloudWatch queries, flagging abnormal behaviors in log patterns.

- **OpenSearch PPL Support**: Now in public preview across OSS, Enterprise, and Cloud. The new PPL query editor includes syntax highlighting, auto-completion suggestions, and sample queries to help you get started faster.

## Quality of Life Improvements

Grafana 12.3 introduces several quality of life improvements that often go unnoticed but make a big difference in daily usage.

### Key Improvements:
- **Switch Template Variable**: Now generally available across Grafana OSS, Enterprise, and Cloud. This feature replaces clunky dropdown menus with an intuitive toggle. You can set it up with boolean values (true/false, yes/no, etc.) or even custom values, making it easier to turn debug modes or filters on and off.

- **Export Dashboards as Images**: This feature is now generally available for OSS, Enterprise, and Cloud. You can export any dashboard as a PNG exactly as it appears on your screen, eliminating the need for half-broken links.

- **Interactive Learning Experience**: This is now in public preview for Grafana OSS and Enterprise. It can be enabled with the interactive learning feature flag. Cloud users can install the plugin manually. This feature creates a rich visual way to walk through various tutorials in Grafana, helping users learn how to set up data sources, explore panels, write queries, and more. It effectively brings the documentation into Grafana without overwhelming users with tabs.

## Conclusion

So that’s Grafana 12.3—three big pieces (or four, if you count the interactive learning experience) all in one release. If you're running Grafana OSS or Enterprise, go ahead and upgrade your instance to try out the new features, and feel free to provide us with your feedback. If you're a Cloud user, you're probably already experiencing these enhancements. 

Until next time, remember to always be observing! And maybe consider giving us a like and a quick subscribe. Take it easy!

## Raw YouTube Transcript

So Grafana 12.3 has officially been
released, and you know what that means? Another TLDR to give you the quick
recap of what's been dropped. Now this release can be broken up into
three big pieces, dashboard upgrades, data source levelups, and
quality of life improvements. And make sure you stick around
because we kind of have a fourth. There's a new interactive way to warn
Grafana well right inside Grafana that you'll definitely want to see. So let's kick off this release or
12.3 with what we all love Grafana for dashboards now in 12.3. Grafanas
log experience just got slicker. The new logs panel now generally
available across Grafana OSS, enterprise and cloud has been rebuilt
from the ground up with better performance and seriously nice visual upgrades. You've now got syntax
highlighting for easier reading, client side filtering and redesigned log
details that can open in line or in a resizable sidebar. You can even embed
traces directly inside the log details when trace IDs are available in
your logs and it doesn't stop there. The new logs context makes it easier
to see the lines before and after your search results. Basically like
using grep right inside Grafana. Plus there's a new field selector
component for logs, again, generally available across all versions
that lets you toggle which log fields are displayed in, reorder them however
you like. It's a much cleaner, faster, and flexible debugging flow. And if you've ever struggled
with time settings in panels, there's a fix for that too. Grafana 12.3 introduces panel time
settings and time comparison currently in public preview for OSS
and enterprise and cloud, it lets you control time ranges, time shifts and comparisons per panel
without editing the entire dashboard. You can even do side-by-side comparisons
like this month versus last month, right in the same panel. So there's no
more dashboard cloning just to compare trends. Alright, now let's talk data. Because Grafana 12.3 didn't just
stop at prettier dashboards, it leveled up your data sources too. This is the part of the release where
Grafana continued to grow the big tent from enterprise data governance to raw
API querying and even a bit of machine learning magic. First
up, for databricks users, the Unity catalog support is now generally
available on Grafana Enterprise and Cloud. Unity Catalog gives you a single
point of control for managing data access permissions and auditing
across all your Databricks workspaces. With this new integration, you can securely query and visualize
governed data directly in Grafana while preserving those fine green permissions
and lineage tracking you've already set in Databricks. Basically, this means you can finally trust that
what's showing up in your dashboard mirrors the same governance rules as
your data warehouse. Then there's one for the honeycomb crowd. Raw Query support is generally
available for enterprise and cloud users. This feature what you use the full
power of the Honeycomb API right inside Grafana complete with support for
variable substitution and complex filters. So if you've been craving more control
over how you query your observability data in Honeycomb, this is it. You can now craft detailed
queries use IN and NOT IN filters, and go full power mode on your
dashboards if you're a honeycomb user. Additionally, SolarWinds joins the lineup with a brand
new data source plugin for enterprise and cloud and public preview. SolarWinds gives you visibility into
network and infrastructure health. You can think CPU load memory usage
and active warts all visualized next to your app metrics. It's perfect for connecting the dots
between infrastructure performance and application behavior without switching
tools and doing it all within Grafana. Over on the AWS side, the CloudWatch logs anomaly detection
and pattern analysis feature is now in public preview for OSS
Enterprise and Cloud. This adds machine learning powered anomaly
detection right inside your Grafana CloudWatch queries. It can flag abnormal behavior with your
log patterns and group recurring events automatically so you can catch weird
behavior before it snowballs into a full-blown AWS incident. And finally,
for all you OpenSearch users out there, PPL support is now in public preview
across OSS and enterprise and cloud. The new PPL query editor
adds syntax highlighting auto
completed suggestions and sample queries to help
you get started faster. You can even hit kickstart your query to
pull in ready-made examples. Basically, it takes the guesswork out of writing
PPL and makes exploring open search data way smoother. Finally, let's talk
about the little yet crucial things. Grafana 12.3 brings a handful of these
quality of life improvements that make it swept under the rug a lot of times, but quietly make your day better every
time you use Grafana. Starting off, let's talk about the
Switch template variable, which is now generally available
across Grafana OSS enterprise and cloud. This feature replaces those clunky
dropdown menus you've been creating. With an intuitive queen toggle, you
can set it up with buoyant values, like true false yes, no one
zero or even custom values. This is perfect for turning debug modes
or filters on and off without breaking your workflows. Next up, something everyone's been asking
for exporting dashboards as images. Now this is also generally available
for OSS Enterprise and Cloud. You can now export any dashboard
as A PNG exactly as it appears on your screen. So there's no more
sending people half broken links. Just click export as image, grab the preview and drop it
straight into your chat slide deck, incident report or whatever. It's one of those small but mighty
features that saves time every single day. And a feature coming with
12.3 that is going to change the self-guided experience is
Grafanas Interactive Learning. This is now public preview for Grafana
OSS along with Enterprise and can be enabled with the
interactiveLearning feature flag. Cloud users will be able to simply
install the plugin manually. Now the new interactive
learning experience creates
a rich visual way to walk through various tutorials in Grafana. So whether you're new to Grafana and
maybe trying to set up a data source, explore a panel, get
started writing queries, or learn any of the features in Grafana, this interactivity gives you
help right where you need it. You can think of it as having the
docs built into Grafana minus the tab overload in a much
slicker user experience. So that's Grafana 12.3,
three big pieces... or four, but just one release. So if you're
running Grafana OSS or Enterprise, go ahead and upgrade your instance, trail out the new features and give us
your feedback. If you're a Cloud user, you're probably already seeing these
features in play. Until next time, always be observing and maybe even
toss us a like in quick subscribe. Take it easy.

