# Grafana Mimir community call -- 2025-07-31

Published on 2025-08-01T18:53:10Z

## Description



URL: https://www.youtube.com/watch?v=dtRI8zCd7ss

## Summary

In this community call, the team discussed the upcoming launch of Mir 3, a major version set to release in the fall. Key speakers included Zal and Nick, who provided an overview of architectural changes, particularly the decoupling of read and write processes and the introduction of new components like the query front end and query scheduler. They highlighted the significance of inest storage, which will require Kafka for operation. The discussion also covered migration concerns, compatibility with existing systems, and the implications of adopting Kafka, including potential resource challenges and costs. The team encouraged community feedback and questions while assuring that documentation regarding migration and architectural changes would be provided in due time.

# Community Call Transcript: Mir 3 Launch Overview

**Moderator:**  
Yeah, we do a recording just for other people's reference later. So, this is the first one for the V3 launch. I'm not sure how many of you have seen this diagram or this video before. Right now, the plan is to launch Mir 3, the new major version, in the fall. 

This is a general overview of the architecture. I think the most meaningful change is the decoupling of read and write. As you can see here on the left-hand side, this is the current architecture. On the right-hand side, we put in "inesters" on the repath for compile apps. For the call version, we use a component called WAR, which is essentially more like managed Kafka. For the community version, you can also use Kafka-compatible protocols, so we can go over that later in the call regarding the keychain changes. 

I think these are the most meaningful changes we introduce in Mir 3. For example, we require the query front end and scheduler, and we will default to the Mir query engine, which is already on in version 2, so this isn't surprising. Another thing is regarding ingest storage or the capa components. We might not make it default at the beginning, but over time, we will make this component default. The last point to call out is the "no reader" deployment mode in the future, but we will still keep the monolith modes in Mir 3. 

That's pretty much the overview of everything we plan to do. I’ll pause here to see whether people have any questions. 

**Moderator:**  
Let me share the overview page. I think you can read through this. I'm going to go ahead and add this to the notes as well to provide context regarding the key changes slide that ZAL presented. 

In 3.0, we are requiring the query front end and query scheduler components. If you're using the Helm chart or JSONet, you're probably already running these, but up until now, they've been technically optional. We're making them required because it makes it simpler to run Mamir if we don't have to support running it in multiple different ways for the read path.

The big change is ingest storage, which is a whole thing. 

**Question:**  
A question about the last question listed in the FAQs: Do we need any third-party tools for application infrastructure?

**Response:**  
Technically, we do need Kafka to run Mamir 3.0. The Mamir binary still has everything except for object storage, CFKA, and cache. If you use ingest storage, you will need CFKA. It's not required to use ingest storage in Mamir 3.0, but it will be available and might be the default. We're still figuring out what that will look like, but you'll still be able to run the classic architecture in 3.0 if you don't want to deal with CFKA at this time.

**Follow-up Question:**  
Is that going to be supported until version 4? I believe at some point, you'll be zoning out the existing functionalities and then making Kafka the default.

**Response:**  
Yes, that is the plan. Classic mode is not going away for a while. It would be a 4.0 change, which is far in the future. We haven't set a timeline for that yet.

**Question:**  
I have a question about how this would affect the enterprise product. Will this be available for enterprise users?

**Response:**  
Right now, we don't have a plan to support enterprise, but we'll probably make a decision on that very soon.

**Question:**  
I've read somewhere that MRI won't be backward compatible with the previous storage. Can we have more information on that?

**Response:**  
I'm not sure what you mean. The TSDB format that gets stored in object storage isn't changing, so you'll still be able to read all your previously ingested data. That will remain the same format. The migration to the CFKA architecture hasn't been decided yet, but it will be complicated. However, the format for historical data will not change, so you'll be able to read it.

**Question:**  
Regarding using Kafka-compatible APIs, will there be any difference in performance? Will there be benchmarks available?

