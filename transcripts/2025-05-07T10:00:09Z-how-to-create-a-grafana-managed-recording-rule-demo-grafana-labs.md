# How to Create a Grafana Managed Recording Rule | Demo | Grafana Labs

Grafana managed recording rules allow you to periodically pre-compute frequently used or computationally expensive queries ...

Published on 2025-05-07T10:00:09Z

URL: https://www.youtube.com/watch?v=67EdY_ZbpEg

Transcript: Graphana manage recording rules allow you to periodically premputee frequently used or computationally expensive queries from any data source that Graphana supports, saving the results as a new time series metric. These metrics can then be used in your alert rules and dashboards. Today we're going to walk through creating a Graphana manage recording rule. First step is locate the Graphfana manage section within your alert rules list and click new recording rule. We first have to give a name to recording rule. We then give a name to the metric that the recording rule is going to create. Next, we select our data source and we submit our query. We select the folder to put this rule in going to be used for arbback purposes and organization. Any labels you'd like to add. And last, your evaluation behavior. This is how often your rule is going to be evaluated. When you're done, click save rule and exit.

