# Git Sync: Observability as code built for scale | Demo | Grafana Labs

Published on 2026-02-05T15:54:40Z

## Description

In this video, Fabrizia Rossano and Roberto Jiménez demonstrate Git Sync, a feature that provides you with the power of Git ...

URL: https://www.youtube.com/watch?v=gjhmarpMPCY

## Summary

In this video, Fabitzia and Roberto introduce Gitsync, a new feature in public preview for Grafana that allows users to combine code editing and dashboard management in a seamless way. They explain that Gitsync enables users to connect Grafana to GitHub, making it easier to edit dashboards in the UI while maintaining version control and traceability of changes. The video includes a demo by Alberto showcasing how to set up Gitsync, synchronize dashboards, and create pull requests directly from Grafana. Key points include the integration of GitHub apps, improved onboarding experiences, and the ability to visualize changes through screenshots in pull requests. The presenters also discuss the limitations of the public preview, highlighting areas for future development before general availability.

## Chapters

Sure! Here are the key moments from the livestream along with their timestamps:

00:00:00 Introductions to Gitsync public preview  
00:01:30 Overview of Gitsync's features and benefits  
00:03:15 Explanation of the public preview status  
00:04:00 Connecting Grafana to GitHub  
00:05:30 Demo: Synchronizing dashboards from GitHub to Grafana  
00:07:00 Configuring repository settings in Grafana  
00:09:15 Creating a new dashboard using Gitsync  
00:10:45 Opening a pull request for the new dashboard  
00:12:30 Editing an existing dashboard and opening another pull request  
00:14:00 Discussion of limitations in the public preview  

Feel free to ask if you need more details!

# Gitsync Public Preview Overview

Hi, I'm Fabitzia, and alongside Roberto, I'm here to guide you through the **Gitsync public preview**. We’ll cover what it is, how it works, what's included, and we'll follow with a demo as well as discuss the main limitations.

## Introduction to Gitsync

Until now, there was no way to combine the perks of working with code with the great user experience of editing dashboards in the UI and seeing the results immediately. At scale, using the Grafana UI often led to untracked changes. This is why many users decided to limit this feature in favor of editing code, which had its own challenges, such as complex setup and difficult integration. Moreover, it lacked a fast feedback loop for changes.

Basically, you could either work with code or in the UI, but not both. Grafana's answer to the trade-off between ease of use and reliability is **Gitsync**. With this feature now rolling out in public preview for all users, you can combine the simplicity of editing dashboards in the Grafana UI with the assurance that your dashboards are stored in a remote repository, allowing you to always know when and who changed them.

## Public Preview Details

I mentioned that Gitsync is now in public preview. This means it is enabled by default in all of our cloud instances, and users can freely utilize it. However, features in public preview are not meant for production environments and are intended for early adopters. That said, it can be enabled and used by our entire user base.

This preview focuses on delivering the core Git workflow. You can connect Grafana to GitHub using either a personal access token or the GitHub app. You can make edits in the UI, commit those changes, and open requests all in one seamless flow. Pull requests include previews and context, allowing reviewers to see what changed before merging.

We've also improved the setup and save experience based on lessons learned from the private preview. The goal is to provide a much smoother onboarding and review process for teams experimenting with dashboards as code. Additionally, we have improved the post-configuration checks and the information we provide during the pull process.

If you're interested, try it in Grafana Cloud and let us know your thoughts. Now, let’s move on to Alberto's demo.

## Alberto’s Demo

Thank you! Hi folks, I'm going to show you what we've built over the last 12 months to make using dashboards as code seamless in Grafana. For this, I have prepared an empty Grafana instance and a repository.

If I go to the terminal, you will see that it contains a bunch of dashboards stored as JSON. I want to bring them into Grafana using Gitsync. 

1. **Configuring Gitsync**: 
   - Go back to Grafana and navigate to the general provisioning section. You will find a new section for Gitsync.
   - You can connect using a GitHub app or a personal access token. The preferred option is the GitHub app, which is more secure. 
   - Once connected, select your repository (in this case, `grafana-manifest-experiments`), choose the main branch, and specify the path within the repo where all your dashboards will be stored.

2. **Synchronizing**: 
   - After making those selections, click "synchronize." After a few seconds, you will see a summary of how many files are in the specified location, and the synchronization process will begin.
   - A progress bar will indicate the system has created multiple folders and dashboards.

3. **Additional Settings**: 
   - You can configure additional settings, such as making the repo read-only or enabling the pull request flow, allowing everyone to create pull requests. You can also decide whether to display screenshot previews of the dashboards before and after changes.

