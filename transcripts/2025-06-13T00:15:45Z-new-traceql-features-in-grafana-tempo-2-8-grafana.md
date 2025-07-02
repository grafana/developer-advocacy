# New TraceQL features in Grafana Tempo 2.8 | Grafana

Published on 2025-06-13T00:15:45Z

## Description

In this video, Joe Elliott does a deep dive demo into the experimental TraceQL features in Grafana Tempo 2.8. Blog post: ...

URL: https://www.youtube.com/watch?v=cI2rmWl8ag0

## Summary

In this video, Joe Elliot discusses three new features introduced in TraceQL with the release of Tempo 2.8. He explains the enhanced metrics capabilities, including the "top K" and "bottom K" functions, which allow users to filter and focus on the most or least significant data points in their queries. Additionally, he introduces a new function called "sum over time," which enables users to calculate the sum of any span attribute over time. Finally, he highlights the long-awaited feature that allows users to retrieve the most recent traces by using the query hint "most recent equals true." Joe emphasizes the performance improvements and bug fixes in this release and encourages users to explore these new functionalities.

# Tempo 2.8 New Features Overview

Hey everyone, my name is Joe Elliot, and today we are going to look at three amazing new features in **TraceQL** released in **Tempo 2.8**.

## New Metrics Features

First of all, we have some new metrics features. I’ll discuss two of those here. Let’s start with a pretty common query where we will calculate a rate by resource service name and span name. This is a straightforward approach where we are looking at the rate of all our spans, grouping them by service name and span name. 

This can help us identify what’s creating a lot of traffic in Tempo. In this case, we have created a series of over 200, which might become overwhelming as we scroll through it. There are tons of options, and it can be challenging to parse this data and get a sense of what’s significant.

To help with this, we’ve added **Top K** and **Bottom K** functions. You can pipeline any metrics into these functions. For example, I have my initial query, and I’m piping that to the rate by service name and span name, but I want to filter this down. 

If I reduce it to the top 10, I can now get a much more focused view of this data, only looking at a reduced subset. You might notice there are actually more than 10 series, and that’s because we calculate Top K in a way similar to **Prometheus**. For every data point, a new Top K is calculated individually, which is why you may see more than 10 results.

We could further drop this down to Top K5 to see even fewer options. This allows me to focus on my top service and operation names, making it easier to analyze the data.

### Bottom K Function

Alongside Top K, we also have the **Bottom K** function, which does the opposite. Both Top K and Bottom K are new functions in Tempo that help reduce the amount of data returned, allowing for a more focused analysis.

## Sum Over Time

Additionally, we have introduced a new function: **Sum Over Time**. This function is an extension of the existing metrics functions and calculates the sum of any attribute over a specific time window. For instance, we can look at the sum over time of response content length, which is an attribute on my spans. This allows us to see where data spikes occur, showing where services are sending more data in their responses.

The sum over time operates on a specified step. Currently, the step is set to auto, but we can change it to, say, 10 seconds, or let Tempo automatically determine it.

## Recent Traces Query Hint

Moving beyond metrics queries, we have a long-requested feature: the ability to retrieve the **most recent traces**. Previously, Tempo would return any trace it finds for speed, which can be less useful for those wanting to see the most recent data. 

Now, you can use a hint in your query: `most recent = true`. This syntax may seem odd, and even **Grafana** doesn’t fully support it yet, but we introduced it in an experimental way to encourage feedback and improvements. 

This feature allows you to see the most recent results, with queries returning traces right up to the last second of your specified time range. For example, if I set my query range to 41 minutes, I can retrieve the 20 most recent queries ordered by their start time, displaying them right up to the current edge of my time range.

## Conclusion

In summary, here are the three new features in TraceQL:

- **Sum Over Time**: A new metrics function that allows you to sum any attribute of any span over time.
- **Top K and Bottom K**: Functions that provide more control over the data returned, allowing you to see focused sets of data based on the highest or lowest values.
- **Most Recent True**: A long-awaited feature that enables you to retrieve the most recent traces easily.

I hope you all enjoy the features in Tempo 2.8. There are many performance improvements and bug fixes in this release. We’re excited about these new trace features and look forward to seeing you in **Tempo 2.9**!

## Raw YouTube Transcript

