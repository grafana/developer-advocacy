# Improved Table Visualization Performance &amp; New Features: Wrap Header Text, Frozen Columns and More

Published on 2025-09-25T14:49:42Z

## Description

The table visualization in Grafana 12.2 has been re-engineered from the ground up, delivering up to 75% faster performance ...

URL: https://www.youtube.com/watch?v=FAf-0Stmf9A

## Summary

In this video, Paul Marbach, a staff engineer on the DataViz team at Grafana Labs, discusses the release of the revamped table visualization in Grafana 12.2, which became generally available on September 23, 2025. He highlights significant performance improvements, including a 75% enhancement in rendering complex tables with large datasets. The new version introduces several long-requested features, such as text wrapping for headers, the ability to freeze columns, and a maximum row height setting for text wrapping. Additionally, two new cell types—the pill cell and markdown/HTML cell—are introduced, along with updates to the table footer for better configurability. Marbach also mentions the new tooltip feature, which allows any field in the table to provide tooltip content. He encourages viewers to check the Grafana documentation for more details on these enhancements.

# Introduction to the Revamped Table Visualization

Hey there, I'm Paul Marbach, a staff engineer on the DataViz team at Grafana Labs. Today, we're going to talk about the release of the revamped table visualization, which is generally available in Grafana 12.2 as of September 23rd, 2025.

## Performance Improvements

The new table visualization performs significantly better when rendering large quantities of data compared to the previous version. We've re-engineered the table from the ground up, leading to improvements in initial rendering of up to **75%** for complex tables with lots of data. These enhancements in performance and architecture will provide a solid foundation for adding new features in the future.

## New Features

We're excited to announce that some long-requested community features are shipping alongside this rework in 12.2. These include:

- The option to **wrap header text**
- The capability to **freeze a number of columns** from the left side of the table
- A setting to **cap the maximum row height** if text wrapping is enabled

Additionally, we've introduced two new cell types in 12.2:

- **Pill Cell**: Renders lists of strings and colorized blocks
- **Markdown and HTML Cell**: Uses GitHub-flavored markdown to render dynamic markdown or HTML content

## Footer Updates

The table footer has also been updated to support multiple reducers and greater configurability. Now, footer reducers can be configured per field instead of solely at the table level.

## Tooltip Feature

Finally, we've added a feature called **tooltip from field**, which allows you to use any of the fields in your table as the source of tooltip content.

For more information on all the new features of the table visualization, check out the **What's New** articles and the Grafana documentation.

## Raw YouTube Transcript

Hey there, I'm Paul Marbach, a staff engineer on the
DataViz team at Grafana Labs. Today we're going to talk
about the release of the
revamped table visualization, which is generally available in
Grafana 12.2 on September 23rd, 2025. The new table visualization performs
significantly better when rendering large quantities of data in
the previous version. We've re-engineered the
table from the ground up, and we've seen improvements in initial
rendering of up to 75% for complex tables with lots of data. These improvements to the performance and
architecture of the table will give us the solid foundation we need to
add new features going forward, and we're excited to announce some
long requested community features are shipping alongside this rework in 12.2, including the option to wrap header text, the capabilities to freeze a number of
columns from the left side of the table, and a setting to cap the maximum row
height if text wrapping is enabled. We've added two new cell types
in 12.2, the pill cell, which renders lists of
strings and colorized blocks, and the markdown and HTML cell, which uses GitHub flavored markdown to
render dynamic markdown or HTML content. The table footer has been updated to
support multiple reducers and greater configurability. Now, the footer reducers can be configured
per field instead of solely at the table level. Finally, we've added a
feature called tooltip from field, which allows you to use any of the fields
in your table as the source of tooltip content. Check out the What's New articles and
the Grafana docs to learn more about all of the new features of
the table visualization.