4. **Creating a Dashboard**: 
   - Now, let’s create a dashboard from the Grafana UI. Go to "New Dashboard," add a visualization panel, and save it.
   - You'll be prompted to select a title, a description, and the folder (synchronized folder) where the file will be created. You can also add a comment for the commit, which is optional but recommended.

5. **Opening a Pull Request**: 
   - Click on "Open Pull Request" on GitHub. After a few seconds, Grafana integration will post a comment with a preview of the changes.
   - You can edit the dashboard directly, create another commit, and see the updated version.

6. **Merging the Pull Request**: 
   - Once you're satisfied, merge the pull request. Going back to Grafana, you will find your new dashboard there.

7. **Editing the Dashboard Again**: 
   - You can modify the dashboard, push changes to a new branch, and open another pull request. The system will post a comment with screenshots comparing the dashboard before and after changes.

8. **Finalizing Changes**: 
   - Merge the pull request again, and you’ll see the updated dashboard in Grafana without needing to refresh.

## Limitations of the Public Preview

Now that we've looked at the capabilities of this feature, let’s discuss the limitations of the public preview. As you know, public preview is the last milestone before general availability, and we have a few things to implement before reaching GA:

- There are limitations regarding changing folder permissions after synchronization.
- Support for other resources besides dashboards and folders is currently limited.
- The ability to synchronize the full instance has been removed because not all resources are available in folders as syncable within this feature.

All limitations are fully documented on our website, alongside the rest of the feature documentation.

Thank you for your attention, and we look forward to your feedback!

## Raw YouTube Transcript

