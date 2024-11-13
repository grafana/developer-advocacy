# How to Create AI-Powered Dashboard Titles &amp; Descriptions with the LLM Plugin (Grafana 11)  | Grafana

With Grafana's LLM app plugin, you can now use AI to generate titles and descriptions for your dashboards that are *actually* ...

Published on 2024-04-09T12:11:30Z

URL: https://www.youtube.com/watch?v=s61WHREHuYE

Transcript: Hi, let's talk about generative AI features
in dashboards now generally available for cloud users and in Grafana
11 for on-prem users. I'm Thanos. I'm a product manager here at Grafana
Labs and working with the dashboards team/ Working in large teams where
big dashboards are shared with many external or internal users. Having meaningful panel titles and
descriptions are crucial for efficient communication and knowledge sharing. But usually these are activities that
are not fun and take time and effort, especially if you think
about the complexity of the
queries and the number of panels inside the dashboard.
For the past few months, we've been looking into meaningful ways
to help you perform these tasks at scale in order to help you focus
on what matters the most. Let me show you what we have developed
to address this. So in this example, I'm working on a dashboard querying a
Prometheus data source for data coming from CI/CD experimental project. Let's look into some of these panels
and give them titles and descriptions. I have already used this
feature to provide the title
and description for these two panels, and let's do the
same for the rest of them. So I can look at this metric here. It's a total CI calls given
those labels querying a Prometheus data source. So now I want
to give it a title and description. Now that the GenAI feature is enabled, you can see that I have an "Auto-generate"
CTA in the corresponding text fields. So I'm gonna click it to
get a title from my panel. So I have my "Total CI Calls for the
Main Lint Frontend" that represents the ci_drone_stage_name. I think
that's a very good title. So I wanna have a description now. Reading through the description, I see this is a really good
representation of my query here, so I like it. If I want
to improve it though, I can click here and I have these
options that I can make it even shorter, more descriptive or regenerate. I
think it's pretty good as it is. So I'm gonna click apply. So let's do the same for the other panel. So you can see in just some seconds. I get a very good description
of the panel as well, a very good explanation
of what this metric does. I think it helps me a lot considering
the number of panels that I want to add, as well as the fact that I want to share
this dashboard to various users that will need to understand
in detail what they see. So let's save this dashboard now. Now to try this feature, which is
generally available in Grafana Cloud, you need to enable and configure
Grafana's LLM app plugin. You can find how to enable the LLM app
plugin under the administration section in the main menu, and you can
go into the App plugin section. I'm gonna search for it, and here it is. The GenAI features are disabled
by default. To enable them, you can use a connection to OpenAI that
is provided by Grafana or through your personal OpenAI account here. This is our first step towards helping
you communicate your dashboards insight efficiently, and we're looking into how we can
expand this functionality covering your scaling needs. Our dashboards team are looking forward
to your feedback and ways you think generative AI features in the taskforce
context will provide the most value to you. Thank you.

