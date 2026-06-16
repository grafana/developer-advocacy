# How the AI Team Scaled Grafana Assistant Context and Built AI Observability

Published on 2026-05-14T17:18:02Z

## Description

Grafana Assistant turned hours of dashboard work into minutes — but scaling an AI agent from impressive demo to reliable ...

URL: https://www.youtube.com/watch?v=Ec5xlCIggh4

## Summary

In this GrafanaCON presentation, Ivana and Yasir discuss the evolution and capabilities of the Grafana Assistant, an AI agent designed to enhance user interactions with Grafana through natural language processing. They highlight the Assistant's growth over the past year, noting an increase in active users and contributions, along with improvements in context engineering, coding agents for self-improvement, and AI observability. Key points include the introduction of "memories" for better context retention, the implementation of "Skills" for capturing organizational knowledge, and the development of a self-improvement loop that uses coding agents to enhance the Assistant's performance. The talk also emphasizes the importance of AI observability for monitoring the Assistant's behavior in real-world applications, showcasing a demo of Grafana AI Observability. Overall, the presentation underscores that creating effective AI agents involves not just advanced models but also relevant context and continuous improvement processes.

## Chapters

Here are 10 key moments from the livestream along with their timestamps:

00:00:00 Introductions of Ivana and Yasir  
00:01:30 Overview of Grafana Assistant and its growth  
00:03:00 Introduction of the three major challenges faced  
00:04:15 Explanation of context engineering and its importance  
00:06:00 Introduction of Assistant Memories feature  
00:08:30 Overview of Skills and their capabilities  
00:10:45 Discussion on managing context effectively  
00:14:00 Introduction of self-improvement loop for Assistant  
00:18:30 Announcement of o11y-bench for Observability agents  
00:25:00 Live demo of Grafana AI Observability in action  

# GrafanaCON AI Talk Transcript

**Hello, GrafanaCON!**  
I'm Ivana.  
Hi, and I'm Yasir. Welcome to your mandatory AI talk. Let's make it actually useful. Today, we're discussing what happens when your AI agent grows up.

Last year, right here at GrafanaCON, we introduced **Grafana Assistant**, our AI agent for Grafana. We demonstrated how you can use it to query your data, build dashboards from scratch, and accomplish tasks in Grafana using natural language. Over the past year, it has been wonderful to see how many of you have started using Assistant in your day-to-day work. 

We've seen people sharing their experiences on social media, writing blog posts, and even racing against Assistant on YouTube to see who can build a dashboard faster. **Spoiler alert:** Assistant wins, turning hours of work into minutes. Here are just a few examples of its impact and how Assistant is changing the way people interact with Grafana.

A year later, Assistant has grown up fast. We now have thousands of active users, we've merged nearly 4,000 PRs, and our team has expanded from about nine people to more than 90 contributors across Grafana. While PRs can be considered an anti-metric, behind them are real improvements. We've developed better tools and support for new data sources like AWS CloudWatch and SQL. Additionally, we've expanded Assistant's capabilities; it can now utilize a knowledge graph, assist with k6 load tests, and handle some IRM incidents. We are still working to expand Assistant into more areas of Grafana.

However, this growth does not come for free. As Assistant has become larger, its behavior has become less predictable, and making changes has become more challenging. Today, we will discuss how we've overcome three major challenges: 

1. Making Assistant more useful through context engineering.
2. Iterating on it with confidence using coding agents and a self-improvement loop.
3. Understanding and trusting Assistant in production through AI Observability.

## Making Assistant More Useful

A significant part of making Assistant useful lies in context. An AI assistant is only as helpful as the context it has. If it does not understand your system, it will spend valuable time trying to figure out what you have instead of helping you with your needs. Therefore, we invested heavily in context engineering, which includes three layers of context:

1. **What You Have**: This includes your dashboards, data, services, and tables.
2. **What You, Your Team, and Your Company Know**: This encompasses an understanding of how your team works and how your company operates, often captured in runbooks, triage guides, internal APIs, or documentation.
3. **What You Are Doing in the Moment**: This refers to the specific task you are trying to solve while using Assistant.

