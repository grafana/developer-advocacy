# Git Sync: GitLab, Bitbucket, and universal provider support

Published on 2026-02-25T17:02:50Z

## Description

In this video, Roberto Jiménez, Staff Software Engineer at Grafana Labs, shares that Git Sync is expanding beyond GitHub to ...

URL: https://www.youtube.com/watch?v=JORGkmhc8pQ

## Summary

In this video, Giten announces the expansion of their service to support multiple Git providers, including Bitbucket and GitLab, in addition to GitHub. The presenter describes the implementation in two layers: a "pure git" solution that is agnostic and utilizes the standard Git HTTP protocol, and an enhanced layer for specific providers that integrates with their APIs for a more seamless experience. The demonstration showcases how to connect a local repository, synchronize files, and perform actions such as modifying dashboards, pushing changes, and opening pull requests across different Git platforms. The main points highlight the new universal support for Git providers and the ease of managing repositories from various sources within Giten's interface.

## Chapters

00:00:00 Introductions and announcement of new features  
00:01:15 Explanation of universal support for Git providers  
00:02:00 Overview of the two-layer integration system  
00:03:30 Demonstration of connecting to a local repository  
00:04:15 Successful synchronization of files and folders  
00:05:00 Modifying a dashboard and pushing changes  
00:06:00 Demonstrating the pull request process  
00:07:30 Merging a pull request to complete the cycle  
00:08:00 Overview of enhanced integrations for different providers  
00:09:00 Final thoughts and summary of features available

# Giten Expands Beyond GitHub

Hey there! I'm excited to share that Giten is expanding its support beyond GitHub. Since we presented this feature at Grafana, the feedback has been overwhelmingly positive. Many people expressed their love for the feature, but some mentioned that they were using Bitbucket or GitLab and asked when we would add support for those platforms. 

## Universal Support for Git Providers

I'm happy to announce that we are adding **universal support for Git providers**. Here’s how it works:

### Two Layers of Implementation

1. **Pure Git Layer**: 
   - This is a provider-agnostic solution that uses the standard Git HTTP protocol. In a nutshell, if your repository speaks Git, we will be able to sync with it.

2. **Enhanced Providers Layer**: 
   - This layer includes specific integrations for providers such as GitHub, Bitbucket, and GitLab. These integrations require extra work with provider-specific APIs and UIs, aiming to create a more seamless experience between systems. This includes smoother pull requests and better handling after merges.

## Demonstration

Without further ado, let's see it in action! When you now open the Giten synchronization admin page, it will look a little different. You will see the integrations for enhanced providers like GitHub, GitLab, and Bitbucket, alongside the new pure Git configuration.

### Connecting to a Local Repository

I have prepared a local repository with a bunch of dashboards. Let's connect to it. Just like any other repository, I enter my username and password, select the branch, and it informs me that I have 22 files to sync. 

Upon clicking **Connect**, the synchronization begins, and it successfully syncs the 22 files and folders. Now I can open the source files. As we can see, we've successfully pulled a lot of resources from my local repository running alongside Grafana. 

If I go to the folders, I can utilize the same features I would use for GitHub. For example, I can modify one of the dashboards, push it to the main branch, and if I go back to the repository in Giten, I can refresh to see the commit I just pushed.

### Submitting a Pull Request

Now, let's edit the dashboard and submit a pull request using the pure Git integration. The process is straightforward: we modify the dashboard, select or create a new branch, and write a commit message. After clicking **Save**, I hit the option to open a pull request. This will be my first pure Git pull request.

Let’s merge it to close the cycle. That’s the main flow! You have the same features as you saw in GitHub.

### Enhanced Integrations

If we go back to the Giten admin page, we can now explore the enhanced integrations. I created several, including those for Bitbucket, GitLab, and GitHub. 

In the dashboards, you will see that I have all those repositories from various providers synchronized at once. Let’s pick Bitbucket and open a pull request in the same manner as we did with the pure Git. 

### Conclusion

This is the basic idea! Now, when you go to the Giten admin page, you have access to all those providers alongside universal provider support. Thank you for your attention, and I look forward to seeing how you utilize these new features!

## Raw YouTube Transcript

Hey there, Giten is expanding beyond GitHub. Since we presented this feature back at Grafana, the feedback that we got was pretty consistent. Like people were like loving it, saying this is great. But some of you were telling us directly, yeah, I I love it, but I'm using Bitbucket or I'm using GitLab. When will you add support for that? So, I'm happy to announce that we're adding universal support for Git providers. How does it look like? Uh we implement this in in two layers. The first layer is what we call pure git. It's a pro agnostic solution. It uses the standard g HTTP protocol and in a nutshell if it your repo speaks gana will be able to sync with it. On top of that layer we have the second layer that is going to be like the enhanced providers for example GitHub, Bit Buckhead or uh GitLab. those require extra integrations with the provider specific APIs or where the UIs and and the goal of that is to make the experience between systems a little more seamless. So pull request more seamless uh what happens after like a merge and without further ado let's see it in action when you open now get g get g get g get g get g get g get g get g get g get g get g sync like the admin providing page it's going to look a little bit different it's going to the integrations the enhance providers for github gitlab and bit bucket and alongside them there will be like the new pure git uh configuration let's try to use it and for that I have prepared like a a giga uh local repository here. Um it has like a bunch of dashboards. Go and and try to connect it with it. Um just like any other repo like username, password. I select the branch and it tells me I have like 22 files and I will going to put it to that folder. I'm just going to click connect. Begin synchronization. It has successfully synchronized 22 files and folders. So I finished the connection. And if you see I can open it it from here like from the source file. So we have successfully pulled a lot of resources as we can see in this page uh from a Gileia local repository running alongside my my local graphana. If I go to folders I can go and use the same features I use for GitHub. I can go to one of the dashboards and modify it. Push it to main. And now if you go back to to the repository in GIA um you will see that if you refresh it has the commit that I just push. Let's go and edit now and and try to submit like a pull request using this the spirit integration. So process is the same. We're going to just modify the dashboard and after we modify the dashboard we are going to select or like write like a new branch and put a commit message. Clicking save and clicking in the open pull request and I will going to open one and this will be my first pure git uh pull request opening with this. [sighs] Let's just merge it to close the cycle. But that is about it. That is the main the main flow. You can has the same features as as you you saw in GitHub. If you go back to the admin page of git sync and and let's look at like the enhanced integrations now I have for example I created a bunch of them and we have for bit bucket we have for for git multiple for gate this is the one that I created I have for gitlab and and github and if I go to dashboards you will see that I have all those repositories from all those providers synchronized at once um um let's pick one let's pick big bugget And let's open like a pull request with it. So like to new branch and so that you can trust me just save it as we did uh with a pure git first and let's open like a pull request for for bit bucket uh is in the same way. It's it's a new provider so you can trust me. But yeah that is that is the basic idea. Now that you go to get and and this admin page you have all those providers alongside the universal provider support.

