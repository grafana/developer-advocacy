# Inside the Grafana AI Team Weekly: AI Observability for the OTel demo and LLMSpec (May 12, 2026)

Published on 2026-06-01T15:00:29Z

## Description

This is an excerpt from a real AI team weekly meeting where we talk about the stuff we build and occasionally also demo them!

URL: https://www.youtube.com/watch?v=wD_vjDT61sQ

## Summary

The show is titled "Inside the Grafana AI Team Weekly: AI Observability for the OTel demo and LLMSpec," published on June 1, 2026. The speakers included members of the Grafana AI team discussing various projects and features. They highlighted the integration of AI observability into demo kits, improvements in the Grafana demo experience, and updates on the LLM spec harness for testing. Key takeaways included the introduction of new tools for managing guards, enhancements in agent workflows, and the ability to run comprehensive tests on plugins without needing to modify them.

Topics: AI observability, demo kits, Grafana demo, LLM spec, testing tools, agent workflows.

## Chapters

00:00:00 Integrating AI into demo kits
00:02:21 Updates on AI agent development and evaluations work
00:03:54 Overview of dashboard functionality and testing process

Okay. I'm sure it gets stopped and it doesn't make sense anymore. 

It's quite funny, I think, to get the date wrong, Rob, but still say, "May the 12th be with you." 

The final labs AI. 

Um, I want to demo something really quick again, please. We were working together with field engineering on integrating into the demo kits. So, demo kits and all the broad environments they're used for, like by all the GTM folks to do customer demos. The main app that generates all the traffic for the demos is the ultra demo. 

Our Grafana demo has this little chat down here, and you can ask a question. "What lyrics do you have? Do you know the lyrics of Nirvana?" Good job! Something like this, right? 

So, this is the EMEA demo kit. If you go to EMEA central, this stuff should now also be visible here. That's my conversation. I used it today in a demo. I think it's a bit easier to compare to using Grafana Assistant because it has fewer tools. It's also easier to show, for example, the kind of dependency graph because it's easier than investigations. I think we can really use that for better demos now. 

It has already also guards. So, if I ask it to tell me about competitors, this does not work because I have a guard that blocks anything related to competitors here. We will work next with field engineering to deploy some or provision some default guards that are very rated, so that's even easier to demo. 

Well, I'll tell you what, that is amazing. 

On feature stuff, we added a bunch. We have a new tool for the guard—that's actually what I demoed in the end weekly last week. It's especially useful for coding agents if you want to block, I don't know, removing your Etsy password file or something. Jack worked on something called experiments, which is basically the first version of offline invites. It's currently behind a feature flag. Sonia is working on agent click workflows, like surfacing that better, similar to the dependency view. Alexander is doing all kinds of very tedious ops work, which is very appreciated as well, of course. So, that's going good. 

Okay, up next is the evaluations work group. 

Cool, I can give the main update, which is we're working on this LLM spec new harness, both for the front end and for Loadstone. This is both in now. The nice thing is now that you can run the entire front end as a plugin and run any kind of scenario against it, including things that we weren't able to do, like testing, for example, suggesting cloud dashboarding and all that. 

You can see in this one, like it just did run, and it fully passed. This is also new; we can see both for the agent and the tool, and we also estimate thinking tokens as well—how much it's costing and where the time is being spent. 

If you look at the actual conversations, this is what we sent, and then this is what we get back. We also validate that we have the same fact grading that we use in all the bench; we brought that here as well. So, when it says something here, when it says a number, we actually check based on a known good query if that's actually true or not. 

So, this in UI is basically this. You can also go in the UI and check what it did inside there as well. I think at this point, dashboard one should have been finished. 

This one's also new, so dashboard one now will—like before, we used to stop here—now it will actually do whatever the plugin is doing. It will change mode, create the dashboard, and do the entire thing. This was a data my existence of doing this without changing the plugin. The good thing now is we can run the whole thing, and it will run exactly as the plugin does, so you don't need to worry about making changes to the plugin. If you rerun this again, it will use what that plugin does. Amazing! 