Hi, I'm Fabitzia and alongside Roberto, I'm here to walk you through Gitsync public preview. What it is, how it works, what's included, and followed by a demo and the main limitations. Until now, there was no way to combine the perks of working with code with the great user experience of editing dashboards in the UI and seeing the results immediately. At scale, using Graphana UI often led to untraceed changes. This is why many user decided to limit this in favor of as good editing. But that had its own challenges like complex setup and difficult integration. Not to mention the inability to have a fast feedback loop of your changes. Basically, you could either work as code or in the UI, but no, both. Graphana. Answer to the trade-off between ease of use and reliability is Gitync. With this feature now rolling out in public preview for all users, you can combine the simplicity of editing dashboards in Graphana UI with the knowledge that your dashboards are stored in a remote repository and you can always know when and who changed them. I mentioned that GitSync is now in public preview. What it means is that is now enabled by default in all of our cloud instances and people can freely use it. However, features in public preview are not meant to be used in production environments and are intended for early adopters, but can of course be enabled and used by all of our user base. This preview is focused on delivering the core Git workflow. You can connect Rofana to GitHub with either a personal access token or the GitHub app. Make edits in the UI and from the save drawer, commit those changes and open up request all in one seamless flow. PR include previews and context so reviewers can see what changed before merging. We've also iterated on the setup and save experience based on lesson from private preview. The goal being a much smoother on boarding and review process for team experimented with dashboard as code. And we did not forget the admins as we also improved the post configuration checks and the information we provide during the pool process. If you're interested try it in Grafana Cloud and tell us what you think. And now it's time for Alberto's demo. >> Thank you for hi folks. I'm just going to show you like with built uh in the last bus uh 12 months to to make using das as code seamless at graphana. For that I have prepared like an empty uh graphana d uh instance and a repo. So if I go to the terminal you will see like that it has like content has like a bunch of like dashboards stored as JSON uh simply as JSON and I want to bring them um to graphana. So that will be bringing both things together and for that let's just try to use gitsync. So if you go back to graphana and then go to uh general provision it you'll have like a new section uh for gits sync we go and configure like a repo and we have two options now so you can connect with a github app or you can connect with a personal access token like prefer option is more secure it's the github app brand new feature so we click in connect and then um yeah the UI will tell us okay do you want to connect with new AB. So, I have created one myself. I'm going to just fill it up with this um with this little plugin and going to put my private key on this and configure the repo. Right. So now I can go in the next page and select my repo which in this case is graphana manifest experiments and yeah you will see any other repos that you have access to and then you select the branch main in this case and you can select even like a pathold in the repo where all your dashwords will be stored as sub directory. Once you have made like the decision for those three things, you go to synchronize um to the next step and after waiting couple of seconds, we will be presented with basically like a summary of how many files you have in that location in particular in the stial location and that we will bring them over to a specific graphana folder um with the name that you pick up there. So once you make that decision clicking syncs with the standard storage and reading all this um we will begin the synchronization process um will be a progress bar and here you will see that um the system has created five folders in total but I go to my repo and 22 dashboards. So yeah and you can go see the the repo. If you click on that particular link we put like a lot of hooks like that in the UI. We click in additional settings. You can make a couple of decisions as well. If you want like this rele to be read only or if you want to enable the pull request flow that forces like everybody or like allows everybody to create pull request and enable push to to the main branch and also um deciding if you want like the pull request to um display some screenshot previews of the dashboards the changes before and after. So we are going to select it for the demo purposes and you clicking finish and we are going to just be redirected to the repository listing page in the admin page of of provisioning and you will see there this is our repo connection um profana manifest permit with the dashboards and folders that we we saw before. You can go to the BU page, the repository status page, and you're going to have a statistics about like how many resources have you created like the health of that connection history of all the the pooling and synchronization jobs and the counts. This this was the initial one in particular. And then you can also like see what is the web hook that we created in the repo in the GitHub repo for things to be more instantaneous. And also you can trigger like a manual manual pool job. So just going to click it here and you will see yeah we we have no changes at all. Like I said before you can go back to the source code at any point in different parts of the UI. And here like this tab is like the resources tab where will you see basically a list of the files and the corresponding graphana resources that we created. You can see them insisting in graphana or going back to the source code. But let's go to the dashboards page again and see that right now we have like this folder that I mentioned that it's going to contain everything uh from the repo. So let's just click in the first one and you will see like yeah the password is here and there like a couple of interesting things about this one in particular. So there is like this little uh provision batch that is going to tell you that this is being managed by the repo connection that we created and there is also like a source link here that if you click it you just basically see the the source code directly in GitHub. So this little pop-up window, you'll see the code. And like I said, we put like multiple of these things uh within the the whole UI. But anyhow, let's go and create a first dashboard uh as code from Graphana UI. Uh this is the interesting one. So you don't do it as a JSON. You just go okay. What you normally do, new dashboard, add a visualization panel, select it. I don't care, right? Just save it. And this part is different. So this part is going to se let you select the title. So my first dashboard here using it sync uh description and this is what it was like before. But now you're going to select the folder which in this case is the synchronized folder and the path within the repo. So you can put like a specific path there and is where the file will be created. A comment for the comet that we're going to create. It's it's actually optional but highly recommended and maybe we make it like mandatory at some point and you have options to push to any of the existing branches including main branch directly if that is something that is allow for your instance or push into a brand new branch. Let's go with a new branch and yeah clicking on save as you did before and now the UI is going to show like this banner that is going to tell you something very interesting that is basically that this resource has been created in a branch in GitHub but it doesn't exist in graphana yet until you don't merge it to main to get that you will have to open a pull request and for that you have like this action button open pull request on GitHub let's go and do add and yeah I just add in my first dashboard. This is my first dashboard. Uh put it like a pull request description. create a pull request and if you wait a couple of seconds, then our Grafana integration will put a comment um with a preview of what you just said. And it also gives you like a link back to Graphana if you want to tweak it. If you want to do something about it, you can always go there, create a commit. Uh so edit again, create another commit and uh see the updated version. But the thing is okay. So we're just going to go and and basically merge um this one. So merging the pull request and yeah it's merge. So let's go back to Grafana and I go to dashboards and if I refresh I will see I have my new dashboard there. It didn't exist before. So this is as code with the source link as we said before. But now let's even like edit that again. So that you get into the the flow. So let's just modify and expand this panel as an example and change the name to put whatever random name with new name. So we push to a new branch as we did it before open another pull request. Yeah, we just click here open pull request and yeah um and I'm going to put the description this time. Just going to wait here for the comment and you will see then in just a few seconds again like it's sync the system Graphana will put another comment with uh the screenshots of the dashboard before I change that panel and after so you can um quickly compare the like visually like that is important thing like you don't want to spend all the time just looking at JSON files you want things visual because we find it's like very visual product so um again have like privilege things. So we go back and we see that when we merge like it's still like without merging and this dashboard is not precise. So let's merge and go back to graphana and is resized. So I didn't even have to refresh this time. So we're going to basically go back to the admin page in provisioning and you will see we have 23 dashboards right now [snorts] and the history of jobs. It has like information about these recent merges. uh where we updated one of the dashboards and also the pull request comments that we put like you will see there what is the pull request in question where we put a comment and there is where you will have the whole history and you can see those those things and that's about it that is the main thing um you're going to be able like to submit changes like very seamlessly from graphana UI as code back to you for it >> now that we've looked at the capabilities of this feature. Let's take a look at the limitation of this public preview. As you know, public preview is the last milestone before general availability and we have a few things that we will implement before reaching GA. We have some limitation about changing folder permissions after the synchronization happens and other around support for other resources than dashboards and folders. We also have removed the ability to synchronize the full instance as this is directly connected to not having all the resources currently available in folders as syncable within this feature. All limitations are fully documented in our website alongside the rest of the feature documentations. Thank you and see you around.

