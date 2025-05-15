# AI-Powered Observability: Grafana Assistant Builds Dashboards &amp; Diagnoses Issues | Demo | Grafana 12

Grafana Assistant isn't just chat—it's an intelligent agent that can build dashboards, explore metrics, fix broken panels, and ...

Published on 2025-05-07T10:00:20Z

URL: https://www.youtube.com/watch?v=ETZnD483mHI

Transcript: Grafana Assistant is an
integrated LLM agent. So you can open it at the top right
corner. It opens as a sidebar, so it's everywhere within
Grafana with you, next to you. And it has a lot of context about where
you are on the page and what action can you take. What we did is also load it with
Grafana-specific best practices. How many nodes do we
have in this Kubernetes cluster? So the assistant has a lot of tools that
it can use to answer the question and is going to use those tools. And
it has a workflow to find data. So find metrics and then
query those metrics. We can expand those tool call to
see the result and what is the input parameters that it did. We want to make sure that we are very
clear about what the agent's thinking, what information it's using to
make decisions and statements. So we show the working throughout. And I can keep going asking more question
about this and the context is still there. Going beyond AI chat, when you
grant access to your specific data, it can answer questions
from your observability data
and if they're multi-step agents, they can query
something, have a look at it, reason about it and either ignore it, move on to something else or
decide to drill in from there. I'm going to ask another question to
show you that it can navigate you around. So, "Can you show me the CPU matrix of parts in Explore?" So I
haven't talked about this, but every time I'm talking about metrics,
I automatically select the Prometheus data source, but this one is also suggested if
I want to add logs into my inquiry. But there's other context tools that
you can add like datasource if you want to avoid searching for datasources,
labels, dashboards, metrics, there's a ton of them. And that's it. We are at the Explore page and from there
I can keep asking questions and refine my query, create another queries. So it's
always there to help me write queries. You can run these investigations and with
this tightly integrated into Grafana, you get a great experience and
it's a real productivity boost. This time I'm going to select both logs
and Prometheus and I'm going to ask, "What is going on with the product catalog service? It's struggling." So I know there's
something going on and I'm sending the agent of an investigation to figure
it out for me, whatever I can. And I want to also show you that all the
conversations are automatically titled for you and in fact they are saved so
you can go back to them and even more they're running in the background. So if I go to that
conversation which was about how to monitor Kubernetes
in Grafana Cloud. And so it used the documentation website
to find the information and it gave me a detailed information on
the steps on how to do that. The other conversation is
still ongoing. So I asked, "What is our service
architecture?" Very blank query. And it went and tried to
find the other metrics, all the services that I have.
So it told me, you are running in three regions
and this is your front end layer, this is your core services. And
what those services are for? Let's go back to the
investigation. So yeah, it's going deep showing me the
product catalog request rate, showing me the errors, looking at the latency and it made a
mistake here and mistakes are fine. If it does make a query mistake, the mistake is sent back to the LLM
and you can adjust, which it did. And it was able to basically
get logs from the services, which you find errors by the
way. So it's still ongoing. And then if you're not on
your computer right now, the investigation is paused at some point
so it doesn't run infinitely and I can keep it going right now. So
this is what I'm going to do. "Do we have Postgres dashboard?" And it is going to navigate us to
this new dashboard. Unfortunately that dashboard is a problem.
One panel is not working. So what we're going to do
is ask to fix the panel. "One panel shows no data. The database size. Fix it and change all panel
color to gradient purple in bulk." Right. So let's see if it's able to actually
fix that panel and also change all the colors. In the meantime, let's
go back to my investigation. And it basically finished, navigated me to Explore with a couple of
queries that are interesting to look at and gave me the root cause saying
something is wrong with Postgres, like a limit of connection
is being reached. Talks about the key finding and
gave me a set of recommended action. So this was just one investigation, but
I can fire up many at once. Alright, so it even knows about what's going
on with this panel is preparing queries. Let's see if it
can fix it. There we go. Panel fixed, this is it. "Create a dashboard for monitoring Kafka with five panels.
Pick the most important metrics." You can
interrupt the conversation, start adding more data and
resume the conversation. You can see your token usage here
as the conversation keeps going. So you know when the
conversation becomes too big. So it is preparing the queries,
preparing the output. Let's see, what is it going to come up with? All right, that's it. We have a
Kafka dashboard, pretty insightful. Just want to emphasize on the fact
that look at the units, they are older. Look at the different
visualizations that it used, like a gauge for the memory,
the description, the title, the crafted queries, the placement of
the panel. If you think about that, this is usually tedious work,
like takes a lot of time. I just did this in very few minutes. So they have it, Grafana Assistant. You can just ask general observability
questions or ones specific about your tech stack. And you can do
this at all levels. CTOs, CEOs can query it in the same
way that a junior SRE or a seasoned SRE can. You
want to go places too? "Show me in Logs Drilldown
this particular set of logs, automatically filtered." "Show me the
same in metrics and profiles." The agents can also investigate, they can dig into particular
issues prompted by you and
guided by you the whole way. And of course you
can make those changes, fix those annoying little bugs that you've
been putting off because it's just a bit of a pain to go and fix it. Or you can build new dashboards much
more quickly or edit them and evolve them much more rapidly. So we're very excited about this project
and we've got a very exciting future we think for this too. And
thanks for listening.

