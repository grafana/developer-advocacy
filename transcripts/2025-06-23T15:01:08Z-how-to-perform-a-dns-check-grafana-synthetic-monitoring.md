# How To Perform A DNS Check | Grafana Synthetic Monitoring

Published on 2025-06-23T15:01:08Z

## Description

Learn how to set up DNS checks using Grafana Cloud Synthetic Monitoring. In this video, we walk through how to create a DNS ...

URL: https://www.youtube.com/watch?v=d7j3-jxe5_M

## Summary

In this video, Pakola, a senior developer advocate at Grafana, explains how to perform DNS checks using Grafana Cloud Synthetic Monitoring. He highlights the importance of DNS checks for verifying domain resolutions and measuring response times to catch potential issues before they impact users. Pakola describes Grafana Cloud Synthetic Monitoring as a comprehensive solution for assessing the performance and availability of services through various types of checks, including DNS checks. He walks viewers through the setup process for their first DNS check, covering account creation, configuring check parameters, setting alert thresholds, and analyzing results through a dashboard that provides real-time insights. The video serves as a practical guide for users looking to leverage Grafana Cloud for DNS monitoring to enhance application reliability and performance.

# DNS Checks with Grafana Cloud Synthetic Monitoring

Hi, I'm Pakola, a senior developer advocate at Grafana. In this video, I'll show you how to perform a DNS check using Grafana Cloud Synthetic Monitoring.

DNS checks are a central way to verify if your domain resolves to the correct response and measure how quickly that resolution occurs. This can help you catch DNS issues before they affect users and verify whether DNS issues are at the root of your application or infrastructure performance problems.

## What is Grafana Cloud Synthetic Monitoring?

Before we walk through DNS checks, let's discuss what Grafana Cloud Synthetic Monitoring is. Grafana Cloud Synthetic Monitoring is a blackbox monitoring solution that allows you to monitor services and applications by running checks from public or private probes located globally. This enables you to assess the availability, performance, and correctness of these services and applications with ease.

Users can perform a wide variety of checks, including:
- Browser checks
- Ping checks
- TCP checks
- HTTP checks
- Scripted checks
- DNS checks

## Setting Up Your First DNS Check

Now, let's focus on DNS checks and walk through how to set up your first DNS check with Grafana Cloud Synthetic Monitoring. 

A DNS check ensures that a domain name resolves correctly to an IP address and measures the average time for that resolution to occur. Behind the scenes, this works by sending automated requests to a DNS server and checking the results for specific domain names. This validates that the domain returns the correct IP address in their A records and other DNS record types.

When a DNS server doesn't respond or when the search domain doesn't return the right IP address, Grafana Cloud Synthetic Monitoring DNS checks can spot that issue and alert the appropriate person on the team. Real-time DNS monitoring can help users identify and resolve network performance challenges before they impact users.

### Benefits of DNS Checks

The benefits of DNS checks include:
- **Real-time DNS Monitoring**: Helps users identify and resolve network performance challenges before they impact users.
- **Security Monitoring**: Detects DDoS attacks and DNS poisoning attempts that could compromise your services.
- **Global DNS Validation**: Tests DNS resolution from multiple locations worldwide to ensure consistent performance.

Grafana Cloud Synthetic Monitoring makes it easy to run DNS checks from different locations around the globe and provides valuable insights into the connection success rate, response time, and service availability.

### Steps to Set Up a DNS Check

To get started, you'll need a Grafana Cloud account. Once you're on the homepage, follow these steps:

1. **Navigate to Testing and Synthetics**:
   - Open the main menu and select **Synthetics Check**.
   - Click on **Create a Check**.

