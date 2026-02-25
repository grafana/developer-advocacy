# How To Create and Manage Secrets | Grafana Cloud Synthetic Monitoring

Published on 2026-02-23T16:09:56Z

## Description

Learn how to create and use secrets management in Grafana Cloud Synthetic Monitoring. In this video, we walk through the steps ...

URL: https://www.youtube.com/watch?v=KDbS8mYj1z0

## Summary

In this video, Bakola, a senior developer advocate at Grafana, explains how to utilize secret management in Grafana Cloud Synthetic Monitoring to securely handle sensitive data such as API keys, passwords, and tokens during automated tests. He provides an overview of Grafana Cloud Synthetic Monitoring, a service for monitoring the availability and performance of services through various checks. Bakola details the process of creating and using secrets, emphasizing their encryption, centralized storage, and automatic redaction in logs to enhance security. He walks through a practical example of creating two secrets for a demo application called Quick Pizza and demonstrates how to implement these secrets in a synthetic monitoring check. The video concludes with guidance on managing and modifying secrets as needed.

## Chapters

00:00:00 Introductions and overview of the stream  
00:01:30 What is Grafana Cloud Synthetic Monitoring?  
00:02:45 Introduction to secrets management in Grafana  
00:03:30 Benefits of using secrets management  
00:04:15 Permissions required for managing secrets  
00:05:00 Creating the first secret for Quick Pizza app  
00:06:00 Creating the second secret for Quick Pizza app  
00:07:15 Using secrets in a synthetic monitoring check  
00:09:00 Configuring check settings and execution  
00:10:30 Reviewing check results and monitoring outputs  

# Using Secret Management in Grafana Cloud Synthetic Monitoring

Hi, I'm Bakola, a senior developer advocate at Grafana. In this video, I'll show you how to use secret management in Grafana Cloud Synthetic Monitoring to securely store and use sensitive data like API keys, passwords, and tokens in your checks. This keeps your credentials secure while running automated tests and prevents accidental exposure of sensitive information.

## What is Grafana Cloud Synthetic Monitoring?

Grafana Cloud Synthetic Monitoring is a black-box monitoring service that allows you to run checks like browser, ping, DNS, and TCP checks from globally distributed public probes or self-hosted private probes. This proactive approach helps measure the availability, latency, and correctness of your services.

## Secrets Management Overview

In Grafana Cloud Synthetic Monitoring, secrets management provides a centralized location to securely store sensitive data such as API keys, passwords, and tokens. Behind the scenes, secrets are encrypted at rest using envelope encryption. When you reference a secret in your test, the value is automatically masked in the UI scripts and logs to prevent accidental exposure.

### Benefits of Secrets Management

- Centralized storage for all your credentials
- Automatic redaction in logs and outputs
- Easy credential rotation without modifying test scripts

**Note:** Currently, secrets can only be accessed in scripted and scripted browser checks, but support for secrets in HTTP checks will be available in the future.

## Creating Your First Secret

Let's walk through how to create your first secret. Before we get started, there are a few important things to note about permissions. By default, only users with the Grafana admin role can create, edit, and delete secrets. However, users with editor and viewer roles can be granted access to manage secrets through role-based access control using a fixed role. Make sure to review the role-based access control section of the documentation before proceeding.

Today, we'll create two secrets for logging into our demo app called Quick Pizza.

1. **Navigate to Testing and Synthetics:**
   - Go to the homepage, then select **Testing** and **Synthetics**.
   - Click on **Config**, then the **Secrets** tab.
   - Click **Create Secrets**.

2. **Create the First Secret:**
   - In the create secret form:
     - **Name:** Quick Pizza Username
     - **Description:** Username to log in to Quick Pizza
     - **Value:** admin
     - **Label:** 
       - **Name:** service 
       - **Value:** quick pizza authentication
   - Click **Save**.

3. **Create the Second Secret:**
   - Click **Create Secret** again.
   - In the create secret form:
     - **Name:** Quick Pizza Password
     - **Description:** Password to log in from Quick Pizza
     - **Value:** admin
     - **Label:** 
       - **Name:** service 
       - **Value:** quick pizza authentication
   - Click **Save**.

Your secrets are now created and ready to use in a synthetic monitoring check.

## Using Secrets in a Synthetic Monitoring Check

Now, let's use the secrets we created in a synthetic monitoring check.

1. **Navigate to Create a New Check:**
   - Go to **Testing and Synthetics**, then select **Checks**.
   - Click **Create a New Check** and choose **Browser** as the check type.

2. **Configure the Check:**
   - **Job Name:** Quick Pizza Admin Login: Browser
   - **Instance:** quickpizza.com/admin
   - In your script, import the Ksix secrets module:
     ```javascript
     import secrets from Ksix secrets;
     ```
   - You can now use the secret name variable anywhere in your script. Uncomment the lines that reference the secret name and password. 
   - Add a log to share your secret (for demonstration purposes):
     ```javascript
     console.log("Trying to log the secret value");
     ```

3. **Add Labels:**
   - Add the same labels as the two secrets:
     - **Name:** service
     - **Value:** quick pizza authentication

4. **Execution:**
   - Choose between public and private probe locations. For this test, select Calgary, Canada, and Tokyo, Japan.

5. **Alerting:**
   - Click the alerting button. Ensure all settings are configured, then click the test button to verify the test works before saving. If it works, click **Save** to initiate the test.

Your scripted check using secrets is now active and running.

