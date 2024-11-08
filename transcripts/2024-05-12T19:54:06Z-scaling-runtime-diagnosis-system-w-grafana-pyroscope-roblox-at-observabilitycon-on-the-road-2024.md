# Scaling Runtime Diagnosis System w/ Grafana Pyroscope | Roblox at ObservabilityCON on the Road 2024

In this video, Xiaofeng and Jialin from Roblox introduce their journey in building a robust runtime diagnostic system using ...

Published on 2024-05-12T19:54:06Z

URL: https://www.youtube.com/watch?v=4gIEwndYbiQ

Transcript: Okay, cool. Thanks a lot Dimitri, for
introducing us. So before we get started, a few quick questions. So how many
of you have heard about Roblox? Maybe raise your hand. Wow.
Okay, cool. That's good. Maybe second question is how many of you
will feel pretty happy if you or your kids can hang out with friends, have fun without any
interruptions on Roblox? Okay, there we go. I see a few hands, right?
So reliability is very important. Cool. So my name is Xiaofeng. I'm from
Roblox. I'm an engineer director there, leading the observability team.
Together with me is my co-worker Jialin, he's a tech lead manager
leading the tracing part. So today we're going to share
some story about how do we build runtime diagnostic system. Cool. So
a little bit about Roblox, right? So we're kind of one of the
largest social and metaverse platform on this planet.
We have, as of end of 2023, we have over 70 million
daily activity users. Together, they contribute over 15.5 billion hours of engagement. That's a lot of hours. We also have a very big
creator community, right? So these are the people who
contribute to our platform. Together they contribute over 4.4 million
different experiences where people can hang out with each other. Cool. So behind that is actually
a pretty complex system. So Roblox still runs primarily on-prem. So it means like we have our major
data centers within the U.S. and we have our edge data
centers distributed globally. Together we have over 1,000 microservices
running on hundreds of thousands of machines, right? So as you can imagine, there's a lot of challenges on how
do we monitor debugging and keep the system up. So now I'm going to hand it over to
Jialin and he will talk about a very specific challenge we try to resolve. Thank you, Xiaofeng Yes. As we just heard from
Xiaofeng about Scout, it's the platform Roblox is running on. However, the way a Roblox engineer to debug production issue
isn't ready for that scale. Let's look at an example.
How we do profiling, one type of runtime diagnostic in the past. When a service is in
trouble, the engineer, they have to do the following
in the past. First, request production access permission,
which require human approval. And they log into one production instance, install the tool, run the tool, and download the data after
the profiling is done and visualize and analyze the data on
their local  server. Finally, the admin has to
revolkethe production access. This is not great, right?
Not scalable. Yeah, there were so many pain
points that is manual, inefficient and there are actually
security and privacy issues for people to log into the production server.
We want to improve this. We want to make it
delightful and an efficient experience for our engineer.
With those questions in mind, we looked for a solution. We went through thorough
process of investigation, evaluation ,and building
proof of concept experiments before we decided to
build in our end-to-end on demand profiling
workflow based on Pyroscope. We conducted comprehensive
performance evaluation on Pyroscope, measured
the performance impact, proven it to be very acceptable to us. Next, we still needed to make a big
decision whether we want to roll it out to continuous profiling directory
or we want to take it there step by step. Why we have this
decision to make - because actually, continuous profiling is a
relatively new concept to majority of our engineers and people are not very comfortable that it's running 24/7. Maybe they don't want to have any
performance issue when they're sleeping. Also reliability is our number
one priority. That's why the team, after you know, thorough consideration, we decided to take it step by step. We decided to build first, an on demand profiling
experience and then hoping to roll it out and let our user
to use it and define it very useful and also do not
cause them any trouble. Then they will feel more comfortable
and more passionate about profiling more, more and more. And then eventually
they want continuous profiling. That's our plan. And with that, we actually want to integrate it
into our end-to-end tool chain. As Dimitri mentioned, you know, Pyroscope has been built for continuous
profiling since the beginning. That's why we actually require quite
some in-depth technical support as well as even, like, new
API from the SDK. Fortunately, as I want to call out that we have a
great partner from the Grafana team that their technical support is
awesome and very helpful. We want to actually say thank you for
a few folks including like Dmitri, Ryan and Bill, as well as maybe many that are not
actually in this room right now. So thank you. Here is the high level architect
of our runtime diagnostic system. We focus on the profiling aspect. On the top center you can see
that we bake the profile into our container based image
and our service framework continuously monitoring our
runtime configuration service to listen to when we need
to provide what instances for how long or turn it off.
Once they get the signal, they actually call the
Pyroscope SDK to dynamically control the profiler and the
profiling data, of course, will upload into the Pyroscope cloud. When a user want to turn on
and off profiling on demand, they use a web-based UI. We build it internally to update
the runtime configuration. On the right hand side. Inside the dotted light box are
what we are planning to build next, which we call an event based profiling. When service critical
event happen such as new deployment, CPU ,and memory issue, etc, they will immediately trigger
automatically profiling. We are hoping that event-based profiling
will be a stepping stone for us to eventually reach the
continuous profiling. We built this and released it for
private review December last year. And now we already receive
overwhelmingly positive feedback from our engineers as well as many
successful story with true impact had been reported. Let's
look at some of them. First, there was a service that they are
doing performance optimization. By doing on-demand profiling, they was able to identify
many bottlenecks. One of them are actually caused
by JSON library they use, that is not performing. By just
replacing that with a better library, they were able to see more
than 36% CPU reduction. That was actually not just their service, they actually being generalized to
other service using the same old library. Second example, a success story is one
of our top services that are doing profiling. To identify performance
bottleneck as well. They actually find out
one of the bottlenecks, and then they replace the expensive regular expression matching
with just a simple dictionary lookup. And that single change, bring them more than 40% of CPU reduction. Last example is a new service.
Before they go to production, they are doing optimization and
hardening. They again, use profiling, on demand profiling, to find out the root cause and
they were able to fix it and see a 10x throughput improvement.
That's all I have. And back to Xiaofeng. Okay, great. Thank you Jialin for walking us through
the journey of adopting Pyroscope. As you know, right, so traditionally logs, metrics and the trace are considered
like the three pillar of observability. And within Roblox we're very happy, like be able to work with Grafana Labs
and build a first pillar of runtime diagnose system so we can look into the
process deeply enough whenever needed. So this is great. Together we try to leverage all the data
we have then continue to improve the reliability, productivity, and efficiency of Roblox's system
and hopefully provide continuous, uninterrupted, no downtime for
our clients. Okay. that's it. So Jialinand I will be
hanging around here. If you have some ideas or similar visions,
feel free to chat with us. Thank you. Thank you.

