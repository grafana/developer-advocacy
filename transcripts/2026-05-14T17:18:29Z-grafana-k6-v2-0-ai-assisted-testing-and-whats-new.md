# Grafana k6 v2.0: AI-Assisted Testing and What&#39;s New

Published on 2026-05-14T17:18:29Z

## Description

k6 v2.0 launched — with AI-assisted test authoring built in from the ground up. This GrafanaCON talk is the official announcement, ...

URL: https://www.youtube.com/watch?v=rbWZekxFlPM

## Summary

The show is titled "Grafana k6 v2.0: AI-Assisted Testing and What's New," published on May 14, 2026. The speakers are Andrey and Théo from the k6 team at Grafana Labs. They announced the launch of k6 v2.0, which includes AI-assisted test authoring, a new assertions API, an overhauled extension catalog, subcommand extensions, and machine-readable outputs. Key takeaways include the importance of integrating testing into workflows, leveraging AI to enhance testing efficiency, and the introduction of tools that allow users to create customized testing strategies. The speakers emphasized that testing is now a critical safety net in the fast-paced development environment.

Topics: k6 v2.0, AI-assisted testing, assertions API, extension catalog, subcommand extensions, machine-readable outputs.

## Chapters

00:00:00 AI-assisted testing in k6 v2.0
00:06:59 Introduction to k6 v2.0 and AI-assisted testing
00:13:15 Introduction of new k6 extensions and features
00:19:32 Overview of k6 v2.0 AI-assisted testing features

Hello everyone, and welcome. My name is Andrey, and I work on the k6 team at Grafana Labs.

And I'm Théo, I'm an engineer and a maintainer of the k6 project. We have a lot to cover in the next almost 30 minutes. We are going to announce something big that Matt already spoiled. We are going to address the elephant, rather, the robot in the room. We will also have a live demo, so buckle up, and let's get straight into it.

Almost a year ago at GrafanaCON in Seattle, we announced k6 v1.0. It took us nine years, countless iterations, and we finally shipped the first major stable version. Today, we're doing it again. K6 version two comes out on May 11th, 2026. Before you panic, a lot of what you know and love about k6 is not going anywhere. If you built your pipelines, wrote your scripts, or extensions with k6 version one, a lot will look and feel familiar, and we were very intentional about that. 

K6 version two is packed with a whole new set of tools that are built for the world we currently live in, a world that looks radically different from the one when we started planning it. Throughout this talk, I'll walk you through some highlights of the new version. We're going to talk about the new assertions API, the overhauled extension catalog with official and community tiers, subcommand extensions, the k6 Operator release, and machine-readable outputs. But first, let me hand it over to Théo because there is a bigger conversation we need to have.

Thanks, Andrey. So, like Andrey said, let's just address the robot in the room. A quick show of hands: who of you uses AI in any form on a daily basis? There you go. I use AI, he uses AI, you all use AI. We had made an initial plan for k6 v2.0, but roughly six months ago, everything went through the window, and we needed to adapt it to this new world. 

We're vibe coding, and now you know that probably most of you are. The first studies are hinting at the fact that at least 80% of engineers are already using AI in their daily workflows, and 60% of them are using it for testing. We software engineers are slowly turning into product engineers. We ship more, there's more output volume, and the speed goes faster and faster when it comes to delivery, but so does the count of bugs, vulnerabilities, and outages. The news is full of it. 

Fresh studies conducted on this very specific topic hint at a 1000% increase in terms of vulnerabilities. You've heard that right—that's 10 times more. So, we might be coding faster than ever, but we believe that speed shouldn't come at the cost of confidence. AI generates code, and nowadays, less and less of us actually fully grasp what's running in production. I certainly don't, and I love my job and engineering things. But that also means we have many more blind spots, and the blast radius of those blind spots is even bigger. When things go wrong, they go wrong in a much more dramatic way. 

Now that we're all 10x engineers, we also have 10 times more opportunities to break things. Hoping AI got it right is probably not the right strategy—it's certainly not ours. Testing, we're pretty much convinced of this, is just not a nice-to-have anymore; it's your safety net. For it to be functional in this new era, it needs to be exactly where the code is generated, directly in your workflows. 

With that in mind, k6 v2.0 treats AI as a first-class feature. To do that, Andrey will tell you a bit more about this feature later, but we leverage a new feature of k6 v2.0, which are subcommand extensions. All you need to know now is that you, as a user, can add custom commands to the tool to make it fit your own workflow. We did that for ourselves, and we are shipping three subcommand extensions specifically targeted at AI and agentic workflows.

