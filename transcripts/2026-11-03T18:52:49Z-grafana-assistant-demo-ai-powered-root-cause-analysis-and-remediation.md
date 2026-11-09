# Grafana Assistant Demo: AI-Powered Root Cause Analysis and Remediation

Published on 2026-11-03T18:52:49Z

## Description

See how Grafana Assistant uses AI to investigate incidents, identify root causes, and help remediate application problems.

URL: https://www.youtube.com/watch?v=DCIlQAJJ7qQ

## Summary

The show titled "Grafana Assistant Demo: AI-Powered Root Cause Analysis and Remediation" was published on November 3, 2026. The speakers included Ksenia and Maurice, who discussed the capabilities of Grafana Assistant in leveraging AI for incident investigation, root cause analysis, and application problem remediation. They highlighted features such as dashboard creation, alert analysis, incident pattern recognition, and the introduction of an always-on agent that autonomously monitors systems and suggests solutions. Key takeaways included the efficiency gains from using Grafana Assistant for ongoing monitoring and alert optimization, as well as the potential for teams to focus more on strategic tasks rather than repetitive operational work.

Topics: Grafana Assistant, AI, root cause analysis, incident management, alert optimization, automation.

## Chapters

00:00:00 Introduction to Grafana Assistant and its capabilities
00:06:20 Grafana Assistant automations and incident investigations
00:12:34 Grafana Assistant for incident investigation and alert management
00:18:49 Grafana Assistant demo: using watchers for telemetry correlation

Hello. How are you guys feeling here in San Francisco? The weather's beautiful to showcase some of our newest things. I'm happy to be here and glad that we can be together. I forgot my clicker, so let me just grab that real quick. Thank you. It's my first time in San Francisco, and I already did In-N-Out. If you have any other recommendations for things to do, please let me know afterward. I really want to experience the culture. Where I come from, it's the world capital of pretzels and beer. Does anyone know what it is? No Germans here? Munich, yes! It's the Oktoberfest city. 

If you have eaten any pumpkin-spiced pretzels or any with dark chocolate, let me know. I haven't tried them yet, and I always want to have more savory experiences with pretzels. I recommend the ones with butter and pepper in Germany if you haven't had them yet.

All right, hi everyone! A little bit about me: I love the outdoors. Whenever I'm not working, you'll find me paddle boarding, rock climbing, or whitewater rafting. I'm always up for swapping recommendations for incredible places to explore around the world.

Now, let's dive in. The past year in AI has been a lot to keep up with—new models, new tools, and many new capabilities. For those of us building software, that's exciting. It means we can experiment faster, get ideas into users' hands sooner, and tackle many more things that previously felt out of reach. However, everything we build still has to run in production. It has dependencies and behaves differently under load. That means someone still needs to understand what has changed when, for example, latency starts climbing or why a deployment that looked perfectly healthy is now causing errors. 

We want AI to help us not only build things faster but also to run and understand things in production. Over the past year, many teams have been turning to Grafana Assistant for help with this work. Let's look at a few examples of questions it could help with. 

First, let's start with something familiar: building a dashboard. You can ask, "Check my available data sources and build a dashboard from the most useful metrics or logs." The Assistant will look at data that you have permissions to access, pull in all the most useful signals, and create a custom dashboard in a couple of minutes. You can ask the Assistant to iterate on it, maybe focus on a particular service, add a different visualization, or include more details. Even internally at Grafana, we have moved away from building dashboards manually because it is a massive time saver for us to just describe what we would like to see and then iterate on it with the Assistant. This gives us more time to actually think about what the dashboard tells us rather than writing queries and configuring panels.

You can also ask, "Analyze my alerts over the past 30 days and optimize them." The system will look at your alert history and identify sources of noise—alerts that constantly fire and resolve, duplicate alerts for the same underlying service, or alerts that fire so frequently that they stop being actionable. From there, it will come up with an improvement plan. This plan is not cast in stone but one that you can iterate and improve together, essentially becoming a guided process for improving your alerting setup.

Another question you can ask is, "Analyze incidents over the past two weeks and tell me what patterns you see." As many engineering teams know, similar problems keep coming back. Here, the Assistant will use semantic search to find relevant incidents and look for recurring patterns. This is a super low-effort way of understanding what keeps coming back for your team and where engineering investment or a deeper investigation can help prevent the next recurrence.

You can ask many different questions and get practical help grounded in your system and data. However, all these examples start the same way: someone opens the Assistant and asks. But what if you didn't have to ask? That is the next iteration we would like to share with you, where Grafana Assistant works as a 24/7 agent. Rather than asking the Assistant for help, a vision has evolved for it to become an always-on agent that constantly watches the state of your system, proactively bringing to your attention any issues or proposed solutions.

