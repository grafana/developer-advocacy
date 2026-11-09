# k8s-monitoring-helm Chart Office Hours (September 2026)

Published on 2026-09-30T20:03:46Z

## Description

In the September edition of the Kubernetes Monitoring Helm chart office hours, we discuss the version 4.4 and 4.5 releases, the ...

URL: https://www.youtube.com/watch?v=kxpn9ndxFyI

## Summary

The show is titled "k8s-monitoring-helm Chart Office Hours" and was held on September 30, 2026. The speaker, Pete Wall, an engineer behind the Kubernetes monitoring Helm chart, discussed the recent development updates and upcoming features for versions 4.6 and 5.0. Key topics included security hardening for the node exporter, improvements in database observability, the reintroduction of a configuration validation feature, and plans to integrate OpenTelemetry collectors. The session emphasized community engagement and the importance of feedback for future enhancements.

Topics: Kubernetes monitoring, Helm chart, security hardening, OpenTelemetry, community engagement.

## Chapters

00:00:00 Overview of Kubernetes monitoring Helm chart updates
00:05:23 Upcoming features in KSM monitoring helm chart
00:10:02 Overview of the manifest viewer in Grafana Cloud

Hello everybody and welcome to the September edition of the Kubernetes Monitoring Helm Chart Office Hours. I'm Pete Wall, one of the engineers behind the Kubernetes Monitoring Helm Chart. We have a pretty short agenda today. Since last month, we haven't completed another minor feature release. If you want to learn about what happened in the 4.4 and 4.5 releases, check out last month's recording where we go in-depth about the content.

This month, we slowed down our development a little bit. We've been focusing on some of the ways that the Kubernetes Monitoring Helm Chart interacts with other internal tools and exploring great collaboration opportunities. I was away a couple of times for different conferences, so I've been out of the loop for a bit. However, we feel like having a slowdown may not be such a bad deal given the huge amount of velocity we had in the last couple of months.

I did want to talk about what we have planned for future versions. The 4.6 release is expected to come out in the next week or two, pending a few things lining up before we merge in all the changes. The focus for 4.6 will be on security hardening. There is a request for node exporter security hardening. Node exporter, by the nature of its work, needs a lot of permissions to perform its tasks. We don't use all of those permissions, so there's an opportunity to tighten things up and make it easier to deploy the Kubernetes Monitoring Helm Chart with its dependent services onto clusters with certain security requirements.

A similar story applies to Alloy. Alloy is a very powerful general-purpose tool that often comes with many security requests by default. Depending on the configuration you provide, you may need different RBAC rules. We're considering tightening that up to make it a bit more secure by default.

Additionally, there are some small changes regarding how we will be deploying things and some minor improvements to existing features. Database observability improvements will also be included in the 4.6 release. 

The configuration validation Helm hook was a feature we had back in the 1.x timeframe. This Helm hook ran before everything else got installed and used Alloy to validate that the configuration you deployed was correct. The goal was to fail fast. If you added some configuration into the extra config sections of your collectors or any rules, there was a chance of sneaking in a syntax error. Without this hook, the only way to find out about such errors was when Alloy pods started crashing or when the Alloy operator couldn't reconcile an Alloy instance configured or deployed to your cluster. 

Having this pre-install hook allows you to validate that the configuration looks good before any issues arise. We removed this feature in 2.0 because I was focused on making deployments faster. Having a Helm hook that installs first, validates, and then returns only to delay the rest of the install felt like it was slowing things down. Since then, I've had feedback from people who would like to have that feature back. We will add it in, but it will probably default to off, allowing you to turn it on if you want that extra validation without making it mandatory.

We will still use Alloy, so the nice thing is that it will utilize the Alloy already deployed based on the collectors you've chosen. In the 5.0 timeframe, we are exploring what we can do with a major version upgrade. We are looking into the possibility of deploying OpenTelemetry operators or collectors. Just like you can specify your Alloy collectors in the collectors list, you will be able to specify OpenTelemetry collectors. 

There will be decisions to make regarding which built-in Helm chart features will be supported on the Alloy side or the OpenTelemetry side. We will not target a one-to-one feature match between the Helm chart and OpenTelemetry in 5.0. Instead, we will likely select a limited set of features that make sense for OpenTelemetry. Validators will be included, as we do with the Helm chart, to ensure that if you map a feature to an OTel collector, you will be warned if it's not a compatible match.

The Kepler project, which generates energy metrics on your clusters, capturing how much power is being used by both the cluster and the workloads running inside it, has moved. Because Helm is structured the way it is, it's challenging to simply point to the new source; it ends up looking like a migration of the chart. We want to be very careful about how we operate that, but it will come in 5.0.

