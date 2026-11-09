# How To Improve Your Agent Using Grafana GCX &amp; Agent Observability

Published on 2026-09-19T00:17:47Z

## Description

In this video, Jack shows how to improve your Agent using GCX and Agent Observability. For this demo, he uses a simple Agent to ...

URL: https://www.youtube.com/watch?v=N3X3czskm1Y

## Summary

The show is titled "How To Improve Your Agent Using Grafana GCX & Agent Observability," published on September 19, 2026. The speaker, Jack from Grafana, demonstrates how to enhance an agent using Grafana's GCX and agent observability features. He showcases the process of analyzing agent performance through conversations and experiments, comparing different models like Haiku, Sonnet, and Opus, and discusses the trade-offs in performance and cost associated with each. Key takeaways include the utility of the GCX CLI for pulling conversation data and experiment results, as well as the importance of iterating on agent improvements based on observed performance metrics.

Topics: Grafana GCX, Agent Observability, agent performance, model comparison, CLI tools.

## Chapters

00:00:00 Using GCX for agent observability
00:02:20 Comparing performance of different models in Grafana Agent
00:05:22 Using GCX for agent improvement and experiment analysis

[music] 

Hey everyone, it's Jack from Grafana here, and today I'm going to be showing you how to improve your agent using GCX and agent observability. For this demo, I just have a simple agent here to help me improve my Fantasy Premier League team, which didn't start out so hot this season. 

I'm just going to go ahead and ask it, "How did my team do week one?" I have my team ID here on the left, so it has the context to pull my team and give me a little breakdown. Awesome! I had it call a tool to get my Premier League team, and then it gave me some breakdowns here. 

So, what does this look like in the Grafana backend? I've instrumented my agent with agent observability. I'm going to pull up the agent observability page where I can see a breakdown of some of my costs and usage, but I want to really see the actual content of the conversation that I pushed. 

If I go ahead and refresh here, "How did my team do week one?" is showing up. Awesome! I can see the workflow breakdown of the agent calling a tool and back, and then I can see the content of the conversation, including the tool input and output and then the response. 

But let's say I was a developer working on this agent and I wanted to improve it. At this point, I would go into my own coding agent and ask it to pull some conversations and suggest some improvements. How would I do that? We have this new CLI from Grafana called GCX, which can do exactly this. 

If I go to my terminal here, I can say `GCX conversations list`. Awesome! You can see the breakdown is very similar to what you would see in the UI, and it lists the latest conversations I have. If I wanted to pull the conversation that I just had, I can do `conversations get`. 

I can see the conversation contents here. What's super useful about this is when I fire up my coding agent, I can ask it, "Can you use GCX and my Jack personal stack to pull the latest 10 conversations?" We'll give it a second here to start up and pull some conversations. 

Reading GCX here. And there we go! It's going to list the latest conversations. Awesome! Doing some discovery. And there we have the latest 10 conversations appear here. I could do things like, "Can you pull specific ones, suggest improvements?" These types of things. 

But what I'm actually interested in for this demo agent is how it'll perform with different models. You know, something using Sonnet versus Haiku versus Opus and how that would affect performance. So, let's do this. I set up an experiment where I had a test suite of 20 different input and output cases. 

Things like captain advice where the input is, "Who should I consider captaining?" and the expected value is it recommends one player. I also compared Salah versus Cole Palmer this week and looked at budget defenders. So, 20 different cases here. I invoked an experiment through Grafana agent observability to look at how my agent would do with Haiku versus Sonnet versus Opus. 

If I hit compare runs here, I can see that for these cases, it looks like Haiku had the worst pass rate. Sonnet improved it, and Opus did the best. But if you look at the cost, as expected, Opus cost the most, then Sonnet was a little less, and Haiku was super cheap. 

These would be considerations I would make when improving my agent or choosing a model. There are different trade-offs. Obviously, you get a little bit better performance with Opus, but maybe you could get the same kind of performance out of Haiku if you change the prompt a little bit. 

So, how would I go about doing this? I would say, go to my coding agent and say, "Can you pull..." Actually, I have a prompt prepared here for pulling experiments. Here we go. It'll say, "Use read-only GCX commands with my personal stack," and gives the experiment IDs that I have to compare the pass rate, average score, failure patterns, and give me a breakdown. 

It's pulling these experiments right here. It has some truncated output. If we go to this, you can actually see a breakdown of the scoring here. If I click into any of these individual experiment runs, I can see the cost, etc. But I can also see the conversation that occurred. 

If I click into the conversation, I can see the input and then what the agent said. I can also see the grader transcript. I've instrumented the judges associated with this experiment, so I can see the actual grading input and output. I can really verify that the graders did a good job. 

Let's go back to our agent and see what it did. It looks like it pulled the experiments and did a more detailed breakdown for me, which is super nice because sometimes these outputs of experiments can be a little hard to sift through to find the important information. 

You can see it does a breakdown of tokens, the different results, best overall, and then some different weaknesses and suggested improvements. My next step here would be to test out some improvements by making a change to the agent and then running a new experiment to see if it improves the results. 

