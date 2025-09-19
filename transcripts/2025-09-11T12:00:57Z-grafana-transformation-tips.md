# Grafana Transformation Tips

Published on 2025-09-11T12:00:57Z

## Description

Learn the valuable tips when using Transformations in Grafana for your Dashboard Panels. Link to complete video: ...

URL: https://www.youtube.com/watch?v=URNkf7XVTSU

## Summary

In this video, the speaker discusses the importance of optimizing data transformations when building dashboards to enhance performance and efficiency. They emphasize that transformations can significantly slow down dashboards if not managed properly, especially when dealing with large datasets. The speaker suggests that if users have control over their API, they should aggregate data before it reaches the transformation stage, which can reduce the load on visualizations and improve overall responsiveness. The focus is on strategies to streamline data processing for better dashboard performance.

To effectively use transformations, it's important to think about how you want to build your dashboard to ensure it's optimized. Here are some key points to consider:

- **Optimize your data sources:** Your databases contain various options for optimizing storage, and you can typically find ways to optimize your APIs as well. 

- **Understand the impact of transformations:** Transformations run on your computer alongside everything else. If you're processing a large dataset and executing a transformation—like pivoting a table or significantly manipulating data—it can slow down your dashboard, and your browser may struggle.

- **Aggregate data when possible:** If you have control over your API, consider aggregating data before it reaches your transformations. This approach can help reduce the workload downstream, making your visualizations more efficient and responsive.

By keeping these factors in mind, you can create a more effective and optimized dashboard experience.

## Raw YouTube Transcript

to use transformations are the time to think about how you want to build your dashboard is just to make it optimized. Like you can optimize stuff, you know, your, your data source databases have a bunch of stuff to optimize storage, your API, you can generally do things to optimize that. transformations, you know, they're running on your computer with everything else that's running on your computer. And so if you're going through a big chunk of data and you're running like a transformation that will like pivot a table or manipulate the data really a lot, that can really slow down your dashboard and just your browser will have a very bad time. So I kind of think of it like this, if you can cut, if you can, aggregate your data like if you have control of your api and you can aggregate your data coming from the api that will help everything downstream from your transformation will have less to to churn through and your visualization will have will be more

