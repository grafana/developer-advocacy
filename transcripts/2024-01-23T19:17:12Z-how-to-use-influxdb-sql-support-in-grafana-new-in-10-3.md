# How to Use InfluxDB SQL Support in Grafana (New in 10.3)

Grafana now supports the new SQL querying language for InfluxDB 3.0, allowing you to utilize Native SQL for your data queries ...

Published on 2024-01-23T19:17:12Z

URL: https://www.youtube.com/watch?v=jGclGsv5PBA

Transcript: Hi, my name is Ismail Simsek and I'm the
Tech Lead of the Observability Metrics Squad at Grafana Labs. Today, I'm excited to announce built-in
SQL querying language support in Grafana InfluxDB Data Source. InfluxDB introduced a
new version 3.0 in April. With this new version, InfluxDB
has put Flux in maintenance mode, but with the new version, we have a
new querying language, Native SQL. So with version 10.3, Grafana has built in support for SQL
querying language in InfluxDB. That said, let's create a new data source. Select the query language as SQL. Put your InfluxDB cloud URL down below. We need to add our database.
Then we need a token. Let's generate one. Paste it and save it. It
works. Let's run some queries. We'll have tables and columns.
We need a time column, and let's add another one. usage_idle and usage_iowait. Let's run the query. Nice. So let's add this to the dashboard. Let's add some template variables.
Add any variable, InfluxDB-4, and we are querying columns of the CPU table. Let's apply this. Let's use that variable. Run the query. It works.
Let's select something else. Run the query and it works. Check out InfluxDB Docs on
Grafana to learn more and go to play.grafana.org to try SQL
supporting InfluxDB for yourself.

