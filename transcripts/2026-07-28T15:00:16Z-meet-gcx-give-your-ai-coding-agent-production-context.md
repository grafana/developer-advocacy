# Meet GCX: Give Your AI Coding Agent Production Context

Published on 2026-07-28T15:00:16Z

## Description

Your AI agents are only as good as the context it has. Without access to what's happening in production, it can only make ...

URL: https://www.youtube.com/watch?v=1HzraMndn_E

## Summary

The show titled "Meet GCX: Give Your AI Coding Agent Production Context" was published on July 28, 2026, featuring Shawn from Grafana Labs. The discussion focused on GCX, a command-line interface (CLI) that connects AI coding agents like Codex and Copilot to production telemetry within the Grafana stack. Key features of GCX include predefined skills for troubleshooting and managing Grafana functionalities, as well as the ability to query telemetry and diagnose issues in real-time. The demonstration highlighted how GCX can efficiently assist in identifying and resolving production issues, such as a missing ingress configuration.

Topics: GCX, Grafana, AI coding agents, telemetry, troubleshooting, command-line interface.

## Chapters

00:00:00 Introduction to GCX and its capabilities
00:04:50 Setting up and using GCX for troubleshooting
00:10:22 Diagnosing ingress issues with GCX

Hey everyone, I'm Shawn from Grafana Labs, and today I am super excited to introduce you to **GCX**. Now, GCX is a CLI that gives your coding agents like Codex, Claude Code, Cursor, and Copilot— the list goes on— direct access to your team's production telemetry right from your Grafana stack.

Now, I know what you may be thinking right out the gate: "Awesome, another CLI! What makes this so special?" And honestly, that is a fair question. But GCX was built for the Agentic era we're living in. There are a few capabilities built into GCX and shipped along with it that are completely changing how your AI agents are able to reason, infer, and investigate real production telemetry issues. Chances are you probably haven't seen some of these features that we're shipping along with it.

So in this video, we'll start from scratch. We'll get GCX connected to Grafana, and I will even show you a few of my favorite workflows that I'm using and tips that can make your AI agent dramatically more useful for you. Let's jump in!

Awesome! So let's start with installation. This part is actually very straightforward. We'll just go into the Grafana GCX GitHub Repo, which is open source, accessible to everyone, and totally public. We'll scroll down to installation. 

Now, depending on which operating system you're on, you're going to go down a different path for installation. If you're on Linux or Mac OS, it's very easy—just use Homebrew or you can even use Curl. As always, if you're on Windows or Mac or Linux, honestly, this goes for anyone, you can just download the prebuilt binary from the releases page. You just click on the releases page here, and then you'll be able to grab the latest version, download it directly, and then unzip that.

Cool! So once we're done with that, let's jump over into our terminal. When we run GCX, you'll see that we get a list of all of our available commands we can run—from alerts to the Grafana Assistant, to authentication, to dashboards, to data sources, to log querying, metric querying, and trace querying. The list goes on. There are a ton of pieces of Grafana functionality jam-packed into GCX that are accessible to you, as well as all the flags. 

For example, we have the `/agent` command or a flag that you can append to your GCX commands. This enables agent mode, JSON output, no color, and better error output. So this is more efficient when it comes to tokens.

When we actually talk about connecting GCX to our stack, there are a few ways you can do this. The very manual way of doing this is just `GCX auth login`. This will kick off an OAuth session into your Grafana Cloud account. However, let's say you're wanting to use some of the predefined skills that GCX has accessible; you can install those. By just running `GCX skills install all`, you'll see that we've installed 17 skills right into our agents-skills directory. 

What's cool about this is that all these skills—like debug with Grafana, export data sources, import dashboards, and manage dashboards—are predefined skills that we have built out and packaged with GCX, so you don't have to write them from scratch. If you go to use QuadCode, Cursor, Copilot, or Codex, whenever you prompt and say, "Hey, I need to investigate something in Grafana," it's going to preload these skills that you've installed into your agent's path.

For example, if we wanted to jump into QuadCode and use the backslash `setup GCX` command, this will actually run that backslash command in QuadCode to be able to set up GCX with your Grafana stack. Now, let's say we wanted to do this on-premise instead. What we can do is jump into QuadCode and say, "I want to connect GCX to my on-premise Grafana stack." 

