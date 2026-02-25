# How To Manage Checks With Terraform | Grafana Cloud Synthetic Monitoring

Published on 2026-02-24T16:19:03Z

## Description

Learn how to create, update and manage terraform synthetic monitoring checks in Grafana Cloud Synthetic Monitoring.

URL: https://www.youtube.com/watch?v=6DlLuuNcFqA

## Summary

In this video, Pakola, a senior developer advocate at Grafana, and Steven Shaw, a staff solutions architect at Grafana, discuss how to manage Grafana Cloud synthetic monitoring checks using Terraform, emphasizing the importance of managing these checks as code for scalability and consistency. They explain that Grafana Cloud synthetic monitoring allows users to run various checks to measure the performance of services, and demonstrate a typical workflow involving creating a synthetic check in the Grafana UI, configuring the Terraform provider, exporting the check to Terraform, and managing updates through Terraform commands. Steven provides a hands-on example of setting up and modifying synthetic monitoring checks using Terraform, illustrating how to deploy and update configurations effectively. The video concludes by encouraging viewers to explore further resources on Grafana synthetic monitoring and Terraform.

## Chapters

Sure! Here are the key moments from the livestream along with their timestamps:

00:00:00 Introductions to the hosts and the purpose of the livestream  
00:01:30 Overview of Grafana Cloud Synthetic Monitoring and its importance  
00:03:15 Explanation of managing synthetic checks as code with Terraform  
00:04:45 Common Terraform workflow for synthetic monitoring checks  
00:06:00 Setting up the Terraform configuration and access token  
00:07:30 Overview of the Terraform provider and its configuration  
00:08:45 Viewing synthetic check details in Terraform HCL code  
00:10:00 Deploying synthetic monitoring checks using Terraform  
00:11:30 Managing updates to existing synthetic checks with Terraform  
00:12:45 Conclusion and resources for further learning about Grafana Cloud Synthetic Monitoring  

Feel free to adjust any descriptions if needed!

# Managing Grafana Cloud Synthetic Monitoring Checks with Terraform

Hi, I'm Pakola, a Senior Developer Advocate at Grafana. Today, I'm joined by Steven Shaw, Staff Solutions Architect at Grafana. In this video, we'll show you how to manage Grafana Cloud synthetic monitoring checks using Terraform, allowing you to manage your synthetic monitoring checks at scale.

## What is Grafana Cloud Synthetic Monitoring?

Grafana Cloud synthetic monitoring is a blackbox monitoring solution that lets you run checks, such as browser ping, DNS, and TCP checks, from globally distributed public probes or self-hosted private probes. This enables you to proactively measure the availability, latency, and correctness of your services. 

As teams scale, managing synthetic checks manually in the UI can become difficult and error-prone. Many teams move to managing checks as code, ensuring updates stay consistent across environments, scale more easily, and are simple to track and review over time. While tools like Grizzly or Grafana CLI can help manage checks at scale, Terraform is Grafana's recommended approach.

Terraform allows you to define synthetic checks in configuration files instead of clicking through the UI. You can also make your checks versioned, reusable, and easy to maintain by managing them as code with Grafana. This provides a consistent, scalable, and repeatable foundation for synthetic monitoring as your system grows.

## Common Terraform Workflow for Synthetic Monitoring Checks

A common Terraform workflow for synthetic monitoring checks looks like this:

1. **Create a synthetic check in Grafana UI.** This helps validate the configuration and generate the required API keys.
2. **Configure the Terraform provider.** This tells Terraform which Grafana Cloud stack to manage.
3. **Export the check to Terraform.** Once exported, the check becomes a Terraform resource that you can modify and reuse.
4. **Manage and deploy updates using Terraform.** From this point forward, Terraform becomes the source of truth for modifying and managing checks.

Now, I'll pass it over to Steven to walk through deploying and managing these checks with Terraform.

## Deploying Synthetic Monitoring Checks

Steven: "Here you can see I have this synthetic check. It's checking this endpoint that is failing about 10% of the time, which is evident here. Now, I want to set up my Terraform config so that this becomes part of my Terraform deployment instead of being done via the UI.