The first one of those is the agent command. This is really hard to name such a feature, but essentially what it does is run it inside of your project, and it's going to configure your agentic workflow of choice—Claude Code, Codex, Cursor, OpenCode, you name it. It's going to bring the configuration, the skills, the references, and specific bits of configuration such as the MCP server I'm about to tell you in a second, so that your AI agent of preference knows how to create a testing strategy and execute on it.

I just spoke about it, but the second command is the MCP. K6 has an MCP server since a couple of months, and this MCP server can be directly run from the command line. What it means is that you don't need to install anything outside of k6. If you have k6, you have the MCP, and your agents are able to validate, run, and verify scripts on the go.

Finally, the docs command is there to help your AI reduce the cost of figuring out how to write a script. K6's center is very much centered around JavaScript. AI is already really good at this, but we have a ton of APIs that are a bit arcane. This subcommand is specifically designed to make it cheap to figure out how it works.

But those are just words. How about we actually show you? What's the best way to prove that this works than to do it on the Grafana website itself? Let's pray for the AI non-deterministic demo gods because you know how it goes. (laughs) It should work in theory.

So, there you go. This is an almost empty folder, and I'm going to run the agent command. You see my terminal is already a little bit clever, and it knows that I prefer Claude Code personally. No judgment—this is my tool of choice. When I run it, what it actually does is initialize this specific project to bring all the tooling and the configuration for you to be able to write tests. 

If you assume that this folder already has some code—right now there isn't, because we're going to do something else very specific—it’s going to bring the settings, which at the moment basically tells your agent where the MCP is. More importantly, it's actually bringing a lot of skills. Among those skills, which for other agents such as VS Code actually are agents, a lot of those are specifically designed to go from requirements to an actual test suite.

So, I mentioned we would dogfood. What are we dogfooding? Let's assume I know nothing about testing, and I have a pretty cool product, if you ask me—Grafana. This is the live website; I'm not pretending—this is play.grafana.org. Let's say we have this dashboard that I really like, which is the SQL Expressions Showcase. As a user, let's say I'm a developer, I'm new on the team, and I'm advising the testing strategy. I want to make sure it works. 

How do I do that? Let's start with things that we all do on a daily basis when we use Grafana. The first thing I do all the time is change the timeframe. One thing I would like to test is switching between 6 and 12 hours, and I want those graphs to essentially update with the new data. Another thing I do all the time, because I never remember the PromQL query format, is go into the panel, edit it, and play around. So how about we also test this? 

Finally, I'm a k6 maintainer, not a Grafana maintainer. I have zero clue how Grafana works, but maybe an agent can figure this out for me and actually write a test that's going to verify that whatever loads those panels with data is actually functional and supports a certain amount of load. To do that, we can go back to Claude, kick it off, and you'll see that now, because we started clean—there was nothing—but the agent command actually brought in this case skills: the load-test skill, the smoke-test skill, the test-planner, browser-test, and also playwright-converter. If you have a Playwright script, it will be converted automatically. The one we're really interested in today is the test-planner.

And so what we're gonna do, if my demo is properly set up—oh, it isn't! (laugh) Give me a second. We're gonna take a prompt that I've already written, and we're just gonna paste it there and kick it off. 

What this prompt is doing is essentially describing the workflow I walked you through. So go on play.grafana.org, and I would like you to ensure that I can change the time range, the data updates, I can go in a panel, edit it, and it updates. Sorry, this is the Chrome MCP, and I tell you to use the Chrome MCP to do that. Also, figure out with the Chrome MCP, look at the traffic, and identify some relevant requests that fill the panels with data. 

Now I ask that, okay, I want to test with, I want to make sure that those things keep working—just do it. But how about you tell us more about k6 v2.0 while this works in the background?

Right. So, can we have the slides back? While our agents are working, let me show you a few highlights of the upcoming v2.0. I have five of them, and I suggest that we start from the top. 

As you might be familiar, k6 v1.0 always had a checks API, and checks are great for load testing cases. We designed them specifically with this in mind. They don't halt execution; they emit metrics and provide failed past percentages. However, for functional testing or for browser testing, or for this kind of validation—does this actually do what I expected?—they always felt like a workaround. 

In v2.0, we deliver the new assertions API. This API, as you might have noticed, is inspired by Playwright syntax. So if you've used Playwright before, you'll see many familiar concepts, like hard and soft assertions, or async ones for browser testing that do these very convenient auto retries. This API moves k6 from "did it crash" to "did it do exactly what I expected?" This is what you need when there is an AI agent that writes the code, and your users depend on this.