What this will do, as QuadCode starts to infer, is it'll load up that `setup GCX` skill similar to the backslash command. It's pretty much just loading it into context here for us. You'll see that it'll check the GCX version. It also goes through path B, which is the on-premise setup, with path A being Grafana Cloud. 

You'll see that GCX is already installed, and it's going to ask what my server URL is because if I'm running it on-premise via open source or Grafana Enterprise, it'll ask where this is running. It could be on localhost:3000, or I could have a proxy URL that it's going to. Also, my authentication method—how do I log into this stack to begin with? Is it through my service account tokens, username, passwords? What context name do we want to give it? 

Once we do this and submit all this, you'll see that we can actually verify which stacks we have connected. If you run `GCX config view`, this will give you all the context you have. For example, if I had my Grafana and this was an open source stack, that context that I give it will be here. 

Now, what I have currently connected, and I can see this by running `GCX config current context`, is "tech content." So it's referencing this context, similar to what you do when you run `kubectl`. It'll have your context or configuration and know what `kubectl` is scoped to, like what cluster, for example. 

You'll also notice that we have a level of security built into GCX out of the box. Tokens are redacted, and any sensitive information is going to be redacted. 

So now that we are all set up with GCX and we verify that we're connected, we can start to jump into some of the cool features that GCX has exposed to it. Like I said, we can query our telemetry directly through GCX. 

So let's run a query, and this is going to be `GCX metrics query`. Inside our apostrophes, we'll have our query that we're running. This is a PromQL query. Essentially, what I'm doing here is I want to get the CPU percentage by container. You'll also notice at the end here, I've appended a few flags. So I'm going to look at the last hour, and then I have this `-O graph` command. What this will do is actually generate a real-time graph right in the CLI or right in the terminal, which is really cool.

But this is more of a manual way that you would use GCX. Like I said, GCX is built for the agentic era. So let's actually jump into a real use case where I'm going to use GCX to troubleshoot.

Okay, so we have been getting some reports from users that our plans page on our application isn't loading. Let's actually jump over into our application to try to figure out what the heck's going on. 

Now, if I load this up, we can see that everything looks to be loading properly in our app, but when we go to this plans page, it goes blank completely. I don't know why that's happening. Even if I refresh, it doesn't seem to be doing anything. So we need to figure out why the heck that's happening. 

Let's jump into our terminal yet again, and let's kick off a process here with QuadCode to troubleshoot. We're going to jump into Quad and say, "We are experiencing an issue in production where the plans page is not loading anything. Let's troubleshoot using Grafana." 

What this is going to do with this very simple prompt is it's going to start inferring and looking at some of the skills that we have accessible through QuadCode. You're going to see that it actually calls this Grafana debugger skill that we've installed with the predefined skills that come out of the box with GCX. 

Now, I'm going to say, "Don't ask me again for any of these GCX commands for approval," essentially, because I don't really need it. I trust it to go do its work with GCX. There's nothing it can really break here; it's just going to be reading telemetry for the most part. 

We can see in real time what it's starting to do. It's starting to look at plan services, and it's going to start looking at some of the other ones that we have accessible, like what are the other service names we have in the cloud logs data source? So it actually has context into how to look for data sources and what telemetry to look at. We can see it's...

Looking at the chat service now, it's even starting to look at our actual code base, which is nice because we're doing this in Quad Code that has access to our code base. We're going to see it's looking for errors, formatting it into JSON, and checking the API plans route. It's examining if there are any exceptions over the last two hours up to now. It's limiting the output that it's giving, which is going to save on tokens. 

At the end of this investigation, we will look at how many tokens it has used in our session because I am curious to know how efficient this is actually being. We can now see that it's looking at the app name "front end," which seems like a step in the right direction. It's starting to cross-reference front end logs as well. As it infers, hopefully, we get a diagnosis that's accurate. I think I know what the problem is; I believe any developer might see the issue pretty obviously. However, I want to see if GCX and Grafana can troubleshoot this for me without me having to think too hard about it.

