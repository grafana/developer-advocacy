# Why Engineers Don&#39;t Trust Autonomous AI — 4th Annual Observability Survey | Grafana Labs

Published on 2026-06-05T10:00:09Z

## Description

The 2026 Observability Survey from Grafana Labs heard from over 1300 engineers and leaders across 76 countries on the ...

URL: https://www.youtube.com/watch?v=DSIYi9aYizQ

## Summary

In this video, Grafana Labs presents insights from their fourth annual observability survey, which gathered responses from over 1,300 engineers and leaders across 76 countries. The main focus is on the role of AI in addressing the increasing complexity of observability, where the survey revealed that the overhead of managing tools is a significant bottleneck. The speaker discusses how AI can efficiently correlate data, reducing manual investigation time and aiding in anomaly detection. However, the survey highlights a reluctance to fully trust AI for autonomous actions, emphasizing a desire for transparency and context in AI reasoning. The video concludes by noting the importance of LLM observability and how organizations need to integrate AI monitoring alongside existing infrastructures to build trust and ensure reliability. Viewers are encouraged to explore the full report and interactive dashboard available on Grafana's website for deeper insights.

## Chapters

00:00:00 Introductions and overview of the observability landscape  
00:01:30 Key findings from the observability survey  
00:03:00 Complexity as the primary bottleneck for teams  
00:04:15 AI's role in reducing complexity and improving efficiency  
00:06:00 The challenge of manual input in AI adoption  
00:08:30 Importance of transparency in AI reasoning  
00:10:00 Discussion on performative reasoning in AI models  
00:12:30 The trust factor in AI for autonomous actions  
00:14:00 Overview of LLM observability and its current state  
00:16:30 The future of AI in observability and its role as a copilot

# 2026 Observability Survey Insights

Hi everyone. The past year has witnessed a massive shift in the observability landscape. But what's actually happening on the ground? To find out, we at Grafana Labs reached out to the global community for our fourth annual observability survey. We heard from over 1,300 engineers and leaders across 76 countries. Today, I'll dive into the data to explore the community's perspectives on the real-world role of AI in observability and how we're navigating these fast-moving waters.

## Complexity: The Biggest Concern

Let's start with the biggest concern in observability today: **complexity**. According to the survey, the sheer complexity and overhead of setting up and maintaining tooling is the primary bottleneck for most teams. It's a bit ironic—we've built incredibly sophisticated stacks to give us visibility, but the sheer amount of telemetry we're producing has created its own kind of fog. This complexity is a massive drain on resources, but it's also where AI's current capabilities shine.

AI is uniquely suited to find correlations across multidimensional data at scale. Instead of an engineer manually dashboard-hopping to link a specific anomaly to a system change, AI can correlate those events almost instantly. For example, it can detect a sudden spike in error rates and immediately point to a configuration change or a specific pull request that was merged just a few minutes earlier. This effectively turns a one-hour manual investigation into a ten-second confirmation, allowing the team to move straight to the fix.

## The Challenge of Manual Input

While AI can, in principle, help reduce complexity, a key finding from the survey is that people don't want to replace one form of toil with another. The biggest hurdle to AI adoption is the requirement for too much manual input. Essentially, engineers don't want to spend more time feeding an AI context than they would have spent solving the issue themselves. They want a system that understands the environment out of the box.

Our survey isn't the first to observe this sentiment among developers. Recent research from the Stanford Digital Economy Lab highlighted that failures in AI adoption often stem from poor workflow integration and context debt rather than inadequate model quality. Solving context debt requires a fundamental shift from feeding the AI snippets of data to giving it access to the full environment. This principle guides our development at Grafana Labs. By leveraging the telemetry already unified in the platform and providing access to additional data sources, AI gains immediate access to the full context of the environment. It’s not just looking at logs in isolation; it’s seeing the interconnected picture you see.

## The Demand for Transparency

One of the most significant shifts in 2026 is the demand for **transparency**. Ninety-five percent of respondents stated it's important for AI to show its reasoning, whether that's citing documentation, explaining its query logic, or providing the internal chain of thought used to correlate different signals. In our world, a black box answer is a real risk. We want AI to show us its work so we can verify the conclusions before taking action.

