# Inside the Grafana AI Team Weekly: Guards for AI Observability (May 5, 2026)

Published on 2026-05-25T15:00:07Z

## Description

This is an excerpt from a real AI team weekly meeting where we talk about the stuff we build and occasionally also demo them!

URL: https://www.youtube.com/watch?v=5ZfAILBR74g

## Summary

In this weekly update video, Sven discusses ongoing improvements in user experience (UX) and operations (ops), specifically focusing on a feature called IcoGuard. He provides a demonstration of its functionality, which aims to enhance security by blocking certain user prompts that could lead to prompt injections. The feature utilizes evaluators to assess user messages, with the capability to implement multiple criteria for different agents. Sven mentions that the current demo includes a guard that blocks messages containing specific phrases, while also expressing plans to develop additional features like automatic redaction of sensitive information. The conversation concludes with a light-hearted note about creating a video that avoids specific brand mentions.

## Chapters

00:00:00 Introductions  
00:01:15 Discussion about demoing features  
00:02:00 Introduction to IcoGuard feature  
00:03:30 Overview of evaluators and their function  
00:04:45 Explanation of synchronous guards for prompt injections  
00:05:30 Live demo of the guard functionality  
00:06:15 Demonstration of blocking user messages containing specific content  
00:07:00 Explanation of Sigil as a security framework  
00:08:30 Discussion on transforming messages for PII reduction  
00:09:15 Closing remarks and future video ideas

# Weekly Update

Hello, welcome to the weekly meeting. Sven, you mentioned demoing something. What do you think?

Yeah, you can go to the Sigils slide for that if you want. It's related to that. There it is. I think in general, we are at the point where we are doing both UX and ops improvements. We saw some rumors yesterday, and we're working on that.

I'm mostly working on a feature called **IcoGuard** at the moment. I shared a video about that last week, but I want to take the opportunity to demo it again. 

So, it is a bit broken. I have some mentions of fixing it at the moment, but something is working that I can demo. We have these evaluators that were basically just running asynchronously whenever a condition was true, mostly for user messages like prompts in the assistant. I thought, why not make this something synchronous and kind of blocking to have guards in place for prompt injections or whatever.

My small demo is not exactly for prompt injection because that's broken, but I have an evaluator that's just testing if a user message contains "data dog is cool." Additionally, to this evaluator, I have a guard set up that uses this evaluator. The guard can contain multiple evaluators and can match more criteria, allowing different evaluators to be matched to different agents, for example.

I could just search under the graph in the assistant here. I think it can't save because that's broken... Yes, perfect! Hopefully, I didn't break it now. 

However, to see it in action, it's enabled and deaf. You can just normally use the assistant as usual. If your prompts don't contain "data dog is cool," everything is working. But if they do, this will be blocked by the guard that's in place in Sigil. I think that's a great use case for using Sigil as a kind of security framework for these things like prompt injections.

Something I'm working on at the moment is not just denying stuff, but actually transforming messages, i.e., PII reduction or secret reductions. For example, if you paste a secret key in your user messages in the assistant, the transform could then automatically redact it before the secret is leaked to the LLM. 

I think that's pretty interesting. 

Yeah, very good. That's a really powerful feature. It might be nice to get a video of that that doesn't mention "data dog." 

Oh, yeah. I can do "New Relic." 

Yes, we're going to do all of them. 

Thank you very much, everyone. Great chat today. See you soon!

## Raw YouTube Transcript

Hello, welcome to the weekly. So, Sven, you mentioned essentially demoing something. What do you think? Yeah, you can go to the Sigils slide for that if you want. Uh it's related to that. Um There it is. I think in general we are at the point where we are doing both UX and and also already ops improvements. Uh we we see some um some rumors yesterday and such and uh we're working on that. And I'm mostly working on a feature called IcoGuard at the moment and I I shared a video about that last week, uh but I want to take the opportunity and demo it as well again. All right. So, uh and it is a bit broken. I have some mentions fixing it at the moment, but at the moment but something is working that I can demo. So, um we have these evaluators that were basically just running um asynchronous um whenever a condition was true, mostly for user messages like you prompt in the assistant and stuff. Uh and I thought why not make this something synchronous and kind of blocking to yeah, have guards in place for prompt injections or whatever. Uh my small demo is not like the prompt injection because that's broken, but I have an evaluator that's just testing if a user message contains a data dog is cool. And I have a um additionally to this evaluator, I have a guard set up um which basically just uses this evaluator. So, the guard as as if can contain multiple evaluators and can can match more criteria to match more like different evaluators to different agents, for example. So, I could just search under graph on the assistant here. I think it can't save because that's broken. Yes. Perfect. Hopefully, I didn't break it now. Uh however, um to see it in action, it's enabled and deaf. Uh, so you can test uh, you can just normally use the assistant um, as as normal uh, if if your prompts don't contain data dog is cool. Everything is working, but if they do, uh, this will be blocked hopefully. Yeah, this will be blocked by this by this guard that's in place in Sigil. And it um, um, and I think that's yeah, that's a great use case to use uh, Sigil as kind of a security um, firewallish uh, framework um, for these things like prompt injections. Something I'm working on at the moment is um, not just denying stuff, but actually transforming messages um, i.e. uh, at PII reduction or or secret reductions. So if you paste a a secret key in in your user messages in the assistant, the transform could then automatically redacted before the secret is leaked to the to the LLM. Um, yeah. I think that's it's pretty pretty interesting. Yeah, very good. Yeah, really powerful feature. Um, might be nice to get a video of that that doesn't mention data dog. Oh, yeah. I can do um, New Relic. Yeah, I We're going to do all of them. Yes. From here. Thank you very much everyone. Great chat today. See you soon.