For the Alloy operator in 5.0, we will by default make it a namespace deployment. When you deploy into, say, the monitoring namespace, the Alloy operator bundled with the KSM Monitoring Helm Chart will only reconcile Alloy instances inside that namespace. You can configure it to watch multiple namespaces or cluster-wide as it does now, but this change simplifies deployments when using multiple instances of the KSM Monitoring Helm Chart in different namespaces, preventing them from stepping on each other.

In the spirit of security for the 4.6 timeframe, we will also look into minimizing our RBAC. We aim to create RBAC rules for the Alloy instances that allow only what you're trying to do, making things more secure by default. There will be some complexity involved when mixing configurations deployed by the Kubernetes Monitoring Helm Chart and pulling configurations from Grafana Cloud's fleet management. This is why we are looking into it for 5.0.

That's the preview we have for upcoming versions. We have been doing some patch releases since 4.5 was released, including updates to dependencies and other bug fixes. If you're on 4.5, please check the most recent patch release for any features or fixes.

Now, we have time for questions. If anybody has a question, feel free to unmute.

> Uh, not really any questions. Um, but we just started deploying out version four. 

Oh, great!

> And I enabled the Kates manifest stuff. 

Yeah. 

> Kind of curious what that... what that...

looked like. 

Yeah. 

Um, it was interesting because I thought it would show me the actual manifest, but it's actually just tailing and letting me know that things changed. 

Yeah. 

So that was because I didn't know what it was going to do, so I just enabled it and went looking for it, and I'm like, "Oh, okay." 

Yeah. 

Okay, that's what I posted in the community channel like, "Hey, has anybody got a dashboard?" because I didn't know what to kind of expect from it. 

Sure. 

So I actually had Grafana Assistant make me a dashboard. 

Nice. 

Uh, yeah, the Kubernetes manifest feature—what time did we add that in? I don't remember, but that was a feature release that we did a little while ago. 

Um, for those that might be unfamiliar with that, the Kubernetes manifest feature, if you enable that, deploys an extra project. I believe it's called Kates manifest tail. 

Uh, and what that does is it will watch for specific types of objects—pods, deployments, anything that you choose—but typically it's going to be workload type deployments into your cluster. It will capture a full snapshot of the YAML manifest on a schedule when it starts up, but also maybe once a day or something like that. I forget what the default time limit is. 

Um, and then it will watch for events from the API server, and when modifications come to those pods or deployments, stateful sets, whatever, it will capture the new manifest, it will diff from the previous one, and it will write the diff as log data. 

So, all of this stuff gets sent to Loki for storage—the full manifest snapshot as well as any of the diffs that occur. 

Um, and so, the idea behind this is if you're using the Kubernetes monitoring feature in Grafana Cloud, you're navigating through your cluster, you go to a deployment, there should be a little button that says "view manifest." 

Um, and so, you can see the actual YAML manifest that's running on the cluster. This may not be the same manifest that is like a YAML file that you apply because of things like mutating webhooks or other sorts of things. This is what the API server reports as saying this is what is running in the cluster for this deployment. 

Uh, but then the diffs, if things change over time, you can then view inside of Grafana Cloud the difference between V1 and V2. What changed? You know, replicas went from three to four, or the image went from this image version to this image version. 

Um, and so, that's the idea behind the manifest viewer. 

Uh, there are some changes that I'd like to see in time. Um, there's no promised timeline for this, but one of the things that I'd like to do is, just like for the host metrics feature, we made it so that you can use Alloy itself to capture things that node exporter or Windows exporter would do. 

I would love to see if I could bake this idea into Alloy or into OpenTelemetry Collector for that matter. 

Um, it seems like something that they should be able to handle. It might not need a separate deployment. 

Um, but please feel free to give it a try. Tell me what you think. If you like it, what sort of things you'd like to see changed about it. 

Um, yeah, I'd take that feedback. But I'm glad that you tried it out. 

>> I'm glad I joined because I didn't know there was a view manifest button. 

Yeah. 

Yep. 

I just went and looked, and I'm like, "Oh, there it is. Oh, okay, that's kind of cool." 

Yeah. 

Um, so one of the things that we do, we do some processing on those manifests before we ship them off cluster. 

Um, most notably, we remove a lot of the stuff that's pretty noisy. So, the whole status object within the manifest goes away because most of that's pretty ephemeral stuff. 

There are some annotations that get set by default by Kubernetes that we've removed. 

Um, you know, last applied type of things. 

Um, we will remove any environment variable values. 

