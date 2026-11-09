# What&#39;s New in Grafana 13.1: Git Sync — Easier Importants, Easier READMEs &amp; Signing

Published on 2026-06-24T21:07:41Z

## Description

Grafana 13.1 cuts down on GitOps pain by making Git Sync stronger — import dashboards to Git with a click, see your repo ...

URL: https://www.youtube.com/watch?v=IgCQHwAVxBU

## Summary

The show is titled "What's New in Grafana 13.1: Git Sync — Easier Imports, Easier READMEs & Signing," published on June 24, 2026. The speaker discusses the enhancements in Grafana 13.1, focusing on the Git Sync feature that simplifies managing dashboards as code. Key improvements include easier importing of dashboards into Git, automatic pull request creation, integration of README files from repositories into Grafana, and the ability to commit changes with verified signatures for enhanced security. These updates aim to streamline workflows and reduce the pain points associated with GitHub integration.

Topics: Grafana 13.1, Git Sync, dashboard management, README integration, commit signing.

## Chapters

00:00:00 Introduction to Git Sync in Grafana 13.1
00:01:32 Enhancements in Git Sync for Grafana
00:02:18 Git Sync commit signing options

Did you know we just removed a lot of GitHub's pain right inside Grafana? Let me show you.

You may or may not know, but in Grafana OSS and Cloud, we have a feature called **Git Sync** that lets you manage dashboards as code. This essentially means that changes you make to dashboards can flow both ways between Grafana and your Git repository. 

For example, you can see I have my **5Flow GitHub** repo syncing or provisioned in Grafana. When I look at the dashboards, you can see that this is bi-directionally reflected. In Grafana, and then also if I go into my code and look at the infrastructure and dashboards folder, you'll see that both of these are presented. 

Now, from the Git side, any changes you make, whether you update a title of a dashboard in the JSON or whatnot, will actually reflect as well in Grafana, hence the bi-directional nature.

In **Grafana 13.1**, we've made that workflow even stronger and improved some of the features in it. One thing is we made getting dashboards into Git a lot easier. If you go into your provision folder that has Git Sync enabled, you can actually go and import a dashboard. 

Let's say you have one as JSON locally; you can upload that JSON dashboard, click on your Git Sync enabled folder, and it will give you a unique identifier, a branch name, and a repo folder if you want to set one, maybe a subdirectory. You can import that, and it will actually open up a pull request. 

You can see a new resource has been created in a branch in GitHub. We can open that pull request, and you'll see that all the changes are reflected here. We can create the pull request, and then what we can even do is merge this. Once we merge it in, those changes will be reflected. There is a sync interval in Git Sync, and that will reflect.

What's pretty cool here is that we wanted to make it easier to keep documentation close to your dashboards. Now, your READMEs get pulled in from your repository to Grafana when Git Sync is linked to that folder. For example, if we look at the dashboards folder in GitHub, you'll see we have a README file, and now this is directly reflected in Grafana as well.

Finally, for teams with stricter security requirements, changes can now be committed with verified signatures. If you go into your general provisioning where Git Sync is enabled, and then into the settings, you'll see that under commit options, there is a commit signing option. You can do GPG, SSH, or S/MIME, and then you can drop in your key here. Now, every commit that Git Sync makes to your branch is signed automatically.

So, if your team is still managing dashboards manually, now is a great time to get started with Git Sync and bring your dashboard workflows right into Git. Take it easy.

## Raw YouTube Transcript

Did you know we just removed a lot of GitHub's pain right inside Grafana? Let me show you. So, you may or may not know, but in Grafana OSS and Cloud, we have a feature called Git Sync that lets you manage dashboards as code. This essentially means that changes that you make to dashboards can flow both ways between Grafana and your Git repository. So, for example, you can see I have my 5Flow GitHub repo syncing or provisioned in Grafana. When I look at the dashboards, you can see that this is bi-directionally reflected. So, in Grafana and then also if I go into my code and look at the infrastructure and dashboards folder, you'll see that both of these are presented. Now, from the Git side, any changes you make as well, so whether update a title of a dashboard in the JSON or whatnot, will actually reflect as well in Grafana, hence the bi-directional. Now, in Grafana 13.1, we've made that workflow even stronger and improved some of the features in it. So, one thing is we made getting dashboards into Git a lot easier. So, if you go into your provision folder that has Git Sync enabled, what you can do is actually go and import a dashboard. So, let's say you have one as JSON locally, you can upload that JSON dashboard, click on your Git Sync enabled folder, it'll give you a unique identifier, a branch name, and a repo folder if you want to set one, so maybe there's a subdirectory. You can import that and it'll actually open up a pull request. So, you can see a new resource has been created in a branch in GitHub. We can open that pull request and you'll see that all the changes are reflected here. We can create the pull request and then what we can even do is merge this. So, once we merge it in, those changes will be reflected. And then there is a sync interval in Git Sync and then that will reflect. So, what's pretty cool here as well is that we wanted to make it easier to keep documentation close to your dashboards. So, now your readmes get pulled in from your repository to Grafana when get sync is linked to that folder. So for example, if we look at the dashboards folder in GitHub, you'll see we have a read me file and now this is directly reflected in Grafana as well. And then finally for teams with stricter security requirements, changes can now be committed with verified signatures. So if you go into your general provisioning where get sync is enabled, if you go into the settings, you'll see that under commit options, there is a commit signing option. You can do GPG, SSH, and then once you click on that or S/MIME, and then you can drop in your key here. So now every commit that get sync makes to your branch is signed automatically. So if your team's still managing dashboards manually, now is a great time to get started with get sync and bring your dashboard workflows right into get. Take it easy.