Let’s start with what you have. Many of you have various data sources used for different purposes and types of data. We believe you shouldn’t have to explain all of that to Assistant every time you interact with it. So, we built features that bring this context to Assistant automatically. Examples include dashboard scans and table discovery using your knowledge graph.

Today, I want to highlight a new capability we call **Assistant Memories**. Memories allow Assistant to regularly (weekly) scan your observability data sources, such as Prometheus, Loki, and Tempo. It discovers services running in your environment, groups them into logical domains, and keeps persistent memory of where things are running, how they are monitored, their dependencies, and top metrics. 

This means that the next time you ask Assistant a question, it does not have to start from scratch; it already understands your environment. It can check its memories and jump directly to querying, grilling, and logs, metrics, and traces, as well as answering your questions.

While that is the context we can discover, there is another kind we cannot: the context that lives with you. This includes how your team works and how your organization operates—the knowledge contained in runbooks, internal APIs, or even just in someone's head. This knowledge is incredibly valuable, which is why we've built **Skills**. Skills allow you to capture this knowledge within Assistant, and you can even import them from GitHub repositories, making it easier to bring in existing runbooks and documentation.

Skills can reference dashboard data sources, tools, or other skills, making them more than just instructions. They are repeatable workflows that can be triggered directly as commands or utilized by the agent when necessary. So, next time someone asks, "Why is my service slow and how do I fix it?" Assistant can search the shared knowledge base, find relevant information, and pull in the right runbook—even if the user never mentioned it by name. This enables faster, more reliable, and repeatable task execution.

Now, let’s discuss the third layer of context: what you are doing in the moment when using Assistant and what you are trying to achieve. We’ve solved this in several ways, starting with **hooks**. We created hooks that Grafana app developers can use to pass context to Assistant automatically. For example, if you're on an explorer page and you open Assistant, it already knows what kind of data source you have selected and what query you were working on, allowing you to seamlessly continue your work in Assistant.

Sometimes, that is not enough, so we made it easy for users to reference what they’ve been working on. We added one-click actions, such as "analyze this trace" or "explain this log line." If you are in a dashboard, we equipped it with a literal pointer, so you don’t have to describe which panel you would like to update; you can just point to it. Additionally, you can attach images to your messages to Assistant. If you see a beautiful dashboard you’d like to recreate—whether it’s a Grafana dashboard or any dashboard created by any tool—you can take a screenshot, send it to Assistant, and it will recreate it for you with your data.

More context helps significantly, but we should also acknowledge that the context window is not unlimited. Let’s discuss a few techniques that help us manage it effectively:

- **Deferred Loading**: For less commonly used tools, we load tool descriptions and instructions on demand, saving tokens while still supporting numerous capabilities.
- **Context Compaction**: If you have a long conversation that approaches the context window limit, we keep only the most relevant and important parts of the context moving forward.
- **Summarization of Large Tool Outputs**: When your tool runs a large query or loads a long runbook, not every character or part of the query response is relevant. We use summarization to retain only what is important, outputting it in a concise manner and again helping to save tokens.

In conclusion, while more relevant context is crucial for making Assistant useful, it also brings complexity, which can create opportunities for things to break. Our goal is to convert all this context into predictable and reliable behavior.

## Iterating with Confidence

So far, we’ve discussed how to make the system more useful, but what do you do when, despite all this, the agent still doesn’t behave as expected? We put this to the test to evaluate how good our AI agents are at observability tasks.

We designed a suite of tests where an agent had three attempts to solve each task. The agent scored points if it passed at least one of three attempts, achieving an 82% pass rate. While that looked promising, we also examined consistency—whether the agent solved the task every single time, not just once every three attempts. The results showed a significant drop, indicating what we refer to in software as a flaky test. However, in AI, this can be a feature, making iteration more challenging. 

You might think, "Just give the AI more instructions," and we did try that. Even when we provided explicit instructions, the AI still didn’t consistently perform as expected. An early version of our Slack Assistant serves as an example of this problem. Programming behavior in natural language is challenging, especially as AI can act in mysterious ways. As the scale increases—with thousands of lines of prompts and tool instructions—it becomes difficult for anyone to understand the whole system and make changes without inadvertently breaking something else. 

If only there were a technology adept at writing and understanding language, capable of processing vast amounts of information at a relatively low cost, and able to make targeted changes based on input. That’s what we decided to test. We thought, what if we could use AI to improve our AI?

