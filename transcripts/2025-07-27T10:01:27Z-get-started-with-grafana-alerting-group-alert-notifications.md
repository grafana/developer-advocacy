# Get started with Grafana Alerting: Group alert notifications

Published on 2025-07-27T10:01:27Z

## Description

In this tutorial you will learn how alert rule grouping works. https://grafana.com/tutorials/alerting-get-started-pt3/ Don't miss the ...

URL: https://www.youtube.com/watch?v=WZ8gqKIQ5Oc

## Summary

In this tutorial, the presenter demonstrates how to effectively manage alert notifications in Grafana by utilizing alert grouping to reduce notification overload for teams, particularly for on-call engineers. The video covers the principles of alert grouping, explaining how related alerts can be combined into single notifications based on labels and timing options. Key concepts include reserved, user-defined, and query labels that help categorize alerts, as well as timing settings like group wait, group interval, and repeat interval to control notification frequency. The tutorial outlines a practical example where alerts from multiple regions are grouped for more streamlined communication, and provides step-by-step instructions on setting up alert rules and notification policies. The presenter emphasizes the benefits of this approach in enhancing response times while minimizing noise, and invites viewers to explore further customization options in future tutorials.

# Alert Grouping in Grafana: A Tutorial

Are you tired of getting flooded with alert notifications? In this tutorial, I'll show you how to group alerts together so your team can focus on solving problems, not sorting through thousands of messages.

## What You'll Learn

Hi there! Today you will learn how alert grouping works, and you will see what group notifications actually look like. If you're not sure what alert instances are, or if you haven't created any alerts yet, we covered that in previous tutorials. You will find links in this tutorial and in the video description.

## Understanding Alert Grouping

Let's take a closer look at how alert grouping works. When many alert rules trigger at the same time, you might receive a flood of notifications. This can be overwhelming, especially for on-call engineers. Grafana helps solve this with alert grouping. 

With grouping, related alerts are combined into one single notification. Instead of getting five messages about high CPU usage in the same region, you just get one clear message. This is done using labels and timing options in your notification policies.

### Labels

Labels tell Grafana how to group alerts. There are three types of labels:

- **Reserved labels**: Created automatically, like alert name.
- **User-defined labels**: You can add these when creating other rules, for example, severity or priority.
- **Query labels**: These come from the data source, such as service instance or region.

### Timing Options

Timing options help you control when and how often group notifications are sent:

- **Group wait**: How long Grafana waits before sending the first group notification.
- **Group interval**: How often Grafana sends updates for the same group.
- **Repeat interval**: How long to wait before sending a notification again, even if nothing has changed.

With grouping, alerts that share the same label value (for example, all alerts from a service, instance, or region) are bundled together and sent based on the timing settings.

## Real-World Scenario

Now that we understand the basics, let's see how this works in a real-world scenario. Imagine you're monitoring a distributed application across multiple regions, like US West and US East. You're keeping an eye on metrics like CPU usage, memory use, and network delays. 

If servers in both regions start using too much CPU, you don't want 10 different messages blowing up your phone. You want just one notification per region. Here’s how to fix that:

1. Use labels present in your alert rules like server instance or region.
2. In your notification policy, group alerts by the region label. This way, all alerts from US West go to the west coast team, while alerts from US East go to the east coast team.
3. Define how often you want to receive updates. For instance, a group interval of five or ten minutes means you will only get updates every 5 or 10 minutes for the same group.

This setup helps reduce noise and ensures the right teams are notified in a clear and organized way.

## Setting Up Alert Grouping in Grafana

To follow along with this tutorial, you have a few options:

- **Grafana Cloud**: No installation is needed. Just create a free account and log in.
- **Interactive environment**: Try the tutorial in our interactive environment where everything is already configured.
- **Grafana OSS locally**: Run Grafana OSS locally with Docker Compose.

### Steps to Set Up

1. **Log into your Grafana instance.**
2. Go to **Alerts > Alerting > Notification Policies**.
3. Add a child policy to handle alerts for a specific region. In the default policy, click **New Child Policy**.
4. Add a label matcher by entering `region` in the label field. Keep `equal` as the operator and enter `us-west` in the value.
5. Select a contact point like email, Slack, webhook, or any contact point of your choice.
6. Enable **Continue matching subsequent sibling notes** so other policies can also be evaluated if needed.
7. Turn on **Override grouping**. Set **Group by** to `region`. This helps combine similar alerts into one notification.
8. Lastly, turn on **Override timing options**. Set **Group interval** to 2 minutes. This ensures follow-up notifications for the same alert group will be sent at intervals of 2 minutes.

