# CoreWeave&#39;s Mission Control Agent: Grafana as a Live Query Layer

Published on 2026-11-03T19:04:21Z

## Description

CoreWeave's Mission Control Agent answers operational questions by investigating live observability data from Grafana, ...

URL: https://www.youtube.com/watch?v=Xt75gdmbxL4

## Summary

The show titled "CoreWeave's Mission Control Agent: Grafana as a Live Query Layer" was published on November 3, 2026. The speaker, Savio, an engineering leader at CoreWeave, discussed the development of the Mission Control Agent, an AI-driven tool designed to enhance observability and streamline investigations in large-scale environments. Key topics included the challenges of managing vast amounts of observability data, the integration of Grafana for monitoring and incident investigation, and the importance of reliable evidence gathering and validation in AI-assisted troubleshooting. Savio emphasized that while AI agents can automate investigations, they must be designed with the implicit knowledge of experienced engineers in mind to ensure reliability and accuracy.

Topics: CoreWeave, Mission Control Agent, Grafana, observability, AI agents, incident investigation.

## Chapters

00:00:00 Observability challenges at CoreWeave
00:06:23 Building a reliable AI agent for operational investigations
00:12:10 Evidence-driven optimization with the mission control agent

Thank you everyone for waiting. I hope you've had a lovely ObservabilityCON. My name is Savio, and I'm an engineering leader at CoreWeave. I build public-facing observability products here at CoreWeave. Today, I'm going to talk about something we're calling the **Mission Control Agent**. You just heard about Any Agent; now we're going to discuss the AI agent in the AI cloud.

If you've ever been on call and found yourself staring at a bunch of Grafana dashboards trying to figure out where to go and how to solve an issue, this talk is probably going to help you relate to how we are building our AI agents to solve the same problem. 

A little bit about me: I have spent my career building distributed systems and machine learning across multiple domains. Now, at CoreWeave, I'm focused on helping simplify observability and insights for GPUs. Outside of work, I love robotics and pottery, so if anyone wants to chat about any of that, please feel free to reach out.

Today, we have a few things to cover. I'll start with some context about CoreWeave and how we approach observability. Then, we'll discuss the challenges of investigation at scale. From there, we'll go through the agent demo and finally talk about some takeaways.

For those who are unfamiliar with CoreWeave, we are an AI cloud platform purpose-built for demanding AI workloads. If you've used any frontier AI models, you've likely experienced CoreWeave at some point. We provide the infrastructure and services required for our customers to train, deploy, and run their AI models at scale. While GPUs are a significant part of our infrastructure, the larger component is the services we provide to support the GPUs, including networking, storage, Kubernetes, inference services, and everything that needs to work together.

When operating at scale, observability becomes incredibly important. Our customers need to understand how to investigate and observe their workloads, and our engineers need to understand what's happening on our infrastructure supporting these workloads. 

So, how do we observe at scale? Before we jump into that, I want to highlight some of the scale at CoreWeave. We are dealing with around **4.8 million scrape targets** across all our sites. We have approximately **5.4 billion active time series**, **280 billion log lines ingested** every single day, and around **3,000 queries per second** across our infrastructure. These are really large numbers, and they make the challenge of telemetry both difficult and interesting.

Imagine if you're a customer running an inference workload and suddenly your latency starts increasing. Somewhere in those billions of time series is probably the answer you're looking for—the signal that will tell you what's wrong. But finding that signal means knowing which queries to run and finding the needle in the haystack. This context is challenging to capture, and it's very difficult to identify when you are in an incident.

Grafana has been a key collaborator and partner for us in our observability journey at CoreWeave. Internally, our engineers use Grafana to monitor our infrastructure, investigate incidents, explore metrics, and correlate logs whenever we need to find more insights. We've also built a customer-facing Grafana experience for our customers, allowing them to understand what's happening in their workloads and the infrastructure they're running on. In many ways, Grafana has become the place for our engineers to understand the operational state of the system.

Grafana makes it possible for our users to explore their observability data, but giving an AI agent the same interface is where it gets a bit more complicated. 

