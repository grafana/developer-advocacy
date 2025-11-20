# Redesigned Logs Panel in Grafana 12.3

Published on 2025-11-19T21:08:05Z

## Description

The revamped panel brings color highlighting, more flexible search, and an overall smoother experience to help you quickly find ...

URL: https://www.youtube.com/watch?v=GpxHV0wYRfc

## Summary

In this video, Matias from the Observability Logs squad introduces the new logs panel being shipped with version 12.3. He highlights significant improvements, including a fully virtualized log list that addresses previous performance issues, enhanced visibility of log levels with color coding, and a new logline menu accessible via a triple dot button. Notable features include syntax highlighting for easier readability, various control options for sorting, filtering, and formatting logs, and redesigned log details available in inline or sidebar formats. The panel also supports features like connecting with the Grafana Assistant, grouping fields by type, and displaying trace IDs when applicable. Matias expresses excitement about these updates and encourages user feedback to improve the experience.

## Chapters

00:00:00 Introductions  
00:01:15 Overview of the new logs panel in version 12.3  
00:02:00 Explanation of visible log levels with colors  
00:02:30 Introduction of the logline menu and accessibility  
00:03:00 Syntax highlighting feature for log lines  
00:03:45 Detailed explanation of log controls  
00:05:00 Redesigned log details available in inline and sidebar versions  
00:06:30 Overview of new filtering options in log details  
00:07:15 Grouping of fields by type in data sources  
00:08:00 Features available in both log drill down and dashboard panels  

Hey there! I'm Matias from the Observability Logs squad, and I wanted to talk to you a little bit about the new logs panel that we are shipping with version 12.3.

To start, this is a fully virtualized list of logs, so all the previous performance issues that we had have been resolved. You will find some familiar features along with some new changes.

### Key Changes

1. **Visible Log Levels**: The log level is now always visible and shown with colors and as a string in your log lines.
   
2. **Logline Menu**: You can now access the logline menu by clicking the triple dot button at the beginning of every logline.

3. **Syntax Highlighting**: Log lines now feature syntax highlighting, which aims to make them easier to read and quicker to get context. We will highlight elements such as numbers, durations, HTTP verbs, and key-value pairs. This highlighting can be disabled by clicking a button in the log controls.

### Controls Overview

Let's go over all the available controls:

- **Expand/Collapse Button**: At the beginning, you will find a button to expand and collapse the controls.
  
- **Scroll Buttons**: Buttons to scroll to the bottom of the list of logs.
  
- **Sorting Control**: A control to change the sorting direction—newest or oldest first.
  
- **String Search**: A new feature that allows you to search for strings within your log lines.
  
- **Duplication and Filtering**: Access to duplication and filtering of your results by log level.
  
- **Timestamp Resolution**: Control to set the timestamp resolution to either milliseconds or nanoseconds, or disable it if not needed.
  
- **Line Wrapping**: Control for line wrapping, which can also format your JSON log lines.
  
- **Highlighting Toggle**: Enable and disable highlighting for better readability.
  
- **Font Size Options**: Choose an alternative smaller font size, similar to the one in the previous panel.
  
- **Download Logs**: A button to download your logs.
  
- **Scroll to Top**: A button to scroll back to the top of the list.

### Redesigned Log Details

We have completely redesigned log details, and it is now available in two versions: inline and sidebar. You can choose the one that best fits your viewport and use case. 

- You can change the type of log details by clicking a button. When using the sidebar version, you can keep multiple details open as tabs.
  
- At the top, you will find a button to connect with the Grafana Assistant, if it's available in your instance. This allows you to scroll to the log line, copy logline, access show context, and change the type of log details.
  
- Additionally, you will find inputs to filter by keys and values. 

### Information Sections

In log details, you will find different sections containing information about your log line:

- A section for the log line you are viewing, along with any links if available.
  
- A list of fields for data sources like Loki. Instead of a single list, your fields will be grouped by type, displaying parsed fields, index labels, and structured metadata.
  
- If your log lines contain a trace ID, which has a configurative drive field, we will show an embedded version of your trace.

### Panel Options

Most of these options are not only available in log drill down and explorer but are also panel options in your dashboards. You can toggle:

- Timestamps and resolution
- Line wrapping and JSON prettifying
- Enable/disable log details
- Choose the type of log details
- Enable/disable scrolling
- Enable controls
- Control font size
- All the usual log panel options

We are super excited about all these new and redesigned components, and we look forward to you using them and enjoying the best possible experience when browsing logs. 

We hope you like all these new features. Thank you for listening! As always, feel free to reach out if you need assistance. We look forward to your feedback!

## Raw YouTube Transcript

Hey there, I'm Matias from
the Observability Logs squad, and I wanted to talk to you a little
bit about the new logs panel that we are shipping with 12.3. So to start, this is a fully virtualized list of logs, so all the previous performance
issues that we had have been solved. And from there you will find some
familiar things along with some new features and changes to begin with. One of the biggest changes now is
that log level is always visible and shown with colors and as
a string in your log lines. The second thing is the logline menu, which can be now accessed by clicking
this triple dot button at the beginning of every logline. And finally, now log lines feature syntax highlighting, which aims to make log lines easier
to read and faster to get context. So we will highlight things like numbers, durations, HTTP verbs,
and also key value pairs. It can be disabled by
clicking this button on the low controls, by the way.
And speaking about controls, let's go over all of them. So at the beginning you will find
a button to expand and collapse the controls. Then buttons two,
scroll to the bottom of it, list of logs, a control to change the sorting
direction, newest or oldest first. And also one new thing, which is search
for strings between your log lines. After that, you can access the duplication and
filtering of your results by log level. After that, you have a control to set
the timestamp resolution to either milliseconds or
nanoseconds if they're available, or disable it if you don't need it. Then control line wrapping, which can also format your JSON log lines. If you're looking at JSON logs, enable and disable highlighting. And an alternative phone
size, a smaller phone size, similar to the one in the previous panel. After that, a button to download your
logs and scroll back to the top of the list. In addition, we have completely redesigned log details, and it's now available in two
versions, inline and sidebar, so you can use the one that better
fits your viewport and your use case. You can change the type of log
details by clicking this button. And when you are using
the sidebar version, you can keep multiple
details open up as tabs. And here at the top you
will find a button to connect with the Grafana Assistant
if it's available in your instance, to scroll to the log line. If you
are using this type of version, copy logline, access show context, and change the type of the
log details. Additionally, you will now find these inputs
filter by keys and values. And here in log details, you will find different sections
containing information about your logline. First, you will find a section for
the logline that you're looking at, links if it has any. Under your list of fields
for data sources like Loki, instead of a single list of fields, you will find your fields grouped by type. So we'll see your parsed fields and your index labels and
your structure metadata. Additionally, if your log
lines contain a trace id, which has a configurative
drive field and a [inaudible], we'll show an embedded
version of your trace. And on these options or
most of these options, you can not only use it in log
drill down and in explorer, but they are also available as
panel options in your dashboards. So you can also toggle
timestamps and resolution, line wrapping and JSON prettifying, enable and disable log details,
choose the type of log details, enable and disable
scrolling, enable controls, control font size, and all
the usual log panel options. We are super excited about all these new
and redesigned components and we look forward for you to use them and enjoy the
best possible experience when browsing logs. So we really hope you
like all these new features. Thank you for listening, and as always,
feel free to reach out if you need it. We look forward for your feedback.