## Reviewing Results

Each synthetic monitoring check includes a preconfigured dashboard that offers key insights into your tests. You can also view the test log, where you'll see that any secret values are automatically redacted with the placeholder "secrets redacted" in asterisks. This feature helps prevent accidental exposure of sensitive data in logs, error messages, and other test outputs.

## Managing Secrets

If you ever want to delete or change secrets, navigate to the homepage, then Testing and Synthetics, followed by Synthetics and Config. Click the Secrets tab. To delete a secret, find the name of the secret and click the trash icon next to it. To change a secret name, find the name of the secret you want to edit and click the edit button next to it.

## Conclusion

And there you have it! You now know how to use secret management in Grafana Cloud Synthetic Monitoring to securely store and reference sensitive data in your tests. If you want to see this in action, please check out Grafana Play Synthetic Monitoring to explore dashboards with a variety of running checks. For more information, make sure to check out the documentation linked below. 

I'll see you in the next video!

## Raw YouTube Transcript

Hi, I'm Bakola, senior developer advocate at Grafana. In this video, I'll show you how to use secret management in Grafana Cloud synthetic monitoring to securely store and use sensitive data like API keys, passwords, and tokens in your checks. This keeps your credentials secure while running automated tests and prevents accidental exposure of sensitive information. Before we dive in, let's quickly cover what Graphana Cloud Synthetic Monitoring is. Graphana Cloud Synthetic Monitoring is a blackbox monitoring service that lets you run checks like browser, ping, DNS, and TCP checks from globally distributed public probes or self-hosted private probes to proactively measure the availability, latency, and correctness of your services. Now, let's talk about secrets management. In Graphana Cloud Synthetic monitoring, secrets management provides a centralized location to securely store sensitive data like API keys, passwords, and tokens. Behind the scenes, secrets are encrypted at rest using envelope encryption. When you reference a secret in your test, the value is automatically masked in the UI scripts and logs to prevent accidental exposure. The benefits of secret management include centralized storage for all your credentials and automatic redaction in logs outputs and easy credential rotation without modifying test scripts. Currently, secrets can only be accessed in scripted and scripted browser checks, but support for secrets and HTTP checks will be available in the future. Let's [clears throat] walk through how to create your first secret. Before we get started, there are a few important things to note about permissions. By default, only users with Graphana admin role can create, edit, and delete secrets. However, users with editor and viewer roles can be granted access to manage secrets through role-based access control using a fixed role. So, make sure you review the role-based access control section of the documentation before proceeding. Today, we'll create two secrets to use for logging into our demo app called Quick Pizza. Once you're on the homepage, navigate to testing and synthetics and then synthetics and then config. Click the secrets tab and then click create secrets. In the create secret form, for name, we'll use Quick Pizza username. For description, we'll add username to log to quick pizza. For value, we'll enter the username, which is admin. You also have the option to add a label. We'll create one with the name service and the value quick pizza authentication. Then click save. Now let's create our second secret. Click create secret again. For name we'll use quick pizza password. For description we'll add password to log in from quick pizza. For value we'll enter the password which is admin. We'll add the same label as before. Name service and value quick pizza authentication. Click save. And your secrets are now created and ready to use in a synthetic monitoring check. But now let's use the secret we created in a synthetic monitoring check. Navigate to testing and synthetics homepage. Select synthetics then checks. Then click create a new check. Choose browser as the check type. Step one. For job name, we'll use the name quick pizza admin login semicolon browser. For instance, we'll choose quick pizza.com/admin. In your script, you'll need to import the Ksix secrets module. We'll add import secrets from Ksix secrets. Because we've created our secrets, you can now use the secret name variable anywhere in your script. The example script has the secret name and password commented out. We'll uncomment those lines to use them in the script. We'll also add a log that shares our secret just to show you how secrets are adapted. The line will look like this. Console.log try to log the secret value. Now, let's move to step three, labels. We'll add the same labels as the two secrets before. Name service and value quick beats authentication. to keep our labels consistent and organized. Now, let's move to step four, execution. In the execution section, you can choose between public and private probe locations. For this test, we'll select Calgary, Canada, and Tokyo, Japan as the probe location. Now, let's move to our final step by clicking the alerting button. In step five, alerting. Now that all settings are configured, you can also choose the test button to ensure the test works before saving. Now that we know that it's working, let's click save to initiate the test. At this point, your scripted check using secrets is now active and running. Let's review the result. Each synthetic monitoring check includes a preconfigured dashboard that offers key insights into your synthetic monitoring tests. You can also view the test log where you'll see that any secret value are automatically redacted with the placeholder secrets redacted in asterisk. This is one of the features of secrets management. Secret values are masked in synthetic monitoring outputs to prevent accidental exposure of sensitive data in logs, error messages, and other test outputs. If you ever want to delete or change secrets, navigate to home, then testing synthetics, then synthetics, then config. Click the secrets tab. To delete a secret, find the name of the secret you want to delete and click the trash icon next to it. To change a secret name, find the name of the secret you want to edit and click the edit button next to it. And there you have it. You now know how to use secret management in Graphana Cloud Synthetic Monitoring to securely store and reference sensitive data in your tests. If you want to see this in action, please check out Grafana Play synthetic monitoring to explore dashboard with a variety of running checks. If you want to learn more about Grafana Cloud synthetic monitoring, make sure to check out the documentation linked down below and I'll see you in the next video. [music] >> [music]