Now, let's talk about how we do investigations at scale. For example, imagine you're running a large language model on a GPU infrastructure. Everything looks healthy in your initial testing, and you're very happy with it. Then, you start sending some real production data to this endpoint, and suddenly your model starts responding much more slowly. 

From the customer's perspective, this problem seems fairly simple: Why is my inference endpoint running slow? But from an infrastructure perspective, there are many possible explanations. Could it be that GPU utilization is the problem? Is there memory pressure? Is there request queuing? Is the model configuration wrong? Or is something in the underlying infrastructure causing the issue? Each of these possibilities requires us to go in a different direction and extract different signals.

The first thing you'll usually do is open up your Grafana dashboard and check if there is a metric that is changing. Maybe the latency starts increasing, which you can see in the graph behind me. You can start identifying the patterns that are happening, but it still doesn't tell you where the problem is occurring. You might have a sense that it's probably coming from the application, but you don't have concrete evidence of whether it's resource contention or something else.

We need to move beyond simply observing these signals and understanding what's wrong to understanding why it's wrong. So, we started taking a few steps back. What does a typical investigation look like? 

In a typical investigation, you start by analyzing the workload behavior. You look at the metrics, query the Loki logs, and find some error rates. From there, you probably need to check your physical deployment and examine your Kubernetes pod health to see if there are any scheduling challenges or issues in your infrastructure. Eventually, you'll realize that you also need to lean on your documentation and the expertise within your company.

One thing is very clear: we look through different layers of the stack, and this knowledge is not centralized anywhere. The evidence of investigation is distributed across multiple systems. Typically, an experienced engineer on our team knows how to navigate this, but much of this knowledge is implicit. It's something engineers learn through their experience, and we are now expecting the AI agents to solve this out of the box. This is something we are investigating further.

So, what are we really asking an AI agent to do? We are trying to automate the manual investigation flow. We want to identify the symptoms, gather evidence by querying logs in Loki and metrics in Prometheus, create a hypothesis, act upon that hypothesis, and eventually validate it. This is the validation loop. This is exactly what we want an AI agent to do: provide this loop all at once.

Let's look at how manual investigation is done. Going back to the same inference example, you'll start seeing that the time for the first token is the first signal that is being highlighted, indicating that the service is not running correctly. The engineer needs to start questioning what's happening. Is it happening across all requests? Is it isolated to just this one deployment? Are the requests spending some time in a queue? There are many different signals that require you to explore various directions.

The obvious question now is: why don't we just give a large language model (LLM) access to these systems and ask it to debug the problem? Well, it turns out it's not quite that simple. One thing we've really found is that your mileage on these responses may vary. Different engineers can ask different models different prompts, and they can provide...

varied context and the tools that it gives to the models can also reflect how the agents respond. But when you actually sometimes take a look at the answers that look possibly right, you'll identify that they might have digressed because the evidence that it provides, the metrics it looks similar, but isn't the right metrics. 

The serious problem is when you're dealing with infrastructure issues in production; you really can't just have this unreliable agent. We don't want an agent that just produces good enough results with convincing explanations, but we want to build something that gathers the right evidence and produces findings that the engineers can verify. That is what we started our journey to build Mission Control. So, unreliable agents can cause inconsistent results. 

We start thinking about the reliable agent loop. The agent loop forms three main components. The first component is evidence gathering. The model needs to figure out what operational signals it needs. If it's an investigation issue across different infrastructure, it needs to know how to gather that information. To do those actions, we have the hardness. The hardness is a system around this model that we built to coordinate the investigation. It manages the tool calling, the context, the permissions of the user, and then eventually the overall investigation process. 

The hardness is actually really important because we've written systems for humans. For example, queries fail, APIs can return a lot of information or incomplete information, and all of these can lead to a wrong hypothesis. So, we need to build software around the model to handle these situations reliably. The last part of reliability is always verification, right? How do we know the agent actually did something useful? To do that, we need to recommend a change and then verify and validate the change. The agent gathers all of this information for you, but this is the loop you need to build to have a reliable agent.

Let's just look again from that inference angle. The Mission Control agent, how does it implement it in its real architecture? Everything starts with a question. It might be something like, "Hey, why is my inference running suddenly slow?" The agent and its hardness interpret the question, understand the scope of the investigation, and start planning what evidence it needs. We'll use an LLM for the reasoning step and the hardness for controlling and coordinating the reasoning. We'll call that the brain.

