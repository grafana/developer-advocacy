# Investigations Arena: how we test Assistant investigations

Published on 2026-07-30T09:43:37Z

## Description

Senior Software Engineer William Dumont demonstrates how we test Assistant Investigations by pitting two versions of the same ...

URL: https://www.youtube.com/watch?v=YPfqchw8LCo

## Summary

The show is titled "Investigations Arena: how we test Assistant investigations," published on July 30, 2026. The speaker, William Dumont, a Senior Software Engineer at Grafana, discusses the development of the Investigations V2 feature, which improves upon the initial version by utilizing an arena-like setup where AI agents compete to solve real incidents in a production cluster. This approach allows for the comparison of different strategies and tools, using a large language model (LLM) as a judge to evaluate their effectiveness against a verified ground truth. Key takeaways include the importance of diverse strategies in improving investigation quality and the potential for sharing this testing framework with the community to enhance various investigation agents. 

Topics: Grafana Assistant, Investigations V2, AI agents, LLM, community sharing.

## Chapters

00:00:00 Introduction to Assistant investigations and testing methods
00:02:18 Comparing different models for investigations
00:03:50 Testing Assistant investigations with LLMs

Hey, my name is Will. I'm a software engineer at Grafana. I've been there for 3 years, and for the past year, I've been focusing on AI, specifically on the Grafana Assistant investigations and memory features.

**What's the latest thing you've been working on?**

We developed Investigations V1 and noticed that we hit a ceiling at some point. We came up with a different approach, but this time we needed a good evaluation and demo environment. The previous cases were too easy and too far from the reality of a production environment. So, we decided to build an arena. 

It's a little bit like the idea of bot programming, where bots fight against each other for specific tasks or games. In this case, the topic was investigations in our production cluster, focusing on real incidents. We started building these bots that had different strategies and tools; these were AI agents. By comparing a diversity of strategies, we were able to surface the best approaches. From there, we could iterate, bring in more test cases through more incidents, and reach higher quality.

The idea is that the bots will try to solve the same case, and we use a large language model (LLM) as a judge to compare the different approaches. We have different criteria because, for the incidents, we have a verified root cause by a human. This gives us a very solid ground truth for comparison. The LLM as a judge will compare this ground truth against the answers that the agents came up with.

The important part at first was not even the score, but the insights. For example, one tool was better with a specific strategy, while another might have some noise in the results that poisons the context. We managed to optimize bit by bit and come up with Investigations V2, which we just released. It's a massive improvement compared to our V1 approach.

**Is it comparing just different models for investigations, or is it also comparing GCX and NCP versus Assistant?**

Right, so both actually. We have different versions of our harness for investigations that we run with Sonnet and with Opus. We also use Claude code harness with GCX, Grok, and NCP, and even just using curl to directly hit our public API.

**Do the models ever cheat?**

So far, it's been quite good. We have guardrails in place. Because we investigate past incidents, we need to ensure that the LLM only looks at a specific time window—only when the incident started. Otherwise, it could find the pull requests that were used to solve the incident. They are pretty good at following the rules; they take it as a game a little bit. 

We have an agent that checks afterward with the judge to make sure that they followed every rule. Interestingly, we had a case where using GCX, it started to use some tools that we did not think about initially. These tools were actually very useful for investigations, and we had never considered them before. This led us to incorporate them into our investigation harness, which helped a lot. Giving the agents freedom and creativity in this environment is very useful; this diversity spawns new ideas that we can implement in our work.

**Do you have any plans to publish this and share it so that other people can do it too, kind of like Ali bench?**

Yeah, I think why not? We can definitely go this route. I'm sure this would be useful for other agents, and it would be great if we could also compare agents from other companies with different harnesses and tools. Right now, it's mostly about our MCP, our CLI, or our investigation harness, but if the community comes up with their own investigation agent, I think it would be fun to put them in the arena and help improve not just our product, but any product in terms of quality.

## Raw YouTube Transcript

Hey, my name is Will. I'm a software engineer at Grafana. I've been there for 3 years and since 1 year I've been focusing on AI. So, the Grafana assistant investigations and memory features. >> And what's the latest thing you've been working on? >> So, we developed investigations V1. And we saw that um we hit a ceiling at some point and we came up with a different approach, but this time um we needed good evaluation and um demo environment or like you need to like this was not enough because these cases were too easy and too far from the reality of production environment. So, we decided to build an arena. So, it's a little little bit like the idea of bot programming uh fighting against each others to for specific task or or games, for example. Um in this case uh the topic was investigations in our production cluster. So, real incidents. And we started building these bots that had different strategies, different tools. These were um AI agents. And um it allowed us by comparing a diversity of strategy to surface the best approaches. Um and from there to iterate and bring more test cases through more incidents and reach higher and higher quality. So, the idea here is that um the bots will try to solve the same case and we use an LLM as a judge to compare the different approaches and we have like different um criterion because for the incidents we have um a verified root cause by a human. So, this gives gives us like a very um our ground truth to compare. And the LLM as a judge will compare this ground truth against um the the answers that the agents came up with. Um yeah, and that's so and the the important part at first was not even um like the score, but these were the insights like this tool was better uh with this strategy, and this one has maybe um like some noise in in the results that poisons the context or um the returned result from this specific tool are like it's too much. So, we managed to really optimize uh bit bits by bits um and come up with um the investigation V2 that we just released, and it's uh a massive improvement compared to uh our V1 approach. >> So, is it comparing just different models for investigations or is it also comparing like GCX and NCP or versus assistant? >> Right. So, um both actually. So, we have different um versions of our harness for investigations that we run with um Sonnet and with Opus. But, we also use Claude code harness with GCX, with Grok and NCP, and even just using curl to like directly hit our public API. Yeah. >> Do the models ever cheat? Specific >> Um so so far, it's been quite good. We have guardrails. Uh so, we make sure So, basically because we investigate on past incidents, um we need to make sure that the LLM um only looks at a specific like time window, so only when the incident started because else it would be able to um like find the pull request that were used to solve the the incident. So, uh but they're they're pretty good at at following the rules. They take it as a game a little bit. And uh yeah, it's so far I mean we have a LLM that comes uh so an agent that checks afterward with the judge to make sure that um like they they followed every rule and they did check. But actually it's a it's a fun it it's funny because um we had the case where using GCX it started to use some tools that we did not think about in the first place. And they were actually very useful for investigation, but they were like we never thought about them. And this was like we brought them to our investigation harness and it it helped a lot actually. So, um letting giving the agents um freedom and creativity in in this kind of environment is very useful. It's like this diversity that spawns this this new ideas that we can put in in our work. >> Cool. Do you have any plans to like publish this and and share this so that other people can do it too kind of like Ali bench? >> Yeah, I think why not? I think we we can we can go this way also. I'm sure this would be useful for other agents and and it would be very nice if we could also compare um agents from like other people, other companies maybe with different harnesses, um maybe even different um like tools because right now it's mostly about our MCP, uh our CLI, uh or our investigation harness, but if the community comes up with their own investigation agent, I think I have seen a few. It would be fun to to like put them in the arena and help not just like our product, but any product to to improve in in quality.

