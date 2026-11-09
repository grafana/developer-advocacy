# Inside the AI Team Weekly: AI Observability workflows and Prometheus exemplars (May 19th, 2026)

Published on 2026-06-16T16:00:27Z

## Description

The Grafana AI team (Engineers Ivana Huckova and Sonia Aguilar) share what's new in AI Observability this week: a new way to ...

URL: https://www.youtube.com/watch?v=P3AX1H527Gs

## Summary

The show "Inside the AI Team Weekly: AI Observability workflows and Prometheus exemplars" aired on May 19th, 2026, featuring engineers Ivana Huckova and Sonia Aguilar from the Grafana AI team. They discussed new features in AI Observability, including the ability to instrument and visualize workflows, and the integration of Prometheus exemplars to enhance debugging capabilities. Key takeaways included the introduction of a new workflows tab for visualizing AI processes and how exemplars can link metrics to specific traces, aiding in the identification of performance issues. The discussion highlighted the ongoing efforts to merge traditional observability concepts with AI observability tools.

Topics: AI Observability, workflows, Prometheus, exemplars, debugging.

## Chapters

00:00:00 Demo of AI observability workflows
00:02:18 Using Prometheus exemplars for AI observability
00:03:52 Using exemplars for AI observability

**Inside the AI Team Weekly: AI Observability workflows and Prometheus exemplars (May 19th, 2026)**

Lots of new features since last week's meeting. For example, we built a feature that is able to instrument and visualize workflows. We also redesigned the agents page, adding data from the quality evaluations and the ability to select multiple conversations to create a new collection. There is a lot of ongoing work, such as visualizing examples and jumping into conversations. Ivana is going to demo this, along with evaluation rule actions and experiments.

I will start with the demo about workflows. We are building AI agents in my team that may use frameworks like LangGraph to produce workflows. In this case, in AI Observability, you now have the ability to instrument this kind of workflows and visualize them. 

Let me show you an example. If you instrumented a conversation as a workflow, you now have this new tab labeled "Workflow." When you click on it, you will see a graph that represents a workflow. Each node represents a step, and each step can contain or not contain LLM calls. For example, this is a step where you can see the name of the step and the loops. In this case, we are running two LLM calls in this step. You can click here and navigate through each generation, seeing all the details of each generation on the right side. 

You can also see the loops. For example, in this step, there is no LLM call; it only contains logic, but you can see that we have two loops. On the right side, in the details, we can see the relevant information regarding the workflow step, including the input state and output state. 

This graph is really useful for debugging. For example, when something goes wrong, you can immediately see which step was failing, the cost of each step, and detect issues very easily. This is a demo for workflows, and I think Ivana has another plan.

**Ivana:** Yeah, I wanted to do a very quick demo, a very small demo. Here, I would just like to show how we can apply concepts from normal observability and bring them to new features and products like AI Observability. 

So, here I am in the AI Observability app, and we are using Prometheus metrics to see how many requests there were, what the error rate was, time to the first token, and so on. Prometheus has a really cool feature called exemplars. Exemplars allow you to attach trace IDs to your metrics, so you can see actual events and traces that contributed to that metric. This is very helpful when you are trying to debug latency issues. 

For example, here we have a spike in time to the first token. You can see actual traces and conversations that contributed to this spiked value. We have decided that in AI Observability, we are going to show exemplars. I would like to mention that the assistant is already instrumented, so this came for free. All histograms, all primitive histograms, already have exemplars. I think it's about 5% of metrics that have exemplars. 

With this new feature, we are able to jump to the conversation that spiked the latency or time to the first token. We can see the trace, the generation that happened, and then use the assistant to investigate the cause of this elevated value. I thought it would be interesting to show how we can use features and functionalities that already exist in our good place and bring them to users in our new apps. 

So, this is my short demo.

**Todd:** This was amazingly cool. Do we have a cloud code plug-in that sends data to SigOpt?

**Ivana:** Yeah. If you go to the SigOpt SDK, we have plugins. Here are the plugins that we support currently.

**Todd:** So, install it as a plugin, and it will track your usage in cloud code, right? This would be cool. We should try that out. 

But I think we'll call it here so we can stop and have five minutes to breathe before anything new starts for everybody. Thank you very much, everybody. It's nice to see you all. I'll see you around. Take care.

## Raw YouTube Transcript

lots of uh new features since last week weekly. Uh for example, we built a feature that is uh been able to instrument and visualize workflows. Uh we also redesigned the agents page adding data from the quality from evaluations and also the ability to select multiple conversations and create a new collection. And lot of ongoing work like visualize an example example sorry example last and jump into conversations. Ivana is going to demo this. And also evaluation rule actions and experiments ongoing work. I will start with the demo about workflows. And we are building AI agents in my team that maybe you use a frameworks like LangGraph that produce workflows. In this case, uh now in AI observability, you have the ability to instrument this kind of workflows and visualize them. Let me show you an example. So in case you instrumented a conversation as a workflow, now you have this new tab here. Workflow that when you click in here, you will see this graph uh this graph. And this this represents a workflow. Each node represents a step. And each step can contain or not LLM calls. For example, this is a step. You can see the the name of the step, the loops. And in this case, we are uh we are running two LLM calls in this step. You can click in here and you can navigate through each generation and see at the right side all the details of each step. Sorry, of each generation. Then you can see also the loops. and you can see for example in this step, this step does not contain any LLM call, it's only logic, but you can see that we have two loops and in the right side in the details, we can see the relevant information regarding the workflow step, this is the state. Input state, output state. Uh, so this is this graph is really useful because when debugging uh, for example, when something goes wrong, you can immediately see which step was failing, the cost of each step and detect things very easily. And this is a demo for workflows. And I think Ivana has another plan. >> Yeah, I wanted to do a very quick demo, um, very small demo and here I would just like to show how sometimes we can apply concepts from, for example, normal observability and bring it to, um, like new features and new products like AI observability. Uh, so here I am in a AI observability app and we are using Prometheus metrics. So, um, to see like how many requests, uh, what was the error rate, time to the first token and so on. And Prometheus has a really cool feature called exemplars. So, exemplars is a way how you can attach trace ID to your metrics. So, you can see actual events, um, actual traces that contributed to to that metric. And this is very helpful when you are, for example, um, trying to debug latency issue or for example, here we have a spike in time to the first token. So, you can see actual traces, actual conversation that contributed to this spiked value. Uh, so we have decided that in AI observability, we are going to show, uh, exemplars. And here I would like to say that assistant is already instrumented. So this came for free. So all histograms all permit like all primitive histograms already have exam five I think it's 5% of metrics have exemplars. And then we are able to jump so that the new feature so we are able to jump to that conversation that spiked the latency or time to the first token. We are able to see the trace. We are able to see like which generation happened and we are able to again then use assistant to investigate why what is the cause of of this elevated value. So yeah, I was thinking it would it's kind of like interesting way to show how we can I don't know if it's a dog food maybe like how we can use features and functionalities that already exist all of our good place and bring them to users also in our new apps. And yeah, so this is my short demo. Yes. >> Todd, this was amazingly cool. Do we have a cloud code plug-in that sends data to SigOpt? >> Yeah. So it If you go to SigOpt SDK and we have plugins. So here are the plugins that we that we support currently. >> So install it as a plugin and it will track your usage in cloud code, right? This would be cool. Should try that out. But I think we'll call it here so we can stop and have 5 minutes to breathe before anything new stops for everybody. Thank you very much everybody. It's nice to see you all. I'll see you around. Take care.

