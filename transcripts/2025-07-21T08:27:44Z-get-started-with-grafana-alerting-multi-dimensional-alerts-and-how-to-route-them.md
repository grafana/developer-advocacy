# Get started with Grafana Alerting: Multi-dimensional alerts and how to route them

Published on 2025-07-21T08:27:44Z

## Description

In this tutorial, we dig into more complex yet equally fundamental elements of Grafana Alerting: alert instances and notification ...

URL: https://www.youtube.com/watch?v=nI-_MEnFBQs

## Summary

In this video, the presenter discusses how to route alerts to specific contact points based on labels from queries in time series data, specifically using Grafana with data sources like Prometheus or Open Telemetry. The video illustrates the concept through an alert rule tracking page views on a website, demonstrating how different labels (e.g., device types like desktop or mobile) can trigger alerts routed to the appropriate teams. The presenter walks through setting up notification policies and creating alert rules to ensure that alerts are sent to the correct contacts based on the conditions defined. The video includes practical examples and encourages viewers to follow along using Grafana Cloud or local setups. The main focus is on alert instance management and routing logic to improve notification efficiency.

Did you know you can route alerts to specific contact points based on the labels returned by your query? When you're querying time series data, say from a system like Prometheus or OpenTelemetry, you're not just getting metrics like CPU or memory usage. You're also getting labels—key-value pairs that describe the context of that data. These labels can tell you things like which instance the data came from.

Imagine this: if you want mobile-related alerts to go to the mobile team and desktop-related ones to the front-end team, you can make that happen automatically with labels. Sounds useful? Stick around, and I will show you how to set it up.

### Understanding Alert Instances

Before we dive in, let's take a moment to understand what alert instances are. We start with an alert rule. This rule runs a query against our data source, tracking page views on a website. The query returns something called time series data. This just means a stream of values over time, often grouped by labels.

In this example, we are getting two time series back: one for desktop page views and one for mobile page views. Each of these includes a label, like `device: desktop` or `device: mobile`, and each represents a different slice of the data. 

Now, Grafana evaluates each time series individually against the condition we set in our alert rule. Here, the condition is: *Is the number of views above 1,000?* For desktop, we get 1,200 views. That's above the threshold, so this time series triggers an alert instance. For mobile, we get 900 views, which stays below the threshold, so it does not fire an alert. 

Finally, that notification is routed to a contact point like email, Slack, or a webhook. To recap, one alert rule can create multiple alert instances, and only the ones that meet the condition will notify the right people.

### Setting Up Notification Policies

Before we create our alert rule, we are going to set up notification policies. This way, when we do create the alert later, we will already have the routing logic in place, allowing us to preview exactly where each alert instance will go based on its labels.

I'm logged into Grafana Cloud, but if you're using the interactive learning environment or running Grafana locally, just head to `localhost:3000`. From the sidebar, go to **Alerting and IRM**, then **Alerting**, and click on **Notification Policies**.

Here, we will start by creating a child policy under the default one. Go ahead and click **New Child Policy**. For this first policy, we are going to route alerts where the device is desktop. In the label field, type `device`, and in the value field, type `desktop`. Then, in the contact point dropdown, choose **Webhook**. 

One more thing before saving: turn on **Continue matching subsequent sibling nodes**. This allows Grafana to continue checking even after it finds a match. That's it for the first policy! Now alerts with the label `device: desktop` will be routed to our webhook contact point.

Let's do the same for mobile. Click **New Child Policy** again, enter `device` as the label and `mobile` as the value, and select the webhook contact point again, or try a different integration if you would like to experiment. 

We are all set to route alerts for each device type separately. Now, when we create our alert rule, these label matchers will come into play.

### Creating an Alert Rule

Now, let's create an alert rule that returns multiple alert instances, each with different labels that match the policies we just set up. Go to **Alerting**, then **Alert Rules**, and click **New Alert Rule**. Give it a name; I will call mine *Web Traffic*. 

For the query, select the test data data source. Under a scenario, choose **CSV content** and paste in the following code snippet. This simulates web traffic where desktop exceeds our threshold and mobile doesn't. 

Now let's set the condition. Under **When**, keep **Last** set to *is above 1,000*. Click **Preview Alert Rule Condition**. You will see two series: `device: desktop` is in the firing state, and `device: mobile` is in the normal state. Only the desktop alert will send a notification for now.

Let's finish setting up the alert rule. Under **Folder**, create one called *Web Traffic Alerts*. For **Evaluation Group**, type *1 minute evaluation*. Set the interval to *1 minute*, and both **Pending** and **Keep firing** to *0 seconds*. 

Now, open **Advanced Options** and click **Preview Routing**. You will see that Grafana matches each alert instance to the notification policy based on its label. `Device: desktop` goes to the desktop policy, and `device: mobile` goes to the mobile one, but only the firing instance (desktop) will actually trigger a notification.

