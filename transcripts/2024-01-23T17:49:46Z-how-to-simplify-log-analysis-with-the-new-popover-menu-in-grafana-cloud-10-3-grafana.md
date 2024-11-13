# How to simplify Log Analysis with the new Popover Menu in Grafana Cloud (10.3) | Grafana

Grafana Cloud introduces a popover menu for logs, designed to make search and filtering of log lines as effortless as possible.

Published on 2024-01-23T17:49:46Z

URL: https://www.youtube.com/watch?v=ievPSzmCrAk

Transcript: My name is Matias Chomicki and I work in
the Observability Logs Team at Grafana Labs. I want to talk about a new feature that
is coming to Grafana 10.3 this January, a popover menu for logs. At the Logs team, we want to make search and filtering
of log lines as easy as possible, so that's why we added a new
popover menu to help you with that. Whenever you select part
of a logline, a popover menu will appear with options to Copy
Selection, Add as Line Contains Filter, and Add as Line Does Not Contain Filter. When you click on Copy Selection,
it will copy your highlighted text. When you click on Add as Line Contains, it will add a filter to your
query matching the selected text. And if you click on Add as
Line Does Not Contain Filter, it will add the opposite filter,
not matching your highlighted text. This is another tool to help you refine
your search and change the query without having to actually write it. And it works perfectly in combination
with the filters in log details. As a reminder from Log Details, you can click on the
magnifying glass icons to filter for labels and label values. This works for any logging data source
that supports this feature such as Loki and Elasticsearch, and it works both in single data
source and mixed data source as well. Keep in mind that we'll add the filter
to the appropriate query that's produced at the logline. I hope you like this
feature, and thank you for listening.

