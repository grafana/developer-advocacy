# Get started with Grafana Alerting: Template your alert notifications

Published on 2025-09-01T18:21:04Z

## Description

In this tutorial you will learn how to template your alerts. https://grafana.com/tutorials/alerting-get-started-pt4/ Don't miss the rest ...

URL: https://www.youtube.com/watch?v=9CSrQGKeZwQ

## Summary

In this tutorial video, the presenter explains how to customize alert notifications in Grafana using templating techniques. The video covers two main methods: templating alert rule annotations and labels, and templating notifications. The presenter emphasizes the difference between these two approaches, likening alert annotations to the content of a letter and notification templates to the design of the envelope. Key concepts discussed include creating alert rules, using alert manager to route notifications, and setting up notification templates for better organization and readability. The session concludes with a demonstration of configuring these templates in Grafana and a teaser for the next tutorial, which will cover routing alerts based on dynamically generated labels.

# Customizing Alert Notifications in Grafana

Do you want to customize your alert notifications so they look the way you want? In this guide, I will show you how to customize, format, and reuse alert notification messages in Grafana. 

## Templating Your Alerts

There are two ways to template your alerts in Grafana:

1. **Templating the Alert Rule Annotations and Labels**
2. **Templating Notifications**

### What's the Difference?

If you template inside an alert rule, you can use Go templating in the labels and annotations. This means you can customize what each alert instance looks like, for example, by adding the instance name, the metric value, or other useful context.

*By the way, if this is your first time creating an alert rule or if you're hearing about alert instances for the first time, I recommend checking out some of the previous tutorials.*

On the other hand, if you are using notification templates, you are not templating the alert rule itself but the message that Alert Manager or Grafana alerting sends out. These templates can be shared across contact points, so you don’t have to rewrite the same format every time. They also allow you to control not just the annotations but also the title and the full body of the notification, giving you much more flexibility in how your messages are structured.

Think of it like this:
- **Templating labels and annotations** is like writing a note on the inside of a letter; it's part of the alert itself.
- **Notification templates**, on the other hand, are like designing the envelope and deciding how the letter is presented when it gets delivered. 

We can say it’s a design reference for all letters sent to a particular contact point. 

### Important Note

While both row templates (labels and annotations) and notification templates use the same templating language, the variables and functions available are different. This is one of the most common mistakes beginners make. So, if you reuse an example or write your own templates, always make sure you are checking the right reference section of the documentation for labels and annotations or for notification templates. We have examples for both.

## How Templating Works in Grafana Alerting

Let’s walk through how templating works. First, we start with the alert rule query. In this example, the query returns a value along with some labels like the instance and the job. 

Since the value crosses the threshold we define in the alert rule, the alert fires. At this point, we have what’s called an **alert instance**. The alert instance also generates a summary, which is where templating comes in. The summary text is defined in the alert rule using a template. In our case, the template says to show the instance label and its value, resulting in a summary that says “Server 80” as in 80% of usage.

Next, the alert instance is sent off to **Alert Manager**. Alert Manager is the component that takes care of what happens after an alert fires. It receives alerts and decides where those alerts should go, determining the right contact point—essentially, who should be notified. Finally, Alert Manager takes the contact point’s notification template, formats the actual message, and sends that notification out.

## Creating an Alert Rule

Now that we have seen how templating works, let’s build on that by creating an alert rule with annotations that we will later use in our notification template. You can follow along in Grafana Cloud, in the interactive environment, or with Grafana OSS locally.

1. Log into Grafana and navigate to **Alerts > Alerting > Alert Rules**.
2. Click **New Alert Rule** and give it a name. 
3. In the query section, use the test data source with a CSV scenario that simulates multiple time series, each generating a separate alert instance.
4. For the alert condition, skip the last reducer function and set the threshold to "is above 75." Then, preview the condition to see some series firing and some normal.
5. Organize the rule into a folder. While it's possible to template labels here, in this tutorial, we focus on templating the summary and annotations fields instead.
6. Set the evaluation group and interval. Choose a one-minute interval and keep the "Pending period" and "Keep firing for" times at zero so the alert triggers and resolves quickly for the demo.
7. In the notifications section, pick a contact point or create one if needed.

