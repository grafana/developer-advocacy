# Grafana Tempo:  Traces diff &amp; span pruning  (August 2026 Community Call)

Published on 2026-08-14T05:07:34Z

## Description

We will look at some new features: traces diff and span pruning Note: anywhere that may say trace-diff is now traces-diff.

URL: https://www.youtube.com/watch?v=FGpuZ4ul2hQ

## Summary

The show is titled "Grafana Tempo: Traces diff & span pruning" and was held on August 14, 2026. The speakers included Tiffany (host), Matt (MP of Tempo), Javi (developer at Tempo), and Jenny (developer on Tempo). The discussion focused on new features in Grafana Tempo, specifically the "traces diff" and "span pruning" functionalities. Key takeaways included the introduction of a deterministic method to analyze differences between traces, which aids in root cause analysis, and the implementation of span pruning to simplify trace visualization by collapsing repeated spans, thereby enhancing performance and usability. 

Topics: Grafana Tempo, traces diff, span pruning, Grafana CLI (GCX), observability.

## Chapters

00:00:00 Introduction of traces diff feature in Tempo
00:07:13 Overview of traces diff and span pruning in Grafana Tempo
00:13:18 Discussion on JSON schema and AI integration in Grafana Tempo
00:20:11 Introduction of span pruning feature in Grafana Tempo
00:26:26 Discussing span pruning and its benefits

Hello. 

Howdy, howdy. It's been a little bit since I've been on one of these. How has that been? It's now. Glad you're back. Thank you. Welcome everybody to the August community call for Tempo. It's kind of crazy; soon enough summer's going to be over. 

Winding down indeed. I like the nice weather. I'm not ready. I'm definitely ready for fall. I can't wait for summer to be over. What's your favorite weather? 

Something not summer, just because I live in Texas. 

Oh, yeah. Okay. Yeah. Um, fall. I think there's a difference in what people like weather-wise in general, but then also being where you are. The weather in the Seattle area is the best in the summer and part of spring, and rainy and sad otherwise, whereas like Texas or New York is insanely hot in the summer, and I'm like, yep. 

But yeah, it's been also a little bit since you've been on here, Jenny, too. So, welcome back in a little bit, but less long of a bit for you, Javi. 

Um, sorry, Tiffany. What was the question? 

Oh, I was saying it's... [laughter] It's been a little bit since you've been on here, too. 

Oh, yeah. Oh, yeah. I think two community calls? Yeah, not too long. Not too long. 

Going to be regular. 

Yeah. 

Cool. 

But yeah, hi if you're new. Hi if you've been here before. If you're new and you want to have... if you have any questions at any point in time, please ask questions in the chat. We'll try asking them throughout and our own questions, too. If you're unable for whatever reason to leave a comment, click on your profile image in the top right and create a channel, and then you will be able to ask all the things. 

So, yeah. We're going to be talking about traces diff and span pruning. Jenny and Javi, can you and Matt introduce yourselves a little bit for people who are new? 

I guess like for me, I'm a developer advocate for Tempo, Pyroscope, and AI things. 

Sure. I can go next. I'm Matt. You've seen me a lot here. I am the PM of Tempo. Which is somewhere over here. 

No, other side for me. 

Oh, really? Okay. That's intriguing to know. And I don't know what I'm doing there. Yeah, I just pointed things. 

The other PM. 

Somewhere here. I also have a developer role on Tempo. And that's not my full-time gig; just doing these video calls once a month. But yeah, I do a little bit of development. Javi. 

Yeah, I'm also a developer working at Tempo. I also work with GCX, which is the Grafana CLI. Today, I want to present you this trace diff and integration with the GCX. 

And yep. 

All right, I have to go after that. I'm just Jenny. I'm just purely a developer on Tempo. 

[laughter] 

Well, I'm going to throw it on the slides. 

Um, yeah, okay. So, we have been working on this new feature at Tempo for a very long time. We have been focusing on improving the performance of the database, making the queries faster, and moving from replication factor three to replication factor one to save some TCO. But this time we want to bring you something really new, which is this traces diff. 

The idea is simple. You can have a trace, or you can have two traces, but if you want to understand what happened from A to B, from trace A to trace B, you need something to compute the diff. These days, people can use LLMs to do that, but the result is not deterministic, and you are going to burn a lot of tokens. Probably it's not going to deliver the results that you are aiming for. 

So, basically, we are introducing this new functionality in Tempo, which is experimental for now. The idea is basically taking two traces, a baseline and a comparison, and seeing what has changed. This is pretty useful for root cause analysis or also for understanding what has changed, for example, an increase in latency, a new error, or a new service in between the calls. 

This is already implemented in the main branch, but not yet released. There are three ways to use it: you can use Tempo CLI, use two local JSON files, or use the new API endpoint, which is this API /B2 traces diff. Soon, you will have it in GCX and probably in the Grafana system as well. The Grafana system and DCS will help you to do this kind of traces analysis. 

