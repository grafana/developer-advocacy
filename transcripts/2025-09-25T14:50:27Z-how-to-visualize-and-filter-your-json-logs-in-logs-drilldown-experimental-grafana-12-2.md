# How to Visualize and Filter your JSON Logs in Logs Drilldown (Experimental) | Grafana 12.2

Published on 2025-09-25T14:50:27Z

## Description

Grafana 12.2 brings a new JSON panel to Logs Drilldown, giving you more ways to explore and filter JSON logs. Expand and ...

URL: https://www.youtube.com/watch?v=YmjEPmjJrEU

## Summary

The video introduces a new feature in the logs drilldown, specifically an experimental JSON visualization panel designed to enhance the analysis of JSON logs. The panel allows users to easily expand and collapse nodes within their JSON logs and enables the selection of new root nodes for focused visualization. Key functionalities include the ability to filter logs based on specific JSON node values, and the use of breadcrumbs for easy navigation back to parent nodes. The feature is available in logs drilldown version 1.0.14 for users utilizing Loki 3.5 or higher, although it currently only returns results from a dataset with identical nodes.

# New in Logs Drilldown: JSON Visualization

In logs drilldown, we're releasing experimental support for a new JSON panel to help visualize and filter your JSON logs. 

The **JSON panel** allows users to:

- Expand and collapse any node in their JSON logs.
- Visualize a specific part of the JSON logs by clicking on the **I icon** to drill down into the JSON object and set a new root node. This feature enables easy comparison of values in a nested JSON object.

The **breadcrumbs** at the top of the panel provide a way for users to quickly drill back up to the parent nodes. Additionally, users can filter by JSON nodes, allowing them to filter logs that contain a certain value at that location in the JSON object or exclude logs that contain that value.

If a parent node is filtered (a node containing other nodes), all logs that contain that node in that position will be visualized or excluded. 

With our current data set, all logs have the same nodes, though we get back no results from Loki. 

The **JSON panel** is available in logs drilldown 1.0.14 for users running Loki 3.5 or greater.

## Raw YouTube Transcript

New in logs drilldown, JSON visualization. In 
logs drilldown, we're releasing experimental support for a new JSON panel to help visualize and 
filter your JSON logs. The JSON panel allows users to expand and collapse any node in their JSON 
logs. If you want to visualize a specific part of your JSON logs, simply click on the I icon to 
drill down into the JSON object and set a new root node. This allows easy comparison of values in a 
nested JSON object. The breadcrumbs at the top of the panel allow users to quickly drill back up to 
the parent nodes. Additionally, users can filter by JSON nodes, filtering logs that contain 
a certain value at that location in the JSON object or excluding logs that contain that value. 
If a parent node is filtered, a node containing other nodes, all logs that contain that node in 
that position will be visualized or excluded. With our current data set, all logs have the same 
nodes, though we get back no results from Loki. The JSON panel is available in logs drilldown 
1.0.14 for users running Loki 3.5 or greater.