Click **Save Rule** to finish. Once the alert fires, you will receive a notification at your webhook endpoint. The payload includes the label `device: desktop`, showing that the notification was routed correctly using the policy we defined earlier.

Want to test mobile instead? Just change the CSV data so mobile crosses the 1,000 threshold.

### Conclusion

And that's it for this part! You learned how notification policies can route individual alert instances using the labels generated by your data and how Grafana automatically maps those to the correct contact points. 

Up next, we will show you how to group alerts together to reduce noise and keep things tidy. See you there!

## Raw YouTube Transcript

Did you know you can route 
alerts to specific contact points based on the labels returned by your query? When you're querying time series data, say from a system like 
Prometheus or Open Telemetry, you're not just getting metrics like CPU or 
memory usage. You're also getting labels, key value pairs that describe 
the context of that data. These labels can tell you things like 
which instance the data came from. Imagine this. If you want mobile 
related alerts to go to the mobile team, and desktop related ones to 
the front end team with labels, you can make that happen automatically. Sounds useful?
Stick around and I will show you how to set it up. All right, before we dive in, let's take a 
moment to understand what alert instances are. We start with an alert rule. This rule runs a query against our data source. It's tracking page views on a website. The query returns something 
called time series data. That just means a stream of values 
over time, often grouped by labels. In this example, we are 
getting two time series back. One for desktop page views 
and one for mobile page views. Each of these includes a label like 
device desktop or device mobile. And each one represents a 
different slice of the data. Now, Grafana evaluates each 
time series individually against the condition we set in our alert rule. Here, the condition is, is the 
number of views above 1,000? For desktop, we get 1,200 views. That's above the threshold. So, this 
time series triggers an alert instance. For mobile, we get 900 views. That stays below the threshold. 
So, it does not fire an alert. Finally, that notification is routed to a contact 
point like an email, Slack, or a web hook. So, to recap,
one alert rule can create multiple alert instances and only the ones that meet the 
condition move forward to notify the right people. Before we get started, here are a few 
different ways you can follow along. I'll be using my own Grafana Cloud account, but you can also use our 
interactive learning environment. It runs right in your browser and it's 
already set up with everything you need. If you prefer to run Grafana 
locally, that works too. You can use Docker, Kubernetes, or 
just run it as a binary on your system. Whichever setup you're using, once you're 
logged to Grafana, you're good to go. Before we create our alert rule, we are 
going to set up notification policies. This way when we do create the alert later, we 
will already have the routing logic in place. So we can preview exactly where each alert 
instance will go based on its labels. I'm logged into Grafana Cloud,
but if you're using the interactive learning environment or running Grafana 
locally, just head to localhost:3000. From the sidebar, go to alert and IRM, then 
alerting, and click on notification policies. Here we will start by creating a 
child policy under the default one. So go ahead and click new child policy. For this first policy, we are going to 
route alerts where the device is desktop. In the label field, type device and 
in the value field, type desktop. Then in the contact point dropdown, choose 
web hook. One more thing before saving, turn on continue matching 
subsequent sibling nodes. This allows Grafana to continue 
checking even after it finds a match. And that's it for the first policy. Now alerts with the label device desktop 
will be routed to our web hook contact point. Let's do the same for mobile. Just click mutual policy again. Enter 
device as the label and mobile as the value and select the web hook contact point 
again or try a different integration if you would like to experiment with 
these two child policies in place. We are all set to route alerts for 
each device type separately. Now when we create our alert rule these 
label matchers will come into play. Okay. Now, let's create an alert rule 
that returns multiple alert instances, each with different labels that 
match the policies we just set up. Go to alerting, then alert 
rules, and click new alert rule. Give it a name. I will call mine web traffic. For the query, select the test data data source. Under a scenario, choose CSV content 
and paste in the following code snippet. This simulates web traffic where desktop 
exceeds our threshold and mobile doesn't. Now let's set the condition. Under when keep 
last set the threshold to is above 1,000. Click preview alert rule condition. You will see two series device desktop is in 
firing state and device mobile is in normal state. Only the desktop alert will 
send a notification for now. Okay, let's finish setting up 
the alert rule. Under folder, create one called web traffic alerts. For evaluation group, type 1 minute evaluation. Set interval to 1 minute and both 
Pending and Keep firing to 0 seconds. Now open advanced options 
and click preview routing. You will see that Grafana matches each alert instance to the notification 
policy based on its label. Device desktop goes to the desktop policy, and the device mobile goes to the mobile one, but only the firing instance desktop 
will actually trigger a notification. Click save rule to finish. Once the alert fires, you will receive a 
notification at your web hook endpoint. The payload includes the label 
device desktop showing that the notification was routed correctly 
using the policy we defined earlier. Want to test mobile instead?
Just change the CSV data. So, mobile crosses the 1000 threshold. And that's it for this part. You learn how notification policies can route individual alert instances using 
the labels generated by your data and how Grafana automatically maps 
those to the correct contact points. Up next, we will show you 
how to group alerts together to reduce noise and keep things tidy. See you there!