Repeat these steps for the US East region, but don't override the grouping or timing settings this time. This will help us compare the difference later.

## Creating Alert Rules

With our policies in place, we are ready to create our alert rules:

1. Go to **Alerts > Alerting > Alert Rules**.
2. Click **New Alert Rule**. Give your rule a name, for example, "High CPU Usage Multi-Region".
3. Define the query using test data. Use the Test Data data source and set the scenario to CSV content. Paste in the CSV data simulating CPU usage in different regions.
4. Configure the alert condition. Keep **Last** as the evaluation method and set the threshold to above 75.
5. Click **Preview Alert Rule Condition**. The returned data simulates a data source returning multiple time series, each leading to the creation of an alert instance for that specific time series.
6. Add a folder for the rule, like "Multi-Region Alerts".
7. Set an evaluation group. Name it "Multi-Region Group" and set the interval to 1 minute.
8. Set both **Pending period** and **Keep firing for** to 0 seconds to see the alert firing and being grouped immediately. (In a real-world setup, we recommend setting a nonzero value for **Keep firing for** to avoid unnecessary repeat notifications and reduce alert noise.)
9. Choose **Use notification policy** and click **Preview Routing** to check that the alert matches your policy.

Finally, click **Save Rule** and exit. Now, let's create a second rule for memory usage by duplicating the other rule and naming it "High Memory Usage Multi-Region". Replace the CSV content with the new data and preview the rule before saving.

## Viewing Alert Notifications

Now that we have set up our alert rules and notification policies, let's see what happens when the conditions are met. Grafana evaluates the alert every minute. When CPU or memory usage goes above 75%, it triggers an alert. 

Thanks to our grouping configuration, we won't get bombarded with individual alerts. Instead, we will receive one group notification per region based on the label region. 

For the US West region, we chose to override grouping and set a faster group interval of 2 minutes. For the US East region, we kept the default settings, so alerts will be sent every 5 minutes. This means the west coast team will get one group notification with both CPU and memory alerts every 2 minutes if the issue continues, while the east coast team will receive two separate notifications, one for CPU and one for memory, sent every 5 minutes.

With this setup, your team will receive fewer, clearer, and more focused alerts, leading to quicker response times with less noise.

## Conclusion

Nice work! You have just learned how to use alert grouping in Grafana to reduce notification noise and improve incident response. If you would like to take it a step further, check out the next part of the template, your alert notifications tutorial. There, you will learn how to customize the message content of alerts to make them even more useful.

Thanks for watching, and see you in the next video!

## Raw YouTube Transcript

