# How To Perform A TCP Check | Grafana Synthetic Monitoring

Published on 2025-07-22T14:05:55Z

## Description

Learn how to set up TCP checks using Grafana Cloud Synthetic Monitoring. In this video, we walk through how to create a TCP ...

URL: https://www.youtube.com/watch?v=7EMHwWLrxfI

## Summary

In this video, Pakola, a senior developer advocate at Grafana, provides a comprehensive guide on performing TCP checks using Grafana Cloud synthetic monitoring. He explains that TCP checks are crucial for monitoring non-HTTP services by verifying server connections and measuring metrics like response latency and uptime, thereby allowing users to proactively identify and resolve connectivity issues. Pakola details the steps to set up a TCP check, including selecting the appropriate check type, configuring request targets, choosing probe locations, and setting up alerting options. He emphasizes the importance of effective monitoring and alerting in maintaining service reliability and provides insights into the dashboard metrics available once the TCP check is active. The video serves as a practical tutorial for users looking to enhance their monitoring capabilities with Grafana.

# TCP Check with Grafana Cloud Synthetic Monitoring

Hi, I'm Pakola, a senior developer advocate at Grafana. In this video, I'll show you how to perform a TCP check using Grafana Synthetic Monitoring. TCP checks are essential for monitoring your non-HTTP services. With a TCP check, you can verify that a server accepts a connection and measure the response latency and uptime. This helps you catch TCP connection issues before they affect users.

## What is Grafana Cloud Synthetic Monitoring?

Before we dive into TCP checks, let's go over what Grafana Cloud Synthetic Monitoring is. Grafana Cloud Synthetic Monitoring is a blackbox monitoring solution that allows you to monitor services and applications by running checks from public and private probes located globally. This enables you to assess the availability, performance, and correctness of these services and applications with ease.

Users can perform a wide variety of checks, including:

- Browser checks
- Ping checks
- DNS checks
- HTTP checks
- Scripted checks
- TCP checks

Now that you have an overview of Grafana Cloud Synthetic Monitoring, let's return to TCP checks.

## Understanding TCP Checks

A TCP check allows you to connect to an endpoint on a given hostname or IP address and port to verify that a server accepts a connection. Additionally, with a TCP check, you can measure the response latency, uptime, and other critical metrics. This can be used to verify non-HTTP services like mail servers, FTP servers, databases, message queues, and applications.

### Key Benefits of TCP Checks

- **Quick Diagnosis**: Identify network connectivity issues by determining when services aren’t accepting connections.
- **Security Monitoring**: Detect when ports are open that shouldn’t be or when required services are down.
- **Proactive Monitoring**: Get alerted before users experience problems.

Grafana Cloud Synthetic Monitoring makes it easy to run a TCP check from different locations around the globe, providing valuable insights into connection success rates, response times, and service availability.

## Setting Up Your First TCP Check

To get started, you'll need a Grafana Cloud account. Once you're on the homepage, follow these steps:

1. **Navigate to Testing and Synthetics**: Open the main menu, select "Synthetics Checks," and then click "Add Create a Check."
2. **Choose Check Type**: Select "API Endpoint" as the check type and provide a job name (we'll use "Example: TCP").
3. **Set Request Type**: Choose "TCP" as the request type and set the target URL to `smtp.gmail.com:587`. You have the option to include a TLS config, but for this video, we'll keep it simple.
4. **Define Uptime**: Click the "Define Uptime" button. You can select the "Add Query-Response" button to specify the query and response. Set the timeout to 10 seconds.
5. **Add Labels**: Click the "Labels" button to create custom labels that add additional information for alerts. Use key-value pairs; for the name, use "N" and for the value, use "test."
6. **Execution Settings**: Click the "Execution" button to choose between public and private probe locations. Grafana offers access to over 20 globally distributed locations. For this test, select Calgary, Canada, and Stockholm, Sweden as the probe locations. Set the test frequency to run every 1 minute.

### Alerting Configuration

Effective alerting is essential for synthetic monitoring. When metrics deviate from expected performance, alerts trigger necessary actions based on these metrics. You have two alerting options: per check alerts or legacy alerts. We recommend per check alerts, which allow you to create alerts based on the number of check failures in a specific time window.

If you remember, we have two probe locations (Calgary and Stockholm) sending one request every minute. In 5 minutes, we will send 10 requests. Specify how many failures of the 10 executions you want to be alerted about. For this tutorial, we'll choose a threshold of 2 out of 10 execution failures in the last 5 minutes.

Once all settings are configured, click "Save" to initiate the test. You can also click the test button to ensure the test works before saving. 

Now, your TCP check is active and running.

## Reviewing the Results

Our script has been running for a few hours, so let’s review the results. Each synthetic monitoring check includes a preconfigured dashboard that provides key insights into your selected synthetic monitoring test. The dashboard offers metrics such as:

- Uptime
- Reachability
- Average latency
- SSL chain expiry
- Frequency

As you scroll through the dashboard, you'll find additional charts for deeper visibility. You can also see response latency by probe location. All data and visualizations are updated in real time as the test continues to run, allowing for continuous performance monitoring and faster issue detection.

## Conclusion

There you have it! You now know about Grafana Cloud Synthetic Monitoring and how to create a TCP check. You can check out Grafana Play Synthetic Monitoring to see a dashboard with a variety of running checks. If you want to learn more about Grafana Cloud Synthetic Monitoring, make sure to check out the documentation. 

I'll see you in the next video!

## Raw YouTube Transcript

Hi, I'm Pakola, a senior developer advocate at Graphfana. In this video, I'll show you how to perform a TCP check using Graphana synthetic monitoring. TCP checks are essential for monitoring your non-HTTP services. With a TCP check, you can verify that a server accepts a connection and measure the response latency and uptime. This helps you catch TCP connections issues before they affect users. Before we walk through TCP tracks, let's walk through what Graphana Cloud synthetic monitoring is. Rafonocloud synthetic monitoring is a blackbox monitoring solution that allows you to monitor services and applications by running checks from public and private probes located globally. This allows you to assess the availability and performance and correctness of these services and applications with ease. Users can perform a wide variety of checks from browser checks, ping checks, DNS checks, HTTP checks, scriptor checks, and TCP checks. Now that you have this overview of Graphana Cloud synthetic monitoring, let's return back to TCP checks. A TCP check allows you to connect to an endpoint on a given host name or IP address and port to verify that a server accepts a connection. Additionally, with a TCP check, you can also measure the response latency, uptime, and other critical metrics. This can be used to verify the nonHTTP services like mail servers, FTP servers, database, message cues, and applications are working properly. Some key benefits of TCP checks are a quick diagnosis of network connectivity issues by identifying when services aren't accepting connections, security monitoring, detecting when ports are open that shouldn't be or when required services are down, proactive monitoring of critical service, getting alerted before users experience problems. Grafano Cloud synthetic monitoring makes it easy to run a TCP check from different locations all over the globe. then provides you with valuable insights into the connection success rate, response time, and service availability. Let's now walk through the steps required to set up your first TCP check. To get started, you'll need a Graphfana Cloud account. Once you're on the homepage, open the main menu and navigate to testing and synthetics. Select synthetics checks and then click add create a check. Choose API endpoint as the check type. Provide a job name. We'll use the name example colon TCP. Select a request type. We'll choose TCP. Select the request target. We'll choose the target URL import smtp.gmail.com 587. When you are specifying your request target, you also have the option to include a TLS config. But for this video, we'll keep it simple. Let's move to step two by clicking the define uptime button. You can select the add query- response button. This will be the query and this will be the response. Now, let's move on to timeout. We'll choose 10 seconds. Let's move to step three by clicking the labels button. We recommend creating custom labels because they add additional information which can be helpful if you are alerted about a test. Each label is using key value pairs. For the name, we'll choose N and for value, we'll choose test. Let's move to step three by clicking the execution button. In the execution section, you can choose between public and private probe locations. Graphana offers access to over 20 globally distributed provocations. For this test, we will select Calgary, Canada, and Stockholm, Sweden as the probe location. Further down on the page, you'll also find the option to set the test frequency. We will configure the TCP check to run every 1 minute. Notice the additional information provided about the estimated executions expected to occur per month. Let's move to step four by clicking the alerting button. Effective alerting is essential for synthetic monitoring. When metrics deviate from expected performance, alerts are the most effective way to trigger the necessary actions based on these metrics. You have two alerting options, per check alerts or legacy alerts. We recommend per check alerts which allow you to create alerts based on the number of check failures in a specific time window. If you remember in the previous section, we have two probe locations, one in Calgary and one in Stockholm, sending one request every minute. So in 5 minutes, we will send 10 requests. In this section, we can specify how many failures of the 10 executions we want to be alerted about. For this tutorial, we'll choose two of 10 execution fails in the last 5 minutes as the threshold to get alerted. Once all settings are configured, click save to initiate the test. You can also choose a test button to ensure the test works before saving. At this point, your TCP check is now active and running. Our script has been running for a few hours, so let's now review the results. Each synthetic monitoring check includes a preconfigured dashboard that offers key insights into your selected synthetic monitoring test. The dashboard provides metrics such as uptime, reachability, average latency, SSL chain expiry, and frequency. As you scroll through the dashboard, you'll also find additional charts that offer deeper visibility. Additionally, you can see response latency by probe location. All the data and visualizations are updated in real time as the test continues to run, allowing you to have continuous performance monitoring and faster issue detection. There you have it. You now know about Graphana Cloud synthetic monitoring solution and how to create a TCP check. You can check out Graphana Play synthetic monitoring to see a dashboard with a variety of running checks. If you want to learn more about Grafana Cloud synthetic monitoring, make sure to check out this documentation and I'll see you in the next video.