The diff does is basically normalize first these spans, and then we do a match by service name, kind, and position to understand the structural differences between two traces. For now, we are providing three different outputs. Since this is an experimental feature, we don't want to focus on a single output. 

So, we have this trace patch, which is similar to a JSON patch, and we will give you the full list of changes. We also have the trace summary, native and composed, which is a summary that we create especially for the LLMs. So, LLMs can consume this output and understand what has happened. 

I can show you a sample of this. I have running Tempo on my machine. I already ingested two traces just for this. 

Can you make it slightly bigger? 

Um, I'm not sure because it probably breaks everything. Oh, yeah, it's working. 

Wow. 

So, we are doing a post operation against the Tempo new endpoint, and we are passing the base trace ID and the compare trace. The format is this trace patch that I already mentioned. 

Oh, yeah. Basically, you can see here the base trace has four spans, the compare one has five spans. Then you have a stats attribute that will tell you what has changed. And then we have this array of modified spans. 

And yeah, I have also here this example, which is pretty cool, I think. It's the same request, but using this summary output. Then we're going to pipe the response, the output, to Pi, which is AI Harness. We're also passing this prompt to summarize this trace diff, tell you the root cause, the blast radius, and next steps. 

I don't know how fast it's going to be because maybe we can try in the meantime. Yeah, it was pretty fast. 

Yeah, so this is the idea. The idea is that instead of using two full traces that can be like 50 megabytes each one and fill the whole AI context window, we are producing a small summary with all the meaningful information about what has changed, and the LLM has a very easy job to understand what has changed and what the next steps are. 

Yeah. That's everything from my side. Questions? 

Hey. Oh. Tiffany, you go ahead if you've got any. 

Um, can you go back to your slides? 

Yep. Here. 

Can you go back one more slide? 

This one? 

So, is there a way to actually visualize this in the UI, like how there's the colors happening here? 

Yeah, that's a very good question. We are working now to create a new UI in the drill down traces. It's still in progress, so I don't have anything to show, but yeah, it is in the pipeline. We would like to have something like this with nice colors and highlighting the differences. 

Yeah. 

I think that would be super helpful. I think the one thing that throws me off a little bit, at least with this diagram, is having things that are removed and things that are errors being the same, because those are two potentially completely different things. 

Yeah, exactly. For now, we have focused only on agents, not so much on real people, but yeah, we are on it. 

Cool. Um, you had mentioned GCX. What is... I think you said you even worked on it. Can you give me like the top-level overview of what GCX is? 

Yeah, GCX is the Grafana CLI. You can use it if you are a cloud customer, but also if you are an open-source user.

and it's a very good way to interact with all the Grafana endpoints, especially if you use it with an agent. You can tell the agent to use GCX to check those trace diffs, and it will do it on your behalf. It's very comfortable and useful. We use it every day internally as well.

Awesome. You mentioned this—oh, go ahead, Tiffany.

I was just going to say, to tie different products together, the last Pyroscope community call actually used GCX if people want to see it. It's cool.

And I think it just went GA.

Yeah, it was GA. I believe it was, what was it? I guess whenever I did this call. So, [laughter] in July, the week of July 30th, there were a bunch of new things for our AI week. So, yeah, GCX went GA, MCP went GA, and much other cool things.

You mentioned this is experimental. Does that mean it's in the cloud yet, or is it just experimental within the OSS?

Yeah, it is experimental, but it will be available for cloud customers probably next week.

Awesome.

Yeah. 

I want to talk about the output of the diff. I think you mentioned it's like you showed there with JSON. Are there multiple ways you can get different outputs, or is it all JSON?

No, the response is always JSON, but JSON has a different schema. The good thing about the summary is it doesn't grow in the same way as the patch format. So, even if you have two very big traces, the summary would be pretty small.

Okay.

But, yeah, the output is always JSON.

Do we have the summary kind of defined anywhere? Do we expect that it'll be pretty fluid and like things may change on it, or do we think the schema is relatively solid? Or at least we are going where it's additive instead of changing the whole world?

Yeah, I hope we don't change the schema too much, but obviously, this is mainly for LLMs to be consumed. So, I think it won't be that bad if we change it a lot or not because the LLM doesn't care about the real schema. But, yeah, we want to keep the patch one stable because this one is going to be the foundation of the UI.

So, that's probably a good indicator. Once we have a UI, it's probably going to be relatively stable. Until then, it's experimental for a reason.

Yeah, as is. Awesome.

Now, I noticed there's like a summary mode. Does that require any LLMs or hooks, or is that all native code?

Native code.

Everything is deterministic. Everything is in code.

Oh, awesome.

The LLM is just to interpret the output. I mean, you can read it by yourself, but, you know, these days, who does that?

We do have a question, it looks like.

Yeah.

Do you have any plans to integrate AI as a native worker to automate the resolution of alerts?

I think we already have something like that with the Grafana system. Correct me if I'm wrong.