Now let's talk about extensions. In v1.0, we introduced native extension support, which massively reduced the number of times you need a custom build. However, the discovery and trust story was still pretty rough. You had to know what was out there, and you had to trust that it works. 

In v2.0, we introduced an extension catalog with two tiers. The extension catalog uses automatic dependency resolution. In short terms, how it works is you reference a model in your script, you run it, and it just works. Everything is handled in the background. With this, k6 is not just a testing tool anymore; it's a testing platform with a real ecosystem. 

The extension catalog comes in two tiers. The first one is official. These are extensions that are built and maintained by Grafana Labs, and we guarantee stability and security. Examples include xk6-faker for test data generation, MQTT for IoT protocol testing, or SQL for database validation. 

The second tier is community extensions. These are maintained by external developers, like Pierrick Hymbert with xk6-sse, or Mostafa Moradian with xk6-kafka. Grafana Labs provides guidelines and tooling to help maintainers keep their extensions stable and secure. But the innovation comes from the community. The extension catalog is already available today. There is a link in there; go explore and see what fits your workflow already.

What I was talking about right now are JavaScript extensions. They provide modules that you can import into your script, and nothing has changed in this regard. However, in v2.0, we introduced a completely new type of extensions: the subcommands. They don't add an import module; they add a whole new command to the k6 CLI itself. 

To create such an extension yourself, the process is very standard. You create a Go module, and k6 picks it up. If this extension is already listed in the catalog, we automatically provision this. So k6 will identify that the command extension is missing, provision the right binary on demand, and run this command. There's no manual step in between. 

If you are building something custom that fits your specific workflow, or maybe something new that is not in the catalog yet, it will just go the same familiar pathways: xk6 and custom builds. Theo already mentioned three of these extensions that are available: the agent, MCP, and the docs. There's also Explore, which helps you or your AI agent navigate the extension catalog and see what's there, maybe find something that fits the job. And anyone can build their own.

With these extensions, k6 is not just a platform; it's a platform for testing. It allows you to define the workflow that your team needs. 

Now let's talk about what's happening beyond the test. Because the test that runs on your laptop is useful; it runs and prints results to the standard output. But it's not enough. Tests need to grow with you, from the first run to production infrastructure. k6 v2.0 is designed to scale alongside your stack. 

We introduced three layers. First, you observe. We ship first-class machine-readable outputs with v2.0. The OpenTelemetry output allows you to stream into your existing observability stack. If you're already using Grafana, Grafana Cloud, Tempo, or Mimir, results will show up right alongside your application telemetry. It's a single pane of glass. 

Then your structured JSON output allows you to integrate k6 into your custom pipelines, dashboards, or maybe give this output to the AI agent to analyze and reason about. 

Next, you automate. We introduced a new GitHub action, run-k6-action, that makes it simple to run k6 on GitHub. Every commit, every merge, every PR, every deployment—all tested automatically. With the new machine-readable outputs, it closes the loop. It gives you this fully automated circle. When the code is written, whether by a human or AI, tests are running, the results go back into the pipeline, and nothing is shipped without proof that it works. 

The third layer is scale. The k6 operator hit v1.0. For those of you who are not familiar with what the operator is, it allows you to run distributed k6 tests on Kubernetes. This is where your app lives. v1.0 is a commitment. It means semantic versioning, stable CRDs, predictable release schedule, and a clear upgrade path. So if you've been holding off using the operator in your production, this is a signal that it's ready. 

This is how you go from "I run a test" to "testing is a part of my infrastructure." You observe, you automate, and you scale. 

Theo, how are our agents doing now? Let's check it out. 

It's doing surprisingly well, but I'm still gonna tell you how it's going, just in case it takes much longer than we felt. Because, yeah, AI is fast, but generally not that fast. Except today, it was supposed to not be done, but it's done. 

Anyway, a terminal output is quite hard to read, right? It's quite hard to parse, especially on a big screen. So I'm spoiling the results a little bit. Claude and k6 v2.0, as part of the demo, did essentially four things. 

As we've seen it do at the very beginning when I launched the skill, it explored play.grafana.org, popping this hideous Chrome for your poor eyes. I'm sorry about that. It started clicking around, taking screenshots, and essentially trying to build a mental model of the app. 

Once it had done that, it switched to the new tools that k6 v2.0 provides. The first of which is the documentation. With us instructing it to use k6 as part of the prompt, it essentially started by reading the documentation. "I have opened this website, I need to test it, what should I do next?" 