For this to be possible, we've given the Assistant four ways to take on work autonomously. The first is the "Eye of Sauron," or perhaps a little less dramatic, what we call watchers for always-on detection. Then we have automations for scheduled work, investigations for event-triggered work, and finally, managed sandboxes for coding tasks that you can delegate to agents.

Let's start with Assistant watchers. Watchers complement your existing alerts by allowing you to describe what matters in plain natural language and then having the Assistant turn that intent into ongoing checks against your telemetry. They watch for any concerning changes, surface insights with supporting evidence, and can also trigger a deeper investigation if there's something critical that needs attention.

Some work needs to run on a schedule, such as daily health summaries or weekly error reviews. For this, we have Assistant automations. Automations take a recurring task and give it to the Assistant to run on a given schedule. The results arrive either in Grafana or directly in Slack or your email, and every run has its own Assistant conversation so that you can dig into the findings and ask any follow-up questions.

When something does go wrong, Assistant investigations can start looking at it right away. When an alert fires or an incident is declared, an investigation can be automatically triggered, testing competing hypotheses against evidence from across your system. Tomorrow, during the IRM talk, you will hear about operational context and how findings from an investigation can be fed into the context of an ongoing incident alongside input from other agents. This allows you to build a shared understanding of what's happening so that both humans and agents can build on each other's findings and resolve incidents faster.

To make investigations practical at scale, we spent the past year continuously optimizing and evaluating our agent harness. Thanks to that optimization loop, we were able to build a highly optimized system that balances quality, speed, and cost, with the token savings passed on to you. Once a problem is understood, the next step is working towards a solution. You can hand over a task to a coding agent, which runs in its own managed secure sandbox in Grafana Cloud. The results come back to you as a draft PR, ready for your team to review and decide what ships.

Now, let's bring all of this to life with a demo. We will not have time to go through all of it, so after this talk and tomorrow, we would love to see you drop by one of our booths to see these capabilities up close and try them out yourself. Thank you, Ksenia. Let's now get into the weeds of how it all works. I will show you some easy workflows in the beginning, and then we will pull it back together into some more advanced workflows as we go through all the features we just mentioned. As Ksenia said, it's a little bit hard to cover everything in this talk, so please visit us at the booths, ask us questions, and you can also try out everything we show you today at the booths. 

Let's start very simply. I have Grafana Assistant open to the side. Let's say I'm very new to the stack and I have never...

been to the stack, I just onboarded on a team. So I ask, "What's being monitored in the stack? Can you draw me a diagram?" Grafana Assistant is now using what you just heard earlier, system search, to go through your whole stack, finding all your labels, the alert rules, the incidents that might be in your infrastructure, and everything you have been instrumented over time as you onboarded into Grafana. You can see that here, and you can always see how Grafana Assistant is working for you. 

And there we go. Just like that, we have a pretty quick diagram of what's going on. If it has been the first time for me to be in the stack, now I already know something very high level. This is something that can take onboarding new people in your team onto your stack from days down to hours so that they can get proactive more quickly. We also had a telecom talk where someone else, who had actually never touched their stuff beforehand, used the system to find something they never heard about to help them with that. So I really love that. I'm a PM, so I'm no engineer, and I can even ask Assistant what's going on with our telemetry data. It's pretty cool.

Okay, let's maybe dive a little bit deeper. Analyze my alerts of the last 30 days. Let's say 14, as it will take very long for us to go through that, 40 days. Which ones are good to keep? Which ones should we retire? Find patterns that help me improve my alerts. Grafana Assistant is a highly parallel agent. So while this is running, we'll actually go in another tab and do another task at the same time because this will be running for a minute or two now as it goes through all the alerts that we have in the stack. 

So on another tab, you can just keep working on Grafana Assistant, and now I will ask, "Are there any active incidents in this stack?" This is really to show you everything that is in your Grafana Cloud stack, be it your metrics, logs, traces, alerts, incidents, or maybe even your scale databases for your business data. Grafana Assistant can help you access that, correlate all of that in one go, and help you find the information you need. 

Okay, so we actually have some incidents ongoing here. Let me just copy that and just imagine, as I said, I'm new to the stack. I don't even know how all of this works. So I will just tell Assistant, "Take me to the name incident," and now Grafana Assistant will also navigate me to the UI element that we need. If you're unsure, like, "Oh, I want to instrument my things and I don't know where I should go," just ask Assistant. It will take you to the right page, get you started on instrumentation, alerting, or wherever you really want to go. 

