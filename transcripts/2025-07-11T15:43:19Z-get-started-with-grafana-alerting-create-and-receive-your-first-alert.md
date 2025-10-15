# Get started with Grafana Alerting: Create and receive your first alert

Published on 2025-07-11T15:43:19Z

## Description

In this tutorial, we walk you through the process of setting up your first alert in just a few minutes. Don't miss the rest of the "Get ...

URL: https://www.youtube.com/watch?v=YVhKNbQNNss

## Summary

In this tutorial, Antonio, a developer advocate at Grafana Labs, provides a comprehensive walkthrough on creating alert rules and setting up notifications in Grafana. He explains various options for following along, including using a Grafana Cloud account, an interactive learning environment, or running Grafana locally via Docker. The video covers the concept of contact points—integrations that send notifications to destinations like email or Slack—before demonstrating how to create a contact point using a web hook. Antonio then guides viewers through the steps to set up a Grafana-managed alert rule, detailing how to configure alert conditions, evaluation intervals, and notification settings. He emphasizes the importance of these features in monitoring data and receiving timely alerts. The tutorial concludes with a promise of future content focused on alert instance routing.

# Getting Started with Grafana Alerting

Hi everyone, I'm Antonio, a developer advocate here at Grafana Labs. Welcome to this tutorial, which is the first part of the "Get Started with Grafana Alerting" series. In this walkthrough, I will show you how to create alert rules and set up notifications to stay on top of important events in your data.

## Options to Follow Along

Before we begin, there are various ways you can follow along with this tutorial. I will be using my own Grafana Cloud account, but if you do not have an account yet or prefer to run it yourself, you have two other options:

1. **Interactive Learning Environment**: Try out this example in our interactive learning environment, where you have a fully configured Grafana instance.
2. **Run Grafana Locally**: You can run a Grafana stack locally. There are many platforms on which you can run Grafana, such as:
   - Downloaded binary
   - Package manager
   - Kubernetes
   - Docker

If you opt for running Grafana locally, you can find the steps to run it on Docker.

Regardless of your choice, once you have logged into Grafana, let's get started.

## Creating a Contact Point

The first step is to create a contact point. But before we do so, let me quickly explain what a contact point is and what you can do with it. 

**Contact points** are integrations that send notifications to specific destinations, such as email, webhooks, or services like Slack, PagerDuty, or Grafana on Call. Besides the built-in integration options, we can also customize how the message will look by using templates or configure Grafana to send alert notifications to certain contact points using notification policies, which we cover in a linked tutorial below.

### Steps to Create a Contact Point