The nice thing about it is that it reads progressively and only what it needs to read. It figured out about the APIs that it should use, best practices, and picked up specific patterns for the kind of testing it wants to do. Once it had done that, it started leveraging the MCP. The MCP essentially allows it to do two...

Things are changing. It writes a script and can call the MCP to validate it quickly and in a token-efficient manner. Then, it runs it against production with very little configuration. We also protect those to ensure that what it actually wrote works in the real world. It keeps iterating until it passes. 

The slides are a bit dated because it used to generate three tests, but in my test this morning, it generated more like six or seven tests, even for things you don't ask about. But that's a good thing. It generates a full test suite that matches the requirements we are looking to achieve.

If we switch back to the demo and to the terminal... Sorry, go for it. Up. Looking at the results, it went really quickly. Based on the requirements we asked for—open play.grafana.org, change the time range, ensure the data is updated, go into a panel, edit it, change the query, and make sure it keeps working—it figured out what requests fill a Grafana dashboard and wrote at least a load test for that. 

What it did was spawn a couple of subagents and used various tools to accomplish this. It ended up generating five tests. Five is bigger than three, so it's probably better. We have a browser dashboard test that's a load test specifically called "load," but it's actually a smoke test. We also have a browser test that verifies the time range change feature, and another one for the panel edit. It performed both a smoke and load test for the API data. 

It tells us what it covers, but more importantly, the skill ensures that it tells you exactly how to run this test suite and even offers to run it for you. We're not going to run it on stage because it will take quite a bit of time. But let's look at what it generated for us. 

We can see that it recorded the captured requests if we want to introspect that. It also generated those tests. If we go into tests, we can see that the file it mentioned actually exists. It did not hallucinate. 

As a user, the first thing I would be interested in is seeing what the script for the time range change looks like. I'm a very skeptical person; I wouldn't trust an AI to do a good job, although most of the time it does. So if we look at the script, it's actually a pretty canonical script, and I'm always amazed to see that. It picked up on the dashboard URL, created a browser scenario, and knows through the documentation exactly how to test through a browser directly in k6. 

It wrote this test, which is nicely annotated and does exactly what we asked for: navigate to the dashboard, wait for the panels to render, assert the panel heading is visible, click the time range picker, select "last one hour" from the dropdown, wait for it to be updated, and finally verify that the URL changed and that the data is updated. This is a resounding success. Honestly, from here, I think it would have taken me probably three or four hours to write something that good.

Now, how about the browser panel? If we quickly take a look, I don't expect anything crazy, but it detected the right URL and noted the expected query. It opens Chrome, navigates to a panel, verifies the query editor row is visible, starts clicking around, verifies that the Prometheus request is correct, modifies it, and so on. This all follows the best practices of k6.

Finally, probably the most interesting part for me as an old backend engineer is the API load test. I want to ensure that when we have, how many, 35 million users at this point? I don't remember. Imagine all those people connecting. How can we make sure that it works? 

Here, it created a load test scenario. It defined some thresholds, automatically deciding that 95% of the requests should take less than one second, and 99% of them less than two seconds. It also ensures that there are no errors, with the rate of failed requests below 1%. Then, it proceeds with writing an actual load test, which is nicely grouped and has those checks, which could also be assertions in smoke tests. It probably is. 

These verify that when we send a given request, we receive responses that look and behave correctly, and we start hitting the server with 20 requests per second. 

If we go back to the slides now, what used to take days—let's say at the very least, a couple of dedicated engineers, testing engineers, or SREs, a lot of time, and a lot of expertise—we just did on stage in five minutes. What would have taken probably four or five days before now takes five minutes. It took requirements, transformed them into a strategy, and delivered a test suite that's ready to go in CI, ready to deploy, and ready to scale with Kubernetes and the operator at the scale of your workloads. 

That's exactly what k6 v2.0 makes possible. You don't have to guess anymore. You can let the AI help you prove that things work the way you say they work.

Let me put it all together. k6 v2.0 drops on May 11th. It will look and feel familiar, but it's also designed for the world we currently live in, where the agents write code, and testing is basically their safety net. 

Here's what we want you to do once the new version drops:

- Please use the agent command to initialize your workflows in whatever projects you have. It could be a pet project or a big production project. Try it out. I was convinced and started skeptical, and now I use this all the time.
- Go explore, browse the extension catalog, and find an extension that fits your stack, or even better, contribute one yourself. Integrate, run k6 action in CI, and make testing non-negotiable. Nothing should be shipped without proof.
- Finally, scale—deploy k6 with the k6-operator where it matters most, in production.