The next step is the hands. To actually give this agent your infrastructure and your observability data, you need to have a controlled environment with tools well-defined for your agent. This is where we build our Mission Control MCP server. This MCP server is not just a server that provides access to API endpoints; it is a set of well-defined scope tools that helps the agent get to the evidence gathering process consistently. 

Lastly, this agent actually needs to go do some actions, and that's where we provide this agent with a sandbox so that the agent has hands that are safe and secure. To support all of this, you obviously need to have a lot of contextual data. You might have seen in many Grafana examples the knowledge base and knowledge architecture. We support that, and we also have tools that provide the agent with documentation, and that's the data. So, it needs to have the brains, the hands, and the data all to execute itself.

So, we've talked about the loop. We've seen how the agent gathers. Let's take a look at how the agent actually works in real life. As I said, the inference deployment was healthy and it was working as expected, but all of a sudden you start realizing, "Hey, why is my throughput down?" So, you ask the agent this question, and it starts gathering and investigating. It identifies that there's a latency issue, a queue depth issue, and KV cache utilization issue. It found that the longer context was putting pressure on KV cache, causing evictions and unnecessary de-competitions.

What's useful here is that we can actually inspect the metrics, the evidence behind its diagnosis, and the agent gives us eventually some options to execute. The first option is to scale out your infrastructure, but we are in a GPU shortage, so probably not. The second is you can run a quantized version of this model, and that should give you some of the memory back, which should help with your cache situation. So, you select that option, you tell the agent to go apply this, and from there on, you'll start seeing that it begins applying this. 

However, because we ran a quantized version of the model, we will actually take some quality hit. Because of that, the agent runs a load test to ensure that the quality benchmarks are the same, and then it will go and execute it. After it runs the quantized version of the model and the load test, it identifies that the token efficiency went from 3,000 tokens per minute per GPU to 5,000 tokens per minute per GPU. 

But here's where it gets interesting. The agent continues the optimization loop and suggests to a customer that there's an opportunity to shrink the model deployment to a smaller footprint because now the quantized model is actually surfacing the same value. So, it's the same amount of GPUs, same spend, but you're getting more use from this infrastructure. You tell the agent to apply that action and then you ask it to validate. 

That's basically what is the kind of evidence-driven optimization we are building with Mission Control. So, you've just applied all of these changes to your model through the Mission Control agent. You've gone through the evidence loop, but the problem still exists, which is I want to, as an engineer, make sure this is the right thing. How do you do that? 

This agent was able to investigate and optimize, but it also provides you with the Grafana endpoints to validate these responses. You can actually take a look at these graphs that I put over here. At the beginning, the cache usage is completely missed because your throughput was not at the right levels. Eventually, as you apply the change, you start seeing the cache usage being there. Having the ability to give our engineers the ability to inspect the agent's response is a key design principle for us. 

We're not trying to replace Grafana with an AI-generated wall of text. We're actually trying to help the agent accelerate our investigation journey and provide evidence in the persistence layers which are embedded in our runbooks because mostly you will have a runbook that has some links associated with the dashboards. 

All right. So, I have a few takeaways from this conversation that I would like to share with all of you. First, the human query layers or the query habits don't really transfer to AI agents. The human operator knows a lot. The experienced engineers bring a lot of implicit knowledge to an investigation. They know which dashboards matter. They know when a query fails, what to change, but the AI agents necessarily don't have that context. 

So, we need to be much more explicit in how we design tools for them. This means making sure that when a payload given back to an agent is overwhelming, you know how to handle the context for an agent. We found that designing tools for an agent makes an enormous difference in how reliable agents can investigate infrastructure. 

The second is when an agent tells you that something is wrong in production, you need to know why and you need to believe that. This means your evidence needs to be inspected. Which metrics did the agent use? What range did it use? How did it come up to that conclusion? Grafana for us, or your dashboarding service of your choice, would be the familiar place that you as an engineer have muscle memory to go validate. So, we need to make sure that no matter what...

Your agents produce data that can actually correlate to the responses in your dashboards that you see eventually. That's about it. Thank you. Thank you all for staying with me.

