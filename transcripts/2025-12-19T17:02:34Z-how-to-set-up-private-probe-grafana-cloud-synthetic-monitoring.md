# How to Set Up Private Probe | Grafana Cloud Synthetic Monitoring

Published on 2025-12-19T17:02:34Z

## Description

Learn how to set up a private probe using Grafana Cloud Synthetic Monitoring. In this video, we walk through the steps you need ...

URL: https://www.youtube.com/watch?v=iSJtYa-MZq4

## Summary

In this video, Bakola, a senior developer advocate at Grafana, and Steven Shaw, a staff solutions architect at Grafana, provide a tutorial on setting up and running a private probe using Grafana Cloud Synthetic Monitoring. They explain that Grafana Cloud Synthetic Monitoring is a blackbox monitoring service allowing users to conduct checks for availability and performance from both public and self-hosted private probes. The video outlines the process of deploying a private probe, which is crucial for monitoring services that aren't publicly accessible, and details the steps involved, including deploying the probe via Kubernetes and configuring monitoring checks. Steven demonstrates the deployment process, including creating necessary secrets and configuring checks for endpoints within a private network. The video concludes with a recommendation to create multiple probes for redundancy and encourages viewers to explore Grafana's documentation for further learning.

## Chapters

Here are the key moments from the livestream along with their timestamps:

00:00:00 Introductions and overview of the livestream  
00:01:15 What is Grafana Cloud Synthetic Monitoring?  
00:02:30 Explanation of public vs. private probes  
00:03:45 Overview of the steps to create a private probe  
00:04:20 Step one: Deploying a private probe using Kubernetes  
00:05:50 Demonstration of creating a private probe in the Grafana interface  
00:07:10 Setting up secrets for the private probe deployment  
00:08:30 Checking the status of the deployed private probe  
00:09:15 Step two: Configuring checks using the private probe  
00:10:50 Recommendations for multiple probes and high availability  

These timestamps should help viewers navigate through the important sections of the livestream effectively.

# Setting Up a Private Probe with Grafana Cloud Synthetic Monitoring

Hi, I'm Bakola, a Senior Developer Advocate at Grafana, and today I'm joined by Steven Shaw, Staff Solutions Architect at Grafana. In this video, we'll show you how to set up and run a private probe using Grafana Cloud Synthetic Monitoring.

## What is Grafana Cloud Synthetic Monitoring?

Before we dive into private probes, let's quickly cover what Grafana Cloud Synthetic Monitoring is. Grafana Cloud Synthetic Monitoring is a blackbox monitoring service that lets you run checks such as browser, ping, DNS, and TCP checks from globally distributed public or self-hosted private probes. This allows you to proactively measure the availability, latency, and correctness of your services.

In Grafana Cloud, there are two types of probes:

- **Public Probes**: Managed by Grafana and available globally.
- **Private Probes**: Deployed by you.

A private probe is a self-hosted agent that runs inside your network, executes the checks you configure, and reports results back to Grafana Cloud. This provides you with the same visibility for your private services as you have for your public ones. 

Private probes are useful for services that aren't publicly accessible, such as:
- Private networks
- Internal APIs
- Staging environments
- Services behind authentication
- Endpoints restricted by IP whitelists or firewalls

## Steps to Create and Run a Synthetic Monitoring Check with a Private Probe

There are two key steps to creating and running a synthetic monitoring check with a private probe:

1. **Deploying the Private Probe**: You can deploy a private probe using Kubernetes, Docker, Ubuntu, Debian, or other supported environments. Please check the documentation for code samples.

2. **Configuring the Synthetic Monitoring Check**: This is done with the private probe you set up in step one.

### Step 1: Deploying a Private Probe

I'll now pass it over to Steven, who will walk you through step one—deploying a private probe on a Kubernetes cluster.

---

**Steven**: To start, we're going to look at the steps in our documentation on how to deploy the synthetic monitoring agent for a private probe with Kubernetes. We have a bunch of manifests that we're going to copy down and examine. 

First, we need to create a private probe. On the probes page, we can see all the public probes available. The reachability only shows on probes that currently have checks, while those not in use say "N/A." We want to add a private probe.

To do this, we click on "Private Probe." I'll name this "test probe" and enter location information to ensure it appears correctly on the map. You can also add custom values and labels, which are helpful if you have many private probes. 

Once we have this set up, we register the probe. After adding it, I receive a one-time token and the server location to register with. We will put this information into our secret. Normally, you would do this with pass-through environment variables, which is a better practice than placing tokens directly in a YAML file. 

Now, let’s deploy the secrets and the deployment. Once I hop over to my Kubernetes cluster, I can see the namespace and that the agent is already running. Everything looks good, and it seems to be registered and operational.

---

### Step 2: Configuring the Checks

With the private probe deployed and running, we can now move on to step two: configuring our checks. 

**Steven**: Now, if I go back to my probes list, I should see "test probe." Although I picked the wrong region, that’s just a label. It’s up and running, and I can configure checks to access endpoints on my private network in the Kubernetes cluster.

Let’s do a ping check against another host that is not accessible from the public internet. In the execution section, we see all our public probes, but we also have the private probe listed. I want to use that one and set it to run every 10 seconds for visibility. I don’t need alerts right now.

Now our check is active, and it’s already successfully pinged the local IP address. Over time, we will see error rates and response times populate. 

We generally recommend creating more than one probe. If a probe goes down or there’s a network issue, having at least three probes can help prevent flapping alerts or false positives. 

Because we deployed the private probes in Kubernetes, we don't necessarily have to do multiple deployments. We can increase the number of replicas in the deployment to make it highly available, and they will all register as the same probe on the Grafana Cloud Synthetic Monitoring site. 