However, there is a nuance here worth noting. While users want transparency, recent research on LLM reasoning suggests that simply seeing the thought process is not enough. A paper from researchers at Goodfire AI and Harvard challenges the idea that a chain of thought provides a truly transparent window into the AI's logic. They found a phenomenon where models often appear to be reasoning but have actually decided on the answer early on. This is termed **reasoning theater** or **performative reasoning**, where the AI generates a plausible-sounding justification to satisfy the user.

The takeaway is critical: we cannot treat a chain of thought as a substitute for verifiable evidence. That's why at Grafana Labs, we focus heavily on grounding the AI in your data and treating the chain of thought as another system output—something to observe, test, and verify rather than accept at face value. We pressure-test the model's reasoning using counterfactuals and adversarial evaluations to ensure its logic holds up under scrutiny. By anchoring that logic in the entire context of your operations—real-time telemetry, incident history, alert rules, chat conversations, and more—we ensure the reasoning is grounded in and constrained by your environment's ground truth.

## Trust in AI

This brings us to the core of the AI conversation: **trust**. When we asked how valuable it would be for AI to handle various tasks within an observability platform, we saw a high readiness for tasks like anomaly detection, dashboarding, query generation, forecasting, onboarding, and root cause analysis. However, that readiness drops drastically when it comes to autonomous action. Fifteen percent of respondents explicitly stated that they don't yet trust AI to act on their behalf. Of those that do trust AI, 36% say that its assistance is not valuable or only somewhat valuable.

Essentially, people readily adopt assistive AI but remain skeptical of autonomous AI. This skepticism makes perfect sense: trust is earned, not granted. Autonomous AI is a long-term evolution that can only happen once the technology has proven its reliability over time. That's why our approach at Grafana Labs centers on **human-in-the-loop AI**. Instead of building a closed system, we ground our models in your unique operational context. By keeping the workflow interactive, we ensure the AI acts as a reasoning assistant that you can steer and validate in real time. The goal is not to replace your judgment but to accelerate it.

## LLM Observability: An Emerging Area

Finally, let's look at **LLM observability**. Compared to other emerging areas in our survey, LLM observability is still in its infancy. In late 2025, when we ran the survey, 29% of organizations said it's not on their radar yet, and only 14% were actually using it in production. Now that we're a few months into 2026, it's likely that more organizations are adopting LLM observability, but I don’t expect adoption to be drastically different. This creates a dangerous discrepancy: the industry is rushing to deploy AI agents, but very few have the means to monitor their effectiveness. Most teams are effectively flying blind.

As a recent Gartner Innovation Insight Report points out, and as many of you likely feel instinctively, LLM observability is the strategic enabler for modern AI. Trust is the biggest barrier to adopting autonomous AI, and you can't build trust by just deploying and hoping for the best. You need telemetry that allows you to scale with evidence. By systematically evaluating prompts and monitoring performance in real time, you can move away from guesswork toward deterministic quality. This level of visibility is exactly what closes the trust gap, turning a black box mystery into a transparent system you can verify and rely on.

Gartner identifies LLM-specific signals that traditional observability simply doesn't cover, such as prompts, generated responses, and token usage. Since you indicated that cost is your number-one selection criterion for new observability tools, managing token consumption becomes a core requirement. By surfacing LLM-specific signals alongside your existing infrastructure data, you're transforming AI from a black box into a first-class citizen of your telemetry.

## Conclusion

The 2026 observability survey results show that we're moving beyond just observing our systems to actually conversing with them. With AI, we're finally at a point where you can ask a dashboard what's wrong and get a useful answer instead of a wall of raw logs. However, the results also reveal that we're making a sharp distinction between intelligence and autonomy. Most of us will happily trust AI to find the needle in the haystack, but we aren't ready to let it sew our parachute—mainly because we fear it might decide that the most efficient way down is to skip the parachute entirely.

This is a sign that our use of AI is maturing. We're past the honeymoon phase and into the pragmatic realization that, while AI is incredibly good at probabilistic detection, observability still requires deterministic truth. Essentially, we stopped looking for a magic wand and started seeking a trusted copilot. 

