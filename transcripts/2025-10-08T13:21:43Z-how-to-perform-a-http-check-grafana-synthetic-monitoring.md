# How To Perform A HTTP Check | Grafana Synthetic Monitoring

Published on 2025-10-08T13:21:43Z

## Description

Learn how to set up HTTP checks using Grafana Cloud Synthetic Monitoring. In this video, we walk through how to create a HTTP ...

URL: https://www.youtube.com/watch?v=1BQ6iGuv_6Q

## Summary

In this video, Bakola, a senior developer advocate at Grafana, provides a comprehensive tutorial on setting up HTTP checks using Grafana Cloud Synthetic Monitoring. The video begins with an overview of Grafana Cloud Synthetic Monitoring, a blackbox monitoring solution designed to proactively monitor services and applications globally. Bakola explains the significance of HTTP checks in verifying endpoint availability, response speed, and status codes, emphasizing their role in maintaining application reliability and user experience. He walks through the setup process using Grafana's demo app, Quick Pizza, detailing steps such as selecting check types, configuring request options, defining uptime parameters, and setting up alerts. Bakola concludes by highlighting the real-time insights and metrics provided by the monitoring checks, encouraging viewers to explore Grafana Play for more examples and to refer to the documentation for further learning.

## Chapters

Here are the key moments from the livestream with timestamps:

00:00:00 Introduction to the video and presenter  
00:00:30 Overview of HTTP checks and their importance  
00:01:15 Explanation of Grafana Cloud Synthetic Monitoring  
00:02:00 Types of checks available in Grafana Cloud  
00:02:45 Introduction to setting up the first HTTP check  
00:03:30 Steps to create an HTTP check using Quick Pizza demo app  
00:05:00 Detailed configuration options for the HTTP check  
00:06:15 Setting up alerting options for the HTTP check  
00:07:30 Overview of the results dashboard for synthetic monitoring  
00:08:00 Conclusion and resources for further learning

# HTTP Checks in Grafana Cloud Synthetic Monitoring

Hi, I'm Bakola, a senior developer advocate at Grafana. In this video, I'll show you how to run an HTTP check in Grafana Cloud Synthetic Monitoring. 

An **HTTP check** verifies that your endpoint is online, measures how fast it responds, and ensures that it's returning the correct status response code. Consistently scheduled HTTP checks allow you to catch HTTP connection errors the moment they happen, before your users experience them. This helps ensure your applications are reliable and that users have a good experience.

## What is Grafana Cloud Synthetic Monitoring?

Before we delve into HTTP checks, let’s review what Grafana Cloud Synthetic Monitoring is. It is a **blackbox monitoring solution** that allows you to proactively monitor services and applications by running checks from public and private probes located globally. This enables easy assessment of the availability, performance, and correctness of these services and applications.

With Grafana Cloud Synthetic Monitoring, users can perform a wide variety of checks, including:

- Browser checks
- Ping checks
- DNS checks
- TCP checks

Now, let's return to the HTTP check and walk through how to set up your first one with Grafana Cloud Synthetic Monitoring.

## Setting Up Your First HTTP Check

An HTTP check is one of the simplest ways to validate that your application is available and responding correctly. With Grafana Cloud Synthetic Monitoring, you can send a request to an HTTP or HTTPS endpoint to measure uptime, track response latencies, and capture errors. These checks can be used to:

- Validate return status codes
- Validate response headers using regular expressions
- Validate response bodies using regular expressions

For more complex validations, consider checking out **multi-step HTTP checks** and **scripted checks**. HTTP checks can run from over 20 managed locations worldwide or from private probes within your own network. The results provide clear insights into your application's health and performance and can trigger alerts to keep you informed when issues arise.

### Steps to Set Up an HTTP Check

For this tutorial, we will use Grafana's demo app, **Quick Pizza**. To get started, you'll need a Grafana Cloud account. Once you're on the homepage, follow these steps:

1. **Navigate to Testing and Synthetics**  
   Open the main menu and select Synthetics, then click on **Create a Check**. You will see various options for checks.

2. **Choose the Check Type**  
   All four check types can perform HTTP tests. Here’s how to decide which one to choose:
   - **Multi-step checks**: Use this if you want to run multiple HTTP requests in sequence, passing response data from one request to the next.
   - **Script checks**: Use this if you want to write a Ksix script that performs an HTTP test.
   - **Browser checks**: Use this if you want to write a Ksix script that controls a headless browser.
   - **API endpoint check**: This is the recommended option if you have a single endpoint to test. This is the one we will choose for this demo.