May 11th. Stop guessing, start proving. Mark your calendars. Thank you. 

Thank you. (audience applauding)

## Raw YouTube Transcript

- Hello everyone, and welcome. My name is Andrey, and I work on the k6 team at Grafana Labs. - And I'm Théo, I'm an engineer and a maintainer of the k6 project. And we have a lot to cover in
the next almost 30 minutes. We are going to announce something big that Matt already spoiled. We are going to address the elephant, rather, the robot in the room. And we are going to have a live demo. So buckle up, and let's
get straight into it. Almost a year ago at
GrafanaCON in Seattle, we announced k6 v1.0. It took us nine years,
countless iterations, and we finally shipped the
first major stable version. And today we're doing it again. K6 version two comes
out on May 11th, 2026. And before you panic, a lot of what you know and love about k6, it's not going anywhere. If you build your pipelines,
you wrote your scripts or extensions with k6 version one, a lot will look and feel familiar, and we were very intentional about that. But k6 version two is packed
with a new whole set of tools that is built for the
world we currently live in, a world that looks radically different from the one when we started planning it. And throughout this talk
I'll walk you through some highlights of the new version. We're gonna talk about new assertions API. We're gonna talk about the
overhauled extension catalog with official and community tiers. We're gonna talk about
subcommand extensions, the k6 Operator release, and
machine-readable outputs. But first let me hand it over to Theo because there is a bigger
conversation we need to have. - Thanks, Andrey. So, like Andrey said, let's just address the robot in the room. A quick show of hand. Who of you uses AI in any
form on a daily basis? There you go. I use AI, he uses AI, you all use AI. And so we had made an
initial plan for k6 v2.0, but I would say roughly six months ago everything went through the window and we needed to adapt
it to this new world. We're vibe coding, now you know that
probably most of you are, and actually the first studies
are hinting at the fact that at least 80% of engineers are already using AI in
their daily workflows. 60% of them are using it for testing. Us software engineers are slowly turning into product engineers. And we ship more, there's
more output volume. The speed goes faster and faster
when it comes to delivery, but so does the count of bugs,
vulnerabilities, outages. The news are full of it. There are fresh studies that are conducted on this very specific topic, and they're hinting at a 1000% increase in terms of vulnerabilities. You've heard that right.
That's 10 times more. So we might be coding faster than ever, but we believe that speed shouldn't come at the cost of confidence. AI generates code, and
nowadays less and less of us actually fully grasp what's
running in production. I certainly don't, and I love my job, and I love engineering things. But that also means that we
have much more blind spots. And the blast radius of those
blind spots is even bigger. When things go wrong, they go wrong in a much more dramatic way. So now that we're all 10x engineers, we also have 10 times more
opportunities to break things. And hoping AI got it right is probably not the right strategy. It's certainly not ours. So testing, we're pretty
much convinced of this, is just not a nice to have
anymore, it's your safety net. And for it to be
functional in this new era, it needs to be exactly
where the code is generated directly in your workflows. So with that in mind, k6 v2.0 treats AI as a first class-feature, and to do that, Andrey
will tell you a bit more about this feature later, but we leverage a new feature of k6 v2.0, which are subcommand extensions. All you need to know now
is that you as a user can add custom commands to the tool to make it fit your own workflow. And we did that for ourselves. And we are shipping three subcommands, subcommand extensions, which are specifically targeted
at AI and agentic workflows. The first one of those
is the agent command. This is really hard to
name such a feature, but essentially what it does is you run it inside of your project, and it's gonna configure your
agentic workflow of choice, Claude Code, Codex, Cursor,
OpenCode, you name it. It's gonna bring the
configuration, the skills, the references, and specific
bits of configuration such as the MCP server I'm
about to tell you in a second, so that your AI agent of preference knows how to create a testing
strategy and execute on it. I just spoke about it, but
the second command is the mcp. So k6 has an MCP server
since a couple of months, and this MCP server can be directly run from the command line. And what it means is that you don't need to install anything outside of k6. If you have k6, you have the MCP, and your agents are able to validate, run, and verify scripts on the go. And finally the docs command
is there to help your AI to help reduce the cost of your AI figuring out how to write a script. K6's centre is very, very much
centered around JavaScript. AI is already really good at this, but we have a ton of APIs
that are a bit like arcane. And so this subcommand
is specifically designed to make it cheap to
figure out how it works. But those are just words. How about we actually show you, and what's the best way to actually prove you that this works than do it on the Grafana website itself? Let's pray for the AI
non-deterministic demo gods, because you know how it goes. (laughs) It should work in theory. So yeah. There you go. So this is an almost empty folder, and I'm gonna run the agent command. And you see my terminal is
already a little bit clever, and it knows that I prefer
Claude Code personally. No judgment. This is my tool of choice. And so when I run it,
what it actually does is it initialized this specific project to bring all the tooling
and the configuration for you to be able to write tests. So if you assume that this
folder already has some code, right now there isn't, because we're gonna do
something else very specific, it's gonna bring the settings, which at the moment
basically tells your agent where the MCP is. But more importantly, it's actually bringing a lot of skills. And among those skills, which for other agents such as
VS Code actually are agents, a lot of those are specifically designed to go from requirements
to an actual test suite. So I mentioned we would dogfood. So what are we dogfooding? Let's assume I know nothing about testing, and I have a a product, a pretty cool product
if you ask me, Grafana. This is the live website, I'm not pretending, this
is play.grafana.org. And let's say we have this
dashboard that I really like, which is the SQL Expressions Showcase. And as a user, let's say I'm a developer, I'm new on the team, and I'm
advising the testing strategy. I want to make sure it
works. How do I do that? Let's start with things that
we all do on a daily basis when we use Grafana. The first thing I do all the
time is change the timeframe. So one thing I would like to test is I switch between 6 and 12 hours, and I want those graphs
to essentially update with the new data. Another thing I do all the time because I never remember
the PromQL query format, is go in the panel, edit
it, and play around. So how about we also test this? And finally, I'm a k6 maintainer,
not a Grafana maintainer. I have zero clue how Grafana works, but maybe an agent can
figure this out for me and actually write a
test that's gonna verify that whatever loads those panels with data is actually functional and supports a certain amount of load. So to do that, we can go
back to Claude, kick it off, and you'll see that now because, so we started clean, there was nothing, but the agent command actually
brought in this case skills. So the load-test skill,
the smoke-test skill, test-planner, browser-test,
and also playwright-converter. If you have a Playwright script, it will be converted automatically. And a couple of MCP resources. But the one we're really
interested in today is the test-planner. And so what we're gonna do if
my demo is properly set up. It isn't, (laugh) give me a second. We're gonna take a prompt
that I've already written, and we're just gonna paste
it there and kick it off. What this prompt is doing, it's essentially describing the workflow I walked you through. So go on play.grafana.org, and I would like you to ensure that, I can change the time
range, the data updates, I can go in a panel,
edit it, and it updates. Sorry, this is the Chrome MCP, and I tell you to use the
Chrome MCP to do that, and also figure out with the Chrome MCP, look at the traffic, what
are some relevant requests that fill the panels with data? And now I ask that, okay,
I want to test with, I want to make sure that
those things keep working, just do it. But how about you tell
us more about k6 v2.0 while this works in the background? - Right. So, can we have the slides back? Right, so while our agents are working, let me show you a few
highlights of the upcoming v2.0. I have five of them, and I suggest that we start from the top. As you might be familiar, k6
v1.0 always had a checks API, and checks are great
for load testing cases. We designed them specifically
with this in mind. They don't halt execution, they emit metrics, they give
failed past percentages. But for functional testing
or for browser testing, or for this kinda, does this
actually do what I expected? Validation, they always
felt like a workaround. In v2.0, we deliver
the new assertions API. And this API, as you might have noticed, is inspired by Playwright syntax. So if you used Playwright before, you'll see many familiar concepts, like hard and soft assertions, or async ones for browser testing that do these very
convenient auto retries. This API moves k6 from did it crash to did it do exactly what I expected? And this is what you need
when there is an AI agent that writes the code, and
your users depend on this. Now let's talk about extensions. In v1.0, we introduced
native extension support. That massively reduced the amount of times when you need a custom build. But the discovery and the trust story was still pretty rough. You had to know what's out there, you had to trust that it works. In v2.0, we introduced an
extension catalog with two tiers. The extension catalog uses
automatic dependency resolution. In short terms, how it works, you reference a model in your script, you run it, and it just works. Everything is handled in the background. And with this k6, it's not
just a testing tool anymore, it's a testing platform
with a real ecosystem. The extension catalog comes in two tiers. The first one is official. These are extensions that are built and maintained by Grafana Labs, and we guarantee stability and security. Things like xk6-faker
for test data generation, or MQTT for IoT protocol testing, or SQL for database validation. The second tier is community extensions. And these are extensions
maintained by external developers, by people like Pierrick
Hymbert with xk6-sse, or Mostafa Moradian with xk6-kafka. Grafana Labs provides guidelines and tooling to help maintainers to keep their extensions
stable and secure. But the innovation, it
comes from community. The extension catalog is
already available today. There is a link in there, go explore, see what fits your workflow already. Now, what I was talking about right now, these are JavaScript extensions. They provide modules that you
can import in your script, and nothing has changed in this regard. But in v2.0, we introduced
a completely new type of extensions, the subcommands. They don't add an import module, they add a whole new command
to the k6 CLI itself. And to create such extension yourself, the process is very standard. You create a Go module and k6 picks it up. And if this extension is
already listed in the catalog, we automatically provision this. So k6 will identify that the command extension is missing, it will provision the
right binary on demand, and it will run this command. There's no manual step in between. But if you are building something custom that fits your specific workflow, or maybe something new that
is not in the catalog yet, it will just go the same familiar pathways xk6 and custom built. And Theo already mentioned
three of these extensions that are available, the
agent, MCP, and the docs. There's also explore that
helps you or your AI agent to navigate the extension catalog and see what's there and maybe find something
that fits the job. And anyone can build their own. And the k6 with these extensions, k6 is not just a platform, it's not a platform for testing. It allows you to define the
workflow that your team needs. And now let's talk what's
happening beyond the test. Because the test that runs
on your laptop, it's useful, it runs, it prints results
to the standard output. But it's not enough. Tests need to grow with you, from the first run to
production infrastructure. And k6 v2.0 is designed to
scale alongside your stack. We introduced three layers. First you observe, we ship first-class
machine-readable outputs with v2.0. The OpenTelemetry output allows you to stream into your existing
observability stack. If you're already using Grafana, Grafana Cloud, Tempo, Mimir, results will show up right alongside your application telemetry. It's a single pane of glass. And then your structured JSON output allows you to integrate k6 into your custom pipelines, dashboards, or maybe give this output to the AI agent to analyze and reason about this. Then you automate. We introduce a new GitHub
action, run-k6-action, that makes it that simple
to run k6 and on GitHub. Every commit, every merge,
every PR, every deployment, all tested automatically. And with the new machine-readable outputs, it closes the loop. It gives you this fully automated circle. When the code is written,
whether by a human or AI, then tests are running, the results go back into the pipeline, and nothing is shipped without
the proof that it works. The third layer is scale. K6-operator hit v1.0. And for those of you who are not familiar what the operator is, it allows you to run distributed k6 tests on Kubernetes. This is where your app lives. And v1.0 is a commitment. It means semantic versioning, stable CRDs, predictable release schedule,
and a clear upgrade path. So if you've been holding
off using operator in your production, this is
a signal that it's ready. And this is how you go from, I run a test to testing is a part of my infrastructure. You observe, you automate, and you scale. Theo, how our agents are doing now? Let's check it out. - It's doing surprisingly well, but I'm still gonna
tell you how it's going, just in case it would take
much longer than we felt. Because, yeah, AI is fast,
but generally not that fast. Except today it was supposed
to not be done, but it's done. But anyway, a terminal output
is quite hard to read, right? And it's quite hard to parse,
especially on a big screen. So I'm spoiling the results a little bit. Claude and k6 v2.0 as part of the demo, did essentially four things. So as we've seen it do
at the very beginning when I launched the skill, it explored play.grafana.org, popping this hideous
chrome for your poor eyes. I'm sorry about that. And it started clicking
around, taking screenshots, and essentially trying to build
a mental model of the app. And once it had done that, then it switched to the new
tools that k6 v2.0 provides. And first of which the documentation. So it essentially with us instructing it to use k6 as part of the prompt, it essentially started by
reading the documentation. I have opened this
website, I need to test it, what should I do next? And the nice thing about it
is that it reads progressively and it reads only what it needs to read. And so it figured out about the APIs that it should use, best practices, and picked up specific patterns for the kind of testing it wants to do. And once it had done that, it
started leveraging the MCP. And the MCP essentially
allows it to do two things. It writes a script and it can call the MCP to validate it really
quick and token efficient, and then run it against production with very, very little settings. We also protect those to make sure that what it actually wrote
works in the real world. And it keeps iterating
using this until it passes. And finally those slides are dated because it used to generate three tests, but in my test this morning it generates more like six or seven tests, even stuff you don't ask about. But that's a good thing. So it generates tests, a full test suite, that is actually matching the requirements that we're looking to achieve. So if we switch back to the
demo and to the terminal. Yeah, sorry. Go for it. Up. And we look at the results. So it went actually really quick. And what we can see is that based on those requirements that we asked, so open play.grafana.org, change the time range, make
sure the data is updated, go in a panel, edit it, change the query, make sure it keeps working. And figure out what are the requests that fill a Grafana dashboard, and write at the very
least a load test for that. What it did is, you can
see, it used a couple of, it spawned a couple of subagents, it used a lot of tools
to be able to do that. And it ended up generating five tests. Five is bigger than three,
so it's probably better. What we see is we have
a browser dashboard test that's a load test specifically, it's called load, but it's
actually a smoke test. We have a browser test that verifies the time
range change feature. We have another one for the panel edit. And it did both a smoke and
load test for the API data. It also tells us what it covers, but more importantly, the skill makes sure that it tells you exactly
how to run this test suite, and it even offers to run it for you. We're not gonna run it on stage because this is gonna
take quite a bit of time. But how about we look at
what it generated for us? So we can see that it actually recorded the captured requests if
we want to introspect that. But it also generated those tests. So if we go in tests, we can see that the file it
mentioned actually exists. It did not hallucinate. And maybe the first thing that I as a user would
be interested in seeing is what is the script for the time range change looking like? Because I'm a very skeptical person. I wouldn't trust an AI to do a good job, although most of the time
it does, it makes me lie. But I'm fine with that. So if we look at the script, it's actually a pretty canonical script, and I'm always amazed to see that. It actually picked up
on the dashboard URL, it created a browser scenario, so it knows through the documentation exactly how to test through
a browser directly in k6. And it wrote this test,
which is nicely annotated and does exactly what we asked for. Navigate to the dashboard,
wait for the panels to render, then assert the panel heading is visible, click the time range picker, in the dropdown, click last one hour, then wait for it to be updated. And finally, verify that the URL changed and that the data are updated. So this one is a resounding success, and honestly from here, I think it would've taken me
probably three or four hours to write something that good. Now, how about the browser panel? If we go really quickly take a look, I don't expect anything crazy, but same, detected the right URL, actually took note of the expected query, and it's the same thing. Opens Chrome, goes there, and same thing. Navigate to a panel, verify the query editor row is visible, start clicking around, verify that the Prometheus
request is correct, modify it, and so on and so forth. And this is all following
the best practices of k6. And finally, probably
the thing that for me as an old backend engineer, I
used to be a backend engineer, is the most interesting,
here's the API load test. So I want to make sure that when we have, how many, 35 million users at this point, something like this? I don't remember. Imagine all those people connect. How can we make sure that it works? Well, this is a test on stage. I'm not gonna take play.grafana down. But here it actually created
a load test scenario. It defined some thresholds. So for instance,
automatically decided for me that 95 of the requests should
take less than one second, and 99% of them less than two seconds. It also makes sure that there's no errors, that the rate of failed
requests is below 1%, and then it proceeds with
writing an actual load test, which is nicely grouped
and have those checks, could also be assertions in smoke tests. It probably is. That verify that when
we send a given request, we receive responses that
look and behave correctly, and we start punching the server, in this case, with 20 requests per second. But so if we go back to the slides now. What used to take days, and let's say at the very least, a couple of dedicated
engineers, testing engineers, most of the time or SRE, a lot of time, a lot of expertise. We've just done it on stage and I checked Claude,
it took five minutes. So what would take probably
four or five days before takes five minutes. It's actually took requirements, transformed it into a strategy, and delivered a test suite
that's ready to go in CI, that's ready to deploy, and that's ready to scale with Kubernetes and with the operator at
the scale of your workloads. So that's exactly what
k6 v2.0 makes possible. You don't have to guess anymore. You can let the AI help you prove that things work the
way you say they work. - And let me put it all together. K6 v2.0 drops on May 11th, and it will look and feel familiar, but it's also designed for the world that we currently live in, where the agents write code, and testing is basically their safety net. And here's what we want you to do once the new version drops. - Please use the agent command, initialize your workflows in
whatever projects you have. It could be a pet project
or big production project. Try it out. I was convinced and I started skeptical, and now I use this all the time. - Go explore, browse
the extension catalog, and find an extension
that fits your stack, or even better, contribute one yourself. Integrate, run k6 action in CI, and make testing non-negotiable. Nothing should be shipped
without the proof. - And finally, scale, like deploy k6 with the k6-operator where it actually matters
the most, in production. - May 11th. Stop guessing, start proving. And mark your calendars. Thank you.
- Thank you. (audience applauding)