**Response:**  
We run Warpstream in Grafana Cloud and can share our experience with it, but the Mamir docs won’t provide a comprehensive section on the CFKA implementation you should pick. We will leave that for everyone to decide. Since Warpstream uses object storage, we found that the end-to-end latency is higher than regular CFKA. 

We need contributions or feedback from the community regarding other Kafka-compatible protocols. We've only tested Warpstream, which is now part of Confluent. 

**Question:**  
Will ingest storage become sort of misnomer now that we have the new component, block builder? Are we going to zone out ingestors and merge them with the queries?

**Response:**  
Yes, they are named incorrectly in the new architecture. Block builder isn’t enabled or used by default in the new architecture yet, but it will be eventually. The ingestors are still responsible for building and uploading blocks for a little while longer.

**Question:**  
What are the concerns regarding migration to Mir, especially if running in production or large scale?

**Response:**  
The biggest concern is that we now have this additional component to run. In the past, you only needed Kubernetes; now you need to think about Kafka, which has its own challenges. Kafka is not easy to run and has significant resource requirements. 

**Question:**  
Will managed CFKA from cloud providers help with that?

**Response:**  
Yes, if that's an option. However, the cost of having managed Kafka is also significantly higher.

**Response:**  
Since classic architecture is not going away in 3.0, you could defer needing to run CFKA yourselves for a while. We anticipate this will be the default in the future, but you can delay that decision.

**Question:**  
Can we get documentation that shows the usage of Kafka depending on load in Mamir? This will help us pre-provision CFKA and allocate resources.

**Response:**  
We might be able to provide directionally correct estimates based on usage. It depends a lot on the specific use case and load patterns.

**Question:**  
Are you planning to use an existing CFKA cluster?

**Response:**  
That’s a good question.

**Question:**  
Besides the Kafka components, do you have any other concerns about other key changes?

**Response:**  
We already run in a distributed mode, so we have the query front end and scheduler. There are no changes there. However, I’m still unclear about what the query engine means in terms of operations.

**Response:**  
In the latest 2.0 release, the query engine is enabled by default. You should see a little less memory and CPU usage there, and it will be the default everywhere in 3.0.

**Question:**  
What will be the retention of objects inside Kafka by default?

**Response:**  
We generally use three to seven days. This only determines how long of an outage your ingestors can go through without losing data. If the ingestors restart and don't come back up within the retention period, you would see gaps in the data.

**Response:**  
Kafka is not used as the write-ahead log currently, so every byte is read only once. This might change in the future.

**Response:**  
For Warpstream, if you want an open-source alternative, there’s a project called AutoMQ. We haven't tested that, but you can check it out. Red Panda is also now open source, which could be a good solution.

**Question:**  
Will there be an upgrade document to migrate from the current architecture to the new one?

**Response:**  
Yes, there will be. It doesn’t exist yet, but you won’t need to do a data migration since the format in object storage is not changing. 

**Response:**  
There will be a migration guide, focusing on the process with downtime first. There are two ways to migrate: one is simpler but involves downtime, and the other doesn't involve downtime.

**Question:**  
Will we get alerts for the new architecture?

**Response:**  
Yes, there are alerts for all relevant parts of the new architecture, and the dashboards will reflect it.

**Moderator:**  
Thank you all for attending this community call, and thanks to everyone who answered questions. If you have additional questions, feel free to post in the community channel, especially regarding Mir 3. We will do our best to answer or share documents for others to reference. If there are no more questions, thanks again, and I will see you online.

**All:**  
Okay, bye!

## Raw YouTube Transcript