We do. Does it automatically resolve it? That might be the thing I don't know. But we certainly have things that will categorize it and kind of automatically triage it.

This is not internal to Tempo. This is more of a Grafana offering. Yeah, we don't really do—currently, Tempo alerts are experimental, private preview, something along those lines. So, whenever those go GA, the other AI assist kind of options will probably roll into that.

Henry, I'm not sure if that fully answered your question. If it didn't, feel free to ask another.

I mean, technically, it's possible to integrate, I don't know, Alertmanager with Slack and AI using GCX, for instance. So, yeah.

Alerts are really flexible.

Yep. And like with this, is there a way, whether it's using the diff or not, to see an ASCII art version of what your traces look like?

Suraj, can you elaborate a bit more?

So, like, can you get a visual representation of what your traces look like using the CLI?

You mean like a Gantt diagram or something like that? Yeah, I think in GCX, there is a possibility to display traces, but I don't know. I will have to check. I know for sure that we do it for metrics, but I'm not sure for traces.

Let's do the most dangerous thing possible because you had a little demo there on the left pane where you're feeding it to pie.

We will try to—if you change the pie description to output me a graphical representation of the difference, what will it do?

I think if you go back on the left pane, you had the—when you were asking it to summarize.

Can you just ask it to make a graph of that or like a visual description of it and see what it does?

To the LLM, you mean?

Yeah, yeah, yeah. Let's just see what this does. This is why it's so dangerous. We are 100% doing this off the cuff. And it's LLM, so we're rolling the dice here.

I'm not sure if with the summary it's going to be able to do that, but let's try.

See what happens. Makes for good content, right? [snorts]

Moment of truth.

Yeah, yeah. They're all like, I don't know what you're asking here. Mermaid, and it just showed this picture of a mermaid. [laughter] Which would be amazing, actually. So that would be a win, too.

It reminds me of when Joe had first put in the Tempo MCP server and was asking it to make songs.

I have something.

Okay, we did get a mermaid. We [laughter] got a mermaid.

It gave us some next steps, so you know. This would probably render something reasonable. That's kind of cool.

Yep. [laughter and snorts] Awesome. Thank you for playing along there.

No problem.

All right, we'll give just maybe a minute or two just to see if any more questions come through, and then we will move on to our next guest, Jenny. Maybe you would hear me hum a bit just in the background.

If they ask questions afterward, we can find the time to answer some of the things in the end after Jenny's section as well.

All right. Yes, and feel free to ask questions during while people are going through things. We'd much rather have a conversation than a presentation. So, please ask any questions, and they don't have to be limited to the topic at hand. If you have any questions related to Tempo or Grafana, we will try to answer them.

All right. Let's get Jenny on stage here.

Done.

Boom.

Hello. Do I share my own screen?

Yeah, if you can get your screen up there, we will add it to the stage.

Cool.

Okay.

Hello. I'm Jenny again. For our feature today, we added the span pruning processor from OpenTelemetry into the read path of the trace by ID request. Definitely can paste that link. That'd be great. Basically, this solves the issue of having a giant trace with thousands of spans, many of which are repeated and look pretty much exactly the same. We want to collapse them so it's easier to view. 

Let me move all this. We do have new configs for this. The first one is pretty easy; it's just to enable it. Unfortunately, this is not yet available in the Grafana front end. This is why we introduced this feature, which is to make it enabled by default when you send a request. The new parameters for the trace by ID request are the span pruning, if you want your trace to be span pruned before it gets responded to you, and then the group by. The group by is basically if all of these spans have the same...

attribute. So for here, the default is `db`. If all the spans have the same `db.statement`, they'll be grouped together in one block. The minimum number of spans to get collapsed is two; if you only have one, it won't collapse into anything. The parent depth indicates how many levels from the collapsed spans you want to keep.

I'm going to show a quick demo here. Let me try to... Oops. Okay. Share the screen. This one. Okay. So, I guess I did a quick search for any traces that are big. I do have it already enabled by default to true. Span pruning is enabled by default to true. When I click it, all of these look like this because they're already collapsed. 

Let's see if this will work. This is just a mock-up. It is not available in Grafana yet, so please don't quote me on this. This is just a mock-up I'm doing for the demo. If we turn it off and refresh, this is what it looks like. Maybe let's do that even better, right? So, this is what it looks like. If you have span pruning turned on, again, this is not real; it's just for the demo. It will come out maybe soon, but this is what it looks like pruned. 

And I think that is it for my presentation. Does anyone have any questions?

>> Sorry, Matt. 
>> [laughter] 
>> I'll be there with you. 
>> It's quicker on the button than I was. 
>> [laughter] 
>> Still too, too, too add happy. 
>> [clears throat] 

I do have a few questions. So, what is the threshold for knowing what to prune? It comes from the span pruning processor, which I assume has some configuration and knobs. What's the lowdown there?

I'm not sure I understand your question.

So, how does it know what to prune? If I have five traces, do all of them get pruned?

