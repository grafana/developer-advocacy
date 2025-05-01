# Grafana Learning Journeys: An Overview of the Grafana Infinity Data Source Plugin

Do you have data formats you want to visualize in Grafana that are not supported natively? Or maybe you want to quickly ...

Published on 2025-04-16T22:01:16Z

URL: https://www.youtube.com/watch?v=OR5pJR7jb8g

Transcript: The Infinity data source plugin for Grafana is 
an open-source plugin that lets you query and   visualize data from various external sources, like 
REST APIs, CSV, JSON, and GraphQL, directly into   your Grafana dashboards. It's particularly useful 
when a native plugin for a specific data source   isn't available, allowing seamless integration of 
diverse data formats into your Grafana dashboards.   The Infinity data source is a great option if you 
don't want to send data to your Grafana Cloud.   This might be the case if you’re unable to install 
Grafana Alloy or use the OpenTelemetry collector. In this video, I’ll talk about all the value and 
key benefits of the Infinity data source plugin.   If you haven't used this plugin yet, you're going 
to want to try it after watching this video. Now, let’s discuss all the 
key value points clearly. The Infinity Data Source plugin allows you to 
connect to any HTTP-based data source, which   is ideal when there is no native Grafana plugin 
for a particular data source. The plugin lets   users pull data from any URL, with support for GET 
and POST requests as well as any custom headers. Infinity data source plugin supports data 
manipulation using familiar languages   such as the Unified Query Language, 
JSONata, and GROQ. With this support,   you can perform powerful transformations 
to your data such as filtering, mapping,   aggregating, and reshaping raw API 
responses. This is ideal if you have   an API endpoint that returns nested JSON 
and you only need specific keys or values. The Infinity data source plugin supports 
different authentication methods, such as basic,   bearer token, API key, and more, which is 
great for accessing secured internal APIs. The plugin works in the front end, 
so there is no need to build backend   connectors or ETL jobs to access the data 
you need. This is great for non-developers   who want to create data visualizations by 
plugging directly into different endpoints. With the Infinity backend parser, you 
can use features such as alerting,   Grafana expressions, recorded 
queries, enterprise query caching,   and shared dashboards to extract 
more value from your data. In summary, the main value of the Infinity 
data source plugin lies in its flexibility,   versatility, and extensibility,   especially when you need to work with data 
that's not supported natively by Grafana. To learn more about the Infinity data source 
plugin, check out all the useful links in the   video description below. You can also check out 
Grafana Play if you want to see how the plugin   works without installing anything. I hope to 
see you on the next video and happy visualizing!

