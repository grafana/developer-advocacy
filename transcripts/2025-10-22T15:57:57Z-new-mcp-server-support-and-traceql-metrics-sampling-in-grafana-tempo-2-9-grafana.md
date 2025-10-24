# New MCP server support and TraceQL metrics sampling in Grafana Tempo 2.9 | Grafana

Published on 2025-10-22T15:57:57Z

## Description

In this video, Tiffany Jernigan walks through new features in Grafana Tempo 2.9, including the MCP server and TraceQL metrics ...

URL: https://www.youtube.com/watch?v=dUQQwOsIAP4

## Summary

In this video, Tiffany Jernigan presents the new features of Tempo 2.9, focusing on the introduction of a Model Context Protocol (MCP) server that allows AI assistants like Claude Code and Cursor to access tracing data via TraceQL queries. She explains how MCP standardizes API connections for AI tools, enabling users to ask natural language questions to diagnose issues effectively. Tiffany demonstrates the functionality of the MCP server using Claude to explore services and find error traces, as well as showcasing a new query hint for probabilistic sampling to speed up query responses. She encourages viewers to check out the release notes and community resources for more information and feedback.

## Chapters

Here are the key moments from the livestream with timestamps:

00:00:00 Introductions and release of Tempo 2.9  
00:01:15 Overview of new MCP server for AI tools  
00:02:30 Explanation of Model Context Protocol (MCP)  
00:03:45 Demonstration of using Tempo with Docker  
00:05:00 Using Claude to query services in Tempo  
00:06:30 Finding traces with errors using natural language  
00:08:00 Querying for slow services in Tempo  
00:09:15 Analyzing specific trace IDs for performance issues  
00:10:30 Introduction of new query hint for probabilistic sampling  
00:12:00 Comparison of query performance with and without sampling  

# Tempo 2.9 Release Highlights

Hey everyone, I'm Tiffany Jernigan, and we just released **Tempo 2.9**! In this video, I want to highlight several key features. For more details, check out the blog and release notes.

## New MCP Server

We’ve added a new **MCP server** that allows AI assistants and LLMs, such as Claude Code and Cursor, to access your tracing data using **TraceQL** queries and other endpoints. If you haven't heard of MCP, it stands for **Model Context Protocol**. It's an open-source specification from **Anthropic** that standardizes how AI tools connect to APIs. 

This means you can ask questions in natural language and receive answers about what’s happening, making it easier to investigate and diagnose issues quickly.

## Using Tempo

Currently, I’m running a local example of Tempo using Docker Compose. If you look at the top of the **Tempo GitHub** page, you can see how to run it locally. 

Once you're in Tempo, you can navigate to the Explorer. Here, you can click **search** to view your various services. If you’re not familiar with navigating through this or using TraceQL, that’s where our **Tempo MCP server** becomes really useful.

### Adding MCP Server

Let's use Claude to demonstrate. First, I will add the MCP server with the command:

```
Claude MCP add
```

Tempo is running on **Port 3200**. If I check with `docker ps`, you can see it's active on that port. 

Now, if I run Claude without additional setup, it will ask if I trust it. I can then ask, “**List all services in Tempo**,” and it will return the same information visible in the Explorer, showing services like the shop backend, auth service, Postgres, etc.

### Querying for Errors

Suppose you’re looking for errors but aren’t familiar with TraceQL. You might simply ask, “**Find some traces with errors**.” Claude will return details about different error patterns and the number of traces with errors.

Next, you might want to find slow services by asking, “**Find me some slow services.**” Claude will provide information on these services, and you can follow up with, “**Why are these services slow?**” It will then analyze a specific trace ID to explain where the time is being spent.

You can also ask, “**What services have problems?**” And just for fun, you might say, “**Let’s write a short poem about this.**” You'll end up with an ode to broken services!

## New Query Hint

Another exciting addition is a **new query hint** that speeds up your queries by returning approximate results through probabilistic sampling. Query hints are special options you can add to a TraceQL query to modify how Tempo processes requests. We introduced one in version 2.8, so be sure to check it out.

### Demonstrating Sampling

Now, I’ll demonstrate using TraceQL to get the rate of all our spans. 

1. Run the query:
   ```
   rate
   ```
   After it runs, it takes a little over three seconds.

2. Next, let’s use the new query hint for dynamic sampling:
   ```
   width, sample=true
   ```
   Running this takes less time. The more data you have, the more noticeable the difference will be between the original query and the one with sampling.

You can compare the two queries. If you duplicate the first query and remove the sampling part, you’ll see that the graphs look quite similar, providing an approximate idea of the data. This feature is especially useful for dashboards that need to run faster.

## Conclusion

For more control over your queries, check our release notes as there are additional query hints available. 

