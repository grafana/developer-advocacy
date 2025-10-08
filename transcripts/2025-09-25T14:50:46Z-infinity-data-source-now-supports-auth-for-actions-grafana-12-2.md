# Infinity Data Source Now Supports Auth for Actions | Grafana 12.2

Published on 2025-09-25T14:50:46Z

## Description

Grafana 12.2 introduces actions authentication with the Infinity data source — giving you more secure and flexible ways to trigger ...

URL: https://www.youtube.com/watch?v=7YBORfb3PMM

## Summary

In this video, Adela, an engineer from the DataViz squad at Grafana Labs, announces the introduction of actions authentication with the Infinity Data Source. Previously, actions could only make HTTP requests from the browser, which were limited by CORS restrictions. The new update allows users to choose between the traditional browser method and the Infinity data source for actions that require authentication. Adela explains how to set up the Infinity data source, including configuring HTTPS basic authentication and creating new actions with the desired connection. She highlights that users with viewer roles can now see or execute actions, and encourages viewers to refer to the Infinity documentation for further details.

# Announcement of Actions Authentication with Infinity Data Source

Hi, my name is Adela, and I'm an engineer on the DataViz squad at Grafana Labs. Today, I'm excited to announce **actions authentication with the Infinity Data Source**.

As a recap, previously, actions could only make HTTP requests from the browser, which are subject to CORS restrictions, significantly limiting their usefulness. With this update, you can now choose between:

- **Direct from browser** (the original method)
- **Infinity Data Source**, which allows you to perform actions that require authentication by leveraging pre-configured Infinity data source connections.

To set up an Infinity data source, follow these steps:

1. Go to **Connections**.
2. Select **Data Sources**.
3. Click **Add New Data Source** and search for **Infinity**.
4. Click **Set Up Authentication**.

For this demo, I'm using **HTTPS Basic Authentication**. So, we'll click **Basic Authentication**, configure the user and password, and add your allowed hosts. For more details, you can refer to **Infinity's documentation page**.

Next, create a new action with a title and URL, and as the connection, choose the desired Infinity connection. To try out this feature, enable the **actions auth feature toggle**. 

Please note that users with the viewer role can see or execute actions. 

Thank you from the DataViz squad at Grafana!

## Raw YouTube Transcript

Hi, my name is Adela and I'm an engineer
on the DataViz squad at Grafana Labs. Today I'm excited to announce actions
authentication with the Infinity Data Source. As a recap, previously actions could only make
HTTP requests from the browser, which are subject to course restriction, significantly limiting their
usefulness. With this update, you can now choose between
direct from browser, the original method and
Infinity data source, which lets you perform actions that
require authentication by leveraging pre-configured Infinity
data source connections. To set up an Infinity data source,
go to connections, data sources, add new data source and search for
Infinity. Click set up authentication. And for this demo, I'm using
HTTPS basic authentication. So we'll click basic authentication,
configure user and password, and add your allowed
hosts. For more detail, you can find on Infinity's
documentation page. Then create a new action at
Title URL, and as connection, choose the desired Infinity connection. To try out this feature, enable
these actions, auth feature toggle. Note that users with the viewer
role can see or execute actions. Thanks from the DataViz squad at Grafana.