The point of this demo is just to show how powerful GCX can be when developing an agent. You can pull conversations, pull experiments, and then make improvements using your coding agent right in your terminal. If you want to see the visual results, you can always go to the Grafana UI. 

It's super nice to have the CLI and your coding agent working together to help you improve your agent. Thanks for watching. 

[music]

## Raw YouTube Transcript

[music] [music] >> Hey everyone, it's Jack from Grafana here and today I'm going to be showing you how to improve your agent using GCX and agent observability. So for this demo, I just have a simple agent here to help me improve my Fantasy Premier League team which didn't start out so hot to start the season. So uh I'm just going to go ahead and ask it, "How did my team do week one?" And I've got my team ID here on the left so it has the context to pull my team and give me a little breakdown. Awesome. So I had it called a tool to get my Premier League team and then gave me some uh breakdowns here. So what does this look like in the Grafana backend? So I've instrumented my agent with agent observability. I'm going to pull up here uh the agent observability page where I can see a breakdown of some of my costs and usage uh but I want to really see the actual content of the conversation that I pushed. So um let's see. Um if I go ahead and refresh here, how did my team do week one showing up here? And awesome, I can see the workflow breakdown of the agent calling a tool and back and then I can see the content of the conversation. So uh the tool input and output and then the response. Awesome, but let's say I was a developer working on this agent and I wanted to improve it. >> [music] >> Um at this point, I would go into my own coding agent and ask it to you know, pull some conversations and uh suggest some improvements. And how would I do that? So uh we have this new uh CLI from Grafana called GCX which can do exactly this. So um if I go to my terminal here, I can say GCX and then conversations list. And awesome, you can see uh the breakdown is very similar to what you would see in the UI and it uh lists the latest conversations I have. So, if I wanted to pull the conversation that I just had, I can do conversations get. And awesome, I can see the conversation contents here. So, what's super useful about this is when I fire up my coding agent, I can ask it, "Can you use GCX and my Jack personal stack to pull the latest 10 conversations?" And we'll give it a second here to uh start up and pull some uh conversations. Reading GCX here. And there we go. It's going to list the latest conversation- -sations. Awesome. Doing some discovery. And there we have the latest uh 10 conversations appear here. And so, I could do things like, "Can you pull specific ones, suggest improvements?" These types of things. But, what I'm actually interested in for uh this demo agent is how it'll perform with different models. So, you know, something using something like Sonnet versus Haiku versus Opus and how that would affect performance. So, let's do this. I set up an experiment where I had a test suite of 20 different uh input and output cases. So, things like captain advice where the input is, "Who should I consider captaining?" And the expected value is it recommends one player. Um compare Salah did versus Cole Palmer this week. Um and things like budget defenders. So, 20 different cases here. And I invoked an experiment through Grafana agent observability to look at how my agent would do with Haiku versus Sonnet versus Opus. And so, if I hit compare runs here, I can see that for these cases, it looks like Haiku did the worst pass rate. Um Sonnet improved it and Opus did the best. But, if you look at the cost, um, as expected, Opus cost the most and then Sonnet, you know, was a little bit less and Haiku was super cheap. So, these would be considerations I would make when making an improvement to my agent or choosing a model. Um, there's different tradeoffs. Obviously, you get a little bit better performance with Opus, but, you know, maybe you could get the same kind of performance out of Haiku if you change the prompt a little bit. And so, how would I go about doing this? I would say, um, go to my coding agent and say, "Can you pull Actually, I have a prompt, uh, prepared here for pulling experiments. And here we go. It'll say here, um, "Use read-only GCX commands with my personal stack." And gives the experiment IDs that I have and going to compare the pass rate, average score, failure patterns, and give me a, uh, breakdown. So, it's pulling these experiments right here. Has some truncated output. And if we go to, uh, this, you can actually see, um, a breakdown of the scoring here. And if I click into any of these individual, uh, experiment runs, I can see the cost, etc. But, I can also see the conversation that occurred. So, if I click into the conversation, I can see the input and then what the agent said. I can also see the grader transcript. I've instrumented the judges associated with this, uh, experiment. So, I can see the actual grading input and output. So, I can really verify that the graders did a good job. Let's go back to our agent and see what it did. So, looks like it pulled the experiments and, uh, kind of did like a more detailed breakdown for me, which is super nice cuz sometimes these outputs of experiments can be a little hard to sift through where the important information is. So, you can see, uh, it does like a breakdown of tokens, the different results, best overall, and then some different weaknesses and suggest improvements. So, my next step here would be, you know, let's test out some improvements by making a change to the agent and then running a new experiment to see that it improves the results. So, um the point of this demo is just to show how powerful that GCX can be when developing an agent. You can pull conversations, pull experiments, and then make improvements using your coding agent just right in your terminal. And then if you want to see the visual results, you can always go to the Grafana UI. But, it's super nice to have the the CLI and your coding agent working together to help you improve your agent. Thanks for watching. >> [music]

