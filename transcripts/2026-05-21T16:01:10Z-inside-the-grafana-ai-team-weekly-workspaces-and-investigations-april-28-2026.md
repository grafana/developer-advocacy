# Inside the Grafana AI Team Weekly: Workspaces and Investigations (April 28, 2026)

Published on 2026-05-21T16:01:10Z

## Description

This is an excerpt from a real AI team weekly meeting where we talk about the stuff we build and occasionally also demo them!

URL: https://www.youtube.com/watch?v=qts_fkMtdps

## Summary

The show is titled "Inside the Grafana AI Team Weekly: Workspaces and Investigations," and it aired on April 28, 2026. The speakers included Ben and Sonia, who discussed ongoing developments within the Grafana AI team. They introduced a new feature called "workspace home," aimed at enhancing user experience, and showcased a dependency graph for investigations that visualizes agent communication and error propagation. Key takeaways included the emphasis on UI enhancements and the importance of clear visualizations for understanding complex interactions within the system. 

Topics: Grafana AI, workspace home, investigations, dependency graph, UI enhancements.

## Chapters

00:00:00 Overview of the new workspace home feature
00:02:17 Demo of new dependency feature in investigations
00:03:50 Demonstrating visualization and navigation features

# Inside the Grafana AI Team Weekly: Workspaces and Investigations (April 28, 2026)

Welcome to the AI weekly, isn't it? Do we have any demos? 

Yeah, maybe you can start with the demo if that works. 

Yeah. Ben, do you want to dive in? I'll at least share my screen. 

So, um, you probably know we are working on a new feature called **workspace home**, which aims to allow the workspace to become the landing page of the assistant, kind of replacing and augmenting the experience that you've got at the moment. 

But you can see in front of me that work is ongoing, and I probably won't be ready to show you just yet. However, some of the bits that have arisen from it I've started to integrate, and I thought I'd show you a couple of bits from that now. 

Mostly, I've been thinking about how we get this **attract mode** for the trip team into the workspace. I'm also considering the different modes that the assistant supports. We’ve got this dropdown that lets you change different modes, and there's a cool little accent that goes on with some of them. 

So, I've been thinking about how we can use that. I'll go into Storybook to show you the actual components in isolation to begin with. 

We've got a new little picker for selecting between the different modes. What I've done is come up with the idea that these accent hues are now associated directly with the mode. The idea being that we can then use that as a touchpoint throughout the workspace UI. 

For example, the purple that we've got here for investigations is going to be surfaced wherever we're referencing investigations within the workspace. We don't yet surface any of the others, but when we get to that, we'll be able to do the same thing. 

And then, let's scroll up. Here's **attract mode**. A little quick demo if you've not already seen the PR. It surfaces the same way. Just some nice little glow effects because how are you supposed to know it's an AI unless it's got a rainbow glow halo? 

You can think it's mostly just a UI polish thing, but it gives you an indication of the direction we're going. It's probably going to be a Marmite choice, but there's a new icon for investigations, which is this little pentagon. 

Give me feedback if you hate it. Give me feedback if you love it. 

Nice. Thank you very much. I can demo one small thing that I really like about what Sonia worked on. She instrumented investigations with a new dependency feature, which lets you see the agents of the conversation as a graph. 

For example, you can see all the generations that are happening from the investigation lead, and then you can go to the start of that and see that, for example, over here, the lead is having some issues. 

If we continue this way, it makes it really clear—clearer than this one straight view—how agents communicate with each other. 

Regarding the dependency graph, let me show you a small one because you will see the propagation of errors. Let me show you. 

Yeah, why were some of those nodes red, by the way? That looks phenomenal. 

Because it was failing. So, this is a small one. We have here an evaluation that is failing, and you can see how this quality propagation is visualized here. All the downstream nodes are visualizing a warning with the upstream quality issue. This is because this evaluator is failing. 

You can also drill down, for example, to a soup duck. Here, it's small, but with the previous one that was bigger, you have the ability to do something like this. You can move through this map. 

For example, you can drill down here, and in this case, it makes more sense. You can also do this. 