To me, that’s the optimistic takeaway: AI isn't here to replace us; it’s here to take on the busy work. It's moving us from the toil of finding problems to the craft of solving them.

If you'd like to dig into the numbers yourself, you can find the full report on our website. We've also built an interactive dashboard where you can slice the data by region, industry role, or company size to see the trends that matter most to you. We've compiled a deep dive into our own takeaways, but the real insights come when you apply the data to your own world.

I appreciate your time. Thanks for watching!

## Raw YouTube Transcript

Hi everyone. The past year has been a year of a massive
shift in the observability landscape, but what's actually happening on
the ground? Well, to find out, we at Grafana Labs reached out to the
global community for our fourth annual observability survey. We heard from over 1,300 engineers
and leaders across 76 countries. And today I'll dive into the data to
see what the community told us about the real world role of AI in observability
and how we're all navigating these fast moving waters. So let's start with the biggest concern
and observability today. Complexity. According to the survey, the sheer complexity and overhead of
setting up and maintaining tooling is the primary bottleneck for most teams. It's a bit of an irony
we're all living through. We've built these incredibly sophisticated
stacks to give us visibility, but the sheer amount of telemetry that
we're producing has created its own kind of fog.
It's a massive drain on resources, but it's also where AI's
current capabilities shine. AI is uniquely suited to find
correlations across multidimensional data at scale. So instead of an engineer manually
dashboard-hopping to link a specific anomaly to a system change, AI can correlate those events almost
instantly. It can look, for example, at a sudden spike in error
rates and immediately point
to a configuration change or a specific PR that was merged just
a few minutes earlier. Effectively, it turns a one hour manual
investigation into a 10 second confirmation - allowing the team
to move straight to the fix. Now, while AI can, in principle,
help reduce complexity, a key finding from the survey is
that people don't want to replace one form of toil with another. The biggest hurdle to adoption of
AI is the requirement for too much manual input. Essentially, engineers don't want to spend more
time feeding an AI context than they would've spent solving the
issue themselves. They want
a system that understands the environment out of the box. Our survey isn't the first one to
observe the sentiment among developers. Recent research from the Stanford Digital
Economy Lab looked at enterprise cases where AI successfully moved from pilot
to production and they highlighted a critical reality. While we expect
the technology to be the hard part, failures typically don't stem from
inadequate model quality. Instead, they hit a wall with poor workflow
integration and context debt. Solving context debt
requires a fundamental shift, moving from feeding the AI snippets of
data to giving it access to the full environment. And that's been the guiding principle
behind our development at Grafana Labs. By leveraging the telemetry
already unified in the
platform and providing access to additional data sources, the AI gains immediate access to
the full context of the environment. So it's not just looking, for example, at logs in the silo. It's seeing the
same interconnected picture you see. This turns AI into a collaborator
that understands your specific stack rather than an apprentice that needs
constant handholding and direction. Now, one of the most significant shifts in
2026 is the demand for transparency. 95% of respondents stated it's
important for AI to show its reasoning, whether that's citing documentation, explaining its query lodging or providing
the internal chain of thought the model used to correlate
different signals. In our world, a black box answer is a real risk. We don't want the AI to
just give us an answer. We want it to show us its work so we
can verify the conclusion before taking action. But there is a small nuance here
that I would like to double click on. While users want transparency, the latest research on LLM reasoning
suggests that simply seeing the thinking is not enough. This paper
from researchers at Goodfire AI and Harvard, challenges the idea that a
chain of thought provides
a truly transparent window into the AI's logic. What they found is a phenomenon where
models often look like they're reasoning, but they've actually decided
on the answer early on. This is what they call reasoning
theater or performative reasoning, where the AI makes a near instant
decision and then generates a long plausible sounding justification
to satisfy the user. The takeaway for us is critical. We cannot treat a chain of though as
a substitute for verifiable evidence. That's why at Grafana Labs, we focus so heavily on grounding the
AI in your data and treating chain of thought like any other system output
as something to observe, test, and verify rather than take at face value. We pressure test the model's
reasoning using counterfactuals and adversarial evaluations to ensure
its logic holds up under scrutiny. By anchoring that logic in the
entire context of your operations, your real-time telemetry, your
incident history, your alert rules, your chat up conversations and so on. We ensure the reasoning you see is
anchored in and constrained by your environment's ground truth rather
than just a performative explanation. And this brings us to the core
of the AI conversation. Trust. When we ask how valuable it would be
for AI to handle various tasks within an observability platform, we saw a high readiness for things
like anomaly detection, dashboarding, query generation, forecasting,
onboarding, and root cause analysis. But that readiness drops drastically
when it comes to autonomous action. 15% of responders explicitly
stated that they don't yet trust AI to act on their behalf.
And of those that do trust AI, 36% say that it's not valuable or
only somewhat valuable. Essentially, people readily adopt assistive AI, but they remain very skeptical of
autonomous AI. And that makes perfect sense. Trust is earned not granted. Autonomous AI is a long-term evolution
that can only happen after the technology has proven its
reliability over time. That's why our approach at Grafana
Labs centers on human in the loop AI. Instead of building a close system, we ground our models in your
unique operational context. And by keeping the workflow interactive, we ensure the AI acts as a reasoning
assistant that you can steer and validate in real time. The goal is not to replace your
judgment but to accelerate it. Finally, let's look at LLM observability. Compared to every other
emerging area in our survey, LLM observability is still
in its infancy. In late 2025, when we ran the survey, 29% of organizations said it's
not on their radar yet and only 14% were actually using it in production. Now that we're a few months into 2026, it's likely that more organizations
are adopting LLM observability, but I don't actually expect adoption
to be drastically different and this creates a dangerous discrepancy.
The industry is rushing to ship AI agents, but very few have the eyes
on them to know if they're working. Most teams are effectively flying blind. As a recent Gartner Innovation
Insight Report points out, and as many of you likely
feel instinctively, LLM observability is the
strategic enabler for modern AI. We've already seen that trust is the
biggest barrier to adopting autonomous AI and you can't build trust by just
deploying and crossing your fingers. You need telemetry that allows
you to scale with evidence. By systematically evaluating prompts
and monitoring performance in real time, you move away from guesswork and
toward deterministic quality. This level of visibility is
exactly what closes the trust gap. It turns a black box mystery into a
transparent system you can actually verify and rely on. Gartner identifies LLM specific signals
that traditional observability simply doesn't cover, such as prompts, generated responses and token usage.
And since you told us that cost is your number one selection criteria
for selecting new observability tools, managing token consumption
becomes a core requirement. By surfacing LLM's specific
signals alongside your existing infrastructure data, you're transforming AI from a black
box into a first class citizen of your telemetry. And the reality is that while the majority
of organizations aren't yet observing LLMs in production, Gartner's
research suggests that when they do, they will not want another AI silo. They'll want to monitor agentic
systems alongside the rest of their infrastructure. At Grafana Labs, we've anticipated this by building AI
observability tools that live where your data already lives. By monitoring complex agentic systems
alongside your existing infrastructure, you ensure your AI is not a
siloed experiment but a reliable observable part of your ecosystem. So the 2026 observability survey results
show us that we're moving beyond just observing our systems to actually
conversing with them. With AI, we're finally at a point where you can
ask a dashboard what's wrong and actually get a useful answer instead
of a wall of raw logs. But the results also revealed that
we're making a sharp distinction between intelligence and autonomy. Most of us will happily trust AI
to find the needle in the haystack, but we aren't ready to
let it sew our parachute, mostly because we are afraid it might
decide that the most efficient way down is to skip the parachute entirely. It's a sign that our
use of AI is maturing. We're past the honeymoon phase and into
the pragmatic realization that while AI is incredibly good at
probabilistic detection, observability still requires
deterministic truth. Essentially, we stopped looking for a magic wand and
started looking for a trusted copilot. And to me, that's the optimistic takeaway. AI isn't here to replace us. It's here to take the busy work.
It's moving us from the toil of finding problems to the craft of solving them. If you'd like to dig into
the numbers yourself, you can find the full
report on our website. We've also built an interactive
dashboard where you can slice the data by region, industry role, or company size to see the
trends that matter most to you. We've put together a deep
dive into our own takeaways, but the real insights come when you
apply the data to your own world. Appreciate your time. Thanks for watching.