Oh, sorry. This is on the read path only, right? So, whatever trace you're looking for, if you pass in the span pruning enabled to true, you will get a pruned span. Unfortunately, it's not available via UI yet, but it is available via the API. If you just pass in all the correct parameters, it will...

And what is the... So, you said it's read side, so this is lossless; nothing's getting deleted. This is only on the read side. Does that happen on the Tempo side or on the Grafana side?

On the Tempo side. Our idea is to make it easier to iterate over a trace, right? We're planning to cache the full trace, and then every time you make a query, you can... A little hint about we have another experimental feature coming for filtering the trace by TraceQL, right? So, let's say you have a giant trace, and you just want to know what happened to a certain part. You zoom in on that part. Before you zoom in on that, you have to prune it first, right? It makes it easier for you to navigate to the section you're interested in. If you have a trace with thousands of spans, you have to scan through all of those spans to know what part you might be interested in. But with this span pruning, you can easily collapse a lot of spans, so you're only left with the more important ones to scan through. 

A feature we're introducing a little bit later is allowing you to filter even further using TraceQL. You can filter by service name, span name, or whatever you want.

Cool.

Yeah, we're planning to do it so that if you find a span that you're interested in, it's already pruned, and you can directly unprune that single span to see all the more details.

I have a question. Are there any performance gains by using span pruning, or do the traces reach the front end faster?

Unfortunately, not now, but for the end user, it will be awesome. Imagine loading a trace with 20,000 spans; your browser is going to freeze before anything else happens. So, if you prune it first, you can still get important information from your trace without having to load thousands of spans. This was originally designed to help LLM use fewer tokens. If you use an API for this, it doesn't have to scan through 20,000 spans to get whatever information it needs.

I think this is also going to unlock a project that I'm just working on. I'll talk about it in a second. It's being able to raise the ceiling on how large a single trace can be. One of the problems we've had is that once you get a 50 or 100 megabyte trace, that can be something like one to two million spans, just based on the average size. So, if you try to load that in the UI, it just chokes. This ideally will allow you to actually use those in a reasonable manner. That's some exciting work that kind of unlocks that feature.

I also had a question on the UI, which you said is just entirely mocked up. I noticed there were black lines that kind of went through some of the gradients, and then there'd be a gap between them. I didn't know if that was a rendering artifact or something that was actually notifying something.

I think the lines are to notify that those spans were pruned.

Okay, awesome. So, you can see there how much of them were pruned.

Yes, that's only on the screen. This part down here is already in Grafana. This is not a mock-up; my only mock-up was just to be able to add the parameters up here. So yeah, this is already in Grafana. If you use the latest Grafana and have span pruning enabled by default to true, this will work.

Awesome.

You were talking about the lines that are on each of the spans, right?

Yeah, I think the things that look like the critical path.

This is what you're talking about, right? This black one?

Yeah. Oh yeah, it gives you a little helper text. That's nice.

Yeah, because that should just be stuff on the critical path usually.

That's actually something I had no idea existed before two months ago.

[laughter]

Is that for the critical path? Because it's hard to fully read? 

Yeah, I mean it does say that, but...

Yeah, because I think if you click the critical path filter, it would end up being just the...

I got to show one more thing. Oh my god. So yeah, when you click onto one of these pruned spans, you can see information about what spans were pruned, like how many spans were pruned, and then the histograms for the latency: min, max, average latency, and the total duration for this.

Cool.

Do you have any more questions?

I don't think I have any specific ones. I'm just thinking about all the cool stuff with this. Yeah, and then, Hobby, you were talking earlier about some stuff that would be potentially in later releases. At what point do you think it would be good to start talking to people about what the next release would even start being involved with?

Yeah, we would like to release a new version soon, especially because people want to have more ways to connect with Kafka endpoints. I don't know yet the timeline, but we are preparing a small one soon. I don't know if all of this trace diff would be non-experimental for them, but hopefully, yes.

Awesome. Thanks so much. For folks, if you end up having questions after this call, feel free to ask them on YouTube, which is probably where you're looking at this, or we also have slack.grafana.com, which is our community.

Slack has a bunch of different channels. There's also a forum, which is community.grafana.com. 

Does anyone else have anything before we end this episode and come back in the next one? 

[snorts] 

I guess that's enough. 

Okay. Thanks, everybody. See you next time. 

Bye-bye. 

Bye.

## Raw YouTube Transcript

