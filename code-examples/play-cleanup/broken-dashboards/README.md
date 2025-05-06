# Testing with K6

Here we're trying to get a sense of how many dashboards are functional, and how many panels they have.

## Execute the test locally

```
k6 run dashboard-broken-panels.js >run.log 2>&1 &
```

This produces CSV which can be extracted from k6 logs like this:

```
cat run.log | grep ResultMeasurement| sed 's/" source=console//' | sed 's/.*msg="//' | sed 's/\\//' > sample.csv
```