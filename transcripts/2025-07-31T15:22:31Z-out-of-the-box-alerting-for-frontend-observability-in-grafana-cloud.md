# Out-of-the-box Alerting for Frontend Observability in Grafana Cloud

Published on 2025-07-31T15:22:31Z

## Description

Get alerted on frontend issues the moment they happen — no setup headaches required. In this short demo, Elliot Kirk from ...

URL: https://www.youtube.com/watch?v=8uacjks_ylg

## Summary

In this video, Elliot Kirk, an engineer on the front-end observability and Pharaoh team at Grafana, introduces a new feature for out-of-the-box alerting tailored for front-end observability. He explains how users can easily enable a set of alerts based on data from their front-end applications through a straightforward configuration screen. The video covers the alerting process, including how to visualize alerts when they fire, edit thresholds, and manage notifications. Elliot highlights the simplicity of modifying alert settings and how alerts can be configured during the creation of new applications, ensuring users have instant access to crucial performance data. Overall, the video emphasizes the ease of integrating and managing alerts within the Grafana platform.

# Introduction to Front-End Observability Alerting

Hello there! My name is Elliot Kirk, and I'm an engineer on the Front-End Observability and Pharaoh team here at Grafana. I'm excited to talk to you today about a new feature we've been developing: **out-of-the-box alerting for front-end observability**.

## Overview of the New Feature

With this feature, we've created a set of alerts and a process for creating these alerts that is as simple as possible, all based on the data coming from your front-end applications. 

From the configuration screen, you can select which alerts you want enabled, as well as the apps to enable them on. When you enable these alerts, we automatically create a set of recording rules and corresponding Grafana managed alerts.

## Monitoring Alerts in Action

Now that we've enabled the alerts, let's see what happens when they start to fire in our application. We can see that a widget indicates the errors count alert firing for us. By clicking through, we can visualize it in the alerting UI in Grafana Cloud. This interface provides a lot of detail about how the series has been performing, along with some configuration options for this alert.

We can dive deeper to examine even more details, and if needed, we have the option to edit the alert.

## Editing Alerts

If you're unfamiliar with the Grafana managed alert UI, we’ve created a way to edit these alerts very simply. Just go to the app settings page and click on **Edit Alert Threshold**. 

For error alerts, you can change how long the alert needs to be above the threshold before it begins to fire. For web vital alerts, you can adjust the value as well as the duration that the alert must exceed the threshold before it starts firing.

## Visualizing and Managing Alerts

The app settings page also provides several ways to visualize these alerts without leaving the Front-End Observability UI. Additionally, it offers options for pausing alerts if you want them to stop firing or if you feel they aren't necessary to enable for this application at the moment.

You can also return to the alerting UI screens to edit them in a more granular way. 

### Notifications

Notifications are an important aspect of alerting on the Grafana platform. If you don’t enable the notification settings, the only way to see these alerts firing is from front-end observability. The alerting documentation we've released alongside this update will cover notifications in more detail.

## Enabling Alerts During App Creation

We’ve also provided an option to enable alerts alongside new app creation. Just follow the normal setup wizard for creating a Front-End Observability app, and you’ll find that the last step allows you to enable alerting for this new app. 

Select as many alerts as you'd like, and they will be configured to fire on your application right from the start.

Thank you for your attention, and I hope you're excited to try out these new alerting features!

## Raw YouTube Transcript

Hello there. My name is Elliot Kirk and I'm an engineer on the front-end observability and Pharaoh team here at Graphfana. And I'm excited to talk to you today about a new feature that we've been cooking up, out of the box alerting for front-end observability. What we've done with this feature is create a set of alerts uh and a process for creating these alerts that's as simple as possible all based off the data coming from your front-end applications. From this config screen, we can select which alerts we want enabled, as well as the apps to enable them on. When we enable these alerts, we automatically create a set of recording rules and corresponding Graphana managed alerts. Now that we've enabled these alerts, let's see what happens when they start to fire in our application. We can see that this widget is indicating that the errors count alert firing for us. and we can click through to visualize it in the alerting UI in uh Graphana Cloud. This gives us a lot of detail about how the series has been performing and some of the configuration options of this alert. We can dive in deeper, look at even more of the details, and we can choose to edit it here if we want. If you're unfamiliar with the Graphana managed alert UI, we created a way to edit these alerts in a very simple way. Just go to the app settings page and click edit alert threshold. For errors, you can change how long the alert needs to be above the threshold before it actually begins to fire. And for web vital alerts, you can change the value as well as the duration that the alert needs to be above that threshold before it starts to fire. The app settings page also provides a few ways to visualize these alerts without leaving the front-end observability UI. as well as providing a few options for pausing alerts if you want them to stop firing or if you don't feel that they're necessary to be enabled on this application at the time. You can also head back into the alerting UI screens and edit them in a more finer grained way. Specifically, uh notifications are an important aspect of alerting on the Graphana platform. If you don't enable the notification settings, the only way that you'll be able to see these alerts firing is from front-end observability. The alerting documentation that we've released alongside this update will cover the notifications in more detail. And of course, we have provided an option to enable alerts alongside new app creation. Just go through the normal setup wizard for creating a front-end observability app and you'll find that the last step allows you to enable alerting for this new app. Select as many as you'd like and alerts will be configured to fire on your application right from the start.