Hey everyone, my name is Joe Elliot and we are going to look at uh three amazing new features in TraceQL released in Tempo 2.8. So first of all, um we have some new metrics features. I think we're going to talk about two of those. Let's look at a pretty common query here, right? We're going to do a rate by and let's just do resource service name, right? And span name. So something pretty straightforward. Um we're going to take the rate of all our spans. We're going to group them by our service name and our span name. Maybe we're just looking to see what's creating a lot of traffic and tempo. Now, in this case, we've created a 200 something series. And this might become a little overwhelming, right? We're looking kind of scrolling through here. I see tons of options. I might um struggle to kind of parse this and really get a sense of what's the top. I can I could kind of mouse over. Maybe I'm struggling to see some of these down here. So, what we've added is top K and bottom K. And this is a a function. you can pipeline any metrics into. So I have my initial query. I'm piping that to the rate with uh by service name, span name, but I want to filter this down some. So let's look at the top 10. Um if I reduce to the top 10, I can now get kind of a much more focused uh view of this data and I'm only looking at a much reduced subset. You'll notice there's actually more than 10 series and that's because we do top K in a very similar method to Prometheus. So in Prometheus for every data point um a new top K is calculated the top 10 on every data point and um tempo is following suit there. So you're going to see more than uh 10 down here and that's because every data point is evaluated individually. Um we could kind of drop this down some maybe do top K5 and see fewer and I can now start mousing over and maybe I'm able to see kind of this really tight view. I can very clearly see my top view service and operation names. So a really quick way to reduce some data sets um to get more value out of the out of out of what you're querying from tempo. Cool. So top k and of course we have bottom k as well um uh which just kind of does the opposite right? So top k and bottom k two new functions in a templ so we have a number of uh over time right we have average over time we have quantile over time we have number number of different uh functions that calculate metrics over a time series a small window and we have since added in this release in tempo 2.8 Okay, we've added a uh sum over time. So, this is going to do what you expect. It was kind of just an easy uh an easy extension of the existing metrics functions. And in this case, we're just going to look at sum over time of this response content length. So, this is an attribute on my spans. And I can kind of clearly see where uh the data is spiking. So, I can see where my services are sending more data in the responses than otherwise. uh sum over time operates on the step. The step is auto right now. So we could change this to be like 10 seconds. We can manually set it to what we want. Um or we can allow tempo to choose uh uh and and if we set it to auto, of course, we're just going to let it choose. And that is what the sum is calculated over. Cool. So top k bottom k nice functions to reduce the amount of data returned to help focus. Sum over time a new function which gives us uh the sum of any attribute. We could use duration which is kind of maybe strange but we could or other any attribute on our uh spans. Um all right so some over time top k bottom k uh not in the field of metrics queries but a new feature added to tempo. This one's been a long time requested and we've now added it as a query hunt is the concept of uh getting the most recent uh traces. So previously currently tempo will return any trace it finds and this is for speed. When you do uh any query it just finds anything it can as fast as it can returns you how your limit. So if we set to 20 or 100 or a thousand it will return that many traces as soon as it finds uh finds anything matching your conditions. But a lot of people want to see the most recent right this is a pretty common request. In fact it might be one of our most common uh requests in uh the GitHub uh issue tracker. So, we've added this ability with uh this hint. Most recent equals true. This is a weird syntax. In fact, Graphana doesn't even like it. We did add it in this kind of experimental way on purpose. Uh we had intended or we talked about adding it as a configuration option here. Maybe a checkbox or something. Um but we decided to add it as a query hunt because we really want to make this default. Um certain elements of the structure of Tempo are preventing it from being as performant as we want at scale. Um so, we added as a query head so people can experiment with it. um they can decide you know how to use it if it's working well for them they can file issues on it we can home it in uh make it performant as we want across all scales uh and then probably make it the default behavior so we really encourage people to experiment with most recent equals true um it allows you to get the most recent results you'll see here like uh 41 minutes is kind of my query range and I'm getting stuff like right up to 41 minutes right so like 59.999996 and kind of like getting right up into that absolute at last second. These are the guaranteed uh 20 most recent queries ordered by their start time. Uh where before if we remove this tempo is just going to find you know whatever it can happen to find and give it back to me. So here I'm seeing like 54 seconds 30 and we're seeing it come kind of scattered across the time range versus kind of pinned all the way to the absolute right edge of my time range. All right, so three new features in TraceQL we're excited about. uh sum over time. A new metrics function allows you to sum any attribute of any span kind of over time. Uh there is the top k and bottom k giving you more control over the data that's returned to see uh focused sets of data. So the top um or the the highest value or the lowest value sets of series in a metric response. And then finally this uh with most recent true is a long time coming. Uh it took some doing. We got it in right after we cut 27 and it is a exciting feature in 28 where you can see these absolute most recent traces. All right. Uh I hope you all enjoy the features in 2.8. There's a lot of uh performance improvements, a lot of bug fixes. It's a good release and these three new trace features. Uh we will see you in Tempo 2.9.