### Self-Improvement Loop

We decided to send Assistant on a journey of self-improvement. Self-improvement, in this case, consists of three steps:

1. **Introspection**: Look inward to discover what’s working and what’s not.
2. **Reflection**: Learn from the experiences.
3. **Making Changes**: Implement changes to improve performance.

This self-improvement loop is ongoing. In practice, it’s powered by coding agents, such as cloud code paired with our internal tools and custom agent skills. They help us navigate through this loop, process large transcripts and code, and streamline the improvement process.

**Introspection** is the most crucial step. If you don’t know what good looks like, the rest of the journey falls apart. Evaluating agents can be challenging, especially with observability tasks that can fail in subtle ways. For example, the AI might generate a valid query but not the correct one, or create a dashboard but not in the desired manner.

To evaluate effectively, we employ three methods:

1. **Deterministic Checks**: For example, if we ask for a dashboard with four panels, we check if it created exactly four panels. If it mentions a trace ID, we verify if that trace ID exists. These reliable checks help us determine basic correctness.
   
2. **LLM Rubrics**: For more complex evaluations, we use an LLM judge and task-specific criteria to assess whether the agent followed the right instructions or found the correct root cause.

3. **Fact-Based LLM Rubrics**: We define what a known good query looks like for a task, run that query in a controlled environment, get the results, and compare them to what the agent produced. This approach ensures we verify whether the agent's output is correct based on actual data.

By aggregating these tasks, we can create a benchmark suite, allowing us to compare different models across various observability tasks. With this, we can measure the reliability of different AI agents instead of relying solely on handpicked demonstrations.

Many companies conduct internal evaluations, but we are not just any company. I made a promise last year to introduce **o11y-bench**, our first open benchmark for observability agents. It includes everything needed to reproduce the leaderboard: tasks, environments, grading logic, and even our results. Our goal is to share these learnings openly, help define what good looks like, and contribute to the broader community building agents around observability. If you want to learn more, clone the repo or read our blog post released yesterday. You can also catch us after the talk.

Now, let’s discuss **Reflection**. This involves examining the good and the bad. We should look beyond headline pass rates and analyze actual evidence. The broader benchmark run reveals which tasks fail, which pass, and where the weak spots are. We can drill down into specific tasks to understand what happened, examining the steps the agent took, which tool calls were made, and the entire transcript of the conversation.

This benchmark becomes useful not just for identifying a score but for understanding what broke and what patterns emerged. Once we gather these results, we can run them through another coding agent, processing thousands of transcripts. This allows us to map out what the system excels at and where the biggest opportunities for improvement lie.

As any life coach would say, **Growth Requires Change**. Change could involve adjusting prompts, tuning instructions, improving tool layers, fixing bugs, or even recalibrating the benchmark itself. The better our learnings from the previous steps, the more targeted our changes can be. Once we have proposed changes, we can send the agent back through the loop to check whether the changes helped and decide on the next steps. Ultimately, the final call remains with us humans: the coding agent proposes, the benchmark verifies, and we can focus on reviewing, validating, and merging those changes.

This process allows us to continually optimize for cost, latency, quality, and reliability, all powered by coding agents and the feedback loop. However, even the best benchmark only tells us how the system performs in a controlled environment. Real users interact with Grafana in their own, sometimes unpredictable ways. Hence, once we ship, there is still one final challenge to conquer: production.

## AI Observability in Production

How do we tackle this challenge? The last question we need to answer is: what happens once Assistant leaves the lab and starts engaging with real users? That’s why we built **Grafana AI Observability**, our new database and platform for observing AI agents. You might have seen parts of it in yesterday's keynote. 

Grafana AI Observability combines our experience in building agents with our expertise in observability systems. It is designed to help us understand our agents, including Grafana Assistant, in production. 

I will now demonstrate Grafana AI Observability. Before I start the demo, I want to mention two important points: 

1. Grafana AI Observability is currently in public preview. You can test and try it with your agent starting today.
2. If we can get the slides working, I’ll proceed with the demo.

**Switching to Demo**