The first thing we need to do is go into the synthetics config and set up an access token. You can click on 'Generate Access Token,' and it will provide a token you can use. 

We also need the API endpoint that we want to use in our Terraform provider. I've already included these in my Terraform config, along with a TF vars file, which defines the URL (that is, the hostname) and the access token. 

You can see here that I've commented out the usual URL and access lines you would put in for a Grafana Terraform provider for other Grafana resources. However, for synthetic monitoring, it has its own API and URL.

Now that that's in place, I can initialize my Terraform provider, which I've already done. Let's look at the Terraform content itself. 

To get what this check looks like in Terraform content, we go back to the config and look at Terraform. We want this in HCL because that's the format Terraform uses natively. I am going to scroll down to find my check. 

This is what it looks like in Terraform HCL code. I can take that and put it into my checks Terraform file, which I've already done. I've made a few changes. I decided to keep the test check so I can play with it or delete it as needed. 

Now, I am going to start deploying the checks that I really want based on that test. Here you can see I've got one for my dev team at a 40% fail rate, and another for my security team at a 20% fail rate, using specific probes and methods to check if SSL is true, along with my frequencies and timeouts.

With this in place, let's deploy it. I’ll run `terraform apply`, and you can see that it's going to pick up and say, 'Yep, I have two synthetic monitoring checks that I need to deploy.' I’ll confirm, and it will go out and deploy them. If I go back to my checks and refresh, you'll see I have two new ones!"

## Managing Updates

Now that I have my state in my Terraform deployment, I can say, "Actually, this is for the dev 2 team, and I want it to run every 2 minutes." Let's do that, and I want this one to have a timeout of five seconds. 

There are several other parameters available; feel free to check out our Grafana Terraform provider documentation specifically for the Grafana synthetic monitoring check resource. You can define various aspects depending on the type of check.

We are modifying the dev synth one. Currently, it has a 60-second frequency and a team of dev, which we're switching to dev 2. I’ll run another `terraform apply`, and it will show me the differences. It will indicate that the frequency is changing, the labels are changing, the timeout is changing, and the other one is fine.

After confirming the changes, if I refresh, the dev monitor will now reflect the changes: it becomes dev 2 with a 120-second frequency, showing all the changes we've made.

## Conclusion

There you have it! You now know how to export synthetic monitoring checks from the UI, manage, and update them as code using Terraform. 

For more examples of Grafana synthetic monitoring configuration management resources, including DNS, HTTP, and other checks, please check out the Grafana Terraform provider documentation. To learn more about Grafana Cloud synthetic monitoring, be sure to explore the Grafana documentation linked below.

If this tutorial was helpful, please make sure to hit the subscribe button and the like button for more Grafana synthetic monitoring content. I'll see you in the next video!

## Raw YouTube Transcript

