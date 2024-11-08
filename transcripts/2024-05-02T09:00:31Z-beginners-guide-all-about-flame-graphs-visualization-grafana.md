# Beginners Guide - All About Flame Graphs Visualization | Grafana

Do you want to know what continuous profiling is and how flame graphs can help? Join Senior Developer Advocate Marie Cruz in ...

Published on 2024-05-02T09:00:31Z

URL: https://www.youtube.com/watch?v=VEvK0JkPlOY

Transcript: Hi everyone! My name is Marie 
Cruz, and I’m a Senior Developer   Advocate at Grafana Labs. In this 
beginner-friendly video tutorial,   I’m going to share with you everything that I 
learned about flame graphs that you should know. By the end of this video tutorial, you should also   know what data a flame graph needs so you 
can visualize it correctly in Grafana. To understand flame graphs, an understanding 
of profiling is quite essential. Profiling is a   technique used in software development to measure 
and analyze the runtime behavior of a program. Profiling tools collect data about various aspects 
of the software's execution, such as CPU usage,   memory usage, or input/output operations. 
You can use the collected data to identify   any bottlenecks, resource-intensive 
code, or inefficient algorithms that   may be causing the software to run 
slowly or consume excessive resources. Profiling is often done in a snapshot 
manner, meaning it captures a snapshot   of the program's behavior at 
a specific time. Continuous   profiling takes the concept of profiling a 
step further by continuously monitoring and   analyzing the behavior of your program. 
Instead of just capturing a snapshot,   continuous profiling allows you to collect data 
continuously while your program is running. There are many profiling tools out there, one 
of which is Grafana Pyroscope. To learn more   about Pyroscope, check out the useful 
links in the video description below. Anyway, as you can imagine, the data that's 
collected by profiling tools can be thousands   and thousands and thousands of lines long 
and it can be very difficult to understand. So, if you quickly want to 
discover the hottest code paths   that are time-consuming or resource-intensive,   using a flame graph can quickly point you 
to where the optimizations are needed. To understand how to read a flame graph, let’s 
consider the scenario of a day in my life as   a Developer Advocate, which is inspired by 
Miha Rekar’s explanation of a flame graph. A typical day for me consists of the following: 
doing the morning school run, doing some admin   work such as reading and replying to emails 
or Slack messages, doing actual Grafana work,   whether that's learning about a new visualization 
type or updating some tutorials, walking the dogs,   having a break, reading and replying to more 
emails and Slack messages, more Grafana work,   such as video recording, joining any 
meetings that I need to be part of,   doing the afternoon school run, having 
a second break, more Grafana work,   such as video editing, and finally replying 
to any unread emails and Slack messages We then end up with this visualization. 
Flame graphs are not time-series data,   which means that your data will not be visualized 
in a time-ascending order. A flame graph will   group similar things together and can give 
you a quick overview of what’s happening. So,   for this example, you can see where I spend 
most of my time by simply looking at the   width of each horizontal block, and I can 
also see which areas I can optimize even more,   such as maybe reading or replying 
to emails and Slack messages less. In Grafana, you must format your data 
as a nested set model to visualize it   effectively as a flame graph. Your data must 
have a few required fields such as the label,   the level, the self, and the value. The level represents the nesting level of 
the item, with 0 being the top level or the   parent item. As the level increases, the 
further it is from the parent item. These   items are the child items. The label 
is simply the name of the item itself. The self refers to the actual value of the 
resource usage of a specific item or function,   but excluding the resources used by the 
child items or the sub-functions. Finally,   the total refers to the combined value or 
the resource usage of an item or a function   along with all of its child items and any 
sub-functions that it's going to call. Now that you have an overview 
of profiling and flame graphs   let’s look at how a flame graph 
visualization works in Grafana. OK, as usual, let’s add a new visualization 
to our dashboard, change our visualization   type from Time series to a flame graph, and 
make sure the grafana-testdata-datasource is   selected. Then, under the scenario, I’m 
going to pick the Flame graph scenario. Let’s explore the data first by going to the 
table view. You can see that our data contains   different labels for our items, and the level 
of the items, the self, and the total value. Returning to the visualization view, Grafana 
displays a table format along the flame graph   by default. You can toggle the view easily by 
clicking the flame graph or the top table view. Looking at the table view, by default, the 
table is sorted by the self value, but it   can be reordered by the total value or the label 
or symbol name by clicking the column headers. Clicking the symbol name or the search icon 
highlights the function in the flame graph.   Besides the search icon, another icon shows the 
sandwich view for the function when clicked. The   sandwich view shows all the function’s callers 
on the top and all the callees at the bottom. Focusing on just the flame graph, clicking a 
function will show a drop-down of additional   actions that you can call. The focus block 
makes it easier to drill down into the smaller   parts of the flame graph by focusing on the 
stack trace call from the parent function up   to that particular child function. The 
copy function name is straightforward,   and the sandwich view is similar to what 
you already saw from the table view. You can change the color scheme 
by their value or by their package   name to visually tie functions 
from the same package together. And there you have it! In this beginner-friendly 
video tutorial, I’ve shown you what flame graphs   are and how you can easily configure a 
flame graph visualization in Grafana. Check out our documentation if you want to 
learn more about flame graphs, profiling,   or Grafana Pyroscope in general, which you 
can all find in the video description below. I hope you found this video useful, and if you do,   let us know in the comments and 
as always, happy visualizing!