Yeah, we do a recording just for other people's like reference later. So, yeah, this is um so the first one is for the V3 launch. Um I'm not sure many of you have seen this um diagram or have seen this video before. Um right now the plan is to launch Mir 3, the new major version in the fall. And this is a general overview of the architecture. I think the most meaningful change is the decoupling of read and write. As you can see here on the left hand side, this is the current architecture. on the right hand side. Um essentially we put inesters um on the uh repath um for copile apps or for the call version we use um a component called war it's essentially the more like manage kafka but again for community version you can also use cafka compatible uh protocols so we can also go over that later in the call regarding the keychain changes. I think these are the most meaningful changes uh we introduce in Mir 3. Um for example, we require query front end and scheduleuler and will default to the mirror query engine. It's already on in 2. So this is not something surprising. Another thing is for inject storage or or the capa components. Um we might not make it default at the beginning but over time we'll make this component default. The last one um to call is a no reader right deployment mode in the future. Um but we'll als we will still keep the monolith modes um uh in m3. Um I think that's pretty much the overview of everything we plan to do. Um and in the community channel we kind of ask a question of like what are the most common um probably um questions you might have and this is list we have already compiled today. Um feel free to read through this. If you have additional questions, feel free to ask live or directly in the in the chat and we'll have people from profile labs to answer if we know if we know um the answer already. So that's pretty much the overview of what we have. Um I'll probably just pause here to see whether people have any questions. Uh let me share the every page. I think this one you can read through this. I'm going to go ahead and add this to the note as well. to add some context uh to the key changes slide that uh ZAL presented. Um in 3.0 we are requiring the query front end and query scheduler components. If you're using the Helm chart or JSONet, um you're already running these uh probably, but up till now they've been technically optional. Um but we're making them required because it makes it uh simpler to to run Mamir if we don't have to support running it multiple different ways uh for the read path. Uh and then obviously the the big change is uh is inest storage which is a whole is a whole thing. Um a question about the the last question listed on this FAQs. Um it asked like whether we need any third party tools uh application infrastructure. Uh technically we do right because we need Kafka in order to do in order to run Mimi 3.0. >> Uh yes. So the the Mamir binary still has everything except for uh object storage, CFKA and cache. Uh but yes, if you use inest storage, you will need CFKA. Um, it's not required to use injest storage in Mamir 3.0, but it will be available and it might be the default. Um, we're still figuring out what that what that would look like, but you'll still be able to run the classic architecture in 3.0 if you want if you don't want to have to deal with CFKA at this time. Um I'm sorry. >> Yeah, just a followup question. So um is that going to be supported until version 4 or I guess like I believe like at some point you will be kind of um zoning out the existing functionalities and then kind of make the Kafka as default. Yeah, I think that is the plan though. Classic mode is not going away for a while. Um it it would be it would be a 4.0 change which is you know far in the future. Um we haven't actually set a timeline for that or anything like that uh yet. >> Thank you. Uh I did have one question about uh how this would affect the enterprise product. This would also be available um if you're if you're an enterprise user. >> Um right now we don't have a plan to support enterprise. Um but yeah, we'll probably yeah probably make a decision very soon. Uh I have a quick question like uh I have read somewhere that uh MRI won't be backward compatible with uh your previous storage. So can we have some more information on that? >> Uh I'm not sure what you mean. The TSDB format that gets stored in object storage isn't changing. So you'll still be able to read all your previously ingested data. That will still work. That will still be the same format. Um the migration to the CFKA architecture is uh we haven't sort of decided on uh what the migration plan will be, but it it's going to be involved. It's going to be a bit complicated. Um, but things that have been ingested and live in object storage already, the format's not changing. So, you'll be able to read historical data. Obviously, that would be that would be a really awful change to make. So, >> got it. Makes sense. Um in in regards to kind of using any Kafka compatible APIs, would there be any difference in performance? Um or would there be any kind of benchmark available like if you use WSRE versus if you don't use your own own Kafka cluster or like um confluent um cloud service etc. So we run warpstream in graphana cloud and we can sort of uh share our experience with it but um the the mammir darks aren't really going to have a comprehensive this is the CFKA implementation you should pick uh section like that's we're going to leave it for everyone to make their make their own decisions. Um because Warpstream uses object storage, we found that the the endto-end latency is higher than uh regular CFKA. >> I think that's probably the area we need some contribution or feedback from the community regarding other Kafka compatible protocol. Uh for us, we have only tested warpstream. Uh by the way, Warframe is part of Confluence now. So essentially it's probably part of their offerings but regarding other Kafka compatible API protocols uh we probably need some communitydriven contributions like if you use Amazon version or any other flavors we don't know uh from our end. >> Yeah, sounds good. Thank you. Um one one more question. So if you go back to the architecture uh we still keeping the injustice in um I I wonder whether this they're going to become sort of misnormal now become because now we have the new component um block builder I think they are the kind of essentially the inesttors now and we'll are we going to kind of zone out inesttors as well and then kind of merge with the quer is. >> So, yeah, they're definitely they're named wrong in the in the new architecture. Um, block builder isn't enabled by default or used by default in the new architecture yet. It will be eventually, but it's it's not today. like even even in our environments, we're not using it in all of them. We're still uh working through some things. Um but yes, the ingesttors uh are named wrong, but they're still responsible for building and uploading blocks uh for a little while. >> Thank you. Maybe one question I want to ask the audience here is like let's say if you want to migrate to Mir Um what are the concerns regarding migration? Uh especially if you run anything in production or large scale. Do you have any concerns or any thing we can provide as like input? I think like at least from uh where I come from like the biggest concern we have that now we have this this additional component to run while in the past you could just deploy you just need Kubernetes you deploy with I mean we uh distributed architecture and it just just work now we need to think about this yeah Kafka and I think with all the challenges which comes with that so yeah I think that the main concern. But I guess that's that's just the architectural choice which we made. So just have to see how how that kind of spans out and Kafka is not not an easy thing to run. It's not like something you can just kind of spun up easily. significant uh resource requirements and yeah >> all the challenges come with that >> the managed CFKA that a lot of cloud providers uh might help with that. Yeah, >> if that's an option >> I guess like also related kind of like it's also like now the cost of of having managed Kafka is also significantly higher than Yeah. Uh so I think that kind of adds to overall. >> So uh because classic architecture is not going away in 3.0, you could you could you could put off uh needing to run CFKA yourselves for a while. Um >> we anticipate this will be the default in the future, but if you want to um you know save that problem for another day, that's an option. >> Yes. Thanks. Um just wondering if if it would be possible to get like a like a documentation or something that um shows um the usage of Kafka depending on how big is the loads in Mimu that if if we can get something like that would be really good. So we can um um uh how can I say like we can see how how it's going to be or how it's going to yeah how it's going to be in our platform for example >> it would be resource usage like >> yeah yeah help me pre-provision CFKA again to help pre-provision CFKA like allocate resources No like uh like uh let's say like okay I I got like a billion metrics like how that will affect to cafka in in this situation and things like that you know >> so maybe uh like maybe records per second or um or bytes per second something like this. >> Yeah. Yeah. Mhm. I think it obviously depends a lot on usage but we might be able to come up with some some directionally correct estimates. >> Yeah, I was just thinking like you know sometimes uh in our for example now what we mean we have a lot of spikes on different times of the day. So we just need to figure out okay um do we need to be like concerned about the you know um the amount of data that is coming uh you know like the storage on on the on the workers and all that stuff that is something that we would need to have in consideration uh when managing Kafka and all that stuff. So it's just a bit of overall usage on on you know like I have this that that like this much of bytes per second. uh you would need you know um this amount of resources or or or you will need to tune it in a way that you know only consume text or things like that like it would be good to have I think >> um I'm curious I don't think it matters a lot but um are you planning on using an existing CFKA cluster maybe Okay. Okay. Thanks. Um maybe besides the Kafka components, um do you guys have any other concerns about other probably um key changes? Um especially like for example do you guys have any feedback for query engine or like if we require query front end query structure how will that impact you guys um I don't think those these changes as big as in storage but just want to double check if you have any feedback or comments. So we already run as I said like if we run uh in in kind of distributed mode so we already have the query front end and scheduleuler. So so there's no changes on that part. Um I'm still not sure like what does query engine would mean kind of in terms of the operations wise. >> So that uh it's in the latest 2.0 0 release. It's enabled by default in queryers. Um, so you should see a little less memory and CPU usage uh there, but uh it's going to be the default everywhere in 3.0. And so um yeah, it's just we we obviously test it to make sure it's compatible uh with the Prometheus engine, but like that's a that's ongoing uh work to make sure that we match. Uh does anyone run Mamir on bare metal? um meaning not Kubernetes that might uh in which case maybe the requiring a queryuler might affect you if you weren't running it before. Any additional questions from the community? >> Uh yeah, quick question. Uh so like uh as we have right now uh the current retention inside injust is by default 12 hours right. So I guess it will continue and uh what will be the retention of objects inside Kafka by default like or what is the ideal uh like suggestion here for the object retention you might know this uh better but I think we use three days or seven days. >> So, this only determines how long of an outage your injusters can go through without losing data. Um, it like you could run it technically with an hour of attention. It should work most of the time, but if the injusters restart and for some reason don't come back up within an hour, you would see some gaps in the data. Um yeah um Kafka is still not used as the write ahead log. So in a way when the gesture restarts it doesn't doesn't replay already replayed data from Kafka. So kind of every bite is read only once. Um, this might change in the future, but right now it's only it's only you can think of it as a transport between distributors and injustice. So yeah, retention depends on how long of an outage you want to tolerate. I think I'm not sure what we run it with. Um, first storage, we use Robstream. We use warpstream which stores the data on object store. So storage is kind of cheap and we run with with a few days just in case. Got it. Makes sense. Um another thing to mention here um is for warpstream if you want the open source alternative there is a project called autoMQ um we haven't tested that but you guys can check it out you can also let us know how you how it works so it's essentially pretty much the same as warpstream um so you guys can check it Uh I guess red panda is also now open source so maybe that can be a good solution here. >> Uh a question in the chat um will there be an upgrade document to migrate from the current architecture to the new one? Um yes there will be. There is not yet. Um, and do you need to do data migrations? Um, there will there's no need to do a data migration. The format in object storage is not changing. So, you won't need to do a migration for all your historical data. Um, there's just a migration when switching uh to the new architecture. And there will be a document and a guide for that but it doesn't exist yet. >> And one piece of detail is that this migration would be a migration a documentation about a migration with down time. So we focus on that first. >> I'm not sure what our exact plan is yet. Um there is uh there's sort of there's two uh ways to migrate. One has downtime and is a lot simpler and the other one is a bit trickier but it doesn't involve downtime. Um GBD Nick, regarding your last question, um I'm not sure I get it, but >> uh are we going to get this new architecture in the mixing dash for alerts? >> Oh, uh yes. Um there are there are alerts uh for all the the relevant parts of the new architecture. Um there you know uh the dashboards reflect it if it's enabled. Um I'm not sure if there's like a you have to compile the mixin with like a ingest storage equals true um or if it just works for both architectures. Uh, I'd have to check, but yes, it will be included in the mix in Okay, that sounds good. Um, yeah, I saw your comments for the um for the meta monitoring. I assume any other questions, comments, or even feedback for the current um or the upcoming uh release. I >> would definitely encourage you to go look at the Mamir 3.0 O milestone um in GitHub. That's where we're tracking all the work. And there's a lot of stuff that's not super interesting or exciting, but it just uh might be good to make sure you know none of these changes will affect you or you or you're aware of them at least. I think there's additional question. Do we have plan to support is still ambient instead of increase engine X? I don't think we have a plan, right? >> Yeah, I don't think we have a plan. You can provide more context regarding why uh you want it and we can probably evaluate from there. Yeah, that sounds great. If you can come up with the PR so we can it's much easier to review from there. Um, any other questions before we go? All good. Um, okay. Um, thanks everyone for attending this community call and also thanks Nick Dear and everyone who answer your question. And if you have additional questions, feel free to post in the community channel especially regarding Mir 3. We will try our best to answer or put in the uh shared like the doc so other people can also refer from there. Um, if there are no more questions, thanks again and I will see you guys online. >> Okay, >> bye.

