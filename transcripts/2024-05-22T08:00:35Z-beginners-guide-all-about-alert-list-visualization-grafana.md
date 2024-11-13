# Beginners Guide - All about Alert List visualization | Grafana

Do you want to know what an alert list visualization is and how you can create one in Grafana? Join Senior Developer Advocate ...

Published on 2024-05-22T08:00:35Z

URL: https://www.youtube.com/watch?v=o4rK7_AXZ9Y

Transcript: Hey everyone! My name is Marie Cruz, and I’m a 
Senior Developer Advocate here at Grafana Labs. In   this quick video tutorial, I’ll show you how you 
can use the alert list visualization in Grafana. To understand how an alert list works, you first 
need to understand the concepts of alerting. In a nutshell, alerting is a process that's 
designed to notify individuals or systems   about certain events or conditions that 
require immediate attention or action. In Grafana, the alerting 
feature periodically queries   your data source and evaluates the 
condition defined in an alert rule.   An alert rule is simply an evaluation 
criteria for when an alert should fire. If the condition defined in the alert rule is met,   Grafana can trigger notifications to alert you 
and your team about potential issues or anomalies. You can also link an alert to a dashboard panel,   which I've explained in this video and it's 
also added in the video description below. But, what if you want to display a list of 
important alerts that you want to track as a   different dashboard panel? This is where 
an alert list visualization can help. An alert lists allow you to display a list of 
important alerts that you want to keep track of   rather than navigating to different alert rules 
manually. Every time your dashboard reloads,   the alert list is also reloaded meaning you always 
get the most up-to-date results for your alerts. With that explanation out of the way,   let’s see how you can configure the 
alert list visualization in Grafana. I have an existing panel created already, 
using the time series visualization,   which monitors the traffic that’s coming to 
this example application called Grafana news. In order to use the alert list visualization, you 
need to configure the alerting feature in Grafana   so let’s create an alert rule first. To set this 
up, I’m going to click the Grafana menu icon here,   navigate to alerting, and then click alert rules. 
Now, let’s create a new alert rule, and I’m going   to give my alert rule a name. I’m going to use the 
same PromQL query as my time-series visualization. Now, let’s scroll down, and 
under the expressions section,   I’m going to keep the default values 
for simplicity. If I quickly preview   these expressions, you can see that one 
of the alert rule state is set to firing. So now, I’m going to just provide a folder where 
the alert rule will be stored. I’m also going to   create an evaluation group and I’m going to 
set my evaluation interval to 10 seconds,   which is how often the alert rule should 
be evaluated. I’ll also update the   pending period to 0 because I want the 
alert to fire immediately for this tutorial Let’s go ahead and click save rule and exit. I’m going to create another alert rule just so we   can simulate having more than 
one alert in our alert list. Now, let’s go back to our dashboard, add a new 
visualization, and change our visualization   type to an alert list. You should see the 
alert rules that we have recently created. Expanding each of the alerts provides 
you with more details and you can   also view the alert rule directly from the list. Over to this side, you can see all the 
alert list options that you can configure. By default, Grafana displays your 
alerts as a list, but you can also   view them as a stat or a single number. 
I’ll leave it as a list for this tutorial. You can also choose how you want to group your 
alerts. You can group them by the alert name   or by their folder. You can also choose to just 
display alerts that are linked to this dashboard. You can also use some filtering 
options, such as by text, label,   data source, or folder. Let’s say, for 
example, that you only want alerts with   specific labels displayed. I’ll update one of 
the alert rules and add an additional label. Going back to the alert list, let’s add the label   that I have added to filter out 
the alert rule with this label. And finally, you can also configure the alert 
list to filter out the state of your alert,   such as firing, pending, or normal. And there you have it! In this beginner-friendly 
video tutorial, I’ve shown you how you can   configure an alert list visualization in Grafana 
and the different ways that you can configure it. Check out our documentation if you want to 
know more about alert list visualization,   which you can find in the video description below. I hope you found this video useful. If you do,   let us know in the comments, and 
as always, happy visualizing!

