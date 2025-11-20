# How to Use Raw Queries in the Honeycomb Enterprise Data Source for Grafana

Published on 2025-11-19T21:08:37Z

## Description

With our Honeycomb Enterprise data source for Grafana, you can query and visualize Honeycomb metrics and link to Honeycomb ...

URL: https://www.youtube.com/watch?v=B1pDjfBDs1o

## Summary

In this video, Diego from the Enterprise Data Source Squad introduces a new feature in the Honeycom data source plug-in that allows users to write Honeycom queries directly in JSON format, providing more control compared to the visual builder. He demonstrates the use of a new query type called "raw query," which includes an editor for entering JSON queries. Key points discussed include automatic handling of filters requiring arrays and variable substitution functionality. Diego shows practical examples of how modifying query parameters affects the results returned, and highlights the addition of a new variable query type called "data set name" for easier querying. Overall, the video aims to enhance user experience and flexibility in querying data.

## Chapters

00:00:00 Introductions by Diego  
00:00:30 Overview of the Honeycom data source plug-in  
00:01:00 Introduction of raw query feature  
00:01:30 Explanation of writing queries in JSON format  
00:02:00 Demonstration of a query that counts values with filters  
00:02:30 Automatic handling of array filters in queries  
00:03:00 Variable substitution in the query builder  
00:03:30 Live demonstration of running a query and modifying it  
00:04:00 Explanation of new variable query type: data set name  
00:04:30 Conclusion and thank you message from Diego  

# Honeycom Data Source Plug-in Feature Overview

Hi, I'm Diego from the Enterprise Data Source Squad. Today, I will walk you through a new feature in the Honeycom data source plug-in: support for Honeycom queries.

Our queries are designed for users who want more control over their queries. Instead of relying only on the visual builder, you can now write queries directly in JSON using the same format that the Honeycom API accepts in the query explorer.

You will notice a new query type called **Raw Query**. When selected, an editor appears where you can enter your query in JSON format. Here's an example of a query that counts values from a column while applying a filter.

## Key Points

- Filters that require arrays, such as the `in` or `not in` operators, are handled automatically. This means that if you use a multi-value variable, Grafana will convert it into the correct JSON array before sending the query to Honey.
- Variable substitution also works in the query builder.

### Example Usage

Let’s take a look at how this works. We have a query that, when run, returns results. For instance, if we remove one of the values from the array (say, the number one) and run the query again, it won't return any data because it's now looking for values that do not match the filtering criteria.

We can also replicate this in the query builder. If we select a column (let me get the name of the column), it won’t return data because the value we removed is missing. However, once we add the value back in, it starts returning results again.

### New Variable Query Type

Additionally, we’ve added a new variable query type called **Data Set Name**. In addition to querying by data set slug (the currently supported variable query type), you can now query by the data set name as well. This makes it easier for those who prefer or need to build queries using data set names rather than data set slugs.

That’s it for today. Thank you!

## Raw YouTube Transcript

Hi, I'm Diego from the Enterprise Data Source Squad. Today I walk you through a new feature in the Honeycom data source plug-in support for honeycom queries. Our queries are designed for users who want more control over their queries. Instead of relying only on the visual builder that you can see here, you can now write queries directly in JSON using the same format that the honeycom API accepts in the query explorer that you can see. You now see a new query type called raw query right over here. When selected, an editor appears where you can enter your query in JSON format. Uh here's an example of a query that counts values from a column while applying a filter. Uh few key points over here. Filters that require arrays such as the int or not in operator that you can see here uh are handled automatically. Meaning if you use a multialue variable, Graphana already going to convert this into the correct JSON array before sending the query to Honey. Um, and of course uh variable substitution also works uh in the query builder as well. Um, but let's go back and see how this is going to work. So we have this query here. If you run the query, um, you're going to see, of course, that it's already returning this result. But for example, if we remove one of the values from this array, for example, number one and run the query again, it doesn't return any data because now it's looking for values that are not uh getting the the match of the filtering. Uh we can do the same thing on the query builder where we can do um select a column. Let me get the name of the column here. This is the column where it end. It's not returning data because the one we removed. But once we add the one again, now it's returning. So uh it works both in the query explorer and the raw query format and we also added a new variable query type. So um the variable query type that we added is called uh data set name. we can see over here. Um and in addition to querying by data sets lug which is the currently supported uh variable query type uh you cannot now query by the data set name as well. This make it makes it easier for those who prefer or need to build queries using data set uh data set names rather than data set slugs. Um, and that's it for today. Thank you.