Finally, let’s create a summary annotation template. This template inserts the instance name from labels and its CPU usage from values, with tabs and line breaks for readability. Here is how it looks in a notification. You can also add a description to give on-call engineers more context about what this alert means. Click **Save Rule**, and we’re done.

## Customizing Alert Notifications

Now that we have configured an alert rule with a template for the summary annotation, the next thing we will learn is how to customize the alert notifications themselves. While the default notification message includes the summary annotations and works well, we can do much more than that. We can change the entire message and tailor it to our needs.

We will use a built-in notification template that references the summary annotation we just set up. If you want to dive deeper, you will find more examples in the documentation.

1. Go to **Alerts > Alerting > Contact Points** and open the **Notification Templates** tab.
2. Click **Add Notification Template Group** and give it a name.
3. Choose **Print Firing and Resolve Alerts** from the examples menu. This template organizes alerts into two sections: firing and resolved. Each section includes only the key details plus the summary and description annotations we set up earlier.

At the top, the custom firing and resolve alerts block prints the number of resolved alerts, then loops through each one and applies the alert summary and description sub-template. It does the same for firing alerts, listing how many there are and their details. The alert summary and description section controls the formatting for each alert, pulling in three key fields: the summary annotation, the alert's status, and the description annotation.

In the preview area, you can see a sample of how the notification will look. Since we have already created our alert rule, you can preview how an actual alert instance from your rule will appear in the notification. 

Click **Edit Payload**, then click **Use Existing Alert Instance**. You should see our alert rule listed on the left. Click the alert rule, select an instance, and then click **Add Alert Data to Payload**. Notice the alert instance is added to the bottom of the preview. Click **Save**, and our template is ready.

## Applying the Template

Next, we will apply it to a contact point to see it in action. 

1. In **Contact Points**, edit your contact point. 
2. Go to the **Optional Settings** section and click **Edit Message**.
3. Under **Select Notification Template**, search for our custom firing and resolve alerts template. 
4. Click **Save**, and finally save your contact point.

Now that the template has been applied to the contact point, you should receive notifications in the specified contact point. If you templated an email contact point, the notification template should look like this. If you chose Slack as your contact point, it should look like that.

You can see how the notification template groups the alert instances into two sections: firing alerts and resolved alerts. Each section includes only the key details for each alert.

## Conclusion

Great job! You have just learned how to configure alert rules with annotations and customize them using built-in notification templates. 

But we are not stopping here. In the next tutorial, we will take it a step further by routing alerts based on dynamically generated labels. This way, critical alerts go directly to the on-call team, while less urgent ones flow into a general monitoring channel. 

See you there!

## Raw YouTube Transcript

