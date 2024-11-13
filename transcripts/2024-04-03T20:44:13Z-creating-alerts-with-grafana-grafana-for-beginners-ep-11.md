# Creating alerts with Grafana | Grafana for Beginners Ep 11

When observing your data with Grafana, you don't need to be glued to your dashboard 24/7. Join Senior Developer Advocate, ...

Published on 2024-04-03T20:44:13Z

URL: https://www.youtube.com/watch?v=6W8Nu4b_PXM

Transcript: Hey! Welcome to Grafana for Beginners. I'm 
Lisa Jung and I'm a developer advocate at   Grafana. In this series, we've been using the 
Grafana dashboard to observe our E-commerce   app. As beautiful as these dashboards are, we 
probably don't want to look at it 24/7. Instead,   we can have Grafana keep an eye on our data and 
alert us if something needs our attention. This   is an example of an alert you may receive from 
Grafana. Today, we're going to create an alert for   high service latency observed in our e-commerce 
app. If service latency is greater than 2 seconds,   then an alert will be emailed to us. This 
alert will display contextual information   and the option to view the dashboard or the 
panel associated with this event. To start,   go to your Grafana instance and expand the menu 
option. From the menu, locate the Alert and IRM   option then click on the arrow to display the sub 
menu. From there, click on the alerting option to   get to the alerting page. There are three steps 
to creating alerts. First, you define a condition   that must be met for an alert to fire. Then, you 
configure where the alert should be delivered. You   do that by establishing contact points. Then, you 
configure which alerts are sent to which contact   points. This is known as defining notification 
policies. We'll start by defining an alert rule   so click on the "Manage alert rules" option, then 
click on the "New alert rule" button. This page   will allow you to define the rule. First, we'll 
give the alert rule a name. We want the alert   to fire if high service latency is observed, 
so we'll name the rule to reflect that. Next,   we'll define the query and alert condition. Let's 
zoom in. Before we can define the alert condition,   we got to tell Grafana what data it needs to 
retrieve and monitor. You can do that by writing   a query in section A. This query asks Grafana to 
retrieve latency data from all services. There   will be times when you need to make changes to the 
retrieved data. For example, your use case might   call for monitoring the average value instead of 
data in its original state. You can manage that by   going to the Expression section, then to section 
B, Reduce. This section allows you to pick the   data you want to change and choose a function you 
want to apply to the data. Using the input option,   you could choose the data you want to change. 
You'll see that the input is selected to A   by default. This means that it's taking the data 
queried from section A. Using the Function option,   you could choose how you want to change the 
data. When you click on the arrow button,   it shows a list of functions such as minimum, 
maximum, mean, sum, etc. You can specify what   function you want to execute by clicking on the 
option. For our example, we're not going to make   any changes so click out of that. Depending 
on your use case, you may want to apply other   operations to make changes to the data. When 
you click on the "Add expression" drop-down,   it shows a list of operations available. If 
you want to delve deeper into these operations,   click on the info card up top to access the 
documentation. Next, we'll set the threshold   in which the alert will fire. We'll instruct 
Grafana to monitor the data queried from section   A so we'll select A as an input here. If the 
service latency is greater than 2 seconds,   we want the alert to fire. So we'll select 
the option "Is above" here. One thing to note:   our service latency data is in milliseconds so we 
need to define the threshold in the same unit of   measurement. 2 seconds is 2,000 milliseconds so 
we'll put that there. To make sure everything is   working correctly, we can click on the "Preview" 
button. This is a great way to test that the alert   rule is set up correctly. Let's take a look at 
section A where we wrote the query. As intended,   it retrieves the service latency data from all 
services within the E-commerce app so the query   is working. Section B - Reduce shows the result 
of whatever operation we apply to the retrieved   data. We didn't change anything so we see the same 
values here. Section C -Threshold shows whether   any services exceeded the threshold condition to 
fire an alert. If the service latency greater than   2,000 milliseconds was observed, it gets a value 
of 1 and the alert fires. If not, it'll show the   value of 0. So it looks like checkout was the 
only service whose latency was greater than   2,000 milliseconds. If we look to the left to 
see the latency value of the checkout service,   we see the value 7,750 milliseconds, which should 
definitely fire an alert. So the alert rule seems   to be sound. Next, we'll move on to the evaluation 
behavior. When you're observing your system,   the chances are you're working with multiple 
alert rules. These rules would be easier to   find and manage if you organize them into folders 
and groups. So let's start by designating a folder   to store the alert rule. I don't have any folders 
set up so I'll click on the "New folder" option.   In the popup menu, give the folder a descriptive 
name. We'll name this "Microbs Alerts",   then click on the "Create" button. You'll 
see that the alert rule has been stored in   the folder "Microbs Alerts". Next, we'll move on 
to the Evaluation group. This grouping is used   when you have multiple alert rules that should be 
evaluated over the same time interval. A situation   that may call for this grouping would be if you 
had alert rules for service throughput, errors,   and latency. Instead of individually setting the 
same time interval for each rule, we can put these   rules in the same evaluation group. So whatever 
time interval is set for the group gets applied to   all. Let's pretend that we're in the same scenario 
and create a new evaluation group. To do so, click   on that option. Next, we'll name the evaluation 
group for alert rules for service throughput,   errors, and latency. These three factors are often 
referred to as RED metrics, which stands for Rate,   Errors, and Duration. So I'm going to name this 
group "RED alerts". The evaluation interval   specifies how often the rule is evaluated. This 
interval depends on your specific need. We'll   enter 5 minutes here, then click on the "Create" 
button. All right. Let's talk about the pending   period. Think of this as a grace period in which 
something could be off until an alert is fired.   For example, if high service latency is observed 
for a brief moment but returns to normal state   right afterward, you probably don't need to be 
alerted about that. But if high service latency   persists for let's say 5 minutes, something is 
off and we should be alerted about it. I put 5   minutes down as an example but the value will 
vary depending on what your goals are. Next,   we'll add labels to this alert rule. Labels come 
in handy in many ways. These could be used for   search. These could be used to route your alerts 
to different contact points. These could also   be used to provide context in the alert details. 
It may sound pretty abstract right now but we'll   see how these labels come into play in a bit. I'm 
going to pull up the alert notification we've seen   earlier. In the alert, we see two labels called 
App with the value of E-commerce and Severity with   the value of Critical. As you can see, these 
labels provide some context about the alert.   So let's create these labels by clicking on the 
"Choose key" option. We'll type in the word App   and hit enter. Then click on the "Choose value" 
option and type in the word "E-commerce". Next,   we'll create a label for Severity. To create this 
label, click on the "Add label" option and repeat   the same process. Now that the two labels are 
added, we will add annotations. In this context,   annotation refers to the information included 
in the alert notification. Let's take a look   at the alert message again. In the alert, we 
want the summary to show that high latency was   observed. We also want the name of the service 
that triggered this alert. To create this,   we'll go to the Summary section. We'll enter the 
words "High latency" then a dash. We'll also add   a variable that will display the name of the 
service associated with this alert. Next, we   want to create custom annotation to show that the 
SLO - the service level objective is 2 seconds. So   we'll click on the "Add custom annotation" button 
here. It will prompt us to add the annotation   name and the content. Under the annotation 
name, I typed in SLO. Under the content,   I typed in 2.0 seconds. Using the same method, you 
could add any annotations you wish. Grafana also   offers an option to link the dashboard and the 
panel associated with the alert. To set this up,   click on that option from the popup menu. Select 
the dashboard and the panel relevant to the alert.   Then click on the "Confirm" button. You'll see 
that the dashboard and the panel have been linked   to the alert rule. We're done setting up the alert 
rule so click on the "Save rule and exit" button.   Now that we have defined an alert rule, we'll 
configure where we want the alert to be sent.   We do this by establishing contact points. From 
the menu, click on the "Contact points" option,   then click on the "Add contact point" button. 
Next, we'll name the contact point. Since   we want the alert to go to the SRE on call, 
we'll name the contact point as such. Next,   we'll select what channel we want to use to 
send the alert. When you click on the arrow,   it gives you a list of channels that can be used 
to send the alert. When you select an option,   it will ask for the info needed to set up the 
contact point. For our example, we'll set up   a simple email so select that option. All you 
have to do is to enter the email addresses here,   then click on the "Save contact" button. It will 
ask you to test the contact point. I just want to   check if it works, so I'm going to select the 
"Predefined" message and click on the "Send   notification" button. When you check that email, 
you'll see that a test alert has been sent to you.   Now we know that we can successfully send alerts 
to the contact point. So go back to the Grafana   page and click on the "Save contact point" button. 
Next, we'll configure which alerts are sent to   which contact points. This can be done by defining 
the notification policies so click on that option.   Next, click on the "New nested policy" option. 
Under the notification policy, we specify which   alert should be sent to which contact point. We 
want the alerts regarding high service latency   to be sent to the SRE on call. Earlier, we added 
some labels to our alert rule. We'll use these   labels to identify which alert we want to send 
to the SRE on call. To do so, we'll add the first   label App with the value of E-commerce. Under the 
label, type in the word App and hit enter. Set the   operator to an equal sign, then type in the value 
E-commerce under the value section and hit enter.   Next, we'll add another label Severity equals 
Critical. To do so, click on the "Add matcher"   button. Repeat the same process to add the second 
label. Then we'll choose where the alert should   be sent. To do so, click on the "Contact point" 
drop down menu and we'll select the contact point   "SRE on call" then click on the "Save policy" 
button. You may want to further customize your   notification policies to fit your team's needs. If 
you want to learn about how to do so, click on the   info card up top to access the documentation. 
All right, so we just created an alert rule,   established a contact point, and configured the 
alerts to be delivered to that contact point. When   Grafana observes service latency that meets the 
condition, it will send you an alert via email.   An alert will look like this. It's titled as 
High service latency. Under the summary, we   see that high latency was observed in the product 
service. The values show the latency data from the   product service. Remember when we set up the alert 
rule? These values from the alert comes from the   sections A, B, and C. In the alert rule page, A is 
a latency data pull from section A, where we wrote   the query. B is the value calculated in section 
B, where you perform operation on the retrieved   data. C is a value pulled from section C where we 
set the threshold. You'll see the value of 1 if   service latency exceeds the threshold. Since the 
alert was fired, you'll see the value of 1 here.   Next, we see the labels we specifically created 
some of these labels such as App and Severity.   The others were pulled from the selections we 
made while creating the alert rule. Together,   these give you context about the alert that 
you have received. Under the annotations,   we see the custom annotation we created earlier, 
which shows that the SLO is 2 seconds. Then you   can either silence this notification or view the 
linked dashboard or the panel by clicking on it.   Before we go to the dashboard, we'll make a note 
of the timestamp when the alert was sent. When you   go to the linked dashboard, select the time and 
the date of when the alert was fired and apply   the time range. It'll take you back to the time 
when the alert fired. Earlier, we linked the panel   "Service latency" with the alert rule. You'll see 
a bunch of dotted lines with arrows on the bottom.   The yellow dotted line shows when the threshold 
was initially exceeded. If the condition persists   beyond the pending period, you'll see an alert 
fire. This is marked by the red dotted line. The   green dotted line is shown if something exceeded 
the threshold but has returned to its normal   state. If you hover over the arrow, it'll show you 
the information about the alert. This is another   way to get more context so you can decide on the 
next steps. All right. We just went over how to   configure Grafana to keep an eye on our data and 
alert us if something needs our attention. Up   until this point, we operated graph as a single 
user. But if you're in an organization where   multiple people are using Grafana, you'll need to 
manage users and permissions. We'll learn how to   do that in the next episode. If you want to access 
more episodes of the Grafana for Beginners series,   go to the Grafana community web page. This is 
where all the community resources are shared.   You can access the series by clicking on the 
Grafana for Beginners card. Last but not least,   we all have different ways of learning. If 
you prefer to learn by reading instead, we   have a blog page. From this page, you can access 
blogs about news, releases, technical articles,   and more. All right, that's a wrap. Thank 
you for watching and I'll see you in the next episode!