We aimed to make it very easy for users to start with Grafana AI Observability. On the setup page, you can find all the instructions needed to get started. We also created agent skills, so if you are using Cursor, Claude Code, or Copilot, you can instrument your apps quickly and send telemetry to Grafana AI Observability.

Now, let’s take a look at how we analyze our AI agent, including Assistant. We can answer questions such as: How many tokens are being used? What is the error rate? What is the time to the first token? And importantly, what are the costs associated with all of my agents? 

Grafana AI Observability includes many features, but I will focus on **online evaluations** today. Online evaluations help us determine how Assistant behaves when used by real users. Users interact with AI agents in unpredictable ways, so we want to ensure that Assistant responds correctly and securely.

The first step is deciding what correct behavior means to us. We set up our evaluators. The first evaluator is an **LLM judge**. We will use another LLM to evaluate our AI agent. Here, we want to ensure that Assistant grounds its answers in real data and does not hallucinate.

The second evaluator focuses on security. We evaluate whether users attempt prompt injection on Assistant. If we detect any, we can review the conversations to ensure Assistant responded securely. The last evaluator is a simpler heuristic that checks response length, ensuring Assistant does not overwhelm users with long texts and instead summarizes the data effectively.

You can create new evaluators based on your agent's techniques or select from numerous templates we have provided. 

Once we have our evaluators, we need to determine which conversations they will evaluate. For our Grafana Assistant, 20% of user-visible generations will be evaluated by our evaluators. We also added a simple integration for alerts, so with two clicks, you can set alerts. For example, if the pass rate falls below 80%, we will be notified.

Now, let’s start scoring. I previously created a similar evaluation role, allowing us to view the results. After updating the time range, we can see measurable data indicating how Assistant behaves. We can monitor trends and set up alerts to notify us if anything goes wrong. Additionally, we can drill down into specific conversations that failed evaluation.

In the conversation view, we can access all information about the interaction, including the user's communication with our agent, metadata, and evaluation results. Most evaluations pass, but if any fail—like groundedness—we receive insights into the reasons behind the failure. In this case, the user asked Assistant to create a new alert rule for the Infinity data source. The LLM judge indicated that while the query was good, it didn't verify the query structure.

We need to assess whether this is bad behavior or an isolated case. If it’s a pattern, we should turn it into a test case scenario, integrate it into our self-improvement loop, and ensure it is addressed in future iterations.

This is how we observe our AI agents in Grafana in a genuinely useful way. 

**End of Demo**

Now, let’s return to the slides. 

As we scaled up Assistant, we faced three major challenges:

1. How to make it more useful through context engineering.
2. How to iterate on it with confidence through self-improvement loops.
3. How to trust and understand it in production with AI Observability.

I want to leave you with this thought: better agents and better agentic systems are not solely about larger, more expensive models. It’s also about providing more relevant context, building effective improvement loops, and observing agents in production. That’s how we transition from impressive demos to something genuinely useful. 

Thank you!  
*(Audience applauding)*

## Raw YouTube Transcript

