# Adaptive Logs Demo | Now Generally Available | Grafana

In this video, Travis Patterson, Senior Software Engineer at Grafana Labs, demonstrates how easy it is to manage log spending ...

Published on 2024-09-24T13:05:52Z

URL: https://www.youtube.com/watch?v=ltkqkbY6Jao

Transcript: Hello, I'm Travis Patterson, a senior
software engineer here at Grafana Labs. We've heard the frustration from teams
who use logs to run their systems but are getting buried in noise and ever
increasing observability costs. We're proud to introduce our
solution to this Adaptive Logs. Adaptive logs helps teams optimize
costs by intelligently adapting to their observability needs. Adaptive logs uses advanced algorithms
to identify redundant and unnecessary log data, allowing teams to optimize
ingestion and save significantly. Teams can easily manage adaptive logs
recommendations in Grafana Cloud in cv, immediate impact, ensuring they only pay for data that's
valuable and speeds up troubleshooting adaptive logs intelligently groups, and prioritizes log data based
on queried and ingested logs, making reduction as simple click away
without any kind of manual work required. And so now that we sort of understand
the basics of adaptive logs and how it changes based on your needs,
let's see it in action. I'll guide you through a quick demo to
show you how easy it is to manage log spending. You'll be able to find adaptive logs
under the hamburger menu in the upper left hand corner under cost
management logs. From here, there's a blue button that takes
you to the adaptive log screen. It'll take a moment for your
recommendations to load, but afterwards, this is what you'll see. These are the recommendations provided
to you about your log data from Adaptive Logs. The first most important thing to see
here is the pattern in this column here. Log patterns are basically just all
of the bits of logs that don't change, and this is what Adaptive Logs uses to
count your ingested logs and your query logs. We can also see this
query to ingest ratio here, which tells you how much of this logs or
this log pattern you're actually using. And then importantly, we've got
our suggested drop right here. This is sort of the core of the Adaptive
Logs recommendation that tells you how many of these logs that
you can actually drop. So now that we sort of understand
what we're looking at here, let's actually go through dropping
some logs. First things first, there can be a lot of recommendations
for your logs depending on the size of your system. So Adaptive Logs allows
you to see where they're coming from. So if we want to then narrow
these down, for example, I want to see only log
recommendations that come from Loki. All I have to do is type that
up here in the service filter, and this gives me all of
the logs for a service. But if I actually only wanna
look for really specific logs, I can do that too with
a fuzzy search here. So if I wanna find this log line
that's got all these Ps in it, it's really quick to do so. So if you
know kind of a part of a log line, it's really easy to find and narrow down
what you wanna apply a recommendation to. Then when we're actually
applying recommendations, sort of the core piece to know is this
maximum drop rate and this set button. Basically what this is doing is
telling adaptive logs to apply the recommendations that it's provided you
at different levels of aggressiveness. If we set it to 100% and say set, what it's gonna do is just
accept all of the law, uh, recommendations as they've been
given. But if, for example, you wanna be a little less
aggressive, you can turn this down. So if we set this to, for
example, 50 and click set, then what you'll see here is that anything
that adaptive logs is recommended at 50% or below as a drop
rate, it's gonna keep. But for those more
aggressive recommendations, it's gonna dial those down and cap
them at whatever this drop rate is. So let's see. You know, we wanna know what the impact of
these recommendations are gonna be. We can use the preview button and
we see at this 50% aggressiveness, we can save about 160 terabytes
and that's over the last 15 days. But I'm really confident
in these recommendations
and so I'm gonna dial these all the way up and
click set and see, okay, great. We can actually save about 260
terabytes and this is much better. Now we know that there's always some logs
that you have to keep either for sort of compliance or security
reasons or anything like that. And Adaptive Logs gives you
a couple of ways to do this. The first way is just sort of
on a per recommendation basis. We've got this little lock here and what
that will do is pin the drop rate at whatever you set it at
here. So for example, we've got some audit logs here and we need these four
various compliance reasons. So you can see I've locked all of these
and they're always gonna be pinned to zero regardless of whatever
future recommendations are. And if you want to sort of exclude logs
from being recommended more broadly, adaptive Logs also supports a label
based filter where you can really broadly define whole sets of logs that you
never want to see in adaptive logs. Once you've dialed in your recommendations
and you set everything and you're happy with your drop rate, you
can then say apply drop rate. It's going to give you a warning to let
you know that you are in fact gonna be, you know, dropping some
data. And we can click this. It'll take a moment to
propagate to the backend. And once this has been done in just a few
minutes, Loki is gonna start dropping, uh, some of your logs based on these,
and you'll see your ingest go down. To summarize. With adaptive logs,
teams can painlessly reduce log data, optimize ingestion and storage, and save costs while ensuring
critical logs are never lost. All with a simple click and no
manual effort. New to cloud, try our free forever plan that makes it
easy to explore adaptive logs and start saving. Try it out in your Cost Management
hub or sign up for GR Cloud today.

