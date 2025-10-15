# A Smoother and Faster Alert Rule List Page in Grafana 12.1 | Grafana Alerting

Published on 2025-07-28T13:57:30Z

## Description

Our new Alert rule list page provides a smoother and faster user experience. It features two views, each supporting its own use ...

URL: https://www.youtube.com/watch?v=CL9BYXjx-l4

## Summary

In this video, the Grafana alerting team introduces a new alert list view designed to enhance performance for users with numerous alert rules. The previous version lacked true pagination, leading to performance issues for customers managing thousands of alerts. The new alert list view features true pagination, ensuring efficient loading regardless of the number of rules. It also allows users to interactively manage their alerts within groups and provides a comprehensive view of all accessible alerts along with their firing status. However, the page has been streamlined by removing firing alert information to improve performance, with plans to develop a dedicated triage dashboard for better incident response in the future. Users can revert to the old view if desired, but this option is exclusive to paid Grafana customers.

The Grafana alerting team has created a new alert list view that provides exceptional performance for all customers, regardless of the number of alert rules they have. The previous alert list view lacked true pagination, which caused performance issues for customers with thousands of alert rules. 

The new view features true pagination and will load efficiently, no matter how many alert rules you create within your stack. In addition to improving performance for customers with a large number of alerts, we have established a clear distinction between creating and maintaining your alert rules and responding to alert notifications. 

We have made this page more interactive for managing your alert rules by allowing you to view your alerts within your alert group. You can also access a list view that displays every alert you have access to, along with their status—whether they are firing or not. By clicking on an alert, you can jump directly to that rule.

Please note that the firing alert information and the alert notification triage details have been removed from this page. While this page enhances performance, it is not the most suitable for responding to alert notifications. A dedicated dashboard page or a new triage page is currently in development and will be released in one of the upcoming quarters, providing a better solution for alert instance triage.

If you do not like the new view, there is an option to revert back; however, this toggle is only available for paid Grafana customers.

## Raw YouTube Transcript

Graphana alerting team has created a new alert list view that will provide exceptional performance for all customers no matter how many alert rules that they have. The previous alert list view did not have true pageionation which cause performance issues for customers with thousands of alert rules. The new view has true pageionation and will load no matter how many alert rules that you create within your stack. On top of creating better performance for customers with a large amount of alerts, we have created a clear delineation between creating and maintaining your alert rules in responding to alert notifications. We've made this page more interactive for creating and maintaining your alert rules by being able to view your alerts within your alert group. You can also have a list view that views every alert that you have access to with the status of whether they're firing or not. And you can jump within that rule by clicking on it. Users will notice that the firing alert information, the alert notification triage information on this page has been removed on top of providing performance issues. This page is not the best page for responding to alert notifications and a dedicated dashboard page or a new triage page that we are working on and will be releasing in one of the upcoming quarters will be better apt to do alert instance triage. You do not like the new view, you can click to go back. The toggle is only available for paid Graphana customers.

