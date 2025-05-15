# We Made Tables in Grafana Dashboards Blazingly Fast | Public Preview | Grafana 12 | Grafana Labs

With this update, you'll notice faster performance in your Grafana dashboards. Other notable updates include much faster and ...

Published on 2025-05-07T10:00:16Z

URL: https://www.youtube.com/watch?v=CJvnccAPBiE

Transcript: Hey there. I'm Alex, an engineer here
on the DataViz team at Grafana Labs. Let's talk about blazing Fast Table
available in public preview in Grafana 12. So why the change? Our old
table served our users needs, but when it came to handling larger data
sets, performance took a hit. Loading, scrolling, sorting and
filtering actions often lagged, diminishing our user experience and
leading to less than smooth tool interactions. And that wasn't
good enough, so we fixed it. So let's look at this table, which
has 41,000 rows and 17 columns. We'll start with text wrap. Text
wrap is now near instantaneous. Sorting is very fast as well, and filtering is blazing fast. So how did we get here? We
explored popular table libraries. We evaluated them based on our needs, and ultimately made the
switch to React data grid. This transition brings all
the same table functionality, but with a massive boost in
speed and responsiveness. Now even the largest tables perform
seamlessly. So what's new? Well, this update isn't necessarily
about new features. It's about delivering blazing
fast performance. However, some notable updates include much
faster and more accurate text wrap, which I demoed, as well as more intuitive sorting for
fields that combine numbers and letters. We encourage you to enable the
feature toggle, give it a spin, and tell us how we can further enhance
your table data visualization experience in the future. Thanks.