## Raw YouTube Transcript

Thank you everyone for waiting. I hope you've 
had a lovely ObservabilityCON. So, my name is Savio. I'm an engineering leader at CoreWeave. 
I build public-facing observability products here at CoreWeave. Today I'm going to talk about 
something we're calling the Mission Control Agent. You just heard about Any Agent. Now we're going 
to talk about the AI agent in the AI cloud. If you've ever been on call and you've been staring 
at a bunch of Grafana dashboards trying to figure out where to go, what, how to solve, this talk is 
probably going to help you relate to how we are building our AI agents to solve the same problem. 
So a little bit about me. I have spent my career building distributed systems and machine learning 
across multiple domains. And now at CoreWeave, I'm focused at helping simplify observability 
and insights for GPUs. Outside of work, I love robotics and pottery. So if anyone wants 
to talk about any of that, please chat with me. All right. So we've got a few things today. 
I'll start with some context of CoreWeave, how we approach observability at CoreWeave, and 
then we'll talk about what are the challenges of investigation at scale. And then from there 
on, we'll go through the agent demo and then finally talk about some takeaways around that. 
So for those who are unfamiliar with CoreWeave, CoreWeave is an AI cloud platform purpose 
built for demanding AI workloads. If you used any frontier AI models, you've definitely 
experienced CoreWeave at some point in your life. We provide the infrastructure and services 
required for our customers to train, deploy, and run their AI models at scale. And while GPUs 
are obviously a big part of our infrastructure, the bigger part are the services that we provide 
to support the GPUs. We've got the networking, the storage, Kubernetes, inference 
services and everything that needs to get all of this working together.
When you're operating this at scale, observability becomes incredibly important. Our customers need 
to understand how to investigate and observe their workloads, and our engineers need to understand 
what's happening on our infrastructure supporting these workloads. So how do we observe at scale? 
Before we jump to that, I want to actually highlight some of the scale at CoreWeave. So at 
CoreWeave, we are roughly dealing with around 4.8 million Scrape targets across all our sites. 
We have around 5.4 billion active time series, 280 billion logs of lines ingested every single 
day, and around 3,000 queries per second across our infrastructure. These are really large numbers 
and these numbers make the challenge of telemetry really, really difficult and interesting. Imagine 
if you're a customer running an inference workload and suddenly your latency starts increasing. 
Somewhere in those billions of time series is probably the answer you're looking for, the 
signal that's going to tell you what's wrong. But finding that signal is knowing to run which 
queries and finding the needle in the haystack. This context is a really difficult context 
to capture, and it's very challenging to identify when you are in an incident.
Grafana has been a key collaborator and a partner for us in our observability journey at 
CoreWeave. Internally, our engineers use Grafana to monitor our infrastructure, investigate 
incidents, explore metrics and correlate logs whenever we need to find more insights. We've 
also built a customer-facing Grafana experience for our customers where our customers use it to 
understand what's happening in their workloads and the infrastructure they're running on. In 
many ways, Grafana has become the place for our engineers to understand the operational state 
of the system. Grafana makes it possible for our people that we interact with to help explore their 
observability data, but what it looks to give an AI agent the same interface, this is where it 
gets a little bit more complicated. So, let's really talk about how do we do investigations 
at scale. Let's take for an example an inference workload. Imagine you're running a large 
language model on a GPU infrastructure. Everything looks healthy in your initial 
testing, you're very happy with it. Then you start sending some real production data 
to this endpoint and suddenly your model starts responding much more slowly. From the 
customer's perspective, this problem is fairly simple. Why is my inference endpoint running 
slow? But from an infrastructure perspective, there are a lot of possible explanations, right? 
Could it be that GP utilization is the problem? Is there a memory pressure? Is there a request 
queuing? Is the model configuration wrong? Or something in the underlying infrastructure is 
a problem? Each of these possibilities requires us to go in a different direction 
and extract different signals. So the first thing you'll usually do is you'll 
open up your Grafana dashboard and take a look at is there a metric that is changing? Maybe the 
latency starts increasing. You can see that in the graph behind me. And you can start identifying 
what is the patterns that are happening, but it still doesn't tell you where the problem 
is happening. You kind of have a sense of it's coming probably from the application, but you 
don't have concrete evidence that it's whether resource contention or something else. 
We need to move beyond simply observing these signals and understanding what's 
wrong to understanding why it's wrong. So we started taking a few steps back. What 
is a typical investigation looks like? In a typical investigation, you typically start with 
analyzing the workload behavior. So you take a look at the metrics, you query the low-key logs 
and you find some error rates. From there on, you probably need to go to your physical deployment 
and take a look at your Kubernetes spot health, see if there's any scheduling challenges or 
anything in your infrastructure. Eventually, you'll realize that you probably also need to 
lean on your docs and your expertise that you have within the company. One thing is very clear, 
we look through different layers of the stack and this knowledge is not centralized anywhere. This 
evidence of investigation is distributed across multiple systems. And typically an experienced 
engineer on our team knows how to navigate this, but a lot of this knowledge is implicit.
So something engineers learn through their experience, we are now expecting the AI agents 
to just solve this out of the box. And that is something we investigate further. So what are we 
really asking an AI agent to do? We're trying to automate the manual investigation flow. So you 
want to identify the symptoms, then you want to take all of the evidence by querying logs in 
Loki and then querying Prometheus for metrics. Eventually you'll find these evidence, create a 
hypothesis and then act upon that hypothesis and eventually validate. That is the validation loop. 
This is exactly what we want an AI agent to do, is to provide this loop at once. So let's 
look at how manual investigation is done, right? Going back to the same inference 
example, you'll start seeing that the time for first token is the first signal that is being 
highlighted and the service is not running right. The engineer needs to start questioning what's 
happening. So is it happening across all requests? Is it isolated to just this one deployment? 
Are the requests spending some time in queue? There's a lot of these different signals that 
require you to go into different directions. And you'll notice that the engineer is no longer 
just reading a dashboard. The engineer is going across different systems and investigating 
what's happening as an evidence of that. So the obvious question now I find myself asking 
is why don't we just give an LLM access to these systems and ask it to debug the problem? Well, 
it turns out it's not that quite enough. The one thing we've really found is your mileage on these 
responses may vary. Different engineers can ask different models, different prompts. They can give 
varied context and the tools that it gives to the models can also reflect how the agents respond.
But when you actually sometimes take a look at the answers that look possibly right, you'll 
identify that they might have digressed because the evidence that it provides, the metrics it 
looks similar, but isn't the right metrics. The serious problem is when you're dealing 
with infrastructure issues in production, you really can't just have this reliable agent. 
We don't want an agent that just produces good enough results with convincing explanations, 
but we want to build something that gathers the right evidence and produces findings that the 
engineers can verify. That is what we started our journey to build mission control. So unreliable 
agents can cause inconsistent results. So we start thinking about the reliable agent loop. 
The agent loop forms of three main components. The first component is the evidence gathering. The 
model needs to figure out what operational signals does it need. If it's an investigation 
issue across different infrastructure, it needs to know how to gather that information.
To do those actions, we have the hardness. The hardness is a system around this model that we 
build to coordinate the investigation. It manages the tool calling, the context, the permissions 
of the user, and then eventually the overall investigation process. The hardness is actually 
really important because we've written systems for humans, like the queries fail, APIs can return 
a lot of information or incomplete information, and all of these can build to a wrong hypothesis. 
So we need to build software around the model to handle these situations reliably. And last 
part of reliability is always verification, right? How do we know the agent actually 
did something useful? So to do that, we need to recommend a change and then verify the 
change and validate the change. The agent gathers all of this information for you, but this is the 
loop you need to build to have a reliable agent. Let's just look again from that inference 
angle, right? The mission controlled agent, how does it implement it in its real architecture? 
So everything starts with a question. It might be something like, "Hey, why is my inference 
running suddenly slow?" The agent and its hardness interprets the question, understands the 
scope of the investigation and starts planning what evidence it needs. We'll use an LLM for the 
reasoning step and the hardness for controlling the reasoning and coordinating the reasoning. 
We'll call that as the brain. The next step over here is the hands. To actually give this agent 
your infrastructure and your observability data, you need to have a controlled environment with 
tools well defined for your agent. This is where we build our mission control MCP server. 
This MCP server is not just a server that provides access to API endpoints. It is a set of 
well-defined scope tools that helps the agent get to the evidence gathering process consistently.
And lastly, this agent actually needs to go do some actions and that's where we actually 
provide this agent with a sandbox so that the agent has hands that are safe and secure. 
And to support all of this, you obviously need to have a lot of contextual data. So you 
might have seen in many Grafana examples, the knowledge basis and knowledge architecture. We 
support that and we also have tools that provide the agent with documentation and that's 
the data. So it needs to have the brains, the hands and the data all to execute in 
itself. So we've talked about the loop. We've seen how the agent gathers. Let's take a look 
at how the agent actually works in real life. So as I said, the inference deployment was 
healthy and it was working as expected, but all of a sudden you start realizing, 
"Hey, why is my throughput down?" So you ask the agent this question and it 
starts gathering and investigating. It identifies that there's a latency issue, there's 
a queue depth issue and KV cache utilization issue. It found that the longer context were 
putting pressure on KV cache causing evictions and unnecessary de-competitions. What's useful 
here is that we can actually inspect the metrics, the evidence behind its diagnosis, and the agent 
gives us eventually some options to execute. The first option is to scale out your infrastructure, 
but we are in GPU shortage, so probably not. The second is you can run a quantized version of 
this model and that should give you some of the memory back, which should help with your cache 
situation. So you select that option, you tell the agent to go apply this, and from there on, 
you'll start seeing that it starts applying this. But because we actually ran a quantized version of 
the model, we will actually take some quality hit. Because of that, the agent runs a load test to 
actually make sure that the quality benchmarks are the same and then it will go and execute it. So 
you can see after it's run the quantized version of the model and run a load test, it's identified 
that the token efficiency went from 3,000 tokens per minute per GPU to 5,000 tokens per minute 
per GPU. But here's where it gets interesting. The agent continues the optimization loop 
and suggests to a customer that there's an opportunity to actually shrink the model 
deployment to a smaller footprint because now the quantized model is actually surfacing them 
the same value. So it's the same amount of GPUs, same spend, but you're getting more use from these 
infrastructure. So you tell the agent to apply that action and then you ask it to validate.
That's basically what is the kind of evidence driven optimization we are 
building with mission control. So you've just applied all of these changes to 
your model through the mission control agent. You've gone through the evidence loop, but 
the problem still exists, which is I want to, as an engineer, make sure this is the right 
thing. How do you do that? This agent was able to investigate and optimize, but it also provides 
you with the Grafana endpoints to validate these responses. You can actually take a look at these 
graphs that I put over here. At the beginning, the cache usage is completely missed because your 
throughput was not at the right levels. And then eventually as you apply the change, you start the 
cache uses being there. Having the ability to give our engineers the ability to inspect the agent's 
response is a key designing principle for us. We're not trying to replace like Grafana with an 
AI generated wall of text. We're actually trying to help the agent accelerate our investigation 
journey and provide evidence in the persistence layers which are embedded in our runbooks 
because mostly you will have a runbook that has some links associated with the dashboards.
All right. So, I have a few takeaways from this conversation that I would like to share with 
all of you. First is the human query layers or the query habits don't really transfer to 
AI agents. The human operator knows a lot. The experienced engineers bring a lot of implicit 
knowledge to an investigation. They know which dashboards matter. They know when a query fails, 
what to change, but the AI agents necessarily don't have that context. So we need to be much 
more explicit in how we design tools for them. This means making sure that when a payload 
given back to an agent is overwhelming, you know how to handle the context for an agent. 
We found that designing tools makes for an agent, makes enormous difference in how reliable 
agents can investigate infrastructure. The second is when an agent tells you 
that something is wrong in production, you need to know why and you need to believe that. 
This means your evidence needs to be inspected. Which metrics did the agent use? What range did 
it use? How did it come up to that conclusion? Grafana for us or like your dashboarding service 
of your choice for you would be the familiar place that you as an engineer have a muscle memory 
to go validate. So we need to make sure that no matter what your agents produce, it can actually 
correlate to the responses in your dashboards that you see eventually. That's about it. Thank 
you. Thank you all for staying with me.

