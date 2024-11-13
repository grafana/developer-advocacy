# Grafana 11 Now GA: Here&#39;s the TL;DR | Grafana

Grafana 11 is here! Our next major release is now GA. In this video, we are hitting the highlights. Think of it as your quick guide to ...

Published on 2024-05-14T14:00:06Z

URL: https://www.youtube.com/watch?v=96ZXShRyMB8

Transcript: It is here. Grafana 11 is now GA. In this major release, we had
three areas of focus: use, operate, and extend. In this video,
we're hitting the highlights. Think of it as your quick guide to
all of the new goodies. And hey, for the nitty gritty on each feature, keep an eye out for our deep dive videos, let's get into what makes
Grafana 11 a game changer. So what's in store for our users? Explore Metrics is a brand new data
discovery tool coming to Prometheus users. It allows you to discover drill into
your observability data without writing a single line of PromQL. You can then start to slice and dice
metrics based upon their labels, as well as discover
relationships with other metrics. We are migrating our
dashboard architecture over
to Grafana Scenes and you will see some early and noticeable
benefits including edit mode, improved load times, as well as the
time picker and dashboard variables. Now snapping to the top of
the canvas as you scroll. Speaking of dashboards, it wouldn't be a Grafana release
without some core updates to our visualizations. Canvas has been
improved with new flow chart elements, midpoint controls, as well as
horizontal and vertical snapping. We have also included the button
element, which can call an API endpoint. Think of the possibilities. The x and
Y chart is now officially supported, including documentation. You can now color full rows
with conditional formatting
in the tables panel. And we've also included a fantastic
community contribution to set threshold colors based on a query. We are also continuing to
improve the usability of alerts. The alert rule detail view has a new look
and feel to provide more comprehensive metadata during configuration. The Keep Last State feature allows you
to alert to a retain its last evaluated state when a rule produces
no data or error results. Last but not least, the PDF export for our cloud and
enterprise users has gotten a massive time reduction anywhere from seven
minutes down to 11 seconds. Make sure to check out our user
deep dive video for the rest of our visualization updates, alert changes, and to see how you can start
using Grafana's new LLM
feature to generate titles and descriptions. Operators also got a lot of love in this
release, sub folders are now available, allowing you to deeply organize
your growing list of dashboards. This also includes nested permissions.
Who said spring cleaning can't be fun? Azure Monitor Data Source can now
authenticate as the logged in Grafana user when using Azure Entra, streamlining authentication for
queries and resource requests. For cloud and enterprise users, we have also introduced label based
access control for low key logs. Each team queries the same data
source filtered by their team's label permissions. For our Grafana developers, it's all about simplifying the
process of extending Grafana. You can now scaffold a
plugin with one command, incorporate data visualizations
using the Scenes library. We are also providing access
to services such as navigation, search and RBAC, so you can extend Grafana meaningfully
without working in the core code base. And the SAGE design system provides a
well-organized set of design elements, patterns, and guidelines for building
extensions with the Grafana touch. Plenty more to talk about here, so stay tuned for our
developers deep dive video. It's been an exciting journey
from Grafana 10.1 to Grafana 11, and we've packed a ton of
great features in along the way. Alas, our job is never done creating an
observability platform that serves our community. Make sure you check out the Grafana 11
deep dive videos and we'll see you next time for Grafana 11.1.

