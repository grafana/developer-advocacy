# Evaluating LLM Agents in the Real World: Inside Grafana Assistant

Published on 2026-01-25T22:44:29Z

## Description

From Observability for GenAI Applications (Grafana ❤️‍   OpenTelemetry Community Call #4) Watch the full episode: ...

URL: https://www.youtube.com/watch?v=0N4JXCLzN8U

## Summary

In this video, the speaker discusses the challenges and strategies related to evaluating AI language models (ALMs) in real-world applications. Key points include the importance of maintaining model performance and avoiding regression with new tools, the necessity of using real data for effective interaction, and the cost implications of evaluation processes. The speaker emphasizes the need for a close feedback loop between real-world scenarios and sandbox testing, using automatic evaluations and human feedback to assess model performance. They also highlight the limitations of ALMs in providing accurate judgments, advocating for boolean criteria in evaluations to enhance reliability, and acknowledging the challenges of large-scale human annotation in traditional machine learning.

## Chapters

00:00:00 Introduction to context window and context rot  
00:02:15 Importance of real data for model evaluation  
00:03:45 Ensuring no regression in model performance  
00:04:30 Cost considerations in evaluation processes  
00:05:50 Feedback loops between real-world data and sandbox scenarios  
00:07:10 Automatic evaluation using BLM as a judge  
00:08:25 Challenges in maintaining user experience during updates  
00:09:40 CGI integration for prompt changes  
00:10:30 Boolean criteria for evaluating model outputs  
00:11:50 Comparing LLM judgments with human feedback

Every token you have due to the context window and what we call context rot is significant. Context rot refers to the idea that every new piece of information you introduce into the context can affect the model's performance. Therefore, whenever we develop a new tool, we must ensure that there is no regression in performance.

There are two key components to this process:

1. **Access to Real Data**: These agents must interact with real data, which is a new concept compared to initial models that only processed input and output.
   
2. **Ensuring Consistency**: We need to make sure everything is still functioning correctly and that changes are not solely due to data variations.

Reflecting on the costs involved, we spent around fifty dollars on evaluations in some rounds, which seems significant. However, it's the most effective method we have right now, even if it's not the best long-term solution. The best practice currently involves rerunning evaluations as frequently as possible and maintaining a close feedback loop between real-world outcomes and sandbox scenarios. This ensures that every new addition genuinely improves the system.

We conduct some automatic evaluations on trajectories using BLM as a judge, but we need to keep costs low. Thus, our evaluation methods are not overly sophisticated. They primarily focus on ensuring that client and user experiences are not degraded. Most of our evaluation runs are performed offline, and we are currently working on integrating CGI. 

The idea is that every time we alter a prompt or description, we run those tasks and scenarios to ensure we are not introducing any errors. Unlike traditional models, where accuracy remains stable, changes can have unpredictable effects. For instance, altering one aspect could unintentionally affect logs due to the context window remaining the same.

We try to utilize LLMs for judging whenever possible. If we can validate our results using regex in comparison with real data, we will do so. However, one lesson learned is that when interacting with LLMs, it’s more effective to use boolean criteria. Instead of asking if something is good or bad on a scale, we began using specific criteria. For example, when evaluating a trace analysis workflow, we might ask if the bottleneck is mentioned or if the trace links are present. This approach allows us to better control the LLM’s responses and reduces the chances of it generating unrelated information.

While this method doesn’t guarantee accuracy, it helps ensure that the LLM’s judgments correlate more closely with the truth. Whenever possible, comparing LLM evaluations with human feedback is beneficial. If we can gather human feedback, it provides a valuable benchmark against which we can measure the accuracy of the LLM’s judgments.

The alternative method used to involve humans annotating data, similar to traditional machine learning practices. However, due to the vast volume of data, this approach is no longer feasible.

## Raw YouTube Transcript

Every token that you had because of the context window and context rot, right? What we call context rod, that means like every new thing that you put in the context, the grades, the model performance. So whenever we come up with a new tool, we have to make sure that. There is no regression, so there's two parts here. 1 making sure that you have access to real data because these agents will have to interact with real data at the end, which is a new thing comparing to the initial alms where it was just input and output. But also how to make sure that? Everything is still working and it's not just data that's changing. So coming back to the cost we spent in some of those rounds, like 50 bucks just in the evaluation and part of it, which is mad if you think. But it's the the best way we can find. I'm not saying it's the best long term, but it's the best available right now, which is rerunning as much as you can, trying to have a very close feedback loop between what is happening in the real world. And what is happening in your sandbox scenario and making sure that every new addition is actually making stuff better. We do some automatic evaluation on the trajectory using BLM as a judge, but we have to keep it cheap. So it's not a a very fancy fancy. For robust evaluation is just to make sure that the clients the the user experience is not being degradated. But most of the evaluation runs offline and recently we are working on adding CGI integration. So the idea is every time you change your prompt. Every time you change up two description, even we run those tasks, the scenarios to make sure that we are not breaking stuff. Because different from traditional model where the accuracy would be very stable, if you change something else, you might be changing something completely different. Might be changing tempo tools and that hurt logs for some reason because the context window is the same right? We defer of using LMS that judge as much as we can. So if we are able to check with regex with comparing it with real data. The other way to compare that data, we will use it. But one thing we learn is that whenever you're asking to ALM if you have a boolean criterias. So instead of asking like is this good? Is this bad in a scale? Usually we started with scale like and zero to 10 is this good? And the elements are not good at that so. We usually say um, for example, if you're evaluating A traces analysis workflow, you would ask like is the bottleneck mentioned? Is the trace a link to traces present? I mean all the criterias you want on that answer in a boolean. Through false way. That way you can control a bit more that the LM is not just inventing stuff, but you're not guaranteed for sure, but a way to make sure that your LLM as a judge is not drifting too much and it's more or less. Related to the truth is whenever you can compare that with human evaluation. So if you get human feedback, that's great, right? So comparing the human feedback with the alarm as a judge, it's a way to have at least a sense if your LMS judge is. Actually representing a human as a judge it The other alternative is having humans annotating data like we used to do with traditional ML. Right, but the volume is so big that that's not as feasible anymore.