Hi, I'm Pakola, a senior developer advocate at Graphfana. And today I'm joined by Steven Shaw, staff solutions architect at Graphana. In this video, we'll show you how to manage Graphana Cloud synthetic monitoring checks using Terraform so you can manage your synthetic monitoring checks at scale. Before we dive in, let's quickly cover what Graphana Cloud Synthetic Monitoring is. Grafana Cloud synthetic monitoring is a blackbox monitoring solution that lets you run checks such as browser ping, DNS, and TCP checks from globally distributed public probes or self-hosted private probes to proactively measure the availability, latency, and correctness of your services. As teams scale, managing synthetic checks manually in the UI becomes difficult and errorprone. Many teams move to managing checks as code so updates stay consistent across environments, scale more easily and are simple to track and review over time. While tools like Grizzly or Graphana CLI can help manage checks at scale, Terraform is Grafana's recommended approach. Terraform lets you define synthetic checks in configuration files instead of clicking through the UI. You can also make your checks versioned, reusable, and easy to maintain by managing checks as code with Graphana. This provides a consistent, scalable, and repeatable foundation for synthetic monitoring as your system grows. A common Terraform workflow for synthetic monitoring checks looks like this. Create a synthetic check in Graphana UI. This helps validate the configuration and generate the required API keys. Configure the Terraform provider. This tells Terraform which Graphana cloud stack to manage. Export the check to Terraform. Once exported, the check becomes a Terraform resource that you can modify and reuse. Manage and deploy updates using Terraform. From this point forward, Terraform becomes the source of truth for modifying and managing checks. I'll pass it over to Steven to walk through deploying and managing these checks with Terraform. >> Here you can see I have this synthetic check. Uh it's checking this endpoint that is failing about 10% of the time. And you can see that's happening here. So now I want to set up my Terraform config so that this becomes part of my Terraform deployment instead of being done via the UI. So first thing we need to do is we need to go into synthetics config and we need to set up an access token. So here you can click on generate access token which I'm not going to show but if you click on it you'll get a token you can use. Uh and the other thing we'll need of course is specifically the API endpoint that we want to use in our Terraform provider. So I've put these already into my Terraform config and uh I have a TF vars file for those of you familiar with Terraform and these define the URL which is that host name and the access token. And you can sort of see here I I commented these ones out. These are the usual URL and O lines you would put in for a Granana Terraform provider uh for just other Graphana resources. But for synthetic monitoring, it has its own API and uh URL. Okay, own API access and URL. So this is what the provider looks like. I've got my TF vars uh variables in there. So that's all set. So now uh that that's in place, I can initialize my Terraform provider, which I've already done. And we can actually go and look at the Terraform content itself. So how do I uh get what this check looks like in Terraform content? Well, that's where we go back to config and we look at Terraform. Uh, we want this in HTL because this is the format the Terraform uses natively. And I'm going to scroll down here to find my check. Looks like it's this one right here. Oops. Let's grab this. Right. And this is what it looks like in Terraform HCL code. So now I can take that and put it into my checks. Terraform file, which I've already done. Um, but I've made a few changes. You know, I actually decided, you know what? I'm going to keep that test one and so I can play with it or delete it or do whatever I want. And now I'm going to start deploying the checks that I really want based off of that test one. So here you can see I've got one for like my dev team uh at a 40% fail rate. And I've got a security team one at 20% fail rate using specific probes using specific methods checking to see if SSL is true you know my frequencies my timeouts right so with this in place let's deploy it so here I'm going to go terraform it okay terraform apply and you can see that it's going to pick that up and say yep I've got two uh synthetic monitoring checks that I need to deploy and I'm going to create two of them. So, I'll say yes. I'll go out and deploy them. And now, if I go back to my checks and refresh this, you'll see, oh, I've got two new ones. And there they are. >> With the checks deployed, let's pass it back to Stephen to show you how to manage updates. Now that I have my state in my Terraform deployment, I can say uh yeah, actually this is um for the dev 2 team, let's say, and I actually want it to run uh every 2 minutes. Let's do that. And I want this one to have a timeout of five, right? And there's a bunch of other parameters here. Feel free to look at our Graphana Terraform provider documentation uh specifically for the Graphana synthetic monitoring check resource and you can define all sorts of things depending on the type of check etc. Okay, so we're modifying the dev synth one. So we can see here that it's a 60-second frequency. It's got a team of dev which is going to switch to dev 2. All these wonderful things. So now if I do another Terraform apply, it'll show me the difference. It'll say yeah I see that your frequency is changing. Um, your labels are changing, your timeout's changing, and the other one's fine. So, I'm not going to change it. We say yes. And now, if I refresh this, the dev monitor now becomes dev 2. It's 120 second frequency. You can see all the changes that we've we've made. Right? >> There you have it. You now know how to export synthetic monitoring checks from the UI, manage, and update them as code using Terraform. For more example of Graphfana synthetic monitoring configuration management resources, including DNS, HTTP, and other checks, please check out Graphana Terraform provider documentation. To learn more about Grafana Cloud synthetic monitoring, be sure to explore the Graphana documentation linked below. If this tutorial was helpful, please make sure to hit the subscribe button and the like button for more Graphana synthetic monitoring content. And I'll see you in the next video. [music] >> [music]