Please explore these new features, share your feedback, and check out the blog for more information. Also, join us in the community at select@grafana.com.

Thanks for watching!

## Raw YouTube Transcript

Hey everyone, I'm Tiffany Jernigan,
and we just released Tempo 2.9. So there's several things that we
wanted to highlight in this video. There's more in the
blog and release notes, but we added a new MCP server
that lets AI assistants and LLMs, such as like Claude Code and Cursor, tap into your tracing data using
TraceQL queries and other endpoints. So if you haven't heard of MCP, it
stands for Model Context Protocol. It's an open Tource spec from Anthropic
that standardizes how AI tools connect to APIs. So basically you can go and ask
questions using natural language and get answers about what's happening as well
as investigate and diagnose issues more quickly. So right now, if we were to go over to Tempo, so I am currently running just
the darker composed local example. If you go to the GitHub for Tempo,
you can see at the top here, you can just run it locally. I'm just
again using Docker compose for that. If we go over here and we
look at Explorer for Tempo, you could for instance, go and
click search and you can see, hey, these are all my different services. But say if you aren't familiar
with going through this, or maybe you're not familiar with
TraceQL and you're wanting to know that, then that's where our Tempo MCP
server becomes really useful. So I'm going to be using Claude. So first thing I'm going to do is I'm
going to go and add the MCP server. So if I do "Claude MCP
add." So right now we have a Tempo running on Port
3,200. So if I run that, you can also look if I do a Docker PS. We can see right now, for instance, that it's a little hard to see here, but it's on 3,200 there.
And so if I just go and run Claude at the moment without all of that, it's going
to go and ask me if I trust things. So then basically I can be like, "Hey, list all services in
Tempo." We can just exit it directly and it should go and end up
telling us the same things that we were just seeing when we were
looking at the front end for Explorer. So we can see we have the
shop backend or off service, Postgres, et cetera. So we can see all of that
there. So next, if we're like, okay, well hey, how do I don't know that
TraceQL for trying to find an error, if you didn't know, for instance,
you could just go here and be like, "Hey, status equals error" and
then you can run your query. You can see the different ones
that are having errors here. But if you didn't know that, you
can go and actually just ask, "find some traces with errors." So we can see that there's
different error patterns, some details about it. You can see
that there's 20 traces with errors. Maybe next I'm just going to be like,
"so find me some slow services." So then it tells you a few things,
and then you can just be like, "okay, so why are these surfaces slow?" And then you can see that,
hey, it's actually going. You can see that as a specific trace ID. It's going and looking into
why that is specifically slow, where the time is being spent. So then we could, for
instance, be like, "okay, if we go back up here and we have
this trace ID, we can be like, Hey, can you analyze this trace ID?" And then I'll tell you more about that.
So then you could also be like, "okay, so what services have problems?" And then if we just felt like it,
we could be like, all right, so let's write a short poem about this. So we now have an ode to
broken services. So yeah, basically, just the types of things that you can
ask via how you would just maybe go and ask a person, or when you're going
and searching something online, you can use here for asking questions to
learn more about what's happening with your traces. So, another thing that we went and
added is a new query hint that lets you speed up your queries by
returning basically an approximate result using probabilistic sampling. Query hints are special options that
you can add to a TraceQL query to modify how Tempo processes the request. So, another feature that we added
is sampling. So, basically, we added a new query hint that lets you
speed up your queries by returning an approximate result using
probabilistic sampling. So if you haven't heard of query hints, there are special options that you can
use to add to a TraceQL query to modify how Tempo processes the request.
There was one that we added in 2.8, if you want to go check that one out. So the first thing I'm going
to do is just using TraceQL, I am going to just get a
rate of all our spans. So, we can just do rate, and then I'm going to
go and run that query. So if we take a look at the
query inspector after it runs, we can see that it takes a
little over three seconds. So now let's try using our new
query hint that basically adds dynamic sampling. So if we do width and then sample equals true, and then we run that, we can see that it takes less time. So
basically the more data that you have, the more difference that you'll end up
actually being able to see and the time that it takes between when you're running
the original query versus when you're running it with sampling. So if we
want to take a look at both of them.. so if we just go and hide
this, if we duplicate it, and we get rid of that
part there, and we run it.. We can see basically that
the two graphs look super similar. There's a little bit of difference
that you can see in some parts, but it basically gives
you an approximate idea. So this can be especially useful if you
have dashboards and you want it to run faster and be able to just
kind of see what it looks like. If you want to be able to have
more control over your query, then you can go and look
at our release notes, since there are other query
hints that we have as well. So, please go and check out these new
features, give us your opinions on them, and also the ones that we have in the
blog and in the rest of the ones that release notes as well. Also, please go to select@grafana.com
and join us in the community there. Thanks for watching!

