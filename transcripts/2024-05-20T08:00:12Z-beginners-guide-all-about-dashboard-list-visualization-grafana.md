# Beginners Guide - All about Dashboard List visualization | Grafana

Do you want to know what a dashboard list visualization is and how you can create one in Grafana? Join Senior Developer ...

Published on 2024-05-20T08:00:12Z

URL: https://www.youtube.com/watch?v=MserjWGWsh8

Transcript: Hi everyone! My name is Marie Cruz,   and I’m a Senior Developer Advocate here at 
Grafana Labs. In this quick video tutorial,   I’ll show you how you can use the 
dashboard list visualization in Grafana. Before we delve into how to 
create this visualization,   let me first explain what a dashboard list is. A dashboard list allows you to display 
dynamic links to other dashboards. This   is useful if you want to display a 
list of essential dashboards that   you want to track rather than manually 
navigating to these different dashboards. You can configure your dashboard 
list to display your most favorite   dashboards or starred dashboards, 
your recently viewed dashboards,   or dashboards that might 
contain a specific tag or query. Speaking of Grafana dashboards, check out this 
video that my awesome colleague Tom Glenn did,   in which he explained what dashboards 
are from a beginner-level perspective. Now that you know what a dashboard list is 
and what it’s used for let’s see how we can   create this visualization in Grafana. But as a 
pre-requisite, make sure that you already have   created other dashboards in order for 
this visualization to work correctly. Ok, now let’s get started! Let’s create a new dashboard and click Add 
Visualization. I don’t need to configure any   data sources, so I can go ahead and close this 
window. I’m going to change my visualization   type to a dashboard list. By default, Grafana 
will display any dashboards that you have marked   as favorites. I have a different dashboard 
on a different tab, which I will mark now   as a favorite. Returning to my dashboard 
list and refreshing the visualization,   you can see that the newly starred or new 
favorite dashboard has now been added. Let’s   add a title for this panel, toggle the show 
heading option off, and save our changes. Let’s add another dashboard list 
visualization, but this time,   I want to display the dashboards I 
have recently viewed. I’m going to   toggle the starred option off and toggle 
the recently viewed option on. By default,   Grafana displays a maximum of 10 items, 
but you can configure this to your liking. Let’s add a title for this panel and toggle 
the show heading option off. I will also update   the timestamp to only display data for the 
last hour instead of the last 6 hours. Then,   I’m going to turn on the include current time 
range option. This option will propagate the   current dashboard's time range to the different 
dashboard links. When I click a dashboard link,   the linked dashboard opens with 
the time range already set. Let me save and apply all the changes. The final dashboard list I want to show 
is a list of dashboards using a specific   query or tag. In Grafana, tags are used to 
organize your dashboards better. To add a tag,   just go to your dashboard 
settings and add the tag here. Now, let’s create another dashboard list 
visualization to showcase our dashboards   with similar tags. I’m going to toggle 
the starred option off and toggle the   search option on. Then, under search, I’m 
going to type demo-dashboard-list. You   should now see a list of dashboard 
links with this particular tag. You can also use specific queries 
or strings. So, for example,   if I want to filter my dashboards based 
on a particular string, such as the word   cardinality, this will only display the 
dashboard links that contain this word. And there you have it! In this 
beginner-friendly video tutorial,   I’ve shown you how you can configure a 
dashboard list visualization in Grafana. Check out our documentation if you want 
to know more about the dashboard list,   which you can find in the video description below. I hope you found this video useful, and if you do,   let us know in the comments below 
and as always, happy visualizing!

