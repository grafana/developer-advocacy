# AI/ML + Grafana: How to Create Intelligent Grafana Apps Leveraging LLMs | GrafanaCON 2024 | Grafana

Grafana Tech Lead Nathan Marrs demonstrates how to leverage the power of large language models (LLMs) to create intelligent ...

Published on 2024-04-25T23:27:10Z

URL: https://www.youtube.com/watch?v=kt6gbQtzmV4

Transcript: Hello everyone. My name is Nathan Marrs and I'm the
tech lead of Grafana Data Visualization Squad. I'm really excited to be here in Amsterdam
to talk about a subject that I've been really interested in -- how recent advancements in AI and the
rise of large language models might fundamentally change how
we approach observability. Here at Grafana, we've been asking what the future
of observability might look like. Who here has also wondered the same?
A couple people in the audience. And who here has wondered how advancements
in AI and LLMs might shape our everyday lives? More people. And finally, who here has wondered how much longer
our jobs will be safe from the iron grasp of robots? That's definitely
something I'm worried about at night. So today we're going to be looking at
how Grafana has been embracing this future. And also we'll end today's
talk with how you, yes you, can directly contribute to and
mold the future of observability. So we're going to begin with Grafana
Labs' approach to how we've integrated machine learning/artificial intelligence
with observability. But first, what is observability and what
problems are we trying to solve? There are many different ways
of defining observability. And this quote from our Director
of Community sums it up nicely. Observability is about enabling humans
to understand complex systems and we need to understand them as
we need to operate them. So what does it take for humans to
understand and operate these systems? I'll go over two different aspects.
The first is deep domain knowledge. You need to understand how your system
works, how its' dependencies work, and where its' boundaries
are. This is not an easy task. As new technologies emerge, the modern stack is getting more and
more complex and there are more and more layers of abstraction. And it's not
just about knowing your service, it's also keeping up with
this new underlying tech. Another consideration is that
there's more data than ever before. There are more metrics, logs,
traces, and profiles to keep up with. And this can really lead
to an information overload. And even if you have this deep domain
knowledge, we're in a team sport here. Maintaining a shared understanding
between people leaving and people joining your team is yet another challenge
we face. Next, we have toil. And this is not just
work I don't like to do. It's work that's tied to
running a healthy service. And this scales as the service grows,
it tends to be repetitive and reactive. Examples can include like restarting a
stuck pod or scaling up your deployment and they're manual tasks that
can take up a lot of your time. So what's the role of machine
learning and AI in all of this? We've defined this role as minimizing
both toil and the need for deep domain knowledge. This enables us to understand complex
systems more efficiently and effectively. And we want to emphasize here
that this is still human. Like we still expect humans to
be the driver of these workflows. We just want to use these tools of
AI/ML to help humans make things less complicated. So let's take a brief look at how we're
integrating machine learning to achieve this goal today. So we're doing things like
adaptive alerting where you
don't need to worry about setting static thresholds. We can just use the thresholds that
we've learned from historical data. Instead of you having to worry which ones
you should set, or with Grafana Sift, which is pictured here, where we can automate some of the
routine parts of incident investigation. So things like Matt just mentioned,
like servicing error log patterns, or uncovering a recent deployment that
might be a cause of an incident. We've already seen these features be
really helpful to engineers to have a springboard when they go to debug issues. And these features are already available
as part of Grafana Cloud as part of the free tier. So this is an AI talk, so you're probably expecting
to hear this next phrase. It's the elephant in the room. So we've all heard of large
language models at this point, and in 2024 they've continued to
improve and there are widely available low-cost, large language model APIs. What's interesting about large language
models is that they kind of serve as this translation layer
between humans and machines, which enables a whole host of
new experiences. We've seen LLMs closing gaps in two different areas.
So you know what you want to do, but you don't know how to do it. So let's say you have a SQL database
and you want to get data out of it, but you don't know SQL or
in this case over here, you know how to do it and it takes a lot
of effort. So summarizing a document. What's key here is that LLMs have natural language as your interface, which makes it more accessible
to everyone. You don't
have to know how to code, you just have to know
how to speak a language. These two gaps actually map nicely to
the two challenges in observability that we just mentioned before. So
LLMs present this kind of big, scary, exciting opportunity. So we've kind of been given this chatGPT
hammer and it's kind of a choose your own adventure. Like what hammers
can we hit or what nails can we hit, not hammers with a hammer. Okay,
it's a bit of a fickle hammer though. It's sometimes great, sometimes not. It
can be unreliable, it can hallucinate. But in some cases we've managed to
knock some sense into this hammer. And the more that we've
learned about this tool, the more we realize the value that it
could have and we want to enable everyone to build with generative
AI throughout Grafana. So what's Grafana's
approach to generative AI? So Grafana Labs has always taken a unique
approach to projects and products for open source. We've developed in the open since the
beginning of our generative AI journey. For big tent, we empower you
to use whatever tools you like, no vendor lock-ins. And for
defaulting to transparency, we have opened up data sets, prompts, and code so you can see exactly what's
going on in the context of the LLM. So we've built in generative AI support
directly into Grafana open source, not just Cloud or Enterprise. Anyone can add generative AI features
into Grafana via plugins, pull requests, feature requests, which I'll demo later. And generative AI features are
fully opt in and they're managed and customized all from one
place with our LLM plugin. We also have released some open source
libraries and examples to give a community a head start and we can't
wait to see what the community comes up with. For big tent, we're making Grafana work for you
regardless of your choice of tech. For generative AI, this looks like you
can actually choose your LLM. For now, we just have OpenAI and
Azure Managed OpenAI, but we're planning on adding
more LLMs in the future, including self-hosted options. Likewise, you can choose the vector database you
can use our built-in solution or you can contribute open source
contributions for more. And a key point here is that we want to
make the AI experience equal across all data sources, not just Prometheus
and Loki, but also for Influx, Elastic and Posgres. We want meet with community where it's
at and not just have favorite children. Finally, for the final value transparency here we
want to turn the black box of LLMs into a glass box. What this means
is we have open prompts, which means you can see the exact inputs
going into the LLM from the open source code, which you'll actually
see in a minute here. We've also shared evaluation and benchmark
results on the performance of these features over time and over model changes. And we're planning on eventually
releasing open data sets to help you get started quickly on building new features. So things like public dashboards or
queries from communities integration. So let's take a look at three generative
AI features that we've built so far. So this first one is
the dashboard assistant. This one's pretty close to my heart as
I was on the team that helped build this out and I learned a ton
doing it. In this case, we see that generative AI is being
used as a helper to add titles and descriptions of panels and dashboards. This is a great example of a small assist
that can reduce toil and quickly add real value. This is not a game changer, but it helps engineers with small hurdles
and can easily make dashboards more robust and consumable. So we're actually look at some code here. So here's a little behind the scenes
look at the dashboard assistant. So here at Grafana we
really do build in the open, like this code is open source
and inside the Grafana repo, which is one of my favorite
aspects of working at Grafana, is all the code is public. Here
we're looking at the prompt, we're providing the LLM
to generate a panel title. Here you can see the panel
JSON and dashboard metadata. We're providing that as helpful context
to help drive reasonable answers. So next we can use LLMs to jumpstart
more challenging tasks like writing PromQL. Here we have a built-in vector model
based on thousands of open source PromQL queries. We can use that model alongside an LLM
to allow users to write queries more quickly. We see it wrote a query for us. So let's take a closer look
inside the query advisor. First we start with the system prompt. And what does system mean
in this context? Well, it's part of three different
roles in OpenAI's chat API. There's system, user, and assistant. System provides high-level
instructions and guidelines. The user presents the queries or prompts.
And assistant is the LLMs response. So here in the query
advisor systems prompt case, try saying that five times fast. We
are providing an explicit policy, not just to makeup label names. As
you can imagine, without that line, it had liberal license to do so before. And now we're gonna look at the
user persona prompt. In a nutshell, we're asking the LLM to pick and
choose relevant PromQL templates found via semantic search based on
the context of the user's input. And I want to zoom in a little bit
further on how we retrieve these PromQL templates from the vector database. So here we can actually see
that Grafana LLM plugin at work. The PrompQL templates are stored in a
vector database filled with thousands of open source PromQL queries. We then use
the LLM plugin to semantically search, and in this case return the top five
results based on the user's input. Then here in the bottom right code block, we pass those results as part of the
user persona prompt and then let the LLM the actual large language model decide
which templates are a best fit for the user's intent. And finally, the final feature I want to
cover today is flame graph AI. This is something that came out recently. I wanna give a huge shout to Ryan Perry
and team on their great work on this feature. This feature helps you understand
your flame graph profiling data. Once a flame graph, well, flame graphs provide a convenient
way to visualize performance data, but not everyone knows how to
read them or get value from them. Flame graph AI closes this gap and makes
flame graphs more accessible to a wider audience. And it does this by
highlighting performance bottlenecks, providing possible root causes, and even includes how you
might resolve these issues. So far we've seen the opportunity with
generative AI is not necessarily in building out a single super
app. Instead it's many, many small improvements across the
workflow that together can make a big difference. We like to call this
delight by a thousand flowers. We've covered some of what we built and I want
to move on now to what you can build and maybe you can phrase this as what
flowers you might be able to plant. So now we get to the fun part, how you can help build the
future of observability. Let's uncover what the intersection of
LLMs and observability might look like. We can simplify this down as an equation. So LLMs plus Grafana plus scenes equals question mark. The goal for the remainder of this
talk is to solve this equation. Sorry if you thought math class
was over. So let's simplify. Hopefully we all know what Grafana
is, so we can check that off. Okay, great. We're one step
closer to solving this equation. Now let's move on to scenes. So Grafana scenes is a front end library
that allows you to effortlessly extend Grafana. With scenes, you can build dynamic
dashboarding experiences
directly in apps with support for data querying and transformations,
time range and variable management, panels and data visualizations, as well as ability to make drill down
experiences as we'll see in a demo in a minute. All right, so
we've got one piece left. Unfortunately, given
the time of this talk, LLMs will have to remain
a bit of a black box, but at a super high level you can just
think of them as an intelligent next word generator and they're specialized and
trained to be a helpful assistant to you. So with LLMs waved away, let's solve
this equation together in a live demo. And this is where things can get
interesting, especially with an LLM. So today we're gonna be taking a
look at a Grafana scenes app template that we have that kind of includes
some examples of basic scene -- a scene with tabs, a drill down experience and
something that we've added recently, or something I added for this demo,
which is integrating with LLM plugin. So here is the basic
template we have just a basic app page with tabs. We see we have support for panels and support
for time ranges and we actually can support multiple different
time ranges on the same page. Something that was not possible before. More interestingly here we have a drill
down example where we can see here, if I click on seller, this
is just a demo panel, right? Showing the temperature of
different rooms in your house. We can see here we actually have a
drill down experience built into the app where we can see the seller's temperature
and humidity and we can see it's actually supported in the navigation
system. We're seeing seller overview here. It's actually coming up here
inside of the URL as well. What this allows for is some
type, type of deep linking. So let's say we just want to go directly
to the seller's humidity overview. We actually link directly to that and
this really enables a ton of really powerful flows. But today we're
here to talk about AI and LLMs. So what we have here is this
new page with LLM integration. So real quickly I want to show you
the LLM plugin that we have released. This is available in open source and we
can see here that you can select your provider. Right now it's
only OpenAI or Azure OpenAI, but we're planning on adding more support
for others later as well as add your OpenAI key. Importantly here, I want to call out that
there's a button here, a big button to disable all
LLM features in Grafana. So we really want to give you
the power and control to enable or disable these features
as you like. Finally, we also have vector settings here, which we're not gonna be messing with
today to configure your vector database to enable things like semantic
search as shown in the PromQL assistant. So let's start talking to the LLM. So this first example is really
just a wrapper around chatGPT is how to describe it. It's basically this example of how
we can integrate the LLM plugin directly into a Grafana app. And so if
I ask, you know, what is 10 times 10 we'll see what it says and it's going to give me a snarky
answer because we're telling it to be actually a cynical assistant in the
system prompt. So it's kind of rude. Your results may vary, but
it's rude to me. That's fine. We'll move on. One second. I need to grab my code window. It's a real demo. So showing you a little bit of code here. But really just to get
some questions to ask. What I want to point out here real fast
is this is a basic implication of scene object and this is basic LLM integration
page that we're seeing on the other page. And what I want to point out here
is the kind of flexibility of scenes. This object that we're rendering
is a scene react object, which allows me to kind of throw
in any react component that I want, which is what this whole UI is. So now I'm gonna ask it. If you had to guess the number
that defines the meaning of life, what would it be and why? And we can see it's streaming in and
the number's 42 based off Hitchhiker's Guide to the Galaxy. I want to point out that
this stream is interesting, the OpenAI API has a streaming
capability as well as just a chat completions capability. And what we found the streaming makes
a lot of sense when you're generating small to medium amounts of text
that the user can actually see. Now let's see the functionality of
just not using a stream capability. So you can see it's loading and then
just loads of requests in. And for this, this is pretty much what
we use for everything else. If there's a huge amount of text you're
trying to generate doesn't really make sense to show that to the
user as it can be distracting. Or a lot of times you're having
kind of discussions internally with the LLM that are not even user-facing,
so you don't need to do a stream. You can show a little
bit of that in code here. So this first thing that's highlighted
is a stream and we can see that this LLMs is our LLM plugin and we're
connecting to the OpenAI API, which is stream chat completions.
Here we're passing in the model, which is 3.5 and the
messages - in this case, the system and user. And you can see the system message
is you are a cynical assistant, which is why it berated me for
asking what 10 times 10 is. And then up here we can just see the
only difference here is instead of stream chat completions, it
says chat completions. And that's the use case that
we use most often. All right, so this is cool. Maybe if you have
like a bird observability app, you could ask it what does this bird
do? Or where does this bird live? If you have chatGPT in there, but this
is not as interesting as it could be. So I want to pose a question. What if you could have a conversation
with your dashboard, with your app, with your data? And would that be a
potential future of observability? Maybe, maybe not. So don't worry about that
code below super hacky. But we're going to ask a couple
questions to this and see what we can do. So in this context, let's just say I have a scenes app where
I'm kind of viewing all the different servers in one place for my company
and I'm only seeing five here, so I actually wanna see 20. So
fingers crossed on this one. Okay, it shows me now 20. I'm
gonna refresh this data, it's dummy data until I
get a result I want. Okay, so let's say I hand this off to someone
and they don't really have context on what they're looking at,
like what does this all mean? What we can do is say, "explain what this data that's being displayed is" and it tells me it's performance metrics
of different servers over time and that understanding this data
helps optimize the server
infrastructure and ensure its reliability and efficiency.
Sounds pretty accurate. This could probably be improved
with some prompt engineering, but it's on a pretty right track
for just giving high-level context. So now let's say I'm looking at this
chart and I notice that my SQL 4 server is a little higher than normal. So
I'm gonna focus in on that one. And let's say I want to figure
out, based on historical data, is this normal for this server?
Do I need to be alarmed by this? Do I need to investigate? So we're just going to ask and fingers crossed on this
one. Okay, so it worked. Look at that. Okay, so we can see
here the comparison data is is lower, substantially lower actually
than this week's data. So this is probably something I want to
look more into and try to dive more into maybe through this interface,
although this is the end of the demo. So that's where we're
gonna be stopping today. So I want to call out that this code
is actually in a PR that's going to be added to the scenes app template. So when you install this template with
one command and start playing around with this yourself locally you can really
start diving into it and be able to play around with this. And
I'm going to move back here. I'll have a QR code at
the end of the slides to get to that PR so you can see the code. So we did it, it turns out that the answer to
the equation by the way is 42, the meaning of life. And in
summary, at Grafana Labs, we've been diving into the potential of
AI and ML and more recently generative AI to transform
observability as we know it. And we invite you all to dive in with
us and we can't wait to see what magical and delightful experiences that you build.
So thank you all for your time today.

