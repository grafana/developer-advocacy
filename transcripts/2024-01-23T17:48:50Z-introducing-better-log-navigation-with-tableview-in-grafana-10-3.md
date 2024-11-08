# Introducing Better Log Navigation with TableView in Grafana 10.3

Discover how Grafana's TableView improves your log analysis experience. This feature simplifies navigating dense log ...

Published on 2024-01-23T17:48:50Z

URL: https://www.youtube.com/watch?v=OAZeqqNpEjc

Transcript: Hi, I'm Galen from the
Observability Log Squad, and I'm here to show you the new
table visualization for logs, which is being released in public preview. Table View is created to help facilitate
ease of use when navigating logs. There's a lot of dense information
contained in log lines, and while some data sources have
specific formatting options, like light loki's line format, these are inconsistent across data sources
and require specific knowledge of the query language. Enter the Logs Table View, which was created to facilitate isolating
fields and log lines in an interactive point and click UI. For
users with many fields, you can facilitate the fuzzy search above
the column selection UI to filter by name. The table columns are interactable
as well. Each field is sortable. The fields are also filterable by
value right within the table UI. The query is also modifiable by
interacting with the table cell values. For example, if I only
want to see logs from this pod, we just go ahead and click on the
filter for value and we'll see that it dynamically updates the table results. This removes the complexity of using
a query language to visualize specific field values. Also, the resultant table can be added to
a dashboard by simply clicking on Add Dashboard. Also, users can share their tables with other
team members by simply sharing the Explore URL, which will maintain
any changes that they made. This has been a brief demo of the
functionality of the new Logs Table UI. Thanks for listening.

