# Grafana 11.4 | Support for OpenSearch PPL and SQL queries in the AWS CloudWatch Data Source Plugin

In this video, Ida, a software engineer from the AWS Data Sources squad, introduces an exciting feature in the CloudWatch data ...

Published on 2024-12-05T20:02:59Z

URL: https://www.youtube.com/watch?v=g1BfokyzF4Q

Transcript: Hi. Let's talk about Opensearch, PPL and SQL support for
CloudWatch Logs Insights. I'm Ida and I'm a software engineer
in the AWS Data Sources squad, and we maintain the
CloudWatch data source plugin. This feature will enable users who
are already familiar with SQL and PPL languages to take advantage of the
features of those languages like SQL John Command, for example, to query
their AWS CloudWatch data. This comes in addition to the already
existing logs insights QL to enable, to query and visualize
exactly what you need. SQL and PPL support is available in
Grafana Cloud and Grafana On Prem 11.4 on December 5th, 2024. So
let me show you how it works. This feature introduced a new dropdown
in the CloudWatch Logs Query Editor. Logs Insights SQL is the default, but we have two additional options.
Opensearch, SQL and Opensearch PPL. So let's start with Opensearch
PPL. Before writing a query, don't forget to select
your log groups to query. This is a mandatory
field in Opensearch PPL, but it will also give you suggestions
for discovered fields while you type. So let me show you that by typing a
query that gets the number of errors per hour. Let's move on to SQL. While the log
group selection in SQL is not mandatory. It gives you the same
suggestion features as in PPL, so we definitely recommend it
for ease of writing queries. So let's write a similar SQL query. As you can see, querying SQL requires you to enter log
group identifier explicitly into the query field. So if you would like
to query multiple log groups, this is how you will do it. We have also updated our logs cheat
sheet with the examples for each of the three query types.
If you click on the query, it will replace your current
query in the query editor with the sample query. If you select
another query language, the query in logs cheat sheet
will be updated with the equivalent inquiries for that language. Keep in mind that only a subset of
commands and functions are available in CloudWatch PPL or SQL. For more info and the complete list of
the supported commands and functions consult the CloudWatch Logs Insights
documentation. If you're on Grafana Cloud, this feature will be
enabled in your instance, depending on your rolling release channel.
And if you're using Grafana on-prem, update 11.4 to try to
feature out for yourself.