My hunch is that it's an ingress issue and that I didn't add the ingress for the plans API into our Kubernetes manifest. I want to see if it can diagnose that for us just to show its accuracy. It's going to look at traces, query our metrics, and examine some of the infrastructure. We can see that it's actually looking at ingress paths as well. Now it's looking at my manifest. I wonder if it identified the issue. It seems like it's doing a really in-depth analysis of our code base, looking at real files and seeing where our gaps are.

Once again, this is definitely an ingress issue. I'm starting to be very confident in that, which is funny because I feel like I should have known to add that. That's also something that I now need to build into my automation workflows to ensure that when I add a new endpoint, it is accessible via the ingress. 

So, the root cause is that the ingress config is missing in the API plans route. The plans page is blank because the production front end ingress has no routing to the API plans, so requests are falling through. Awesome! It looks at the FARO logs, and we see all 200s for the requests, indicating that the backend is not the issue. There are zero planned request events that we're logging out through the chat service. All traces terminate at the front end pod, with no downstream span to the chat service. This is all very indicative that this was an issue with our ingress.

Let's just say, let's add that into our ingress and deploy. This is essentially GCX working its magic, right? It was using all the skills at its disposal to properly diagnose this issue for us. I'm just smiling right now because I didn't know if it was going to be able to actually do this for us, but it caught the issue very well.

Now I want to know, since we've identified this issue with GCX, what our usage is in Quad Code. We can see that this whole investigation with GCX was something maybe this simple. Obviously, there are going to be things that are probably more in-depth and more subtle that you'll be catching with GCX. But this was a $1.70 investigation, taking about 360 input tokens to Claude Haiku 4.5 and using about 556 input tokens into Opus 4.7. Overall, not that many tokens were used; $1.70 for this is really good.

So, let's just say only the ingress changed; everything else is confirmed. Let me verify we're pointing out the right cluster. Confirmed, it applied. Okay, awesome! In a few moments, this will all load up, and we will be all set.

To summarize what we've done in this video, we introduced you to GCX. We set it up with our Grafana stack, which can be done through on-prem and cloud instances with Grafana. Additionally, we installed some out-of-the-box skills that come with GCX, which can be super helpful for troubleshooting, managing dashboards, handling data sources, and so forth. We even troubleshot an incident in real time that I personally messed up with ingress paths.

This is just a quick introduction for you to meet and become comfortable with GCX. We will be building more content around GCX and its use cases. Thank you so much for tuning in! Please like and subscribe to this channel, and we'll catch you in the next video. Take it easy!

## Raw YouTube Transcript