So now we are on our IRM product. You will see more of that tomorrow in the IRM talk. In the IRM suite, we can now see this incident that has been ongoing for quite a while. That's when you can see when I started my demo stacks 70 days ago, so I practiced a lot to deliver this demo to you guys. We also have another feature down here, which is our assistant investigation that we just mentioned. 

Assistant investigation is our way in the background to asynchronously analyze what incidents are about. Let's say an alert is firing and it's critical. If you declare an incident critical, we can run investigations automatically with you. So the moment someone is paged and they're coming back to the PC, they already have something that they can go off on. 

So let's just open that really quick. This is an investigation that has already run. An investigation can run anywhere between a minute to 10 minutes, depending on how complex your stack is, how many data sources you have connected, and how complex the root cause is, but it will keep going. This is like its poll job. I like to call it our keep-going agent, which is literally built to just keep going until we find something it thinks is the right thing. 

On our investigations, we can now see there's a small summary of what's going on. We can see some data, a timeline of what has happened when, and we can see what was checked. We also have a feature for hypotheses, so you can see what the assistant tried to think about. In this case, it thought the incident was declared by automation before the banking process existed, as you can see in the demo environment. You can see the evidence for that and the timeline for that. 

We can even say, "This is it," or we can say, "Oh, this is actually not it," and steer the investigation. You can run your investigations either completely autonomously or with a human in the loop, where you help and steer, providing more information as it becomes available. You can do both, however you choose to do it. Lastly, we have all the sources so you know that the agent didn't just fabricate new logs that don't actually exist in your system. You can always review all of that. 

But let's imagine I also want to know what was actually the problem with that. Where's the code for that? We can just follow up on this investigation and ask for that. We can ask it, "Find me the code for this problem. Why did we have this problem?" So it's very unspecific. I didn't say which repo, I didn't say, "Oh, it's this service." I didn't say because I might not actually know. Sometimes you get alerted, and it just says, "Error rate is high," and you're like, "Okay, what should I do now?" 

With Grafana Assistant, you can search code and look at how your coding agents are working. And there we go. It has spawned a sub-agent for us. Oh, they see failed for some reason. Oh no, that happens when you do a live demo, but we can see how the assistant is recovering to try to get going again. In an ideal case, it would have just spawned a sub-agent for us, which would go through our repo and tell us what's actually going on. 

So let's maybe come back to that in a second and instead go back to our learning analysis. Who of you has alert noise? Okay. Who thinks alert noise is, well, noisy and annoying? No, just kidding. Of course, it's annoying. So with Grafana Assistant, when we analyze all our alerts, if you remember at the start of the demo, I asked for that. 

Let me actually zoom out. Sorry. We asked for that, and you can see what has happened here. Now we can see what the main patterns are. We have a broken notification sync that is sending all-time notifications. We have machine traffic, we have routes that fire with no panic, we have flapping warnings, we have correlated signals, and so on. So we have lots of alert noise in this stack specifically. 

The assistant even asks us what we should do next. We can change things; you can tell it, "Maybe let's just do this." Now the assistant will get to work for us and will work on this specific task and help us fix these alerts and alert rules so that they become better. Fixing alert noise is a job that's continuous; it's always happening. You always have more alerts, you have to retire new alerts, and more applications are onboarding while others are offboarding again. 

With Assistant, you can really always do a snapshot of that. If you would normally look at all of these alerts, it would take days, maybe even weeks, depending on the size of your stack, to find all the notification rules that are firing that might not be efficient, and so on. There we go. It even gives us recommendations on what we should do. 

So these are the basics of Grafana Assistant. Now let's go to the more advanced stuff that you can build. As you know, in the keynote, we announced Grafana pages as a new way to build any kind of view that you want to build. I was thinking I want to have a view, and let me share that view with you. I wanted to have just a very simple view for myself that I built in five...

**Grafana Assistant Demo: AI-Powered Root Cause Analysis and Remediation**

Everything you see here is built in five minutes, where I want to see just the essentials for me when I get started for my job. I was thinking maybe I should also have a little button that says "Brief Me," where I can see what's happening. Then we can see the platform has two major incidents with delayed transfers and so on.

I wanted to have my incidents up here. I wanted to have all the things that made me need me up here. I also wanted to have something about CI/CD. I wanted to see which of our GitHub actions are working, which are burning out, and which are very slow or stalling. So, I asked Grafana Assistant, connected to GitHub via the API, built it on a page, and now I have this overview pretty quickly. As I said, this was built in five minutes with Assistant pages.

