# SQL Expressions Demo: Smarter Data Transformations in Grafana | Private Preview | Grafana 12

SQL Expressions in Grafana 12 (private preview) let you transform, join, and aggregate data from multiple sources—like Loki and ...

Published on 2025-05-07T10:01:26Z

URL: https://www.youtube.com/watch?v=tGIqVQrPgR8

Transcript: Hi there. I'm Sam Jewell, an
engineer here at Grafana Labs. Let's talk about SQL expressions, which is available on private
preview in Grafana 12. So why make this change? Well, Grafana users often want to
transform the data that they get back from their data source queries.
This is valuable for a few reasons. It allows data to be
joined, ordered, filtered, and aggregated before it
is then visualized in a Grafana dashboard. It can be used to combine
data from disparate data sets. So for example, this is a query that returns metrics data, time series data, which is coming back
from a logging data source, in this case, Loki. And this query is responding
with tabular data, which has come back from a SQL data
source, in this case, BigQuery. And with the SQL expression, we've been able to combine those disparate
types of data from disparate data sources at query time in Grafana with a single SQL transformation.
And we haven't had to run any ETL pipelines. We haven't had to run any
data warehouse or data lake to do this. So that is super powerful.
And last but not least, this gives us the ability
to alert on data that has been transformed. So you can see we're loading the data
sources here into a new alert rule. There's the logging, logs query,
here's the BigQuery query, and then here is the SQL
expression, powering an alert. And you can see if we preview
it, you can see it's firing. This query was not written to power an alert with many labels, but you can see that the
alert is working already. So now you may know that we have
for a long time already had this menu of transformations in
Grafana, which is powerful. But there are limits. Users might want a transformation
which is not yet supported, and sometimes it's hard to kind
of find the option that you need. And after you've added a
few of these transformations, it can start to become quite
unwieldy, sometimes a bit slow. But we found we can simplify and
speed things up by replacing lists of four or six or 10 transformations into a single SQL expression. And moreover, Grafana transforms did not support
alerting because they're all running in the browser. Okay, so how do we go about actually
adding a SQL expression from scratch here? I've got a brand new
dashboard with a new panel, and I'm just going to use the
test data source to add some dummy data that we can use to test
this out. So I'm going to use, there's population data which has
some rows and columns you can see, and I could visualize that
in a bar chart. Alright, so the first thing I'm going to do is
switch back to the table view here. That's important. So we can see our rows and columns
and how our fields have been named so we can reference them. So now
we're going to start transforming. We'll come down here and add click,
add expression, that button there. And then from this list, we need
to pick the bottom option SQL, transform data using SQL,
which uses the MySQL syntax. And you'll see there's some
more help text here. Okay. Now straightaway we can run that. And what you'll see is that there's
now two tables we can choose from. This top one is coming back from query
A and this bottom one from query B. We want to work with B now and start
evolving our query. So we'll pick that, and actually I'd recommend you hide
the response from query A because that's now a dependency
that will be evaluated when query B runs. Okay, so the
first thing to know is that here, these field names are
available to your SQL query as column names. So what we can
do, we can say select state, let's try 2020. And actually we need backticks
because this is a number. And so we've been able
to reference the field names as column names here in the query. The other thing to note is that the
reference, the name of the query here, if this was called Pop for Population, for example, and we tried to run that,
we'd get an error, table not found A. That's because it can't
find this table A here. The query names or the query references to your data sources are available
in the query as table names. That's how you've got to refer
to them. So there you go. And we're away now so we can
start transforming the data. We could limit to two rows. For example, we could rename 2020 as latest, and we could even bring back, let's say we brought
back 1980 data as well, and we can see that now at this point, we could try to visualize the final
result. So I'll show you that. And you might've spotted,
I've made a mistake here. You've seen what the solution is already. But I wanted also to illustrate the power. One of the powerful things about
SQL is that we live in the age of generative AI now and LLMs. And so some of us might
not consider our SQL ability to be very strong, but LLMs and generative
AI are fantastic at explaining and understanding and
writing SQL because it's prevalent. There's so many examples out there in
the world. So if I want to fix this, I can just copy it and land it into LLM service. I can say I'm
not seeing data from 1980, I'm just seeing that value over
and over. What did I do wrong? And it's going to give me a solution
here. I'll just copy that, drop it in, and let's see if that fixes
the issue. It does. Look, I've got my original numeric data back, and there we go.
I've transformed the data successfully. And just to illustrate a bit more how
I've been using LLMs to write my SQL queries I've got here, I had a kind of regular expression here, and I wanted to implement
it in my SQL instead for lifting a sub string. It wrote
the query for me straight away, and then I extended it further
with grouping by one of the fields, which was name was Noun. And
lo and behold, there it goes. It just keeps building longer
and longer SQL queries, and I just keep dropping them in and seeing how they get. So
that's SQL Expressions. It's fantastically powerful. Many of us here at Grafana
are super excited about it. So please reach out to us if you'd
like to join the private preview. We would love to have you try it out
and to hear your feedback. Thank you.

