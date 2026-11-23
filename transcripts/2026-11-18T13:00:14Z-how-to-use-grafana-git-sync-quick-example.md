# How to use Grafana Git Sync | Quick Example

Published on 2026-11-18T13:00:14Z

## Description

Check this video that gives a quick overview how to use the Grafana Git Sync to sync your dashboards. 

*Watch the complete video*
https://www.youtube.com/watch?v=-Bz9f-kIB9I

Get started with the Grafana Cloud forever-free tier: https://grafana.com/g/cloud
Have a question? Ask Grot, your AI helper: https://grafana.com/grot/
Reach out in our community forums: https://gra.fan/communityyf

Links/resources: 

---
Thanks for watching! 

👍 Was this video helpful? Like and subscribe to our channel for more videos.

Connect with Grafana Labs: 
X: (https://www.twitter.com/grafana)   
LinkedIn: (https://www.linkedin.com/company/grafana-labs/)
Facebook: (https://www.facebook.com/grafana)

#Grafana #Observability #git #github #gitlab

URL: https://www.youtube.com/watch?v=J_mPol6TUuQ

## Summary

The video titled "How to use Grafana Git Sync | Quick Example," published on November 18, 2026, provides a brief overview of using Grafana Git Sync to synchronize dashboards. The speaker discusses the functionality of Git Sync, particularly how it manages folder metadata, including titles and IDs, to maintain consistency when folders are moved or created. Key takeaways include the automatic generation of metadata for new folders and the process of creating pull requests to ensure proper synchronization. 

Topics: Grafana Git Sync, dashboard synchronization, folder metadata, pull requests.

## Raw YouTube Transcript

So if we go here, we go to the resources, um this folder put JSON will appear. Uh let's see that this one is something that help us um having meta data of the folder. For example, the title and also the the ID that we are going to use for the folder. And this is something that GitSync uses to keep the folder having the same ID always. And also it helps GitSync referencing to the folders in case we move them. and and we do that. And um one thing that might happen is for example this one. Let's say we create a new folder which only has it's it's just an empty folder. Let's push that. Uh creating a new folder. Okay. And that should also immediately pull. It's already pulling. Um so here it will show exactly this one. Um so if git sync spots that a folder doesn't have that metadata it will just show that and we ask do you want to fix the folder ids? So do you want us to create the metadata for you? And if you just click this is going to create the repository uh sorry the branch and this is going to run this. It's going to create that is you can open the P request that is going to remove the keep file for example and create the folder metadata so that you can create merge for example and that is going to immediately pull again and um and change the folder so that it has exactly this metadata.