3. **Configure the Check**  
   - Provide a job name (we'll use **Quick Pizza: HTTP**).
   - Select a request type (we'll choose **HTTP**).
   - Select a request target (we'll choose **GET** and set our endpoint to `https://quickpizza`).

   When specifying your request target, you can also include additional options by selecting **Request Options**. Here, you can add options like specifying whether to follow redirects, a body for requests, authentication, specific TLS options, etc. Please note that if you add a request body, the body size is limited to 64 KB.

4. **Define Uptime**  
   Click the **Define Uptime** button. We will leave the valid status code and HTTP version blank (defaulting to any 200 status code). For SSL options, we will choose to **ignore SSL certification**. Set the timeout to **3 seconds**; if you don't get a response in this time, the check will fail.

5. **Add Labels**  
   Click the **Labels** button. It’s recommended to create custom labels for additional information, which can be helpful if you are alerted about a test. Each label uses key-value pairs. We’ll choose **Quick Pizza: Test**.

6. **Execution Settings**  
   Click the **Execution** button. You can choose between public and private probe locations. For this example, we will choose **Montreal**, **Jakarta**, and **Stockholm**. We will stick to public probes for this demo. Set the test frequency to run every **1 minute**.

7. **Alerting Options**  
   Click the **Alerting** button. Effective alerting is essential for synthetic monitoring. You have two alerting options: **per check alerts** or **legacy alerts**. We recommend per check alerts, which allow you to create alerts based on the number of check failures in a specific time window, TLS certificate failures, or latency thresholds. 

   We will select all three types of per check alerts:
   - **Fail check**: If three out of 15 executions fail in the last 5 minutes, we will be alerted.
   - **TLS certificate**: We will check alerts if the target certificate expires in less than a specified time.
   - **Latency**: We will check alerts if latency exceeds 200 milliseconds over the last 5 minutes.

Once all settings are configured, click **Save** to initiate the test. You can also choose the **Test** button to ensure the test works before saving.

### Reviewing the Results

At this point, your HTTP check is now active and running. Our script has been running for a few hours, so let's review the results. Each synthetic monitoring check includes a preconfigured dashboard that provides key insights into your selected synthetic monitoring tests. This dashboard offers metrics such as:

- Uptime
- Reachability
- Average latency
- SSL expiry
- Frequency

As you scroll through the dashboard, you'll find additional charts that offer deeper visibility, including response latency by phase and response latency by probe location. All data and visualizations are updated in real-time as the test continues to run, allowing for continuous performance monitoring and faster issue detection.

### Conclusion

There you have it! You now know about Grafana Cloud Synthetic Monitoring and how to create an HTTP check. You can check out Grafana Play Synthetic Monitoring to see a dashboard with a variety of running checks. If you want to learn more about Grafana Cloud Synthetic Monitoring, make sure to check out the documentation.

See you in the next video!

## Raw YouTube Transcript

Hi, I'm Bakola, senior developer advocate at Grafana. In this video, I'll show you how to run an HTTP check in Graphana Cloud Synthetic Monitoring. An HTTP check verifies that your endpoint is online and measures how fast it responds and verifies that it's returning the correct status response code. Consistently scheduled HTTP checks allow you to catch HTTP connection errors the moment they happen and before your users experience them, allowing you to ensure your applications are reliable and users have a good experience. Before we walk through HTTP checks, let's walk through what Graphana Cloud Synthetic Monitoring is. Graphana Cloud Synthetic Monitoring is a blackbox monitoring solution that allows you to proactively monitor services and applications by running checks from public and private probes located globally. This allows you to easily assess the availability, performance, and correctness of these services and applications. With Graphana Cloud Synthetic Monitoring, users can perform a wide variety of checks, including browser checks, ping checks, DNS checks, TCP checks, to name a few check options. Let's return back to HTTP check and walk through how to set up your first HTTP check with Graphfana Cloud Synthetic Monitoring. An HTTP check is one of the simplest ways to validate that your application is available and responding correctly. With Graphana Cloud Synthetic Monitoring, you can send a request to an HTTP or HTTPS endpoint to measure uptime, track response latencies, and capture errors. These checks can be used to validate return status code, validate response headers using regular expressions, and validate response bodies using regular expressions. If you'd like to configure more complex validations, please check out a multi-step HTTP check and scripted checks. HTTP checks can run from over 20 plus managed locations from around the world or from private probes within your own network. The results give you clear insights into your application's health and performance and can trigger alerts to keep you informed when issues appear. Let's now walk through the steps required to set up your first HTTP check. For this tutorial, we are using Graphana's demo app, Quick Pizza. To get started, you'll need a Graphfana Cloud account. Once you're on the homepage, open the main menu and navigate to testing and synthetics. Select synthetics and checks and then click create a check. You'll see many options for checks. All four check types can perform HTTP tests, but here's how to decide which one to choose. Multi-step checks. Use this if you want to run multiple HTTP requests in sequence. Passing response data from one request to the next. Script checks. Use this if you want to write a Ksix script that performs an HTTP test. Browser checks. Use this if you want to write a Ksix script that controls a headless browser. API endpoint check. This is the recommended option if you have a single endpoint you want to test. This is the one we'll choose for this demo. Provide a job name. We'll use the name quick pizza semicolon http. Select a request type. We'll choose http. Select a request target. We'll choose get and make our endpoint httpsquick pizza. When you are specifying your request target, you can also include additional options by selecting request options. This is where you can add additional options like specifying whether to follow redirects, a body for requests, authentication specific and TLS options and etc. Please note if you do choose to add a request body, the body size is limited to 64 KBs. Let's move to step two by clicking the define uptime button. Valid status code, we will leave this blank. This defaults to any 200 status code. Valid HTTP version, we will leave this blank. SSL options. We will choose ignore SSL certification. But this section is where you can check if an SSL is present or not. Time out. We will choose 3 seconds. If you don't get a response in 3 seconds, our check will fail. Let's move to step three by clicking the labels button. In this section, we recommend creating custom labels because they add additional information which can be helpful if you are alerted about a test. Each label is using key value pairs. We'll choose quick pizza, test. Let's move to step three by clicking the execution button. In the execution section, you can choose between public and private probe locations. Here you can decide which probe locations to send the request from. We'll choose Montreal, Jakarta, Stockholm for this example. You can also set up a private probe, but we'll stick to public probes for this example. Further down on this page, you'll find the option to set the test frequency. We will configure the HTTP check to run every 1 minute. Notice the additional information provided about the estimated executions expected to occur per month. Let's move to step four by clicking the alerting button. Effective alerting is essential for synthetic monitoring. When metrics deviate from expected performance, alerts are the most effective way to increase awareness and trigger necessary actions based on those metrics. You have two alerting options, per check alerts or legacy alerts. Legacy alerts allow you to create alerts based on preconfigured alerting sensitivity thresholds. We recommend per check alerts which allow you to create alerts based on the number of check failures in a specific time window or if there is a TLS certificate failure or by latency threshold. We will select all three types of per check alerts. Fail check. If you remember in the previous section we had three probe locations Montreal, Jakarta and Stockholm sending one request every 5 minutes. So in 15 minutes we will send 15 requests. We can specify how many failures of the 15 executions we want to be alerted about. For this tutorial we will choose three of the 15 executions failure in the last 5 minute as the threshold to get alerted. TLS certificate we will check alerts if the target certificate expires in less than. For latency we will check alert if latency exceeds 200 milliseconds over the last 5 minutes. Once all settings are configured, click save to initiate the test. You can also choose a test button to ensure the test works before saving. At this point, your HTTP check is now active and running. Our script has been running for a few hours, so let's now review the results. Each synthetic monitoring check includes a preconfigured dashboard that offers key insights into your selected synthetic monitoring tests. This dashboard provides metrics such as uptime, reachability, average latency, SSL expiry, and frequency. As you scroll through the dashboard, you'll find additional charts that offer deeper visibility, including response latency by phase. Additionally, you can see response latency by probe location. All data and visualizations are updated in real time as the test continues to run, allowing for continuous performance monitoring and faster issue detection. There you have it. that you now know about Grafana Cloud synthetic monitoring solution and how to create an HTTP check. You can check out Grafana Play synthetic monitoring to see a dashboard with a variety of running checks. If you want to learn more about Grafana Cloud synthetic monitoring, make sure to check out the documentation. See you in the next video.