I found this really useful because, for example, you don't know what this error is. What is the button, right? So, you see here the tooltip, but you can click on here and navigate directly to the button. 

And that's it. 

Well, that's amazing. It is a great kind of visualization because at a high level, you really do just see where problems are and then drill in. It looks great. 

Okay, well, that's all the time we have. But thank you very much, everyone, for another weekly. Please have a think about what you might like to demo next time. 

Thanks very much. Have a lovely rest of your Tuesday.

## Raw YouTube Transcript

Welcome to the AI weekly, isn't it? Do we have any demos? Yeah. Maybe you can start with the demo if that works, yeah. Yeah. Ben, do you want to dive in? I'll at least we can share my screen. So, um you probably know we are working on a new feature called workspace home, which the goal of which is to allow workspace to become the sort of the landing page of assistant to kind of replace and augment the experience that you've got at the moment. But, you can see in front of me. Um that work is ongoing and I'm probably won't be ready to show you just yet. But, uh some of the bits that have arisen from it I've uh started to integrate and I thought I'd show you a couple of bits from from that now. Um mostly I've been thinking about how we get this this attract mode um for the uh the trip team um into uh workspace. And I'm also thinking a little bit about these uh the different modes that assistant supports. So, we've got this drop down that lets you change different modes and there's a kind of there's a cool little uh accent that goes on with some of them. So, I've been thinking about how we can use that. I'll go into storybook to show you the actual components in uh isolation to begin with. But, um we've got a a new little picker for picking between the different modes. Um and I what I've done is I've come up with the idea that these these accent hues are now associated sort of directly with the mode. The idea being that we can then use that as a touch point throughout the workspace UI. So, the purple that we've got here for investigations is then going to be surfaced wherever we we're referencing investigations within workspace. We don't yet surface any of the others yet. But, when we get to that, we'll be able to do the same thing. And then let's scroll up. Here's attract mode. A little quick demo if you've not already seen the PR. It surfaces the same way. Yeah. Um just some nice little sort of glow effects because how are you supposed to know it's an AI unless it's got a a rainbow glow halo? You can think it's mostly got for now it's mostly just a UI polish thing. But, it's kind of give you an indication of the direction we're going. Um It's probably going to be a Marmite choice, but there's a new icon for assistant, which is this little Sorry, for investigation, but it's just a little little pentagon assist. Give me a feedback if you hate it. Give me a feedback if you love it. Um yeah. Nice. Thank you very much. I can demo one small thing that I really like about Sonia worked on. Uh she uh instrumented uh investigations with um such a new dependency uh feature basically, and that lets you see the agents of the conversation as a as a graph. Um so, here for example, you can see all the generations that are happening from the investigation lead, and then you can go to the the start of that basically, and see that for example, over here the the lead lead is having some issues. Um I think uh if we continue this way, it makes it really clear like clearer than this one straight view how how agents communicate with each other. Regarding the uh dependency graph, let me show you a uh a small one because you you will see the propagation of errors. Let me show you. Yeah, why were some of those nodes by the way? That looks phenomenal. Why were some of the nodes red? Because it was failing. So, this is Yes, this is a small one. So, we have here uh an evaluation that is failing, and you can see how this quality propagation is visualizing here. So, all the downstream nodes are visualizing a warning with the upstream quality issue. This is because this uh evaluator is failing. Yeah. And you can also um drill down, for example, to a soup duck. Like here. And here is because it's a small, but with the previous one that was bigger, it's like you have the ability to to do something like this. You can move through this map. And for example, you can drill down here and in this case makes more sense. And you can also you can also do this. I'm finishing. This is uh I found this really useful because for example, you don't know this this a arrow. What is the button, right? So, you you see here the the tooltip, but you can click on here and you go directly. You navigate to the button, no. And that's it. Well, that's amazing. It's a It is a great kind of visualization for cuz at high level you really do just see where problems are and then drill in. It's It's looks great. Okay. Well, that's all the time we have. But, thank you very much everyone for another weekly. Uh please have a think about what you might like to demo next time. Thanks very much. Have a lovely rest of your Tuesday.

