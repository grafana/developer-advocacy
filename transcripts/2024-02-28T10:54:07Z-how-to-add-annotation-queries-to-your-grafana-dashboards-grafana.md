# How to Add Annotation Queries to Your Grafana Dashboards | Grafana

Did you know you can add queries from any data source and add them as annotations to your dashboards? Join Senior ...

Published on 2024-02-28T10:54:07Z

URL: https://www.youtube.com/watch?v=2istdJpPj2Y

Transcript: Hi! My name is Marie Cruz, and I’m a 
Senior Developer Advocate at Grafana   Labs. In this video, I’ll quickly show 
you how you create annotations from your   data source and display them on your dashboards. By the end of this tutorial, you should 
have an annotation query added into your   panel that can be visualized as 
markers across your dashboard. As a pre-requisite, make sure that you already 
have a panel added into your dashboard,   and it would be best if you have some 
data sources configured. For this demo,   I have configured Loki and 
Prometheus for my data sources. Now, let’s get started! So here I have a panel called “Traffic” 
that visualizes the incoming traffic from   this demo application called Grafana News. So, 
Grafana News basically just lets you post links,   and then you can vote for the ones that you like. Now, a user can actually add a new 
entry without providing any URL,   and this can trigger this empty 
URL error in the application. So,   what if I want to visualize this error 
as an annotation to my dashboard? The good news is this can easily be configured 
with Grafana using annotation queries. To set this up, let’s click Dashboard 
settings and we’ll go to Annotations.   Once you’re in this view, click 
the add annotation query button. Let’s give a name for our annotation query. So,   I’m going to call mine “Errors,” and I’m going to 
select the data source for the annotation query,   which for my example, my logs are stored 
in Loki, so I’m going to select Loki. Now, make sure that the Enabled 
checkbox is ticked as well because   this will enable the annotation query 
to be issued on every dashboard refresh. So now you can choose which panel 
you would like the annotation query   to be added. For this example, I’m 
going to select the Traffic panel. Next, I’m going to provide the query 
for displaying the error logs. Now,   this query will look different depending 
on your use case, but for this example,   I’m going to check that the tns app log 
file name consists of the string error. Now, let’s go ahead and save 
the changes to our dashboard. Now, when you navigate back to your 
dashboard, you should now see a toggle   button for the annotation query, 
and it’s set to enabled by default. To test the changes, I’m going to go 
back to the Grafana News application   and I’m going to add a new entry without any link. Now, if I go back to my dashboard, I should now 
see an annotation here, which is visualized as a   red vertical line, and if I hover over the line, 
I can see the error message coming from my logs. And there you have it! In this quick tutorial,   I’ve shown you how you can add an annotation 
query to your Grafana dashboards. Let us know   in the comments section below if you found 
this tutorial useful, and happy visualizing!