Are you tired of getting flooded 
with alert notifications? In this tutorial, I'll show you how to group alerts together so your team 
can focus on solving problems, not sorting through thousands of messages. Hi there. Today you will learn how 
alert grouping works and then you will see what group notifications actually look like. If you're not sure what alert instances are 
or if you haven't created any alerts yet, we covered that in previous tutorials. You will find links in this tutorial 
and in the video description. Now, let's take a closer look 
at how alert grouping works. When many alert rules trigger at the same time,
you might receive a flood of notifications. This can be overwhelming, especially for on call engineers. Grafana helps 
solve this with alert grouping. With grouping, related alerts are 
combined into one single notification. Instead of getting five messages about 
high CPU usage in the same region, you just get one clear message. This is done using labels and timing 
options in your notification policies. Let's break it down. Labels tell Grafana how to group alerts. There are three types of labels. Reserved labels. These are created 
automatically like alert name. User-defined labels. You can add these when creating other rules for 
example severity or priority and query labels. These come from the data source 
such as service instance or region. Next are the timing options, which help you control when and how 
often group notifications are sent. Group wait, how long Grafana waits before 
sending the first group notification. Group interval, how often Grafana 
sends updates for the same group. And Repeat interval, how long to wait 
before sending a notification again, even if nothing has changed. With grouping, alerts that 
share the same label value, for example, all alerts from service, instance, or region are bundled together and 
sent based on the timing settings. And now that we understand the basics, let's see how this works in a real world scenario. Imagine this, you're monitoring 
a distributed application across multiple regions like US West and US East. You're keeping an eye on things like CPU 
usage, memory use, and network delays. Now, if servers in both regions 
start using too much CPU, you don't want 10 different 
messages blowing up your phone. You want just one notification per region. Here is how always fix that. Use labels present in your alert 
rules like server instance or region. In your notification policy, 
group alerts by the region label. So all alerts from US West 
go to the west coast team and alerts from US East go to the east coast team. Then define how often you want to receive updates. For example, a group interval of five 
or 10 minutes means you will only get updates every 5 or 10 minutes for the same group. This setup helps reduce noise and make sure the right teams are notified in 
a clear and organized way. To follow along with this 
tutorial, there are a few options. Grafana cloud, no installation is needed. Just create a free account and login. You can also try the tutorial 
in our interactive environment where everything is already configured, or run Grafana OSS locally with docker compose. Now let's walk through how to 
set up alert grouping in Grafana. Start by logging into your Grafana instance. Then go to alerts, alerting notification policies. We're going to add a child policy to 
handle alerts for a specific region. In the default policy, click new child policy. Add a label matcher by entering 
region in the label field. Keep equal as the operator 
and in value enter us-west. Select a contact point like email, slack, 
webhook or any contact point of your choice. Enable continue matching subsequent sibling notes 
so other policies can also be evaluated if needed. Next, turn on override grouping. Set group by to region. Group by helps combine similar 
alerts into one notification. For example, if several alerts come 
in with the label region US West, they will be grouped together. So instead of getting a separate 
notification for each one, you get just one. Lastly, turn on override timing options. We're 
going to set group interval to two minutes. This ensures follow-up notifications for the same alert group will be sent 
at intervals of 2 minutes. While the default is 5 minutes, we choose 2 minutes here to provide faster 
feedback for demonstration purposes. Good. Now, repeat these 
steps for the US East region, but don't override the grouping 
or timing settings this time. This will help us compare the difference later. With our policies in place, we're 
ready to create our alert rules. Let's now create other rules 
based on our monitoring example. Go to Alerts > Alerting > Alert rules. Click new alert rule. Give your rule a name. For example, 
high CPU usage multi-region. Now, let's define the query using test data. Use the Test data data source. Set the scenario 
to CSV content. Paste in this CSV data. This data simulates CPU 
usage in different regions. Now configure the alert condition. Keep last as the valuation method 
and set the threshold to above 75. Click preview alert rule condition. The return data simulates a data 
source returning multiple time series each leading to the creation of an alert 
instance for that specific time series. Then let's add a folder for the 
rule like multi-region alerts. Set an evaluation group. Name it multi-region group and 
set the interval to 1 minute. Set both pending period and keep firing for to 0 seconds. So you can immediately see 
the alert firing and being grouped. However, in a real world setup, we 
recommend setting a nonzero value for keep firing for to avoid unnecessary 
repeat notifications and reduce alert noise. Finally, choose use notification policy and click preview routing to check that 
the alert matches your policy. The preview should show that the region label 
from our data source is successfully matching the notification policies that we created earlier 
thanks to the label matcher that we configured. Click save rule and exit. Now let's create a second rule for memory usage. Duplicate the other rule. Name it high memory usage multi-region. Replace the CSV content with the following data. Again, preview the rule and save. With both rules in place, let's now 
take a look at the alert notifications. Now that we have set up our alert 
rules and notification policies, let's see what happens when 
the conditions are met. Grafana evaluates the alert every minute. When CPU or memory usage goes 
above 75%, it triggers an alert. Thanks to our grouping configuration, we 
won't get bombarded with individual alerts. Instead, we will receive one group notification 
per region based on the label region. So, for the US West region, we chose to override grouping and set 
a faster group interval of 2 minutes. For the US East region, we kept the default 
settings, so alerts will be sent every 5 minutes. This means the west coast team will 
get one group notification with both CPU and memory alerts every 2 
minutes if the issue continues. The east coast team will receive 
two separate notifications, one for CPU and one for 
memory. Sent every 5 minutes. With this setup, your team receive 
fewer, clearer, and more focused alerts. And that means quicker 
response time with less noise. Nice work! You have just learned how to 
use alert grouping in Grafana to reduce notification noise and improve incident response. If you would like to take it a step further, check out the next part of the template, 
your alert notifications tutorial. There you will learn how to customize the message 
content of alerts to make them even more useful. Thanks for watching, and 
see you in the next video.

