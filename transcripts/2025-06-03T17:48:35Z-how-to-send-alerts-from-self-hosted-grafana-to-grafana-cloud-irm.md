# How to send alerts from self-hosted Grafana to Grafana Cloud IRM

Published on 2025-06-03T17:48:35Z

## Description

Learn how to send alerts from Grafana OSS or Grafana Enterprise to Grafana Cloud IRM. In this quick demo, we'll show you how ...

URL: https://www.youtube.com/watch?v=SgaiMlFeSQY

## Summary

In this video, Pepe, a developer advocate at Grafana, provides a quick demonstration on how to send specific alerts from a local Grafana instance to the Incident Response Management (IRM) system on Grafana Cloud. He walks viewers through the steps of setting up the integration, including configuring the integration in Grafana Cloud, creating a contact point in the local Grafana, and testing the notification. Pepe highlights the importance of choosing which alerts to forward to IRM and mentions that viewers can find more detailed information in linked resources for a comprehensive IRM demo.

# Sending Alerts from Grafana to IRM

Hi everyone, I am Pepe, a developer advocate at Grafana. In this quick demo, I'll show you how to send specific alerts from a local Grafana instance to IRM on Grafana Cloud.

**Step 1: Set Up Integration in Grafana Cloud IRM**

1. In Grafana Cloud IRM, go to the **Integration** tab.
2. Click on **Add Integration**.
3. Choose the type **Alert Manager**.
4. Give it a name and, optionally, assign it to a team.
5. You may want to choose an **escalation chain** to handle all the alerts coming to this integration.
6. Finally, on this page, copy the **RE endpoint** for this integration.

**Step 2: Configure Contact Point in Local Grafana**

Now, switch over to your local Grafana:

1. Go to **Contact Points** in **Alerting**.
2. Click on **Create Contact Point**.
3. Give it a name.
4. Select the type **Webhook** and enter the URL of the IRM integration.

**Step 3: Test the Integration**

Now let's test the integration quickly:

1. Click on **Send Test Notification**.
2. Don't forget to set the contact point.

**Step 4: Verify in IRM**

Now back in IRM, you will find an incoming alert group. You can click to view the details. From here, you can:

- Acknowledge
- Resolve
- Take additional actions

On the timeline, we can see how this alert group was handled by the escalation chain. I already received a phone call and an email.

And that's all for this quick demo! 

The next step is for you to decide which alerts you want to forward to IRM—whether all of them or only some of them. 

If you want to see a full IRM demo, check out our **Getting Started** video linked in the description below.

## Raw YouTube Transcript

Hi everyone, I am Pepe, developer advocate at Graphana. In this quick demo, I'll show you how to send a specific alerts from a local Graphana instance to IRM on Graphana Cloud. First, in Grafana Cloud IRM, go to the integration tab. Add integration. Choose the type alert manager. Give it a name and optionally assign to a team. Then you may want to choose an escalation chain to handle all the alerts coming to this integration. And finally on this page, copy the re end point for this integration. Now switch over to your local graphana. Go to contact points in alerting. Create contact point. Give it a name. Select the type web hook and enter the URL of the IRM integration. Now let's test the integration quickly. Click send test notification and don't forget to set the contact point. Now back in IRM we find an incoming alert group. We can click to view the details. From here we can acknowledge resolve or take additional actions. On the timeline we can see how this other group was handled by the escalation chain. I already received a phone call and email. And that's all for this quick demo. The next step is for you to decide which alerts you want to forward to IRM. All or only some of them. And finally, if you want to see a full RM demo, check out our getting started video links in the description below.

