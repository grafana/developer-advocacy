# Anomaly detection and root cause analysis with Application Observability | Grafana Cloud

In this video, we walk you through the latest features of Grafana Cloud Application Observability, designed to accelerate anomaly ...

Published on 2024-06-13T14:05:27Z

URL: https://www.youtube.com/watch?v=9tMv-6ilOvg

Transcript: Hi, my name is Cedric, and I'm a Product Manager 
at Grafana Labs. Let me show you what's new in   Application Observability. Often times when 
working with application performance data,   you're asking yourself the question, "Is what 
I'm seeing normal, or is it a deviation from   my expectation, and thus an anomaly? How 
can we know?" In Application Observability,   we introduced a capability called Time Window 
Comparison. So now, with a click of a button,   you can enable a comparison time frame and it can 
either be the previous period, or the week before,   or even the month before, and then you can set 
your current data into context of the historic   performance of this particular service. Sometimes 
an exact comparison is not what you're looking   for. That's why we introduced a capability called 
Automatic Baselining. An automatic baseline metric   is calculated from your historic data, and it uses 
standard deviation to factor in some seasonality   effects and aggregates the previous performance. 
Let's switch to Baseline as comparison time frame   here. As you can see, we now have a base band in 
the right panel and all the others. And we can   see our current data, which is the green band in 
the middle, and then the upper and lower boundary,   denoted by this colorful band which is 
the expectation of the performance. Based   on the historic performance of this particular 
service. Automatic baselines are available for   the RED metrics, rate error and duration for 
every service in application observability,   once you've configured it. Let's imagine that 
through one of our comparisons, we found an   interesting time series. A deviation that we can't 
really explain, and now we want to use domain   specific attributes to actually find out what's 
wrong. So, we can use group-by and filter-by to   sequentially narrow it down, until we reduce the 
noise so much that we get to the actual signal.   Okay. In Application Observability, you can always 
select a group-by-dimension. In our configuration,   we have enabled metric generation for the 
geo.country attribute and now we can enable   group-by-geo.country, and the one time series 
gets broken down into individual time series,   one per dimension in this particular attribute. 
And we can see that the different countries here,   Germany, Poland, Spain, and USA, have different 
performance. This breakdown enables you to better   understand the characteristics of your deployment. 
Let's see for example in the duration panel here,   we can see that Spain has a higher latency 
usually, than the other countries. That's   interesting. So now we can use filter-by to 
once again select the geo.country attribute,   and then we can select the Spain value, and reduce 
the noise in our user interface, and we get to the   signal. Now we only see the time series for Spain. 
We can remove the group-by dimension and start   again with a different attribute, that we can then 
group-by and sequentially reduce the noise. Let's   imagine that we are that close enough and we now 
really want to investigate some of the errors that   we are seeing. So, we introduced more contextual 
navigation. At any given point in time you could   navigate to traces, for a given time frame for 
example. Or to the logs that are related to the   service, but you can now natively interact with 
the graphs here in the rate error and duration   panels. So for example, this particular time 
frame looks interesting to me, and I can now jump   to logs for this particular time frame, or traces 
that were just produced within this particular   time frame. And you can see that we transferred 
all the filter attributes into that new user   interface here, and you now see at the particular 
set of transactions, that you have already   narrowed down through group-by and filter-by. This 
should greatly help you find the transactions that   are interesting for you, and have the performance 
characteristics that you are looking for. You   can do that from any panel in Application 
Observability service detail dashboards,   so it works for rate error and duration. One of 
the more interesting things for you to get started   very quickly, is actually the go-to-traces button 
right here. If you click here in the arrows panel,   then we show you just the traces that have an 
erroneous span. So for example, this trace, that   originated in the load generator, it is marked 
as erroneous, and we can neatly see the chain   in the transaction here. That's a trace that went 
through load generator, then frontend proxy. Some   envoy middleman here, and then into the frontend 
service. And then the place order grpc action,   actually was marked as the root of this error. And 
if we open the details here, then we can see the   error message of the grpc library, unavailable. It 
seems like the downstream service that was meant   to be called by this grpc interaction was not 
available.And this is now your place to start   investigating why that downstream service wasn't 
there. We think this in-context navigation for   traces and logs really helps you to narrow down 
more quickly. You can also do it from the duration   distribution. So for example if we look here, we 
have these buckets, and if you just want to see   traces that are in this 25 milliseconds 
bucket, you can actually click on that   and directly zoom in, and you have the relevant 
filter applied. Imagine that you're seeing very   high durations for transactions, and it's not 
really expected. Then here you are. It's very   easy for you to just find these transactions that 
are slow, and then you can drill down into these,   and find out what's wrong about them. And that's 
all that I got for you today. Happy observing.