Hello. >> Howdy, howdy. >> It's been a little bit since I've been on one of these. >> How has that been? >> It's now. >> Glad you're back. >> Thank you. Welcome everybody to the August uh community call for a Tempo. It's kind of crazy. Like soon enough summer's going to be over. >> Winding down indeed. >> I like the nice weather. I'm not ready. I'm not ready. >> I'm definitely ready for fall. >> I can't wait for summer to be over. What's your favorite weather? >> Something not summer, just because I live in Texas. >> Oh, yeah. Okay. Yeah. Um >> Fall. >> I think I think there's a difference in what people like weather-wise in general, but then also being where you are. Like the weather on in Seattle area is the best in the summer and part of spring and rainy and sad otherwise, whereas like yeah, like Texas or like New York is insanely hot in the summer and I'm like, yep. But yeah, it's been also a little bit since you've been on here, Jenny, too. So, welcome back in a little bit, but less long of a bit for you, Hobby. >> Um uh sorry, Tiffany. What was the question? >> Oh, I was saying it's >> [laughter] >> It's been a little bit since you've been on here, too. >> Oh, yeah. Oh, yeah. Uh I think two community calls? Yeah, not not too long. Not too long. >> Going to be regular. >> Yeah. >> Cool. >> But yeah, uh hi if you're new. Hi if you're if you've been here before. If you're new, um and you want to have if you have any questions at any point in time, please ask questions in the chat. And we'll try asking them throughout and our own questions, too. If you're unable for whatever reason to leave a comment, click on your profile image in the top right and create a channel, and then you will be able to ask all the things. So, yeah. We're going to be talking about trace stiff and span pruning. Jenny and Javi, can you and Matt, if you all want to introduce yourselves a little bit for people who are new. I guess like for me, developer advocate for Tempo, Pyroscope, and AI things. >> Sure. I can go next. I'm Matt. You've seen me a lot here. I am the MP of Tempo. Which is somewhere over here. >> No, other side for me. >> Oh, really? Okay. That's intriguing to know. And I don't know what I'm doing there. Yeah, I just pointed things. >> The other MP. >> Somewhere here. I also have a developer on Tempo. And that's not my full-time gig, just doing these video calls once a month. But yeah, I do a little bit of development. Javi. >> Yeah, I'm also a developer working at Tempo. I also work with GCX thing, which is the Grafana CLI. Today, I want to present you this trade diff and integration with the GCX. And yep. >> All right, I have to go after that. I'm just I'm just Jenny. I'm just purely a developer on Tempo. >> [laughter] >> Well, I'm going to throw it on the slides. >> Um yeah, okay. So, um we have been working on this new feature uh at Tempo for a very long time. We have been focusing just on the improving the performance the performance of the database, making the queries faster, um um and moving from replication factor three to replication factor one to save some TCO. But, uh this time we want to bring you something really new, which is uh this Tracediff. Um the idea is simple. Um you can have a trace, or you can have two traces, but if you want to understand what happened from A to B, from the trace A to the trace B, you need something to compute the diff. Um these days, people can use LLMs to do that. But, the result is not deterministic, and you are going to burn a lot of tokens, um probably it's not going to deliver the uh results that you are aiming for. So, basically we are uh introducing this new uh functionality in Tempo, which is uh experimental for now. Um yeah, the idea is basically taking two traces, a baseline and a comparison, and see what has changed. Um this is pretty useful for root uh root analysis, or also for understanding what has changed it uh for example, an increase in the latency, or a new error, or a new service in in between the calls. Um yeah. So, this is already implemented in main branch, uh not yet released. Um there are like a three ways to um to use it. Uh you can use Tempo CLI, um use two local JSON files. You can also uh use the new uh API endpoint, which is this API {slash} B2 traces diff. Um soon, you will have it in GCX and probably in the Grafana system as well. So, the Grafana system and DCS will help you to do this kind of traces analysis. Um I'm making this um investigation better. Um the different what it does is basically normalize first these spans and then we do a match by service name, kind, and position to understand the structural differences between two traces. Um and yeah, we for now we are providing three different outputs. Since this is an experimental feature, we don't want to be uh like a focusing on a single output. So, we have this trace patch, which is um similar to a JSON patch, and we will give you the full um list of changes. We also have the trace summary native and compose, we call it, which is a summary that we um create especially for the LLMs. So, LLMs can consume this output and understand what has happened. Um I can show you a sample of this. Um so, I have running Tempo on my machine. Um I already ingested two traces just for this um >> Can you make it slightly bigger? >> Um I'm not sure because uh probably breaks everything. Oh, yeah, it's working. >> Wow. >> Um so, we are doing a post a post operation against the Tempo new endpoint, and we are passing the base trace ID and the compare trace. And the format is this trace patch that I already mentioned. Um Oh, yeah. Basically, you can see here um the base the base trace has four spans, the compare one has five spans. Then you have a stats attribute that we will tell you what has changed. And then we have this array of modify um spans. Um And yeah. And I have also here this example, which is pretty cool, I think. It's the same the same request, but using this summary output. And then we're going to pipe the response, the output, to Pi, which is um AI Harness. And then we're passing also this prompt to summarize this trace diff tell you the root cause and the blast radius and next steps. Um I don't know how fast it's going to be because maybe we can try at the meantime. Yeah. It was pretty fast. Um Yeah, so this is the idea. The idea is that instead of using two full traces that can be like a 50 megabytes each one um and fill the whole AI context window, we are producing on a small summary with all the meaningful information about what has changed um and the LLM has a very very easy job to understand what has changed and what are the next steps. Um Yeah. Um That's everything uh from my side. Question? >> Hey. Oh. Tiffany, you go ahead if you've got any. >> Um if you Can you go back to your slides? >> Yep. Here. >> Can you go back one more slide? >> This one? >> So, um is there a way to like actually visualize this in the UI, like how there's the colors happening here? >> Yeah, that's a very good question. Uh we are working now to we to create a new UI in the drill down traces. It's a still in progress, so I I don't have uh anything to show, but uh yeah, it is in the pipeline. We will We would like to have something like this with nice colors and highlighting the differences. Um Yeah. >> Yeah, I think that would be super helpful. I think the one thing that throws me off a little bit, at least with this diagram, is having um things that are removed and things that are errors being the same, cuz those are two potentially completely different things. >> Yeah. Exactly. Yeah, for now we have focused only in agents, not [snorts] so much in real people, but uh yeah, we are on it. >> Cool. Um you had mentioned GCX. What is I think you said you even worked on it. Uh can you give me like the top-level overview of what GCX is? >> Yeah, GCX is the Grafana CLI. Um you can use it if you are an a cloud customer, but also if you are an open source user. Um and it's a very good way to interact with all the Grafana endpoints and especially if you use it with an agent. So, you can tell the agent to use GCX to check those trace diff and he will do it on behalf. Um yeah, it's very comfy. It's uh very useful CLI. Uh we use it every day internally as well. >> Awesome. Uh you mentioned this Oh, go ahead, Tiffany. >> I was just going to say the to tie different product or mention different products and stuff things. Um the last Pyrescope community call was actually using GCX if people want to see it. It's cool. >> Uh and I think it just went GA. >> Yeah, it was uh GA. I believe it was What was it? I guess whenever I did this call. So, >> [laughter] >> um July the week of July 30th, there was a bunch of new things um for our AI week. Um so, yeah, GCX went GA, MCP went GA. >> Awesome. >> Much other cool things. >> Uh you'd mentioned this is experimental. Does that mean it's in cloud yet or is it just experimental within the OSS? >> Yeah, it is experimental, but it's already uh it will be available for cloud customers probably next week. >> Awesome. >> Yeah. >> Uh I want to talk about the >> It it won't be it won't be a release it or release it won't be GA uh for open source user till the next release, probably. >> Got you. Um you mentioned the output of the diff. Uh I think you mentioned it's like uh you you showed there with JSON. Is there multiple ways you can get different outputs or is it all JSON? >> Um No, the response is always JSON, but JSON has like a different uh schema. So, this is the summary. The good thing about the summary is it doesn't grow in the same way as the, uh, patch format. So, even if you have two very big traces, the summary would be pretty small. >> Okay. >> But, yeah. Um, the output is always, uh, JSON. >> Do we have the summary kind of defined anywhere? Like, do we expect that it'll be pretty fluid and like things may change on it, or do we think the schema is relatively solid? Or at least we are going where it it's additive instead of like changing the whole world. >> Yeah, I hope, uh, we don't change, uh, too much the schema, but, um, obviously, this is, uh, mainly for LLMs to be consumed. So, I think it won't be that bad if we change it, uh, a lot or not. Because, uh, the LLM doesn't care about the >> [laughter] >> about the real schema. But, yeah, we we want to keep the patch one. We want to keep it as stable because, uh, this one is going to be the foundation of the UI. >> So, that's probably a good indicator is once the UI is once we have a UI that it's probably going to be relatively stable. Um, and until then it it it's experimental for a reason. >> Yeah, as as it Awesome. >> Uh, now, I noticed the the there's like a summary mode. Does that require any like LLMs or hooks, or is that all, um, native code? Native code >> Um, everything is, um, deterministic. Everything is, uh, in code. >> Oh, awesome. >> The LLM is just to interpret, uh, the output, um. I mean, you can read it by yourself, but, uh, you know, these days who does that? >> Uh, we do have a question, it looks like. >> Yeah. >> Uh, I'm >> Do you have any plans to integrate AI as a native worker to automate the resolve alerts? >> I think we already have something like that with the Grafana system. Correct me if I'm wrong. >> We do. Uh Does it automatically resolve it? Might be the thing I don't know. Um but we certainly have things that will categorize it and um kind of automatically triage it. >> Mhm. >> This is not internal to Tempo. Uh this is more of a I guess like a Grafana offering. Um Yeah, we don't really do Currently we we uh Tempo alerts are um experimental private preview something along there. Um so whenever those go GA, the other AI assist kind of options will probably roll into that. >> Mhm. >> Uh Henry, I'm not sure if that fully answered your question. Uh and if it didn't, feel free to ask another. >> I mean, technically it's uh possible to integrate, I don't know, alert manager with a Slack and AI using GCX, for instance. So, yeah. No. >> Alert are really flexible. >> Yep. >> And like with this, is there a way like whether it's using the diff or not, but to like see like I don't know, ASCII art version of what your traces look like? >> Um Suraj, can you elaborate a bit more? >> So like can you get a like using the CLI, can you see a visual representation of what your traces look like? >> You mean like a Gantt diagram or something like that? Yeah, I think in GCX, there is a possibility to display traces, but I don't know. I don't know. I will have to check. I know for sure that we we do it for matrix, but I'm not sure for traces. >> Let's do the most dangerous thing possible cuz you had a little demo there on the left pane where you're feeding it to pie. >> We will try to >> If you change the pie description to output me a graphical representation of the difference, what will it do? >> Mhm. >> I think if you go back on the left pane you had the the when you were asking it to summarize. >> Mhm. >> Uh can you just ask it to make a graph of that or like a visual description of it and see what it does? >> To the LLM you mean? >> Yeah, yeah, yeah. Let's just see what this does. This is why it's so dangerous. We 100% uh doing this off the cuff. And it's LLM, so we're rolling the dice here. >> I'm not sure if with the summary it's going to be able to do that, but let's try. >> See what happens. Makes for good content, right? >> [snorts] >> Moment of truth. >> Yeah, yeah. They're all like, I don't know what you're asking here. Mermaid and it just showed this picture of a mermaid. Um [laughter] which would be amazing actually. Uh so that would be a win, too. >> It is It reminds me of when Joe um had first put in the Tempo MCP server and was asking it to like make songs. >> I have something. >> Okay, we did get a mermaid. We [laughter] got a mermaid. >> Uh >> It gave us some next steps, so you know. This would probably render something reasonable. Uh that's kind of cool. >> Yep. >> [laughter and snorts] >> Awesome. Thank you for uh playing along there. >> No problem. >> All right, we'll give just maybe a minute or two just to see if any more questions come through and then we will move on to our next guest, Jenny. Maybe you would hear me hum a bit just in the background. >> if they ask questions afterwards we can find the time to answer some of the things in the end after Jenny's section as well. >> All right. Uh yes, and feel free to ask questions during um while people are going through things. We're more than we'd much rather have a conversation uh than a presentation. So, please ask any questions and they don't have to be limited to the topic at hand. Uh if you have any questions related to Tempo or Grafana, we will try to answer them. All right. Uh let's get Jenny on stage here. >> Done. >> Boom. >> Hello. Do I share my own screen? >> Yeah, if you can get your screen up there we will add it to the stage. >> Cool. >> Okay. >> Hello. I'm Jenny again. But um so for our feature today I we added the span pruning processor from Otel into the read path of the trace by ID request. Um definitely can paste that link. That'd be great. Um but basically this what this solves is if you have a giant trace with thousands of spans and a lot of them are repeated, they look pretty much exactly the same. Um so Do want to collapse them so it's easier to view? And And then So Let me move all this. So we do have new configs for this. The first one is pretty easy. It's just to enable it. To enable the feature and then I'm So unfortunately this is not yet available in the Grafana front end yet. This is why we introduced this feature which to make it enabled by default when you send a request. Um And the new parameters for the trace by the request are the span pruning. If you want to your trace to be span pruned before it get responded to you. And then the group by. The group by is basically if all of these spans have the same attribute. So for here the default is db. So db if all this the spans have the same db. statement they'll be grouped together in one block. And then the minimum So the minimum number of spans um to Wait. To get collapsed. If you only have two or one it won't collapse into anything, right? And then the parent depth um basically however many level from the collapsed spans you want to keep. Uh so I'm going to show a quick demo here. Let me try to Oops. Okay. Share the screen. This one. Okay. So right. I I guess I did a quick search for any traces that are big. And I do have it already enabled by default to true. Span So it's spanning span pruning enabled by default to true. So, when I click it, all of these um look like this cuz they're already collapsed. And let's see let's see if this will work. So, this is just a mock-up. It is not available in Grafana yet, so please don't quote me on this. This is just a mock-up. I'm doing this for the demo. So, if we turn it off, refresh, this is what it looks like for. Maybe let's do that even better, right? So, this is what it looks for. And then if you have span pruning turned on, again, this is not real. It's just for the demo. Uh it will come out maybe soon, but and then and this is what it looks like um pruned. And I think that is it for my presentation. Does anyone have any questions? >> Sorry, Matt. >> [laughter] >> I'll be there with you. >> It's quicker on the button than I was. >> [laughter] >> Still too too too add happy. >> [clears throat] >> Uh I do have a few questions. So, what is the like threshold for knowing what to prune? Like uh it comes from the span pruning processor, which I assume has some configuration and knobs. Um so, what's the like lowdown there? >> I'm not sure I understand your question. >> So, like how does it know what to prune? Like if I have like five traces, right? Like uh do all of them get pruned? Is it like um >> Oh, sorry. So, this is on the read path only, right? So, whatever trace you're looking for, if you pass in the span pruning enabled to true, you will get a pruned span. Um but yeah, like I said, unfortunately, it's not available via UI yet, but it is available via the API. So, if you just pass in the all the correct or all the parameters, it will >> And what is the um So, you said it's read side, so this is lossless, like nothing's getting deleted. This is only on the um read side. And does that happen on the Tempo side or on the Grafana side? >> On the Tempo side. So, our idea actually is to make it easier to iterate over a trace, right? So, we're planning to cache the trace, the full trace, and then every time you make a query, you can um I mean, a little hint about we have a another feature experiment feature coming for filtering the trace by uh trace QL, right? So, let's say you you have a giant trace, right? You just want to You know, I don't know what happened to a certain part. So, you zoom in on that part. So, before you zoom in on that, you have to prune it first, right? So, it's make it easier for you to navigate in what section you're interested in. If you have a trace with thousands of traces, you have to scan through all of those spans, right? To know what part you might be interested in. But with this span pruning, you can easily um because it collapse a lot of spans, you're only left with like the more important ones to scan through. And then um a feature we're introducing a little bit later is we're allowing you to filter even further using trace QL. So, you can filter by service name or span name, whatever you want. >> Cool. >> And uh yeah, we're we're planning to do it so that if you find a a span that you're interested in, it's already pruned, you can directly just unprune that single spans, so you can see all the more details. >> Um I I a question. Um so, are there any performance uh gains by using these fun pruning or the traces reaching the front end faster or >> Uh unfortunately not now, but for the end user it will be awesome because imagine loading a trace with like 20,000 spans, right? That your browser is going to freeze before anything else happen. So, if you prune it before you can still get important information from your trace without having to load thousands of spans. And this originally was designed for to help LLM use less tokens, right? So, again if you use an API for this, it doesn't have to scan through 20,000 spans basically to get whatever information it needs. >> Yeah, I think this is also going to unlock a project that I'm just working on. So, I'll talk about it in a second. Is the being able to raise the ceiling on how large a single trace can be because one of the problems we've had is once you get like a 50 or 100 megabyte trace, that can be something like one to two million spans just going based on the average size. So, like you try to load that in the UI and it just chokes. Um so, this ideally will allow you to actually be able to use those in a reasonable manner. Um so, that's some exciting um work that kind of unlocks uh that feature. >> Yeah. >> I also had a question on the UI. Um which you said is just entirely mocked up, but I but I noticed there were black lines that kind of went through some of the gradients and then there'd be like a gap between them. I didn't know if that was a rendering artifact or like something that was actually like um >> Maybe channel >> notifying something maybe. >> I think this the lines are to notify that those bands were pruned. >> Okay, awesome. So you kind of can see there like how much of them were pruned. >> Yes, that's only on the screen. It's more or so. So this part down here is already in Grafana. This is This is not a mock up. My only mock up was just to be able to turn the to add the parameters up here. Um so yeah, this is already in Grafana. So if you use the latest Grafana and you have um the span prune enabled by default true, this will work on it. >> Awesome. >> And you you were talking about like the lines that are on the each of the spans basically cuz >> Yeah, I think >> the things that look like the critical path on basically. >> This is what you're talking about, right? This black one? >> Yeah. Oh yeah, it gives you a little helper text. That's nice. >> Yeah, so cuz that should just be stuff on the critical path usually. >> That's actually something I had no idea existed before 2 months ago. >> [laughter] >> Is that for critical path cuz it's hard to fully read? Uh yeah, I mean it does say that but um >> Yeah. Cuz like I think if you click the critical path filter, it would end up being just the >> I got to show one more thing. Oh my god. So yeah, when you click onto one of these pruned spans, you can see information about what spans were pruned, like how many I think it's how many spans were pruned, right? And then the histograms for the latency, min max min max average latency. Uh the total duration for this. >> Cool. >> Do you have any more questions? >> I don't think I have any specific ones. I'm just like thinking about all the cool stuff with this. Yeah, and then uh Hobby, you were talking earlier um about uh some stuff that would be potentially in like later and then like things that would be in the next uh release. So, like at what point do you think would be good to start talking to people about what the next release would even like start being involved with? >> Um yeah, we we would like to release a new version soon uh especially because people want to have more ways to connect with Kafka endpoints. Um so, I I don't know yet the timeline, but um yeah, we we are preparing on a small one uh soon. I don't know if all of this of the trace diff would be non-experimental for them, but um yeah. Hopefully, yes. >> Awesome. So, thanks so much. Um and yeah, for folks if you end up having questions uh after this call, uh feel free to ask them in YouTube, which probably is where you're looking at this. Um or we also have uh slack.grafana.com, which is our community slack. Um so, there's a bunch of different channels there. Um there's also a forum, which is community.grafana.com. Um so, yeah, just anyone else have anything else uh before we end this episode and come back in the next one? >> [snorts] >> Guess that's enough. Okay. >> Okay. >> Thanks, everybody. See you next time. >> Bye-bye. >> Bye.