- Hello, GrafanaCON, I'm Ivana. - Hi, and I'm Yasir. And welcome to your mandatory AI talk. - And let's make it actually useful. Let's talk about what happens when your AI agent grows up. Last year, right here at GrafanaCON, we introduced Grafana Assistant, our AI agent for Grafana. We showed you how you can
use it to query your data, build dashboards from scratch, and get things done in Grafana
using natural language. Over the past year, it has been so great to see how many of you started to use Assistant in your day-to-day work. We've seen people sharing their
experience on social media, writing blog posts, even people on YouTube
racing against Assistant to see who can build the dashboard faster. Spoiler alert, Assistant wins turning hours of work into minutes. And here are just few
examples of that impact, and how Assistant is changing the way people interact with Grafana. - Yeah, and a year later, Assistant has grown up fast, right? We now have thousands of active users. We've merged nearly 4,000 PRs and we went from a single
team of about nine people to more than 90
contributors across Grafana. Now I know PRs are a bit of anti-metric. But behind these, there are
some real improvements, right? We've got better tools. We've got support from new data
sources like AWS CloudWatch. We've got SQL in there as well. And also, we just
expanded the capabilities that the Assistant has. So it can now, like,
utilize a knowledge graph, it can help you with your k6 load test, or even, like, deal with
some of the IRM incidents. And we're still continuing
to expand Assistant to even, like, more corners of Grafana. But all of this growth does
not come for free, right? As Assistant got larger, its behavior got less predictable and making changes got harder as well. So today, we're gonna talk about how we've overcome three major challenges: how we made Assistant more
useful with context engineering, how we're iterating on it with confidence using coding agents and
a self-improvement loop, and how we're using AI Observability to understand and trust
Assistant in production. - So how do we make Assistant more useful? A big part of the answer is in context because an AI assistant is
only as helpful and as useful as the context it has. If it does not understand your system, it's going to spend valuable time trying to figure out what you have instead of helping you with what you need. So we invested heavily
in context engineering. And it comes down to
three layers of context. First layer is what you have. Here we are talking about
your dashboard, your data, your services and tables. The second layer is what you, your team, and your company knows. It's an understanding
of how your team works and how your company operates. This is often captured in your
round book, triage guides, internal APIs or documentation. And the last layer is the context about what you are doing in the moment when you're using Assistant. What task are you trying to solve? So let's start with
what you have and, well, many of you have a lot
in your environment, a lot of different data sources used for different purposes and all kinds of data. And we strongly believe that
you should not have to explain all of that to Assistant every
time you interact with it. So we've built the features
and functionalities that bring this context to
Assistant automatically. Examples of these features
are dashboards scan, table discovery using
your knowledge graph. But today, I would like to talk about something that we call Assistant memories. Memories is a new capability where Assistant regularly, weekly, scans your
observability data sources such as Prometheus, Loki and Tempo. It discovers services
running in your environment, groups them into logical domains. And for each of these domains, it keeps persistent memory
of where things are running, how are they monitored, what are their dependencies
and top metrics. So next time when you
ask Assistant question, it does not have to start from zero. It already understands your environment. So it can just check memories and jump directly into
query, grill and logs, metrics and traces and of course answering your questions. - So that was context we can discover, but there's another kind we cannot, right? And it's a context that lives with you. It's how your team works, how your organization operates. It's the things that
live in your runbooks, your internal APIs or even stuff that just
lives in somebody's head. So that knowledge is incredibly valuable and that's why we've built Skills. So Skills allows you to capture
this knowledge in Assistant and you can even import them. Like if you have them in a GitHub repo, you can bring them in. And that makes it easier to bring in existing runbooks and docs. And because skills can reference
dashboard data sources, tools or even other skills, they're more than just instructions. They are repeatable workflows that can be triggered directly as commands or they can be used by the
agent when it needs it. So next time when somebody
asks like you know, "Why is my service slow
and how do I fix it?" Assistant can search this
shared knowledge base. It can find anything relevant, pull in the right runbook even if the user never
mentioned it by name. And then that allows it to
execute this task in a faster, more reliable and repeatable way. So that means like a
senior member of your team can write a triage guide once and then every other
on-call engineer on the team can then benefit from that same expertise. And with MCP integrations, Skills can go even beyond Grafana, right? You can reference any MCP tool in any skill that you define. So part of your step-by-step guide could be like pull in
some additional context from your AWS or your internal APIs or even it can take actions. So it be like create an
entry in our internal wiki. - And there is one more layer of context, it's the context about what
you are doing in the moment when you're using Assistant and what are you trying to achieve. And we've solved this in several ways. Starting with hooks. We created hooks that
Grafana app developers can use to pass context to Assistant automatically. So if you are for example an explorer page and you open Assistant, Assistant already knows what kind of data source you have selected and what's the query
you've been working on. So you can just seamlessly
continue your work in Assistant. But sometimes that is not enough and we wanted to make it very
easy for you for our users to reference what you've
been working on to Assistant. So we've added one click action such as analyze this trace or explain this log line. If you are in dashboard, we equip dashboard with a literal pointer. So you don't have to describe what panel you would like to update, you can just point to it. And you can also attach images to your messages to Assistant. So if you ever see a beautiful dashboard that you would like to recreate, and this can be Grafana dashboard or it can be any kind of dashboard you found on internet
created by any kind of tool, you can just take screenshot of it, send it to Assistant, and Assistant will be able
to recreate it for you with your data. So yeah, more context helps a lot, but we should also acknowledge that context window is not unlimited. So let's talk about few techniques that help us manage it effectively. Starting with different tools. Assistant has a lot of tools
and a lot of capabilities. For those tools that
are less commonly used, we use deferred loading. It means that we load tool descriptions and instruction on
demand only when needed. In this case, we are still able to support a lot of capabilities, but we are saving tokens. Also, if you have a long conversation that is close to hitting
context window limit, we use context compact compaction. This means that we keep
only the most relevant and important parts of
context moving forward. And last technique I would like to mention is summarization of large tool outputs. When your tool runs large query or loads large runbook, usually not every
character in the round book and not every part of that query response is relevant and adds value. So we use summarization to
keep only what's relevant, what's important, and then output it in a summarized concise way. Again, helping us save tokens. So to conclude, yes, more context and specifically more relevant context is crucial in making
Assistant actually useful. But more context also
brings more complexity, and more complexity
creates more opportunities for things to break. So in the end, we to
turn all of this context into predictable and reliable behavior. - Yeah, so far we talked about
the things that we can do and you can do to make
a system more useful, but like what do you do
when despite all of this, the agent still doesn't
behave like you want, right? So we put this at a test. We wanted to find out how good our AI agents really
at Observability tasks. So we designed a suite of tests and then we gave an agent three attempts to solve each task, and then like it got a score if it passed at least one side of three. So that's a pass rate at three And at 82%, that looked like a good score. Like you know, that looked promising. But then we looked at consistency. So this is about does it solve the task? Not just once every three
times but every single time. So every three times, and then you see like a much bigger drop. And in software like this, this is what we call
the flaky test, right? But then AI, this is a feature. And this makes iteration much harder. Because when you're making changes, you're not just changing behavior, you're also changing reliability. And you might think, well, just give the AI
more instructions, right? And we did that. We tried it. But even when you literally tell the AI exactly what to do, it still doesn't consistently do it. And you can see this example from an early version
of our Slack Assistant. And the problem here is that it's really
hard to program behavior in natural language, especially when like the AI
can move in mysterious ways. And this problem only becomes harder to reason about at scale. Like when you have thousands
of lines of prompts and tool instructions, it becomes hard for any one person to really understand the whole system and even harder to make changes without breaking something else. And that's a scary part of
large agentic systems, right? You might be fixing one behavior and then three other things that you weren't even
looking at are breaking. So if only there was something, a technology that was
really good at writing and understanding language could ingest vast amounts of information at a relatively lowish cost that may or may not be subsidized and then surgically make changes
based on your input, right? Sometimes it is a devil
that you know, right? So that's what we put to the test. We thought what if we could use AI to improve our AI? - And so we decided to send Assistant on a journey of self-improvement. And when I say self-improvement, you might be imagining something like this that we'd made our agent
do a little bit of yoga, meditation, a bit of self-discovery. Well, almost, In our case, self-improvement
looks like this. It has three steps. First one is introspection. So first you need to look inward, you need to discover
what's good and what's bad, what's working and what's not working. Then, you reflect and
learn from the experience. And last step is making
changes to hopefully improve. And this journey never really ends. It's an ongoing loop. And I promise I'm still
talking about the AI here. So in practice, and in our case, it looks like this. The self-improvement loop
is powered by coding agents such as cloud code paired
with our internal tools and custom agent skills. They help us walk through the loop, go through large amount
of transcripts and code, and make the whole improvement
process easier to run. - So let's start with
the first step, right? Introspection, and honestly
it is the most important step, because if you don't know
what good looks like, the rest of the journey
kind of falls apart. And it's really hard evaluating agents, like this is a very
hard step to get right, especially with Observability task because they can fail in very subtle ways. Like sometimes it can
generate a query that is valid but not the right query. Sometimes like you ask
it to create a dashboard and it creates a dashboard but not in the way that you ask for it. So we needed to come up with a way that was not just about
evaluating the text but actually being able to verify the outcome and the behavior. And we do this in three ways, right? We have deterministic checks. So if we ask for a
dashboard with four panels, we can check did it create
exactly four panels? If it mentions a trace ID, we can check does that
trace ID actually exist? So these are simple but
reliable checks that we can run. The second thing that
we're doing is LLM rubrics. And we use that for things that are a
bit harder to encode, like you know expresses code. So here we use an LLM judge and we use task specific criteria, like did it follow the right instructions? Did it find the right root cause? And these are quite helpful to validate the semantic
correctness of the answer. But then finally, and this is quite special
for Observability, is we use these fact-based LLM rubrics. So here we define for a task, we define what a known good query is. We run that query against
the controlled environment, get the result, and then compare to what the agent did. So if the agent says
latency is 2.3 seconds but then we run our query
and we get five seconds, we actually catch that. So this is a bit more than, oh, did the agent say the magic words? It said it's really about
verifying if the agent did the actual work and is
correct compared to the data. Now when you put a lot
of these tasks together, you get a nice little benchmark suite and then we can use that to
come up with a leaderboard. And this leaderboard is useful because it allows us to
compare different models across different categories
of Observability task. And with it, we can now actually measure how reliable different AI
agents are at Observability task instead of just relying
on a few handpicked demos. Now a lot of companies do
this kind of stuff internally, but we are not a lot of companies. And also I've personally
made a promise last year. So yesterday we announced that we're introducing o11y-bench, right? It's our first open benchmark
for Observability agents. So it has everything you need to reproduce that leaderboard. It has a task, the environment, the grading logic and
even our own results. And our goal is really here to share these learnings in the open, kind of help define what good looks like and hopefully like contribute back to the broader community that's like building agents
around Observability. So if you wanna learn more
about this, clone the repo. We read our blog post that
is out since yesterday. And also like you can always
catch us after the talk. So that was introspection. Let's talk about reflection, right? Learning the good from the bad. So I showed you this already, right? This is kind of like in this step we stop looking at just
the headline pass rates and we start looking
at the actual evidence. So on the on the right here, we can see the broader benchmark run. So we can see which task fails, which ones pass, which ones failed, and like just generally
where the weak spots are. But then on the right, we can drill into like a specific task and then we can look at
what happened, right? We can look at which
steps did the agent take, which tool calls, we can look at the entire
transcript of the conversation, and also look at why the
run failed or passed. So this already benchmark
actually becomes useful because it's not just about,
oh, the score went down, it's about, here's what
broke, here's the pattern and here's what we might wanna do next. Now once we have these results, we can then run them through
another coding agent, right? These are like thousands and
thousands of transcripts. So again, this is where
these agents can really shine because they can ingest
all of this information. And that gets us a map of
what the system is good at, what it's bad at, and also where the
biggest opportunities are. And that's really the
core of reflection here. It's about like turning this
pile of results and transcripts into something that is actually useful and an actual direction for improvement. And then as all life coaches
eventually will tell us, growth requires change, right? Change, whether that's
changing the prompt, tuning the instructions,
improving the tool layer, fixing bug, or even like
calibrating the benchmark itself. And the better our learnings
are from the previous step, the more targeted changes
the agent can come up with. And once we have these proposed changes, we can just go back to
the first step, right? We can send it back through the loop to check if the changes
actually helped or not and then decide on what to do next. So the final call still
remains with us humans, right? So the coding agent proposes,
the benchmark verifies and then we can focus on reviewing, validating, and emerging those changes. And that's how we improve
agents with confidence. And the journey never really ends there. Like as the agent gets more capabilities, we can run it through the loop again. And that allows us to
continuously optimize for cost, latency, quality, reliability. And all of this is
powered by coding agents and that feedback loop. But like even the best
benchmark, it only tells you how it works in a controlled environment, but the real world is a bit different. You still have real users
that interact with Grafana in their very own sometimes weird ways. So once we ship, there's still one final
mountain to conquer and that is production. - So how do we conquer that mountain? The last question we need to answer is what happens once
Assistant leaves the lab and starts dealing with the
real users in the real world? That's why we've built
Grafana AI Observability, our new database and platform
for observing AI agents. You could already see parts
of it in yesterday keynote. It connects our experience building agents with our experience building
Observability systems. With Grafana AI Observability, we've built something that we needed, something that helps us
understand our agents including Grafana Assistant in production. So I'll be doing a live demo for this. But before I start the demo and before my screen load, I would like to say two things. First one is that Grafana AI Observability is in public preview. So everything that I will
be showing you today, you can test, you can try with your agent as soon as today. Also, if we can get the slides,
- Switch the demo. - Working, so.
- Is it working? - Okay, yeah. So we wanted to make it very easy for you, for our users to start with
Grafana AI Observability. So if you go to start up, you can see all of the
instruction you need to set up. We also created agent skills. So if you are using Cursor,
Claude code or Copilot, you will be able to instrument
your apps within a minute and you will be able
to send your telemetry to Grafana AI Observability very fast. So now let's have a look. This is where we analyze our AI agent, including Assistant and answer questions such as how many tokens are being used, what is the error rate
time to the first token, or very important metric, what are costs associated
with all of my agents? Grafana AI Observability
has a lot of features, but today I will be focusing
on online evaluations. Because with online evaluations, we can answer that last question which is: how is Assistant behaving when it's used by real users? Because in practice,
users are using AI agents in unpredictable ways. And we still want to make sure that our AI agent Assistant is responding correctly and securely. So first step is deciding what
correct behavior means to us. And this is where we
set up our evaluators. So first evaluator I'm
setting up is an LLM judge. So we are going to be using
another LLM to judge our LLM, our AI agent. And here we want to make sure that Assistant grounds
its answers in real data and that it does not hallucinate. The second evaluator I'm setting up is more security oriented evaluator. So here we are evaluating whether users are trying to do prompt
injection on our Assistant. And in the case, we detected
we can review conversations and make sure that Assistant
responded securely. Last evaluator I'm setting
up is more simple one. So this is a heuristic one and we are just checking
the length of the response. So here we want to make sure that Assistant is not
showing a wall of text to you to our users that nobody would read and that it nicely summarizes the data. You could also create a new evaluator based on your agent techniques based on what do you care about, and either starts from scratch or we also created a lot of templates that you can choose from. So now when we have our evaluators, we need to decide where
are these evaluations on which conversations are
they going to be running? So let's select our Grafana Assistant. And in this case, 20% of
Grafana Assistant generations that are user visible are going to be evaluated
by our evaluators. We also added very simple
integration for alerts. So basically with two clicks, you can also add alerting. And in this case, if pass
rate falls under 80%, we will get notified. So we will learn if something
goes wrong with our agents. And we can start scoring. So as you can see, I created very similar
evaluation role before, so we can have a look at the result. I'll update the time range. And so now we have a data, a measurable way detect
how is Assistant behaving. We can monitor trends, we can even like we set up alerts so we will get notified
if something goes wrong. And we are even able to drill down into those
specific conversations that failed evaluation. So we can have a look at one of those. So this will take us to conversation view where we can say all of the information about the conversation. We can see how user was
communicating with our agents, we can see the metadata and we can see all of the evaluation that were run on this conversation. So as you can see, most of them passed but there is one that failed,
which is groundedness. We get also information
here why it failed. So you get more insights into why this LLM judge
considered this five out of 10. In this case, user was asking
to create a new alert rule for Infinity data source, but what is LLM judge telling us is that it provided a good query but it didn't double check what the query structure looks like. So we need to evaluate if this is a bad behavior or if it's fine, and if it's bad behavior, is it a one off case or is it actually a pattern that has been happening over time? And if it's a pattern, if we've noticed that this has been
happening multiple times, we should turn this
into test case scenario, bring it into our self improvement loop and make sure that we fix
this in future iterations. And so this is how we are observing our AI agents in Grafana
in actually useful way. This is the end of my demo and I would like to say that
if you are building agent and if you are interested
in AI Observability, go and test it out or you can join us in our AI demonstration and we will be more than happy to show you more features from
Grafana AI Observability. (audience applauding) - Let's go back to starts. Can we switch back to slides? Yes. Okay, so that was our story. So as we scaled up Assistant, we had to solve these three
harder problems, right? How to make it more useful
with context engineering, how we iterate on it with confidence with these self-improvement loops, and how we trust and
understand it in production with AI Observability. And I'm gonna leave you with this, right? Better agents and better agentic systems are not just about bigger,
larger, more expensive models, it's also about providing
more relevant context. It's about building and
using good improvement loops so that you can tune them. And also it's about observing
your agents in production, and that's how you move from something that's just like an impressive demo to something that is actually useful. Thank you. (audience applauding)

