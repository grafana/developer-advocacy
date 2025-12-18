# Tail sampling vs. head sampling in distributed tracing

Published on 2025-12-18T16:53:46Z

## Description

In this video, Grafana Labs' Robin Gustafsson (CEO for K6 + VP, Product) and Sean Porter (Distinguished Engineer) discuss the ...

URL: https://www.youtube.com/watch?v=4bjIkpnen3s

## Summary

In this video, the discussion revolves around effective trace sampling methods in data storage and analysis, particularly in the context of high-volume requests. The speaker emphasizes the importance of ensuring that stored data is valuable, contrasting traditional head sampling—which randomly selects traces from a large volume of requests—with a more advanced technique called tail sampling. This method, utilized by Grafana Cloud, involves collecting complete traces and then applying specific evaluation policies to determine their significance based on various attributes (such as errors or status codes). By doing so, organizations can make more informed sampling decisions that prioritize valuable data over sheer volume, enhancing the efficiency of data storage and analysis.

## Chapters

00:00:00 Introduction to the topic of valuable data storage  
00:01:00 Explanation of sampling in tracing  
00:02:15 Discussion on the volume of requests and their impact  
00:03:00 Introduction to heads sampling method  
00:04:30 Limitations of heads sampling  
00:05:15 Introduction to tail sampling  
00:06:00 Explanation of how tail sampling works  
00:07:30 Benefits of using tail sampling over heads sampling  
00:08:45 Adaptive traces and their evaluation criteria  
00:09:30 Summary of intelligent sampling methods

It's about making sure that the thing that ultimately gets stored is actually valuable. This can mean sometimes more, sometimes less. 

Sampling is inherently part of tracing because every request technically could produce a trace. If you're handling hundreds of thousands or millions of requests a day, that equates to hundreds of millions of traces. One approach most organizations take is referred to as **head sampling**, which is a sophisticated method of random sampling done at the instrumentation level. 

Upfront, you decide to capture just a fraction of a percent of all your traces due to sheer volume. This means you end up sampling randomly and hoping that the unique and interesting traces will surface and be stored. However, this method leaves you sifting through a lot of data without a clear strategy.

What adaptive tracing does at Grafana Cloud is known as **tail sampling**. In this method, we wait and collect all the spans, or the individual components that make up a trace. We wait until we have what looks like a complete trace, and then we apply policies to evaluate these traces. We can assess whether a trace contains errors, is particularly long, or has specific attributes relevant to a team or namespace. 

There are many different ways to evaluate the traces, including checking their status codes. After this evaluation, we can make an informed sampling decision. This approach gives you much more power and shifts your strategy from randomly sampling and hoping to intelligently sampling what actually has value to you.

## Raw YouTube Transcript

It's about making sure that the thing that ultimately gets stored is actually uh valuable, right? Which can mean sometimes more, sometimes less. >> I mean, sampling is inherently part of of tracing just because every request technically could produce a trace. Um, so if you're doing hundreds of thousands or millions of requests a day, that equates to hundreds of millions of >> traces. Um, so one approach most organizations take is referred to as heads sampling. um which is basically a sophisticated method of random sampling done in the instrumentation. So up front you're like I just want a fraction of a percent of all my traces um just due to straight volume. So you're kind of just like sample randomly and hope is the strategy. Uh which is which just doesn't sound very appealing. You're just hoping through sheer volume alone like the unique and interesting ones are going to surface and be stored. But you're left still sifting through all that. So what adaptive traces does at Graphana Cloud is referred to as tail sampling, which is we wait and we collect all the spans or the the individual components that make up a trace. We wait until we have what looks like a complete trace and then we have policies that can evaluate the traces to see like does this contain errors? Is this particularly long? Does this have these attributes for this team or this uh name space or so many different ways to look at does it have this status code? You can look at all these attributes and then you can make a sampling decision then. Um so you have a lot more power. So it turns you kind of shift from sample randomly and hope to like intelligently sampling what actually has value to you.