2. **Choose Check Type**:
   - Select **API Endpoint** as the check type.
   - Provide a job name (e.g., **Example DNS**).
   - Select a request type (choose **DNS**).
   - Specify the request target (we'll choose **target URL graphana.com**).

3. **Define Uptime**:
   - Click the **Define Uptime** button.
   - Select your valid response code from a variety of options (we'll choose **No Error**).
   - Set the timeout (we'll choose **10 seconds**).

4. **Add Labels**:
   - Click the **Labels** button.
   - Create custom labels for additional information. For the name, choose **N** and for the value, choose **Test**.

5. **Execution Settings**:
   - Click the **Execution** button.
   - Choose between public and private probe locations. Grafana offers access to over 20 globally distributed probe locations. For this test, we'll choose **Oregon, US**, and **Singapore** as the probe locations.
   - Set the test frequency to run every minute.

6. **Alerting Configuration**:
   - Click the **Alerting** button.
   - We recommend **Per Check Alerts**, which allow you to create alerts based on the number of check failures in a specific time window.
   - Specify the threshold for alerts (for this tutorial, we'll choose **2 of 10 execution failures** in the last 5 minutes).

7. **Save the Configuration**:
   - Once your settings are configured, click **Save** to initiate the test.
   - You can also click the **Test** button to ensure that the test works before saving.

At this point, your DNS check is now active and running.

## Reviewing Results

Our script has been running for a few hours, so let's review the results. Each synthetic monitoring check includes a preconfigured dashboard that offers key insights into your selected tests. This dashboard provides metrics such as:
- Uptime
- Reachability
- Average latency
- Frequency

As you scroll through the dashboard, you'll also find additional charts that offer deeper visibility, including response latency by probe location and resource records for each probe location. All data and visualizations are updated in real-time as the tests continue to run, allowing for continuous performance monitoring and faster issue detection.

## Conclusion

There you have it! You now know about Grafana Cloud Synthetic Monitoring and how to create a DNS check. You can check out Grafana Play Synthetic Monitoring to see a dashboard with a variety of running checks. 

If you want to learn more about Grafana Cloud Synthetic Monitoring, make sure to check out the documentation. Thank you for watching, and I'll see you in the next video!

## Raw YouTube Transcript

Hi, I'm Pakola, senior developer advocate at Graphana. In this video, I'll show you how to perform a DNS check using Graphana Cloud synthetic monitoring. DNS checks are a central way to verify if your domain resolves to the correct response and measures how quickly that resolution occurs. This can help you catch DNS issues before they affect users and verify whether DNS issues are at the root of your application or infrastructure performance issues. Before we walk through DNS checks, let's walk through what Graphana Cloud Synthetic Monitoring is. Graph Final Cloud Synthetic Monitoring is a blackbox monitoring solution that allows you to monitor services and applications by running checks from public or private probes located globally. This allows you to assess the availability and performance and correctness of these services and applications with ease. Users can perform a wide variety of checks from browser checks, ping checks, TCP checks, HTTP checks, scripted checks, and DNS checks. Let's return back to DNS checks and walk through how to set up your first DNS check with Graphana Cloud Synthetic Monitoring. A DNS check ensures that a domain name resolves correctly to an IP address and measures the average time for that resolution to happen. Behind the scenes, this works by sending automated requests to a DNS server and checking the results of the specific domain names, validating that the domain returns the correct IP address in their A records and other DNS record types. When a DNS server doesn't respond or when the search domain doesn't return the right IP address, Graphana Cloud Synthetic Monitoring DNS checks spot that issue and alert the right person on the team. Realtime DNS monitoring can help users identify and resolve network performance challenges before they impact users. The benefits of DNS checks include real-time DNS monitoring, which can help users identify and resolve network performance challenges before they impact users. Security monitoring which can help users detect DDoS attacks and DNS poisoning attempts that could compromise your services. Global DNS validation which can test DNS resolution from multiple locations worldwide to ensure consistent performance. Grafon cloud synthes monitoring makes it easy to run DNS check from different locations all over the globe. Then provides you with valuable insights into the connection success rate, response time, and service availability. Now, let's walk through the steps required to set up your first scan as check. To get started, you'll need a Graphana Cloud account. Once you're on the homepage, open the main menu and navigate to testing and synthetics. Select synthetics check and then add create a check. Choose API endpoint as the check type. Provide a job name. We'll select the name example DNS. Select a request type. We'll choose DNS. Select a request target. We'll choose target URL graphana.com. You also have additional request options. You can specify the record, the server, the protocol, and the port. Let's move on to step two by clicking the define uptime button. Select your valid response code. We have a variety of response codes to choose from. Add which response codes you expecting to receive. We'll choose no error. Select timeout. We'll choose 10 seconds. And let's move on to step two by clicking the labels button. We recommend creating custom labels because they add additional information which can be helpful if you are alerted about a test. Each label is using key value pairs. For the name, we'll choose N and for value, we'll choose test. Let's move on to step four by clicking the execution button. In the execution section, you can choose between public and private probe locations. Graphana offers access to over 20 globally distributed probe locations. And for this test, we'll choose Oregon, US, and Singapore as the probe location. Further down the configuration page, you'll find the option to set the test frequency. We will configure the DNS check to run every 1 minute. Notice the additional information provided about the estimated usage of this check. Let's move on to our final step by clicking the alerting button. Effective alerting is essential for synthetic monitoring. When metrics deviate from the expected performance, alerts are the most effective way to trigger necessary action based on those metrics. We have two alerting options, per check alerts or legacy alerts. We recommend perch check alerts which allow you to create alerts based on the number of check failures in a specific time window. If you remember in the previous section, we have two probe locations, Oregon and Singapore, sending one request every minute. So in 5 minutes, there will be 10 executions. In this section, we can specify how many of the failures of the 10 executions we want to be alerted about. For this tutorial, we'll choose two of 10 execution failures in the last 5 minutes as the threshold to get alerted. Once our settings are configured, click save to initiate the test. You can also choose the test button to ensure that the test works before saving. At this point, your DNS check is now active and running. Our script has been running for a few hours, so let's review the results. Each synthetic monitoring check includes a preconfigured dashboard that offers key insights into your selected synthetic monitoring tests. This dashboard provides metrics such as uptime, reachability, average latency, and frequency. As you scroll through the dashboard, you'll also find additional charts that offer deeper visibility, including response latency by probe location. Additionally, you can see resource records for each probe location. All data and visualizations are updated in real time as the tests continue to run, allowing for continuous performance monitoring and faster issue detection. There you have it. You now know about Grafana Cloud synthetic monitoring solution and how to create a DNS check. You can check out Grafana Play synthetic monitoring to see a dashboard with a variety of running checks. If you want to learn more about Grafana Cloud synthetic monitoring, make sure to check out this documentation and I'll see you in the next video.