1. In the Grafana sidebar, navigate to **Alerts** and **IRM**.
2. Click on **Contact Points**.
3. Click **Create Contact Point**.
4. In the **Name** field, write "web hook".
5. In **Integration**, choose "web hook" or any other integration of your choice.
6. In another tab, go to [webhook.site](https://webhook.site) to obtain a public webhook URL, which will allow us to test that the notifications are sent correctly.
7. Copy the webhook URL and navigate back to Grafana.
8. In the **URL** field, paste the endpoint.
9. Click **Test** and then click **Send Test Notification**.
10. Navigate back to webhook.site, and you should see the test notification.
11. Return to Grafana and click **Save Contact Point**.

Great! We have our contact point ready. 

## Setting Up an Alert Rule

Now that we have our contact point, we can move on to setting up an alert rule. 

### Overview of Alert Rules

In Grafana, you can create Grafana-managed and data source-managed alert rules. Grafana-managed alert rules can query data from multiple data sources in a single alert rule. They are flexible as you can add expressions to transform your data, set all rule conditions, and add templates.

### Creating a Grafana Managed Alert Rule

Let's go ahead and create a Grafana-managed alert rule. This alert rule will allow us to define when and how alerts should trigger based on our data. We will use the test data source included in Grafana to create random time series data and create an alert rule that always fires, so we can see exactly how notifications are sent and received.

1. Navigate to **Alerts** and **IRM** -> **Alert Rules**.
2. Click on **New Alert Rule**.
3. Enter a name for the alert rule. Make it short and descriptive, as this will appear in your alert notifications (e.g., "Database Metrics").
4. Define the query and alert condition:
   - Select the **test data source** from the drop-down menu.
   - In the alert condition section, keep "When query is above zero," which displays the last value of aggregated time series values, with zero as the threshold value.
5. Click **Preview Alert Rule Condition** to run the query. It should return random time series data, and the alert rule state should be firing.

### Adding Folders and Labels

Next, we add folders and labels:
1. In the **Folder** section, click **New Folder** and enter a name (e.g., "Metric Alerts"). This folder will contain our alerts.
  
### Setting the Evaluation Behavior

The alert rule evaluation defines the conditions under which an alert rule triggers:
1. Click **New Evaluation Group**.
2. Name it "One Minute Evaluation."
3. Choose an evaluation interval (e.g., every one minute).
4. Set the **Pending Period** to zero seconds, so the alert rule fires the moment the condition is met.
5. **Firing For** defines how long an alert should remain in the firing state after the condition stops being true. Set this to zero to avoid additional notifications when alerts quickly switch between firing and resolved due to noisy or unstable metrics.

### Configuring Notifications

Finally, in the **Configure Notification** section, choose the contact point where you want to receive your alert notifications:
1. Under **Contact Point**, select "web hook" from the drop-down menu.
2. Click **Save Rule** and **Exit**.

## Conclusion

Now that our alert is configured, we are ready to see it in action. Grafana will automatically evaluate the alert rule based on the conditions we set, and once the rule fires, we will receive a notification. 

The alert notification details will show that the alert rule state is firing and will include the value that made the rule trigger by exceeding the threshold. The notification will also include links to see the alert rule details and add a silence to it. 

This is how the exact same notification will look if you use Slack or email as the contact point.

And that’s it for this tutorial! You have successfully set up an alert rule and received notifications. In the next tutorial, I will show you how to leverage alert instances for routing. Just follow the link at the bottom of the tutorial, or if you're watching on YouTube, you can also find the link to that and the rest of the tutorials in the description.

Thanks for following along, and see you in the next tutorial!

## Raw YouTube Transcript

Hi everyone, I'm Antonio, a developer advocate here at Grafana Labs. Welcome to this tutorial. This is the first part of the get started with Grafana alerting tutorials. In this walkthrough, I will show you how to create alert rules and set up notifications to stay on top of important events in your data. All right, before you begin, there are various ways you can follow along with this tutorial. I will use my own Graphan Cloud account, but if you do not have an account yet or prefer to run it yourself, you have two other options. The first option is to try out this example in our interactive learning environment where you have a fully configured graphana instance. One last option is to run a graphana stack locally. There are many platforms on which you can run graphana such as a downloaded binary, a package manager, Kubernetes or Docker. If you opt for this option, you can find the steps to run it on Docker. Regardless of your choice and once you have logged to Grafana, let's get started. The first step is to create a contact point. But before we do so, allow me to quickly explain what a contact point is and what you can do with it. Contact points are integrations that send notifications to specific destinations such as email, web hooks, or services like Slack, Pager Duty, or Graphana on Call. Besides the built-in integration options, we can also customize how the message will look like by using templates or even configure Graphana to send alert notifications to certain contact points by using notification policies which we cover in a tutorial link below. Okay, let's create a contact point. We begin with this step before creating the alert rule so that we have a contact point ready to link to the alert rule that we will create later. In graphana sidebar, navigate to alerts and IRM. Then click contact points. Click create contact point. In name, write web hook. In integration, choose web hook or any other integration of your choice. In another tab, go to web hook.site where you will obtain a public web hook URL. This will allow us to test that the notifications are sent correctly. Copy the web hook URL and navigate back to graphana. In URL, paste the endpoint. Click test and then click send test notification. Navigate back to web hook.side and you should see the test notification. Return to graphana and click save contact point. Great. We have our contact point. With our contact point ready, we can now move on to setting up an alert rule. But before we do that, allow me to quickly explain that in graphana you can create graphana managed and data source manage other rules. Graphana manage other rules can query data from multiple data sources in a single other rule. They are flexible as you can add expressions to transform your data, set all rule conditions and add templates. That said, let's go ahead and create a graphana manage alert rule. This alert rule will allow us to define when and how alert rules should trigger based on our data. We will use test data source which is included in graphana to create random time series data to create an alert rule that always fires so we can see exactly how notifications are sent and received. Let's configure the alert rule in Grafana. Navigate to alerts and IRM alert rules. Click on new alert rule. Enter a name for the alert rule. Make it short and descriptive as this appears in your alert notifications. For instance, database matrix. Next, let's define the query and alert condition. In this section, we use the default options for graphana manage alert rule creation. Select the test data data source from the drop-down menu. In the alert condition section, keep when query is above zero, which displays the last value of aggregated time series values and zero as a threshold value. This is the value above which the alert rule should trigger. Click preview alert rule condition to run the query. It should return random time series data and the alert rule state should be firing. Next, we add folders and labels. In folder, click new folder and enter a name. For example, metric alerts. This folder contains our alerts. Next, set the evaluation behavior. The alert rule evaluation defines the conditions under which an alert rule triggers. Click new evaluation group. Name it one minute evaluation. Choose an evaluation interval. This is how often alert rules are evaluated. For example, every one minute. Set the pending period to zero seconds. So, the alert rule fires the moment the condition is met. Keep firing for defines how long an alert should remain in the firing state after the alert condition stops being true. This is to avoid additional notifications when alerts quickly switch between firing and resolve due to noisy or unstable metrics. So we will set it to zero. Finally, in the configure notification section, choose the contact point where you want to receive your alert notifications. Under contact point, select web hook from the drop-own menu. Click save rule and exit. Now that our alert is configured, we are ready to see it in action. Graphana will automatically evaluate the alert rule based on the conditions we set. And once the rule fires, we will receive a notification. The alert notification details show that the alert rule state is firing and it includes the value that made the rule trigger by exceeding the threshold of the alert rule condition. The notification also include links to see the alert rule details and another link to add a silence to it. And this is how the exact same notification will look like if you instead use Slack or email as the contact point. And that's it for this tutorial. You have set up an alert rule and receive notifications. In the next tutorial, I will show you how you can leverage alert instances for routing. Just follow the link at the bottom of the tutorial or if you're watching on YouTube, you can also find the link to that and the rest of the tutorials in the description. Thanks for following along and see you in the next tutorial.