Do you want to customize your alert 
notifications so they look like the way you want? I'll show you how to customize, format, 
and reuse alert notification messages. There are two ways of templating 
your alerts in Grafana. Templating the alert rule annotations 
and labels, or templating notifications. So what's the difference? If you template inside an alert rule, you can 
use go templating in the labels and annotations. This means you can customize what 
each alert instance looks like. For example, adding the instance name, 
the metric value, or other useful context. By the way, if this is the first time 
you're creating another rule or you're hearing about alert instance, I will advise you 
to check out any of these previous tutorials. The other case is using notification templates. Here you're not templating 
the alert rule itself but the message that alert manager 
or Grafana alerting sends out. These templates can be shared across 
contact points so you don't have to rewrite the same format every time. 
Plus they let you control not just the annotations but also the title and 
the full body of the notification. This gives you much more flexibility 
in how your messages are structured. Think of it like this. Templating labels and annotations is like writing a note on the inside of a letter. 
It's part of the alert itself. Notification templates on the 
other hand are like designing the envelope and deciding how a letter 
is presented when it gets delivered. We can say it's a design of reference for all 
letters sent to a particular contact point. And one last important thing to 
note, while both row templates, labels and annotations and notification 
templates use the same templating language, the variables and functions 
available are different. This is one of the most 
common mistake beginners make. So if you are reusing an example or writing your 
own templates, always make sure you are checking the right reference section of the docs for labels 
and notations or for notification templates. We've got examples for both. Okay, let's walk through how 
templating works in Grafana alerting. First, we start with the alert rule query. In this example, the query returns a value along 
with some labels like the instance and the job. Now since the value crosses the threshold 
we define in the all rule the alert fires. At this point we have what's 
called an alert instance. The alert instance also generates a summary. And this is where templating comes in. The summary text is defined in 
the alert rule using a template. In our case the template says show 
me the instance label and its value. So the summary ends up saying 
server 80 as in 80% of usage. Next, the alert instance is sent off 
to alert manager. Alert manager is the component that takes care of 
what happens after an alert fires. It receives alerts and then decides where 
those alerts should go. In other words, is responsible for figuring out the right 
contact point. Basically, who should be notified. Finally, alert manager takes the 
contact points notification template, uses it to format the actual message 
and sends that notification out. Now that we have seen how templating 
works, let's build on that by creating an other rule with annotations that we will 
later use in our notification template. You can follow along in Grafana cloud, in the interactive environment, 
or with Grafana OSS locally. Let's log into Grafana and head to 
alerts and IRM > Alerting Alert rules. Click new alert rule and give it a name. In the query section, I will use the test 
data data source with a CSV scenario that simulates multiple time series. Each one 
generating a separate alert instance. For the alert condition, skip last as the reducer function and set the threshold to is 
above 75. Then preview the condition. You will see some series firing and some normal. Next, we will organize the rule into a folder. By 
the way, while it's possible to template labels here, in this tutorial, we focus on templating 
the summary and annotations fields instead. Next, set the evaluation group and interval. Choose a one minute interval and 
keep the "Pending period" and "Keep firing for" times at zero so the alert 
triggers and resolve quickly for the demo. In the notifications section, pick a 
contact point or create one if needed. Finally, let's create a 
summary annotation template. This template inserts the instance 
name from labels and its CPU usage from values A with tabs and 
line brakes for readability. Here is how it looks in a notification. You can also add a description 
to give on-call engineers more context about what this alert means. Click save rule and we're done. Now that we have configured an alert rule 
with a template for the summary annotation, the next thing we will learn is customize 
the alert notification themselves. While the default notification message includes the summary annotations and works 
well, we can do much more than that. We can change the entire message 
and tailor it to our needs. We will use a built-in notification template that 
references the summary annotation we just set up. As mentioned before, in this step, we will 
use a built-in notification template to format our alerts. If you want to dive deeper, 
you will find more examples in the docs. Let's go to alerts and alerting contact points 
and open the notification templates tab. Click add notification template group. Give it a name. Then choose Print firing 
and resolve alerts from the examples menu. This template organize alerts into two 
sections, firing and result. Each section includes only the key details plus the summary 
and description annotations we set up earlier. At the top, the custom firing and resolve alerts 
block prints the number of resolved alerts, then loops through each one and applies the 
alert summary and description sub-template. Next, it does the same for filing alerts, 
listing how many there are and their details. The alert summary and description section controls the formatting for each alert. 
It pulls in three key fields. The summary annotation, the alerts 
status, and the description annotation. In the preview area, you can see a 
sample of how the notification will look. Since we have already created our alert 
rule, you can take it a step further by previewing how an actual alert instance from 
your rule will appear in the notification. Click edit payload, then click 
use existing alert instance. You should see our alert rule listed on the left. Click the alert rule. Select an instance and then click add alert data to payload. Notice the alert instance 
is added to the bottom of the preview. Click save and our template is ready. Next, we will apply it to a contact point to see it in action. In contact 
points, edit your contact point. Go to optional settings 
section. Click edit message. Under select notification template, search for 
our custom firing and resolve alerts template. Click save. Finally, save your contact point. Now that the template has been 
applied to the contact point, you should receive notifications 
in the specified contact point. If you templated an email contact point, the 
notification template should look like this. And this is how it should look like if 
you chose Slack as your contact point. You can see how the notification template 
groups the alert instances into two sections: firing alerts and resolved alerts. Each section 
includes only the key details for each alert. Great job! You have just learned 
how to configure other rules with annotations and customize them using 
built-in notification templates. But we are not stopping here. In the next tutorial, we 
will take it a step further, routing alerts based on 
dynamically generated labels. That way, critical alerts go 
directly to the UN call team, while less urgent ones flow into 
a general monitoring channel. See you there.