Thank you! I also want to see all the pull requests that we have open because you always want to know if there are new merges getting merged in, or new changes being deployed. I wanted to bring in all the things that we have. So, I implemented tiny little buttons for me where I can just click "Ask," and now I already have a prompt preformed in here where we can ask about all of these things.

Another thing I wanted to do is sometimes you have PRs that are very big. They change lots of things that might change a lot of infrastructure. They change your backend or frontend significantly. I wanted to have a way to watch these things after they merge. So, I will just put this prompt in here. Let me zoom in for you guys real quick. 

Here I am creating a temporary throwaway watcher that will only watch this PR until it's merged and then kills itself essentially. So, watchers are also alerts that you can set a deadline on. You say, "I just want to watch this PR, and if it's working out, all good. If not, just stop." 

I will just start that. We won't go through this now because the watcher will actually look at all our telemetry. It will look at all the baselines and establish what the telemetry and the baseline look like. This will take about two to five minutes depending on how big your stack is. Instead, I'm just going to show you real quick what a watcher will look like when it's done.

A watcher is our new form to help you correlate across different things, for example, for release readiness or if you want to correlate telemetry data and business data. One example is checking on your checkout service while also seeing how much money is being transferred through that. Are orders going up or down? You can have it all in one view.

I have set up a watcher previously, which is my banking payment pipeline health one. If anyone works here at a bank, I think top of mind is probably transactions going through so people get their money on time. If not, that's kind of bad. I defined a very small mission for what it's supposed to watch. You can see here, it watches the banking payment pipeline in the namespace "banking prod" and so on. 

This watch has been running for quite a while and has created all of these little blips for me that are all looking fine. So, this watch is not alerting anything. We can click on that and see what's actually happening. You can correlate across different signals. This watch is monitoring metrics, logs, and traces all in one go, and you can have all of that in one watcher.

That's it for the demo. If you want to see more, as I said, it's very hard to condense all of this into just ten minutes for you guys. Please come to the demo booths. We have engineers here, seniors are here, and I'm here. You can ask us any questions, and you can try out all of this. We are not shy about that.

So, let's bring this home and take it to the end. 

Thanks, Maurice. You've seen a few ways to put Assistant to work, but there is so much more that you can build on top of that foundation. Think about your team. What problems keep coming back, or what would you love to keep a closer eye on if you had more time? 

You've seen in a demo how you can connect an alert or a watcher to an investigation and then task a coding agent to come up with a proposed solution. You can build on top of that by combining the various building blocks in the way that works for your team. You can connect together alerting and watchers in Incident Response Management (IRM) to decide when work should begin. 

You can use an investigation to understand what's happening and the managed sandboxes to come up with a proposed solution that you get to review and decide whether it ships. All of these are powerful building blocks that allow you to create a tailored workflow for your team. 

You can also learn from your users and customers faster than ever, and then take what you learn and use it to guide and prioritize what to build next. Most teams have a lot of customer context that already exists, but it's spread across various tools. You might have account information in Salesforce, calls in a warehouse like BigQuery or Snowflake, or support tickets in Jira, for example. 

A system does not need a separate integration for each of these. If your data sits in a Grafana data source or behind an MCP server, a system can bring that into the same conversation as your telemetry. It can maybe create an issue in Jira or Linear in GitHub, and then your team gets to decide what to do with that next.

Now, you can also describe an experience that you'd like to build and then work with Grafana Assistant to bring it to life as a Grafana page. You've already seen some examples during the keynote. We've also seen teams create very interactive, very powerful pages for things that matter to them, such as deployment trackers or how the systems evolve over time or custom visualizations for product adoption. 

You can iterate on these pages, share them with your teammates, and remix somebody else's creation. It opens up a lot of room to be creative and create an exact experience that you think will work best for your team. 

Now, you might have guessed it already, this presentation is all Grafana pages, so you can let your imagination go wild. The opportunity across all of these examples is to spend less time on the things that slow you down and more time on the work that you actually would like to move forward. 

But you don't have to take our word for it. This is how our customers describe the difference it's making for their own teams. Eric from CellPoint Digital says that his role is becoming much more architectural, allowing him to focus on translating ideas into technical requirements while Grafana Assistant takes care of most of the tedious work. 

Here's another quote from Alessio from Qubit. His team sees that with these tools, they experience fewer incidents, and when they do happen, they resolve faster, allowing them to stay focused on deploying new features. 