Get back. This tool is there; each way is there as well. 

Would it be possible, because as an engineer, how do we use it? What if I wanted to go and add a test for something? Could we maybe have a video just showing us how to do that? 

We'll do that. Essentially, I've also updated docs, so if you're using an agent, it should know about that and how to use the CLI. The whole thing is like add the YAML, then run the CLI, and then you should be good to go. 

Thanks, everyone. 

Thanks, everyone.

## Raw YouTube Transcript

Okay. I'm sure it gets stopped and it doesn't make sense anymore. >> It's quite funny I think to get the date wrong Rob but still say like May the 12th be with you. >> The final labs AI. >> Um I want to demo something really quick again, please. Uh we were working on uh together with field engineering on um integrating into into the demo kits. So demo kits uh and uh and all the broad environments they're used for like by all the GTM folks to do customer demos. And um the main main app uh that kind of generates all the traffic for the demos is the the ultra demo. And uh our Grafana demo has this little chat up down here and you can ask a question. Are you What lyrics do you have? Do you know the lyrics of Nirvana? Good Good job. Something like this, right? And then uh so this is the EMEA demo kit. If you go to EMEA central this stuff should now also uh be visible here. Uh so that's my conversation. Um I used it today in a demo uh I think it's it's a bit easier to uh compare to using Grafana assistant because it has less tools. Uh it's a bit easier to to also show for example the kind of dependency graph because it's easier than investigations. Um and I think we can really use that for for better demos now. It has already also guards. So if I ask it to uh tell me about competitors this does not work because I have a guard that blocks any everything or anything that is related to competitors here. Um but um we will work next with feed engineering to um deploy some or provision some default guards and that are very rated, so that's even easier to to demo. >> Well, I'll tell you what, that is amazing. >> Um on feature stuff, we added a bunch. Uh we have a new tool for the guard that's actually what I demoed in end weekly last week. Uh especially useful for coding agents if you want to block, I don't know, removing uh your Etsy password file or something, I don't know. Uh we have uh Jack worked on something called experiments, which is basically first version of offline invites. Um it's currently behind a feature flag. Uh Sonia is working on um on agent click workflows like surfacing that better uh like similar to the dependency view. Alexander is doing all kinds of very tedious uh ops works, which is very appreciated as well, of course. So, that's yeah, it's going good. >> Okay, up next is the evaluations work group. >> Uh cool, I can give um well, the main update, which is uh we're working on this LLM spec new harness both for the front end and for loadstone. This is both in now. So, the nice thing is now that you can run the entire front end this is a plugin and run any kind of like scenario against it. Um including things that we weren't able to do like, you know, test for example, like suggest cloud dashboarding and all that. So, um you can see in this one like it just did run run, it fully passed. Um this is also new like, you know, we can see both for the agent and the tool, and we also estimate thinking tokens as well, how much it's costing and like where the time is being spent. But then if you look at the actual conversations, so this is what we sent, and then this is what we get back Um and then we also validate like you know we we have like the same fact grading that we use in all the bench we brought that here as well. So like you know when it says something here when it says number we actually check based on a known good query if that's actually true or not. But so that this in UI is basically this. So you can also go in the UI and and check what it did inside there as well. Um and I think at this point uh >> dashboard one should have been finished. >> And this one's also new so dashboard one now will like before we used to stop here uh now it will actually do whatever the plugin is doing. So it will like change mode create the dashboard and do like the entire thing. Um this was a data my existence of like doing this without changing the plugin. Um but this is kind of like the good thing now is we can run the whole thing and it will run exactly as the plugin does so you don't need to worry about like you know making changes to plugin if you rerun this again it will use what that plugin does. Amazing. Get back. This tool is there each way is there as well. >> Would it be possible cuz as an engineer like how do we use it? What I still you know if I wanted to go and add a test for something and like could we maybe have a video just showing us how to do that? >> We'll do that. Essentially I've also updated docs so if you're using an agent it should know about that and how to use the CLI. But the whole thing is like add the YAML then run the CLI and then you should be good to go. >> Thanks everyone. >> Thanks everyone.

