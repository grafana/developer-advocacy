# Kapa Summarize Readme

## Problem

1. Multiple threads on [The Community Forum](https://community.grafana.com) get long, and complicated, become popular, but are unanswered
2. Even when they contain good information, they're very hard to sift through
3. Ideally, we would have summaries of all of the good advice posted there.

## Solution Approach

We do have the [Kapa Discourse Solver](https://github.com/grafana/kapa-discourse?tab=readme-ov-file#solver) that can do this.

1. Use the tooling there to fetch/summarize threads
2. Have a human edit the response
3. Post that response, mark as the solution to the thread, and close the thread.
4. Do this only for threads that are old, complex, highly viewed, and unsolved.

[You can see a list of top unsolved topics over time here](https://community.grafana.com/top?ascending=false&order=views&period=all&solved=no)

## Log of Sample threads

This is the running log of threads where this has been done, just to keep track.

* [Creating custom time range buttons](https://community.grafana.com/t/creating-custom-time-range-buttons-in-grafana-dashboards/113662/11?u=davidallen5)
* [Extracting values from loglines in Grafana using Elasticsearch](https://community.grafana.com/t/extracting-values-from-log-lines-in-grafana-using-elasticsearch/112517/10?u=davidallen5)
* [Displaying and structuring JSON from Zabbix](https://community.grafana.com/t/displaying-and-structuring-json-data-in-grafana-from-zabbix/119827/32?u=davidallen5)
* [Bad Gateway Errors when Connecting Data sources](https://community.grafana.com/t/bad-gateway-errors-when-connecting-data-sources-e-g-influxdb/15883/37?u=davidallen5)
* [Math operations with fields](https://community.grafana.com/t/math-operations-with-fields/34022/11?u=davidallen5)