Um, I'm seeing it less and less, but I do see it occasionally where people will set credentials as environment variables and not as a reference to a secret, but you know, just directly, you know, key is this, value is this, right? 

Um, so just out of trying to be safe, we redact any of the environment variable values before we send it off cluster. 

Um, yeah. So, we try to be safe on that. But good question. I'm glad that you're bringing it up. 

>> Yes, my Grafana system, the dashboard I made has a chart that shows me the manifest tail stuff and everything. 

So, when I made kind of a big change to a couple of different clusters, all of a sudden it goes from like nothing to boom. Good chunk, and then we have to just back off, and I'm like, "Okay." 

Yeah. 

And then I just started looking through the logs and everything, trying to look at what changed and diff and everything, and then I had to go back to my day job, so I couldn't keep digging into that sort of stuff. 

But yeah, the view manifest is kind of cool. 

>> Yeah. 

Yeah. 

Um, that is something that came out of a Grafana hackathon, actually. 

So, you know, that's one of the things that we like to do at Grafana Labs. Every once in a while, we'll do hackathons to come up with cool projects, and you know, often they turn into features, so it's neat. 

Um, all right. 

Uh, any other questions? Otherwise, we'll call it a meeting. 

Cool. 

>> Um, no, can't think of anything. 

Great. 

Well, thank you so much for joining. Thanks for listening. If you're watching the recording, I appreciate that. 

Um, if you want to join one of these meetings, we typically hold them on the third Friday of the month. Time shifts because of schedules and things like that, but I will always try to communicate when the meetings are going to be in the Kubernetes channel of the Grafana community Slack workspace. 

If you want to join that workspace, grafana.slack.com. 

Um, this Helm chart is very much community-focused. We want to make sure that it's effective for you, and so it is developed in the open source at grafana/k8s-monitoring-helm on our GitHub repository. 

So, if you have feature requests, if you have rough edges that you'd like to see smoothed out, feel free to file an issue there. 

Uh, feel free to file a pull request to fix something that you might see. 

Um, we welcome all of that engagement. 

So, thank you so much again for joining, and we'll see you next month. 

>> All right. So, take care everyone. Thank you.

## Raw YouTube Transcript

