# How to Display Grafana Alerts to Your Dashboards | Grafana

Did you know you can display Grafana alerts on your dashboards? Join Senior Developer Advocate Marie Cruz in this quick ...

Published on 2024-03-11T15:15:58Z

URL: https://www.youtube.com/watch?v=ClLp-iSoaSY

Transcript: Hi! My name is Marie Cruz, and I’m a Senior 
Developer Advocate at Grafana Labs. In this   video tutorial, I’ll quickly show you how you 
can add Grafana alerting to your dashboards. By the end of this tutorial, you should 
have an alert rule linked to a panel in   your dashboard. When the condition 
in the alert rule has been breached,   you should be able to see this 
as an annotation to your panel. As a pre-requisite, make sure that you already 
have a panel created into your dashboard and I’ve   also configured a data source as part of this 
demo. In this case, I’ll be using Prometheus. Now, let’s get started! So here, I have a panel called Traffic that 
visualizes the incoming traffic from this   demo application called Grafana News. Let’s say 
that I want to create an alert rule, and while   we have a notification policy in place that sends 
out a notification to your chosen contact point,   what if you also want to visualize these 
alerts as annotations to your dashboards? The good news is this can easily 
be configured with Grafana. To set this up, I’m going to click the 
Grafana menu icon here, navigate to alerting,   and then let’s just go ahead and click alert 
rules. Now, let’s create a new alert rule,   and I’m going to give my alert rule a name 
of, let’s say, “traffic-alert.” I’m going to   choose Prometheus as my data source, and 
I’m going to add my sample PromQL query. Now, let’s scroll down, and then under rule type, 
make sure that this is set as Grafana-managed. Then, under the expressions section, we have 
our reduce and our threshold expressions. The   reduce expression here basically just 
returns the last value of our query,   while the threshold expression checks if 
the value that’s returned by this reduce   expression is above a certain threshold. Now, 
for this demo, I’m going to use a very small   threshold so that it’s easy to test. 
So, let’s say I want to set it to 0.1. You can also quickly preview these expressions 
by clicking the preview button. Now since one   of the results is above 0.1, then you can see 
that the alert rule state is set to firing. So now, I’m going to just provide a folder 
where the alert rule will be stored. So,   I’m going to check if I have any. I don’t have 
any folders so I’m just going to create a new   one. I’ll just call that test folder, and I’m 
also going to create an evaluation group. Now,   I don’t have any evaluation group set at the 
moment, so again, let’s add a new group and I’m   going to set my evaluation interval to 10 seconds. 
Now, the evaluation interval is basically how   often the alert rule should be evaluated. I’ve 
set it to 10 seconds so that we can test this   change easily. I’ll also update the pending period 
to 0 because I want the alert to fire immediately. To link this alerting, let’s scroll 
down to the next section which is the   add annotation section. Now I’m going to 
just click the link dashboard and panel,   and then select the panel that I 
want this alert rule to be linked to. So let’s go ahead and confirm that and 
let’s go ahead and save rule and exit. Now, if I navigate back to my dashboard 
here, so let’s click Grafana News. I can   see that there is a red, broken heart 
icon beside the panel title. Now,   this signifies that the alert rule was 
triggered because the alert condition was met,   and I can also see this red annotation here, which 
is visualized as this red vertical dotted line,   and if I hover over the line, I 
can see a description of my alert. And there you have it! In this quick tutorial,   I’ve shown you how you can add Grafana 
alerts to your dashboards. Let us know   in the comments down below if you found this 
video useful, and as always, happy visualizing!