We started with questions you can ask the assistant, and then we've shown you what's possible when you don't have to ask every time. Now think about your own team. What would you like handled for you, and what would that free you up to focus on instead? Choose one recurring task, give a system the context it needs, see what you can take off your team's plate, and then build from there.

## Raw YouTube Transcript

Hello. How are you guys
feeling here in San Francisco? Weather's beautiful to showcase you
some of our newest things. Well, happy to be here. Happy that we can
be here together. I forgot my clicker. Let me just get me real quick. Thank you. And it's my first time in San Francisco.
So yeah, I already did in and out. If you have anything else I should
do, please let me know afterwards. I really want to experience the culture. So where I come from, it's the
world capital of pretzel and beer. Anyone know what it is? No Germans
are out, by the way? Munich, yeah. It's the Oktoberfest city. And the next one. And you can
ask me all about pretzels. So if we go to the next slide, if you have eaten any pumpkin
spiced pretzels or any with dark chocolate, let me know. I didn't eat them yet. And I always want
to have more savory experiences on the pretzel front, but I recommend the
ones with butter and pepper in Germany, if you haven't eaten them yet. All right. Hi everyone. A little
bit about me. I love the outdoors. So whenever I'm not working, you'll
find me paddle boarding, rock climbing, whiteboarder rafting. So I'm always up for swapping
recommendations for incredible places to explore around the world.
All right, so let's dive in. The past year in AI has been a
lot to keep up with. New models, new tools, many, many new capabilities. For those of us building
software, that's exciting. It means we can experiment faster. It means we can get ideas
into users' hands sooner. And it also means that we can tackle
many more things that previously felt out of reach. But everything we build still has to
run in production. It has dependencies. It behaves differently under load. And that means that somebody still needs
to understand what has changed when, for example, latency started climbing
or why a deployment that
looked perfectly healthy is now causing errors. So we want AI to help us not only build things faster, but also to run and
understand things in production. So over the past year, many teams have been turning to Grafana
Assistant for help with this work. So let's look at a few examples of
questions that it could help with. So let's start with something familiar,
building a dashboard. You can ask, check my available data sources and
build a dashboard from the most useful metrics or logs. So
what Assistant will do, it will look at data that you
have permissions to access. It will pull in all the most
useful signals and create a custom dashboard in a couple of minutes.
And you can ask the assistant to iterate on it, maybe focus on a particular service or
add a different visualization or add more details. Even internally at Grafana, we have moved away from
building dashboards manually
because it is a massive time saver for us to just describe what
we would like to see and then iterate on it with the assistant. And that gives us more time to actually
think about what the dashboard tells us rather than writing queries
and configuring panels. Now you can also ask, analyze my alerts
over the past 30 days and optimize them. What a system will do is look at your
alert history and identify sources of noise. So maybe alerts that constantly fire
and resolve or duplicate alerts for the same underlying service or alerts
that fire so frequently that they stop being actionable. Now from then on, it will come up with an improvement plan.
And that's not a plan that is cast in stone, but one that you can
iterate and improve together. So it essentially becomes a guided
process for improving your alerting setup. You can also ask, analyze incidents over the past two
weeks and tell me what patterns you see. As many engineering teams know,
similar problems keep coming back. So here assistant will
use assistant search, which is our semantic search layer to
find the relevant incidents and look for recurring patterns. So this is a super low effort way of
understanding what keeps coming back for your team and where maybe engineering
investment or a deeper investigation can help prevent the next recurrence. So you can ask many different questions
and get practical help that is grounded in your system and data. But all these examples that I've
shown the start the same way. Someone opens the assistant and asks, "But what if you didn't
have to ask?" Well, that is the next iteration that we would
like to share with you where Grafana Assistant works as a twenty
four seven agent. So rather than asking assistant for help, a vision has evolved to it becoming
an always on agent that constantly watches the state of your system, proactively bringing to your attention
any issues or proposed solutions. So for this to be possible, we've given assistant four ways
to take on work autonomously. So the first one is the eye of Soron,
or perhaps a little bit less dramatic, what we call watchers
for always on detection. Then we have automations
for scheduled work. We have investigations
for event triggered work, and finally manage sandboxes for
coding tasks that you can delegate to agents. So let's start
with assistant watchers. Watchers compliment your existing
alerts by allowing you to describe what matters in plain
natural language and then having the assistant turn that intent into
ongoing checks against your telemetry. So they watch for any concerning changes, surface insights with supporting evidence, and then they can also trigger a deeper
investigation if there's something critical that needs attention.
So this is ongoing checks, but some work needs to run on a schedule, so maybe daily health summaries or
weekly error reviews. And for this, we have assistant automations. So automations take a recurring
task and give it to the assistant to run on a given schedule. Now, the results arrive either in Grafana
or directly in Slack or in your email, and every run has its own assistant
conversation so that you can dig into the findings and ask any follow up questions. Now, when something does go wrong, assistant investigations can
start looking at it right away. So when an alert fired or
an incident is declared, an investigation can be automatically
triggered where it starts testing competing hypotheses against
evidence from across your system. Now tomorrow during the IRM talk, you will hear about operational
context and how findings from an investigation can be fed into
the context of an ongoing incident alongside input from other
agents. So that is something that allows you to build a shared understanding
of what's happening so that both humans and agents can build on top
of each other's findings and resolve incidents faster. Now to make
investigations practical at scale, we spent the past year
continuously optimizing and evaluating our agent harness. So
thanks to that optimization loop, we were able to build a highly
optimized system that balances quality, speed and cost with the token
savings passed on to you. Now, once a problem is understood, the
next step is working towards a solution. So you can hand over a
task to a coding agent, which runs in its own managed
secure sandbox in Grafana Cloud. Now the results come back
to you as a draft PR, ready for your team to review
and decide what ships. All right, so let's bring all of
this to life with a demo. We will not have time to go through all
of it. So after this talk and tomorrow, we would love to see you drop by one
of our booths to see these capabilities from up close and try them out yourself. Thank you, Ksenia. Let's now get
into the weeds of how it all works. I will show you some easy workflows in
the beginning and then we will pull it back together into some more advanced
workflows as we go through all the features we just mentioned. As Ksenia
said, it's a little bit hard to get all of it in this talk. So please visit
us at the booths, ask us questions, and you can also try out everything
we show you today at the booths. So let's start very simple. I have
open Grafana Assistant to the side. Let's say I'm very new to the stack
and I have never been to the stack, I just onboarded on a team. So I ask what's being
monitored in the stack? Can you draw me a diagram? And Grafana Assistant is now
using what you just heard earlier, system search to go
through your whole stack, finding all your labels that
you have, the alert rules, the incident that might
be your infrastructure, everything you have been instrumented
over the time as you onboard it into Grafana. You can see that here and you
can always see how Grafana Assistant is working for you. And there
we go. Just like that, we have a pretty quick
diagram of what's going on. So if it has been the first
time for me to be in the stack, now I already know
something very high level. This is something that can take onboarding
new people in your team onto your stack from days down to hours so that
they can get proactive more quickly. We also had a telecom talk where someone
else who has actually never touched their stuff beforehand used the system
to find something they never heard about to help them with that. So I
really love that. I'm a PM, so I'm no engineer and I even can ask
Assistant what's going on with our telemetry data. It's pretty cool. Okay, let's maybe dive a little bit deeper.
Analyze my alerts of the last 30 days. Let's say 14 as it will take very long
for us to go through that, 40 days. Which ones are good to keep? Which ones should we retire? Find patterns that help
me improve my alerts. Grafana Assistant is a highly parallel
agent. So while this is running, we'll actually go in another tab and do
another task at the same time because this will be running for a minute or two
now as it goes through all the alerts that we have in the
stack. So on another tab, you can just keep working on Grafana
Assistant and now I will ask, are there any active
incidents in this stack? And this is really to show you everything
that is in your Grafana cloud stack, be it like your metrics logs,
traces, your alerts, your incidents, maybe even your scale databases
for your business data. Grafana Assistant can help you access
that, correlate all of that in one go, help you find the information you need.
Okay, so we actually have some
incidents ongoing here. So let me just copy that and just
imagine, as I said, I'm new to the stack. I don't even know how all of this
works. So I will just tell Assistant, take me to the name incident and
now Grafana Assistant will also actually navigate me to the UI element
that we need. So if you're unsure like, "Oh, I want to instrument my things and I
don't know where I should go," just ask Assistant. We'll take
you to the right page, just get started on instrumentation,
get you to the right page, get started on alerting,
wherever you really want to go. So now we are on our IRM product. You will see more of that
tomorrow in the IRM talk. And in the IRM suite, we can now see this incident that has
been ongoing for quite a while. That's when you can see when I started
my demo stacks 70 days ago, so I practice a lot to
deliver this demo to you guys. And we have also another
feature down here, which is our assistant investigation
that we just mentioned. Assistant investigation is our way in
the background to asynchronously analyze what incidents are about. Let's say
an alert is firing and it's critical. Let's say you decline incidents critical. We can run investigations
automatically with you. So the moment someone is paged
and they're coming back to the PC, they already have something
that they can go off on. So let's just open that really quick. This is an investigation
that has already run. An investigation can run anywhere
between a minute to 10 minutes, depending how complex your stack is, how
many data sources have you connected, how complex is the root cause, but it will keep going.
This is like its pole job. I like to call it our keep going agent, which is literally built to
just keep going, going, going, going until we find something
it thinks is the right thing. So on our investigations, we can now see there's a small summary
of what's going on. We can see some data. We can even see a timeline,
so what has happened when, and we can see what was checked. We
also have a feature for hypothesis, so you can see what has the
assistant tried to think about. So in this case it though, the incident was declared by automation
before the banking process existed, as you can see the demo environment. And
then you can see the evidence for that, you can see the timeline for that.
And we can even say, this is it, or we can say, oh, this is actually not it and steer the
investigation. So you can run your investigations either
completely autonomously or
you can run them human in the loop where you help and steer provide
more information as it becomes available and you can do both however you
choose to do it. And then lastly, we have all the sources so you know
that the agent didn't just fabricate new locks that don't actually
exist in your system. So you can always review all of that. But let's imagine I also want
to know what was actually the problem with that?
Where's the code for that? We can just follow up on
this investigation, ask
for that. We can ask it, find me the code for this problem. Why did we have this problem? So it's
very unspecific. I didn't say which repo. I didn't say, oh, it's
this service. I didn't say, because I might not actually
know. Sometimes you get alerted, it just says like error rate
is high and you're like, okay, what should I do now? And with
Grafana Assistant bringing in, you can search code, you can look at how your coding
agents is working and there we go. It has spawned a sub-agent for us.
Oh, they see failed for some reason. Oh no, that happens
when you do a live demo, but we can see how the assistant is
recovering to try to get going again. In ideal case, it would have
just spawned a subagent for us, which going through our repo and would
tell us what's actually going on. So let's maybe come back to that in a
second and instead go back to our learning analysis.
Who of you has alert noise? Okay. Who thinks alert noise is, well,
noisy and annoying? No, just kidding. Of course it's annoying.
So with Grafana Assistant, when we analyze all our alerts, if
you remember at the start of the demo, I asked for that, then... Oh,
let me actually zoom out. Sorry. We asked for that. Then you can see
what has happened here and now we can... Sorry. And you can see what
are the main patterns. So we have a broken notification sync
that is sending all time notifications. We have machine traffic, we have
routes that fire with no panic, we have flapping warnings, we have
correlated signals and so on and so on. So we have lots of alerts noise
in this stack specifically. So the assistant even asks
us what should we do next? So we can change the things, you
can tell, maybe let's just say, maybe let's do this. And now the assistant
will get to work for us and will work on this specific task and
help us fix these alerts, fix the alert rules so
that they come better. Fixing alert noise is a
job that's continuously, it's like ongoing and it's always
happening. You always have more alerts, you have to retire new alerts,
more applications are onboarding, other applications are offboarding
again. And with assistant, you can really always
do a snapshot of that. If you would normally look at all
of these alerts, it would take days, maybe even weeks depending on the
size of your stack to find all the notification rules that are firing that
might not be efficient and so on and so on. So there we go. It even gives us
recommendations what we should do. So these are the basics
of Grafana Assistant. So let's now go to the more advanced
stuff that you can build now. As you know, in the keynote, we announced Grafana pages are a new way
to build any kind of view that you want to build. So I was thinking I want to have a view
and let me share that view with you. I wanted to have just a very simple
view for myself that I built in five minutes. So everything you see
here is built in five minutes, where I want to see just the essentials
for me when I get started for my job. And I was thinking maybe I should also
have a little button that says brief me where I'm seeing what's happening and
then we can see the platform as two major incidents with delayed
transfers and so on and so on. And I wanted to have my incidents up here. I wanted to have all the things that
made me need me up here. And I wanted to also have something about CI/CD. I wanted to see which of our
GitHub actions are working,
which are burning out, which are very slow or stalling.
I wanted to see that too. So I asked just to find assistant,
I connected to GitHub, to the API, build it in a page, and now I also have
this overview pretty quickly. As I said, this was built in five minutes with
assistant pages. Oh, thank you. And then I also want to see all the pull
requests that we have open because you always want to know there are
new mergers getting merged in, new changes are being deployed,
something might change. And I wanted to bring in
all the things that we have. So I implemented tiny little buttons
for me so where I can just click ask and now I already have a prompt prefermed in
here where we can now ask about all of these things. And another thing that I
wanted to do is sometimes you have PRs that are very big. They change lots of things that
might change lots of infrastructure. They change your backend
or front end significantly. I wanted to have a way to
watch these things after merge. So I will just put this prompt in here. Let me zoom in that for
you guys real quick. And there I am creating a temporary
throwaway watcher that will only watch this PR until it's getting
merged and then kills itself essentially. So watches are also alerts that you
can set a deadline on. So you say, I just want to watch this PR and if
it's working out and if not, just stop. If it's working out, all
good. Well, that's it. And I will just start that. We won't go through this now because the
watcher will actually now look at all our telemetry.
It will look like all the baselines. We'll establish what does the
telemetry and the baseline look like. So this will take like two to five minutes
depending on how big your stack is. So instead I'm just going to show you
real quick what a watcher will look like when it's done. And a watcher is our new form to help
you correlate across different things, for example, for release readiness or if you want to
correlate telemetry data and business data and one goes, for example, you
want to check on your checkout service, but you also want to see how much money
are you transferring through that. Are orders going up, going down,
so you can all have it in one view. So I have set up a watcher previously, which is my banking payment
pipeline health one. So if anyone works here on a bank, I think top of mind is
probably transactions going
through so people get their money on time.
If not, that's kind of bad. And there I defined like a very small
mission, what's supposed to watch. So you can see here, like watch the banking payment pipeline
and name space banking prod and so on and so on and watch for these things. And you can see it has been running
for quite a while and it has created like all of these little blips
for me that are all looking fine. So this watch is not alerting anything. We can click on that and we can
see what's actually happening. So you can correlate
across different signals. So this watch is watching metrics,
logs, traces, all in one go, and you can have all of that
in one watcher. All right. So that's it for the demo. If
you want to see more, as I said, it's very hard to condense all of this
in just like 10 minutes for you guys. So please come to the demo booths. We
have engineers here, Senior is here, I'm here. You can ask us any
questions. You can try out all of this. We are not shy for that. So yeah, let's bring this home
and take it to the end. All right. Thanks, Maurice. So you've seen a few ways
to put Assistant to work, but there is so much more that you
can build on top of that foundation. So think about your team. What problems keep coming back or what
would you love to keep a closer eye on if you had more time? So you've seen in a demo how you
can connect an alert or a watcher to investigation and then task a coding
agent to come up with a proposed solution. Well, you can build on top of that by combining
the various building blocks in the way that works for your team. So you can connect together alerting
and watchers in IRM to decide when work should begin. You can use an investigation to understand
what's happening and the managed sandboxes to come up with a proposed
solution that you get to review and decide whether it chips. So all of these are
powerful building blocks that allow you to create a tailored workflow for your team. You can also learn from your users
and customers faster than ever, and then take what you learn and use it
to guide and to prioritize what to build next. Most teams have a lot of customer
context that already exist, but it's spread across various tools. So you might have account
information in Salesforce, you might have calls in a
warehouse like BigQuery or Snowflake, or you might have support
tickets in Jira, for example. A system does not need a separate
integration for each of these. If your data sits in a Grafana data
source or behind an MCP server, a system can bring that into the
same conversation as your telemetry. And then it can maybe create an
issue in Jira or Linear in GitHub, and then your team gets to
decide what to do with that next. Now you can also describe an experience
that you'd like to build and then work with Grafana Assistant to bring
it to life as a Grafana page. You've already seen some
examples during the keynote. We've also seen teams
create very interactive, very powerful pages for
things that matter to them, deployment trackers or how the
systems evolve over time or custom visualizations for
the product adoption. So you can iterate on these pages. You
can share them with your teammates. You can remix somebody else's creation. It opens up a lot of room
to be creative and create an exact experience that you think
will work best for your team. Now, you might have guessed it already,
this presentation is all Grafana pages, so you can let your
imagination go wild. Now, the opportunity across all of these
examples is to spend less time on the things that slow you down and
more time on the work that you actually would like to move forward, but you
don't have to take our word for it. This is how our customers describe the
difference it's making for their own teams. So this is Eric from CellPoint Digital
that says that his role is becoming much more architectural. So you can focus on translating ideas
into technical requirements while Grafana assistant takes care
of most of the tedious work. And here's another quote
from Alessio from Qubit. His team sees that with these tools, they see fewer incidents
and when they do happen, they resolve faster so they can stay
focused on deploying new features. So we started with questions you can ask
the assistant and then we've shown you what's possible when you
don't have to ask every time. Now think about your own team. What would you like handled for you and
what would that free you up to focus on instead? Choose one recurring task, give a system the context it needs, see
what you can take off your team's plate, and then build from there.