Hello everybody and welcome to the September edition of the Kubernetes monitoring Helm chart office hours. I'm Pete Wall, I'm one of the engineers behind the Kubernetes monitoring Helm chart. And uh we have a a pretty short agenda today. Uh we uh since the last month um we haven't completed another minor release, a feature release. Uh so if you want to learn about what happened in like the 4.4, 4.5 releases, uh check out last month's recording. We go into depth about what was uh the content that was in Uh the this month we slowed down our development a little bit. We've been focusing on some of the ways that the Kates monitoring Helm chart interacts with other internal tools. Uh and other like great collaboration type of opportunities there. I was gone uh a couple times for different conferences and so I've been away for a little bit, but uh we feel like, you know, we we had a huge amount of velocity in the last couple months. We uh slowing down maybe is not such a bad deal. Uh but I did want to talk about um what we have coming up for uh we still have planned for future versions. Uh the 4.6 release, which I'm hoping maybe be coming out in in the next week or two or so. We'll see. We're waiting for a couple things to to line up before we're uh we're going to merge in all the changes. Um but the the focus for 4.6 will be on security hardening. Uh there's a there's a request out there for uh node exporter security hardening. Uh you know, node exporter by the nature of its work needs a lot of permissions to do some of the things that it does. We don't use all of those and so there's a way that we could tighten some of those things up and make it a easier thing to deploy the Kates monitoring Helm chart with its dependent services onto clusters that have certain security requirements. Uh similar story for Alloy. Oops. Back. Uh Alloy uh is a very powerful general-purpose tool. Um often comes with a lot of security, uh, requests by default because depending on the configuration you give it, uh, you need different RBA rules or other things like that. Um, we're thinking about tightening that up so that, uh, you know, it's just a little bit more secure by default. Oops. Excuse me. Um, a couple other features that, uh, that I didn't mention on to here, but, um, uh, some small changes on how we're going to be deploying things and some, uh, some minor changes with regards to, you know, improvements on some of the existing features. Um, there's some database observability improvements that will be coming, um, but, uh, but yeah, that all be coming into the 4.6. Uh, the configuration validation webhook, or not webhook, but, uh, Helm hook. Uh, that was a feature we had back in the 1.0, uh, 1.x time frame. Um, that was a Helm hook that ran before everything else got installed and it essentially used Alloy to validate that the configuration that you deployed was was good. Um, this was the the goal for that was to fail fast, right? So, if you added some configuration into the extra config sections of your collectors or into, uh, any of the rules or any sorts of places where you're adding raw Alloy configuration. Um, there's a chance that, you know, you could sneak in a little syntax error or something like that. Uh, without this, the only way that you find out about this is that when you've got Alloy pods that start crashing or maybe Alloy operator doesn't get to reconcile an Alloy instance that gets configured or deployed to your cluster. So, having this pre-install hook just lets you validate that the configuration looks good before any of that stuff shows up. Uh, we removed that in 2.0. Uh, the reason why we removed it is I was focused on, can we make it so that you can deploy fast? And having a webhook that, or webhook, having a Helm hook that installs first, does its validation, and then returns only to delay the rest of the install, I felt like was slowing things down. Since then, I've had people say, you know, I kind of would like to have that back. So, what we'll do is we'll add that in, but I'll probably make it default to off. So, you can turn that on if you want that extra validation, uh but it's not going to be a a mandatory feature. Uh we will still use alloy, so the the nice thing about that is it will utilize the alloy that's already going to be deployed based on the collectors that you've that you've chosen. Uh in the 5.0 time frame, uh what we're looking there, what can we do if we're picking a major version upgrade? Um we're looking into being able to deploy open telemetry operator or collectors. So, just like you can specify your alloy collectors in the in the collectors list, uh can you specify open telemetry collectors? Uh this will have some decisions to be made as far as what of the built-in helm chart features will be supported on the alloy side or the open telemetry side. We will not be tar- targeting to get one-to-one, you know, you can use all features in the helm chart on open telemetry in 5.0. We'll probably pick a very few set of things that makes sense to go onto the open telemetry side of things. Um obviously, we'll put in validators uh like we do with the helm chart to make sure that if you map a feature to an otel collector, uh that will will warn you if it's not a compatible match. Uh the Kepler uh project, Kepler is used to generate energy metrics on your clusters, so capturing how much power is actually being used by not only the cluster, but the workloads that are running inside of the cluster. Uh that project has moved, and because helm is the way helm is, it's hard to just say, point to the new source. You have to actually it it it ends up looking like a migration of the chart and so we want to be very careful on how we how we operate that. But that will come in the 5.0. Alloy operator, what we'll do for 5.0 is we will by default make it a name space deployment. So when you deploy into say the monitoring name space, the alloy operator that gets bundled in with the KSM monitoring helm chart will only reconcile alloy instances inside of the monitoring name space. You can set it back, you can have it watch for multiple name spaces or you can have it watch cluster wide like it does now. But this way it makes it simpler if you are going to be deploying multiple instances of the KSM monitoring helm chart in different name spaces, they won't step on each other. And I think that having it name space makes sense because often you aren't having people deploying in one place and then deploying alloy CRs, alloy instances all across your cluster. You can and we can make that easy. And then in the spirit of security of the like the 4.6 time frame, we're going to look into can we do some minimization of our back? So can we actually look at the configuration that you've chosen and only create our back rules for the alloy instances specifically that allow only what you're trying to do. So make things more secure by default. And you know, that there's some complexity that will be involved there when you mix not only the configuration that's deployed by the Kubernetes monitoring helm chart, but also pulling config from things like Grafana Cloud's fleet management. Some of that stuff you won't know after you've pulled that configuration to know what sort of features you'll need. That's why we're looking into that for 5.0. That's the preview we've got coming up for upcoming versions. Obviously, we have been doing some patch releases since the since 4.5 was released and so updates to some of the dependencies, other bug fixes. So if you're on 4.5, uh please look at the most recent patch release for any features or fixes there. Uh and like I said, it's going to be a short one. So now we have time for questions. If anybody has a question, feel free to unmute. >> Uh not really any questions. Um but we just started deploying out version four. >> Oh, great. >> And I enabled the the Kates manifest stuff. >> Yeah. >> kind of curious what that what that looked like. >> Yeah. >> Um it was interesting cuz I I I thought it would show me actual manifest, but it's actually just tailing and letting me know that things changed. >> Yeah. >> So that was cuz I didn't know what it was going to do, so I just enabled it and went looking for it and I'm like, "Oh, okay." >> Yeah. >> Okay, that's what I I posted in the the community channel like, "Hey, has anybody got a dashboard?" Cuz I didn't know what to kind of expect from it. >> Sure. >> So I actually had Grafana assistant make me a dashboard. >> Nice. Uh yeah, the the Kubernetes manifest feature um what what time did we add that in? I don't remember, but that was a feature release that we did a little while ago. Um for for those that might be unfamiliar with that, the Kubernetes manifest feature, uh if you enable that, that deploys a an extra project. I believe it's called Kates manifest tail. Uh and what that does is it will watch for specific types of objects, um pods, deployments, um anything that you choose, but typically it's going to be workload type deployments um into your cluster and it will capture a full snapshot of the YAML manifest um on a on a schedule. When it starts up, but also maybe once a day or something like that. I forget what the default time limit is. Um, and then it will watch for events from the API server and when modifications come to those pods or deployments, staple sets, whatever, uh, it will capture the new manifest, it will diff from the previous one, and it will write uh, the diff to um, to as log data. So, all of this stuff gets sent to like Loki for the for storage. Um, the full manifest snapshot as well as any of the diffs that occur. Um, and so, the the idea behind this is if you're using the Kubernetes monitoring feature in Grafana Cloud, uh, you're navigating through your cluster, you go to a deployment, there should be a little button that says view manifest. Um, and so, you can see the actual YAML manifest that's running on the cluster. This may not be the same manifest that is, uh, like a a YAML file that you apply because of things like mutating webhooks or other third sorts of things. This is what the API servers reports saying this is what is running in the cluster for this deployment. Uh, but then the diffs, if you if uh, things change over time, you can then view inside of Grafana Cloud the difference between V1 and V2. What changed? You know, replicas went from three to four or the image went from, you know, this image version to this image version. Um, and so, that's the idea behind the manifest viewer. Uh, there are some changes that I'd like to see in time. Um, there's no promised timeline of this, but one of the things that I'd like to do is, uh, just like for the host metrics feature, we made it so that you can use Alloy itself to capture things that node exporter or Windows exporter would do. I would love to see if I could bake this idea into Alloy or into Open Telemetry Collector for that matter. Um, it seems like something that they should be able to handle. It might not need a separate deployment. Um, but please feel free to give it a try. Tell me what you think. If you like it, what sort of things that you'd like to see changed about it. Um, yeah, I'd take that feedback. But I'm glad that you tried it out. >> I'm glad I joined cuz I didn't know there was a view manifest button. >> Yeah. Yep. >> I just I just went and looked and I'm like, "Oh, there it is. Oh, okay, that's kind of cool." >> Yeah. Um, so one of the things that we do, we do some processing on those manifests before we ship them off cluster. Um, most notably we remove a lot of the stuff that's pretty noisy. So, the whole status object um, within the manifest that goes away cuz most of that's pretty ephemeral stuff. There are some annotations that get set by default by Kubernetes that we've removed. Um, you know, last applied type of things. Um, we will remove any environment variable values. Um, it's I'm seeing it less and less, but I do see it occasionally where people will set credentials as environment variables and not as a reference to a secret, but you know, just directly, you know, key is this, value is this, right? Um, so just out of being trying to be safe, we redact any of the environment variable values um, before we send it off cluster. Um, yeah. So, try to be safe on that. But good question. I'm glad that you're you're bringing it up. >> Yes, my uh, Grafana system, the dashboard I made um, has a chart that shows me like like the manifest tail stuff and everything. So, when um, I'll go through and I made kind of uh, kind of a big change to a couple different clusters, all of a sudden it goes from like nothing to boom. Good chunk and then it just we have to just back off and I'm like, "Okay." Yeah. And then I just started looking trying to look through the logs and everything like trying to look at what what change and diff and everything and then I had to go back to my day job so I couldn't keep like digging in digging into that sort of stuff but yeah the view manifest is kind of cool. >> Yeah. Yeah. Um that is something that came out of a a Grafana hackathon actually. So you know that's one of the things that we like to do at Grafana Labs every every once in a while we'll do hackathons to come up with cool projects and you know often they they turn into features so It's neat. Um all right. Uh any other questions otherwise we'll call it a meeting. Cool. >> Um no can't think of anything. >> Great. Well thank you so much for joining. Thanks for listening. If you're watching the recording I appreciate that. Um if you want to join into one of these meetings we typically hold them on the third Friday of the month. Time shift because of you know schedules [snorts] and things like that but I will always try to communicate when the meetings are going to be in the Kubernetes channel of the Grafana community Slack workspace. If you want to join that workspace grafana.slack.com. Um this Helm chart is very much community focused. We want to make sure that it's effective for you uh and um and so it is developed in the open source at grafana/k8s-monitoring-helm on our GitHub repository. So if you have feature requests if you have rough edges that you'd like to see smoothed out feel free to file an issue there. Uh feel free to file a pull request to fix something that you might see. Um we welcome all of that uh engagement. So thank you so much again for joining and we'll see you next month. >> All right. So take care everyone. Thank you.