However, separate deployments would be needed if you wanted additional probes from different locations within your private network.

---

## Conclusion

There you have it! You now know how to set up and run a private probe check using Grafana Cloud Synthetic Monitoring. Check out Grafana Play Synthetic Monitoring to see a dashboard with a variety of running checks. 

If you want to learn more about Grafana Cloud Synthetic Monitoring, please refer to the documentation. If this video was helpful to you, please like the video and subscribe to learn more about Grafana Cloud Synthetic Monitoring. 

I’ll see you in the next video! 

--- 

*[music]*

## Raw YouTube Transcript

Hi, I'm Bakola, a senior developer advocate at Grafana, and today I'm joined by Steven Shaw, staff solutions architect at Graphfana. In this video, we'll show you how to set up and run a private probe using Graphana Cloud synthetic monitoring. Before we dive into private probes, let's quickly cover what Graphana Cloud Synthetic Monitoring is. Graphana Cloud Synthetic Monitoring is a blackbox monitoring service that lets you run checks such as browser, ping, DNS, and TCP checks from globally distributed public or self-hosted private probes to proactively measure the availability, latency, and correctness of your services. In Graphana Cloud, there are two types of probes. Public probes, which are managed by Grafana and available globally, and private probes, which you deploy yourself. A private probe is a self-hosted agent that runs inside your network, executes the checks you configure, and reports results back to Graphfana Cloud, which gives you the same visibility for your private services as your public one. Private probes are used for services that aren't publicly accessible, such as private networks, internal APIs, staging environments, services behind authentication, or endpoints restricted by IPO list or firewalls. There are two key steps to creating and running a synthetic monitoring check with a private probe. Step one is deploying the private probe. You can deploy a private probe using Kubernetes, Docker, Ubuntu, Debian, or other supported environments. Please check the documentation for code samples. Step two is configuring the synthetic monitoring check with the private probe you set up in step one. I'll now pass it over to Steven who will walk you through step one, deploying a private probe on a Kubernetes cluster. So to start uh we're going to look at the steps here in our documentation on how we deploy the synthetic monitoring agent we call it for a private probe with Kubernetes. So we have a bunch of manifests here. We're just going to take these and copy them down and then we're going to look at these manifests to see what's in here. And we have a namespace, we have a secret and we have the deployment of the actual pod itself. Now as part of this uh we need to pull in some secrets. So, I'm going to go grab this now. So, the first thing we need to do is we need to create a private probe. So, on the probes uh page here, we can see all the public probes that are available. And you'll notice that the reachability only shows on probes that currently have checks. So, it's actually showing like the summary of your checks on each probe. So, for those you aren't using, they'll say NA. But, we want to add a private probe. So, to do this, we click this here, private probe. I'm going to call this test probe. And you can put in location information so it shows up on the map correctly. Um, you know, there's like a region that you can put in. You can also do custom values and custom labels as well. These are usually helpful when you have a lot of private probes. Um, so just something to keep in mind. Uh, and then really all we need to do now is register this thing. So you can see once I add this probe, I will get my one-time token and the the server location I should register with. So, we're going to put this information into our secret. Now, normally you would do this with pass through environment variables and and far better than this. This is just for demo purposes so you can see what I'm doing. Uh, please don't put your tokens into a YAML file. That is generally a bad practice. So, let's get these into our secret. Okay. And now we're going to deploy those. So, get the nameace out there. We're going to do the secrets. I'm doing these one at a time so you can see what I'm doing. And then uh the deployment. Okay. And now if I hop over to my Kubernetes cluster, I can see I've got the namespace. Uh there's the agent. It's already running. Uh everything looks good and it looks like it's registered and it's up and running. >> With the private probe deployed and running, we can now move on to step two, which is configuring our checks. Let's pass it back to Stephen to show how to configure your checks using private probes. >> So now if I go back to my probes list, I should see there you go. Here's test probe. And clearly I picked the wrong region, but that's fine. It's just a label. And it's up and running. And now I can configure checks to access endpoints that are on my private network in my Kubernetes cluster. So let's go do that. We're going to do a um DNS or sorry a ping check against another host that is not accessible from the public internet. And this all looks good. Now in the execution section, you can see we have all of our public probes still, but we also have a private probe. And I want to use that one. So let's do that. I'm going to have it go every 10 seconds just so we can see it quickly. I don't need alerts right now. All right. So now our check is here and we're running. So you can see it's already uh it's already successfully pinged it. If I look at this here, we can see that uh it did a ping check against that local IP address and uh that resolved via DNS and everything looks good. And what you'll actually see is over time you'll see um any error rates or response and all that kind of stuff as this populates as well. We do generally recommend however that uh you create more than one probe uh because let's say a probe goes down or there's a network issue. Just like with our public probes, we generally recommend at least three if you can to prevent flapping alerts or uh network events from giving you false positives. It's also worth noting later on that because we deployed the private probes in Kubernetes, we don't necessarily have to do multiple deployments. um we can just increase the number of replicas that we have in the deployment and then make it highly available and they all register as the same probe on the graphana cloud synthetic monitoring site. Really, it would be separate deployments if you wanted additional probes from different locations within your private network. >> There you have it. You now know how to set up and run a private probe check using Graphana Cloud Synthetic Monitoring. Check out Graphfana Play synthetic monitoring to see a dashboard with a variety of running checks. If you want to learn more about Grafana Cloud synthetic monitoring, make sure to check out this documentation. If this video was helpful to you, please make sure to like the video and subscribe to learn more about Graphana Cloud synthetic monitoring. And I'll see you in the next video. >> [music]