Hey everyone, I'm Shawn from Grafana Labs, and today I am super excited
to introduce you to GCX. Now, GCX is a CLI that gives your coding
agents like Codex, Claude Code, Cursor, Copilot. The list goes on direct access to your
team's production telemetry right from your Grafana stack. Now, I know what
you may be thinking right out the gate, which is awesome, another CLI, what
makes this so special? And honestly, that is a fair question, but GCX was built for the
Agentic era we're living in. And there are a few capabilities built
into GCX and shipped along with it that are completely changing how your AI
agents are able to reason, inference, and investigate real
production telemetry issues. And chances are you probably haven't
seen some of these features that we're shipping along with it. So in this
video, we'll start from scratch. We'll get GCX connected to Grafana, and I will even show you a few of my
favorite workflows that I'm using and tips that can make your AI agent dramatically
more useful for you. Let's jump in. Awesome. So let's start with installation. This part is actually
very straightforward. We'll just go into the Grafana GCX
GitHub Repo, which is open source, accessible to everyone, totally public.
We'll scroll down to installation. Now, depending on which
operating system you're on, you're going to go down a
different path for installation. If you're on Linux or Mac OS, very easy, just use HomeBrew or you can
even use Curl. As always, if you're on Windows or Mac or Linux,
honestly, this goes for anyone. You can just download the prebuilt
binary from the releases page. You just click on the releases page here, and then you'll be able to grab the
latest version here, download it directly, and then unzip that. Cool.
So once we're done with that, let's jump over into our
terminal. When we run GCX, you'll see that we get a list of all of
our available commands we can run from alerts to the Grafana assistant,
to authentication, to dashboards, to data sources, to log
querying, metric querying, trace querying.
The list goes on. There are a ton of pieces of Grafana
functionality jam packed into GCX that is accessible to you, as
well as all the flags. For example, we have the /agent command
or a flag that you can append to your GCX commands.
This enables agent mode, JSON output, no color,
better error output. So this is more efficient
when it comes to tokens. So when we actually talk about
connecting GCX to our stack, there's a few ways you can do this. The very manual way of doing
this is just GCX auth login. This will kick off an OAuth session into
your Grafana Cloud account. However, let's say you're wanting to use
some of the predefined skills that GCX has accessible,
you can install those. So by just running GCX
skills install and then all, you'll see that we've
installed 17 skills right into our agents-skills directory.
And what's cool about this is all these skills like debug with
Grafana, export data sources, import dashboards, manage dashboards, these are predefined skills that we have
built out and packaged with GCX so you don't have to write them by scratch. So if you go to use QuadCode
or Cursor or Copilot or Codex, whenever you prompt and say like, "Hey, I need to investigate
something in Grafana," it's
going to preload these skills that you've installed into your
agent's path. So for example, if we wanted to jump into Quad
Code and use the backslash setup GCX command, this will actually run that backslash
command in QuadCode to be able to set up GCX with your Grafana stack. Now, let's say we wanted to do
this on-premise instead. What we can do is we can go
just jump into QuadCode and say, "I want to connect GCX to my on-premise Grafana
stack." And what this will do as QuadCode starts to sort of
infer is it'll load up that setup GCX skill similar to the backslash
command. It's pretty much just loading it into context here for us. And then you'll
see that it'll check the GCX version. It also goes through path B,
which is the on-premise setup, path A being Grafana Cloud. So you'll see that GCX is
already installed and it's
going to ask what my server URL is, because if I'm running it on-premise via
open source or Grafana Enterprise per se, it'll ask where this is running.
It could be on a local host 3000. I could have a proxy URL that it's going
to. Also, my authentication method. How do I log into this
stack to begin with? Is it through my service account
tokens, username, passwords? What context name do we want to give it? And once we do this and submit all this, you'll see that we can actually
verify which stacks we have connected. So if you run GCX config view, this will give you all the
context you have. So for example, if I had my Grafana and this
was an open source stack, that context that I give
it, that will be here. Now what I have currently connected, and I can see this by running
GCX config current context, is tech content. So it's
referencing this context, similar to what you do
when you run kubectl. It'll have your context
or configuration and know what kubectl is scoped to,
like what cluster, for example. And you'll also notice that we have a
level of security built into GCX out of the box. So tokens are redacted. Any sensitive information
is going to be redacted. So now that we are all set up
with GCX and we verify that we're connected, we can start to jump into some of the
cool features that GCX has exposed to it. So like I said, we can query our telemetry directly
through GCX. So let's run a query, and this is going to be GCX
metrics query. And then inside our apostrophes essentially, we'll
have our query that we're running. This is a prompt QL query. So essentially what I'm doing here is
I want to get the CPU percentage by container. And you'll also notice at
the end here, I've appended a few flags. So I'm going to look at the last hour
and then I have this hyphen O graph command. And what this will do is actually
generate a real-time graph right in the CLI or right in the
terminal, which is really cool. But this is more of a manual way
that you would use GCX. Like I said, GCX is built for the agentic era. So let's actually jump into a real
use case where I'm going to use GCX to troubleshoot. Okay. So we have been getting some reports
from users that our plans page on our application isn't loading. So let's
actually jump over into our application to try to figure out what the heck's
going on. Now, if I load this up, we can see that everything looks
to be loading properly in our app, but when we go to this plans
page that it goes blank completely. And I don't know why
that's happening. Even if I refresh, it doesn't seem to be doing anything. So we need to figure out why
the heck that's happening. So let's jump into our terminal yet again, and let's kick off a process here
with QuadCode to troubleshoot. So we're going to jump into Quad and
we're going to say we are experiencing an issue in production where the plans page is not loading anything. Let's troubleshoot using Grafana. So what this is going to
do with this very simple prompt is it's going to start inferring
and looking at some of the skills that we have accessible through Quad Code. So you're going to see that it actually
calls this Grafana debugger skill that we've installed with the predefined
skills that come out of the box with GCX. Now I'm going to say, don't ask me again for any of
these GCX commands for approval, essentially, because I
don't really need it. I trust it to go do its work with GCX.
There's nothing it can really break here. It's just going to be reading
telemetry for the most part. So we can see in real time
what it's starting to do. It's starting to look at plan services. It's going to start and look at some of
the other ones that we have accessible. Like what are the other service names
we have in the cloud logs data source? So it actually has context into
how to look for data sources, what telemetry to look at. We can see
it's looking at the chat service now. It's even starting to look
at our actual code base, which is nice because we're doing this
in quad code that has access to our code base. We're going to see it's looking
for errors. It's formatting it into JSON. It's looking at the API plans route. It's looking at if there's any exceptions
over the last two hours to now. It's limiting the output that it's
giving that's going to save on tokens. And we're actually going to look
at the end of this investigation, how many tokens it's used in our session
because I am curious to know like, hey, how efficient is this actually being?
So we can now see that it's looking at the app name front end, which is a step in the right
direction it seems like. So it's starting to cross-reference
front end logs as well. And as it infers, hopefully we get a diagnosis
that's accurate because I think I know what the problem is. I think any developer
might see the issue pretty obviously, but I want to see if GCX and Grafana
can sort of troubleshoot this for me without me having to
think too hard about it. Now my hunch is that it's an ingress
issue and I didn't add the ingress for the plans API into our Kubernetes manifest, but I want to see if it
can sort of diagnose that for us just to show its accuracy. So
it's going to look at traces. We can have it go do that. It's
going to try to query our metrics, look at some of the infrastructure. And we can see that it's actually
looking at ingress paths as well. And now it's looking at my manifest. I wonder if it identified the issue.
It seems like it's doing a really in-depth analysis of our code base as well. So it's looking at real files and seeing
maybe where our gaps are. Once again, this is an ingress issue for sure. I'm
starting to be very confident in that, which is funny because I just feel
like I should have known to add that, but that's also something that I now need
to build into my automation workflows to be able to say when
I add a new endpoint, to make sure that that's accessible via
the ingress. So let's see. Root cause. Ingress config missing
in the API plans route. The plans page is blank because production
front end ingress has no routing to the API plans. So requests are
following through. Awesome. So it looks at the FARO logs.
We see all 200s to the requests. So the backend is not the issue.
There's zero was planned request events that we're logging out
through the chat service. All traces terminate at the front end
pod, no downstream span to chat service. This is all very indicative
that this was a issue with our ingress. So let's just say, let's add that into our ingress and deploy. So this is essentially
GCX working its magic, right? It was using all the
skills that it has to its disposal and being able to properly
diagnose this issue for us. And I'm just smiling right now because
I didn't know if it was going to be able to actually do this for us, but
it caught the issue very well. Now I want to know since we've
sort of identified this issue with GCX, what our usage is in quad code. So we can see that this
whole investigation with
GCX was something maybe this simple. Obviously there's going to be
things that are probably more in depth, more silent that you'll be catching
with GCX. But this was a $1.70, took about 360 input
tokens to Claude Haiku 4.5, used about 556 input tokens into Opus 4.7. And then not that many tokens overall, like $1.70 for
this is really good. So let's just say only the
ingress changed, everything else. Let me verify we're pointing out the
right cluster confirmed. It applied. Okay, awesome. So we should be
good. In a few moments, this will all load up and
we will be all gravy. Okay. So just to summarize kind of
what we've done in this video, we introduced you to GCX. We set
it up with our Grafana stack. You can see how that can be done
through on-prem and cloud instances with Grafana. On top of that, we installed some out-of-the-box skills
that comes with GCX that can be super helpful for you when it comes to
troubleshooting, managing dashboards, handling data sources and so forth.
We even troubleshooted an incident in real time that I personally
messed up with ingress paths. And yeah, this is just a quick introduction and
for you to meet and be comfortable with GCX. We're going to be building more
content around GCX and use cases, but thank you so much for tuning in. Please like and subscribe to this channel
and we'll catch you in the next video. Take it easy.

