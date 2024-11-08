# Annotating Events with Grafana | Grafana for Beginners Ep. 10

As we observe our system, we are bound to come across some interesting events or failures. By flagging these events and adding ...

Published on 2024-03-19T20:45:14Z

URL: https://www.youtube.com/watch?v=N5iOlyYyK6Q

Transcript: Hey! Welcome to Grafana for Beginners. I'm Lisa 
Jung and I'm a developer Advocate at Grafana. In   the last episode, we created a visualization 
dashboard to observe our e-commerce app. As   we observe our system, we're bound to come 
across some interesting events or failures.   By flagging these events and adding context, we 
can communicate whether further investigation   is needed or if action should be taken to address 
these events. This is known as annotating events.   Think of this as adding a little Post-It note to 
an interesting event for your team. It's there to   flag an event with just enough context to decide 
on the next steps. You can add these annotations   manually or automatically. You're most likely 
to manually add annotations for specific events   that you don't normally encounter. For regularly 
occurring events, automatic annotations are used.   In this episode, we'll cover how to manually add 
annotations. I'll add the tutorial to automatic   annotations towards the end of the video. So 
this dashboard observes the same e-commerce   app we've been using as an example. It's more 
comprehensive and advanced than the dashboard   we built in the last episode and it's divided 
into three sections. The Application Metrics   give an overview of the traffic that each service 
is dealing with. The Application Logs display info   about errors observed in these services. The 
Kubernetes Metrics visualize info about the   infrastructure that the app is running in. At 
first glance, these four panels may stand out   to you as something that may need to be annotated. 
Let's zoom in on the Application Metrics section.   You see a spike in service latency, which suggests 
that these services are taking longer to complete   the tasks. You also see a dip in the service 
throughput, which suggests that the services   are handling fewer requests per second. If 
you look at the Kubernetes metrics, something   may be going on with the container memory and 
container CPU for the product service. Whatever   may be going on seems to make this service work 
harder to fulfill the request. As a result,   the service may take longer to complete the 
task and handle fewer requests per second. Now,   these are just initial assumptions and we have no 
idea if it's true. But we want to flag these so we   can decide what we want to do next. To manually 
add an annotation, click on wherever you want to   add it. Once the popup menu appears, click on the 
Add annotation option. In the description is where   you would add the context and or a call to action 
here. What you write here depends on the situation   you're dealing with. If you want a team member 
to investigate this further, you would add a note   here asking them to do so. Or let's say 2 minutes 
after deployment, you observe a huge spike in   service latency. You would annotate that something 
went wrong during deployment and ask to roll this   back. Or it might be a scenario where somebody 
accidentally reconfigured the service, which led   to this huge spike in service latency. You caught 
it, rolled it right back, and everything is good   but you still may want to annotate that here so 
that if another teammate were to come across this,   they have the context to what happened. Once 
you're done filling out the description,   click on the Save button. You'll see a little 
arrow added here signifying that an annotation   has been added. If you hover your mouse over the 
arrow, the text of the annotation will appear.   You may want to annotate a certain region of your 
visualization. If you want to do this using a PC,   press control and hold. Then click and drag 
across a region you want to highlight. Then   the box should appear where you can add and save 
the description. If you're using a Mac, you would   press and hold the command key and follow the 
exact same steps. At the moment, there's no way to   tag somebody within the annotation. So if you want 
somebody to take a look at what you annotated,   you would share the URL of the dashboard using 
whatever messaging platform you use. All right. We   just went over how to manually add annotations to 
your dashboard. If you want to automatically add   annotations, you can do so by writing annotation 
queries. My teammate Marie created a fantastic   tutorial on it so if you're if you're interested, 
click on the info card up top to watch the video.   As beautiful as these dashboards are, you probably 
don't want to monitor them 24/7. With Grafana, you   can set up alerts for certain events that require 
your attention. In the next episode, we'll learn   how to create alerts with Grafana. If you want to 
access more episodes of the Grafana for Beginners   series, go to the Grafana community web page. This 
is where all the community resources are shared.   You can access the series by clicking on the 
Grafana for Beginners card. Last but not least,   as you continue your journey with Grafana, you may 
need something beyond what's currently available   within Grafana. If you would like resources 
on creating plugins or whatever else to extend   Grafana capabilities, the Developer Portal is a 
great place to start. This is where you can find   documentation specific to app development. You 
can also find plugin tools and guides to help   you get started. Make sure to check that out if 
you need something beyond what's available within   Grafana. All right, that's a wrap. Thank you for 
watching and I'll see you in the next episode.

