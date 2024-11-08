# Most commonly used visualizations in Grafana | Grafana for Beginners Ep. 8

The types of visualizations you can create with Grafana are endless! Join Senior Developer Advocate, Lisa Jung to learn about ...

Published on 2024-02-22T15:59:48Z

URL: https://www.youtube.com/watch?v=JwF6FgeotaU

Transcript: Hey! Welcome to Grafana for Beginners. I'm 
Lisa Jung and I'm a developer advocate at   Grafana. In the series, we've learned how to 
run Grafana, how to add data sources to it,   and how to explore the data. The next step 
is to create a dashboard of visualizations   to understand and monitor your data. But before 
we can create a dashboard, it would be helpful   to know exactly what visualizations we could 
create with Grafana. Today, we'll go over the   most commonly used visualizations in Grafana and 
when to use which visualization type to understand   your data. The time series visualization is the 
most frequently used visualization in Grafana.   As the name suggests, it's used to visualize data 
that has been collected over time. It's probably   what you think of when you hear the word graph. 
So if you ever looked at a graph that shows the   rise and fall of the temperature throughout 
the day or if you're a YouTuber tracking the   number of subscribers over time, you're looking at 
time series visualization. These could be lines,   points, bars, or a mix of all of them as shown 
here. What they all have in common is that on   the y-axis, it shows you the values of whatever 
factor you're looking at and on the x-axis, it   shows the time from left to right. You would use 
time series visualization if you want to look at   the trend. In other words, how a value is changing 
over time rather than one specific value. Next,   we have bar charts. These are useful when you 
want to compare data by categories. For example,   let's look at the bar chart of the browser 
market share. On the y-axis, it displays   different categories of browsers such as Chrome, 
Firefox, Safari, etc. On the x-axis, it shows you   the value of the market share. You could clearly 
compare the market share of each browser by   looking at the size of the bars. So if you want to 
visualize how each category compares to another,   a bar chart could be a great option. The Stat 
visualization looks something like this. You   would use this if you want real-time stats about 
a value that you're interested in. For example,   let's say you're monitoring an e-commerce app and 
you want to know the percentage of the time when   you're app isn't working the way it should. 
You would tell Grafana how to calculate the   service error rate and display that in a stat 
visualization as shown here. Next, we have gauge   and bar gauge visualizations. These look like a 
fuel gauge in your car or a volume meter on your   sound system. They show you the numeric value of 
whatever you're observing and where it lies within   the range you specify. These are especially 
useful when you're monitoring something that   you want to stay within a certain range. For 
example, let's say you're monitoring a piece   of equipment that would malfunction if it hits 
a certain temperature threshold. This is where   a visualization like a gauge would be helpful. 
With a gauge, you can tell at a glance whether   the temperature is within the acceptable range or 
if you need to take action to address it. Next,   we have a table visualization, which all of us 
are probably familiar with. It's similar to a   spreadsheet and you would use this when you want 
to show data in rows and columns. Even something   as basic as a table could be jazzed up with 
Grafana to help you monitor things that matter to   you. You can incorporate visualizations into the 
table. In this example, you see a bar gauge here.   You could also highlight rows, columns, or cells 
with different colors to bring your attention   to important information. You're also probably 
familiar with pie charts as well. With Grafana,   you can make a traditional pie chart or a doughnut 
chart as shown here. Each piece of the pie or   donut represents a category in your data and it 
allows you to see its proportionate part of the   whole. Let's look at the donut chart, which shows 
you the market share of each browser. At a glance,   you could easily tell that Chrome has the majority 
of market share, followed by Internet Explorer,   Firefox, and Safari. All right. Let's move on to 
the State Timeline and Status History. At first,   it could be a bit overwhelming to look at but 
it's quite simple once you break it down. Both   are used to observe how the state of whatever 
you're tracking changes over time. So let me   give you a scenario where you might want to use 
these. So we'll start with the State Timeline. Say   you're monitoring the temperature of a machinery 
over time. These machines are located on three   levels of the building: Levels A,B, and C. The 
temperature of these machines must stay within   a specific range to function properly. Certain 
ranges of temperatures are considered low, high,   normal, or critical, which would result in the 
malfunction of the machine. As you can see, the   State Timeline shows you how long the temperature 
stayed in a certain state. For example, in the   machine on level B, we see that the temperature 
stayed within the normal temperature reach until   hour 15, then the status changed to low from hour 
15:15 to 16:30, then the temperature fell into   the critical range from hour 16:30 to 18 and so 
on. So the State Timelines let you see how long   something stays in a certain state and when the 
state change occurs. All right, so let's look at   the Status History. Imagine that we're in the same 
building where the machinery is being monitored.   There are two entrances to the room that house 
the machine. The first door is being monitored   by sensor A. The second door is being monitored by 
sensor B. These sensors detect whether these doors   are open or closed. If it's closed, it shows a 
Boolean value of True. If it's open, it shows the   value of False. The Status History shows you the 
state at one point in time. For example, the state   of sensor B was True at hour 16:02, then was False 
at hour 16:47. Now we have no idea what the state   was between hour 16:02 and 16:47. But we know the 
state of these doors at those specific points in   time. To sum up, you would use State timeline and 
Status history if you're looking to observe how   the state of whatever you are tracking changes 
over time. If you want to observe the state   continuously over time and see when the state 
change occurred, then you would use the State   Timeline. If you want to observe the state at one 
point in time then you would use a Status History.   Next, we have Text visualization. You would use 
this when you want to add text or external images   to the dashboard. In the visualization shown on 
the screen, the text and images were added to the   dashboard using markdown or HTML. So if you want 
to jazz up your dashboard with something extra,   you could create that with text visualization. 
Now, if you want to visualize data in relation   to a location, Geomap is a visualization you would 
use. For example, this map shows you where the web   requests are coming from in the US. The larger the 
bubble, the larger the number of requests coming   in from that state. At a glance, you could see 
that we got a lot more requests coming in from   Colorado than Washington state. With Grafana, you 
could use a global map, street data, cartographic,   and geographic infosystem maps. You could also 
provide your own base layer data depending on what   you want to show. Last but not least, we have the 
Node Graph. This visualization is used to show the   state of all parts of your system and how these 
parts are connected to one another. In Grafana,   it's most commonly used to visualize trace data to 
show how services relate to one another. With this   type of visualization, you can predict how the 
state of one service will impact other services   downstream, so you can figure out what to do 
next. Now, there will be times when you need   visualizations outside of what's already available 
in Grafana. Your first stop should be the Panel   Plugins page. The link is shown on the screen 
here. This lists all sorts of plugins you could   install to create the visualization you want. All 
right, so we just learned about the most commonly   used visualizations in Grafana and when to use 
which visualization type to understand your data.   Next we'll learn how to create visualizations with 
Grafana. We'll pick a few of the visualization   types we went over and learn how to create these 
using the tools in the Grafana dashboard. So this   series goes over how to get started with Grafana 
at a high level. If you want to delve deeper into   some of these topics check out the book, Getting 
Started with Grafana. This was written by Ronald   McCollam, who is a Solutions Engineering Manager 
at Grafana. This is a resource I often turn to   when I want an overview of some of the topics that 
I cover in this series. Plus, Ronald is my go-to   person if I have any questions about Grafana so I 
definitely recommend it if you want a deeper dive   into whatever we covering in the series and more. 
If you want to access more episodes of Grafana for   Beginner series, go to the Grafana Community web 
page. This is where all the community resources   are shared. You can access the series by clicking 
on the Grafana for Beginners card. Last but not   least, if you want to connect with other community 
members and ask questions about Grafana, you could   join the Community Slack channel. To join, scroll 
down on the page and click on the Community Slack   card, get your invite to join the community on 
Slack, join the channels you're interested in, and   start chatting. All right, that's a wrap. Thank 
you for watching and I'll see you in the next episode!

